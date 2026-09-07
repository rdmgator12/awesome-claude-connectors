# Anthropic directory feed — capture 2026-09-06

Captured by `python3 scripts/feed_diff.py --snapshot` from:

```
GET https://api.anthropic.com/api/directory/servers?limit=5000&visibility=commercial,gsuite,gsuite-google&verified_tier=anthropic,partner,community
```

`total` = 2421, `next_cursor` = None, `stale_feeds` = [].
Servers: 2421 — by tier {'anthropic': 9, 'community': 1643, 'partner': 769}; by type {'local': 135, 'remote': 2286}.

`servers.tsv` is one row per server: name, tier, type, visibility, added_at (date), author name/URL, slug, directory URL, documentation URL, one-liner. The raw JSON (~6 MB) is not committed; re-run the script to regenerate.

This feed is the in-app surface for the two-surface test (CONTRIBUTING.md): an entry absent here AND absent from the claude.com/connectors sitemap is a removal candidate.
