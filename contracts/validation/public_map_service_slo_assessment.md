<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/public-map-service-slo-assessment
title: PublicMapServiceSLOAssessment Candidate Contract
type: semantic-contract
version: v1.1.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Validation steward · Map runtime steward · Release steward · Reliability steward
created: 2026-08-11
updated: 2026-09-06
maturity: repository-grounded; fixture-packet-backed; hosted-currentness-unverified; non-authoritative
owning_root: contracts/
policy_label: internal; validation; map-service; slo; error-budget; rollback-review
responsibility: Define a fixture-only assessment of declared public-map-service availability, latency, and error-budget arithmetic without monitoring a live service, setting production thresholds, or changing promotion, rollback, release, deployment, or publication state.
truth_posture: "CONFIRMED current repository packet, supplied-card/source-map traceability, and Drive doctrine corroboration; PROPOSED inactive assessment contract and fixture matrix; UNKNOWN production objectives, runtime consumer adoption, and current hosted acceptance; NEEDS VERIFICATION human review and exact-head CI"
related:
  - ./pipeline_replay_assessment.md
  - ../release/operational_trust_rollup.md
  - ../release/promotion_decision.md
  - ../release/rollback_card.md
  - ../../schemas/contracts/v1/validation/public_map_service_slo_assessment.schema.json
  - ../../fixtures/contracts/v1/validation/public_map_service_slo_assessment/cases.json
  - ../../tools/validators/validate_public_map_service_slo_assessment.py
  - ../../tests/validators/test_validate_public_map_service_slo_assessment.py
  - ../../.github/workflows/public-map-service-slo-assessment.yml
  - ../../docs/intake/exploratory/pass-18-public-map-service-slo-assessment-source-map.md
  - ../../docs/architecture/map-master/PERFORMANCE_BUDGETS.md
  - ../../data/receipts/generated/genrec-pass18-public-map-service-slo-assessment-20260811.json
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 23c3487a1731f9558a6efc7143be65966f59efd5
  prior_contract_blob: b3e1f8cce81f34531220e9d3387a412941700dce
  schema_blob: 9bf95e421b871dbe5d21ab076e1569fe6cd24a51
  fixture_blob: 73cb28f0d4c0456ea265c0f9d9a1f6a69d98b683
  validator_blob: 82493f9d5bbd800f1db3852544d5a8e739a70ca0
  focused_tests_blob: c98844dbb7409be322d30ce10721f66e7c90788b
  workflow_blob: aebe9d84f28afaec58655d2b3f340843064a1827
  source_map_blob: 23c8cb0f3d6276d51229b82a2c1919d1cc853a18
  performance_budgets_blob: c800cdd8d622ca2a4596cf80e9951f241fc70187
  historical_receipt_blob: 4443cb94e040d88d7461df06e0e6bd777f61a6be
  fixture_cases: 34
  focused_tests: 11
  service_kinds: 5
  validator_registry_entry: "No matching entry observed; the dedicated workflow invokes the validator directly."
  current_main_workflow_readback: "No workflow runs or combined status results returned for main@23c3487a1731f9558a6efc7143be65966f59efd5 at readback"
