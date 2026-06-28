<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/agriculture/readme
name: Agriculture Raw README
path: data/raw/agriculture/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <agriculture-domain-steward>
  - <source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: agriculture
artifact_family: immutable-agriculture-source-capture
sensitivity_posture: raw-internal; source-role-preserving; rights-needs-verification; no-public-path; release-blocked
related:
  - usda-nass/README.md
  - ../README.md
  - ../../README.md
  - ../../quarantine/agriculture/README.md
  - ../../processed/agriculture/README.md
  - ../../catalog/domain/agriculture/README.md
  - ../../published/layers/agriculture/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../docs/domains/agriculture/SOURCES.md
  - ../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../connectors/domains/agriculture/README.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - agriculture
  - source-capture
  - source-role
  - rights-review
  - immutable-capture
  - quickstats
  - cdl
  - ssurgo
  - mesonet
  - scan
  - uscrn
  - smap
  - hls
  - evidence-first
notes:
  - "This README replaces the greenfield stub and documents the parent Agriculture RAW lifecycle lane."
  - "Confirmed child README lane during this edit: `usda-nass/`."
  - "RAW is immutable source capture and source-admission context; it is not Agriculture truth, processed truth, catalog truth, proof, receipt authority, release authority, public API/UI output, or generated-answer authority."
  - "Agriculture source docs mark source endpoints, rights, cadences, and current terms as NEEDS VERIFICATION before ingestion."
  - "Domain child README presence does not prove raw payload presence, connector activation, SourceDescriptor records, validators, fixtures, CI enforcement, downstream receipts, review completion, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture RAW

