<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/natureserve/readme
name: Habitat NatureServe Raw README
path: data/raw/habitat/natureserve/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
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
source_family: natureserve
source_role: administrative-aggregate-context
artifact_family: immutable-habitat-natureserve-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; review-required; release-blocked
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
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - natureserve
  - ecological-systems
  - source-capture
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/habitat/natureserve/README.md`."
  - "Parent `data/raw/habitat/README.md` is currently a greenfield stub."
  - "This lane is source capture only; implementation wiring and payload presence remain unverified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat NatureServe RAW Lane

RAW source-family lane for NatureServe Habitat source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: NatureServe" src="https://img.shields.io/badge/source-NatureServe-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/habitat/natureserve/` is a RAW source-capture lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, or generated-answer authority.

---

## Scope

This directory is for immutable NatureServe-related Habitat source captures and RAW-local sidecars.

KFM treats this source family as Habitat context for ecological-system definitions, conservation context, and related review workflows. The repository docs classify NatureServe ecological systems as administrative/aggregate context, with rights still needing verification. The exact admitted role must be set by SourceDescriptor.

RAW records what was captured, where it came from, what source role it carried, and which identifiers, times, rights notes, citations, version fields, hashes, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/natureserve/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `habitat` |
| Source family | `natureserve` |
| Source role | `administrative` / `aggregate`; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/habitat/` or `data/quarantine/habitat/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, citation, validation, or release support is insufficient |

---

## Source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Ecological-system definition material | Capture as administrative/context source material when admitted. | Native source classification remains visible. |
| Conservation context material | Capture as aggregate/context source material when admitted. | Context does not become public-release authority by itself. |
| Review-gated package | Hold for source and rights review before downstream use. | Review state must be recorded before use outside RAW. |
| Crosswalk to GAP/LANDFIRE | Preserve crosswalk target and advisory status. | Crosswalks are advisory and do not replace source classification. |
| Mixed package | Split by SourceDescriptor or quarantine. | One descriptor carries one role. |

---

## Accepted material

- source-reference manifests;
- release references, definition references, context references, steward-provided file references, service references, or raw payload references;
- product type, terms reference, source identifiers, source time, retrieval time, source vintage, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Source-family doctrine | `docs/sources/catalog/` or `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, or release policy | `policy/` and governed review lanes |
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
data/raw/habitat/natureserve/
├── README.md
├── <run_id>/
│   ├── source_reference.json
│   ├── payload_ref.json
│   ├── checksums.sha256
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was captured, but no downstream decision has been made. |
| Quarantine | Source role, rights, citation, schema, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/habitat/natureserve/
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Habitat lane and NatureServe source family.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, rights, citation, review posture, and hash posture.
- [ ] Confirm the source role is not collapsed across products.
- [ ] Confirm source classification and advisory crosswalks remain separate.
- [ ] Confirm rights, terms, citation, steward permissions, and allowed reuse have been reviewed or marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/natureserve/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat docs identify NatureServe / Natural Heritage as ecological-system and conservation context. | **CONFIRMED by GitHub contents API during this edit** |
| Actual NatureServe RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat NatureServe RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
