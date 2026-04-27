# Archaeology Runbook

## Safe first-run sequence

1. Verify docs and source-registry scaffolding.
2. Confirm no live connectors are enabled.
3. Run fixture-based validation and policy checks.
4. Validate public DTO safety.
5. Validate catalog/proof closure.
6. Approve promotion only with completed review evidence.

## Incident handling

- If sensitivity leakage is detected: disable affected release, publish correction notice, execute rollback card, and re-run closure validation.
