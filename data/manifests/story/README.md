<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-manifests-story-readme
title: data/manifests/story/README.md — Story Manifests Compatibility / Retirement README
version: v0.1
type: readme; data-lifecycle-note; compatibility-retirement-note; story-manifest-note
status: draft; PROPOSED; NON-CANONICAL; compatibility; story; manifests; release-gated; needs-migration-decision
owners: OWNER_TBD — Story steward · Data steward · Release steward · Manifest steward · Evidence steward · Catalog steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; manifests; story; compatibility; non-canonical; release-governance
tags: [kfm, data, manifests, story, story-nodes, release, ReleaseManifest, rollback, correction, receipts, proofs, catalog, publication, ADR-0011]
related:
  - ../README.md
  - ../../README.md
  - ../../../release/README.md
  - ../../../release/manifests/
  - ../../published/
  - ../../catalog/
  - ../../catalog/domain/roads-rail-trade/story-nodes/README.md
  - ../../proofs/
  - ../../receipts/
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
notes:
  - "This file replaces a greenfield stub at `data/manifests/story/README.md`."
  - "The parent `data/manifests/` lane is non-canonical; this Story child is a compatibility/retirement note only."
  - "Story release-level manifests belong under `release/manifests/`; approved story descriptors belong with released artifacts or governed catalog/story-node lanes when allowed."
  - "Do not store story release manifests, story publication approvals, rollback cards, correction notices, receipts, proofs, catalog records, source registries, schemas, policy rules, published artifacts, or executable code here."
  - "Rollback target for this replacement is previous stub blob SHA `81b75075363b2e550ef5ac42b6790a2c6cb6b476`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/manifests/story

> Non-canonical compatibility and retirement README for `data/manifests/story/`. Story release-level manifests belong under `release/manifests/`, not this data root.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Posture: non-canonical" src="https://img.shields.io/badge/posture-non--canonical-red">
  <img alt="Segment: story" src="https://img.shields.io/badge/segment-story-blue">
  <img alt="Canonical: release/manifests" src="https://img.shields.io/badge/canonical-release%2Fmanifests-blue">
  <img alt="Decision: ADR-0011 proposed" src="https://img.shields.io/badge/decision-ADR--0011__PROPOSED-orange">
</p>

**Status:** draft / PROPOSED / NON-CANONICAL  
**Path:** `data/manifests/story/README.md`  
**Owning root:** `data/manifests/` only as a compatibility/retirement child  
**Canonical release-manifest home:** `release/manifests/`  
**Segment:** `story`  
**Exposure posture:** not public; this path must not publish or authorize release  
**Truth posture:** CONFIRMED target was a greenfield stub · CONFIRMED parent `data/manifests/` is non-canonical and must not host trust-bearing manifests · CONFIRMED `release/` owns release decisions and manifests · CONFIRMED ADR-0011 proposes that `data/manifests/` must not exist as a root · NEEDS VERIFICATION for whether this child path should remain as a redirect, be removed, or be migrated.

