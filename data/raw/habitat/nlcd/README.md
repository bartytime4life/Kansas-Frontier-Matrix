<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/nlcd/readme
name: Habitat NLCD Raw README
path: data/raw/habitat/nlcd/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <nlcd-source-steward>
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
source_family: nlcd
source_role: observed-aggregate-per-product
artifact_family: immutable-habitat-nlcd-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; native-classification-preserved; crosswalk-advisory; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/habitat/README.md
  - ../../../processed/habitat/README.md
  - ../../../catalog/domain/habitat/README.md
  - ../../../published/layers/habitat/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/domains/habitat/SOURCES.md
  - ../../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../../docs/domains/habitat/POLICY.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - nlcd
  - land-cover
  - remotely-sensed
  - source-capture
  - native-classification
  - advisory-crosswalk
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/habitat/nlcd/README.md`."
  - "Parent `data/raw/habitat/README.md` is currently a greenfield stub, so this child file stays source-family-lane bounded."
  - "NLCD material is treated as source capture for remotely sensed land-cover classification. Native classes and vintage metadata must be preserved."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, sensitivity controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat NLCD RAW Lane

RAW source-family lane for immutable National Land Cover Database source captures, release/vintage references, classification references, and source-admission sidecars in the Habitat domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: NLCD" src="https://img.shields.io/badge/source-NLCD-1f6feb">
  <img alt="Role: observed / aggregate" src="https://img.shields.io/badge/role-observed%20%2F%20aggregate-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [NLCD source posture](#nlcd-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/habitat/nlcd/` is a no-public-path RAW source-family lane. It is not processed Habitat truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for NLCD material admitted to the Habitat lane.

KFM treats NLCD as a multi-year, remotely sensed land-cover classification source. It may support habitat patch derivation, land-cover observation, change detection, and suitability inputs after governed normalization, but RAW capture is not itself processed truth or a public artifact.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, which release/vintage was used, what role it carried, and which identifiers, times, rights, citations, classification scheme, raster form, hashes, sensitivity-on-join notes, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/nlcd/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `habitat` |
| Source family | `nlcd` |
| Source role | `observed` for remotely sensed classification; aggregate summaries require separate role handling where applicable |
| Artifact role | RAW source-family lane for NLCD captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/habitat/` or `data/quarantine/habitat/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, product vintage, classification scheme, raster form, citation, validation, correction, rollback, or release support is insufficient |

---

## NLCD source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| NLCD release or vintage | Capture as observed land-cover classification source material when admitted. | A new vintage must not silently overwrite a prior vintage. |
| Native land-cover class map | Preserve source class IDs, labels, scheme, and version. | Crosswalks to common habitat vocabularies are advisory, not authoritative. |
| Raster payload or raster reference | Preserve raster form, source reference, digest, and retrieval context. | Raster capture is not a published tile or public layer. |
| Aggregate summary derived from NLCD | Hold for separate role handling and downstream receipt support. | Aggregate statistics are not the same object as the source raster. |
| Join to occurrence or sensitive context | Route through policy review before downstream public use. | Sensitivity arises on join, not from NLCD alone. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- NLCD release references, download/service references, raster payload references, classification references, or raw payload references;
- product version/vintage, classification scheme, raster form, source URI, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, tile counts, or raster metadata where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| NLCD/source-family doctrine | `docs/sources/catalog/` or `docs/domains/habitat/` |
| Habitat domain doctrine | `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, review, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/habitat/` |
| Normalized working material | `data/work/habitat/` |
| Validated Habitat objects | `data/processed/habitat/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, review, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Habitat suitability truth, occurrence truth, regulatory designation truth, or public answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/habitat/nlcd/
├── README.md
├── <vintage_or_run_id>/
│   ├── source_reference.json
│   ├── product_ref.json
│   ├── classification_ref.json
│   ├── raster_ref.json
│   ├── checksums.sha256
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, product vintage, classification scheme, raster form, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/generalization receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/habitat/nlcd/
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Habitat lane and the NLCD source family.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, product/surface identity, rights, cadence, citation, review posture, and hash posture.
- [ ] Confirm product version/vintage, classification scheme, raster form, source URI, and source vintage are recorded.
- [ ] Confirm a new vintage is stored as a new capture and does not overwrite a prior vintage in place.
- [ ] Confirm native NLCD classes are preserved before any advisory crosswalk.
- [ ] Confirm derived aggregate summaries are not treated as the same object as source raster captures.
- [ ] Confirm joins to occurrence or other sensitive context are handled by downstream policy before public use.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/nlcd/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-family doctrine identifies NLCD as multi-year remotely sensed land-cover classification. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-family doctrine says NLCD native classes are preserved and crosswalks are advisory. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-registry doctrine lists NLCD as observed/aggregate for patch derivation, land-cover observation, and change detection. | **CONFIRMED by GitHub contents API during this edit** |
| Actual NLCD RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/habitat/README.md`](../../../quarantine/habitat/README.md)
- [`../../../processed/habitat/README.md`](../../../processed/habitat/README.md)
- [`../../../catalog/domain/habitat/README.md`](../../../catalog/domain/habitat/README.md)
- [`../../../published/layers/habitat/README.md`](../../../published/layers/habitat/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/habitat/SOURCE_REGISTRY.md`](../../../../docs/domains/habitat/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/habitat/SOURCE_FAMILIES.md`](../../../../docs/domains/habitat/SOURCE_FAMILIES.md)
- [`../../../../docs/domains/habitat/SOURCES.md`](../../../../docs/domains/habitat/SOURCES.md)
- [`../../../../docs/domains/habitat/SENSITIVITY.md`](../../../../docs/domains/habitat/SENSITIVITY.md)
- [`../../../../docs/domains/habitat/POLICY.md`](../../../../docs/domains/habitat/POLICY.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat NLCD RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, habitat-suitability truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
