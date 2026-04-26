#!/bin/sh
set -eu

# Static checks for the proposed KFM HUC12 ↔ admin crosswalk lane.
# No database, network, or source-data access required.

ROOT="${1:-.}"

WATCHER_DIR="$ROOT/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch"
SCHEMA_JSON="$ROOT/schemas/contracts/v1/crosswalk/crosswalk_pair.schema.json"
POLICY_FILE="$ROOT/policy/crosswalk/crosswalk.rego"
SOURCE_REGISTRY="$ROOT/data/registry/crosswalk/sources.yaml"
VALIDATOR_SQL="$ROOT/tools/validators/crosswalk/validate_crosswalk_sql.sql"
TEST_FILE="$ROOT/tests/crosswalk/test_crosswalk_fixture.py"

fail() {
  echo "check_crosswalk_static: FAIL: $*" >&2
  exit 1
}

check_file() {
  test -s "$1" || fail "missing or empty file: $1"
}

# Required lane files.
check_file "$WATCHER_DIR/README.md"
check_file "$WATCHER_DIR/runner.py"
check_file "$WATCHER_DIR/ingest_wbd.py"
check_file "$WATCHER_DIR/ingest_tiger_admin.py"
check_file "$WATCHER_DIR/sql/001_schema.sql"
check_file "$WATCHER_DIR/sql/010_build_crosswalk.sql"
check_file "$WATCHER_DIR/fixtures/create_fixture.sql"
check_file "$SCHEMA_JSON"
check_file "$POLICY_FILE"
check_file "$SOURCE_REGISTRY"
check_file "$VALIDATOR_SQL"
check_file "$TEST_FILE"

# Python syntax.
python3 -m py_compile \
  "$WATCHER_DIR/runner.py" \
  "$WATCHER_DIR/ingest_wbd.py" \
  "$WATCHER_DIR/ingest_tiger_admin.py" \
  "$TEST_FILE"

# JSON syntax.
python3 -m json.tool "$SCHEMA_JSON" >/dev/null

# Content guardrails.
grep -q "EPSG:5070" "$WATCHER_DIR/README.md" || fail "README missing EPSG:5070"
grep -q "run_receipt" "$WATCHER_DIR/README.md" || fail "README missing run_receipt"
grep -q "spec_hash" "$WATCHER_DIR/README.md" || fail "README missing spec_hash"

grep -q "CREATE EXTENSION IF NOT EXISTS postgis" "$WATCHER_DIR/sql/001_schema.sql" || fail "schema SQL missing PostGIS extension"
grep -q "kfm_crosswalk.crosswalk_pairs" "$WATCHER_DIR/sql/001_schema.sql" || fail "schema SQL missing crosswalk_pairs"
grep -q "ST_Intersection" "$WATCHER_DIR/sql/010_build_crosswalk.sql" || fail "build SQL missing ST_Intersection"
grep -q "ST_AsEWKB" "$WATCHER_DIR/sql/010_build_crosswalk.sql" || fail "build SQL missing EWKB geometry hashing"
grep -q "sha256" "$WATCHER_DIR/sql/010_build_crosswalk.sql" || fail "build SQL missing sha256 hashing"

grep -q "usgs_wbd_huc12" "$SOURCE_REGISTRY" || fail "source registry missing WBD source"
grep -q "census_tiger" "$SOURCE_REGISTRY" || fail "source registry missing TIGER source"

grep -q "package kfm.crosswalk" "$POLICY_FILE" || fail "policy file missing package"
grep -q "EPSG:5070" "$POLICY_FILE" || fail "policy missing CRS guardrail"

grep -q "KFM_CROSSWALK_TEST_DSN" "$TEST_FILE" || fail "test missing crosswalk test DSN gate"
grep -q "no-publish" "$TEST_FILE" || fail "test missing no-publish runner check"

echo "check_crosswalk_static: completed"
