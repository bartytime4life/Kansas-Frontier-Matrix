<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/claim-scope-dimension-assessment
title: ClaimScopeDimensionAssessmentCandidate Contract
type: semantic-contract
version: v1.0.1
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Spatial-representation steward · Validation steward
created: 2026-08-10
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; evidence; claim-scope; representation; time-space-attribute
responsibility: Define a fixture-only assessment that makes the measured and controlled time, space, and attribute dimensions of one claim scope explicit without creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability, repository placement, and validator hardening; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./evidence_bundle.md
  - ./representation_fitness_assessment.md
  - ../common/temporal_window.md
  - ../common/spatial_geometry.md
  - ../../schemas/contracts/v1/evidence/claim_scope_dimension_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/claim_scope_dimension_assessment/cases.json
  - ../../tools/validators/evidence/validate_claim_scope_dimension_assessment.py
  - ../../tests/validators/evidence/test_validate_claim_scope_dimension_assessment.py
  - ../../docs/intake/exploratory/pass-18-claim-scope-dimension-assessment-source-map.md
  - ../../data/receipts/generated/genrec-pass18-claim-scope-dimension-assessment-validator-hardening-20260811.json
[/KFM_META_BLOCK_V2] -->

# ClaimScopeDimensionAssessmentCandidate

`ClaimScopeDimensionAssessmentCandidate` records which one of time, space, or attribute is measured while the other two are controlled for one bounded claim-scope candidate. It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-376`.

## Boundary

A validator `PASS` proves only that the candidate's closed shape, deterministic identity, dimension roles, scope-reference resolution declarations, interpretation label, limitations, and fixed-false authority declarations are internally coherent under this fixture profile.

It does not inspect a claim, resolve an `EvidenceBundle`, authenticate scope references, evaluate geographic fitness, transform coordinates, infer a temporal or spatial model, decide policy or review, promote, release, deploy, publish, or authorize public use. The three-dimension profile is a proposed disclosure aid, not a universal geographic ontology.

## Dimension profile

A complete candidate declares exactly one `MEASURED` dimension and two `CONTROLLED` dimensions:

| Measured dimension | Local interpretation label |
|---|---|
| `TIME` | `TIME_SERIES_AT_CONTROLLED_SPACE_ATTRIBUTE` |
| `SPACE` | `SPATIAL_CROSS_SECTION_AT_CONTROLLED_TIME_ATTRIBUTE` |
| `ATTRIBUTE` | `ATTRIBUTE_COMPARISON_AT_CONTROLLED_TIME_SPACE` |

An incomplete or unknown candidate uses `UNRESOLVED` dimension roles, `UNKNOWN` measured dimension, and `UNRESOLVED` interpretation. The validator abstains rather than inventing scope closure.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Dimension roles, references, interpretation, review posture, and identity are locally coherent. |
| `ABSTAIN` | The assessment or one or more dimension scopes remain incomplete, unknown, or unresolved. |
| `DENY` | Role cardinality, measured-dimension identity, interpretation, completeness, public-candidate review, limitation, or deterministic-binding claims are incoherent. |
| `ERROR` | The candidate cannot be evaluated safely under the closed schema or contains malformed JSON text such as an unpaired UTF-16 surrogate. |

These outcomes are not claim-truth, evidence, representation-fitness, policy, review, release, publication, or runtime-answer decisions.

The validator rejects unpaired surrogate code points before deterministic hashing. Malformed text therefore produces a finite `ERROR` finding instead of raising `UnicodeEncodeError` and terminating the process.

## Directory Rules basis

Semantic meaning belongs under `contracts/evidence/`; machine shape under `schemas/contracts/v1/evidence/`; synthetic cases under `fixtures/contracts/v1/evidence/`; validation under `tools/validators/evidence/`; executable conformance evidence under `tests/validators/evidence/`; orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

The profile composes `EvidenceBundle`, `RepresentationFitnessAssessment`, `TemporalWindow`, and `SpatialGeometry` by opaque reference without modifying or replacing them. It creates no parallel claim, evidence, geometry, time, attribute, layer, policy, release, or publication authority.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_claim_scope_dimension_assessment -v
python tools/validators/evidence/validate_claim_scope_dimension_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no claim, source, evidence, policy, lifecycle, layer, release, deployment, or public artifact.
