<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/gbif/readme
name: GBIF Raw Fauna README
path: data/raw/fauna/gbif/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <fauna-domain-steward>
  - <fauna-source-steward>
  - <gbif-source-steward>
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
source_family: gbif
source_role: aggregator-observed-occurrence
artifact_family: immutable-gbif-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; per-dataset-license-gating; sensitive-geometry-fail-closed; backbone-version-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/fauna/README.md
  - ../../../processed/fauna/README.md
  - ../../../catalog/domain/fauna/README.md
  - ../../../published/layers/fauna/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/sources/catalog/gbif/README.md
  - ../../../../docs/sources/catalog/gbif/occurrence-api.md
  - ../../../../docs/sources/catalog/gbif/async-download.md
  - ../../../../docs/sources/catalog/gbif/dataset-metadata.md
  - ../../../../docs/sources/catalog/gbif/backbone-taxonomy.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../../docs/domains/fauna/POLICY.md
  - ../../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../connectors/gbif/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - fauna
  - gbif
  - biodiversity
  - occurrence
  - aggregator
  - darwin-core
  - download-doi
  - backbone-taxonomy
  - sensitive-geometry
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested GBIF Fauna RAW source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/fauna/README.md` is currently a greenfield stub, so this child file stays source-family-lane bounded."
  - "GBIF is treated as both occurrence aggregator and taxonomic backbone, but this RAW lane is source capture only and does not make GBIF local taxonomic, rights, catalog, proof, release, or public authority."
  - "Payload presence, SourceDescriptor records, connector activation, DOI capture, receipts, validators, fixtures, CI enforcement, geoprivacy controls, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GBIF RAW Fauna Lane

RAW source-family lane for immutable GBIF occurrence-source captures, download/API references, dataset metadata sidecars, and Backbone-version support in the Fauna domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Source family: GBIF" src="https://img.shields.io/badge/source-GBIF-1f6feb">
  <img alt="Role: aggregator occurrence" src="https://img.shields.io/badge/role-aggregator%20occurrence-228be6">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [GBIF source posture](#gbif-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/fauna/gbif/` is a no-public-path RAW source-family lane. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity authority, policy authority, sole taxonomic authority, specimen authority, exact public occurrence authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for GBIF material admitted to the Fauna lane.

KFM treats GBIF as a biodiversity occurrence aggregator and as a taxonomic backbone/crosswalk source. This RAW lane captures source material and supporting metadata; it does not decide taxonomic truth, rights clearance, sensitivity posture, catalog validity, or public release.

GBIF records carry originating institution, dataset, license, citation, and upstream provenance. Those details must travel downstream; KFM must not collapse all GBIF content into one undifferentiated source, license, or authority claim.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/fauna/gbif/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `fauna` |
| Source family | `gbif` |
| Source role | Aggregator occurrence source; taxonomic backbone/crosswalk support when explicitly captured |
| Artifact role | RAW source-family lane for GBIF captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/fauna/` or `data/quarantine/fauna/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, dataset license, restricted-use inheritance, Backbone version, DOI/citation, sensitive geometry, taxonomy, time, validation, correction, rollback, or release support is insufficient |

---

