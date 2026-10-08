# Awesome List for Claude Connectors [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Last Commit](https://img.shields.io/github/last-commit/rdmgator12/awesome-claude-connectors)](https://github.com/rdmgator12/awesome-claude-connectors/commits/main)

<p align="center">
  <img src="media/banner.svg" alt="Awesome Claude Connectors" width="800">
</p>

> A comprehensive directory of the connectors in Anthropic's [Claude Connectors catalog](https://www.anthropic.com/partners/mcp) — {{LISTED}} MCP integrations across both catalog surfaces (the curated web directory and the in-app catalog, which additionally surfaces community-built and desktop-extension connectors), plus {{HELD}} held pending vendor verification, organized by category with descriptions and use cases.

**Last updated:** {{LAST_UPDATED}} | **Connectors tracked:** {{LISTED}} listed + {{HELD}} held | **Categories:** {{NCAT}}

Claude connectors are MCP (Model Context Protocol) servers that extend Claude with real-time access to external tools, data sources, and services. They work across Claude.ai, Claude Desktop, Claude Mobile, Claude Code, and Claude Cowork. Connectors in the **curated web directory** are vetted by Anthropic for security, reliability, and compatibility; the **in-app catalog** additionally surfaces community-built and local desktop-extension connectors that Anthropic makes available but does not itself build or vet. This list tracks the union of both surfaces — see CONTRIBUTING.md for the two-surface methodology.

For more information, see the [Connectors Documentation](https://claude.com/docs/connectors/directory), [Submission Guidelines](https://claude.com/docs/connectors/building/submission), and [MCP Protocol Specification](https://modelcontextprotocol.io).

Connectors marked with **`A`** are built and maintained by Anthropic. Connectors marked with **`C`** carry the in-app catalog's Community badge — published in the catalog by Anthropic but built by third parties and not vetted the way web-directory entries are. `C` markers currently reflect the {{CAPTURE_DATE}} catalog capture, taken from the directory feed's verified tier (community → `C`, partner → none) and re-synced every sweep.

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

{{TOC}}

---

## Categories

Each category has its own page; the list outgrew what GitHub will render as a single file.

{{CATEGORY_INDEX}}

## Held for Verification

Every link on the category pages has been checked against the live page — a URL ships only when the page content confirms the product. These catalog entries are real (each appears in the in-app connectors catalog) but no vendor URL could be confirmed for them yet, so they are listed here without a link rather than with a guessed or generic one. If you are the vendor, or know the canonical product page, open an issue or PR with the URL — the entry graduates to its category once the page confirms the product.

{{HELD_TABLE}}

## Related

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Model Context Protocol servers powering many of the connectors above.
- [awesome-chatgpt-apps](https://github.com/rdmgator12/awesome-chatgpt-apps) - Companion list cataloging apps in the ChatGPT directory.
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - LLM-powered applications across providers.

---

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Ralph Martello](https://github.com/rdmgator12) has waived all copyright and related or neighboring rights to this work.
