#!/bin/sh
set -eu

ROOT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "dev_up: running script lane checks from $ROOT_DIR"
python3 scripts/catalog_validate.py
python3 scripts/validate_schemas.py

echo "dev_up: baseline checks passed"
echo "dev_up: no long-running local services are currently defined in this repository"
