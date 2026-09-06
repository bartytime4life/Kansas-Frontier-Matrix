<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/pipeline-replay-assessment
title: PipelineReplayAssessment Candidate Contract
type: semantic-contract
version: v1.1.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Pipeline steward · Validation steward · Receipt steward
created: 2026-08-09
updated: 2026-09-06
policy_label: internal; validation; pipeline-replay; deterministic; fail-closed
maturity: repository-grounded; fixture-and-validator-backed; historical-hosted-run-backed; current-main-replay-unverified; non-authoritative
owning_root: contracts/
responsibility: fixture-only deterministic comparison of replay pins and observations without running a pipeline or claiming a real replay occurred
truth_posture: CONFIRMED current repository packet and historical exact-head workflow evidence / PROPOSED inactive comparison profile / NEEDS VERIFICATION current-main rerun, independent steward review, and runtime consumer admission
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
  - ../../.github/workflows/pipeline-replay-assessment.yml
  - ../../data/receipts/generated/genrec-pipeline-replay-assessment-20260809.json
  - ../../tools/ci/install_python_ci.py
  - ../../tools/ci/python-dependency-lock-migration.json
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 5efb430268fb59fccc0b1332d187615f5c063b10
  branch_merge_base: 23c3487a1731f9558a6efc7143be65966f59efd5
  previous_contract_blob: 154f67fbb69ad179b062e02fc3f1bbf85fc497dd
  target_path_history: "Only implementation commit observed: 2c7062a51fdb4b5b2c0a76bfb02bf502fc3d9161; no later target-path commit through current main@5efb430268fb59fccc0b1332d187615f5c063b10"
  source_packet_pr: 2398
  source_packet_head: 9b200d2733d899c1ca69e4b014fd9430362249f9
  source_packet_merge_commit: 6f582f8bbbc0934b69ee433c4b092c96af611436
  schema_blob: 5a0d60a41771176869cae478be6c4049fbe60f21
  fixture_manifest_blob: fb57d7444525f181984dab4e3cbfae2cc44288e6
  validator_blob: 33320e1e904fb4e6e059104a86fbd73cfc54314a
  focused_tests_blob: 6b2a59eaed60cdd56c58d139a8e054fd584e0d3d
  source_map_blob: 15892580f1a33f999c5cee5d49669f161ab0aac3
  current_workflow_blob: 14a4f308810216bbdc52e20cd38d7efc0c2f264f
  historical_workflow_blob: e4e2a4b8b99354f4b7c01822734ee03ae4c30cd6
  authoring_receipt_blob: 1475c02e0ed6617cdf472e4625c79639744d5711
  workflow_migration_manifest_blob: 9a28ba458535cad825d0b8529e7d118fef8eb247
  fixture_corpus: "14 cases: 7 validator PASS cases (one matching profile, five single-dimension drifts, one multi-drift case) and 7 DENY cases; PASS cases produce both replay PASS and replay FAIL outcomes"
  historical_hosted_run: "GitHub Actions run 31351078454, job 93341901442, success; associated with PR head 9b200d2733d899c1ca69e4b014fd9430362249f9 and checked out merge ref 53797f6dec766029dee0a9d379747ead29cf9977"
  historical_run_observation: "11 focused tests passed, fixture CLI returned cases=14/failures=0/suite_match=true, and generated-receipt integrity returned valid with review=pending"
  current_main_hosted_run: "NEEDS VERIFICATION — PR-triggered workflow readback for main@5efb430268fb59fccc0b1332d187615f5c063b10 returned no runs; the push-triggered current-main result was not established"
  receipt_boundary: "The 2026-08-09 receipt remains historical and immutable; it binds the pre-refresh contract bytes and is not current-main replay or review authority"
tags: [kfm, validation, pipeline, replay, drift, fixture, currentness]
notes:
  - "Adapts the Drive Full Atlas card Replay Verification of Pipelines and Receipts Implementation Surface; the source proposal remains PROPOSED."
  - "Version v1.1.0 is a repository-evidence/currentness refresh only; it does not change field meaning, canonicalization, outcome vocabulary, denied authorities, or activation posture."
  - "A matching declaration is not proof that a pipeline ran or that any output is true, admissible, reviewed, released, or public."
  - "The historical generated receipt is preserved rather than rewritten; receipt/workflow successor handling is a separate dependency-closed decision."
