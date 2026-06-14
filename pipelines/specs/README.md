<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-specs-readme
title: Pipelines Specs Compatibility README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <pipeline-spec-steward>
  - <docs-steward>
  - <governance-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/specs/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipeline_specs/README.md
  - pipeline_specs/
  - pipelines/
  - tests/
  - fixtures/
  - data/receipts/pipeline/
tags: [kfm, pipelines, specs, pipeline-specs, compatibility, declarative-config, governance]
notes:
  - "This README fills the blank pipelines/specs path as a compatibility/guardrail README only."
  - "Canonical declarative pipeline configuration belongs in pipeline_specs/, not pipelines/specs/."
  - "pipelines/ is executable pipeline logic — the how. pipeline_specs/ is declarative configuration — the what."
  - "Do not place authoritative specs here unless an accepted ADR or migration note changes the root contract."
  - "If files already appear here later, treat them as drift candidates until reviewed against Directory Rules and pipeline_specs/ authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipelines Specs Compatibility Guardrail

> Guardrail README for the `pipelines/specs/` compatibility path. Authoritative declarative pipeline specs belong in `pipeline_specs/`; executable pipeline logic belongs in `pipelines/`.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![canonical-spec-root](https://img.shields.io/badge/canonical%20spec%20root-pipeline__specs%2F-d62728)
![authority](https://img.shields.io/badge/authority-compatibility%20guardrail-455a64)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/specs/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Canonical declarative-spec root:** `pipeline_specs/`  
**Placement posture:** compatibility/guardrail only; authoritative specs here are `NEEDS VERIFICATION / ADR`  
**Public posture:** no direct publication; specs and pipelines are build-time/control-plane inputs, not public artifacts.

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

`pipelines/specs/` is a compatibility/guardrail path only.

Its purpose is to prevent a common drift pattern: putting declarative pipeline specifications inside the executable `pipelines/` root when the repo already has a canonical `pipeline_specs/` root.

Use this README to make the boundary explicit:

```text
pipelines/       = executable pipeline logic, adapters, runners, helpers, and receipts emitters
a
pipeline_specs/  = declarative pipeline configuration, schedules, profiles, source scopes, and run contracts
```

This path does not authorize a new spec home. It documents the boundary so future maintainers do not accidentally create a parallel authority surface.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why does this README exist? | To guard against specs being placed in the wrong root. | CONFIRMED need from requested path |
| Is `pipelines/specs/` canonical? | No. Canonical declarative configuration belongs in `pipeline_specs/`. | CONFIRMED by root READMEs |
| What belongs under `pipelines/`? | Executable pipeline logic: the **how**. | CONFIRMED root contract |
| What belongs under `pipeline_specs/`? | Declarative pipeline configuration: the **what**. | CONFIRMED root contract |
| Can this folder contain real specs? | Not by default. Real specs here require an ADR or migration note. | NEEDS VERIFICATION / ADR |
| Can public clients read this folder? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust posture |

> [!IMPORTANT]
> Do not create a parallel spec authority at `pipelines/specs/`. Move or create authoritative declarative specs under `pipeline_specs/` unless an accepted ADR explicitly changes the root contract.

[⬆ Back to top](#top)

---

## 3. Anti-collapse rules

Disallowed collapses:

```text
pipelines/specs/ -> pipeline_specs/
executable runner -> declarative spec
declarative spec -> executable implementation
profile YAML -> policy decision
pipeline schedule -> release approval
successful run -> publication
spec location convenience -> authority root
```

Required distinctions:

- executable pipeline code remains under `pipelines/`;
- declarative run profiles and pipeline specs remain under `pipeline_specs/`;
- tests remain under `tests/`;
- fixtures remain under `fixtures/`;
- receipts remain under `data/receipts/`;
- proof artifacts remain under `data/proofs/`;
- release decisions remain under `release/`;
- no spec or pipeline run can bypass lifecycle, evidence, policy, review, correction, or rollback gates.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents are limited to guardrail material:

- this `README.md`;
- migration notes that explain moving misplaced specs to `pipeline_specs/`;
- temporary compatibility pointers during a governed migration;
- deprecation notices that tell maintainers which canonical `pipeline_specs/` path to use.

A good placement test:

> If the file is an actual declarative pipeline spec, it should normally live in `pipeline_specs/`, not here.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Declarative pipeline specs | `pipeline_specs/` |
| Domain-specific pipeline specs | `pipeline_specs/<domain>/` or accepted spec home |
| Executable pipeline code | `pipelines/` sublanes outside `pipelines/specs/` |
| Shared pipeline code | `pipelines/<lane>/` or accepted package/tool home |
| Tests | `tests/` |
| Fixtures | `fixtures/` |
| Receipts | `data/receipts/` |
| EvidenceBundles / proof data | `data/proofs/evidence_bundle/` |
| Runtime config with secrets | never commit secrets; use approved config/runtime secret paths |
| Policy | `policy/` |
| Release decisions / manifests | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Migration posture

If a file is discovered under `pipelines/specs/`, classify it before moving:

| Finding | Default action | Status |
|---|---|---|
| Actual declarative spec | Move to `pipeline_specs/` through a reviewable migration. | PROPOSED |
| Executable code | Move to the proper `pipelines/<lane>/` implementation path. | PROPOSED |
| Test fixture | Move to `fixtures/`. | PROPOSED |
| Test code | Move to `tests/`. | PROPOSED |
| Receipt/proof output | Move to `data/receipts/` or `data/proofs/`. | PROPOSED |
| Release decision | Move to `release/`. | PROPOSED |
| Unclear file | Hold, document in drift register, and request steward review. | NEEDS VERIFICATION |

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
pipelines/specs/
└── README.md   # guardrail only
```

Canonical spec shape:

```text
pipeline_specs/
├── README.md
├── <domain>/
│   └── <pipeline>.yaml
├── proofs/
│   └── <proof_id>.yaml
├── ingest/
├── normalize/
├── validate/
├── watchers/
└── triplets/
```

This README should not be used as evidence that `pipelines/specs/` is an accepted alternative to `pipeline_specs/`.

[⬆ Back to top](#top)

---

## 8. Definition of done

This README is done when it:

- fills the blank `pipelines/specs/README.md` file;
- marks the path as a compatibility/guardrail path, not a canonical spec root;
- directs authoritative declarative specs to `pipeline_specs/`;
- preserves the `pipelines/` versus `pipeline_specs/` split;
- blocks parallel schema, contract, policy, source, lifecycle, proof, catalog, release, public API, or UI authority;
- gives maintainers a migration posture for misplaced files.

Future work in this path should be limited to guardrail or migration documentation unless an ADR changes the root contract.

[⬆ Back to top](#top)

---

## 9. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPECS-001` | Should `pipelines/specs/` remain as a guardrail README only, or should the directory be removed after migration cleanup? | NEEDS VERIFICATION / ADR |
| `PIPE-SPECS-002` | Should a lint rule block declarative specs under `pipelines/specs/`? | NEEDS VERIFICATION |
| `PIPE-SPECS-003` | Should this README be referenced from `pipeline_specs/README.md` as a compatibility warning? | NEEDS VERIFICATION |
| `PIPE-SPECS-004` | Should misplaced files be tracked in `docs/registers/DRIFT_REGISTER.md`? | NEEDS VERIFICATION |

---

## Maintainer note

Treat this directory as a warning sign. Do not add executable code, declarative specs, schemas, contracts, policies, source descriptors, lifecycle outputs, proof artifacts, receipts, release decisions, public API code, UI code, or generated summaries here unless a governed ADR or migration note says why.
