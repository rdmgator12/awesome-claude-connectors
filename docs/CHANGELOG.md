# Changelog

Counting convention: **listed** = entries in category sections; **held** = rows in Held for Verification; **tracked** = listed + held. Sweep deltas are stated as the net change in listed entries; gross additions are called out separately where they differ (renames and variant merges make a naive name-diff overcount).

## 2026-10-30 — sixth feed-era sweep (6,368 → 8,045 listed; held 51 → 57)

**The 10/23 feed-diff run failed instead of filing a report.** The directory feed grew while `feed_diff.py` was paging through it (7,097 servers returned against a reported `total` of 7,087), and the count check added on 10/19 failed loud as designed, so no issue was filed that week. `load_feed()` now refetches the whole feed once when the paged count disagrees with `total` and still fails if the second fetch disagrees; offline files still fail on the first mismatch. This sweep was built against the full feed captured at sweep time: **8,292 servers** (anthropic 10, community 7,251, partner 1,031) and a **1,045-slug** web sitemap.

Count derivation:

- 6,368 listed + 51 held at sweep open
- + 2 contributor PRs, landed with the contributor as commit author: Hanging Context (#38), TraderWAI Charts (#40) = 6,370. A third, #41, re-pointed alexandria. to alexandria.place (no count change)
- − 1 two-surface removal: Ryanair (absent from all 8,292 feed servers and the sitemap; its slug page `/marketplace/connectors/ryanair` returns 404) = 6,369
- + 1,674 adds from 1,683 candidates: 1,717 feed entries match nothing on the list, − 18 that match held rows, − 14 in the known non-add set, − 2 known same-vendor siblings that share a listed entry's URL (Jotform App Builder, D&B Digital Audiences); 8 of the 1,683 → Held, and 1 withheld (a compliance-audit connector whose catalog name trips this repository's pre-commit PHI check; verified and written, it lands once that is resolved)
- + 2 graduated from Held: DealFinder (now at gocottontail.com) and The 07:00 Brief (now at 0700.io), each with its own page
- = **8,045 listed + 57 held**

**Vendor URLs.** Every candidate URL was fetched and checked under the strict rule (the page's title, site name or heading must carry a distinctive part of the *product's* own name). 1,426 matched on the feed's declared URL. 182 more were confirmed on the product's own page, found from the feed's documentation link or MCP host. The last 75 (bot walls, sites unreachable from the sweep machine, developer or agency homepages) went through a second fetch channel: 60 kept, 14 re-pointed, 1 held. Candidates sharing a vendor URL with each other or with a listed entry (30) were checked for a page of their own: 16 re-pointed to one, 7 kept, 7 held. Eleven were resolved by hand after reading the pages. A post-merge audit of the new links found none to an MCP directory or a social profile; the two on a big-platform domain are the vendor's own product page (Claude Academy on Anthropic's academy.claude.com, LinkedIn Hiring Pro on LinkedIn's business site). Two repository links were moved to the products' own sites (Bugasura → bugasura.io, Panderr → panderr.com).

**Security screen** over all 1,683 candidates, the five 10/8 checks; 52 flags, none held. 31 lookalike-domain hits were distinct real products. 14 brand names in a connector name were honest third-party integrations (Google, Telegram, Discord, LinkedIn, Shopify, X, QuickBooks and Xero, YouTube, Amazon Seller Central, and three connectors naming Claude itself). Four government-styled hits are a bond Q&A library, a rent-data tool built on government statistics, a government-procurement search and a directory of government fax numbers, and none presents itself as a government. Three agent-directed phrases are ordinary tool-routing, feature or safety language (one tells the assistant never to send because an email asks it to).

**Entry text.** Written in eighteen batches from each connector's feed description and MCP tool names only, then checked by the validator. A full fidelity pass reviewed all 1,683 drafts against their source and changed 174. An adversarial check on a seeded sample of 60 reviewed entries then found 7 rule breaches (1 misleading, 6 minor), three of them one pattern: the catalog claims a write action that the connector's tool list does not include, and the entry repeated the catalog. All 7 were fixed; a mechanical scan of every entry for write verbs with no matching tool flagged 142, of which 3 were real and fixed (the rest were nouns, negations, or tools named in another language), and 3 more entries were narrowed where the catalog gates an action behind a setting or plan. In total 187 entries (11.1%) changed after drafting. Where a catalog claims an action and the tool list does not include it, the entry now follows the tools.

