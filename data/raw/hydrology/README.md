<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hydrology/readme
title: Hydrology Raw README
path: data/raw/hydrology/README.md
type: data-raw-domain-index-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <hydrology-domain-steward>
  - <hydrology-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Hydrology RAW compatibility and reference documentation without treating this subtree or its source-named children as a physical source-first capture home or duplicating RAW bytes.
domain: hydrology
artifact_family: hydrology-raw-compatibility-reference-index
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; freshness-bound; rights-needs-verification; release-blocked
related:
  - fema_nfhl/README.md
  - usgs_3dep/README.md
  - usgs_nhdplus_hr/README.md
  - usgs_water_data/README.md
  - usgs_wbd/README.md
  - ../README.md
  - ../../README.md
  - ../../quarantine/hydrology/README.md
  - ../../processed/hydrology/README.md
  - ../../catalog/domain/hydrology/README.md
  - ../../published/layers/hydrology/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../docs/domains/hydrology/SOURCE_FAMILIES.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../docs/architecture/source-roles.md
  - ../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hydrology
  - source-capture
  - source-role
  - source-family-index
  - water-data
  - nfhl
  - wbd
  - nhdplus-hr
  - usgs-3dep
  - no-public-path
  - evidence-first
  - compatibility-reference
  - source-first
notes:
  - "This README replaces the greenfield stub at `data/raw/hydrology/README.md`."
  - "Confirmed child README lanes during this edit: `fema_nfhl/`, `usgs_3dep/`, `usgs_nhdplus_hr/`, `usgs_water_data/`, and `usgs_wbd/`."
  - "README presence confirms documentation lanes only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, review controls, or release readiness."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology RAW

