<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/modeled/cams/readme
name: CAMS Modeled Raw Atmosphere README
path: data/raw/atmosphere/modeled/cams/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <atmosphere-source-steward>
  - <cams-source-steward>
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
source_family: cams
artifact_family: immutable-cams-model-run-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; model-run-required; not-observation; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../administrative/README.md
  - ../../aggregate/README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../quarantine/atmosphere/README.md
  - ../../../../processed/atmosphere/README.md
  - ../../../../processed/atmosphere/aod/README.md
  - ../../../../catalog/domain/atmosphere/README.md
  - ../../../../published/layers/atmosphere/README.md
  - ../../../../registry/sources/README.md
  - ../../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../../../docs/domains/atmosphere/API_CONTRACTS.md
  - ../../../../../docs/architecture/source-roles.md
  - ../../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - modeled
  - cams
  - ecmwf-family
  - model-run
  - model-field
  - not-observation
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested CAMS Atmosphere RAW modeled source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/modeled/README.md` is currently an empty file, so this child file stays source-family-lane bounded."
  - "CAMS-family modeled fields are source captures, not observations, not AQI concentration truth, not sensor readings, not official emergency instructions, and not public KFM products."
  - "Source rights, current terms, payload presence, source descriptors, connector activation, model-run receipt wiring, validator wiring, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CAMS Modeled RAW Atmosphere Lane

Source-family RAW lane for immutable CAMS / ECMWF-family modeled Atmosphere fields and model-run-bound captures.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Source role: modeled" src="https://img.shields.io/badge/source%20role-modeled-7048e8">
  <img alt="Source: CAMS" src="https://img.shields.io/badge/source-CAMS-555">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [CAMS modeled posture](#cams-modeled-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/atmosphere/modeled/cams/` is a RAW source-family capture lane. Material here is not public, not processed Atmosphere truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not observed sensor truth, not AQI concentration truth, not AOD-to-PM2.5 truth, not emergency alerting, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for CAMS / ECMWF-family Atmosphere model fields whose source role is `modeled`, or whose source-role review is expected to resolve as `modeled`.

Typical material includes model-run references, model field payload references, product metadata, variable/level/time-slice manifests, issue/retrieval metadata, grid/support metadata, source vintage notes, and digest sidecars. The model run, model family, product name, initialization or analysis time, forecast/valid time, variable, level, units, grid, processing basis, and retrieval time must remain inspectable.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a record may publish, whether a model is reliable, whether an observation occurred, whether PM2.5 exists at a point, whether AOD or smoke implies concentration, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/modeled/cams/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Parent source-role lane | `modeled/` |
| Source family | `cams` |
| Artifact role | RAW source-family lane for CAMS modeled captures and RAW-local sidecars |
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

## CAMS modeled posture

| Source / knowledge character | Role handling | RAW rule |
|---|---|---|
| CAMS / ECMWF-family model field | `modeled` | Preserve model family, product, run/reference time, valid time, variable, level, units, grid/support, source URL/reference, rights posture, digest, and caveats. |
| Forecast or analysis field | `modeled`; may carry forecast/advisory context only if separately sourced | Keep initialization/analysis time separate from valid time and retrieval time. Do not present as an observation. |
| Derived smoke/air-quality context from CAMS | `modeled` or `derived_fusion` depending on basis | Preserve source list, method notes, weights where available, model-run refs, caveats, and whether downstream use is public-safe. |
| CAMS plus observed station payload | **NEEDS REVIEW** | Split roles or quarantine. A modeled field cannot silently become an observed reading. |
| CAMS plus aggregate rollup | **NEEDS REVIEW** | Split modeled and aggregate support or quarantine until aggregation unit and source roles are explicit. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- CAMS model-run references, product references, or raw payload references;
- model-run metadata, variable lists, level lists, units, grid/support metadata, forecast/valid times, analysis/initialization times, retrieval time, source vintage, source URL/reference, attribution, and digest sidecars;
- source-head records, response metadata, status codes, chunking/tile notes where applicable, and checksums;
- minimal README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, observation, alert, or public authority.

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
| Ingest, validation, aggregation, redaction, source-role, model-run, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Observed sensor readings, regulatory archives, AQI reports as concentrations, AOD rasters as PM2.5, low-cost sensor point truth, or aggregate truth | Owning source-role/product lane and downstream governed stages; never this CAMS RAW lane by itself |
| Emergency alerting, life-safety instructions, evacuation/routing advice, or authoritative health guidance | External official authorities, not KFM RAW data |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/modeled/cams/
├── README.md
├── <product_id>/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── model_run_ref.json
│       ├── product_manifest.json
│       ├── grid_support.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, observation index, model-truth authority, alerting source, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Rights, source role, model-run identity, product identity, valid time, variable/level/unit, grid/support, attribution, citation, digest, sensitivity, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, model-run/product support, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, model-run receipt where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
data/raw/atmosphere/modeled/cams/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Atmosphere lane and is CAMS / ECMWF-family modeled material.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, authority, rights, sensitivity, cadence, citation, model-run identity, product identity, and hash posture.
- [ ] Confirm modeled material is not being cited as an observed sensor reading, single-station truth, regulatory archive, AQI concentration truth, or emergency/life-safety instruction.
- [ ] Confirm model family, product, run/reference time, valid time, retrieval time, variable, level, units, grid/support, and caveats are recorded where material.
- [ ] Confirm AOD, smoke, or chemical fields are not transformed into concentration or health claims without governed downstream evidence and receipts.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested CAMS Atmosphere modeled RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/atmosphere/modeled/README.md` is currently an empty file. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source registry doctrine lists CAMS / ECMWF-family model fields as modeled and terms NEEDS VERIFICATION. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source-role doctrine says modeled records require model-run reference and must not be published as observations. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere doctrine says AQI is not concentration, AOD is not PM2.5, model fields are not observations, and such collapses are denied at the trust membrane. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference, requires SourceDescriptor/RawCaptureReceipt, and is denied to public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual CAMS RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, model-run receipts, validators, fixtures, CI checks, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, observation truth, model truth authority, AQI concentration truth, emergency guidance, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../administrative/README.md`](../../administrative/README.md)
- [`../../aggregate/README.md`](../../aggregate/README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../../README.md`](../../../../README.md)
- [`../../../../quarantine/atmosphere/README.md`](../../../../quarantine/atmosphere/README.md)
- [`../../../../processed/atmosphere/README.md`](../../../../processed/atmosphere/README.md)
- [`../../../../processed/atmosphere/aod/README.md`](../../../../processed/atmosphere/aod/README.md)
- [`../../../../catalog/domain/atmosphere/README.md`](../../../../catalog/domain/atmosphere/README.md)
- [`../../../../published/layers/atmosphere/README.md`](../../../../published/layers/atmosphere/README.md)
- [`../../../../registry/sources/README.md`](../../../../registry/sources/README.md)
- [`../../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md`](../../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md)
- [`../../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md`](../../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md)
- [`../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md`](../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
- [`../../../../../docs/domains/atmosphere/API_CONTRACTS.md`](../../../../../docs/domains/atmosphere/API_CONTRACTS.md)
- [`../../../../../docs/architecture/source-roles.md`](../../../../../docs/architecture/source-roles.md)
- [`../../../../../release/manifests/README.md`](../../../../../release/manifests/README.md)

---

KFM rule: this directory is a CAMS Atmosphere modeled RAW source-family lane only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, observation truth, model truth authority, AQI concentration truth, AOD-to-PM2.5 truth, emergency guidance, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
