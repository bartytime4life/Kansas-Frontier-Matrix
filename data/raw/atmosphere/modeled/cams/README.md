<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/modeled/cams/readme
title: CAMS Modeled Raw Atmosphere README
path: data/raw/atmosphere/modeled/cams/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
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
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked CAMS modeled Atmosphere RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: atmosphere
source_role: modeled
source_family: cams
artifact_family: atmosphere-cams-raw-compatibility-reference
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
  - compatibility-reference
  - source-first
notes:
  - "This README documents the requested CAMS Atmosphere RAW modeled source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/modeled/README.md` was an empty file when this lane was first authored; it now exists as a compatibility/reference index. This child file stays source-family-lane bounded."
  - "CAMS-family modeled fields are source-first captures referenced (not held) by this compatibility lane; they are not observations, not AQI concentration truth, not sensor readings, not official emergency instructions, and not public KFM products."
  - "Source rights, current terms, payload presence, source descriptors, connector activation, model-run receipt wiring, validator wiring, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CAMS Modeled RAW Atmosphere Lane

Compatibility and reference documentation for Atmosphere-facing CAMS / ECMWF-family modeled fields and model-run-bound RAW topology; not a physical source-capture home.

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
> `data/raw/atmosphere/modeled/cams/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named lane is not a default physical capture home and must not receive duplicate RAW payloads. Material here is not public, not processed Atmosphere truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not observed sensor truth, not AQI concentration truth, not AOD-to-PM2.5 truth, not emergency alerting, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory documents tracked Atmosphere-facing RAW topology for CAMS / ECMWF-family model fields whose source role is `modeled`, or whose source-role review is expected to resolve as `modeled`. It may reference one governed source-first capture, but it does not hold that capture or establish where it is stored.

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
| Artifact role | Compatibility/reference lane for CAMS modeled source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Atmosphere WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
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
| Capture identity is source-first | All roles and components | Register one `source_id` and preserve one immutable capture identity; domain references may support Atmosphere without duplicating RAW bytes. |
| Physical placement is held | All roles and components | Do not infer `data/raw/atmosphere/modeled/cams/` or a child directory as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| CAMS / ECMWF-family model field | `modeled` | Preserve model family, product, run/reference time, valid time, variable, level, units, grid/support, source URL/reference, rights posture, digest, and caveats. |
| Forecast or analysis field | `modeled`; may carry forecast/advisory context only if separately sourced | Keep initialization/analysis time separate from valid time and retrieval time. Do not present as an observation. |
| Derived smoke/air-quality context from CAMS | `modeled` or `derived_fusion` depending on basis | Preserve source list, method notes, weights where available, model-run refs, caveats, and whether downstream use is public-safe. |
| CAMS plus observed station payload | **NEEDS REVIEW** | Split roles or quarantine. A modeled field cannot silently become an observed reading. |
| CAMS plus aggregate rollup | **NEEDS REVIEW** | Split modeled and aggregate support or quarantine until aggregation unit and source roles are explicit. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; like any README, it must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, observation, alert, or public authority.

The governed source-first capture or reference (not this subtree) must carry or point to the CAMS capture material below:

- source-reference manifests;
- CAMS model-run references, product references, or raw payload references;
- model-run metadata, variable lists, level lists, units, grid/support metadata, forecast/valid times, analysis/initialization times, retrieval time, source vintage, source URL/reference, attribution, and digest sidecars;
- source-head records, response metadata, status codes, chunking/tile notes where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Atmosphere. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. The per-run layout previously sketched here (`<product_id>/<run_id>/` holding `source_reference.json`, `model_run_ref.json`, `product_manifest.json`, `grid_support.json`, `checksums.sha256`, and a run `README.md`) is a proposed shape for a future accepted source-first home, not this subtree. Do not add a product or run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

An optional local documentation index, if ever accepted, would not be a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, observation index, model-truth authority, alerting source, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This lane may retain a governed reference only. |
| Quarantine | Rights, source role, model-run identity, product identity, valid time, variable/level/unit, grid/support, attribution, citation, digest, sensitivity, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Atmosphere WORK only when SourceDescriptor, rights posture, source role, model-run/product support, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, model-run receipt where required, correction path, rollback target, and release manifest where applicable. |

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
- [ ] Confirm the source is CAMS / ECMWF-family modeled material; source-family classification does not make this lane a capture home.
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
| Parent `data/raw/atmosphere/modeled/README.md` was an empty file when this lane was first authored. | **CONFIRMED at original authoring; SUPERSEDED — parent README is present at `main@9e8bf3e6` and was reconciled as a compatibility/reference index on 2026-10-11** |
| Atmosphere source registry doctrine lists CAMS / ECMWF-family model fields as modeled and terms NEEDS VERIFICATION. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source-role doctrine says modeled records require model-run reference and must not be published as observations. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere doctrine says AQI is not concentration, AOD is not PM2.5, model fields are not observations, and such collapses are denied at the trust membrane. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference, requires SourceDescriptor/RawCaptureReceipt, and is denied to public access. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual CAMS RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| SourceDescriptor records, connector activation, model-run receipts, validators, fixtures, CI checks, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
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

KFM rule: this directory is a CAMS Atmosphere-facing modeled compatibility/reference lane. One governed source-first capture may support Atmosphere without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, observation truth, model truth authority, AQI concentration truth, AOD-to-PM2.5 truth, emergency guidance, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
