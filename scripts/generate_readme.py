#!/usr/bin/env python3
"""Emit README.md and categories/<slug>.md from data/connectors.json — the single source of truth.

Usage:
    python3 scripts/generate_readme.py          # regenerate README.md + category pages
    python3 scripts/generate_readme.py --check  # verify every generated file matches the data (CI)

README.md is the front page (intro, Snap Stack, category index, held table); each
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
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "connectors.json"
TEMPLATE = REPO / "README.template.md"
README = REPO / "README.md"
CATEGORIES_DIR = REPO / "categories"

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
        for k in ("last_updated", "capture_date"):
            if not isinstance(meta[k], str) or not meta[k].strip():
                add(f"meta.{k} must be a non-empty string")
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
        else:
            names.setdefault(name.lower(), []).append(name)
        url = e.get("url")
        if not isinstance(url, str) or not url.startswith("https://"):
            add(f"{label}: url must start with https://")
        elif ")" in url or " " in url or "\n" in url or "\r" in url:
            add(f"{label}: url must not contain ')', spaces, or newlines")
        else:
            urls.setdefault(url, []).append(label)
        if e.get("marker") not in ("A", "C", None):
            add(
                f"{label}: marker must be \"A\", \"C\", or null, got {e.get('marker')!r}"
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

    for low, group in _grouped_dict(names):
        if len(group) > 1:
            add(f"duplicate connector name (case-insensitive): {group}")
    for url, group in urls.items():
        if len(group) > 1:
            add(f"duplicate URL {url}: {group}")

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


def main():
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
