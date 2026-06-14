<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-domains-agriculture-readme
title: Domains Agriculture Pipeline Specs Compatibility README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <agriculture-domain-steward>
  - <docs-steward>
  - <governance-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/domains/agriculture/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipeline_specs/README.md
  - pipeline_specs/agriculture/README.md
  - pipelines/README.md
  - pipelines/domains/agriculture/README.md
  - docs/domains/agriculture/ARCHITECTURE.md
  - data/registry/sources/agriculture/
  - data/receipts/pipeline/agriculture/
  - tests/pipeline_specs/agriculture/
  - fixtures/pipeline_specs/agriculture/
tags: [kfm, pipeline-specs, domains, agriculture, compatibility, declarative-config, governance]
notes:
  - "This README replaces the one-character pipeline_specs/domains/agriculture stub with a compatibility/guardrail contract."
  - "Canonical Agriculture declarative pipeline specs currently belong in pipeline_specs/agriculture/, not this nested domains path."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Use this path only as a compatibility, migration, or alias guardrail unless an ADR changes the accepted spec layout."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domains Agriculture Pipeline Specs Compatibility Guardrail

> Guardrail README for `pipeline_specs/domains/agriculture/`. The canonical Agriculture spec lane is `pipeline_specs/agriculture/`; executable Agriculture logic belongs under `pipelines/domains/agriculture/`.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![canonical-spec-root](https://img.shields.io/badge/canonical-pipeline__specs%2Fagriculture%2F-d62728)
![authority](https://img.shields.io/badge/authority-compatibility%20guardrail-455a64)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fagriculture%2F-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/domains/agriculture/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Canonical Agriculture spec lane:** `pipeline_specs/agriculture/`  
**Companion implementation lane:** `pipelines/domains/agriculture/` — executable pipeline logic, the **how**  
**Placement posture:** compatibility/guardrail only; authoritative specs here are `NEEDS VERIFICATION / ADR`.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Anti-collapse rules](#3-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Migration posture](#6-migration-posture)
- [7. Directory contract](#7-directory-contract)
- [8. Definition of done](#8-definition-of-done)
- [9. Open questions](#9-open-questions)

---

## 1. Purpose

`pipeline_specs/domains/agriculture/` is a compatibility/guardrail path, not the canonical Agriculture spec home.

Its purpose is to prevent a parallel-authority drift pattern:

```text
pipeline_specs/agriculture/           = canonical Agriculture declarative specs
pipeline_specs/domains/agriculture/   = compatibility / migration guardrail only
pipelines/domains/agriculture/        = executable Agriculture implementation
```

This path may document migration notes or compatibility pointers, but it should not become a second authoritative Agriculture spec tree without an ADR or migration note.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why does this README exist? | To guard against nested-domain spec drift. | CONFIRMED need from requested path |
| Is this the canonical Agriculture spec home? | No. Current canonical Agriculture spec lane is `pipeline_specs/agriculture/`. | CONFIRMED current repo evidence |
| What does `pipeline_specs/` own? | Declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| What does `pipelines/domains/agriculture/` own? | Executable Agriculture pipeline behavior. | CONFIRMED companion-lane posture |
| Can real specs live here? | Not by default. Real specs here require ADR or documented migration. | NEEDS VERIFICATION / ADR |
| Does this path approve release or store data? | No. Specs do not approve release or store lifecycle outputs. | CONFIRMED boundary posture |

> [!IMPORTANT]
> Do not split Agriculture specs between `pipeline_specs/agriculture/` and `pipeline_specs/domains/agriculture/` for convenience. That creates a parallel authority surface and weakens buildability, review, and rollback.

[⬆ Back to top](#top)

---

## 3. Anti-collapse rules

Disallowed collapses:

```text
pipeline_specs/domains/agriculture/ -> pipeline_specs/agriculture/
nested path convenience -> authority root
spec profile -> executable pipeline
spec profile -> release approval
source list -> source authority
schedule -> source freshness proof
validation profile -> ValidationReport
catalog profile -> catalog truth
publish profile -> PUBLISHED
spec summary -> evidence
```

Required separations:

- canonical Agriculture declarative specs stay in `pipeline_specs/agriculture/` unless changed by ADR;
- executable Agriculture logic stays in `pipelines/domains/agriculture/`;
- source descriptors stay in accepted source registry homes;
- tests and fixtures stay in `tests/` and `fixtures/`;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents are limited to guardrail material:

- this `README.md`;
- migration notes for moving misplaced nested specs to `pipeline_specs/agriculture/`;
- temporary compatibility pointers during a governed migration;
- deprecation notices pointing maintainers to the canonical Agriculture spec lane;
- an ADR reference if a future decision changes the canonical layout.

A good placement test:

> If the file is an actual Agriculture declarative pipeline spec, it should normally live in `pipeline_specs/agriculture/`, not here.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Agriculture declarative pipeline specs | `pipeline_specs/agriculture/` |
| Executable Agriculture pipeline code | `pipelines/domains/agriculture/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/agriculture/` or accepted registry home |
| Agriculture doctrine/object meaning | `docs/domains/agriculture/`, `contracts/domains/agriculture/` |
| JSON Schemas | `schemas/contracts/v1/domains/agriculture/` or accepted schema home |
| Policy/review decisions | `policy/` or accepted review roots |
| Tests | `tests/pipeline_specs/agriculture/` |
| Fixtures | `fixtures/pipeline_specs/agriculture/` |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Migration posture

If a file is discovered under this path, classify it before moving:

| Finding | Default action | Status |
|---|---|---|
| Actual Agriculture declarative spec | Move to `pipeline_specs/agriculture/` through a reviewable migration. | PROPOSED |
| Executable code | Move to `pipelines/domains/agriculture/` or an accepted implementation lane. | PROPOSED |
| Test fixture | Move to `fixtures/pipeline_specs/agriculture/` or accepted fixture home. | PROPOSED |
| Test code | Move to `tests/pipeline_specs/agriculture/`. | PROPOSED |
| Receipt/proof output | Move to accepted `data/receipts/` or `data/proofs/` home. | PROPOSED |
| Release decision | Move to `release/`. | PROPOSED |
| Unclear file | Hold, document drift, and request steward review. | NEEDS VERIFICATION |

Migration discipline:

1. preserve history;
2. document old and new paths;
3. update references;
4. add compatibility pointers only when needed;
5. validate with tests or link checks;
6. provide rollback instructions.

[⬆ Back to top](#top)

---

## 7. Directory contract

Recommended long-term shape:

```text
pipeline_specs/domains/agriculture/
└── README.md   # compatibility / guardrail only
```

Canonical Agriculture spec shape remains:

```text
pipeline_specs/agriculture/
├── README.md
├── ingest.yaml                 # PROPOSED
├── normalize.yaml              # PROPOSED
├── validate.yaml               # PROPOSED
├── catalog.yaml                # PROPOSED
├── triplets.yaml               # PROPOSED
├── publish.yaml                # PROPOSED
├── rollback.yaml               # PROPOSED
├── watchers.yaml               # PROPOSED
└── <sublane-or-source-profile>.yaml   # PROPOSED
```

This README should not be used as evidence that `pipeline_specs/domains/agriculture/` is an accepted alternative to `pipeline_specs/agriculture/`.

[⬆ Back to top](#top)

---

## 8. Definition of done

This README is done when it:

- replaces the one-character `pipeline_specs/domains/agriculture/README.md` stub;
- marks this nested path as compatibility/guardrail only;
- points authoritative Agriculture declarative specs to `pipeline_specs/agriculture/`;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- prevents a parallel domain-spec authority tree;
- gives maintainers a migration posture for misplaced files.

Future work here should be limited to guardrail or migration documentation unless an ADR changes the root contract.

[⬆ Back to top](#top)

---

## 9. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-DOM-AG-001` | Should `pipeline_specs/domains/agriculture/` remain as a guardrail path or be removed after cleanup? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-DOM-AG-002` | Should a lint rule block specs under `pipeline_specs/domains/agriculture/`? | NEEDS VERIFICATION |
| `PIPE-SPEC-DOM-AG-003` | Should this path be referenced from `pipeline_specs/agriculture/README.md` as a compatibility warning? | NEEDS VERIFICATION |
| `PIPE-SPEC-DOM-AG-004` | Should misplaced nested-domain specs be tracked in a drift register? | NEEDS VERIFICATION |

---

## Maintainer note

Treat this directory as a warning sign. Do not add executable code, declarative specs, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, or generated summaries here unless a governed ADR or migration note says why.
