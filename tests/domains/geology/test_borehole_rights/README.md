<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-test-borehole-rights-readme
title: Tests — Geology Borehole Rights
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <geology-domain-steward> + <rights-steward> + <sensitivity-reviewer> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/domains/geology/OBJECT_FAMILIES.md
  - docs/runbooks/geology/PROMOTION_RUNBOOK.md
  - tests/domains/geology/source_role/README.md
  - tests/domains/geology/public-safe-geometry/README.md
  - tests/domains/geology/catalog-closure/README.md
  - tests/domains/geology/governed-ai/README.md
tags: [kfm, tests, geology, borehole, well-log, rights, sensitivity, public-safe-geometry, fail-closed]
notes:
  - "This README documents the intended borehole/well-log rights test contract."
  - "It does not claim executable tests, fixtures, validators, policy rules, or CI wiring already exist."
  - "Tests must use synthetic or public-safe fixtures and must not include restricted real-world geometry or private source payloads."
[/KFM_META_BLOCK_V2] -->

# Tests — Geology Borehole Rights

> **Purpose.** This folder is the Geology-domain test lane for borehole and well-log rights. It proves that restricted or rights-limited subsurface reference records do not leak into `PROCESSED`, catalog, release, public map/API payloads, Evidence Drawer payloads, or governed AI answers through joins, summaries, or derivative artifacts.

## Placement

| Field | Value |
|---|---|
| Path | `tests/domains/geology/test_borehole_rights/` |
| Owning root | `tests/` |
| Domain | `geology` |
| Test lane | `test_borehole_rights` |
| Primary objects | `BoreholeReference`, `WellLogReference`, related subsurface-reference metadata |
| Status | `draft`; implementation coverage remains `UNKNOWN` |

This is a test lane only. It must not store fixtures, source payloads, schemas, policy rules, receipts, proofs, catalog records, release records, or package code.

## Evidence basis

The Geology Promotion Runbook requires SourceDescriptor records to carry role, authority, rights, sensitivity, cadence, and steward context at admission. It also says borehole and well-log feeds default to restricted or generalized sensitivity unless rights confirm otherwise, and names a proposed borehole/well-log rights validator that prevents restricted records from leaking into `PROCESSED` via joined or derivative payloads.

The Geology object-family document treats subsurface reference objects as sensitivity-controlled. It states that exact subsurface point locations default to restricted or generalized public geometry, and that public artifacts require public-safe geometry fingerprints and redaction receipt support where generalized.

## Proposed checks

| ID | Check | Expected behavior |
|---|---|---|
| `GEOL-BH-001` | Rights metadata required | Borehole or well-log source records without rights posture hold or fail. |
| `GEOL-BH-002` | Sensitivity posture required | Subsurface-reference records without sensitivity posture hold or fail. |
| `GEOL-BH-003` | Public-safe geometry required | Public surfaces receive only approved generalized/public-safe geometry. |
| `GEOL-BH-004` | Redaction receipt required | Generalized public derivatives carry a resolvable receipt/reference. |
| `GEOL-BH-005` | Restricted payload blocked | Restricted source detail does not enter public or release-bound payloads. |
| `GEOL-BH-006` | Join leakage blocked | Joined or derivative records do not bypass rights or sensitivity gates. |
| `GEOL-BH-007` | Well-log reference only | Public outputs use safe references, not raw/protected payloads. |
| `GEOL-BH-008` | Evidence closure required | Catalog/release candidates resolve EvidenceBundle, SourceDescriptor, and policy support. |
| `GEOL-BH-009` | Governed AI abstains | AI cannot cite restricted or unreleased borehole/well-log material as current truth. |
| `GEOL-BH-010` | Finite outcomes | Missing rights, sensitivity, receipt, or evidence returns bounded fail/hold/deny/abstain. |

## Proposed test files

```text
tests/domains/geology/test_borehole_rights/
├── README.md
├── test_rights_metadata_required.py         # PROPOSED
├── test_sensitivity_posture_required.py     # PROPOSED
├── test_public_safe_geometry_required.py    # PROPOSED
├── test_redaction_receipt_required.py       # PROPOSED
├── test_restricted_payload_blocked.py       # PROPOSED
├── test_join_leakage_blocked.py             # PROPOSED
├── test_well_log_reference_only.py          # PROPOSED
├── test_evidence_closure_required.py        # PROPOSED
├── test_governed_ai_abstains.py             # PROPOSED
└── test_finite_outcomes.py                  # PROPOSED
```

## Fixture posture

Use synthetic, no-network fixtures under the approved Geology fixture home. Valid fixtures should represent minimal rights-reviewed and public-safe subsurface-reference records. Invalid fixtures should isolate one failure at a time, such as missing rights posture, missing sensitivity posture, missing redaction receipt, missing EvidenceBundle, unsafe public geometry, derivative leakage, or AI citation of blocked material.

## Non-goals

This lane does not define source rights policy, store source records, publish map layers, authorize release, expose exact restricted detail, or turn generated summaries into evidence.

## Current implementation note

This README replaces an empty placeholder. It defines a proposed test matrix only. Executable tests, fixtures, validators, policy wiring, and CI remain `UNKNOWN` until verified.
