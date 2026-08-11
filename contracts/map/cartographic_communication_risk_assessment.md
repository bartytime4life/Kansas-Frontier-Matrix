<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/cartographic-communication-risk-assessment
title: CartographicCommunicationRiskAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Map steward · Cartographic review steward · Evidence steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; map; cartography; communication-risk; public-candidate
responsibility: Define a fixture-only cartographic communication-risk assessment for public-facing map candidates without rendering a map, judging evidence truth, approving review, or creating release or publication authority.
truth_posture: "CONFIRMED supplied-card traceability, visual review, and bounded repository gap; PROPOSED inactive assessment; UNKNOWN consumer adoption; NEEDS VERIFICATION map, cartographic communication, evidence, release, and validation review plus hosted exact-head CI"
related:
  - ./representation_fitness_assessment.md
  - ../data/cartographic_omission_disclosure.md
  - ../data/map_scale_generalization_disclosure.md
  - ../evidence/projection_distortion_disclosure.md
  - ../../schemas/contracts/v1/map/cartographic_communication_risk_assessment.schema.json
  - ../../fixtures/contracts/v1/map/cartographic_communication_risk_assessment/cases.json
  - ../../tools/validators/map/validate_cartographic_communication_risk_assessment.py
  - ../../tests/validators/map/test_validate_cartographic_communication_risk_assessment.py
  - ../../docs/intake/exploratory/pass-18-cartographic-communication-risk-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# CartographicCommunicationRiskAssessment Candidate

`CartographicCommunicationRiskAssessmentCandidate` is an additive, fixture-only
review declaration for one public or semi-public map candidate. It implements
the smallest reviewable portion of supplied Pass 18 card
`KFM-P18-INV-352`: make selection, framing, scale, symbology, and omission
communication risks explicit before publication review.

## Boundary

A validator `PASS` means only that the synthetic declaration is closed,
content-addressed, supported by opaque adjacent-assessment references, complete
for all five review axes, and free of a declared misleading state. It does not:

- render, inspect, compare, or approve a map or style;
- prove evidence strength, spatial accuracy, completeness, fitness, or fairness;
- resolve the referenced fitness, scale, omission, distortion, classification,
  evidence, policy, or review records;
- decide whether a visual choice is legally or ethically acceptable; or
- promote, release, deploy, publish, or authorize public use.

The candidate stores no geometry, coordinates, source rows, style JSON, color
values, labels, screenshots, tiles, URLs, or public payloads.

## Review axes

| Axis | Review question |
|---|---|
| `SELECTION` | Does the selected evidence population match the claim and declared scope? |
| `FRAMING` | Does the visible context avoid overstating authority or excluding necessary context? |
| `SCALE` | Does display scale avoid implying unsupported precision or geographic coverage? |
| `SYMBOLOGY` | Do hierarchy, legend, labels, and uncertainty cues match declared evidence strength? |
| `OMISSION` | Are consequential exclusions disclosed rather than hidden by the visual surface? |

Every axis is declared exactly once in canonical order as `ACCEPTABLE`,
`MITIGATED`, `UNRESOLVED`, or `MISLEADING`. A mitigated axis requires an opaque
mitigation reference. An unresolved axis yields `ABSTAIN`; a misleading axis
yields `DENY`. These finite outcomes remain validator results, not review or
release decisions.

## Supporting assessments

The profile composes existing representation-fitness, map-scale,
cartographic-omission, and projection-distortion responsibilities by opaque
reference. Classification disclosure may be `NOT_APPLICABLE` for a map that
does not classify values. The profile does not copy or replace any adjacent
schema and does not authenticate those references.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The five axes, supporting references, review declaration, summary, timestamp, and content hash are locally coherent. |
| `ABSTAIN` | Consequence, an axis, a supporting assessment, or review posture remains unresolved. |
| `DENY` | A misleading axis, incoherent mitigation, contradictory support, non-canonical review record, timestamp, or content hash is declared. |
| `ERROR` | The candidate cannot be safely parsed or evaluated under the closed schema. |

## Directory Rules basis

The object is map-specific semantic meaning, so it belongs under
`contracts/map/`. Machine shape, synthetic replay, repository validation,
executable conformance, read-only CI, source reconciliation, and authoring
accountability remain under their established `schemas/`, `fixtures/`,
`tools/`, `tests/`, `.github/`, `docs/`, and `data/receipts/generated/`
responsibility roots. No style authority, evidence store, policy lane, review
store, release path, public surface, or new repository root is created.

## Validation and rollback

```bash
python -m unittest tests.validators.map.test_validate_cartographic_communication_risk_assessment -v
python tools/validators/map/validate_cartographic_communication_risk_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive profile has no renderer,
registry, release, deployment, cache, publication, or public-state side effect.
