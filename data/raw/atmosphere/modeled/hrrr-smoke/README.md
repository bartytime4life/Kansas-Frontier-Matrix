<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/modeled/hrrr-smoke/readme
name: HRRR-Smoke Modeled Raw Atmosphere README
path: data/raw/atmosphere/modeled/hrrr-smoke/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <atmosphere-source-steward>
  - <hrrr-smoke-source-steward>
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
source_role: modeled
source_family: hrrr-smoke
artifact_family: immutable-hrrr-smoke-model-run-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; model-run-required; forecast-not-observation; not-alert-authority; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../cams/README.md
  - ../../README.md
  - ../../administrative/README.md
  - ../../aggregate/README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../quarantine/atmosphere/README.md
  - ../../../../processed/atmosphere/README.md
  - ../../../../processed/atmosphere/smoke_context/README.md
  - ../../../../catalog/domain/atmosphere/README.md
  - ../../../../published/layers/atmosphere/README.md
  - ../../../../registry/sources/README.md
  - ../../../../../docs/sources/catalog/noaa/hrrr-smoke.md
  - ../../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../../../docs/architecture/smoke-atmosphere-hazards.md
  - ../../../../../docs/architecture/source-roles.md
  - ../../../../../connectors/hrrr_smoke/README.md
  - ../../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - modeled
  - hrrr-smoke
  - noaa
  - smoke-forecast
  - model-run
  - forecast-cycle
  - lead-time
  - not-observation
  - not-alert-authority
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested HRRR-Smoke Atmosphere RAW modeled source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/modeled/README.md` is currently an empty file, so this child file stays source-family-lane bounded."
  - "HRRR-Smoke modeled forecast fields are source captures, not observations, not measured PM2.5 readings, not current-state truth, not official emergency instructions, and not public KFM products."
  - "Source rights, current terms, payload presence, source descriptors, connector activation, ModelRunReceipt wiring, validator wiring, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# HRRR-Smoke Modeled RAW Atmosphere Lane

Source-family RAW lane for immutable NOAA HRRR-Smoke modeled forecast fields and model-run-bound smoke-context captures.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Source role: modeled" src="https://img.shields.io/badge/source%20role-modeled-7048e8">
  <img alt="Source: HRRR-Smoke" src="https://img.shields.io/badge/source-HRRR--Smoke-555">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [HRRR-Smoke modeled posture](#hrrr-smoke-modeled-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/atmosphere/modeled/hrrr-smoke/` is a RAW source-family capture lane. Material here is not public, not processed Atmosphere truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not observed sensor truth, not measured PM2.5 truth, not AQI concentration truth, not current-state truth, not emergency alerting, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for NOAA HRRR-Smoke model fields whose source role is `modeled`, or whose source-role review is expected to resolve as `modeled`.

Typical material includes model-run references, HRRR-Smoke product references, smoke forecast field payload references, cycle/lead-time manifests, forecast/valid time slices, grid/support metadata, source vintage notes, and digest sidecars. Forecast cycle, lead time, valid time, model family, product name, variable, level, units, grid, physics/version reference where available, and retrieval time must remain inspectable.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a record may publish, whether a forecast is reliable, whether an observation occurred, whether PM2.5 exists at a point, whether smoke forecasts are current-state conditions, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/modeled/hrrr-smoke/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Parent source-role lane | `modeled/` |
| Source family | `hrrr-smoke` |
| Artifact role | RAW source-family lane for HRRR-Smoke modeled captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/atmosphere/` or `data/quarantine/atmosphere/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when rights, source role, model-run identity, forecast cycle, lead time, valid time, variable/level/unit, grid/support, citation, sensitivity, validation, correction, rollback, or release support is insufficient |

---

## HRRR-Smoke modeled posture

