<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hydrology/usgs-wbd/readme
title: Hydrology USGS WBD Raw README
path: data/raw/hydrology/usgs_wbd/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <hydrology-domain-steward>
  - <hydrology-source-steward>
  - <usgs-wbd-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Hydrology USGS WBD RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: hydrology
adjacent_domain: spatial-foundation
source_family: usgs_wbd
source_role: authority-context
artifact_family: hydrology-usgs-wbd-raw-compatibility-reference
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
  - ../../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md
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
  - compatibility-reference
  - source-first
notes:
  - "This README replaces placeholder content at `data/raw/hydrology/usgs_wbd/README.md`."
  - "Parent `data/raw/hydrology/README.md` was a greenfield stub when this README was first authored on 2026-06-27; it is now a tracked compatibility/reference index."
  - "USGS WBD/HUC material is authority/context source capture for HUC geometry and nested hydrologic units."
  - "WBD/HUC material is not observed flow, gauge truth, current flood extent, floodplain regulation, emergency alert, parcel/title authority, or generated-answer authority."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology USGS WBD RAW Lane

Compatibility/reference documentation for Hydrology-facing USGS WBD RAW topology; not a physical source-capture home.

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
> `data/raw/hydrology/usgs_wbd/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named subtree is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed Hydrology truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, observed-flow truth, current-flood-extent truth, floodplain-regulation authority, parcel/title authority, or generated-answer authority.

---

## Scope

This directory documents Hydrology-facing USGS WBD / HUC source handling and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

KFM treats USGS WBD as authority/context source material for HUC geometry, nested hydrologic units, watershed accounting, aggregation scopes, map filtering, and cross-domain joins. It may support downstream `HUCUnit`, `Watershed`, rollups, drought links, water-use links, irrigation links, and public-safe contextual layers after governed normalization, but RAW capture is not observed flow, floodplain regulation, parcel/title truth, or public release state by itself.

A governed source-first capture records what was captured, where it came from, what source role it carried, and which HUC codes, HUC levels, names, parent/child hierarchy, WBD snapshot/vintage, geometry support metadata, area fields, rights notes, citations, retrieval times, checksums, and caveats must travel downstream.

[ADR-0026](../../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md) (effective status `proposed`, source status `draft`) proposes that WBD HUC12 lead the Hydrology source spine. Even if accepted, it requires a separate governed source-admission decision, which it describes as routing a validated candidate to `data/raw/hydrology/wbd_huc12/` or `data/quarantine/hydrology/wbd_huc12/`. It does not name this `usgs_wbd/` subtree as a capture home and does not decide physical RAW placement.

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
| Artifact role | Compatibility/reference documentation for Hydrology-facing USGS WBD source handling and unresolved legacy RAW topology |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | Governed Hydrology WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
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
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; references may support Hydrology without duplicating RAW bytes. | A hydrology-scoped copy is not a second capture identity. |
| Physical placement is held | Do not infer `data/raw/hydrology/usgs_wbd/` or any subfolder as the capture home. Use only an accepted writer/path contract; none is established by this README. | This lane may retain governed references only. |
| HUC geometry | Capture as authority/context accounting geometry when admitted. | HUC geometry is not observed flow, flood extent, parcel/title truth, or regulation by itself. |
| HUC code and level | Preserve HUC2, HUC4, HUC6, HUC8, HUC10, HUC12 code/level identity where present. | HUC identity must not be reused without WBD snapshot/vintage context. |
| Parent/child hierarchy | Preserve nesting and lineage where present. | Hierarchy supports accounting; it does not create per-place truth. |
| WBD snapshot/vintage | Preserve source snapshot, vintage, retrieval time, and digest. | New snapshots must not overwrite prior captures in place. |
| HUC rollup input | Preserve aggregation scope and source lineage. | HUC rollups are aggregates, not per-record or per-place observations. |
| Cross-domain join context | Hold for governed review before downstream public use. | Join context does not promote RAW WBD into public artifact authority. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, review, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads.

The governed source-first capture or reference that supports Hydrology USGS WBD use must carry, where applicable:

- source-reference manifests;
- USGS WBD/HUC download references, service references, HUC boundary references, snapshot/vintage references, hierarchy references, or raw payload references;
- HUC code, HUC level, HUC name, parent HUC, child HUC references, WBD snapshot/vintage, geometry support metadata, area fields, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, geometry counts, hierarchy counts, or package metadata where applicable, and checksums.

None of these, and no local README or index, becomes proof, catalog, registry, policy, release, public artifact, observed-flow truth, regulatory truth, parcel/title truth, or answer authority.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Hydrology. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source-run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Earlier drafts sketched groupings keyed by snapshot or run: `boundaries/` carrying `source_reference.json`, `huc_boundary_ref.json`, `wbd_snapshot_ref.json`, `checksums.sha256`, and a run README; `hierarchy/` carrying `source_reference.json`, `huc_hierarchy_ref.json`, `parent_child_ref.json`, `checksums.sha256`, and a run README; and `rollup-context/` carrying `source_reference.json`, `aggregation_scope_ref.json`, `source_lineage_ref.json`, `checksums.sha256`, and a run README, plus an optional RAW-local index. That layout is a proposed shape for a future accepted source-first home, not this subtree.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was captured, but no downstream decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, rights, WBD snapshot, HUC code, HUC level, hierarchy, geometry, citation, schema, aggregation scope, source activation, or physical placement is unresolved. |
| Return / reject | Admission or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Hydrology WORK only when SourceDescriptor, rights posture, source role, source-family identity, citation, hash, WBD snapshot metadata, HUC identity support, hierarchy support, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence, aggregation-scope support, correction path, and rollback target. |

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
| Parent `data/raw/hydrology/README.md` was a greenfield stub when this README was first authored (2026-06-27). | **CONFIRMED historically; superseded — the parent is now a tracked compatibility/reference index reconciled on 2026-10-11** |
| Hydrology source-registry doctrine lists USGS WBD/HUC as authority/context for HUC geometry and nested hydrologic units, not observed flow or floodplain regulation. | **CONFIRMED by GitHub contents API during this edit** |
| HUCUnit contract doctrine defines HUCUnit as WBD hydrologic accounting/context geometry with HUC code, level, hierarchy, source vintage, evidence support, release state, correction lineage, and rollback target. | **CONFIRMED by GitHub contents API during this edit** |
| HUCUnit contract doctrine says HUCUnit is not observed readings, regulatory flood-zone determination, observed inundation, modeled hydrograph, parcel/title authority, or life-safety guidance. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| ADR-0026 decides physical RAW placement for WBD captures or names this subtree as the WBD capture home. | **DENY — ADR-0026 is `proposed`; it names `data/raw/hydrology/wbd_huc12/` only as a possible future admission route, not an accepted placement** |
| Actual USGS WBD RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
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
- [`../../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md`](../../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hydrology-facing USGS WBD compatibility/reference lane. One governed source-first capture may support Hydrology without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, observed-flow truth, current-flood-extent truth, NFHL regulatory truth, legal jurisdiction, parcel/title authority, per-place aggregate truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
