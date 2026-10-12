<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pipeline-replay-assessment-source-map
title: Pipeline Replay Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · Pipeline steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded mapping from a Drive Full Atlas replay proposal to a bounded repository comparison profile without treating proposal material as execution evidence or authority
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/validation/pipeline_replay_assessment.md
  - ../../../contracts/governance/recompile_manifest.md
  - ../../../contracts/runtime/replay_safe_effect_ledger.md
  - ../../../contracts/runtime/run_receipt.md
tags: [kfm, atlas, pipeline, replay, drift, source-map]
[/KFM_META_BLOCK_V2] -->

# Pipeline Replay Assessment Source Map

## Drive source lineage

The Google Doc `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) contains the programming card **Replay Verification of Pipelines and Receipts Implementation Surface**. Its normalized proposal says KFM should pin source snapshots, transform parameters, model identity, and validator versions; replay drift should be finite `FAIL` with a structured reason code.

The card cites `SRC-DOCTRINE`, `SRC-AIBOC`, `SRC-ATLAS-V11`, and `SRC-BUILD`. Those sources motivate reproducibility and accountable build behavior. They do not prove that a replay harness, pipeline run, receipt, model, or validator exists or ran in the repository.

## Bounded adaptation

| Source concept | Retained here | Deferred |
|---|---|---|
| Pin source snapshots | Sorted exact source reference and digest array. | Resolving or retrieving source bytes. |
| Pin transform parameters | One exact parameter-set digest. | Executing transform code. |
| Pin model identity | Provider, model, version, and artifact digest. | Calling, loading, approving, or evaluating a model. |
| Pin validators | Sorted reference, version, and artifact digest array. | Running or approving validators. |
| Report replay drift | Reproduced `PASS` or `FAIL` plus closed drift codes. | Claiming that a real replay or equivalence proof occurred. |

## Repository reconciliation

- `RunReceipt` records runtime execution provenance; this candidate cannot issue or attest one.
- `RecompileManifest` binds one fixture-only query/proposal recompilation and no-write output. It is not a generic pipeline pin comparison.
- `ReplaySafeEffectLedger` governs duplicate delivery and idempotent side-effect history. It is not deterministic output replay.
- Source snapshots, transform contracts, model cards, validator assurance, policy, review, release, and publication retain their existing authorities.
- Repository search at base `1ab34018d7fb13ad41cfe8a79aed5d4763e58bf8` found no complete generic object comparing all five proposed replay dimensions outside source/proposal material.

## Path decision

~~~yaml
path_decision:
  artifact: PipelineReplayAssessmentCandidate
  proposed_path: contracts/validation/pipeline_replay_assessment.md
  artifact_kind: semantic contract
  authority_owner: validation assurance for replay pin comparison
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: object_family
  scope_id: pipeline-replay-assessment
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - Google Drive KFM_Full_Atlas_seed_cards
  rules:
    - DIR-SIGNATURE-001
    - DIR-AUTHROOT-001
    - DIR-SCOPELANE-004
    - DIR-DEP-001
  outcome: PLACE
~~~

## Non-effects

This packet does not resolve sources, execute a pipeline or transform, invoke a model, run validators, attest a receipt, write lifecycle state, establish output truth, evaluate policy, approve review, authorize release, publish, or permit public use.
