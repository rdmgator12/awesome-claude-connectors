# Awesome List for Claude Connectors [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Last Commit](https://img.shields.io/github/last-commit/rdmgator12/awesome-claude-connectors)](https://github.com/rdmgator12/awesome-claude-connectors/commits/main)

<p align="center">
  <img src="media/banner.svg" alt="Awesome Claude Connectors" width="800">
</p>

> A comprehensive directory of the connectors in Anthropic's [Claude Connectors catalog](https://www.anthropic.com/partners/mcp) — 2,980 MCP integrations across both catalog surfaces (the curated web directory and the in-app catalog, which additionally surfaces community-built and desktop-extension connectors), plus 29 held pending vendor verification, organized by category with descriptions and use cases.

**Last updated:** September 25, 2026 | **Connectors tracked:** 2,980 listed + 29 held | **Categories:** 30

Claude connectors are MCP (Model Context Protocol) servers that extend Claude with real-time access to external tools, data sources, and services. They work across Claude.ai, Claude Desktop, Claude Mobile, Claude Code, and Claude Cowork. Connectors in the **curated web directory** are vetted by Anthropic for security, reliability, and compatibility; the **in-app catalog** additionally surfaces community-built and local desktop-extension connectors that Anthropic makes available but does not itself build or vet. This list tracks the union of both surfaces — see CONTRIBUTING.md for the two-surface methodology.

