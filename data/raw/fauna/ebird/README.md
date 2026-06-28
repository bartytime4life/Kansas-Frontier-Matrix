<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/ebird/readme
name: eBird Raw Fauna README
path: data/raw/fauna/ebird/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <fauna-domain-steward>
  - <fauna-source-steward>
  - <ebird-source-steward>
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
source_family: ebird
source_role: observed
artifact_family: immutable-ebird-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; restricted-use-needs-verification; sensitive-species-deny-by-default; observer-privacy-review-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/fauna/README.md
  - ../../../processed/fauna/README.md
  - ../../../catalog/domain/fauna/README.md
  - ../../../published/layers/fauna/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/sources/catalog/ebird/README.md
  - ../../../../docs/sources/catalog/ebird/ebird-api.md
  - ../../../../docs/sources/catalog/ebird/ebird-basic-dataset.md
  - ../../../../docs/sources/catalog/ebird/sampling-event-data.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../../docs/domains/fauna/POLICY.md
  - ../../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - fauna
  - ebird
  - birds
  - observed
  - citizen-science
  - sensitive-species
  - observer-privacy
  - restricted-use
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested eBird Fauna RAW source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/fauna/README.md` is currently a greenfield stub, so this child file stays source-family-lane bounded."
  - "eBird records are treated as observed community/citizen-science occurrence source material, not specimen-backed evidence and not public release authority."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, observer-privacy controls, sensitivity policies, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# eBird RAW Fauna Lane

RAW source-family lane for immutable eBird source captures and source-admission sidecars in the Fauna domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Source family: eBird" src="https://img.shields.io/badge/source-eBird-1f6feb">
  <img alt="Source role: observed" src="https://img.shields.io/badge/source%20role-observed-228be6">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [eBird product posture](#ebird-product-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/fauna/ebird/` is a no-public-path RAW source-family lane. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity authority, policy authority, public API/UI material, release authority, specimen authority, exact public occurrence authority, or generated-answer authority.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for eBird material admitted to the Fauna lane.

KFM treats eBird as an observed community/citizen-science avian occurrence source. eBird records may support coverage and occurrence evidence after admission, but they are not specimen-backed evidence, do not displace specimen records, and do not become public map or answer authority merely because they were captured.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, which product surface was used, what role it carried, and which identifiers, times, rights, citations, attribution, hashes, sensitivity flags, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/fauna/ebird/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `fauna` |
| Source family | `ebird` |
| Default source role | `observed` |
| Artifact role | RAW source-family lane for eBird captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/fauna/` or `data/quarantine/fauna/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, observer privacy, sensitive-species handling, taxonomy, time, geometry, citation, validation, correction, rollback, or release support is insufficient |

---

## eBird product posture

| Product / surface | RAW handling | Boundary |
|---|---|---|
| eBird API | Source capture for recent or regional observation views when admitted. | Operational coverage source; not specimen evidence or public release authority. |
| eBird Basic Dataset (EBD) | Source capture for bulk occurrence records when access, rights, and product state are recorded. | Restricted-use posture; public derivatives default to DENY or REVIEW until policy and release gates close. |
| Sampling Event Data (SED) | Companion effort/checklist source capture when paired with EBD or separately admitted. | Observer privacy and join-key exposure require separate review before any public use. |
| eBird via GBIF / EOD | Crosswalked source capture only when provider and upstream source are preserved. | GBIF redistribution does not erase upstream eBird rights or attribution duties. |
| Mixed or incomplete package | Capture source reference and route to review. | Do not flatten API, EBD, SED, GBIF redistribution, aggregate, or interpretation outputs into one source-role meaning. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- eBird API response references, EBD references, SED references, or restricted raw payload references;
- product identity, source identity, checklist/observation identifiers where present, species code fields, effort metadata references, event/source time, retrieval time, source version, citation, attribution, rights posture, sensitivity hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| eBird product/source doctrine | `docs/sources/catalog/ebird/` |
| Fauna domain doctrine | `docs/domains/fauna/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, redaction, observer privacy, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/fauna/` |
| Normalized working material | `data/work/fauna/` |
| Validated Fauna objects | `data/processed/fauna/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, redaction, aggregation, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Specimen-backed authority, exact public occurrence authority, sensitive-site authority, or observer-privacy authority | Owning governed downstream/policy/proof lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/fauna/ebird/
├── README.md
├── api/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── response_ref.json
│       ├── checksums.sha256
│       └── README.md
├── ebd/
│   └── <release_or_run_id>/
│       ├── source_reference.json
│       ├── ebd_ref.json
│       ├── rights_ref.json
│       ├── checksums.sha256
│       └── README.md
├── sed/
│   └── <release_or_run_id>/
│       ├── source_reference.json
│       ├── sed_ref.json
│       ├── observer_privacy_review_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, species authority, observer-privacy authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, restricted-use terms, observer privacy, sensitive-species handling, taxonomy, event/source time, geometry/support, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/aggregation/privacy receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/fauna/ebird/
→ data/processed/fauna/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Fauna lane and the eBird source family.
- [ ] Confirm the correct product subfolder or create a documented child README before adding payloads.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, product identity, source role, rights, cadence, citation, attribution, sensitivity posture, and hash posture.
- [ ] Confirm eBird observations are not treated as specimen-backed evidence or allowed to displace specimen records in dedupe.
- [ ] Confirm sensitive species, exact geometry, checklist locations, observer identifiers, group identifiers, and comments are handled by deny-by-default policy and review before downstream use.
- [ ] Confirm rights, current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested eBird Fauna RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/fauna/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| eBird family source docs identify API, EBD, and SED as distinct products under the eBird source family. | **CONFIRMED by GitHub contents API during this edit** |
| eBird source docs assign eBird to observed community/citizen-science occurrence material and distinguish it from specimen-backed evidence. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, with no public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual eBird RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, observer-privacy controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, specimen authority, exact public occurrence authority, public artifact authority, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/sources/catalog/ebird/README.md`](../../../../docs/sources/catalog/ebird/README.md)
- [`../../../../docs/sources/catalog/ebird/ebird-api.md`](../../../../docs/sources/catalog/ebird/ebird-api.md)
- [`../../../../docs/sources/catalog/ebird/ebird-basic-dataset.md`](../../../../docs/sources/catalog/ebird/ebird-basic-dataset.md)
- [`../../../../docs/sources/catalog/ebird/sampling-event-data.md`](../../../../docs/sources/catalog/ebird/sampling-event-data.md)
- [`../../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../../docs/domains/fauna/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/fauna/POLICY.md`](../../../../docs/domains/fauna/POLICY.md)
- [`../../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../../docs/domains/fauna/CANONICAL_PATHS.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is an eBird Fauna RAW source-family lane for source capture only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, specimen authority, exact public occurrence authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
