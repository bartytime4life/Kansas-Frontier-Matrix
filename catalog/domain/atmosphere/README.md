<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-domain-atmosphere-readme
title: catalog/domain/atmosphere/ — Atmosphere Domain Catalog Compatibility Redirect
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Catalog steward · Atmosphere steward · Data steward · Source steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../../data/README.md
  - ../../../data/catalog/README.md
  - ../../../data/catalog/domain/README.md
  - ../../../data/receipts/README.md
  - ../../../data/proofs/README.md
  - ../../../data/published/README.md
  - ../../../data/registry/README.md
  - ../../../release/README.md
  - ../../../schemas/contracts/v1/
  - ../../../contracts/
  - ../../../policy/
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, catalog, domain, atmosphere, air, climate, weather, compatibility-root, redirect, data-catalog, non-authoritative, drift-fence]
notes:
  - "Root-level catalog/domain/atmosphere/ is treated as a compatibility/redirect fence, not canonical atmosphere domain catalog authority."
  - "Canonical atmosphere domain catalog material should be placed under the governed data catalog domain lane, currently proposed as data/catalog/domain/atmosphere/ or otherwise under data/catalog/domain/ per accepted catalog conventions."
  - "Do not add atmosphere domain catalog records, source descriptors, receipts, proofs, release records, or published artifacts here without an ADR/migration note."
  - "Specific current contents, producers, canonical sublane acceptance, migration status, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# Atmosphere Domain Catalog Compatibility Redirect

`catalog/domain/atmosphere/`

**Compatibility / redirect fence for legacy or accidental root-level atmosphere-domain catalog placement. Canonical atmosphere catalog records belong under the governed `data/catalog/domain/` tree, not this root-level `catalog/domain/atmosphere/` folder.**

