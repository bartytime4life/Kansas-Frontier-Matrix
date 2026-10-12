<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/agriculture/readme
title: Agriculture Raw README
path: data/raw/agriculture/README.md
type: data-raw-domain-index-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <agriculture-domain-steward>
  - <source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Agriculture RAW compatibility and reference index without treating this domain subtree or its source-named children as physical source-first capture homes or duplicating RAW bytes.
domain: agriculture
artifact_family: agriculture-raw-compatibility-reference-index
sensitivity_posture: raw-internal; source-role-preserving; rights-needs-verification; no-public-path; release-blocked
related:
  - usda-nass/README.md
  - ../usda-nass/README.md
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
  - compatibility-reference
  - source-first
notes:
  - "This README replaces the greenfield stub and documents the Agriculture-facing RAW compatibility/reference index."
  - "Confirmed child README lane during this edit: `usda-nass/`."
  - "RAW is immutable source-first capture and source-admission context; this domain index is not a physical capture home and is not Agriculture truth, processed truth, catalog truth, proof, receipt authority, release authority, public API/UI output, or generated-answer authority."
  - "Agriculture source docs mark source endpoints, rights, cadences, and current terms as NEEDS VERIFICATION before ingestion."
  - "Domain child README presence does not prove raw payload presence, connector activation, SourceDescriptor records, validators, fixtures, CI enforcement, downstream receipts, review completion, or release readiness."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture RAW

Compatibility and reference index for legacy Agriculture-scoped RAW documentation; not a physical source-capture home.

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
> `data/raw/agriculture/` is a no-public-path compatibility/reference index inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this domain subtree and its source-named children are not default physical capture homes and must not receive duplicate RAW payloads. Material here is not processed Agriculture truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not crop truth, not field truth, not parcel truth, not farm/operator truth, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory indexes tracked Agriculture-facing source documentation and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture preserves the source references, source-head snapshots, query snapshots, manifest snapshots, checksums, and minimal source-admission context that Agriculture use depends on.

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
| Artifact role | Compatibility/reference index for Agriculture-facing source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Agriculture WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when rights, source role, query lineage, product identity, sensitivity, aggregation unit, citation, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source lanes

The source lane below is a README path confirmed by current-session GitHub fetches/edits. Treat it as compatibility/reference documentation or unresolved legacy topology, not a source-first capture home. This table confirms README presence only; it does **not** prove or authorize payloads, source descriptors, connectors, validators, fixtures, receipts, CI checks, migration, or release readiness.

| Source lane | Status | Boundary summary |
|---|---|---|
| [`usda-nass/`](usda-nass/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | USDA NASS source documentation; not a capture home. QuickStats / Crop Progress are aggregate; CDL is a separate modeled/classification product; neither may become field, parcel, farm, operator, person, crop, or release truth from RAW. |

The top-level [`../usda-nass/README.md`](../usda-nass/README.md) documents the same USDA NASS upstream source as a compatibility lane. Both lanes must reference the same single source-first capture, never two copies.

---

## Proposed source families

Agriculture source docs name the families below. They are source-routing guidance, not proof that RAW folders, payloads, SourceDescriptors, connectors, fixtures, or validators exist, and not authorization to create Agriculture-scoped RAW folders for them. Each admitted family needs one source-first capture identity; several families (for example SSURGO, Mesonet, SCAN, USCRN, and SMAP, also listed by [`../soil/README.md`](../soil/README.md)) may also support other domains without duplicated RAW bytes.

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

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- the tracked README files listed below;
- links to canonical SourceDescriptor, source-admission, rights, sensitivity, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted.

The source-first capture or its governed reference must carry, where material: source-reference manifests; source query snapshots and parameter records; raw response payloads or raw payload references; raster, tabular, station, or manifest payload references with digest closure; and source-head records, retrieval timestamps, row counts, pagination/chunking notes, product-vintage notes, and checksums. Any README or index sidecar must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, or public authority.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Agriculture. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── usda-nass/README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a future source directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Any optional local documentation index (previously sketched in this map as a local JSON index file) is a proposed shape for a future accepted source-first home or documentation contract, not this subtree. If accepted, it must not become a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, crop-truth index, field-truth index, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This index may retain a governed reference only. |
| Quarantine | Rights, source role, product identity, query lineage, aggregation unit, sensitivity, citation, digest, schema, source activation, admission state, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Agriculture WORK only when SourceDescriptor, rights posture, source role, product separation, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/agriculture/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Agriculture-scoped copy.
- [ ] Treat this README and the source-named child README as compatibility/reference documentation only; do not create a child directory as a payload destination.
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
| `usda-nass/README.md` exists as a confirmed child Agriculture compatibility/reference README. | **CONFIRMED by GitHub contents API during this edit** |
| `data/` is documented as a lifecycle data root. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/README.md` was a greenfield stub when this README was first authored. | **CONFIRMED by GitHub contents API during that edit; superseded — the parent now carries the source-first contract** |
| Agriculture source docs say endpoints, rights, cadences, and current terms remain NEEDS VERIFICATION before ingestion. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture source docs say source role is set at admission and preserved through promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture source docs say aggregate NASS data must not become per-place/field/farm/parcel/person truth. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual Agriculture RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| `data/raw/agriculture/usda-nass/` and top-level `data/raw/usda-nass/` both document USDA NASS and must reference one source-first capture, never two copies. | **CONFIRMED README presence; shared capture placement NEEDS VERIFICATION** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, validators, fixtures, CI checks, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, crop truth, field truth, parcel truth, farm/operator truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`usda-nass/README.md`](usda-nass/README.md)
- [`../usda-nass/README.md`](../usda-nass/README.md)
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

KFM rule: this directory is an Agriculture-facing compatibility/reference index. One governed source-first capture may support Agriculture without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, crop truth, field truth, parcel truth, farm/operator truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
