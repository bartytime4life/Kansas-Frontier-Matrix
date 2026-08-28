<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hazards/fema/readme
name: Hazards FEMA Raw README
path: data/raw/hazards/fema/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <hazards-domain-steward>
  - <hazards-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: hazards
source_family: fema
source_role: administrative-or-regulatory-per-product
artifact_family: immutable-hazards-fema-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../quarantine/hazards/README.md
  - ../../../processed/hazards/README.md
  - ../../../catalog/domain/hazards/README.md
  - ../../../published/layers/hazards/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hazards/SOURCES.md
  - ../../../../docs/sources/catalog/fema/openfema-disaster-declarations.md
  - ../../../../docs/sources/catalog/fema/map-service-center.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hazards
  - fema
  - openfema
  - flood-context
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/hazards/fema/README.md`."
  - "Parent `data/raw/hazards/README.md` is currently a greenfield stub."
  - "FEMA material requires per-product role handling: OpenFEMA Disaster Declarations are administrative; FEMA MSC/NFHL material is regulatory context."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards FEMA RAW Lane

RAW source-family lane for immutable FEMA source captures and source-admission sidecars in the Hazards domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-c62828">
  <img alt="Source family: FEMA" src="https://img.shields.io/badge/source-FEMA-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/hazards/fema/` is a RAW source-capture lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, or generated-answer authority.

---

## Scope

This directory is for immutable FEMA source captures and RAW-local sidecars in the Hazards domain.

KFM treats FEMA as an authority cluster with multiple product surfaces, not one flat role. OpenFEMA Disaster Declarations are administrative records. FEMA Map Service Center and NFHL-related material are regulatory flood-context records. These roles must stay separate through SourceDescriptor records and downstream evidence handling.

RAW records what was captured, where it came from, what source role it carried, and which identifiers, times, rights notes, citations, source versions, service references, checksums, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hazards/fema/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hazards` |
| Source family | `fema` |
| Source role | `administrative` or `regulatory` per product; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/hazards/` or `data/quarantine/hazards/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, product identity, version/vintage, citation, validation, or release support is insufficient |

---

## FEMA source posture

| FEMA source condition | RAW handling | Boundary |
|---|---|---|
| OpenFEMA Disaster Declarations | Capture as administrative source material when admitted. | A declaration is an administrative record, not an observed event. |
| FEMA MSC / effective FIRM material | Capture as regulatory source material when admitted. | Regulatory flood context is not observed inundation. |
| NFHL companion material | Preserve version/vintage, effective date, service URI, and citation. | NFHL/MSC outputs require SourceDescriptor separation where product role or access differs. |
| Preliminary or candidate FEMA material | Hold as candidate or quarantine until activation review. | Candidate material must not be published as effective regulatory context. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

- source-reference manifests;
- OpenFEMA dataset references, FEMA service references, MSC/NFHL references, product/version references, or raw payload references;
- declaration identifiers, declaration type, incident type as administrative metadata, declared geography, product vintage, effective date where applicable, service URI, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| FEMA/source-family doctrine | `docs/sources/catalog/fema/` or `docs/domains/hazards/` |
| Connector code or connector decisions | `connectors/fema/` or other connector authority roots |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, sensitivity, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/hazards/` |
| Normalized working material | `data/work/hazards/` |
| Validated Hazards objects | `data/processed/hazards/` |
| Catalog, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hazards/fema/
├── README.md
├── openfema-disaster-declarations/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── dataset_ref.json
│       ├── checksums.sha256
│       └── README.md
├── map-service-center/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── product_ref.json
│       ├── version_ref.json
│       ├── checksums.sha256
│       └── README.md
├── nfhl/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── service_ref.json
│       ├── version_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was captured, but no downstream decision has been made. |
| Quarantine | Source role, rights, product identity, version/vintage, citation, schema, freshness, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, source-family identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/hazards/fema/
→ data/processed/hazards/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hazards lane and the FEMA source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, product identity, rights, cadence, citation, version/vintage, freshness posture, and hash posture.
- [ ] Confirm OpenFEMA Disaster Declarations are not treated as observed hazard events.
- [ ] Confirm FEMA MSC/NFHL material is not treated as observed inundation.
- [ ] Confirm preliminary/candidate FEMA material is not treated as effective regulatory material.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/hazards/fema/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/hazards/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Hazards source-registry doctrine lists FEMA Disaster Declarations/OpenFEMA as administrative and FEMA NFHL/MSC as regulatory flood context. | **CONFIRMED by GitHub contents API during this edit** |
| OpenFEMA Disaster Declarations doctrine says declarations are administrative federal actions, not observed hazard events. | **CONFIRMED by GitHub contents API during this edit** |
| FEMA MSC doctrine says MSC artifacts are regulatory context, never observed inundation. | **CONFIRMED by GitHub contents API during this edit** |
| Actual FEMA RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../quarantine/hazards/README.md`](../../../quarantine/hazards/README.md)
- [`../../../processed/hazards/README.md`](../../../processed/hazards/README.md)
- [`../../../catalog/domain/hazards/README.md`](../../../catalog/domain/hazards/README.md)
- [`../../../published/layers/hazards/README.md`](../../../published/layers/hazards/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/hazards/SOURCE_REGISTRY.md`](../../../../docs/domains/hazards/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`](../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md)
- [`../../../../docs/domains/hazards/SOURCES.md`](../../../../docs/domains/hazards/SOURCES.md)
- [`../../../../docs/sources/catalog/fema/openfema-disaster-declarations.md`](../../../../docs/sources/catalog/fema/openfema-disaster-declarations.md)
- [`../../../../docs/sources/catalog/fema/map-service-center.md`](../../../../docs/sources/catalog/fema/map-service-center.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hazards FEMA RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
