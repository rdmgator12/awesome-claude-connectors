#!/usr/bin/env python3
"""Emit README.md and categories/<slug>.md from data/connectors.json — the single source of truth.

Usage:
    python3 scripts/generate_readme.py          # regenerate README.md + category pages
    python3 scripts/generate_readme.py --check  # verify every generated file matches the data (CI)
    python3 scripts/generate_readme.py --selftest  # CI: prove the validator on planted entries, then exit

README.md is the front page (intro, Splice, category index, held table); each
category's entries live on their own page because GitHub stops rendering a
markdown file at ~512 KB (the single-file README hit 764 KB on 2026-09-14 and
went dark from mid-Marketing and Sales onward).

Render switches live in data/connectors.json meta.render, never CLI flags, so the
flagless CI --check is deterministic against versioned input. Content is emitted
verbatim — no punctuation or whitespace normalization (descriptions legitimately
end in "。" and "!" as well as "."). Provenance markers (A/C) are stored in the
data even when render-suppressed: awesome-lint 2.3.0 rejects a bold-code marker
before a description that does not start with an uppercase Latin letter.
"""

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "connectors.json"
TEMPLATE = REPO / "README.template.md"
README = REPO / "README.md"
CATEGORIES_DIR = REPO / "categories"
# Absolute, because a category page is a file view: it has no Star button of its
# own, and a relative link would land on another file view.
REPO_URL = "https://github.com/rdmgator12/awesome-claude-connectors"

# GitHub truncates rendering at ~512 KB; fail well before it.
RENDER_CEILING = 500_000

TERMINAL = (".", "。", "!")
INDEX_SECTION = "Categories"
TAIL_SECTIONS = ("Held for Verification", "Related")
STRUCTURAL_TOKENS = {"{{TOC}}", "{{CATEGORY_INDEX}}", "{{HELD_TABLE}}"}
SIMPLE_TOKENS = {
    "{{LISTED}}",
    "{{HELD}}",
    "{{NCAT}}",
    "{{LAST_UPDATED}}",
    "{{CAPTURE_DATE}}",
}
KNOWN_TOKENS = STRUCTURAL_TOKENS | SIMPLE_TOKENS

ENTRY_KEYS = {"name", "url", "marker", "category", "description", "use_case"}
OPTIONAL_ENTRY_KEYS = {"subcategory"}
HELD_KEYS = {"name", "catalog_description", "why_held"}
HELD_HEADER = ("Connector", "Catalog description", "Why held")
INDEX_HEADER = ("Category", "Connectors")

# Entry text is emitted verbatim into markdown, so anything that would render as a
# link, an image or raw HTML is refused: a description is prose, and the entry's one
# link is its vetted `url`. A bare "www." in any case, any scheme and an email address
# autolink on GitHub, and it looks for them after it has decoded character references
# and dropped backslash escapes: "https&#58;//x.example", "www\.x.example" and
# "a\@x.example" all rendered as links on its renderer (2026-11-24). So prose carries
# no backslash and no reference at all ("www." is tested apart, for its case).
UNSAFE_TEXT = ("<", ">", "`", "](", "://", "\\")
ENTITY = re.compile(r"&(?:#[0-9]+|#[xX][0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]*);")
# The host may start with a dot: GitHub links "a@.x.example" too.
EMAIL = re.compile(r"[A-Za-z0-9._+-]@(?=[A-Za-z0-9._-]*\.[A-Za-z0-9_-])")
# A name is the text of its entry's link, where "www." and an address stay inert. A
# reference or an escape there would make one name read as another ("Strip&#101;").
NAME_UNSAFE = ("<", ">", "`", "://")
NAME_ESCAPE = re.compile(r"\\(?:\S|$)")
URL_UNSAFE = '"\\<>{}|^`('
URL_HOST = re.compile(r"https://([^/?#]*)")
# A category or subcategory becomes a heading, an anchor and a link's text.
HEADING = re.compile(r"[A-Za-z0-9 ]+")
# Both dates are printed into the README and every category page as they stand.
LAST_UPDATED = re.compile(r"[A-Z][a-z]+ [0-9]{1,2}, [0-9]{4}")
CAPTURE_DATE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
# Characters that render as nothing. IGNORABLE holds the members of Unicode's
# Default_Ignorable_Code_Point that the category test in unsafe_chars() does not catch
# (compared against the whole property in Unicode 13, plus U+180F from Unicode 14); it
# includes the variation selectors, emoji selector U+FE0F among them, until a name
# needs one. BLANK holds blank-rendering characters outside that property.
IGNORABLE = (
    (0x034F, 0x034F),
    (0x115F, 0x1160),
    (0x17B4, 0x17B5),
    (0x180B, 0x180F),
    (0x3164, 0x3164),
    (0xFE00, 0xFE0F),
    (0xFFA0, 0xFFA0),
    (0xE0100, 0xE01EF),
)
BLANK = {0x2800, 0x16FE4, 0x1D159}

