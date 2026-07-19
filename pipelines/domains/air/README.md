<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-air-readme
title: pipelines/domains/air/ — Air Pipeline Compatibility and Migration Guardrail
type: readme; directory-readme; pipeline-compatibility-lane; slug-conflict-guardrail; migration-boundary; non-publisher-guardrail
version: v0.2
status: draft; repository-grounded; direct-lane-readme-only; compatibility-only; preferred-atmosphere-lane-confirmed; no-air-executable-established; atmosphere-execution-unestablished; slug-adr-open
owners:
  - OWNER_TBD — Atmosphere and Air domain steward
  - OWNER_TBD — Pipeline steward
  - OWNER_TBD — Directory Rules and migration steward
  - OWNER_TBD — Pipeline-spec steward
  - OWNER_TBD — Source and rights steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Measurement, unit, time, and freshness steward
  - OWNER_TBD — Evidence and receipt steward
  - OWNER_TBD — Policy and sensitivity steward
  - OWNER_TBD — Validation and CI steward
  - OWNER_TBD — Hazards and official-authority liaison
  - OWNER_TBD — Release steward
  - OWNER_TBD — Security reviewer
  - OWNER_TBD — Docs steward
created: 2026-06-13
updated: 2026-07-19
supersedes: v0.1
policy_label: public-doc; pipelines; domains; air; atmosphere; compatibility-only; slug-drift; migration; no-secrets; no-live-source-access; no-source-activation; no-direct-raw-admission; no-parallel-executable-authority; no-direct-publication; not-medical-guidance; not-regulatory-authority; not-emergency-alerting; not-life-safety-authority; source-role-preserving; knowledge-character-preserving; time-aware; freshness-aware; caveat-aware; evidence-bound; rights-aware; review-gated; correction-aware; rollback-aware
current_path: pipelines/domains/air/README.md
owning_root: pipelines/
responsibility: preserve the existing air-segment pipeline path as a documentation-only compatibility, migration, duplicate-authority, and rollback guardrail; redirect new Atmosphere pipeline implementation toward the preferred pipelines/domains/atmosphere lane pending an accepted slug decision; and prevent this path from activating sources, duplicating executable stages, changing domain meaning, defining machine shape, deciding policy, creating proof, approving release, or serving public outputs
truth_posture: CONFIRMED target README and prior blob; pipelines responsibility root and domain-pipeline parent; direct Air lane surfaced as README-only through bounded search and exact checks; checked absence of local pipeline contract, fixture runner, Air normalizer, package initializer, and dedicated pipeline-test README; Atmosphere canonical-path guide directs new work to atmosphere and classifies air as an ADR-class drift candidate; pipeline_specs/air and policy/domains/air are repository-grounded compatibility guardrails; pipeline_specs/atmosphere is README-only with no active consumer-bound specification; pipelines/domains/atmosphere and normalize/validate child lanes are documentation-backed and explicitly leave executable behavior unverified; Atmosphere helper package is version 0.0.0 with empty __init__.py; Atmosphere contracts are partial; the known Atmosphere decision-envelope schema is a permissive PROPOSED scaffold; policy/domains/atmosphere is a 33-line greenfield scaffold; Atmosphere tests are scaffolded; domain-atmosphere is a read-only readiness-hold workflow that performs no validation, proof, release, deployment, or publication; no overlapping open PR or matching task branch was found / PROPOSED retain this Air path as compatibility documentation only, redirect new code to Atmosphere, define one canonical implementation and consumer-bound spec, add deterministic migration checks, and retire the Air path only after reference inventory, correction, rollback, and steward review / CONFLICTED air versus atmosphere segments coexist across pipelines, specs, policy, contracts, schemas, and tests; current doctrine prefers atmosphere but no accepted slug ADR was verified; preferred Atmosphere lanes remain scaffolded rather than executable / UNKNOWN exhaustive recursive inventory, historical consumers, imports, generated references, external links, active source bindings, parser or scheduler behavior, executable Atmosphere modules under differently named paths, fixture payloads, executable tests, validator implementations, emitted receipts and proofs, runtime use, monitoring, branch-protection significance, release integration, deployment, and public consumers / NEEDS VERIFICATION named owners and CODEOWNERS, accepted slug ADR, compatibility lifetime, reference migration manifest, active source descriptors and rights, accepted object contracts and schemas, policy bundle and evaluator, source-role and knowledge-character vocabularies, station identity, units and methods, time and freshness profiles, caveat rules, official-authority redirects, correction consumers, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 2783739bba744f560772388a9969ed3107d08930
  target_prior_blob: 75bcd81d996c93595492e61860a34b3c8f6dfe51
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  atmosphere_canonical_paths_blob: 97296d516792ad3bc2bc1f18d03e2518e367d28a
  atmosphere_pipeline_blob: 87de68dfa7b65ad83b4da7a17d16276728b3d4f0
  atmosphere_normalize_blob: 535f6b447596383987a9efa1e9316a3c5acb99b1
  atmosphere_validate_blob: 412540835acf15b5719df5ff6a6c9bc316adaa9f
  air_spec_guardrail_blob: 16a5096d5edcad9bbba51c87ef5f5d5521c2a0d6
  atmosphere_spec_blob: e049335b00967ca723c9df4a770b85e307ae840c
  atmosphere_package_readme_blob: 8a9ed10923fe73ac9157242b67b5b4270e9c807e
  atmosphere_package_init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  atmosphere_package_pyproject_blob: 504e4c6b71f059b72877fd19eee7f358893c644f
  atmosphere_contract_blob: 2626d011b5d80e6d58870be3eff817d95116ffc7
  atmosphere_schema_blob: 1165bd4719fff2c17ce4e7f5253fa8af8315f333
  air_policy_guardrail_blob: d722464dcce4effeb5f70861bbfb629b8d3aed9d
  atmosphere_policy_scaffold_blob: d897f4f67458f9d12e0ef2b2e7146eeba935df4b
  atmosphere_tests_blob: 6474cc33c3bdd668fd8713e06e94f7dacda97b6b
  atmosphere_workflow_blob: 9d38e1b292d4907e9d910b7a96f1bef9a00f6c84
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  direct_lane_files_confirmed:
    - pipelines/domains/air/README.md
  checked_absent_paths:
    - pipelines/domains/air/PIPELINE_CONTRACT.md
    - pipelines/domains/air/run_dry_fixture.py
    - pipelines/domains/air/normalize_air_observation.py
    - pipelines/domains/air/__init__.py
    - tests/pipelines/domains/air/README.md
  concurrency_check: no open pull request matching pipelines/domains/air/README.md and no branch matching air-pipeline were surfaced
  inventory_method: GitHub connector exact file reads plus bounded repository code-index queries; absence and README-only conclusions are limited to checked paths, indexed results, and the pinned branch snapshot
