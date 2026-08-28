<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hydrology/usgs-water-data/readme
name: Hydrology USGS Water Data Raw README
path: data/raw/hydrology/usgs_water_data/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <hydrology-domain-steward>
  - <hydrology-source-steward>
  - <usgs-water-data-source-steward>
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
adjacent_domain: hazards
source_family: usgs_water_data
source_role: observed-aggregate-administrative-modeled-per-subproduct
artifact_family: immutable-hydrology-usgs-water-data-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; provisional-approved-state-preserved; aggregate-not-instantaneous; not-regulatory; not-forecast; rights-needs-verification; release-blocked
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
  - ../../../../docs/sources/catalog/usgs/nwis-water.md
  - ../../../../docs/sources/catalog/usgs/nhdplus-hr.md
  - ../../../../docs/sources/catalog/usgs/README.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hydrology
  - hazards
  - usgs
  - usgs-water-data
  - nwis
  - gauge
  - streamflow
  - groundwater
  - water-quality
  - instantaneous-values
  - daily-values
  - provisional-approved
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/hydrology/usgs_water_data/README.md`."
  - "Parent `data/raw/hydrology/README.md` is currently a greenfield stub."
  - "USGS Water Data / NWIS material is observed, aggregate, administrative, or modeled by sub-product. The approval-status lifecycle must travel with observed values."
  - "This lane is not NHDPlus network identity, FEMA NFHL regulatory context, operational forecast, water-rights enforcement, dam-operation authority, public release, or generated-answer authority."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology USGS Water Data RAW Lane

RAW source-family lane for immutable USGS Water Data / NWIS source captures and source-admission sidecars in the Hydrology domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Source family: USGS Water Data" src="https://img.shields.io/badge/source-USGS%20Water%20Data-1f6feb">
  <img alt="Role: observed / aggregate" src="https://img.shields.io/badge/role-observed%20%2F%20aggregate-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [USGS Water Data source posture](#usgs-water-data-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/hydrology/usgs_water_data/` is a RAW source-capture lane. It is not processed Hydrology truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, NHDPlus network truth, NFHL regulatory truth, operational forecast authority, water-rights authority, dam-operation authority, or generated-answer authority.

---

## Scope

This directory is for immutable USGS Water Data / NWIS source captures and RAW-local sidecars in the Hydrology domain.

KFM treats USGS Water Data as the primary observed-hydrology source family for gauge stations, monitoring sites, instantaneous readings, peak flows, groundwater levels, and water-quality readings, with separate handling for site metadata, daily values, annual statistics, and rating curves. It may support downstream `GaugeSite`, `FlowObservation`, `WaterLevelObservation`, `WaterQualityObservation`, `GroundwaterWell`, and Hazards context after governed normalization, but RAW capture is not public release state by itself.

