<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/observed/hms/readme
name: HMS Observed Raw Atmosphere README
path: data/raw/atmosphere/observed/hms/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <hms-source-steward>
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
source_family: hms
artifact_family: immutable-hms-observed-component-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; multi-component-split-required; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../goes-abi/README.md
  - ../../README.md
  - ../../modeled/README.md
  - ../../administrative/README.md
  - ../../aggregate/README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../quarantine/atmosphere/README.md
  - ../../../../processed/atmosphere/README.md
  - ../../../../catalog/domain/atmosphere/README.md
  - ../../../../published/layers/atmosphere/README.md
  - ../../../../registry/sources/README.md
  - ../../../../../docs/sources/catalog/noaa/hms-fire-smoke.md
  - ../../../../../docs/architecture/source-roles.md
  - ../../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - observed
  - hms
  - noaa
  - analyst-augmented
  - multi-component
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested HMS Atmosphere RAW observed source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/observed/README.md` is currently an empty file, so this child file stays source-family-lane bounded."
  - "HMS is multi-component; components must be split by source role before downstream use."
  - "Payload presence, source descriptors, connector activation, receipts, validators, fixtures, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# HMS Observed RAW Atmosphere Lane

RAW source-family lane for HMS observed-component source capture and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Source role: observed component" src="https://img.shields.io/badge/source%20role-observed%20component-228be6">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Component posture](#component-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/atmosphere/observed/hms/` is a no-public-path RAW source capture lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for HMS material whose component role is `observed`, or whose component role still needs review before downstream normalization.

HMS is a multi-component source. KFM must keep observed, modeled, aggregate, and candidate components separate instead of admitting the whole feed as one truth type.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a record may publish, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/observed/hms/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Parent source-role lane | `observed/` |
| Source family | `hms` |
| Artifact role | RAW source-family lane for HMS observed-component captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/atmosphere/` or `data/quarantine/atmosphere/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, component split, rights, provenance, time, geometry, citation, validation, correction, rollback, or release support is insufficient |

---

## Component posture

| Component condition | RAW handling |
|---|---|
| Observed component is identified | May use this lane with source-role support. |
| Modeled or interpretive component is present | Split to modeled governance or quarantine. |
| Aggregate derivative is present | Split to aggregate governance or quarantine. |
| Mixed package is present | Preserve source reference and route to role-split review. |
| Review metadata is exposed by the source | Preserve it without inventing unavailable internal details. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- HMS observed-component references or raw payload references;
- component-split notes, issue time, retrieval time, source vintage, source reference, attribution, and digest sidecars;
- geometry/source packet references, quality notes, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, or public authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| HMS product doctrine | `docs/sources/catalog/noaa/hms-fire-smoke.md` |
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
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Modeled, aggregate, candidate, or public-output authority | Owning source-role/product lane and downstream governed stages |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/observed/hms/
├── README.md
├── <source_id_or_product_id>/
│   └── <issue_or_retrieval_id>/
│       ├── source_reference.json
│       ├── hms_component_split.json
│       ├── observed_component_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, component split, rights, provenance, time, geometry, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, component split, rights posture, source role, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/atmosphere/observed/hms/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to HMS and the Atmosphere lane.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, rights, cadence, citation, component split, and hash posture.
- [ ] Confirm observed, modeled, aggregate, and candidate components are not collapsed into one source role.
- [ ] Confirm review metadata is recorded where exposed, without inventing internal details.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested HMS Atmosphere observed RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/atmosphere/observed/README.md` is currently an empty file. | **CONFIRMED by GitHub contents API during this edit** |
| HMS source-page doctrine says HMS is multi-component and must not be admitted under a single source role. | **CONFIRMED by GitHub contents API during this edit** |
| HMS source-page doctrine says analyst augmentation carries a provenance burden and should not fabricate internal analyst details. | **CONFIRMED by GitHub contents API during this edit** |
| Actual HMS observed RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../goes-abi/README.md`](../goes-abi/README.md)
- [`../../README.md`](../../README.md)
- [`../../modeled/README.md`](../../modeled/README.md)
- [`../../administrative/README.md`](../../administrative/README.md)
- [`../../aggregate/README.md`](../../aggregate/README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../../README.md`](../../../../README.md)
- [`../../../../quarantine/atmosphere/README.md`](../../../../quarantine/atmosphere/README.md)
- [`../../../../processed/atmosphere/README.md`](../../../../processed/atmosphere/README.md)
- [`../../../../catalog/domain/atmosphere/README.md`](../../../../catalog/domain/atmosphere/README.md)
- [`../../../../published/layers/atmosphere/README.md`](../../../../published/layers/atmosphere/README.md)
- [`../../../../registry/sources/README.md`](../../../../registry/sources/README.md)
- [`../../../../../docs/sources/catalog/noaa/hms-fire-smoke.md`](../../../../../docs/sources/catalog/noaa/hms-fire-smoke.md)
- [`../../../../../docs/architecture/source-roles.md`](../../../../../docs/architecture/source-roles.md)
- [`../../../../../release/manifests/README.md`](../../../../../release/manifests/README.md)

---

KFM rule: this directory is an HMS observed RAW source-family lane for role-split source capture only. It is not source-family doctrine, source registry authority, rights authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
