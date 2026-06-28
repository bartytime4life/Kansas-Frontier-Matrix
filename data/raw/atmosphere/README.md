<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/readme
name: Atmosphere Raw README
path: data/raw/atmosphere/README.md
type: data-raw-domain-index-readme
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
artifact_family: immutable-atmosphere-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; rights-needs-verification; release-blocked
related:
  - administrative/README.md
  - aggregate/README.md
  - modeled/README.md
  - observed/README.md
  - ../README.md
  - ../../README.md
  - ../../quarantine/atmosphere/README.md
  - ../../processed/atmosphere/README.md
  - ../../catalog/domain/atmosphere/README.md
  - ../../published/layers/atmosphere/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../docs/architecture/source-roles.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - source-role
  - source-capture
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/atmosphere/README.md`."
  - "Confirmed child source-role README lanes during this edit: `administrative/`, `aggregate/`, `modeled/`, and `observed/`."
  - "Atmosphere RAW records remain source captures until governed downstream lifecycle transitions close."
  - "Payload presence, source descriptors, connector activation, receipts, validators, fixtures, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere RAW

Parent RAW lifecycle index for immutable Atmosphere source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source-role lanes](#confirmed-source-role-lanes) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/atmosphere/` is a no-public-path RAW lifecycle lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, public API/UI material, release authority, or generated-answer authority. Public clients and normal UI surfaces must not read this lane directly.

---

## Scope

This directory indexes immutable RAW source captures and source-admission sidecars for the Atmosphere domain.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what role it was admitted under, and which identifiers, times, rights, citations, hashes, and caveats must travel with it.

RAW does not decide what a source means, whether rights permit reuse, whether a record can publish, whether a value is valid, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Artifact role | Parent RAW domain index for Atmosphere source captures and RAW-local sidecars |
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

## Confirmed source-role lanes

The child lanes below are README paths confirmed by current-session GitHub fetches/edits. This table confirms README presence only; it does **not** prove payloads, source descriptors, connectors, validators, fixtures, receipts, CI checks, or release readiness exist.

| Source-role lane | Status | Boundary summary |
|---|---|---|
| [`administrative/`](administrative/README.md) | **CONFIRMED README** | Administrative and advisory-context source capture. Administrative records must not become observations or model fields by convenience. |
| [`aggregate/`](aggregate/README.md) | **CONFIRMED README** | Aggregate records, rollups, normals, and summary captures. Aggregation unit must remain visible and cannot be joined back to a single record as if observed. |
| [`modeled/`](modeled/README.md) | **CONFIRMED README** | Modeled fields, forecasts, retrieval-like model products, and model-run-bound captures. Model fields are not observations. |
| [`observed/`](observed/README.md) | **CONFIRMED README** | Observed source records and source packets. Observed does not mean published, and mixed packages must split or hold. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, modeled, aggregate, administrative, regulatory, candidate, and interpretation outputs must not be flattened. |
| Time fields stay explicit | Issue time, expiry time, observed time, valid time, model run time, retrieval time, and release time must not collapse. |
| Rights and citations travel with the source | SourceDescriptor, citation, rights posture, cadence, sensitivity, and digest closure are required before downstream use. |
| Public use requires governed release | Public layers, reports, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- role, source identity, time, version, quality, geometry/support, citation, rights, attribution, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Product and source-family doctrine | `docs/sources/catalog/` |
| Atmosphere domain doctrine | `docs/domains/atmosphere/` |
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
| Public-output authority or generated-answer authority | Governed published/API/evidence surfaces only |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/
├── README.md
├── administrative/
│   └── README.md
├── aggregate/
│   └── README.md
├── modeled/
│   ├── README.md
│   ├── cams/
│   │   └── README.md
│   └── hrrr-smoke/
│       └── README.md
├── observed/
│   ├── README.md
│   ├── goes-abi/
│   │   └── README.md
│   ├── hms/
│   │   └── README.md
│   └── viirs/
│       └── README.md
├── <future-source-role-or-source-family>/
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
data/raw/atmosphere/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Atmosphere lane.
- [ ] Confirm the correct source-role or source-family subfolder or create a documented README before adding payloads.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, rights, cadence, citation, status, and hash posture.
- [ ] Confirm observed, modeled, aggregate, administrative, regulatory, candidate, and interpretation outputs are not collapsed into one source role.
- [ ] Confirm source identity, source time, retrieval time, valid time where applicable, version, quality fields, geometry/support, and caveats are recorded where material.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/atmosphere/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `administrative/README.md`, `aggregate/README.md`, `modeled/README.md`, and `observed/README.md` exist as confirmed child source-role lanes. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, downstream receipts, or release readiness. | **DENY** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, and public access is denied. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source registry doctrine says source-role collapses such as AQI-as-concentration, AOD-as-PM2.5, and model-fields-as-observations are denied. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Atmosphere RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`administrative/README.md`](administrative/README.md)
- [`aggregate/README.md`](aggregate/README.md)
- [`modeled/README.md`](modeled/README.md)
- [`observed/README.md`](observed/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/atmosphere/README.md`](../../quarantine/atmosphere/README.md)
- [`../../processed/atmosphere/README.md`](../../processed/atmosphere/README.md)
- [`../../catalog/domain/atmosphere/README.md`](../../catalog/domain/atmosphere/README.md)
- [`../../published/layers/atmosphere/README.md`](../../published/layers/atmosphere/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/atmosphere/SOURCE_REGISTRY.md`](../../../docs/domains/atmosphere/SOURCE_REGISTRY.md)
- [`../../../docs/domains/atmosphere/DATA_LIFECYCLE.md`](../../../docs/domains/atmosphere/DATA_LIFECYCLE.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is an Atmosphere RAW domain index for source capture only. It is not source-family doctrine, source registry authority, rights authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
