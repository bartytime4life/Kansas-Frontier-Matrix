#!/usr/bin/env bash
set -euo pipefail

FILE="${1:?file is required}"
EXPECTED="${2:?expected-sha256 is required}"

if [[ ! -f "$FILE" ]]; then
  echo "::error::File does not exist: $FILE"
  exit 1
fi

ACTUAL=$(sha256sum "$FILE" | awk '{print $1}')
echo "actual_sha256=$ACTUAL" >> "$GITHUB_OUTPUT"

if [[ "$ACTUAL" != "$EXPECTED" ]]; then
  echo "::error::Digest mismatch for $FILE"
  echo "expected=$EXPECTED"
  echo "actual=$ACTUAL"
  exit 1
fi

echo "Provenance digest verified for $FILE"
