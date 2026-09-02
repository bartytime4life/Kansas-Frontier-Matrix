<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hydrology/fema-nfhl/readme
name: Hydrology FEMA NFHL Raw README
path: data/raw/hydrology/fema_nfhl/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <hydrology-domain-steward>
  - <hydrology-source-steward>
  - <fema-nfhl-source-steward>
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
source_family: fema_nfhl
source_role: regulatory
artifact_family: immutable-hydrology-fema-nfhl-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; regulatory-not-observed-inundation; not-forecast; not-life-safety; rights-needs-verification; release-blocked
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
  - ../../../../docs/sources/catalog/fema/nfhl-flood-hazard.md
  - ../../../../docs/sources/catalog/fema/map-service-center.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hydrology
  - hazards
  - fema
  - nfhl
  - fema-nfhl
  - flood-context
  - nfhl-zone
  - regulatory
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/hydrology/fema_nfhl/README.md`."
  - "Parent `data/raw/hydrology/README.md` is currently a greenfield stub."
  - "FEMA NFHL material is regulatory flood-zone / flood-context source capture for Hydrology. It is not observed inundation, not forecast, not modeled flood output, and not life-safety guidance."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology FEMA NFHL RAW Lane

RAW source-family lane for immutable FEMA National Flood Hazard Layer source captures and source-admission sidecars in the Hydrology domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Source family: FEMA NFHL" src="https://img.shields.io/badge/source-FEMA%20NFHL-1f6feb">
  <img alt="Role: regulatory" src="https://img.shields.io/badge/role-regulatory-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [FEMA NFHL source posture](#fema-nfhl-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/hydrology/fema_nfhl/` is a RAW source-capture lane. It is not processed Hydrology truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, observed inundation truth, forecast truth, model output, life-safety guidance, or generated-answer authority.

---

## Scope

This directory is for immutable FEMA NFHL source captures and RAW-local sidecars in the Hydrology domain.

KFM treats FEMA NFHL as regulatory flood-zone and flood-context source material for `NFHLZone / FloodContext`. It may support downstream exposure, context, and regulatory-citation work after governed normalization, but RAW capture is not observed flood evidence, not a predictive flood model, not a forecast, not a live condition statement, and not public release state by itself.

RAW records what was captured, where it came from, what source role it carried, and which identifiers, times, rights notes, citations, service/version metadata, effective-date fields, regulatory attributes, geometry/support metadata, checksums, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hydrology/fema_nfhl/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hydrology` |
| Adjacent lane | `hazards` for flood-hazard context and exposure joins |
| Source family | `fema_nfhl` |
| Source role | `regulatory`; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/hydrology/` or `data/quarantine/hydrology/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when role, rights, source surface, version/effective-date metadata, citation, datum/units, validation, or release support is insufficient |

---

## FEMA NFHL source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| NFHL regulatory flood-zone material | Capture as regulatory source material when admitted. | Regulatory zone context is not observed inundation, forecast, or model output. |
| `NFHLZone / FloodContext` input | Preserve panel/version/effective-date identity and source-role metadata. | Hydrology flood context remains distinct from `ObservedFloodEvent` and `Hydrograph`. |
| REST / vector surface | Preserve service URI, source time, retrieval time, version metadata, and digest. | Vector material is analytical input only after governed normalization and evidence closure. |
| WMS / visualization surface | Record only as visualization context if admitted. | WMS pixels are not valid analytical evidence for zone, BFE, or in/out claims. |
| MSC companion evidence | Preserve NFHL/MSC separation. | NFHL and MSC are companion descriptors, not duplicate or interchangeable sources. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- FEMA NFHL REST/service references, feature-class references, version/effective-date references, WMS visualization references, MSC cross-reference sidecars, or raw payload references;
- `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, flood-zone fields, BFE/datum fields where present, study/FIS references, LOMR/LOMA lineage references where present, service URI, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, observed-event truth, model truth, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| FEMA NFHL/source-family doctrine | `docs/sources/catalog/fema/` or `docs/domains/hydrology/` |
| Connector code or connector decisions | `connectors/fema/` or `connectors/fema/nfhl/` if present |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, sensitivity, freshness, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/hydrology/` |
| Normalized working material | `data/work/hydrology/` |
| Validated Hydrology objects | `data/processed/hydrology/` |
| Catalog, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Observed flood evidence, forecast truth, model truth, life-safety guidance, public artifact authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hydrology/fema_nfhl/
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
data/raw/hydrology/fema_nfhl/
→ data/processed/hydrology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hydrology lane and the FEMA NFHL source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, source surface, rights, cadence, citation, version/effective-date metadata, and hash posture.
- [ ] Confirm FEMA NFHL material is not treated as observed inundation, modeled inundation, forecast, live condition truth, or life-safety guidance.
- [ ] Confirm REST/vector and WMS/visualization surfaces are not collapsed.
- [ ] Confirm `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, flood-zone fields, BFE/datum fields where present, and study/lineage references are preserved where present.
- [ ] Confirm NFHL and MSC remain separate but cross-citable descriptors where needed.
- [ ] Confirm `NFHLZone / FloodContext`, `ObservedFloodEvent`, `Hydrograph`, and emergency-warning context remain distinct truth classes.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/hydrology/fema_nfhl/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/hydrology/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Hydrology source-registry doctrine lists FEMA NFHL / MSC as regulatory context and says regulatory flood layers are not observed flooding. | **CONFIRMED by GitHub contents API during this edit** |
| Hydrology object-family doctrine says `NFHLZone / FloodContext`, `ObservedFloodEvent`, `Hydrograph`, and emergency warnings are distinct truth classes. | **CONFIRMED by GitHub contents API during this edit** |
| NFHL source catalog doctrine identifies NFHL as regulatory flood-hazard context, not observed inundation, and not a predictive flood model. | **CONFIRMED by GitHub contents API during this edit** |
| Actual FEMA NFHL RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, observed-inundation truth, model truth, life-safety guidance, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/sources/catalog/fema/nfhl-flood-hazard.md`](../../../../docs/sources/catalog/fema/nfhl-flood-hazard.md)
- [`../../../../docs/sources/catalog/fema/map-service-center.md`](../../../../docs/sources/catalog/fema/map-service-center.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hydrology FEMA NFHL RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, observed-inundation truth, forecast truth, model truth, life-safety guidance, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
