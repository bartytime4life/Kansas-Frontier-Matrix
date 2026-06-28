<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/agriculture/usda-nass/readme
name: USDA NASS Raw Agriculture README
path: data/raw/agriculture/usda-nass/README.md
type: data-raw-source-lane-readme
version: v0.1.0
status: draft
owners:
  - <agriculture-domain-steward>
  - <source-steward>
  - <usda-nass-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: agriculture
source_family: usda-nass
artifact_family: immutable-source-capture
sensitivity_posture: raw-internal; source-role-preserving; rights-needs-verification; aggregate-only-guard-required; field-level-claims-deny; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/agriculture/README.md
  - ../../../processed/agriculture/README.md
  - ../../../catalog/domain/agriculture/README.md
  - ../../../published/layers/agriculture/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../../docs/domains/agriculture/SOURCES.md
  - ../../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../../docs/sources/catalog/usda/usda-nass-quickstats.md
  - ../../../../docs/sources/catalog/usda/usda-nass-cdl.md
  - ../../../../connectors/usda-nass/README.md
  - ../../../../connectors/nass/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - agriculture
  - usda
  - usda-nass
  - nass
  - quickstats
  - crop-progress
  - cdl
  - aggregate
  - source-role
  - rights-review
  - evidence-first
notes:
  - "This README documents the requested RAW source lane for Agriculture USDA NASS material."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/` and `data/raw/agriculture/` READMEs are currently greenfield stubs, so this file stays source-lane bounded."
  - "USDA NASS QuickStats / Crop Progress is aggregate in KFM source-role posture; field-level NASS claims deny."
  - "USDA NASS CDL and QuickStats are separate product surfaces and must not collapse into one source role, cadence, geometry, or receipt path."
  - "Rights, endpoints, current terms, source descriptors, connector activation, payload presence, validator wiring, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USDA NASS RAW Agriculture Lane

Source-specific RAW landing lane for immutable USDA National Agricultural Statistics Service material admitted into the Agriculture lifecycle.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-2e7d32">
  <img alt="Source: USDA NASS" src="https://img.shields.io/badge/source-USDA%20NASS-555">
  <img alt="Posture: aggregate guard" src="https://img.shields.io/badge/posture-aggregate%20guard-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Product separation](#product-separation) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/agriculture/usda-nass/` is a RAW source-capture lane. Material here is not processed truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not policy authority, not crop truth, not field truth, not parcel truth, not farm/operator truth, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory may hold immutable source captures, source references, query snapshots, manifest snapshots, checksums, and minimal source-admission sidecars for USDA NASS material after a SourceDescriptor and admission decision identify the material as Agriculture-domain input.

The lane is designed for source preservation, replay, and audit. It does not decide what the source means, whether it may publish, whether rights permit reuse, whether a statistic is safe to join, or whether a downstream claim is true.

USDA NASS source material must preserve product identity. QuickStats / Crop Progress, CDL, and any future NASS product are separate source surfaces with separate roles, cadences, geometry/support, query lineage, and receipts.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/agriculture/usda-nass/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `agriculture` |
| Source family | `usda-nass` |
| Artifact role | Immutable RAW source captures and source-admission sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/agriculture/` or `data/quarantine/agriculture/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when rights, source role, query lineage, product identity, sensitivity, aggregation unit, citation, validation, correction, rollback, or release support is insufficient |

---

## Product separation

