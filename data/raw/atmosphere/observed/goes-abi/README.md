<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/observed/goes-abi/readme
title: GOES ABI Observed Raw Atmosphere README
path: data/raw/atmosphere/observed/goes-abi/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <atmosphere-source-steward>
  - <goes-abi-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked GOES ABI observed Atmosphere RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: atmosphere
source_role: observed
source_family: goes-abi
artifact_family: atmosphere-goes-abi-raw-compatibility-reference
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; sensor-capture-only; aod-retrieval-excluded; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../modeled/README.md
  - ../../modeled/cams/README.md
  - ../../modeled/hrrr-smoke/README.md
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
  - ../../../../../docs/sources/catalog/noaa/goes-abi-aod.md
  - ../../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../../../docs/architecture/source-roles.md
  - ../../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - observed
  - goes
  - abi
  - noaa
  - sensor-capture
  - radiance
  - source-role
  - no-public-path
  - evidence-first
  - compatibility-reference
  - source-first
notes:
  - "This README documents the requested GOES ABI Atmosphere RAW observed source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/observed/README.md` was an empty file when this lane was first authored; it now exists as a compatibility/reference index. This child file stays source-family-lane bounded."
  - "This lane documents references to upstream GOES ABI observed sensor/radiance-style source-first captures only (it does not hold them); GOES ABI AOD retrieval is modeled by default and is not observed surface truth."
  - "Payload presence, source descriptors, connector activation, validators, fixtures, CI enforcement, receipts, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GOES ABI Observed RAW Atmosphere Lane

