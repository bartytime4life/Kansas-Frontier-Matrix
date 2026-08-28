<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/ecoregions/readme
name: Habitat Ecoregions Raw README
path: data/raw/habitat/ecoregions/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <ecoregions-source-steward>
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
domain: habitat
source_family: ecoregions
source_role: administrative-context
artifact_family: immutable-habitat-ecoregions-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; context-layer-not-truth-root; sensitive-joins-fail-closed; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/habitat/README.md
  - ../../../quarantine/habitat/ecoregions/README.md
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
  - ecoregions
  - landscape-context
  - administrative
  - context-layer
  - source-capture
  - sensitive-join
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the placeholder content at `data/raw/habitat/ecoregions/README.md`."
  - "Parent `data/raw/habitat/README.md` is currently a greenfield stub, so this child file stays source-family-lane bounded."
  - "Ecoregion material is treated as Habitat landscape context fabric and administrative/context source capture, not habitat truth, occurrence truth, regulatory truth, or public release authority."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, sensitivity controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Ecoregions RAW Lane

RAW source-family lane for immutable ecoregion source captures and source-admission sidecars in the Habitat domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: ecoregions" src="https://img.shields.io/badge/source-ecoregions-1f6feb">
  <img alt="Role: administrative context" src="https://img.shields.io/badge/role-administrative%20context-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Ecoregion source posture](#ecoregion-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/habitat/ecoregions/` is a no-public-path RAW source-family lane. It is not processed Habitat truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity policy authority, regulatory authority, occurrence authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for ecoregion material admitted to the Habitat lane.

KFM treats ecoregion material as landscape context fabric: useful for coarse ecological region context, habitat stratification, cross-domain joins, and map interpretation. It is not interchangeable geometry truth, not occurrence evidence, not a regulatory designation by default, and not a public release authority merely because it was captured.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, which source surface was used, what role it carried, and which identifiers, times, rights, citations, geometry/support notes, classification vocabulary, hashes, sensitivity flags, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/ecoregions/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `habitat` |
| Source family | `ecoregions` |
| Source role | `administrative` / `context`; exact role set by SourceDescriptor |
| Artifact role | RAW source-family lane for ecoregion captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/habitat/` or `data/quarantine/habitat/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, provenance, geometry/support, classification vocabulary, sensitive-join risk, citation, validation, correction, rollback, or release support is insufficient |

---

## Ecoregion source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| EPA ecoregions or equivalent ecoregion layer | Capture as Habitat context source material when admitted. | Context layer; not habitat truth or occurrence truth by itself. |
| Landscape context fabric bundle | Preserve component identity, source role, version, and geometry scope. | Do not collapse ecoregions, PLSS, watershed boundaries, land cover, or stewardship layers into interchangeable geometry truth. |
| Native classification / level hierarchy | Preserve source labels, level, code, version, and citation. | Advisory crosswalks must not replace native classification. |
| Join to occurrence or rare-species data | Route through sensitivity review before downstream use. | Sensitive joins fail closed; no exact occurrence-linked public product from RAW. |
| Public derivative proposal | Hold until processed, catalog/proof, policy, review, release, correction, and rollback gates close. | RAW capture is not release state. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- ecoregion dataset references, service references, download references, or restricted raw payload references;
- source identifiers, region codes, names, classification level, version/vintage, source time, retrieval time, geometry/support notes, citation, attribution, rights posture, sensitivity hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Ecoregion/source-family doctrine | `docs/sources/catalog/` or `docs/domains/habitat/` |
| Habitat domain doctrine | `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, geoprivacy, redaction, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/habitat/` |
| Normalized working material | `data/work/habitat/` |
| Validated Habitat objects | `data/processed/habitat/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, redaction, aggregation, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Occurrence truth, regulatory designation truth, habitat suitability truth, taxonomic truth, or public answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/habitat/ecoregions/
├── README.md
├── <source_id>/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── dataset_ref.json
│       ├── classification_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, regulatory authority, occurrence authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, sensitivity, geometry/support, classification vocabulary, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/generalization receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/habitat/ecoregions/
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Habitat lane and the ecoregions source family.
- [ ] Confirm whether the captured material is EPA ecoregions, another ecoregion product, or a broader context-fabric package.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, product/surface identity, rights, cadence, citation, sensitivity posture, and hash posture.
- [ ] Confirm native classification, level hierarchy, source version/vintage, and geometry scope are preserved before any crosswalk.
- [ ] Confirm ecoregions are not being treated as occurrence truth, regulatory designation truth, habitat suitability truth, or interchangeable geometry truth.
- [ ] Confirm sensitive joins to Fauna/Flora occurrence, rare-species, or steward-controlled records fail closed until policy review, geoprivacy transform, and receipts exist.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/ecoregions/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-registry doctrine lists ecoregion/context-fabric style sources as Habitat context material and says sensitive joins fail closed. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-family doctrine identifies EPA ecoregions / PLSS / WBD HUC12 as landscape context fabric with administrative role posture. | **CONFIRMED by GitHub contents API during this edit** |
| Actual ecoregion RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, sensitivity controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, regulatory authority, occurrence authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/habitat/README.md`](../../../quarantine/habitat/README.md)
- [`../../../quarantine/habitat/ecoregions/README.md`](../../../quarantine/habitat/ecoregions/README.md)
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

KFM rule: this directory is a Habitat ecoregions RAW source-family lane for source capture only. It is not source-family doctrine, source registry authority, rights authority, sensitivity policy authority, proof authority, receipt authority, release authority, catalog authority, regulatory authority, occurrence authority, habitat-suitability truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
