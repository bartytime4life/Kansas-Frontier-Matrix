<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-proof-readme
title: catalog/proof/ — Proof Compatibility Redirect
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Catalog steward · Proof steward · Evidence steward · Data steward · Receipt steward · Release steward · Policy steward · Schema steward · Docs steward
created: 2026-06-16
updated: 2026-07-10
policy_label: public
related:
  - ../README.md
  - release/README.md
  - release-closure/README.md
  - ../../data/README.md
  - ../../data/catalog/README.md
  - ../../data/proofs/README.md
  - ../../data/receipts/README.md
  - ../../data/published/README.md
  - ../../data/registry/README.md
  - ../../release/README.md
  - ../../schemas/contracts/v1/
  - ../../contracts/
  - ../../policy/
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, catalog, proof, evidence, evidence-bundle, proof-pack, compatibility-root, redirect, data-proofs, receipt-proof-separation, release-governance, non-authoritative, drift-fence, no-public-use]
notes:
  - "Refreshes the root-level catalog/proof compatibility-redirect fence."
  - "Root-level catalog/proof/ is compatibility and drift-control documentation only, not canonical proof authority."
  - "Canonical proof-support material belongs under data/proofs/; dedicated data/proofs/release/ and data/proofs/release-closure/ sublanes were not found on main during this revision and remain NEEDS VERIFICATION until created or accepted."
  - "Receipts are process memory under data/receipts/; release-governance records belong under release/; catalog records belong under data/catalog/."
  - "Do not add EvidenceBundles, ProofPacks, attestations, receipts, release records, catalog records, schemas, policy rules, published artifacts, generated proof bundles, or producer outputs here without an ADR/migration note."
  - "Actual current contents beyond this README and documented child README paths, historical producers, workflow writes, migration status, proof schema maturity, canonical proof sublane acceptance, CI/review enforcement, public-client/producer exclusion, and ADR disposition remain NEEDS VERIFICATION."
  - "v0.2 adds current evidence basis, Directory Rules placement basis, canonical data/proofs alignment, receipt/proof/catalog/release separation, child redirect posture, minimum safe redirect slice, anti-bypass matrix, migration/rollback posture, and safe language rules without claiming migration or enforcement maturity."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# Proof Compatibility Redirect

`catalog/proof/`

**Root-level compatibility and drift-control fence for legacy or accidental proof placement. Canonical proof support belongs under `data/proofs/`; process receipts belong under `data/receipts/`; catalog records belong under `data/catalog/`; release-governance records belong under `release/`.**

