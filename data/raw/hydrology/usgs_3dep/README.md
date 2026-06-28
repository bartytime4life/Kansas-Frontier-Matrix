<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hydrology/usgs-3dep/readme
name: Hydrology USGS 3DEP Raw README
path: data/raw/hydrology/usgs_3dep/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <hydrology-domain-steward>
  - <hydrology-source-steward>
  - <usgs-3dep-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: hydrology
adjacent_domain: spatial-foundation
source_family: usgs_3dep
source_role: authority-model-input-per-subproduct
artifact_family: immutable-hydrology-usgs-3dep-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; terrain-not-water-observation; datum-crs-gate-critical; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../quarantine/hydrology/README.md
  - ../../../processed/hydrology/README.md
  - ../../../catalog/domain/hydrology/README.md
  - ../../../published/layers/hydrology/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../../docs/domains/hydrology/SOURCE_FAMILIES.md
  - ../../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../../docs/sources/catalog/usgs/3dep-elevation.md
  - ../../../../docs/sources/catalog/usgs/README.md
  - ../../../../docs/architecture/spatial-foundation.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hydrology
  - spatial-foundation
  - usgs
  - usgs-3dep
  - terrain
  - elevation
  - dem
  - lidar
  - laz
  - ept
  - copc
  - datum
  - crs
  - model-input
  - source-capture
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/hydrology/usgs_3dep/README.md`."
  - "Parent `data/raw/hydrology/README.md` is currently a greenfield stub."
  - "USGS 3DEP terrain is authority/model-input for elevation and terrain-derived hydrology, not observed water-level truth."
  - "3DEP sub-products require role separation: LAZ point clouds are observed source truth; DEMs and derivatives are modeled outputs; EPT/COPC are derivative analytic carriers."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology USGS 3DEP RAW Lane

RAW source-family lane for immutable USGS 3DEP terrain/elevation source captures and source-admission sidecars in the Hydrology domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Source family: USGS 3DEP" src="https://img.shields.io/badge/source-USGS%203DEP-1f6feb">
  <img alt="Role: authority / model input" src="https://img.shields.io/badge/role-authority%20%2F%20model--input-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [USGS 3DEP source posture](#usgs-3dep-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/hydrology/usgs_3dep/` is a RAW source-capture lane. It is not processed Hydrology truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, observed water-level truth, flood-event truth, engineering-grade flood-elevation authority, or generated-answer authority.

---

## Scope

This directory is for immutable USGS 3DEP terrain/elevation source captures and RAW-local sidecars in the Hydrology domain.

KFM treats USGS 3DEP as elevation and terrain source material that can support terrain-derived hydrology after governed normalization. Within Hydrology, it is authority/model-input context for terrain surfaces, catchment derivation, flow-routing support, slope/aspect inputs, and vertical-datum checks. It is not observed water level, not gauge truth, not flood-event evidence, not NFHL regulatory truth, and not public release state by itself.

RAW records what was captured, where it came from, what source role each sub-product carried, and which identifiers, times, rights notes, citations, acquisition windows, quality-level fields, horizontal CRS, vertical datum, geoid model, units, nodata policy, checksums, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hydrology/usgs_3dep/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hydrology` |
| Adjacent lane | `spatial-foundation` for terrain/elevation cataloging |
| Source family | `usgs_3dep` |
| Source role | Heterogeneous by sub-product: observed LAZ, analytic EPT/COPC carrier, modeled DEM/derivatives; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/hydrology/` or `data/quarantine/hydrology/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when sub-product role, rights, source surface, acquisition window, datum/CRS/units, quality level, citation, lineage, validation, or release support is insufficient |

---

## USGS 3DEP source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| LAZ point clouds | Capture as observed elevation source truth when admitted. | LAZ is not a DEM substitute; derived rasters must preserve lineage. |
| EPT / COPC | Capture as derivative analytic carrier tied back to LAZ. | Streaming/analytics carrier does not become a new source truth. |
| 1 m DEM / coarser DEM | Capture as modeled raster derivative when admitted. | DEM is not observed point-cloud truth and not observed water level. |
| Hillshade / slope / aspect / uncertainty | Capture as modeled second-order derivative when admitted. | Derived visualization or analysis surfaces must not be cited as observed elevation. |
| Terrain-derived hydrology | Preserve terrain lineage, datum, CRS, units, nodata, and uncertainty support. | Terrain input does not prove flow observation, flood event, or NFHL zone. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- USGS 3DEP STAC references, TNM/download references, LAZ references, EPT/COPC references, DEM raster references, derivative raster references, uncertainty references, or raw payload references;
- source family, sub-product identity, source role, acquisition window, quality level, horizontal CRS, vertical datum, geoid model, vertical/horizontal units, nodata value, data type, source point-cloud reference, derivation chain, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, point counts, raster metadata, tile counts, or service metadata where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, water-observation truth, model truth, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| USGS 3DEP/source-family doctrine | `docs/sources/catalog/usgs/` or `docs/domains/hydrology/` |
| Connector code or connector decisions | `connectors/usgs/` or `connectors/usgs/3dep/` if present |
| Pipeline code or pipeline decisions | `pipelines/domains/hydrology/` |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, sensitivity, datum/unit policy, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/hydrology/` |
| Normalized working material | `data/work/hydrology/` |
| Validated Hydrology objects | `data/processed/hydrology/` |
| Catalog, triplets, graph truth, STAC/DCAT/PROV closure, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Observed water level, observed flood event, NFHL regulatory truth, engineering-grade flood-elevation claim, public artifact authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hydrology/usgs_3dep/
├── README.md
├── laz/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── pointcloud_ref.json
│       ├── acquisition_ref.json
│       ├── crs_datum_units_ref.json
│       ├── checksums.sha256
│       └── README.md
├── ept-copc/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── analytic_carrier_ref.json
│       ├── source_pointcloud_ref.json
│       ├── checksums.sha256
│       └── README.md
├── dem/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── raster_ref.json
│       ├── derivation_chain_ref.json
│       ├── crs_datum_units_ref.json
│       ├── checksums.sha256
│       └── README.md
├── derivatives/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── derivative_raster_ref.json
│       ├── derivation_chain_ref.json
│       ├── uncertainty_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was captured, but no downstream decision has been made. |
| Quarantine | Source role, rights, source surface, acquisition window, quality level, CRS/datum/units, lineage, citation, schema, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, source-family identity, citation, hash, CRS/datum/units metadata, lineage metadata, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence, datum/unit validation, lineage/provenance closure, and rollback target. |

