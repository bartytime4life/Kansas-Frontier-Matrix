#!/usr/bin/env bash
set -euo pipefail
# Roll back atmosphere_air domain slug normalization moves
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if [ -d docs/domains/atmosphere_air ]; then
    git mv docs/domains/atmosphere_air docs/domains/atmosphere-air
  fi
fi
# Restore edited references from commit parent
# git restore --source=HEAD~1 -- README.md docs tests tools