## GBIF source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Async occurrence download | Preferred RAW capture for reproducible downstream evidence when Download DOI and archive digest are recorded. | DOI capture does not bypass license, sensitivity, validation, catalog, or release gates. |
| Synchronous occurrence API response | May be captured for preview, watcher, smoke-test, or cached-fixture use. | Not publication-class evidence unless paired with replay-stable evidence. |
| Dataset metadata | Preserve dataset key, license, citation, DOI, publisher, rights holder, and originating institution where exposed. | License is per dataset, not per GBIF family as a whole. |
| Backbone taxonomy | Preserve Backbone DOI/version when used for anchoring or crosswalk. | ITIS remains primary U.S. anchor where applicable; GBIF Backbone is not a blanket override. |
| Restricted-use upstream dataset | Route to restricted review or quarantine. | Redistributed records do not lose upstream restrictions or attribution duties. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- GBIF async download references, Download DOI records, DwC-A archive references, occurrence API response references, cached-fixture references, dataset-metadata references, or Backbone-version references;
- query predicates, request parameters, dataset keys, taxon keys, Backbone DOI/version, originating institution, license, citation, attribution, source time, retrieval time, record counts, sensitivity hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| GBIF source/product doctrine | `docs/sources/catalog/gbif/` |
| Fauna domain doctrine | `docs/domains/fauna/` |
| Connector code or connector decisions | `connectors/gbif/` or accepted connector home |
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
| Taxonomic final authority, specimen authority, exact public occurrence authority, or public answer authority | Owning governed downstream/policy/proof lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/fauna/gbif/
├── README.md
├── occurrence-api/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── request_parameters.json
│       ├── response_ref.json
│       ├── checksums.sha256
│       └── README.md
├── async-download/
│   └── <download_key_or_run_id>/
│       ├── source_reference.json
│       ├── download_doi.json
│       ├── predicate.json
│       ├── dwca_ref.json
│       ├── dataset_metadata_ref.json
│       ├── checksums.sha256
│       └── README.md
├── backbone-taxonomy/
│   └── <snapshot_or_run_id>/
│       ├── backbone_version.json
│       ├── backbone_ref.json
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
| Quarantine | Source role, dataset license, restricted-use inheritance, DOI/citation, Backbone version, sensitive geometry, taxonomic anchor, attribution, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, dataset/product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/aggregation receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/fauna/gbif/
→ data/processed/fauna/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Fauna lane and the GBIF source family.
- [ ] Confirm whether the captured material is occurrence API output, async download output, dataset metadata, Backbone taxonomy support, or a mixed package.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, product/surface identity, dataset license, citation, attribution, sensitivity posture, Backbone version where used, and hash posture.
- [ ] Confirm synchronous occurrence API output is not used as publication-class evidence unless paired with replay-stable evidence such as a Download DOI or governed cached fixture.
- [ ] Confirm GBIF is not being used as sole taxonomic authority where ITIS applies, specimen authority, rights authority, or public-release authority.
- [ ] Confirm sensitive taxa, exact geometry, restricted-use upstream datasets, observer/collector-like fields, and media references are handled by fail-closed policy before downstream use.
- [ ] Confirm rights, current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested GBIF Fauna RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/fauna/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| GBIF source docs identify GBIF as both biodiversity occurrence aggregator and taxonomic backbone/crosswalk source. | **CONFIRMED by GitHub contents API during this edit** |
| GBIF source docs say per-dataset licensing, sensitivity, Download DOI capture, and Backbone version capture matter for downstream use. | **CONFIRMED by GitHub contents API during this edit** |
| GBIF source docs say connectors do not publish and write only to RAW or QUARANTINE. | **CONFIRMED by GitHub contents API during this edit** |
| Actual GBIF RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, DOI capture, receipts, validators, fixtures, CI checks, geoprivacy controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, taxonomic final authority, specimen authority, exact public occurrence authority, public artifact authority, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/sources/catalog/gbif/README.md`](../../../../docs/sources/catalog/gbif/README.md)
- [`../../../../docs/sources/catalog/gbif/occurrence-api.md`](../../../../docs/sources/catalog/gbif/occurrence-api.md)
- [`../../../../docs/sources/catalog/gbif/async-download.md`](../../../../docs/sources/catalog/gbif/async-download.md)
- [`../../../../docs/sources/catalog/gbif/dataset-metadata.md`](../../../../docs/sources/catalog/gbif/dataset-metadata.md)
- [`../../../../docs/sources/catalog/gbif/backbone-taxonomy.md`](../../../../docs/sources/catalog/gbif/backbone-taxonomy.md)
- [`../../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../../docs/domains/fauna/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/fauna/POLICY.md`](../../../../docs/domains/fauna/POLICY.md)
- [`../../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../../docs/domains/fauna/CANONICAL_PATHS.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../connectors/gbif/README.md`](../../../../connectors/gbif/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a GBIF Fauna RAW source-family lane for source capture only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, taxonomic final authority, specimen authority, exact public occurrence authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