Parent RAW lifecycle lane for immutable Agriculture-domain source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-2e7d32">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Rights: needs verification" src="https://img.shields.io/badge/rights-NEEDS%20VERIFICATION-orange">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source lanes](#confirmed-source-lanes) · [Proposed source families](#proposed-source-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/agriculture/` is a RAW source-capture lane. Material here is not processed Agriculture truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not crop truth, not field truth, not parcel truth, not farm/operator truth, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory holds immutable source captures, source references, source-head snapshots, query snapshots, manifest snapshots, checksums, and minimal source-admission sidecars for Agriculture source families.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a source can publish, whether a statistic can be joined, whether a model is reliable, whether a candidate is accepted, or whether a downstream claim is true.

Agriculture source role is set at admission and preserved. Observed readings, modeled products, aggregates, administrative records, candidates, and synthetic content are not interchangeable.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/agriculture/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `agriculture` |
| Artifact role | Parent RAW lane for Agriculture source captures and RAW-local sidecars |
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

## Confirmed source lanes

The source lane below is a README path confirmed by current-session GitHub fetches/edits. This table confirms README presence only; it does **not** prove payloads exist.

| Source lane | Status | Boundary summary |
|---|---|---|
| [`usda-nass/`](usda-nass/README.md) | **CONFIRMED README** | USDA NASS RAW source-capture lane. QuickStats / Crop Progress are aggregate; CDL is a separate modeled/classification product; neither may become field, parcel, farm, operator, person, crop, or release truth from RAW. |

---

## Proposed source families

Agriculture source docs name the families below. They are source-routing guidance, not proof that RAW folders, payloads, SourceDescriptors, connectors, fixtures, or validators exist.

| Source family | Source-role posture | Status |
|---|---|---|
| SSURGO / Soil Data Access | `observed` for soil survey evidence; `aggregate` for summaries | **PROPOSED / NEEDS VERIFICATION** |
| gSSURGO | `aggregate` gridded derivative | **PROPOSED / NEEDS VERIFICATION** |
| Kansas Mesonet | `observed` for station sensor readings; `aggregate` for summaries | **PROPOSED / NEEDS VERIFICATION** |
| NRCS SCAN | `observed` for station sensor records; `aggregate` for summaries | **PROPOSED / NEEDS VERIFICATION** |
| NOAA USCRN | `observed` reference sensor record; `aggregate` for summaries | **PROPOSED / NEEDS VERIFICATION** |
| NASA SMAP | `modeled` Level-3/4 product; `aggregate` for downscaled or averaged surfaces | **PROPOSED / NEEDS VERIFICATION** |
| NASA HLS / HLS-VI | `modeled` harmonized/derived vegetation product; `aggregate` for composites | **PROPOSED / NEEDS VERIFICATION** |
| USDA NASS QuickStats / Crop Progress | `aggregate`; `administrative` for survey panel definitions where applicable | **CONFIRMED source-family doctrine / NEEDS VERIFICATION current terms** |
| USDA CDL | `modeled` annual classification; aggregate only for documented roll-ups | **PROPOSED / NEEDS VERIFICATION** |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- source query snapshots and parameter records;
- raw response payloads or raw payload references;
- raster, tabular, station, or manifest payload references with digest closure;
- source-head records, retrieval timestamps, row counts, pagination/chunking notes, product-vintage notes, and checksums;
- minimal README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, or public authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Agriculture source-family doctrine | `docs/domains/agriculture/` and `docs/sources/catalog/` |
| Connector code or connector alias decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` or accepted source-registry lane |
| Rights, terms, attribution, sensitivity, or policy rules | `policy/` |
| Quarantine holds and remediation notes | `data/quarantine/agriculture/` |
| Normalized working material | `data/work/agriculture/` |
| Validated processed Agriculture objects | `data/processed/agriculture/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, aggregation, redaction, citation, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Field-level crop, farm, operator, parcel, person, or land-ownership truth | Owning governed domain lane; never this RAW lane |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/agriculture/
├── README.md
├── usda-nass/
│   └── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, crop-truth index, field-truth index, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Rights, source role, product identity, query lineage, aggregation unit, sensitivity, citation, digest, schema, source activation, or admission state is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, product separation, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
data/raw/agriculture/
→ data/processed/agriculture/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Agriculture lane.
- [ ] Confirm the correct source family subfolder or create a documented source-lane README before adding payloads.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, authority, rights, sensitivity, cadence, citation, and hash posture.
- [ ] Confirm product identity, support, aggregation unit, geography/time scope, units, and source vintage where material.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm aggregate sources are not joined to field, farm, parcel, person, or operator truth.
- [ ] Confirm modeled products are not treated as observed measurements.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/agriculture/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `usda-nass/README.md` exists as a confirmed child RAW Agriculture source-lane README. | **CONFIRMED by GitHub contents API during this edit** |
| `data/` is documented as a lifecycle data root. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture source docs say endpoints, rights, cadences, and current terms remain NEEDS VERIFICATION before ingestion. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture source docs say source role is set at admission and preserved through promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture source docs say aggregate NASS data must not become per-place/field/farm/parcel/person truth. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Agriculture RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, validators, fixtures, CI checks, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, crop truth, field truth, parcel truth, farm/operator truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`usda-nass/README.md`](usda-nass/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/agriculture/README.md`](../../quarantine/agriculture/README.md)
- [`../../processed/agriculture/README.md`](../../processed/agriculture/README.md)
- [`../../catalog/domain/agriculture/README.md`](../../catalog/domain/agriculture/README.md)
- [`../../published/layers/agriculture/README.md`](../../published/layers/agriculture/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/agriculture/SOURCE_REGISTRY.md`](../../../docs/domains/agriculture/SOURCE_REGISTRY.md)
- [`../../../docs/domains/agriculture/SOURCES.md`](../../../docs/domains/agriculture/SOURCES.md)
- [`../../../docs/domains/agriculture/SENSITIVITY.md`](../../../docs/domains/agriculture/SENSITIVITY.md)
- [`../../../docs/domains/agriculture/DATA_LIFECYCLE.md`](../../../docs/domains/agriculture/DATA_LIFECYCLE.md)
- [`../../../connectors/domains/agriculture/README.md`](../../../connectors/domains/agriculture/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is an Agriculture RAW source-capture index only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, crop truth, field truth, parcel truth, farm/operator truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
