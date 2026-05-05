#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-receipts}"
: "${COSIGN_CERTIFICATE_OIDC_ISSUER:=https://token.actions.githubusercontent.com}"

verify_one() {
  local file="$1"
  local bundle="${file}.sigstore.json"
  if [[ ! -f "$bundle" ]]; then
    echo "missing signature bundle: $bundle" >&2
    return 1
  fi

  local cmd=(cosign verify-blob "$file" --bundle "$bundle")
  if [[ -n "${COSIGN_PUBLIC_KEY:-}" ]]; then
    cmd+=(--key "$COSIGN_PUBLIC_KEY")
  else
    if [[ -n "${COSIGN_CERTIFICATE_IDENTITY:-}" ]]; then
      cmd+=(--certificate-identity="$COSIGN_CERTIFICATE_IDENTITY")
    elif [[ -n "${COSIGN_CERTIFICATE_IDENTITY_REGEXP:-}" ]]; then
      cmd+=(--certificate-identity-regexp="$COSIGN_CERTIFICATE_IDENTITY_REGEXP")
    else
      echo "Set COSIGN_CERTIFICATE_IDENTITY, COSIGN_CERTIFICATE_IDENTITY_REGEXP, or COSIGN_PUBLIC_KEY" >&2
      return 1
    fi
    cmd+=(--certificate-oidc-issuer="$COSIGN_CERTIFICATE_OIDC_ISSUER")
  fi
  echo "verifying: $file"
  "${cmd[@]}" >/dev/null
}

count=0
while IFS= read -r -d '' file; do
  verify_one "$file"
  count=$((count + 1))
done < <(find "$ROOT" -type f \( -name 'evidence_bundle.json' -o -name 'decision_log.json' -o -name 'run_receipt.json' \) -print0 | sort -z)

if [[ "$count" -eq 0 ]]; then
  echo "no receipt artifacts found under $ROOT" >&2
  exit 1
fi

echo "verified $count signed receipt artifacts under $ROOT"
