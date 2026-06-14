<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-readme
title: Pipelines Root README
type: readme
version: v0.2
status: draft
owners:
  - <pipeline-owner>
  - <domain-stewards>
  - <source-steward>
  - <evidence-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/release-discipline.md
  - pipeline_specs/README.md
  - pipelines/ingest/README.md
  - pipelines/normalize/README.md
  - pipelines/validate/README.md
  - pipelines/catalog/README.md
  - pipelines/triplets/README.md
  - pipelines/publish/README.md
  - pipelines/rollback/README.md
  - pipelines/watchers/README.md
  - pipelines/domains/README.md
  - pipelines/proofs/README.md
  - tests/
  - fixtures/
  - data/receipts/pipeline/
tags: [kfm, pipelines, executable-logic, lifecycle, receipts, governance]
notes:
  - "This README upgrades the previous pipelines root stub into a governed root contract."
  - "pipelines/ is executable pipeline logic — the how. pipeline_specs/ is declarative configuration — the what."
  - "Pipeline code remains subordinate to lifecycle, evidence, policy, review, release, correction, and rollback controls."
  - "Executable behavior and CI coverage remain NEEDS VERIFICATION unless proven by tests and current repo evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipelines

> Canonical implementation root for executable KFM pipeline logic: ingest, normalize, validate, catalog, triplet, publish-readiness, rollback-readiness, watcher, proof, and domain pipeline support.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![specs](https://img.shields.io/badge/specs-pipeline__specs%2F-d62728)
![release](https://img.shields.io/badge/release-governed-d62728)

**Status:** Draft  
**Path:** `pipelines/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic, the **how**  
**Companion root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Truth posture:** lane implementation claims are `NEEDS VERIFICATION` until backed by files, tests, fixtures, receipts, or runtime evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Root authority](#2-root-authority)
- [3. Lifecycle contract](#3-lifecycle-contract)
- [4. Anti-collapse rules](#4-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Lane map](#7-lane-map)
- [8. Inputs and outputs](#8-inputs-and-outputs)
- [9. Required gates](#9-required-gates)
- [10. Expansion rules](#10-expansion-rules)
- [11. Definition of done](#11-definition-of-done)
- [12. Open questions](#12-open-questions)

---

## 1. Purpose

`pipelines/` owns executable pipeline logic for KFM.

It may contain code and README contracts for:

- ingest and source-intake helpers;
- normalization helpers;
- validation helpers;
- catalog-closure support;
- graph/triplet projection helpers;
- publish-readiness checks;
- rollback-readiness checks;
- watcher/source-change support;
- domain-specific processing lanes;
- proof harnesses;
- receipt emitters and blocker builders.

Short rule:

```text
pipelines/       = executable pipeline logic, the HOW
pipeline_specs/  = declarative pipeline configuration, the WHAT
data/            = lifecycle state and artifacts
release/         = release decisions and release control
```

[⬆ Back to top](#top)

---

## 2. Root authority

| Question | Answer | Status |
|---|---|---|
| What does `pipelines/` own? | Executable pipeline logic and implementation-lane README contracts. | CONFIRMED root contract |
| What does `pipeline_specs/` own? | Declarative configuration, schedules, profiles, scopes, and run contracts. | CONFIRMED companion-root contract |
| Does `pipelines/` own lifecycle data? | No. Lifecycle outputs belong under `data/`. | CONFIRMED lifecycle posture |
| Does `pipelines/` own release decisions? | No. Release decisions and manifests belong under `release/`. | CONFIRMED authority separation |
| Does `pipelines/` own schemas/contracts/policy? | No. Those live under their responsibility roots. | CONFIRMED authority separation |

> [!IMPORTANT]
> A successful pipeline run is not publication. A run can produce candidates, reports, receipts, blockers, and handoffs; PUBLISHED state requires governed release gates.

[⬆ Back to top](#top)

---

## 3. Lifecycle contract

All pipeline lanes preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Pipeline code may help move material toward the next governed state, but promotion is closed only when required artifacts exist, required references resolve, and review/policy gates are recorded.

| Phase | Pipeline responsibility | Non-responsibility |
|---|---|---|
| Admission | Prepare or check intake and RAW/QUARANTINE handoffs. | Does not define source authority. |
| Normalization | Transform candidate shapes and emit receipts. | Does not validate as public truth. |
| Validation | Emit finite ValidationReports and blockers. | Does not create EvidenceBundles or publish. |
| Catalog/triplet | Prepare catalog or graph projection handoffs. | Does not create public truth by itself. |
| Publish | Check release readiness and hand off to release authority. | Does not approve release. |
| Rollback/correction | Check readiness, invalidation, and prior-release refs. | Does not silently edit history. |

[⬆ Back to top](#top)

---

## 4. Anti-collapse rules

Disallowed collapses:

```text
pipeline run -> public truth
runner config -> policy decision
pipeline_specs entry -> executable implementation
ValidationReport -> EvidenceBundle
catalog/triplet projection -> public release
publish-readiness pass -> release approval
rollback-readiness pass -> rollback approval
generated summary -> evidence
```

Required separations:

- code stays in `pipelines/`;
- specs stay in `pipeline_specs/`;
- schemas stay in `schemas/`;
- contracts stay in `contracts/`;
- policy stays in `policy/`;
- tests stay in `tests/`;
- fixtures stay in `fixtures/`;
- lifecycle data stays in `data/`;
- release decisions stay in `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include:

- executable pipeline runners;
- shared lane helpers;
- domain pipeline adapters;
- dry-run harnesses;
- receipt emitters;
- blocker builders;
- validation/candidate/report emitters;
- graph/triplet projection helpers;
- publish/rollback readiness helpers;
- lane README files that explain executable responsibility.

A good placement test:

> If the file answers “how does this governed pipeline step execute?” it may belong here. If it answers “what should run?”, “what does an object mean?”, “what is the schema?”, “what is allowed?”, “what was released?”, or “what does the public client read?”, it belongs in another root.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Declarative pipeline specs | `pipeline_specs/` |
| Object meaning | `contracts/` |
| Machine shapes | `schemas/` |
| Policy/admissibility rules | `policy/` |
| Source descriptors | `data/registry/sources/` or accepted registry home |
| Lifecycle records | `data/` lifecycle homes |
| EvidenceBundles and proof data | `data/proofs/evidence_bundle/` or accepted proof homes |
| Release decisions, manifests, rollback cards, correction notices | `release/` |
| Public API or UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Tests | `tests/` |
| Fixtures | `fixtures/` |
| Infrastructure config | `infra/`, `configs/`, `runtime/` as applicable |

[⬆ Back to top](#top)

---

## 7. Lane map

| Lane | Responsibility | Status |
|---|---|---|
| `pipelines/ingest/` | Shared intake/admission support. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/normalize/` | Shared normalization support. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/validate/` | Shared validation helpers. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/catalog/` | Shared catalog-closure support. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/triplets/` | Shared graph/triplet projection support. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/publish/` | Shared publish-readiness support. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/rollback/` | Shared rollback-readiness support. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/watchers/` | Shared source-change watcher support. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/domains/` | Domain-owned executable lanes. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/proofs/` | Proof harness support. | PROPOSED / NEEDS VERIFICATION |
| `pipelines/specs/` | Compatibility guardrail only; canonical specs remain in `pipeline_specs/`. | PROPOSED / NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | In / out | Correct home | Notes |
|---|---|---|---|
| Declarative spec | Input | `pipeline_specs/` | The what. |
| Fixture | Input | `fixtures/` | Public-safe by default. |
| Source descriptor | Input | `data/registry/sources/` | Read by stable ref. |
| Lifecycle candidate | Input/output | `data/` lifecycle homes | Written only through governed transitions. |
| Receipt | Output | `data/receipts/pipeline/` | Records inputs, checks, outputs, hashes, and blockers. |
| EvidenceBundle | Input/ref | `data/proofs/evidence_bundle/` | Referenced or required; not fabricated by generic helpers. |
| Release control | Handoff | `release/` | Release authority owns final decisions. |

[⬆ Back to top](#top)

---

## 9. Required gates

Every pipeline lane must identify and enforce relevant gates:

1. **Scope gate** — caller, domain, source, profile, and lifecycle phase are explicit.
2. **Spec gate** — declarative profile comes from `pipeline_specs/` or accepted spec home.
3. **Lifecycle gate** — input and output states follow the lifecycle invariant.
4. **Evidence gate** — claims that need evidence have resolvable EvidenceBundle support or abstain.
5. **Source gate** — source ids and source roles resolve to governed descriptors where required.
6. **Policy/review gate** — rights, sensitivity, review, and policy state are explicit where material.
7. **Receipt gate** — inputs, outputs, hashes, reason codes, and blocker states are recorded.
8. **Release gate** — publish and rollback helpers hand off to release authority rather than approving release directly.

[⬆ Back to top](#top)

---

## 10. Expansion rules

Before adding a new lane or file under `pipelines/`:

1. identify the owning lifecycle phase or domain lane;
2. verify that the file is executable logic, not spec/schema/contract/policy/data/release/UI material;
3. add or update a lane README;
4. add a spec under `pipeline_specs/` if declarative configuration is needed;
5. add fixtures and tests if behavior is material;
6. emit receipts for trust-bearing transformations;
7. document rollback or correction implications if output can reach release.

Domain-specific behavior usually belongs under `pipelines/domains/<domain>/` rather than as a new root-level topic folder.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- upgrades the previous `pipelines/README.md` stub into a governed root contract;
- states that `pipelines/` owns executable logic and `pipeline_specs/` owns declarative configuration;
- preserves lifecycle, evidence, policy, review, publication, correction, and rollback boundaries;
- blocks pipeline-run-as-public-truth, generated-summary-as-evidence, publish-readiness-as-release-approval, and rollback-readiness-as-approval;
- gives maintainers placement rules for lanes, code, specs, data, tests, fixtures, receipts, proofs, releases, APIs, and UI.

Future executable lanes are done only when their README, spec refs, tests, fixtures, receipts, source/evidence/policy/review posture, and rollback/correction implications are documented and verifiable.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-ROOT-001` | Which pipeline lanes are implemented versus README-only scaffolds? | NEEDS VERIFICATION |
| `PIPE-ROOT-002` | Which CI workflow owns root pipeline invariant checks? | UNKNOWN |
| `PIPE-ROOT-003` | Should `pipelines/specs/` remain as a guardrail directory or be removed after cleanup? | NEEDS VERIFICATION / ADR |
| `PIPE-ROOT-004` | Which receipt schema is canonical for shared pipeline lanes? | NEEDS VERIFICATION |
| `PIPE-ROOT-005` | Which lanes should move into shared packages once implementation matures? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep `pipelines/` boring and inspectable. Pipeline code should be reversible, testable, receipt-emitting, and subordinate to source descriptors, contracts, schemas, policy, evidence, review, release, correction, and rollback controls.