![status](https://img.shields.io/badge/status-draft-blue)
![authority](https://img.shields.io/badge/authority-compatibility-orange)
![proof home](https://img.shields.io/badge/proof__home-data%2Fproofs-blue)
![receipt home](https://img.shields.io/badge/receipt__home-data%2Freceipts-purple)
![release home](https://img.shields.io/badge/release__home-release%2F-blueviolet)
![trust](https://img.shields.io/badge/trust__content-forbidden-red)
![truth](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)

[Evidence](#0-evidence-basis-for-this-revision) · [Purpose](#1-purpose) · [Canonical homes](#2-canonical-homes) · [Boundary](#3-authority-boundary) · [Allowed](#5-allowed-contents) · [Forbidden](#6-forbidden-contents) · [Children](#8-child-redirect-lanes) · [Migration](#11-migration-posture) · [Definition of done](#18-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Path:** `catalog/proof/README.md`  
> **Responsibility root:** compatibility redirect / drift fence only  
> **Canonical proof home:** `data/proofs/` unless an accepted ADR changes the proof authority model  
> **Receipt home:** `data/receipts/`  
> **Catalog home:** `data/catalog/`  
> **Release-governance home:** `release/`  
> **Directory Rules basis:** file location encodes ownership, governance, and lifecycle. Proof-support records belong under `data/proofs/`; process-memory receipts belong under `data/receipts/`; catalog records belong under `data/catalog/`; release-governance records belong under `release/`; released public-safe artifacts belong under `data/published/`. Root-level `catalog/proof/` is a compatibility redirect only and must not become a parallel proof, receipt, catalog, release, schema, policy, source-registry, published-artifact, pipeline, package, tool, search, or UI authority.  
> **Truth posture:** CONFIRMED current GitHub README path / CONFIRMED parent root-level `catalog/README.md` exists and treats `catalog/` as compatibility redirect / CONFIRMED `data/proofs/README.md` exists and treats `data/proofs/` as proof-support root / CONFIRMED `data/receipts/README.md` exists and states receipts are process memory, not proof, catalog, release, or publication approval / CONFIRMED `release/README.md` exists and treats `release/` as release-governance root / CONFIRMED ADR-0011 document exists and states proposed receipt/proof/catalog/publication separation / CONFIRMED Directory Rules document exists / CONFIRMED `data/proofs/release/README.md` and `data/proofs/release-closure/README.md` were not found on `main` during this revision / PROPOSED root-level `catalog/proof/` redirect contract / UNKNOWN actual files beyond README, historical producers, workflow writes, migration status, proof schema maturity, canonical proof sublane acceptance, CI/review guard, public-client/producer exclusion, and ADR disposition

> [!CAUTION]
> Do not make `catalog/proof/` a parallel proof authority. KFM EvidenceBundles, ProofPacks, attestations, citation-validation bundles, catalog-closure proof, release-readiness proof, and claim-support records belong under `data/proofs/`; process receipts belong under `data/receipts/`; catalog and discovery carriers belong under `data/catalog/`; release manifests, release decisions, rollback cards, correction notices, withdrawal records, supersession records, signatures, and release-state records belong under `release/`.

---

## Quick jump

- [0. Evidence basis for this revision](#0-evidence-basis-for-this-revision)
- [1. Purpose](#1-purpose)
- [2. Canonical homes](#2-canonical-homes)
- [3. Authority boundary](#3-authority-boundary)
- [4. Default posture](#4-default-posture)
- [5. Allowed contents](#5-allowed-contents)
- [6. Forbidden contents](#6-forbidden-contents)
- [7. Directory shape](#7-directory-shape)
- [8. Child redirect lanes](#8-child-redirect-lanes)
- [9. Minimum safe redirect slice](#9-minimum-safe-redirect-slice)
- [10. Diagram](#10-diagram)
- [11. Migration posture](#11-migration-posture)
- [12. Runtime and producer anti-bypass matrix](#12-runtime-and-producer-anti-bypass-matrix)
- [13. Inspection path](#13-inspection-path)
- [14. Validation expectations](#14-validation-expectations)
- [15. Safe change pattern](#15-safe-change-pattern)
- [16. Rollback and correction posture](#16-rollback-and-correction-posture)
- [17. Safe language rules](#17-safe-language-rules)
- [18. Definition of done](#18-definition-of-done)
- [19. Open verification items](#19-open-verification-items)

---

## 0. Evidence basis for this revision

This README is a documentation boundary, not migration proof, proof-validation proof, release approval proof, or CI enforcement proof. The 2026-07-10 revision updates an existing compatibility README and keeps maturity bounded while aligning root-level `catalog/proof/` with the canonical `data/proofs/` proof-support root, separate `data/receipts/` process-memory root, separate `data/catalog/` catalog root, separate `release/` governance root, and Directory Rules placement posture.

| Evidence item | Status | What it supports | What it does not prove |
|---|---|---|---|
| `catalog/proof/README.md` exists on `main`. | CONFIRMED | This is an existing README update, not a new path proposal. | It does not prove actual contents beyond the README, historical producers, migration status, CI enforcement, public-client exclusion, or ADR disposition. |
| `catalog/README.md` exists and treats root-level `catalog/` as a compatibility redirect, not canonical catalog authority. | CONFIRMED document presence and redirect posture | `catalog/proof/` should inherit root-level redirect/fence behavior. | It does not prove all root-level catalog/proof drift has been removed. |
| `data/proofs/README.md` exists and treats `data/proofs/` as proof-support root. | CONFIRMED proof-root posture | Canonical proof support belongs under `data/proofs/` or accepted proof-family/domain lanes. | It does not prove emitted proof inventories, schemas, validators, fixtures, CI workflows, or release-gate enforcement. |
| `data/proofs/release/README.md` and `data/proofs/release-closure/README.md` were not found on `main` during this revision. | CONFIRMED fetch result from current session | Dedicated proof sublanes for release and release-closure remain `NEEDS VERIFICATION` until created or accepted. | It does not prove future sublanes are invalid or that release proof files do not exist elsewhere under `data/proofs/`. |
| `data/receipts/README.md` exists and states receipts are process memory, not proof, catalog, release, or publication approval. | CONFIRMED receipt-root posture | Receipt files must not be stored or treated as proof in this redirect path. | It does not prove emitted receipt inventories, signing, validators, or release integration. |
| `release/README.md` exists and treats `release/` as release-governance root for release decisions, manifests, corrections, rollback, and signatures. | CONFIRMED release-root posture | Release-governance records belong under `release/`, not root-level `catalog/proof/`. | It does not prove release manifest lane convention, singular/plural lane choice, or release workflow maturity is finalized. |
| `docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md` exists and states the proposed separation rule `receipt ≠ proof ≠ catalog ≠ publication`. | CONFIRMED ADR document presence; PROPOSED decision status | Supports separation language while keeping ADR acceptance bounded. | It does not prove ADR acceptance or validator enforcement. |
| `docs/doctrine/directory-rules.md` exists and states that file location encodes ownership, governance, and lifecycle. | CONFIRMED placement doctrine | Root-level `catalog/proof/` must remain a compatibility fence; proof, receipt, catalog, and release records belong under their owning roots. | It does not prove live repo drift has been fully audited. |

[Back to top](#top)

---

## 1. Purpose

`catalog/proof/` is a **root-level compatibility redirect** for proof path drift.

It exists only to prevent accidental, legacy, generated, copied, or externally imported proof material from becoming a parallel authority outside KFM's proof-support, process-memory, catalog, and release-governance roots.

This folder should not be used for canonical:

- EvidenceBundles, ProofPacks, attestations, citation-validation bundles, claim-support records, or proof envelopes;
- catalog-closure proof, release-readiness proof, source-rights proof, sensitivity proof, correction proof, rollback proof, or integrity proof;
- process receipts, validation receipts, redaction/generalization receipts, AI receipts, release dry-run receipts, migration receipts, or telemetry receipts;
- ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, release signature, withdrawal, supersession, or release-decision records;
- catalog records, STAC/DCAT/PROV records, CatalogMatrix records, source descriptors, or discovery indexes;
- released public-safe artifacts, tiles, API payloads, stories, reports, or exports;
- schemas, contracts, policy rules, producer code, generated manifests, or build outputs.

This README does not prove that any proof material currently exists here, that migration has been completed, that producer tools avoid this path, that public clients exclude this path, that proof schemas are implemented, that CI blocks writes here, or that any ADR has finalized long-term retention of this compatibility root.

[Back to top](#top)

---

## 2. Canonical homes

Canonical proof-support material belongs under:

```text
data/proofs/
```

Dedicated proof sublanes may be used only when accepted and verified:

```text
data/proofs/release/           # NEEDS VERIFICATION — README not found on main during this revision
data/proofs/release-closure/   # NEEDS VERIFICATION — README not found on main during this revision
```

Process-memory receipts belong under:

```text
data/receipts/
```

Catalog records and discovery/interchange carriers belong under:

```text
data/catalog/
```

Release decision and release-state material belongs under:

```text
release/
```

Released public-safe artifacts belong under:

```text
data/published/
```

The root-level `catalog/proof/` directory is a redirect/fence only.

```text
catalog/proof/          # compatibility redirect only; do not add proof records here
data/proofs/            # canonical proof-support root
data/receipts/          # process-memory root
data/catalog/           # catalog-stage lifecycle root
release/                # release-governance root
data/published/         # released public-safe artifacts after governed release
```

If a future ADR or migration creates additional `data/proofs/` proof-family sublanes, this README should be updated to cite the accepted target, producer-configuration evidence, validation evidence, and any migration, correction, or rollback records.

## 3. Authority boundary

`catalog/proof/` has **no canonical proof authority**, **no receipt authority**, **no catalog authority**, and **no release authority**. It may hold only redirect guidance, migration notes, drift logs, or temporary markers while misplaced material is reviewed and moved into its proper owning root.

```text
WRONG / LEGACY ROOT          CANONICAL PROOF HOME             RECEIPT / CATALOG / RELEASE HOMES
catalog/proof/          -->  data/proofs/                -->  data/receipts/
compatibility fence only     proof support / bundles          data/catalog/
not authoritative            accepted proof-family lanes      release/
                                                               data/published/
```

A proof record outside `data/proofs/` should be treated as proof drift until reviewed and migrated. A receipt outside `data/receipts/` should be treated as process-memory drift. A catalog record outside `data/catalog/` should be treated as catalog drift. A release decision record outside `release/` should be treated as release-plane drift.

## 4. Default posture

Anything found under root-level `catalog/proof/` should be treated as **NEEDS VERIFICATION** and potentially misplaced.

Do not expose, publish, index, cite, search, cache, export, tile, or depend on root-level proof files as canonical proof records. First confirm object family, claim scope, source refs, provenance, rights, sensitivity, evidence resolution, schema validity, policy decision, lifecycle state, receipt support, catalog closure, release state, rollback path, correction path, and whether the object is actually a proof, receipt, catalog carrier, or release-governance record.

## 5. Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| README / redirect docs | `README.md` | Compatibility fence only |
| Migration note | `MIGRATION.md` | Temporary and ADR/review-linked |
| Drift note | `DRIFT.md`, `OPEN-QUESTIONS.md` | Must point to canonical homes and review steps |
| Placeholder marker | `.gitkeep` | Does not authorize proof, receipt, catalog, release, policy, schema, or publication content |
| Child redirect README | `release/README.md`, `release-closure/README.md` | Must remain compatibility guidance unless canonical homes are accepted elsewhere |

## 6. Forbidden contents

| Forbidden here | Correct home |
|---|---|
| EvidenceBundles, ProofPacks, attestations, citation-validation bundles, claim-support records | `data/proofs/` or accepted proof-family/domain lanes |
| Catalog-closure proof, release-readiness proof, evidence-closure proof, policy-closure proof | `data/proofs/` and governed validation homes |
| Receipts, validation reports, redaction/generalization receipts, AI receipts, release dry-run receipts, migration receipts | `data/receipts/` |
| Catalog records, catalog indexes, STAC/DCAT/PROV records, CatalogMatrix records | `data/catalog/` |
| Catalog-derived or proof-derived public products | `data/published/` after governed release |
| Source descriptors, source registry rows, rights rows, sensitivity rows | `data/registry/` or governed registry homes |
| ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, release signatures, release decisions, withdrawals, supersession records | `release/` |
| Schemas and machine-shape contracts | `schemas/contracts/v1/` |
| Human contracts and object-meaning docs | `contracts/` |
| Policy rules and policy decisions | `policy/` and governed policy-decision homes |
| Source code, scripts, packages, pipelines, build tools, producers | `apps/`, `packages/`, `tools/`, `scripts/`, `pipelines/` |
| Raw, work, quarantine, processed, catalog, triplet, or published lifecycle data | `data/` lifecycle subtrees |

## 7. Directory shape

Current implementation inventory remains `NEEDS VERIFICATION`.

```text
catalog/proof/
├── README.md                 # compatibility redirect / drift fence
├── release/README.md         # child compatibility redirect if path exists
├── release-closure/README.md # child compatibility redirect if path exists
├── MIGRATION.md              # PROPOSED only if migration is active
└── DRIFT.md                  # PROPOSED only if misplaced proof material is found
```

> [!WARNING]
> Do not treat this suggested shape as complete repo inventory. Verify actual contents before making inventory, producer, enforcement, release, proof, or migration claims.

## 8. Child redirect lanes

Child lanes under root-level `catalog/proof/` are compatibility guidance only unless an accepted ADR or migration note says otherwise.

| Child lane | Status | Canonical target | Boundary |
|---|---|---|---|
| `catalog/proof/release/` | Compatibility redirect path when present | `data/proofs/` or an accepted `data/proofs/release/` sublane | Release-governance records still belong under `release/`. |
| `catalog/proof/release-closure/` | Compatibility redirect path when present | `data/proofs/` or an accepted `data/proofs/release-closure/` sublane | Closure receipts, catalog closure, and release decisions stay in their owning roots. |

These child lanes must not become proof stores, release manifests, catalog indexes, receipt buckets, public export homes, or producer output targets.

## 9. Minimum safe redirect slice

A smallest safe `catalog/proof/` state should prove only that the folder prevents drift; it should not contain trust-bearing material.

| Slice item | Minimum requirement | Why it matters |
|---|---|---|
| Redirect README | Points to `data/proofs/` for proof support, `data/receipts/` for process memory, and `release/` for release governance | Prevents parallel authority |
| No proof records | No EvidenceBundle, ProofPack, release attestation, citation validation, or claim-support files | Keeps proof support in lifecycle proof root |
| No receipt records | No RunReceipt, ValidationReceipt, AIReceipt, migration receipt, release dry-run receipt, or redaction receipt | Preserves receipt/process-memory root |
| No release-governance records | No ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, signatures, withdrawals, supersessions, or release decisions | Preserves release root authority |
| No catalog records | No STAC, DCAT, PROV, CatalogMatrix, source descriptor, or catalog index files | Preserves catalog and registry roots |
| Drift procedure | Explains how to inspect and migrate misplaced records | Keeps remediation reversible |
| Producer guard | Producers, generators, scripts, and CI should not write durable proof/release records here | Prevents reintroducing drift |
| Public-use guard | Public clients, search services, map runtimes, exports, and indexes must not read from this path as canonical | Preserves governed access path |
| Child-lane guard | Root-level child proof redirect lanes remain compatibility only | Prevents subfolder drift from hardening into authority |
| Verification backlog | Open items stay visible | Prevents documentation from pretending migration/enforcement is complete |

## 10. Diagram

```mermaid
flowchart TD
    wrong["catalog/proof/\nroot-level redirect"] --> review["review for proof / receipt / catalog / release drift"]
    review --> classify["classify object family"]
    classify --> proofs["data/proofs/\nproof support / EvidenceBundle / ProofPack"]
    proofs -. optional .-> proof_release["data/proofs/release/\nNEEDS VERIFICATION"]
    proofs -. optional .-> proof_closure["data/proofs/release-closure/\nNEEDS VERIFICATION"]
    classify --> receipts["data/receipts/\nprocess memory"]
    classify --> catalog["data/catalog/\ncatalog records"]
    classify --> release["release/\nReleaseManifest / decisions / rollback / correction"]
    release --> published["data/published/\npublic-safe released artifacts"]
    catalog --> release
    proofs --> release
    receipts --> proofs
    wrong -. "must not be public/canonical" .-> published
    wrong -. "must not be producer target" .-> proofs
```

## 11. Migration posture

If proof files are found here:

1. Do not publish, cite, index, search, cache, export, tile, or depend on them.
2. Identify whether they are EvidenceBundles, ProofPacks, attestations, citation-validation records, claim-support records, receipts, catalog records, CatalogMatrix/STAC/DCAT/PROV records, release manifests, release decisions, rollback/correction records, source registry rows, schemas, policy records, published-output material, generated previews, temporary build artifacts, or producer outputs.
3. Determine whether the file is historical drift, generated drift, copied output, unreviewed local work, or an intentional migration marker.
4. Move or regenerate durable proof material into `data/proofs/` or an accepted, verified sublane under it.
5. Move receipts into `data/receipts/`.
6. Move catalog records into `data/catalog/` and source/rights/sensitivity registry records into `data/registry/`.
7. Move release-governance records into `release/`.
8. Move published artifacts into `data/published/` only after governed release approval.
9. Preserve provenance, source refs, digests, receipts, review notes, producer identity, release refs, correction refs, and rollback path.
10. Add a drift register, migration note, or correction note if the misplaced material was previously consumed.
11. Add or update validation checks so producers do not recreate root-level proof drift.
12. Leave `catalog/proof/` as a redirect/fence unless an accepted ADR explicitly changes the authority model.

## 12. Runtime and producer anti-bypass matrix

| Bypass risk | Required behavior | Review signal |
|---|---|---|
| Producer writes proof records to `catalog/proof/` | Fail review/CI; write to `data/proofs/` or accepted proof sublane instead | Generator config and output paths checked |
| Producer writes receipts here | Fail review/CI; write to `data/receipts/` instead | Receipt path check passes |
| Producer writes ReleaseManifest or release decisions here | Fail review/CI; write to `release/` instead | Release path check passes |
| Public client reads root-level proof path | Deny; route through governed API/release/public-safe path | Client/search/index config excludes this path |
| Root-level proof is treated as canonical | Mark as drift and migrate/regenerate | Migration note references canonical target |
| Child redirect lane becomes proof store | Mark as drift; migrate to `data/proofs/` | Directory review blocks trust support records |
| Receipts/proofs/release records stored here | Move to owning roots | Directory review blocks mixed-family storage |
| Schema/profile file stored here | Move to `schemas/` or standards docs as appropriate | Schema-home review passes |
| Policy rule stored here | Move to `policy/` | Policy-root review passes |
| Published artifact stored here | Move to `data/published/` after release gate | Release/publication review passes |
| Search/cache/export/tile pipeline consumes this path | Deny as canonical; switch to governed proof/release source | Producer and client config reviewed |
| Drift file already consumed downstream | Add correction/migration note and rollback path | Correction path is auditable |
| README claims CI enforcement without run/check evidence | Mark enforcement `NEEDS VERIFICATION` | Current CI evidence cited before pass claims |

## 13. Inspection path

Actual root-level contents, producers, workflow writes, migration status, proof-schema maturity, canonical proof sublane acceptance, CI/review enforcement, public-client/index exclusion, and current ADR disposition remain `NEEDS VERIFICATION`.

```bash
find catalog/proof -maxdepth 6 -type f | sort
find data/proofs data/receipts data/catalog data/published data/registry release schemas contracts policy docs tools scripts pipelines pipeline_specs .github/workflows -maxdepth 6 -type f 2>/dev/null | grep -Ei 'EvidenceBundle|EvidenceRef|ProofPack|proof|citation|closure|release|ReleaseManifest|PromotionDecision|RollbackCard|CorrectionNotice|withdraw|supersede|RunReceipt|AIReceipt|ValidationReceipt|CatalogMatrix|stac|dcat|prov|schema|policy|validator|publish|workflow|migration|drift' | sort
```

## 14. Validation expectations

Useful validation for this folder should cover:

- no EvidenceBundles, ProofPacks, attestations, citation-validation records, or claim-support records are stored here;
- no receipts, validation reports, AI receipts, migration receipts, release dry-run receipts, or redaction/generalization receipts are stored here;
- no ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, release decisions, withdrawals, supersession records, signatures, or release-state records are stored here;
- no STAC, DCAT, PROV, CatalogMatrix, source registry records, policy rules, schemas, source code, pipelines, tools, producer outputs, or published artifacts are stored here;
- any non-README content is tied to an active migration, drift note, or placeholder marker;
- producer tools, scripts, generated outputs, workflows, indexes, search services, public clients, exports, tile jobs, and map runtimes do not target `catalog/proof/` as canonical;
- child redirect lanes do not store proof, receipt, catalog, release, schema, policy, or public-output records;
- links point users to `data/proofs/`, `data/receipts/`, `data/catalog/`, `release/`, `data/published/`, and other owning roots;
- CI or review checks flag root-level `catalog/proof/` writes when enforcement exists;
- CI/pass/enforcement state is not claimed without current evidence.

## 15. Safe change pattern

For changes under `catalog/proof/`:

1. Confirm the change is redirect documentation, migration support, drift documentation, or a non-authoritative placeholder only.
2. Confirm it does not create a parallel proof, receipt, catalog, release, schema, policy, or publication authority.
3. Confirm durable proof records are placed under `data/proofs/` or an accepted and verified sublane.
4. Confirm receipts remain under `data/receipts/`.
5. Confirm catalog records remain under `data/catalog/`.
6. Confirm release-governance records remain under `release/`.
7. Confirm published artifacts appear only under `data/published/` after governed release.
8. Confirm no public client, search index, map runtime, export job, tile job, story/focus/evidence surface, proof producer, release producer, or cache reads this path as canonical.
9. Document migration, correction, and rollback if any misplaced material was moved or previously consumed.
10. Update docs and validation rules when behavior materially changes.

## 16. Rollback and correction posture

If material was added here by mistake, rollback should be small and auditable:

- remove or revert the misplaced file from `catalog/proof/`;
- regenerate or move durable proof support into `data/proofs/` through a governed migration;
- move receipts into `data/receipts/`;
- move catalog records into `data/catalog/`;
- move release-governance records into `release/` through the appropriate release review path;
- preserve digest/provenance notes for anything already referenced;
- add a correction note if public, semi-public, generated downstream, search, export, cache, release, proof, or catalog artifacts consumed the misplaced path;
- update producer configuration and tests so the drift is not recreated.

## 17. Safe language rules

Use these terms carefully:

| Phrase | Allowed here? | Safer wording |
|---|---:|---|
| "canonical proof in `catalog/proof/`" | No | "misplaced or legacy proof requiring review" |
| "receipt proves the claim" | No | "receipt records process execution; proof/evidence still required" |
| "catalog record is proof" | No | "catalog record is discovery/interchange metadata" |
| "ReleaseManifest in `catalog/proof/`" | No | "release-governance manifest belongs under `release/`" |
| "published from `catalog/proof/`" | No | "published only after release via canonical lifecycle path" |
| "CI blocks this" | Only with current evidence | "CI guard remains NEEDS VERIFICATION" |
| "migration complete" | Only with migration evidence | "migration status remains NEEDS VERIFICATION" |
| "safe to consume" | Only after release/access evidence | "do not consume as canonical from this path" |
| "proof sublane exists" | Only with path evidence | "dedicated proof sublane remains NEEDS VERIFICATION" |

## 18. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual root-level `catalog/proof/` contents are verified.
- [ ] Actual child-lane contents under `catalog/proof/` are verified.
- [ ] Any misplaced proof material is migrated, removed, regenerated under `data/proofs/`, or documented as drift.
- [ ] Any misplaced receipt material is migrated, removed, regenerated under `data/receipts/`, or documented as drift.
- [ ] Any misplaced catalog material is migrated, removed, regenerated under `data/catalog/`, or documented as drift.
- [ ] Any misplaced release-governance material is migrated, removed, regenerated under `release/`, or documented as drift.
- [ ] `data/proofs/` is confirmed as the canonical proof-support home in current docs.
- [ ] Any dedicated proof-family sublanes are created, accepted, and documented before being named canonical.
- [ ] No trust-bearing records live here.
- [ ] No EvidenceBundles, ProofPacks, receipts, catalog records, release records, published artifacts, schemas, contracts, policy rules, source code, producer outputs, or lifecycle data live here.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.
- [ ] Any migration has a rollback and correction path.

## 19. Open verification items

| Item | Why it matters |
|---|---|
| Confirm actual files under root-level `catalog/proof/` | Prevents overclaiming or missing drift |
| Confirm whether any workflow writes here | Required before producer claims |
| Confirm proof schema and EvidenceBundle maturity | Required before implementation claims |
| Confirm canonical proof sublane acceptance | Required before naming sublanes as canonical |
| Confirm migration status to `data/proofs/` | Required before canonical-home claims beyond doctrine |
| Confirm CI/review guard exists | Required before enforcement claims |
| Confirm no trust records are stored here | Required before Directory Rules compliance claims |
| Confirm ADR status for root-level `catalog/proof/` | Required before long-term retention claims |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The previous README established `catalog/proof/` as a proof-specific redirect and anti-parallel-authority contract without claiming proof files, EvidenceBundle implementation maturity, migration work, CI enforcement, producer workflows, or ADR disposition are implemented.

This revision preserves that boundary and adds stronger family separation, evidence basis, child redirect posture, producer/public-use guardrails, rollback/correction posture, safe language rules, and explicit `NEEDS VERIFICATION` treatment for unverified canonical proof sublanes.

</details>

## Status summary

`catalog/proof/` is a root-level compatibility redirect and proof drift fence. It is not the canonical proof home and must not become a public or semi-public trust source.

Proof authority belongs under `data/proofs/`; receipts belong under `data/receipts/`; catalog records belong under `data/catalog/`; release decisions belong under `release/`; released public-safe products belong under `data/published/`.

<p align="right"><a href="#top">Back to top</a></p>
