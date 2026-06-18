<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-index-readme
title: catalog/index/ — Catalog Index Compatibility Redirect
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Catalog steward · Data steward · Source steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../data/README.md
  - ../../data/catalog/README.md
  - ../../data/receipts/README.md
  - ../../data/proofs/README.md
  - ../../data/published/README.md
  - ../../data/registry/README.md
  - ../../release/README.md
  - ../../schemas/contracts/v1/
  - ../../contracts/
  - ../../policy/
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, catalog, index, compatibility-root, redirect, data-catalog, catalog-index, non-authoritative, drift-fence]
notes:
  - "Root-level catalog/index/ is treated as a compatibility/redirect fence, not canonical catalog-index authority."
  - "Canonical catalog index material should be placed under the governed data catalog tree, currently data/catalog/ with a possible data/catalog/index/ sublane if accepted and verified."
  - "Do not add catalog indexes, source indexes, search indexes, receipts, proofs, release records, or published artifacts here without an ADR/migration note."
  - "Specific current contents, producers, canonical sublane acceptance, migration status, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# Catalog Index Compatibility Redirect

`catalog/index/`

**Compatibility / redirect fence for legacy or accidental root-level catalog-index placement. Canonical catalog index material belongs under the governed `data/catalog/` tree, not this root-level `catalog/index/` folder.**

