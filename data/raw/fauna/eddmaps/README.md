<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/eddmaps/readme
name: EDDMapS Raw Fauna README
path: data/raw/fauna/eddmaps/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <fauna-domain-steward>
  - <fauna-source-steward>
  - <eddmaps-source-steward>
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
source_family: eddmaps
source_role: observed-plus-aggregator
artifact_family: immutable-eddmaps-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; rights-needs-verification; sensitive-joins-fail-closed; private-flag-quarantine; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/fauna/README.md
  - ../../../processed/fauna/README.md
  - ../../../catalog/domain/fauna/README.md
  - ../../../published/layers/fauna/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/sources/catalog/eddmaps/README.md
  - ../../../../docs/sources/catalog/eddmaps/invasive-species-observations.md
  - ../../../../docs/sources/catalog/eddmaps/advanced-query-download.md
  - ../../../../docs/sources/catalog/eddmaps/state-species-lists.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../../docs/domains/fauna/POLICY.md
  - ../../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../connectors/eddmaps/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - fauna
  - eddmaps
  - invasive-species
  - observed
  - aggregator
  - verifier-gated
  - sensitive-geometry
  - geoprivacy
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested EDDMapS Fauna RAW source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/fauna/README.md` is currently a greenfield stub, so this child file stays source-family-lane bounded."
  - "EDDMapS is treated as mixed observation plus aggregator source material for invasive-species records, not regulatory authority, emergency guidance, taxonomic authority, or public release authority."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, geoprivacy controls, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EDDMapS RAW Fauna Lane

RAW source-family lane for immutable EDDMapS source captures and source-admission sidecars in the Fauna domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Source family: EDDMapS" src="https://img.shields.io/badge/source-EDDMapS-1f6feb">
  <img alt="Role: observed + aggregator" src="https://img.shields.io/badge/role-observed%20%2B%20aggregator-228be6">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [EDDMapS source posture](#eddmaps-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/fauna/eddmaps/` is a no-public-path RAW source-family lane. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity authority, policy authority, regulatory authority, taxonomic authority, emergency guidance, exact public occurrence authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for EDDMapS material admitted to the Fauna lane.

KFM treats EDDMapS as mixed observation plus aggregator source material for invasive-species records. Upstream verifier status may be useful evidence metadata, but it does not satisfy KFM validation, policy, evidence, catalog, or release gates by itself.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, which query or product surface was used, what role it carried, and which identifiers, times, rights, citations, hashes, sensitivity flags, geoprivacy flags, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/fauna/eddmaps/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `fauna` |
| Source family | `eddmaps` |
| Source role | `observed` primary with aggregator annotation where applicable |
| Artifact role | RAW source-family lane for EDDMapS captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/fauna/` or `data/quarantine/fauna/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, upstream private flag, sensitive join, taxonomy, time, geometry, citation, validation, correction, rollback, or release support is insufficient |

---

## EDDMapS source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Verifier-gated invasive observation | May use this lane as RAW source capture when admitted. | Upstream review is evidence metadata, not KFM release approval. |
| Aggregated upstream record | Preserve EDDMapS identity and upstream source hints where exposed. | Do not collapse aggregator identity into the upstream authority. |
| Private or sensitive-location record | Route to quarantine or restricted review before downstream use. | No exact public exposure without redaction/review closure. |
| State species list pointer | Capture only as source context if admitted. | EDDMapS is not the Kansas regulatory authority. |
| Flora-relevant invasive-plant record | Preserve cross-lane relation. | Flora owns `InvasivePlantRecord`; Fauna owns fauna-side invasive records. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- EDDMapS download references, query references, ArcGIS/Hub asset references, or restricted raw payload references;
- source record identifiers, source query parameters, upstream verification state where exposed, source identity, taxon names, event/source time, retrieval time, geometry/support notes, citation, rights posture, sensitivity hints, private-flag hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| EDDMapS source/product doctrine | `docs/sources/catalog/eddmaps/` |
| Fauna domain doctrine | `docs/domains/fauna/` |
| Flora invasive-plant object doctrine | `docs/domains/flora/` and `contracts/domains/flora/` |
| Connector code or connector decisions | `connectors/eddmaps/` or accepted connector home |
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
| Regulatory status authority, taxonomic authority, exact public occurrence authority, or emergency guidance | Owning governed downstream/policy/proof lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/fauna/eddmaps/
├── README.md
├── observations/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── query_parameters.json
│       ├── eddmaps_payload_ref.json
│       ├── checksums.sha256
│       └── README.md
├── state-lists/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── list_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, species authority, regulatory authority, geoprivacy authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, private flag, sensitive join, taxonomy, event/source time, geometry/support, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, product/query identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/aggregation receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/fauna/eddmaps/
→ data/processed/fauna/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Fauna lane and the EDDMapS source family.
- [ ] Confirm whether the captured material is an observation download, state-list pointer, partner asset, or cross-lane Flora-relevant record.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, rights, cadence, citation, upstream verification state, sensitivity posture, and hash posture.
- [ ] Confirm EDDMapS is not being used as regulatory status authority, taxonomic authority, or public-release authority.
- [ ] Confirm sensitive taxa, exact geometry, upstream private flags, reporter/landowner-like fields, and media references are handled by fail-closed policy before downstream use.
- [ ] Confirm rights, current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested EDDMapS Fauna RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/fauna/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| EDDMapS source docs identify EDDMapS as a recognized invasive-source family for Fauna and as mixed observation plus aggregator material. | **CONFIRMED by GitHub contents API during this edit** |
| EDDMapS source docs say rights/current terms need verification and sensitive joins fail closed. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, with no public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual EDDMapS RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, geoprivacy controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, regulatory authority, taxonomic authority, exact public occurrence authority, public artifact authority, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/sources/catalog/eddmaps/README.md`](../../../../docs/sources/catalog/eddmaps/README.md)
- [`../../../../docs/sources/catalog/eddmaps/invasive-species-observations.md`](../../../../docs/sources/catalog/eddmaps/invasive-species-observations.md)
- [`../../../../docs/sources/catalog/eddmaps/advanced-query-download.md`](../../../../docs/sources/catalog/eddmaps/advanced-query-download.md)
- [`../../../../docs/sources/catalog/eddmaps/state-species-lists.md`](../../../../docs/sources/catalog/eddmaps/state-species-lists.md)
- [`../../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../../docs/domains/fauna/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/fauna/POLICY.md`](../../../../docs/domains/fauna/POLICY.md)
- [`../../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../../docs/domains/fauna/CANONICAL_PATHS.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../connectors/eddmaps/README.md`](../../../../connectors/eddmaps/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is an EDDMapS Fauna RAW source-family lane for source capture only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, regulatory authority, taxonomic authority, exact public occurrence authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