Compatibility and reference documentation for Atmosphere-facing NOAA GOES Advanced Baseline Imager sensor/radiance-style RAW topology; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Source role: observed" src="https://img.shields.io/badge/source%20role-observed-228be6">
  <img alt="Source: GOES ABI" src="https://img.shields.io/badge/source-GOES--ABI-555">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [GOES ABI observed posture](#goes-abi-observed-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/atmosphere/observed/goes-abi/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named lane is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, AOD retrieval authority, PM2.5 authority, smoke-detection authority, public API/UI material, or release authority. Public clients and normal UI surfaces must not read this lane directly.

---

## Scope

This directory documents tracked Atmosphere-facing RAW topology for GOES ABI material whose source role is `observed`, or whose review is expected to resolve as `observed`. It may reference one governed source-first capture, but it does not hold that capture or establish where it is stored.

For this lane, `observed` means upstream sensor/radiance-style capture such as ABI source packets, radiance references, channel metadata, scan/time metadata, quality flags, source-head manifests, and digest sidecars.

A downstream AOD retrieval computed from ABI radiances is not an observed surface measurement. AOD retrieval material must stay under modeled/retrieval governance and must not be treated as PM2.5, smoke detection, or air-quality guidance.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/observed/goes-abi/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Parent source-role lane | `observed/` |
| Source family | `goes-abi` |
| Artifact role | Compatibility/reference lane for GOES ABI observed sensor/radiance source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Atmosphere WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when rights, source role, product identity, scan time, channel identity, quality flags, grid support, citation, validation, correction, rollback, or release support is insufficient |

---

## GOES ABI observed posture

| Source / knowledge character | Role handling | RAW rule |
|---|---|---|
| Capture identity is source-first | All roles and components | Register one `source_id` and preserve one immutable capture identity; domain references may support Atmosphere without duplicating RAW bytes. |
| Physical placement is held | All roles and components | Do not infer `data/raw/atmosphere/observed/goes-abi/` or a child directory as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| GOES ABI sensor/radiance capture | `observed` for upstream sensor/radiance-style material | Preserve satellite/platform, instrument, channel/band, scan time, acquisition time, grid support, quality flags, source reference, rights posture, digest, and caveats. |
| GOES ABI AOD retrieval | `modeled` by default, not observed | Route retrieval product material to modeled/retrieval governance; do not place retrieval authority or retrieval payloads in this observed lane. |
| AOD-to-PM workflow | Modeled or derived downstream workflow | Requires calibration, uncertainty, evidence, receipts, and policy closure. Fixed shortcuts fail closed. |
| GOES ABI plus aggregate rollup | **NEEDS REVIEW** | Split observed and aggregate support or quarantine until aggregation unit and source roles are explicit. |
| GOES ABI plus advisory/report payload | **NEEDS REVIEW** | Split observed and administrative/regulatory support or quarantine. Sensor capture is not advisory authority. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; like any README, it must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, retrieval, alert, or public authority.

The governed source-first capture or reference (not this subtree) must carry or point to the GOES ABI capture material below:

- source-reference manifests;
- GOES ABI sensor/radiance packet references, product references, or raw payload references;
- platform, instrument, channel, scan time, acquisition time, grid support, quality flags, source vintage, source reference, attribution, and digest sidecars;
- source-head records, response metadata, status codes, chunking/tile notes where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Atmosphere. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
| GOES ABI AOD product doctrine | `docs/sources/catalog/noaa/goes-abi-aod.md` |
| Atmosphere source-family doctrine | `docs/domains/atmosphere/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, or policy rules | `policy/` |
| Quarantine holds and remediation notes | `data/quarantine/atmosphere/` |
| Normalized working material | `data/work/atmosphere/` |
| Validated processed Atmosphere objects | `data/processed/atmosphere/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| AOD retrieval products, AOD rasters as PM2.5, observed smoke detections, measured PM2.5 readings, regulatory archives, low-cost sensor point truth, aggregate truth, or advisory authority | Owning source-role/product lane and downstream governed stages |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/observed/goes-abi/
└── README.md
```

This is the confirmed documentation topology, not a storage specification. The per-run layout previously sketched here (`<source_id_or_product_id>/<run_id_or_scan_time>/` holding `source_reference.json`, `sensor_capture_ref.json`, `channel_metadata.json`, `quality_flags.json`, `grid_support.json`, `checksums.sha256`, and a run `README.md`) is a proposed shape for a future accepted source-first home, not this subtree. Do not add a product or run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

An optional local documentation index, if ever accepted, would not be a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, retrieval authority, AOD authority, PM2.5 authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This lane may retain a governed reference only. |
| Quarantine | Rights, source role, product identity, scan/acquisition time, channel identity, quality flags, grid support, attribution, citation, digest, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Atmosphere WORK only when SourceDescriptor, rights posture, source role, product/channel support, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, quality-screen receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Atmosphere-scoped copy.
- [ ] Treat this source-named README as compatibility/reference documentation only; do not create a child directory as a payload destination.
- [ ] Confirm the source is GOES ABI observed sensor/radiance-style material; source-family classification does not make this lane a capture home.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, authority, rights, cadence, citation, product identity, channel identity, and hash posture.
- [ ] Confirm AOD retrieval products are not placed or cited here as observed sensor truth.
- [ ] Confirm GOES ABI material is not being cited as PM2.5 truth, AOD-to-concentration truth, smoke detection truth, regulatory archive, or advisory authority.
- [ ] Confirm platform, instrument, channel/band, scan/acquisition time, source time, grid support, quality flags, and caveats are recorded where material.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested GOES ABI Atmosphere observed RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/atmosphere/observed/README.md` was an empty file when this lane was first authored. | **CONFIRMED at original authoring; SUPERSEDED — parent README is present at `main@9e8bf3e6` and was reconciled as a compatibility/reference index on 2026-10-11** |
| GOES ABI AOD source-page doctrine says the AOD retrieval is modeled by default, while raw ABI radiance bands can be separate upstream observed material. | **CONFIRMED by GitHub contents API during this edit** |
| GOES ABI AOD source-page doctrine says AOD is not PM2.5 and is not direct observation of a surface property. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference, requires SourceDescriptor/RawCaptureReceipt, and is denied to public access. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual GOES ABI observed RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| SourceDescriptor records, connector activation, quality-screen receipts, validators, fixtures, CI checks, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| This README is proof, receipt, release, catalog, registry, policy, retrieval authority, AOD authority, PM2.5 authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../modeled/README.md`](../../modeled/README.md)
- [`../../modeled/cams/README.md`](../../modeled/cams/README.md)
- [`../../modeled/hrrr-smoke/README.md`](../../modeled/hrrr-smoke/README.md)
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
- [`../../../../../docs/sources/catalog/noaa/goes-abi-aod.md`](../../../../../docs/sources/catalog/noaa/goes-abi-aod.md)
- [`../../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md`](../../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md)
- [`../../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md`](../../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md)
- [`../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md`](../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
- [`../../../../../docs/architecture/source-roles.md`](../../../../../docs/architecture/source-roles.md)
- [`../../../../../release/manifests/README.md`](../../../../../release/manifests/README.md)

---

KFM rule: this directory is a GOES ABI Atmosphere-facing observed compatibility/reference lane. One governed source-first capture may support Atmosphere without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, proof authority, receipt authority, release authority, catalog authority, AOD retrieval authority, PM2.5 authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
