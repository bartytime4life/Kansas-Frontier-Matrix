<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/feature-set-manifest
title: FeatureSetManifest Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Evidence steward · Analytics steward · Model steward · Privacy steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; evidence; analytics; model-inputs; privacy; no-network
owning_root: contracts/
responsibility: Define one immutable model feature-set declaration with explicit semantics, lineage, missing-data, sensitivity, target-leakage, disclosure, and no-authority boundaries.
truth_posture: CONFIRMED source and repository gap / PROPOSED inactive manifest / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ./analytic_output_disclosure_assessment.md
  - ../governance/model_card_envelope.md
  - ../../schemas/contracts/v1/evidence/feature_set_manifest.schema.json
  - ../../fixtures/contracts/v1/evidence/feature_set_manifest/cases.json
  - ../../tools/validators/evidence/validate_feature_set_manifest.py
  - ../../tests/validators/evidence/test_validate_feature_set_manifest.py
  - ../../docs/intake/exploratory/feature-set-manifest-source-map.md
tags: [kfm, evidence, analytics, machine-learning, features, lineage, sensitivity, deterministic, fixture-only]
notes:
  - "Implements one bounded dependency named by Full Atlas KFM-TRIAD-030 / KFM-CAND-0090 and the AnalyticOutputDisclosureAssessment follow-up boundary."
  - "A manifest declares feature semantics only; it does not extract values, resolve evidence, train or run a model, review, release, or publish."
[/KFM_META_BLOCK_V2] -->

# FeatureSetManifest Candidate

> A deterministic, fixture-only declaration for which inputs one model family may use, how those inputs retain lineage and source roles, and which missingness, sensitivity, and target-leakage constraints reviewers must see.

## Purpose

`AnalyticOutputDisclosureAssessment` already requires a `FeatureSetManifest` reference for an ML result, but the referenced object family is not implemented on the pinned repository base. This packet fills only that feature-declaration seam.

A `FeatureSetManifest` records:

- opaque model-family, intended-use, and optional target references plus a `TRAINING`, `INFERENCE`, or `BOTH` phase;
- a sorted feature list with stable key, semantic reference, data type, unit, spatial and temporal support;
- the source role for every feature without collapsing derived, modeled, or interpretive inputs into observations;
- mandatory evidence posture, explicit missing-data treatment, and separately reviewed derivation or imputation references;
- sensitivity classification with policy-profile references for restricted inputs;
- source-descriptor, EvidenceBundle, training-dataset, and feature-extraction-receipt lineage; and
- deterministic RFC 8785 JCS plus SHA-256 identity.

The manifest carries declarations and opaque references, never feature values, records, credentials, sensitive payloads, model weights, or executable transformation code.

## Feature rules

| Concern | Required posture |
|---|---|
| Ordering and identity | Feature keys are unique and lexical; the declaration is content addressed. |
| Evidence | Every feature fixes `evidence_required: true`; source and EvidenceBundle reference arrays are non-empty, unique, and lexical. |
| Derived inputs | `DERIVED`, `MODELED`, and `INTERPRETIVE` roles require a `derivation_ref`; other roles prohibit one. |
| Missingness | `FORBIDDEN`, `ALLOW_WITH_INDICATOR`, or `IMPUTE_WITH_METHOD_REF`; only the last requires an opaque imputation-method reference. |
| Sensitivity | `RESTRICTED` and `HIGHLY_RESTRICTED` require an opaque policy-profile reference; `PUBLIC` and `INTERNAL` prohibit one. |
| Target separation | A feature semantic reference cannot equal the declared target reference, and `target_leakage` is fixed false. |
| Phase lineage | `TRAINING` and `BOTH` require a training-dataset reference; inference-only manifests prohibit one. |

These checks establish declaration consistency only. They cannot prove that evidence or policy artifacts exist, that a feature is safe or predictive, or that a training dataset is admissible.

## Interpretation limits

Every manifest requires:

- `NOT_ROOT_TRUTH`;
- `NOT_OBSERVATION`;
- `NO_MODEL_VALIDITY_CLAIM`;
- `SCOPE_BOUND`; and
- `NO_PUBLICATION_AUTHORITY`.

The governance block fixes execution to `FIXTURE_ONLY` and all extraction, model, evidence, policy, review, promotion, release, public-use, and publication effects to false.

## Deterministic identity

The validator removes only `manifest_id` and `spec_hash`, canonicalizes the remaining object with RFC 8785 JCS, and computes SHA-256.

```text
spec_hash  = SHA-256(JCS(identity subject))
manifest_id = kfm:feature-set-manifest:<first 24 digest hex>
```

Feature keys and lineage-reference arrays are lexical and unique. Ordering, coupling, stored-identity, or authority drift fails closed.

## Directory Rules basis

Feature-set meaning belongs under `contracts/evidence/` because it defines lineage and disclosure expectations for inputs to a modeled analytic claim. Machine shape belongs under `schemas/contracts/v1/evidence/`; synthetic cases under `fixtures/contracts/v1/evidence/`; reusable validation under `tools/validators/evidence/`; executable evidence under `tests/validators/evidence/`; read-only orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and AI authoring accountability under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. The packet does not create a model registry, feature store, privacy-policy home, evidence store, runtime, training lane, public API, release lane, or publication path.

## Validation

```bash
python -m unittest -v tests.validators.evidence.test_validate_feature_set_manifest
python tools/validators/evidence/validate_feature_set_manifest.py --fixtures
```

## Non-effects and rollback

A passing fixture proves only local manifest consistency. It does not prove any source, EvidenceBundle, feature value, extraction receipt, dataset, method, policy profile, model, run, validation report, review, release, or public output exists.

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive packet. No live data, extraction, training, inference, evidence, lifecycle state, policy, deployment, cache, release, or public artifact requires operational rollback.
