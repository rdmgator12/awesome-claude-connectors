# Changelog

Counting convention: **listed** = entries in category sections; **held** = rows in Held for Verification; **tracked** = listed + held. Sweep deltas are stated as the net change in listed entries; gross additions are called out separately where they differ (renames and variant merges make a naive name-diff overcount).

## 2026-09-14 — first feed-era sweep (1,629 → 2,562 listed; held 71 → 39)

The first sweep applied from the Friday feed-diff report ([#16](https://github.com/rdmgator12/awesome-claude-connectors/issues/16)), rebuilt against the live directory feed on the day: **2,645 servers** (anthropic 9 · partner 794 · community 1,842). The web sitemap doubled between 9/7 and 9/11 (405 → 806 slugs), all partner/anthropic tier — still no community entries on the web surface.

Count derivation:

- 1,629 listed at sweep open (1,627 on 9/7 + GoodBarber #15 + Brixa Studio #14, both merged 9/14)
- + 941 adds from 985 feed candidates: − 2 already listed by exact name (ラッコキーワード, 다나와 가격비교), − 4 naming-drift variants of listed entries (Streamline, PDF Tools, Paytm Payment Gateway, Milan Metro Status), − 6 sharing a listed entry's URL (Jotform Apps, four Windsor.ai variants), − 32 → Held
- − 8 delisted under the two-surface rule: Asteroid, Biomni Lab, Clockwise, DoorDash, GitHub MCP, GitLab, OpenArt Lite, Qlik (absent from the feed under any name or domain, from the sitemap, and their `claude.com/connectors/<slug>` pages 404 or redirect)
- = **2,562 listed + 39 held** (held: 71 − 62 graduated on their feed URLs + 30 new rows; 2 rows re-held with a fresh reason)

Held reasons this sweep: 14 feed URLs that are a profile/org or asset page rather than a product page, 15 entries sharing a vendor URL with another new entry (lint rejects duplicate links), 2 dead vendor URLs (Dango, NeetoRecord), 1 with no vendor URL (Pasteapp). 15 entries kept on their declared URL though unreachable from the sweep machine (noted UNVERIFIED in the sweep report).

Also this sweep: 250 provenance markers synced to the feed's verified tier (exact-name matches only: 202 gained `C`, 40 lost it on partner tier, 8 gained `A`); `feed_diff.py` tokenizer fix so names with no ASCII letters match themselves; 356 adds in the three subcategorized sections carry subcategories. Not applied, for review next sweep: 175 vendor-URL drift items, 94 non-exact name matches, 38 sitemap-only slugs. Snap Stack: [The one-person supply chain](stacks/2026-09-14-one-person-supply-chain.md).

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
