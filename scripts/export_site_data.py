#!/usr/bin/env python3
"""data/connectors.json -> site-data/, the website's read-only feed.

Usage:
    python3 scripts/export_site_data.py           # write site-data/, record new changes
    python3 scripts/export_site_data.py --check   # CI: fail if site-data/ is stale
    python3 scripts/export_site_data.py --selftest  # CI: prove the id rule and the change log on planted cases

Why a separate export: data/connectors.json is about 6 MB and shaped for the
README generator. A browser wants small files it can fetch lazily and a
stable id per entry for its URLs. This script derives both from the same data,
so the site can never disagree with the list: same entries, same text, same
order. Stdlib only. Output is deterministic (no timestamps beyond the data's own
dates), so --check is a byte comparison. The one clock read is the date on a
change the export records in data/changes.json when it writes; --check never
records.

Layout (schema_version 1):
    site-data/index.json               meta, categories with counts and file names
    site-data/search.json              id, name, category slug, marker and first-seen date
                                       ("added") per listed entry (search by name here; full
                                       text lives in the category files)
    site-data/categories/<slug>.json   full entries of one category
    site-data/held.json                Held for Verification rows
    site-data/editorial.json           featured picks and collections, from data/editorial.json
    site-data/stacks.json              Splices (once Connector Snap Stacks), parsed from docs/stacks/*.md
    site-data/changes.json             ids added, removed and renamed per dated change, newest first,
                                       from data/changes.json

Entry ids are slugs of the entry name ("Google Drive" -> "google-drive"). Names
are unique case-insensitively, but slugging drops punctuation and Latin accents,
so two names can share a slug ("PDF Viewer" / "pdf-viewer", "Agora" / "Ágora").
Those get a hand-picked id in ID_OVERRIDES, and any new collision fails loud
rather than being numbered, so an id never silently changes meaning. A renamed
entry gets a new id. Names in other scripts keep their letters whole: kana keep
their voiced marks and Hangul stays composed.

First-seen dates come from data/changes.json, the record of when each id joined
or left the listed set (rebuilt from git history up to 2026-11-22 by
scripts/backfill_changes.py, appended by this script since). "added" is the date
an entry was first listed here, not the date Anthropic added it to the catalog.
A renamed entry keeps its date, and so does an id that leaves and comes back.
When data/connectors.json and the record disagree, a plain run appends a change
dated today (a name that changed while its URL stayed is recorded as a rename)
and --check fails, so CI never needs the git history.

Schema changes add fields and never repurpose one; a breaking change bumps
schema_version. Fields planned, not yet in the data: auth (sign-in required or
not, from the feed) and per-tool permission flags (read-only, destructive).
"""

import datetime
import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "connectors.json"
EDITORIAL = REPO / "data" / "editorial.json"
CHANGES = REPO / "data" / "changes.json"
STACKS = REPO / "docs" / "stacks"
OUT = REPO / "site-data"
SCHEMA_VERSION = 1
# Names whose slug collides with another entry's: a person picks each id once.
ID_OVERRIDES = {
    "PDF Viewer": "pdf-viewer",
    "pdf-viewer": "pdf-viewer-quickstarts",
    "Agora": "agora",
    "Ágora": "agora-red",
}
# marker -> tier. An unmarked entry is partner tier or predates feed-tier sync, so
# it gets null rather than a guess.
TIER = {"A": "anthropic", "C": "community"}
MARKERS = {
    "A": "Built and maintained by Anthropic",
    "C": "Community badge in the in-app catalog: published by Anthropic, built by a third party",
}


# Marks a slug may drop without changing a letter: an accent left with no base
# letter, emoji selectors and keycaps, and the optional pointing of Arabic and Hebrew.
LOOSE_MARK = re.compile(
    r"[\u0300-\u036f\u20d0-\u20ff\ufe00-\ufe0f"
    r"\u0591-\u05c7\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed]"
)