# The two allowlists live here, not in data/, so a data-only pull request cannot
# edit its own guard: a new heading or a new Anthropic-built entry is a change to
# this file, made on purpose.
#
# Subcategory headings, per subcategorized category.
SUBCATEGORIES = {
    "Data and Analytics": (
        "Business Intelligence and Dashboards",
        "Commerce and Revenue Analytics",
        "Company and Market Intelligence",
        "Data Engineering and Pipelines",
        "Databases and Warehouses",
        "Geospatial and Industry Data",
        "People and Customer Insights",
        "Product and Web Analytics",
    ),
    "Finance and Trading": (
        "Accounting Payroll and Financial Planning",
        "Business Banking and Spend Management",
        "Credit Risk Compliance and Insurance",
        "Crypto and Web3",
        "Payments Billing and Invoicing",
        "Personal Finance and Consumer Tax",
        "Private Markets Real Estate and Deal Intelligence",
        "Trading Brokerage and Wealth Management",
    ),
    "Lifestyle and Local": (
        "Cars and Mobility",
        "Fitness Sports and Outdoors",
        "Food Groceries and Restaurants",
        "Hobbies Culture and Everyday Life",
        "Home Pets and Local Services",
        "Real Estate and Housing",
        "Shopping Deals and Price Comparison",
    ),
    "Marketing and Sales": (
        "Advertising and Paid Media",
        "Brand Management and Content Creation",
        "CRM and Pipeline Management",
        "Email SMS and Lifecycle Marketing",
        "Loyalty Referrals and Partner Programs",
        "Marketing Analytics and Consumer Insights",
        "Sales Prospecting and Engagement",
    ),
    "Productivity": (
        "Forms Slides and Workspaces",
        "Meetings and Transcription",
        "Notes and Knowledge Management",
        "Reading and Saved Content",
        "Small Business and Field Operations",
        "Tasks Planning and Habits",
        "Team HR and Time Tracking",
        "Thinking Tools and Utilities",
    ),
}
# The names that carry marker "A": the directory feed's `anthropic` tier, plus the
# four Anthropic quickstart extensions (github.com/anthropics) that the feed files
# under its partner tier.
ANTHROPIC_BUILT = {
    "Anthropic Economic Index",
    "bioRxiv",
    "ChEMBL",
    "Claude Academy",
    "Clinical Trials",
    "CMS Coverage",
    "ICD-10 Codes",
    "Microsoft 365",
    "NPI Registry",
    "PDF Viewer",
    "pdf-viewer",
    "PowerPoint (By Anthropic)",
    "PubMed",
    "Word (By Anthropic)",
}


def unsafe_chars(value):
    """Code points that hide or reorder text: control, format (zero-width, bidi),
    private-use, surrogate and unassigned characters, line and paragraph separators,
    any space but the ASCII one, and everything in IGNORABLE and BLANK. Unassigned
    follows the interpreter's Unicode tables; CI runs Python 3.13."""
    return sorted(
        {
            f"U+{ord(c):04X}"
            for c in value
            if unicodedata.category(c) in ("Cc", "Cf", "Co", "Cs", "Cn", "Zl", "Zp")
            or (unicodedata.category(c) == "Zs" and c != " ")
            or ord(c) in BLANK
            or any(lo <= ord(c) <= hi for lo, hi in IGNORABLE)
        }
    )


def text_problems(value):
    """What in a piece of prose would render as a link or markup, as a list."""
    found = [repr(token) for token in UNSAFE_TEXT if token in value]
    if "www." in value.lower():
        found.append(repr("www."))
    if ENTITY.search(value):
        found.append("a character reference such as '&#58;'")
    if EMAIL.search(value):
        found.append("an email address")
    return found


def url_problem(url):
    """Why a link target is refused, or None. The host must read as what it is."""
    host = URL_HOST.match(url).group(1)
    if "@" in host:
        return "carries userinfo before the host"
    if ":" in host:
        return "carries a port"
    if not re.fullmatch(r"[a-z0-9.-]+", host):
        return "host is not lowercase ASCII"
    if "" in host.split("."):
        return "host has an empty label (a leading, trailing or doubled dot)"
    if host.startswith("xn--") or ".xn--" in host:
        return "host is punycode (an internationalized domain needs a deliberate exception here)"
    # A browser reads a host whose last label is a number as an IP address, and it
    # accepts hex there (0x7f.0.0.1), so the last label must be letters.
    if "." not in host or not re.fullmatch(r"[a-z]+", host.rsplit(".", 1)[1]):
        return "host is not a domain name"
    return None


