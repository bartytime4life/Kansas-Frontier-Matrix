# tests/policy

Policy and governance guardrail tests.

## Boundary suite
The boundary suite currently includes:

- `test_control_plane_register_meta_contract.py`
- `test_explorer_web_adapter_boundary.py`
- `test_pipeline_connector_non_publisher.py`

Shared constants are centralized in `boundary_constants.py`.

Run locally:

```bash
pytest -q \
  tests/policy/test_control_plane_register_meta_contract.py \
  tests/policy/test_explorer_web_adapter_boundary.py \
  tests/policy/test_pipeline_connector_non_publisher.py \
  apps/governed-api/tests/test_boundary_guards.py
```

CI coverage is provided by `.github/workflows/policy-boundary-guards.yml`.

## CI report artifact

For local parity with CI report output:

```bash
make boundary-guards-ci
```

This writes `artifacts/qa/policy-boundary-guards.xml` (ignored by `.gitignore`) for report consumption.
