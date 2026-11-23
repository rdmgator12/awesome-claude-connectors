#!/usr/bin/env python3
"""One-time git history -> data/changes.json backfill. Kept for provenance.

data/changes.json is the record of when each entry id joined or left the listed
set. scripts/export_site_data.py reads it for the site feed's first-seen dates
and keeps it current from here on; this script only rebuilt the past, from the
history of the two files that have held the catalog:

    README.md             2026-04-13 to 2026-08-10 (hand-edited entry lines)
    data/connectors.json  since 2026-08-11

Method. Every commit that touched either file is replayed oldest first. An
entry's date is the commit's own calendar date (the committer date as recorded,
which is the maintainer's day for every commit to date and agrees with the
dated headings in docs/CHANGELOG.md). Changes are netted per date, so an entry
held and restored the same day leaves no trace, and one that joined and left
within a single day is dated from its later return. A name that changes while its
URL stays the same is a rename: the entry keeps its first date under the new
id. A rename that also changed the URL cannot be told from a removal plus an
addition and is recorded as one. An id that leaves and later returns keeps its
first date. Ids are computed with today's id rule, the only one the site has
ever seen.

Needs the full history (not a shallow clone). Refuses to overwrite an existing
data/changes.json: after the first run the file is maintained by the export
and may carry hand corrections.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

from export_site_data import CHANGES, entry_id, replay

REPO = Path(__file__).resolve().parent.parent
ENTRY = re.compile(r"^- \[(?P<name>.+?)\]\((?P<url>https?://[^)]+)\)")
NOT_CATALOG = {
    "Contents",
    "Held for Verification",
    "Related",
    "Contributing",
    "License",
}


def git(*args, check=True):
    return subprocess.run(
        ["git", "-C", str(REPO), *args], capture_output=True, text=True, check=check
    )


def listed_at(commit):
    """{id: url} of the listed entries at one commit."""
    shown = git("show", f"{commit}:data/connectors.json", check=False)
    if shown.returncode == 0:
        pairs = [(e["name"], e["url"]) for e in json.loads(shown.stdout)["connectors"]]
    else:
        pairs, section = [], None
        for line in git("show", f"{commit}:README.md").stdout.split("\n"):
            if line.startswith("## "):
                title = line[3:].strip()
                section = None if title in NOT_CATALOG else title
            elif section and (m := ENTRY.match(line)):
                pairs.append((m["name"], m["url"]))
    ids = {}
    for name, url in pairs:
        i = entry_id(name)
        if i in ids and ids[i] != url:
            sys.exit(f"{commit[:7]}: two entries share the id {i!r}")
        ids[i] = url
    return ids


def main():
    if CHANGES.exists():
        sys.exit(f"{CHANGES.relative_to(REPO)} exists; this backfill runs once")
    if git("rev-parse", "--is-shallow-repository").stdout.strip() == "true":
        sys.exit("shallow clone: the backfill needs the full history")
    log = git(
        "log",
        "--first-parent",
        "--reverse",
        "--format=%H %cs",
        "--",
        "README.md",
        "data/connectors.json",
    ).stdout.split("\n")
    commits = [line.split() for line in log if line]

    # A token follows one entry through its renames; an id that returns takes
    # its old token back.
    live, urls, gone, first = {}, {}, {}, {}
    born = set()  # tokens created on the date being walked
    days = []  # [date, {token: id} at the end of that date]
    for commit, date in commits:
        if days and days[-1][0] != date:
            # An entry that joined and left within one day leaves no trace.
            for i in [i for i, token in gone.items() if token in born]:
                del gone[i]
            born.clear()
        ids = listed_at(commit)
        added = sorted(set(ids) - set(live))
        removed = set(live) - set(ids)
        by_url = {urls[i]: i for i in removed}
        for i in added:
            old = by_url.pop(ids[i], None)
            if old is not None:
                live[i] = live.pop(old)
                removed.discard(old)
            elif i in gone:
                live[i] = gone.pop(i)
            else:
                live[i] = len(first)
                first[live[i]] = date
                born.add(live[i])
        for i in removed:
            gone[i] = live.pop(i)
        urls = ids
        snapshot = {token: i for i, token in live.items()}
        if days and days[-1][0] == date:
            days[-1][1] = snapshot
        else:
            days.append([date, snapshot])

    changes, before = [], {}
    for date, after in days:
        change = {
            "date": date,
            "added": sorted(i for t, i in after.items() if t not in before),
            "removed": sorted(i for t, i in before.items() if t not in after),
            "renamed": sorted(
                (
                    {"from": before[t], "to": i}
                    for t, i in after.items()
                    if t in before and before[t] != i
                ),
                key=lambda r: r["from"],
            ),
        }
        if change["added"] or change["removed"] or change["renamed"]:
            changes.append(change)
        before = after

    # The export's own reader must agree with the walk above, or the file is wrong.
    replayed = replay(changes)
    walked = {i: first[token] for i, token in live.items()}
    if replayed != walked:
        sys.exit("replay of the built log disagrees with the history walk")
    data = json.loads((REPO / "data" / "connectors.json").read_text(encoding="utf-8"))
    now = {entry_id(e["name"]) for e in data["connectors"]}
    if set(replayed) != now:
        sys.exit("the built log does not end at today's listed entries")

    doc = {
        "_comment": (
            "When each entry id joined or left the listed set. Dates before "
            f"{commits[-1][1]} were rebuilt from git history by "
            "scripts/backfill_changes.py; scripts/export_site_data.py appends "
            "from there. 'removed' means no longer listed (delisted, or moved "
            "to Held). A renamed entry keeps its first date. Safe to correct by "
            "hand: the export checks it against data/connectors.json."
        ),
        "changes": changes,
    }
    CHANGES.write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"wrote {CHANGES.relative_to(REPO)} from {len(commits)} commits: "
        f"{len(changes)} dated changes, {len(now):,} ids listed today, "
        f"{sum(len(c['renamed']) for c in changes)} renames, "
        f"first {changes[0]['date']}, last {changes[-1]['date']}"
    )


if __name__ == "__main__":
    main()
