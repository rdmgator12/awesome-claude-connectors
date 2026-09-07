# Anthropic directory feed — capture 2026-09-06

First capture of the in-app catalog through Anthropic's public directory feed (surfaced in PR #9):

```
GET https://api.anthropic.com/api/directory/servers?limit=5000&visibility=commercial,gsuite,gsuite-google&verified_tier=anthropic,partner,community
```

Captured 2026-09-06 ~20:15 ET. `total` = 2421, `next_cursor` = None, `stale_feeds` = [].
Servers: 2421 — by tier {'community': 1643, 'partner': 769, 'anthropic': 9}; by type {'remote': 2286, 'local': 135}.

`servers.tsv` is one row per server: name, tier, type, visibility, added_at (date), author name/URL, slug, directory URL, documentation URL, one-liner. The raw JSON (~6 MB) is not committed; re-run the GET to regenerate.

This feed is the in-app surface for the two-surface test (CONTRIBUTING.md): an entry absent here AND absent from the claude.com/connectors sitemap is a removal candidate. The 2026-08-10 paste export in `../in-app-2026-08-10/` had 1,691 unique names; this feed reports 2421.
