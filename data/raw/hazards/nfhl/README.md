<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hazards/nfhl/readme
title: Hazards NFHL Raw README
path: data/raw/hazards/nfhl/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
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
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Hazards NFHL RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: hazards
adjacent_domain: hydrology
source_family: nfhl
source_role: regulatory
artifact_family: hazards-nfhl-raw-compatibility-reference
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
  - ../fema/README.md
  - ../../hydrology/fema_nfhl/README.md
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
  - compatibility-reference
  - source-first
notes:
  - "This README replaces placeholder content at `data/raw/hazards/nfhl/README.md`."
  - "Parent `data/raw/hazards/README.md` was a greenfield stub when this README was first authored on 2026-06-27; it is now a tracked compatibility/reference index."
  - "NFHL material is regulatory flood-hazard context. It is not observed inundation, not a predictive model, and not public-release authority by itself."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards NFHL RAW Lane

Compatibility/reference documentation for Hazards-facing NFHL RAW topology; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-c62828">
  <img alt="Source family: NFHL" src="https://img.shields.io/badge/source-NFHL-1f6feb">
  <img alt="Role: regulatory" src="https://img.shields.io/badge/role-regulatory-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/hazards/nfhl/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named subtree is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, observed inundation truth, model output, or generated-answer authority.

---

## Scope

This directory documents Hazards-facing FEMA NFHL source handling and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

KFM treats NFHL as regulatory flood-hazard context. NFHL can support downstream flood-context and exposure analysis after governed normalization, but RAW capture is not observed inundation, not a predictive flood model, not a live condition statement, and not a public artifact by itself.

A governed source-first capture records what was captured, where it came from, what source role it carried, and which identifiers, times, rights notes, citations, service/version metadata, effective-date fields, regulatory attributes, geometry/support metadata, checksums, and caveats must travel downstream.

The same FEMA NFHL source is also documented by the Hydrology-facing lane [`../../hydrology/fema_nfhl/`](../../hydrology/fema_nfhl/README.md) and referenced by [`../fema/`](../fema/README.md). These lanes must reference the same single source-first NFHL capture, never two copies.

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
| Artifact role | Compatibility/reference documentation for Hazards-facing NFHL source handling and unresolved legacy RAW topology |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | Governed Hazards WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when role, rights, source surface, version/effective-date metadata, citation, datum/units, validation, or release support is insufficient |

---

## NFHL source posture

| NFHL source condition | RAW handling | Boundary |
|---|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; references may support Hazards without duplicating RAW bytes. | A hazards-scoped copy is not a second capture identity. |
| Physical placement is held | Do not infer `data/raw/hazards/nfhl/` or any subfolder as the capture home. Use only an accepted writer/path contract; none is established by this README. | This lane may retain governed references only. |
| ArcGIS REST / FeatureServer vector surface | Capture as regulatory source material when admitted. | REST/vector is the analytics path; RAW capture is still not release state. |
| WMS / WMTS visualization surface | Record only as visualization context if admitted. | WMS pixels are not valid analytical evidence for zone, BFE, or in/out tests. |
| Regulatory attributes | Preserve `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, zone, BFE/datum fields where present, study references, and lineage references. | Do not drop or recode regulatory fields before catalog/proof closure. |
| MSC companion evidence | Preserve NFHL/MSC separation. | NFHL and MSC are companion descriptors, not duplicate or interchangeable sources. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, review, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads.

The governed source-first capture or reference that supports Hazards NFHL use must carry, where applicable:

- source-reference manifests;
- NFHL REST/service references, feature-class references, version/effective-date references, WMS visualization references, or raw payload references;
- `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, flood-zone fields, BFE/datum fields where present, study/FIS references, LOMR/LOMA lineage references where present, service URI, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums.

None of these, and no local README or index, becomes proof, catalog, registry, policy, release, public artifact, observed-event truth, model truth, or answer authority.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Hazards. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source-run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Earlier drafts sketched surface-specific run groupings: `rest-featureserver/` runs carrying `source_reference.json`, `service_ref.json`, `feature_class_ref.json`, `version_ref.json`, `checksums.sha256`, and a run README; and `visualization/` runs carrying `source_reference.json`, `wms_ref.json`, `visualization_only_ref.json`, `checksums.sha256`, and a run README, plus an optional RAW-local index. That layout is a proposed shape for a future accepted source-first home, not this subtree.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was captured, but no downstream decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, rights, source surface, version/effective-date metadata, regulatory fields, citation, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Hazards WORK only when SourceDescriptor, rights posture, source role, source-family identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/hazards/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Hazards-scoped copy.
- [ ] Treat this source-named README as compatibility/reference documentation only; do not create a child directory as a payload destination.
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
| Parent `data/raw/hazards/README.md` was a greenfield stub when this README was first authored (2026-06-27). | **CONFIRMED historically; superseded — the parent is now a tracked compatibility/reference index reconciled on 2026-10-11** |
| NFHL source catalog doctrine identifies NFHL as regulatory flood-hazard context, not observed inundation, and not a predictive flood model. | **CONFIRMED by GitHub contents API during this edit** |
| NFHL source catalog doctrine says REST/vector and WMS/visualization surfaces have different trust postures. | **CONFIRMED by GitHub contents API during this edit** |
| NFHL and MSC are companion descriptors, not duplicates. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual NFHL RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
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
- [`../fema/README.md`](../fema/README.md)
- [`../../hydrology/fema_nfhl/README.md`](../../hydrology/fema_nfhl/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hazards-facing NFHL compatibility/reference lane. One governed source-first capture may support Hazards without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, observed-inundation truth, model truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