def slugify(title):
    # GitHub's slugger, verified to reproduce every anchor in the live TOC
    return re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")


def marker_renderable(entry):
    return (
        bool(entry.get("marker"))
        and re.match(r"[A-Z]", entry["description"]) is not None
    )


def render_entry(entry):
    mk = f" **`{entry['marker']}`**" if marker_renderable(entry) else ""
    return (
        f"- [{entry['name']}]({entry['url']}){mk}"
        f" - {entry['description']} *Use case: {entry['use_case']}*"
    )


def category_path(cat):
    return f"categories/{slugify(cat)}.md"


def connector_count(n):
    return f"{n:,} connector{'s' if n != 1 else ''}"


def render_toc():
    return "\n".join(
        f"- [{t}](#{slugify(t)})" for t in (INDEX_SECTION,) + TAIL_SECTIONS
    )


def render_index(data, by_cat):
    # a table, not a list: awesome-lint's list-item rule rejects relative links
    return render_table(
        INDEX_HEADER,
        [
            (f"[{cat}]({category_path(cat)})", f"{len(by_cat[cat]):,}")
            for cat in data["categories"]
        ],
    )


def page_subcategories(data, entries):
    if not data["meta"]["render"]["subcategory_headings"]:
        return []
    return sorted(
        {e["subcategory"] for e in entries if e.get("subcategory")}, key=str.lower
    )


def render_category_page(data, cat, entries):
    entries = sorted(entries, key=lambda e: e["name"].lower())
    header = [f"[All categories](../README.md#{slugify(INDEX_SECTION)})"]
    if data["meta"]["render"]["category_counts"]:
        header.append(connector_count(len(entries)))
    header.append(f"Last updated {data['meta']['last_updated']}")
    header.append(f"[Star the list]({REPO_URL}) if it helped")
    lines = [
        "<!-- Generated from data/connectors.json by scripts/generate_readme.py. Edit the data, not this file. -->",
        "",
        f"# {cat}",
        "",
        " · ".join(header),
        "",
        "Connectors marked **`A`** are built and maintained by Anthropic; **`C`** marks the in-app catalog's "
        "Community badge (third-party built, not vetted like web-directory entries). "
        "Methodology and the held-entry policy are in the [README](../README.md) and [CONTRIBUTING.md](../CONTRIBUTING.md).",
        "",
    ]
    subs = page_subcategories(data, entries)
    if subs:
        # one line, not a list: awesome-lint's list-item rule rejects anchor links
        lines += [" · ".join(f"[{s}](#{slugify(s)})" for s in subs), ""]
        for sub in subs:
            lines += [f"## {sub}", ""]
            lines += [render_entry(e) for e in entries if e.get("subcategory") == sub]
            lines.append("")
    else:
        lines += [render_entry(e) for e in entries] + [""]
    return "\n".join(lines)


def render_table(header, rows):
    # pipes aligned and delimiter padded, or awesome-lint fails
    # table-pipe-alignment / table-cell-padding
    widths = [
        max(len(header[i]), max(len(r[i]) for r in rows)) for i in range(len(header))
    ]

    def line(cells):
        return "| " + " | ".join(c.ljust(w) for c, w in zip(cells, widths)) + " |"

    sep = "| " + " | ".join("-" * w for w in widths) + " |"
    return "\n".join([line(header), sep] + [line(r) for r in rows])


def render_held_table(rows):
    rows = sorted(rows, key=lambda r: r["name"].lower())
    keys = ("name", "catalog_description", "why_held")
    return render_table(HELD_HEADER, [tuple(r[k] for k in keys) for r in rows])


def suppressed_markers(connectors):
    return [
        e["name"] for e in connectors if e.get("marker") and not marker_renderable(e)
    ]


