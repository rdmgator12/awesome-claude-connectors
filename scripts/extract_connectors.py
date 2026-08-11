#!/usr/bin/env python3
"""One-time README.md -> data/connectors.json extraction. Kept for provenance.

Markers are stored as-rendered: render-suppressed badges cannot be recovered from
the README and backfill in future catalog sweeps. Every entry line must round-trip
byte-identically through the generator's renderer before the JSON is written.
"""

import json
import re
import sys
from pathlib import Path

from generate_readme import render_entry, render_held_table

REPO = Path(__file__).resolve().parent.parent
README = REPO / "README.md"
DATA = REPO / "data" / "connectors.json"

ENTRY_RE = re.compile(
    r"^- \[(?P<name>.+?)\]\((?P<url>https://[^)]+)\)"
    r"(?P<mk> \*\*`(?P<mkl>[AC])`\*\*)?"
    r" - (?P<desc>.*?) \*Use case: (?P<uc>.*)\*$"
)
META_RE = re.compile(
    r"^\*\*Last updated:\*\* (?P<lu>.+?) \| "
    r"\*\*Connectors tracked:\*\* (?P<listed>[\d,]+) listed \+ (?P<held>[\d,]+) held \| "
    r"\*\*Categories:\*\* (?P<ncat>\d+)$"
)
CAPTURE_RE = re.compile(r"currently reflect the (\d{4}-\d{2}-\d{2}) catalog capture")
SKIP = {"Contents", "Held for Verification", "Related"}


def main():
    text = README.read_text(encoding="utf-8")
    lines = text.split("\n")

    meta_match = next((m for ln in lines[:30] if (m := META_RE.match(ln))), None)
    if not meta_match:
        sys.exit("meta line (**Last updated:** ...) not found in README head")
    capture_match = CAPTURE_RE.search(text)
    if not capture_match:
        sys.exit(
            'capture date ("currently reflect the YYYY-MM-DD catalog capture") not found'
        )

    categories, connectors, held_lines = [], [], []
    current, in_held = None, False
    for i, ln in enumerate(lines, 1):
        if ln.startswith("## "):
            title = ln[3:]
            in_held = title == "Held for Verification"
            current = None if title in SKIP else title
            if current:
                categories.append(current)
            continue
        if current:
            if not ln:
                continue
            m = ENTRY_RE.match(ln)
            if not m:
                sys.exit(f"line {i}: unparseable line in category {current!r}:\n{ln}")
            entry = {
                "name": m["name"],
                "url": m["url"],
                "marker": m["mkl"],
                "category": current,
                "description": m["desc"],
                "use_case": m["uc"],
            }
            rendered = render_entry(entry)
            if rendered != ln:
                sys.exit(
                    f"line {i}: round-trip mismatch:\n"
                    f"  original: {ln!r}\n  rendered: {rendered!r}"
                )
            connectors.append(entry)
        elif in_held and ln.startswith("|"):
            held_lines.append((i, ln))

    if len(held_lines) < 3:
        sys.exit("held table not found under ## Held for Verification")
    header = tuple(c.strip() for c in held_lines[0][1].split("|")[1:-1])
    if header != ("Connector", "Catalog description", "Why held"):
        sys.exit(f"unexpected held table header: {header}")
    held = []
    for i, ln in held_lines[2:]:
        cells = [c.strip() for c in ln.split("|")[1:-1]]
        if len(cells) != 3:
            sys.exit(f"line {i}: held row does not have exactly 3 cells:\n{ln}")
        held.append(
            {"name": cells[0], "catalog_description": cells[1], "why_held": cells[2]}
        )

    original_block = "\n".join(ln for _, ln in held_lines)
    rendered_block = render_held_table(held)
    if rendered_block != original_block:
        for orig, rend in zip(original_block.split("\n"), rendered_block.split("\n")):
            if orig != rend:
                sys.exit(
                    f"held table round-trip mismatch:\n  original: {orig!r}\n  rendered: {rend!r}"
                )
        sys.exit("held table round-trip mismatch (row count differs)")

    for cat in categories:
        names = [e["name"] for e in connectors if e["category"] == cat]
        if names != sorted(names, key=str.lower):
            sys.exit(f"category {cat!r} is not in str.lower() sort order")
    held_names = [h["name"] for h in held]
    if held_names != sorted(held_names, key=str.lower):
        sys.exit("held table is not in str.lower() sort order")

    stated = {
        "listed": int(meta_match["listed"].replace(",", "")),
        "held": int(meta_match["held"].replace(",", "")),
        "categories": int(meta_match["ncat"]),
    }
    parsed = {
        "listed": len(connectors),
        "held": len(held),
        "categories": len(categories),
    }
    if stated != parsed:
        sys.exit(f"count mismatch — README states {stated}, parsed {parsed}")

    data = {
        "meta": {
            "last_updated": meta_match["lu"],
            "capture_date": capture_match[1],
            "render": {"category_counts": False, "subcategory_headings": False},
        },
        "categories": categories,
        "connectors": connectors,
        "held": held,
    }
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"wrote {DATA.relative_to(REPO)} — {len(connectors):,} connectors, "
        f"{len(held)} held, {len(categories)} categories; all lines round-tripped"
    )


if __name__ == "__main__":
    main()
