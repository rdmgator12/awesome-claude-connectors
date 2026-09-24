# Awesome List for Claude Connectors [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Last Commit](https://img.shields.io/github/last-commit/rdmgator12/awesome-claude-connectors)](https://github.com/rdmgator12/awesome-claude-connectors/commits/main)

<p align="center">
  <img src="media/banner.svg" alt="Awesome Claude Connectors" width="800">
</p>

> A comprehensive directory of the connectors in Anthropic's [Claude Connectors catalog](https://www.anthropic.com/partners/mcp) — 2,562 MCP integrations across both catalog surfaces (the curated web directory and the in-app catalog, which additionally surfaces community-built and desktop-extension connectors), plus 39 held pending vendor verification, organized by category with descriptions and use cases.

**Last updated:** September 14, 2026 | **Connectors tracked:** 2,562 listed + 39 held | **Categories:** 30

Claude connectors are MCP (Model Context Protocol) servers that extend Claude with real-time access to external tools, data sources, and services. They work across Claude.ai, Claude Desktop, Claude Mobile, Claude Code, and Claude Cowork. Connectors in the **curated web directory** are vetted by Anthropic for security, reliability, and compatibility; the **in-app catalog** additionally surfaces community-built and local desktop-extension connectors that Anthropic makes available but does not itself build or vet. This list tracks the union of both surfaces — see CONTRIBUTING.md for the two-surface methodology.