def validate(data, template):
    errors = []
    add = errors.append

    if not isinstance(data, dict) or set(data) != {
        "meta",
        "categories",
        "connectors",
        "held",
    }:
        return ["top-level keys must be exactly meta/categories/connectors/held"]

    meta = data["meta"]
    subheadings_on = False
    if not isinstance(meta, dict) or set(meta) != {
        "last_updated",
        "capture_date",
        "render",
    }:
        add("meta keys must be exactly last_updated/capture_date/render")
    else:
        for k, shape, like in (
            ("last_updated", LAST_UPDATED, "November 23, 2026"),
            ("capture_date", CAPTURE_DATE, "2026-11-23"),
        ):
            if not isinstance(meta[k], str) or not shape.fullmatch(meta[k]):
                add(f"meta.{k} must read like {like!r}, got {meta[k]!r}")
        render = meta["render"]
        if not isinstance(render, dict) or set(render) != {
            "category_counts",
            "subcategory_headings",
        }:
            add("meta.render keys must be exactly category_counts/subcategory_headings")
        elif not all(isinstance(v, bool) for v in render.values()):
            add("meta.render values must be booleans")
        else:
            subheadings_on = render["subcategory_headings"]

    cats = data["categories"]
    if (
        not isinstance(cats, list)
        or not cats
        or not all(isinstance(c, str) and c and c == c.strip() for c in cats)
    ):
        add("categories must be a non-empty list of non-empty stripped strings")
        cats = [c for c in cats if isinstance(c, str)] if isinstance(cats, list) else []
    for low, group in _grouped(cats, str.lower):
        if len(group) > 1:
            add(f"duplicate category (case-insensitive): {group}")
    for heading in cats + [s for subs in SUBCATEGORIES.values() for s in subs]:
        if not HEADING.fullmatch(heading):
            add(
                f"category or subcategory {heading!r} must be letters, digits and "
                "spaces only (it becomes a heading, an anchor and a link)"
            )

    catset = set(cats)
    names, urls, subcategories = {}, {}, set()
    if not isinstance(data["connectors"], list) or not data["connectors"]:
        add("connectors must be a non-empty list")
    for e in data["connectors"] if isinstance(data["connectors"], list) else []:
        if not isinstance(e, dict):
            add(f"connector is not an object: {e!r}")
            continue
        label = (
            e.get("name")
            if isinstance(e.get("name"), str) and e.get("name")
            else repr(e)[:80]
        )
        missing = ENTRY_KEYS - set(e)
        unknown = set(e) - ENTRY_KEYS - OPTIONAL_ENTRY_KEYS
        if missing:
            add(f"{label}: missing key(s) {sorted(missing)}")
        if unknown:
            add(f"{label}: unknown key(s) {sorted(unknown)}")
        name = e.get("name")
        if not isinstance(name, str) or not name or name != name.strip():
            add(f"{label}: name must be a non-empty stripped string")
        elif "[" in name or "]" in name or "\n" in name or "\r" in name:
            add(f"{label}: name must not contain square brackets or newlines")
        elif any(token in name for token in NAME_UNSAFE):
            add(
                f"{label}: name must not contain any of {' '.join(NAME_UNSAFE)} "
                "(it would render as a second link or markup)"
            )
        elif ENTITY.search(name) or NAME_ESCAPE.search(name):
            add(
                f"{label}: name must not contain a character reference or a backslash "
                "escape (it would read as another name)"
            )
        else:
            names.setdefault(name.lower(), []).append(name)
        url = e.get("url")
        if not isinstance(url, str) or not url.startswith("https://"):
            add(f"{label}: url must start with https://")
        elif ")" in url or " " in url or "\n" in url or "\r" in url:
            add(f"{label}: url must not contain ')', spaces, or newlines")
        elif any(c in url for c in URL_UNSAFE):
            add(f"{label}: url must not contain any of {' '.join(URL_UNSAFE)}: {url}")
        elif ENTITY.search(url):
            add(f"{label}: url must not contain a character reference: {url}")
        elif url_problem(url):
            add(f"{label}: url {url_problem(url)}: {url}")
        else:
            urls.setdefault(url, []).append(label)
        if e.get("marker") not in ("A", "C", None):
            add(
                f"{label}: marker must be \"A\", \"C\", or null, got {e.get('marker')!r}"
            )
        elif (e.get("marker") == "A") != (
            isinstance(name, str) and name in ANTHROPIC_BUILT
        ):
            add(
                f"{label}: marker {e.get('marker')!r} disagrees with ANTHROPIC_BUILT "
                '(scripts/generate_readme.py): "A" goes on exactly the names listed there'
            )
        cat = e.get("category")
        if not isinstance(cat, str) or cat not in catset:
            add(f"{label}: unknown category {cat!r}")
        for field in ("description", "use_case"):
            v = e.get(field)
            if not isinstance(v, str) or not v or v != v.strip():
                add(f"{label}: {field} must be a non-empty stripped string")
                continue
            if "\n" in v or "\r" in v:
                add(f"{label}: {field} must not contain newlines")
            if "*" in v:
                add(
                    f"{label}: {field} must not contain '*' (breaks the italic wrapper)"
                )
            for found in text_problems(v):
                add(
                    f"{label}: {field} must not contain {found} (it would render as a link or markup)"
                )
            if not v.endswith(TERMINAL):
                add(
                    f"{label}: {field} must end with one of {'/'.join(TERMINAL)}, got ...{v[-15:]!r}"
                )
        if "subcategory" in e:
            sub = e["subcategory"]
            if sub is not None and (
                not isinstance(sub, str)
                or not sub
                or sub != sub.strip()
                or "\n" in sub
                or "\r" in sub
            ):
                add(f"{label}: subcategory must be null or a non-empty stripped string")
            elif isinstance(sub, str):
                subcategories.add(sub)
                if sub not in SUBCATEGORIES.get(
                    cat if isinstance(cat, str) else "", ()
                ):
                    add(
                        f"{label}: subcategory {sub!r} is not a heading of {cat!r} "
                        "in SUBCATEGORIES (scripts/generate_readme.py)"
                    )

    for low, group in _grouped_dict(names):
        if len(group) > 1:
            add(f"duplicate connector name (case-insensitive): {group}")
    for url, group in urls.items():
        if len(group) > 1:
            add(f"duplicate URL {url}: {group}")
    listed_names = {n for group in names.values() for n in group}
    for stale in sorted(ANTHROPIC_BUILT - listed_names):
        add(f"ANTHROPIC_BUILT names no listed entry: {stale!r}")

    if isinstance(data["connectors"], list):
        used = Counter(
            e.get("category")
            for e in data["connectors"]
            if isinstance(e, dict) and e.get("category") in catset
        )
        for c in cats:
            if not used[c]:
                add(f"category has no connectors: {c}")
        if subheadings_on:
            # all-or-none per category: a partially subcategorized category would
            # render its unfiled entries as a headless clump above the first ###
            for c in cats:
                entries = [
                    e
                    for e in data["connectors"]
                    if isinstance(e, dict) and e.get("category") == c
                ]
                unfiled = [
                    e["name"]
                    for e in entries
                    if not e.get("subcategory") and isinstance(e.get("name"), str)
                ]
                if unfiled and len(unfiled) != len(entries):
                    add(
                        f"category {c!r} is partially subcategorized — assign these or "
                        f"none: {unfiled[:5]}{' ...' if len(unfiled) > 5 else ''}"
                    )

    held_names = {}
    if not isinstance(data["held"], list) or not data["held"]:
        add(
            "held must be a non-empty list (if the held table should disappear, that is a template decision, not an empty array)"
        )
    for h in data["held"] if isinstance(data["held"], list) else []:
        if not isinstance(h, dict) or set(h) != HELD_KEYS:
            add(f"held row keys must be exactly {sorted(HELD_KEYS)}: {h!r}"[:200])
            continue
        hlabel = h["name"] if isinstance(h["name"], str) and h["name"] else repr(h)[:80]
        for k in HELD_KEYS:
            v = h[k]
            if not isinstance(v, str) or not v or v != v.strip():
                add(f"held {hlabel}: {k} must be a non-empty stripped string")
            elif "|" in v or "\n" in v or "\r" in v:
                add(f"held {hlabel}: {k} must not contain '|' or newlines")
            else:
                for found in text_problems(v):
                    add(
                        f"held {hlabel}: {k} must not contain {found} (it would render as a link or markup)"
                    )
        if isinstance(h["name"], str) and h["name"]:
            held_names.setdefault(h["name"].lower(), []).append(h["name"])
    for low, group in _grouped_dict(held_names):
        if len(group) > 1:
            add(f"duplicate held name (case-insensitive): {group}")
    for low in set(held_names) & set(names):
        add(f"name appears both listed and held: {held_names[low]} / {names[low]}")

    def walk(x, path):
        if isinstance(x, str):
            if "{{" in x or "}}" in x:
                add(f"'{{{{' / '}}}}' not allowed in data ({path}): {x[:60]!r}")
            if unsafe_chars(x):
                add(
                    f"control, invisible, unassigned or non-ASCII space character {unsafe_chars(x)} in data ({path}): {x[:60]!r}"
                )
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, f"{path}[{i}]")
        elif isinstance(x, dict):
            for k, v in x.items():
                walk(v, f"{path}.{k}")

    walk(data, "data")

    # anchors are per file now: the README's own headings, then each category page's
    pages = {"README.md": ["Contents", INDEX_SECTION] + list(TAIL_SECTIONS)}
    for c in cats:
        subs = set()
        if subheadings_on and isinstance(data["connectors"], list):
            subs = {
                e["subcategory"]
                for e in data["connectors"]
                if isinstance(e, dict)
                and e.get("category") == c
                and isinstance(e.get("subcategory"), str)
            }
        pages[category_path(c)] = [c] + sorted(subs)
    for page, titles in pages.items():
        slugs = {}
        for t in titles:
            slugs.setdefault(slugify(t), []).append(t)
        for slug, group in slugs.items():
            if len(group) > 1:
                add(f"headings collide on GitHub anchor #{slug} in {page}: {group}")
    paths = {}
    for c in cats:
        paths.setdefault(category_path(c), []).append(c)
    for path, group in paths.items():
        if len(group) > 1:
            add(f"categories collide on page {path}: {group}")

    tokens = Counter(re.findall(r"\{\{[^}]*\}\}", template))
    for t in tokens:
        if t not in KNOWN_TOKENS:
            add(f"template has unknown placeholder {t}")
    for t in STRUCTURAL_TOKENS:
        if tokens[t] != 1:
            add(f"template must contain {t} exactly once (found {tokens[t]})")
    for t in SIMPLE_TOKENS:
        if not tokens[t]:
            add(f"template missing placeholder {t}")

    return errors


