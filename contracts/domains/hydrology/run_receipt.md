# run_receipt

Schema: `https://schemas.kfm.local/contracts/v1/domains/hydrology/run_receipt.schema.json`

Status: PROPOSED

This hydrology contract is a domain-lane alias of the common `runtime/run_receipt` contract via `$ref`.

## Meaning
Hydrology records must satisfy the shared common contract shape.

## Invariants
- MUST validate against the referenced common schema.
- Domain lane adds no extra fields in this step.

## Open questions
- NEEDS VERIFICATION: hydrology-specific constraints to add in PR 2b.
