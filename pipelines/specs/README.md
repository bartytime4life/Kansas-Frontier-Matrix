<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-specs-readme
title: Pipelines Specs Compatibility README
type: readme
version: v0.2
status: draft; repository-grounded; compatibility-only; no-active-specs
owners:
  - <pipeline-owner>
  - <pipeline-spec-steward>
  - <docs-steward>
  - <governance-steward>
created: 2026-06-13
updated: 2026-07-22
supersedes: v0.1
policy_label: public
path: pipelines/specs/README.md
responsibility_root: pipelines/
path_posture: compatibility-guardrail; not-canonical; not-generated; not-mirrored; not-localized
truth_posture: CONFIRMED current path, README and .gitkeep inventory, pipelines executable root, pipeline_specs declarative root, and compatibility references / CONFLICTED Directory Rules document placement / UNKNOWN runtime consumers, branch-protection enforcement, and future removal decision / NEEDS VERIFICATION lint enforcement and owner assignment
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 459b41d7ec91240742d8b2d3e5d9eb4dbd248df7
  target_prior_blob: 1314bf0fe34736e75f1a2d0900b049ebea2d87bd
  bounded_path_inventory:
    - pipelines/specs/.gitkeep
    - pipelines/specs/README.md
  checked_absent_instructions:
    - AGENTS.md
    - pipelines/AGENTS.md
    - pipelines/specs/AGENTS.md
related:
  - ../../CONTRIBUTING.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/architecture/DIRECTORY_RULES.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../README.md
  - ../../pipeline_specs/README.md
  - ../../.github/workflows/README.md
  - ../../.github/CODEOWNERS
  - ../../data/receipts/generated/README.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, pipelines, specs, pipeline-specs, compatibility, declarative-config, governance]
notes:
  - "This README documents pipelines/specs/ as a compatibility guardrail only."
  - "Canonical declarative pipeline configuration belongs in pipeline_specs/, not pipelines/specs/."
  - "pipelines/ is executable pipeline logic — the how. pipeline_specs/ is declarative configuration — the what."
  - "No accepted ADR inspected at the evidence snapshot changes this root split."
  - "The repository contains conflicting Directory Rules copies; this README relies only on their shared pipelines/pipeline_specs responsibility rule and does not resolve their placement."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipelines Specs Compatibility Guardrail

> Guardrail for the `pipelines/specs/` compatibility path. Authoritative declarative pipeline specifications belong in [`pipeline_specs/`](../../pipeline_specs/README.md); executable pipeline logic belongs in [`pipelines/`](../README.md).

