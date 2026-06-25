<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-manifests-release-readme
title: data/manifests/release/README.md — Release Manifests Compatibility / Retirement README
version: v0.1
type: readme; data-lifecycle-note; compatibility-retirement-note; release-manifest-note
status: draft; PROPOSED; NON-CANONICAL; compatibility; release; manifests; release-governance; needs-migration-decision
owners: OWNER_TBD — Release steward · Manifest steward · Data steward · Evidence steward · Catalog steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; manifests; release; compatibility; non-canonical; release-governance
tags: [kfm, data, manifests, release, ReleaseManifest, promotion, rollback, correction, withdrawal, receipts, proofs, catalog, publication, ADR-0011]
related:
  - ../README.md
  - ../../README.md
  - ../../../release/README.md
  - ../../../release/manifests/
  - ../../published/
  - ../../catalog/
  - ../../proofs/
  - ../../receipts/
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
notes:
  - "This file replaces a greenfield stub at `data/manifests/release/README.md`."
  - "The parent `data/manifests/` lane is non-canonical; this Release child is a compatibility/retirement note only."
  - "Release-level manifests belong under `release/manifests/`; release decisions and related publication controls belong under `release/`."
  - "Do not store release manifests, rollback cards, correction notices, withdrawal notices, signatures, receipts, proofs, catalog records, source registries, schemas, policy rules, published artifacts, or executable code here."
  - "Rollback target for this replacement is previous stub blob SHA `d30b3fce038248d88f1c6c8561b04ede10a4e09e`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/manifests/release

> Non-canonical compatibility and retirement README for `data/manifests/release/`. Release-level manifests belong under `release/manifests/`, not this data root.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Posture: non-canonical" src="https://img.shields.io/badge/posture-non--canonical-red">
  <img alt="Segment: release" src="https://img.shields.io/badge/segment-release-blue">
  <img alt="Canonical: release/manifests" src="https://img.shields.io/badge/canonical-release%2Fmanifests-blue">
  <img alt="Decision: ADR-0011 proposed" src="https://img.shields.io/badge/decision-ADR--0011__PROPOSED-orange">
</p>

**Status:** draft / PROPOSED / NON-CANONICAL  
**Path:** `data/manifests/release/README.md`  
**Owning root:** `data/manifests/` only as a compatibility/retirement child  
**Canonical release-manifest home:** `release/manifests/`  
**Canonical release-decision home:** `release/`  
**Segment:** `release`  
**Exposure posture:** not public; this path must not publish or authorize release  
**Truth posture:** CONFIRMED target was a greenfield stub · CONFIRMED parent `data/manifests/` is non-canonical and must not host trust-bearing manifests · CONFIRMED `release/` owns release decisions and manifests · CONFIRMED ADR-0011 proposes that `data/manifests/` must not exist as a root · NEEDS VERIFICATION for whether this child path should remain as a redirect, be removed, or be migrated.

