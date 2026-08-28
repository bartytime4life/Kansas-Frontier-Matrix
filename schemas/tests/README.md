<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-readme
title: schemas/tests/ — Schema-Test Compatibility and Routing Boundary
type: README
version: v0.2
status: draft; repository-grounded; compatibility-documentation-only; no-executable-tests; no-fixture-payloads; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; independent schema, fixture, test, validator, and documentation stewardship remain NEEDS VERIFICATION"
created: 2026-07-04
updated: 2026-08-13
policy_label: public
truth_posture: cite-or-abstain
owning_root: schemas/
responsibility: "Document the historical schemas/tests compatibility lane, route machine shapes, fixtures, executable tests, and validators to their current responsibility roots, and prevent path presence from being mistaken for validation or authority."
current_path: schemas/tests/README.md
supersedes:
  - "v0.1 documentation at the same path"
superseded_by: []
evidence_snapshot: "bartytime4life/Kansas-Frontier-Matrix main@e842898e36c6a49fa32de08f69deb1a26cc46bfc"
evidence_refs:
  - "schemas/tests/README.md@b6c2c6d44fcefbdf6ab9e452b1c09326563a4c8e"
  - "schemas/README.md@ce53d0ddb998ddcb8208d0367c90f9c25e31a8ad"
  - "schemas/tests/valid/README.md@79da4aed79a670024eadecf150101b5b1632b65b"
  - "schemas/tests/invalid/README.md@cb988fea8e291c936470de3d4201261665ae8053"
  - "tests/schemas/README.md@cf1c80a3c9aca7df41a8620f64e1f384a0aba42f"
  - "tests/contracts/README.md@f58e0222de1c8228daff6d4dc6243ed713927607"
  - "tools/validators/validator_registry.json@c65c1c2b27b85be4bdc3c42d0555c6e8e44698e2"
  - "tools/validators/_common/run_all.py@39e57978b3d3d24769ab56cf5b805d51de18f33f"
  - ".github/workflows/schema-validation.yml@0e1562f539323daa401184738a0c490b51e2999b"
  - "Makefile@c5d0aee3de558d76c1e1639bcfd8cf1c71a0d326"
  - ".github/CODEOWNERS@dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61"
  - "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md@3ba5f902ffe20a65a259cb0a7dab07f1725d204b"
  - "docs/doctrine/directory-rules.md@fd49a0b83e55cef52c1124281f093e263526898d"
