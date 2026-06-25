<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-manifests-flora-readme
title: data/manifests/flora/README.md — Flora Manifests Compatibility / Retirement README
version: v0.1
type: readme; data-lifecycle-note; compatibility-retirement-note; flora-note
status: draft; PROPOSED; NON-CANONICAL; compatibility; flora; manifests; release-gated; needs-migration-decision
owners: OWNER_TBD — Flora steward · Data steward · Release steward · Manifest steward · Evidence steward · Catalog steward · Docs steward
created: NEEDS VERIFICATION — placeholder existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; manifests; flora; compatibility; non-canonical; release-governance
tags: [kfm, data, manifests, flora, release, ReleaseManifest, rollback, correction, withdrawal, receipts, proofs, catalog, publication, ADR-0011]
related:
  - ../README.md
  - ../../README.md
  - ../../../release/README.md
  - ../../../release/manifests/
  - ../../published/
  - ../../catalog/domain/flora/README.md
  - ../../catalog/stac/flora/README.md
  - ../../catalog/dcat/flora/README.md
  - ../../catalog/prov/flora/README.md
  - ../../proofs/
  - ../../receipts/
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
notes:
  - "This file replaces a placeholder at `data/manifests/flora/README.md`."
  - "The parent `data/manifests/` lane is non-canonical; this Flora child is a compatibility/retirement note only."
  - "Flora release-level manifests belong under `release/manifests/`; public-safe released Flora artifact descriptors belong with approved released artifacts under `data/published/...` when allowed."
  - "Do not store Flora release manifests, rollback cards, correction notices, receipts, proofs, catalog records, source registries, schemas, policy rules, published artifacts, or executable code here."
  - "Rollback target for this replacement is previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/manifests/flora

> Non-canonical compatibility and retirement README for `data/manifests/flora/`. Flora release-level manifests belong under `release/manifests/`, not this data root.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Posture: non-canonical" src="https://img.shields.io/badge/posture-non--canonical-red">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-green">
  <img alt="Canonical: release/manifests" src="https://img.shields.io/badge/canonical-release%2Fmanifests-blue">
  <img alt="Decision: ADR-0011 proposed" src="https://img.shields.io/badge/decision-ADR--0011__PROPOSED-orange">
</p>

**Status:** draft / PROPOSED / NON-CANONICAL  
**Path:** `data/manifests/flora/README.md`  
**Owning root:** `data/manifests/` only as a compatibility/retirement child  
**Canonical release-manifest home:** `release/manifests/`  
**Domain segment:** `flora`  
**Exposure posture:** not public; this path must not publish or authorize release  
**Truth posture:** CONFIRMED target was a placeholder · CONFIRMED parent `data/manifests/` is non-canonical and must not host trust-bearing manifests · CONFIRMED `release/` owns release decisions and manifests · CONFIRMED ADR-0011 proposes that `data/manifests/` must not exist as a root · NEEDS VERIFICATION for whether this child path should remain as a redirect, be removed, or be migrated.

