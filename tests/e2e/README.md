# `tests/e2e/` — Governed End-to-End Enforceability Root

> Parent boundary for proving that complete KFM request paths preserve evidence, policy, release, correction, rollback, and public-client controls without bypassing the trust membrane or treating a green test as truth or publication.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-e2e-readme
title: tests/e2e/README.md — Governed End-to-End Enforceability Root
type: readme; directory-readme; e2e-test-parent
version: v0.2
status: draft; repository-grounded; agriculture-child-confirmed; no-executable-parent-suite-established
owners: OWNER_TBD — QA steward · E2E steward · Governed API steward · Evidence steward · Policy steward · Release steward · Map/UI steward · Security reviewer · Domain stewards · Docs steward
created: NEEDS VERIFICATION
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doctrine; tests; e2e; governed-composition; no-network-default; synthetic-only; no-publication
current_path: tests/e2e/README.md
truth_posture: CONFIRMED target README, tests root, Agriculture child v0.2, bounded search showing only the parent and Agriculture child under tests/e2e, checked absence of parent conftest.py, test_smoke.py, and pytest.ini, TODO-only e2e-smoke workflow, and Makefile test target limited to tests/schemas plus tests/contracts / PROPOSED child admission, deterministic harness, no-network enforcement, zero-collection failure, side-effect guards, correction and rollback cases, substantive CI, and promotion blocking / UNKNOWN exhaustive inventory, dynamic collection, public-surface adapters, pass rates, runtime, flakes, and release-gate dependency / NEEDS VERIFICATION owners, runner, fixture split, outcome vocabularies, network denial, artifact retention, and CI ownership
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 01026cd58b1e687c4f8fa3363229b9857613102b
  target_prior_blob: efbd7c6132a8920d6615c897a59b2b0009b5bdc9
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    tests_root_readme: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
    agriculture_child_readme: a9500ca93564adddab29dfc7e1edceac4d36dc57
    e2e_smoke_workflow: df1130aa8a2e8dc255e97cf0a9ea7f66b8dd99e3
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
  direct_lane_files_confirmed:
    - tests/e2e/README.md
    - tests/e2e/agriculture/README.md
  checked_absent_paths:
    - tests/e2e/conftest.py
    - tests/e2e/test_smoke.py
    - tests/e2e/pytest.ini
related:
  - ../README.md
  - agriculture/README.md
  - ../../fixtures/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../release/
  - ../../runtime/
  - ../../apps/
  - ../../.github/workflows/e2e-smoke.yml
  - ../../Makefile
