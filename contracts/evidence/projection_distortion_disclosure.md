<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/projection-distortion-disclosure
title: ProjectionDistortionDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Cartography steward · Spatial-reference steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; evidence; cartography; projection; distortion; disclosure
responsibility: Define a fixture-only disclosure of projection choice and declared material distortion risks without transforming coordinates, measuring distortion, resolving evidence, or creating review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository gap; PROPOSED inactive contract; UNKNOWN consumer adoption and cartographic fitness; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./representation_fitness_assessment.md
  - ../data/cartographic_omission_disclosure.md
  - ../../schemas/contracts/v1/evidence/projection_distortion_disclosure.schema.json
  - ../../fixtures/contracts/v1/evidence/projection_distortion_disclosure/cases.json
  - ../../tools/validators/evidence/validate_projection_distortion_disclosure.py
  - ../../tests/validators/evidence/test_validate_projection_distortion_disclosure.py
  - ../../docs/intake/exploratory/pass-18-projection-distortion-disclosure-source-map.md
tags: [kfm, evidence, cartography, projection, distortion, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-426."
  - "A PASS proves declaration coherence only; it does not prove that a CRS, transformation, projection, or map is fit for use."
[/KFM_META_BLOCK_V2] -->

# ProjectionDistortionDisclosureCandidate

`ProjectionDistortionDisclosureCandidate` makes one statewide, regional, or local map candidate's projection choice and declared distortion posture inspectable. It records the CRS and projection family, area of use, transformation reference, a digest-bound distortion assessment, the intended claim scope, declared effects on area, distance, direction, shape, and scale variation, and review-facing disclosure.

## Boundary

A validator `PASS` proves only that the closed candidate shape, deterministic profile hash, references, declared materiality, distortion dimensions, risk codes, and required public disclosure are locally coherent.

The profile does not transform coordinates, calculate distortion, infer fitness from a projection family, inspect map geometry, resolve references, authenticate evidence, approve a CRS, decide policy or review, promote, release, deploy, publish, or authorize public use.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The authored projection and distortion disclosure is locally coherent. |
| `ABSTAIN` | Projection, scope, materiality, or a required reference remains unresolved. |
| `DENY` | A complete declaration is internally inconsistent, under-disclosed, or hash-invalid. |
| `ERROR` | The candidate is schema-invalid or explicitly declares an evaluation error. |

These are validator results, not cartographic findings, evidence conclusions, review decisions, release states, or runtime answers.

## Disclosure rules

A complete candidate declares all four distortion dimensions and scale variation. `MATERIAL` declarations name at least one material risk, and every dimension declared `DISTORTED` has its corresponding risk code. `NOT_MATERIAL` requires an authored rationale reference; the validator does not endorse that rationale. Public or policy-context statewide and regional candidates also require a review record, Evidence Drawer section, and plain-language caveat.

## Directory Rules basis

Projection disclosure evaluates evidence support for a representation, so semantic meaning belongs under `contracts/evidence/`; shape under `schemas/contracts/v1/evidence/`; synthetic replay under `fixtures/contracts/v1/evidence/`; validation under `tools/validators/evidence/`; conformance proof under `tests/validators/evidence/`; orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. No CRS registry, transformation engine, evidence store, policy rule, release record, or public map path is created.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_projection_distortion_disclosure -v
python tools/validators/evidence/validate_projection_distortion_disclosure.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no source, coordinate, geometry, layer, evidence, policy, review, release, deployment, or public artifact.
