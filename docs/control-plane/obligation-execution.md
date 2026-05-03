---
doc_id: kfm://doc/governance/obligation-execution-v1
title: Obligation Execution + Recompute Queue + Publish Enforcement v1
status: draft
domain: governance
layer: obligation_execution_v1
rights: public
promotion_state: not_promoted
network: disabled
sensitivity: public
kfm_meta_block: v2
created: NEEDS_VERIFICATION
updated: NEEDS_VERIFICATION
---

# Obligation Execution v1

## Lifecycle placement
This layer sits between EvidenceBundle obligation declaration and publish-time promotion. Publication is treated as a governed state transition.

## Object separation
- `ObligationExecutionReceipt.v1`: action execution proof.
- `RecomputeQueueItem.v1`: deferred recompute/suppression backlog.
- `RevocationImpactReport.v1`: consent delta impact summary.
- `PublishEnforcementReport.v1`: final publish allow/deny/block result.

## Receipt chain
Publish decisions reference receipts and run attestations; policy decisions stay separate from execution receipts.

## Recompute queue behavior
Any consent revocation or policy-triggered recompute opens queue items; unresolved items force publish DENY/BLOCK.

## Publish-time fail-closed rules
- missing obligations/receipts: deny
- revoked consent with allow: deny
- retention expired with allow: deny
- unresolved recompute queue with allow: deny
- unverified/unsigned run receipt: deny

## Public-safety constraints
Public artifacts must exclude forbidden/raw/sensitive fields such as exact coordinates, raw payload fields, private identifiers, tokens, and genomics markers.

## Validation commands
- `python3 tools/validators/governance/validate_obligation_execution.py --bundle tests/fixtures/governance/obligation_execution/valid/suppress_huc12.json`
- `pytest -q tests/governance/test_obligation_execution_validator.py`
- `opa test policy/governance/obligation_execution.rego policy/governance/obligation_execution_test.rego` (when OPA is installed)

## CI gate expectations
CI runs schema+validator fixture checks and pytest offline. OPA checks are best-effort with skip + `NEEDS_VERIFICATION` when OPA is unavailable.

## Rollback / correction path
If enforcement logic regresses, rollback by reverting this layer commit, re-running governance fixture tests, and issuing correction artifacts that supersede incorrect publish decisions.