notes:
  - "v0.2 replaces a speculative future tree with a commit-pinned current-state boundary."
  - "The e2e-smoke workflow is echo-only and cannot establish coverage."
  - "The Makefile test target excludes tests/e2e."
  - "Runtime outcomes are assertions, not pytest statuses."
  - "This revision changes documentation only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Children: Agriculture only" src="https://img.shields.io/badge/children-Agriculture__only-lightgrey">
  <img alt="Executable suite: not established" src="https://img.shields.io/badge/executable__suite-not__established-orange">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Publication: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [E2E definition](#what-counts-as-end-to-end) · [Children](#child-lane-admission-and-index) · [Case contract](#minimum-e2e-case-contract) · [Harness](#harness-fixtures-security-and-side-effects) · [Outcomes](#test-results-and-runtime-outcomes) · [Correction](#correction-withdrawal-and-rollback) · [Runner](#runner-ci-and-promotion-boundary) · [Directory map](#directory-map) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Evidence:** `main@01026cd58b1e687c4f8fa3363229b9857613102b`
> **Prior blob:** `efbd7c6132a8920d6615c897a59b2b0009b5bdc9`
> **Confirmed files:** this README and `agriculture/README.md`
> **Absent at checked paths:** `conftest.py`, `test_smoke.py`, `pytest.ini`
> **Workflow:** `e2e-smoke` echoes TODO commands
> **Makefile:** `make test` runs `tests/schemas` and `tests/contracts`, not E2E

`tests/e2e/` is currently a documentation parent. Agriculture is the only confirmed child README. No executable parent test, shared harness, dedicated runner, substantive E2E workflow, pass rate, or promotion dependency is established.

| Capability | Status |
|---|---:|
| Parent README | `CONFIRMED` |
| Agriculture child README | `CONFIRMED` |
| Other child lanes | `NOT ESTABLISHED` |
| Parent harness/config | `NOT FOUND AT CHECKED PATHS` |
| E2E workflow | `TODO-ONLY` |
| Makefile E2E collection | `NOT ESTABLISHED` |
| Network denial | `UNKNOWN` |
| Promotion blocking | `UNKNOWN` |

Truth labels: `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`, `DENY`.

[Back to top](#top)

---

## Purpose

E2E tests prove governed composition across responsibility roots.

```text
synthetic request
  -> governed envelope
  -> identity, source-role, time, schema, and contract checks
  -> EvidenceRef resolution
  -> policy, audience, review, and release checks
  -> governed API / UI / map / export / AI carrier
  -> correction / withdrawal / rollback invalidation
  -> expected finite runtime outcome
```

A passing test means the scoped controls behaved as expected. It does not prove claim truth, source admission, policy approval, release, publication, or production behavior.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Authority home | E2E role |
|---|---|---|
| General enforceability | `tests/` | Canonical test root. |
| Domain-local tests | `tests/domains/<domain>/` | Composed, not duplicated. |
| Meaning | `contracts/` | Tested, not authored here. |
| Shape | `schemas/` | Validated, not defined here. |
| Policy | `policy/` | Exercised, not invented here. |
| Reusable fixtures | `fixtures/` | Referenced, not duplicated by default. |
| Runtime/API/UI/map | accepted implementation roots | Exercised through safe adapters. |
| Evidence/proof | governed trust roots | Referenced with synthetic or released-safe IDs. |
| Release/correction/rollback | `release/` | Tested, never approved here. |
| CI | `.github/workflows/` | Calls tests; green status is not authority. |

This lane must not become a shadow application, policy engine, registry, lifecycle store, proof store, or release system.

[Back to top](#top)

---

## Confirmed current state

```text
tests/e2e/
├── README.md
└── agriculture/
    └── README.md
```

The Agriculture child is repository-grounded but README-only. It defines aggregate-only, no-network, evidence, policy, release, correction, rollback, and public-surface expectations without claiming executable coverage.

Current workflow:

```yaml
- echo TODO spin-up-mock-runtime
- echo TODO run-e2e-smoke
```

Current Makefile:

```make
test:
	python -m pytest tests/schemas tests/contracts -q
```

A green echo-only workflow is not E2E proof.

[Back to top](#top)

---

## What counts as end-to-end

A case belongs here when its main assertion crosses multiple roots through a governed interface.

Suitable cases:

- request → evidence → policy → release → governed response;
- missing evidence → `ABSTAIN`;
- denied rights or sensitivity → `DENY`;
- unreleased object blocked from public output;
- correction or withdrawal invalidates prior output;
- rollback restores an identified target;
- cross-lane response preserves ownership, source role, time, and sensitivity;
- deliberate network access is blocked.

One-function, schema, contract, policy, validator, domain-local, component, and live-source tests belong in narrower lanes.

Direct internal-store access followed by public rendering is a trust-membrane bypass, not valid E2E proof.

[Back to top](#top)

---

## Child-lane admission and index

| Child | Current maturity |
|---|---:|
| [`agriculture/`](agriculture/README.md) | `README-ONLY / EXECUTABLE SUITE NOT ESTABLISHED` |

Do not create `tests/e2e/<name>/` merely because a topic exists. A new child needs:

- a real composed scenario;
- an accountable owner;
- verified placement;
- approved synthetic fixtures;
- an accepted harness;
- positive and fail-closed cases;
- no-network default or separately governed integration profile;
- failure on zero collection;
- CI, cleanup, and rollback plans;
- explicit cross-domain ownership where relevant.

A broad `cross-domain/` child remains `PROPOSED / NEEDS VERIFICATION`.

[Back to top](#top)

---

## Minimum E2E case contract

```yaml
case_id: stable-id
owner: named-owner
participating_roots: []
participating_domains: []
fixture_refs: []
expected_runtime_outcome: ANSWER | ABSTAIN | DENY | ERROR
expected_reason_code: accepted-code
evidence_resolution: required | not-applicable
policy_expectation: allow | restrict | deny | hold | error
release_expectation: required-state | not-applicable
forbidden_claims: []
forbidden_fields: []
network_allowed: false
governed_root_writes_allowed: false
correction_case_ref: null
withdrawal_case_ref: null
rollback_case_ref: null
deterministic: true
zero_collection_fails: true
```

This shape is `PROPOSED`. A complete case must state forbidden behavior such as source-role upcast, aggregate-to-exact collapse, unreleased output, secret leakage, stale corrected output, network success, or governed-root mutation.

[Back to top](#top)

---

## Harness, fixtures, security, and side effects

An accepted harness may use an in-process adapter, local subprocess, loopback mock service, static envelope runner, or browser harness. It must be deterministic, isolated, documented, and unable to fall back to live services.

Default tests must block or detect DNS, sockets, HTTP clients, provider SDKs, map services, geocoders, graphs, live connectors, and external subprocesses. Include a deliberate blocked-attempt case.

Fixtures must be synthetic, reviewable, minimized, marked as test data, and safe to retain. Reusable payloads belong under `fixtures/`.

Do not use real secrets, production logs, living-person private data, DNA/genomic material, protected locations, sensitive infrastructure, private farm/operator records, or real release/proof artifacts.

Tests must not write to canonical `data/`, registry, receipt, proof, contract, schema, policy, or release roots. Use isolated temporary directories and verify repository state before and after execution.

[Back to top](#top)

---

## Test results and runtime outcomes

Keep vocabularies separate:

| Layer | Examples |
|---|---|
| Test process | pass, fail, skip, error, zero-collected |
| Runtime response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Policy decision | allow, restrict, deny, hold, error |
| Workflow state | proposed, validated, active, suspended, retired |
| Release state | candidate, released, corrected, withdrawn, superseded, rolled back |

A test passes when the observed runtime outcome matches the expected governed behavior. `DENY` is not itself a test failure.

Required tests must not silently skip because a fixture, dependency, harness, or environment variable is absent. A runner advertised as coverage must fail when zero tests are collected.

[Back to top](#top)

---

## Correction, withdrawal, and rollback

E2E coverage is incomplete when it tests only initial success.

- Correction must identify the prior object, invalidate stale carriers, preserve lineage, and avoid deleting audit history.
- Withdrawal must stop ordinary public access and remove dependent serving.
- Rollback must identify an eligible prior target, record the transition, update dependent carriers, and remain distinct from deletion.
- Partial invalidation fails closed.

[Back to top](#top)

---

## Runner, CI, and promotion boundary

No accepted parent runner exists. A candidate future command is:

```bash
python -m pytest tests/e2e -q
```

It remains `PROPOSED / NEEDS VERIFICATION`.

Before activation, verify collection, zero-test failure, network denial, fixtures, harness, cleanup, bounded skips, meaningful exit codes, and sanitized artifacts.

A substantive workflow must install declared dependencies, run collection, start the approved harness, enforce no-network, execute the exact suite, fail on missing fixtures or zero collection, clean up processes, and report counts and duration.

An echo-only job must not satisfy release or promotion gates. Promotion blocking requires accepted ownership, executable cases, negative coverage, stable CI, acceptable flake rate, and explicit gate dependency.

[Back to top](#top)

---

## Directory map

### Confirmed

```text
tests/e2e/
├── README.md
└── agriculture/
    └── README.md
```

### Proposed support

```text
tests/e2e/
├── conftest.py
├── _harness/
├── _assertions/
├── _fixtures/
└── <accepted-child>/
    ├── README.md
    └── test_*.py
```

Do not create these merely to appear mature. Every new path needs ownership, verified placement, an actual consumer, fixture and cleanup rules, no duplicate authority, and rollback.

Production code, contracts, schemas, policy, reusable fixtures, source descriptors, lifecycle data, receipts, proofs, releases, public artifacts, secrets, and real sensitive data do not belong here.

[Back to top](#top)

---

## Definition of done

### This revision

- [x] Records the parent and Agriculture child as the confirmed bounded inventory.
- [x] Records absent parent harness/config paths.
- [x] Records the TODO-only workflow and Makefile exclusion.
- [x] Replaces speculative child directories with admission rules.
- [x] Separates test, runtime, policy, workflow, and release vocabularies.
- [x] Defines no-network, fixture, side-effect, and zero-collection controls.
- [x] Preserves evidence, policy, release, correction, and rollback boundaries.
- [x] Changes documentation only.
- [ ] Record repository-native CI after PR creation.

The parent is not operationally complete until owners, child naming, harness, executable tests, fixture homes, network denial, zero-collection failure, side-effect guards, correction/rollback coverage, substantive CI, metrics, promotion dependency, and integration rollback are verified.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `E2E-001` | What is the accepted shared harness? | `UNKNOWN` |
| `E2E-002` | Is the bounded inventory complete? | `NEEDS VERIFICATION` |
| `E2E-003` | Are tests dynamically collected elsewhere? | `UNKNOWN` |
| `E2E-004` | What child naming and ownership rule is accepted? | `NEEDS VERIFICATION` |
| `E2E-005` | What fixture split is canonical? | `NEEDS VERIFICATION` |
| `E2E-006` | What envelope, outcome, and reason-code contracts are accepted? | `NEEDS VERIFICATION` |
| `E2E-007` | How is no-network enforced? | `UNKNOWN` |
| `E2E-008` | Which public-surface adapters are safe? | `UNKNOWN` |
| `E2E-009` | How are cross-domain cases owned? | `NEEDS VERIFICATION` |
| `E2E-010` | How do correction, withdrawal, and rollback propagate? | `UNKNOWN` |
| `E2E-011` | What is the accepted runner, and does zero collection fail? | `UNKNOWN` |
| `E2E-012` | When will `e2e-smoke` become substantive? | `UNKNOWN` |
| `E2E-013` | Which E2E jobs block promotion? | `UNKNOWN` |
| `E2E-014` | What artifacts and retention are allowed? | `NEEDS VERIFICATION` |
| `E2E-015` | What are current counts, pass rates, runtime, and flake rate? | `UNKNOWN` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| prior blob `efbd7c61…` | `CONFIRMED` | Existing parent boundary. | Executable coverage. |
| Directory Rules `2affb080…` | `CONFIRMED DOCTRINE` | Tests root, authority separation, reversibility. | Current behavior. |
| tests root `5614de99…` | `CONFIRMED ROOT CONTRACT` | Tests are enforceability proof. | E2E runner. |
| Agriculture child `a9500ca9…` | `CONFIRMED DOCUMENTATION` | README-only maturity and E2E requirements. | Executable Agriculture E2E. |
| workflow `df1130aa…` | `CONFIRMED TODO SCAFFOLD` | Workflow exists and echoes TODO. | Test execution. |
| Makefile `4dc8cf63…` | `CONFIRMED` | Current test target excludes E2E. | E2E collection. |
| bounded search/path checks | `CONFIRMED BOUNDED RESULT` | Parent, child, and absent checked files. | Exhaustive history or dynamic collection. |

Current test code, collection output, workflow commands, logs, and generated reports outrank README plans for implementation claims.

[Back to top](#top)

---

## Maintainer note

Do not create child directories, empty tests, or green echo workflows to make the repository look mature. Add one complete scenario at a time with an accepted harness, synthetic fixtures, negative states, no-network enforcement, no governed side effects, meaningful failure, and an explicit owner.

A green test that bypasses the trust membrane is not E2E governance. A green job that collects zero tests is not coverage. A green workflow that echoes TODO is not proof.

<p align="right"><a href="#top">Back to top</a></p>
