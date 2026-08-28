<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/public-map-service-slo-assessment
title: PublicMapServiceSLOAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Validation steward · Map runtime steward · Release steward · Reliability steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; validation; map-service; slo; error-budget; rollback-review
responsibility: Define a fixture-only assessment of declared public-map-service availability, latency, and error-budget arithmetic without monitoring a live service, setting production thresholds, or changing promotion, rollback, release, deployment, or publication state.
truth_posture: "CONFIRMED supplied-card traceability, Drive corroboration, and bounded repository gap; PROPOSED inactive assessment contract; UNKNOWN production objectives and consumer adoption; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ./pipeline_replay_assessment.md
  - ../release/operational_trust_rollup.md
  - ../release/promotion_decision.md
  - ../release/rollback_card.md
  - ../../schemas/contracts/v1/validation/public_map_service_slo_assessment.schema.json
  - ../../fixtures/contracts/v1/validation/public_map_service_slo_assessment/cases.json
  - ../../tools/validators/validate_public_map_service_slo_assessment.py
  - ../../tests/validators/test_validate_public_map_service_slo_assessment.py
  - ../../docs/intake/exploratory/pass-18-public-map-service-slo-assessment-source-map.md
tags: [kfm, validation, map-service, slo, error-budget, latency, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-500."
  - "A PASS proves bounded declaration and arithmetic coherence only; it does not prove live availability or authorize promotion, rollback, release, deployment, publication, or public use."
[/KFM_META_BLOCK_V2] -->

# PublicMapServiceSLOAssessment Candidate

`PublicMapServiceSLOAssessmentCandidate` is a bounded, fixture-only declaration for reviewing one synthetic public-map-service measurement window. It makes the declared availability objective, latency objective, error-budget arithmetic, supporting references, and finite assessment outcome inspectable without contacting a service or treating operational telemetry as map or evidence truth.

The candidate implements the narrow requirement in supplied Pass 18 card `KFM-P18-INV-500`: public map services should have SLO and error-budget checks that can inform promotion holds or rollback review without turning telemetry into truth content. This first packet does not create the operational gate. It validates only a closed synthetic candidate and explicitly leaves production objectives unresolved outside referenced policy.

## Boundary

A validator `PASS` proves only that:

- the closed candidate shape, deterministic hash, and assessment identity replay;
- the measurement window is complete and ordered;
- a declared SLO policy reference is present;
- availability and error-budget counts agree using exact integer arithmetic;
- latency state agrees with the declared target and observation;
- telemetry, review, and rollback references are present and canonical;
- the finite report is reproduced from the candidate; and
- every authority claim remains false.

The validator does not query a service, authenticate telemetry, establish a production objective, decide policy or review, mutate a PromotionDecision or RollbackCard, release, deploy, publish, or authorize public use.

## Deterministic arithmetic

Availability objectives use basis points rather than floating-point values. For `eligible_events = E` and `target_basis_points = T`, the allowed bad-event budget is:

`floor(E × (10000 - T) / 10000)`

Observed bad events equal `eligible_events - good_events`. Remaining budget equals allowed bad events minus observed bad events and may be negative when the budget is exhausted. The validator reproduces all three fields and the declared `WITHIN_BUDGET` or `EXHAUSTED` state.

Latency is a separately declared percentile objective. The candidate records only the percentile label, target milliseconds, observed milliseconds, sample count, and derived state. It does not validate the upstream sampling method or telemetry receipt.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The complete synthetic declaration is coherent, within its referenced objectives, and carries the required review and rollback references. |
| `ABSTAIN` | Measurement, policy, telemetry, review, rollback, or latency support is explicitly incomplete or unresolved. |
| `DENY` | The declared error budget is exhausted, latency is breached, arithmetic or identity is inconsistent, or another fail-closed invariant is violated. |
| `ERROR` | The candidate cannot be parsed or safely evaluated, fails schema validation, or explicitly declares assessment error. |

`DENY` does not itself block promotion or execute rollback. It means only that this candidate cannot support promotion and should be routed to the separate release and rollback authorities named by its references.

## Service kinds

The closed fixture vocabulary distinguishes `STATIC_PMTILES`, `STATIC_COG`, `SERVER_MEDIATED_LAYER`, `GOVERNED_MAP_API`, and `COMPOSITE_MAP_SURFACE`. The vocabulary does not decide which objectives are mandatory for any production service kind; that remains a policy and reliability-review question.

## Directory Rules basis

The object owns validation meaning—whether a declared SLO window and error budget are internally coherent—so its semantic contract belongs under `contracts/validation/`. Machine shape, synthetic replay, repository validation, executable conformance, read-only CI, source reconciliation, and AI-authoring accountability remain under `schemas/`, `fixtures/`, `tools/`, `tests/`, `.github/workflows/`, `docs/intake/exploratory/`, and `data/receipts/generated/` respectively.

Release, rollback, telemetry, evidence, policy, runtime, and public-surface authority remain in their existing roots and are referenced only. No monitoring service, telemetry emitter, metric store, production threshold, release gate, rollback executor, deployment path, or public route is created.

## Validation

    python -m unittest tests.validators.test_validate_public_map_service_slo_assessment -v
    python tools/validators/validate_public_map_service_slo_assessment.py --fixtures

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no service, telemetry stream, evidence object, policy, review, lifecycle record, promotion, rollback, release, deployment, or public artifact.
