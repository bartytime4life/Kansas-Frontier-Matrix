<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/natureserve/readme
title: NatureServe Raw Fauna README
path: data/raw/fauna/natureserve/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <fauna-domain-steward>
  - <fauna-source-steward>
  - <natureserve-source-steward>
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
responsibility: Preserve the tracked NatureServe Fauna RAW compatibility and reference documentation without treating this source-named lane as a physical source-first capture home or duplicating RAW bytes.
domain: fauna
source_family: natureserve
source_role: authority-context
artifact_family: fauna-natureserve-raw-compatibility-reference
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; controlled-access-needs-verification; sensitive-rank-fail-closed; provider-permissions-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/fauna/README.md
  - ../../../processed/fauna/README.md
  - ../../../catalog/domain/fauna/README.md
  - ../../../published/layers/fauna/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../../docs/domains/fauna/POLICY.md
  - ../../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../../docs/architecture/ecology-cross-domain.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../connectors/natureserve/README.md
  - ../../../../connectors/natureserve/explorer/README.md
  - ../../habitat/natureserve/README.md
  - ../../flora/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - fauna
  - natureserve
  - conservation-status
  - heritage-ranks
  - authority-context
  - sensitive-rank
  - geoprivacy
  - controlled-access
  - no-public-path
  - evidence-first
  - compatibility-reference
  - source-first
