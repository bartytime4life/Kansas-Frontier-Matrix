<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hydrology/usgs-nhdplus-hr/readme
name: Hydrology USGS NHDPlus HR Raw README
path: data/raw/hydrology/usgs_nhdplus_hr/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <hydrology-domain-steward>
  - <hydrology-source-steward>
  - <usgs-nhdplus-hr-source-steward>
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
source_family: usgs_nhdplus_hr
source_role: observed-geometry-modeled-vaa-per-subproduct
artifact_family: immutable-hydrology-usgs-nhdplus-hr-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; comid-network-aware; vaa-modeled-not-gauged; not-regulatory; not-current-flood-extent; rights-needs-verification; release-blocked
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
  - ../../../../docs/sources/catalog/usgs/nhdplus-hr.md
  - ../../../../docs/sources/catalog/usgs/3dep-elevation.md
  - ../../../../docs/sources/catalog/usgs/README.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hydrology
  - spatial-foundation
  - usgs
  - nhdplus-hr
  - nhd
  - 3dhp
  - hydrography
  - comid
  - reach-identity
  - network-topology
  - vaa
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/hydrology/usgs_nhdplus_hr/README.md`."
  - "Parent `data/raw/hydrology/README.md` is currently a greenfield stub."
  - "USGS NHDPlus HR / 3DHP material is authority/context/model-input source capture for stream/reach network identity, flow direction, and catchment derivation."
  - "NHDPlus HR sub-products require role separation: digitized hydrography geometry is observed; VAAs and network topology are modeled; WBD packaging context is administrative."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology USGS NHDPlus HR RAW Lane

RAW source-family lane for immutable USGS NHDPlus High Resolution source captures and source-admission sidecars in the Hydrology domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Source family: NHDPlus HR" src="https://img.shields.io/badge/source-NHDPlus%20HR-1f6feb">
  <img alt="Identity: COMID" src="https://img.shields.io/badge/identity-COMID-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [USGS NHDPlus HR source posture](#usgs-nhdplus-hr-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/hydrology/usgs_nhdplus_hr/` is a RAW source-capture lane. It is not processed Hydrology truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, gauge-observation truth, current-flood-extent truth, regulatory flood-zone truth, engineering hydraulic-model authority, or generated-answer authority.

---

## Scope

This directory is for immutable USGS NHDPlus HR source captures and RAW-local sidecars in the Hydrology domain.

KFM treats USGS NHDPlus HR / 3DHP as authority/context/model-input source material for stream and reach network identity, flow direction, catchment derivation, and COMID-keyed hydrography. It may support downstream `ReachIdentity`, `HydroFeature`, `UpstreamTrace`, catchment, irrigation-link, and habitat-geometry work after governed normalization, but RAW capture is not gauge observation truth, current flood extent, regulatory flood-zone truth, or public release state by itself.