[/KFM_META_BLOCK_V2] -->

# PipelineReplayAssessment Candidate Contract

PipelineReplayAssessmentCandidate is a repository-present, fixture-only comparison profile. It compares one pinned replay profile with one declared replay observation so source snapshots, transform parameters, model identity, validator identities, and output digest drift remain independently inspectable. It does not turn those declarations into a pipeline runner or a real replay proof.

Version v1.1.0 reconciles the original packet with current main and historical hosted evidence. It does not change the candidate's semantic fields, canonicalization, finite outcomes, or authority boundary.

## Source-derived gap

The Google Drive Full Atlas card Replay Verification of Pipelines and Receipts Implementation Surface proposes a replay harness that pins source snapshots, transform parameters, model identity, and validator versions, with replay drift represented as finite FAIL plus a structured reason code. The repository source map records the same proposal and its bounded adaptation.

The source card remains design input. It does not prove that a replay harness, pipeline run, receipt, model, or validator exists or ran. The current repository packet proves only the narrower fixture comparison surface described below.

## Current status and evidence

| Evidence surface | Current bounded reading |
|---|---|
| Semantic and activation status | PROPOSED_INACTIVE, fixture-only, and non-authoritative. No source, pipeline, model, validator, lifecycle, release, publication, or public-use authority is created. |
| Repository packet | Current main contains this contract path plus the closed schema, 14-case fixture manifest, deterministic validator, 11-test focused suite, source map, read-only workflow, and generated authoring receipt. The pins are recorded in the metadata block. |
| Schema | The machine profile is marked PROPOSED, uses a closed Draft 2020-12 object, and declares the comparison and governance fields required by this contract. |
| Fixture corpus | Seven cases validate successfully: one exact match, five single-dimension drift cases, and one multiple-drift case. Seven cases are DENY cases covering report, identity, profile binding, canonical-order, and governance/schema failures. |
| Historical hosted execution | PR #2398's pipeline-replay-assessment run 31351078454 completed successfully. The associated job passed all steps, ran 11 focused tests, replayed all 14 fixture cases, and validated the historical generated receipt. |
| Current-main execution | NEEDS VERIFICATION. The historical run is tied to the original PR merge ref, not current main. No current-main hosted pass is claimed. |
| Receipt status | The historical 2026-08-09 generated receipt remains unchanged and binds the pre-refresh artifact set. It is process memory, not review, proof, release, or current-main authority. |
| Runtime adoption | UNKNOWN. This packet adds no runtime consumer, source adapter, pipeline executor, model call, validator orchestration, lifecycle writer, release gate, or public route. |

The historical receipt reported an adjacent ReplaySafeEffectLedger suite failure caused by an unrelated pre-existing syntax-corrupted file at the time of authoring. That failure was outside this packet and remains historical evidence; it is not relabeled as a current result.

## Authority boundary

This profile validates declarations only. It does not:

- resolve a source snapshot or retrieve source bytes;
- execute a transform or pipeline;
- call, load, approve, or evaluate a model;
- run a referenced validator;
- compare real artifact bytes or establish output truth;
- issue or attest a RunReceipt;
- mutate RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state;
- evaluate policy, authenticate review, approve promotion, release, deployment, or publication; or
- authorize public use.

A validator PASS is a bounded conformance result. It is not evidence that a real replay happened.

## Compared records

The records remain deliberately distinct:

- replay_profile is the expected pin set;
- replay_observation is the declared observed pin set and output digest; and
- report is reproduced from exact comparison of those records.

The observation binds the exact replay profile reference. The comparison never infers missing execution evidence.

## Finite report

| Outcome | Meaning |
|---|---|
| PASS | All pinned declarations and the output digest match exactly. |
| FAIL | One or more comparison dimensions drifted; every drift dimension is named by a structured code. |

The closed v1 drift codes are SOURCE_SNAPSHOT_DRIFT, TRANSFORM_PARAMETERS_DRIFT, MODEL_IDENTITY_DRIFT, VALIDATOR_SET_DRIFT, and OUTPUT_DRIFT. A report may contain several codes, sorted and unique. Neither report outcome proves that replay execution occurred.