notes:
  - "This README documents the requested NatureServe Fauna RAW source-family lane as compatibility/reference documentation."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/fauna/README.md` was a greenfield stub when this README was first authored on 2026-06-27; it is now the reconciled Fauna compatibility/reference index, and this child stays source-family-lane bounded."
  - "Current-session evidence confirms NatureServe as a Fauna heritage/status source family and confirms connector-family/explorer lanes; a dedicated `docs/sources/catalog/natureserve/` source profile was not confirmed in that 2026-06-27 session; a README at that path is present at `main@9e8bf3e6`, but its authority remains NEEDS VERIFICATION."
  - "NatureServe material is source material for status/sensitivity/context workflows, not public release authority, taxonomic final authority, occurrence truth by itself, or conservation-status final truth without governed downstream closure."
  - "Payload presence, SourceDescriptor records, connector activation, provider permissions, receipts, validators, fixtures, CI enforcement, geoprivacy controls, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NatureServe RAW Fauna Lane

Compatibility and reference documentation for NatureServe-facing Fauna RAW topology — Explorer-service references, status/rank context, data-sensitivity hints, and source-admission references; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Source family: NatureServe" src="https://img.shields.io/badge/source-NatureServe-1f6feb">
  <img alt="Role: authority context" src="https://img.shields.io/badge/role-authority%20context-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [NatureServe source posture](#natureserve-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/fauna/natureserve/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named lane is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity policy authority, release authority, taxonomic final authority, exact public occurrence authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents tracked NatureServe-facing Fauna source material and legacy source-named RAW topology. It may reference one governed source-first NatureServe capture, but it does not establish where that capture is stored. The Habitat-facing [`natureserve`](../../habitat/natureserve/README.md) lane documents the same upstream NatureServe source, and the [Flora RAW hold](../../flora/README.md) carries a `.gitkeep`-only `natureserve/` label; all of these lanes must reference the same single source-first NatureServe capture, never two copies.

KFM treats NatureServe / natural-heritage-style material as a heritage, conservation-status, rank, and sensitivity-context source family. NatureServe ranks and data-sensitivity signals may help drive sensitivity review, but they do not replace KFM policy, SourceDescriptor admission, EvidenceBundle closure, RedactionReceipt requirements, or release decisions.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture records what was admitted, where it came from, which NatureServe surface or service was used, what role it carried, and which identifiers, times, rights, citations, rank fields, sensitivity fields, hashes, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/fauna/natureserve/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `fauna` |
| Source family | `natureserve` |
| Source role | `authority` / `context` for status, rank, heritage, and sensitivity support; exact role set by SourceDescriptor |
| Artifact role | Compatibility/reference lane for NatureServe-facing Fauna source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Fauna WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, provider permission, access tier, rights, citation, rank semantics, data-sensitivity class, taxon identity, validation, correction, rollback, or release support is insufficient |

---

## NatureServe source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable NatureServe capture identity; references here may support Fauna without duplicating RAW bytes. | A second Fauna-scoped copy of a capture held elsewhere is not permitted. |
| Physical placement is held | Do not infer `data/raw/fauna/natureserve/` or any product subdirectory as the capture home. | Use only an accepted writer/path contract; none is established by this README. |
| Conservation-status or rank response | May be captured at the accepted source-first RAW home when admitted; this lane may hold a governed reference only. | Rank capture does not bypass KFM policy, review, catalog, or release gates. |
| Data-sensitivity flag or category | Preserve as source evidence for review. | Source-side sensitivity is an input to KFM policy, not a substitute for KFM redaction/release decisions. |
| Explorer taxon/search/export response | Preserve request criteria, result metadata, source time, retrieval time, identifiers, citation, and digest. | Connector/service output is source admission only and does not decide conservation truth. |
| Controlled-access or unclear-permission material | Route to restricted review or quarantine. | Do not publish or derive public artifacts until provider permissions and rights gates close. |
| Cross-domain flora/habitat/context material | Preserve domain relation and route to owning downstream lane. | Fauna RAW does not become Flora, Habitat, or ecology doctrine. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this tracked README;
- links to canonical SourceDescriptor, source-admission, rights, sensitivity, and connector authority;
- references to a governed source-first NatureServe capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; it must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

Wherever an accepted contract places it, the governed source-first NatureServe capture (or a reference to it) is expected to carry or point to:

- source-reference manifests;
- NatureServe Explorer response references, export/job references, taxon/search result references, domain-values references, data-sensitivity references, provider/source references, or restricted raw payload references;
- request parameters, source identifiers, element/global identifiers where exposed, rank/status fields, provider fields, data-sensitivity fields, source time, retrieval time, citation, rights/access posture, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, job status records where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Fauna. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
| NatureServe source/product doctrine | `docs/sources/catalog/natureserve/` if accepted; currently NEEDS VERIFICATION in this session |
| Fauna domain doctrine | `docs/domains/fauna/` |
| Flora or Habitat doctrine | `docs/domains/flora/`, `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/natureserve/` and child connector lanes |
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
| Taxonomic final authority, exact public occurrence authority, public conservation-status authority, or public answer authority | Owning governed downstream/policy/proof lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/fauna/natureserve/
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Earlier drafts of this README sketched an `explorer/<run_id>/` folder (`source_reference.json`, `request_parameters.json`, `explorer_response_ref.json`, `rights_access_review_ref.json`, `checksums.sha256`, per-run `README.md`), a `data-sensitivity/<run_id>/` folder (`source_reference.json`, `sensitivity_ref.json`, `review_reason.json`, `checksums.sha256`, per-run `README.md`), and a `domain-values/<run_id>/` folder (`source_reference.json`, `domain_values_ref.json`, `checksums.sha256`, per-run `README.md`), plus an optional RAW-local index. Treat that layout as a *proposed shape for a future accepted source-first home, not this subtree*. Do not add a product directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Any such local index, wherever it is accepted, is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, conservation-status authority, taxonomic authority, rights authority, geoprivacy authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, provider permission, access tier, rights, data-sensitivity class, taxon identity, citation, attribution, digest, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Fauna WORK only when SourceDescriptor, rights/access posture, source role, product/surface identity, citation, hash, and minimal validation support are sufficient for normalization. |
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

- [ ] Confirm one registered `source_id` and one immutable source-first NatureServe capture identity; do not create a second Fauna-scoped copy.
- [ ] Treat this README as compatibility/reference documentation only; do not create a product subdirectory or child directory as a payload destination.
- [ ] Confirm whether the captured material is Explorer response, export/job output, domain-values support, data-sensitivity support, provider metadata, or a mixed package.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, provider/access posture, rights, cadence, citation, data-sensitivity posture, taxonomy-anchor posture, and hash posture.
- [ ] Confirm NatureServe material is not being used as release authority, SourceDescriptor authority, KFM policy authority, taxonomic final authority, or exact public occurrence authority.
- [ ] Confirm controlled-access terms, provider permissions, data-sensitivity flags, exact geometry, and sensitive taxa are handled by fail-closed policy before downstream use.
- [ ] Confirm rights, current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested NatureServe Fauna RAW source-family lane boundary as compatibility/reference documentation. | **CONFIRMED authored; reframed 2026-10-11** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/fauna/README.md` was a greenfield stub when this README was first authored. | **CONFIRMED by GitHub contents API during the original 2026-06-27 edit; superseded — the parent is now the reconciled Fauna compatibility/reference index** |
| Fauna source registry doctrine identifies NatureServe / natural-heritage as a Fauna heritage/status source family. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna source registry doctrine says rights/current terms for source families need verification and sensitive joins fail closed. | **CONFIRMED by GitHub contents API during this edit** |
| NatureServe connector docs say connector output may enter raw or quarantine only and rights/sensitivity/public-release posture fail closed until verified. | **CONFIRMED by GitHub contents API during this edit** |
| A dedicated `docs/sources/catalog/natureserve/` source-family profile exists and is authoritative. | **NEEDS VERIFICATION** — a README is present at that path at `main@9e8bf3e6`; its authority is not established here |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual NatureServe RAW payloads exist under this subtree. | **No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN; none added or moved by this documentation correction** |
| SourceDescriptor records, connector activation, provider permissions, receipts, validators, fixtures, CI checks, geoprivacy controls, and downstream receipts are wired to an accepted source-first RAW writer for this source family. | **NEEDS VERIFICATION** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| This README is proof, receipt, release, catalog, registry, policy, taxonomic final authority, conservation-status final authority, exact public occurrence authority, public artifact authority, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../../docs/domains/fauna/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/fauna/POLICY.md`](../../../../docs/domains/fauna/POLICY.md)
- [`../../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../../docs/domains/fauna/CANONICAL_PATHS.md)
- [`../../../../docs/architecture/ecology-cross-domain.md`](../../../../docs/architecture/ecology-cross-domain.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../connectors/natureserve/README.md`](../../../../connectors/natureserve/README.md)
- [`../../../../connectors/natureserve/explorer/README.md`](../../../../connectors/natureserve/explorer/README.md)
- [`../../habitat/natureserve/README.md`](../../habitat/natureserve/README.md)
- [`../../flora/README.md`](../../flora/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a NatureServe-facing Fauna compatibility/reference lane. One governed source-first capture may support Fauna without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, sensitivity policy authority, proof authority, receipt authority, release authority, catalog authority, taxonomic final authority, conservation-status final authority, exact public occurrence authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
