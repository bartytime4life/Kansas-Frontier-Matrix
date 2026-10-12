<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/eddmaps/readme
title: EDDMapS Raw Fauna README
path: data/raw/fauna/eddmaps/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
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
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked EDDMapS Fauna RAW compatibility and reference documentation without treating this source-named lane as a physical source-first capture home or duplicating RAW bytes.
domain: fauna
source_family: eddmaps
source_role: observed-plus-aggregator
artifact_family: fauna-eddmaps-raw-compatibility-reference
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
  - compatibility-reference
  - source-first
notes:
  - "This README documents the requested EDDMapS Fauna RAW source-family lane as compatibility/reference documentation."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/fauna/README.md` was a greenfield stub when this README was first authored on 2026-06-27; it is now the reconciled Fauna compatibility/reference index, and this child stays source-family-lane bounded."
  - "EDDMapS is treated as mixed observation plus aggregator source material for invasive-species records, not regulatory authority, emergency guidance, taxonomic authority, or public release authority."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, geoprivacy controls, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EDDMapS RAW Fauna Lane

Compatibility and reference documentation for EDDMapS-facing Fauna RAW topology and source-admission references; not a physical source-capture home.

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
> `data/raw/fauna/eddmaps/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named lane is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity authority, policy authority, regulatory authority, taxonomic authority, emergency guidance, exact public occurrence authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory documents tracked EDDMapS-facing Fauna source material and legacy source-named RAW topology. It may reference one governed source-first EDDMapS capture, but it does not establish where that capture is stored.

KFM treats EDDMapS as mixed observation plus aggregator source material for invasive-species records. Upstream verifier status may be useful evidence metadata, but it does not satisfy KFM validation, policy, evidence, catalog, or release gates by itself.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture records what was admitted, where it came from, which query or product surface was used, what role it carried, and which identifiers, times, rights, citations, hashes, sensitivity flags, geoprivacy flags, and caveats must travel with it.

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
| Artifact role | Compatibility/reference lane for EDDMapS-facing Fauna source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Fauna WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
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
| Capture identity is source-first | Register one `source_id` and preserve one immutable EDDMapS capture identity; references here may support Fauna without duplicating RAW bytes. | A second Fauna-scoped copy of a capture held elsewhere is not permitted. |
| Physical placement is held | Do not infer `data/raw/fauna/eddmaps/` or any product subdirectory as the capture home. | Use only an accepted writer/path contract; none is established by this README. |
| Verifier-gated invasive observation | May be captured at the accepted source-first RAW home when admitted; this lane may hold a governed reference only. | Upstream review is evidence metadata, not KFM release approval. |
| Aggregated upstream record | Preserve EDDMapS identity and upstream source hints where exposed. | Do not collapse aggregator identity into the upstream authority. |
| Private or sensitive-location record | Route to quarantine or restricted review before downstream use. | No exact public exposure without redaction/review closure. |
| State species list pointer | Capture only as source context if admitted. | EDDMapS is not the Kansas regulatory authority. |
| Flora-relevant invasive-plant record | Preserve cross-lane relation. | Flora owns `InvasivePlantRecord`; Fauna owns fauna-side invasive records. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this tracked README;
- links to canonical SourceDescriptor, source-admission, rights, sensitivity, and connector authority;
- references to a governed source-first EDDMapS capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; it must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

Wherever an accepted contract places it, the governed source-first EDDMapS capture (or a reference to it) is expected to carry or point to:

- source-reference manifests;
- EDDMapS download references, query references, ArcGIS/Hub asset references, or restricted raw payload references;
- source record identifiers, source query parameters, upstream verification state where exposed, source identity, taxon names, event/source time, retrieval time, geometry/support notes, citation, rights posture, sensitivity hints, private-flag hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Fauna. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Earlier drafts of this README sketched an `observations/<run_id>/` folder (`source_reference.json`, `query_parameters.json`, `eddmaps_payload_ref.json`, `checksums.sha256`, per-run `README.md`) and a `state-lists/<run_id>/` folder (`source_reference.json`, `list_ref.json`, `checksums.sha256`, per-run `README.md`), plus an optional RAW-local index. Treat that layout as a *proposed shape for a future accepted source-first home, not this subtree*. Do not add a product directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Any such local index, wherever it is accepted, is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, species authority, regulatory authority, geoprivacy authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, rights, private flag, sensitive join, taxonomy, event/source time, geometry/support, attribution, citation, digest, schema, source activation, or physical placement is unresolved. |
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

- [ ] Confirm one registered `source_id` and one immutable source-first EDDMapS capture identity; do not create a second Fauna-scoped copy.
- [ ] Treat this README as compatibility/reference documentation only; do not create a product subdirectory or child directory as a payload destination.
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
| This README defines the requested EDDMapS Fauna RAW source-family lane boundary as compatibility/reference documentation. | **CONFIRMED authored; reframed 2026-10-11** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/fauna/README.md` was a greenfield stub when this README was first authored. | **CONFIRMED by GitHub contents API during the original 2026-06-27 edit; superseded — the parent is now the reconciled Fauna compatibility/reference index** |
| EDDMapS source docs identify EDDMapS as a recognized invasive-source family for Fauna and as mixed observation plus aggregator material. | **CONFIRMED by GitHub contents API during this edit** |
| EDDMapS source docs say rights/current terms need verification and sensitive joins fail closed. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, with no public access. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual EDDMapS RAW payloads exist under this subtree. | **No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN; none added or moved by this documentation correction** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, geoprivacy controls, and downstream receipts are wired to an accepted source-first RAW writer for this source family. | **NEEDS VERIFICATION** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
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

KFM rule: this directory is an EDDMapS-facing Fauna compatibility/reference lane. One governed source-first capture may support Fauna without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, proof authority, receipt authority, release authority, catalog authority, regulatory authority, taxonomic authority, exact public occurrence authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
