#!/usr/bin/env python3
"""Diff Anthropic's directory feed (the in-app catalog) against data/connectors.json.

Usage:
    python3 scripts/feed_diff.py                          # markdown report to stdout
    python3 scripts/feed_diff.py --out report.md          # capped report (issue-sized)
    python3 scripts/feed_diff.py --full-out full.md       # uncapped report
    python3 scripts/feed_diff.py --snapshot               # also write docs/catalog-snapshots/directory-feed-<today>/
    python3 scripts/feed_diff.py --roster docs/catalog-snapshots/in-app-2026-08-10/roster.txt
                                                          # coverage check: paste-export names missing from the feed
    python3 scripts/feed_diff.py --feed feed.json --sitemap sitemap.xml
                                                          # offline inputs (re-runs, tests)

This is a LOOK, not an UPDATE. It reports what changed upstream; a person (or a
sweep session) applies the changes under CONTRIBUTING.md: adds need a verified
vendor URL, a description, a use case and a category; removals need the
two-surface test. Stdlib only. Exit 0 on a completed report, 2 on a fetch error.

The two surfaces:
  feed     https://api.anthropic.com/api/directory/servers  (in-app catalog, all tiers)
  sitemap  https://claude.com/sitemap.xml -> /connectors/<slug>  (curated web directory)
"""

import argparse
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "connectors.json"
SNAPSHOTS = REPO / "docs" / "catalog-snapshots"

FEED_URL = (
    "https://api.anthropic.com/api/directory/servers"
    "?limit=5000&visibility=commercial,gsuite,gsuite-google"
    "&verified_tier=anthropic,partner,community"
)
SITEMAP_URL = "https://claude.com/sitemap.xml"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "Chrome/126.0 Safari/537.36 awesome-claude-connectors/feed_diff"
)

# verified_tier -> the marker data/connectors.json stores for it
TIER_MARKER = {"community": "C", "anthropic": "A", "partner": None}

# Tokens that vary between a catalog name and a list name without meaning a
# different product ("GitHub MCP" vs "GitHub", "Foo AI" vs "Foo").
NOISE_TOKENS = {
    "mcp",
    "server",
    "connector",
    "ai",
    "app",
    "io",
    "com",
    "the",
    "by",
    "for",
    "beta",
    "and",
}

LOCALE_PREFIX = re.compile(r"claude\.com/[a-z]{2}(-[A-Za-z]+)?/connectors/")
SITEMAP_LOC = re.compile(
    r"<loc>(https://claude\.com/(?:[a-z]{2}(?:-[A-Za-z]+)?/)?connectors/([^<]+))</loc>"
)
APOSTROPHES = re.compile(r"[’'`]")

# GitHub's issue body limit is 65,536 bytes; 100 rows per table keeps a full report well under it.
DEFAULT_MAX_ROWS = 100


# ---------------------------------------------------------------- fetching


def fetch(url, timeout=60):
    req = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def load_feed(path=None):
    raw = Path(path).read_text(encoding="utf-8") if path else fetch(FEED_URL)
    data = json.loads(raw)
    servers = data.get("servers") if isinstance(data, dict) else data
    if not isinstance(servers, list) or not servers:
        raise ValueError("feed has no 'servers' list")
    meta = {
        "total": data.get("total") if isinstance(data, dict) else None,
        "next_cursor": data.get("next_cursor") if isinstance(data, dict) else None,
        "stale_feeds": data.get("stale_feeds") if isinstance(data, dict) else None,
    }
    return servers, meta


def load_sitemap_slugs(path=None):
    raw = Path(path).read_text(encoding="utf-8") if path else fetch(SITEMAP_URL)
    slugs = set()
    for full, slug in SITEMAP_LOC.findall(raw):
        if LOCALE_PREFIX.search(full):
            continue
        slugs.add(slug.strip("/"))
    return slugs


# ---------------------------------------------------------------- matching


def clean(value):
    return " ".join(str(value or "").split())


