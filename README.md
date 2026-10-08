# Awesome List for Claude Connectors [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Last Commit](https://img.shields.io/github/last-commit/rdmgator12/awesome-claude-connectors)](https://github.com/rdmgator12/awesome-claude-connectors/commits/main)

<p align="center">
  <img src="media/banner.svg" alt="Awesome Claude Connectors" width="800">
</p>

> A comprehensive directory of the connectors in Anthropic's [Claude Connectors catalog](https://www.anthropic.com/partners/mcp) — 4,675 MCP integrations across both catalog surfaces (the curated web directory and the in-app catalog, which additionally surfaces community-built and desktop-extension connectors), plus 43 held pending vendor verification, organized by category with descriptions and use cases.

**Last updated:** October 8, 2026 | **Connectors tracked:** 4,675 listed + 43 held | **Categories:** 30

Claude connectors are MCP (Model Context Protocol) servers that extend Claude with real-time access to external tools, data sources, and services. They work across Claude.ai, Claude Desktop, Claude Mobile, Claude Code, and Claude Cowork. Connectors in the **curated web directory** are vetted by Anthropic for security, reliability, and compatibility; the **in-app catalog** additionally surfaces community-built and local desktop-extension connectors that Anthropic makes available but does not itself build or vet. This list tracks the union of both surfaces — see CONTRIBUTING.md for the two-surface methodology.

