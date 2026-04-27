#!/usr/bin/env bash
set -euo pipefail

COMMAND="${1:?command is required}"
ALLOW_PATTERN="${2:-(^|\\s)(true|allow|allowed)(\\s|$)}"

if ! command -v bash >/dev/null 2>&1; then
  echo "::error::bash is required to execute policy command"
  exit 1
fi

set +e
DECISION=$(bash -lc "$COMMAND" 2>&1)
STATUS=$?
set -e

echo "decision<<EOF" >> "$GITHUB_OUTPUT"
echo "$DECISION" >> "$GITHUB_OUTPUT"
echo "EOF" >> "$GITHUB_OUTPUT"

if (( STATUS != 0 )); then
  echo "::error::Policy command failed with exit code $STATUS"
  echo "$DECISION"
  exit "$STATUS"
fi

if ! grep -Eiq "$ALLOW_PATTERN" <<<"$DECISION"; then
  echo "::error::Policy decision did not match allow pattern"
  echo "$DECISION"
  exit 1
fi

echo "Policy gate passed"