![status](https://img.shields.io/badge/status-repository--grounded%20draft-yellow)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![canonical-spec-root](https://img.shields.io/badge/canonical%20spec%20root-pipeline__specs%2F-d62728)
![authority](https://img.shields.io/badge/authority-compatibility%20guardrail-455a64)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

- **Status:** Draft
- **Version:** `v0.2`
- **Path:** `pipelines/specs/README.md`
- **Responsibility root:** `pipelines/` — executable pipeline logic
- **Canonical declarative-spec root:** [`pipeline_specs/`](../../pipeline_specs/README.md)
- **Placement posture:** compatibility guardrail only; authoritative specs here are `PROPOSED / CONFLICTED` until an accepted ADR and migration plan change the responsibility split
- **Evidence snapshot:** `main@459b41d7ec91240742d8b2d3e5d9eb4dbd248df7`
- **Public posture:** no direct publication; specs and pipelines are build-time or control-plane inputs, not public truth surfaces.

> [!IMPORTANT]
> Do not create a parallel spec authority at `pipelines/specs/`. Create or move authoritative declarative specs under `pipeline_specs/` unless an accepted ADR changes the root contract and supplies migration and rollback.

> [!NOTE]
> Directory Rules placement is `CONFLICTED`: the repository contains `docs/architecture/directory-rules.md`, `docs/architecture/DIRECTORY_RULES.md`, and `docs/doctrine/directory-rules.md`. The first two share one `doc_id`, while the doctrine copy uses another. Their shared responsibility rule is consistent—`pipelines/` owns executable logic and `pipeline_specs/` owns declarative configuration—but this README does not select a canonical Directory Rules file.

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
- [9. Verification register](#9-verification-register)
- [10. Evidence ledger](#10-evidence-ledger)
- [Change history](#change-history)

---

## 1. Purpose

`pipelines/specs/` is a compatibility guardrail, not a specification authority.

Its purpose is to prevent a common drift pattern: placing declarative pipeline specifications inside the executable `pipelines/` root when the repository already has the canonical `pipeline_specs/` responsibility root.

Use this boundary:

```text
pipelines/       = executable pipeline logic, adapters, runners, helpers, and receipt emitters
pipeline_specs/  = declarative pipeline configuration, profiles, source scopes, and run contracts
```

This path does not authorize a second spec home, activate a specification, identify a parser or consumer, admit a source, approve a lifecycle transition, or publish an artifact.

[Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Evidence state |
|---|---|---:|
| Why does this README exist? | To keep declarative specs out of the executable root and point maintainers to the accepted responsibility root. | `CONFIRMED` at the evidence snapshot |
| Is `pipelines/specs/` canonical? | No. It is a compatibility guardrail. | `CONFIRMED` by the target, parent README, and canonical companion README |
| What belongs under `pipelines/`? | Executable pipeline logic: the **how**. | `CONFIRMED` repository contract |
| What belongs under `pipeline_specs/`? | Declarative pipeline configuration: the **what**. | `CONFIRMED` repository contract |
| What is currently in this directory? | `.gitkeep` and this `README.md`; no specification payload is present. | `CONFIRMED` bounded tree at the evidence snapshot |
| Can this folder contain authoritative specs? | Not under the current responsibility split. Doing so would create a conflicting authority surface. | `CONFIRMED` boundary; any exception is `PROPOSED / CONFLICTED` pending accepted ADR and migration |
| Is this output generated, mirrored, or localized? | No generator, mirror, or localization relationship was found for this target. | `CONFIRMED` bounded inspection; full-history behavior remains `UNKNOWN` |
| Can public clients read this folder as truth? | No. Public clients use governed interfaces and released public-safe artifacts. | `CONFIRMED` doctrine; runtime enforcement outside the inspected evidence remains `UNKNOWN` |

No accepted ADR inspected at the pinned base changes the `pipelines/` versus `pipeline_specs/` split. Relevant ADRs about identity, receipts, promotion, review, and public-client boundaries remain proposed or draft and do not authorize this directory as a spec home.

[Back to top](#top)

---

## 3. Anti-collapse rules

Disallowed collapses:

```text
pipelines/specs/ ≠ pipeline_specs/
executable runner ≠ declarative spec
declarative spec ≠ executable implementation
profile YAML ≠ policy decision
pipeline schedule ≠ release approval
successful run ≠ publication
convenient path ≠ authority root
```

Required distinctions:

- executable pipeline code remains under `pipelines/`;
- declarative run profiles and pipeline specs remain under `pipeline_specs/`;
- tests remain under `tests/`;
- fixtures remain under `fixtures/`;
- receipts remain under `data/receipts/`;
- proofs remain under `data/proofs/`;
- release decisions remain under `release/`;
- no spec or pipeline run bypasses lifecycle, evidence, policy, review, correction, or rollback gates;
- a merge, workflow result, synchronized mirror, or generated document is not KFM publication.

[Back to top](#top)

---

## 4. What belongs here

Contents are limited to non-authoritative compatibility material:

- this `README.md`;
- the existing `.gitkeep`, until maintainers remove it through a separate reviewed cleanup;
- a bounded migration note that identifies the old path, the canonical `pipeline_specs/` destination, affected consumers, and rollback;
- a temporary compatibility pointer during a governed migration;
- a deprecation notice that directs maintainers to an exact canonical `pipeline_specs/` path.

A compatibility note must not define new fields, IDs, schedules, source bindings, activation rules, consumer behavior, policy decisions, or release semantics.

> If a file is an actual declarative pipeline specification, it belongs under `pipeline_specs/`, not here.

[Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Declarative pipeline specs | `pipeline_specs/` |
| Domain-specific pipeline specs | `pipeline_specs/<domain>/` or another accepted lane under that root |
| Executable pipeline code | `pipelines/` outside this compatibility path |
| Shared implementation code | An accepted `pipelines/` lane or `packages/` home |
| Tests | `tests/` |
| Fixtures | `fixtures/` |
| Receipts | `data/receipts/` |
| EvidenceBundles or proof data | `data/proofs/` |
| Runtime private configuration or secrets | Approved private configuration or runtime systems; never repository prose |
| Policy | `policy/` |
| Release decisions, manifests, corrections, or rollback cards | `release/` |
| Public API or UI code | Governed application or package roots |

[Back to top](#top)

---

## 6. Migration posture

If a file appears under `pipelines/specs/`, classify it before changing or moving it:

| Finding | Default action | Evidence state |
|---|---|---:|
| Actual declarative spec | Freeze activation and prepare a reviewable move to `pipeline_specs/`. | `PROPOSED` until exact consumers and destination are verified |
| Executable code | Move to the owning `pipelines/` lane. | `PROPOSED` until ownership and imports are verified |
| Test fixture | Move to `fixtures/`. | `PROPOSED` |
| Test code | Move to `tests/`. | `PROPOSED` |
| Receipt or proof output | Move to the correct `data/receipts/` or `data/proofs/` family. | `PROPOSED` |
| Release decision | Move to `release/`. | `PROPOSED` |
| Unclear file | Hold it, record the conflict in the drift register, and request owner review. | `NEEDS VERIFICATION` |

Migration discipline:

1. pin the base commit and inventory exact files, IDs, consumers, schedules, references, and generated relationships;
2. preserve history and distinguish canonical source from compatibility pointer;
3. select the destination from Directory Rules and accepted ADR evidence;
4. update authorized references and synchronized outputs atomically;
5. validate parsing, consumers, tests, links, and rollback;
6. keep activation, release, and publication separate from the file move;
7. record unresolved authority conflicts in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)

---

## 7. Directory contract

The bounded current tree at `main@459b41d7ec91240742d8b2d3e5d9eb4dbd248df7` is:

```text
pipelines/specs/
├── .gitkeep    # non-authoritative placeholder
└── README.md   # compatibility guardrail
```

The authoritative spec inventory, maturity posture, and lane registry live in [`pipeline_specs/README.md`](../../pipeline_specs/README.md). Do not duplicate that inventory here; duplicated authority would drift.

This README is not evidence that `pipelines/specs/` is an accepted alternative to `pipeline_specs/`, and the presence of a file under either path does not prove activation or runtime use.

[Back to top](#top)

---

## 8. Definition of done

This compatibility README is complete when it:

- identifies `pipelines/specs/` as non-canonical and compatibility-only;
- directs authoritative declarative specs to `pipeline_specs/`;
- preserves the executable `pipelines/` versus declarative `pipeline_specs/` split;
- records the current bounded path inventory and evidence snapshot;
- keeps the conflicting Directory Rules placement visible without selecting an authority copy;
- blocks parallel schema, contract, policy, source, registry, receipt, proof, catalog, release, public API, or UI authority;
- gives maintainers a reversible migration posture for misplaced files;
- distinguishes documentation, validation, merge, activation, release, and publication.

For any future change in this path, reviewers must also verify the base tree, overlapping branches or pull requests, workflow triggers, links, sensitive-content posture, generated-work receipt requirement, and rollback plan.

[Back to top](#top)

---

## 9. Verification register

| ID | Item | Status |
|---|---|---:|
| `PIPE-SPECS-001` | Whether this compatibility directory should remain or be retired after repository cleanup. | `NEEDS VERIFICATION`; an authority-changing decision may require ADR review |
| `PIPE-SPECS-002` | Whether a repository-owned static check should reject declarative payloads under `pipelines/specs/`. | `NEEDS VERIFICATION` |
| `PIPE-SPECS-003` | Whether any parser, scheduler, consumer, or deployment reads this path. | `UNKNOWN`; path presence and README references do not prove runtime use |
| `PIPE-SPECS-004` | Directory Rules document authority and placement. | `CONFLICTED`; three live copies, including a duplicate `doc_id` pair |
| `PIPE-SPECS-005` | Drift-register coverage for this path. | `CONFIRMED` bounded no-result at the evidence snapshot; add an entry when concrete drift is observed |
| `PIPE-SPECS-006` | Branch protection and required-check status for triggered workflows. | `UNKNOWN` |

[Back to top](#top)

---

## 10. Evidence ledger

| Evidence at `main@459b41d7ec91240742d8b2d3e5d9eb4dbd248df7` | Supports | Does not prove |
|---|---|---|
| `pipelines/specs/` tree | Only `.gitkeep` and this README are present. | Full history, other branches, runtime consumers, or future intent. |
| [`pipelines/README.md`](../README.md) §§1–7 | `pipelines/` owns executable logic and identifies this path as a compatibility guardrail. | That every described lane is implemented or tested. |
| [`pipeline_specs/README.md`](../../pipeline_specs/README.md) authority and current-state sections | `pipeline_specs/` is the declarative responsibility root and this path is not alternate authority. | An accepted schema, active parser, scheduler, or active spec system. |
| [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) §4 and §7.4 plus [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) §4 and §7.4 | Shared responsibility rule for `pipelines/` and `pipeline_specs/`. | Which Directory Rules copy is canonical. |
| [`docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | No bounded entry currently names `pipelines/specs/`. | That drift does not exist outside the inspected file and commit. |
| [Workflow inventory](../../.github/workflows/README.md) and `policy-boundary-guards.yml` | A change under `pipelines/**` triggers a read-only boundary suite; broad PR workflows also run or hold. | Required-check status, branch protection, release approval, or publication. |
| [`.github/CODEOWNERS`](../../.github/CODEOWNERS) | Review routing for `pipelines/` resolves to `@bartytime4life`. | Semantic ownership, independent approval, or policy/release authority. |

### Evidence limits

Repository state was inspected at the pinned commit through authenticated GitHub reads and a complete Git tree. No repository scripts were executed during authoring. No runtime, deployment, source system, protected environment, branch ruleset, or public release was inspected. A green workflow proves only the steps it ran.

[Back to top](#top)

---

## Change history

### v0.2 — 2026-07-22

- pinned the repository, base commit, target blob, and current two-file directory inventory;
- preserved the compatibility-only boundary while replacing unsupported or stale evidence labels;
- surfaced the conflicting Directory Rules copies without selecting one as canonical;
- clarified generated, mirror, localization, activation, migration, validation, and publication boundaries;
- delegated the authoritative lane inventory to `pipeline_specs/README.md` to avoid drift;
- added a verification register and evidence ledger;
- changed documentation only.

### v0.1 — 2026-06-13

- established the compatibility guardrail and the `pipelines/` versus `pipeline_specs/` responsibility split.

---

## Maintainer note

Treat this directory as a warning boundary. Do not add executable code, declarative specs, schemas, contracts, policies, source descriptors, lifecycle outputs, proof artifacts, receipts, release decisions, public API code, UI code, or generated summaries here unless a reviewed migration or accepted ADR explains the exception and preserves rollback.

[Back to top](#top)
