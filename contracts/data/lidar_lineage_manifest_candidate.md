<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/lidar-lineage-manifest-candidate
title: LiDAR Lineage Manifest Candidate
type: semantic-contract
version: v0.1.0
status: proposed; experimental; fixture-only; non-authoritative
owners: OWNER_TBD — Geospatial steward · Data steward · Map steward · Sensitivity steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; data; lidar; lineage; terrain; fixture-only
owning_root: contracts/
responsibility: Define a bounded synthetic LiDAR lineage candidate that preserves acquisition, classification, vertical datum, processing, derived-carrier, evidence, and public-safety declarations without activating a source or authorizing release.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED deterministic synthetic implementation / NEEDS VERIFICATION source rights, final object home, operational readers, and steward review
related:
  - ../../schemas/contracts/v1/data/lidar_lineage_manifest_candidate.schema.json
  - ../../fixtures/contracts/v1/data/lidar_lineage_manifest_candidate/cases.json
  - ../../tools/validators/data/validate_lidar_lineage_manifest_candidate.py
  - ../../tests/validators/data/test_lidar_lineage_manifest_candidate.py
  - ../../docs/intake/exploratory/lidar-lineage-manifest-candidate-source-map.md
  - ../../docs/architecture/planetary-3d.md
  - ../../docs/sources/catalog/usgs/3dep-elevation.md
tags: [kfm, lidar, point-cloud, terrain, vertical-datum, lineage, maplibre, fixture-only]
notes:
  - "Implements a bounded contract-first slice of the Full Atlas LiDAR Lineage Manifest proposal."
  - "The source card's proposed scene/lidar schema home is not adopted; this candidate uses existing data contract/schema lanes and creates no scene authority."
[/KFM_META_BLOCK_V2] -->

# LiDAR Lineage Manifest Candidate

## Status and purpose

`LidarLineageManifestCandidate` is a **PROPOSED**, experimental, fixture-only
contract for preserving the acquisition and processing facts needed to
interpret LiDAR-derived terrain, point-cloud, and 3D scene carriers.

The source card calls out collection program, vintage, classification, vertical
datum, point density, and sensor identity as the minimum lineage that should not
be lost when a point cloud becomes a terrain or scene artifact. This candidate
adds those declarations while keeping observed point-cloud input distinct from
derived terrain and representation outputs.

A `PASS` means only that one synthetic declaration is internally coherent. It
does not prove source bytes, rights, accuracy, vertical transformation quality,
point classification quality, public safety, release state, or operational
MapLibre behavior.

## Preserved distinctions

- **Observed input vs. derived carrier.** The source role is fixed to
  `OBSERVED_POINT_CLOUD`; outputs may be `DERIVED_POINT_CLOUD`,
  `DERIVED_TERRAIN`, or `DERIVED_SCENE`, never source truth.
- **Horizontal vs. vertical reference.** Horizontal CRS, vertical CRS, vertical
  datum, units, and any vertical transform are declared separately.
- **Classification vs. filtering.** The upstream classification standard and
  available classes remain distinct from classes selected for a derivative.
- **Evidence vs. representation.** Scene outputs require an EvidenceBundle
  reference and a RealityBoundaryNote reference.
- **Internal precision vs. public safety.** Exact infrastructure exposure is
  fixed false; public use and release authority remain fixed false.

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | The synthetic lineage candidate is internally coherent. | Still `REVIEW_REQUIRED`; no source, artifact, or scene is admitted. |
| `DENY` | Shape, identity, temporal, vertical, classification, reference, role, or safety invariants fail. | No transform, release, or fallback inference. |
| `ERROR` | Input or schema cannot be boundedly read. | No partial lineage is trusted. |

## Directory Rules basis

The card suggested `schemas/contracts/v1/scene/lidar/`, but also marked that
placement ADR-pending. Current adopted Directory Rules prohibit turning that
suggestion into authority. This packet instead uses existing responsibility
lanes:

| Responsibility | Home |
|---|---|
| Candidate semantic meaning | `contracts/data/` |
| Machine shape | `schemas/contracts/v1/data/` |
| Synthetic cases | `fixtures/contracts/v1/data/` |
| Deterministic validation | `tools/validators/data/` |
| Executable conformance evidence | `tests/validators/data/` |
| Hosted read-only orchestration | `.github/workflows/` |
| Source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No source connector, scene root, terrain store, published artifact, or new
authority lane is created.

## Non-effects

A green result does not:

- activate USGS 3DEP or another source;
- retrieve, open, transform, or publish point-cloud or raster bytes;
- validate LAS, LAZ, COPC, EPT, COG, PMTiles, 3D Tiles, or glTF;
- prove vertical datum conversion or classification accuracy;
- approve a sensitive-location transform;
- create EvidenceBundle, policy, review, promotion, release, deployment, or
  public-use authority.

## Rollback

Before merge, close the draft pull request and remove its branch. After an
authorized merge, revert this additive packet and rerun its dedicated workflow.
No source, data, map, scene, release, deployment, or public state requires
restoration.
