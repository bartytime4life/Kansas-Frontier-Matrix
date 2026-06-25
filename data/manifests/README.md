<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-manifests-readme
title: data/manifests/README.md — Manifests Compatibility / Retirement README
version: v0.1
type: readme; data-lifecycle-note; compatibility-retirement-note
status: draft; PROPOSED; NON-CANONICAL; compatibility; manifests; release-gated; needs-migration-decision
owners: OWNER_TBD — Data steward · Release steward · Manifest steward · Evidence steward · Catalog steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; manifests; compatibility; non-canonical; release-governance
tags: [kfm, data, manifests, release, ReleaseManifest, rollback, correction, withdrawal, receipts, proofs, catalog, publication, ADR-0011]
related:
  - ../README.md
  - ../../release/README.md
  - ../../release/manifests/
  - ../published/
  - ../catalog/
  - ../proofs/
  - ../receipts/
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/lifecycle-law.md
notes:
  - "This file replaces a greenfield stub at `data/manifests/README.md`."
  - "ADR-0011 proposes that `data/manifests/` must not exist as a root and that release-level ReleaseManifest records belong under `release/manifests/`."
  - "Until ADR/path-map/migration decisions are accepted and verified, treat this path as a NON-CANONICAL compatibility/retirement note only."
  - "Do not store release manifests, rollback cards, correction notices, receipts, proofs, catalog records, source registries, schemas, policy rules, published artifacts, or executable code here."
  - "Rollback target for this expansion is previous stub blob SHA `6723e635ccf1e4885d8359d214467a3e6d4de9de`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/manifests

> Non-canonical compatibility and retirement README for `data/manifests/`. Release-level manifests belong under `release/manifests/`, not this data root.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Posture: non-canonical" src="https://img.shields.io/badge/posture-non--canonical-red">
  <img alt="Canonical: release/manifests" src="https://img.shields.io/badge/canonical-release%2Fmanifests-blue">
  <img alt="Decision: ADR-0011 proposed" src="https://img.shields.io/badge/decision-ADR--0011__PROPOSED-orange">
  <img alt="Trust: separation" src="https://img.shields.io/badge/trust-receipt≠proof≠catalog≠publication-green">
</p>

**Status:** draft / PROPOSED / NON-CANONICAL  
**Path:** `data/manifests/README.md`  
**Owning root:** `data/` only as a compatibility/retirement note  
**Canonical release-manifest home:** `release/manifests/`  
**Exposure posture:** not public; this path must not publish or authorize release  
**Truth posture:** CONFIRMED target was a greenfield stub · CONFIRMED `data/` is the lifecycle data root · CONFIRMED `release/` owns release decisions and manifests · CONFIRMED ADR-0011 proposes that `data/manifests/` must not exist as a root · NEEDS VERIFICATION for whether this path should remain as a redirect, be removed, or be migrated.

**Quick jumps:** [Purpose](#purpose) · [Boundary](#boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Guardrails](#guardrails) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/manifests/` is not treated here as a canonical KFM authority root. It exists only because the path currently exists and needs a clear boundary while the repository resolves migration and compatibility.

This README prevents the folder from becoming an accidental release-manifest root. Release decisions, release manifests, promotion records, rollback cards, withdrawal notices, correction notices, signatures, and release changelogs belong under `release/`.

## Boundary

KFM separates four trust-bearing artifact families:

```text
receipt ≠ proof ≠ catalog ≠ publication
```

A manifest that decides or describes a release is a publication/release artifact, not a lifecycle data scratchpad. A lane-internal manifest may describe an already released artifact under `data/published/...`, but it is not a release-level `ReleaseManifest`.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Release-level manifests | `release/manifests/` | Canonical release authority. |
| Release decisions, rollback, correction, withdrawal, signatures, changelog | `release/` | Canonical release-decision root. |
| Public-safe artifact bytes | `data/published/` | Downstream after release. |
| Lane-internal released artifact descriptors | `data/published/<domain>/...` | May exist beside released artifacts if approved. |
| Process receipts | `data/receipts/` | Process memory, not release proof alone. |
| Proof support | `data/proofs/` | EvidenceBundle, ProofPack, CatalogMatrix, integrity bundles. |
| Catalog records | `data/catalog/` | Discovery and interchange records. |
| Source registry | `data/registry/` | SourceDescriptor/source-admission records. |
| Schemas and policy | `schemas/`, `policy/` | Separate roots. |
| `data/manifests/` | Non-canonical compatibility/retirement note | Do not add trust-bearing records here. |

## Accepted contents

Until an accepted ADR/path map says otherwise, accepted contents are limited to:

- This README.
- Migration notes that identify any historical use of `data/manifests/` and where each artifact moved.
- Redirect/crosswalk notes pointing to `release/manifests/`, `data/published/...`, `data/receipts/`, `data/proofs/`, or `data/catalog/`.
- Empty placeholder indexes needed only to preserve compatibility during migration.

## Exclusions

Do not store these under `data/manifests/`:

- `ReleaseManifest` records.
- Release decisions, promotion records, rollback cards, withdrawal notices, correction notices, signatures, or release changelogs.
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
| Process receipt found here | Move to `data/receipts/` and preserve run linkage. |
| Proof support found here | Move to `data/proofs/` and preserve evidence/proof identity. |
| Catalog discovery record found here | Move to `data/catalog/`. |
| Released artifact descriptor found here | Move beside the released artifact under `data/published/...` if approved. |
| No trust-bearing content found | Keep this README as a compatibility note or remove the folder through governed migration. |

## Guardrails

- Do not create new trust-bearing manifest files here.
- Do not publish from this path.
- Do not use this path as a release authority shortcut.
- Do not collapse receipts, proofs, catalog records, and release manifests.
- Do not treat a file move into `data/manifests/` as promotion.
- Promotion remains a governed state transition and must leave release, receipt, proof, catalog, correction, and rollback trails in the correct homes.

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous file | CONFIRMED | Target existed as a greenfield stub. | Did not define manifest boundaries. |
| `data/README.md` | CONFIRMED | `data/` is lifecycle data root and excludes code, schemas, policy rules, and release decisions. | Does not authorize `data/manifests/` as canonical. |
| `release/README.md` | CONFIRMED | `release/` owns release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog. | Does not prove `release/manifests/` inventory. |
| `ADR-0011` | CONFIRMED doctrine / PROPOSED placement | Proposes strict receipt/proof/catalog/publication separation and says `data/manifests/` must not exist as a root. | ADR status is proposed and implementation remains NEEDS VERIFICATION. |

## Validation checklist

- [ ] Confirm whether `data/manifests/` contains any files beyond this README.
- [ ] Confirm whether this path should remain as compatibility, redirect, or be removed.
- [ ] Confirm release-level manifests live under `release/manifests/`.
- [ ] Confirm any lane-internal artifact manifests live under approved `data/published/...` paths.
- [ ] Confirm receipts, proofs, catalogs, source registry records, schemas, policy, and code are not stored here.
- [ ] Confirm migration notes and rollback targets before moving or deleting anything.

## Rollback

Rollback is required if this lane becomes a parallel release-manifest root, release-decision root, source-data root, proof store, receipt store, catalog root, source-registry root, published-output root, schema root, policy root, validator root, implementation root, public API shortcut, or public exposure shortcut.

Rollback target for this expansion: previous stub blob SHA `6723e635ccf1e4885d8359d214467a3e6d4de9de`.

<p align="right"><a href="#top">Back to top</a></p>
