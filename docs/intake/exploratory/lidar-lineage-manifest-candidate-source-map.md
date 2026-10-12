<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/lidar-lineage-manifest-candidate-source-map
title: LiDAR Lineage Manifest Candidate Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Geospatial steward · Data steward · Map steward · Sensitivity steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded adaptation of the LiDAR lineage proposal into a bounded synthetic candidate without activating a source, executing a transform, or creating scene authority
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION source rights and hosted exact-head execution
related:
  - ../../../contracts/data/lidar_lineage_manifest_candidate.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../architecture/planetary-3d.md
  - ../../sources/catalog/usgs/3dep-elevation.md
tags: [kfm, lidar, lineage, terrain, vertical-datum, maplibre, source-map]
[/KFM_META_BLOCK_V2] -->

# LiDAR Lineage Manifest Candidate Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards`, document `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho` | The "LiDAR Lineage Manifest" card names collection program, vintage, classification, vertical datum, point density, and sensor as distinct lineage needed by terrain and 3D carriers. | Proposal register; its `scene/lidar` path is explicitly ADR-pending. |
| `docs/architecture/planetary-3d.md` | Existing architecture keeps 3D and synthetic carriers downstream of evidence and requires reality-boundary disclosure. | Architecture doctrine; not source activation or release proof. |
| `docs/sources/catalog/usgs/3dep-elevation.md` and `connectors/usgs/3dep/README.md` | Existing repository surfaces identify 3DEP as a candidate elevation/LiDAR source family. | Source documentation and connector boundary; current rights, products, and operational use remain separate. |
| Adopted Directory Rules v2 | Paths are assigned by responsibility and proposed source paths do not create authority. | Placement law only; it does not decide whether the object is adopted. |

## Repository reconciliation

GitHub `main@c4cb046829f72afd07e39d167c781fb7435a9ac4` contained 3DEP
source/connector documentation and 3D architecture guidance, but exact searches
found no `lidar_lineage_manifest`, `LidarLineageManifestCandidate`, or matching
classification-and-vertical-datum validator packet.

The Drive card's proposed `schemas/contracts/v1/scene/lidar/` home remains
unaccepted. This packet therefore uses existing `contracts/data/` and
`schemas/contracts/v1/data/` responsibility lanes and states that choice
explicitly rather than creating a `scene/` authority.

## Bounded adaptation

| Source pressure | Retained behavior | Deferred authority |
|---|---|---|
| Acquisition lineage | Program, collection ID, acquisition interval, sensor, and digest are explicit. | Source activation, rights, and byte verification. |
| Classification lineage | Standard, available classes, and selected classes remain distinct. | Classification accuracy and operational filtering. |
| Vertical lineage | Source/target vertical CRS, datum, units, and transform declaration are explicit. | Transform correctness and geodetic acceptance. |
| Derived carriers | Point-cloud, terrain, and scene outputs cannot claim observed source truth. | Release, MapLibre runtime behavior, and public use. |
| Sensitive detail | Exact infrastructure exposure is fixed false and transforms remain references. | Instance-level policy and steward approval. |

## Path decision

~~~yaml
path_decision:
  artifact: LidarLineageManifestCandidate
  proposed_path: contracts/data/lidar_lineage_manifest_candidate.md
  artifact_kind: semantic contract
  authority_owner: bounded data-lineage candidate meaning
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: object_family
  scope_id: lidar-lineage-manifest-candidate
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/architecture/planetary-3d.md
    - docs/sources/catalog/usgs/3dep-elevation.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

The data contract lane owns this bounded lineage-candidate meaning. The packet
does not establish a `scene/` contract/schema lane, source registry entry,
derived artifact store, or release path.

## Non-effects

This packet does not activate a source, retrieve or transform bytes, validate a
point-cloud format, establish geodetic accuracy, expose exact infrastructure,
resolve evidence, evaluate policy, approve review, promote, release, deploy,
publish, or authorize public use.
