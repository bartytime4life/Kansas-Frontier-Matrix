# Validation Entrypoints

Quick-reference for running repository validation checks without searching across multiple docs.

## Core entrypoints (CONFIRMED in this repo)

- Python test configuration: `pytest.ini`
- Python tests root: `tests/`
- Web test script: `apps/web/package.json` (`npm run test`)
- Policy-focused tests: `tests/policy/` and `policy/tests/`

## Recommended quick checks

```bash
pytest --collect-only -q
npm --prefix apps/web run test -- --run
```

## Notes

- These commands are discoverability entrypoints, not full release qualification.
- Promotion remains governed by policy/review/release gates and evidence artifacts.