tags: [kfm, validation, map-service, slo, error-budget, latency, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-500."
  - "A PASS proves bounded declaration and arithmetic coherence only; it does not prove live availability or authorize promotion, rollback, release, deployment, publication, or public use."
  - "Version v1.1.0 is a repository-evidence/currentness refresh; it does not establish production objectives, runtime consumption, validator-registry admission, or hosted acceptance."
[/KFM_META_BLOCK_V2] -->

# PublicMapServiceSLOAssessment Candidate

`PublicMapServiceSLOAssessmentCandidate` is a bounded, fixture-only declaration for reviewing one synthetic public-map-service measurement window. The repository now carries a schema, 34-case fixture matrix, deterministic validator, 11-test focused suite, dedicated no-network workflow, and historical receipt; none is a live monitoring or release authority. The declaration makes the availability objective, latency objective, error-budget arithmetic, supporting references, and finite assessment outcome inspectable without contacting a service or treating operational telemetry as map or evidence truth.

The candidate implements the narrow requirement in supplied Pass 18 card `KFM-P18-INV-500`: public map services should have SLO and error-budget checks that can inform promotion holds or rollback review without turning telemetry into truth content. This packet remains fixture-only and does not create the operational gate. It validates only a closed synthetic candidate and explicitly leaves production objectives, telemetry authenticity, runtime consumption, and consumer adoption unresolved outside separately governed policy and release authorities.

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

### Current implementation evidence

| Surface | Bounded readback |
|---|---|
| Fixture matrix | 34 exact PASS, ABSTAIN, DENY, and ERROR cases are materialized in the controlled fixture manifest. |
| Focused suite | 11 deterministic unittest methods cover service kinds, arithmetic, latency, identity, support references, finite outcomes, schema errors, duplicate JSON, and no-network behavior. |
| Dedicated workflow | The workflow sets `KFM_NO_NETWORK=1`, compiles the validator/tests, runs the focused suite and fixture replay, validates the historical generated receipt, and records the trust boundary. |
| Adjacent performance posture | `docs/architecture/map-master/PERFORMANCE_BUDGETS.md` remains fixture-first and non-authoritative; production profiles and deployed performance remain unresolved. |
| Validator registry | No matching `public-map-service-slo-assessment` entry was observed in `tools/validators/validator_registry.json`; the dedicated workflow invokes this validator directly and does not create a runtime registry. |
| Current main | `main@23c3487a1731f9558a6efc7143be65966f59efd5`; no workflow runs or combined status results were returned for that merge commit at readback. |

These are repository and historical-receipt facts, not production SLO evidence. They do not establish live availability, latency, telemetry authenticity, a production threshold, policy acceptance, review approval, promotion, rollback execution, release, deployment, publication, or public use.

## Deterministic arithmetic

Availability objectives use basis points rather than floating-point values. For `eligible_events = E` and `target_basis_points = T`, the allowed bad-event budget is:

`floor(E × (10000 - T) / 10000)`

Observed bad events equal `eligible_events - good_events`. Remaining budget equals allowed bad events minus observed bad events and may be negative when the budget is exhausted. The validator reproduces all three fields and the declared `WITHIN_BUDGET` or `EXHAUSTED` state.

Latency is a separately declared percentile objective. The candidate records only the percentile label, target milliseconds, observed milliseconds, sample count, and derived state. It does not validate the upstream sampling method or telemetry receipt. The controlled schema contains no floating-point fields for the declared objectives or observations; this still does not validate upstream sampling, clock quality, telemetry delivery, or service health.

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

The current packet is enforced by its dedicated read-only workflow rather than by a validator-registry entry. That implementation detail does not expand the semantic authority of this contract and must not be treated as a runtime admission path.

## Validation

The dedicated workflow's focused command set is:

    python -m py_compile tools/validators/validate_public_map_service_slo_assessment.py tests/validators/test_validate_public_map_service_slo_assessment.py
    python -m unittest tests.validators.test_validate_public_map_service_slo_assessment --verbose
    python tools/validators/validate_public_map_service_slo_assessment.py --fixtures
    python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-pass18-public-map-service-slo-assessment-20260811.json --repo-root .

The historical receipt records PASS for syntax, schema metadata, workflow parsing, the focused suite, 34-case fixture replay, adjacent release/map regressions, documentation metadata and links, no-network boundaries, receipt hash replay, and diff hygiene. It also records a full-validator discovery failure—five failures and thirteen errors in three pre-existing validator modules—reproduced by an exact 31-test replay on the untouched base; the 11 new SLO tests passed inside that run.

Hosted exact-head CI and human review were SKIPPED in that receipt. The current main readback returned no workflow run or combined status result, so this contract makes no current hosted-pass or production-readiness claim.

## Rollback

Rollback is a single-file revert of this contract currentness update to prior blob `b3e1f8cce81f34531220e9d3387a412941700dce`. Preserve the historical receipt and its original artifact hashes; rollback does not mutate a service, telemetry stream, evidence object, policy, review, lifecycle record, promotion, rollback, release, deployment, or public artifact.