## Deterministic comparison

- Source pins are sorted by source_ref, unique, and compared as complete arrays.
- Validator pins are sorted by validator_ref, unique, and compare reference, version, and artifact digest.
- Transform parameters compare one SHA-256 digest.
- Model identity compares provider, model, version, and artifact digest as one object.
- Output compares one SHA-256 digest.
- The observation binds the exact replay profile reference.
- spec_hash is RFC 8785 JCS plus SHA-256 over the candidate excluding only assessment_id and spec_hash.
- assessment_id uses the first 24 hexadecimal characters of the resulting digest.
- Every execution and governance effect remains false.

The validator also fails closed on duplicate JSON keys, non-finite numbers, symlink inputs, oversized JSON input, schema violations, non-canonical inventories, identity tampering, and report mismatch. The bounded input budget is 1 MiB. The validator source contains no network, pipeline, model, or runtime client.

## Validator meaning

Validator PASS means the declaration, reproduced report, deterministic identity, canonical inventories, and non-authority fields agree. It can accompany report outcome PASS or FAIL.

Validator DENY identifies an incoherent declaration, report, or identity. ERROR identifies unsafe JSON input. Neither outcome grants execution, evidence, review, policy, lifecycle, promotion, release, deployment, publication, or public-use authority.

## Directory Rules basis

ADR-0029's accepted placement decision and the repository's Directory Rules evidence place semantic validation-assurance meaning under contracts/validation/. Machine shape belongs under schemas/contracts/v1/validation/; fixtures, executable validation, focused tests, read-only CI, source mapping, dependency-install controls, and authoring accountability remain in their established roots.

This packet creates no pipeline runner, receipt authority, lifecycle state, model integration, policy, release, publication, or parallel schema/contract home.

## Validation

The dedicated workflow currently installs the declared project-test profile through the repository-owned locked installer, then runs the focused suite, fixture CLI, generated-receipt validation, and trust-boundary summary:

~~~bash
python tools/ci/install_python_ci.py project-test
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_pipeline_replay_assessment.py' \
  --verbose
python tools/validators/validate_pipeline_replay_assessment.py --fixtures
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-pipeline-replay-assessment-20260809.json \
  --repo-root .
~~~

The historical hosted run passed the then-current workflow and these bounded checks on the PR merge ref. The workflow later changed its dependency-install step to the locked installer; that migration is governed by tools/ci/python-dependency-lock-migration.json. The migration ledger does not convert the historical run into current-main proof.

## Source and adjacent boundaries

- RunReceipt records runtime execution provenance; this candidate cannot issue or attest one.
- RecompileManifest binds one fixture-only query/proposal recompilation and no-write output. It is not a generic pipeline pin comparison.
- ReplaySafeEffectLedger governs duplicate delivery and idempotent side-effect history. It is not deterministic output replay.
- ValidatorAssuranceReport records bounded validator mutation-assurance evidence. It does not approve this profile or establish a universal replay threshold.
- Source snapshots, transform contracts, model cards, validator assurance, policy, review, release, and publication retain their existing authorities.

## Receipt and currentness boundary

The generated receipt from the original packet is retained as historical process memory and is not rewritten by this contract refresh. Its historical hosted run is useful evidence for the original packet at its exact merge ref, but it is not a current-main run and does not authenticate human review.

Any successor receipt, workflow-pointer change, or migration-ledger change must be handled as a separate dependency-closed change. It must preserve the original receipt bytes, bind the final artifact set, record exact validation outcomes, and remain subordinate to independent review and repository controls.

## Non-effects and rollback

This packet cannot run or certify a pipeline, attest a receipt, establish reproducibility of a real build, approve a model or validator, evaluate policy, approve review, promote, release, deploy, publish, or permit public use.

Rollback is additive and reversible: revert the currentness-refresh contract commit or the complete draft branch. Preserve the original PR #2398 merge, historical workflow run, generated receipt, schema, fixtures, validator, tests, and source map as historical lineage. No external runtime or lifecycle state is changed by this document.
