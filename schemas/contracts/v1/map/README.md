# `schemas/contracts/v1/map/` — Map Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-map-readme
title: schemas/contracts/v1/map/ — Map Schema Family Index
type: readme; schema-family-index; map-schema-boundary; map-publication-guardrail
authority_class: schema-family-index
version: v0.1
status: draft; map-family-present; PROPOSED scaffolds present; overlaps-layers-family; release-adjacent; tile-artifact-adjacent; no-parallel-authority; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Map steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Layer steward
  - OWNER_TBD — Tile steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; map; maplibre; map-ui; layer-manifest; style-manifest; tile-artifact-manifest; map-release-manifest; release-adjacent; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, map, maplibre, map-ui, layer-manifest, style-manifest, tile-artifact-manifest, map-release-manifest, layers-overlap, tiles, evidence-drawer, release, rollback, no-parallel-authority]
related:
  - ../README.md
  - ../layers/README.md
  - ../layers/layer_manifest.schema.json
  - ../layers/layer_descriptor.schema.json
  - ./layer_manifest.schema.json
  - ./style_manifest.schema.json
  - ./map_release_manifest.schema.json
  - ./tile_artifact_manifest.schema.json
  - ../../../../docs/architecture/maplibre-master.md
  - ../../../../docs/architecture/map-master/README.md
  - ../../../../docs/doctrine/map-first.md
  - ../../../../docs/standards/MVT.md
  - ../../../../docs/domains/archaeology/API_CONTRACTS.md
  - ../../../../docs/domains/atmosphere/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/fauna/API_CONTRACTS.md
  - ../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/people-dna-land/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/roads-rail-trade/API_CONTRACTS.md
  - ../../../../docs/domains/settlements-infrastructure/MAP_UI_CONTRACTS.md
  - ../../../../contracts/
  - ../../../../policy/
  - ../../../../fixtures/
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/map/README.md."
  - "Current search surfaced layer_manifest.schema.json, style_manifest.schema.json, map_release_manifest.schema.json, and tile_artifact_manifest.schema.json under this folder."
  - "Opened map schemas are PROPOSED scaffolds with empty properties and additionalProperties true; schema maturity remains NEEDS VERIFICATION."
  - "The map layer_manifest.schema.json overlaps conceptually with schemas/contracts/v1/layers/layer_manifest.schema.json, so shared layer-vs-map placement must be resolved before promotion."
  - "This folder defines map-related machine-checkable shapes only; it is not MapLibre runtime code, tile storage, release authority, policy authority, or a public-safe display guarantee."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-map-navy)
