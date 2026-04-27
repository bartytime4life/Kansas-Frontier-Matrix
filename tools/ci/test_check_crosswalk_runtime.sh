#!/bin/sh
set -eu

# Tests for tools/ci/check_crosswalk_runtime.sh
# Uses fail-closed checks without requiring PostGIS for negative-path coverage.
# If KFM_CROSSWALK_TEST_DSN or DATABASE_URL is present, also runs a live fixture check.

ROOT="${1:-.}"
CHECK_SCRIPT="$ROOT/tools/ci/check_crosswalk_runtime.sh"
FIXTURE_SQL="$ROOT/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/fixtures/create_fixture.sql"
RUNNER="$ROOT/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/runner.py"

fail() {
  echo "test_check_crosswalk_runtime: FAIL: $*" >&2
  exit 1
}

pass() {
  echo "test_check_crosswalk_runtime: PASS: $*"
}

test -f "$CHECK_SCRIPT" || fail "missing $CHECK_SCRIPT"
test -x "$CHECK_SCRIPT" || chmod +x "$CHECK_SCRIPT"

# Negative path: missing DSN must fail.
if env -u KFM_CROSSWALK_TEST_DSN -u DATABASE_URL sh "$CHECK_SCRIPT" "$ROOT" >/dev/null 2>&1; then
  fail "missing DSN did not fail"
else
  pass "missing DSN fails closed"
fi

DSN="${KFM_CROSSWALK_TEST_DSN:-${DATABASE_URL:-}}"

# Live fixture path is optional for local runs.
if [ -z "${DSN:-}" ]; then
  echo "test_check_crosswalk_runtime: skipping live DB fixture check; no DSN provided"
  echo "test_check_crosswalk_runtime: completed"
  exit 0
fi

command -v psql >/dev/null 2>&1 || {
  echo "test_check_crosswalk_runtime: skipping live DB fixture check; psql not installed"
  echo "test_check_crosswalk_runtime: completed"
  exit 0
}

test -s "$FIXTURE_SQL" || fail "missing fixture SQL: $FIXTURE_SQL"
test -s "$RUNNER" || fail "missing runner: $RUNNER"

psql "$DSN" -v "ON_ERROR_STOP=1" -Atc "SELECT 1;" >/dev/null

psql "$DSN" -v "ON_ERROR_STOP=1" -f "$FIXTURE_SQL" >/dev/null

python3 "$RUNNER" \
  --dsn "$DSN" \
  --run-id "ci-runtime-validator-fixture" \
  --no-publish \
  --replace-run >/dev/null

sh "$CHECK_SCRIPT" "$ROOT" >/dev/null

pass "live fixture validation"
echo "test_check_crosswalk_runtime: completed"