![status](https://img.shields.io/badge/status-draft-blue)
![authority](https://img.shields.io/badge/authority-compatibility-orange)
![canonical](https://img.shields.io/badge/canonical_home-data%2Fcatalog-blue)
![trust](https://img.shields.io/badge/trust__content-forbidden-red)
![truth](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)

[Purpose](#1-purpose) · [Canonical home](#2-canonical-home) · [Authority boundary](#3-authority-boundary) · [Allowed contents](#5-allowed-contents) · [Forbidden contents](#6-forbidden-contents) · [Migration](#9-migration-posture) · [Definition of done](#12-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Path:** `catalog/index/README.md`  
> **Responsibility root:** compatibility redirect / drift fence only  
> **Canonical catalog index home:** `data/catalog/` with `data/catalog/index/` as a PROPOSED sublane until accepted and verified  
> **Truth posture:** CONFIRMED README path / CONFIRMED root-level `catalog/` is a compatibility redirect / CONFIRMED `data/` lifecycle root lists `catalog` as belonging under `data/` / PROPOSED catalog-index redirect contract / UNKNOWN current index files, canonical sublane acceptance, historical producers, migration status, CI enforcement, and ADR disposition

> [!CAUTION]
> Do not make `catalog/index/` a parallel catalog-index authority. KFM catalog indexes, domain/source lookup tables, search indexes, collection summaries, publication-state indexes, and crosswalk indexes must live in the governed data lifecycle path, especially `data/catalog/`, with receipts/proofs/release records in their own canonical roots.

---

## 1. Purpose

`catalog/index/` is a **root-level compatibility redirect** for catalog-index path drift.

It exists only to prevent accidental or legacy catalog index material from becoming a parallel authority outside the KFM lifecycle data root. This folder should not be used for canonical catalog indexes, search indexes, source indexes, domain indexes, STAC/DCAT/PROV lookup indexes, or publication records.

This README does not prove that any catalog index material currently exists here, that a canonical index sublane has been accepted, that a migration has been completed, or that CI currently blocks writes to this path.

[Back to top](#top)

---

## 2. Canonical home

Canonical catalog index material should live under the governed data catalog tree:

```text
data/catalog/
```

A dedicated index sublane may be used when accepted and verified:

```text
data/catalog/index/   # PROPOSED canonical sublane; NEEDS VERIFICATION
```

The root-level `catalog/index/` directory is a redirect/fence only.

## 3. Authority boundary

`catalog/index/` has **no canonical catalog-index authority**. It may hold only README guidance, migration notes, drift logs, or temporary redirect markers while catalog index material is moved into its proper lifecycle home.

```text
WRONG / LEGACY ROOT                CANONICAL LIFECYCLE HOME              TRUST SUPPORT HOMES
catalog/index/                -->  data/catalog/index/              -->  data/receipts/
compatibility fence only           or data/catalog/                       data/proofs/
not authoritative                  catalog indexes / lookup tables        release/
                                                                           data/published/
```

A catalog index outside the governed `data/catalog/` tree should be treated as drift until reviewed and migrated.

## 4. Default posture

Anything found under root-level `catalog/index/` should be treated as **NEEDS VERIFICATION** and potentially misplaced.

Do not expose, publish, index, cite, or depend on root-level catalog index files as canonical records. First confirm source, provenance, rights, sensitivity, schema validity, lifecycle state, receipts, proofs, release state, rollback path, and correction path.

## 5. Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| README / redirect docs | `README.md` | Compatibility fence only |
| Migration note | `MIGRATION.md` | Temporary and ADR/review-linked |
| Drift note | `DRIFT.md`, `OPEN-QUESTIONS.md` | Must point to canonical homes and review steps |
| Placeholder marker | `.gitkeep` | Does not authorize index content |

## 6. Forbidden contents

| Forbidden here | Correct home |
|---|---|
| Catalog indexes, lookup tables, search indexes, collection summaries | `data/catalog/` or an accepted sublane under it |
| Domain, source, STAC, DCAT, PROV, publication-state, or crosswalk indexes | `data/catalog/` under their proper family lanes |
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
catalog/index/
├── README.md                 # compatibility redirect / drift fence
├── MIGRATION.md              # PROPOSED only if migration is active
└── DRIFT.md                  # PROPOSED only if misplaced catalog index material is found
```

> [!WARNING]
> Do not treat this suggested shape as repo fact. Verify actual contents before making inventory or migration claims.

## 8. Diagram

```mermaid
flowchart TD
    wrong["catalog/index/\nroot-level redirect"] --> review["review for catalog-index drift"]
    review --> canonical["data/catalog/index/\nPROPOSED canonical sublane"]
    canonical --> receipts["data/receipts\nvalidation / transform receipts"]
    canonical --> proofs["data/proofs\nEvidenceBundles / proof packs"]
    canonical --> release["release\npublication decisions"]
    release --> published["data/published\npublic-safe released artifacts"]
    wrong -. "must not be public/canonical" .-> published
```

## 9. Migration posture

If catalog index files are found here:

1. Do not publish or depend on them.
2. Identify whether they are catalog indexes, lookup tables, domain/source indexes, STAC/DCAT/PROV indexes, receipts, proofs, release records, source registry rows, or published-output material.
3. Check sensitivity, rights, and redaction/generalization requirements before moving or exposing anything.
4. Move or regenerate them into the correct owning root through a governed migration.
5. Normalize canonical placement to `data/catalog/` or an accepted `data/catalog/index/` sublane.
6. Preserve provenance, source refs, digests, receipts, review notes, and rollback path.
7. Add a drift register or migration note if the material has already been consumed.
8. Leave root-level `catalog/index/` as a redirect/fence unless an ADR explicitly says otherwise.

## 10. Validation expectations

Useful validation for this folder should cover:

- no catalog indexes, lookup tables, search indexes, collection summaries, or crosswalk indexes are stored here;
- no receipts, proofs, release records, registry records, policy rules, schemas, source code, or published artifacts are stored here;
- any non-README content is tied to an active migration or drift note;
- CI or review checks flag root-level `catalog/index/` writes;
- links point users to `data/catalog/` and other canonical homes.

## 11. Safe change pattern

For changes under `catalog/index/`:

1. Confirm the change is redirect documentation, migration support, or drift documentation only.
2. Confirm it does not create a parallel catalog-index authority.
3. Confirm durable catalog index records are placed under the governed `data/catalog/` tree.
4. Confirm receipts/proofs/release records are placed under their owning roots.
5. Document migration and rollback if any misplaced material was moved.
6. Update docs and validation rules when behavior materially changes.

## 12. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual root-level `catalog/index/` contents are verified.
- [ ] Any misplaced catalog index material is migrated or documented as drift.
- [ ] Canonical catalog index placement under `data/catalog/` is accepted and documented.
- [ ] No trust-bearing records live here.
- [ ] No catalog indexes, STAC/DCAT/PROV indexes, registry records, receipts, proofs, release records, published artifacts, schemas, contracts, policy rules, source code, or lifecycle data live here.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## 13. Open verification items

| Item | Why it matters |
|---|---|
| Confirm actual files under root-level `catalog/index/` | Prevents overclaiming or missing drift |
| Confirm whether any workflow writes here | Required before producer claims |
| Confirm accepted canonical catalog-index placement | Required before final migration claims |
| Confirm migration status to `data/catalog/` | Required before canonical-home claims beyond doctrine |
| Confirm CI/review guard exists | Required before enforcement claims |
| Confirm no trust records are stored here | Required before Directory Rules compliance claims |
| Confirm ADR status for root-level `catalog/index/` | Required before long-term retention claims |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The previous README was empty. This replacement adds a catalog-index redirect and anti-parallel-authority contract without claiming catalog index files, migration work, CI enforcement, producer workflows, canonical sublane acceptance, or ADR disposition are implemented.

</details>

## Status summary

`catalog/index/` is a root-level compatibility redirect and catalog-index drift fence. It is not the canonical catalog-index home.

Catalog index authority belongs under the governed `data/catalog/` tree; trust-bearing support belongs under `data/receipts/`, `data/proofs/`, and `release/`; released public-safe products belong under `data/published/`.

<p align="right"><a href="#top">Back to top</a></p>
