<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/usfws-ecos/readme
name: Habitat USFWS ECOS Raw README
path: data/raw/habitat/usfws-ecos/README.md
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
source_family: usfws-ecos
source_role: regulatory-context
artifact_family: immutable-habitat-usfws-ecos-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; rights-needs-verification; release-blocked
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
  - ../../../../docs/sources/catalog/usfws_ecos/README.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - usfws
  - ecos
  - regulatory
  - source-capture
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/habitat/usfws-ecos/README.md`."
  - "Parent `data/raw/habitat/README.md` is currently a greenfield stub."
  - "This lane is source capture only; implementation wiring and payload presence remain unverified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat USFWS ECOS RAW Lane

RAW source-family lane for USFWS ECOS Habitat source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: USFWS ECOS" src="https://img.shields.io/badge/source-USFWS%20ECOS-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/habitat/usfws-ecos/` is a RAW source-capture lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, model output, or generated-answer authority.

---

## Scope

This directory is for immutable USFWS ECOS source captures and RAW-local sidecars in the Habitat domain.

KFM treats USFWS ECOS as regulatory context for Habitat. The Habitat docs identify ECOS as a regulatory source family and require role authority, designation type, species reference, product version, service URI, and rights in the SourceDescriptor. The ECOS catalog says the Federal Register rule is the legal source and ECOS is the carrier.

RAW records what was captured, where it came from, what role it carried, and which identifiers, times, rights notes, citations, product version, service URI, species reference, hashes, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/usfws-ecos/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `habitat` |
| Source family | `usfws-ecos` |
| Source role | `regulatory`; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/habitat/` or `data/quarantine/habitat/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when role, rights, product version, service URI, species reference, citation, validation, or release support is insufficient |

---

## Source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| ECOS service pull | Capture as regulatory context when admitted. | RAW capture is not release state. |
| Product version or service URI | Preserve version, URI, source time, retrieval time, citation, and digest. | Updates must not overwrite prior captures in place. |
| Species reference | Preserve source reference and crosswalk target. | Habitat does not own taxon truth. |
| Framing as modeled output | Quarantine or deny. | ECOS context must not be collapsed with modeled Habitat products. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

- source-reference manifests;
- ECOS service references, product/version references, species-reference sidecars, or raw payload references;
- role authority, designation type, species reference, product version, service URI, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Source-family doctrine | `docs/sources/catalog/usfws_ecos/` or `docs/domains/habitat/` |
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
data/raw/habitat/usfws-ecos/
├── README.md
├── <service_or_run_id>/
│   ├── source_reference.json
│   ├── ecos_service_ref.json
│   ├── product_ref.json
│   ├── species_reference_ref.json
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
| Quarantine | Source role, rights, product version, service URI, species reference, citation, schema, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, source-family identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/habitat/usfws-ecos/
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Habitat lane and the USFWS ECOS source family.
- [ ] Confirm SourceDescriptor or admission ticket records role authority, designation type, species reference, product version, service URI, rights, citation, and hash posture.
- [ ] Confirm ECOS material is not collapsed with modeled Habitat products or occurrence evidence.
- [ ] Confirm species reference crosswalks preserve the correct owner lane for taxon truth.
- [ ] Confirm updates are stored as new captures and routed to downstream correction review where needed.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/usfws-ecos/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat docs identify USFWS ECOS as regulatory context and require role authority, designation type, species reference, product version, service URI, and rights. | **CONFIRMED by GitHub contents API during this edit** |
| ECOS catalog docs say the Federal Register rule is the legal source and ECOS is the carrier. | **CONFIRMED by GitHub contents API during this edit** |
| Actual USFWS ECOS RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
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
- [`../../../../docs/sources/catalog/usfws_ecos/README.md`](../../../../docs/sources/catalog/usfws_ecos/README.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat USFWS ECOS RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, model-output truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
