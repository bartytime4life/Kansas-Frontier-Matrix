<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/archaeology/three-d-visibility-assumption-disclosure
title: ThreeDVisibilityAssumptionDisclosure Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Archaeology steward · 3D analysis steward · Cultural review steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; archaeology; three-d; visibility; assumptions; no-network
owning_root: contracts/
responsibility: Define fixture-only disclosure semantics for 3D visibility-analysis assumptions without creating archaeological fact, evidence, interpretation, policy, review, release, or publication authority.
truth_posture: CONFIRMED source-card and repository-gap evidence / PROPOSED inactive profile / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ./three_d_documentation.md
  - ../../map/three_d_admission_decision.md
  - ../../../schemas/contracts/v1/domains/archaeology/three_d_visibility_assumption_disclosure.schema.json
  - ../../../fixtures/contracts/v1/domains/archaeology/three_d_visibility_assumption_disclosure/cases.json
  - ../../../tools/validators/domains/archaeology/validate_three_d_visibility_assumption_disclosure.py
  - ../../../tests/validators/domains/archaeology/test_validate_three_d_visibility_assumption_disclosure.py
  - ../../../docs/intake/exploratory/pass-18-three-d-visibility-assumption-disclosure-source-map.md
[/KFM_META_BLOCK_V2] -->

# ThreeDVisibilityAssumptionDisclosure Candidate

`ThreeDVisibilityAssumptionDisclosure` is an inactive, fixture-only profile for
recording the assumptions behind one archaeology 3D visibility analysis. It
implements the narrow seam proposed by Pass 18 card `KFM-P18-INV-458` and
complements `ThreeDDocumentation`; it does not alter that contract or create a
second owner for 3D asset paradata.

## Disclosed assumptions

The candidate binds opaque references and bounded classifications for:

- the analysis and scene/model used;
- horizontal and vertical model resolution and vertical-datum reference;
- observer and target counts, geometry-disclosure posture, height, and height
  basis;
- terrain, built, or custom obstacles and their completeness;
- algorithm, line-of-sight rule, curvature, refraction, distance limit, and
  scenario identifiers; and
- interpretation and uncertainty scope.

Exact observer, target, site, or obstacle coordinates are outside the closed
schema. Geometry is referenced only as `EXACT_RESTRICTED`, `GENERALIZED`, or
`WITHHELD`. A public candidate cannot carry an exact-restricted posture.

## Finite result

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic disclosure is internally coherent and ready for human review. |
| `ABSTAIN` | Analysis, model, height, obstacle, method, evidence, or review information is unresolved. |
| `DENY` | Shape, identity, sensitivity, assumption-closure, or public-release rules conflict. |
| `ERROR` | The declared analysis state is `ERROR`, or bounded file handling cannot proceed safely. |

`PASS` is not a claim that a person, place, feature, or archaeological event was
visible. Visibility output remains an assumption-bound interpretation.

## Deterministic identity

The validator computes SHA-256 over canonical JSON after removing only
`spec_hash` and `disclosure_id`. The ID is
`kfm:archaeology:visibility-disclosure:` plus the first 24 digest hex
characters. Reference arrays must be unique and lexicographically ordered.

## Trust boundary

Validation does not open a model, resolve a geometry, run a viewshed, inspect a
site, verify a datum, decide archaeological meaning, evaluate cultural or
policy constraints, approve review, transform a location, release, publish, or
authorize public use. All authority claims are fixed to `false`.

## Directory Rules and rollback

Accepted ADR-0029 keeps domain semantics in
`contracts/domains/archaeology/`; machine shape, fixtures, validation, tests,
workflow orchestration, source reconciliation, and generated accountability
stay in their existing paired roots. No new root or parallel authority is
introduced.

Rollback is one additive feature-commit revert. No model, evidence, policy,
review, release, deployment, or public state is mutated by this packet.
