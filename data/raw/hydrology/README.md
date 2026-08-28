<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hydrology/readme
name: Hydrology Raw README
path: data/raw/hydrology/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <hydrology-domain-steward>
  - <hydrology-source-steward>
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
artifact_family: immutable-hydrology-source-capture
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
notes:
  - "This README replaces the greenfield stub at `data/raw/hydrology/README.md`."
  - "Confirmed child README lanes during this edit: `fema_nfhl/`, `usgs_3dep/`, `usgs_nhdplus_hr/`, `usgs_water_data/`, and `usgs_wbd/`."
  - "README presence confirms documentation lanes only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, review controls, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology RAW

Parent RAW lifecycle index for immutable Hydrology source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source-family lanes](#confirmed-source-family-lanes) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/hydrology/` is a no-public-path RAW lifecycle lane. It is not processed Hydrology truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, or generated-answer authority.

---

## Scope

This directory indexes immutable RAW source captures and source-admission sidecars for the Hydrology domain.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what source role it carried, and which identifiers, versions, vintages, times, rights notes, citations, source-head metadata, geometry/support metadata, datum/unit metadata, freshness posture, hashes, review notes, and caveats must travel downstream.

RAW does not decide what a hydrologic fact means, whether a provisional value is approved, whether an aggregate can support a per-place claim, whether a regulatory layer describes observed conditions, whether a modeled output can be used as observation, whether rights permit reuse, or whether a downstream claim can publish.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hydrology/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hydrology` |
| Artifact role | Parent RAW domain index for Hydrology source captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/hydrology/` or `data/quarantine/hydrology/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, source family, endpoint, citation, geometry/support, datum/units, freshness, classification, review state, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source-family lanes

The child lanes below are README paths confirmed by current-session GitHub fetches. This table confirms README presence only; it does **not** prove payloads, SourceDescriptors, connectors, validators, fixtures, receipts, CI checks, review controls, or release readiness.

| Source-family lane | Status | Parent boundary |
|---|---|---|
| [`fema_nfhl/`](fema_nfhl/README.md) | **CONFIRMED README** | Regulatory flood-zone / flood-context source capture; not observed inundation, forecast, or model output. |
| [`usgs_3dep/`](usgs_3dep/README.md) | **CONFIRMED README** | Terrain/elevation source capture; not observed water-level truth. |
| [`usgs_nhdplus_hr/`](usgs_nhdplus_hr/README.md) | **CONFIRMED README** | Stream/reach network identity and catchment context; geometry, VAAs, topology, and packaging retain separate roles. |
| [`usgs_water_data/`](usgs_water_data/README.md) | **CONFIRMED README** | Gauge/site/time-series source capture; approval status and aggregation scope must travel. |
| [`usgs_wbd/`](usgs_wbd/README.md) | **CONFIRMED README** | HUC geometry and nested hydrologic-unit context; not observed flow or floodplain regulation. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
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

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source identity, source family, source role, source time, observed time, retrieval time, valid/effective time where applicable, product version/vintage, endpoint identity, geometry/support metadata, datum/unit metadata, citation, attribution, rights posture, freshness posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, feature counts, series counts, site counts, raster metadata, topology counts, or package metadata where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
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
├── fema_nfhl/
│   └── README.md
├── usgs_3dep/
│   └── README.md
├── usgs_nhdplus_hr/
│   └── README.md
├── usgs_water_data/
│   └── README.md
├── usgs_wbd/
│   └── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, source family, endpoint, product/version identity, citation, geometry/support, datum/units, schema, freshness, source activation, or source-role split is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, source-head metadata, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/model/freshness receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/hydrology/
→ data/processed/hydrology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hydrology lane and a documented source-family subfolder.
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
| Actual Hydrology RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
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
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Hydrology RAW domain index for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, observed-water truth, gauge truth, regulatory truth, model truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
