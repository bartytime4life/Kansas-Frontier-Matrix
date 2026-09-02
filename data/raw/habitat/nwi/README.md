<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/nwi/readme
name: Habitat NWI Raw README
path: data/raw/habitat/nwi/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <nwi-source-steward>
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
source_family: nwi
source_role: observed-inventory
artifact_family: immutable-habitat-nwi-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; cowardin-classification-preserved; crosswalk-advisory; regulatory-boundary-needs-descriptor; rights-needs-verification; release-blocked
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
  - ../../../../docs/domains/habitat/REASON_CODES.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - nwi
  - wetlands
  - usfws
  - cowardin
  - wetlands-mapper
  - source-capture
  - advisory-crosswalk
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/habitat/nwi/README.md`."
  - "Parent `data/raw/habitat/README.md` is currently a greenfield stub, so this child file stays source-family-lane bounded."
  - "NWI material is treated as source capture for federal wetlands inventory mapping. Cowardin classes and project delta strategy must be preserved."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, sensitivity controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat NWI RAW Lane

RAW source-family lane for immutable USFWS National Wetlands Inventory source captures, Wetlands Mapper references, Cowardin classification references, and source-admission sidecars in the Habitat domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: NWI" src="https://img.shields.io/badge/source-NWI-1f6feb">
  <img alt="Role: observed inventory" src="https://img.shields.io/badge/role-observed%20inventory-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [NWI source posture](#nwi-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/habitat/nwi/` is a no-public-path RAW source-family lane. It is not processed Habitat truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, public API/UI material, release authority, regulatory determination authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for NWI material admitted to the Habitat lane.

KFM treats NWI as a federal wetlands inventory mapping source. It may support wetland/riparian habitat context, wetlands extent, and Cowardin class support after governed normalization, but RAW capture is not itself processed truth, regulatory determination, or public artifact.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, which Wetlands Mapper service or download was used, what role it carried, and which identifiers, times, rights, citations, Cowardin class fields, project delta strategy, geometry/support metadata, hashes, sensitivity-on-join notes, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/nwi/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `habitat` |
| Source family | `nwi` |
| Source role | `observed` wetlands-inventory source; regulatory framing requires explicit SourceDescriptor support where applicable |
| Artifact role | RAW source-family lane for NWI captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/habitat/` or `data/quarantine/habitat/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, product/service identity, Cowardin class fields, project delta strategy, citation, validation, correction, rollback, or release support is insufficient |

---

## NWI source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Wetlands Mapper service or download | Capture as observed wetlands-inventory source material when admitted. | RAW capture is not a published layer or regulatory determination. |
| Cowardin classification | Preserve source Cowardin fields, labels, code, version/vintage, and citation. | Crosswalks to Habitat vocabulary are advisory and must not replace native classification. |
| Project delta / update strategy | Preserve delta strategy, source vintage, retrieval time, and digest. | Updates must not silently overwrite prior captures. |
| Regulatory boundary framing | Hold for explicit SourceDescriptor role review. | Inventory material must not be presented as regulatory authority without recorded basis. |
| Join to occurrence or sensitive context | Route through policy review before downstream public use. | Sensitivity arises on join, not from NWI alone. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- NWI Wetlands Mapper service references, download references, geometry payload references, Cowardin classification references, or raw payload references;
- product/service identity, project delta strategy, Cowardin class fields, source URI, source time, retrieval time, source vintage, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, geometry counts, tile counts, or service metadata where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| NWI/source-family doctrine | `docs/sources/catalog/` or `docs/domains/habitat/` |
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
| Regulatory determination truth, habitat suitability truth, occurrence truth, or public answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/habitat/nwi/
├── README.md
├── <service_or_run_id>/
│   ├── source_reference.json
│   ├── service_ref.json
│   ├── cowardin_classification_ref.json
│   ├── project_delta_ref.json
│   ├── checksums.sha256
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, regulatory authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, product/service identity, Cowardin fields, project delta strategy, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/generalization receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/habitat/nwi/
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Habitat lane and the NWI source family.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, product/surface identity, rights, cadence, citation, review posture, and hash posture.
- [ ] Confirm Wetlands Mapper metadata, Cowardin class fields, service/download URI, project delta strategy, and source vintage are recorded.
- [ ] Confirm a new service pull or update is stored as a new capture and does not overwrite a prior capture in place.
- [ ] Confirm native Cowardin classes are preserved before any advisory crosswalk.
- [ ] Confirm inventory material is not being framed as regulatory determination authority without explicit SourceDescriptor support.
- [ ] Confirm joins to occurrence or other sensitive context are handled by downstream policy before public use.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/nwi/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-family doctrine identifies NWI as National Wetlands Inventory federal wetlands mapping from USFWS Wetlands Mapper. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-family doctrine says Cowardin classification is preserved and crosswalks are advisory. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-registry doctrine lists NWI as observed, with regulatory boundaries where designated requiring role-awareness. | **CONFIRMED by GitHub contents API during this edit** |
| Actual NWI RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, regulatory determination authority, public artifact authority, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/domains/habitat/REASON_CODES.md`](../../../../docs/domains/habitat/REASON_CODES.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat NWI RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, regulatory determination authority, habitat-suitability truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
