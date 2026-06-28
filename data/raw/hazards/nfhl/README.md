<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hazards/nfhl/readme
name: Hazards NFHL Raw README
path: data/raw/hazards/nfhl/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <hazards-domain-steward>
  - <hydrology-domain-steward>
  - <hazards-source-steward>
  - <nfhl-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: hazards
adjacent_domain: hydrology
source_family: nfhl
source_role: regulatory
artifact_family: immutable-hazards-nfhl-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; regulatory-not-observed-inundation; vector-rest-for-analytics; wms-visualization-only; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../quarantine/hazards/README.md
  - ../../../processed/hazards/README.md
  - ../../../catalog/domain/hazards/README.md
  - ../../../published/layers/hazards/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hazards/SOURCES.md
  - ../../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../../docs/sources/catalog/fema/nfhl-flood-hazard.md
  - ../../../../docs/sources/catalog/fema/map-service-center.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hazards
  - hydrology
  - fema
  - nfhl
  - flood-context
  - regulatory
  - vector-rest
  - wms-visualization-only
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/hazards/nfhl/README.md`."
  - "Parent `data/raw/hazards/README.md` is currently a greenfield stub."
  - "NFHL material is regulatory flood-hazard context. It is not observed inundation, not a predictive model, and not public-release authority by itself."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards NFHL RAW Lane

RAW source-family lane for immutable FEMA National Flood Hazard Layer source captures and source-admission sidecars in the Hazards domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-c62828">
  <img alt="Source family: NFHL" src="https://img.shields.io/badge/source-NFHL-1f6feb">
  <img alt="Role: regulatory" src="https://img.shields.io/badge/role-regulatory-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/hazards/nfhl/` is a RAW source-capture lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, observed inundation truth, model output, or generated-answer authority.

---

## Scope

This directory is for immutable FEMA NFHL source captures and RAW-local sidecars in the Hazards domain.

KFM treats NFHL as regulatory flood-hazard context. NFHL can support downstream flood-context and exposure analysis after governed normalization, but RAW capture is not observed inundation, not a predictive flood model, not a live condition statement, and not a public artifact by itself.

RAW records what was captured, where it came from, what source role it carried, and which identifiers, times, rights notes, citations, service/version metadata, effective-date fields, regulatory attributes, geometry/support metadata, checksums, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hazards/nfhl/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hazards` |
| Adjacent lane | `hydrology` for `NFHLZone` / flood-context use |
| Source family | `nfhl` |
| Source role | `regulatory`; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/hazards/` or `data/quarantine/hazards/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when role, rights, source surface, version/effective-date metadata, citation, datum/units, validation, or release support is insufficient |

---

## NFHL source posture

| NFHL source condition | RAW handling | Boundary |
|---|---|---|
| ArcGIS REST / FeatureServer vector surface | Capture as regulatory source material when admitted. | REST/vector is the analytics path; RAW capture is still not release state. |
| WMS / WMTS visualization surface | Record only as visualization context if admitted. | WMS pixels are not valid analytical evidence for zone, BFE, or in/out tests. |
| Regulatory attributes | Preserve `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, zone, BFE/datum fields where present, study references, and lineage references. | Do not drop or recode regulatory fields before catalog/proof closure. |
| MSC companion evidence | Preserve NFHL/MSC separation. | NFHL and MSC are companion descriptors, not duplicate or interchangeable sources. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

- source-reference manifests;
- NFHL REST/service references, feature-class references, version/effective-date references, WMS visualization references, or raw payload references;
- `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, flood-zone fields, BFE/datum fields where present, study/FIS references, LOMR/LOMA lineage references where present, service URI, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, observed-event truth, model truth, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| NFHL/source-family doctrine | `docs/sources/catalog/fema/` or `docs/domains/hazards/` |
| Connector code or connector decisions | `connectors/fema/` or `connectors/fema/nfhl/` if present |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, sensitivity, freshness, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/hazards/` |
| Normalized working material | `data/work/hazards/` |
| Validated Hazards objects | `data/processed/hazards/` |
| Catalog, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hazards/nfhl/
├── README.md
├── rest-featureserver/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── service_ref.json
│       ├── feature_class_ref.json
│       ├── version_ref.json
│       ├── checksums.sha256
│       └── README.md
├── visualization/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── wms_ref.json
│       ├── visualization_only_ref.json
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
| Quarantine | Source role, rights, source surface, version/effective-date metadata, regulatory fields, citation, schema, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, source-family identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/hazards/nfhl/
→ data/processed/hazards/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hazards lane and the NFHL source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, source surface, rights, cadence, citation, version/effective-date metadata, and hash posture.
- [ ] Confirm NFHL material is not treated as observed inundation, modeled inundation, forecast, or live condition truth.
- [ ] Confirm REST/vector and WMS/visualization surfaces are not collapsed.
- [ ] Confirm `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, flood-zone fields, BFE/datum fields where present, and study/lineage references are preserved where present.
- [ ] Confirm NFHL and MSC remain separate but cross-citable descriptors where needed.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/hazards/nfhl/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/hazards/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| NFHL source catalog doctrine identifies NFHL as regulatory flood-hazard context, not observed inundation, and not a predictive flood model. | **CONFIRMED by GitHub contents API during this edit** |
| NFHL source catalog doctrine says REST/vector and WMS/visualization surfaces have different trust postures. | **CONFIRMED by GitHub contents API during this edit** |
| NFHL and MSC are companion descriptors, not duplicates. | **CONFIRMED by GitHub contents API during this edit** |
| Actual NFHL RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, observed-inundation truth, model truth, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../quarantine/hazards/README.md`](../../../quarantine/hazards/README.md)
- [`../../../processed/hazards/README.md`](../../../processed/hazards/README.md)
- [`../../../catalog/domain/hazards/README.md`](../../../catalog/domain/hazards/README.md)
- [`../../../published/layers/hazards/README.md`](../../../published/layers/hazards/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/hazards/SOURCE_REGISTRY.md`](../../../../docs/domains/hazards/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`](../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md)
- [`../../../../docs/domains/hazards/SOURCES.md`](../../../../docs/domains/hazards/SOURCES.md)
- [`../../../../docs/domains/hazards/DATA_LIFECYCLE.md`](../../../../docs/domains/hazards/DATA_LIFECYCLE.md)
- [`../../../../docs/sources/catalog/fema/nfhl-flood-hazard.md`](../../../../docs/sources/catalog/fema/nfhl-flood-hazard.md)
- [`../../../../docs/sources/catalog/fema/map-service-center.md`](../../../../docs/sources/catalog/fema/map-service-center.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hazards NFHL RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, observed-inundation truth, model truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
