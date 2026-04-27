#!/usr/bin/env bash
set -euo pipefail

FILES_INPUT="${1:-}"
REQUIRED_TOKEN="${2:-[KFM_META_BLOCK_V2]}"

if [[ -z "${FILES_INPUT//$'\n'/}" ]]; then
  mapfile -t FILES < <(find . -type f -name '*.md' -not -path './.git/*' | sort)
else
  mapfile -t FILES <<<"$FILES_INPUT"
fi

checked=0
missing=0
missing_files=()

for file in "${FILES[@]}"; do
  [[ -z "$file" ]] && continue
  if [[ ! -f "$file" ]]; then
    echo "::warning::Skipping missing file: $file"
    continue
  fi

  checked=$((checked + 1))
  if ! grep -qF "$REQUIRED_TOKEN" "$file"; then
    missing=$((missing + 1))
    missing_files+=("$file")
  fi
done

{
  echo "checked_count=$checked"
  echo "missing_count=$missing"
} >> "$GITHUB_OUTPUT"

echo "Checked $checked markdown file(s)."

if (( missing > 0 )); then
  echo "::error::Missing '$REQUIRED_TOKEN' in ${missing} file(s): ${missing_files[*]}"
  exit 1
fi
