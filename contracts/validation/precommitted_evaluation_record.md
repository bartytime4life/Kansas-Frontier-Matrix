<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/precommitted-evaluation-record
title: PrecommittedEvaluationRecord Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Validation steward · Evidence steward · Review steward
created: 2026-08-25
updated: 2026-08-25
policy_label: internal; validation; preregistration; scoring; deterministic; fail-closed
owning_root: contracts/
responsibility: fixture-only verification of a sealed precommitment, evaluation timing, intervention disclosure, outcome coverage, and exact Brier scoring
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../schemas/contracts/v1/validation/precommitted_evaluation_record.schema.json
  - ../../fixtures/contracts/v1/validation/precommitted_evaluation_record/cases.json
  - ../../tools/generators/precommitted_evaluation_record/build_precommitted_evaluation_record.py
  - ../../tools/validators/validate_precommitted_evaluation_record.py
  - ../../tests/validators/test_validate_precommitted_evaluation_record.py
  - ../../docs/intake/exploratory/cairnwake-precommitted-evaluation-source-map.md
tags: [kfm, validation, preregistration, commitment, reveal, brier, fixture]
[/KFM_META_BLOCK_V2] -->

# PrecommittedEvaluationRecord Candidate Contract

PrecommittedEvaluationRecord verifies that a revealed synthetic evaluation payload matches a commitment published before its observation window, that interventions are disclosed, that every preregistered prediction has one observed outcome, and that exact Brier scoring is reproducible.

## Commit and reveal

The commitment is SHA-256 over the repository RFC 8785 JCS encoding of sealed_payload. The declared publication time must precede the evaluation window. Reveal may not occur before the window closes. The candidate carries both the revealed payload and commitment so a validator can reproduce the check without network access.

## Predictions and scoring

Predictions are sorted and unique by prediction_id. Each declares an event definition, an explicit falsifier, and confidence_basis_points from 0 through 10000. Outcomes are sorted, unique, and cover the prediction set exactly.

For prediction confidence p in basis points and observed value y in {0, 10000}, squared_error_basis_points_2 is (p - y)^2. The mean Brier score is stored as an exact fraction with numerator equal to the sum of squared errors and denominator equal to prediction_count multiplied by 100000000. No floating-point rounding or curve adjustment is permitted.

## Interventions

Every disclosed intervention is ordered by timestamp and must fall between commitment publication and reveal. The record does not claim the list is complete; validator PASS means only that the declared list is canonical and internally bounded. A real evaluation would require independent evidence and review.

## Validator outcomes

PASS means schema, seal, temporal order, inventories, score, identity, and non-authority fields agree. DENY identifies an incoherent candidate. ERROR identifies unsafe JSON input. PASS does not make a prediction true, establish calibration, authenticate an observation, approve an intervention, or authorize publication.

## Authority boundary and rollback

The profile is fixture-only, no-network, and non-mutating. It does not publish a commitment, collect observations, authenticate evidence, run an experiment, update a scoreboard, approve review, or create release, deployment, publication, or public-use authority. Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive commit; no external state requires correction.
