#!/usr/bin/env python3
"""Flag listings whose URL looks like a misspelling of their own name.

Usage:
    python3 scripts/name_url_check.py              # report to stdout, exit 1 if anything is flagged
    python3 scripts/name_url_check.py --selftest   # prove the detector on known cases, then report
    python3 scripts/name_url_check.py --quiet      # exit code only

Why this exists: the link checker can only catch a wrong URL when the wrong URL
happens to be DEAD. BirdSift was listed at birsift.com (missing the "d" from its
own name) and was caught on 2026-09-15 only because that domain has no DNS
record (issue #17). Had the misspelling landed on a live domain -- a parking
page, a squatter, or an unrelated company -- it would have passed every check in
this repo and shipped indefinitely. Kinetik, in the same sweep, is correctly
listed at kineto.app while kinetik.com is a natural gas midstream operator on
the NYSE; "correcting" the domain to match the name would have been the bug.

So this is a REPORT, never an autofix. Each hit needs a human to open the site
and read it. Stdlib only. Exit 0 when clean, 1 when something is flagged.

The signal: name and domain root that are near-identical but where NEITHER
contains the other. Containment is what separates a typo from a brand
convention -- "recall" is inside "recallai" (Recall.ai), "datadog" is inside
"datadoghq" (Datadog), but "birsift" and "birdsift" contain neither.
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "connectors.json"

MIN_LEN = 5        # below this, edit distance is meaningless
MAX_DIST = 2       # a typo is one or two characters; more is a different brand

# Pairs a human has opened and read. A near-miss that is NOT a typo belongs here
# with the evidence, so the check fails only on something new. Verified 2026-09-15.
VERIFIED = {
    ("Kinetik", "kineto.app"):
        "site says 'Kinetik' and matches the listing; kinetik.com is Kinetik Holdings (NYSE: KNTK), a gas midstream operator",
    ("Attribution MCP", "www.attributionapp.com"):
        "vendor brand is Attribution, domain adds 'app'; 'MCP' is the connector suffix, not part of the company name",
    ("BusyCal", "www.busymac.com"):
        "BusyMac is the company, BusyCal the product; the path /busycal is the product page",
    ("Pace AI", "www.pacehq.ai"):
        "vendor brand is Pace, domain adds 'hq'",
    ("Plan@Job", "planajob.com"):
        "site title is 'Plan@Job | The AI CRM for contractors'; the domain spells the '@' as 'a'",
    ("NoveLand", "novel-land.com"):
        "site title is 'トップページ | NoveLand' (a Japanese novel platform); the domain hyphenates the brand",
}


def norm(s: str) -> str:
    """Lowercase, strip accents and every non-alphanumeric character."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def lev(a: str, b: str) -> int:
    """Levenshtein distance, iterative two-row."""
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def domain_root(host: str) -> str:
    """Registrable-ish label: drop www., the TLD, and any leading subdomains."""
    host = re.sub(r"^www\.", "", host)
    return host.rsplit(".", 1)[0].split(".")[-1]


def suspicious(name: str, host: str):
    """Return the edit distance if this pair looks like a typo, else None."""
    n, r = norm(name), norm(domain_root(host))
    if len(n) < MIN_LEN or len(r) < MIN_LEN:
        return None
    if n in r or r in n:
        return None                      # brand + suffix, not a misspelling
    d = lev(n, r)
    return d if 0 < d <= MAX_DIST else None


def selftest() -> None:
    """A detector nobody has seen fail proves nothing. Break it on known cases."""
    cases = [
        ("BirdSift", "www.birsift.com", 1, "the real typo, from issue #17"),
        ("Recall.ai", "recall.ai", None, "brand repeating its own TLD"),
        ("Datadog", "www.datadoghq.com", None, "brand + hq"),
        ("Kinetik", "kineto.app", 2, "genuine near-miss that is NOT a typo -- needs a human"),
        ("Square", "squareup.com", None, "brand + up"),
    ]
    for name, host, want, why in cases:
        got = suspicious(name, host)
        status = "ok " if got == want else "FAIL"
        print(f"  {status} {name:12s} {host:22s} want={want} got={got}   ({why})")
        if got != want:
            sys.exit("detector self-test failed -- do not trust this run")
    print("  self-test passed\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--selftest", action="store_true", help="run the detector self-test first")
    ap.add_argument("--quiet", action="store_true", help="exit code only, no report")
    args = ap.parse_args()

    if args.selftest:
        selftest()

    data = json.loads(DATA.read_text())
    items = data if isinstance(data, list) else data.get("connectors", data.get("items", []))

    hits = []
    for c in items:
        m = re.match(r"https?://([^/]+)", c.get("url") or "")
        if not m:
            continue
        host = m.group(1)
        d = suspicious(c.get("name", ""), host)
        if not d:
            continue
        note = VERIFIED.get((c.get("name"), host))
        hits.append((d, c.get("name"), c.get("url"), note))
    hits.sort(key=lambda h: (h[3] is not None, h[0], h[1]))
    new_hits = [h for h in hits if h[3] is None]

    if not args.quiet:
        print(f"scanned {len(items)} listings -- typo-shaped pairs: {len(hits)} "
              f"({len(new_hits)} unverified, {len(hits) - len(new_hits)} previously verified)")
        for d, name, url, note in hits:
            if note is None:
                print(f"  NEW    d={d}  {name:34s} {url}")
        for d, name, url, note in hits:
            if note is not None:
                print(f"  ok     d={d}  {name:34s} {url}\n           verified: {note}")
        if new_hits:
            print("\nEach hit needs a human to open the site and read it. A near-miss is not")
            print("proof of a typo: Kinetik is correctly at kineto.app, and kinetik.com is an")
            print("unrelated NYSE-listed pipeline company.")
    return 1 if new_hits else 0


if __name__ == "__main__":
    sys.exit(main())
