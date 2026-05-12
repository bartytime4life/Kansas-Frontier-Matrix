# Contract: promotion_decision

**Family:** `release`
**Schema:** `schemas/contracts/v1/release/promotion_decision.schema.json`
**Status:** PROPOSED

## Meaning
A `promotion_decision` records a governed transition decision for a specific domain run.
The decision must cite evidence, the policy bundle used, and an explicit rollback target.

## Fields
- `id`: deterministic decision id.
- `domain`: lane being promoted (e.g., `hydrology`).
- `run_id`: pipeline execution id being evaluated.
- `decision`: one of `APPROVE`, `DENY`, `ABSTAIN`.
- `evidence_ref` and `evidence_bundle_uri`: citation closure.
- `rollback_card_uri`: rollback target for the promoted unit.
- `review`: reviewer and ticket binding for auditable oversight.

## Invariants
- Promotion is a state transition decision, not a file move.
- `decision=APPROVE` requires non-empty evidence and rollback references.
- Review metadata is mandatory.

## Lifecycle
Created by promotion gate evaluation, validated by schema+policy tests, and stored under `release/promotion_decisions/<domain>/`.

## Related contracts
`release_manifest`, `rollback_card`, domain evidence bundle contracts.
