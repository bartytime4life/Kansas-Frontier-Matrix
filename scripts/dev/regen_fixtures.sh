#!/usr/bin/env bash
# Regenerate deterministic fixtures through the reviewed readiness registry.
#
# Fixture regeneration is a named HOLD in control_plane/readiness/lanes.json
# until tools/fixtures/regenerate.py and its manifest are accepted. This wrapper
# delegates to that lane so it can never report success without a producer;
# a HOLD exits 3 and is not validation, release, or publication evidence.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PYTHON="${PYTHON:-python3}"

if [[ $# -ne 0 ]]; then
  echo "regen_fixtures: no arguments are accepted; lane inputs come from the readiness registry" >&2
  exit 2
fi

cd "$ROOT"
exec env KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC \
  "$PYTHON" tools/readiness/run_lane.py fixtures
