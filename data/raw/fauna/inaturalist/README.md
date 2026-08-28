<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/inaturalist/readme
name: iNaturalist Raw Fauna README
path: data/raw/fauna/inaturalist/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <fauna-domain-steward>
  - <fauna-source-steward>
  - <inaturalist-source-steward>
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
domain: fauna
source_family: inaturalist
source_family_enum: inat
source_role: observed-aggregator
artifact_family: immutable-inaturalist-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; research-grade-and-normalized-cc-required; geoprivacy-preserved-as-evidence; sensitive-geometry-fail-closed; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/fauna/README.md
  - ../../../processed/fauna/README.md
  - ../../../catalog/domain/fauna/README.md
  - ../../../published/layers/fauna/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/sources/catalog/inaturalist/README.md
  - ../../../../docs/sources/catalog/inaturalist/research-grade-observations.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../../docs/domains/fauna/POLICY.md
  - ../../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../connectors/inaturalist/README.md
  - ../../../../connectors/fauna/inaturalist/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - fauna
  - inaturalist
  - inat
  - biodiversity
  - occurrence
  - community-science
  - research-grade
  - geoprivacy
  - sensitive-geometry
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested iNaturalist Fauna RAW source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/fauna/README.md` is currently a greenfield stub, so this child file stays source-family-lane bounded."
  - "iNaturalist is treated as community-observation occurrence source material, not regulatory authority, legal-status authority, sensitive-location authority, canonical taxonomic authority, or public release authority."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, geoprivacy controls, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# iNaturalist RAW Fauna Lane

RAW source-family lane for immutable iNaturalist source captures and source-admission sidecars in the Fauna domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Source family: iNaturalist" src="https://img.shields.io/badge/source-iNaturalist-1f6feb">
  <img alt="Source role: observed aggregator" src="https://img.shields.io/badge/role-observed%20aggregator-228be6">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [iNaturalist source posture](#inaturalist-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/fauna/inaturalist/` is a no-public-path RAW source-family lane. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity authority, policy authority, regulatory authority, legal-status authority, exact sensitive-location authority, canonical taxonomic authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for iNaturalist material admitted to the Fauna lane.

KFM treats iNaturalist as community-observation occurrence evidence with confidence and quality-state metadata. It is useful as one biodiversity evidence stream, but it is not a replacement for KDWP, USFWS, NatureServe, specimen-backed collections, or taxonomic authority sources.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, which API/product surface was used, what role it carried, and which identifiers, times, licenses, citations, geoprivacy states, sensitivity flags, taxonomy anchors, hashes, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/fauna/inaturalist/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `fauna` |
| Source family | `inaturalist` / `inat` |
| Source role | `observed` as community-observation aggregator; `candidate` for records needing steward review |
| Artifact role | RAW source-family lane for iNaturalist captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/fauna/` or `data/quarantine/fauna/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, quality grade, per-record license, geoprivacy, sensitivity, taxonomy, time, geometry, citation, validation, correction, rollback, or release support is insufficient |

---