For more information, see the [Connectors Documentation](https://claude.com/docs/connectors/directory), [Submission Guidelines](https://claude.com/docs/connectors/building/submission), and [MCP Protocol Specification](https://modelcontextprotocol.io).

Connectors marked with **`A`** are built and maintained by Anthropic. Connectors marked with **`C`** carry the in-app catalog's Community badge — published in the catalog by Anthropic but built by third parties and not vetted the way web-directory entries are. `C` markers currently reflect the 2026-10-08 catalog capture, taken from the directory feed's verified tier (community → `C`, partner → none) and re-synced every sweep.

This list is maintained weekly. To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

> This is an independent, community-maintained list. Not affiliated with, endorsed by, or sponsored by Anthropic PBC. "Claude" and related marks are the property of Anthropic PBC. Each connector is the property of its respective owner.

> [!TIP]
> ### Connector Snap Stack — October 8, 2026
>
> Each sweep features a persona and a small stack of connectors that click together. Past stacks are archived in [docs/stacks](docs/stacks/); sweep-by-sweep history lives in the [changelog](docs/CHANGELOG.md).
>
> **The medical-bill and appeal night** — Med Bill Check *(new)* · Appeal My Claim *(new)* · Google Drive · Google Calendar · running in **Claude Desktop**
>
> The person in the household who handles the medical paperwork, one Desktop conversation: pull the itemized ER bill and the insurer's Explanation of Benefits from the family folder in Google Drive, run each line of the bill through Med Bill Check against the Medicare rate for the state, decode the denial code on the EOB with Appeal My Claim and check the appeal deadline for that plan type, have Appeal My Claim draft the appeal letter and Med Bill Check draft a financial-assistance request to the hospital, then put the appeal deadline and a follow-up reminder on Google Calendar. Two new connectors that know the billing and appeal rules, two proven ones that hold the paperwork and the dates, with Claude carrying the case between them; both letters come out as drafts to review and send. Composed, not yet field-tested — if you run it against a live bill, send a Field Report (see CONTRIBUTING).

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
| [AI and ML](categories/ai-and-ml.md)                                       | 111        |
| [Automation and Integration](categories/automation-and-integration.md)     | 65         |
| [Calendar and Scheduling](categories/calendar-and-scheduling.md)           | 31         |
| [Cloud and Infrastructure](categories/cloud-and-infrastructure.md)         | 108        |
| [CMS and Web Building](categories/cms-and-web-building.md)                 | 104        |
| [Communication](categories/communication.md)                               | 114        |
| [Customer Support](categories/customer-support.md)                         | 92         |
| [Data and Analytics](categories/data-and-analytics.md)                     | 438        |
| [Design and Creative](categories/design-and-creative.md)                   | 161        |
| [Desktop Automation](categories/desktop-automation.md)                     | 16         |
| [Development Tools](categories/development-tools.md)                       | 206        |
| [Documents and Files](categories/documents-and-files.md)                   | 110        |
| [Education](categories/education.md)                                       | 78         |
| [Entertainment](categories/entertainment.md)                               | 57         |
| [Finance and Trading](categories/finance-and-trading.md)                   | 519        |
| [Government and Nonprofit](categories/government-and-nonprofit.md)         | 66         |
| [Healthcare and Life Sciences](categories/healthcare-and-life-sciences.md) | 90         |
| [Jobs](categories/jobs.md)                                                 | 80         |
| [Legal](categories/legal.md)                                               | 189        |
| [Lifestyle and Local](categories/lifestyle-and-local.md)                   | 308        |
| [Marketing and Sales](categories/marketing-and-sales.md)                   | 737        |
| [Observability and Monitoring](categories/observability-and-monitoring.md) | 43         |
| [Productivity](categories/productivity.md)                                 | 298        |
| [Project Management](categories/project-management.md)                     | 162        |
| [Research and Academic](categories/research-and-academic.md)               | 67         |
| [SAP](categories/sap.md)                                                   | 4          |
| [Security](categories/security.md)                                         | 98         |
| [SEO and Web](categories/seo-and-web.md)                                   | 111        |
| [Ticketing and Events](categories/ticketing-and-events.md)                 | 45         |
| [Travel](categories/travel.md)                                             | 167        |

## Held for Verification

Every link on the category pages has been checked against the live page — a URL ships only when the page content confirms the product. These catalog entries are real (each appears in the in-app connectors catalog) but no vendor URL could be confirmed for them yet, so they are listed here without a link rather than with a guessed or generic one. If you are the vendor, or know the canonical product page, open an issue or PR with the URL — the entry graduates to its category once the page confirms the product.

| Connector                                          | Catalog description                                                                                                                                              | Why held                                                                                                                                                                        |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Academic report builder                            | Write your university report with Claude, in the official format, and download it as a Word document.                                                            | vendor page returns 404, its Claude page included (2026-10-08)                                                                                                                  |
| Agent Grid                                         | Create, share, and evolve interactive artifacts with humans and AI agents.                                                                                       | agentgrid.sh exists but is a coding-agent canvas, not an interactive-artifact platform; no confident match.                                                                     |
| AI Dispatcher by FieldCamp                         | AI dispatch and scheduling for field-service teams — view your jobs, technicians and board, run AI dispatch, and accept assignments, right from Claude.          | shares vendor URL fieldcamp.ai with "FieldCamp" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                                    |
| Aster Share                                        | Create in Claude. Publish with Aster.                                                                                                                            | the vendor site returns a hosting error on every page (deployment disabled, HTTP 402) (2026-09-25)                                                                              |
| Capi Agent                                         | Find products from independent online stores in Saudi Arabia, the Gulf and Türkiye                                                                               | shares its vendor URL with Capi Agent for Merchants, whose product that page is; no page for the shopping connector was found (2026-09-25)                                      |
| Code de loi - GTACityRP                            | Les codes de loi fictifs du serveur de jeu de rôle GTACityRP : lire un article, chercher un sujet, parcourir un Code.                                            | vendor site presents itself as the government of the State of Tennessee on a non-government domain (a roleplay server's site); held under the impersonation screen (2026-10-08) |
| ConstruChain Tracker                               | Review authorized construction progress, weekly snapshots and schedules.                                                                                         | shares vendor URL construchain.com.br with "ConstruChain Vision" (list lint rejects duplicate links); needs its own product page (2026-10-08)                                   |
| Cover Letter Checker & Builder - ResumeNext        | Check a cover letter against a fixed checklist, read example letters by role, and open the final letter in the ResumeNext cover letter editor.                   | shares vendor URL resumenext.io with "ATS Resume Checker & Resume Builder - ResumeNext" (list lint rejects duplicate links); needs its own product page (2026-10-08)            |
| CSME Developer Build Compliance and Content Filter | Check what you build against the law before it ships.                                                                                                            | the feed URL is a misspelled, unregistered domain and the product has no page of its own apart from the one CSME Content Creator uses (2026-09-24)                              |
| Dango                                              | Build beautiful presentations, in your own brand.                                                                                                                | vendor site and its docs page return Cloudflare 530 (origin unreachable) on every check since 2026-09-28; graduated 2026-09-25, re-held 2026-10-08 until the site is back.      |
| Decision Matrix                                    | Decision Matrix helps Claude run structured, criteria‑based evaluations so teams can make and defend complex decisions with confidence.                          | generic term; search returns the decision-matrix method, not a vendor product page.                                                                                             |
| doDomain                                           | Connect customer domains from chat                                                                                                                               | shares vendor URL devino.ca with "BioFlow" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                                         |
| Domain & Redirect Checker                          | Domain not working or redirecting? Check redirects, DNS, propagation and "not secure" SSL errors for any domain and get the fix. Free, no sign-up.               | shares vendor URL domain-forward.com with "Domain Forward" (list lint rejects duplicate links); needs its own product page (2026-10-08)                                         |
| Events for Organisers                              | Organisers on Events.mt manage their events, company invitations and guest lists in plain words: invite, remind, name guests, edit events and tickets.           | shares vendor URL events.com.mt with "Events" (list lint rejects duplicate links); needs its own product page (2026-10-08)                                                      |
| FocusPulse                                         | News stories for India and the US linked to the listed companies, commodities, indices or currency they concern, each with its sources.                          | vendor site returns no content to either fetch channel (2026-10-08)                                                                                                             |
| GetItDone                                          | Run your team's tasks and workspaces from chat                                                                                                                   | shares vendor URL devino.ca with "BioFlow" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                                         |
| Hiver in Gmail                                     | Find, manage, and analyze customer conversations                                                                                                                 | shares vendor URL hiverhq.com with "Hiver Omni" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                                    |
| HtAG Spatial                                       | HtAG Spatial gives Claude H3-indexed access to Australia’s property market, price/rent, socio-environmental and geography-concordance layers, so spatial questio | shares vendor URL htag.com.au with "HtAG Documentation" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                            |
| Inbin Pulse                                        | Is this flight price actually a deal? Grounded answers from observed fare history, not vibes.                                                                    | shares vendor URL inbin.dev with "Inbin" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                                           |
| Job Match & Resume Keyword Scanner - ResumeNext    | Compare a resume with a job description: matched and missing keywords, coverage, and a job-tailored ATS score.                                                   | shares vendor URL resumenext.io with "ATS Resume Checker & Resume Builder - ResumeNext" (list lint rejects duplicate links); needs its own product page (2026-10-08)            |
| Memco Shared Memory                                | Shared memory for all your agents                                                                                                                                | shares vendor URL memco.ai with "Memco Personal Memory" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                            |
| Mercado Libre Inmuebles                            | Encontrar tu propiedad ideal                                                                                                                                     | Product page exists per country (.com.ar / .com.mx / .com.co /c/inmuebles); connector's country not specified.                                                                  |
| Milan Metro Status                                 | Real-time Milan Metro Status                                                                                                                                     | no vendor page found; only official ATM Milano transit site, which is not this connector.                                                                                       |
| MindMap                                            | Turn AI insights into interactive mind maps.                                                                                                                     | Several same-named projects; no confident match.                                                                                                                                |
| miniOrange MCP for WordPress                       | Securely Manage Your WordPress from Claude                                                                                                                       | shares vendor URL miniorange.com with "miniOrange MCP for Magento" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                 |
| origami.publica.la                                 | Origami is publica.la's publishing toolchain                                                                                                                     | shares vendor URL publica.la with "EbooksDepository" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                               |
| pensieve-notes                                     | Save notes, search them and set reminders from Claude                                                                                                            | the feed URL is the developer's personal site; a same-named notes app exists but is not confirmed as this connector's (2026-09-25)                                              |
| Prativedan                                         | Write your academic report with Claude, in your university's format, and download it as a Word document.                                                         | vendor URL is the developer's personal site, and the product's own Claude page and homepage return 404 (2026-10-08)                                                             |
| Resume Examples & Templates - ResumeNext           | Browse resume examples by role and resume templates, each with a link that opens it in the ResumeNext editor as a starting point.                                | shares vendor URL resumenext.io with "ATS Resume Checker & Resume Builder - ResumeNext" (list lint rejects duplicate links); needs its own product page (2026-10-08)            |
| Resume Skills & Keywords by Role - ResumeNext      | Get the skills and terms that recur for a role and see where a resume uses them: listed and shown, listed only, shown only, or not mentioned.                    | shares vendor URL resumenext.io with "ATS Resume Checker & Resume Builder - ResumeNext" (list lint rejects duplicate links); needs its own product page (2026-10-08)            |
| Roraima holiday rentals                            | Find holiday rentals and smart devices on Roraima, get a price quote, and receive a link to book, or a booking prepared to check and pay on roraima.io.          | shares vendor URL roraima.io with "Roraima for hosts" (list lint rejects duplicate links); needs its own product page (2026-10-08)                                              |
| Rush SR Lap Analyzer                               | Analyze lap data: lap times, best and theoretical best, compare laps, find lost time, and compare two drivers or sessions. Works with AiM data and sim data.     | shares vendor URL rushautoworks.com with "Rush SR Maintenance" (list lint rejects duplicate links); needs its own product page (2026-10-08)                                     |
| SiD Corp MCP                                       | An product from SiD Corp to connect with MCP                                                                                                                     | vendor-level match only; unrelated same-named firm exists — downgraded at merge.                                                                                                |
| Sinch Build Docs                                   | Search Sinch Build developer docs and API references.                                                                                                            | shares vendor URL sinch.com with "Mailgun Docs MCP" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                                |
| Structured Reflection                              | Structured Reflection helps Claude debug ideas and decisions by talking through them step by step, just like a classic developer rubber‑d…                       | generic name; no vendor page identified, only unrelated open-source reflection/rubber-duck MCPs.                                                                                |
| Table12 Manager                                    | For restaurant owners on Table12: see bookings and waiting requests, answer them, add and change bookings, close off tables and change opening hours by asking.  | shares vendor URL table12.com with "Table12" (list lint rejects duplicate links); needs its own product page (2026-10-08)                                                       |
| Task Ninja                                         | Command your entire to-do list by voice or chat: plan your day, capture tasks and chase your team.                                                               | the feed's vendor URL is an unrelated supplement retailer, and the product's own domain serves no readable content to either fetch channel (2026-10-08)                         |
| TopCounsel by The L Suite                          | Outside Counsel recommendations from Inhouse Counsel                                                                                                             | the product site says the app is not live yet, and the vendor's own site (The L Suite) never names TopCounsel (2026-09-25)                                                      |
| Uptimely                                           | Monitor uptime, incidents, and on-call from AI                                                                                                                   | shares vendor URL devino.ca with "BioFlow" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                                         |
| Vid Kraken                                         | Cut audio or video clips from your own long-form videos by timestamp — podcasts, lectures, streams — and get a file ready for your editor.                       | shares vendor URL omnivision.solutions with "Transcript LOL" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                       |
| Virtualna Pisarna - By REWORQ                      | Your virtual office in one place                                                                                                                                 | the feed URL is REWORQ's agency homepage, which never names the product, and no product page was found (2026-09-25)                                                             |
| Voxtell Phone                                      | Your business phone system, answered from Claude                                                                                                                 | shares vendor URL voxtell.com with "Voxtell Chat" (list lint rejects duplicate links); needs its own product page (2026-09-14)                                                  |
| Windowbox                                          | Search and read Portland City Council meeting transcripts, with speaker names, agenda items, and links to the recording and the official record.                 | vendor URL is http-only, its domain has no address record, and a second fetch channel got an error (2026-10-08)                                                                 |

## Related

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Model Context Protocol servers powering many of the connectors above.
- [awesome-chatgpt-apps](https://github.com/rdmgator12/awesome-chatgpt-apps) - Companion list cataloging apps in the ChatGPT directory.
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - LLM-powered applications across providers.

---

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Ralph Martello](https://github.com/rdmgator12) has waived all copyright and related or neighboring rights to this work.
