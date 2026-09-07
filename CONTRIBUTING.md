# Contributing

This list tracks every connector in Anthropic's official Connectors Directory. Contributions welcome.

> This is an independent, community-maintained project. Not affiliated with, endorsed by, or sponsored by Anthropic PBC.

## How This Repo Works (Data-First)

`data/connectors.json` is the source of truth. `README.md` is generated from it -- don't hand-edit the README; CI rejects any README that doesn't match the data (`generated-in-sync` job).

To add or change an entry:

1. Edit `data/connectors.json` (add the entry object anywhere -- sorting is automatic).
2. Run `python3 scripts/generate_readme.py` (stdlib only, no dependencies).
3. Commit `data/connectors.json` and `README.md` together.

The generator validates the data before writing: duplicate names (case-insensitive), duplicate URLs, unknown categories, entry format, and terminal punctuation all fail loud with the offending entry named. `python3 scripts/generate_readme.py --check` runs the exact check CI runs.

## What You Can Contribute

### New Connectors
When Anthropic adds new connectors to the directory, submit a PR adding them to `data/connectors.json` with the appropriate category, a description, and a use case.

### Improved Descriptions
If a description or use case is missing detail or could be more helpful, submit a PR with a better one.

### Category Corrections
If a connector is in the wrong category, submit a PR moving it.

### Field Reports
Tested a connector and have real-world notes? Open an issue or PR with one paragraph on what worked, what didn't, what surprised you -- be specific. (The README is generated, so field reports land through the data file; the entry schema grows a field when the first report is accepted.)

## Guidelines

- One PR per change unless closely related.
- Keep descriptions concise -- one sentence for the description, one sentence for the use case.
- The use case is one sentence containing a concrete task or 2--3 comma-separated task fragments a user would actually perform in Claude (e.g. "Comparing carrier rates for a 40-lb package, buying a return label, checking where an order stalled in transit."). It must NOT restate the description -- it adds scenario information the description lacks. No vendor voice ("your"/"our"), no marketing adjectives, and every capability it implies must be stated in the description.
- Provenance markers: **`A`** only for entries whose canonical URL is Anthropic-owned (anthropic.com / github.com/anthropics) or whose catalog name self-identifies as Anthropic-built; **`C`** for entries carrying the in-app catalog's Community badge, applied from dated catalog captures (see docs/catalog-snapshots/).
- Don't add connectors that aren't in the official Anthropic directory. This list tracks the official directory, not all MCP servers (see [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) for that).
- Alphabetical order within categories is enforced by the generator -- add entries anywhere in `data/connectors.json`.

## Weekly Updates

This list is updated weekly to stay in sync with the official directory. If you notice the directory has added connectors that aren't listed here, please open an issue or PR.

### The two surfaces

Anthropic's catalog lives on two surfaces that don't fully overlap, and this list tracks the **union** of both:

- **Web directory** (claude.com/connectors) -- a curated subset, enumerable from `claude.com/sitemap.xml`. Exclude locale-prefixed duplicates when counting.
- **In-app catalog** (claude.ai -> Settings -> Connectors) -- the full set, including Community connectors and local desktop extensions that never appear on the web listing. Enumerable since September 2026 through Anthropic's directory feed (`api.anthropic.com/api/directory/servers`, one JSON call, tier + vendor URL per entry); `python3 scripts/feed_diff.py` diffs it and the sitemap against the data and the `feed-diff` workflow files that report as an issue every Friday. The feed's coverage against the app view is still being validated -- treat feed-absence as one surface, not both.

**Removal rule: only remove an entry when it is absent from _both_ surfaces.** Absence from one surface alone is expected and is not evidence of delisting. A removal batch was cancelled in July 2026 for exactly this reason, and three entries were removed in July 2026 only after failing the two-surface test.

Before removing, confirm the slug rather than trusting a 404 -- a wrong slug guess looks identical to a delisting. GitHub MCP (`/connectors/github`), Cortellis (`/connectors/cortellis-regulatory`), and Computer by DevRev (`/connectors/devrev`) have each been mistaken for removals this way.

### Naming

The two surfaces disagree on some display names (web directory: PitchBook, Oracle NetSuite, Monday; in-app: PitchBook Premium, NetSuite, monday.com). **This list follows the web directory's name where they differ.** Those are naming drift, not renames -- don't "fix" them, and don't add the in-app variant as a separate entry.

### Verification

Every entry needs a working vendor URL. A domain returning 200 is not proof of identity -- confirm the page content matches the connector before listing it. If a vendor can't be confirmed, hold the entry rather than shipping a guessed link.

### Held entries

Catalog entries whose vendor URL cannot be confirmed are published in the README's **Held for Verification** section -- name, catalog description, and the reason held, with no link -- rather than being listed with a guessed or generic link, and rather than being silently omitted. Presence in at least one catalog surface is still required.

If you are the vendor of a held entry, or you know its canonical product page, open an issue or PR with the URL. The entry graduates to its category section once the page content confirms the product. Never point a held entry at a generic directory page as a placeholder -- shared placeholder links fail lint (`double-link`) and tell the reader nothing.

### Connector Snap Stacks

Each sweep features a Connector Snap Stack in the README tip: a persona plus a small stack of connectors that click together, run through Claude Cowork or Claude Code. Composition rule: at least one connector new to the list and at least one proven one (the 2026-08-10 debut used four new entries; that is the exception, not the pattern). Stacks are archived in docs/stacks/; sweep statistics live in docs/CHANGELOG.md. A stack write-up must not assert outcomes that have not been field-tested -- mark untested stacks as composed, and upgrade them when a Field Report comes in.