Compatibility and reference index for legacy Hydrology-scoped RAW documentation; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source-family lanes](#confirmed-source-family-lanes) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/hydrology/` is a no-public-path compatibility/reference index inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this domain subtree and its source-named children are not default physical capture homes and must not receive duplicate RAW payloads. It is not processed Hydrology truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, or generated-answer authority.

---

## Scope

This directory indexes tracked Hydrology-facing source documentation and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture records what was admitted, where it came from, what source role it carried, and which identifiers, versions, vintages, times, rights notes, citations, source-head metadata, geometry/support metadata, datum/unit metadata, freshness posture, hashes, review notes, and caveats must travel downstream.

RAW does not decide what a hydrologic fact means, whether a provisional value is approved, whether an aggregate can support a per-place claim, whether a regulatory layer describes observed conditions, whether a modeled output can be used as observation, whether rights permit reuse, or whether a downstream claim can publish.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hydrology/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hydrology` |
| Artifact role | Compatibility/reference index for Hydrology-facing source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Hydrology WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, source family, endpoint, citation, geometry/support, datum/units, freshness, classification, review state, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source-family lanes

The child lanes below are confirmed README paths. Treat them as compatibility/reference documentation or unresolved legacy topology, not source-first capture homes. Their presence does **not** prove or authorize payloads, SourceDescriptors, connectors, validators, fixtures, receipts, CI checks, review controls, migration, or release readiness.

| Source-family lane | Status | Parent boundary |
|---|---|---|
| [`fema_nfhl/`](fema_nfhl/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Regulatory flood-zone / flood-context source documentation; not observed inundation, forecast, model output, or a capture home. |
| [`usgs_3dep/`](usgs_3dep/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Terrain/elevation source documentation; not observed water-level truth or a capture home. |
| [`usgs_nhdplus_hr/`](usgs_nhdplus_hr/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Stream/reach network identity and catchment context; geometry, VAAs, topology, and packaging retain separate roles; not a capture home. |
| [`usgs_water_data/`](usgs_water_data/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Gauge/site/time-series source documentation; approval status and aggregation scope must travel; not a capture home. |
| [`usgs_wbd/`](usgs_wbd/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | HUC geometry and nested hydrologic-unit context; not observed flow, floodplain regulation, or a capture home. |

FEMA NFHL is also documented by the Hazards-facing lane [`../hazards/nfhl/`](../hazards/nfhl/README.md), and 3DEP terrain is also cited by [`../geology/README.md`](../geology/README.md). Each source must be referenced through one single source-first capture, never duplicated domain copies.

---

## RAW source posture

| Rule | Handling |
|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; domain references may support Hydrology without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/hydrology/` or a child directory as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| RAW is immutable source capture | Payloads or payload references at the accepted source-first home must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Time kinds stay distinct | Source time, observed time, valid/effective time, retrieval time, release time, and correction time remain separate where material. |
| Provisional is not approved | Provisional USGS Water Data readings require explicit lifecycle state before downstream claims. |
| Aggregate is not per-instant truth | Daily values, annual statistics, HUC rollups, drought links, and other rollups must carry aggregation scope. |
| Regulatory is not observed | FEMA NFHL / MSC flood context must not be reframed as observed inundation, forecast, or model output. |
| Modeled is not observed | VAAs, rating curves, terrain-derived catchments, DEM derivatives, hydrographs, and reconstructed traces require model/lineage support before claim use. |
| Authority/context is not release | WBD/HUC and NHDPlus context can support joins and maps only after downstream proof/release gates. |
| Watchers do not publish | Watchers may emit intake candidates; they do not admit, promote, publish, or answer public claims. |
| Public use requires governed release | Public layers, PMTiles, reports, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- the tracked README files listed below;
- links to canonical SourceDescriptor, source-admission, rights, freshness, review, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; it would not be a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

The governed source-first capture or reference that supports Hydrology must carry: source-reference manifests; raw payloads or raw payload references; SourceDescriptor or admission-ticket references; source identity, source family, source role, source time, observed time, retrieval time, valid/effective time where applicable, product version/vintage, endpoint identity, geometry/support metadata, datum/unit metadata, citation, attribution, rights posture, freshness posture, review notes, and digests; and source-head records, retrieval metadata, status metadata, row counts, feature counts, series counts, site counts, raster metadata, topology counts, or package metadata where applicable, and checksums. None of these becomes proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Hydrology. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
| Hydrology domain doctrine | `docs/domains/hydrology/` |
| Source-family doctrine | `docs/sources/catalog/` or `docs/domains/hydrology/` |
| Connector code or connector decisions | `connectors/` |
| Pipeline code or pipeline decisions | `pipelines/domains/hydrology/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, review, sensitivity, freshness, provisional-vs-approved, datum/unit, aggregation, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/hydrology/` |
| Normalized working material | `data/work/hydrology/` |
| Validated Hydrology objects | `data/processed/hydrology/` |
| Catalog records, triplets, graph truth, STAC/DCAT/PROV closure, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Observed-water truth, gauge truth, regulatory truth, model truth, engineering-grade claims, public artifact authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hydrology/
├── README.md
├── fema_nfhl/README.md
├── usgs_3dep/README.md
├── usgs_nhdplus_hr/README.md
├── usgs_water_data/README.md
└── usgs_wbd/README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a future source directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This index may retain a governed reference only. |
| Quarantine | Source role, rights, source family, endpoint, product/version identity, citation, geometry/support, datum/units, schema, freshness, source activation, source-role split, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Hydrology WORK only when SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, source-head metadata, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/model/freshness receipts where required, correction path, rollback target, and release manifest where applicable. |

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
- [ ] Treat this README and any source-named child README as compatibility/reference documentation only; do not create a child directory as a payload destination.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, product identity, rights, cadence, citation, endpoint identity, freshness posture, and hash posture.
- [ ] Confirm source roles are not collapsed across observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic products.
- [ ] Confirm observed readings preserve site identity, parameter code, observation time, approval status, unit, datum, method metadata, and retrieval time where applicable.
- [ ] Confirm daily values, annual statistics, HUC rollups, drought links, and other rollups preserve aggregation scope and are not cited as per-instant truth.
- [ ] Confirm regulatory context is not treated as observed or modeled condition truth.
- [ ] Confirm modeled surfaces, rating curves, VAAs, topology, DEM derivatives, and reconstructed hydrographs preserve model/run/lineage support where applicable.
- [ ] Confirm WBD/HUC and NHDPlus network context are not treated as gauge observations, current flood extent, or legal/regulatory determinations by themselves.
- [ ] Confirm rights, current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior captures in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/hydrology/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Child README lanes confirmed during this edit: `fema_nfhl`, `usgs_3dep`, `usgs_nhdplus_hr`, `usgs_water_data`, and `usgs_wbd`. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, receipts, review controls, or release readiness. | **DENY** |
| Hydrology source-registry doctrine lists WBD/HUC, NHDPlus HR/3DHP, USGS Water Data/NWIS, FEMA NFHL/MSC, and USGS 3DEP with distinct source-role boundaries. | **CONFIRMED by GitHub contents API during this edit** |
| Hydrology source-role doctrine says role is assigned at admission and role/claim mismatch is a DENY condition. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| ADR-0026 (`proposed`, source status `draft`) names `data/raw/hydrology/wbd_huc12/` only as a possible route for a future governed source-admission decision if the ADR is accepted. | **CONFIRMED; it does not accept physical placement for this subtree or any child** |
| Actual Hydrology RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| Child READMEs `fema_nfhl/`, `usgs_3dep/`, `usgs_nhdplus_hr/`, `usgs_water_data/`, and `usgs_wbd/` are reconciled to the source-first parent contract as compatibility/reference documentation. | **CONFIRMED authored 2026-10-11 (documentation only)** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`fema_nfhl/README.md`](fema_nfhl/README.md)
- [`usgs_3dep/README.md`](usgs_3dep/README.md)
- [`usgs_nhdplus_hr/README.md`](usgs_nhdplus_hr/README.md)
- [`usgs_water_data/README.md`](usgs_water_data/README.md)
- [`usgs_wbd/README.md`](usgs_wbd/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/hydrology/README.md`](../../quarantine/hydrology/README.md)
- [`../../processed/hydrology/README.md`](../../processed/hydrology/README.md)
- [`../../catalog/domain/hydrology/README.md`](../../catalog/domain/hydrology/README.md)
- [`../../published/layers/hydrology/README.md`](../../published/layers/hydrology/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/hydrology/SOURCE_REGISTRY.md`](../../../docs/domains/hydrology/SOURCE_REGISTRY.md)
- [`../../../docs/domains/hydrology/OBJECT_FAMILIES.md`](../../../docs/domains/hydrology/OBJECT_FAMILIES.md)
- [`../../../docs/domains/hydrology/SOURCE_FAMILIES.md`](../../../docs/domains/hydrology/SOURCE_FAMILIES.md)
- [`../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md)
- [`../../../docs/domains/hydrology/DATA_LIFECYCLE.md`](../../../docs/domains/hydrology/DATA_LIFECYCLE.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md`](../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Hydrology-facing compatibility/reference index. One governed source-first capture may support Hydrology without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, observed-water truth, gauge truth, regulatory truth, model truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
