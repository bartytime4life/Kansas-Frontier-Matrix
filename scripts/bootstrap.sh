#!/bin/sh
set -eu

if command -v python3 >/dev/null 2>&1; then
  pyv="$(python3 --version 2>&1)"
  echo "python3: ${pyv}"
  echo "bootstrap: docs-first workspace; no dependency installer is defined in this repo yet"
  exit 0
fi

echo "python3 is required but was not found on PATH" >&2
exit 1