def _grouped(items, key):
    groups = {}
    for it in items:
        groups.setdefault(key(it), []).append(it)
    return groups.items()


def _grouped_dict(groups):
    return groups.items()


def _fixture():
    """A small valid list built from the two allowlists, so the self-test never
    depends on what data/connectors.json holds today. The last entry is the probe."""
    plain = "Zz Plain"
    connectors = []

    def entry(name, category, **extra):
        connectors.append(
            {
                "name": name,
                "url": f"https://example.com/{len(connectors)}",
                "marker": None,
                "category": category,
                "description": "Does one thing.",
                "use_case": "Doing that one thing.",
                **extra,
            }
        )

    for cat, subs in SUBCATEGORIES.items():
        entry(f"Filed {len(connectors)}", cat, subcategory=subs[0])
    for name in sorted(ANTHROPIC_BUILT):
        entry(name, plain, marker="A")
    entry("Zz Probe", plain)
    data = {
        "meta": {
            "last_updated": "November 23, 2026",
            "capture_date": "2026-11-23",
            "render": {"category_counts": True, "subcategory_headings": True},
        },
        "categories": sorted(SUBCATEGORIES) + [plain],
        "connectors": connectors,
        "held": [
            {
                "name": "Zz Held",
                "catalog_description": "A held row.",
                "why_held": "No vendor page.",
            }
        ],
    }
    return data, " ".join(sorted(KNOWN_TOKENS))


