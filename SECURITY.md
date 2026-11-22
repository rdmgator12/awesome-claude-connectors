# Security

This repository is a list of links. Nothing here is installed or run on your machine, so the risks worth reporting are about where the links lead and how the list is built.

## What to report

- **A listed link that has gone bad.** The site now serves malware, a credential-phishing page or a scam, or the domain has changed hands and no longer belongs to the product named in the entry.
- **An entry that impersonates someone.** A connector presenting itself as a company, product or public body it is not.
- **A flaw in the tooling.** Something in `scripts/` or `.github/workflows/` that would let a pull request, an issue, or text from the catalog feed change the published list, run code in CI with more access than it should have, or plant a link nobody reviewed.

Ordinary link rot (a 404, an expired domain with nothing on it) is not sensitive. Open an issue or a pull request for those.

## How to report

Email **coups.matins6v@icloud.com** with the entry name, the URL, what you saw and when. Please do not open a public issue for a link that is actively harmful: an issue advertises the link to everyone who reads it.

A report gets an acknowledgement, a check of the link from a second network, and one of three outcomes: the entry is re-pointed to the product's real page, moved to **Held for Verification** with the reason and date, or removed. The outcome is recorded in [docs/CHANGELOG.md](docs/CHANGELOG.md).

## What a listing does and does not mean

A listing means the connector appeared in Anthropic's connector catalog and that, when it was added, the linked page named the product. It is not a security review of the connector, its vendor or its MCP server, and it is not an endorsement.

- Entries marked **`C`** carry the catalog's Community badge. They are built by third parties and are not vetted the way the curated web-directory entries are.
- This list is independent and community-maintained. It is not affiliated with, endorsed by, or sponsored by Anthropic PBC.
- Before you connect any connector to an account, read what it asks permission to do and who runs it. That decision is yours.

## What the list checks

- **At each sweep:** every new vendor URL is fetched and the page must name the product itself, not only its vendor. Each candidate is screened for brand names it does not own, lookalike domains, MCP endpoints on a large brand's domain the vendor does not control, government-styled pages on non-government domains, and catalog text written to steer an AI assistant. A confirmed problem is held and published without a link.
- **Weekly:** a link check over every page, filed as an issue, and a diff of the catalog feed against the list.
- **On every commit and pull request:** the generator rejects an entry whose text contains a link, markup or hidden characters, and a link whose host carries credentials, a port, an IP address, punycode or anything other than a plain lowercase domain name. `scripts/name_url_check.py` flags a URL that looks like a misspelling of its own entry's name.

Workflows run with a read-only token and no secrets. The two scheduled jobs can also open issues; none of them can push to the repository.