**Quick jumps:** [Purpose](#purpose) · [Boundary](#boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Guardrails](#guardrails) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/manifests/story/` is not a canonical Story manifest root. It exists only because the path currently exists and needs a clear compatibility boundary while the repository resolves migration and cleanup.

This README prevents the folder from becoming an accidental story-publication or release-manifest root. Release decisions, release manifests, promotion records, rollback cards, withdrawal notices, correction notices, signatures, and release changelogs belong under `release/`.

## Boundary

KFM separates four trust-bearing artifact families:

```text
receipt != proof != catalog != publication
```

A Story manifest that decides or describes a release is a publication/release artifact, not lifecycle data scratch. Story-node catalog records and story descriptors must not replace release decisions, evidence support, policy review, or rollback records.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Story release-level manifests | `release/manifests/` | Canonical release authority. |
| Story release decisions, rollback, correction, withdrawal, signatures, changelog | `release/` | Canonical release-decision root. |
| Public-safe story artifact bytes | `data/published/` | Downstream after release. |
| Story catalog records | `data/catalog/` | Discovery and interchange records. |
| Story-node domain catalog records | `data/catalog/domain/.../story-nodes/` | Domain-scoped story catalog records when verified. |
| Story receipts | `data/receipts/` | Process memory, not release proof alone. |
| Story proof support | `data/proofs/` | EvidenceBundle, ProofPack, CatalogMatrix, integrity bundles. |
| Story source registry | `data/registry/` | SourceDescriptor/source-admission records. |
| Story schemas and policy | `schemas/`, `policy/` | Separate roots. |
| `data/manifests/story/` | Non-canonical compatibility/retirement note | Do not add trust-bearing records here. |

## Accepted contents

Until an accepted ADR/path map says otherwise, accepted contents are limited to:

- This README.
- Migration notes that identify any historical Story use of `data/manifests/story/` and where each artifact moved.
- Redirect/crosswalk notes pointing to `release/manifests/`, `data/published/...`, `data/receipts/`, `data/proofs/`, or `data/catalog/...`.
- Empty placeholder indexes needed only to preserve compatibility during migration.

## Exclusions

Do not store these under `data/manifests/story/`:

- Story `ReleaseManifest` records.
- Story release decisions, promotion records, rollback cards, withdrawal notices, correction notices, signatures, or release changelogs.
- Story publication approvals or public exposure shortcuts.
- Story process receipts.
- Story EvidenceBundle, ProofPack, CatalogMatrix, citation validation, integrity bundles, or proof-side closure records.
- Story STAC, DCAT, PROV, or domain catalog records.
- Story published artifact bytes.
- Story SourceDescriptor/source-registry records.
- Story schemas, policy rules, validators, tests, packages, pipelines, app/UI/API code.

## Migration posture

PROPOSED until an accepted ADR/path map confirms the final treatment:

| Case | Action |
|---|---|
| Story release-level manifest found here | Move to `release/manifests/` through governed migration and record rollback. |
| Story release decision found here | Move to `release/` through governed migration and record rollback. |
| Story process receipt found here | Move to `data/receipts/` and preserve run linkage. |
| Story proof support found here | Move to `data/proofs/` and preserve evidence/proof identity. |
| Story catalog discovery record found here | Move to the matching `data/catalog/...` lane. |
| Published story artifact bytes found here | Move to approved `data/published/...` location or quarantine if release status is unclear. |
| No trust-bearing content found | Keep this README as a compatibility note or remove the folder through governed migration. |

## Guardrails

- Do not create new trust-bearing Story manifest files here.
- Do not publish from this path.
- Do not use this path as a release authority shortcut.
- Do not use this path for story publication approvals.
- Do not collapse receipts, proofs, catalog records, story descriptors, and release manifests.
- Do not treat a file move into `data/manifests/story/` as promotion.
- Promotion remains a governed state transition and must leave release, receipt, proof, catalog, correction, and rollback trails in the correct homes.

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous file | CONFIRMED | Target existed as a greenfield stub. | Did not define Story manifest boundaries. |
| `data/manifests/README.md` | CONFIRMED | Parent lane is non-canonical and points release-level manifests to `release/manifests/`. | Does not prove this child path should remain. |
| `release/README.md` | CONFIRMED | `release/` owns release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog. | Does not prove `release/manifests/` inventory. |
| `ADR-0011` | CONFIRMED doctrine / PROPOSED placement | Proposes strict receipt/proof/catalog/publication separation and says `data/manifests/` must not exist as a root. | ADR status is proposed and implementation remains NEEDS VERIFICATION. |

## Validation checklist

- [ ] Confirm whether `data/manifests/story/` contains any files beyond this README.
- [ ] Confirm whether this child path should remain as compatibility, redirect, or be removed.
- [ ] Confirm Story release-level manifests live under `release/manifests/`.
- [ ] Confirm Story release decisions live under `release/`.
- [ ] Confirm Story receipts, proofs, catalogs, source registry records, schemas, policy, published artifacts, and code are not stored here.
- [ ] Confirm migration notes and rollback targets before moving or deleting anything.

## Rollback

Rollback is required if this lane becomes a parallel Story release-manifest root, release-decision root, source-data root, proof store, receipt store, catalog root, source-registry root, published-output root, schema root, policy root, validator root, implementation root, public API shortcut, or public exposure shortcut.

Rollback target for this replacement: previous stub blob SHA `81b75075363b2e550ef5ac42b6790a2c6cb6b476`.

<p align="right"><a href="#top">Back to top</a></p>
