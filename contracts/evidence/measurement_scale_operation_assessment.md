<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/measurement-scale-operation-assessment
title: MeasurementScaleOperationAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Cartography steward · Data-quality steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; evidence; measurement-scale; aggregation; legend
responsibility: Define a fixture-only assessment of whether requested aggregation, ranking, and legend operations are coherent with declared measurement-scale metadata without creating analytics, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./representation_fitness_assessment.md
  - ../../schemas/contracts/v1/evidence/measurement_scale_operation_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/measurement_scale_operation_assessment/cases.json
  - ../../tools/validators/evidence/validate_measurement_scale_operation_assessment.py
  - ../../tests/validators/evidence/test_validate_measurement_scale_operation_assessment.py
  - ../../docs/intake/exploratory/pass-18-measurement-scale-operation-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# MeasurementScaleOperationAssessmentCandidate

`MeasurementScaleOperationAssessmentCandidate` records one mapped attribute's declared measurement scale and a closed set of requested aggregation, ranking, classification, symbol, and legend operations. It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-377`.

## Boundary

A validator `PASS` proves only that the candidate's closed shape, deterministic identity, scale metadata, operation partition, review references, and fixed-false authority declarations are internally coherent under this fixture profile.

It does not inspect source values, infer a scale class, select a statistic, calculate an aggregation, render a legend, resolve evidence, evaluate policy, approve review, promote, release, deploy, publish, or authorize public use. The operation matrix is a proposed test profile, not a normative scientific policy.

## Proposed operation matrix

| Scale class | Locally compatible operation families |
|---|---|
| `NOMINAL` | categorical legend and mode |
| `ORDINAL` | categorical/ordered legends, sequential ramps, rank, mode, median, min/max, and quantile classification |
| `INTERVAL` | ordinal operations plus mean, difference, and diverging ramps; ratio, sum, and proportional-symbol claims remain blocked |
| `RATIO` | all operations in the closed v1 vocabulary when unit and true-zero declarations are present |
| `MIXED` / `CUSTOM` | no automatic compatibility result; retain an abstaining review posture |

This matrix is intentionally conservative and reviewable. Domain-specific semantics may narrow it but cannot silently broaden this inactive profile.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared scale and operation partition are locally coherent. |
| `ABSTAIN` | Scale definition or assessment is unresolved, incomplete, mixed, or custom. |
| `DENY` | Metadata, unit, true-zero, review, partition, or operation compatibility is incoherent. |
| `ERROR` | The candidate cannot be evaluated under the closed schema. |

These outcomes are not evidence, policy, review, analytics, release, or publication decisions.

## Directory Rules basis

Semantic meaning belongs under `contracts/evidence/`; machine shape under `schemas/contracts/v1/evidence/`; synthetic cases under `fixtures/contracts/v1/evidence/`; validation under `tools/validators/evidence/`; executable conformance evidence under `tests/validators/evidence/`; orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

The profile composes `RepresentationFitnessAssessment` without modifying it and does not create parallel attribute-registry, legend, analytics, policy, layer, release, or publication authority.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_measurement_scale_operation_assessment -v
python tools/validators/evidence/validate_measurement_scale_operation_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no source value, layer, evidence, policy, lifecycle, release, deployment, or public artifact.