---

## Forbidden shortcut

```text
data/raw/hydrology/usgs_3dep/
→ data/processed/hydrology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hydrology lane and the USGS 3DEP source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, sub-product identity, rights, cadence, citation, acquisition window, quality level, CRS/datum/units posture, and hash posture.
- [ ] Confirm LAZ, EPT/COPC, DEM, and derivative rasters are not collapsed into one source role.
- [ ] Confirm DEMs and hillshade/slope/aspect derivatives are not treated as observed elevation or observed water level.
- [ ] Confirm horizontal CRS, vertical datum, geoid model where applicable, vertical/horizontal units, nodata value, and analysis vs delivery CRS are preserved.
- [ ] Confirm DEM and derivative outputs preserve LAZ → DEM → derivative lineage where applicable.
- [ ] Confirm terrain-derived hydrology claims do not become flow observations, observed flood events, NFHL regulatory truth, or engineering-grade flood-elevation claims without owning downstream evidence.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/hydrology/usgs_3dep/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/hydrology/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Hydrology source-registry doctrine lists USGS 3DEP terrain as authority/model-input for elevation surface and terrain-derived hydrology, not observed water level. | **CONFIRMED by GitHub contents API during this edit** |
| USGS 3DEP catalog doctrine separates LAZ observed source truth, EPT/COPC analytic carriers, DEM modeled derivatives, and hillshade/slope/aspect second-order derivatives. | **CONFIRMED by GitHub contents API during this edit** |
| USGS 3DEP catalog doctrine says CRS, vertical datum, geoid model, units, nodata, source point-cloud reference, and derivation chain are gate-critical. | **CONFIRMED by GitHub contents API during this edit** |
| Actual USGS 3DEP RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, observed-water-level truth, model truth, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../quarantine/hydrology/README.md`](../../../quarantine/hydrology/README.md)
- [`../../../processed/hydrology/README.md`](../../../processed/hydrology/README.md)
- [`../../../catalog/domain/hydrology/README.md`](../../../catalog/domain/hydrology/README.md)
- [`../../../published/layers/hydrology/README.md`](../../../published/layers/hydrology/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/hydrology/SOURCE_REGISTRY.md`](../../../../docs/domains/hydrology/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/hydrology/OBJECT_FAMILIES.md`](../../../../docs/domains/hydrology/OBJECT_FAMILIES.md)
- [`../../../../docs/domains/hydrology/SOURCE_FAMILIES.md`](../../../../docs/domains/hydrology/SOURCE_FAMILIES.md)
- [`../../../../docs/domains/hydrology/DATA_LIFECYCLE.md`](../../../../docs/domains/hydrology/DATA_LIFECYCLE.md)
- [`../../../../docs/sources/catalog/usgs/3dep-elevation.md`](../../../../docs/sources/catalog/usgs/3dep-elevation.md)
- [`../../../../docs/sources/catalog/usgs/README.md`](../../../../docs/sources/catalog/usgs/README.md)
- [`../../../../docs/architecture/spatial-foundation.md`](../../../../docs/architecture/spatial-foundation.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hydrology USGS 3DEP RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, observed-water-level truth, observed-flood truth, NFHL regulatory truth, engineering-grade flood-elevation authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
