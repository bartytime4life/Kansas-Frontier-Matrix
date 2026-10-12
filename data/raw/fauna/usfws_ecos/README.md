<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/usfws-ecos/readme
title: USFWS ECOS Raw Fauna README
path: data/raw/fauna/usfws_ecos/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <fauna-domain-steward>
  - <habitat-domain-steward>
  - <fauna-source-steward>
  - <usfws-ecos-source-steward>
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
responsibility: Preserve the tracked USFWS ECOS Fauna RAW compatibility and reference documentation without treating this source-named lane as a physical source-first capture home or duplicating RAW bytes.
domain: fauna
adjacent_domain: habitat
source_family: usfws_ecos
source_role: regulatory-authority-plus-administrative-context
artifact_family: fauna-usfws-ecos-raw-compatibility-reference
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; federal-register-reality-boundary; sensitive-joins-fail-closed; ipac-project-review-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/fauna/README.md
  - ../../../processed/fauna/README.md
  - ../../../catalog/domain/fauna/README.md
  - ../../../published/layers/fauna/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/sources/catalog/usfws_ecos/README.md
  - ../../../../docs/sources/catalog/usfws_ecos/species-profiles.md
  - ../../../../docs/sources/catalog/usfws_ecos/esa-listing-status.md
  - ../../../../docs/sources/catalog/usfws_ecos/critical-habitat.md
  - ../../../../docs/sources/catalog/usfws_ecos/ipac-project-lists.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../../docs/domains/fauna/POLICY.md
  - ../../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../../docs/architecture/source-roles.md
  - ../../habitat/usfws-ecos/README.md
  - ../../flora/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - fauna
  - habitat-adjacent
  - usfws
  - ecos
  - esa
  - regulatory
  - authority-source
  - critical-habitat
  - conservation-status
  - federal-register
  - sensitive-join
  - no-public-path
  - evidence-first
  - compatibility-reference
  - source-first