def slug(text):
    """Slug of a name. Latin letters lose their accents; every other script keeps
    its letters whole and NFC-composed (URLs allow them). A mark with no rule here
    stops the export, so a name is never slugged into a different word."""
    kept, latin = [], False
    for c in unicodedata.normalize("NFKD", text):
        if unicodedata.combining(c):
            if latin:
                continue
        else:
            latin = unicodedata.name(c, "").startswith("LATIN")
        kept.append(c)
    t = unicodedata.normalize("NFC", "".join(kept)).lower()
    for c in t:
        if unicodedata.category(c)[0] == "M" and not LOOSE_MARK.match(c):
            raise SystemExit(
                f"slug() has no rule for {unicodedata.name(c, hex(ord(c)))} in "
                f"{text!r}: decide how that script slugs before the name gets an id"
            )
    t = "".join(c for c in t if unicodedata.category(c)[0] != "M")
    t = re.sub(r"[^\w]+", "-", t, flags=re.UNICODE).strip("-_")
    return re.sub(r"[-_]+", "-", t)


def entry_id(name):
    return ID_OVERRIDES.get(name) or slug(name) or "entry"


def selftest():
    """An id rule nobody has seen fail proves nothing. Break it on known names."""
    cases = [
        ("Café Über", "cafe-uber", "Latin accents fold"),
        ("PDF Viewer", "pdf-viewer", "spaces and case"),
        ("a_b -- c", "a-b-c", "punctuation runs collapse"),
        ("O´Hoi", "o-hoi", "a spacing accent is punctuation"),
        ("わだち", "わだち", "hiragana keeps its voiced mark"),
        ("クラウド会計", "クラウド会計", "katakana keeps its voiced mark"),
        ("ﾃﾞｰﾀ", "データ", "half-width kana compose"),
        ("한글 Notes", "한글-notes", "Hangul stays composed"),
        ("Йога", "йога", "Cyrillic keeps its breve"),
        ("كِتَاب", "كتاب", "Arabic loses its optional pointing"),
        ("سؤال", "سؤال", "Arabic keeps hamza on its letter"),
    ]
    for name, want, why in cases:
        got = slug(name)
        ok = got == want and got == unicodedata.normalize("NFC", got)
        print(f"  {'ok ' if ok else 'FAIL'} {name!r} -> {got!r} want {want!r}   ({why})")
        if not ok:
            sys.exit("id self-test failed -- do not trust this export")
    try:
        slug("สวัสดี")
    except SystemExit:
        print("  ok  a mark with no rule stops the export")
    else:
        sys.exit("id self-test failed -- a mark with no rule must stop the export")
    selftest_changes()
    print("  self-test passed")


def replay(changes):
    """data/changes.json -> {id: first date} for the ids listed after the last change.
    Stops on a record that cannot have happened, so a bad hand edit never reaches the site."""
    first, retired, last = {}, {}, ""
    for n, ch in enumerate(changes, 1):
        where = f"data/changes.json change {n} ({ch.get('date')})"
        if set(ch) != {"date", "added", "removed", "renamed"}:
            raise SystemExit(f"{where}: keys must be exactly date/added/removed/renamed")
        date = ch["date"]
        try:
            iso = datetime.date.fromisoformat(date).isoformat() == date
        except (TypeError, ValueError):
            iso = False
        if not iso:
            raise SystemExit(f"{where}: date must be YYYY-MM-DD")
        if date < last:
            raise SystemExit(f"{where}: dates must not go backwards")
        last = date
        for i in ch["removed"]:
            if i not in first:
                raise SystemExit(f"{where}: removes {i!r}, which is not listed at that point")
            retired[i] = first.pop(i)
        moved = {}
        for r in ch["renamed"]:
            if r["from"] not in first:
                raise SystemExit(f"{where}: renames {r['from']!r}, which is not listed at that point")
            moved[r["to"]] = first.pop(r["from"])
        for i, d in moved.items():
            if i in first:
                raise SystemExit(f"{where}: renames onto {i!r}, which is already listed")
            first[i] = d
        for i in ch["added"]:
            if i in first:
                raise SystemExit(f"{where}: adds {i!r}, which is already listed")
            first[i] = retired.pop(i, date)
    return first


