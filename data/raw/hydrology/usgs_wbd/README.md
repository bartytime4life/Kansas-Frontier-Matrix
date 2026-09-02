<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hydrology/usgs-wbd/readme
name: Hydrology USGS WBD Raw README
path: data/raw/hydrology/usgs_wbd/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <hydrology-domain-steward>
  - <hydrology-source-steward>
  - <usgs-wbd-source-steward>
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
source_family: usgs_wbd
source_role: authority-context
artifact_family: immutable-hydrology-usgs-wbd-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; huc-accounting-geometry; aggregate-safe-not-per-place-truth; not-observed-flow; not-floodplain-regulation; rights-needs-verification; release-blocked
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
  - ../../../../contracts/domains/hydrology/huc_unit.md
  - ../../../../contracts/domains/hydrology/watershed.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hydrology
  - spatial-foundation
  - usgs
  - wbd
  - huc
  - huc-unit
  - watershed-boundary-dataset
  - watershed
  - accounting-geometry
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/hydrology/usgs_wbd/README.md`."
  - "Parent `data/raw/hydrology/README.md` is currently a greenfield stub."
  - "USGS WBD/HUC material is authority/context source capture for HUC geometry and nested hydrologic units."
  - "WBD/HUC material is not observed flow, gauge truth, current flood extent, floodplain regulation, emergency alert, parcel/title authority, or generated-answer authority."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology USGS WBD RAW Lane

RAW source-family lane for immutable USGS Watershed Boundary Dataset source captures and source-admission sidecars in the Hydrology domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Source family: USGS WBD" src="https://img.shields.io/badge/source-USGS%20WBD-1f6feb">
  <img alt="Role: authority / context" src="https://img.shields.io/badge/role-authority%20%2F%20context-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [USGS WBD source posture](#usgs-wbd-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/hydrology/usgs_wbd/` is a RAW source-capture lane. It is not processed Hydrology truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, observed-flow truth, current-flood-extent truth, floodplain-regulation authority, parcel/title authority, or generated-answer authority.

---

## Scope

This directory is for immutable USGS WBD / HUC source captures and RAW-local sidecars in the Hydrology domain.

KFM treats USGS WBD as authority/context source material for HUC geometry, nested hydrologic units, watershed accounting, aggregation scopes, map filtering, and cross-domain joins. It may support downstream `HUCUnit`, `Watershed`, rollups, drought links, water-use links, irrigation links, and public-safe contextual layers after governed normalization, but RAW capture is not observed flow, floodplain regulation, parcel/title truth, or public release state by itself.

