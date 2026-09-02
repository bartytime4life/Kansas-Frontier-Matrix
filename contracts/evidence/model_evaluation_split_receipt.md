<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/model-evaluation-split-receipt
title: ModelEvaluationSplitReceiptCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Model-evaluation steward · Layer steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; evidence; validation; model-evaluation; holdout; leakage
responsibility: Define a fixture-only receipt candidate that records model-evaluation split method, seed, stratification, spatial and temporal holdout scope, digest-bound partition summaries, leakage checks, and disclosure without accessing rows, executing a model, or creating evidence, review, release, deployment, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and bounded repository gap; PROPOSED inactive receipt; UNKNOWN consumer adoption and real split correctness; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ./predictive_layer_generalization_assessment.md
  - ./classification_layer_evaluation_assessment.md
  - ../governance/model_card_envelope.md
  - ../../schemas/contracts/v1/evidence/model_evaluation_split_receipt.schema.json
  - ../../fixtures/contracts/v1/evidence/model_evaluation_split_receipt/cases.json
  - ../../tools/validators/evidence/validate_model_evaluation_split_receipt.py
  - ../../tests/validators/evidence/test_validate_model_evaluation_split_receipt.py
  - ../../docs/intake/exploratory/pass-18-model-evaluation-split-receipt-source-map.md
tags: [kfm, evidence, model-evaluation, train-test, holdout, spatial-block, temporal-block, leakage, fixture-only]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-481."
  - "A PASS proves bounded declaration and accounting coherence only; it does not prove partition membership, leakage absence, model performance, generalization, evidence, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# ModelEvaluationSplitReceiptCandidate

ModelEvaluationSplitReceiptCandidate is an additive, fixture-only process-memory profile for declaring how one model-assisted layer was partitioned for evaluation. It records the split method, random seed where relevant, stratification and grouping choices, spatial and temporal holdout scope, digest-bound partition summaries, leakage-check posture, metric references, and public explanation disclosures.

It implements the narrow requirement in supplied Pass 18 card KFM-P18-INV-481: model-assisted layers should record split method, random seed, stratification choices, and evaluation holdout scope before model outputs can support a public explanation. The card specifically warns that spatial autocorrelation can make ordinary random splits overstate performance.

## Boundary

A validator PASS proves only that:

- the closed shape, deterministic profile hash, and receipt identity replay;
- model, layer, source-snapshot, split-manifest, method, and evaluation references are explicit;
- TRAIN and TEST partitions, with an optional VALIDATION partition, have canonical roles, distinct references and digests, and counts that reconcile to the declared population;
- stochastic methods declare a seed;
- stratified partitions carry class-distribution references;
- group, spatial, temporal, and spatiotemporal methods declare their required scopes;
- identity, group, spatial, and temporal leakage checks have coherent status and evidence-reference posture;
- a public-explanation candidate carries a holdout-scope note, evidence and review references, and a generalization-assessment reference; and
- every authority claim remains false.

The validator never opens a dataset, reads identifiers, assigns records to partitions, computes a distribution, evaluates leakage evidence, trains or runs a model, recomputes a metric, proves performance or generalization, resolves evidence, decides policy or review, promotes, releases, deploys, publishes, or authorizes public use.

## Split methods

| Method | Additional declaration |
|---|---|
| RANDOM_HOLDOUT | Random seed |
| STRATIFIED_HOLDOUT | Random seed, stratification fields, and per-partition class-distribution references |
| GROUP_HOLDOUT | Grouping fields and a group-overlap check |
| SPATIAL_BLOCK | Block or leave-region-out scope, geography and policy references, per-partition spatial scope, and spatial-overlap check |
| TEMPORAL_BLOCK | Forward-chain or holdout-window scope, window and policy references, per-partition temporal scope, and temporal-order check |
| SPATIOTEMPORAL_BLOCK | Both spatial and temporal declarations and checks |
| K_FOLD | Random seed and bounded TRAIN/TEST projection for the evaluated fold |
| CUSTOM | Digest-bound method definition and the same partition and leakage invariants |
| UNRESOLVED | Validation ABSTAINS |

The profile stores partition artifacts and counts only. It deliberately has no member for rows, record identifiers, labels, features, coordinates, raw prompts, model outputs, or unrestricted metadata.

## Relationship to adjacent contracts

PredictiveLayerGeneralizationAssessment records an evaluation strategy and bounded generalization labels. ClassificationLayerEvaluationAssessment records classification-evaluation evidence posture. This receipt does not replace either object: it binds the reproducibility metadata for one split and its partition accounting, while any performance or generalization interpretation remains in adjacent reviewed assessments.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| PASS | Identity, split method, partitions, counts, leakage checks, disclosure, and no-authority declarations are locally coherent. |
| ABSTAIN | Evaluation, a required reference, split method, partition, holdout scope, or leakage check remains explicitly unresolved. |
| DENY | Seed, stratification, grouping, partition, scope, leakage, disclosure, deterministic identity, or authority declarations are contradictory. |
| ERROR | The candidate cannot be parsed or evaluated safely, or declares evaluation error. |

These outcomes are validator results only. They are not dataset, model, evidence, review, release, deployment, or publication decisions.

## Directory Rules basis

The object is process memory for evidence-affecting model evaluation, so semantic meaning belongs under contracts/evidence/. Machine shape, synthetic replay, repository validation, conformance proof, CI orchestration, source reconciliation, and authoring accountability remain under schemas/, fixtures/, tools/, tests/, .github/workflows/, docs/intake/exploratory/, and data/receipts/generated/ respectively.

No dataset store, feature store, model registry, evaluation engine, EvidenceBundle home, policy lane, release record, deployment path, public API, or new root is created.

## Validation

    python -m unittest tests.validators.evidence.test_validate_model_evaluation_split_receipt -v
    python tools/validators/evidence/validate_model_evaluation_split_receipt.py --fixtures

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no dataset, split, model, layer, evidence, policy, review, lifecycle record, release, deployment, or public artifact.