def selftest():
    """A validator nobody has seen refuse an entry proves nothing. Plant one defect
    per rule and require that rule's own message, then plant what must stay legal."""
    if validate(*_fixture()):
        sys.exit("validator self-test failed -- its own clean fixture is refused")

    def probe(**fields):
        return lambda d: d["connectors"][-1].update(fields)

    def filed(sub):  # the first entry sits in a subcategorized category
        return lambda d: d["connectors"][0].update(subcategory=sub)

    def meta(key, value):
        return lambda d: d["meta"].update({key: value})

    def held(key, value):
        return lambda d: d["held"][0].update({key: value})

    def new_category(name):
        def plant(d):
            d["categories"].append(name)
            d["connectors"][-1]["category"] = name

        return plant

    def unmark(d):
        next(e for e in d["connectors"] if e["marker"] == "A")["marker"] = None

    def unlist(d):
        d["connectors"].remove(next(e for e in d["connectors"] if e["marker"] == "A"))

    link = "https://evil.example"
    cases = [
        (
            "a name carrying an HTML link",
            probe(name=f'Zz Probe <a href="{link}">Stripe</a>'),
            "name must not contain any of",
        ),
        (
            "a name carrying a code span",
            probe(name="Zz `Probe`"),
            "name must not contain any of",
        ),
        (
            "a name carrying a bare URL",
            probe(name=f"Zz {link}"),
            "name must not contain any of",
        ),
        (
            "a subcategory written as a link",
            filed(f"Zz]({link}) [more"),
            "is not a heading of",
        ),
        (
            "a subcategory nobody added to SUBCATEGORIES",
            filed("Brand New Heading"),
            "is not a heading of",
        ),
        (
            "a subcategory in a category that has none",
            probe(subcategory="Crypto and Web3"),
            "is not a heading of",
        ),
        (
            "a category name carrying a link",
            new_category(f"Zz [x]({link})"),
            "letters, digits and spaces only",
        ),
        (
            'marker "A" on a name outside ANTHROPIC_BUILT',
            probe(marker="A"),
            "disagrees with ANTHROPIC_BUILT",
        ),
        (
            'an ANTHROPIC_BUILT name without marker "A"',
            unmark,
            "disagrees with ANTHROPIC_BUILT",
        ),
        (
            "an ANTHROPIC_BUILT name that is not listed",
            unlist,
            "ANTHROPIC_BUILT names no listed entry",
        ),
        (
            "a description carrying an ftp link",
            probe(description="See ftp://evil.example/x."),
            "must not contain '://'",
        ),
        (
            "a use case carrying an email address",
            probe(use_case="Write to sales@evil.example."),
            "an email address",
        ),
        (
            "a held row carrying an email address",
            held("why_held", "Ask sales@evil.example."),
            "an email address",
        ),
        (
            "a URL host ending in a dot",
            probe(url="https://evil.example./x"),
            "empty label",
        ),
        (
            "a URL whose host is an IP address written in hex",
            probe(url="https://0x7f.0.0.1/x"),
            "host is not a domain name",
        ),
        (
            "a URL carrying a double quote",
            probe(url='https://example.com/"x'),
            "url must not contain any of",
        ),
        (
            "a URL carrying a backslash",
            probe(url="https://example.com/a\\b"),
            "url must not contain any of",
        ),
        (
            "a last-updated date carrying a link",
            meta("last_updated", f"[x]({link})"),
            "meta.last_updated must read like",
        ),
        (
            "a capture date carrying markup",
            meta("capture_date", "2026-11-23 <b>"),
            "meta.capture_date must read like",
        ),
        (
            "a description hiding a link's colon in a character reference",
            probe(description="See https&#58;//evil.example/login."),
            "a character reference",
        ),
        (
            "a description hiding www. behind a backslash",
            probe(description="See www\\.evil.example today."),
            "must not contain '\\\\'",
        ),
        (
            "a description with WWW. in capitals",
            probe(description="See WWW.evil.example today."),
            "must not contain 'www.'",
        ),
        (
            "a use case with an address whose host starts with a dot",
            probe(use_case="Write to a@.evil.example today."),
            "an email address",
        ),
        (
            "a name spelling a letter as a character reference",
            probe(name="Zz Prob&#101;"),
            "a character reference or a backslash escape",
        ),
        (
            "a name escaping a character with a backslash",
            probe(name="Zz\\&Probe"),
            "a character reference or a backslash escape",
        ),
        (
            "a name ending in a backslash, which would unhook its link",
            probe(name="Zz Probe\\"),
            "a character reference or a backslash escape",
        ),
        (
            "a URL carrying a character reference",
            probe(url="https://example.com/&#64;x"),
            "url must not contain a character reference",
        ),
        (
            "a URL carrying an opening parenthesis",
            probe(url="https://example.com/a(b"),
            "url must not contain any of",
        ),
    ]
    for cp, what in [
        (0x007F, "delete"),
        (0x0085, "next line"),
        (0x00A0, "no-break space"),
        (0x034F, "combining grapheme joiner"),
        (0x17B4, "Khmer inherent vowel"),
        (0x180B, "Mongolian variation selector"),
        (0x180F, "Mongolian variation selector four"),
        (0x200B, "zero-width space"),
        (0x202E, "right-to-left override"),
        (0x2028, "line separator"),
        (0x2029, "paragraph separator"),
        (0x2800, "braille blank"),
        (0x3164, "Hangul filler"),
        (0xFE0F, "variation selector 16"),
        (0xFFFE, "a noncharacter"),
        (0x16FE4, "Khitan filler"),
        (0x1D159, "null notehead"),
        (0xE0100, "variation selector 17"),
    ]:
        cases.append(
            (
                f"U+{cp:04X} ({what}) in a description",
                probe(description=f"Hidden{chr(cp)}character."),
                f"U+{cp:04X}",
            )
        )
    cases += [
        ("a name that starts with www.", probe(name="www.zz-probe.example"), None),
        ("a name with _ | ~ and \\", probe(name="Zz_probe | one ~ two \\ three"), None),
        ("a name in another script", probe(name="ずんだ ノート"), None),
        (
            "an @handle in a use case",
            probe(use_case="Following @handle mentions."),
            None,
        ),
        ("a description ending in 。", probe(description="日本語の説明。"), None),
        (
            "a name with & and ; that spell no reference",
            probe(name="Zz & Probe; one"),
            None,
        ),
        ("a price in a description", probe(description="Costs $5 a month."), None),
        ("R&D in a use case", probe(use_case="Planning R&D budgets; and more."), None),
    ]
    failed = 0
    for why, plant, want in cases:
        data, template = _fixture()
        plant(data)
        errors = validate(data, template)
        ok = not errors if want is None else any(want in e for e in errors)
        failed += not ok
        must = "accepted" if want is None else "refused"
        print(f"  {'ok  ' if ok else 'FAIL'} {why}: must be {must}")
        if not ok:
            print(f"       want {want!r}\n       got  {errors}")
    if failed:
        sys.exit("validator self-test failed -- do not trust this check")
    print("  self-test passed")


