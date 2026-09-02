<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-30-lidar-derived-product-lineage-source-map
title: Pass 30 LiDAR Derived Product Lineage Receipt Source Map
type: source-adaptation-record
version: v0.1.0
status: draft; PROPOSED adaptation; repository-grounded; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory-intake; pass-30; lidar; lineage
owning_root: docs/
responsibility: Record how KFM-P30-PROG-0028 was reconciled with current repository evidence and narrowed into a fixture-only lineage receipt.
truth_posture: "CONFIRMED source and repository evidence; PROPOSED contract; UNKNOWN operational state; NEEDS VERIFICATION human review"
related:
  - ../../../contracts/spatial-foundation/lidar_derived_product_lineage_receipt.md
  - ../../../schemas/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt.schema.json
  - ../../../fixtures/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt/cases.json
  - ../../../tools/validators/validate_lidar_derived_product_lineage_receipt.py
  - ../../../tests/validators/test_validate_lidar_derived_product_lineage_receipt.py
  - ../../sources/catalog/usgs/3dep-elevation.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
tags: [kfm, pass-30, source-map, lidar, laz, copc, ept, dem, terrain, lineage, fixture-first]
notes:
  - "The consolidated atlas is proposal pressure and remains non-authoritative."
  - "The selected adaptation creates no source admission, live artifact, lifecycle mutation, catalog record, release, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pass 30 LiDAR Derived Product Lineage Receipt Source Map

## Goal

Turn the smallest dependency-closed portion of `KFM-P30-PROG-0028` into a reviewable repository capability without treating an atlas card, a fixture hash, or a local validator pass as external evidence or operational authority.

## Source boundary

The attached `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` has SHA-256 digest:

```text
020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639
```

The retained card states:

| Card | State | Card identity | Proposal |
|---|---|---|---|
| `KFM-P30-PROG-0028` | `active`, `UNCHANGED`, `PROPOSED`; implementation `UNKNOWN` in the source | `sha256:2b7745b5907cf7b607ebed642e7fb87d4abfaf7bd24522e2b453425ec25c75ed` | Emit lineage receipts from LAZ source tiles through COPC/EPT access products and DEM/terrain derivatives. |

The PDF and card hashes identify the supplied source and retained card. They are not implementation, artifact, evidence, or release hashes.

## Current repository evidence inspected

At the selected base revision, the repository already contains:

- `docs/sources/catalog/usgs/3dep-elevation.md`, which distinguishes LAZ source capture, EPT/COPC analytic delivery, and modeled DEM/terrain derivatives;
- explicit requirements for acquisition window, quality level, horizontal CRS, vertical datum, geoid model, units, transform receipts, and LAZ ancestry;
- the accepted Directory Rules ADR and adopted Directory Rules document;
- a canonical RFC 8785 JCS plus SHA-256 hashing package;
- local JSON Schema resolution, exact fixture-oracle, no-network CI, and generated-receipt patterns; and
- spatial-foundation ownership of cross-domain representation, control, reference systems, and geometry lineage.

Repository search found documentation and connector pressure for the chain but no strict `LidarDerivedProductLineageReceipt` schema, semantic validator, or reviewed positive/negative fixture family. That is the bounded implementation gap selected here.

## Reconciliation decision

The source wording calls COPC/EPT “access products.” Current repository guidance says they retain observation semantics while being derivative carriers. The adaptation therefore separates:

- `source_role`: `OBSERVED` or `MODELED`; and
- `product_role`: source capture, analytic access carrier, elevation model, or terrain derivative.

This preserves existing meaning and avoids inventing a second source-role vocabulary. LAZ is the only source-capture root. COPC/EPT do not become a new observation. DEM/terrain do not become observed or substitute for the point cloud.

## Directory Rules decision

| Responsibility signature | Decision |
|---|---|
| Primary responsibility | Cross-domain LiDAR product lineage and spatial reference preservation |
| Semantic owner | `contracts/spatial-foundation/` |
| Machine shape | `schemas/contracts/v1/spatial-foundation/` |
| Proof surfaces | Existing `fixtures/`, `tools/validators/`, `tests/`, and `.github/workflows/` roots |
| Accountability | Existing `data/receipts/generated/` authoring-receipt exception |
| Lifecycle phase | None; fixture and validation artifacts only |
| Exposure | Internal review; opaque references and synthetic hashes only |
| Root admission | No new root |
| ADR trigger | No authority-root, lifecycle, schema-home, or public-path change |

