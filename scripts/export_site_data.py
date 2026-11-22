#!/usr/bin/env python3
"""data/connectors.json -> site-data/, the website's read-only feed.

Usage:
    python3 scripts/export_site_data.py           # write site-data/
    python3 scripts/export_site_data.py --check   # CI: fail if site-data/ is stale

Why a separate export: data/connectors.json is about 6 MB and shaped for the
README generator. A browser wants small files it can fetch lazily and a
stable id per entry for its URLs. This script derives both from the same data,
so the site can never disagree with the list: same entries, same text, same
order. Stdlib only. Output is deterministic (no timestamps beyond the data's own
dates), so --check is a byte comparison.

Layout (schema_version 1):
    site-data/index.json               meta, categories with counts and file names
    site-data/search.json              id, name, category slug and marker per listed entry
                                       (search by name here; full text lives in the category files)
    site-data/categories/<slug>.json   full entries of one category
    site-data/held.json                Held for Verification rows

Entry ids are slugs of the entry name ("Google Drive" -> "google-drive"). Names
are unique case-insensitively, but slugging drops punctuation and accents, so two
names can share a slug ("PDF Viewer" / "pdf-viewer", "Agora" / "Ágora"). Those
get a hand-picked id in ID_OVERRIDES, and any new collision fails loud rather
than being numbered, so an id never silently changes meaning. A renamed entry
gets a new id.

Schema changes add fields and never repurpose one; a breaking change bumps
schema_version. Fields planned, not yet in the data: auth (sign-in required or
not, from the feed) and per-tool permission flags (read-only, destructive).
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "connectors.json"
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


def slug(text):
    """ASCII slug; non-Latin names keep their letters (URLs allow them)."""
    t = unicodedata.normalize("NFKD", text)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = re.sub(r"[^\w]+", "-", t, flags=re.UNICODE).strip("-_")
    return re.sub(r"[-_]+", "-", t)


def entry_id(name):
    return ID_OVERRIDES.get(name) or slug(name) or "entry"


def build(data):
    cats = data["categories"]
    cat_slugs = {c: slug(c) for c in cats}
    if len(set(cat_slugs.values())) != len(cats):
        raise SystemExit("category slugs collide")

    ids = {}
    for e in data["connectors"]:
        i = entry_id(e["name"])
        if i in ids:
            raise SystemExit(f"entry id collision {i!r}: {ids[i]!r} and {e['name']!r}")
        ids[i] = e["name"]

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
    files["index.json"] = {
        "schema_version": SCHEMA_VERSION,
        "last_updated": data["meta"]["last_updated"],
        "capture_date": data["meta"]["capture_date"],
        "listed": len(data["connectors"]),
        "held": len(held),
        "markers": MARKERS,
        "categories": index_cats,
        "files": {"search": "search.json", "held": "held.json"},
    }
    return {
        p: json.dumps(v, ensure_ascii=False, separators=(",", ":")) + "\n"
        for p, v in files.items()
    }


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    want = build(data)
    have = {
        str(p.relative_to(OUT)): p.read_text(encoding="utf-8")
        for p in OUT.rglob("*.json")
    } if OUT.exists() else {}
    if "--check" in sys.argv:
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
