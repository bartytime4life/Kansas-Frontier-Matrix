<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/feature-transform-receipt
title: FeatureTransformReceiptCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Model-governance steward · Analytics steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; evidence; processing-receipt; feature-transform; model-assisted
responsibility: Define fixture-only process memory for ordered feature scaling, normalization, encoding, engineering, and selection declarations without executing a transform or creating evidence, model, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and bounded repository gap; PROPOSED inactive receipt profile; UNKNOWN runtime adoption; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ./feature_set_manifest.md
  - ./predictive_layer_generalization_assessment.md
  - ./analytic_output_disclosure_assessment.md
  - ../governance/model_card_envelope.md
  - ../../schemas/contracts/v1/evidence/feature_transform_receipt.schema.json
  - ../../fixtures/contracts/v1/evidence/feature_transform_receipt/cases.json
  - ../../tools/validators/evidence/validate_feature_transform_receipt.py
  - ../../tests/validators/evidence/test_validate_feature_transform_receipt.py
  - ../../docs/intake/exploratory/pass-18-feature-transform-receipt-source-map.md
tags: [kfm, evidence, feature-transform, scaling, normalization, encoding, selection, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-408."
  - "A PASS proves declaration and transform-chain coherence only; it does not prove execution, scientific fitness, evidence closure, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# FeatureTransformReceiptCandidate

`FeatureTransformReceiptCandidate` is an inactive process-memory declaration for one ordered feature-processing chain. It records whether features were scaled, normalized, encoded, engineered, or selected; which declared feature set entered and left each step; which method and parameter manifests were used; and which training population was used to fit a transform.

The profile implements the bounded requirement in supplied Pass 18 card `KFM-P18-INV-408`: ML and analytical feature pipelines should make preprocessing transforms evidence-bearing and visible instead of leaving reviewers unable to tell whether a value is raw, standardized, encoded, selected, or engineered.

## Boundary

A validator `PASS` proves only that:

- the closed candidate shape and deterministic profile hash agree;
- input, intermediate, and output feature references form one explicit linear chain;
- step ordinals, identifiers, feature arrays, evidence arrays, and limitations are canonical;
- declared feature counts match the listed references;
- feature-selection steps actually reduce the declared feature set;
- the declared transform family agrees with its output-state label;
- method, parameter, split, leakage-review, model-card, feature-manifest, and run-receipt references are locally complete; and
- an evaluation-bearing candidate does not declare that fitted preprocessing used the full dataset.

The validator does not read feature values, fit or apply a transform, authenticate a method or receipt, resolve an EvidenceBundle, prove leakage freedom, assess scientific fitness, train or run a model, evaluate policy, approve review, promote, release, deploy, publish, or authorize public use.

## Transform families and state labels

| Family | Required output state | Local declaration rule |
|---|---|---|
| `SCALING` | `SCALED` | Feature count is preserved. |
| `NORMALIZATION` | `NORMALIZED` | Feature count is preserved. |
| `ENCODING` | `ENCODED` | At least one output feature remains declared. |
| `FEATURE_ENGINEERING` | `ENGINEERED` | At least one output feature remains declared. |
| `FEATURE_SELECTION` | `SELECTED` | Output references are a strict subset of the input references. |
| `CUSTOM` | `CUSTOM` | The method and parameter manifest remain explicit; no mathematical equivalence is inferred. |

These checks are intentionally structural. They do not establish that a scaling formula, normalization range, encoding vocabulary, engineered feature, or selection criterion is correct.

## Training and leakage disclosure

Every step declares `fitted_on` as `TRAINING_ONLY`, `EXTERNAL_REFERENCE`, `FULL_DATASET`, `NOT_APPLICABLE`, or `UNRESOLVED`. When a held candidate declares an evaluation population, a fitted preprocessing step that says `FULL_DATASET` fails closed as an evaluation-leakage risk. This is a declaration check, not proof that the referenced split was followed.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Identity, references, chain, counts, states, training disclosure, and non-authority declarations are locally coherent. |
| `ABSTAIN` | Execution, fit scope, or a required reference remains incomplete or unresolved. |
| `DENY` | Chain, count, selection, state, leakage, review, ordering, timestamp, limitation, or deterministic-identity declarations are incoherent. |
| `ERROR` | The candidate cannot be parsed or evaluated safely, or declares execution error. |

These outcomes are validation results only. They are not evidence, model-quality, policy, review, promotion, release, or publication decisions.

## Directory Rules basis

This object is process memory for an evidence-affecting analytical transform, so semantic meaning belongs under `contracts/evidence/`; machine shape under `schemas/contracts/v1/evidence/`; synthetic replay under `fixtures/contracts/v1/evidence/`; executable validation under `tools/validators/evidence/`; conformance proof under `tests/validators/evidence/`; orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and generated authoring provenance under `data/receipts/generated/`.

The receipt composes the existing `FeatureSetManifest`, `ModelCardEnvelope`, run-receipt, predictive-generalization, and analytic-output disclosure seams by reference. It does not create a feature registry, transform engine, model store, evidence store, policy lane, release path, or public surface.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_feature_transform_receipt -v
python tools/validators/evidence/validate_feature_transform_receipt.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no source, dataset, feature registry, model, evidence, policy, lifecycle, review, release, deployment, or public artifact.
