#!/usr/bin/env bash
set -euo pipefail

ARTIFACT_PATH="${1:?artifact-path is required}"
MANIFEST_PATH="${2:-sbom-manifest.sha256}"
SIGNATURE_PATH="${3:-}"

if [[ ! -e "$ARTIFACT_PATH" ]]; then
  echo "::error::artifact-path does not exist: $ARTIFACT_PATH"
  exit 1
fi

if [[ -d "$ARTIFACT_PATH" ]]; then
  find "$ARTIFACT_PATH" -type f -print0 | sort -z | xargs -0 sha256sum > "$MANIFEST_PATH"
else
  sha256sum "$ARTIFACT_PATH" > "$MANIFEST_PATH"
fi

echo "manifest_path=$MANIFEST_PATH" >> "$GITHUB_OUTPUT"

if [[ -n "$SIGNATURE_PATH" ]]; then
  if command -v openssl >/dev/null 2>&1 && [[ -n "${KFM_SIGNING_KEY_PEM:-}" ]]; then
    printf '%s' "$KFM_SIGNING_KEY_PEM" > /tmp/kfm-signing-key.pem
    openssl dgst -sha256 -sign /tmp/kfm-signing-key.pem -out "$SIGNATURE_PATH" "$MANIFEST_PATH"
    rm -f /tmp/kfm-signing-key.pem
    echo "signature_path=$SIGNATURE_PATH" >> "$GITHUB_OUTPUT"
  else
    echo "::warning::Skipping signature generation; openssl or KFM_SIGNING_KEY_PEM is unavailable"
  fi
fi

echo "Created manifest at $MANIFEST_PATH"
