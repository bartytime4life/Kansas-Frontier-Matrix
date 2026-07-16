# `tests/invalid/` — Governed Cross-Cutting Fail-Closed Compatibility Lane

> Repository-grounded boundary for cross-cutting negative tests whose primary purpose is to prove that unsupported, unsafe, malformed, stale, conflicted, forbidden, or governance-incomplete paths fail closed without creating a second schema, policy, fixture, evidence, lifecycle, release, or implementation authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-invalid-readme
title: tests/invalid/README.md — Governed Cross-Cutting Fail-Closed Compatibility Lane
type: readme; directory-readme; negative-test-compatibility-boundary; fail-closed-routing-index
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; compatibility-utility-lane; specific-negative-tests-confirmed-elsewhere; no-dedicated-invalid-suite-established
owners: OWNER_TBD — QA steward · Test steward · Security steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Runtime steward · Release steward · Domain stewards · Docs steward
created: 2026-07-06
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doctrine; tests; invalid; fail-closed; negative-tests; compatibility-lane; synthetic-only; no-network-default; no-parallel-authority; no-publication
current_path: tests/invalid/README.md
truth_posture: CONFIRMED target README, canonical tests root, tests/valid sibling README, tests/fixtures parent README, root invalid-fixture README, schema invalid-fixture test, policy non-publisher test, Explorer Web adapter-boundary test, governed-API boundary tests, Makefile test target limited to tests/schemas plus tests/contracts, TODO-only deny-test workflow, checked absence of tests/invalid/conftest.py, tests/invalid/test_invalid.py, and tests/invalid/pytest.ini, and bounded search that did not establish direct executable coverage / PROPOSED compatibility-lane retention rule, routing matrix, minimum negative-case contract, positive-control requirement, non-leaking denial assertions, deterministic no-network harness, zero-collection failure, correction and rollback cases, CI graduation gates, and deprecation path / UNKNOWN exhaustive recursive lane inventory, ignored or generated files, dynamic collection, complete invalid fixture inventory, accepted shared runner, current pass rates, coverage, mutation score, flake rate, and promotion dependency / NEEDS VERIFICATION owners, whether this compatibility lane should be retained, canonical fixture split, accepted failure and reason vocabularies, network-denial mechanism, sensitive-fixture review, artifact retention, CI ownership, and migration of future cases into specific lanes
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: a0bbd85cd2a953654bd131f6d1ef7fbe3ef9a430
  target_prior_blob: f3b7d281ab9895f7bb23ac76f8efffdb147bcd0a
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    tests_root_readme: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
    valid_sibling_readme: fb405f82578d70538d3f54d05662b258b39f3303
    tests_fixtures_readme: 2d0147e85eae86f687e85c5bea0d3e61f9c3a8f7
    root_invalid_fixtures_readme: 4cf897379d49eceb2b14a69d3ce1a1c13ed19aa9
    schema_invalid_fixture_test: b04342cc034d7f1cc554e155fdd02d6e972976e6
    pipeline_connector_non_publisher_test: c6164787bc848eb2347c347af203d76afae37a2b
    explorer_web_adapter_boundary_test: 97d44069b0a5ab4a82b1e1fc48665e905c08a287
    governed_api_boundary_test: d84ccd2a93bdf786e8fca11ee596dcc47e543fc2
    deny_test_workflow: d2dd40c274d55a33488b7f601ee33440911431b9
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    cross_domain_readme: cdf514e6a972be821f5f10d27d504aa3a5d03131
  direct_lane_files_confirmed:
    - tests/invalid/README.md
  checked_absent_paths:
    - tests/invalid/conftest.py
    - tests/invalid/test_invalid.py
    - tests/invalid/pytest.ini
  bounded_inventory_note: repository search and representative path checks did not establish a direct executable suite under tests/invalid; this is not proof against ignored, generated, historical, branch-local, dynamically collected, or external files
related:
  - ../README.md
  - ../valid/README.md
  - ../fixtures/README.md
  - ../schemas/
  - ../contracts/
  - ../policy/
  - ../api/
  - ../release/
  - ../runtime_proof/
  - ../domains/
  - ../cross_domain/README.md
  - ../../fixtures/invalid/README.md
  - ../../apps/governed-api/tests/test_boundary_guards.py
  - ../../docs/doctrine/directory-rules.md
  - ../../.github/workflows/deny-test.yml
  - ../../Makefile