| Product surface | KFM source-role posture | RAW handling rule |
|---|---|---|
| USDA NASS QuickStats / Crop Progress | `aggregate` for county / CRD / state / county-year statistics; `administrative` for survey panel definitions where applicable | Preserve query parameters, geography, year/period, commodity, statistic, unit, aggregation unit, row count, response status, retrieval time, and response digest. Never imply field, parcel, farm, operator, or person truth. |
| USDA NASS CDL / Cropland Data Layer | `modeled` annual crop classification, with `aggregate` only for roll-ups where documented | Preserve product identity, raster vintage, classification/model caveats, spatial support, source URL/reference, rights posture, and digest. Do not collapse with QuickStats. |
| Future USDA NASS product | **NEEDS VERIFICATION** | Admit only after SourceDescriptor, rights, source role, cadence, sensitivity, citation, and validation posture are recorded. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- source query snapshots and parameter records;
- raw response payloads or raw payload references;
- manifest files, checksums, content hashes, retrieval timestamps, and source-head records;
- row-count, pagination/chunking, aggregation-unit, and product-vintage notes;
- minimal README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, or public authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Agriculture source-family doctrine | `docs/domains/agriculture/` and `docs/sources/catalog/usda/` |
| Connector code or connector alias decisions | `connectors/nass/`, `connectors/usda-nass/`, or accepted connector home |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` or accepted source-registry lane |
| Rights, terms, attribution, or sensitivity policy | `policy/rights/`, `policy/sensitivity/`, `policy/domains/agriculture/` |
| Quarantine holds and remediation notes | `data/quarantine/agriculture/` |
| Normalized working material | `data/work/agriculture/` |
| Validated processed Agriculture objects | `data/processed/agriculture/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, aggregation, redaction, citation, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Field-level crop, farm, operator, parcel, person, or land-ownership truth | Owning governed domain lane; never this RAW source lane |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/agriculture/usda-nass/
├── README.md
├── <source_id>/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── query_parameters.json
│       ├── response.raw.json
│       ├── manifest.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, crop-truth index, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Rights, source role, product identity, query lineage, aggregation unit, sensitivity, citation, digest, schema, or admission state is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, product separation, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
data/raw/agriculture/usda-nass/
→ data/processed/agriculture/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to USDA NASS and is intended for the Agriculture lane.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, authority, rights, sensitivity, cadence, citation, and hash posture.
- [ ] Confirm product identity: QuickStats, Crop Progress, CDL, or another NASS product.
- [ ] Confirm QuickStats / Crop Progress aggregation unit is preserved and not joined to field, farm, parcel, person, or operator truth.
- [ ] Confirm CDL/classification products remain separate from QuickStats aggregates.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested RAW source-lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `data/` is documented as a lifecycle data root. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/README.md` and `data/raw/agriculture/README.md` are currently greenfield stubs. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture source registry doctrine identifies USDA NASS QuickStats / Crop Progress as aggregate and field-level NASS claims as denied. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture sources doctrine says endpoints, rights, cadences, and current terms remain NEEDS VERIFICATION before ingestion. | **CONFIRMED by GitHub contents API during this edit** |
| Connector USDA NASS alias documentation says connector output may enter raw or quarantine admission lanes only and must not publish. | **CONFIRMED by GitHub contents API during this edit** |
| Actual USDA NASS raw payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, validators, fixtures, CI checks, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, crop truth, field truth, parcel truth, farm/operator truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/agriculture/README.md`](../../../quarantine/agriculture/README.md)
- [`../../../processed/agriculture/README.md`](../../../processed/agriculture/README.md)
- [`../../../catalog/domain/agriculture/README.md`](../../../catalog/domain/agriculture/README.md)
- [`../../../published/layers/agriculture/README.md`](../../../published/layers/agriculture/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/agriculture/SOURCE_REGISTRY.md`](../../../../docs/domains/agriculture/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/agriculture/SOURCES.md`](../../../../docs/domains/agriculture/SOURCES.md)
- [`../../../../docs/domains/agriculture/SENSITIVITY.md`](../../../../docs/domains/agriculture/SENSITIVITY.md)
- [`../../../../docs/sources/catalog/usda/usda-nass-quickstats.md`](../../../../docs/sources/catalog/usda/usda-nass-quickstats.md)
- [`../../../../docs/sources/catalog/usda/usda-nass-cdl.md`](../../../../docs/sources/catalog/usda/usda-nass-cdl.md)
- [`../../../../connectors/usda-nass/README.md`](../../../../connectors/usda-nass/README.md)
- [`../../../../connectors/nass/README.md`](../../../../connectors/nass/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a USDA NASS RAW source-capture lane only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, crop truth, field truth, parcel truth, farm/operator truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
