<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hazards/fema/readme
title: Hazards FEMA Raw README
path: data/raw/hazards/fema/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <hazards-domain-steward>
  - <hazards-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Hazards FEMA RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: hazards
source_family: fema
source_role: administrative-or-regulatory-per-product
artifact_family: hazards-fema-raw-compatibility-reference
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
  - ../nfhl/README.md
  - ../../hydrology/fema_nfhl/README.md
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
  - compatibility-reference
  - source-first
notes:
  - "This README replaces placeholder content at `data/raw/hazards/fema/README.md`."
  - "Parent `data/raw/hazards/README.md` was a greenfield stub when this README was first authored on 2026-06-27; it is now a tracked compatibility/reference index."
  - "FEMA material requires per-product role handling: OpenFEMA Disaster Declarations are administrative; FEMA MSC/NFHL material is regulatory context."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards FEMA RAW Lane

Compatibility/reference documentation for Hazards-facing FEMA RAW topology; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-c62828">
  <img alt="Source family: FEMA" src="https://img.shields.io/badge/source-FEMA-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/hazards/fema/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named subtree is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, or generated-answer authority.

---

## Scope

This directory documents Hazards-facing FEMA source handling and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

KFM treats FEMA as an authority cluster with multiple product surfaces, not one flat role. OpenFEMA Disaster Declarations are administrative records. FEMA Map Service Center and NFHL-related material are regulatory flood-context records. These roles must stay separate through SourceDescriptor records and downstream evidence handling.

A governed source-first capture records what was captured, where it came from, what source role it carried, and which identifiers, times, rights notes, citations, source versions, service references, checksums, and caveats must travel downstream.

FEMA NFHL material is also documented by the sibling lanes [`../nfhl/`](../nfhl/README.md) and [`../../hydrology/fema_nfhl/`](../../hydrology/fema_nfhl/README.md). All of these lanes must reference the same single source-first NFHL capture, never separate copies.

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
| Artifact role | Compatibility/reference documentation for Hazards-facing FEMA source handling and unresolved legacy RAW topology |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | Governed Hazards WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, product identity, version/vintage, citation, validation, or release support is insufficient |

---

## FEMA source posture

| FEMA source condition | RAW handling | Boundary |
|---|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; references may support Hazards without duplicating RAW bytes. | A hazards-scoped copy is not a second capture identity. |
| Physical placement is held | Do not infer `data/raw/hazards/fema/` or any subfolder as the capture home. Use only an accepted writer/path contract; none is established by this README. | This lane may retain governed references only. |
| OpenFEMA Disaster Declarations | Capture as administrative source material when admitted. | A declaration is an administrative record, not an observed event. |
| FEMA MSC / effective FIRM material | Capture as regulatory source material when admitted. | Regulatory flood context is not observed inundation. |
| NFHL companion material | Preserve version/vintage, effective date, service URI, and citation. | NFHL/MSC outputs require SourceDescriptor separation where product role or access differs. |
| Preliminary or candidate FEMA material | Hold as candidate or quarantine until activation review. | Candidate material must not be published as effective regulatory context. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, review, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads.

The governed source-first capture or reference that supports Hazards FEMA use must carry, where applicable:

- source-reference manifests;
- OpenFEMA dataset references, FEMA service references, MSC/NFHL references, product/version references, or raw payload references;
- declaration identifiers, declaration type, incident type as administrative metadata, declared geography, product vintage, effective date where applicable, service URI, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums.

None of these, and no local README or index, becomes proof, catalog, registry, policy, release, public artifact, or answer authority.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Hazards. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source-run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Earlier drafts sketched per-product run groupings: `openfema-disaster-declarations/` runs carrying `source_reference.json`, `dataset_ref.json`, `checksums.sha256`, and a run README; `map-service-center/` runs carrying `source_reference.json`, `product_ref.json`, `version_ref.json`, `checksums.sha256`, and a run README; and `nfhl/` runs carrying `source_reference.json`, `service_ref.json`, `version_ref.json`, `checksums.sha256`, and a run README, plus an optional RAW-local index. That layout is a proposed shape for a future accepted source-first home, not this subtree.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was captured, but no downstream decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, rights, product identity, version/vintage, citation, schema, freshness, source activation, or physical placement is unresolved. |
| Return / reject | Admission or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Hazards WORK only when SourceDescriptor, rights posture, source role, source-family identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/hazards/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Hazards-scoped copy.
- [ ] Treat this source-named README as compatibility/reference documentation only; do not create a child directory as a payload destination.
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
| Parent `data/raw/hazards/README.md` was a greenfield stub when this README was first authored (2026-06-27). | **CONFIRMED historically; superseded — the parent is now a tracked compatibility/reference index reconciled on 2026-10-11** |
| Hazards source-registry doctrine lists FEMA Disaster Declarations/OpenFEMA as administrative and FEMA NFHL/MSC as regulatory flood context. | **CONFIRMED by GitHub contents API during this edit** |
| OpenFEMA Disaster Declarations doctrine says declarations are administrative federal actions, not observed hazard events. | **CONFIRMED by GitHub contents API during this edit** |
| FEMA MSC doctrine says MSC artifacts are regulatory context, never observed inundation. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual FEMA RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
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
- [`../nfhl/README.md`](../nfhl/README.md)
- [`../../hydrology/fema_nfhl/README.md`](../../hydrology/fema_nfhl/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hazards-facing FEMA compatibility/reference lane. One governed source-first capture may support Hazards without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