notes:
  - "This README documents the requested USFWS ECOS Fauna RAW source-family lane as compatibility/reference documentation."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/fauna/README.md` was a greenfield stub when this README was first authored on 2026-06-27; it is now the reconciled Fauna compatibility/reference index, and this child stays source-family-lane bounded."
  - "USFWS ECOS is treated as a federal regulatory/authority carrier for status and critical-habitat source material, with ECOS species profiles as administrative context; the Federal Register remains the legal/reality boundary for listed status and designated critical habitat."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, sensitive-join controls, IPaC credential handling, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USFWS ECOS RAW Fauna Lane

Compatibility and reference documentation for USFWS ECOS-facing Fauna RAW topology, with Habitat adjacency for critical-habitat surfaces; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Adjacent: habitat" src="https://img.shields.io/badge/adjacent-habitat-6f42c1">
  <img alt="Source family: USFWS ECOS" src="https://img.shields.io/badge/source-USFWS%20ECOS-1f6feb">
  <img alt="Role: regulatory authority" src="https://img.shields.io/badge/role-regulatory%20authority-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [USFWS ECOS source posture](#usfws-ecos-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/fauna/usfws_ecos/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named lane is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity policy authority, release authority, occurrence evidence, public API/UI material, or generated-answer authority. Public clients and normal UI surfaces must not read this lane directly.

---

## Scope

This directory documents tracked USFWS ECOS-facing Fauna source material and legacy source-named RAW topology. It may reference one governed source-first USFWS ECOS capture, but it does not establish where that capture is stored. The Habitat-facing [`usfws-ecos`](../../habitat/usfws-ecos/README.md) lane documents the same upstream USFWS ECOS source, and the [Flora RAW hold](../../flora/README.md) carries a `.gitkeep`-only `usfws_ecos/` label; all of these lanes must reference the same single source-first USFWS ECOS capture, never two copies.

KFM treats USFWS ECOS as a federal regulatory and authority carrier for ESA listing/status, critical-habitat, IPaC project-list, and species-profile source material. The Federal Register rule remains the legal/reality boundary for listed status and designated critical habitat; ECOS carries and exposes source material for governed KFM use.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture records what was admitted, where it came from, which ECOS surface or product was used, what source role it carried, and which identifiers, times, rights, citations, rule references, geometry/support notes, sensitivity labels, hashes, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/fauna/usfws_ecos/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `fauna` |
| Adjacent domain | `habitat` for critical-habitat surfaces and habitat joins |
| Source family | `usfws_ecos` |
| Source role | `regulatory` for ESA listing/status, critical habitat, and IPaC; `administrative` for species-profile narrative/reference graph |
| Artifact role | Compatibility/reference lane for USFWS ECOS-facing Fauna source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Fauna or Habitat WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, Federal Register reference, API/product identity, IPaC credential posture, rights/citation, sensitive-join risk, geometry support, validation, correction, rollback, or release support is insufficient |

---

## USFWS ECOS source posture

| ECOS surface | RAW handling | Boundary |
|---|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable USFWS ECOS capture identity; references here may support Fauna without duplicating RAW bytes. | A second Fauna-scoped copy of a capture held elsewhere is not permitted. |
| Physical placement is held | Do not infer `data/raw/fauna/usfws_ecos/` or any product subdirectory as the capture home. | Use only an accepted writer/path contract; none is established by this README. |
| ESA listing/status records | Capture as `regulatory` source material when admitted. | Status text is not occurrence evidence and does not prove where an animal was observed. |
| Final/proposed critical habitat | Capture as regulatory geometry/source support, usually Habitat-adjacent. | KFM-derived geometry requires generalization/sensitivity labels before publication; sensitive joins fail closed. |
| IPaC project species list | Capture only when source activation, credential, project-scope, and policy posture are documented. | Project-scoped lists may be sensitive and require policy review before any public use. |
| Species profile narrative/reference graph | Capture as `administrative` context. | Profile narrative explains and links; it is not the legal determination itself. |
| Direct ECOS URL reference | Preserve as source reference and citation. | Link-only references do not authorize KFM republication or derivative public layers. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this tracked README;
- links to canonical SourceDescriptor, source-admission, rights, sensitivity, and connector authority;
- references to a governed source-first USFWS ECOS capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; it must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

Wherever an accepted contract places it, the governed source-first USFWS ECOS capture (or a reference to it) is expected to carry or point to:

- source-reference manifests;
- ECOS listing/status response references, critical-habitat service references, IPaC list references, species-profile narrative/reference-graph references, or restricted raw payload references;
- Federal Register citation references, ECOS species identifiers, entity identifiers, request parameters, service URLs, issue/retrieval times, status/proposal/final flags, geometry/support notes, no-warranty/disclaimer notes, citation, attribution, rights posture, sensitivity hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, job/status records where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Fauna. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
| USFWS ECOS source/product doctrine | `docs/sources/catalog/usfws_ecos/` |
| Fauna or Habitat domain doctrine | `docs/domains/fauna/`, `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/usfws_ecos/` or accepted connector home if/when present |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, geoprivacy, sensitive-join, redaction, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/fauna/` |
| Normalized working material | `data/work/fauna/` or `data/work/habitat/` |
| Validated Fauna/Habitat objects | `data/processed/fauna/` or `data/processed/habitat/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, redaction, aggregation, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Observed occurrence evidence, state heritage rank authority, NatureServe sensitivity authority, KDWP state-status authority, or public answer authority | Owning governed downstream/policy/proof lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/fauna/usfws_ecos/
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Earlier drafts of this README sketched `esa-listing-status/<run_id>/` (`source_reference.json`, `request_parameters.json`, `listing_status_ref.json`, `federal_register_ref.json`), `critical-habitat/<run_id>/` (`source_reference.json`, `service_ref.json`, `geometry_support_ref.json`, `sensitivity_review_ref.json`), `ipac-project-lists/<run_id>/` (`source_reference.json`, `project_scope_ref.json`, `list_ref.json`, `policy_review_ref.json`), and `species-profiles/<run_id>/` (`source_reference.json`, `narrative_ref.json`, `reference_graph_ref.json`) folders, each also carrying `checksums.sha256` and a per-run `README.md`, plus an optional RAW-local index. Treat that layout as a *proposed shape for a future accepted source-first home, not this subtree*. Do not add a product directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Any such local index, wherever it is accepted, is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, legal authority, occurrence authority, rights authority, sensitive-join authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, Federal Register reference, product identity, rights/citation, project-scope sensitivity, sensitive-join risk, geometry support, attribution, digest, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Fauna or Habitat WORK only when SourceDescriptor, rights/citation posture, source role, product/surface identity, Federal Register reference where needed, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/generalization receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/fauna/ or data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first USFWS ECOS capture identity; do not create a second Fauna- or Habitat-scoped copy, and record Habitat adjacency where critical-habitat material is involved.
- [ ] Treat this README as compatibility/reference documentation only; do not create a product subdirectory or child directory as a payload destination.
- [ ] Confirm whether the captured material is ESA listing/status, critical-habitat geometry/service support, IPaC project-list support, species-profile narrative/reference graph, or a mixed package.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, product/surface identity, Federal Register reference where required, rights/citation posture, sensitive-join posture, and hash posture.
- [ ] Confirm ECOS regulatory material is not being cited as observed occurrence evidence.
- [ ] Confirm species-profile narrative is not being treated as the legal determination itself.
- [ ] Confirm KFM-derived critical-habitat geometry is not published without generalization/sensitivity labels, receipts, review state, and release state.
- [ ] Confirm IPaC project-scoped material has credential, project-scope, privacy/sensitivity, and policy posture recorded before any downstream use.
- [ ] Confirm rights, current terms, citation, no-warranty/disclaimer handling, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested USFWS ECOS Fauna RAW source-family lane boundary as compatibility/reference documentation. | **CONFIRMED authored; reframed 2026-10-11** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/fauna/README.md` was a greenfield stub when this README was first authored. | **CONFIRMED by GitHub contents API during the original 2026-06-27 edit; superseded — the parent is now the reconciled Fauna compatibility/reference index** |
| USFWS ECOS source docs identify ECOS as a regulatory/authority carrier for ESA listing/status, critical habitat, and IPaC project-list support. | **CONFIRMED by GitHub contents API during this edit** |
| USFWS ECOS source docs say the Federal Register rule is the legal source and ECOS is the carrier. | **CONFIRMED by GitHub contents API during this edit** |
| USFWS ECOS source docs say source role is regulatory for listing/status/critical habitat/IPaC and administrative for species-profile narrative/reference graph. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, with no public access. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual USFWS ECOS RAW payloads exist under this subtree. | **No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN; none added or moved by this documentation correction** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, sensitive-join controls, IPaC credential handling, and downstream receipts are wired to an accepted source-first RAW writer for this source family. | **NEEDS VERIFICATION** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| This README is proof, receipt, release, catalog, registry, policy, observed occurrence evidence, public artifact authority, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/sources/catalog/usfws_ecos/README.md`](../../../../docs/sources/catalog/usfws_ecos/README.md)
- [`../../../../docs/sources/catalog/usfws_ecos/species-profiles.md`](../../../../docs/sources/catalog/usfws_ecos/species-profiles.md)
- [`../../../../docs/sources/catalog/usfws_ecos/esa-listing-status.md`](../../../../docs/sources/catalog/usfws_ecos/esa-listing-status.md)
- [`../../../../docs/sources/catalog/usfws_ecos/critical-habitat.md`](../../../../docs/sources/catalog/usfws_ecos/critical-habitat.md)
- [`../../../../docs/sources/catalog/usfws_ecos/ipac-project-lists.md`](../../../../docs/sources/catalog/usfws_ecos/ipac-project-lists.md)
- [`../../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../../docs/domains/fauna/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/fauna/POLICY.md`](../../../../docs/domains/fauna/POLICY.md)
- [`../../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../../docs/domains/fauna/CANONICAL_PATHS.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../habitat/usfws-ecos/README.md`](../../habitat/usfws-ecos/README.md)
- [`../../flora/README.md`](../../flora/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a USFWS ECOS-facing Fauna compatibility/reference lane. One governed source-first capture may support Fauna without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, sensitivity policy authority, proof authority, receipt authority, release authority, catalog authority, observed occurrence evidence, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
