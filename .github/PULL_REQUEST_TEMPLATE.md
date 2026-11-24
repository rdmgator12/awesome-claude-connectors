<!--
Thanks for contributing! Please confirm the checklist below before submitting.
Entries that don't follow the format will be closed.
-->

## What you're adding

<!-- One line summary -->

## Entry format

Entries live in `data/connectors.json`. `README.md`, the pages under `categories/` and the website feed under `site-data/` are generated from it (see CONTRIBUTING.md), so don't edit those by hand. Add an object like:

```json
{
  "name": "Name",
  "url": "https://link",
  "marker": null,
  "category": "Existing Category",
  "subcategory": "Existing Subcategory",
  "description": "One-sentence description ending with a period.",
  "use_case": "A concrete scenario or 2-3 comma-separated scenarios that do not restate the description; no \"your\"/\"our\"."
}
```

`subcategory` is required in the five categories that have subcategories (Data and Analytics, Finance and Trading, Lifestyle and Local, Marketing and Sales, Productivity) and must be one of the headings on that category's page. Leave it out everywhere else.

Then run:

```
python3 scripts/generate_readme.py
python3 scripts/export_site_data.py
```

and commit `data/connectors.json`, `README.md`, `categories/` and `site-data/` together, plus `data/changes.json` if the export changed it. Sorting is automatic; duplicates and format are validated for you.

## Checklist

- [ ] Connector is publicly listed in Anthropic's connector directory (web or in-app)
- [ ] Entry added to `data/connectors.json` with an existing category (and subcategory, where the category has them)
- [ ] Description is one sentence, no marketing language, ends with a period
- [ ] `use_case`: one sentence, 1-3 concrete comma-separated scenarios, not a restatement of the description
- [ ] Link uses HTTPS and points to the product's own page, and I opened it and saw the product named there
- [ ] `python3 scripts/generate_readme.py --check` and `python3 scripts/export_site_data.py --check` pass
- [ ] `npx awesome-lint@2.3.0` (the README) and `bash scripts/lint_category_pages.sh` (every category page) pass; both need Node

## Notes

<!-- Anything reviewers should know -->
