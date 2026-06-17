<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-domain-fauna-readme
title: catalog/domain/fauna/ — Fauna Domain Catalog Compatibility Redirect
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Catalog steward · Fauna steward · Ecology sensitivity steward · Data steward · Source steward · Docs steward
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
tags: [kfm, catalog, domain, fauna, ecology, biodiversity, habitat, sensitivity, compatibility-root, redirect, data-catalog, non-authoritative, drift-fence]
notes:
  - "Root-level catalog/domain/fauna/ is treated as a compatibility/redirect fence, not canonical fauna domain catalog authority."
  - "Canonical fauna domain catalog material should be placed under the governed data catalog domain lane, currently proposed as data/catalog/domain/fauna/ or otherwise under data/catalog/domain/ per accepted catalog conventions."
  - "Do not add fauna domain catalog records, species occurrence indexes, source descriptors, receipts, proofs, release records, or published artifacts here without an ADR/migration note."
  - "Specific current contents, producers, canonical sublane acceptance, sensitivity decisions, migration status, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# Fauna Domain Catalog Compatibility Redirect

`catalog/domain/fauna/`

**Compatibility / redirect fence for legacy or accidental root-level fauna-domain catalog placement. Canonical fauna catalog records belong under the governed `data/catalog/domain/` tree, not this root-level `catalog/domain/fauna/` folder.**