def main():
    if "--selftest" in sys.argv:
        selftest()
        return
    data = json.loads(DATA.read_text(encoding="utf-8"))
    template = TEMPLATE.read_text(encoding="utf-8")

    errors = validate(data, template)
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(f"{len(errors)} validation error(s) in data/connectors.json")

    by_cat = {c: [] for c in data["categories"]}
    for e in data["connectors"]:
        by_cat[e["category"]].append(e)

    subs = {
        "{{LAST_UPDATED}}": data["meta"]["last_updated"],
        "{{CAPTURE_DATE}}": data["meta"]["capture_date"],
        "{{LISTED}}": f"{len(data['connectors']):,}",
        "{{HELD}}": f"{len(data['held']):,}",
        "{{NCAT}}": str(len(data["categories"])),
        "{{TOC}}": render_toc(),
        "{{CATEGORY_INDEX}}": render_index(data, by_cat),
        "{{HELD_TABLE}}": render_held_table(data["held"]),
    }
    out = template
    for k, v in subs.items():
        out = out.replace(k, v)
    leftover = re.findall(r"\{\{[^}]*\}\}", out)
    if leftover:
        sys.exit(f"UNFILLED placeholders: {sorted(set(leftover))}")

    outputs = {README: out.encode("utf-8")}
    for cat in data["categories"]:
        outputs[REPO / category_path(cat)] = render_category_page(
            data, cat, by_cat[cat]
        ).encode("utf-8")

    oversize = [
        f"{p.relative_to(REPO)} ({len(b):,} bytes)"
        for p, b in outputs.items()
        if len(b) > RENDER_CEILING
    ]
    if oversize:
        sys.exit(
            f"OVER THE RENDER CEILING ({RENDER_CEILING:,} bytes; GitHub stops rendering at ~512 KB): "
            + ", ".join(oversize)
        )
    stray = sorted(
        str(p.relative_to(REPO))
        for p in (CATEGORIES_DIR.glob("*.md") if CATEGORIES_DIR.exists() else [])
        if p not in outputs
    )

    largest = max(outputs.items(), key=lambda kv: len(kv[1]))
    summary = (
        f"{len(data['connectors']):,} listed + {len(data['held'])} held | "
        f"{len(data['categories'])} categories | {len(outputs)} files, "
        f"README {len(outputs[README]):,} bytes, largest {largest[0].relative_to(REPO)} "
        f"{len(largest[1]):,} bytes"
    )
    if "--check" in sys.argv:
        stale = [
            str(p.relative_to(REPO))
            for p, b in outputs.items()
            if not p.exists() or p.read_bytes() != b
        ]
        if stale or stray:
            if stale:
                print(f"OUT OF DATE: {', '.join(stale)}", file=sys.stderr)
            if stray:
                print(
                    f"NOT GENERATED from the data (delete them): {', '.join(stray)}",
                    file=sys.stderr,
                )
            sys.exit(
                "edit data/connectors.json, then run: python3 scripts/generate_readme.py"
            )
        print(f"generated files match data/connectors.json — {summary}")
    else:
        CATEGORIES_DIR.mkdir(exist_ok=True)
        for p, b in outputs.items():
            p.write_bytes(b)
        print(f"wrote {len(outputs)} files — {summary}")
        if stray:
            sys.exit(
                f"NOT GENERATED from the data (delete them, then re-run --check): {', '.join(stray)}"
            )
    sup = suppressed_markers(data["connectors"])
    if sup:
        print(
            f"note: {len(sup)} marker(s) stored but render-suppressed "
            f"(description not uppercase-initial): {', '.join(sup)}"
        )


if __name__ == "__main__":
    main()