related:
  - ../../README.md
  - ../README.md
  - ../atmosphere/README.md
  - ../atmosphere/normalize/README.md
  - ../atmosphere/validate/README.md
  - ../../../docs/architecture/directory-rules.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/PIPELINE.md
  - ../../../pipeline_specs/air/README.md
  - ../../../pipeline_specs/atmosphere/README.md
  - ../../../packages/domains/atmosphere/src/atmosphere/README.md
  - ../../../contracts/domains/atmosphere/README.md
  - ../../../schemas/contracts/v1/domains/atmosphere/README.md
  - ../../../policy/domains/air/README.md
  - ../../../policy/domains/atmosphere/README.md
  - ../../../tests/domains/atmosphere/README.md
  - ../../../.github/workflows/domain-atmosphere.yml
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../data/receipts/generated/README.md
  - ../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags:
  - kfm
  - pipelines
  - domains
  - air
  - atmosphere
  - compatibility
  - migration
  - slug-drift
  - air-quality
  - weather
  - climate
  - smoke
  - aerosol
  - model
  - forecast
  - advisory-context
  - source-role
  - knowledge-character
  - units
  - time
  - freshness
  - caveats
  - evidence
  - policy
  - correction
  - rollback
notes:
  - "v0.2 replaces a speculative second executable lane with a commit-pinned compatibility, migration, and duplicate-authority guardrail."
  - "The direct Air lane is README-only in bounded inspection. No local runner, normalizer, execution contract, initializer, dedicated pipeline tests, active specification, source activation, or production execution is established."
  - "Current repository doctrine and adjacent compatibility READMEs prefer atmosphere for new work, but the slug decision remains ADR-class and the preferred Atmosphere implementation is itself not established."
  - "This documentation-only revision changes no executable code, source activation, spec, package API, contract, schema, policy rule, fixture, test, workflow, lifecycle record, receipt instance, proof, release object, runtime behavior, route, deployment, advisory, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `pipelines/domains/air/` — Air Pipeline Compatibility and Migration Guardrail

> **One-line purpose.** Preserve the existing `air/` pipeline segment as a reviewable compatibility and migration boundary while directing new Atmosphere implementation work toward [`pipelines/domains/atmosphere/`](../atmosphere/README.md), preventing duplicate executable authority, and keeping official guidance, evidence, policy, release, and publication outside this lane.

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-yellow">
  <img alt="Role: compatibility only" src="https://img.shields.io/badge/role-compatibility__only-orange">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Preferred lane: atmosphere" src="https://img.shields.io/badge/preferred-pipelines%2Fdomains%2Fatmosphere%2F-success">
  <img alt="Slug decision: ADR open" src="https://img.shields.io/badge/slug__ADR-open-critical">
  <img alt="Publication: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Path:** `pipelines/domains/air/README.md`
**Version:** `v0.2`
**Owning root:** [`pipelines/`](../../README.md) — executable pipeline logic, the **how**
**Parent lane:** [`pipelines/domains/`](../README.md) — domain-owned executable routing
**Preferred implementation lane:** [`pipelines/domains/atmosphere/`](../atmosphere/README.md) — documentation-aligned, implementation still unestablished
**Air specification lane:** [`pipeline_specs/air/`](../../../pipeline_specs/air/README.md) — compatibility guardrail
**Preferred specification lane:** [`pipeline_specs/atmosphere/`](../../../pipeline_specs/atmosphere/README.md) — README-only; no active specification established
**Public posture:** no source admission, observation authority, medical advice, regulatory determination, warning issuance, emergency alerting, lifecycle promotion, release, deployment, or publication
**Evidence snapshot:** `main@2783739bba744f560772388a9969ed3107d08930`

> [!IMPORTANT]
> **This Air pipeline directory is documentation-only at the pinned snapshot.** Exact checks found no local execution contract, fixture runner, Air observation normalizer, package initializer, or dedicated pipeline-test README. New executable stages, consumers, specs, schedules, source bindings, or output writers must not be added here by default.

> [!CAUTION]
> **The preferred Atmosphere lane is not implementation proof.** It has a parent README and README-backed normalize, validate, catalog, and publish sublanes, but current repository evidence and the `domain-atmosphere` readiness workflow do not establish an accepted executable validation command, proof producer, release dry run, active source binding, or production runtime.

> [!WARNING]
> **KFM is not an air-quality, medical, regulatory, emergency-alerting, or life-safety issuing authority.** AQI is not pollutant concentration, AOD or smoke context is not surface PM2.5 observation, a model or forecast is not an observation, and advisory context is not an official warning or protective instruction.

