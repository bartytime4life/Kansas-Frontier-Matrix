<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-domain-flora-readme
title: catalog/domain/flora/ — Flora Domain Catalog Compatibility Redirect
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Catalog steward · Flora steward · Ecology sensitivity steward · Data steward · Source steward · Docs steward
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
tags: [kfm, catalog, domain, flora, botany, plants, habitat, sensitivity, compatibility-root, redirect, data-catalog, non-authoritative, drift-fence]
notes:
  - "Root-level catalog/domain/flora/ is treated as a compatibility/redirect fence, not canonical flora domain catalog authority."
  - "Canonical flora domain catalog material should be placed under the governed data catalog domain lane, currently proposed as data/catalog/domain/flora/ or otherwise under data/catalog/domain/ per accepted catalog conventions."
  - "Do not add flora domain catalog records, plant indexes, source descriptors, receipts, proofs, release records, or published artifacts here without an ADR/migration note."
  - "Specific current contents, producers, canonical sublane acceptance, sensitivity decisions, migration status, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# Flora Domain Catalog Compatibility Redirect

`catalog/domain/flora/`

**Compatibility / redirect fence for legacy or accidental root-level flora-domain catalog placement. Canonical flora catalog records belong under the governed `data/catalog/domain/` tree, not this root-level `catalog/domain/flora/` folder.**