Held this sweep (8): Candour APP (the vendor homepage names neither connector and the app's documentation page returns 404) and Beauty & Wellness Biz Grader (no page names it), for which no page confirms the product; Enzo Notes, Spekboom Host, Form Backend, Klisten Cross Border, Klisten EntityResolver and Vivasites Marketing, which share a vendor URL with a listed sibling and have no page of their own.

Markers: 14 synced to the feed tier, all losing `C` on partner tier (AUTONOMAD, Sent, docsend.com, Aptus.AI - NextOS, CoinGecko, Jump, ClickFunnels, Cube Software, Sequence, Addgene, Optilogic, Promptless, Print.com, Backstory). Word and PowerPoint keep `A`.

Fixes beyond the adds: link check #39 — 235 of its 248 errors were TLS handshake failures on every page from productivity.md onward, a runner artifact (10 of 10 sampled sites were live); AIReady re-pointed to ai-ready.magicteams.ai (its GitHub repository returns 404). TryMermaid and CashSheet, carried from 10/19, both answer 200 and stay listed. Recall (500), Openpath (404), IndexLinks (503) and InflueXpert (timeout) were still failing on a direct fetch at sweep close; they stay listed and will be held if the next link check agrees. Hanging Context's entry from #38 got a fidelity fix against its catalog text. `name_url_check.py` gained one verified near-miss pair: LeadBot AI at leadbotapp.com (site title 'LeadBot AI — Chatbot that books appointments').

Page size: the Marketing and Sales page is now 477,644 bytes against the generator's 500,000-byte cap, about 56 entries of headroom; it needs splitting before the next sweep adds to it.

Not applied, for review: 599 vendor-URL drift items, 279 non-exact name matches, 68 sitemap slugs matching no list name, 33 web-only entries, 30 marker rows. The post-sweep diff's candidate adds are the known non-adds plus Very Simple Notes, Very Simple Projects, Jotform App Builder and D&B Digital Audiences; its removal candidates are PageHub, Bansaj and Streamline, as before. Snap Stack: [The back-room gig night](stacks/2026-10-30-back-room-gig-night.md).

## 2026-10-19 — fifth feed-era sweep (4,675 → 6,368 listed; held 43 → 51)

**The 10/9 and 10/16 feed-diff reports were truncated.** The directory feed passed the 5,000-row page limit around 10/9, and `feed_diff.py` read only the first page, so [#31](https://github.com/rdmgator12/awesome-claude-connectors/issues/31) and [#33](https://github.com/rdmgator12/awesome-claude-connectors/issues/33) undercounted (3,761 feed entries matched on 10/16 against 4,783 the week before). `load_feed()` now follows `next_cursor` and fails loud when the server count disagrees with the feed's `total`. This sweep was built against the full feed captured at sweep time: **6,562 servers** (anthropic 9 · partner 963 · community 5,590; 974 web-sitemap slugs).

Count derivation:

- 4,675 listed + 43 held at sweep open
- + 2 contributor PRs, landed with the contributor as commit author: qrlia (#34), Equibles (#35) = 4,677
- − 1 held in the link-check fixes for #32/#36: Autonoma (every page on its domain returns 404, in link checks a week apart) = 4,676 listed + 44 held
- + 1,692 adds from 1,705 feed entries not on the list (after the known non-add set, 13 names that match held rows, and Jotform App Builder and D&B Digital Audiences, which share a listed entry's URL): − 2 known variants (Very Simple Notes and Very Simple Projects, the earlier names of Pinpal Notes and Pinpal Projects) − 4 regional or edition variants folded into one entry (V7 Go EU/US → V7 Go; Xakia United States/United Kingdom/Australia → Xakia; PRINTOOLS docs into PRINTOOLS) − 7 → Held
- = **6,368 listed + 51 held**

**Vendor URLs.** Every candidate URL was fetched and checked under the strict rule from the 10/8 correction pass: the page's title, site name or heading must carry a distinctive part of the *product's* own name, never only the vendor's. 1,423 matched on the feed's declared URL. 210 more were confirmed on the product's own page, found from the feed's documentation link or MCP host (129 of them at the product's own root). The last 72 (bot walls, sites unreachable from the sweep machine, developer or agency homepages, catalog names that differ from the site's brand) went through a second fetch channel: 52 kept their declared URL, 17 were re-pointed to the product's page, 2 were held and 1 folded as a variant. Four redirects were followed to the product's current domain: Chiostro Legal Ai, Vacamp, Sigil Brand Agency, and Code actu (now Meilleur Code Parrainage, which lists "Codeactu" as an alternate name). A review of 63 matches that rested only on dictionary words moved Fred Goals off a developer's personal site to its product site. Sixteen same-vendor groups (57 connectors) shared one URL: 36 were given their own verified product pages, 3 folded as variants, 2 held, and one connector per group keeps the shared URL.

**Security screen** over all 1,705 candidates and both PRs, the five 10/8 checks; 36 flags, none held. Brand names in a connector name were honest third-party integrations (WhatsApp Business, Facebook and Google Ads, a Medicare fee-schedule lookup, a CMS "for Claude"). Lookalike domains were all distinct real products. One Atlassian Forge app runs on Atlassian's own MCP hosting. Seven government-styled hits are procurement, disclosure or council-records data tools, and none presents itself as a government. The one agent-directed phrase ("paste the system prompt") refers to the user's own voice agent.

**Entry text.** Written in twenty batches from each connector's feed description and MCP tool names only, checked by a validator proven first against planted defects. Mid-sweep the validator was found to reject the country abbreviation "US" as a pronoun, which led some writers to blur or drop geography; it was fixed, and the fidelity pass put the source's place names back. A full fidelity pass then reviewed all 1,698 drafts against their source and changed 234 (13.8%). Most changes restored geography, made the description state a capability its use case relied on, or narrowed write verbs to the tools that exist ("deletes" became "trashes" where the catalog says deletion goes to the trash). Where a server's tool list held only meta tools (whoami, version, a generic call or query), which some servers expose before sign-in, the entry was rewritten from the catalog text. A final adversarial read of a seeded sample (60 entries, three per batch) found 6 breaches and no invented capability, number, place or platform: 1 borderline misleading (MailVakt's "inbox tests" now reads "email-receipt tests (not inbox-versus-spam placement)"), 3 use cases relying on a capability the description didn't name, and 2 wording nits. All six are fixed. Projected from the sample, roughly 5% of new entries may still have a use case that shows a capability the description leaves unnamed; those under-describe rather than over-claim and were not chased entry by entry.

Held this sweep (8): Autonoma; Global Travel Planner, DealFinder, Then & There (그때그곳) — Business Cards & Meeting Log, and EnergyInCloud, for which no page confirms the product; The 07:00 Brief, Lexplorer Workbench and Torgix Equipment Tools, which share a vendor URL with a listed sibling and have no page of their own. The 13 held rows whose names are in the feed were rechecked and none graduates: shared vendor URLs are still shared, Dango still returns Cloudflare 530, Aster Share 402, CSME has no DNS record, and the GTACityRP site still presents itself as a state government.

Markers: 9 synced to the feed tier, all losing `C` on partner tier (Yelp, Evernote, komoot, Blaze SQL, Rippit, Shop, Richpanel AI, WeTransfer, AfterShip Post-Purchase; every matched feed record agrees). Left as they are: 23 entries whose matched records sit at two tiers. PDF Viewer, Word and PowerPoint keep `A`.

Fixes beyond the adds: link checks #32 and #36 — Spendify re-pointed to spendify.money (the vendor moved domains; the feed agrees), Autonoma held, and saturation.io and www.vinilogy.com added to `.lycheeignore` (HTTP/2 negotiation failures from the runner, both sites live). CashSheet (Cloudflare 530) and TryMermaid (502) were still failing at sweep close after a single link-check report; they stay listed and will be held if the next check agrees. The other #32/#36 hits were transient. `name_url_check.py` gained six verified near-miss pairs, each confirmed by reading the site: Glo Invoie is the catalog's misspelling of Glo Invoice, and SecureSMTP, Clerq MCP, Dýrabær, LinkDrop and StrategyX are the vendors' own domains.

Not applied, for review: 467 vendor-URL drift items (grown by this sweep's re-points), 223 non-exact name matches, 56 sitemap slugs matching no list name, 32 web-only entries, 26 marker rows. The post-sweep diff's candidate adds are the known non-adds plus Very Simple Notes, Very Simple Projects, Jotform App Builder and D&B Digital Audiences; its removal candidates are PageHub, Bansaj and Streamline, as before. Snap Stack: [The kitchen-table bills night](stacks/2026-10-19-kitchen-table-bills-night.md).

One verified add landed in a follow-up commit: its catalog name is name-shaped beside an SSN label and tripped the maintainer's pre-commit PHI check until an exact-string exception was added for it.

## 2026-10-08 (later) — vendor-URL correction pass (4,678 → 4,675 listed; held 42 → 43)

An audit of the sweep's new links found no link to an Anthropic, Claude or MCP-directory page and none to a social profile, but it did find that the sweep's content check had accepted a page naming the *vendor* as a match for the *product*. About ninety new entries pointed at the developer's personal site, a development agency, or a parent company's homepage rather than the product. Rechecked with a stricter rule (the page title, site name or heading must carry a distinctive part of the product's own name), using the feed's documentation link and MCP host as the source for product pages:

- 92 vendor URLs re-pointed to the product's own verified page (for example My Flohmarkt from a consultancy's homepage to my-flohmarkt.de, Knighn from a developer's personal site to knighn.com, Carillon from a fractional-CTO site to carillon.dev, The Economist - Graphs and IDC Quanta from the publisher's homepage to the connector's page). Four followed redirects to the product's current domain: LinkyCal (now GoodInbound, "formerly LinkyCal"), OpenAlex (from its parent nonprofit), IANS and TecPass Communities.
- 1 held: Prativedan (the only working page is the developer's personal site; the product's own pages return 404).
- 2 folded as variants: Very Simple Notes and Very Simple Projects are the same vendor's earlier names for Pinpal Notes and Pinpal Projects (their domains now redirect there); they join the known non-add set (15).
- About thirty weak matches were kept on their URL after review because the URL already is the product's own site: the name appears only in another script (Korean, Japanese, Arabic, Hebrew), the title is a tagline (Icons8, AI2SQL, Namecheap), or a bot wall answers the sweep machine while a second channel confirmed the page.

The feed-diff's vendor-URL drift section grows by these re-points; that is expected, since the feed's author URL is the developer's page in each case.

## 2026-10-08 — fourth feed-era sweep, from feed-diff #27 (3,044 → 4,678 listed; held 26 → 42)

The largest sweep in the list's history. Worked from the Friday feed-diff report ([#27](https://github.com/rdmgator12/awesome-claude-connectors/issues/27), filed at 799 candidates) and rebuilt against the live directory feed captured at sweep time: **4,830 servers** (anthropic 9 · partner 909 · community 3,912; 922 web-sitemap slugs). The feed grew by 1,677 servers in the thirteen days since the 9/25 sweep, 855 of the candidates carrying an October `added_at`.

Count derivation:

- 3,044 listed + 26 held at sweep open
- + 4 contributor PRs, landed with the contributor as commit author: PostWire (#25), PlayDrop (#26), Aitho (#28), Shipvela (#30) = 3,048
- − 1 re-held in the link-check fixes for #24/#29: Dango (Cloudflare 530 since 9/28) = 3,047 listed + 27 held
- + 1,633 adds from 1,660 feed entries not on the list: − 11 known non-adds (five Windsor.ai variants, Bigin by Zoho CRM, Jotform Apps, PDF Tools, Streamline Icons, Illustrations, Emojis, Paytm Payment Gateway, PopHIVE Public Health Data) − 1 variant (Colaunched (public), folded into Colaunched) − 15 → Held
- − 2 delisted under the two-surface rule: Arkon Vault and Links Connect (absent from the feed under any name or domain and from the sitemap; their marketplace slugs 404). Links Connect is a repeat: delisted 9/24, back in the feed 9/25, gone again by 10/8.
- = **4,678 listed + 42 held**

**Vendor URLs.** Every vendor URL was fetched and its page title, site name or description checked for the product's or the vendor's name (too loose, see the correction pass above: a vendor-name match let developer, agency and parent-company homepages through): 1,529 matched on content from the sweep machine, and 84 more (bot walls, sites unreachable from the sweep machine's network, or pages where only the domain carried the name) were content-checked through a second fetch channel. Twenty-two feed URLs pointed at a developer's site (two of them dead), an agency, a parent company or a LinkedIn, Instagram, YouTube or GitHub profile rather than the product and were replaced with the product's own page (The Founding Reader, DebtStack, AALY, Nabled, Finito, Trains.fyi, Pakistan Case Law, Concertje, mcp.creatoros.ca, Internet Tools, Thavorn.asia, Yemen-Jobs, Gradient Builder, A-Char, Front-End Checklist, LivePage, CampVantage, Arihaan Jobs, Notiero, CV_builder, MCP & Skills Finder, SkedCast). Four malformed feed URLs (a scheme or host pasted twice, a missing dot) were repaired (mcp.holicay.com, Invent, PageHub, Yungle), and eight http-only URLs moved to https. Forty-eight same-vendor connectors that share one feed URL were given their own verified product pages (Good Turn Studio's fifteen apps, Lukka's five data products, Pinpal's three apps, among others); where no product page exists, one connector keeps the shared URL and the rest are held. Yuna is kept on its declared URL, UNVERIFIED: the domain is live but a bot wall answered both fetch channels.

**Entry text.** Written in twenty batches from each connector's feed description and MCP tool names only, then checked three ways: a mechanical lint (categories and subcategories, voice, punctuation, leading product name; proven against six planted defects), an adversarial read of a seeded random sample (60 entries, three per batch: no invented numbers, platforms or integrations, but ten breaches of the letter of the rules, three of them misleading), and, because one overstated description in 60 projects to dozens across the sweep, a full fidelity pass over all 1,633 entries against the feed text. That pass changed 256 entries (186 descriptions, 81 use cases), mostly use cases that implied a capability the description did not state, and verbs such as "updates" applied to more objects than the connector's write tools cover.

**Security screen.** New this sweep, run over all 1,660 candidates and the four PRs before any entry was written: brand names in a connector name (all eight hits were honest third-party integrations, such as "Checklist for Jira" and "Revenue Analytics for HubSpot"), lookalike domains within two edits of a major brand's (eighteen hits, all distinct real products), MCP endpoints on a big-brand domain the vendor does not own (four: three Atlassian Forge apps on Atlassian's own MCP hosting and one AWS API Gateway, all legitimate), government-styled sites on non-government domains (one real hit, held), and agent-directed text in the feed descriptions (four connectors carry ordinary tool-routing language, such as "use this whenever someone asks what is happening in crypto"; none overrides safety or impersonates anyone, they list normally, and no entry here repeats the instruction). The four PR diffs were checked for hidden characters, extra links and non-data files: none.

Held this sweep (15): Code de loi - GTACityRP (its site presents itself as the government of the State of Tennessee on a non-government domain; held under the impersonation screen), Academic report builder (404), FocusPulse (no content to either fetch channel), Task Ninja (the feed URL is an unrelated retailer and the product domain serves no readable content), Windowbox (http-only, no address record), and ten same-vendor connectors that share a URL with a listed sibling and have no page of their own (four ResumeNext tools, Domain & Redirect Checker, Events for Organisers, Table12 Manager, Roraima holiday rentals, ConstruChain Tracker, Rush SR Lap Analyzer). Still held: Aster Share (HTTP 402), CSME Developer Build Compliance and Content Filter (no DNS record), pensieve-notes and Virtualna Pisarna - By REWORQ (unchanged URLs).

Fixes beyond the adds: Superscout Platform moved off a subdomain that no longer resolves to its live product page; FRED added to `.lycheeignore` (HTTP/2 negotiation failure from the runner, site live). Two catalog names are malformed in the feed and are listed under the product's own name: `https://pagehub.dev/api/mcp` as PageHub and `app.bansaj.pitam.com.npBansaj` as Bansaj. Both will show as candidate adds and removal candidates in every feed diff until the feed is corrected; they join the known non-add set. Sgewise keeps the catalog's spelling (the vendor is Segwise) and is recorded in `name_url_check.py` with Better Angles and C8 FX Hedge, whose domains legitimately differ from their names. Aitho's and Shipvela's contributed descriptions were moved into the list's third-person voice.

Markers: 26 synced to the feed tier, all losing `C` on partner tier (Chariot, Upwork, Constant Contact and 23 more; exact-name matches whose every matched feed record agrees). Left as they are: Airwallex, Lindo AI, Clarity AI, Consensus, Aurora and Trellis (matched feed records at two tiers), and the Anthropic-built PDF Viewer, Word and PowerPoint keep `A`.

Not applied, for review: 243 vendor-URL drift items, 181 non-exact name matches, 49 sitemap slugs matching no list name, 32 web-only entries, 24 marker rows (split-tier records, loose or domain matches, and the three Anthropic-built entries). The post-sweep diff's candidate adds are the 11 known non-adds plus PageHub and Bansaj; its removal candidates are Streamline (the known rename), PageHub and Bansaj. Snap Stack: [The medical-bill and appeal night](stacks/2026-10-08-medical-bill-and-appeal-night.md).

Also on 10/8: link checks #24 and #29 closed (FRED ignored, Dango re-held, Superscout re-pointed; tooluniverse.org and voris.ai were transient).

## 2026-09-25 — third feed-era sweep, from feed-diff #21 (2,980 → 3,044 listed; held 29 → 26)

Worked from the Friday feed-diff report ([#21](https://github.com/rdmgator12/awesome-claude-connectors/issues/21)) and rebuilt against the live directory feed at sweep time: **3,153 servers** (anthropic 9 · partner 831 · community 2,313). The report was filed at 3,140; 11 more candidates landed before the sweep ran.

Count derivation:

- 2,980 listed at sweep open (after the 9/25 link fixes)
- + 58 adds from 72 feed entries not on the list: − 11 known non-adds (five Windsor.ai variants, Bigin by Zoho CRM and Jotform Apps share a listed entry's URL; PDF Tools, Streamline Icons, Illustrations, Emojis and PopHIVE Public Health Data are naming drift of listed entries; Paytm Payment Gateway, as before) − 3 → Held
- + 6 graduated from Held on verified product pages: 1Stay, Community Pulse, Dango, Denodo MCP Connector, droplinked, Pasteapp
- = **3,044 listed + 26 held** (held: 29 − 6 graduated + 3 new)

Links Connect is back: delisted on 9/24 under the two-surface rule, it has reappeared in the feed and returns with its 9/24 text. Six feed vendor URLs pointed at a developer, a parent company or an agency rather than the product, and were replaced with the product's own page after a content check (Iminify, HELEN by ELIKA, comethru, Pics.io, FALCON Verify, EDINET DB). Every vendor URL was content-checked through a second fetch channel, not the sweep machine's network.

Held this sweep: Virtualna Pisarna - By REWORQ (the feed URL is the agency's homepage and no product page exists), pensieve-notes (the feed URL is the developer's personal site), Capi Agent (shares its URL with Capi Agent for Merchants, whose product that page is). Still held: Aster Share (HTTP 402 on every page) and CSME Developer Build Compliance and Content Filter (its domain has no DNS record).

Markers: 3 synced to the feed tier (Expensify, Spara and Ubersuggest lose `C` on partner tier). The other marker rows in the report either already agree on an exact-name match or have a name the feed carries at two tiers; PDF Viewer, Word and PowerPoint keep `A`.

Not applied, for review: 190 vendor-URL drift items, 139 non-exact name matches, 45 sitemap slugs matching no list name, 31 web-only entries. The one removal candidate, Streamline: Icons, Illustrations and Elements, is the listed name of the product the feed calls Streamline Icons, Illustrations, Emojis, so it is not a removal.

Also on 9/25: link checks #20 and #22 closed with no link rot (elixion.ai and valossa.com ignored as bot-armored; lychee timeout 20 s → 30 s).

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