**Quick navigation:** [Status](#0-status-and-evidence-boundary) · [Purpose](#1-purpose) · [Authority](#2-placement-and-authority) · [Slug contract](#3-slug-conflict-and-compatibility-contract) · [Maturity](#4-current-repository-maturity) · [Anti-collapse](#5-anti-collapse-rules) · [Allowed content](#6-allowed-and-denied-content) · [Preferred lane](#7-preferred-atmosphere-implementation-boundary) · [Knowledge](#8-source-measurement-and-knowledge-character-boundaries) · [Lifecycle](#9-lifecycle-and-finite-outcomes) · [Time](#10-time-freshness-method-and-spatial-support) · [Outputs](#11-output-and-side-effect-boundary) · [Policy](#12-rights-sensitivity-policy-and-security) · [Split](#13-specification-package-and-executable-split) · [Testing](#14-validators-fixtures-tests-and-ci) · [Evidence](#15-receipts-proofs-and-evidence-closure) · [Release](#16-promotion-release-correction-and-rollback) · [Directory](#17-directory-contract-and-file-admission) · [Migration](#18-adr-migration-and-deprecation) · [Sequence](#19-smallest-sound-resolution-sequence) · [Done](#20-definition-of-done) · [Open](#21-open-verification-register) · [Ledger](#22-evidence-ledger) · [History](#23-change-history)

---

## 0. Status and evidence boundary

### Current determination

`pipelines/domains/air/` is an existing path inside the executable `pipelines/` root, but the inspected repository establishes it only as a **README-backed compatibility candidate**. It is not an accepted Air pipeline implementation and must not compete with the Atmosphere lane.

| Surface | Inspected state | Evidence-bounded conclusion |
|---|---:|---|
| Target README | `CONFIRMED` | v0.1 existed; this revision updates it in place. |
| Direct Air lane inventory | `README ONLY` | Bounded search and exact probes surfaced no Air executable. |
| Air execution contract | `NOT FOUND AT CHECKED PATH` | No local executable contract is established. |
| Air fixture runner | `NOT FOUND AT CHECKED PATH` | No no-network Air runner is established. |
| Air observation normalizer | `NOT FOUND AT CHECKED PATH` | No direct Air transform is established. |
| Air package initializer | `NOT FOUND AT CHECKED PATH` | This path is not a Python package boundary. |
| Dedicated Air pipeline tests | `NOT FOUND AT CHECKED PATH` | No `tests/pipelines/domains/air/README.md` is established. |
| Air pipeline-spec lane | `COMPATIBILITY GUARDRAIL` | No active Air specification was established. |
| Air policy lane | `COMPATIBILITY GUARDRAIL` | No active Air policy package was established. |
| Atmosphere canonical-path guidance | `PREFERS ATMOSPHERE` | New work should use `atmosphere/`; `air/` is an ADR-class drift candidate. |
| Atmosphere executable parent | `README-BACKED` | Documentation alignment exists; executable behavior remains unverified. |
| Atmosphere stage sublanes | `README-BACKED` | Normalize and validate contracts exist; their own text marks execution unverified. |
| Atmosphere specification | `README ONLY` | No active, parser-bound, consumer-bound, or scheduled spec was established. |
| Atmosphere helper package | `0.0.0 / EMPTY INIT` | Reusable implementation is not established. |
| Atmosphere contracts | `PARTIAL / DRAFT` | Object meanings are documented; enforcement and full schema pairing remain incomplete. |
| Atmosphere schemas | `PARTIAL SCAFFOLD` | Known decision-envelope schema is permissive and `PROPOSED`. |
| Atmosphere policy | `GREENFIELD SCAFFOLD` | Preferred path exists but does not establish an evaluator or accepted rules. |
| Atmosphere tests | `SCAFFOLD` | Parent and child documentation exist; executable coverage remains unverified. |
| Domain workflow | `EXPLICIT READINESS HOLD` | It checks maturity and refuses to claim validation, proof, or release execution. |
| Production/runtime use | `UNKNOWN` | No runtime trace, release manifest, deployment, or public consumer was inspected. |

### Safe conclusions

- **CONFIRMED:** the current Air path and README exist.
- **CONFIRMED:** the direct Air lane is README-only within the bounded inspection.
- **CONFIRMED:** current Atmosphere placement guidance and adjacent compatibility documents prefer `atmosphere/` for new work.
- **CONFIRMED:** no accepted Air runner, spec, policy package, test lane, or source activation is established by the checked paths.
- **PROPOSED:** retain this path as compatibility documentation until an accepted ADR and migration plan resolve it.
- **CONFLICTED:** both `air` and `atmosphere` segments exist across several responsibility roots.
- **UNKNOWN:** exhaustive repository references, runtime consumers, deployment aliases, and external links.
- **NEEDS VERIFICATION:** every owner, compatibility lifetime, migration step, executable interface, source binding, policy binding, test command, receipt, proof, release, and public consumer.

### Truth and outcome vocabulary

| Term | Use in this README |
|---|---|
| `CONFIRMED` | Verified from the pinned repository snapshot or this change's remote readback. |
| `PROPOSED` | A safe design, migration, or implementation direction not accepted as current behavior. |
| `CONFLICTED` | Repository paths or documents disagree and no accepted decision resolves them. |
| `UNKNOWN` | The bounded inspection did not establish the fact. |
| `NEEDS VERIFICATION` | Checkable, but not checked strongly enough to act as fact. |
| Operational result | A future machine result emitted by accepted code; never inferred from this prose. |

[Back to top](#top)

---

## 1. Purpose

This directory exists because the repository contains an `air` pipeline segment while current Atmosphere placement guidance directs new implementation work toward `atmosphere`.

Its durable question is:

> Can KFM preserve historical or proposed `air` references without allowing them to create a second executable pipeline, source activation path, specification registry, lifecycle writer, proof producer, release path, public route, or official-guidance surface?

The answer must remain inspectable and reversible.

This path should currently:

1. identify the unresolved slug conflict;
2. redirect new executable work to the preferred Atmosphere lane;
3. prevent duplicate runners, stage directories, specs, schedules, source bindings, receipts, or release semantics;
4. record migration and deprecation requirements;
5. preserve the v0.1 Air/Atmosphere safety and knowledge-boundary requirements;
6. provide a safe review checklist for references that still point here;
7. remain documentation-only unless an accepted decision explicitly assigns another role.

This path must not become a convenient place to implement a subset of Atmosphere processing while the preferred lane develops separately.

[Back to top](#top)

---

## 2. Placement and authority

### Directory Rules basis

Directory Rules place files by responsibility. Pipeline execution belongs under `pipelines/`; domain-specific execution uses a domain segment. Directory Rules also require drift to remain visible and reversible rather than silently hardening repository convention into authority.

| Question | Current answer | Status |
|---|---|---:|
| Why does this path remain under `pipelines/`? | Its historical or proposed responsibility concerns pipeline execution compatibility. | `CONFIRMED root fit` |
| Is `air` the accepted domain segment? | No accepted slug ADR was verified. | `CONFLICTED` |
| Which segment does current placement guidance prefer? | `atmosphere` for new work. | `CONFIRMED documentation posture` |
| Can this README declare the slug resolved? | No. | `DENIED` |
| Can this path own a second executable implementation? | No, absent an accepted ADR and migration contract. | `DENIED BY DEFAULT` |
| Where does new Atmosphere pipeline code belong today? | In the reviewed Atmosphere implementation lane, after contract and test admission. | `PROPOSED / preferred` |
| Can either lane publish directly? | No. | `CONFIRMED invariant` |

### Authority map

| Concern | Owning home | Air compatibility role |
|---|---|---|
| Atmosphere doctrine and domain scope | `docs/domains/atmosphere/` | Link only. |
| Canonical path decision | Accepted ADR plus Directory Rules and lane register | Hold and report conflict. |
| Executable Atmosphere pipeline | `pipelines/domains/atmosphere/` after implementation acceptance | Redirect new work; do not duplicate. |
| Declarative run intent | `pipeline_specs/atmosphere/` after spec acceptance | `pipeline_specs/air/` remains a compatibility guardrail. |
| Reusable helpers | `packages/domains/atmosphere/` | No Air package implied. |
| Object meaning | `contracts/domains/atmosphere/` | No semantic authority. |
| Machine shape | `schemas/contracts/v1/domains/atmosphere/` | No schema authority. |
| Policy and obligations | `policy/domains/atmosphere/` after accepted implementation | `policy/domains/air/` remains compatibility-only. |
| Fixtures and tests | `fixtures/domains/atmosphere/`, `tests/domains/atmosphere/`, accepted pipeline-test lanes | No duplicate Air suites. |
| Lifecycle data | `data/.../atmosphere/` after governed transitions | No writes. |
| Receipts and proof | `data/receipts/`, `data/proofs/` | No emitted artifacts. |
| Release, correction, rollback | `release/` | No decisions. |
| Public serving | governed API, released artifacts, reviewed UI/runtime | No direct route. |

[Back to top](#top)

---

## 3. Slug conflict and compatibility contract

### Current conflict

The repository contains both `air` and `atmosphere` segments across multiple roots. Presence alone does not make either path canonical. The strongest inspected placement guidance says:

- use `atmosphere/` for new Atmosphere domain lanes;
- treat pre-existing `air/` segments as drift candidates;
- avoid parallel evolution;
- require an ADR-class decision before creating or promoting parallel authority.

### Compatibility invariants

The Air path must satisfy all of these:

1. **One implementation authority.** A concern has one accepted executable home.
2. **No code fork.** Air must not copy Atmosphere runners, stages, helpers, or tests.
3. **No spec fork.** Air must not host duplicate specs, IDs, schedules, or consumer bindings.
4. **No source fork.** Alias selection must not activate a source or alter source role.
5. **No semantic fork.** Contracts and schemas stay under the accepted Atmosphere homes.
6. **No policy fork.** Air must not evaluate a second bundle or produce divergent decisions.
7. **No lifecycle fork.** Air must not write parallel RAW, WORK, PROCESSED, catalog, or published lanes.
8. **No receipt fork.** The same run must not emit separate Air and Atmosphere receipts.
9. **No release fork.** Alias handling must not create separate manifests or rollback targets.
10. **No public alias by accident.** A route, tile, export, cache key, screenshot, or AI reference cannot become public merely because a path exists.
11. **Migration visibility.** Every changed reference is inventoried and reviewable.
12. **Rollback availability.** Reference migration can be reversed without restoring duplicate authority.

### Proposed documentation-only dispositions

These labels are proposed review dispositions, not machine enums:

| Disposition | Meaning |
|---|---|
| `RETAIN_COMPATIBILITY_DOC` | Keep this README while references remain unresolved. |
| `REDIRECT_NEW_WORK` | Send new implementation to the preferred Atmosphere lane. |
| `HOLD_FOR_ADR` | Do not add or migrate executable behavior until governance resolves the slug. |
| `MIGRATE_REFERENCE` | Update a verified reference under an approved migration plan. |
| `DEPRECATE_AFTER_PROOF` | Retire the Air path only after consumers, links, receipts, and rollback are verified. |
| `CONFLICT_ERROR` | Stop when both paths appear active or a migration cannot prove single authority. |

[Back to top](#top)

---

## 4. Current repository maturity

### Capability matrix

| Capability | Current evidence | Safe status |
|---|---|---:|
| Air parent path | This README exists. | `CONFIRMED` |
| Air executable files | Checked contract, runner, normalizer, initializer absent. | `NOT ESTABLISHED` |
| Air child stage directories | No child stage implementation surfaced in bounded search. | `NOT ESTABLISHED` |
| Atmosphere parent path | Parent README exists. | `CONFIRMED DOCUMENTATION` |
| Atmosphere stage lanes | Normalize, validate, catalog, and publish README paths surfaced. | `README-BACKED` |
| Atmosphere stage execution | Child READMEs mark execution `NEEDS VERIFICATION`; workflow retains explicit holds. | `NOT ESTABLISHED` |
| Air spec lane | Compatibility guardrail; no concrete profile surfaced. | `COMPATIBILITY ONLY` |
| Atmosphere spec lane | README-only; no active profile surfaced. | `NO ACTIVE SPEC` |
| Atmosphere package | `kfm-domain-atmosphere` version `0.0.0`; empty `__init__.py`. | `GREENFIELD SCAFFOLD` |
| Atmosphere contracts | Object contract roster and expanded prose exist. | `PARTIAL / DRAFT` |
| Atmosphere schemas | One permissive decision-envelope scaffold and index children. | `PARTIAL SCAFFOLD` |
| Air policy | Repository-grounded compatibility guardrail. | `COMPATIBILITY ONLY` |
| Atmosphere policy | 33-line greenfield scaffold with over-broad placement wording. | `UNIMPLEMENTED` |
| Atmosphere tests | Parent scaffold and planned child lanes. | `EXECUTABLE COVERAGE UNVERIFIED` |
| Atmosphere workflow | Read-only maturity checks and explicit holds. | `READINESS GUARD, NOT ENFORCEMENT` |
| Proof production | Workflow confirms no accepted proof producer or command. | `HOLD` |
| Release dry run | Workflow confirms no accepted command or candidate manifest contract. | `HOLD` |
| Runtime/public use | Not established by inspected evidence. | `UNKNOWN` |

### What repository presence proves

Repository presence can prove:

- a path or document exists;
- a compatibility warning is recorded;
- an interface or future requirement is described;
- a workflow checks that current scaffold assumptions still hold.

It does not prove:

- source admission or source freshness;
- executable importability;
- an active parser, scheduler, or consumer;
- a complete contract or schema;
- accepted policy evaluation;
- collected tests or substantive CI;
- evidence closure;
- release approval;
- public availability;
- medical, regulatory, emergency, or life-safety authority.

[Back to top](#top)

---

## 5. Anti-collapse rules

The Air compatibility boundary must prevent naming drift from becoming knowledge or authority drift.

### Slug and implementation collapse

```text
air path exists                    -> air is canonical
air README is complete             -> air implementation exists
compatibility link                 -> executable alias exists
same code copied under both slugs  -> harmless redundancy
green readiness workflow           -> executable pipeline validated
```

All are denied.

### Atmosphere knowledge-character collapse

```text
AQI or category                    -> pollutant concentration
AOD, plume, smoke mask             -> surface PM2.5 observation
model, forecast, reanalysis        -> observed sensor value
climate normal or anomaly          -> current weather
station metadata                   -> measurement
low-cost sensor value              -> regulatory observation
advisory reference                 -> official warning or instruction
county or grid aggregate           -> person, household, parcel, or station exposure
```

All require explicit contracts, source roles, methods, caveats, time support, and evidence; several remain categorically non-equivalent.

### Governance collapse

```text
source reference          -> admitted source
successful fetch          -> source correctness
valid schema              -> validated Atmosphere claim
validator pass            -> policy approval
run receipt               -> EvidenceBundle
proof record              -> ReleaseManifest
release candidate         -> publication
AI explanation            -> evidence or official guidance
```

All are denied.

[Back to top](#top)

---

## 6. Allowed and denied content

### Allowed now

Until an accepted slug decision changes the role, this directory may contain only:

- this README;
- migration or deprecation notes that reference an accepted decision;
- a verified reference inventory or path map;
- static compatibility tests that prove no duplicate authority, after the test home is accepted;
- a narrowly documented redirect manifest, after its contract and consumer are accepted;
- correction notes for stale repository references;
- rollback instructions for a reviewed migration.

### Conditionally allowed later

A thin compatibility shim may be considered only when all are true:

1. an accepted ADR defines its purpose and lifetime;
2. the Atmosphere implementation is the sole executable authority;
3. the shim contains no transform, validation, policy, storage, receipt, proof, or release logic;
4. import and CLI behavior are tested;
5. no source or lifecycle side effect occurs at import time;
6. deprecation messaging is stable and safe;
7. one owner and rollback target are named;
8. the shim cannot be confused with a public route or official issuer.

### Denied content

Do not place here:

- Air-specific runners, normalizers, validators, catalog builders, or publishers;
- duplicated Atmosphere stage directories;
- source fetchers, credentials, private endpoints, or live payloads;
- declarative specs or schedules;
- reusable domain helpers;
- contracts, schemas, or policy rules;
- fixtures or tests copied from Atmosphere;
- RAW, WORK, QUARANTINE, PROCESSED, catalog, triplet, or published data;
- run receipts, evidence bundles, proof packs, manifests, correction notices, or rollback cards;
- API routes, tiles, exports, UI code, alerting code, or AI prompts that treat this path as truth.

[Back to top](#top)

---

## 7. Preferred Atmosphere implementation boundary

### Current preferred routing

```text
new Atmosphere implementation request
  -> verify domain scope and accepted object contract
  -> use pipeline_specs/atmosphere for reviewed declarative intent
  -> use packages/domains/atmosphere for reusable pure helpers
  -> use pipelines/domains/atmosphere for executable orchestration
  -> use accepted validators and tests
  -> write only through governed lifecycle transitions
  -> hand off to release authority
```

The graph is a responsibility map, not proof that every step exists today.

### Atmosphere stage lanes

The repository surfaces README-backed sublanes such as:

| Sublane | Intended role | Current evidence |
|---|---|---:|
| `normalize/` | Shape admitted material into validation-ready WORK candidates. | README-backed; execution unverified. |
| `validate/` | Produce bounded validation outcomes and quarantine/processed readiness. | README-backed; execution unverified. |
| `catalog/` | Prepare catalog closure after prior gates. | README surfaced; execution unverified. |
| `publish/` | Publish-readiness or release handoff only, never approval. | README surfaced; execution unverified. |

New work must not assume these documents define imports, commands, DTOs, schemas, outputs, or active consumers. Admission requires current file inspection and tests.

### One implementation rule

A future accepted pipeline must identify:

- one executable entrypoint;
- one consumer-bound specification;
- one package/helper boundary;
- one contract and schema set;
- one policy-evaluation path;
- one validator topology;
- one receipt vocabulary;
- one correction and rollback path.

If two paths claim the same responsibility, implementation stops until the conflict is resolved.

[Back to top](#top)

---

## 8. Source, measurement, and knowledge-character boundaries

### Source admission

Neither this Air lane nor the Atmosphere pipeline README admits sources. A future run may consume only:

- synthetic, minimized, no-network fixtures;
- immutable admitted RAW captures;
- governed WORK candidates;
- QUARANTINE records in explicit remediation mode;
- prior PROCESSED baselines when the contract permits comparison;
- accepted source descriptors and activation records by reference.

A source URL, connector README, dataset name, schedule, or successful HTTP response is not source admission.

### Minimum source obligations

Every input must preserve:

| Obligation | Required information |
|---|---|
| Identity | Stable source descriptor reference and source-native identifier. |
| Role | Observation, regulatory archive, public report, model, forecast, remote sensing, advisory context, climate baseline/anomaly, aggregate, candidate, synthetic, or another accepted role. |
| Rights | License, attribution, redistribution, confidentiality, and audience posture. |
| Time | Observation/report/issue/valid/expiry/model-run/retrieval timestamps as applicable. |
| Spatial support | Station, grid, raster, plume, county, region, level, height, and precision. |
| Method | Instrument, model, algorithm, correction, calibration, averaging period, and quality flags. |
| Caveats | Known limitations, outages, uncertainty, low-cost sensor status, and official-authority redirect. |
| Integrity | Input digest, retrieval record, and immutable lifecycle reference. |

### Required distinctions

- station or network context is not a measurement;
- an observation is not an AQI report category;
- AQI is not concentration;
- AOD is not PM2.5;
- smoke or plume context is not an exposure measurement;
- modeled and forecast fields are not observations;
- climate normals and anomalies are not current weather;
- advisory context is referral metadata, not KFM guidance;
- low-cost sensor values retain correction and limitation status;
- a derived fusion product retains every contributing role and method.

[Back to top](#top)

---

## 9. Lifecycle and finite outcomes

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Alias handling must never create a second lifecycle.

### Air compatibility posture by stage

| Stage | Air path behavior |
|---|---|
| Source event / Pre-RAW | No action. Redirect to accepted source and Atmosphere orchestration. |
| RAW | No write. Air must not create `data/raw/air/` by convenience. |
| WORK | No candidate creation. Compatibility checks may report stale references only. |
| QUARANTINE | No domain record write. Migration conflicts are documented in review artifacts or accepted drift lanes. |
| PROCESSED | No write. Air is not an alternate processed-data namespace. |
| CATALOG / TRIPLET | No projection. Existing references must resolve to the accepted Atmosphere identity. |
| PUBLISHED | No action. Public aliases require explicit application/release review. |

### Future pipeline outcome requirements

A future accepted Atmosphere pipeline should use finite, contract-backed outcomes such as:

- candidate produced for review;
- input held or quarantined;
- no-op because the exact governed version already exists;
- abstain because evidence, time, rights, or method support is insufficient;
- deny because the requested operation or audience is prohibited;
- error because execution could not complete safely.

This README does not define machine enum strings. The accepted contracts and schemas must do that.

### Alias conflict failure

When a run, spec, receipt, or public consumer references both Air and Atmosphere identities for the same responsibility, the safe result is a hold or error—not silent deduplication.

[Back to top](#top)

---

## 10. Time, freshness, method, and spatial support

### Time kinds

Atmosphere processing must distinguish, where applicable:

- observation time;
- sample start and end;
- report or issue time;
- valid start and end;
- expiry time;
- forecast reference time;
- model initialization and lead time;
- retrieval time;
- processing time;
- catalog time;
- release time;
- correction and supersession time.

A generic `timestamp` is insufficient when more than one time kind affects meaning.

### Freshness

Current-state presentation requires:

1. an accepted freshness profile;
2. source cadence and outage behavior;
3. last successful retrieval and observation/issue time;
4. stale-state reason;
5. fallback or no-data behavior;
6. visible age or validity where material;
7. denial of current-state claims when support is stale or unresolved.

An alias must not reset or hide freshness age.

### Units and methods

Every transformation must preserve:

- source parameter and unit;
- normalized parameter and unit;
- averaging period;
- conversion formula and version;
- instrument or model method;
- calibration/correction state;
- quality flags;
- uncertainty and limitations;
- TransformReceipt inputs when conversion is consequential.

### Spatial support

Do not collapse:

- station point into area-wide exposure;
- raster cell into station measurement;
- plume polygon into concentration;
- model level into surface condition;
- county aggregate into household or person exposure;
- exact infrastructure or private-sensor location into public geometry without review.

[Back to top](#top)

---

## 11. Output and side-effect boundary

### Air compatibility outputs

This lane may produce only documentation and review artifacts:

| Output | Allowed? | Notes |
|---|---:|---|
| Updated README | Yes | Documentation only. |
| Migration inventory | Proposed | Must be minimized and reviewed. |
| Drift reference | Proposed | Belongs in the accepted drift register. |
| Static compatibility test result | Proposed | Test root must own executable proof. |
| Runtime candidate | No | Atmosphere pipeline responsibility. |
| Lifecycle record | No | Governed data transition responsibility. |
| Receipt or proof | No | Emitted only by accepted systems. |
| Release object | No | Release authority only. |
| Public alias or route | No | Application and release review required. |

### Side effects denied by default

A compatibility path must not:

- perform network requests;
- load secrets;
- activate connectors;
- write filesystem, database, object-store, cache, queue, telemetry, or lifecycle state;
- evaluate policy;
- mint canonical IDs;
- create EvidenceRefs or EvidenceBundles;
- emit run receipts;
- assemble release manifests;
- publish, deploy, alert, notify, or redirect public clients;
- mutate source or Atmosphere records.

### Error and log minimization

Compatibility errors must reveal only what is necessary:

- path or profile identifier;
- safe reason code;
- expected preferred target;
- migration action or reviewer role;
- no source payload, credentials, exact private location, or sensitive observation content.

[Back to top](#top)

---

## 12. Rights, sensitivity, policy, and security

### Rights and sensitivity

Atmosphere products can expose or imply:

- exact station, sensor, infrastructure, or facility locations;
- private or low-cost sensor deployments;
- health- or exposure-adjacent interpretations;
- operational outages or network gaps;
- restricted source terms;
- cross-domain infrastructure, agriculture, habitat, or population patterns.

Aggregation, coarsening, aliasing, or summarization does not automatically lower sensitivity.

### Policy boundary

The inspected Air policy path is compatibility-only. The preferred Atmosphere policy path is still a greenfield scaffold. Therefore:

- no policy evaluator is assumed;
- no filename, package name, or README text is treated as an active rule;
- no allow, deny, restrict, abstain, redirect, or obligation vocabulary is canonical until contracts and schemas accept it;
- the most restrictive source, rights, sensitivity, time, audience, advisory, and release posture wins;
- policy success never replaces evidence, validation, or release approval.

### Official-authority boundary

KFM must not issue or simulate:

- AQI or medical guidance;
- regulatory compliance determinations;
- watches, warnings, advisories, evacuation instructions, or protective actions;
- official forecasts;
- emergency notifications;
- exposure diagnoses.

A released public carrier may reference an official source and direct the user there, subject to evidence, rights, policy, time validity, and release review.

### Security controls

Future implementation must include:

- no secrets in specs, fixtures, logs, receipts, screenshots, or issues;
- no network in the default test suite;
- pinned and reviewed dependencies where required;
- input size and decompression limits;
- timeouts and bounded retries for source operations;
- safe parsing of archives and structured payloads;
- no dynamic code execution from source content;
- minimized telemetry;
- deterministic replay;
- review of public geometry and low-cost sensor detail;
- rollback for code, configuration, source activation, and release changes.

[Back to top](#top)

---

## 13. Specification, package, and executable split

### Air compatibility specification

[`pipeline_specs/air/`](../../../pipeline_specs/air/README.md) is a compatibility guardrail. It must not receive a copy of an Atmosphere specification.

### Preferred Atmosphere specification

[`pipeline_specs/atmosphere/`](../../../pipeline_specs/atmosphere/README.md) is the documentation-preferred spec lane, but current evidence shows:

- README-only bounded inventory;
- no active profile;
- no accepted parser or registry;
- no consumer binding;
- no schedule activation;
- no source activation;
- no release linkage.

A future spec must name exactly one verified executable consumer and the accepted contract/schema/policy versions.

### Reusable package

[`packages/domains/atmosphere/src/atmosphere/`](../../../packages/domains/atmosphere/src/atmosphere/README.md) is the reusable helper boundary. Current evidence shows:

- package version `0.0.0`;
- empty `__init__.py`;
- no established exports or API;
- documentation of proposed helper families.

Reusable helpers must be pure or side-effect-minimal and cannot own orchestration, source admission, policy, evidence, lifecycle writes, release, or public serving.

### Executable orchestration

[`pipelines/domains/atmosphere/`](../atmosphere/README.md) is the preferred executable boundary. It must own:

- spec consumption;
- stage sequencing;
- lifecycle input/output handoffs;
- calls to accepted packages and validators;
- run identity and replay;
- receipt emission by accepted emitters;
- bounded failure and quarantine routing.

The Air path owns none of those while it remains compatibility-only.

[Back to top](#top)

---

## 14. Validators, fixtures, tests, and CI

### Current posture

- Atmosphere test documentation exists, but executable coverage is unverified.
- The Air pipeline-specific test README is absent at the checked path.
- The Atmosphere workflow actively checks for the appearance of executable tests and validators so maintainers replace readiness holds deliberately.
- A green readiness hold proves only that the repository still matches the documented scaffold state.

### First executable proof slice

The first implementation slice should be owned by Atmosphere, not Air, and should be:

- no-network;
- deterministic;
- synthetic and public-safe;
- limited to one accepted object family and one source role;
- schema- and contract-bound;
- explicit about units, methods, time, spatial support, caveats, and freshness;
- incapable of writing public or release state;
- tested for positive, negative, abstain/hold, and replay behavior.

### Required test families

Before active use, prove:

1. Air references redirect or fail without executing duplicate logic.
2. No Air runner, spec, policy, or lifecycle writer is discovered as active.
3. Atmosphere imports and commands are deterministic.
4. Default tests perform no network access.
5. AQI cannot pass as concentration.
6. AOD, smoke, or plume context cannot pass as PM2.5 observation.
7. model and forecast records cannot pass as observations.
8. stale inputs cannot support current-state claims.
9. low-cost sensor caveats cannot be dropped.
10. official advisory context cannot become KFM instruction.
11. source role, time, units, method, and spatial support survive transforms.
12. unresolved evidence causes bounded abstention or hold.
13. policy absence or conflict fails closed.
14. no direct public or release write occurs.
15. correction and rollback invalidate or supersede affected outputs.
16. migration and deprecation preserve links and rollback.

### CI graduation

Replace the current holds only when:

- the accepted command is named;
- its inputs and outputs are contract-backed;
- fixtures and negative cases exist;
- tests are collected and deterministic;
- validator ownership is resolved;
- policy and evidence dependencies are explicit;
- artifact and receipt handling is defined;
- no-network behavior is enforced;
- correction and rollback tests pass;
- the workflow remains least-privilege and non-publishing.

[Back to top](#top)

---

## 15. Receipts, proofs, and evidence closure

### Separation

| Artifact | Purpose | Not equivalent to |
|---|---|---|
| Run receipt | Records execution inputs, versions, parameters, outputs, and result. | EvidenceBundle or release approval. |
| Transform receipt | Records consequential conversion or normalization. | Measurement truth. |
| Validation report | Records checks and findings. | PolicyDecision or proof. |
| Policy decision | Records accepted policy evaluation. | Evidence or release. |
| EvidenceBundle | Supports consequential claims. | Release approval. |
| Proof pack | Packages verification evidence. | Public publication. |
| Release manifest | Records governed release decision and artifacts. | Source truth or official advice. |
| Correction/rollback record | Changes validity or serving state. | Hidden deletion. |

### Future receipt obligations

An accepted Atmosphere run should record:

- pipeline and spec identity/version;
- canonical domain segment;
- source descriptor and activation references;
- input lifecycle references and hashes;
- source roles and knowledge characters;
- object contract and schema versions;
- package and executable versions;
- method, units, averaging period, time support, spatial support, caveats, and freshness profile;
- policy and validation dependency results;
- output refs and hashes;
- finite outcome and safe reason codes;
- prior version and correction lineage;
- reviewer or release handoff where required.

An alias or compatibility layer must not mint a second receipt for the same execution.

### Evidence rule

Consequential answer-like or public-facing Atmosphere claims require resolvable EvidenceRef-to-EvidenceBundle support appropriate to the claim. When support is absent, stale, incomplete, rights-restricted, method-mismatched, or role-collapsed, narrow, abstain, deny, hold, or report an error.

[Back to top](#top)

---

## 16. Promotion, release, correction, and rollback

### Proposed trust chain

```text
admitted Atmosphere input
  -> deterministic WORK candidate
  -> validation result
  -> policy decision
  -> evidence closure
  -> PROCESSED version
  -> catalog / triplet candidate
  -> independent review
  -> release candidate
  -> ReleaseManifest
  -> governed public carrier
```

The Air compatibility path does not appear in this chain as a processing authority.

### Release boundary

A future Air route alias, legacy export name, or public link may exist only when:

- the release manifest explicitly names it;
- the alias resolves to the same released artifact and version;
- policy obligations and caveats remain unchanged;
- freshness and correction state remain visible;
- official-authority redirection remains intact;
- the rollback card covers the alias;
- no internal or unreleased store is exposed.

### Correction propagation

A correction affecting Atmosphere data or pipeline behavior must identify:

- affected source and source versions;
- affected runs and receipts;
- affected processed, catalog, triplet, proof, and release objects;
- affected Air compatibility references or aliases;
- validity interval and superseding version;
- public carrier behavior;
- withdrawal or rollback action;
- reviewer and audit trail.

### Rollback

Rollback must be able to:

- restore the prior README or compatibility mapping;
- disable a newly introduced alias;
- revert a spec or source activation independently;
- supersede invalid processed/catalog outputs;
- withdraw released carriers;
- preserve receipts, proof, decisions, and correction history;
- avoid restoring duplicate executable authority.

[Back to top](#top)

---

## 17. Directory contract and file admission

### Confirmed direct lane

```text
pipelines/domains/air/
└── README.md
```

This is a bounded inspected shape, not a permanent recursive proof.

### Do not scaffold the v0.1 tree

The v0.1 README proposed files such as:

- `PIPELINE_CONTRACT.md`;
- `run_dry_fixture.py`;
- Air observation, weather, smoke, and AOD normalizers;
- caveat receipt and catalog helpers;
- validators and emitters;
- local adapters and tests.

Do not create those paths mechanically. Most belong in the preferred Atmosphere lane, shared packages, validators, schemas, policy, tests, data, or release roots after specific contracts are accepted.

### File-admission checklist

Before adding anything under this Air path, prove:

1. the file's primary responsibility is compatibility or migration;
2. it cannot live in an existing accepted Atmosphere or shared root;
3. an ADR or migration record authorizes the file when executable behavior is involved;
4. it does not duplicate Atmosphere implementation or semantics;
5. it has named owners and review burden;
6. it has deterministic tests;
7. it performs no hidden source, lifecycle, policy, proof, release, or public side effect;
8. its lifetime and deprecation trigger are defined;
9. correction and rollback are defined;
10. all related references are updated without creating a second authority.

### Migration discipline

A move or retirement must preserve:

- Git history;
- stable documentation identity where practical;
- inbound link and import inventory;
- redirect or deprecation behavior;
- receipt, proof, catalog, and release references;
- correction and rollback targets;
- a record of why the decision was made;
- tests proving one canonical implementation remains.

[Back to top](#top)

---

## 18. ADR, migration, and deprecation

### ADR questions

The slug decision must answer:

- Is `atmosphere` the canonical domain segment?
- Does `air` remain as documentation only, a temporary import alias, a public alias, or no path?
- Which roots currently contain Air segments?
- Which Air segments are compatibility-only versus potentially active?
- What is the migration order?
- Which references are breaking?
- How are receipts, schema IDs, contract IDs, catalog IDs, routes, caches, and release records handled?
- What is the deprecation period?
- What proves that no duplicate authority remains?
- What is the rollback plan?

### Migration manifest

A governed migration should inventory:

| Reference class | Examples |
|---|---|
| Repository files | Markdown links, imports, configs, specs, workflows, tests, fixtures. |
| Machine identifiers | schema `$id`, contract IDs, spec IDs, pipeline IDs, receipt fields. |
| Data and catalog | lifecycle paths, dataset IDs, catalog/triplet references. |
| Release | candidates, manifests, aliases, corrections, rollback cards. |
| Applications | API routes, UI links, tile/layer IDs, exports, cache keys. |
| Operations | dashboards, alerts, runbooks, telemetry, scheduled tasks. |
| External | published links, bookmarks, integrations, downstream consumers. |

Unknown classes remain explicit. Do not assume repository search covers external consumers.

### Deprecation gate

Retire this path only when:

- an accepted decision exists;
- all known references are classified;
- no executable Air implementation exists;
- the Atmosphere implementation and tests are accepted;
- redirects or replacements are validated;
- release and correction records are updated;
- external breakage risk is reviewed;
- rollback is tested;
- the final removal is independently reviewed.

[Back to top](#top)

---

## 19. Smallest sound resolution sequence

### Wave 0 — freeze duplicate growth

- Keep Air documentation-only.
- Block new Air runners, specs, source bindings, policies, lifecycle lanes, and public routes.
- Inventory current Air and Atmosphere paths.
- Record drift and owners.

### Wave 1 — decide authority

- Draft and review the slug ADR.
- Select one canonical implementation, spec, contract, schema, policy, test, data, and release segment.
- Define compatibility lifetime and migration rules.
- Establish CODEOWNERS and separation of duties.

### Wave 2 — close semantic and machine contracts

- Accept object contracts and source-role / knowledge-character vocabulary.
- Accept schemas, IDs, units, time, freshness, spatial, caveat, and outcome profiles.
- Accept policy input/decision contracts.
- Establish synthetic fixtures and negative cases.

### Wave 3 — implement one Atmosphere slice

- Implement one deterministic, no-network Atmosphere entrypoint.
- Bind one reviewed specification.
- Use reusable package helpers deliberately.
- Emit accepted receipts.
- Add executable tests and validators.
- Keep all public and release side effects denied.

### Wave 4 — prove governance and migrate

- Close evidence resolution and policy evaluation.
- Add catalog/release handoff with independent review.
- Test correction and rollback.
- Migrate Air references through the approved manifest.
- Retain or retire this path according to the ADR.

[Back to top](#top)

---

## 20. Definition of done

### This README revision

This revision is complete when it:

- records the current Air lane as README-only;
- identifies the Atmosphere preference without claiming it is executable;
- preserves the slug conflict as ADR-class;
- removes the implication that a second Air implementation should be scaffolded;
- routes every responsibility to the correct root;
- preserves source-role, knowledge-character, unit, time, freshness, caveat, evidence, policy, release, correction, and rollback boundaries;
- denies direct publication and official-guidance behavior;
- provides a reversible migration and file-admission contract;
- pairs the change with a generated-work receipt.

### Future compatibility resolution

Compatibility resolution is complete only when:

- the slug ADR is accepted;
- owners and review duties are named;
- all known Air/Atmosphere references are inventoried;
- one canonical implementation and spec are accepted;
- contracts and schemas are sufficiently complete;
- policy and validator topology are accepted;
- no-network fixtures and executable tests exist;
- receipts and proof paths are verified;
- public aliases, if any, are release-controlled;
- correction and rollback are tested;
- no duplicate executable, policy, data, or release authority remains.

### Future Atmosphere implementation

A production claim additionally requires runtime evidence: successful deterministic executions, emitted receipts, validated outputs, policy results, evidence closure, monitoring, review, release records, correction handling, rollback proof, and governed public consumption.

[Back to top](#top)

---

## 21. Open verification register

| ID | Question | Status |
|---|---|---|
| `AIR-PIPE-001` | Which slug is accepted as canonical: `air` or `atmosphere`? | `NEEDS ADR` |
| `AIR-PIPE-002` | What is the long-term role and lifetime of this Air path? | `NEEDS VERIFICATION` |
| `AIR-PIPE-003` | Which inbound repository links and imports reference this path? | `UNKNOWN` |
| `AIR-PIPE-004` | Which external consumers or published links reference Air identifiers? | `UNKNOWN` |
| `AIR-PIPE-005` | Who owns the canonical Atmosphere pipeline implementation? | `NEEDS VERIFICATION` |
| `AIR-PIPE-006` | Are any differently named executable Atmosphere modules already present? | `UNKNOWN` |
| `AIR-PIPE-007` | Which Atmosphere stage READMEs correspond to actual code? | `NEEDS VERIFICATION` |
| `AIR-PIPE-008` | What parser or registry owns Atmosphere specifications? | `UNKNOWN` |
| `AIR-PIPE-009` | Which sources are admitted and active for Atmosphere? | `UNKNOWN` |
| `AIR-PIPE-010` | Which source roles and knowledge characters are accepted? | `NEEDS VERIFICATION` |
| `AIR-PIPE-011` | Which object contracts are accepted rather than draft prose? | `NEEDS VERIFICATION` |
| `AIR-PIPE-012` | Which schemas are field-complete and validator-backed? | `NEEDS VERIFICATION` |
| `AIR-PIPE-013` | What policy bundle, namespace, evaluator, and decision vocabulary are accepted? | `NEEDS VERIFICATION` |
| `AIR-PIPE-014` | What validator topology owns Atmosphere checks? | `CONFLICTED / NEEDS VERIFICATION` |
| `AIR-PIPE-015` | Which fixtures contain real payloads and named consumers? | `UNKNOWN` |
| `AIR-PIPE-016` | Which Atmosphere tests are collected and substantive? | `UNKNOWN` |
| `AIR-PIPE-017` | What station/network identity profile is accepted? | `NEEDS VERIFICATION` |
| `AIR-PIPE-018` | What unit, method, averaging-period, and quality vocabularies are accepted? | `NEEDS VERIFICATION` |
| `AIR-PIPE-019` | What observation, issue, valid, expiry, model-run, retrieval, and release time contract is accepted? | `NEEDS VERIFICATION` |
| `AIR-PIPE-020` | What freshness and stale-state profiles exist per source family? | `NEEDS VERIFICATION` |
| `AIR-PIPE-021` | What low-cost sensor correction and caveat profile is accepted? | `NEEDS VERIFICATION` |
| `AIR-PIPE-022` | How are AQI/report, concentration, AOD, smoke, and model boundaries enforced? | `NEEDS VERIFICATION` |
| `AIR-PIPE-023` | What official-authority redirect contract applies to advisory context? | `NEEDS VERIFICATION` |
| `AIR-PIPE-024` | Which run, transform, validation, caveat, freshness, and correction receipts are accepted? | `NEEDS VERIFICATION` |
| `AIR-PIPE-025` | What evidence resolver and proof producer support Atmosphere claims? | `UNKNOWN` |
| `AIR-PIPE-026` | Which release candidate, manifest, correction, withdrawal, and rollback records are accepted? | `NEEDS VERIFICATION` |
| `AIR-PIPE-027` | Which workflows are branch-protection significant? | `UNKNOWN` |
| `AIR-PIPE-028` | Which public APIs, layers, tiles, exports, or AI surfaces consume Atmosphere outputs? | `UNKNOWN` |
| `AIR-PIPE-029` | How will compatibility redirects be tested and monitored? | `PROPOSED / NEEDS VERIFICATION` |
| `AIR-PIPE-030` | What proves migration completion and safe Air-path retirement? | `NEEDS VERIFICATION` |

[Back to top](#top)

---

## 22. Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior `pipelines/domains/air/README.md` | `CONFIRMED` | Existing path, v0.1 scope, safety gates, and slug conflict. | Design-forward trees and candidate examples did not prove implementation. |
| Directory Rules | `CONFIRMED doctrine` | Responsibility roots, drift visibility, ADR triggers, reversible migration. | Does not decide implementation existence. |
| Atmosphere canonical-path guide | `CONFIRMED repository document / draft decision` | Prefers `atmosphere` for new work and treats `air` as drift candidate. | The slug ADR remains unaccepted in inspected evidence. |
| Atmosphere pipeline parent | `CONFIRMED README` | Preferred executable boundary and stage responsibilities. | Does not establish executable behavior. |
| Atmosphere normalize and validate READMEs | `CONFIRMED README-backed sublanes` | Detailed intended stage contracts. | Both explicitly leave execution unverified. |
| Air pipeline-spec README | `CONFIRMED compatibility guardrail` | Air specs must not become parallel authority. | Does not prove redirect code or active spec. |
| Atmosphere pipeline-spec README | `CONFIRMED README-only preferred lane` | Current spec maturity and required future contract. | No active profile, parser, schedule, or consumer established. |
| Atmosphere package README, pyproject, and initializer | `CONFIRMED scaffold` | Reusable package responsibility, version `0.0.0`, empty `__init__.py`. | Other differently named helpers remain possible but unverified. |
| Atmosphere contract README | `CONFIRMED partial contract index` | Object meanings and anti-collapse rules. | Full schema pairing and enforcement remain incomplete. |
| Atmosphere schema README | `CONFIRMED partial scaffold` | Preferred schema path and permissive decision-envelope scaffold. | Does not prove field-complete schemas or validation. |
| Air policy README | `CONFIRMED compatibility guardrail` | Redirect and no-parallel-policy posture. | Does not implement policy. |
| Atmosphere policy README | `CONFIRMED greenfield scaffold` | Preferred path exists. | Placement wording is over-broad; no accepted evaluator or rule set. |
| Atmosphere tests README | `CONFIRMED scaffold` | Required proof families and no-network posture. | Executable inventory and results remain unverified. |
| `domain-atmosphere` workflow | `CONFIRMED readiness guard` | Least-privilege checks and explicit validation/proof/release holds. | A green held run is not substantive validation or release proof. |
| Exact Air path checks | `CONFIRMED bounded absence` | No checked local contract, runner, normalizer, initializer, or pipeline-test README. | Not a permanent or exhaustive historical absence claim. |
| Open PR and branch searches | `CONFIRMED bounded concurrency check` | No matching active task surfaced. | Search indexing and naming limits apply. |

[Back to top](#top)

---

## 23. Change history

### v0.2 — 2026-07-19

- Reclassified the Air lane as compatibility and migration only.
- Pinned the README to current repository evidence.
- Confirmed bounded README-only direct inventory.
- Redirected new implementation toward Atmosphere without claiming that lane is executable.
- Replaced speculative executable/spec/test trees with file-admission and migration contracts.
- Removed the pseudo-machine Air candidate example.
- Added maturity, anti-collapse, source, measurement, time, freshness, policy, security, CI, evidence, release, correction, rollback, ADR, and deprecation guidance.
- Added a 30-item verification register and evidence ledger.
- Changed no executable or public behavior.

### v0.1 — 2026-06-13

- Established the Air/Atmosphere pipeline outline.
- Recorded slug conflict, lifecycle, source-family, caveat, evidence, policy, release, correction, and rollback intent.
- Proposed a local executable tree and illustrative candidate shape that v0.2 now reclassifies as unimplemented design.

---

> [!IMPORTANT]
> **Publication boundary.** Updating or merging this README does not activate a source, resolve the Air/Atmosphere slug, implement a pipeline, validate an observation, create evidence, apply policy, release an artifact, publish a map or API, or authorize medical, regulatory, emergency, or life-safety guidance.
