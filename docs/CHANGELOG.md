# Changelog

Counting convention: **listed** = entries in category sections; **held** = rows in Held for Verification; **tracked** = listed + held. Sweep deltas are stated as the net change in listed entries; gross additions are called out separately where they differ (renames and variant merges make a naive name-diff overcount).

## 2026-09-24 — per-category pages, and the second feed-era sweep (2,562 → 2,982 listed; held 39 → 27)

**The README went dark past 512 KB.** The 9/14 sweep took the single-file README to 764,327 bytes; GitHub stops rendering a markdown file at about 512 KB, so the page cut off mid-entry inside Marketing and Sales and roughly 800 entries — Observability through Travel, plus the Held table and Related — were invisible on GitHub for ten days. Entries now live on one generated page per category under `categories/`; the README is the front page and category index. The generator fails any page over 500,000 bytes, and a new CI step runs awesome-lint's entry rules over every category page.

**The web directory moved.** claude.com now serves connector pages at `/marketplace/connectors/<slug>` (old `/connectors/` paths redirect). `feed_diff.py` matched zero sitemap slugs and would have reported 34 removal candidates, 32 of them web-only entries; it now accepts both paths (835 slugs) and fails loud on zero.

Feed on the day: **3,088 servers** (anthropic 9 · partner 824 · community 2,255).

Count derivation:

- 2,562 listed at sweep open
- + 421 adds from 444 feed entries not on the list: − 7 sharing a listed entry's URL (five Windsor.ai variants, Jotform Apps, Bigin by Zoho CRM) − 7 variants (Orgvue US/AP/EU and Clara Mexico/Colombia/Brazil each merged into one entry; PopHIVE Public Health Data, PDF Tools and Streamline Icons, Illustrations, Emojis are naming drift of listed entries) − 2 not added (Paytm Payment Gateway, per the 9/14 ruling; Minutes Conversation Memory, handled as a rename) − 7 → Held
- − 1 delisted under the two-surface rule: Links Connect (absent from the feed under any name or domain, from the sitemap, and its marketplace slug 404s)
- = **2,982 listed + 27 held** (held: 39 − 13 graduated − 2 folded into listed entries + 3 new; 4 re-held with a fresh reason)

Also this sweep: "Minutes — Meeting Memory for AI" renamed to the catalog's "Minutes Conversation Memory" and moved from minutes.me (a parked domain) to its product site. Five feed vendor URLs pointed at a developer portfolio, a parent company, an agency or an unrelated firm rather than the product (TryMermaid, Deley, Embarko, Screens.icu, Mappenings) and were replaced with the product's own verified domain; twelve profile, LinkedIn or image-asset feed URLs were resolved through the feed's documentation link. 10 provenance markers synced to the feed tier (exact-name matches only); Consensus, Clarity AI and Trellis were left as they are because each matches two feed records with different tiers, and the Anthropic-built PDF Viewer, Word and PowerPoint keep `A` though the feed lists them as partner tier. Not applied, for review next sweep (feed diff re-run after the merge): 191 vendor-URL drift items, 136 non-exact name matches, 40 sitemap-only slugs, 5 `C` markers suggested by loose matches. The re-run's candidate adds are exactly the 11 known non-adds above, and its one removal candidate is the Streamline rename. Snap Stack: [The small-firm litigator's Monday](stacks/2026-09-24-small-firm-litigator.md).

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
