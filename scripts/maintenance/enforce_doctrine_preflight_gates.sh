#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"

exec python scripts/maintenance/run_doctrine_artifact_preflight.py \
  --strict \
  --strict-provenance \
  --require-consumer-readiness \
  "$@"