def _tokenize(text):
    text = APOSTROPHES.sub("", clean(text).lower())
    tokens = [t for t in re.sub(r"[^a-z0-9]+", " ", text).split() if t]
    if tokens:
        return tokens
    # A name with no ASCII letters or digits (CJK, Cyrillic, ...) used to tokenize to
    # nothing and never match itself: a false add AND a false removal every run.
    whole = re.sub(r"\s+", "", text)
    return [whole] if whole else []


def token_variants(name):
    """Token lists for a name: '&' read as 'and' and as nothing ('S&P' -> 's and p' / 'sp')."""
    base = clean(name)
    variants = [_tokenize(base.replace("&", " and "))]
    if "&" in base:
        variants.append(_tokenize(base.replace("&", "")))
    return variants


def keys(name):
    return {"-".join(v) for v in token_variants(name) if v}


def loose_keys(name):
    out = set()
    for v in token_variants(name):
        kept = [t for t in v if t not in NOISE_TOKENS]
        out.add("-".join(kept) if kept else "-".join(v))
    return {k for k in out if k}


def content_tokens(name):
    out = set()
    for v in token_variants(name):
        out.update(t for t in v if t not in NOISE_TOKENS)
    return out


def domain(url):
    try:
        host = urlsplit(clean(url)).netloc.lower()
    except ValueError:
        return ""
    return host[4:] if host.startswith("www.") else host


def author_url(server):
    author = server.get("author") or {}
    return clean(author.get("url"))


def match_feed_to_list(servers, listed):
    """Return {feed_index: (list_index, how)} plus the unmatched feed indices.

    how ∈ exact | loose | domain. Domain matches require a unique list entry on
    that domain — shared vendor domains (one company, several connectors) never
    match by domain alone.
    """
    by_key = defaultdict(list)
    by_loose = defaultdict(list)
    by_domain = defaultdict(list)
    for i, entry in enumerate(listed):
        for k in keys(entry["name"]):
            by_key[k].append(i)
        for k in loose_keys(entry["name"]):
            by_loose[k].append(i)
        if entry.get("url"):
            by_domain[domain(entry["url"])].append(i)

    matched, unmatched = {}, []
    for j, server in enumerate(servers):
        name = clean(server.get("name"))
        hit = None
        exact = [i for k in keys(name) for i in by_key.get(k, [])]
        if exact:
            hit = (exact[0], "exact")
        else:
            loose = sorted({i for k in loose_keys(name) for i in by_loose.get(k, [])})
            if len(loose) == 1:
                hit = (loose[0], "loose")
            else:
                dom = domain(author_url(server))
                if dom and len(by_domain.get(dom, [])) == 1:
                    hit = (by_domain[dom][0], "domain")
        if hit:
            matched[j] = hit
        else:
            unmatched.append(j)
    return matched, unmatched


def on_web(name, slugs, slug_keys, slug_loose):
    """A list name is on the web directory if a slug matches it exactly, loosely, or by
    token containment (slug 'devrev' ⊂ 'Computer by DevRev', 'cortellis-regulatory' ⊂
    'Cortellis Regulatory Intelligence') — the drift cases CONTRIBUTING warns about."""
    if keys(name) & slug_keys or loose_keys(name) & slug_loose:
        return True
    name_tokens = content_tokens(name)
    for slug in slugs:
        st = content_tokens(slug)
        if st and st <= name_tokens:
            return True
    return False


# ---------------------------------------------------------------- report


def md_cell(text, limit=None):
    text = clean(text).replace("|", "\\|")
    if limit and len(text) > limit:
        text = text[: limit - 1] + "…"
    return text


def table(header, rows, cap):
    if not rows:
        return ["_none_", ""]
    out = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    shown = rows if cap == 0 else rows[:cap]
    out += ["| " + " | ".join(r) + " |" for r in shown]
    if cap and len(rows) > cap:
        out.append("")
        out.append(
            f"_… {len(rows) - cap} more rows — the full report is the workflow artifact, or run "
            "`python3 scripts/feed_diff.py --full-out full.md` locally._"
        )
    out.append("")
    return out


