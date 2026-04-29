#!/bin/sh
set -eu

ROOT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$ROOT_DIR"

bash scripts/bootstrap.sh
python3 scripts/catalog_validate.py
python3 scripts/validate_schemas.py

echo "build_all: scripts lane checks completed"