## Admission ledger

### Admitted and implemented

| Candidate element | Disposition | Reason |
|---|---|---|
| One LAZ source-capture root | `ADMIT` | Preserves the repository’s source hierarchy. |
| COPC/EPT analytic access carrier nodes | `ADAPT` | Keeps observed semantics and explicit derivation from LAZ. |
| DEM/terrain modeled derivative nodes | `ADMIT` | Prevents role up-cast and point-cloud substitution. |
| Parent DAG and transform receipt references | `ADMIT` | Makes every derivation edge explicit and locally closable. |
| Acquisition window and quality level inheritance | `ADMIT` | Preserves when and at what declared collection quality the returns were captured. |
| Horizontal CRS, vertical datum, geoid, and units | `ADMIT` | Matches current gate-critical repository guidance. |
| Exact artifact and receipt hashes | `ADAPT` | Uses opaque synthetic bindings; no artifact bytes are claimed verified. |
| Deterministic identity and summary projection | `ADMIT` | Uses current repository hashing authority. |
| Exact positive/negative fixtures and no-network CI | `ADMIT` | Provides non-vacuous, reviewable local proof. |

### Deferred

| Candidate | Required next evidence |
|---|---|
| Live USGS/TNM/STAC resolution or download | Admitted source descriptor, rights, endpoints, retry/rate-limit rules, integrity receipts, and connector review. |
| Cross-CRS, cross-datum, or cross-unit lineage | Transform semantics, numeric test oracle, precision/uncertainty rules, and independently reviewed fixtures. |
| Actual LAZ/COPC/EPT/DEM inspection | Bounded binary/raster/point-cloud validators, size limits, sandbox policy, and trusted fixture assets. |
| Catalog or PROV-O projection | Canonical catalog owner, object mappings, supersession behavior, and projection validation. |
| Map or provenance-browser UI | Released public-safe contract, API projection, sensitivity policy, correction path, and rollback target. |
| Policy, promotion, release, deployment, publication | Separate authoritative decisions and human approvals. |

### Rejected from this review boundary

| Behavior | Reason |
|---|---|
| DEM represented as observed or as a complete point-cloud substitute | Violates source-role anti-collapse. |
| COPC/EPT represented as a new source capture | Collapses a derived carrier into source authority. |
| Derived node without an earlier parent, transform receipt, or LAZ ancestor | Breaks lineage closure. |
| Silent acquisition, CRS, datum, geoid, quality-level, or unit change | Exceeds this profile and can change meaning. |
| Real URLs, coordinates, geometry, point-cloud bytes, or elevation values | Unnecessary for the selected fixture-only proof and would widen trust/sensitivity scope. |
| Source, evidence, policy, lifecycle, release, or public-use claims | No authoritative process is executed. |

## Dependency-closed packet

```text
contracts/spatial-foundation/lidar_derived_product_lineage_receipt.md
schemas/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt.schema.json
fixtures/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt/cases.json
tools/validators/validate_lidar_derived_product_lineage_receipt.py
tests/validators/test_validate_lidar_derived_product_lineage_receipt.py
.github/workflows/lidar-derived-product-lineage-receipt.yml
data/receipts/generated/genrec-pass30-lidar-lineage-receipt-20260809.json
docs/intake/exploratory/pass-30-lidar-derived-product-lineage-source-map.md
```

## Acceptance boundary

The slice is complete only when the schema is closed; identities recompute; both valid carrier/model chains pass; source-role, product-role, ancestry, topology, transform, acquisition, spatial-reference, order, authority, and identity violations fail closed; diagnostics are deterministic and do not echo untrusted values; no network/write surface exists; the generated authoring receipt binds final bytes; and hosted exact-head checks plus human semantic review remain separate.

## Non-effects and rollback

This packet does not fetch source data, admit a source, mutate a lifecycle lane, write a catalog, verify an external artifact, evaluate policy, release, deploy, publish, or authorize public use. Before merge, close the draft pull request and delete the feature branch. After merge, revert the bounded commit or merge commit; no live-state migration or public correction is required.

<p align="right"><a href="#top">Back to top</a></p>
