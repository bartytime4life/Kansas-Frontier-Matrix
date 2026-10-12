<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/modeled/hrrr-smoke/readme
title: HRRR-Smoke Modeled Raw Atmosphere README
path: data/raw/atmosphere/modeled/hrrr-smoke/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
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
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked HRRR-Smoke modeled Atmosphere RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: atmosphere
source_role: modeled
source_family: hrrr-smoke
artifact_family: atmosphere-hrrr-smoke-raw-compatibility-reference
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
  - compatibility-reference
  - source-first
notes:
  - "This README documents the requested HRRR-Smoke Atmosphere RAW modeled source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/modeled/README.md` was an empty file when this lane was first authored; it now exists as a compatibility/reference index. This child file stays source-family-lane bounded."
  - "HRRR-Smoke modeled forecast fields are source-first captures referenced (not held) by this compatibility lane; they are not observations, not measured PM2.5 readings, not current-state truth, not official emergency instructions, and not public KFM products."
  - "Source rights, current terms, payload presence, source descriptors, connector activation, ModelRunReceipt wiring, validator wiring, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# HRRR-Smoke Modeled RAW Atmosphere Lane

Compatibility and reference documentation for Atmosphere-facing NOAA HRRR-Smoke modeled forecast fields and model-run-bound smoke-context RAW topology; not a physical source-capture home.

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
> `data/raw/atmosphere/modeled/hrrr-smoke/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named lane is not a default physical capture home and must not receive duplicate RAW payloads. Material here is not public, not processed Atmosphere truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not observed sensor truth, not measured PM2.5 truth, not AQI concentration truth, not current-state truth, not emergency alerting, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory documents tracked Atmosphere-facing RAW topology for NOAA HRRR-Smoke model fields whose source role is `modeled`, or whose source-role review is expected to resolve as `modeled`. It may reference one governed source-first capture, but it does not hold that capture or establish where it is stored.

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
| Artifact role | Compatibility/reference lane for HRRR-Smoke modeled source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Atmosphere WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
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
| Capture identity is source-first | All roles and components | Register one `source_id` and preserve one immutable capture identity; domain references may support Atmosphere without duplicating RAW bytes. |
| Physical placement is held | All roles and components | Do not infer `data/raw/atmosphere/modeled/hrrr-smoke/` or a child directory as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| HRRR-Smoke forecast field | `modeled` | Preserve model family, product, forecast cycle, lead time, valid time, variable, level, units, grid/support, source URL/reference, rights posture, digest, and caveats. |
| Forecast cycle / lead-time item | `modeled` | Treat cycle and lead time as item identity. A later cycle must not silently overwrite an earlier cycle for the same valid time. |
| Smoke-context derivative from HRRR-Smoke | `modeled` or `derived_fusion` depending on basis | Preserve source list, method notes, model-run refs, uncertainty/caveats where available, and whether downstream use is public-safe. |
| HRRR-Smoke plus observed station payload | **NEEDS REVIEW** | Split roles or quarantine. A modeled forecast field cannot silently become an observed reading. |
| HRRR-Smoke plus aggregate rollup | **NEEDS REVIEW** | Split modeled and aggregate support or quarantine until aggregation unit and source roles are explicit. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; like any README, it must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, observation, alert, or public authority.

The governed source-first capture or reference (not this subtree) must carry or point to the HRRR-Smoke capture material below:

- source-reference manifests;
- HRRR-Smoke model-run references, product references, or raw payload references;
- model-run metadata, forecast cycle, lead time, valid time, variable lists, level lists, units, grid/support metadata, retrieval time, source vintage, source URL/reference, attribution, and digest sidecars;
- source-head records, response metadata, status codes, chunking/tile notes where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Atmosphere. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. The per-run layout previously sketched here (`<product_id>/<cycle_or_run_id>/` holding `source_reference.json`, `model_run_ref.json`, `forecast_cycle.json`, `lead_time_index.json`, `product_manifest.json`, `grid_support.json`, `checksums.sha256`, and a run `README.md`) is a proposed shape for a future accepted source-first home, not this subtree. Do not add a product or run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

An optional local documentation index, if ever accepted, would not be a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, observation index, smoke-truth authority, alerting source, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This lane may retain a governed reference only. |
| Quarantine | Rights, source role, model-run identity, product identity, forecast cycle, lead time, valid time, variable/level/unit, grid/support, attribution, citation, digest, sensitivity, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Atmosphere WORK only when SourceDescriptor, rights posture, source role, model-run/product support, forecast-cycle/lead-time support, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, ModelRunReceipt where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Atmosphere-scoped copy.
- [ ] Treat this source-named README as compatibility/reference documentation only; do not create a child directory as a payload destination.
- [ ] Confirm the source is NOAA HRRR-Smoke modeled forecast material; source-family classification does not make this lane a capture home.
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
| Parent `data/raw/atmosphere/modeled/README.md` was an empty file when this lane was first authored. | **CONFIRMED at original authoring; SUPERSEDED — parent README is present at `main@9e8bf3e6` and was reconciled as a compatibility/reference index on 2026-10-11** |
| Atmosphere source registry doctrine lists HRRR-Smoke / NOAA smoke forecast as modeled with public NOAA terms and model-run cadence. | **CONFIRMED by GitHub contents API during this edit** |
| HRRR-Smoke source-page doctrine says HRRR-Smoke is modeled forecast material, requires ModelRunReceipt, and is not an observation or alert authority. | **CONFIRMED by GitHub contents API during this edit** |
| HRRR-Smoke source-page doctrine says cycle and lead time are part of identity and later cycles must not silently overwrite earlier cycles. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere doctrine says AQI is not concentration, AOD is not PM2.5, model fields are not observations, and such collapses are denied at the trust membrane. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference, requires SourceDescriptor/RawCaptureReceipt, and is denied to public access. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual HRRR-Smoke RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| SourceDescriptor records, connector activation, ModelRunReceipt wiring, validators, fixtures, CI checks, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
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

KFM rule: this directory is an HRRR-Smoke Atmosphere-facing modeled compatibility/reference lane. One governed source-first capture may support Atmosphere without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, observation truth, model truth authority, AQI concentration truth, smoke-truth authority, emergency guidance, hazards event truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