| Source / knowledge character | Role handling | RAW rule |
|---|---|---|
| HRRR-Smoke forecast field | `modeled` | Preserve model family, product, forecast cycle, lead time, valid time, variable, level, units, grid/support, source URL/reference, rights posture, digest, and caveats. |
| Forecast cycle / lead-time item | `modeled` | Treat cycle and lead time as item identity. A later cycle must not silently overwrite an earlier cycle for the same valid time. |
| Smoke-context derivative from HRRR-Smoke | `modeled` or `derived_fusion` depending on basis | Preserve source list, method notes, model-run refs, uncertainty/caveats where available, and whether downstream use is public-safe. |
| HRRR-Smoke plus observed station payload | **NEEDS REVIEW** | Split roles or quarantine. A modeled forecast field cannot silently become an observed reading. |
| HRRR-Smoke plus aggregate rollup | **NEEDS REVIEW** | Split modeled and aggregate support or quarantine until aggregation unit and source roles are explicit. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- HRRR-Smoke model-run references, product references, or raw payload references;
- model-run metadata, forecast cycle, lead time, valid time, variable lists, level lists, units, grid/support metadata, retrieval time, source vintage, source URL/reference, attribution, and digest sidecars;
- source-head records, response metadata, status codes, chunking/tile notes where applicable, and checksums;
- minimal README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, observation, alert, or public authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| HRRR-Smoke source/product doctrine | `docs/sources/catalog/noaa/hrrr-smoke.md` |
| Atmosphere source-family doctrine | `docs/domains/atmosphere/` |
| Connector code or connector decisions | `connectors/hrrr_smoke/` or accepted connector home |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` or accepted source-registry lane |
| Rights, terms, sensitivity, or policy rules | `policy/` |
| Quarantine holds and remediation notes | `data/quarantine/atmosphere/` |
| Normalized working material | `data/work/atmosphere/` |
| Validated processed Atmosphere objects | `data/processed/atmosphere/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, aggregation, redaction, source-role, model-run, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Observed sensor readings, regulatory archives, AQI reports as concentrations, AOD rasters as PM2.5, HMS analyst smoke detections, low-cost sensor point truth, or aggregate truth | Owning source-role/product lane and downstream governed stages; never this HRRR-Smoke RAW lane by itself |
| Emergency alerting, life-safety instructions, evacuation/routing advice, authoritative health guidance, or hazards event truth | External official authorities / owning downstream domains, not KFM RAW data |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/modeled/hrrr-smoke/
├── README.md
├── <product_id>/
│   └── <cycle_or_run_id>/
│       ├── source_reference.json
│       ├── model_run_ref.json
│       ├── forecast_cycle.json
│       ├── lead_time_index.json
│       ├── product_manifest.json
│       ├── grid_support.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, observation index, smoke-truth authority, alerting source, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Rights, source role, model-run identity, product identity, forecast cycle, lead time, valid time, variable/level/unit, grid/support, attribution, citation, digest, sensitivity, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, model-run/product support, forecast-cycle/lead-time support, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, ModelRunReceipt where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
data/raw/atmosphere/modeled/hrrr-smoke/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Atmosphere lane and is NOAA HRRR-Smoke modeled forecast material.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, authority, rights, sensitivity, cadence, citation, model-run identity, product identity, and hash posture.
- [ ] Confirm modeled forecast material is not being cited as an observed sensor reading, current-state truth, regulatory archive, AQI concentration truth, measured PM2.5 reading, HMS observed smoke product, or emergency/life-safety instruction.
- [ ] Confirm forecast cycle, lead time, valid time, retrieval time, variable, level, units, grid/support, and caveats are recorded where material.
- [ ] Confirm later cycles do not silently overwrite earlier cycles for the same valid time.
- [ ] Confirm modeled smoke or PM2.5-equivalent fields are not transformed into concentration, health, hazard, or life-safety claims without governed downstream evidence and receipts.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested HRRR-Smoke Atmosphere modeled RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/atmosphere/modeled/README.md` is currently an empty file. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source registry doctrine lists HRRR-Smoke / NOAA smoke forecast as modeled with public NOAA terms and model-run cadence. | **CONFIRMED by GitHub contents API during this edit** |
| HRRR-Smoke source-page doctrine says HRRR-Smoke is modeled forecast material, requires ModelRunReceipt, and is not an observation or alert authority. | **CONFIRMED by GitHub contents API during this edit** |
| HRRR-Smoke source-page doctrine says cycle and lead time are part of identity and later cycles must not silently overwrite earlier cycles. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere doctrine says AQI is not concentration, AOD is not PM2.5, model fields are not observations, and such collapses are denied at the trust membrane. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference, requires SourceDescriptor/RawCaptureReceipt, and is denied to public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual HRRR-Smoke RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, ModelRunReceipt wiring, validators, fixtures, CI checks, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, observation truth, model truth authority, AQI concentration truth, smoke-truth authority, emergency guidance, hazards event truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../cams/README.md`](../cams/README.md)
- [`../../README.md`](../../README.md)
- [`../../administrative/README.md`](../../administrative/README.md)
- [`../../aggregate/README.md`](../../aggregate/README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../../README.md`](../../../../README.md)
- [`../../../../quarantine/atmosphere/README.md`](../../../../quarantine/atmosphere/README.md)
- [`../../../../processed/atmosphere/README.md`](../../../../processed/atmosphere/README.md)
- [`../../../../processed/atmosphere/smoke_context/README.md`](../../../../processed/atmosphere/smoke_context/README.md)
- [`../../../../catalog/domain/atmosphere/README.md`](../../../../catalog/domain/atmosphere/README.md)
- [`../../../../published/layers/atmosphere/README.md`](../../../../published/layers/atmosphere/README.md)
- [`../../../../registry/sources/README.md`](../../../../registry/sources/README.md)
- [`../../../../../docs/sources/catalog/noaa/hrrr-smoke.md`](../../../../../docs/sources/catalog/noaa/hrrr-smoke.md)
- [`../../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md`](../../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md)
- [`../../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md`](../../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md)
- [`../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md`](../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
- [`../../../../../docs/architecture/smoke-atmosphere-hazards.md`](../../../../../docs/architecture/smoke-atmosphere-hazards.md)
- [`../../../../../docs/architecture/source-roles.md`](../../../../../docs/architecture/source-roles.md)
- [`../../../../../connectors/hrrr_smoke/README.md`](../../../../../connectors/hrrr_smoke/README.md)
- [`../../../../../release/manifests/README.md`](../../../../../release/manifests/README.md)

---

KFM rule: this directory is an HRRR-Smoke Atmosphere modeled RAW source-family lane only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, observation truth, model truth authority, AQI concentration truth, smoke-truth authority, emergency guidance, hazards event truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
