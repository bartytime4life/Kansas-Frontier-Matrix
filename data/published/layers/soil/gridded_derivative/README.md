<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/soil/gridded-derivative/readme
name: Soil Gridded Derivative Published Layer README
path: data/published/layers/soil/gridded_derivative/README.md
type: data-lane-readme
version: v0.1.0
status: draft
owners:
  - <soil-domain-steward>
  - <release-steward>
  - <map-layer-steward>
created: 2026-06-26
updated: 2026-06-26
policy_label: public-with-review
truth_posture: cite-or-abstain
lifecycle_phase: published
responsibility_root: data/
domain: soil
sublane: gridded_derivative
artifact_family: released-public-safe-soil-gridded-derivative-layer
support_type: gridded_derivative_soil
sensitivity_posture: public-safe-at-appropriate-scale; support-type-separation-required; farm-owner-operational-detail-review-required; release-required
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../docs/domains/soil/API_CONTRACTS.md
  - ../../../../docs/doctrine/derived-stays-derived.md
  - ../../../proofs/soil/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - published
  - layers
  - soil
  - gridded-derivative
  - gssurgo
  - gnatsgo
  - soilgrids
  - support-type
  - release
  - evidence-first
notes:
  - "This README documents the released public-safe gridded derivative layer lane for the Soil domain."
  - "Gridded derivatives are derived/support-type-specific artifacts; they do not replace static soil survey truth or EvidenceBundle authority."
  - "Every published artifact here must preserve support_type, source role, time caveat, release state, field allowlist, digest, and rollback path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil — Gridded Derivative Published Layers

