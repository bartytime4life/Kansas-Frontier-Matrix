<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/inaturalist/readme
title: iNaturalist Raw Fauna README
path: data/raw/fauna/inaturalist/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
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
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked iNaturalist Fauna RAW compatibility and reference documentation without treating this source-named lane as a physical source-first capture home or duplicating RAW bytes.
domain: fauna
source_family: inaturalist
source_family_enum: inat
source_role: observed-aggregator
artifact_family: fauna-inaturalist-raw-compatibility-reference
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
  - ../../habitat/occurrence-context/README.md
  - ../../flora/README.md
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
  - compatibility-reference
  - source-first
notes:
  - "This README documents the requested iNaturalist Fauna RAW source-family lane as compatibility/reference documentation."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/fauna/README.md` was a greenfield stub when this README was first authored on 2026-06-27; it is now the reconciled Fauna compatibility/reference index, and this child stays source-family-lane bounded."
  - "iNaturalist is treated as community-observation occurrence source material, not regulatory authority, legal-status authority, sensitive-location authority, canonical taxonomic authority, or public release authority."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, geoprivacy controls, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# iNaturalist RAW Fauna Lane

Compatibility and reference documentation for iNaturalist-facing Fauna RAW topology and source-admission references; not a physical source-capture home.

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
> `data/raw/fauna/inaturalist/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named lane is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity authority, policy authority, regulatory authority, legal-status authority, exact sensitive-location authority, canonical taxonomic authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory documents tracked iNaturalist-facing Fauna source material and legacy source-named RAW topology. It may reference one governed source-first iNaturalist capture, but it does not establish where that capture is stored. The Habitat-facing [`occurrence-context`](../../habitat/occurrence-context/README.md) lane also documents iNaturalist as occurrence context, and the [Flora RAW hold](../../flora/README.md) carries a `.gitkeep`-only `inaturalist/` label; all of these lanes must reference the same single source-first iNaturalist capture, never two copies.

KFM treats iNaturalist as community-observation occurrence evidence with confidence and quality-state metadata. It is useful as one biodiversity evidence stream, but it is not a replacement for KDWP, USFWS, NatureServe, specimen-backed collections, or taxonomic authority sources.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture records what was admitted, where it came from, which API/product surface was used, what role it carried, and which identifiers, times, licenses, citations, geoprivacy states, sensitivity flags, taxonomy anchors, hashes, and caveats must travel with it.

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
| Artifact role | Compatibility/reference lane for iNaturalist-facing Fauna source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Fauna WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
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
| Capture identity is source-first | Register one `source_id` and preserve one immutable iNaturalist capture identity; references here may support Fauna without duplicating RAW bytes. | A second Fauna-scoped copy of a capture held elsewhere is not permitted. |
| Physical placement is held | Do not infer `data/raw/fauna/inaturalist/` or any product subdirectory as the capture home. | Use only an accepted writer/path contract; none is established by this README. |
| Research-grade observation with normalized CC license | May be captured at the accepted source-first RAW home when admitted; this lane may hold a governed reference only. | Research-grade status does not bypass KFM rights, sensitivity, validation, catalog, or release gates. |
| Non-research-grade / casual observation | Treat as candidate or review-required unless a separate admitted product exists. | Do not silently promote under the research-grade bar. |
| Obscured or private geoprivacy state | Preserve as source evidence and route through sensitivity review. | Do not infer, back-fill, or deobscure exact coordinates. |
| Sensitive taxon or sensitive-site class | Route to quarantine/restricted review before downstream use. | No exact public exposure without redaction/review closure. |
| Taxonomic identification | Preserve source taxon and confidence fields. | Reconcile against ITIS/GBIF Backbone or other controlled authority; iNaturalist is not canonical taxonomy. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this tracked README;
- links to canonical SourceDescriptor, source-admission, rights, sensitivity, and connector authority;
- references to a governed source-first iNaturalist capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; it must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

Wherever an accepted contract places it, the governed source-first iNaturalist capture (or a reference to it) is expected to carry or point to:

- source-reference manifests;
- iNaturalist API response references, observation references, media-reference manifests, or restricted raw payload references;
- observation identifiers, quality grade, license fields, taxon identifiers/names, identification state where exposed, event/source time, retrieval time, geoprivacy state, geometry/support notes, citation, attribution, sensitivity hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Fauna. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Earlier drafts of this README sketched a `research-grade/<run_id>/` folder (`source_reference.json`, `request_parameters.json`, `observations_ref.json`, `license_summary.json`, `geoprivacy_summary.json`, `checksums.sha256`, per-run `README.md`) and a `candidate/<run_id>/` folder (`source_reference.json`, `candidate_observations_ref.json`, `review_reason.json`, `checksums.sha256`, per-run `README.md`), plus an optional RAW-local index. Treat that layout as a *proposed shape for a future accepted source-first home, not this subtree*. Do not add a product directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Any such local index, wherever it is accepted, is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, taxonomic authority, rights authority, geoprivacy authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, quality grade, per-record license, geoprivacy, sensitive taxon/site class, taxonomic anchor, attribution, citation, digest, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Fauna WORK only when SourceDescriptor, rights posture, source role, product/query identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/aggregation receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/fauna/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first iNaturalist capture identity; do not create a second Fauna-scoped copy.
- [ ] Treat this README as compatibility/reference documentation only; do not create a product subdirectory or child directory as a payload destination.
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
| This README defines the requested iNaturalist Fauna RAW source-family lane boundary as compatibility/reference documentation. | **CONFIRMED authored; reframed 2026-10-11** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/fauna/README.md` was a greenfield stub when this README was first authored. | **CONFIRMED by GitHub contents API during the original 2026-06-27 edit; superseded — the parent is now the reconciled Fauna compatibility/reference index** |
| iNaturalist source docs identify it as a community-observation source family, not legal/listed status, regulatory, exact-sensitive-location, or canonical taxonomy authority. | **CONFIRMED by GitHub contents API during this edit** |
| iNaturalist research-grade product docs require research-grade status, normalized CC license, controlled-taxonomy resolution, and geoprivacy preservation. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, with no public access. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual iNaturalist RAW payloads exist under this subtree. | **No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN; none added or moved by this documentation correction** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, geoprivacy controls, and downstream receipts are wired to an accepted source-first RAW writer for this source family. | **NEEDS VERIFICATION** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
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
- [`../../habitat/occurrence-context/README.md`](../../habitat/occurrence-context/README.md)
- [`../../flora/README.md`](../../flora/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is an iNaturalist-facing Fauna compatibility/reference lane. One governed source-first capture may support Fauna without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, regulatory authority, legal-status authority, exact sensitive-location authority, canonical taxonomic authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
