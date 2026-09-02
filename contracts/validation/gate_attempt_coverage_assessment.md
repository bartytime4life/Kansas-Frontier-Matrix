<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/gate-attempt-coverage-assessment
title: GateAttemptCoverageAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Validation steward · Runtime steward · Audit steward
created: 2026-08-28
updated: 2026-08-28
policy_label: internal; validation; gate-accounting; deterministic; fail-closed
owning_root: contracts/
responsibility: fixture-only verification that every guarded-action attempt is classified, terminal classes remain distinct, and reported metric denominators declare their complete class population
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../schemas/contracts/v1/validation/gate_attempt_coverage_assessment.schema.json
  - ../../fixtures/contracts/v1/validation/gate_attempt_coverage_assessment/cases.json
  - ../../tools/generators/gate_attempt_coverage_assessment/build_gate_attempt_coverage_assessment.py
  - ../../tools/validators/validate_gate_attempt_coverage_assessment.py
  - ../../tests/validators/test_validate_gate_attempt_coverage_assessment.py
  - ../../docs/intake/exploratory/cairnwake-gate-attempt-coverage-source-map.md
tags: [kfm, validation, gate, attempts, refusals, coverage, denominator, fixture]
[/KFM_META_BLOCK_V2] -->

# GateAttemptCoverageAssessment Candidate Contract

GateAttemptCoverageAssessment is a fixture-only validation object for detecting survivorship bias in guarded-operation reporting. It accounts for one bounded attempt population without retaining submitted payloads or sensitive values.

## Attempt population

Every attempted guarded action is assigned to exactly one class:

- `ADMITTED` — the gate admitted the guarded action and the action occurred within the declared synthetic record;
- `REFUSED` — the gate refused the action; the refusal does not prove the guarded action occurred;
- `ERROR` — processing failed without confirming the guarded action occurred;
- `UNOBSERVED` — an attempt reference exists but no terminal record was observed.

The declared invariant is:

`attempted_count = admitted_count + refused_count + error_count + unobserved_count`

Each class count must equal its reference-row count. Attempt references are unique across the population. Terminal record references are unique across admitted, refused, and error classes. The four classes use distinct signature domains so a refusal or error cannot be reinterpreted as an admission record.

## Denominators and feedback

Every reported metric denominator declares both included and excluded attempt classes. Those sets must be disjoint, canonical, and together cover all four classes. The declared denominator count is reproduced from the included class counts.

A refusal record has `guarded_action_occurrence = DID_NOT_OCCUR` and `same_gate_feedback_allowed = false`. A refusal may be counted as a refusal, but it must not serve as evidence that the guarded action occurred or feed the same gate in a way that manufactures later refusals. Error and unobserved classes likewise cannot confirm the guarded action.

## References and carrier boundary

Rows carry opaque KFM references and signature-domain labels only. Rejected payloads, addresses, messages, credentials, personal data, and sensitive values are prohibited from this candidate surface.

The repository currently records the `run_receipt` family as `CONFLICTED` across runtime, source, source-event, and release-bound variants. This candidate therefore selects no live receipt carrier and creates no parallel receipt authority. Its references are synthetic fixtures. Any live integration requires a separately reviewed carrier decision, producer and consumer mapping, retention policy, rights and sensitivity review, and migration or compatibility plan.

## Validator outcomes

`PASS` means the candidate is schema-valid, its attempt population reconciles, reference roles and signature domains remain distinct, denominator declarations are complete, refusal semantics are fail-closed, terminal coverage state is truthful, and deterministic identity reproduces. `DENY` identifies an incoherent candidate. `ERROR` identifies unsafe JSON input.

`PASS` does not prove delivery, authenticate a real attempt or terminal record, configure a gate, permit feedback, admit a source, approve review, or authorize merge, lifecycle mutation, release, deployment, publication, or public use.

## Authority boundary and rollback

The profile is `PROPOSED_INACTIVE`, fixture-only, no-network, and non-mutating. Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive commit. No source, gate, lifecycle, data, release, deployment, or public state requires correction.
