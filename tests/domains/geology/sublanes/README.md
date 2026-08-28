<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-sublanes-readme
title: Tests — Geology Sublanes
class: test-readme-index
status: draft
truth_posture: CONFIRMED path / PROPOSED index contract / UNKNOWN enforcement completeness
owner: <geology-domain-steward> + <test-steward> + <docs-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/domains/geology/OBJECT_FAMILIES.md
  - docs/domains/geology/sublanes/bedrock_geology.md
  - tests/domains/geology/README.md
  - tests/domains/geology/source_role/README.md
  - tests/domains/geology/claim-class/README.md
  - tests/domains/geology/catalog-closure/README.md
  - tests/domains/geology/public-safe-geometry/README.md
  - tests/domains/geology/governed-ai/README.md
  - tests/domains/geology/rollback/README.md
  - tests/domains/geology/sublanes/surficial/README.md
tags: [kfm, tests, geology, sublanes, test-index, evidence, fail-closed]
notes:
  - "This README indexes Geology sublane test folders under tests/domains/geology/sublanes/."
  - "It is a test index, not domain doctrine, source authority, schema authority, policy authority, release authority, or proof of executable coverage."
[/KFM_META_BLOCK_V2] -->

# Tests — Geology Sublanes

> **Purpose.** This folder indexes Geology sublane test lanes. It keeps sublane tests aligned with shared Geology invariants: source-role preservation, claim-class separation, public-safe geometry, evidence closure, governed-AI boundaries, correction, rollback, and cross-lane ownership.

## Placement

| Field | Value |
|---|---|
| Path | `tests/domains/geology/sublanes/` |
| Owning root | `tests/` |
| Domain | `geology` |
| Role | Sublane test index |
| Status | `draft`; implementation coverage remains `UNKNOWN` |

This folder is for test-lane organization only. It must not store fixtures, source payloads, schemas, policy rules, receipts, proofs, catalog records, release records, or package code.

## Evidence basis

The Geology object-family document groups foundational map-unit, stratigraphy, structure, subsurface-reference, observation, resource, operational, lineage, and cross-lane object families. It also records roster naming and membership drift that sublane tests must not silently resolve.

The bedrock sublane document shows a proposed sublane pattern and names sibling sublanes such as surficial, stratigraphy, structures, boreholes/wells, geophysics, geochemistry, and resources. Because sublane layout remains partly proposed, this README treats the folder as a requested test index rather than proof of final topology.

## Current sublane test lanes

| Sublane | Path | Current posture |
|---|---|---|
| Surficial | [`surficial/`](surficial/README.md) | README exists; executable coverage remains `UNKNOWN`. |

## Proposed future sublane lanes

The following folders are proposed only if matching test coverage is needed and the repo accepts this sublane layout:

```text
tests/domains/geology/sublanes/
├── README.md
├── surficial/
├── bedrock/
├── stratigraphy/
├── structures/
├── boreholes-wells/
├── geophysics/
├── geochemistry/
└── resources/
```

Do not create parallel homes for the same responsibility. If a sublane already has another accepted test path, add a pointer or migration note instead of duplicating authority.

## Shared checks every sublane should inherit

| Check family | Required behavior |
|---|---|
| Object identity | Sublane objects preserve their object-family identity and do not silently merge with siblings. |
| Source role | `source_role` is explicit, admitted, and preserved through tests. |
| Claim class | Sublane tests do not strengthen or collapse claim meaning. |
| Temporal support | Source, valid, retrieval, release, and correction times remain distinct where material. |
| Geometry posture | Public-facing geometry is role-tagged and evidence-linked. |
| Evidence closure | Catalog/release candidates resolve required evidence and policy support. |
| Cross-lane boundary | Geology sublanes may provide context to adjacent lanes but do not own adjacent-lane truth. |
| Public summaries | API, map, drawer, and AI summaries keep qualifiers and citations. |
| Correction/rollback | Superseded outputs mark stale state and invalidate derivatives where required. |
| Finite outcomes | Unsupported records fail, hold, deny, abstain, or error with reason codes. |

## Minimal acceptance matrix

| ID | Scenario | Then |
|---|---|---|
| `GEOL-SUB-001` | Sublane README exists. | It identifies scope, boundaries, and implementation status. |
| `GEOL-SUB-002` | Sublane test fixture is added. | It uses the approved fixture home, not this index folder. |
| `GEOL-SUB-003` | Sublane object overlaps another sublane. | The test names the boundary and fails closed on silent collapse. |
| `GEOL-SUB-004` | Sublane output is public-facing. | It must pass source-role, evidence, policy, geometry, and release checks. |
| `GEOL-SUB-005` | Sublane layout changes. | A migration note, redirect README, or ADR records the decision. |

## Non-goals

This index does not define Geology doctrine, object schemas, policy rules, public routes, fixtures, or release behavior. It does not prove executable sublane tests exist.

## Current implementation note

This README replaces an empty placeholder. It defines a proposed index contract only. Executable sublane tests, fixtures, validators, and CI wiring remain `UNKNOWN` until verified.
