#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-receipts}"

sign_one() {
  local file="$1"
  local bundle="${file}.sigstore.json"
  if [[ -f "$bundle" ]]; then
    echo "already signed: $file"
    return 0
  fi
  local cmd=(cosign sign-blob --yes --bundle "$bundle")
  if [[ -n "${COSIGN_KEY:-}" ]]; then
    cmd+=(--key "$COSIGN_KEY")
  fi
  cmd+=("$file")
  echo "signing: $file"
  "${cmd[@]}"
}

while IFS= read -r -d '' file; do
  sign_one "$file"
done < <(find "$ROOT" -type f \( -name 'evidence_bundle.json' -o -name 'decision_log.json' -o -name 'run_receipt.json' \) -print0 | sort -z)