![status](https://img.shields.io/badge/status-draft-blue)
![authority](https://img.shields.io/badge/authority-compatibility-orange)
![canonical](https://img.shields.io/badge/canonical_home-data%2Fcatalog%2Fdomain-blue)
![domain](https://img.shields.io/badge/domain-flora-388e3c)
![trust](https://img.shields.io/badge/trust__content-forbidden-red)
![truth](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)

[Purpose](#1-purpose) · [Canonical home](#2-canonical-home) · [Authority boundary](#3-authority-boundary) · [Sensitivity posture](#4-sensitivity-posture) · [Allowed contents](#5-allowed-contents) · [Forbidden contents](#6-forbidden-contents) · [Migration](#9-migration-posture) · [Definition of done](#12-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Path:** `catalog/domain/flora/README.md`  
> **Responsibility root:** compatibility redirect / drift fence only  
> **Canonical flora domain catalog home:** `data/catalog/domain/` with `data/catalog/domain/flora/` as a PROPOSED sublane until accepted and verified  
> **Truth posture:** CONFIRMED README path / CONFIRMED root-level `catalog/domain/` is a compatibility redirect / CONFIRMED `data/catalog/domain/README.md` path exists as a stub / PROPOSED flora-domain redirect contract / UNKNOWN current flora catalog files, canonical sublane acceptance, sensitivity decisions, historical producers, migration status, CI enforcement, and ADR disposition

> [!CAUTION]
> Do not make `catalog/domain/flora/` a parallel flora catalog authority. KFM flora catalog truth, plant indexes, source mappings, habitat references, sensitivity posture, STAC/DCAT/PROV crosswalks, and publication state must live in the governed data lifecycle path, with receipts/proofs/release records in their own canonical roots.

---

## 1. Purpose

`catalog/domain/flora/` is a **root-level compatibility redirect** for flora-domain catalog path drift.

It exists only to prevent accidental or legacy flora catalog material from becoming a parallel authority outside the KFM lifecycle data root. This folder should not be used for canonical flora catalog records, plant indexes, source crosswalks, policy mappings, habitat mappings, or publication records.

This README does not prove that any flora catalog material currently exists here, that a canonical flora sublane has been accepted, that a migration has been completed, or that CI currently blocks writes to this path.

[Back to top](#top)

---

## 2. Canonical home

Canonical flora domain catalog material should live under the governed data catalog domain lane:

```text
data/catalog/domain/
```

A domain-specific flora sublane may be used when accepted and verified:

```text
data/catalog/domain/flora/   # PROPOSED canonical sublane; NEEDS VERIFICATION
```

The root-level `catalog/domain/flora/` directory is a redirect/fence only.

## 3. Authority boundary

`catalog/domain/flora/` has **no canonical flora catalog authority**. It may hold only README guidance, migration notes, drift logs, or temporary redirect markers while flora catalog material is moved into its proper lifecycle home.

```text
WRONG / LEGACY ROOT                    CANONICAL LIFECYCLE HOME                TRUST SUPPORT HOMES
catalog/domain/flora/             -->  data/catalog/domain/flora/        -->  data/receipts/
compatibility fence only                or data/catalog/domain/                data/proofs/
not authoritative                       flora catalog records/indexes          release/
                                                                                data/published/
```

A flora catalog record outside the governed `data/catalog/` tree should be treated as drift until reviewed and migrated.

## 4. Sensitivity posture

Flora catalog work can be policy-sensitive when it includes sensitivity-relevant site details, vulnerable species context, habitat context, collection context, stewardship context, or other exposure-sensitive details.

This folder must only hold redirect documentation and safe migration guidance. It must not hold sensitive flora catalog content. When sensitivity, rights, or redaction/generalization posture is unresolved, the safe outcome is to withhold, redact, generalize, quarantine, deny publication, or route to review — not to store records here.

## 5. Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| README / redirect docs | `README.md` | Compatibility fence only |
| Migration note | `MIGRATION.md` | Temporary and ADR/review-linked |
| Drift note | `DRIFT.md`, `OPEN-QUESTIONS.md` | Must point to canonical homes and review steps |
| Placeholder marker | `.gitkeep` | Does not authorize flora catalog content |

## 6. Forbidden contents

| Forbidden here | Correct home |
|---|---|
| Flora domain catalog records, indexes, manifests, occurrence crosswalks, or habitat references | `data/catalog/domain/` or an accepted sublane under it |
| Plant survey, monitoring, restoration, or sensitivity catalog records | `data/catalog/domain/` or accepted catalog family homes |
| Sensitive flora site details | Governed protected data homes with policy/redaction gates |
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
catalog/domain/flora/
├── README.md                 # compatibility redirect / drift fence
├── MIGRATION.md              # PROPOSED only if migration is active
└── DRIFT.md                  # PROPOSED only if misplaced flora catalog material is found
```

> [!WARNING]
> Do not treat this suggested shape as repo fact. Verify actual contents before making inventory or migration claims.

## 8. Diagram

```mermaid
flowchart TD
    wrong["catalog/domain/flora/\nroot-level redirect"] --> review["review for flora-domain drift"]
    review --> sensitivity["sensitivity / rights / redaction check"]
    sensitivity --> canonical["data/catalog/domain/flora/\nPROPOSED canonical sublane"]
    canonical --> receipts["data/receipts\nvalidation / transform receipts"]
    canonical --> proofs["data/proofs\nEvidenceBundles / proof packs"]
    canonical --> release["release\npublication decisions"]
    release --> published["data/published\npublic-safe released artifacts"]
    wrong -. "must not be public/canonical" .-> published
```

## 9. Migration posture

If flora catalog files are found here:

1. Do not publish or depend on them.
2. Identify whether they are flora domain records, source crosswalks, habitat references, STAC/DCAT/PROV records, receipts, proofs, release records, source registry rows, or published-output material.
3. Check sensitivity, rights, and redaction/generalization requirements before moving or exposing anything.
4. Move or regenerate them into the correct owning root through a governed migration.
5. Normalize canonical placement to `data/catalog/domain/` or an accepted `data/catalog/domain/flora/` sublane.
6. Preserve provenance, source refs, digests, receipts, review notes, and rollback path.
7. Add a drift register or migration note if the material has already been consumed.
8. Leave root-level `catalog/domain/flora/` as a redirect/fence unless an ADR explicitly says otherwise.

## 10. Validation expectations

Useful validation for this folder should cover:

- no flora catalog records, indexes, manifests, occurrence crosswalks, or habitat references are stored here;
- no sensitivity-relevant flora details are stored here;
- no receipts, proofs, release records, registry records, policy rules, schemas, source code, or published artifacts are stored here;
- any non-README content is tied to an active migration or drift note;
- CI or review checks flag root-level `catalog/domain/flora/` writes;
- links point users to `data/catalog/domain/` and other canonical homes.

## 11. Safe change pattern

For changes under `catalog/domain/flora/`:

1. Confirm the change is redirect documentation, migration support, or drift documentation only.
2. Confirm it does not create a parallel flora domain catalog authority.
3. Confirm no sensitivity-relevant flora detail is added.
4. Confirm durable flora catalog records are placed under the governed `data/catalog/` tree.
5. Confirm receipts/proofs/release records are placed under their owning roots.
6. Document migration and rollback if any misplaced material was moved.
7. Update docs and validation rules when behavior materially changes.

## 12. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual root-level `catalog/domain/flora/` contents are verified.
- [ ] Any misplaced flora catalog material is migrated or documented as drift.
- [ ] Canonical flora catalog placement under `data/catalog/domain/` is accepted and documented.
- [ ] No trust-bearing records live here.
- [ ] No flora catalog records, sensitivity-relevant flora detail, STAC/DCAT/PROV records, registry records, receipts, proofs, release records, published artifacts, schemas, contracts, policy rules, source code, or lifecycle data live here.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## 13. Open verification items

| Item | Why it matters |
|---|---|
| Confirm actual files under root-level `catalog/domain/flora/` | Prevents overclaiming or missing drift |
| Confirm whether any workflow writes here | Required before producer claims |
| Confirm accepted canonical flora catalog placement | Required before final migration claims |
| Confirm sensitivity/redaction handling | Required before safe-publication claims |
| Confirm migration status to `data/catalog/domain/` | Required before canonical-home claims beyond doctrine |
| Confirm CI/review guard exists | Required before enforcement claims |
| Confirm no trust records are stored here | Required before Directory Rules compliance claims |
| Confirm ADR status for root-level `catalog/domain/flora/` | Required before long-term retention claims |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The previous README was empty. This replacement adds a flora-domain-catalog redirect and anti-parallel-authority contract without claiming flora catalog files, migration work, CI enforcement, producer workflows, canonical sublane acceptance, sensitivity decisions, or ADR disposition are implemented.

</details>

## Status summary

`catalog/domain/flora/` is a root-level compatibility redirect and flora-domain drift fence. It is not the canonical flora domain catalog home.

Flora catalog authority belongs under the governed `data/catalog/domain/` tree; trust-bearing support belongs under `data/receipts/`, `data/proofs/`, and `release/`; released public-safe products belong under `data/published/`.

<p align="right"><a href="#top">Back to top</a></p>
