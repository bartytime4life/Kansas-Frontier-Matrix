<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/observed/readme
name: Atmosphere Observed Raw README
path: data/raw/atmosphere/observed/README.md
type: data-raw-source-role-index-readme
version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <atmosphere-source-steward>
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
artifact_family: immutable-atmosphere-observed-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; product-role-split-required; rights-needs-verification; release-blocked
related:
  - goes-abi/README.md
  - hms/README.md
  - viirs/README.md
  - ../README.md
  - ../administrative/README.md
  - ../aggregate/README.md
  - ../modeled/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../published/layers/atmosphere/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/sources/catalog/noaa/goes-abi-aod.md
  - ../../../../docs/sources/catalog/noaa/hms-fire-smoke.md
  - ../../../../docs/sources/catalog/noaa/viirs-hotspot.md
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - observed
  - source-role
  - source-capture
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the empty parent `data/raw/atmosphere/observed/README.md` file and documents the Atmosphere observed RAW source-role index."
  - "Confirmed child README lanes during this edit: `goes-abi/`, `hms/`, and `viirs/`."
  - "Observed Atmosphere source records remain source captures until governed downstream lifecycle transitions close."
  - "Payload presence, source descriptors, connector activation, receipts, validators, fixtures, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Observed RAW

Parent RAW source-role index for immutable observed Atmosphere source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Source role: observed" src="https://img.shields.io/badge/source%20role-observed-228be6">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Observed source posture](#observed-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/atmosphere/observed/` is a no-public-path RAW source-role index. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, public API/UI material, release authority, or generated-answer authority. Public clients and normal UI surfaces must not read this lane directly.

---

## Scope

This directory indexes Atmosphere RAW material whose source role is `observed`, or whose source-role review is expected to resolve as observed after admission.

Observed material records a source event, reading, packet, or source record and its metadata. It does not automatically become downstream interpretation, public context, release truth, or an answerable claim.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a record may publish, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/observed/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Source role | `observed` |
| Artifact role | Parent RAW source-role index for observed Atmosphere captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/atmosphere/` or `data/quarantine/atmosphere/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, provenance, time, geometry/support, citation, validation, correction, rollback, or release support is insufficient |

---

## Confirmed child lanes

The child lanes below are README paths confirmed by current-session GitHub fetches/edits. This table confirms README presence only; it does **not** prove payloads, source descriptors, connectors, validators, fixtures, receipts, CI checks, or release readiness exist.

| Child lane | Status | Boundary summary |
|---|---|---|
| [`goes-abi/`](goes-abi/README.md) | **CONFIRMED README** | Upstream GOES ABI sensor/radiance-style source capture. AOD retrieval authority stays out of this observed lane. |
| [`hms/`](hms/README.md) | **CONFIRMED README** | HMS observed-component source capture. Mixed components require role-split review before downstream use. |
| [`viirs/`](viirs/README.md) | **CONFIRMED README** | VIIRS observed source capture. Source record, platform/time/version/quality metadata, and review state remain inspectable. |

---

## Observed source posture

| Rule | Handling |
|---|---|
| Observed does not mean published | RAW observed material stays internal until downstream lifecycle gates close. |
| Source role is preserved | Observed, modeled, aggregate, administrative, regulatory, candidate, and interpretation outputs must not be flattened. |
| Metadata is part of evidence | Platform/source identity, source time, retrieval time, version, quality fields, geometry/support, citation, and digest stay inspectable. |
| Mixed packages split or hold | If one upstream delivery contains multiple component roles, split it into governed lanes or quarantine it. |
| Public use requires release | Public layers, stories, reports, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- observed source-record references or raw payload references;
- source identity, platform/instrument/source metadata, source time, retrieval time, version, quality fields, source reference, attribution, and digest sidecars;
- geometry/support references, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Product and source-family doctrine | `docs/sources/catalog/` |
| Domain doctrine | `docs/domains/atmosphere/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, or policy rules | `policy/` |
| Quarantine holds and remediation notes | `data/quarantine/atmosphere/` |
| Normalized working material | `data/work/atmosphere/` |
| Validated processed objects | `data/processed/atmosphere/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Modeled, aggregate, administrative, regulatory, candidate, interpretation, or public-output authority | Owning source-role/product lane and downstream governed stages |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/observed/
├── README.md
├── goes-abi/
│   └── README.md
├── hms/
│   └── README.md
├── viirs/
│   └── README.md
├── <future-observed-source-family>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, component split, rights, provenance, source time, geometry/support, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/atmosphere/observed/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Atmosphere lane and is observed or expected to resolve as observed.
- [ ] Confirm the correct source-family subfolder or create a documented source-lane README before adding payloads.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, rights, cadence, citation, status, and hash posture.
- [ ] Confirm observed, modeled, aggregate, administrative, regulatory, candidate, and interpretation outputs are not collapsed into one source role.
- [ ] Confirm source identity, source time, retrieval time, version, quality fields, geometry/support, and caveats are recorded where material.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the empty parent file at `data/raw/atmosphere/observed/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `goes-abi/README.md`, `hms/README.md`, and `viirs/README.md` exist as confirmed child observed RAW source-family lanes. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, downstream receipts, or release readiness. | **DENY** |
| Actual observed Atmosphere RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`goes-abi/README.md`](goes-abi/README.md)
- [`hms/README.md`](hms/README.md)
- [`viirs/README.md`](viirs/README.md)
- [`../README.md`](../README.md)
- [`../administrative/README.md`](../administrative/README.md)
- [`../aggregate/README.md`](../aggregate/README.md)
- [`../modeled/README.md`](../modeled/README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/atmosphere/README.md`](../../../quarantine/atmosphere/README.md)
- [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- [`../../../catalog/domain/atmosphere/README.md`](../../../catalog/domain/atmosphere/README.md)
- [`../../../published/layers/atmosphere/README.md`](../../../published/layers/atmosphere/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/sources/catalog/noaa/goes-abi-aod.md`](../../../../docs/sources/catalog/noaa/goes-abi-aod.md)
- [`../../../../docs/sources/catalog/noaa/hms-fire-smoke.md`](../../../../docs/sources/catalog/noaa/hms-fire-smoke.md)
- [`../../../../docs/sources/catalog/noaa/viirs-hotspot.md`](../../../../docs/sources/catalog/noaa/viirs-hotspot.md)
- [`../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md`](../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md`](../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is an Atmosphere observed RAW source-role index for source capture only. It is not source-family doctrine, source registry authority, rights authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
