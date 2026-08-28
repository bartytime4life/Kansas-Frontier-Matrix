<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/atmosphere/administrative/readme
name: Atmosphere Administrative Raw README
path: data/raw/atmosphere/administrative/README.md
type: data-raw-source-role-lane-readme
version: v0.1.0
status: draft
owners:
  - <atmosphere-domain-steward>
  - <atmosphere-source-steward>
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
source_role: administrative
artifact_family: immutable-atmosphere-administrative-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; advisory-not-life-safety; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../processed/atmosphere/air_observations/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../published/layers/atmosphere/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../../docs/domains/atmosphere/API_CONTRACTS.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - atmosphere
  - administrative
  - advisory-context
  - source-role
  - no-public-path
  - not-life-safety
  - evidence-first
notes:
  - "This README documents the requested Atmosphere RAW administrative source-role lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/atmosphere/README.md` is currently a greenfield stub, so this child file stays source-role-lane bounded."
  - "Administrative Atmosphere records are source captures, not observations, not model fields, not AQI concentration truth, not official emergency instructions, and not public KFM products."
  - "Source rights, current terms, payload presence, source descriptors, connector activation, validator wiring, CI enforcement, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Administrative RAW Lane

Source-role RAW lane for immutable Atmosphere administrative records and advisory-context captures.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Source role: administrative" src="https://img.shields.io/badge/source%20role-administrative-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Administrative source posture](#administrative-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/atmosphere/administrative/` is a RAW source-role capture lane. Material here is not public, not processed Atmosphere truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not observed sensor truth, not model truth, not AQI concentration truth, not official life-safety instruction, not emergency alerting, not public API/UI material, and not release authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for Atmosphere material whose source role is administrative, or whose source-role review is expected to resolve as administrative.

Typical administrative Atmosphere material includes agency bulletin captures, advisory-context records, state-issued context summaries, administrative compilations, network/site administrative metadata, and issue/expiry-bounded context records. Some sources may also carry `regulatory` role from the issuing body; this lane must preserve that distinction instead of collapsing roles.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a record may publish, whether an advisory is current, whether an observation occurred, whether a model is reliable, whether a concentration exists, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/atmosphere/administrative/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `atmosphere` |
| Source role | `administrative` |
| Artifact role | RAW source-role lane for administrative/advisory-context captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/atmosphere/` or `data/quarantine/atmosphere/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when rights, source role, issue/expiry time, citation, sensitivity, freshness, advisory framing, validation, correction, rollback, or release support is insufficient |

---

## Administrative source posture

| Source / knowledge character | Role handling | RAW rule |
|---|---|---|
| KDHE bulletin or state advisory context | `administrative`; may also cite a `regulatory` issuing authority where documented | Preserve issuer, issue time, expiry/effective window, citation, source URL/reference, digest, attribution, and caveats. |
| Forecast / advisory context | `administrative` or `regulatory` depending on issuing body | Preserve issue/expiry, official-source redirection, and not-life-safety caveat. Do not turn KFM into an alerting surface. |
| Network or site administrative metadata | `administrative` / `network_and_site_context` | Preserve operator/network identity, metadata vintage, rights, and sensitivity. Do not imply sensor observation values. |
| Administrative compilation or summary | `administrative` | Preserve source basis, compilation date, scope, issuer, and caveats. Do not cite it as observed evidence. |
| Mixed administrative + observed payload | **NEEDS REVIEW** | Split roles or quarantine. An administrative record cannot silently become an observed reading. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- bulletin/advisory/source packet snapshots or stable source references;
- raw payloads or raw payload references;
- issue time, expiry time, effective window, retrieval time, source vintage, issuer, source URL/reference, attribution, and digest sidecars;
- source-head records, response metadata, status codes, row counts where applicable, and checksums;
- minimal README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, observation, model, alert, or public authority.

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
| Ingest, validation, aggregation, redaction, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Observed sensor readings, model fields, concentration observations, AQI reports, AOD rasters, climate normals, or derived fusion truth | Owning source-role/product lane and downstream governed stages; never this administrative RAW lane by itself |
| Emergency alerting, life-safety instructions, evacuation/routing advice, or authoritative health guidance | External official authorities, not KFM RAW data |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/atmosphere/administrative/
├── README.md
├── <source_id>/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── advisory_or_bulletin_ref.json
│       ├── manifest.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph edge source, layer/story/report pointer, search index, vector index, map source, observation index, advisory authority, alerting source, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Rights, source role, issue/expiry, attribution, freshness, citation, digest, sensitivity, schema, source activation, or advisory framing is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, issue/expiry handling, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
data/raw/atmosphere/administrative/
→ data/processed/atmosphere/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Atmosphere lane and is administrative or expected to resolve as administrative.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, authority, rights, sensitivity, cadence, citation, issue/expiry posture, and hash posture.
- [ ] Confirm administrative material is not being cited as observed sensor evidence, model evidence, AQI concentration truth, or emergency/life-safety instruction.
- [ ] Confirm official-source redirection and not-life-safety caveats are preserved for advisory-context material.
- [ ] Confirm issue time, expiry/effective window, retrieval time, and stale-state rules are recorded where material.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested Atmosphere administrative RAW source-role lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/atmosphere/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source registry doctrine lists KDHE bulletins as administrative/regulatory state advisory context. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source registry doctrine lists forecast/advisory context as administrative/regulatory and explicitly not life-safety. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere source-role doctrine says an administrative compilation must not be cited as observation, and source role is fixed at admission. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere lifecycle doctrine says RAW captures immutable source payload/reference, requires SourceDescriptor/RawCaptureReceipt, and is denied to public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual administrative Atmosphere RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, validators, fixtures, CI checks, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, observation truth, model truth, advisory authority, emergency guidance, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/atmosphere/README.md`](../../../quarantine/atmosphere/README.md)
- [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- [`../../../processed/atmosphere/air_observations/README.md`](../../../processed/atmosphere/air_observations/README.md)
- [`../../../catalog/domain/atmosphere/README.md`](../../../catalog/domain/atmosphere/README.md)
- [`../../../published/layers/atmosphere/README.md`](../../../published/layers/atmosphere/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md`](../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md`](../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md`](../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
- [`../../../../docs/domains/atmosphere/API_CONTRACTS.md`](../../../../docs/domains/atmosphere/API_CONTRACTS.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is an Atmosphere administrative RAW source-role lane only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, observation truth, model truth, AQI concentration truth, advisory authority, emergency guidance, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