Released public-safe gridded derivative soil layer artifacts for map and API delivery.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: published" src="https://img.shields.io/badge/lifecycle-published-success">
  <img alt="Domain: soil" src="https://img.shields.io/badge/domain-soil-795548">
  <img alt="Support type: gridded derivative soil" src="https://img.shields.io/badge/support-gridded__derivative__soil-6e40c9">
  <img alt="Policy: public with review" src="https://img.shields.io/badge/policy-public%20with%20review-blue">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Publication boundary](#publication-boundary) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!IMPORTANT]
> A gridded derivative soil layer is a **support-type-specific derived artifact**. It may carry gSSURGO, gNATSGO, SoilGrids, or similar gridded products to the public map, but it must not masquerade as static survey truth, station soil moisture, satellite soil moisture, pedon evidence, or an interpretation layer without an explicit reviewed derivation step.

---

## Scope

This directory may hold released public-safe gridded derivative soil artifacts. These layers may support map display, API delivery, Evidence Drawer lookups, suitability context, hydrologic group context, or other public-safe soil derivative views after the normal KFM release gates have passed.

A gridded derivative layer here is a downstream delivery artifact. It is not the source record, canonical soil truth, static survey authority, catalog truth, proof bundle, release decision, registry authority, or AI interpretation.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/published/layers/soil/gridded_derivative/` |
| Responsibility root | `data/` |
| Lifecycle phase | `published/` |
| Domain lane | `soil` |
| Parent published layer lane | `data/published/layers/soil/` |
| Support type | `gridded_derivative_soil` |
| Artifact role | Released public-safe gridded derivative layer bytes and sidecars |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/soil/` and `data/receipts/`, not this directory |
| Default failure posture | `DENY`, `HOLD`, `RESTRICT`, or `ABSTAIN` when evidence, source role, support type, rights, time caveat, sensitivity, release, or rollback support is insufficient |

---

## Inputs

Accepted content is limited to release-approved, public-safe derivatives such as:

- gSSURGO, gNATSGO, SoilGrids, or similar gridded derivative artifacts after source-role, rights, support-type, and release review;
- PMTiles, Cloud Optimized GeoTIFF, GeoParquet, GeoJSON, vector-tile, or raster-tile artifacts;
- public-safe derived property grids, hydrologic soil group grids, suitability context grids, or caveated interpretation grids;
- layer manifests, tile metadata, and support-type/time-caveat summaries;
- field allowlists, digests, and generated release pointers;
- release-local notes that explain artifact contents without replacing proof or release authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| RAW source captures or source mirrors | `data/raw/soil/` or source-specific intake |
| WORK files, candidates, unresolved joins, or review drafts | `data/work/soil/` |
| Quarantined or unclear material | `data/quarantine/soil/` |
| Canonical processed soil objects | `data/processed/soil/` |
| Catalog records, triplets, or graph truth | `data/catalog/` and triplet/projection lanes |
| EvidenceBundle / ProofPack | `data/proofs/soil/` |
| Validation, transform, redaction, grid-build, or release receipts | `data/receipts/` |
| Release manifests or promotion decisions | `release/` |
| Static survey truth labeled as gridded derivative | Correct support-specific soil lane, not this sublane |
| Station, satellite, pedon, or interpretation payloads without reviewed derivation | Correct support-specific soil lane or quarantine |
| Farm-specific, owner-specific, proprietary, or operational sensor detail | Restricted governed lanes only; not public published layers |
| Direct model-generated claims | Governed answer/provenance paths only |

---

## Directory map

```text
data/published/layers/soil/gridded_derivative/
├── README.md
├── <release_id>/
│   ├── soil_gridded_derivative.pmtiles
│   ├── soil_gridded_derivative.cog.tif
│   ├── soil_gridded_derivative.geoparquet
│   ├── soil_gridded_derivative.sha256
│   ├── layer.manifest.json
│   ├── fields.allowlist.json
│   ├── support_type.summary.json
│   ├── time_caveat.summary.json
│   ├── review.summary.json
│   └── README.md
└── latest.json
```

`latest.json` must be generated from release state. Remove or withhold it when release, review, digest, registry, correction, support-type, or rollback support is incomplete.

---

## Publication boundary

```mermaid
flowchart LR
    RAW["RAW<br/>soil source capture"] --> WORK["WORK<br/>normalize + derive grid candidate"]
    WORK --> GATE{Evidence + support type + rights + policy gate}
    GATE -->|fail / unclear| QUAR["QUARANTINE<br/>hold or deny"]
    GATE -->|pass| PROC["PROCESSED<br/>validated soil objects / grid candidates"]
    PROC --> CAT["CATALOG / TRIPLET<br/>EvidenceBundle refs + caveats"]
    CAT --> REL["RELEASE<br/>manifest + rollback"]
    REL --> PUB["PUBLISHED<br/>gridded derivative layer artifacts"]
    PUB --> API["governed API / layer resolver"]
    API --> UI["MapLibre + Evidence Drawer"]
```

The forbidden shortcut is:

```text
RAW / WORK / QUARANTINE / processed candidate / direct source record / direct model output / unlabeled support type
→ direct public gridded derivative soil layer
```

---

## Required checks before use

- [ ] Confirm the release manifest and promotion decision.
- [ ] Confirm proof and receipt closure.
- [ ] Confirm source descriptors, source roles, rights posture, and current terms.
- [ ] Confirm `support_type = gridded_derivative_soil` is present and preserved.
- [ ] Confirm support-type separation from static survey, station, satellite, pedon, and interpretation surfaces.
- [ ] Confirm time caveat, source vintage, retrieval time, release time, and correction time where material.
- [ ] Confirm field allowlist and released-byte digest.
- [ ] Confirm layer registry entry.
- [ ] Confirm rollback target and correction path.
- [ ] Confirm public clients consume this layer through governed APIs or release-resolved artifacts.
- [ ] Confirm no farm-specific, owner-specific, proprietary, operational sensor, or restricted detail is present in released bytes.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested path boundary. | **CONFIRMED authored** |
| The target path exists in the live repository. | **CONFIRMED by GitHub contents API during this edit** |
| Soil doctrine includes gridded derivative soil as a support type. | **CONFIRMED by GitHub contents API during this edit** |
| Actual released artifacts exist in this subtree. | **UNKNOWN** |
| Validators for this exact layer are implemented and wired in CI. | **NEEDS VERIFICATION** |
| A release manifest currently approves a gridded derivative soil layer. | **UNKNOWN** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../../docs/domains/soil/ARCHITECTURE.md`](../../../../docs/domains/soil/ARCHITECTURE.md)
- [`../../../../docs/domains/soil/DATA_LIFECYCLE.md`](../../../../docs/domains/soil/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/soil/CANONICAL_PATHS.md`](../../../../docs/domains/soil/CANONICAL_PATHS.md)
- [`../../../../docs/domains/soil/API_CONTRACTS.md`](../../../../docs/domains/soil/API_CONTRACTS.md)
- [`../../../../docs/doctrine/derived-stays-derived.md`](../../../../docs/doctrine/derived-stays-derived.md)
- [`../../../proofs/soil/README.md`](../../../proofs/soil/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a released gridded-derivative soil layer lane only. It is not source authority, proof authority, release authority, catalog authority, static survey truth, station observation truth, interpretation truth, registry authority, or AI truth.

[Back to top](#top)
