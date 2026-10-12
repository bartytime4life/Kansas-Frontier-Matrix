<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hydrology/usgs-3dep/readme
title: Hydrology USGS 3DEP Raw README
path: data/raw/hydrology/usgs_3dep/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <hydrology-domain-steward>
  - <hydrology-source-steward>
  - <usgs-3dep-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Hydrology USGS 3DEP RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: hydrology
adjacent_domain: spatial-foundation
source_family: usgs_3dep
source_role: authority-model-input-per-subproduct
artifact_family: hydrology-usgs-3dep-raw-compatibility-reference
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
  - ../../geology/README.md
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
  - compatibility-reference
  - source-first
notes:
  - "This README replaces placeholder content at `data/raw/hydrology/usgs_3dep/README.md`."
  - "Parent `data/raw/hydrology/README.md` was a greenfield stub when this README was first authored on 2026-06-27; it is now a tracked compatibility/reference index."
  - "USGS 3DEP terrain is authority/model-input for elevation and terrain-derived hydrology, not observed water-level truth."
  - "3DEP sub-products require role separation: LAZ point clouds are observed source truth; DEMs and derivatives are modeled outputs; EPT/COPC are derivative analytic carriers."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology USGS 3DEP RAW Lane

Compatibility/reference documentation for Hydrology-facing USGS 3DEP RAW topology; not a physical source-capture home.

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
> `data/raw/hydrology/usgs_3dep/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named subtree is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed Hydrology truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, observed water-level truth, flood-event truth, engineering-grade flood-elevation authority, or generated-answer authority.

---

## Scope

This directory documents Hydrology-facing USGS 3DEP terrain/elevation source handling and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

KFM treats USGS 3DEP as elevation and terrain source material that can support terrain-derived hydrology after governed normalization. Within Hydrology, it is authority/model-input context for terrain surfaces, catchment derivation, flow-routing support, slope/aspect inputs, and vertical-datum checks. It is not observed water level, not gauge truth, not flood-event evidence, not NFHL regulatory truth, and not public release state by itself.

A governed source-first capture records what was captured, where it came from, what source role each sub-product carried, and which identifiers, times, rights notes, citations, acquisition windows, quality-level fields, horizontal CRS, vertical datum, geoid model, units, nodata policy, checksums, and caveats must travel downstream.

3DEP terrain is also cited by the Geology-facing RAW index [`../../geology/README.md`](../../geology/README.md) and by spatial-foundation architecture. Every such use must reference the same single source-first 3DEP capture, never a second domain-scoped copy.

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
| Artifact role | Compatibility/reference documentation for Hydrology-facing USGS 3DEP source handling and unresolved legacy RAW topology |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | Governed Hydrology WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
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
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; references may support Hydrology without duplicating RAW bytes. | A hydrology-scoped copy is not a second capture identity. |
| Physical placement is held | Do not infer `data/raw/hydrology/usgs_3dep/` or any subfolder as the capture home. Use only an accepted writer/path contract; none is established by this README. | This lane may retain governed references only. |
| LAZ point clouds | Capture as observed elevation source truth when admitted. | LAZ is not a DEM substitute; derived rasters must preserve lineage. |
| EPT / COPC | Capture as derivative analytic carrier tied back to LAZ. | Streaming/analytics carrier does not become a new source truth. |
| 1 m DEM / coarser DEM | Capture as modeled raster derivative when admitted. | DEM is not observed point-cloud truth and not observed water level. |
| Hillshade / slope / aspect / uncertainty | Capture as modeled second-order derivative when admitted. | Derived visualization or analysis surfaces must not be cited as observed elevation. |
| Terrain-derived hydrology | Preserve terrain lineage, datum, CRS, units, nodata, and uncertainty support. | Terrain input does not prove flow observation, flood event, or NFHL zone. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, review, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads.

The governed source-first capture or reference that supports Hydrology USGS 3DEP use must carry, where applicable:

- source-reference manifests;
- USGS 3DEP STAC references, TNM/download references, LAZ references, EPT/COPC references, DEM raster references, derivative raster references, uncertainty references, or raw payload references;
- source family, sub-product identity, source role, acquisition window, quality level, horizontal CRS, vertical datum, geoid model, vertical/horizontal units, nodata value, data type, source point-cloud reference, derivation chain, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, point counts, raster metadata, tile counts, or service metadata where applicable, and checksums.

None of these, and no local README or index, becomes proof, catalog, registry, policy, release, public artifact, water-observation truth, model truth, or answer authority.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Hydrology. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source-run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Earlier drafts sketched sub-product run groupings: `laz/` runs carrying `source_reference.json`, `pointcloud_ref.json`, `acquisition_ref.json`, `crs_datum_units_ref.json`, `checksums.sha256`, and a run README; `ept-copc/` runs carrying `source_reference.json`, `analytic_carrier_ref.json`, `source_pointcloud_ref.json`, `checksums.sha256`, and a run README; `dem/` runs carrying `source_reference.json`, `raster_ref.json`, `derivation_chain_ref.json`, `crs_datum_units_ref.json`, `checksums.sha256`, and a run README; and `derivatives/` runs carrying `source_reference.json`, `derivative_raster_ref.json`, `derivation_chain_ref.json`, `uncertainty_ref.json`, `checksums.sha256`, and a run README, plus an optional RAW-local index. That layout is a proposed shape for a future accepted source-first home, not this subtree.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was captured, but no downstream decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, rights, source surface, acquisition window, quality level, CRS/datum/units, lineage, citation, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Hydrology WORK only when SourceDescriptor, rights posture, source role, source-family identity, citation, hash, CRS/datum/units metadata, lineage metadata, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence, datum/unit validation, lineage/provenance closure, and rollback target. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/hydrology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Hydrology-scoped copy.
- [ ] Treat this source-named README as compatibility/reference documentation only; do not create a child directory as a payload destination.
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
| Parent `data/raw/hydrology/README.md` was a greenfield stub when this README was first authored (2026-06-27). | **CONFIRMED historically; superseded — the parent is now a tracked compatibility/reference index reconciled on 2026-10-11** |
| Hydrology source-registry doctrine lists USGS 3DEP terrain as authority/model-input for elevation surface and terrain-derived hydrology, not observed water level. | **CONFIRMED by GitHub contents API during this edit** |
| USGS 3DEP catalog doctrine separates LAZ observed source truth, EPT/COPC analytic carriers, DEM modeled derivatives, and hillshade/slope/aspect second-order derivatives. | **CONFIRMED by GitHub contents API during this edit** |
| USGS 3DEP catalog doctrine says CRS, vertical datum, geoid model, units, nodata, source point-cloud reference, and derivation chain are gate-critical. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual USGS 3DEP RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
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
- [`../../geology/README.md`](../../geology/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hydrology-facing USGS 3DEP compatibility/reference lane. One governed source-first capture may support Hydrology without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, observed-water-level truth, observed-flood truth, NFHL regulatory truth, engineering-grade flood-elevation authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
