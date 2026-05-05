#!/bin/sh
set -eu

# Static checks for the KFM HUC12 ↔ admin crosswalk lane.
# No database, network, or source-data access required.

ROOT="${1:-.}"

WATCHER_DIR="$ROOT/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch"
SCHEMA_JSON="$ROOT/schemas/contracts/v1/crosswalk/crosswalk_pair.schema.json"
POLICY_FILE="$ROOT/policy/crosswalk/crosswalk.rego"
POLICY_TEST_FILE="$ROOT/policy/crosswalk/crosswalk_test.rego"
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

check_contains() {
  file="$1"
  pattern="$2"
  label="$3"

  grep -q "$pattern" "$file" || fail "$label"
}

check_file "$WATCHER_DIR/README.md"
check_file "$WATCHER_DIR/runner.py"
check_file "$WATCHER_DIR/ingest_wbd.py"
check_file "$WATCHER_DIR/ingest_tiger_admin.py"
check_file "$WATCHER_DIR/sql/001_schema.sql"
check_file "$WATCHER_DIR/sql/010_build_crosswalk.sql"
check_file "$WATCHER_DIR/fixtures/create_fixture.sql"
check_file "$SCHEMA_JSON"
check_file "$POLICY_FILE"
check_file "$POLICY_TEST_FILE"
check_file "$SOURCE_REGISTRY"
check_file "$VALIDATOR_SQL"
check_file "$TEST_FILE"

python3 -m py_compile \
  "$WATCHER_DIR/runner.py" \
  "$WATCHER_DIR/ingest_wbd.py" \
  "$WATCHER_DIR/ingest_tiger_admin.py" \
  "$TEST_FILE"

python3 -m json.tool "$SCHEMA_JSON" >/dev/null

if command -v opa >/dev/null 2>&1; then
  opa test "$ROOT/policy/crosswalk"
fi

check_contains "$WATCHER_DIR/README.md" "EPSG:5070" "README missing EPSG:5070"
check_contains "$WATCHER_DIR/README.md" "run_receipt" "README missing run_receipt"
check_contains "$WATCHER_DIR/README.md" "spec_hash" "README missing spec_hash"

check_contains "$WATCHER_DIR/sql/001_schema.sql" "CREATE EXTENSION IF NOT EXISTS postgis" "schema SQL missing PostGIS extension"
check_contains "$WATCHER_DIR/sql/001_schema.sql" "kfm_crosswalk.crosswalk_pairs" "schema SQL missing crosswalk_pairs"
check_contains "$WATCHER_DIR/sql/010_build_crosswalk.sql" "ST_Intersection" "build SQL missing ST_Intersection"
check_contains "$WATCHER_DIR/sql/010_build_crosswalk.sql" "ST_AsEWKB" "build SQL missing EWKB geometry hashing"
check_contains "$WATCHER_DIR/sql/010_build_crosswalk.sql" "sha256" "build SQL missing sha256 hashing"

check_contains "$SOURCE_REGISTRY" "usgs_wbd_huc12" "source registry missing WBD source"
check_contains "$SOURCE_REGISTRY" "census_tiger" "source registry missing TIGER source"

check_contains "$POLICY_FILE" "package kfm.crosswalk" "policy file missing package"
check_contains "$POLICY_FILE" "EPSG:5070" "policy missing CRS guardrail"

check_contains "$POLICY_TEST_FILE" "test_valid_pair_allowed" "policy test missing valid allow case"
check_contains "$POLICY_TEST_FILE" "test_bad_crs_denied" "policy test missing CRS deny case"

check_contains "$TEST_FILE" "KFM_CROSSWALK_TEST_DSN" "test missing crosswalk test DSN gate"
check_contains "$TEST_FILE" "no-publish" "test missing no-publish runner check"

echo "check_crosswalk_static: completed"
