<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/modeled/readme
name: Atmosphere Modeled Raw README
path: data/raw/atmosphere/modeled/README.md
type: data-raw-source-role-index-readme
version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <atmosphere-source-steward>
  - <data-steward>
  - <model-run-reviewer>
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
artifact_family: immutable-atmosphere-modeled-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; model-run-required; not-observation; not-alert-authority; rights-needs-verification; release-blocked
related:
  - cams/README.md
  - hrrr-smoke/README.md
  - ../README.md
  - ../administrative/README.md
  - ../aggregate/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../processed/atmosphere/aod/README.md
  - ../../../processed/atmosphere/smoke_context/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../published/layers/atmosphere/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../../docs/sources/catalog/noaa/hrrr-smoke.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - modeled
  - model-field
  - model-run
  - forecast
  - cams
  - hrrr-smoke
  - not-observation
  - not-alert-authority
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the empty parent `data/raw/atmosphere/modeled/README.md` file and documents the Atmosphere modeled RAW source-role index."
  - "Confirmed child README lanes during this edit: `cams/` and `hrrr-smoke/`."
  - "Modeled Atmosphere records are source captures, not observations, not AQI concentration truth, not measured PM2.5 truth, not alert authority, not public KFM products, and not generated-answer authority."
  - "Model-run identity, forecast/valid time, variable/unit/grid support, rights posture, source role, and receipt closure must remain inspectable before anything leaves RAW."
  - "Payload presence, source descriptors, connector activation, model-run receipts, validators, fixtures, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Modeled RAW

Parent RAW source-role index for immutable Atmosphere modeled fields, forecasts, retrieval-like model products, model-run-bound captures, and model-derived context.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Source role: modeled" src="https://img.shields.io/badge/source%20role-modeled-7048e8">
  <img alt="Posture: model not observation" src="https://img.shields.io/badge/posture-model%20%E2%89%A0%20observation-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed modeled source lanes](#confirmed-modeled-source-lanes) · [Modeled source posture](#modeled-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/atmosphere/modeled/` is a no-public-path RAW source-role index. Material here is not public, not processed Atmosphere truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not observed sensor truth, not measured PM2.5 truth, not AQI concentration truth, not emergency alerting, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory indexes Atmosphere RAW material whose source role is `modeled`, or whose source-role review is expected to resolve as `modeled`.

Typical modeled material includes numerical weather prediction outputs, smoke forecasts, atmospheric model fields, retrieval/model products, model-run-bound forecast fields, and model-derived context packets. The model family, product, run/reference time, forecast/valid time, variable, level, units, grid/support, model version or physics reference where available, retrieval time, source vintage, citation, rights posture, and digest must remain inspectable.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a model is reliable, whether an observation occurred, whether PM2.5 exists at a point, whether a smoke forecast is current-state truth, whether an AOD-like retrieval implies ground concentration, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/modeled/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Source role | `modeled` |
| Artifact role | Parent RAW source-role index for modeled Atmosphere captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/atmosphere/` or `data/quarantine/atmosphere/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when rights, source role, model-run identity, product identity, valid time, variable/level/unit, grid/support, citation, sensitivity, validation, correction, rollback, or release support is insufficient |

---

## Confirmed modeled source lanes

The child lanes below are README paths confirmed by current-session GitHub fetches/edits. This table confirms README presence only; it does **not** prove payloads, source descriptors, connectors, validators, fixtures, receipts, CI checks, or release readiness exist.

| Source lane | Status | Boundary summary |
|---|---|---|
| [`cams/`](cams/README.md) | **CONFIRMED README** | CAMS / ECMWF-family modeled fields. Preserve model family, product, run/reference time, valid time, variable, level, units, grid/support, rights posture, digest, and caveats. |
| [`hrrr-smoke/`](hrrr-smoke/README.md) | **CONFIRMED README** | NOAA HRRR-Smoke modeled forecast fields. Preserve forecast cycle, lead time, valid time, model-run identity, grid/support, rights posture, digest, and not-alert-authority caveats. |

---

## Modeled source posture