RAW records what was captured, where it came from, what source role it carried, and which HUC codes, HUC levels, names, parent/child hierarchy, WBD snapshot/vintage, geometry support metadata, area fields, rights notes, citations, retrieval times, checksums, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hydrology/usgs_wbd/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hydrology` |
| Adjacent lane | `spatial-foundation` for boundary geometry and map-context cataloging |
| Source family | `usgs_wbd` |
| Source role | `authority` / `context`; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/hydrology/` or `data/quarantine/hydrology/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, WBD snapshot, HUC code, HUC level, hierarchy, geometry, citation, validation, aggregation scope, correction, rollback, or release support is insufficient |

---

## USGS WBD source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| HUC geometry | Capture as authority/context accounting geometry when admitted. | HUC geometry is not observed flow, flood extent, parcel/title truth, or regulation by itself. |
| HUC code and level | Preserve HUC2, HUC4, HUC6, HUC8, HUC10, HUC12 code/level identity where present. | HUC identity must not be reused without WBD snapshot/vintage context. |
| Parent/child hierarchy | Preserve nesting and lineage where present. | Hierarchy supports accounting; it does not create per-place truth. |
| WBD snapshot/vintage | Preserve source snapshot, vintage, retrieval time, and digest. | New snapshots must not overwrite prior captures in place. |
| HUC rollup input | Preserve aggregation scope and source lineage. | HUC rollups are aggregates, not per-record or per-place observations. |
| Cross-domain join context | Hold for governed review before downstream public use. | Join context does not promote RAW WBD into public artifact authority. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- USGS WBD/HUC download references, service references, HUC boundary references, snapshot/vintage references, hierarchy references, or raw payload references;
- HUC code, HUC level, HUC name, parent HUC, child HUC references, WBD snapshot/vintage, geometry support metadata, area fields, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, geometry counts, hierarchy counts, or package metadata where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, observed-flow truth, regulatory truth, parcel/title truth, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| USGS WBD/source-family doctrine | `docs/sources/catalog/usgs/` or `docs/domains/hydrology/` |
| Connector code or connector decisions | `connectors/usgs/` or `connectors/usgs/wbd/` if present |
| Pipeline code or pipeline decisions | `pipelines/domains/hydrology/` |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, sensitivity, aggregation, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/hydrology/` |
| Normalized working material | `data/work/hydrology/` |
| Validated Hydrology objects | `data/processed/hydrology/` |
| Catalog, triplets, graph truth, STAC/DCAT/PROV closure, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Gauge observations, flow observations, current flood extent, NFHL regulatory truth, legal jurisdiction, parcel/title claim, per-place aggregate truth, public artifact authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hydrology/usgs_wbd/
├── README.md
├── boundaries/
│   └── <snapshot_or_run_id>/
│       ├── source_reference.json
│       ├── huc_boundary_ref.json
│       ├── wbd_snapshot_ref.json
│       ├── checksums.sha256
│       └── README.md
├── hierarchy/
│   └── <snapshot_or_run_id>/
│       ├── source_reference.json
│       ├── huc_hierarchy_ref.json
│       ├── parent_child_ref.json
│       ├── checksums.sha256
│       └── README.md
├── rollup-context/
│   └── <snapshot_or_run_id>/
│       ├── source_reference.json
│       ├── aggregation_scope_ref.json
│       ├── source_lineage_ref.json
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
| Quarantine | Source role, rights, WBD snapshot, HUC code, HUC level, hierarchy, geometry, citation, schema, aggregation scope, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, source-family identity, citation, hash, WBD snapshot metadata, HUC identity support, hierarchy support, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence, aggregation-scope support, correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/raw/hydrology/usgs_wbd/
→ data/processed/hydrology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hydrology lane and the USGS WBD source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, rights, cadence, citation, WBD snapshot/vintage, HUC identity posture, and hash posture.
- [ ] Confirm HUC code, HUC level, name, parent/child hierarchy, geometry, area, and WBD snapshot/vintage are preserved where present.
- [ ] Confirm WBD/HUC material is not treated as observed flow, current flood extent, NFHL regulatory truth, legal jurisdiction, or parcel/title authority.
- [ ] Confirm HUC rollups are treated as aggregates with an explicit scope, not per-place truth.
- [ ] Confirm cross-domain joins preserve WBD as accounting/context geometry and do not promote RAW material directly.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and new snapshots do not overwrite prior captures in place.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/hydrology/usgs_wbd/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/hydrology/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Hydrology source-registry doctrine lists USGS WBD/HUC as authority/context for HUC geometry and nested hydrologic units, not observed flow or floodplain regulation. | **CONFIRMED by GitHub contents API during this edit** |
| HUCUnit contract doctrine defines HUCUnit as WBD hydrologic accounting/context geometry with HUC code, level, hierarchy, source vintage, evidence support, release state, correction lineage, and rollback target. | **CONFIRMED by GitHub contents API during this edit** |
| HUCUnit contract doctrine says HUCUnit is not observed readings, regulatory flood-zone determination, observed inundation, modeled hydrograph, parcel/title authority, or life-safety guidance. | **CONFIRMED by GitHub contents API during this edit** |
| Actual USGS WBD RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, observed-flow truth, regulatory truth, parcel/title truth, or generated-answer authority. | **DENY** |

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
- [`../../../../contracts/domains/hydrology/huc_unit.md`](../../../../contracts/domains/hydrology/huc_unit.md)
- [`../../../../contracts/domains/hydrology/watershed.md`](../../../../contracts/domains/hydrology/watershed.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hydrology USGS WBD RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, observed-flow truth, current-flood-extent truth, NFHL regulatory truth, legal jurisdiction, parcel/title authority, per-place aggregate truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
