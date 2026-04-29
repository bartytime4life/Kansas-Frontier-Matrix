#!/usr/bin/env bash
# KFM Ecology Focus Mode Validation Runner
#
# Validates governed Focus Mode fixtures, runtime outcomes, and response schema.
#
# Expectations:
# - request fixtures must pass schema validation
# - valid_request.json must return ANSWER
# - deny_sensitive_request.json must return DENY
# - abstain_missing_evidence.json must return ABSTAIN
# - runtime responses must validate against FocusModeResponse schema
#
# Exit code:
#   0 → success
#   1 → failure

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
VALIDATOR="$ROOT_DIR/tools/validators/ecology/validate_ecology_bundle.py"
RUNTIME="$ROOT_DIR/apps/governed_api/ecology/focus_mode.py"
REQUEST_DIR="$ROOT_DIR/tests/fixtures/ecology/focus_mode"
RESPONSE_SCHEMA="$ROOT_DIR/schemas/contracts/v1/ecology/focus_mode_response.schema.json"

echo "=== KFM Ecology Focus Mode Checks ==="
echo "ROOT_DIR: $ROOT_DIR"
echo

if [[ ! -f "$VALIDATOR" ]]; then
  echo "ERROR: validator not found at $VALIDATOR"
  exit 1
fi

if [[ ! -f "$RUNTIME" ]]; then
  echo "ERROR: Focus Mode runtime not found at $RUNTIME"
  exit 1
fi

if [[ ! -f "$RESPONSE_SCHEMA" ]]; then
  echo "ERROR: Focus Mode response schema not found at $RESPONSE_SCHEMA"
  exit 1
fi

if [[ ! -d "$REQUEST_DIR" ]]; then
  echo "ERROR: Focus Mode fixture directory missing: $REQUEST_DIR"
  exit 1
fi

require_fixture() {
  local file="$1"

  if [[ ! -f "$REQUEST_DIR/$file" ]]; then
    echo "ERROR: required Focus Mode fixture missing: $REQUEST_DIR/$file"
    exit 1
  fi
}

run_runtime_expect_outcome() {
  local fixture="$1"
  local expected="$2"
  local output_file

  output_file="$(mktemp)"

  echo "→ Executing Focus Mode fixture: $fixture"
  echo "  expected_outcome=$expected"

  python "$RUNTIME" "$REQUEST_DIR/$fixture" > "$output_file"

  python - "$output_file" "$RESPONSE_SCHEMA" "$expected" <<'PY'
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

output_path = Path(sys.argv[1])
schema_path = Path(sys.argv[2])
expected = sys.argv[3]

payload = json.loads(output_path.read_text(encoding="utf-8"))
schema = json.loads(schema_path.read_text(encoding="utf-8"))

errors = sorted(
    Draft202012Validator(schema).iter_errors(payload),
    key=lambda err: list(err.path),
)

if errors:
    print("ERROR: Focus Mode response schema validation failed")
    for err in errors:
        location = ".".join(str(part) for part in err.path) or "<root>"
        print(f"  schema_error:{location}:{err.message}")
    print("Actual output:")
    print(json.dumps(payload, indent=2, sort_keys=True))
    raise SystemExit(1)

outcome = payload.get("outcome")
visible_outcome = payload.get("visible_outcome")

if outcome != expected or visible_outcome != expected:
    print("ERROR: Focus Mode outcome mismatch")
    print(f"Expected: {expected}")
    print(f"Actual outcome: {outcome}")
    print(f"Actual visible_outcome: {visible_outcome}")
    print("Actual output:")
    print(json.dumps(payload, indent=2, sort_keys=True))
    raise SystemExit(1)

print(json.dumps(payload, indent=2, sort_keys=True))
PY

  rm -f "$output_file"
  echo
}

require_fixture "valid_request.json"
require_fixture "deny_sensitive_request.json"
require_fixture "abstain_missing_evidence.json"

echo "→ Validating Focus Mode request fixtures"
python "$VALIDATOR" \
  --bundle "$REQUEST_DIR"/*.json \
  --expect pass

echo
run_runtime_expect_outcome "valid_request.json" "ANSWER"
run_runtime_expect_outcome "deny_sensitive_request.json" "DENY"
run_runtime_expect_outcome "abstain_missing_evidence.json" "ABSTAIN"

echo "✓ Ecology Focus Mode checks completed"
