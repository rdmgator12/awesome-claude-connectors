# Changelog

Counting convention: **listed** = entries in category sections; **held** = rows in Held for Verification; **tracked** = listed + held. Sweep deltas are stated as the net change in listed entries; gross additions are called out separately where they differ (renames and variant merges make a naive name-diff overcount).

## 2026-08-10 — catalog-doubling catch-up sweep (841 → 1,625 listed; held 19 → 72)

The largest sweep in the list's history. The in-app catalog measured **1,691 unique entries** — the first untruncated export (snapshot: [docs/catalog-snapshots/in-app-2026-08-10](catalog-snapshots/in-app-2026-08-10/)) — while the curated web directory sat unchanged at 405 slugs. Likely accelerant: the [MCP 2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) moved the protocol to a stateless request/response core, letting a connector run as a serverless request handler. Of the 847 catalog additions, **281 carry the catalog's `New` badge**; the remainder were live earlier but invisible below the 2026-07-23 export's truncation point.

Count derivation:

- 841 listed (2026-07-23)
- − 3 delisted under the two-surface rule: Klarity, macOS, Mnemoverse Memory (the latter two carried as candidates since 7/23)
- + 790 verified additions (847 unique catalog additions − 53 unverifiable → Held − 4 same-product variant pairs merged: Fospha regions, Badger Maps tiers, CE Cosmos products, Articulate EU)
- − 1 pre-existing variant folded (Massive Market Data desktop extension → Massive)
- = 1,627 at sweep close
- Post-sweep QA: DNS Inspector demoted to Held (vendor match inferred, page fetch 400); Harness MCP Server folded into Harness (variant rule); dot. graduated from Held (vendor page confirmed) — its Held row removed
- = **1,625 listed + 72 held** (held: 19 + 53 + 1 − 1)

Also this sweep: eight catalog renames tracked (Harness.io → Harness, Jus Mundi → Jus AI by Jus Mundi (Light Mode), Channel3 MCP → Channel3 Shopping, LogRocket MCP → LogRocket, Nuvemshop-mcp → Nuvemshop, GuruWalk → GuruWalk – Tours & Activities, Agentic Presentations by SlidesGPT → SlidesGPT, Perseus Vault suffix drop). Every added URL search-verified, then liveness-checked (756× HTTP 200; bot-walled domains confirmed alive via DNS-over-HTTPS). PR #4 (PodPast) closed under the two-surface gate. Connector of the Week retired in favor of the Connector Snap Stack ([docs/stacks](stacks/)).

## 2026-07-30

- dot. added to Held for Verification (7/2 in-app sighting; getdot.ai ruled out). Graduated 2026-08-10 after leaveadot.com confirmed.

## 2026-07-23 — +106 (735 → 841 listed)

Official tier moved in volume (ElevenLabs, v0, Railway, AngelList) alongside ~100 Community additions. BlueConic re-added after its 7/15 removal — the two-surface rule cuts both ways. Seven in-app renames tracked (Mozilla MDN → MDN, CData → CData Connect AI, Tableau MCP Server → Tableau, among others). Held for Verification section created — 18 entries published transparently rather than shipped with guessed links. COTW: Anthropic Economic Index.

## 2026-07-15

First-ever removals under the newly codified two-surface rule: Outlook (folded into Microsoft 365), BlueConic, protocols.io. Two-surface methodology written into CONTRIBUTING.
