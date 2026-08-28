<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/pipeline-replay-assessment
title: PipelineReplayAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Pipeline steward · Validation steward · Receipt steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; validation; pipeline-replay; deterministic; fail-closed
owning_root: contracts/
responsibility: fixture-only deterministic comparison of replay pins and observations without running a pipeline or claiming a real replay occurred
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ./README.md
  - ./validator_assurance_report.md
  - ../runtime/run_receipt.md
  - ../runtime/replay_safe_effect_ledger.md
  - ../governance/recompile_manifest.md
  - ../../schemas/contracts/v1/validation/pipeline_replay_assessment.schema.json
  - ../../fixtures/contracts/v1/validation/pipeline_replay_assessment/cases.json
  - ../../tools/validators/validate_pipeline_replay_assessment.py
  - ../../tests/validators/test_validate_pipeline_replay_assessment.py
  - ../../docs/intake/exploratory/pipeline-replay-assessment-source-map.md
tags: [kfm, validation, pipeline, replay, drift, fixture]
notes:
  - "Adapts the Drive Full Atlas card Replay Verification of Pipelines and Receipts Implementation Surface."
  - "A matching declaration is not proof that a pipeline ran or that any output is true, admissible, reviewed, released, or public."
[/KFM_META_BLOCK_V2] -->

# PipelineReplayAssessment Candidate Contract

`PipelineReplayAssessmentCandidate` compares one pinned synthetic replay profile with one synthetic replay observation. It makes source snapshots, transform parameters, model identity, validator identities, and output digest independently inspectable so replay drift cannot collapse into an unlabeled success.

## Source-derived gap

The Drive-backed Full Atlas card **Replay Verification of Pipelines and Receipts Implementation Surface** proposes a replay harness that pins source snapshots, transform parameters, model identity, and validator versions, with replay drift represented as finite `FAIL` plus structured reasons. Existing repository contracts cover run receipts, fixture-only recompilation, and replay-safe side effects, but none of those provides this generic cross-pipeline comparison profile.

## Authority boundary

This profile validates declarations only. It does not resolve a source snapshot, execute a transform, call a model, run a validator, compare real artifact bytes, issue a run receipt, mutate lifecycle data, or authorize any result.

The two compared records are deliberately distinct:

- `replay_profile` is the expected pin set;
- `replay_observation` is the declared observed pin set and output digest; and
- `report` is reproduced from exact comparison of those two records.

## Finite report

| Outcome | Meaning |
|---|---|
| `PASS` | All pinned declarations and the output digest match exactly. |
| `FAIL` | One or more comparison dimensions drifted; every drift dimension is named by a structured code. |

The closed v1 drift codes are `SOURCE_SNAPSHOT_DRIFT`, `TRANSFORM_PARAMETERS_DRIFT`, `MODEL_IDENTITY_DRIFT`, `VALIDATOR_SET_DRIFT`, and `OUTPUT_DRIFT`. A report may contain several codes, sorted and unique. Neither report outcome proves that replay execution occurred.

## Deterministic comparison

- Source pins are sorted by `source_ref`, unique, and compared as complete arrays.
- Validator pins are sorted by `validator_ref`, unique, and compare reference, version, and artifact digest.
- Transform parameters compare one SHA-256 digest.
- Model identity compares provider, model, version, and artifact digest as one object.
- Output compares one SHA-256 digest.
- The observation binds the exact replay profile reference.
- Every execution and governance effect remains false.

`spec_hash` is RFC 8785 JCS plus SHA-256 over the candidate excluding only `assessment_id` and `spec_hash`. `assessment_id` uses the first 24 digest characters.

## Validator meaning

Validator `PASS` means the declaration, reproduced report, deterministic identity, canonical inventories, and non-authority fields agree. It can accompany report outcome `PASS` or `FAIL`. Validator `DENY` identifies an incoherent declaration, report, or identity. `ERROR` identifies unsafe JSON input.

## Directory Rules basis

This object records validation-assurance meaning—what exact replay dimensions match or drift—so semantic meaning belongs in `contracts/validation/`. Machine shape belongs in `schemas/contracts/v1/validation/`; fixtures, executable validation, tests, read-only CI, source mapping, and AI authoring accountability remain in established roots. It creates no pipeline runner, receipt authority, lifecycle state, model integration, policy, release, or publication surface.

## Non-effects and rollback

The packet cannot run or certify a pipeline, attest a receipt, establish reproducibility of a real build, approve a model or validator, evaluate policy, approve review, promote, release, deploy, publish, or permit public use. Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet; it has no runtime consumer or external state.