def build_report(servers, meta, slugs, data, cap, roster_names=None, today=None):
    today = today or dt.date.today().isoformat()
    listed = data["connectors"]
    held = data.get("held", [])
    matched, unmatched = match_feed_to_list(servers, listed)
    matched_list_idx = {li for li, _ in matched.values()}

    tiers = Counter(clean(s.get("verified_tier")) or "?" for s in servers)
    lines = [
        f"# Directory feed diff — {today}",
        "",
        "Report only: nothing here has been applied. Adds need a verified vendor URL, description, use case and "
        "category; removals need the two-surface test (CONTRIBUTING.md).",
        "",
        "## Summary",
        "",
        f"- Feed: **{len(servers)}** servers (total={meta.get('total')}, next_cursor={meta.get('next_cursor')}, "
        f"stale_feeds={meta.get('stale_feeds')}); by tier: "
        + ", ".join(f"{k} {v}" for k, v in sorted(tiers.items())),
        f"- Web sitemap: **{len(slugs)}** connector slugs",
        f"- List: **{len(listed)}** listed + **{len(held)}** held",
        f"- Feed entries matched to listed entries: **{len(matched)}** "
        f"(exact {sum(1 for _, h in matched.values() if h == 'exact')}, "
        f"loose {sum(1 for _, h in matched.values() if h == 'loose')}, "
        f"domain {sum(1 for _, h in matched.values() if h == 'domain')})",
        "",
    ]

    # 1. New in feed / 2. held entries present in the feed
    held_keys = set().union(*(keys(h["name"]) for h in held)) if held else set()
    new_rows, held_hits = [], []
    for j in unmatched:
        s = servers[j]
        row = (
            md_cell(s.get("name"), 60),
            md_cell(s.get("verified_tier")),
            md_cell(s.get("type")),
            md_cell((s.get("added_at") or "")[:10]),
            md_cell(author_url(s), 70),
            md_cell(s.get("one_liner"), 100),
        )
        if keys(s.get("name")) & held_keys:
            held_hits.append(row)
        else:
            new_rows.append(row)
    new_rows.sort(key=lambda r: (r[3] or "0000", r[0].casefold()), reverse=True)
    lines += [
        f"## 1. In the feed, not on the list — {len(new_rows)} candidate adds",
        "",
    ]
    lines += table(
        ("name", "tier", "type", "added", "author url", "one-liner"), new_rows, cap
    )

    held_hits.sort(key=lambda r: r[0].casefold())
    lines += [
        f"## 2. Held entries present in the feed — {len(held_hits)} graduation candidates",
        "",
    ]
    lines += [
        "Check the author URL's content matches the connector, then move the row from `held` to `connectors`.",
        "",
    ]
    lines += table(
        ("name", "tier", "type", "added", "author url", "one-liner"), held_hits, cap
    )

    # 3. Listed but absent from both surfaces / 4. web-only
    slug_keys = set().union(*(keys(s) for s in slugs)) if slugs else set()
    slug_loose = set().union(*(loose_keys(s) for s in slugs)) if slugs else set()
    gone, web_only = [], []
    for i, entry in enumerate(listed):
        if i in matched_list_idx:
            continue
        row = (
            md_cell(entry["name"], 60),
            md_cell(entry.get("category")),
            md_cell(entry.get("url"), 70),
        )
        (
            web_only if on_web(entry["name"], slugs, slug_keys, slug_loose) else gone
        ).append(row)
    gone.sort(key=lambda r: r[0].casefold())
    web_only.sort(key=lambda r: r[0].casefold())
    lines += [
        f"## 3. Listed, absent from the feed AND the sitemap — {len(gone)} removal candidates",
        "",
    ]
    lines += [
        "Two-surface rule applies. Same-vendor variants the feed lists once (e.g. one Windsor.ai entry) land here "
        "as a set; naming drift with a different domain can too — search the feed for the vendor domain before removing. "
        "The feed's visibility filter is known to omit some partner entries (see section 9), so a web-only entry is "
        "never a removal.",
        "",
    ]
    lines += table(("name", "category", "listed url"), gone, cap)
    lines += [
        f"## 4. Listed, absent from the feed but on the sitemap — {len(web_only)} web-only entries",
        "",
    ]
    lines += table(("name", "category", "listed url"), web_only, cap)

    # 5. Vendor URL mismatch / 6. marker mismatch / 7. fuzzy matches
    url_rows, marker_rows, fuzzy_rows = [], [], []
    for j, (i, how) in sorted(
        matched.items(), key=lambda kv: clean(servers[kv[0]].get("name")).casefold()
    ):
        s, entry = servers[j], listed[i]
        feed_dom, list_dom = domain(author_url(s)), domain(entry.get("url"))
        if (
            feed_dom
            and list_dom
            and feed_dom != list_dom
            and not feed_dom.endswith("." + list_dom)
            and not list_dom.endswith("." + feed_dom)
        ):
            url_rows.append(
                (
                    md_cell(entry["name"], 60),
                    md_cell(entry.get("url"), 70),
                    md_cell(author_url(s), 70),
                )
            )
        tier = clean(s.get("verified_tier"))
        if tier in TIER_MARKER and entry.get("marker") != TIER_MARKER[tier]:
            marker_rows.append(
                (
                    md_cell(entry["name"], 60),
                    md_cell(tier),
                    md_cell(entry.get("marker") or "null"),
                    md_cell(TIER_MARKER[tier] or "null"),
                )
            )
        if how != "exact":
            fuzzy_rows.append(
                (md_cell(s.get("name"), 60), md_cell(entry["name"], 60), how)
            )
    lines += [
        f"## 5. Vendor URL differs from the feed's author URL — {len(url_rows)}",
        "",
    ]
    lines += [
        "Usually a wrong domain on our side or a vendor move; content-check the feed URL before switching.",
        "",
    ]
    lines += table(("name", "listed url", "feed author url"), url_rows, cap)
    lines += [f"## 6. Marker disagrees with the feed tier — {len(marker_rows)}", ""]
    lines += [
        "community → `C`, anthropic → `A`, partner → null. Markers were synced to the feed tier on 2026-09-14 for exact-name matches; loose and domain matches are left for review.",
        "",
    ]
    lines += table(("name", "feed tier", "listed marker", "expected"), marker_rows, cap)
    lines += [f"## 7. Non-exact name matches (review) — {len(fuzzy_rows)}", ""]
    lines += table(("feed name", "list name", "how"), fuzzy_rows, cap)

    # 8. Sitemap slugs unmatched by any name
    all_names = [e["name"] for e in listed] + [h["name"] for h in held]
    all_tokens = [content_tokens(n) for n in all_names]
    all_keys = set().union(*(keys(n) for n in all_names))
    all_loose = set().union(*(loose_keys(n) for n in all_names))
    orphan_slugs = sorted(
        s
        for s in slugs
        if not (keys(s) & all_keys or loose_keys(s) & all_loose)
        and not any(content_tokens(s) and content_tokens(s) <= t for t in all_tokens)
    )
    lines += [
        f"## 8. Sitemap slugs matching no list name — {len(orphan_slugs)} (web-only candidate adds or naming drift)",
        "",
    ]
    lines += ["`" + "` `".join(orphan_slugs) + "`" if orphan_slugs else "_none_", ""]

    # 9. Coverage check against a paste export
    if roster_names is not None:
        feed_keys = set().union(*(keys(s.get("name")) for s in servers))
        feed_loose = set().union(*(loose_keys(s.get("name")) for s in servers))
        missing = sorted(
            n
            for n in roster_names
            if not (keys(n) & feed_keys or loose_keys(n) & feed_loose)
        )
        lines += [
            f"## 9. Coverage check — {len(missing)} of {len(roster_names)} paste-export names absent from the feed",
            "",
            "Names the app showed that the feed's visibility filter does not return (or that were delisted since the "
            "export). Anything here that is still on the sitemap proves the filter is narrower than the app view.",
            "",
        ]
        lines += table(("export name",), [(md_cell(n, 80),) for n in missing], cap)

    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------- snapshot