![authority](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-PROPOSED-orange)
![overlap](https://img.shields.io/badge/overlap-layers-yellow)
![release](https://img.shields.io/badge/release-adjacent-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/map/` is the shared schema family for map-facing object shapes: layer manifests, style manifests, tile artifact manifests, and map release manifest descriptors.
>
> **One-line boundary.** Map schemas define object shape only. They do not render MapLibre, publish tiles, authorize public display, decide sensitivity, prove evidence closure, or replace release records.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Map-vs-layers overlap](#map-vs-layers-overlap) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Map-family rules](#map-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/map/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Does this folder contain map schema files? | Yes. Search surfaced `layer_manifest.schema.json`, `style_manifest.schema.json`, `map_release_manifest.schema.json`, and `tile_artifact_manifest.schema.json`. | **CONFIRMED path evidence** |
| Are these schemas mature? | Not proven. Opened files are PROPOSED scaffolds with empty `properties` and `additionalProperties: true`. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Is there overlap with the `layers/` schema family? | Yes. Both `map/` and `layers/` have a `layer_manifest.schema.json` surface. | **CONFIRMED overlap** |
| Is `map_release_manifest.schema.json` a release record? | No. It is a schema scaffold for a map release manifest object; actual release records belong under release-governed roots. | **CONFIRMED boundary** |
| Is `tile_artifact_manifest.schema.json` a tile artifact? | No. It is a schema scaffold for describing tile artifacts; actual tile files/artifacts do not belong here. | **CONFIRMED boundary** |
| Can this folder store MapLibre runtime code, released payloads, map tiles, catalog records, or public artifacts? | No. This is a schema family folder, not a runtime, data, release, publication, tile, or UI root. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A map manifest is not a map release. A style manifest is not evidence. A tile artifact manifest is not a tile. Schema validation alone does not make a map surface public-safe.

---

## Authority and placement

This folder belongs under the schema responsibility root:

```text
schemas/contracts/v1/map/
```

It may define map-facing JSON Schema shapes when the following are clear:

- which semantic contract explains the object meaning;
- whether `layer_manifest` belongs here, under `layers/`, or both via an explicit profile strategy;
- which map object references released layer descriptors, style descriptors, tile artifact manifests, evidence, policy, release, correction, and rollback records;
- which fixtures and validators prove expected behavior;
- which API/UI/MapLibre consumers are allowed to rely on the shape;
- which sensitive or restricted map surfaces require fail-closed handling before display.

Adjacent authority remains separate:

- `schemas/contracts/v1/layers/` owns shared layer-family shapes unless an ADR/profile says otherwise.
- `schemas/contracts/v1/domains/<domain>/` owns domain-specific map/layer profiles and domain object shapes.
- `contracts/` owns semantic meaning.
- `policy/` owns allow/deny/restrict/abstain posture and exposure rules.
- `fixtures/` and `tests/` prove examples and validator behavior.
- `data/` owns lifecycle records, registries, receipts, proofs, catalog/triplet records, and published data products where applicable.
- `release/` owns promotion, release, correction, withdrawal, and rollback records.
- UI/API/MapLibre code renders released/public-safe payloads; it is not owned by this folder.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── map/
        │   ├── README.md                         # this file
        │   ├── layer_manifest.schema.json        # PROPOSED scaffold; overlaps layers/
        │   ├── style_manifest.schema.json        # PROPOSED scaffold
        │   ├── map_release_manifest.schema.json  # PROPOSED scaffold; release-adjacent
        │   └── tile_artifact_manifest.schema.json# PROPOSED scaffold; tile-artifact-adjacent
        ├── layers/
        │   ├── README.md
        │   ├── layer_manifest.schema.json        # overlapping shared layer-family shape
        │   ├── layer_descriptor.schema.json
        │   └── layer_catalog_item.schema.json
        └── domains/
            └── <domain>/                         # domain layer/map profiles where accepted

contracts/
policy/
fixtures/
tests/
data/
release/
```

---

## Current inventory

| Path | Kind | Current posture | Notes |
|---|---|---|---|
| `README.md` | README | **CONFIRMED present** | Parent map schema family index. |
| `layer_manifest.schema.json` | JSON Schema | **PROPOSED scaffold** | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/map/layer_manifest.schema.json`; empty `properties`; `additionalProperties: true`; source docs include Archaeology, Atmosphere, Fauna, Hazards, People/DNA/Land, Roads/Rail/Trade, and Settlements/Infrastructure API or map/UI docs. |
| `style_manifest.schema.json` | JSON Schema | **PROPOSED scaffold** | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/map/style_manifest.schema.json`; empty `properties`; `additionalProperties: true`; source docs include Atmosphere, People/DNA/Land, and Settlements/Infrastructure map/UI docs. |
| `map_release_manifest.schema.json` | JSON Schema | **PROPOSED scaffold / release-adjacent** | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/map/map_release_manifest.schema.json`; empty `properties`; `additionalProperties: true`; not an emitted release record. |
| `tile_artifact_manifest.schema.json` | JSON Schema | **PROPOSED scaffold / tile-artifact-adjacent** | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/map/tile_artifact_manifest.schema.json`; empty `properties`; `additionalProperties: true`; not a tile file or tile store. |

---

## Map-vs-layers overlap

Current evidence shows two related schema families:

| Family | Confirmed path | Role signal | Promotion risk |
|---|---|---|---|
| Map family | `schemas/contracts/v1/map/layer_manifest.schema.json` | Map-facing layer manifest scaffold. | May duplicate shared layer manifest meaning. |
| Layers family | `schemas/contracts/v1/layers/layer_manifest.schema.json` | Shared layer-family manifest scaffold. | May duplicate map family meaning unless `$ref` or profile strategy is chosen. |
| Domain profiles | `schemas/contracts/v1/domains/<domain>/layer_manifest.schema.json` | Domain-specific layer manifest profiles surfaced across many domains. | May drift from shared/map shapes unless profiled. |

Required decision before promotion:

```text
Option A: layers/layer_manifest is canonical; map/layer_manifest is deprecated or aliases it.
Option B: map/layer_manifest is canonical; layers/layer_manifest is deprecated or aliases it.
Option C: shared layers/layer_manifest is canonical, while map/layer_manifest is an explicit map-facing profile that $refs shared definitions.
Option D: both remain, but only with a documented ADR and no duplicate semantic fields.
```

Until that decision is made, treat both surfaces as **PROPOSED** and **NEEDS VERIFICATION**.

---

## What belongs here

- This README.
- Map-facing JSON Schema files such as `style_manifest`, `tile_artifact_manifest`, and map-release descriptor shapes.
- Map-specific profile notes for layer manifests if a shared-vs-map strategy is accepted.
- Links to paired semantic contracts, layer schemas, domain profiles, fixtures, validators, policy references, evidence references, release references, correction references, and rollback references.
- Migration notes if `map/` and `layers/` manifest schemas are consolidated, profiled, or renamed.

---

## What does not belong here

- MapLibre runtime code.
- UI/API implementation.
- Domain-owned canonical schemas except explicit map-facing profiles.
- Semantic contract prose beyond README boundary notes.
- Policy rules, sensitivity decisions, exposure decisions, or release decisions.
- Source data, lifecycle data, emitted map records, emitted layer records, vector tiles, raster tiles, style bundles, tile archives, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, public map artifacts, dashboards, screenshots, or generated summaries.
- Claims that a map, style, layer, tile artifact, or map release is valid, complete, evidence-backed, policy-safe, release-approved, or public-ready merely because it validates against a schema.

---

## Map-family rules

| Rule | Requirement |
|---|---|
| Shape is not runtime | A map schema constrains an object shape; it does not render a map. |
| Manifest is not release | `map_release_manifest.schema.json` defines shape only; release decisions and records live under release-governed roots. |
| Tile manifest is not tile storage | Tile artifact manifests describe artifacts; vector/raster tiles and archives do not belong here. |
| Style is not evidence | Style rules and MapLibre paint/layout decisions are not evidence for underlying claims. |
| Layer overlap must be governed | `map/layer_manifest` and `layers/layer_manifest` need `$ref`, profile, alias, or deprecation strategy. |
| Domain truth stays separate | Map objects should reference domain-owned objects, evidence, and release records rather than becoming domain truth. |
| Evidence must be explicit | Map objects that carry claims should resolve EvidenceRef to EvidenceBundle or equivalent support. |
| Policy must be explicit | Map objects intended for public or semi-public display need policy and sensitivity posture. |
| Release must be explicit | Public map payloads need release state, correction path, and rollback target support. |
| Public UI must be governed | Normal UI surfaces should consume governed APIs and released artifacts, not raw/canonical/internal stores. |

---

## Promotion checklist

A map schema or map-facing profile should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists.
- [ ] Map-vs-layers profile strategy is documented.
- [ ] `$id` is stable and follows the accepted namespace convention.
- [ ] Required fields are defined.
- [ ] Evidence references are defined where claims depend on evidence.
- [ ] Policy and sensitivity fields are defined where exposure matters.
- [ ] Release/correction/rollback references are defined for public use.
- [ ] Tile artifact references distinguish manifest metadata from artifact storage.
- [ ] Style references distinguish visual presentation from evidence.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Public-safe and restricted examples exist where needed.
- [ ] Validators exist.
- [ ] CI/schema-test coverage exists.
- [ ] API/UI/MapLibre consumers are documented without bypassing governed release paths.
- [ ] Migration notes exist for overlapping `map/`, `layers/`, and domain layer schemas.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the map schema family.
find schemas/contracts/v1/map -maxdepth 3 -type f | sort

# Compare map and layer manifest surfaces.
find schemas/contracts/v1/map schemas/contracts/v1/layers -maxdepth 3 -type f \
  | grep -Ei 'layer_manifest|layer_descriptor|style_manifest|map_release|tile_artifact|README' \
  | sort

# Detect potential map/layer/domain layer drift.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'layer_manifest|layer_descriptor|layer_catalog|style_manifest|map_release_manifest|tile_artifact_manifest|maplibre|mvt' \
  | sort

# Validate JSON syntax for map schemas.
find schemas/contracts/v1/map -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Validate JSON syntax for layer schemas.
find schemas/contracts/v1/layers -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/map/README.md`.

Rollback for future map schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore layer, domain, policy, evidence, release, correction, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public map surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `layer_manifest.schema.json` live under `map/`, `layers/`, or both through an explicit profile strategy? | **NEEDS VERIFICATION / ADR-sensitive** | Map steward + Layer steward + Schema steward |
| Which semantic contract owns `StyleManifest`, `TileArtifactManifest`, and `MapReleaseManifest` meaning? | **NEEDS VERIFICATION** | Contract steward + Map/UI steward |
| Should `map_release_manifest.schema.json` remain under `map/` or move/profile under `release/` schema families? | **NEEDS VERIFICATION / release-sensitive** | Release steward + Schema steward |
| Should tile artifact descriptors live under `map/`, `tiles/`, `artifacts/`, or a release-artifact schema family? | **NEEDS VERIFICATION / artifact-sensitive** | Tile steward + Release steward |
| Which fields are mandatory for public-safe map exposure? | **NEEDS VERIFICATION / policy-sensitive** | Policy steward + Release steward |
| Which MapLibre/API/Evidence Drawer consumers rely on these shapes? | **NEEDS VERIFICATION** | Map/UI steward + API steward |

---

## Maintainer notes

- Keep this folder focused on map-facing object shapes, not runtime rendering or actual map artifacts.
- Treat current schemas as PROPOSED scaffolds until fields, contracts, fixtures, validators, and release gates are verified.
- Prevent drift between `map/layer_manifest`, `layers/layer_manifest`, and domain `layer_manifest` profiles.
- Preserve evidence, sensitivity, domain ownership, policy, release, correction, and rollback boundaries for every map surface.
