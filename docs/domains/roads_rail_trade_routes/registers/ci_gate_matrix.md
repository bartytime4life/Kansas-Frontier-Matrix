# CI Gate Matrix

CI gate plan for promotion safety.

## Recommended gates
- Lint and markdown checks.
- Contract validation and fixture tests.
- Policy checks for source role and sensitivity.
- Catalog/proof closure checks.
- Release dry-run checks with rollback reference.

## Promotion gate
- Block merge/release when any required lane gate fails.