RAW records what was captured, where it came from, what source role each sub-product carried, and which site IDs, parameter codes, timestamps, approval status, statistic/aggregation units, method metadata, datum, rating-curve references, rights notes, citations, retrieval times, checksums, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hydrology/usgs_water_data/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hydrology` |
| Adjacent lane | `hazards` for flood-context joins after governed review |
| Source family | `usgs_water_data` |
| Source role | Heterogeneous by sub-product: administrative site metadata, observed IV/peak/water-quality readings, aggregate daily/annual values, modeled rating curves; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/hydrology/` or `data/quarantine/hydrology/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when sub-product role, rights, endpoint identity, site identity, parameter code, approval status, aggregation unit, method metadata, datum, rating-curve reference, citation, freshness, validation, or release support is insufficient |

---

## USGS Water Data source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Site metadata | Capture as administrative site/source material when admitted. | A site record is not evidence of a current water condition. |
| Instantaneous Values — provisional | Capture as observed readings with `approval_status: provisional`. | Provisional readings must not be cited as approved values. |
| Instantaneous Values — approved | Capture as observed readings with `approval_status: approved`. | Still requires provenance, timestamp, parameter code, and site identity. |
| Peak flows | Capture as observed peak records with uncertainty/rating context where present. | Peak records must not drop rating-curve uncertainty or method context. |
| Daily values | Capture as aggregate values with `role_aggregation_unit: 1d`. | Daily means/max/min are not instantaneous observations. |
| Annual statistics | Capture as aggregate values with `role_aggregation_unit: 1yr`. | Annual summaries are not per-instant or per-event truth. |
| Water-quality records | Capture as observed records with method, detection-limit, unit, and parameter metadata where present. | Method and detection-limit context must not be stripped. |
| Rating-curve metadata | Capture as modeled/calibration context when admitted. | Stage-to-discharge transfer functions are not direct observations. |
| Legacy / modern endpoint pair | Preserve endpoint used, migration state, and parity notes where applicable. | Endpoint migration must not silently merge conflicting results. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- USGS Water Data API references, legacy NWIS/WaterServices references, site metadata references, IV references, DV references, peak-flow references, annual-statistics references, water-quality references, rating-curve references, or raw payload references;
- site ID, monitoring location identity, parameter code, statistic code, source time, observation time, retrieval time, approval status, aggregation unit, method metadata, units, datum, rating-curve vintage/reference, endpoint used, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, series counts, site counts, or endpoint metadata where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, gauge-observation truth, regulatory truth, forecast truth, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| USGS Water Data/source-family doctrine | `docs/sources/catalog/usgs/` or `docs/domains/hydrology/` |
| Connector code or connector decisions | `connectors/usgs/` or `connectors/usgs/water_data/` if present |
| Pipeline code or pipeline decisions | `pipelines/domains/hydrology/` |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, sensitivity, provisional-vs-approved, freshness, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/hydrology/` |
| Normalized working material | `data/work/hydrology/` |
| Validated Hydrology objects | `data/processed/hydrology/` |
| Catalog, triplets, graph truth, STAC/DCAT/PROV closure, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| NHDPlus network identity, modeled mean annual reach flow, NFHL regulatory truth, operational flood forecast, dam-operation authority, water-rights enforcement, public artifact authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hydrology/usgs_water_data/
├── README.md
├── sites/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── site_metadata_ref.json
│       ├── endpoint_ref.json
│       ├── checksums.sha256
│       └── README.md
├── instantaneous-values/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── iv_series_ref.json
│       ├── approval_status_ref.json
│       ├── parameter_code_ref.json
│       ├── checksums.sha256
│       └── README.md
├── daily-values/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── dv_series_ref.json
│       ├── aggregation_ref.json
│       ├── checksums.sha256
│       └── README.md
├── peaks/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── peak_flow_ref.json
│       ├── rating_curve_ref.json
│       ├── checksums.sha256
│       └── README.md
├── water-quality/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── water_quality_ref.json
│       ├── method_metadata_ref.json
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
| Quarantine | Source role, rights, endpoint identity, site ID, parameter code, approval status, aggregation unit, method metadata, datum, citation, schema, freshness, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, source-family identity, citation, hash, endpoint identity, site identity, parameter metadata, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence, approval-status handling, freshness handling, correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/raw/hydrology/usgs_water_data/
→ data/processed/hydrology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hydrology lane and the USGS Water Data source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, sub-product identity, rights, cadence, citation, endpoint identity, site identity, parameter code, approval status, freshness posture, and hash posture.
- [ ] Confirm site metadata, IV readings, peak flows, daily values, annual statistics, water-quality records, and rating curves are not collapsed into one source role.
- [ ] Confirm provisional readings are not cited as approved values.
- [ ] Confirm daily values and annual statistics are not treated as instantaneous observations.
- [ ] Confirm rating-curve metadata is not treated as a direct observation.
- [ ] Confirm USGS Water Data is not framed as NHDPlus network identity, FEMA NFHL regulatory truth, operational forecast, dam-operation authority, or water-rights enforcement.
- [ ] Confirm endpoint-used and migration/parity metadata are preserved where applicable.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/hydrology/usgs_water_data/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/hydrology/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Hydrology source-registry doctrine lists USGS Water Data / NWIS as observed for continuous and daily hydrologic time series plus monitoring-location metadata, not regulatory flood zones or emergency alerts. | **CONFIRMED by GitHub contents API during this edit** |
| USGS Water Data catalog doctrine separates site metadata, instantaneous values, peak flows, daily values, annual statistics, water-quality records, and rating curves by source role and lifecycle state. | **CONFIRMED by GitHub contents API during this edit** |
| USGS Water Data catalog doctrine says provisional readings are not approved values, daily values and annual statistics are aggregates, and endpoint migration/parity must be preserved. | **CONFIRMED by GitHub contents API during this edit** |
| Actual USGS Water Data RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, regulatory truth, forecast truth, operational authority, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/sources/catalog/usgs/nwis-water.md`](../../../../docs/sources/catalog/usgs/nwis-water.md)
- [`../../../../docs/sources/catalog/usgs/nhdplus-hr.md`](../../../../docs/sources/catalog/usgs/nhdplus-hr.md)
- [`../../../../docs/sources/catalog/usgs/README.md`](../../../../docs/sources/catalog/usgs/README.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hydrology USGS Water Data RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, NHDPlus network truth, NFHL regulatory truth, operational forecast authority, water-rights authority, dam-operation authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
