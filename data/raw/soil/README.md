<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/soil/readme
name: Soil Raw README
path: data/raw/soil/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <soil-domain-steward>
  - <soil-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: soil
artifact_family: immutable-soil-source-capture-index
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; support-type-separation-required; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../quarantine/soil/README.md
  - ../../processed/soil/README.md
  - ../../catalog/domain/soil/README.md
  - ../../published/layers/soil/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../docs/sources/catalog/nrcs/gssurgo.md
  - ../../../docs/sources/catalog/nrcs.md
  - ../../../docs/architecture/source-roles.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - soil
  - ssurgo
  - gssurgo
  - gnatsgo
  - soil-data-access
  - mesonet
  - scan
  - uscrn
  - smap
  - soilgrids
  - mukey
  - cokey
  - chkey
  - horizon
  - source-capture
  - source-role
  - support-type
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/soil/README.md`."
  - "The Soil canonical paths document lists `data/raw/soil/` as the RAW lifecycle phase for the soil domain."
  - "No child RAW README lanes under `data/raw/soil/` were confirmed during this edit."
  - "README presence confirms documentation only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil RAW

Parent RAW lifecycle index for immutable Soil source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: soil" src="https://img.shields.io/badge/domain-soil-8B4513">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Source-family posture](#source-family-posture) · [Support-type boundaries](#support-type-boundaries) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/soil/` is a no-public-path RAW lifecycle lane. It is not processed Soil truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, support-type fusion authority, suitability authority, or generated-answer authority.

---

## Scope

This directory indexes immutable RAW source captures and RAW-local sidecars for the Soil domain.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what source role it carried, and which identifiers, versions, vintages, source times, retrieval times, rights notes, citations, geometry/support metadata, source-head metadata, hashes, support-type notes, review notes, and caveats must travel downstream.

RAW does not decide whether a soil map unit, component, horizon, property, hydrologic soil group, soil-moisture reading, pedon/profile view, erosion-risk surface, suitability rating, component-horizon join, map layer, public claim, or generated answer is true or release-ready.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/soil/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `soil` |
| Artifact role | Parent RAW domain index for source captures and RAW-local sidecars |
| Confirmed child README lanes | None confirmed during this edit |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Explicitly admitted connector/source-admission output only |
| Downstream | `data/work/soil/` or `data/quarantine/soil/` after governed triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, source family, product vintage, support type, resolution, station/depth/unit/QC metadata, citation, validation, correction, rollback, or release support is insufficient |

---

## Source-family posture

The Soil canonical-path docs identify source families that may feed the lane after governed admission. This README does not prove that any payloads or child source-family folders exist.

| Source family | Typical RAW posture | Boundary |
|---|---|---|
| NRCS SSURGO | Static survey source capture for map units, components, horizons, and tabular attributes. | Static survey material is not a gridded derivative, station reading, satellite grid, or suitability claim by itself. |
| USDA NRCS Soil Data Access | Query/API capture over soil survey source surfaces. | Query hash, query text, retrieval time, and reproducibility metadata must travel downstream. |
| NRCS gSSURGO | Gridded derivative source capture. | Must carry derivative lineage, support-type label, source vintage, resolution, and resampling notes. |
| NRCS gNATSGO | CONUS gridded derivative source capture. | Must not silently merge with SSURGO, SoilGrids, station readings, or SMAP. |
| Kansas Mesonet soil moisture | Station observation capture with depth, unit, timestamp, and QC. | Station readings are not static survey truth or gridded surface truth. |
| NRCS SCAN | Station observation capture. | Depth/unit/QC and station identity must be preserved. |
| NOAA USCRN | Station observation capture. | Depth/unit/QC and station identity must be preserved. |
| NASA SMAP | Satellite grid source capture. | Satellite-grid values require granule lineage, retrieval algorithm, footprint, and support-type label. |
| ISRIC SoilGrids | Global gridded derivative source capture. | Attribution, source resolution, resampling, and derivative lineage must be preserved. |

---

## Support-type boundaries