| Rule | Handling |
|---|---|
| Model fields are not observations | A modeled value may inform context or downstream analysis, but it cannot be re-labeled as observed sensor truth. |
| Forecast cycle and valid time are distinct | Run/reference time, forecast lead time, valid time, retrieval time, and release time must not collapse. |
| Model-run support is required | Modeled outputs require model-run identity and a downstream ModelRunReceipt or equivalent before promotion beyond RAW. |
| Product identity must remain visible | Product name, version/physics reference where available, variable, level, units, grid/support, and source vintage are part of review. |
| AQI/AOD/PM2.5 collapses are denied | AQI is not concentration; AOD is not PM2.5; modeled smoke or chemical fields are not measured concentrations. |
| Mixed-role payloads are not flattened | Payloads combining model, aggregate, administrative, regulatory, or observed content must split roles or quarantine. |
| KFM is not alert authority | Forecast/model data must not become emergency guidance, evacuation advice, life-safety instruction, or authoritative health guidance. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- model-run references, product references, model field payload references, or restricted raw payload references;
- model-run metadata, product metadata, variable lists, level lists, units, grid/support metadata, forecast/valid times, analysis/initialization times, retrieval time, source vintage, source URL/reference, attribution, and digest sidecars;
- source-head records, response metadata, status codes, chunking/tile notes where applicable, and checksums;
- minimal README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, observation, alert, or public authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Atmosphere source-family doctrine | `docs/domains/atmosphere/` and `docs/sources/catalog/` |
| Connector code or connector decisions | `connectors/` |
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
| Observed sensor readings, regulatory archives, AQI reports as concentrations, AOD rasters as PM2.5, HMS analyst smoke detections, low-cost sensor point truth, aggregate truth, or advisory authority | Owning source-role/product lane and downstream governed stages; never this modeled RAW lane by itself |
| Emergency alerting, life-safety instructions, evacuation/routing advice, authoritative health guidance, or hazards event truth | External official authorities / owning downstream domains, not KFM RAW data |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/modeled/
├── README.md
├── cams/
│   └── README.md
├── hrrr-smoke/
│   └── README.md
├── <future-modeled-source-family>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, observation index, model-truth authority, alerting source, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Rights, source role, model-run identity, product identity, valid time, variable/level/unit, grid/support, attribution, citation, digest, sensitivity, schema, source activation, or role-mixing is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, model-run/product support, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, ModelRunReceipt where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
data/raw/atmosphere/modeled/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Atmosphere lane and is modeled or expected to resolve as modeled.
- [ ] Confirm the correct source-family subfolder or create a documented source-lane README before adding payloads.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, authority, rights, sensitivity, cadence, citation, model-run identity, product identity, and hash posture.
- [ ] Confirm modeled material is not being cited as an observed sensor reading, single-station truth, regulatory archive, AQI concentration truth, measured PM2.5 reading, HMS observed smoke product, or emergency/life-safety instruction.
- [ ] Confirm model family, product, run/reference time, valid time, retrieval time, variable, level, units, grid/support, and caveats are recorded where material.
- [ ] Confirm AOD, smoke, or chemical fields are not transformed into concentration, health, hazard, or life-safety claims without governed downstream evidence and receipts.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the empty parent file at `data/raw/atmosphere/modeled/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `cams/README.md` and `hrrr-smoke/README.md` exist as confirmed child modeled RAW source-family lanes. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source registry doctrine lists HRRR-Smoke / NOAA smoke forecast and CAMS / ECMWF-family model fields as modeled sources. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source-role doctrine says modeled records require model-run reference and must not be published as observations. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere doctrine says AQI is not concentration, AOD is not PM2.5, model fields are not observations, and such collapses are denied at the trust membrane. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference, requires SourceDescriptor/RawCaptureReceipt, and is denied to public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual modeled Atmosphere RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, ModelRunReceipt wiring, validators, fixtures, CI checks, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, observation truth, model truth authority, AQI concentration truth, smoke-truth authority, emergency guidance, hazards event truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`cams/README.md`](cams/README.md)
- [`hrrr-smoke/README.md`](hrrr-smoke/README.md)
- [`../README.md`](../README.md)
- [`../administrative/README.md`](../administrative/README.md)
- [`../aggregate/README.md`](../aggregate/README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/atmosphere/README.md`](../../../quarantine/atmosphere/README.md)
- [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- [`../../../processed/atmosphere/aod/README.md`](../../../processed/atmosphere/aod/README.md)
- [`../../../processed/atmosphere/smoke_context/README.md`](../../../processed/atmosphere/smoke_context/README.md)
- [`../../../catalog/domain/atmosphere/README.md`](../../../catalog/domain/atmosphere/README.md)
- [`../../../published/layers/atmosphere/README.md`](../../../published/layers/atmosphere/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md`](../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md`](../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md`](../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
- [`../../../../docs/sources/catalog/noaa/hrrr-smoke.md`](../../../../docs/sources/catalog/noaa/hrrr-smoke.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is an Atmosphere modeled RAW source-role index only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, observation truth, model truth authority, AQI concentration truth, AOD-to-PM2.5 truth, smoke-truth authority, emergency guidance, hazards event truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