## iNaturalist source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Research-grade observation with normalized CC license | May use this lane as RAW source capture when admitted. | Research-grade status does not bypass KFM rights, sensitivity, validation, catalog, or release gates. |
| Non-research-grade / casual observation | Treat as candidate or review-required unless a separate admitted product exists. | Do not silently promote under the research-grade bar. |
| Obscured or private geoprivacy state | Preserve as source evidence and route through sensitivity review. | Do not infer, back-fill, or deobscure exact coordinates. |
| Sensitive taxon or sensitive-site class | Route to quarantine/restricted review before downstream use. | No exact public exposure without redaction/review closure. |
| Taxonomic identification | Preserve source taxon and confidence fields. | Reconcile against ITIS/GBIF Backbone or other controlled authority; iNaturalist is not canonical taxonomy. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- iNaturalist API response references, observation references, media-reference manifests, or restricted raw payload references;
- observation identifiers, quality grade, license fields, taxon identifiers/names, identification state where exposed, event/source time, retrieval time, geoprivacy state, geometry/support notes, citation, attribution, sensitivity hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| iNaturalist source/product doctrine | `docs/sources/catalog/inaturalist/` |
| Fauna domain doctrine | `docs/domains/fauna/` |
| Connector code or connector decisions | `connectors/inaturalist/` or accepted connector home |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, geoprivacy, redaction, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/fauna/` |
| Normalized working material | `data/work/fauna/` |
| Validated Fauna objects | `data/processed/fauna/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, redaction, aggregation, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Legal/listed status authority, regulatory authority, exact sensitive-location authority, canonical taxonomy, emergency guidance, or specimen-backed authority | Owning governed downstream/policy/proof lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/fauna/inaturalist/
├── README.md
├── research-grade/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── request_parameters.json
│       ├── observations_ref.json
│       ├── license_summary.json
│       ├── geoprivacy_summary.json
│       ├── checksums.sha256
│       └── README.md
├── candidate/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── candidate_observations_ref.json
│       ├── review_reason.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, taxonomic authority, rights authority, geoprivacy authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, quality grade, per-record license, geoprivacy, sensitive taxon/site class, taxonomic anchor, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, product/query identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/aggregation receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/fauna/inaturalist/
→ data/processed/fauna/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Fauna lane and the iNaturalist source family.
- [ ] Confirm whether the captured material is research-grade, candidate/non-research-grade, media reference, or derived aggregate material.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, product/surface identity, license posture, citation, attribution, geoprivacy posture, sensitivity posture, taxonomy-anchor posture, and hash posture.
- [ ] Confirm research-grade, normalized CC license, and controlled-taxonomy requirements are met for promotion-track material.
- [ ] Confirm obscured/private coordinates are preserved as evidence and are not inferred away, back-filled, or deobscured.
- [ ] Confirm iNaturalist is not being used as regulatory authority, listed-status authority, exact sensitive-location authority, canonical taxonomy, or public-release authority.
- [ ] Confirm sensitive taxa, exact geometry, observer/user-like fields, comments, and media references are handled by fail-closed policy before downstream use.
- [ ] Confirm rights, current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested iNaturalist Fauna RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/fauna/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| iNaturalist source docs identify it as a community-observation source family, not legal/listed status, regulatory, exact-sensitive-location, or canonical taxonomy authority. | **CONFIRMED by GitHub contents API during this edit** |
| iNaturalist research-grade product docs require research-grade status, normalized CC license, controlled-taxonomy resolution, and geoprivacy preservation. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, with no public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual iNaturalist RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, geoprivacy controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, regulatory authority, listed-status authority, exact sensitive-location authority, taxonomic authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/fauna/README.md`](../../../quarantine/fauna/README.md)
- [`../../../processed/fauna/README.md`](../../../processed/fauna/README.md)
- [`../../../catalog/domain/fauna/README.md`](../../../catalog/domain/fauna/README.md)
- [`../../../published/layers/fauna/README.md`](../../../published/layers/fauna/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/sources/catalog/inaturalist/README.md`](../../../../docs/sources/catalog/inaturalist/README.md)
- [`../../../../docs/sources/catalog/inaturalist/research-grade-observations.md`](../../../../docs/sources/catalog/inaturalist/research-grade-observations.md)
- [`../../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../../docs/domains/fauna/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/fauna/POLICY.md`](../../../../docs/domains/fauna/POLICY.md)
- [`../../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../../docs/domains/fauna/CANONICAL_PATHS.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../connectors/inaturalist/README.md`](../../../../connectors/inaturalist/README.md)
- [`../../../../connectors/fauna/inaturalist/README.md`](../../../../connectors/fauna/inaturalist/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is an iNaturalist Fauna RAW source-family lane for source capture only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, regulatory authority, legal-status authority, exact sensitive-location authority, canonical taxonomic authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
