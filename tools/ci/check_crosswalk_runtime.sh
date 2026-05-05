#!/bin/sh
set -eu

# Runtime DB validation for the KFM HUC12 ↔ admin crosswalk lane.
# Requires a PostGIS database and populated kfm_crosswalk.crosswalk_pairs.
#
# Usage:
#   KFM_CROSSWALK_TEST_DSN="postgresql://postgres:postgres@localhost:5432/postgres" \
#   sh ./tools/ci/check_crosswalk_runtime.sh
#
# Optional:
#   KFM_CROSSWALK_RUNTIME_ALLOW_EMPTY=1 sh ./tools/ci/check_crosswalk_runtime.sh

ROOT="${1:-.}"
DSN="${KFM_CROSSWALK_TEST_DSN:-${DATABASE_URL:-}}"
VALIDATOR_SQL="$ROOT/tools/validators/crosswalk/validate_crosswalk_sql.sql"

fail() {
  echo "check_crosswalk_runtime: FAIL: $*" >&2
  exit 1
}

test -n "$DSN" || fail "KFM_CROSSWALK_TEST_DSN or DATABASE_URL is required"
test -s "$VALIDATOR_SQL" || fail "missing validator SQL: $VALIDATOR_SQL"

command -v psql >/dev/null 2>&1 || fail "psql is required"

psql "$DSN" -v "ON_ERROR_STOP=1" -Atc "SELECT 1;" >/dev/null

ROW_COUNT="$(psql "$DSN" -v "ON_ERROR_STOP=1" -Atc "
  SELECT count(*)
  FROM information_schema.tables
  WHERE table_schema = 'kfm_crosswalk'
    AND table_name = 'crosswalk_pairs';
")"

if [ "$ROW_COUNT" = "0" ]; then
  fail "kfm_crosswalk.crosswalk_pairs table does not exist"
fi

PAIR_COUNT="$(psql "$DSN" -v "ON_ERROR_STOP=1" -Atc "
  SELECT count(*)
  FROM kfm_crosswalk.crosswalk_pairs;
")"

if [ "$PAIR_COUNT" = "0" ] && [ "${KFM_CROSSWALK_RUNTIME_ALLOW_EMPTY:-0}" != "1" ]; then
  fail "kfm_crosswalk.crosswalk_pairs is empty"
fi

TMP_OUT="$(mktemp)"
trap 'rm -f "$TMP_OUT"' EXIT

psql "$DSN" -v "ON_ERROR_STOP=1" -At -F '|' -f "$VALIDATOR_SQL" > "$TMP_OUT"

FAILURES="$(awk -F '|' '{ total += $2 } END { print total + 0 }' "$TMP_OUT")"

if [ "$FAILURES" -ne 0 ]; then
  echo "check_crosswalk_runtime: validation failures:" >&2
  cat "$TMP_OUT" >&2
  exit 1
fi

echo "check_crosswalk_runtime: completed"
