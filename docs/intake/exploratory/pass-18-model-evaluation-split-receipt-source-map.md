<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-model-evaluation-split-receipt-source-map
title: Pass 18 Model-Evaluation Split Receipt Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Model-evaluation steward · Layer steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; model-evaluation; holdout
responsibility: Reconcile one supplied model-evaluation split idea with current repository evidence while withholding private discovery-source identifiers from public provenance.
truth_posture: "CONFIRMED supplied-card, current-main inspection, and bounded gap; PROPOSED inactive implementation profile; UNKNOWN real split correctness and consumer adoption; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/evidence/model_evaluation_split_receipt.md
  - ../../../contracts/evidence/predictive_layer_generalization_assessment.md
  - ../../../contracts/evidence/classification_layer_evaluation_assessment.md
  - ../../../contracts/governance/model_card_envelope.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-18, model-evaluation, train-test, spatial-holdout, leakage]
[/KFM_META_BLOCK_V2] -->

# Pass 18 Model-Evaluation Split Receipt Source Map

This map records source adaptation only; it creates no dataset, model, or evaluation authority.

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied and connected-Drive Pass 18 card KFM-P18-INV-481 | Model-assisted layers should record split method, random seed, stratification choices, and evaluation holdout scope before supporting a public explanation; spatial autocorrelation can make ordinary random splits overstate performance. | CONFIRMED source statement |
| contracts/evidence/predictive_layer_generalization_assessment.md | The existing assessment names split strategy, cross-validation posture, overfitting risk, and generalization labels, but it does not bind a deterministic split manifest, partition counts, partition digests, or explicit leakage-check evidence. | CONFIRMED adjacent contract |
| contracts/evidence/classification_layer_evaluation_assessment.md | The existing assessment records classification evaluation posture, not the reproducible partition construction for one model-assisted layer. | CONFIRMED adjacent contract |
| contracts/governance/model_card_envelope.md | The existing envelope governs model-card metadata and authority boundaries, not one evaluation split receipt. | CONFIRMED adjacent contract |
| Starting main@aaf508425818749d5c5d2b9f1cf5808f018d2535 search | No exact card ID, model-evaluation split receipt packet, matching branch, or matching pull request was found before implementation. | CONFIRMED bounded gap |
| Connected private research corpus | Used for candidate discovery and corroboration only. Private file identifiers, URLs, and copied prose are intentionally excluded. | CONFIRMED provenance boundary |

## Adaptation

The implementation is a closed synthetic process-memory candidate under the existing evidence family. It records model, layer, source-snapshot, split-manifest, method-definition, evaluation-receipt, and metric references; a seed and field choices; digest-bound TRAIN, optional VALIDATION, and TEST summaries; spatial and temporal holdout declarations; leakage-check posture; and public explanation disclosures.

The source card proposes training data, test data, model evaluation, and AIReceipt as dependencies. This packet carries only opaque or digest-bound references and counts. It deliberately stores no training rows, test rows, identifiers, labels, features, coordinates, model parameters, predictions, or private reasoning.

## Directory Rules basis

The packet uses established responsibility roots: semantic meaning in contracts/evidence/, shape in schemas/contracts/v1/evidence/, synthetic replay in fixtures/contracts/v1/evidence/, repository validation in tools/validators/evidence/, conformance evidence in tests/validators/evidence/, orchestration in .github/workflows/, source reconciliation in docs/intake/exploratory/, and authoring accountability in data/receipts/generated/.

No data lane, model registry, feature store, evaluation service, evidence authority, policy authority, review authority, release path, deployment surface, or public route is introduced.

## Non-effects and rollback

A local PASS authenticates no dataset, partition membership, leakage result, model, layer, metric, performance, generalization, evidence, policy, review, release, deployment, publication, or public-use state. Rollback is one additive revert with no model or external-state cleanup.
