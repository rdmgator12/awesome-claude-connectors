#!/usr/bin/env bash
# awesome-lint every generated category page. Entry-level rules (list-item,
# double-link, punctuation, ...) apply exactly as they did when every entry lived
# in README.md. Two page-level rules cannot apply to a subpage and are the only
# ones ignored: awesome-contributing (looks for contributing.md beside the file)
# and awesome-heading (wants an "Awesome X" title).
#
# Each page must report awesome-contributing: that is the proof the rules ran,
# so a crashed or silent linter fails here instead of passing vacuously.
set -uo pipefail

cd "$(dirname "$0")/.."
shopt -s nullglob
pages=(categories/*.md)
if [ ${#pages[@]} -eq 0 ]; then
  echo "no category pages found" >&2
  exit 1
fi

fail=0
for page in "${pages[@]}"; do
  out="$(npx --yes awesome-lint@2.3.0 "$page" 2>&1)"
  if ! grep -q "awesome-contributing" <<<"$out"; then
    echo "$page: awesome-lint did not run its rules:" >&2
    echo "$out" >&2
    fail=1
    continue
  fi
  errors="$(grep "✖" <<<"$out" | grep "remark-lint:" | grep -vE "remark-lint:awesome-(contributing|heading)" || true)"
  if [ -n "$errors" ]; then
    echo "$page:" >&2
    echo "$errors" >&2
    fail=1
  fi
done

if [ $fail -eq 0 ]; then
  echo "category pages: ${#pages[@]} linted, 0 entry-level errors"
fi
exit $fail