RAW records what was captured, where it came from, what source role each sub-product carried, and which identifiers, release vintages, COMIDs, WBD packaging units, feature types, VAA fields, topology fields, rights notes, citations, timestamps, checksums, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hydrology/usgs_nhdplus_hr/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hydrology` |
| Adjacent lane | `spatial-foundation` for network geometry and topology cataloging |
| Source family | `usgs_nhdplus_hr` |
| Source role | Heterogeneous by sub-product: observed geometry, modeled VAA/network topology, administrative packaging; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/hydrology/` or `data/quarantine/hydrology/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when sub-product role, rights, release vintage, COMID identity, WBD packaging scope, VAA lineage, topology lineage, citation, validation, or release support is insufficient |

---

## USGS NHDPlus HR source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| NHDFlowline geometry | Capture as observed digitized hydrography geometry when admitted. | Geometry is not gauged flow, regulatory status, or current flood extent. |
| NHDArea / NHDWaterbody geometry | Capture as observed digitized area/waterbody geometry when admitted. | Mapped waterbody geometry is not a live water-level or flood observation. |
| COMID identity | Preserve COMID, release vintage, feature type, WBD package context, and source identifiers. | COMID identity must not be reused without release/vintage context. |
| Value-Added Attributes | Capture as modeled per-COMID attributes when admitted. | VAAs such as drainage area, mean annual flow, velocity, and stream order are not measured values at a gauge. |
| Network topology | Capture as modeled graph/topology material when admitted. | Upstream/downstream position is a model of network behavior, not first-hand observation. |
| WBD HU-4 packaging context | Preserve as administrative packaging context. | Packaging scope is not regulatory jurisdiction by itself. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- TNM/download references, NHDPlus HR geodatabase references, feature-class references, VAA table references, network-topology references, WBD package references, Science Data Catalog crosswalk references, or raw payload references;
- COMID, release vintage, WBD HU-4 package, feature type, `ftype` / `fcode` where present, reachcode where present, geometry support metadata, VAA field references, topology references, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, feature counts, topology counts, or package metadata where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, gauge-observation truth, regulatory truth, model truth, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| USGS NHDPlus HR/source-family doctrine | `docs/sources/catalog/usgs/` or `docs/domains/hydrology/` |
| Connector code or connector decisions | `connectors/usgs/` or `connectors/usgs/nhdplus_hr/` if present |
| Pipeline code or pipeline decisions | `pipelines/domains/hydrology/` |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, sensitivity, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/hydrology/` |
| Normalized working material | `data/work/hydrology/` |
| Validated Hydrology objects | `data/processed/hydrology/` |
| Catalog, triplets, graph truth, STAC/DCAT/PROV closure, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Gauge observations, current flood extent, NFHL regulatory truth, legal waterway jurisdiction, engineering hydraulic-model output, public artifact authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hydrology/usgs_nhdplus_hr/
├── README.md
├── geometry/
│   └── <release_or_run_id>/
│       ├── source_reference.json
│       ├── feature_class_ref.json
│       ├── comid_identity_ref.json
│       ├── release_vintage_ref.json
│       ├── checksums.sha256
│       └── README.md
├── vaa/
│   └── <release_or_run_id>/
│       ├── source_reference.json
│       ├── vaa_table_ref.json
│       ├── vaa_model_lineage_ref.json
│       ├── comid_identity_ref.json
│       ├── checksums.sha256
│       └── README.md
├── network-topology/
│   └── <release_or_run_id>/
│       ├── source_reference.json
│       ├── topology_ref.json
│       ├── upstream_downstream_ref.json
│       ├── derivation_ref.json
│       ├── checksums.sha256
│       └── README.md
├── packaging/
│   └── <release_or_run_id>/
│       ├── source_reference.json
│       ├── wbd_package_ref.json
│       ├── sdc_crosswalk_ref.json
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
| Quarantine | Source role, rights, release vintage, COMID identity, WBD package, VAA lineage, topology lineage, citation, schema, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, source-family identity, citation, hash, release-vintage metadata, COMID support, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence, VAA/model lineage closure, topology validation, correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/raw/hydrology/usgs_nhdplus_hr/
→ data/processed/hydrology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hydrology lane and the USGS NHDPlus HR source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, sub-product identity, rights, cadence, citation, release vintage, COMID identity posture, and hash posture.
- [ ] Confirm NHDFlowline, NHDArea, NHDWaterbody geometry, VAAs, topology, and packaging context are not collapsed into one source role.
- [ ] Confirm VAAs are not treated as gauge observations or measured values at the reach.
- [ ] Confirm network topology is not treated as first-hand observation or engineering hydraulic-model output.
- [ ] Confirm NHDPlus HR is not framed as regulatory flood-zone truth or legal waterway jurisdiction.
- [ ] Confirm COMID, release vintage, WBD package context, feature type, VAA lineage, topology lineage, and crosswalk basis are preserved where present.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/hydrology/usgs_nhdplus_hr/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/hydrology/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Hydrology source-registry doctrine lists USGS NHDPlus HR / 3DHP as authority/context/model for stream/reach network identity, flow direction, and catchment derivation, not gauge observations or current flood extent. | **CONFIRMED by GitHub contents API during this edit** |
| NHDPlus HR catalog doctrine separates observed hydrography geometry, modeled VAAs, modeled network topology, and administrative WBD packaging context. | **CONFIRMED by GitHub contents API during this edit** |
| NHDPlus HR catalog doctrine says COMID identity, release vintage, WBD package, feature type, VAA/model lineage, and network topology are material source-capture fields. | **CONFIRMED by GitHub contents API during this edit** |
| Actual USGS NHDPlus HR RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, gauge-observation truth, regulatory truth, model truth, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/sources/catalog/usgs/nhdplus-hr.md`](../../../../docs/sources/catalog/usgs/nhdplus-hr.md)
- [`../../../../docs/sources/catalog/usgs/3dep-elevation.md`](../../../../docs/sources/catalog/usgs/3dep-elevation.md)
- [`../../../../docs/sources/catalog/usgs/README.md`](../../../../docs/sources/catalog/usgs/README.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hydrology USGS NHDPlus HR RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, gauge-observation truth, current-flood-extent truth, NFHL regulatory truth, legal waterway jurisdiction, engineering hydraulic-model authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