def record(changes, data, have, today):
    """Append what the listed ids did since the last recorded change. True if it appended."""
    first = replay(changes)
    now = {entry_id(e["name"]): e["url"] for e in data["connectors"]}
    added, removed = set(now) - set(first), set(first) - set(now)
    if not (added or removed):
        return False
    if changes and today < changes[-1]["date"]:
        raise SystemExit(f"today ({today}) is earlier than the last change in data/changes.json")
    # A name that changed while its URL stayed is a rename. The last export on
    # disk still holds the old id for that URL.
    old_id = {}
    for path, text in have.items():
        if path.startswith("categories/"):
            for row in json.loads(text)["connectors"]:
                old_id[row["url"]] = row["id"]
    renamed = []
    for i in sorted(added):
        old = old_id.get(now[i])
        if old in removed:
            renamed.append({"from": old, "to": i})
            removed.discard(old)
            added.discard(i)
    changes.append({"date": today, "added": sorted(added), "removed": sorted(removed),
                    "renamed": sorted(renamed, key=lambda r: r["from"])})
    return True


def selftest_changes():
    """The change log on planted cases: what it must carry, and what must stop it."""
    def ch(day, added=(), removed=(), renamed=()):
        return {"date": f"2026-01-0{day}", "added": list(added), "removed": list(removed),
                "renamed": [{"from": a, "to": b} for a, b in renamed]}
    got = replay([ch(1, ["a", "b"]), ch(2, removed=["a"], renamed=[("b", "c")]), ch(3, ["a", "b"])])
    for i, want, why in [
        ("a", "2026-01-01", "an id that leaves and returns keeps its first date"),
        ("c", "2026-01-01", "a renamed entry keeps its first date"),
        ("b", "2026-01-03", "a new entry under a freed id starts fresh"),
    ]:
        ok = got.get(i) == want
        print(f"  {'ok ' if ok else 'FAIL'} {i!r} first seen {got.get(i)} want {want}   ({why})")
        if not ok:
            sys.exit("change-log self-test failed -- do not trust the first-seen dates")
    for why, bad in [
        ("a removal of an id that is not listed", [ch(1, removed=["x"])]),
        ("an id added twice", [ch(1, ["a"]), ch(2, ["a"])]),
        ("dates that go backwards", [ch(2, ["a"]), ch(1, ["b"])]),
        ("a rename onto a listed id", [ch(1, ["a", "b"]), ch(2, renamed=[("a", "b")])]),
        ("a date that is not a date", [{**ch(1, ["a"]), "date": "2026-13-01"}]),
    ]:
        try:
            replay(bad)
        except SystemExit:
            print(f"  ok  {why} stops the export")
        else:
            sys.exit(f"change-log self-test failed -- {why} must stop the export")
    log = [ch(1, ["old-name", "gone"])]
    data = {"connectors": [{"name": "New Name", "url": "https://kept.example"},
                           {"name": "Fresh", "url": "https://fresh.example"}]}
    have = {"categories/c.json": json.dumps({"connectors": [
        {"id": "old-name", "url": "https://kept.example"},
        {"id": "gone", "url": "https://gone.example"}]})}
    want = ch(2, ["fresh"], ["gone"], [("old-name", "new-name")])
    ok = record(log, data, have, "2026-01-02") and log[-1] == want and not record(log, data, have, "2026-01-03")
    print(f"  {'ok ' if ok else 'FAIL'} a write records one add, one removal and one rename, then nothing")
    if not ok:
        sys.exit("change-log self-test failed -- the export records changes wrongly")