![status](https://img.shields.io/badge/status-draft-blue)
![authority](https://img.shields.io/badge/authority-compatibility-orange)
![canonical](https://img.shields.io/badge/canonical_home-data%2Fcatalog%2Fdomain-blue)
![domain](https://img.shields.io/badge/domain-atmosphere-1976d2)
![trust](https://img.shields.io/badge/trust__content-forbidden-red)
![truth](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)

[Purpose](#1-purpose) · [Canonical home](#2-canonical-home) · [Authority boundary](#3-authority-boundary) · [Allowed contents](#5-allowed-contents) · [Forbidden contents](#6-forbidden-contents) · [Migration](#9-migration-posture) · [Definition of done](#12-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Path:** `catalog/domain/atmosphere/README.md`  
> **Responsibility root:** compatibility redirect / drift fence only  
> **Canonical atmosphere domain catalog home:** `data/catalog/domain/` with `data/catalog/domain/atmosphere/` as a PROPOSED sublane until accepted and verified  
> **Truth posture:** CONFIRMED README path / CONFIRMED root-level `catalog/domain/` is a compatibility redirect / CONFIRMED `data/catalog/domain/README.md` path exists as a stub / PROPOSED atmosphere-domain redirect contract / UNKNOWN current atmosphere catalog files, canonical sublane acceptance, historical producers, migration status, CI enforcement, and ADR disposition

> [!CAUTION]
> Do not make `catalog/domain/atmosphere/` a parallel atmosphere catalog authority. KFM atmosphere catalog truth, domain indexes, source mappings, sensor/platform references, STAC/DCAT/PROV crosswalks, and publication state must live in the governed data lifecycle path, with receipts/proofs/release records in their own canonical roots.

---

## 1. Purpose

`catalog/domain/atmosphere/` is a **root-level compatibility redirect** for atmosphere-domain catalog path drift.

It exists only to prevent accidental or legacy atmosphere catalog material from becoming a parallel authority outside the KFM lifecycle data root. This folder should not be used for canonical atmosphere catalog records, indexes, source crosswalks, policy mappings, sensor/platform mappings, or publication records.

This README does not prove that any atmosphere catalog material currently exists here, that a canonical atmosphere sublane has been accepted, that a migration has been completed, or that CI currently blocks writes to this path.

[Back to top](#top)

---

## 2. Canonical home

Canonical atmosphere domain catalog material should live under the governed data catalog domain lane:

```text
data/catalog/domain/
```

A domain-specific atmosphere sublane may be used when accepted and verified:

```text
data/catalog/domain/atmosphere/   # PROPOSED canonical sublane; NEEDS VERIFICATION
```

The root-level `catalog/domain/atmosphere/` directory is a redirect/fence only.

## 3. Authority boundary

`catalog/domain/atmosphere/` has **no canonical atmosphere catalog authority**. It may hold only README guidance, migration notes, drift logs, or temporary redirect markers while atmosphere catalog material is moved into its proper lifecycle home.

```text
WRONG / LEGACY ROOT                         CANONICAL LIFECYCLE HOME                     TRUST SUPPORT HOMES
catalog/domain/atmosphere/            -->   data/catalog/domain/atmosphere/         -->   data/receipts/
compatibility fence only                     or data/catalog/domain/                      data/proofs/
not authoritative                            atmosphere catalog records/indexes           release/
                                                                                          data/published/
```

An atmosphere catalog record outside the governed `data/catalog/` tree should be treated as drift until reviewed and migrated.

## 4. Default posture

Anything found under root-level `catalog/domain/atmosphere/` should be treated as **NEEDS VERIFICATION** and potentially misplaced.

Do not expose, publish, index, cite, or depend on root-level atmosphere catalog files as canonical records. First confirm source, provenance, rights, sensitivity, schema validity, lifecycle state, receipts, proofs, release state, rollback path, and correction path.

## 5. Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| README / redirect docs | `README.md` | Compatibility fence only |
| Migration note | `MIGRATION.md` | Temporary and ADR/review-linked |
| Drift note | `DRIFT.md`, `OPEN-QUESTIONS.md` | Must point to canonical homes and review steps |
| Placeholder marker | `.gitkeep` | Does not authorize atmosphere catalog content |

## 6. Forbidden contents

| Forbidden here | Correct home |
|---|---|
| Atmosphere domain catalog records, indexes, manifests, or source crosswalks | `data/catalog/domain/` or an accepted sublane under it |
| Weather, climate, air-quality, station, sensor, platform, model-run, or observation catalog records | `data/catalog/domain/` or accepted catalog family homes |
| STAC, DCAT, or PROV records | `data/catalog/` under their proper family lanes |
| Catalog-derived public products | `data/published/` after governed release |
| Source descriptors, source registry rows, rights rows, sensitivity rows | `data/registry/` or governed registry homes |
| Receipts, validation reports, redaction receipts | `data/receipts/` |
| EvidenceBundles, proof packs, attestations | `data/proofs/` |
| ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, signatures | `release/` |
| Schemas and machine-shape contracts | `schemas/contracts/v1/` |
| Human contracts and object-meaning docs | `contracts/` |
| Policy rules and policy decisions | `policy/` and governed policy-decision homes |
| Source code, scripts, packages, pipelines, build tools | `apps/`, `packages/`, `tools/`, `scripts/`, `pipelines/` |
| Raw, work, quarantine, processed, or published lifecycle data | `data/` lifecycle subtrees |

## 7. Directory shape

Current implementation inventory remains `NEEDS VERIFICATION`.

```text
catalog/domain/atmosphere/
├── README.md                 # compatibility redirect / drift fence
├── MIGRATION.md              # PROPOSED only if migration is active
└── DRIFT.md                  # PROPOSED only if misplaced atmosphere catalog material is found
```

> [!WARNING]
> Do not treat this suggested shape as repo fact. Verify actual contents before making inventory or migration claims.

## 8. Diagram

```mermaid
flowchart TD
    wrong["catalog/domain/atmosphere/\nroot-level redirect"] --> review["review for atmosphere-domain drift"]
    review --> canonical["data/catalog/domain/atmosphere/\nPROPOSED canonical sublane"]
    canonical --> receipts["data/receipts\nvalidation / transform receipts"]
    canonical --> proofs["data/proofs\nEvidenceBundles / proof packs"]
    canonical --> release["release\npublication decisions"]
    release --> published["data/published\npublic-safe released artifacts"]
    wrong -. "must not be public/canonical" .-> published
```

## 9. Migration posture

If atmosphere catalog files are found here:

1. Do not publish or depend on them.
2. Identify whether they are atmosphere domain records, source crosswalks, STAC/DCAT/PROV records, receipts, proofs, release records, source registry rows, or published-output material.
3. Move or regenerate them into the correct owning root through a governed migration.
4. Normalize canonical placement to `data/catalog/domain/` or an accepted `data/catalog/domain/atmosphere/` sublane.
5. Preserve provenance, source refs, digests, receipts, review notes, and rollback path.
6. Add a drift register or migration note if the material has already been consumed.
7. Leave root-level `catalog/domain/atmosphere/` as a redirect/fence unless an ADR explicitly says otherwise.

## 10. Validation expectations

Useful validation for this folder should cover:

- no atmosphere catalog records, indexes, manifests, or crosswalks are stored here;
- no receipts, proofs, release records, registry records, policy rules, schemas, source code, or published artifacts are stored here;
- any non-README content is tied to an active migration or drift note;
- CI or review checks flag root-level `catalog/domain/atmosphere/` writes;
- links point users to `data/catalog/domain/` and other canonical homes.

## 11. Safe change pattern

For changes under `catalog/domain/atmosphere/`:

1. Confirm the change is redirect documentation, migration support, or drift documentation only.
2. Confirm it does not create a parallel atmosphere domain catalog authority.
3. Confirm durable atmosphere catalog records are placed under the governed `data/catalog/` tree.
4. Confirm receipts/proofs/release records are placed under their owning roots.
5. Document migration and rollback if any misplaced material was moved.
6. Update docs and validation rules when behavior materially changes.

## 12. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual root-level `catalog/domain/atmosphere/` contents are verified.
- [ ] Any misplaced atmosphere catalog material is migrated or documented as drift.
- [ ] Canonical atmosphere catalog placement under `data/catalog/domain/` is accepted and documented.
- [ ] No trust-bearing records live here.
- [ ] No atmosphere catalog records, STAC/DCAT/PROV records, registry records, receipts, proofs, release records, published artifacts, schemas, contracts, policy rules, source code, or lifecycle data live here.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## 13. Open verification items

| Item | Why it matters |
|---|---|
| Confirm actual files under root-level `catalog/domain/atmosphere/` | Prevents overclaiming or missing drift |
| Confirm whether any workflow writes here | Required before producer claims |
| Confirm accepted canonical atmosphere catalog placement | Required before final migration claims |
| Confirm migration status to `data/catalog/domain/` | Required before canonical-home claims beyond doctrine |
| Confirm CI/review guard exists | Required before enforcement claims |
| Confirm no trust records are stored here | Required before Directory Rules compliance claims |
| Confirm ADR status for root-level `catalog/domain/atmosphere/` | Required before long-term retention claims |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The previous README was empty. This replacement adds an atmosphere-domain-catalog redirect and anti-parallel-authority contract without claiming atmosphere catalog files, migration work, CI enforcement, producer workflows, canonical sublane acceptance, or ADR disposition are implemented.

</details>

## Status summary

`catalog/domain/atmosphere/` is a root-level compatibility redirect and atmosphere-domain drift fence. It is not the canonical atmosphere domain catalog home.

Atmosphere catalog authority belongs under the governed `data/catalog/domain/` tree; trust-bearing support belongs under `data/receipts/`, `data/proofs/`, and `release/`; released public-safe products belong under `data/published/`.

<p align="right"><a href="#top">Back to top</a></p>
