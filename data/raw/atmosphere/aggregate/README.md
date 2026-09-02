<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/aggregate/readme
name: Atmosphere Aggregate Raw README
path: data/raw/atmosphere/aggregate/README.md
type: data-raw-source-role-lane-readme
version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <atmosphere-source-steward>
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
domain: atmosphere
source_role: aggregate
artifact_family: immutable-atmosphere-aggregate-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; aggregate-unit-required; no-single-record-joinback; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../administrative/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../processed/atmosphere/air_observations/README.md
  - ../../../processed/atmosphere/aod/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../published/layers/atmosphere/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../../docs/domains/atmosphere/API_CONTRACTS.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - aggregate
  - source-role
  - climate-normal
  - openaq
  - rollup
  - aggregation-unit
  - no-joinback
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested Atmosphere RAW aggregate source-role lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/README.md` is currently a greenfield stub, so this child file stays source-role-lane bounded."
  - "Aggregate Atmosphere records are source captures, not individual observations, not model fields, not AQI concentration truth, not single-station truth, and not public KFM products."
  - "Source rights, current terms, payload presence, source descriptors, connector activation, validator wiring, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Aggregate RAW Lane

Source-role RAW lane for immutable Atmosphere aggregate records, rollups, climate normals, source-vintage aggregates, and aggregation-unit-bound captures.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Source role: aggregate" src="https://img.shields.io/badge/source%20role-aggregate-7048e8">
  <img alt="Posture: no joinback" src="https://img.shields.io/badge/posture-no%20single--record%20joinback-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Aggregate source posture](#aggregate-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/atmosphere/aggregate/` is a RAW source-role capture lane. Material here is not public, not processed Atmosphere truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not observed sensor truth, not single-station truth, not model truth, not AQI concentration truth, not emergency alerting, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for Atmosphere material whose source role is aggregate, or whose source-role review is expected to resolve as aggregate.

Typical aggregate Atmosphere material includes climate normals, climate/anomaly aggregates, OpenAQ-like source-vintage rollups, period/geography summaries, multi-station summary records, derived source-level summaries, and aggregation-unit-bound context records. The aggregation unit must remain visible and must not be joined back to a single station, person, parcel, address, low-cost sensor, or event as if it were observed evidence.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a record may publish, whether an aggregate is representative, whether an observation occurred, whether a model is reliable, whether a concentration exists at a point, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/aggregate/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Source role | `aggregate` |
| Artifact role | RAW source-role lane for aggregate captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/atmosphere/` or `data/quarantine/atmosphere/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when rights, source role, aggregation unit, period, geography, citation, sensitivity, representativeness, validation, correction, rollback, or release support is insufficient |

---

## Aggregate source posture

| Source / knowledge character | Role handling | RAW rule |
|---|---|---|
| Climate normals / anomalies | `aggregate` over multi-year period, geography, station network, or grid support | Preserve period, baseline, aggregation unit, source vintage, geography/support, unit, citation, digest, and caveats. |
| OpenAQ-like rollups | `aggregate`; may also carry `observed` provenance for underlying contributing observations | Preserve source-vintage, contributing-source list if available, aggregation period, geography, units, source terms, and caveats. Do not join back to a single record. |
| Multi-station summaries | `aggregate` | Preserve station/network population, inclusion/exclusion rules, temporal window, statistic, and units. Do not present as one observed station reading. |
| Derived aggregate context | `aggregate` or `derived_fusion` depending on basis | Preserve source list, weights or method notes where available, aggregation unit, caveats, and whether it is public-safe. |
| Mixed aggregate + observed payload | **NEEDS REVIEW** | Split roles or quarantine. An aggregate record cannot silently become an observed reading. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- aggregate/source packet snapshots or stable source references;
- raw payloads or raw payload references;
- period, baseline, aggregation unit, geography/support, units, contributing-source list, method notes, source vintage, retrieval time, source URL/reference, attribution, and digest sidecars;
- source-head records, response metadata, status codes, row counts where applicable, and checksums;
- minimal README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, observation, model, alert, or public authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Atmosphere source-family doctrine | `docs/domains/atmosphere/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` or accepted source-registry lane |
| Rights, terms, sensitivity, or policy rules | `policy/` |
| Quarantine holds and remediation notes | `data/quarantine/atmosphere/` |
| Normalized working material | `data/work/atmosphere/` |
| Validated processed Atmosphere objects | `data/processed/atmosphere/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, aggregation, redaction, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Single observed sensor readings, model fields, AQI reports as concentrations, AOD rasters as PM2.5, or low-cost sensor point truth | Owning source-role/product lane and downstream governed stages; never this aggregate RAW lane by itself |
| Emergency alerting, life-safety instructions, evacuation/routing advice, or authoritative health guidance | External official authorities, not KFM RAW data |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/aggregate/
├── README.md
├── <source_id>/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── aggregate_ref.json
│       ├── aggregation_unit.json
│       ├── manifest.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, observation index, aggregate truth authority, alerting source, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Rights, source role, aggregation unit, period, geography/support, attribution, citation, digest, sensitivity, schema, source activation, or joinback risk is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, aggregation unit, period/geography support, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
data/raw/atmosphere/aggregate/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Atmosphere lane and is aggregate or expected to resolve as aggregate.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, authority, rights, sensitivity, cadence, citation, aggregation unit, period/geography support, and hash posture.
- [ ] Confirm aggregate material is not being cited as an observed sensor reading, single-station truth, model evidence, AQI concentration truth, or emergency/life-safety instruction.
- [ ] Confirm aggregation unit, time period, geography/support, units, baseline, method, and contributing-source list are recorded where material.
- [ ] Confirm aggregate cells are not joined back to a single record, person, parcel, address, low-cost sensor, or station without governed review.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested Atmosphere aggregate RAW source-role lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/atmosphere/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| `data/raw/atmosphere/administrative/README.md` exists as a sibling source-role lane. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source registry doctrine lists OpenAQ-like aggregators as aggregate/observed and climate normals/anomalies as aggregate. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source-role doctrine says aggregate records require an aggregation unit and must not be joined back to a single record. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference, requires SourceDescriptor/RawCaptureReceipt, and is denied to public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual aggregate Atmosphere RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, validators, fixtures, CI checks, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, observation truth, model truth, aggregate truth authority, emergency guidance, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../administrative/README.md`](../administrative/README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/atmosphere/README.md`](../../../quarantine/atmosphere/README.md)
- [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- [`../../../processed/atmosphere/air_observations/README.md`](../../../processed/atmosphere/air_observations/README.md)
- [`../../../processed/atmosphere/aod/README.md`](../../../processed/atmosphere/aod/README.md)
- [`../../../catalog/domain/atmosphere/README.md`](../../../catalog/domain/atmosphere/README.md)
- [`../../../published/layers/atmosphere/README.md`](../../../published/layers/atmosphere/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md`](../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md`](../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md`](../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
- [`../../../../docs/domains/atmosphere/API_CONTRACTS.md`](../../../../docs/domains/atmosphere/API_CONTRACTS.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is an Atmosphere aggregate RAW source-role lane only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, observation truth, model truth, AQI concentration truth, aggregate truth authority, emergency guidance, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