For more information, see the [Connectors Documentation](https://claude.com/docs/connectors/directory), [Submission Guidelines](https://claude.com/docs/connectors/building/submission), and [MCP Protocol Specification](https://modelcontextprotocol.io).

Connectors marked with **`A`** are built and maintained by Anthropic. Connectors marked with **`C`** carry the in-app catalog's Community badge — published in the catalog by Anthropic but built by third parties and not vetted the way web-directory entries are. `C` markers currently reflect the 2026-09-24 catalog capture, taken from the directory feed's verified tier (community → `C`, partner → none) and re-synced every sweep.

This list is maintained weekly. To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

> This is an independent, community-maintained list. Not affiliated with, endorsed by, or sponsored by Anthropic PBC. "Claude" and related marks are the property of Anthropic PBC. Each connector is the property of its respective owner.

> [!TIP]
> ### Connector Snap Stack — September 24, 2026
>
> Each sweep features a persona and a small stack of connectors that click together. Past stacks are archived in [docs/stacks](docs/stacks/); sweep-by-sweep history lives in the [changelog](docs/CHANGELOG.md).
>
> **The small-firm litigator's Monday** — Case Status *(new)* · lawdiver.com *(new)* · PointOne *(new)* · CourtListener · running in **Claude Desktop**
>
> Monday, one Desktop conversation: ask Case Status which matters have overdue tasks and which clients are waiting on a reply, pull the opinion and docket behind the ruling a client is asking about from CourtListener, run the draft opposition's citations through lawdiver to confirm each case is still good law, send the client a plain-language update through Case Status, then log the morning to the right matters in PointOne with each entry checked against that client's billing guidelines before it goes out. Four connectors that each hold one piece of the practice — the client file, the public record, the citator, the timesheet — with Claude carrying the matter across all four. Composed, not yet field-tested — if you run it against a live practice, send a Field Report (see CONTRIBUTING).

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
| [AI and ML](categories/ai-and-ml.md)                                       | 78         |
| [Automation and Integration](categories/automation-and-integration.md)     | 48         |
| [Calendar and Scheduling](categories/calendar-and-scheduling.md)           | 21         |
| [Cloud and Infrastructure](categories/cloud-and-infrastructure.md)         | 70         |
| [CMS and Web Building](categories/cms-and-web-building.md)                 | 69         |
| [Communication](categories/communication.md)                               | 77         |
| [Customer Support](categories/customer-support.md)                         | 55         |
| [Data and Analytics](categories/data-and-analytics.md)                     | 313        |
| [Design and Creative](categories/design-and-creative.md)                   | 101        |
| [Desktop Automation](categories/desktop-automation.md)                     | 15         |
| [Development Tools](categories/development-tools.md)                       | 133        |
| [Documents and Files](categories/documents-and-files.md)                   | 77         |
| [Education](categories/education.md)                                       | 42         |
| [Entertainment](categories/entertainment.md)                               | 30         |
| [Finance and Trading](categories/finance-and-trading.md)                   | 314        |
| [Government and Nonprofit](categories/government-and-nonprofit.md)         | 43         |
| [Healthcare and Life Sciences](categories/healthcare-and-life-sciences.md) | 65         |
| [Jobs](categories/jobs.md)                                                 | 38         |
| [Legal](categories/legal.md)                                               | 105        |
| [Lifestyle and Local](categories/lifestyle-and-local.md)                   | 122        |
| [Marketing and Sales](categories/marketing-and-sales.md)                   | 503        |
| [Observability and Monitoring](categories/observability-and-monitoring.md) | 34         |
| [Productivity](categories/productivity.md)                                 | 191        |
| [Project Management](categories/project-management.md)                     | 104        |
| [Research and Academic](categories/research-and-academic.md)               | 51         |
| [SAP](categories/sap.md)                                                   | 4          |
| [Security](categories/security.md)                                         | 77         |
| [SEO and Web](categories/seo-and-web.md)                                   | 81         |
| [Ticketing and Events](categories/ticketing-and-events.md)                 | 28         |
| [Travel](categories/travel.md)                                             | 91         |

## Held for Verification

Every link on the category pages has been checked against the live page — a URL ships only when the page content confirms the product. These catalog entries are real (each appears in the in-app connectors catalog) but no vendor URL could be confirmed for them yet, so they are listed here without a link rather than with a guessed or generic one. If you are the vendor, or know the canonical product page, open an issue or PR with the URL — the entry graduates to its category once the page confirms the product.

| Connector                                          | Catalog description                                                                                                                                              | Why held                                                                                                                                           |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1Stay                                              | Live worldwide hotel search, loyalty points eligible rates. Book with secure checkout, get the hotel's own confirmation number, pay at the hotel.                | the feed's vendor page (Stayker) never names 1Stay, so the vendor match is unconfirmed (2026-09-24)                                                |
| Agent Grid                                         | Create, share, and evolve interactive artifacts with humans and AI agents.                                                                                       | agentgrid.sh exists but is a coding-agent canvas, not an interactive-artifact platform; no confident match.                                        |
| AI Dispatcher by FieldCamp                         | AI dispatch and scheduling for field-service teams — view your jobs, technicians and board, run AI dispatch, and accept assignments, right from Claude.          | shares vendor URL fieldcamp.ai with "FieldCamp" (list lint rejects duplicate links); needs its own product page (2026-09-14)                       |
| Aster Share                                        | Create in Claude. Publish with Aster.                                                                                                                            | the vendor site returns a hosting error on every page (deployment disabled, HTTP 402) (2026-09-25)                                                 |
| Community Pulse                                    | Ask a question, get New Zealand's real numbers — Community Pulse by Data n Dashboards                                                                            | vendor site returns a server error (2026-09-24)                                                                                                    |
| CSME Developer Build Compliance and Content Filter | Check what you build against the law before it ships.                                                                                                            | the feed URL is a misspelled, unregistered domain and the product has no page of its own apart from the one CSME Content Creator uses (2026-09-24) |
| Dango                                              | Build beautiful presentations, in your own brand.                                                                                                                | vendor site still returns an origin error (Cloudflare 530), as on 2026-09-14 (2026-09-24)                                                          |
| Decision Matrix                                    | Decision Matrix helps Claude run structured, criteria‑based evaluations so teams can make and defend complex decisions with confidence.                          | generic term; search returns the decision-matrix method, not a vendor product page.                                                                |
| Denodo MCP Connector                               | Connect Claude Desktop to a Denodo Virtual DataPort database via MCP                                                                                             | feed URL is a GitHub profile/org page, not a product page (2026-09-24)                                                                             |
| doDomain                                           | Connect customer domains from chat                                                                                                                               | shares vendor URL devino.ca with "BioFlow" (list lint rejects duplicate links); needs its own product page (2026-09-14)                            |
| droplinked                                         | Discover and verify products across droplinked's KYB-attested merchant network. Read-only agentic-commerce discovery.                                            | feed URL is a GitHub profile/org page, not a product page (2026-09-24)                                                                             |
| GetItDone                                          | Run your team's tasks and workspaces from chat                                                                                                                   | shares vendor URL devino.ca with "BioFlow" (list lint rejects duplicate links); needs its own product page (2026-09-14)                            |
| Hiver in Gmail                                     | Find, manage, and analyze customer conversations                                                                                                                 | shares vendor URL hiverhq.com with "Hiver Omni" (list lint rejects duplicate links); needs its own product page (2026-09-14)                       |
| HtAG Spatial                                       | HtAG Spatial gives Claude H3-indexed access to Australia’s property market, price/rent, socio-environmental and geography-concordance layers, so spatial questio | shares vendor URL htag.com.au with "HtAG Documentation" (list lint rejects duplicate links); needs its own product page (2026-09-14)               |
| Inbin Pulse                                        | Is this flight price actually a deal? Grounded answers from observed fare history, not vibes.                                                                    | shares vendor URL inbin.dev with "Inbin" (list lint rejects duplicate links); needs its own product page (2026-09-14)                              |
| Memco Shared Memory                                | Shared memory for all your agents                                                                                                                                | shares vendor URL memco.ai with "Memco Personal Memory" (list lint rejects duplicate links); needs its own product page (2026-09-14)               |
| Mercado Libre Inmuebles                            | Encontrar tu propiedad ideal                                                                                                                                     | Product page exists per country (.com.ar / .com.mx / .com.co /c/inmuebles); connector's country not specified.                                     |
| Milan Metro Status                                 | Real-time Milan Metro Status                                                                                                                                     | no vendor page found; only official ATM Milano transit site, which is not this connector.                                                          |
| MindMap                                            | Turn AI insights into interactive mind maps.                                                                                                                     | Several same-named projects; no confident match.                                                                                                   |
| miniOrange MCP for WordPress                       | Securely Manage Your WordPress from Claude                                                                                                                       | shares vendor URL miniorange.com with "miniOrange MCP for Magento" (list lint rejects duplicate links); needs its own product page (2026-09-14)    |
| origami.publica.la                                 | Origami is publica.la's publishing toolchain                                                                                                                     | shares vendor URL publica.la with "EbooksDepository" (list lint rejects duplicate links); needs its own product page (2026-09-14)                  |
| Pasteapp                                           | Local MCP server bridge for Paste — give Claude Desktop, Claude Code, Cursor, Codex, and other AI tools access to your Mac clipboard history and pinboards.      | the feed carries no vendor URL (2026-09-24)                                                                                                        |
| SiD Corp MCP                                       | An product from SiD Corp to connect with MCP                                                                                                                     | vendor-level match only; unrelated same-named firm exists — downgraded at merge.                                                                   |
| Sinch Build Docs                                   | Search Sinch Build developer docs and API references.                                                                                                            | shares vendor URL sinch.com with "Mailgun Docs MCP" (list lint rejects duplicate links); needs its own product page (2026-09-14)                   |
| Structured Reflection                              | Structured Reflection helps Claude debug ideas and decisions by talking through them step by step, just like a classic developer rubber‑d…                       | generic name; no vendor page identified, only unrelated open-source reflection/rubber-duck MCPs.                                                   |
| TopCounsel by The L Suite                          | Outside Counsel recommendations from Inhouse Counsel                                                                                                             | the product site says the app is not live yet, and the vendor's own site (The L Suite) never names TopCounsel (2026-09-25)                         |
| Uptimely                                           | Monitor uptime, incidents, and on-call from AI                                                                                                                   | shares vendor URL devino.ca with "BioFlow" (list lint rejects duplicate links); needs its own product page (2026-09-14)                            |
| Vid Kraken                                         | Cut audio or video clips from your own long-form videos by timestamp — podcasts, lectures, streams — and get a file ready for your editor.                       | shares vendor URL omnivision.solutions with "Transcript LOL" (list lint rejects duplicate links); needs its own product page (2026-09-14)          |
| Voxtell Phone                                      | Your business phone system, answered from Claude                                                                                                                 | shares vendor URL voxtell.com with "Voxtell Chat" (list lint rejects duplicate links); needs its own product page (2026-09-14)                     |

## Related

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Model Context Protocol servers powering many of the connectors above.
- [awesome-chatgpt-apps](https://github.com/rdmgator12/awesome-chatgpt-apps) - Companion list cataloging apps in the ChatGPT directory.
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - LLM-powered applications across providers.

---

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Ralph Martello](https://github.com/rdmgator12) has waived all copyright and related or neighboring rights to this work.
