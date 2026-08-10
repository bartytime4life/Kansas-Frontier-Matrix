<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/lifecycle-gate-closure-assessment
title: LifecycleGateClosureAssessment Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Governance steward · Lifecycle steward · Evidence steward · Policy steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; governance; lifecycle; fail-closed; no-network
owning_root: contracts/
responsibility: Define a bounded assessment of whether one declared lifecycle gate has its required artifacts, dependency resolution, policy record, and failure-closed disposition without executing the transition.
truth_posture: CONFIRMED source and repository gap / PROPOSED inactive assessment / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ../../docs/atlases/pipeline-gate-reference.md
  - ./gate_outcome_mapping.md
  - ../release/promotion_decision.md
  - ../../schemas/contracts/v1/governance/lifecycle_gate_closure_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/lifecycle_gate_closure_assessment/cases.json
  - ../../tools/validators/governance/validate_lifecycle_gate_closure_assessment.py
  - ../../tests/validators/governance/test_validate_lifecycle_gate_closure_assessment.py
  - ../../docs/intake/exploratory/lifecycle-gate-closure-assessment-source-map.md
tags: [kfm, governance, lifecycle, gates, closure, fail-closed, fixture-only]
notes:
  - "Adapts the Full Atlas Universal Pipeline Gate Reference cards and the existing repository carrier's explicit fixture-validator gap."
  - "A conforming assessment describes gate readiness only; it never performs a lifecycle write, promotion, release, correction, rollback, or publication."
[/KFM_META_BLOCK_V2] -->

# LifecycleGateClosureAssessment Candidate

> A deterministic, fixture-only profile that makes the seven RAW-to-PUBLISHED lifecycle gates inspectable while preserving the rule that a transition is a governed decision, never a file move.

## Purpose

`LifecycleGateClosureAssessment` binds one synthetic subject and one attempted gate to:

- its declared prior and target lifecycle stages;
- the gate-specific artifact roles required for closure;
- the declared local resolution state of each artifact and dependency;
- a recorded PolicyDecision dependency;
- a finite `ALLOW`, `HOLD`, `DENY`, or `ERROR` result;
- the exact failure-closed disposition for the attempted gate; and
- deterministic JCS plus SHA-256 identity.

The profile does not fetch or authenticate referenced objects. `RESOLVED` is an input assertion tested for internal consistency, not proof that an external object exists.

## Seven-gate ladder

| Gate | Prior -> target | Minimum artifact roles | Failure-closed disposition |
|---|---|---|---|
| `ADMISSION` | `DISCOVERED -> RAW` | `SOURCE_DESCRIPTOR`, `PAYLOAD_IDENTITY`, `POLICY_DECISION` | `NOT_ADMITTED` |
| `NORMALIZATION` | `RAW -> WORK` | `TRANSFORM_RECEIPT`, `VALIDATION_REPORT`, `POLICY_DECISION` | `QUARANTINE` |
| `VALIDATION` | `WORK -> PROCESSED` | `VALIDATION_REPORT`, `POLICY_DECISION`; conditional redaction and aggregation receipts | `STAY_WORK` |
| `CATALOG_CLOSURE` | `PROCESSED -> CATALOG` | `CATALOG_MATRIX`, `EVIDENCE_BUNDLE`, `POLICY_DECISION`; conditional graph and model-run artifacts | `HOLD_PROCESSED` |
| `RELEASE` | `CATALOG -> PUBLISHED` | `RELEASE_MANIFEST`, `ROLLBACK_TARGET`, `CORRECTION_PATH`, `POLICY_DECISION`; conditional review record | `HOLD_CATALOG` |
| `CORRECTION` | `PUBLISHED -> PUBLISHED_SUPERSEDED` | `CORRECTION_NOTICE`, `REVIEW_RECORD`, `INVALIDATION_LIST`, `RELEASE_MANIFEST`, `POLICY_DECISION` | `STALE_STATE_ANNOUNCEMENT` |
| `ROLLBACK` | `PUBLISHED -> PRIOR_RELEASE` | `ROLLBACK_CARD`, `CORRECTION_NOTICE`, `INVALIDATION_LIST`, `RELEASE_MANIFEST`, `POLICY_DECISION` | `HOLD_CURRENT_RELEASE` |

The source carrier marks some reason-code spelling and the A-G content-check mapping as proposed. This profile therefore owns only its local `GATE_*` diagnostic vocabulary; it does not canonicalize the carrier's broader catalog.

## Closure algorithm

The validator derives the decision in this order:

1. `assessment_state = ERROR` yields `ERROR / ASSESSMENT_ERROR`.
2. An invalid required artifact or dependency yields `DENY` and preserves the prior stage.
3. A missing or unresolved required artifact or dependency fails closed. `VALIDATION` yields `DENY / STAY_WORK`; the other gates yield `HOLD` with their declared disposition.
4. Only an exact gate-specific artifact set, every required artifact and dependency resolved, and a resolved PolicyDecision dependency yields `ALLOW / ADVANCE`.

`ALLOW` means only that the synthetic packet is locally complete. The assessment's governance block fixes every operational effect to false, including the transition itself.

## Conditional requirements

- `VALIDATION` adds `REDACTION_RECEIPT` when `sensitivity_transform_required` is true.
- `VALIDATION` adds `AGGREGATION_RECEIPT` when `aggregation_required` is true.
- `CATALOG_CLOSURE` adds `GRAPH_PROJECTION` when `graph_projection_required` is true.
- Any gate may require `MODEL_RUN_RECEIPT` only when `model_run_required` is true; the model dependency must then be resolved.
- `RELEASE` adds `REVIEW_RECORD` when `review_required` is true. Correction always requires review under this profile.

Unused condition flags are rejected so that a gate cannot smuggle unrelated requirements into its meaning.

## Dependency boundary

The fixed dependency slots distinguish:

- `source_descriptor` resolution for source identity;
- `evidence_bundle` resolution where evidence closure is required;
- `model_run_receipt` resolution when a model dependency is declared; and
- `policy_decision` resolution for every gate.

A dependency that is not required must be `NOT_REQUIRED`. Missing, unresolved, invalid, or role-confused dependencies cannot be treated as closure.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the complete object after removing only `assessment_id` and `spec_hash`.

```text
spec_hash      = SHA-256(JCS(identity subject))
assessment_id  = kfm:lifecycle-gate-closure:<first 24 digest hex>
```

Artifact order is lexical by role. Duplicate roles, unstable ordering, identity drift, or a stored decision that differs from the derived result fail closed.

## Directory Rules basis

Cross-family lifecycle-gate meaning belongs under `contracts/governance/`; machine shape under `schemas/contracts/v1/governance/`; synthetic cases under `fixtures/contracts/v1/governance/`; reusable validation under `tools/validators/governance/`; executable evidence under `tests/validators/governance/`; read-only orchestration under `.github/workflows/`; exploratory source adaptation under `docs/intake/exploratory/`; and AI authoring accountability under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. The packet creates no lifecycle store, policy engine, evidence resolver, receipt authority, release lane, public API, dashboard, or publication path.

## Validation

```bash
python -m unittest -v tests.validators.governance.test_validate_lifecycle_gate_closure_assessment
python tools/validators/governance/validate_lifecycle_gate_closure_assessment.py --fixtures
```

## Non-effects and rollback

A passing fixture does not prove that a source, artifact, EvidenceBundle, ModelRunReceipt, PolicyDecision, review, release manifest, correction record, rollback record, or lifecycle object exists. It grants no authority to move or publish data.

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive packet. No live source, lifecycle state, policy decision, release, deployment, cache, or public artifact requires operational rollback.