**Quick jumps:** [Purpose](#purpose) · [Boundary](#boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Guardrails](#guardrails) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/manifests/flora/` is not a canonical Flora manifest root. It exists only because the path currently exists and needs a clear compatibility boundary while the repository resolves migration and cleanup.

This README prevents the folder from becoming an accidental Flora release-manifest root. Flora release decisions, release manifests, promotion records, rollback cards, withdrawal notices, correction notices, signatures, and release changelogs belong under `release/`.

## Boundary

KFM separates four trust-bearing artifact families:

```text
receipt != proof != catalog != publication
```

A Flora manifest that decides or describes a release is a publication/release artifact, not lifecycle data scratch. A lane-internal descriptor may describe an already released Flora artifact under `data/published/...` if approved, but it is not a release-level `ReleaseManifest`.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Flora release-level manifests | `release/manifests/` | Canonical release authority. |
| Flora release decisions, rollback, correction, withdrawal, signatures, changelog | `release/` | Canonical release-decision root. |
| Public-safe Flora artifact bytes | `data/published/` | Downstream after release. |
| Lane-internal released Flora artifact descriptors | `data/published/<domain>/...` | May exist beside released artifacts if approved. |
| Flora receipts | `data/receipts/` | Process memory, not release proof alone. |
| Flora proof support | `data/proofs/` | EvidenceBundle, ProofPack, CatalogMatrix, integrity bundles. |
| Flora catalog records | `data/catalog/{domain,stac,dcat,prov}/flora/` | Discovery and interchange records. |
| Flora source registry | `data/registry/` | SourceDescriptor/source-admission records. |
| Flora schemas and policy | `schemas/`, `policy/` | Separate roots. |
| `data/manifests/flora/` | Non-canonical compatibility/retirement note | Do not add trust-bearing records here. |

## Accepted contents

Until an accepted ADR/path map says otherwise, accepted contents are limited to:

- This README.
- Migration notes that identify any historical Flora use of `data/manifests/flora/` and where each artifact moved.
- Redirect/crosswalk notes pointing to `release/manifests/`, `data/published/...`, `data/receipts/`, `data/proofs/`, or `data/catalog/.../flora/`.
- Empty placeholder indexes needed only to preserve compatibility during migration.

## Exclusions

Do not store these under `data/manifests/flora/`:

- Flora `ReleaseManifest` records.
- Flora release decisions, promotion records, rollback cards, withdrawal notices, correction notices, signatures, or release changelogs.
- Flora process receipts.
- Flora EvidenceBundle, ProofPack, CatalogMatrix, citation validation, integrity bundles, or proof-side closure records.
- Flora STAC, DCAT, PROV, or domain catalog records.
- Flora published artifact bytes.
- Flora SourceDescriptor/source-registry records.
- Flora schemas, policy rules, validators, tests, packages, pipelines, app/UI/API code.

## Migration posture

PROPOSED until an accepted ADR/path map confirms the final treatment:

| Case | Action |
|---|---|
| Flora release-level manifest found here | Move to `release/manifests/` through governed migration and record rollback. |
| Flora process receipt found here | Move to `data/receipts/` and preserve run linkage. |
| Flora proof support found here | Move to `data/proofs/` and preserve evidence/proof identity. |
| Flora catalog discovery record found here | Move to the matching `data/catalog/.../flora/` lane. |
| Released Flora artifact descriptor found here | Move beside the released artifact under `data/published/...` if approved. |
| No trust-bearing content found | Keep this README as a compatibility note or remove the folder through governed migration. |

## Guardrails

- Do not create new trust-bearing Flora manifest files here.
- Do not publish from this path.
- Do not use this path as a release authority shortcut.
- Do not collapse receipts, proofs, catalog records, and release manifests.
- Do not treat a file move into `data/manifests/flora/` as promotion.
- Promotion remains a governed state transition and must leave release, receipt, proof, catalog, correction, and rollback trails in the correct homes.

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous file | CONFIRMED | Target existed as a placeholder. | Did not define Flora manifest boundaries. |
| `data/manifests/README.md` | CONFIRMED | Parent lane is non-canonical and points release-level manifests to `release/manifests/`. | Does not prove this child path should remain. |
| `release/README.md` | CONFIRMED | `release/` owns release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog. | Does not prove `release/manifests/` inventory. |
| `ADR-0011` | CONFIRMED doctrine / PROPOSED placement | Proposes strict receipt/proof/catalog/publication separation and says `data/manifests/` must not exist as a root. | ADR status is proposed and implementation remains NEEDS VERIFICATION. |

## Validation checklist

- [ ] Confirm whether `data/manifests/flora/` contains any files beyond this README.
- [ ] Confirm whether this child path should remain as compatibility, redirect, or be removed.
- [ ] Confirm Flora release-level manifests live under `release/manifests/`.
- [ ] Confirm any lane-internal Flora artifact descriptors live under approved `data/published/...` paths.
- [ ] Confirm Flora receipts, proofs, catalogs, source registry records, schemas, policy, and code are not stored here.
- [ ] Confirm migration notes and rollback targets before moving or deleting anything.

## Rollback

Rollback is required if this lane becomes a parallel Flora release-manifest root, release-decision root, source-data root, proof store, receipt store, catalog root, source-registry root, published-output root, schema root, policy root, validator root, implementation root, public API shortcut, or public exposure shortcut.

Rollback target for this replacement: previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

<p align="right"><a href="#top">Back to top</a></p>