| Support type | RAW handling | Must not become |
|---|---|---|
| Static survey | Capture source vintage, MUKEY/COKEY/CHKEY lineage, citation, and table/geometry support. | Live station reading, satellite grid, or suitability rating by itself. |
| Gridded derivative | Capture source resolution, resampling method, source vintage, and derivation lineage. | Unlabeled authoritative static survey. |
| Station reading | Capture station identity, observation time, depth, unit, and QC flags. | Countywide or mapunit-wide truth without aggregation/proof. |
| Satellite grid | Capture granule, algorithm, footprint, retrieval time, and resolution. | Station observation or static survey truth. |
| Pedon evidence | Capture sampling date, sample identity, lab/source lineage, and citation. | Generalized mapunit truth without scope and evidence. |
| Interpretation / suitability | Capture derivation rule, evidence basis, scope of validity, and caveats. | Source observation or determination unless independently supported. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Support type is preserved | Static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation must not be silently fused. |
| Resolution stays visible | Source resolution, resampling method, and derivation lineage must travel with gridded or composite outputs. |
| Soil identity keys stay visible | MUKEY, COKEY, CHKEY, horizon depth, and component-horizon lineage must be preserved where applicable. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW lane directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source identity, source family, source role, source time, retrieval time, product vintage, query hash, source resolution, resampling note, station/depth/unit/QC metadata, granule lineage, MUKEY/COKEY/CHKEY references, horizon-depth references, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, feature counts, raster metadata, station counts, horizon counts, or package metadata where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, support-type fusion authority, suitability authority, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Soil domain doctrine | `docs/domains/soil/` |
| Source-family doctrine | `docs/sources/catalog/` or `docs/domains/soil/` |
| Connector code or connector decisions | `connectors/` by source organization, not `data/raw/soil/` |
| Pipeline code or pipeline decisions | `pipelines/domains/soil/` and `pipeline_specs/soil/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, review, support-type, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/soil/` |
| Normalized working material | `data/work/soil/` |
| Validated Soil objects | `data/processed/soil/` only after gates close |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, graph edges, vector indexes, or generated answers | `data/published/` only after release gates close |
| Crop/yield truth, streamflow truth, groundwater truth, flood truth, lithology truth, suitability authority, public artifact authority, or generated-answer authority | Owning governed downstream/proof/policy/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/soil/
├── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

Potential future source-family folders must be created only after admission/path review. Examples may include `ssurgo/`, `sda/`, `gssurgo/`, `gnatsgo/`, `kansas-mesonet/`, `nrcs-scan/`, `noaa-uscrn/`, `nasa-smap/`, and `isric-soilgrids/`, but none are confirmed by this README.

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, source family, product/vintage identity, query hash, support type, resolution, unit/depth/QC metadata, citation, schema, or activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, source-head metadata, support-type metadata, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, support-type/resolution labels, review/policy state, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/soil/
→ data/processed/soil/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Soil lane and a documented source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, rights, citation, product/vintage identity, retrieval time, support type, and hash posture.
- [ ] Confirm static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation are not silently fused.
- [ ] Confirm source resolution, resampling method, and derivation lineage are present for gridded or composite surfaces.
- [ ] Confirm station observations preserve station identity, observation time, depth, unit, and QC flags.
- [ ] Confirm MUKEY/COKEY/CHKEY lineage, horizon depth, and component-horizon joins are preserved where applicable.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW Soil material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/soil/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `data/raw/soil/` is the documented RAW phase path for the Soil domain. | **CONFIRMED by GitHub contents API during this edit** |
| Child RAW README lanes under `data/raw/soil/` were confirmed during this edit. | **UNKNOWN / not confirmed** |
| README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, receipts, review controls, or release readiness. | **DENY** |
| Soil source-family doctrine lists NRCS SSURGO, SDA, gSSURGO, gNATSGO, Kansas Mesonet, NRCS SCAN, NOAA USCRN, NASA SMAP, and ISRIC SoilGrids. | **CONFIRMED by GitHub contents API during this edit** |
| Soil doctrine requires support-type separation and blocks unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state from public promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Soil RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, support-type fusion authority, suitability authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/soil/README.md`](../../quarantine/soil/README.md)
- [`../../processed/soil/README.md`](../../processed/soil/README.md)
- [`../../catalog/domain/soil/README.md`](../../catalog/domain/soil/README.md)
- [`../../published/layers/soil/README.md`](../../published/layers/soil/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/soil/CANONICAL_PATHS.md`](../../../docs/domains/soil/CANONICAL_PATHS.md)
- [`../../../docs/domains/soil/DATA_LIFECYCLE.md`](../../../docs/domains/soil/DATA_LIFECYCLE.md)
- [`../../../docs/sources/catalog/nrcs/ssurgo.md`](../../../docs/sources/catalog/nrcs/ssurgo.md)
- [`../../../docs/sources/catalog/nrcs/gssurgo.md`](../../../docs/sources/catalog/nrcs/gssurgo.md)
- [`../../../docs/sources/catalog/nrcs.md`](../../../docs/sources/catalog/nrcs.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Soil RAW domain index for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, support-type fusion authority, suitability authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
