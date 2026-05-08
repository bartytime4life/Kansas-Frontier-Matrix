# policy

## Purpose
Policy-as-code plus policy documentation. Governs allow / deny / restrict / abstain / redaction / public release / promotion / sensitivity.

## Authority level
canonical (singular `policy/`; legacy `policies/` not created in greenfield)

## What belongs here
OPA/rego (or equivalent) modules, policy bundles, fixtures, runtime/promotion/sensitivity/rights/release/UI policies.

## What does not belong here
Schema definitions, source data, executable application code beyond the policy runtime.

## Inputs
See related folders.

## Outputs
See related folders.

## Validation
See `tests/` and `tools/validators/`.

## Review burden
Maintainer review; steward review for trust-bearing changes.

## Related folders
`schemas/contracts/v1/policy/`, `tests/policy/`, `fixtures/policy/`, `apps/governed-api/`.

## Status
PROPOSED
