<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/full-atlas-m30-domain-convergence-cross-lane-join-governance-source-map
title: Full Atlas M30 Domain Convergence & Cross-Lane Join Governance Source Map
type: source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; first-slice-selected
owners: OWNER_TBD - Intake steward; Join steward; Hydrology steward; Agriculture steward; Docs steward
created: 2026-09-01
updated: 2026-09-01
policy_label: public-with-gates; provenance; cross-lane; abstain-first; no-source-activation
owning_root: docs/
responsibility: Record the current-main overlap map and one bounded synthetic Hydrology × Agriculture join slice for M30 without creating authority, source admission, release, or publication effects.
truth_posture: cite-or-abstain
-->

# Full Atlas M30 domain convergence & cross-lane join governance source map

## Selected slice

| Item | Evidence reference | Truth label |
|---|---|---|
| Overlap issue | `bartytime4life/Kansas-Frontier-Matrix#2899` | `CONFIRMED` drought/hydrology evidence slice with distinct source and time roles. |
| Milestone issue | `bartytime4life/Kansas-Frontier-Matrix#3391` | `CONFIRMED` M30 coordination checkpoint. |
| Current main | `main@db23a8bfa9fa126e87009a41240576619ccaac02` | `CONFIRMED` execution-start pin for this run. |
| Open overlap PR | `#4073` | `CONFIRMED` WIP implementation overlap for the same milestone. |
| Open overlap PR | `#4093` | `CONFIRMED` WIP hydrology envelope overlap for the same evidence family. |
| Accepted placement authority | `docs/doctrine/directory-rules.md` + `ADR-0029` | `CONFIRMED` placement authority only; no source or release authority. |

The selected first slice is a **synthetic Hydrology × Agriculture join candidate** that reuses the generic fixture-first candidate lane and treats #2899’s drought evidence as time-separated context, not public truth.

## Current-main overlap map

| Surface | Status | Why it matters |
|---|---|---|
| `contracts/joins/cross_lane_join_assessment.md` | `IMPLEMENTED` | Closed, fixture-first candidate semantics already exist. |
| `schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json` | `IMPLEMENTED` | Closed Draft 2020-12 shape for the generic candidate lane. |
| `tools/joins/join_candidates.py` | `IMPLEMENTED` | Deterministic local-only helper; no network, no writes, no publication authority. |
| `fixtures/contracts/v1/joins/cross_lane_join_assessment/cases.json` | `PARTIAL` | Synthetic cases exist; the selected slice still needs an explicit Hydrology × Agriculture abstention case. |
| `tests/joins/test_join_candidates.py` | `IMPLEMENTED` | Focused regression coverage for the generic candidate lane. |
| `contracts/domains/hydrology/drought_link.md` | `PARTIAL` | Preserves drought context separation and source-role visibility. |
| `contracts/domains/hydrology/water_use_link.md` | `PARTIAL` | Hydrology ↔ water-use seam meaning exists, but no public claim authority. |
| `docs/domains/agriculture/CROSS_LANE.md` | `PARTIAL` | Agriculture × Hydrology edge doctrine already states observed flow is not a yield input without modeling. |
| `contracts/domains/hydrology/evidence_bundle.md` | `PARTIAL` | Support, rights, and sensitivity remain separate gates. |
| `contracts/domains/hydrology/SOURCE_ROLE_MATRIX.md` | `PARTIAL` | Source-role collapse remains fail-closed. |
| Public claim / source admission / release / deployment | `ABSENT` | Not authorized by this slice and explicitly out of scope. |

## Required controls for the selected slice

The slice is only reviewable when all of these remain explicit:

- support compatibility: both sides must have admitted evidence support;
- uncertainty: time-separated drought context must stay distinct from the agriculture fixture;
- rights: unknown or unresolved rights abstain;
- sensitivity: the most restrictive sensitivity wins;
- harmful precision: exact location / private parcel / operator details remain generalized or withheld;
- deterministic abstention: unresolved support, rights, sensitivity, or harmful precision must yield `ABSTAIN` rather than a public claim.

## Material outcome classification

| Outcome | Classification |
|---|---|
| Generic candidate lane | `IMPLEMENTED` |
| Hydrology × Agriculture seam doctrine | `PARTIAL` |
| Rights / uncertainty / harmful-precision enforcement for public claim | `ABSENT` |
| Source admission / ingest / release / deployment / publication | `ABSENT` |
| M30 overlap map and execution-start pin | `IMPLEMENTED` |

## Non-effects

This source map does not admit a source, retrieve live payloads, promote lifecycle data, change repository settings, release, deploy, or publish. It only records the bounded exploratory slice and the overlap context.

## Rollback

Revert this document to remove the exploratory record. No source state, workflow state, or release state needs operational rollback.