TSV_COLUMNS = (
    "name",
    "verified_tier",
    "type",
    "visibility",
    "added_at",
    "author_name",
    "author_url",
    "slug",
    "directory_url",
    "documentation",
    "one_liner",
)


def write_snapshot(servers, meta, today):
    out_dir = SNAPSHOTS / f"directory-feed-{today}"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for s in servers:
        a = s.get("author") or {}
        rows.append(
            [
                clean(s.get("name")),
                clean(s.get("verified_tier")),
                clean(s.get("type")),
                ",".join(s.get("visibility") or []),
                clean(s.get("added_at"))[:10],
                clean(a.get("name")),
                clean(a.get("url")),
                clean(s.get("slug")),
                clean(s.get("directory_url")),
                clean(s.get("documentation")),
                clean(s.get("one_liner")),
            ]
        )
    rows.sort(key=lambda r: r[0].casefold())
    with (out_dir / "servers.tsv").open("w", encoding="utf-8") as f:
        f.write("\t".join(TSV_COLUMNS) + "\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    tiers = Counter(clean(s.get("verified_tier")) for s in servers)
    types = Counter(clean(s.get("type")) for s in servers)
    (out_dir / "README.md").write_text(
        f"# Anthropic directory feed — capture {today}\n\n"
        f"Captured by `python3 scripts/feed_diff.py --snapshot` from:\n\n```\nGET {FEED_URL}\n```\n\n"
        f"`total` = {meta.get('total')}, `next_cursor` = {meta.get('next_cursor')}, `stale_feeds` = {meta.get('stale_feeds')}.\n"
        f"Servers: {len(servers)} — by tier {dict(sorted(tiers.items()))}; by type {dict(sorted(types.items()))}.\n\n"
        "`servers.tsv` is one row per server: name, tier, type, visibility, added_at (date), author name/URL, slug, "
        "directory URL, documentation URL, one-liner. The raw JSON (~6 MB) is not committed; re-run the script to regenerate.\n\n"
        "This feed is the in-app surface for the two-surface test (CONTRIBUTING.md): an entry absent here AND absent "
        "from the claude.com/connectors sitemap is a removal candidate.\n",
        encoding="utf-8",
    )
    return out_dir


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--feed", help="local feed JSON instead of fetching")
    ap.add_argument("--sitemap", help="local sitemap XML instead of fetching")
    ap.add_argument("--out", help="write the capped report here")
    ap.add_argument("--full-out", help="write the uncapped report here")
    ap.add_argument(
        "--max-rows",
        type=int,
        default=DEFAULT_MAX_ROWS,
        help=f"rows per table in the capped report (0 = unlimited; default {DEFAULT_MAX_ROWS})",
    )
    ap.add_argument(
        "--snapshot",
        action="store_true",
        help="write docs/catalog-snapshots/directory-feed-<today>/",
    )
    ap.add_argument(
        "--roster",
        help="paste-export roster (one name per line) for the coverage check",
    )
    ap.add_argument("--today", help="override the report date (YYYY-MM-DD)")
    args = ap.parse_args()

    today = args.today or dt.date.today().isoformat()
    try:
        servers, meta = load_feed(args.feed)
        slugs = load_sitemap_slugs(args.sitemap)
    except (
        urllib.error.URLError,
        TimeoutError,
        ValueError,
        json.JSONDecodeError,
    ) as exc:
        print(f"feed_diff: fetch failed: {exc}", file=sys.stderr)
        return 2

    data = json.loads(DATA.read_text(encoding="utf-8"))
    roster = None
    if args.roster:
        roster = [
            clean(line)
            for line in Path(args.roster).read_text(encoding="utf-8").splitlines()
            if clean(line)
        ]

    capped = build_report(servers, meta, slugs, data, args.max_rows, roster, today)
    if args.out:
        Path(args.out).write_text(capped, encoding="utf-8")
    if args.full_out:
        Path(args.full_out).write_text(
            build_report(servers, meta, slugs, data, 0, roster, today), encoding="utf-8"
        )
    if not args.out and not args.full_out:
        sys.stdout.write(capped)
    if args.snapshot:
        print(
            f"snapshot written: {write_snapshot(servers, meta, today).relative_to(REPO)}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