related:
  - ../README.md
  - ./valid/README.md
  - ./invalid/README.md
  - ../../fixtures/README.md
  - ../../tests/README.md
  - ../../tests/schemas/README.md
  - ../../tests/contracts/README.md
  - ../../tools/validators/README.md
  - ../../tools/validators/validator_registry.json
  - ../../.github/workflows/schema-validation.yml
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, schemas, tests, compatibility, fixtures, validation, machine-shape, non-authoritative, no-network]
notes:
  - "Current repository evidence confirms that this lane contains documentation and empty-directory sentinels only: nineteen README files and fourteen .gitkeep files across the full schemas/tests subtree."
  - "No JSON schema, fixture payload, Python test module, validator implementation, validation report, receipt, proof, release object, or published artifact is established under this path."
  - "The schema-validation workflow is triggered by schemas/** changes but consumes schema JSON, fixtures/, tests/schemas, tests/contracts, and tools/validators surfaces; trigger inclusion does not make this compatibility lane an executable test root."
  - "This revision changes documentation only and creates no schema, contract, fixture, test, validator, policy, lifecycle, release, deployment, or publication effect."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/tests/` — Schema Test Compatibility Index

> **One-line purpose.** `schemas/tests/` is a documentation-only compatibility lane that routes schema definitions, fixture polarity, executable tests, and validator code to their current responsibility roots without becoming a second test or fixture authority.

[![Status: compatibility](https://img.shields.io/badge/status-compatibility--only-6e7781?style=flat-square)](#status-and-evidence)
[![Contents: docs only](https://img.shields.io/badge/contents-READMEs%20%2B%20.gitkeep-0969da?style=flat-square)](#current-directory-map)
[![Executable tests: elsewhere](https://img.shields.io/badge/executable%20tests-tests%2F-f59e0b?style=flat-square)](#responsibility-routing)
[![Fixtures: elsewhere](https://img.shields.io/badge/fixtures-fixtures%2F-8250df?style=flat-square)](#responsibility-routing)
[![Publication: none](https://img.shields.io/badge/publication-none-b42318?style=flat-square)](#non-effects-and-trust-boundary)

> [!IMPORTANT]
> **Path presence is not test authority.** Accepted ADR-0029 adopts the Directory Rules placement model, which assigns machine shape to `schemas/`, executable enforceability to `tests/`, representative cases to `fixtures/`, and reusable validation code to `tools/`. This nested compatibility lane may explain those relationships; it may not collapse them.

<!-- callout-separator -->

> [!WARNING]
> **Do not add valid or invalid payloads here by convention.** The current `valid/` and `invalid/` subtrees contain only navigation READMEs and `.gitkeep` sentinels. New examples belong in an accepted fixture family, and new assertions belong in an accepted test root, unless a separately reviewed migration establishes a different single writer and updates every consumer.

<!-- callout-separator -->

> [!CAUTION]
> **A passing schema check proves bounded machine-shape behavior only.** It does not establish semantic truth, evidence closure, source authority, policy approval, rights or sensitivity clearance, review completion, release readiness, public safety, or publication.

**Quick navigation:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-and-inheritance) · [Map](#current-directory-map) · [Routing](#responsibility-routing) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Flow](#inputs-outputs-writers-and-consumers) · [Exposure](#exposure-mutation-retention-and-storage) · [Compatibility](#compatibility-and-migration-posture) · [Validation](#validation-and-negative-checks) · [CI](#ci-and-execution-surface) · [Contribute](#contributor-workflow) · [Review](#review-and-escalation) · [Rollback](#correction-rollback-and-retirement) · [Open items](#open-verification-items) · [References](#references)

---

<a id="purpose"></a>

## Purpose

`schemas/tests/` preserves a historical schema-test navigation shape inside the canonical machine-shape root. Its current job is to:

- make the legacy `valid/` and `invalid/` branches visible;
- state that neither branch is a current fixture or executable-test authority;
- route contributors to canonical schemas, semantic contracts, fixtures, tests, validators, and workflows;
- prevent empty directories and polished READMEs from being described as implementation evidence;
- retain migration context until maintainers explicitly retain, migrate, mirror, deprecate, or retire the lane.

This README governs `schemas/tests/` and its direct children only. Child READMEs own deeper navigation and local compatibility notes. Nothing in this document accepts ADR-0001 or ADR-0002, creates a new canonical home, moves files, activates validation, or changes runtime behavior.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and Evidence

The current evidence snapshot is pinned to `main@e842898e36c6a49fa32de08f69deb1a26cc46bfc`.

| Surface | Current result | Safe conclusion |
| --- | --- | --- |
| Tracked path | **CONFIRMED** | `schemas/tests/README.md` exists and retains its exact document identity and H1. |
| Root role | **CONFIRMED** | `schemas/` owns machine-checkable shape under the adopted responsibility-root model. |
| Local role | **CONFIRMED** | `schemas/README.md` classifies `schemas/tests/` as a compatibility/documentation lane. |
| Direct children | **CONFIRMED** | Exactly `valid/` and `invalid/`, plus this README. |
| Full local subtree | **CONFIRMED** | Nineteen READMEs and fourteen `.gitkeep` files; no other tracked file classes. |
| Schema definitions here | **NONE CONFIRMED** | No `.json` or `.schema.json` file exists under `schemas/tests/`. |
| Fixture instances here | **NONE CONFIRMED** | No valid, invalid, edge, golden, or expected-output payload is present. |
| Executable tests here | **NONE CONFIRMED** | No Python, JavaScript, shell, or other runnable test source is present. |
| Canonical executable test lanes | **CONFIRMED** | Current schema-validation invokes `tests/schemas/` and `tests/contracts/`. |
| Fixture authority | **CONFIRMED elsewhere** | Configured aggregate validators consume nonempty valid/invalid families under `fixtures/`. |
| Validator implementation | **CONFIRMED elsewhere** | Registry and validator code live under `tools/validators/`. |
| Workflow relationship | **CONFIRMED trigger, not ownership** | Changes under `schemas/**` trigger schema validation; the workflow does not treat this README subtree as fixture or test authority. |
| Review route | **CONFIRMED routing only** | `.github/CODEOWNERS` routes `/schemas/` to `@bartytime4life`; required independent approval remains unverified. |
| Hosted result for a future revision | **NEEDS VERIFICATION** | Workflow source is not proof that a particular branch passed. |

### Truth labels used here

| Label | Meaning |
| --- | --- |
| **CONFIRMED** | Verified from pinned repository bytes, tree objects, source, tests, or workflow definitions. |
| **PROPOSED** | A future placement, migration, guard, or decision not yet accepted and implemented. |
| **UNKNOWN** | Available evidence does not support a stronger statement. |
| **NEEDS VERIFICATION** | A named repository, review, or operational check can resolve the item. |
| **CONFLICTED** | More than one admissible source claims incompatible ownership or behavior. |

[Back to top](#top)

---

<a id="authority-and-inheritance"></a>

## Authority and Inheritance

This boundary inherits from:

1. KFM's truth, evidence, lifecycle, non-publication, correction, and rollback invariants;
2. accepted ADR-0029 and the adopted Directory Rules bytes;
3. the current [`schemas/` root contract](../README.md);
4. the separate [`fixtures/`](../../fixtures/README.md), [`tests/`](../../tests/README.md), and [`tools/validators/`](../../tools/validators/README.md) responsibility roots;
5. current repository evidence as implementation fact, not automatic canon.

ADR-0001 proposes `schemas/contracts/v1/` as the canonical contract-backed schema home. ADR-0002 records the contracts-versus-schemas split but remains source `draft` and effectively proposed. Current code and documentation may follow parts of those proposals; this compatibility README cannot accept either decision.

### Local authority statement

This directory owns only:

- human navigation for its own compatibility subtree;
- explicit non-ownership and non-effect boundaries;
- migration, deprecation, correction, and rollback guidance for this path;
- links to the current executable surfaces.

It does not own schema meaning, schema adoption, fixture truth, test assertions, validator behavior, CI policy, policy decisions, data lifecycle, evidence, release, or publication.

[Back to top](#top)

---

<a id="current-directory-map"></a>

## Current Directory Map

Verified direct-child view:

```text
schemas/tests/
├── README.md   # This compatibility and routing boundary
├── invalid/    # Documentation-only negative-case compatibility index
└── valid/      # Documentation-only positive-case compatibility index
```

| Direct child | Current posture | Deeper inventory owner |
| --- | --- | --- |
| [`invalid/`](./invalid/README.md) | Nine READMEs and seven `.gitkeep` files across its subtree; no negative-case payloads | `invalid/README.md` and its child READMEs |
| [`valid/`](./valid/README.md) | Nine READMEs and seven `.gitkeep` files across its subtree; no positive-case payloads | `valid/README.md` and its child READMEs |

The empty-directory sentinels preserve tracked paths only. They do not prove a case exists, a validator consumes the lane, a domain is implemented, or a compatibility path should remain indefinitely.

[Back to top](#top)

---

<a id="responsibility-routing"></a>

## Responsibility Routing

| Need | Current responsibility surface | Boundary |
| --- | --- | --- |
| Canonical machine-checkable shape | [`schemas/contracts/v1/`](../contracts/v1/) and reviewed schema-family lanes | Schema location does not establish semantic or policy authority. |
| Semantic meaning and invariants | [`contracts/`](../../contracts/README.md) | Contract prose does not execute validation. |
| Valid, invalid, edge, denied, and golden examples | [`fixtures/`](../../fixtures/README.md) under an accepted object-family lane | Fixture presence is not truth, source admission, or release. |
| Executable schema conformance | [`tests/schemas/`](../../tests/schemas/README.md) | Tests prove only selected observed behavior. |
| Executable semantic/fixture bindings | [`tests/contracts/`](../../tests/contracts/README.md) | Contract tests do not own schemas or policy. |
| Reusable validators and orchestration | [`tools/validators/`](../../tools/validators/README.md) | Validator code does not adopt a schema or approve an object. |
| Validator selection | [`validator_registry.json`](../../tools/validators/validator_registry.json) | The registry selects commands and profiles; it is not a schema registry or release record. |
| Schema CI coordination | [`schema-validation.yml`](../../.github/workflows/schema-validation.yml) | Workflow execution produces bounded run evidence, not authority. |
| Allow, deny, restrict, hold, or abstain decisions | [`policy/`](../../policy/README.md) | Policy does not replace shape or semantic contracts. |
| Lifecycle records, receipts, proofs, catalogs, and published carriers | Governed [`data/`](../../data/README.md) families | No lifecycle artifact belongs under this compatibility lane. |
| Release, correction, withdrawal, and rollback decisions | [`release/`](../../release/README.md) | Schema validity never grants release or publication. |

### Dependency direction

```text
contracts ──described-by──> schemas
fixtures  ──validated-by──> schemas + validators
tests     ──exercise──────> schemas + fixtures + validators
workflow  ──coordinates──> schemas + fixtures + tests + validators

schemas/tests/ ──documents routing only──> those responsibility surfaces
```

No reverse arrow grants this path authority over the linked root.

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What Belongs Here

Under the current compatibility posture, permitted content is narrow:

- this boundary README;
- child navigation READMEs that accurately describe existing paths and non-effects;
- `.gitkeep` sentinels while a reviewed compatibility or retirement plan still needs the empty path;
- migration, alias, deprecation, and tombstone notes that point to one canonical target;
- verified links to schemas, contracts, fixtures, tests, validators, policies, and workflows;
- historical context clearly labeled as lineage rather than current implementation.

Any proposal to add payloads or executable code changes the lane's mutation and authority behavior. Treat it as a material placement decision, not ordinary documentation maintenance.

[Back to top](#top)

---

<a id="what-is-prohibited"></a>

## What Is Prohibited

Do not place or generate these under `schemas/tests/` while the current boundary remains in force:

- canonical or compatibility `.schema.json` definitions;
- semantic contract prose that belongs under `contracts/`;
- valid, invalid, edge, golden, expected-error, or expected-output payloads;
- executable tests, shared assertions, test runners, or test configuration;
- validator, generator, migration, runtime, package, API, UI, connector, pipeline, or watcher code;
- real source exports, production records, credentials, private endpoints, or sensitive-domain details;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED lifecycle material;
- SourceDescriptors, EvidenceBundles, receipts, proofs, review records, release manifests, correction notices, withdrawal notices, or rollback cards;
- generated validation reports, coverage output, logs, caches, compiled output, or documentation previews;
- policy decisions, rights approvals, sensitivity approvals, review approvals, release decisions, or publication claims.

Also prohibited are claims that a directory name, README, `.gitkeep`, schema, fixture, test, validator, workflow, green check, or merge proves semantic truth, complete coverage, production use, public safety, or governed release.

[Back to top](#top)

---

<a id="inputs-outputs-writers-and-consumers"></a>

## Inputs, Outputs, Writers, and Consumers

### Inputs

- adopted Directory Rules and accepted placement ADRs;
- the current `schemas/` root contract;
- current tracked tree and child README evidence;
- current fixture, test, validator, and workflow source;
- verified migration, compatibility, correction, or retirement decisions.

### Outputs

This lane produces human-readable navigation and boundary guidance only. It emits no schema instance, fixture, test result, validation report, receipt, proof, policy decision, lifecycle record, release object, build artifact, deployment, or public payload.

### Permitted writers

- contributors through reviewed Git changes;
- repository automation only if a separately reviewed change defines a reproducible documentation-generation source and edit policy.

Current CI is read-only for this lane. No connector, watcher, pipeline, validator, test runner, runtime service, model, or public client is granted write authority here.

### Consumers

- maintainers navigating historical schema-test paths;
- documentation, link, metadata, and document-graph checkers;
- migration or topology review that needs to classify the compatibility lane.

A reference is not a writer, and a path-filtered workflow trigger is not a content consumer.

[Back to top](#top)

---

<a id="non-effects-and-trust-boundary"></a>

## Non-Effects and Trust Boundary

Editing this README does not:

- adopt or supersede an ADR;
- make `schemas/tests/` canonical, executable, fixture-bearing, or production-ready;
- validate a schema or classify an instance as valid or invalid;
- change validator selection, fixture polarity, test behavior, or CI requirements;
- admit a source, resolve evidence, approve policy, clear rights, or reduce sensitivity;
- move an object through the KFM lifecycle;
- create a receipt, proof, review, release, correction, rollback, or publication decision;
- deploy code, activate a service, publish data, or widen public access.

The lane is repository-public documentation. All prose, examples, command output, issue links, and future migration notes must therefore exclude secrets, private endpoints, restricted payloads, living-person data, DNA/genomic material, precise protected locations, private-land linkages, culturally restricted information, and critical-infrastructure vulnerability details.

[Back to top](#top)

---

<a id="exposure-mutation-retention-and-storage"></a>

## Exposure, Mutation, Retention, and Storage

| Concern | Current rule |
| --- | --- |
| Exposure | Public repository documentation; no sensitive or source-restricted material. |
| Mutation | Reviewed Git history only; one canonical writer per retained compatibility document. |
| Retention | Retain while verified navigation, migration, or audit value exists; path age alone is not a retention rule. |
| Physical storage | Small Markdown and empty-directory sentinels only under the current posture. |
| Generation | None established; any generated mirror must declare source, generator, digest, and edit policy. |
| Caches and outputs | Never tracked here. |
| Deletion | Requires consumer search, child-path review, link repair, compatibility classification, and rollback evidence. |
| Renaming | Requires exact old-to-new mapping and review of path filters, imports, links, registries, and external consumers. |

No symlink, submodule, generated copy, or external reference may hide a second writable authority behind this path.

[Back to top](#top)

---

<a id="compatibility-and-migration-posture"></a>

## Compatibility and Migration Posture

The current finite placement result is **MIGRATE-OR-RETAIN DECISION HELD**:

- the lane exists and is documented;
- its payload and executable roles are empty;
- current canonical responsibilities are established elsewhere;
- verified consumers requiring the nested `valid/` and `invalid/` path shape have not been exhaustively established;
- no accepted migration or retirement decision was reviewed in this update.

Until that decision is made:

1. keep the lane documentation-only;
2. send all new schema, fixture, test, and validator work to the current responsibility roots;
3. do not duplicate a canonical artifact here;
4. treat child names as compatibility navigation, not implementation commitments;
5. repair links and metadata when current responsibility surfaces change;
6. record any verified consumer before deleting or renaming a path.

### Requirements for a future migration or retirement

- exact old and target paths;
- authority basis and decision class;
- tracked writer and consumer inventory;
- object-family and identity mapping where payloads are involved;
- single-write rule and any bounded dual-read window;
- link, workflow-filter, registry, import, and documentation repair plan;
- validation evidence and negative checks;
- owner, reviewers, start state, exit criteria, and expiry where applicable;
- correction and rollback procedure.

A tombstone README may preserve navigation after retirement. It must not retain a live writable copy of migrated authority.

[Back to top](#top)

---

<a id="validation-and-negative-checks"></a>

## Validation and Negative Checks

### Inspect this compatibility lane

```bash
# Deterministic tracked-content inventory.
find schemas/tests -type f -print | LC_ALL=C sort

# These commands should print nothing under the current posture.
find schemas/tests -type f \
  \( -name '*.json' -o -name '*.schema.json' -o -name '*.py' \
     -o -name '*.js' -o -name '*.ts' -o -name '*.sh' \) \
  -print | LC_ALL=C sort
```

Review any nonempty second result as material drift. Do not silently bless it because it already exists on a branch.

### Run current schema validation surfaces

```bash
# Registry identity and selected commands.
python tools/validate_all.py --list

# Full registered validator profile.
python tools/validate_all.py --profile full

# Historical compatibility entrypoint used by the Makefile.
make schemas

# Executable schema and contract test roots.
python -m pytest -q tests/schemas tests/contracts

# Aggregate validators plus the executable test roots.
make validate
```

Run the smallest relevant command first, then the dependency-closed aggregate when the change affects shared schema, fixture, validator, or workflow behavior. A documentation-only change still requires Markdown, local-link, metadata, and hosted exact-head review.

### Required negative assertions

- no schema or fixture payload is introduced under this lane;
- no executable test or validator source is introduced under this lane;
- no command uses `|| true`, broad exception swallowing, or empty-case success as evidence;
- invalid fixtures are rejected for the reviewed reason, not merely by any nonzero exit;
- valid fixtures pass without network, credential, time, randomness, or service dependence unless explicitly governed;
- no validation path writes lifecycle, receipt, proof, release, or published material;
- no documentation claim upgrades a proposal, placeholder, or workflow definition into accepted or operational status.

[Back to top](#top)

---

<a id="ci-and-execution-surface"></a>

## CI and Execution Surface

The current [`schema-validation` workflow](../../.github/workflows/schema-validation.yml) is the main orchestration evidence relevant to this lane.

| Workflow step | Confirmed behavior | Boundary |
| --- | --- | --- |
| Trigger | Pull requests, pushes to `main`, and dispatch; `schemas/**` changes are in scope | Triggering on this README does not consume it as a fixture or executable test. |
| Inventory | Parses JSON under `schemas/`; meta-validates `*.schema.json`; checks canonical v1 Draft 2020-12 and unique `$id` values | This compatibility lane currently contributes no JSON. |
| Fixture preflight | Pins eight fixture-backed compatibility validators and requires nonempty valid/invalid lanes with reviewed rejection expectations | Those payloads live under `fixtures/`, not `schemas/tests/`. |
| Aggregate validation | Runs `make schemas`, which delegates through the compatibility runner to the registry-driven `full` profile | The current full profile contains ten validators, including workflow-security and repository-topology guardrails. |
| Executable tests | Runs `python -m pytest -q tests/schemas tests/contracts` | Assertions live under `tests/`. |
| Output | Process output and job summary only | No governed ValidationReport, receipt, proof, policy decision, release object, or published artifact is emitted. |

The historical `RUNNER_VALIDATORS` export intentionally includes only full-profile validators carrying `--fixtures`; the current full registry contains additional repository guardrails. Do not confuse the eight fixture-backed inventory with the complete ten-validator profile.

Workflow source proves configured intent. Only the exact-head run conclusion proves that a particular revision executed successfully, and even a green run remains bounded validation evidence rather than semantic, policy, evidence, review, release, or publication authority.

[Back to top](#top)

---

<a id="contributor-workflow"></a>

## Contributor Workflow

### Documentation-only maintenance

1. Pin current `main` and the target blob.
2. Search open pull requests and recent target history.
3. Verify the direct-child tree and the current canonical routing surfaces.
4. Edit only this README when behavior and placement do not change.
5. Preserve the exact path, document ID, H1, compatibility posture, and local anchors.
6. Validate Markdown, metadata, local links, anchors, and sensitive-content posture.
7. Open a focused draft PR and record any inherited CI failure separately from head-specific defects.

### Proposed payload or executable change

Stop and perform placement review before writing. At minimum:

1. identify the object or test family and its current owner;
2. explain why `fixtures/`, `tests/`, or `tools/validators/` is insufficient;
3. inventory writers, readers, path filters, links, registries, and generated outputs;
4. determine whether an ADR or migration is required;
5. define single-write, compatibility, correction, and rollback behavior;
6. include deterministic positive and negative evidence;
7. obtain schema, fixture, test, validator, security, and documentation review appropriate to the change.

Do not mix a new authority decision with its dependent structural implementation in one batch.

[Back to top](#top)

---

<a id="review-and-escalation"></a>

## Review and Escalation

`.github/CODEOWNERS` currently routes `/schemas/` changes to `@bartytime4life`. That is a GitHub review route, not proof of independent approval or accepted stewardship.

| Change | Minimum review burden |
| --- | --- |
| Typo, link, or non-semantic wording repair | Schema-path owner route plus documentation review |
| Boundary or routing clarification | Schema, fixture, test, validator, and documentation perspectives |
| New fixture or executable content under this lane | Architecture/placement, schema, fixture, test, validator, security, and affected domain review |
| Rename, move, mirror, deprecation, or retirement | Verified consumers, migration plan, compatibility checks, correction, and rollback review |
| Rights-, sensitivity-, source-, evidence-, or release-significant change | Independent policy/trust review in addition to technical review |

Escalate rather than guess when:

- an accepted ADR and current repository behavior disagree;
- a verified tool consumes this path as more than documentation;
- a child lane contains unexpected payload or executable bytes;
- a proposed cleanup would break a path filter, import, registry, generated receipt, or external consumer;
- validation requires live network, credentials, restricted data, or public-side effects;
- owners, required checks, or rollback responsibility cannot be verified.

[Back to top](#top)

---

<a id="correction-rollback-and-retirement"></a>

## Correction, Rollback, and Retirement

### Documentation rollback

Before merge, close the draft PR and abandon its scoped branch.

After merge, use a focused reviewed revert or restore the immediate v0.1 blob:

```text
b6c2c6d44fcefbdf6ab9e452b1c09326563a4c8e
```

Do not roll back by changing schemas, fixtures, tests, validators, workflows, or topology baselines unless those bytes were part of the reviewed dependency closure.

### Incorrect routing claim

1. mark the affected statement as held or conflicted;
2. pin the contradictory repository evidence;
3. identify the actual writer and consumer;
4. correct this README and every directly dependent link;
5. preserve the prior claim in Git history and the PR record;
6. verify that no parallel writable authority remains.

### Retirement

Retire the lane only after proving:

- zero payload and executable ownership here;
- zero required consumers of the old path shape, or an accepted compatibility plan;
- child link and workflow-filter repair;
- no generated or machine registry dependency;
- a reversible deletion or tombstone strategy;
- reviewed correction behavior if a missed consumer is discovered.

[Back to top](#top)

---

<a id="open-verification-items"></a>

## Open Verification Items

| Item | Current disposition | Resolution evidence |
| --- | --- | --- |
| Long-term retention versus retirement of `schemas/tests/` | **NEEDS VERIFICATION** | Consumer inventory and reviewed placement/migration decision |
| Need for every nested domain compatibility directory | **NEEDS VERIFICATION** | Link, workflow, import, registry, and external-consumer search per child |
| Automated prohibition on payload or executable drift here | **NOT ESTABLISHED** | Focused topology or path-policy test with positive and negative fixtures |
| Independent schema/test/fixture/validator stewardship | **NEEDS VERIFICATION** | Accepted responsibility assignments and enforced review rules |
| Required-check status of schema-validation and related workflows | **NEEDS VERIFICATION** | Current repository ruleset evidence |
| Exact-head success for this revision | **NEEDS VERIFICATION until hosted run completes** | GitHub Actions result for the PR head |

These are bounded review items, not permission to add content, declare the lane canonical, or weaken the current separation.

[Back to top](#top)

---

<a id="review-checklist"></a>

## Review Checklist

- [ ] Exact target path, blob, base commit, and competing PR search are recorded.
- [ ] The direct-child map lists only `valid/` and `invalid/`.
- [ ] Full subtree counts remain nineteen READMEs and fourteen `.gitkeep` files, or any drift is explicitly reconciled.
- [ ] No schema, fixture payload, executable test, validator, generated output, lifecycle object, or release object is introduced here.
- [ ] Canonical schema, fixture, test, validator, policy, data, and release routes remain distinct.
- [ ] ADR-0001 and ADR-0002 are not described as accepted.
- [ ] Workflow trigger scope is not confused with content ownership or runtime success.
- [ ] Commands are fail-closed and no-network by default.
- [ ] Public documentation contains no secret, restricted, private, or sensitive detail.
- [ ] Links, anchors, metadata, Markdown, and exact remote bytes are validated.
- [ ] Any generated authoring receipt is either included within authorized scope or its omission is explicit.
- [ ] The PR remains draft and no merge, release, deployment, or publication occurs.

[Back to top](#top)

---

## No-Loss and Change Ledger

| v0.1 element | v0.2 disposition |
| --- | --- |
| Parent compatibility-index purpose | Preserved and grounded in current root authority. |
| Valid and invalid child navigation | Preserved as the only direct-child map. |
| Non-ownership boundary | Preserved and expanded across every responsibility root. |
| Child inventory | Preserved at direct-child level; deeper counts summarized without taking child ownership. |
| Correct nearby lanes | Preserved as an evidence-backed responsibility-routing matrix. |
| Belongs and prohibited lists | Preserved, tightened, and aligned with current empty-tree evidence. |
| Compatibility rules | Preserved and extended with single-write, migration, and retirement requirements. |
| Provisional `pytest ... \|\| true` command | Removed; replaced with current fail-closed repository commands. |
| Unknown CI consumer question | Resolved: schema-validation is path-triggered, but cases and assertions come from `fixtures/` and `tests/`. |
| Unknown validator command question | Resolved to `tools/validate_all.py`, `make schemas`, `pytest`, and `make validate`, with scope limits. |
| Placement uncertainty | Refined to a held retain-or-retire compatibility decision; no authority promotion. |
| Test/publication boundary | Preserved and strengthened. |
| Correction and rollback | Added with exact prior blob. |

[Back to top](#top)

---

<a id="references"></a>

## References

### Governing and adjacent documentation

- [Schemas root contract](../README.md)
- [Contracts root](../../contracts/README.md)
- [Fixtures root](../../fixtures/README.md)
- [Tests root](../../tests/README.md)
- [Executable schema tests](../../tests/schemas/README.md)
- [Executable contract tests](../../tests/contracts/README.md)
- [Validator root](../../tools/validators/README.md)
- [Policy root](../../policy/README.md)
- [Data root](../../data/README.md)
- [Release root](../../release/README.md)
- [Contributing guide](../../CONTRIBUTING.md)
- [CODEOWNERS](../../.github/CODEOWNERS)

### Decisions and doctrine

- [ADR-0001 — proposed schema home](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md)
- [ADR-0002 — contracts versus schemas split](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md)
- [ADR-0029 — accepted Directory Governance Standard v2](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Adopted Directory Rules](../../docs/doctrine/directory-rules.md)

### Executable surfaces

- [Schema-validation workflow](../../.github/workflows/schema-validation.yml)
- [Repository Makefile](../../Makefile)
- [Canonical aggregate entrypoint](../../tools/validate_all.py)
- [Validator registry](../../tools/validators/validator_registry.json)
- [Compatibility aggregate entrypoint](../../tools/validators/_common/run_all.py)

---

## Change Log

| Version | Date | Change |
| --- | --- | --- |
| `v0.2` | 2026-08-13 | Repository-grounded modernization: confirmed the documentation-only tree, separated compatibility navigation from schemas, fixtures, executable tests, validators, CI, policy, lifecycle, and release authority; replaced provisional commands and stale open questions; added current execution mapping, contribution, migration, correction, rollback, review, and no-loss guidance; changed documentation only. |
| `v0.1` | 2026-07-04 | Established the parent compatibility index, valid/invalid child inventory, routing boundaries, provisional validation, and open placement questions. |

---

**Last reviewed:** 2026-08-13 against `main@e842898e36c6a49fa32de08f69deb1a26cc46bfc` · **Role:** compatibility documentation only · **Executable tests:** `tests/` · **Fixtures:** `fixtures/` · **Validators:** `tools/validators/` · **Publication:** none · **Path:** `schemas/tests/README.md` · [Back to top](#top)