![status](https://img.shields.io/badge/status-draft-blue)
![authority](https://img.shields.io/badge/authority-compatibility-orange)
![canonical](https://img.shields.io/badge/canonical_home-data%2Fcatalog%2Fdomain-blue)
![domain](https://img.shields.io/badge/domain-fauna-2e7d32)
![trust](https://img.shields.io/badge/trust__content-forbidden-red)
![truth](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)

[Purpose](#1-purpose) · [Canonical home](#2-canonical-home) · [Authority boundary](#3-authority-boundary) · [Sensitivity posture](#4-sensitivity-posture) · [Allowed contents](#5-allowed-contents) · [Forbidden contents](#6-forbidden-contents) · [Migration](#9-migration-posture) · [Definition of done](#12-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Path:** `catalog/domain/fauna/README.md`  
> **Responsibility root:** compatibility redirect / drift fence only  
> **Canonical fauna domain catalog home:** `data/catalog/domain/` with `data/catalog/domain/fauna/` as a PROPOSED sublane until accepted and verified  
> **Truth posture:** CONFIRMED README path / CONFIRMED root-level `catalog/domain/` is a compatibility redirect / CONFIRMED `data/catalog/domain/README.md` path exists as a stub / PROPOSED fauna-domain redirect contract / UNKNOWN current fauna catalog files, canonical sublane acceptance, sensitivity decisions, historical producers, migration status, CI enforcement, and ADR disposition

> [!CAUTION]
> Do not make `catalog/domain/fauna/` a parallel fauna catalog authority. KFM fauna catalog truth, species indexes, occurrence/source mappings, habitat references, sensitivity posture, STAC/DCAT/PROV crosswalks, and publication state must live in the governed data lifecycle path, with receipts/proofs/release records in their own canonical roots.

---

## 1. Purpose

`catalog/domain/fauna/` is a **root-level compatibility redirect** for fauna-domain catalog path drift.

It exists only to prevent accidental or legacy fauna catalog material from becoming a parallel authority outside the KFM lifecycle data root. This folder should not be used for canonical fauna catalog records, species indexes, occurrence crosswalks, source crosswalks, policy mappings, habitat mappings, or publication records.

This README does not prove that any fauna catalog material currently exists here, that a canonical fauna sublane has been accepted, that a migration has been completed, or that CI currently blocks writes to this path.

[Back to top](#top)

---

## 2. Canonical home

Canonical fauna domain catalog material should live under the governed data catalog domain lane:

```text
data/catalog/domain/
```

A domain-specific fauna sublane may be used when accepted and verified:

```text
data/catalog/domain/fauna/   # PROPOSED canonical sublane; NEEDS VERIFICATION
```

The root-level `catalog/domain/fauna/` directory is a redirect/fence only.

## 3. Authority boundary

`catalog/domain/fauna/` has **no canonical fauna catalog authority**. It may hold only README guidance, migration notes, drift logs, or temporary redirect markers while fauna catalog material is moved into its proper lifecycle home.

```text
WRONG / LEGACY ROOT                    CANONICAL LIFECYCLE HOME                TRUST SUPPORT HOMES
catalog/domain/fauna/             -->  data/catalog/domain/fauna/        -->  data/receipts/
compatibility fence only                or data/catalog/domain/                data/proofs/
not authoritative                       fauna catalog records/indexes          release/
                                                                                data/published/
```

A fauna catalog record outside the governed `data/catalog/` tree should be treated as drift until reviewed and migrated.

## 4. Sensitivity posture

Fauna catalog work is policy-sensitive where exact occurrence locations, rare or vulnerable species, breeding/nesting/denning sites, collection locations, protected habitat, private land context, indigenous/sovereign stewardship context, or other exposure-sensitive details are involved.

This folder must only hold redirect documentation and safe migration guidance. It must not hold precise or exposure-sensitive fauna catalog content. When sensitivity, rights, or redaction/generalization posture is unresolved, the safe outcome is to withhold, redact, generalize, quarantine, deny publication, or route to review — not to store records here.

## 5. Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| README / redirect docs | `README.md` | Compatibility fence only |
| Migration note | `MIGRATION.md` | Temporary and ADR/review-linked |
| Drift note | `DRIFT.md`, `OPEN-QUESTIONS.md` | Must point to canonical homes and review steps |
| Placeholder marker | `.gitkeep` | Does not authorize fauna catalog content |

## 6. Forbidden contents

| Forbidden here | Correct home |
|---|---|
| Fauna domain catalog records, indexes, manifests, occurrence crosswalks, or habitat references | `data/catalog/domain/` or an accepted sublane under it |
| Species occurrence, survey, monitoring, collection, or sensitivity catalog records | `data/catalog/domain/` or accepted catalog family homes |
| Precise protected fauna locations or exposure-sensitive site details | Governed protected data homes with policy/redaction gates |
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
catalog/domain/fauna/
├── README.md                 # compatibility redirect / drift fence
├── MIGRATION.md              # PROPOSED only if migration is active
└── DRIFT.md                  # PROPOSED only if misplaced fauna catalog material is found
```

> [!WARNING]
> Do not treat this suggested shape as repo fact. Verify actual contents before making inventory or migration claims.

## 8. Diagram

```mermaid
flowchart TD
    wrong["catalog/domain/fauna/\nroot-level redirect"] --> review["review for fauna-domain drift"]
    review --> sensitivity["sensitivity / rights / redaction check"]
    sensitivity --> canonical["data/catalog/domain/fauna/\nPROPOSED canonical sublane"]
    canonical --> receipts["data/receipts\nvalidation / transform receipts"]
    canonical --> proofs["data/proofs\nEvidenceBundles / proof packs"]
    canonical --> release["release\npublication decisions"]
    release --> published["data/published\npublic-safe released artifacts"]
    wrong -. "must not be public/canonical" .-> published
```

## 9. Migration posture

If fauna catalog files are found here:

1. Do not publish or depend on them.
2. Identify whether they are fauna domain records, occurrence/source crosswalks, habitat references, STAC/DCAT/PROV records, receipts, proofs, release records, source registry rows, or published-output material.
3. Check sensitivity, rights, and redaction/generalization requirements before moving or exposing anything.
4. Move or regenerate them into the correct owning root through a governed migration.
5. Normalize canonical placement to `data/catalog/domain/` or an accepted `data/catalog/domain/fauna/` sublane.
6. Preserve provenance, source refs, digests, receipts, review notes, and rollback path.
7. Add a drift register or migration note if the material has already been consumed.
8. Leave root-level `catalog/domain/fauna/` as a redirect/fence unless an ADR explicitly says otherwise.

## 10. Validation expectations

Useful validation for this folder should cover:

- no fauna catalog records, indexes, manifests, occurrence crosswalks, or habitat references are stored here;
- no precise protected fauna locations or exposure-sensitive details are stored here;
- no receipts, proofs, release records, registry records, policy rules, schemas, source code, or published artifacts are stored here;
- any non-README content is tied to an active migration or drift note;
- CI or review checks flag root-level `catalog/domain/fauna/` writes;
- links point users to `data/catalog/domain/` and other canonical homes.

## 11. Safe change pattern

For changes under `catalog/domain/fauna/`:

1. Confirm the change is redirect documentation, migration support, or drift documentation only.
2. Confirm it does not create a parallel fauna domain catalog authority.
3. Confirm no precise protected fauna detail or exposure-sensitive detail is added.
4. Confirm durable fauna catalog records are placed under the governed `data/catalog/` tree.
5. Confirm receipts/proofs/release records are placed under their owning roots.
6. Document migration and rollback if any misplaced material was moved.
7. Update docs and validation rules when behavior materially changes.

## 12. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual root-level `catalog/domain/fauna/` contents are verified.
- [ ] Any misplaced fauna catalog material is migrated or documented as drift.
- [ ] Canonical fauna catalog placement under `data/catalog/domain/` is accepted and documented.
- [ ] No trust-bearing records live here.
- [ ] No fauna catalog records, protected fauna detail, STAC/DCAT/PROV records, registry records, receipts, proofs, release records, published artifacts, schemas, contracts, policy rules, source code, or lifecycle data live here.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## 13. Open verification items

| Item | Why it matters |
|---|---|
| Confirm actual files under root-level `catalog/domain/fauna/` | Prevents overclaiming or missing drift |
| Confirm whether any workflow writes here | Required before producer claims |
| Confirm accepted canonical fauna catalog placement | Required before final migration claims |
| Confirm sensitivity/redaction handling | Required before safe-publication claims |
| Confirm migration status to `data/catalog/domain/` | Required before canonical-home claims beyond doctrine |
| Confirm CI/review guard exists | Required before enforcement claims |
| Confirm no trust records are stored here | Required before Directory Rules compliance claims |
| Confirm ADR status for root-level `catalog/domain/fauna/` | Required before long-term retention claims |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The previous README was empty. This replacement adds a fauna-domain-catalog redirect and anti-parallel-authority contract without claiming fauna catalog files, migration work, CI enforcement, producer workflows, canonical sublane acceptance, sensitivity decisions, or ADR disposition are implemented.

</details>

## Status summary

`catalog/domain/fauna/` is a root-level compatibility redirect and fauna-domain drift fence. It is not the canonical fauna domain catalog home.

Fauna catalog authority belongs under the governed `data/catalog/domain/` tree; trust-bearing support belongs under `data/receipts/`, `data/proofs/`, and `release/`; released public-safe products belong under `data/published/`.

<p align="right"><a href="#top">Back to top</a></p>