**Quick jumps:** [Purpose](#purpose) · [Boundary](#boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Guardrails](#guardrails) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/manifests/release/` is not a canonical release-manifest root. It exists only because the path currently exists and needs a clear compatibility boundary while the repository resolves migration and cleanup.

This README prevents the folder from becoming an accidental second release root. Release decisions, release manifests, promotion records, rollback cards, withdrawal notices, correction notices, signatures, and release changelogs belong under `release/`.

## Boundary

KFM separates four trust-bearing artifact families:

```text
receipt != proof != catalog != publication
```

A release manifest is a publication/release artifact, not lifecycle data scratch. A file under this path must not be treated as a release decision, release manifest, release proof, public artifact, or promotion event.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Release-level manifests | `release/manifests/` | Canonical release authority. |
| Release decisions, rollback, correction, withdrawal, signatures, changelog | `release/` | Canonical release-decision root. |
| Public-safe released artifact bytes | `data/published/` | Downstream after release. |
| Process receipts | `data/receipts/` | Process memory, not release proof alone. |
| Proof support | `data/proofs/` | EvidenceBundle, ProofPack, CatalogMatrix, integrity bundles. |
| Catalog records | `data/catalog/{domain,stac,dcat,prov}/` | Discovery and interchange records. |
| Source registry | `data/registry/` | SourceDescriptor/source-admission records. |
| Schemas and policy | `schemas/`, `policy/` | Separate roots. |
| `data/manifests/release/` | Non-canonical compatibility/retirement note | Do not add trust-bearing records here. |

## Accepted contents

Until an accepted ADR/path map says otherwise, accepted contents are limited to:

- This README.
- Migration notes that identify any historical use of `data/manifests/release/` and where each artifact moved.
- Redirect/crosswalk notes pointing to `release/manifests/`, `release/`, `data/published/...`, `data/receipts/`, `data/proofs/`, or `data/catalog/...`.
- Empty placeholder indexes needed only to preserve compatibility during migration.

## Exclusions

Do not store these under `data/manifests/release/`:

- `ReleaseManifest` records.
- Release decisions, promotion records, rollback cards, withdrawal notices, correction notices, signatures, or release changelogs.
- Release candidates or publication approvals.
- Process receipts.
- EvidenceBundle, ProofPack, CatalogMatrix, citation validation, integrity bundles, or proof-side closure records.
- STAC, DCAT, PROV, or domain catalog records.
- Published artifact bytes.
- SourceDescriptor/source-registry records.
- Schemas, policy rules, validators, tests, packages, pipelines, app/UI/API code.

## Migration posture

PROPOSED until an accepted ADR/path map confirms the final treatment:

| Case | Action |
|---|---|
| Release-level manifest found here | Move to `release/manifests/` through governed migration and record rollback. |
| Release decision found here | Move to `release/` through governed migration and record rollback. |
| Process receipt found here | Move to `data/receipts/` and preserve run linkage. |
| Proof support found here | Move to `data/proofs/` and preserve evidence/proof identity. |
| Catalog discovery record found here | Move to the matching `data/catalog/...` lane. |
| Published artifact bytes found here | Move to approved `data/published/...` location or quarantine if release status is unclear. |
| No trust-bearing content found | Keep this README as a compatibility note or remove the folder through governed migration. |

## Guardrails

- Do not create new trust-bearing release manifest files here.
- Do not publish from this path.
- Do not use this path as a release authority shortcut.
- Do not use this path for release candidates or publication approvals.
- Do not collapse receipts, proofs, catalog records, published artifacts, and release manifests.
- Do not treat a file move into `data/manifests/release/` as promotion.
- Promotion remains a governed state transition and must leave release, receipt, proof, catalog, correction, and rollback trails in the correct homes.

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous file | CONFIRMED | Target existed as a greenfield stub. | Did not define release-manifest boundaries. |
| `data/manifests/README.md` | CONFIRMED | Parent lane is non-canonical and points release-level manifests to `release/manifests/`. | Does not prove this child path should remain. |
| `release/README.md` | CONFIRMED | `release/` owns release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog. | Does not prove `release/manifests/` inventory. |
| `ADR-0011` | CONFIRMED doctrine / PROPOSED placement | Proposes strict receipt/proof/catalog/publication separation and says `data/manifests/` must not exist as a root. | ADR status is proposed and implementation remains NEEDS VERIFICATION. |

## Validation checklist

- [ ] Confirm whether `data/manifests/release/` contains any files beyond this README.
- [ ] Confirm whether this child path should remain as compatibility, redirect, or be removed.
- [ ] Confirm release-level manifests live under `release/manifests/`.
- [ ] Confirm release decisions live under `release/`.
- [ ] Confirm receipts, proofs, catalogs, source registry records, schemas, policy, published artifacts, and code are not stored here.
- [ ] Confirm migration notes and rollback targets before moving or deleting anything.

## Rollback

Rollback is required if this lane becomes a parallel release-manifest root, release-decision root, source-data root, proof store, receipt store, catalog root, source-registry root, published-output root, schema root, policy root, validator root, implementation root, public API shortcut, or public exposure shortcut.

Rollback target for this replacement: previous stub blob SHA `d30b3fce038248d88f1c6c8561b04ede10a4e09e`.

<p align="right"><a href="#top">Back to top</a></p>
