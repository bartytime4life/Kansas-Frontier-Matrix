<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/kdwp/readme
title: Habitat KDWP Raw README
path: data/raw/habitat/kdwp/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <kdwp-source-steward>
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
responsibility: Preserve the tracked Habitat KDWP RAW compatibility and reference documentation without treating this lane as a physical source-first capture home or duplicating RAW bytes.
domain: habitat
source_family: kdwp
source_role: per-product-regulatory-or-observed
artifact_family: habitat-kdwp-raw-compatibility-reference
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; steward-mediated; rights-needs-verification; review-required; release-blocked
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
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - kdwp
  - kansas
  - state-review
  - source-role
  - source-capture
  - no-public-path
  - evidence-first
  - compatibility-reference
  - source-first
notes:
  - "This README replaces placeholder content at `data/raw/habitat/kdwp/README.md`."
  - "Parent `data/raw/habitat/README.md` was a greenfield stub when this README was first authored; it now exists as the Habitat RAW compatibility/reference index."
  - "KDWP material is treated as state review context. State designations and survey observations require separate role handling."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat KDWP RAW Lane

Compatibility/reference lane for Habitat-facing KDWP source documentation and legacy RAW topology; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: KDWP" src="https://img.shields.io/badge/source-KDWP-1f6feb">
  <img alt="Role: per product" src="https://img.shields.io/badge/role-per%20product-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [KDWP source posture](#kdwp-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/habitat/kdwp/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named directory is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed Habitat truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, public API/UI material, release authority, or generated-answer authority.

---

## Scope

This directory documents KDWP material as it bears on Habitat and the legacy Habitat-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

KFM treats KDWP material as Kansas state review context. Per product, KDWP material may carry state designation/list context, survey context, or administrative stewardship context. These roles must be split into separate `SourceDescriptor` records where applicable; this compatibility/reference lane does not collapse them into one authority.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture records what was admitted, where it came from, which KDWP surface or steward-mediated product was used, what role it carried, and which identifiers, times, rights, citations, product flags, geometry/support notes, hashes, review flags, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/kdwp/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `habitat` |
| Source family | `kdwp` |
| Source role | `regulatory` for state designations; `observed` for survey observations; exact role set by SourceDescriptor |
| Artifact role | Compatibility/reference lane for Habitat-facing KDWP source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Habitat WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights/steward terms, product identity, designation/survey split, geometry/support, citation, validation, correction, rollback, or release support is insufficient |

---

## KDWP source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; references may support Habitat without duplicating RAW bytes. | This lane does not create a second Habitat-scoped copy. |
| Physical placement is held | Do not infer `data/raw/habitat/kdwp/` as the capture home; use only an accepted writer/path contract. | None is established by this README. |
| State designation or list | Capture as regulatory or administrative context when admitted. | Designation context does not become occurrence evidence by default. |
| Survey observation context | Capture as observed source material when admitted. | Survey material does not become state designation or public release authority by itself. |
| Steward-mediated material | Route through rights/steward review before downstream use. | Do not infer public permissions from source name alone. |
| Crosswalk to federal or taxonomy sources | Preserve target and owner lane. | USFWS owns federal designation surfaces; Fauna owns taxon/occurrence truth where applicable. |
| Mixed package | Split by SourceDescriptor or quarantine. | One provider may yield multiple roles; one descriptor carries one role. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this tracked README;
- links to canonical SourceDescriptor, admission-ticket, source-admission, rights, sensitivity, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; it must not become proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

The governed source-first capture or reference for KDWP material, not this lane, must carry:

- source-reference manifests;
- KDWP state review references, list references, designation references, survey-context references, steward-provided file references, service references, or restricted raw payload references;
- product type, designation/survey flag, source identifiers, species/taxon references where applicable, state-review fields, source time, retrieval time, source vintage, geometry/support notes, citation, attribution, rights/steward-term posture, review hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Habitat. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
| KDWP/source-family doctrine | `docs/sources/catalog/` or `docs/domains/habitat/` |
| Habitat domain doctrine | `docs/domains/habitat/` |
| Fauna taxon/occurrence doctrine | `docs/domains/fauna/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, redaction, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/habitat/` |
| Normalized working material | `data/work/habitat/` |
| Validated Habitat objects | `data/processed/habitat/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, review, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| State legal-status final truth, observed occurrence truth, federal designation truth, taxonomic truth, habitat suitability truth, or public answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/habitat/kdwp/
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source-run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

The earlier version of this map sketched `state-designations/<run_id>/` (`source_reference.json`, `designation_ref.json`, `crosswalk_ref.json`), `state-review/<run_id>/` (`source_reference.json`, `review_ref.json`), and `survey-context/<run_id>/` (`source_reference.json`, `survey_ref.json`, `geometry_support_ref.json`) folders, each with `checksums.sha256` and a run `README.md`, plus an optional local index. Treat that layout as a proposed shape for a future accepted source-first home, not this subtree.

Any local documentation index accepted later must remain non-authoritative; it is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, legal-status authority, occurrence authority, taxonomic authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, rights/steward terms, product identity, designation/survey split, geometry/support, attribution, citation, digest, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Habitat WORK only when SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/redaction/generalization receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Habitat-scoped copy.
- [ ] Treat this README as compatibility/reference documentation only; do not create a child directory under this lane as a payload destination.
- [ ] Confirm whether the captured material is state designation/list context, survey context, stewardship context, or a mixed package.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, product/surface identity, rights/steward terms, cadence, citation, review posture, and hash posture.
- [ ] Confirm regulatory designation material and observed survey material are split by SourceDescriptor rather than collapsed into one source role.
- [ ] Confirm crosswalks to federal status or Fauna taxonomy preserve ownership boundaries and do not turn KDWP material into federal designation or taxon truth.
- [ ] Confirm rights, endpoint/current terms, citation, steward permissions, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/kdwp/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` was a greenfield stub when this README was first authored; it now exists as the Habitat RAW compatibility/reference index. | **CONFIRMED at reconciliation base `main@9e8bf3e6` (2026-10-11)** |
| Habitat source-family doctrine identifies KDWP as state review context with lists, state designations, and survey context. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-family doctrine says KDWP roles split per product: regulatory for state designations and observed for survey observations. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat source-family doctrine says KDWP rights/terms need verification and sensitive joins require review before public use. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual KDWP RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired to an accepted source-first RAW writer for this source family. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, state legal-status final authority, occurrence authority, public artifact authority, or generated-answer authority. | **DENY** |

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
- `../../../../docs/domains/habitat/POLICY.md` (not present)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat-facing KDWP compatibility/reference lane. One governed source-first capture may support Habitat without duplicated RAW bytes; this lane does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, state legal-status final authority, occurrence authority, habitat-suitability truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