notes:
  - "v0.2 replaces a planning-heavy catch-all guide with a commit-pinned compatibility and routing boundary."
  - "The direct lane is README-only at the bounded snapshot."
  - "Executable fail-closed coverage exists in specific schema, policy, and governed-API lanes and must not be relabeled as tests/invalid coverage."
  - "The Makefile test target does not collect tests/invalid, and deny-test is an echo-only workflow scaffold."
  - "This revision changes documentation only and creates no test, fixture, schema, contract, policy, workflow behavior, data, receipt, proof, release object, or public surface."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Placement: compatibility utility" src="https://img.shields.io/badge/placement-compatibility__utility-orange">
  <img alt="Failure posture: fail closed" src="https://img.shields.io/badge/failure-fail__closed-critical">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Publication authority: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Routing](#placement-and-routing-law) · [Case contract](#minimum-negative-case-contract) · [Failure classes](#failure-classification) · [Controls](#positive-controls-and-non-tautology) · [Fixtures](#fixtures-test-data-and-sensitive-material) · [Security](#network-security-and-side-effects) · [Outcomes](#test-results-runtime-outcomes-and-policy-decisions) · [Leakage](#non-leaking-failure-responses) · [Lifecycle](#lifecycle-release-correction-and-rollback) · [Runner](#runner-ci-and-promotion-boundary) · [Migration](#migration-deprecation-and-rollback) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Evidence snapshot:** `main@a0bbd85cd2a953654bd131f6d1ef7fbe3ef9a430`  
> **Prior target blob:** `f3b7d281ab9895f7bb23ac76f8efffdb147bcd0a`  
> **Direct lane:** `tests/invalid/README.md` only at the bounded snapshot  
> **Checked absent:** `conftest.py`, `test_invalid.py`, `pytest.ini`  
> **Makefile:** `make test` runs `tests/schemas` and `tests/contracts`, not this lane  
> **Workflow:** `deny-test` checks out the repository and echoes three TODO commands

`tests/invalid/` is currently a documented **compatibility and utility lane**, not an established executable suite.

The repository does contain substantive negative tests, but they live under the responsibility that owns the assertion:

- schema fixture rejection under `tests/schemas/`;
- non-publisher and adapter boundaries under `tests/policy/`;
- route, method, import, and internal-store boundaries under `apps/governed-api/tests/`.

Those tests are evidence of specific negative coverage. They are not evidence that `tests/invalid/` collects tests, has a runner, or blocks promotion.

| Capability | Status | Safe conclusion |
|---|---:|---|
| README | `CONFIRMED` | This routing boundary exists. |
| Direct executable module | `NOT ESTABLISHED` | Bounded search and checked paths did not establish one. |
| Lane-local harness/config | `NOT FOUND AT CHECKED PATHS` | No independent collection contract was established. |
| Specific negative tests elsewhere | `CONFIRMED` | Schema, policy, and API boundary tests exist. |
| Root invalid-fixture README | `CONFIRMED` | Fixture intent exists; payload inventory remains unverified. |
| Makefile collection | `NOT ESTABLISHED` | Current default test target omits this lane. |
| Deny workflow | `TODO-ONLY` | A green run cannot prove negative behavior. |
| Pass rate / coverage | `UNKNOWN` | No dedicated suite or report was verified. |
| Promotion blocking | `UNKNOWN` | No verified gate depends on this lane. |

Truth labels used here: `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`, and `DENY`.

[Back to top](#top)

---

## Purpose

Use `tests/invalid/` only for **genuinely cross-cutting** negative tests when no more specific test owner can express the assertion without duplication.

A negative test should prove a named unsafe or unsupported condition is rejected, denied, held, narrowed, abstained from, or surfaced as an error according to the contract under test.

It must not prove—or claim to prove—that:

- a source is authoritative;
- a claim is true;
- a fixture is evidence;
- a schema-valid object is admissible;
- a policy decision is approved;
- a release exists;
- publication occurred;
- a rollback was operationally executed;
- the same behavior is deployed in production.

`invalid` is a **test result category**, not an authority category.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Authority home | This lane's role |
|---|---|---|
| Test assertions | `tests/` | May own a cross-cutting assertion after routing review. |
| Machine shape | `schemas/` | Tested, not defined here. |
| Semantic meaning | `contracts/` | Tested, not rewritten here. |
| Policy | `policy/` | Exercised, not invented here. |
| Reusable validators | `tools/validators/` or package owner | Tested, not implemented here. |
| Reusable fixtures | `fixtures/` | Referenced, not duplicated. |
| Test-local fixtures | `tests/fixtures/` | Referenced under the fixture split. |
| Evidence and proof | governed trust-object roots | Synthetic refs only. |
| Lifecycle data | governed `data/` phase roots | Never stored or mutated here. |
| Release and rollback | `release/` | Tested, never approved here. |
| API/UI/runtime | accepted implementation roots | Exercised through bounded interfaces. |
| Cross-domain composition | `tests/cross_domain/` while that placement remains governed/conflicted | Separate classification from invalidity. |

> [!WARNING]
> This lane must not become a second schema, policy, fixture, source, registry, receipt, proof, release, runtime, or data home.

[Back to top](#top)

---

## Confirmed current state

### Direct lane

```text
tests/invalid/
└── README.md
```

The map is bounded, not exhaustive. Ignored, generated, historical, branch-local, or dynamically collected files remain `UNKNOWN`.

### Confirmed negative coverage outside this lane

| Evidence | What it proves | Boundary |
|---|---|---|
| `tests/schemas/test_common_contracts.py` | Invalid contract fixtures must produce schema errors. | Shape only; not semantic or policy proof. |
| `tests/policy/test_pipeline_connector_non_publisher.py` | Connector/pipeline write contexts must not target catalog, published, or release paths. | Static boundary check; not all mutation paths. |
| `tests/policy/test_explorer_web_adapter_boundary.py` | Runtime map imports stay in adapters and UI code omits internal-store literals. | UI code boundary only. |
| `apps/governed-api/tests/test_boundary_guards.py` | Unknown routes, unsupported methods, forbidden imports, route drift, and internal-store references fail. | Scaffold/API boundary; not production deployment. |

Do not copy these tests into this lane merely to centralize “invalid” behavior.

[Back to top](#top)

---

## Placement and routing law

Prefer the most specific responsibility owner.

| Primary assertion | Preferred lane |
|---|---|
| JSON Schema rejection | `tests/schemas/` |
| Contract semantic violation | `tests/contracts/` |
| Policy deny/restrict/hold/abstain | `tests/policy/` |
| Validator rejection | `tests/validators/` or validator package tests |
| Source admission or source-role failure | `tests/source/` or owning connector/domain lane |
| Pipeline transition failure | `tests/pipelines/` or owning pipeline tests |
| Governed API rejection | `tests/api/` or application tests |
| UI trust-state failure | `tests/ui/` |
| Release/correction/rollback failure | `tests/release/` |
| Runtime finite-outcome failure | `tests/runtime_proof/` |
| Domain-owned invalidity | `tests/domains/<domain>/` |
| End-to-end composed failure | `tests/e2e/<owner>/` |
| Multi-domain composition failure | governed cross-domain lane after placement review |
| Truly cross-cutting negative invariant with no specific owner | `tests/invalid/`, if retained |

A test belongs here only when:

1. the invalid condition spans multiple responsibility owners;
2. no existing specific lane can own it cleanly;
3. moving it here avoids—not creates—duplication;
4. its contracts, fixtures, policy, evidence, and release references remain external;
5. ownership and CI collection are explicit.

[Back to top](#top)

---

## Minimum negative-case contract

Every substantive case should declare:

```yaml
case_id: invalid-<stable-id>
owner: <qa-or-domain-owner>
primary_invalid_condition: <one condition>
system_under_test: <verified path or interface>
fixture_ref: <synthetic fixture>
positive_control_ref: <nearby accepted case>
expected_test_result: pass
expected_system_outcome: <validation-error|ABSTAIN|DENY|ERROR|HOLD|RESTRICT>
expected_reason_code: <stable-safe-code>
must_not_emit:
  - <protected field or false claim>
must_not_mutate:
  - <governed root or state>
network: denied
contract_refs: []
schema_refs: []
policy_refs: []
evidence_refs: []
release_refs: []
cleanup: <required cleanup>
```

Rules:

- One primary invalid condition per case.
- Expected failures must be precise enough to catch the wrong rejection.
- Missing expected-error assertions are incomplete coverage.
- A failure for an unrelated reason is not a passing negative test.
- Stable reason codes should be preferred over brittle full-message matching.
- The test must assert forbidden outputs and side effects, not only the returned status.

[Back to top](#top)

---

## Failure classification

| Class | Example | Primary owner |
|---|---|---|
| Shape | missing field, bad enum, wrong version | schema tests |
| Semantic | shape parses but meaning violates contract | contract tests |
| Evidence | unresolved or incomplete EvidenceRef/EvidenceBundle | evidence/runtime/domain tests |
| Citation | missing, stale, mismatched support | citation/evidence tests |
| Source role | contextual source upcast as primary authority | source/domain tests |
| Rights | rights unknown or use forbidden | policy/domain tests |
| Sensitivity | precision or audience unsafe | policy/domain tests |
| Lifecycle | phase skipped or promotion unsupported | pipeline/release tests |
| Trust membrane | direct internal-store or admin shortcut | API/UI/policy tests |
| Runtime | unsupported route/method/provider state | runtime/API tests |
| Release | missing review, manifest, correction, or rollback support | release tests |
| Network | live service or model call in default tests | owning harness tests |
| Leakage | denial or error exposes protected details | API/UI/security tests |

A case may touch several classes, but one primary owner must remain clear.

[Back to top](#top)

---

## Positive controls and non-tautology

A negative suite that rejects everything proves nothing useful.

Trust-bearing negative cases need a nearby positive control demonstrating that:

- a minimally valid case passes the tested boundary;
- changing the intended invalid condition changes the outcome;
- unrelated fields do not accidentally determine the result;
- the rule is selective rather than permanently closed;
- the expected reason code changes when the failure class changes.

Mutation resistance should be considered for high-consequence cases. At minimum, reviewers should ask whether removing or inverting the tested guard would make the test fail.

[Back to top](#top)

---

## Fixtures, test data, and sensitive material

### Fixture homes

| Fixture use | Preferred home |
|---|---|
| Shared cross-cutting invalid example | `fixtures/invalid/` |
| Domain-owned invalid example | `fixtures/domains/<domain>/invalid/` or accepted domain negative lane |
| Test-local invalid data | `tests/fixtures/<owner>/` |
| Minimal scalar/object inline value | test file, when clearly synthetic and reviewable |

### Fixture requirements

Fixtures must be:

- synthetic;
- compact;
- deterministic;
- public-safe;
- clearly marked as test material;
- bound to an expected outcome;
- free of real credentials, private identifiers, exact sensitive locations, and production records.

Sensitive domains—living persons, DNA/genomics, archaeology, rare species, infrastructure, land-title/private joins, and operational security—require transformed canaries and appropriate steward review. Real sensitive data must not enter the default suite.

[Back to top](#top)

---

## Network, security, and side effects

Default negative tests are no-network.

The harness should deny or intercept:

- HTTP/HTTPS clients;
- DNS and sockets;
- live connectors;
- geocoders and tile services;
- model providers;
- cloud SDKs;
- package installation during tests;
- subprocesses that can escape the fixture boundary.

A future active suite must include a deliberate network-attempt case proving the guard is executable. “No network was needed” is weaker than “network access was attempted and blocked.”

Tests must not mutate:

- lifecycle stores;
- source or catalog registries;
- receipt or proof roots;
- policy or contract roots;
- release state;
- public artifacts;
- production caches.

Temporary files must be isolated, declared, and cleaned. Logs and retained reports must be sanitized.

[Back to top](#top)

---

## Test results, runtime outcomes, and policy decisions

Do not collapse vocabularies.

| Layer | Example vocabulary |
|---|---|
| Test runner | pass, fail, skip, xfail, error |
| Validation | valid, invalid, validation error |
| Runtime | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Policy | allow, restrict, hold, deny, abstain, error—only where accepted |
| Workflow | queued, running, succeeded, failed, cancelled |
| Release | candidate, approved, rejected, withdrawn, superseded, rolled back |

A pytest pass can assert that the system returned `DENY`; it does not mean “DENY” is a pytest status. A schema error is not automatically a policy denial. A workflow success is not release approval.

Skips and xfails require a reason, owner, issue, and expiry. Zero collection must fail once this lane is activated.

[Back to top](#top)

---

## Non-leaking failure responses

A failure response is unsafe if it reveals what the guard was meant to protect.

Negative cases should assert absence or redaction of:

- private identifiers;
- exact sensitive geometry;
- source-restricted fields;
- operator or parcel joins;
- proprietary attributes;
- internal store paths;
- policy internals that aid bypass;
- credentials and endpoint details;
- stack traces in public envelopes.

A correct status with a leaking payload is a failed test.

[Back to top](#top)

---

## Lifecycle, release, correction, and rollback

Negative coverage should prove that invalid or unsupported objects cannot silently advance through:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Where material, test:

- unsupported admission routes to quarantine or fails;
- failed validation does not reach processed state;
- missing evidence or policy blocks catalog/release use;
- absent review or release state blocks public carriers;
- corrections invalidate dependent projections;
- withdrawals stop public use;
- rollback restores an identified prior target rather than deleting history.

A test may verify these controls. It may not perform or approve an operational promotion, correction, or rollback.

[Back to top](#top)

---

## Runner, CI, and promotion boundary

### Current state

- No accepted `tests/invalid` runner is established.
- `make test` collects only `tests/schemas` and `tests/contracts`.
- `make deny-test` echoes TODO.
- `.github/workflows/deny-test.yml` runs three echo-only jobs.

A candidate future command is:

```bash
python -m pytest tests/invalid -q
```

It remains `PROPOSED / NEEDS VERIFICATION`.

### Activation prerequisites

Before activation, verify:

1. lane retention and ownership;
2. at least one genuinely cross-cutting case;
3. deterministic non-zero collection;
4. positive controls;
5. fixture routing;
6. no-network enforcement;
7. no governed-root side effects;
8. non-leaking failure assertions;
9. meaningful exit codes;
10. bounded skip/xfail policy;
11. sanitized artifacts and cleanup;
12. CI ownership and rollback.

### Promotion posture

Substantive negative tests may block promotion after acceptance. They cannot approve promotion.

A green echo-only job is not enforcement.

[Back to top](#top)

---

## Migration, deprecation, and rollback

Retain this lane only for cross-cutting cases without a clearer owner.

When ownership becomes specific:

1. move the test to the owning lane;
2. preserve history;
3. update fixture references;
4. update CI collection;
5. remove duplicate assertions;
6. retain a compatibility pointer only when needed;
7. compare behavior before and after migration;
8. document rollback.

If all cases gain specific owners, this lane may become a README-only pointer or be retired through a documented migration. Do not delete it while callers, docs, or workflows still reference it.

Revert this README if it claims nonexistent coverage, centralizes all negative tests here, weakens fail-closed/no-network defaults, permits sensitive data, or creates parallel authority.

[Back to top](#top)

---

## Definition of done

### This revision

- [x] Records the lane as README-only without claiming exhaustive absence.
- [x] Records checked-absent harness and test paths.
- [x] Classifies the lane as compatibility/utility rather than universal negative authority.
- [x] Identifies substantive negative coverage in specific schema, policy, and API lanes.
- [x] Records fixture-home boundaries.
- [x] Records Makefile exclusion and TODO-only deny workflow.
- [x] Replaces speculative files with routing and admission rules.
- [x] Separates test, validation, runtime, policy, workflow, and release vocabularies.
- [x] Adds positive-control, non-leakage, no-network, side-effect, correction, and rollback requirements.
- [x] Changes documentation only.
- [ ] Record repository-native CI after PR creation.

### Future active direct lane

The direct lane is not complete until retention is accepted, owners are assigned, substantive tests collect, positive controls pass, fixtures are governed, no-network is enforced, protected data cannot leak, governed roots remain unchanged, CI runs the exact suite, promotion dependency is explicit, and migration/rollback are documented.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `INVALID-001` | Should `tests/invalid/` be retained? | `NEEDS VERIFICATION` |
| `INVALID-002` | Is the bounded direct inventory complete? | `NEEDS VERIFICATION` |
| `INVALID-003` | Are tests dynamically collected into this lane? | `UNKNOWN` |
| `INVALID-004` | What qualifies as genuinely cross-cutting? | `NEEDS VERIFICATION` |
| `INVALID-005` | What fixture split is canonical? | `NEEDS VERIFICATION` |
| `INVALID-006` | What failure and reason vocabularies are accepted? | `NEEDS VERIFICATION` |
| `INVALID-007` | What is the accepted runner? | `UNKNOWN` |
| `INVALID-008` | How is zero collection made fatal? | `UNKNOWN` |
| `INVALID-009` | How is no-network enforced? | `UNKNOWN` |
| `INVALID-010` | What positive-control rule is accepted? | `NEEDS VERIFICATION` |
| `INVALID-011` | Is mutation testing required for trust-bearing cases? | `NEEDS VERIFICATION` |
| `INVALID-012` | How are sensitive fixtures reviewed? | `NEEDS VERIFICATION` |
| `INVALID-013` | What reports may CI retain? | `NEEDS VERIFICATION` |
| `INVALID-014` | Which workflow should replace the deny-test scaffold? | `UNKNOWN` |
| `INVALID-015` | Does this suite block promotion? | `UNKNOWN` |
| `INVALID-016` | What are current count, pass rate, coverage, duration, and flake rate? | `UNKNOWN` |
| `INVALID-017` | What is the deprecation trigger? | `NEEDS VERIFICATION` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| prior blob `f3b7d281…` | `CONFIRMED` | Existing v0.1 lane intent. | Direct executable coverage. |
| Directory Rules `2affb080…` | `CONFIRMED DOCTRINE` | Tests root, responsibility separation, reversibility. | Runtime behavior. |
| tests root `5614de99…` | `CONFIRMED ROOT CONTRACT` | Compatibility/utility posture if retained. | Direct runner. |
| valid sibling `fb405f82…` | `CONFIRMED DOCUMENTATION` | Positive companion is also placement-sensitive. | Positive executable suite. |
| tests fixtures `2d0147e8…` | `CONFIRMED DOCUMENTATION` | Test-local fixture split. | Complete payload inventory. |
| root invalid fixtures `4cf89737…` | `CONFIRMED DOCUMENTATION` | Cross-cutting reusable invalid-fixture intent. | Payloads or consumer tests. |
| schema test `b04342cc…` | `CONFIRMED EXECUTABLE` | Invalid contract fixtures must produce schema errors. | Semantic, policy, or release coverage. |
| non-publisher test `c6164787…` | `CONFIRMED EXECUTABLE` | Connector/pipeline publish-target writes are rejected. | All mutation paths. |
| Explorer boundary test `97d44069…` | `CONFIRMED EXECUTABLE` | Adapter and internal-store boundaries. | Full UI negative coverage. |
| governed API test `d84ccd2a…` | `CONFIRMED EXECUTABLE` | Route, method, import, and internal-store negative checks. | Production deployment. |
| deny workflow `d2dd40c2…` | `CONFIRMED TODO SCAFFOLD` | Workflow exists. | Deny-test execution. |
| Makefile `4dc8cf63…` | `CONFIRMED` | Default test target omits this lane. | Dynamic external collection. |
| cross-domain parent `cdf514e6…` | `CONFIRMED / CONFLICTED` | Multi-domain composition has a separate routing lane. | Invalid-lane ownership. |
| bounded search/path checks | `CONFIRMED BOUNDED RESULT` | README-only conclusion and checked absent files. | Exhaustive absence. |

Current test code, fixture payloads, collection output, workflow commands, logs, and generated reports outrank README plans for implementation claims.

[Back to top](#top)

---

## Maintainer note

Keep negative assertions close to the responsibility that owns them. Use this lane only for genuine cross-cutting cases.

A green test that always rejects is not proof of selective policy. A green job that collects zero tests is not coverage. A denial response that leaks protected information is not safe. A TODO workflow is not enforcement.

<p align="right"><a href="#top">Back to top</a></p>
