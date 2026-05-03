# Layer 34 Runtime Admission

## CLI invocations
- plan-only: `python soilgrids_runtime_admission.py --mode plan-only --runtime-admission-spec runtime_admission/runtime_admission_spec_example.json --output-root out`
- verify-binding: `... --mode verify-binding --policy-lockfile ... --policy-runtime-binding ...`
- preflight: `... --mode preflight --admission-request runtime_admission/requests/example_admission_request.json`
- admit: `... --mode admit ...`
- launch-local: `... --mode launch-local --execute-launch --layer15-command python tests/fixtures/runtime_admission/mock_layer15_success.py`
- replay-admission: `... --mode replay-admission --previous-execution-context-lock ...`
- verify-lock: `... --mode verify-lock --execution-context-lock ... --runtime-input-lock ...`
- local-api: `... --mode local-api --host 127.0.0.1 --port 0`

## Examples
See JSON examples in:
- `runtime_admission/runtime_admission_spec_example.json`
- `runtime_admission/requests/example_admission_request.json`
- `examples/locks/execution_context_lock_example.json`
- `examples/locks/runtime_input_lock_example.json`
- `examples/api/runtime_admission_openapi_example.json`

## Exit codes
0 success/planned/verified, 5 dry-run, 10 warnings, 15 review, 20 deny, 30 malformed input, 40 binding failure, 50 request failure, 60 preflight, 70 lock, 80 launch, 90 replay drift, 100 api, 110 unsafe path/public bind, 120 secret, 130 ledger, 140 internal.

> This layer only admits and locks runtime operations. It does not execute pipeline logic except optional explicit Layer 15 launch, activate policies, change trust status, or grant protected-resource access.
