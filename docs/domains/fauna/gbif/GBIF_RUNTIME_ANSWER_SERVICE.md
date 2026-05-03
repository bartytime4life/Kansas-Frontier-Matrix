# KFM Meta Block v2
- domain: fauna
- component: GBIF runtime answer service
- version: v1

## Purpose
Fixture-backed governed runtime answering for GBIF occurrence aggregates.

## Lifecycle placement
TRIPLET -> RUNTIME_READ_MODEL -> GOVERNED_ANSWER_SERVICE -> PUBLIC_UI_DTO/API_DTO -> ANSWER_RECEIPT.

## Contracts
Implements query DTO, answer envelope, UI card, map layer, and receipt schemas in `schemas/runtime/fauna`, `schemas/ui/fauna`, and `schemas/receipts/fauna`.

## Citation and abstention rules
Cited answers require citations/evidence/download/geoprivacy/spec hash and safe postures; otherwise abstain with enumerated reason.

## Forbidden language and geoprivacy
Blocks confirmed-presence language and exact coordinate fields; map layers are generalized_public_area only.

## CLI examples
See `tools/runtime/fauna/kfm_gbif_answer_cli.py` for fixture-query and direct-args modes.

## Validator + policy gates
Validator: `tools/validators/fauna/gbif_runtime_answer_validator.py`.
Policy: `policy/fauna/gbif_runtime_answer.rego` + tests.

## Testing posture
Pytest coverage for service, CLI, UI DTO, validator, schema and receipt-hash stability.

## Limitations
No live GBIF network access; fixture-driven only.

## Promotion checklist
- pass pytest
- pass validator checks
- pass rego tests

## Rollback/correction notes
Rollback by reverting service/schema/policy bundle commit and regenerating outputs.

## NEEDS_VERIFICATION
- Runtime API registration convention (apps/governed_api integration) left unchanged; implemented as library + CLI only.
- MCP tool registration convention left unchanged.
