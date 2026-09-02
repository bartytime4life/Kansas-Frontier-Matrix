<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/observed/goes-abi/readme
name: GOES ABI Observed Raw Atmosphere README
path: data/raw/atmosphere/observed/goes-abi/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <atmosphere-source-steward>
  - <goes-abi-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: atmosphere
source_role: observed
source_family: goes-abi
artifact_family: immutable-goes-abi-sensor-source-capture
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
notes:
  - "This README documents the requested GOES ABI Atmosphere RAW observed source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/observed/README.md` is currently an empty file, so this child file stays source-family-lane bounded."
  - "This lane is for upstream GOES ABI observed sensor/radiance-style capture only; GOES ABI AOD retrieval is modeled by default and is not observed surface truth."
  - "Payload presence, source descriptors, connector activation, validators, fixtures, CI enforcement, receipts, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GOES ABI Observed RAW Atmosphere Lane

Source-family RAW lane for immutable NOAA GOES Advanced Baseline Imager sensor/radiance-style captures and source-admission sidecars.

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
> `data/raw/atmosphere/observed/goes-abi/` is a no-public-path RAW source capture lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, AOD retrieval authority, PM2.5 authority, smoke-detection authority, public API/UI material, or release authority. Public clients and normal UI surfaces must not read this lane directly.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for GOES ABI material whose source role is `observed`, or whose review is expected to resolve as `observed`.

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
| Artifact role | RAW source-family lane for GOES ABI observed sensor/radiance captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/atmosphere/` or `data/quarantine/atmosphere/` after governed admission/triage |
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
| GOES ABI sensor/radiance capture | `observed` for upstream sensor/radiance-style material | Preserve satellite/platform, instrument, channel/band, scan time, acquisition time, grid support, quality flags, source reference, rights posture, digest, and caveats. |
| GOES ABI AOD retrieval | `modeled` by default, not observed | Route retrieval product material to modeled/retrieval governance; do not place retrieval authority in this observed lane. |
| AOD-to-PM workflow | Modeled or derived downstream workflow | Requires calibration, uncertainty, evidence, receipts, and policy closure. Fixed shortcuts fail closed. |
| GOES ABI plus aggregate rollup | **NEEDS REVIEW** | Split observed and aggregate support or quarantine until aggregation unit and source roles are explicit. |
| GOES ABI plus advisory/report payload | **NEEDS REVIEW** | Split observed and administrative/regulatory support or quarantine. Sensor capture is not advisory authority. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- GOES ABI sensor/radiance packet references, product references, or raw payload references;
- platform, instrument, channel, scan time, acquisition time, grid support, quality flags, source vintage, source reference, attribution, and digest sidecars;
- source-head records, response metadata, status codes, chunking/tile notes where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, retrieval, alert, or public authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
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
├── README.md
├── <source_id_or_product_id>/
│   └── <run_id_or_scan_time>/
│       ├── source_reference.json
│       ├── sensor_capture_ref.json
│       ├── channel_metadata.json
│       ├── quality_flags.json
│       ├── grid_support.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, retrieval authority, AOD authority, PM2.5 authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Rights, source role, product identity, scan/acquisition time, channel identity, quality flags, grid support, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, product/channel support, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, quality-screen receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/atmosphere/observed/goes-abi/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Atmosphere lane and is GOES ABI observed sensor/radiance-style material.
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
| Parent `data/raw/atmosphere/observed/README.md` is currently an empty file. | **CONFIRMED by GitHub contents API during this edit** |
| GOES ABI AOD source-page doctrine says the AOD retrieval is modeled by default, while raw ABI radiance bands can be separate upstream observed material. | **CONFIRMED by GitHub contents API during this edit** |
| GOES ABI AOD source-page doctrine says AOD is not PM2.5 and is not direct observation of a surface property. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference, requires SourceDescriptor/RawCaptureReceipt, and is denied to public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual GOES ABI observed RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, quality-screen receipts, validators, fixtures, CI checks, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
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

KFM rule: this directory is a GOES ABI observed RAW source-family lane only. It is not source-family doctrine, source registry authority, rights authority, proof authority, receipt authority, release authority, catalog authority, AOD retrieval authority, PM2.5 authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
