<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/observed/readme
title: Atmosphere Observed Raw README
path: data/raw/atmosphere/observed/README.md
type: data-raw-source-role-index-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <atmosphere-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Atmosphere observed RAW compatibility and reference index without treating this subtree or its source-named children as physical source-first capture homes or duplicating RAW bytes.
domain: atmosphere
source_role: observed
artifact_family: atmosphere-observed-raw-compatibility-reference-index
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
  - compatibility-reference
  - source-first
notes:
  - "This README replaces the empty parent `data/raw/atmosphere/observed/README.md` file and documents the Atmosphere observed RAW source-role index."
  - "Confirmed child README lanes during this edit: `goes-abi/`, `hms/`, and `viirs/`."
  - "Observed Atmosphere source records remain source captures at their source-first RAW home (not this compatibility index) until governed downstream lifecycle transitions close."
  - "Payload presence, source descriptors, connector activation, receipts, validators, fixtures, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Observed RAW

Compatibility and reference index for Atmosphere-facing observed RAW documentation; not a physical source-capture home.

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
> `data/raw/atmosphere/observed/` is a no-public-path compatibility/reference index inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-role index and its source-named children are not a default physical capture home and must not receive duplicate RAW payloads. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, public API/UI material, release authority, or generated-answer authority. Public clients and normal UI surfaces must not read this lane directly.

---

## Scope

This directory indexes tracked documentation and legacy domain-scoped RAW topology for Atmosphere material whose source role is `observed`, or whose source-role review is expected to resolve as observed after admission. It may reference one governed source-first capture, but it does not establish where that capture is stored.

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
| Artifact role | Compatibility/reference index for observed Atmosphere source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Atmosphere WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, provenance, time, geometry/support, citation, validation, correction, rollback, or release support is insufficient |

---

## Confirmed child lanes

The child lanes below are README paths confirmed by current-session GitHub fetches/edits. Treat them as compatibility/reference documentation or unresolved legacy topology, not source-first capture homes. This table confirms README presence only; it does **not** prove or authorize payloads, source descriptors, connectors, validators, fixtures, receipts, CI checks, migration, or release readiness.

| Child lane | Status | Boundary summary |
|---|---|---|
| [`goes-abi/`](goes-abi/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Upstream GOES ABI sensor/radiance-style source documentation; not a capture home. AOD retrieval authority stays out of this observed lane. |
| [`hms/`](hms/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | HMS observed-component source documentation; not a capture home. Mixed components require role-split review before downstream use. |
| [`viirs/`](viirs/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | VIIRS observed source documentation; not a capture home. Source record, platform/time/version/quality metadata, and review state remain inspectable. |

---

## Observed source posture

| Rule | Handling |
|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; domain references may support Atmosphere without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/atmosphere/observed/` or a source-named child directory as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| Observed does not mean published | Observed material at the source-first RAW home stays internal until downstream lifecycle gates close. |
| Source role is preserved | Observed, modeled, aggregate, administrative, regulatory, candidate, and interpretation outputs must not be flattened. |
| Metadata is part of evidence | Platform/source identity, source time, retrieval time, version, quality fields, geometry/support, citation, and digest stay inspectable. |
| Mixed packages split or hold | If one upstream delivery contains multiple component roles, split it through governed role review (without copying RAW bytes into several domain lanes) or quarantine it. |
| Public use requires release | Public layers, stories, reports, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README and the tracked child README files listed below;
- links to canonical SourceDescriptor, source-admission, rights, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; like any README, it must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

The governed source-first capture or reference (not this subtree) must carry or point to the observed capture material below:

- source-reference manifests;
- observed source-record references or raw payload references;
- source identity, platform/instrument/source metadata, source time, retrieval time, version, quality fields, source reference, attribution, and digest sidecars;
- geometry/support references, row counts where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Atmosphere. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── viirs/
    └── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a future observed source-family directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

An optional local documentation index, if ever accepted, would not be a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This index may retain a governed reference only. |
| Quarantine | Source role, component split, rights, provenance, source time, geometry/support, attribution, citation, digest, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Atmosphere WORK only when SourceDescriptor, rights posture, source role, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, correction path, rollback target, and release manifest where applicable. |

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
- [ ] Treat this README and any source-named child README as compatibility/reference documentation only; do not create a child directory as a payload destination.
- [ ] Confirm the source role is observed or expected to resolve as observed; role classification does not make this index or a child a capture home.
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
| `goes-abi/README.md`, `hms/README.md`, and `viirs/README.md` exist as child observed compatibility/reference documents. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, downstream receipts, or release readiness. | **DENY** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual observed Atmosphere RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
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

KFM rule: this directory is an Atmosphere-facing observed compatibility/reference index. One governed source-first capture may support Atmosphere without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
