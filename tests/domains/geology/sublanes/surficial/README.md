<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-sublanes-surficial-readme
title: Tests — Geology Sublane — Surficial
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <geology-domain-steward> + <surficial-geology-steward> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/domains/geology/OBJECT_FAMILIES.md
  - docs/domains/geology/sublanes/bedrock_geology.md
  - tests/domains/geology/source_role/README.md
  - tests/domains/geology/catalog-closure/README.md
  - tests/domains/geology/public-safe-geometry/README.md
tags: [kfm, tests, geology, sublanes, surficial, surficial-unit, parent-material, cross-lane, fail-closed]
notes:
  - "This README documents the intended Surficial Geology sublane test contract."
  - "It does not claim executable tests, fixtures, validators, or CI wiring already exist."
[/KFM_META_BLOCK_V2] -->

# Tests — Geology Sublane — Surficial

> **Purpose.** This folder is the Geology-domain test lane for `SurficialUnit` behavior: surficial mapping-unit identity, parent-material context, source-role preservation, public-safe geometry posture, evidence support, and cross-lane boundaries with Soil.

## Placement

| Field | Value |
|---|---|
| Path | `tests/domains/geology/sublanes/surficial/` |
| Owning root | `tests/` |
| Domain | `geology` |
| Sublane | `surficial` |
| Primary object | `SurficialUnit` |
| Status | `draft`; implementation coverage remains `UNKNOWN` |

This is a test lane only. It must not store fixtures, source payloads, schemas, policy rules, receipts, proofs, catalog records, release records, or package code.

## Evidence basis

The Geology object-family document identifies `SurficialUnit` as a foundational object and records that it appears in the §E / §INDEX-18 roster while not appearing in §B verbatim. That roster difference remains a naming/membership reconciliation issue, not a test shortcut.

The bedrock sublane document defines bedrock as consolidated rock and names surficial geology as the sibling lane for unconsolidated cover. Surficial tests should therefore preserve the boundary between bedrock, surficial geology, and Soil-owned truth.

## Proposed checks

| ID | Check | Expected behavior |
|---|---|---|
| `GEOL-SURF-001` | Surficial identity | A valid surficial record is typed as `SurficialUnit`. |
| `GEOL-SURF-002` | Roster drift | Tests do not silently resolve unresolved object-roster drift. |
| `GEOL-SURF-003` | Bedrock boundary | Surficial records are not silently relabeled as bedrock units. |
| `GEOL-SURF-004` | Soil boundary | Parent-material context does not become Soil-owned truth. |
| `GEOL-SURF-005` | Source role | Source role is present and preserved. |
| `GEOL-SURF-006` | Time support | Source, valid, release, and correction times stay distinct where material. |
| `GEOL-SURF-007` | Geometry posture | Public-facing geometry is role-tagged and evidence-linked. |
| `GEOL-SURF-008` | Evidence closure | Catalog or release candidates resolve required evidence support. |
| `GEOL-SURF-009` | Public summaries | API, map, drawer, or AI summaries keep surficial qualifiers. |
| `GEOL-SURF-010` | Finite outcomes | Missing support returns a bounded fail/hold/abstain outcome. |

## Proposed test files

```text
tests/domains/geology/sublanes/surficial/
├── README.md
├── test_surficial_unit_identity.py          # PROPOSED
├── test_roster_drift_awareness.py           # PROPOSED
├── test_bedrock_boundary.py                 # PROPOSED
├── test_soil_boundary.py                    # PROPOSED
├── test_source_role_preserved.py            # PROPOSED
├── test_temporal_support.py                 # PROPOSED
├── test_geometry_posture.py                 # PROPOSED
├── test_evidence_closure.py                 # PROPOSED
├── test_public_summary_qualifiers.py        # PROPOSED
└── test_finite_outcomes.py                  # PROPOSED
```

## Fixture posture

Use synthetic, no-network fixtures under the approved Geology fixture home. Valid fixtures should represent minimal `SurficialUnit` records. Invalid fixtures should isolate one failure at a time, such as missing object family, missing source role, missing time support, missing evidence support, bedrock/surficial collapse, or Soil-boundary overclaim.

## Non-goals

This lane does not define Soil objects, publish map layers, resolve roster drift, decide release state, or turn generated summaries into evidence.

## Current implementation note

This README replaces an empty placeholder. It defines a proposed test matrix only. Executable tests, fixtures, validators, and CI wiring remain `UNKNOWN` until verified.
