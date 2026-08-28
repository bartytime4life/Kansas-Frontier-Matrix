<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/occurrence-context/readme
name: Habitat Occurrence Context Raw README
path: data/raw/habitat/occurrence-context/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <fauna-domain-steward>
  - <flora-domain-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: habitat
source_family: occurrence-context
source_role: observed-context-join
artifact_family: immutable-habitat-occurrence-context-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; fauna-flora-own-occurrence-truth; geoprivacy-bound; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../quarantine/habitat/README.md
  - ../../../processed/habitat/README.md
  - ../../../catalog/domain/habitat/README.md
  - ../../../published/layers/habitat/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/domains/habitat/SOURCES.md
  - ../../../../docs/domains/habitat/POLICY.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - occurrence-context
  - darwin-core
  - geoprivacy
  - source-capture
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/habitat/occurrence-context/README.md`."
  - "Parent `data/raw/habitat/README.md` is currently a greenfield stub."
  - "Occurrence records enter Habitat only as context. Fauna and Flora retain occurrence truth ownership."
  - "Payload presence, SourceDescriptor records, connectors, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Occurrence Context RAW Lane

RAW source-family lane for occurrence-context captures used by Habitat joins.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: occurrence context" src="https://img.shields.io/badge/source-occurrence%20context-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/habitat/occurrence-context/` is a RAW source-capture lane. It is not processed Habitat truth, occurrence truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for occurrence-context material admitted to the Habitat lane.

KFM treats occurrence providers such as GBIF, iNaturalist, and iDigBio as observed occurrence sources owned by Fauna or Flora. Habitat consumes those records only as context for habitat assignment, association analytics, or review. This lane must not make Habitat the owner of occurrence truth.

RAW records what was captured, where it came from, what provider supplied it, what source role it carried, and which Darwin Core fields, license terms, geoprivacy status, public-safe geometry state, source URI, timestamps, citations, hashes, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/occurrence-context/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `habitat` |
| Source family | `occurrence-context` |
| Source role | `observed` context under governed join; provider identity remains visible |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Occurrence truth owner | Fauna or Flora domain, not this Habitat RAW lane |
| Downstream | `data/work/habitat/` or `data/quarantine/habitat/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when owner domain, source role, license, geoprivacy, citation, validation, or release support is insufficient |

---

## Occurrence-context posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| GBIF, iNaturalist, iDigBio, or similar context | Capture as observed context when admitted. | Fauna/Flora own occurrence truth; Habitat consumes context only. |
| Darwin Core record or occurrence reference | Preserve native fields, source URI, record identity, license, and citation. | Do not flatten providers into one generic source. |
| Geoprivacy status present | Preserve status and public-safe geometry state. | Missing or unresolved public-safe geometry blocks downstream public use. |
| Habitat join proposal | Require governed join review before downstream use. | A join does not promote RAW context into Habitat truth. |
| Public derivative proposal | Hold until downstream policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

- source-reference manifests;
- occurrence record references, Darwin Core references, provider record identifiers, source URI references, or raw payload references;
- provider, source family, record ID, taxon/source identifiers, event/source time, retrieval time, per-record license, citation, geoprivacy status, public-safe geometry state, join reason, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Occurrence-source doctrine | `docs/sources/catalog/` and owning Fauna/Flora source docs |
| Habitat domain doctrine | `docs/domains/habitat/` |
| Fauna or Flora occurrence truth | Owning processed/catalog/proof lanes |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, geoprivacy, review, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/habitat/` |
| Normalized working material | `data/work/habitat/` |
| Validated Habitat objects | `data/processed/habitat/` |
| Catalog, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/habitat/occurrence-context/
├── README.md
├── <provider>/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── occurrence_ref.json
│       ├── geoprivacy_ref.json
│       ├── habitat_join_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was captured, but no downstream join decision has been made. |
| Quarantine | Owner domain, source role, license, geoprivacy, citation, schema, or source activation is unresolved. |
| Move to work | SourceDescriptor, owner domain, source role, rights posture, geoprivacy posture, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/habitat/occurrence-context/
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the material belongs to Habitat occurrence context and has an owning Fauna or Flora source.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, owner domain, provider, rights, citation, geoprivacy posture, and hash posture.
- [ ] Confirm Darwin Core fields, per-record license, source URI, geoprivacy status, and public-safe geometry state are preserved where present.
- [ ] Confirm Habitat is not being treated as owner of occurrence truth.
- [ ] Confirm provider identity is preserved and not flattened across occurrence sources.
- [ ] Confirm any Habitat join is reviewed before downstream use.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/occurrence-context/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat docs say GBIF, iNaturalist, and iDigBio are occurrence aggregators used as context while Fauna owns occurrence truth. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat docs say geoprivacy status and public-safe geometry are required controls for occurrence-context use. | **CONFIRMED by GitHub contents API during this edit** |
| Actual occurrence-context RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, occurrence truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../quarantine/habitat/README.md`](../../../quarantine/habitat/README.md)
- [`../../../processed/habitat/README.md`](../../../processed/habitat/README.md)
- [`../../../catalog/domain/habitat/README.md`](../../../catalog/domain/habitat/README.md)
- [`../../../published/layers/habitat/README.md`](../../../published/layers/habitat/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/habitat/SOURCE_REGISTRY.md`](../../../../docs/domains/habitat/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/habitat/SOURCE_FAMILIES.md`](../../../../docs/domains/habitat/SOURCE_FAMILIES.md)
- [`../../../../docs/domains/habitat/SOURCES.md`](../../../../docs/domains/habitat/SOURCES.md)
- [`../../../../docs/domains/habitat/POLICY.md`](../../../../docs/domains/habitat/POLICY.md)
- [`../../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/flora/SOURCE_REGISTRY.md`](../../../../docs/domains/flora/SOURCE_REGISTRY.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat occurrence-context RAW lane for source capture and governed joins only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, occurrence truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