For more information, see the [Connectors Documentation](https://claude.com/docs/connectors/directory), [Submission Guidelines](https://claude.com/docs/connectors/building/submission), and [MCP Protocol Specification](https://modelcontextprotocol.io).

Connectors marked with **`A`** are built and maintained by Anthropic. Connectors marked with **`C`** carry the in-app catalog's Community badge — published in the catalog by Anthropic but built by third parties and not vetted the way web-directory entries are. `C` markers currently reflect the 2026-09-14 catalog capture, taken from the directory feed's verified tier (community → `C`, partner → none) and re-synced every sweep.

This list is maintained weekly. To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

> This is an independent, community-maintained list. Not affiliated with, endorsed by, or sponsored by Anthropic PBC. "Claude" and related marks are the property of Anthropic PBC. Each connector is the property of its respective owner.

> [!TIP]
> ### Connector Snap Stack — September 14, 2026
>
> Each sweep features a persona and a small stack of connectors that click together. Past stacks are archived in [docs/stacks](docs/stacks/); sweep-by-sweep history lives in the [changelog](docs/CHANGELOG.md).
>
> **The one-person supply chain** — Terminal49 *(new)* · Stord *(new)* · LetMeShip Next *(new)* · PostCo *(new)* · running in **Claude Desktop**
>
> Tuesday, one Desktop conversation: ask Terminal49 which inbound containers are still sitting at the port and pull the event history behind the one that slipped, check Stord for stock at the facility about to run the promotion and which retailer missed on-time-in-full last week, price the pallet to Spain in LetMeShip with duties estimated before committing, then rank PostCo's return reasons by SKU and ask the question none of the four dashboards can answer alone — is the SKU we're about to reorder the one customers keep sending back. Four connectors that each see one leg of the chain, with Claude holding the whole route. Composed, not yet field-tested — if you run it against a live operation, send a Field Report (see CONTRIBUTING).

---

## Contents

- [Categories](#categories)
- [Held for Verification](#held-for-verification)
- [Related](#related)

---

## Categories

Each category has its own page; the list outgrew what GitHub will render as a single file.

| Category                                                                   | Connectors |
| -------------------------------------------------------------------------- | ---------- |
| [AI and ML](categories/ai-and-ml.md)                                       | 71         |
| [Automation and Integration](categories/automation-and-integration.md)     | 39         |
| [Calendar and Scheduling](categories/calendar-and-scheduling.md)           | 16         |
| [Cloud and Infrastructure](categories/cloud-and-infrastructure.md)         | 62         |
| [CMS and Web Building](categories/cms-and-web-building.md)                 | 61         |
| [Communication](categories/communication.md)                               | 66         |
| [Customer Support](categories/customer-support.md)                         | 44         |
| [Data and Analytics](categories/data-and-analytics.md)                     | 254        |
| [Design and Creative](categories/design-and-creative.md)                   | 93         |
| [Desktop Automation](categories/desktop-automation.md)                     | 14         |
| [Development Tools](categories/development-tools.md)                       | 117        |
| [Documents and Files](categories/documents-and-files.md)                   | 71         |
| [Education](categories/education.md)                                       | 33         |
| [Entertainment](categories/entertainment.md)                               | 24         |
| [Finance and Trading](categories/finance-and-trading.md)                   | 259        |
| [Government and Nonprofit](categories/government-and-nonprofit.md)         | 38         |
| [Healthcare and Life Sciences](categories/healthcare-and-life-sciences.md) | 61         |
| [Jobs](categories/jobs.md)                                                 | 35         |
| [Legal](categories/legal.md)                                               | 85         |
| [Lifestyle and Local](categories/lifestyle-and-local.md)                   | 95         |
| [Marketing and Sales](categories/marketing-and-sales.md)                   | 443        |
| [Observability and Monitoring](categories/observability-and-monitoring.md) | 29         |
| [Productivity](categories/productivity.md)                                 | 166        |
| [Project Management](categories/project-management.md)                     | 91         |
| [Research and Academic](categories/research-and-academic.md)               | 48         |
| [SAP](categories/sap.md)                                                   | 4          |
| [Security](categories/security.md)                                         | 69         |
| [SEO and Web](categories/seo-and-web.md)                                   | 74         |
| [Ticketing and Events](categories/ticketing-and-events.md)                 | 22         |
| [Travel](categories/travel.md)                                             | 78         |

## Held for Verification

Every link on the category pages has been checked against the live page — a URL ships only when the page content confirms the product. These catalog entries are real (each appears in the in-app connectors catalog) but no vendor URL could be confirmed for them yet, so they are listed here without a link rather than with a guessed or generic one. If you are the vendor, or know the canonical product page, open an issue or PR with the URL — the entry graduates to its category once the page confirms the product.

| Connector                                                           | Catalog description                                                                                                                                              | Why held                                                                                                                                        |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Adside — Meta Ads, Google Ads & LinkedIn Ads reporting for agencies | Ad performance, brand kits and competitor intelligence for Meta Ads, Google Ads and LinkedIn Ads — built for agencies managing many clients.                     | feed carries only a profile/org or asset page (app.adside.ai/logo_512.png), not a product page (2026-09-14)                                     |
| Agent Grid                                                          | Create, share, and evolve interactive artifacts with humans and AI agents.                                                                                       | agentgrid.sh exists but is a coding-agent canvas, not an interactive-artifact platform; no confident match.                                     |
| AI Dispatcher by FieldCamp                                          | AI dispatch and scheduling for field-service teams — view your jobs, technicians and board, run AI dispatch, and accept assignments, right from Claude.          | shares vendor URL fieldcamp.ai with "FieldCamp" (list lint rejects duplicate links); needs its own product page (2026-09-14)                    |
| Airmail                                                             | Manage emails, calendars, contacts, and more from Claude using Airmail's MCP server.                                                                             | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| Commerce Layer Metrics                                              | Commerce Layer Metrics MCP server                                                                                                                                | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| Dango                                                               | Build beautiful presentations, in your own brand.                                                                                                                | vendor URL trydango.com returned HTTP 530 on 2026-09-14                                                                                         |
| Decision Matrix                                                     | Decision Matrix helps Claude run structured, criteria‑based evaluations so teams can make and defend complex decisions with confidence.                          | generic term; search returns the decision-matrix method, not a vendor product page.                                                             |
| Denodo MCP Connector                                                | Connect Claude Desktop to a Denodo Virtual DataPort database via MCP                                                                                             | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| doDomain                                                            | Connect customer domains from chat                                                                                                                               | shares vendor URL devino.ca with "BioFlow" (list lint rejects duplicate links); needs its own product page (2026-09-14)                         |
| droplinked                                                          | Discover and verify products across droplinked's KYB-attested merchant network. Read-only agentic-commerce discovery.                                            | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| Fieldy                                                              | Search and recall your Fieldy conversations directly in Claude.                                                                                                  | feed carries only a profile/org or asset page (a LinkedIn personal profile), not a product page (2026-09-14)                                    |
| Firefox Control                                                     | Control Mozilla Firefox: tabs, history and web content (privacy aware)                                                                                           | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| FlitIQ — FMCSA Carrier Intelligence                                 | Look up U.S. motor carriers, check CSA safety scores, verify insurance, and save carriers to your FlitIQ pipeline — all inside Claude. Requires a FlitIQ Pro or  | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| GetItDone                                                           | Run your team's tasks and workspaces from chat                                                                                                                   | shares vendor URL devino.ca with "BioFlow" (list lint rejects duplicate links); needs its own product page (2026-09-14)                         |
| Hiver in Gmail                                                      | Find, manage, and analyze customer conversations                                                                                                                 | shares vendor URL hiverhq.com with "Hiver Omni" (list lint rejects duplicate links); needs its own product page (2026-09-14)                    |
| HtAG Spatial                                                        | HtAG Spatial gives Claude H3-indexed access to Australia’s property market, price/rent, socio-environmental and geography-concordance layers, so spatial questio | shares vendor URL htag.com.au with "HtAG Documentation" (list lint rejects duplicate links); needs its own product page (2026-09-14)            |
| hvacbuilder.app                                                     | Design, solve and simulate HVAC systems with real physics                                                                                                        | feed carries only a profile/org or asset page (a LinkedIn personal profile), not a product page (2026-09-14)                                    |
| Inbin Pulse                                                         | Is this flight price actually a deal? Grounded answers from observed fare history, not vibes.                                                                    | shares vendor URL inbin.dev with "Inbin" (list lint rejects duplicate links); needs its own product page (2026-09-14)                           |
| Memco Shared Memory                                                 | Shared memory for all your agents                                                                                                                                | shares vendor URL memco.ai with "Memco Personal Memory" (list lint rejects duplicate links); needs its own product page (2026-09-14)            |
| Mercado Libre Inmuebles                                             | Encontrar tu propiedad ideal                                                                                                                                     | Product page exists per country (.com.ar / .com.mx / .com.co /c/inmuebles); connector's country not specified.                                  |
| Milan Metro Status                                                  | Real-time Milan Metro Status                                                                                                                                     | no vendor page found; only official ATM Milano transit site, which is not this connector.                                                       |
| MindMap                                                             | Turn AI insights into interactive mind maps.                                                                                                                     | Several same-named projects; no confident match.                                                                                                |
| miniOrange MCP for WordPress                                        | Securely Manage Your WordPress from Claude                                                                                                                       | shares vendor URL miniorange.com with "miniOrange MCP for Magento" (list lint rejects duplicate links); needs its own product page (2026-09-14) |
| Minutes Conversation Memory                                         | The private, owned conversation-memory layer for AI. Record, transcribe, and search every meeting, voice memo, and dictation entirely on your own machine — noth | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| NeetoDesk                                                           | Triage tickets, draft replies, manage customers and agents, and pull support reports in your NeetoDesk workspace.                                                | shares vendor URL neeto.com with "NeetoCal" (list lint rejects duplicate links); needs its own product page (2026-09-14)                        |
| NeetoForm                                                           | Search your forms, read the answers people submitted, and manage who can access them in your NeetoForm workspace.                                                | shares vendor URL neeto.com with "NeetoCal" (list lint rejects duplicate links); needs its own product page (2026-09-14)                        |
| NeetoRecord                                                         | Connect your NeetoRecord workspace to search recordings by speech or title, read transcripts, capture video frames, and manage folders and sharing.              | vendor URL neeto.com/neetorecord returned HTTP 404 on 2026-09-14                                                                                |
| origami.publica.la                                                  | Origami is publica.la's publishing toolchain                                                                                                                     | shares vendor URL publica.la with "EbooksDepository" (list lint rejects duplicate links); needs its own product page (2026-09-14)               |
| Pasteapp                                                            | Local MCP server bridge for Paste — give Claude Desktop, Claude Code, Cursor, Codex, and other AI tools access to your Mac clipboard history and pinboards.      | feed carries no vendor URL (2026-09-14)                                                                                                         |
| PopHIVE Public Health Data                                          | Access near real-time public health data from PopHIVE dashboards including immunizations, respiratory diseases, chronic conditions, hospital capacity, injury/ov | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| Reddit MCP Buddy                                                    | Browse Reddit directly in Claude Desktop. Search posts, analyze users, explore communities - no API keys needed.                                                 | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| SiD Corp MCP                                                        | An product from SiD Corp to connect with MCP                                                                                                                     | vendor-level match only; unrelated same-named firm exists — downgraded at merge.                                                                |
| Sinch Build Docs                                                    | Search Sinch Build developer docs and API references.                                                                                                            | shares vendor URL sinch.com with "Mailgun Docs MCP" (list lint rejects duplicate links); needs its own product page (2026-09-14)                |
| Structured Reflection                                               | Structured Reflection helps Claude debug ideas and decisions by talking through them step by step, just like a classic developer rubber‑d…                       | generic name; no vendor page identified, only unrelated open-source reflection/rubber-duck MCPs.                                                |
| Things (AppleScript)                                                | Claude Desktop Extension for Things, the award-winning personal task manager                                                                                     | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |
| Uptimely                                                            | Monitor uptime, incidents, and on-call from AI                                                                                                                   | shares vendor URL devino.ca with "BioFlow" (list lint rejects duplicate links); needs its own product page (2026-09-14)                         |
| Vid Kraken                                                          | Cut audio or video clips from your own long-form videos by timestamp — podcasts, lectures, streams — and get a file ready for your editor.                       | shares vendor URL omnivision.solutions with "Transcript LOL" (list lint rejects duplicate links); needs its own product page (2026-09-14)       |
| Voxtell Phone                                                       | Your business phone system, answered from Claude                                                                                                                 | shares vendor URL voxtell.com with "Voxtell Chat" (list lint rejects duplicate links); needs its own product page (2026-09-14)                  |
| Website Auditor                                                     | AI visibility and site audits: see whether ChatGPT, Perplexity, Claude, and Gemini recommend a website.                                                          | feed carries only a profile/org or asset page (a GitHub profile or org page), not a product page (2026-09-14)                                   |

## Related

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Model Context Protocol servers powering many of the connectors above.
- [awesome-chatgpt-apps](https://github.com/rdmgator12/awesome-chatgpt-apps) - Companion list cataloging apps in the ChatGPT directory.
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - LLM-powered applications across providers.

---

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Ralph Martello](https://github.com/rdmgator12) has waived all copyright and related or neighboring rights to this work.