ORDINALS = {"debut": 1, "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5,
            "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10}
STACK_LINK = re.compile(r"\*\*\[([^\]]+)\]\((https://[^)]+)\)\*\*( \*\(new\)\*)?")


def parse_stack(path, ids_by_name):
    """One docs/stacks/*.md file -> a stack record. Fails loud on an unexpected shape."""
    lines = path.read_text(encoding="utf-8").splitlines()
    m = re.match(r"# Splice — (.+)$", lines[0])
    meta = re.match(r"\*(\d{4}-\d{2}-\d{2}) · (\w+) Splice\*$", lines[2])
    if not (m and meta):
        raise SystemExit(f"{path.name}: unexpected stack header")
    combo = lines[4]
    client = re.search(r"— running in \*\*([^*]+)\*\*\s*$", combo)
    links = STACK_LINK.findall(combo)
    if not (client and links):
        raise SystemExit(f"{path.name}: unexpected connector line")
    body = [l for l in lines[5:] if l.strip()]
    status = body[-1].strip("*") if body and body[-1].startswith("*Status:") else None
    prose = " ".join(l for l in body if not l.startswith("*Status:"))
    return {
        "slug": path.stem[11:],
        "title": m.group(1),
        "date": meta.group(1),
        "number": ORDINALS.get(meta.group(2).lower()),
        "client": client.group(1),
        "connectors": [
            {"name": n, "url": u, "new": bool(new), "id": ids_by_name.get(n.lower())}
            for n, u, new in links
        ],
        "summary": prose,
        "status": status,
        "source": f"docs/stacks/{path.name}",
    }


def build_editorial(listed_ids):
    if not EDITORIAL.exists():
        return {"schema_version": SCHEMA_VERSION, "featured": [], "collections": []}
    ed = json.loads(EDITORIAL.read_text(encoding="utf-8"))
    ed.pop("_comment", None)
    for f in ed["featured"]:
        if f["id"] not in listed_ids:
            raise SystemExit(f"editorial featured id {f['id']!r} is not a listed entry")
    for c in ed["collections"]:
        for sec in c["sections"]:
            for i in sec["ids"]:
                if i not in listed_ids:
                    raise SystemExit(f"collection {c['slug']!r} id {i!r} is not a listed entry")
    return {"schema_version": SCHEMA_VERSION, **ed}


def build(data, changes):
    cats = data["categories"]
    cat_slugs = {c: slug(c) for c in cats}
    if len(set(cat_slugs.values())) != len(cats):
        raise SystemExit("category slugs collide")

    stale = sorted(set(ID_OVERRIDES) - {e["name"] for e in data["connectors"]})
    if stale:
        raise SystemExit(f"ID_OVERRIDES names no listed entry: {stale}")

    ids = {}
    for e in data["connectors"]:
        i = entry_id(e["name"])
        if i in ids:
            raise SystemExit(f"entry id collision {i!r}: {ids[i]!r} and {e['name']!r}")
        ids[i] = e["name"]

    first = replay(changes)
    unrecorded, departed = sorted(set(ids) - set(first)), sorted(set(first) - set(ids))
    if unrecorded or departed:
        raise SystemExit(
            "data/changes.json is out of step with data/connectors.json: "
            f"{len(unrecorded)} listed ids not recorded {unrecorded[:5]}, "
            f"{len(departed)} recorded ids no longer listed {departed[:5]}; "
            "run python3 scripts/export_site_data.py to record them"
        )

    by_cat = {c: [] for c in cats}
    for e in data["connectors"]:
        by_cat[e["category"]].append(e)

    files = {}
    search = []
    index_cats = []
    for c in cats:
        entries = sorted(by_cat[c], key=lambda e: e["name"].lower())
        rows = []
        subs = {}
        for e in entries:
            row = {
                "id": entry_id(e["name"]),
                "name": e["name"],
                "url": e["url"],
                "marker": e.get("marker"),
                "tier": TIER.get(e.get("marker")),
                "category": c,
                "subcategory": e.get("subcategory"),
                "description": e["description"],
                "use_case": e["use_case"],
            }
            rows.append(row)
            if row["subcategory"]:
                subs[row["subcategory"]] = subs.get(row["subcategory"], 0) + 1
            search.append(
                {
                    "id": row["id"],
                    "n": e["name"],
                    "c": cat_slugs[c],
                    "m": e.get("marker"),
                    "added": first[row["id"]],
                }
            )
        files[f"categories/{cat_slugs[c]}.json"] = {
            "schema_version": SCHEMA_VERSION,
            "category": c,
            "slug": cat_slugs[c],
            "count": len(rows),
            "connectors": rows,
        }
        index_cats.append(
            {
                "name": c,
                "slug": cat_slugs[c],
                "count": len(rows),
                "file": f"categories/{cat_slugs[c]}.json",
                "subcategories": [
                    {"name": s, "count": n} for s, n in sorted(subs.items())
                ],
            }
        )

    search.sort(key=lambda r: r["n"].lower())
    held = sorted(data["held"], key=lambda h: h["name"].lower())
    files["search.json"] = {"schema_version": SCHEMA_VERSION, "connectors": search}
    files["held.json"] = {"schema_version": SCHEMA_VERSION, "count": len(held), "held": held}
    listed_ids = {r["id"] for r in search}
    files["editorial.json"] = build_editorial(listed_ids)
    ids_by_name = {e["name"].lower(): entry_id(e["name"]) for e in data["connectors"]}
    stacks = [parse_stack(p, ids_by_name) for p in sorted(STACKS.glob("*.md"))] if STACKS.exists() else []
    stacks.sort(key=lambda s: s["date"], reverse=True)
    files["stacks.json"] = {"schema_version": SCHEMA_VERSION, "count": len(stacks), "stacks": stacks}
    files["changes.json"] = {"schema_version": SCHEMA_VERSION, "count": len(changes),
                             "changes": changes[::-1]}
    files["index.json"] = {
        "schema_version": SCHEMA_VERSION,
        "last_updated": data["meta"]["last_updated"],
        "capture_date": data["meta"]["capture_date"],
        "listed": len(data["connectors"]),
        "held": len(held),
        "markers": MARKERS,
        "categories": index_cats,
        "files": {"search": "search.json", "held": "held.json",
                  "editorial": "editorial.json", "stacks": "stacks.json",
                  "changes": "changes.json"},
    }
    return {
        p: json.dumps(v, ensure_ascii=False, separators=(",", ":")) + "\n"
        for p, v in files.items()
    }


def main():
    if "--selftest" in sys.argv:
        selftest()
        return
    data = json.loads(DATA.read_text(encoding="utf-8"))
    log = json.loads(CHANGES.read_text(encoding="utf-8"))
    have = {
        p.relative_to(OUT).as_posix(): p.read_text(encoding="utf-8")
        for p in OUT.rglob("*.json")
    } if OUT.exists() else {}
    check = "--check" in sys.argv
    if not check and record(log["changes"], data, have, datetime.date.today().isoformat()):
        CHANGES.write_text(json.dumps(log, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        ch = log["changes"][-1]
        print(
            f"recorded in data/changes.json, dated {ch['date']}: {len(ch['added'])} added, "
            f"{len(ch['removed'])} removed, {len(ch['renamed'])} renamed"
        )
    want = build(data, log["changes"])
    if check:
        stale = sorted(p for p in want if have.get(p) != want[p])
        stray = sorted(set(have) - set(want))
        if stale or stray:
            raise SystemExit(
                "site-data/ is out of date with data/connectors.json; run "
                f"python3 scripts/export_site_data.py (stale: {stale[:5]}, stray: {stray[:5]})"
            )
        print(f"site-data/ matches data/connectors.json — {len(want)} files")
        return
    for p in set(have) - set(want):
        (OUT / p).unlink()
    for p, text in want.items():
        f = OUT / p
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text, encoding="utf-8")
    sizes = sorted(((len(t.encode()), p) for p, t in want.items()), reverse=True)
    print(
        f"wrote {len(want)} files to site-data/; largest {sizes[0][1]} "
        f"{sizes[0][0]:,} bytes; search.json {len(want['search.json'].encode()):,} bytes"
    )


if __name__ == "__main__":
    main()
