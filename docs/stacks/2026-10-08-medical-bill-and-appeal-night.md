# Connector Snap Stack — The medical-bill and appeal night

*2026-10-08 · fourth stack*

**[Med Bill Check](https://goodturn-mcp.pages.dev/medbillcheck)** *(new)* · **[Appeal My Claim](https://goodturn-mcp.pages.dev/appealmyclaim)** *(new)* · **[Google Drive](https://drive.google.com)** · **[Google Calendar](https://calendar.google.com)** — running in **Claude Desktop**

The person in the household who handles the medical paperwork, one Desktop conversation: pull the itemized ER bill and the insurer's Explanation of Benefits from the family folder in Google Drive, run each line of the bill through Med Bill Check against the Medicare rate for the state, decode the denial code on the EOB with Appeal My Claim and check the appeal deadline for that plan type, have Appeal My Claim draft the appeal letter and Med Bill Check draft a financial-assistance request to the hospital, then put the appeal deadline and a follow-up reminder on Google Calendar. Two new connectors that know the billing and appeal rules, two proven ones that hold the paperwork and the dates, with Claude carrying the case between them. Both letters come out as drafts for the person to review and send.

*Status: composed, not yet field-tested against a live bill. If you run it, send a Field Report (see CONTRIBUTING).*
