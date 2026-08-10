<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/measurement-support-reconciliation
title: Measurement Support Reconciliation Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Measurement steward · Domain stewards · Contract steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: public; common; measurement-support; comparison; no-network
owning_root: contracts/
responsibility: Define a bounded cross-domain comparison seam that preserves unit, vertical, temporal, spatial, uncertainty, quality, and knowledge-character support without performing scientific harmonization or authorizing downstream use.
truth_posture: CONFIRMED synthetic validator behavior / PROPOSED inactive semantic profile / NEEDS VERIFICATION steward adoption, scientific fitness, and hosted exact-head execution
related:
  - ./condition_relation.md
  - ../../schemas/contracts/v1/common/measurement_support_reconciliation.schema.json
  - ../../fixtures/contracts/v1/common/measurement_support_reconciliation/cases.json
  - ../../tools/validators/validate_measurement_support_reconciliation.py
  - ../../tests/validators/test_validate_measurement_support_reconciliation.py
  - ../../docs/intake/exploratory/measurement-support-reconciliation-source-map.md
tags: [kfm, common, measurement, unit-transform, scale, support, comparison, fixture-only]
notes:
  - "Implements the bounded KFM-TRIAD-048 and KFM-CAND-0144 gap from the Full Atlas."
  - "A PASS result proves local fixture consistency only; it does not establish scientific comparability, evidence closure, policy approval, review approval, release, or publication."
[/KFM_META_BLOCK_V2] -->

# Measurement Support Reconciliation Candidate

> A deterministic, fixture-only profile for deciding whether two synthetic environmental values are directly comparable, comparable only with explicit qualifications, or unsupported because their declared measurement support does not close.

## Purpose

Environmental values that share a parameter label can still differ in unit, observation or model character, depth or height, averaging interval, footprint, CRS, resolution, uncertainty, quality, and no-data meaning. This candidate preserves those axes and records an inspectable comparison-fitness result. It does not calculate a scientific product, choose a resampling method, or replace the domain contracts that own each observation or model output.

The existing `ConditionRelation` contract records contextual relationships and source roles. This profile supplies the narrower missing seam for unit transformation and measurement-support reconciliation before a comparison is treated as meaningful.

## Object surface

`MeasurementSupportReconciliation` binds exactly two synthetic supports:

- source role and knowledge character;
- parameter, value, unit, and uncertainty;
- vertical support;
- temporal extent and aggregation;
- spatial footprint, CRS, resolution, and geometry reference;
- quality and no-data semantics;
- a reviewed identity, linear, or unsupported unit-transform declaration;
- a reviewed none, nearest, bilinear, area-weighted, or unsupported resampling declaration; and
- a mechanically derived reconciliation summary.

Source-native records remain authoritative for their own assertions. The profile never rewrites either input.

## Finite results

| Reconciliation outcome | Validator result | Meaning |
|---|---|---|
| `COMPARABLE` | `PASS` / `REVIEW_REQUIRED` | Every support axis is aligned and no conversion or qualification is required. |
| `QUALIFIED` | `PASS` / `REVIEW_REQUIRED` | The declared comparison needs a reviewed unit conversion, resampling, partial temporal overlap, knowledge-character disclosure, or suspect-quality caveat. |
| `UNSUPPORTED` | `ABSTAIN` / `HOLD` | Parameter, unit, vertical, temporal, spatial, or quality support is unresolved or incompatible. |
| malformed or contradictory packet | `DENY` | Shape, identity, arithmetic, summary, ordering, or authority invariants failed. |
| unreadable input | `ERROR` | The bounded validator could not safely read the candidate. |

`PASS` is not a scientific approval. `REVIEW_REQUIRED` is fixed for every positive candidate.

## Anti-collapse rules

1. Measured, modeled, and derived values retain distinct knowledge character and source role.
2. Unit conversion does not erase depth, time-window, footprint, resolution, uncertainty, or quality differences.
3. Resampling is a declared, reviewed qualification; it is not evidence that the inputs are co-located or equivalent.
4. A mismatch or unknown support axis produces `UNSUPPORTED`; the validator does not average, interpolate, or infer a replacement.
5. Numeric fixture values and methods are synthetic test material, not adopted scientific thresholds or algorithms.
6. No result creates evidence, policy, review, promotion, release, publication, or public-use authority.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the complete candidate after removing only `assessment_id` and `spec_hash`.

```text
spec_hash      = SHA-256(JCS(identity subject))
assessment_id  = kfm:measurement-support-reconciliation:<first 24 digest hex>
```

Support order, transform and resampling declarations, reconciliation summary, and fixed governance flags all participate in identity.

## Directory Rules basis

The adopted Directory Rules assign shared semantic meaning to `contracts/common/`, machine shape to `schemas/contracts/v1/common/`, synthetic inputs to `fixtures/contracts/v1/common/`, repository validation to `tools/validators/`, executable conformance evidence to `tests/validators/`, CI orchestration to `.github/workflows/`, exploratory source adaptation to `docs/intake/exploratory/`, and AI-authoring process memory to `data/receipts/generated/`. The packet creates no new root or parallel contract, schema, policy, evidence, data, receipt, proof, release, or publication authority.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_measurement_support_reconciliation
python tools/validators/validate_measurement_support_reconciliation.py --fixtures
```

## Rollback

Before merge, close the draft pull request and remove its branch. After an authorized merge, revert this additive contract/schema/fixture/validator/test/workflow/source-map/receipt packet. No live source, stored observation, model, transform, policy, release, deployment, cache, or published artifact requires operational rollback.
