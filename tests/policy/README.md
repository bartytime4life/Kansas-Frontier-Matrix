# `tests/policy/` — Governed Policy and Boundary-Guard Test Contract

> Repository-grounded enforceability boundary for proving that KFM policy-adjacent control surfaces fail closed, preserve authority separation, and do not bypass governed APIs, lifecycle gates, policy inputs, release controls, or publication boundaries—without turning static scans, schema fixtures, test success, or a policy decision record into policy authority or release approval.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-policy-readme
title: tests/policy/README.md — Governed Policy and Boundary-Guard Test Contract
type: readme; directory-readme; policy-test-parent; governance-boundary-suite; enforceability-boundary
version: v0.3
status: draft; repository-grounded; executable-boundary-suite-confirmed; static-and-structural-coverage; policy-engine-tests-unestablished; policy-runtime-placeholder; policy-workflow-split; non-authoritative
owners: OWNER_TBD — QA steward · Policy steward · Governance steward · Control-plane steward · Governed API steward · Explorer Web steward · Connector steward · Pipeline steward · Contract/schema steward · Evidence steward · Rights/sensitivity steward · Release steward · Security reviewer · CI steward · Docs steward
created: 2026-07-06
updated: 2026-07-16
supersedes: v0.2
policy_label: public-doctrine; tests; policy; boundary-guards; fail-closed; no-network-default; synthetic-only; authority-separation; trust-membrane; non-publisher; evidence-subordinate; rights-aware; sensitivity-aware; release-gated; correction-aware; rollback-aware
current_path: tests/policy/README.md
truth_posture: CONFIRMED target README v0.2, Directory Rules, canonical tests root, singular policy root, direct boundary_constants.py plus three direct test modules, app-owned governed-api boundary companion, exact Makefile boundary-guards and boundary-guards-ci commands, path-filtered substantive policy-boundary-guards workflow, ignored local JUnit report path, TODO-only generic policy-test workflow and make policy target, root make test exclusion, policy contracts and mixed-maturity schemas, minimal PolicyDecision valid/invalid fixtures exercised by the common schema harness, PolicyDecision outcome vocabulary ANSWER|ABSTAIN|DENY|ERROR, decision-policy prose that also discusses engine-native ALLOW|RESTRICT|HOLD, README-only policy bundle lane, placeholder policy-runtime namespace, one sampled default-deny Rego scaffold, absent policy/policy/ path named by schema, and absent dedicated PolicyDecision validator at the schema-declared path / PROPOSED accepted policy case contract, explicit static-guard target manifests and nonempty-scan assertions, policy-engine and bundle-evaluation tests, rights/sensitivity/consent/revocation/redaction/release matrices, obligation-enforcement tests, reason-code registry tests, policy version/digest/replay tests, network/filesystem/secret controls, workflow trigger expansion, zero-collection failure, coverage and mutation metrics, substantive generic policy CI, promotion blocking, correction, deprecation, and rollback / CONFLICTED static boundary suite versus broader policy behavior claims; canonical PolicyDecision outcomes versus engine-native policy vocabulary; schema-declared policy/policy/ and validator paths versus checked absence; policy-boundary workflow path filters versus policy/contracts/schemas/fixtures changes; mixed policy schema maturity; policy root authority versus placeholder runtime and bundle implementation / UNKNOWN exhaustive policy source and test inventory, dynamic collection, accepted evaluator, active bundle selection, OPA/WASM binding, policy bundle format, complete reason-code and obligation registries, actual policy coverage, current mutation score, production enforcement, deployment, receipt emission, branch-protection significance, and promotion dependency / NEEDS VERIFICATION owners, direct-lane retention, root versus app/package/domain test placement, non-vacuous static scan enforcement, accepted outcome normalization, policy fixture completeness, sensitive-test review, artifact retention, trigger ownership, release-gate integration, and migration plan
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 1852516d033a6180507c7ad0b4390689a401c988
  target_prior_blob: e64e81df769ac9f6b398f40fd46875f30eda5c8f
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    tests_root_readme: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
    policy_root_readme: 09cd966ab188d5e831960869117522a98274cb7f
    policy_decision_readme: 0f81c17a705dd29a2d4b6ba725070c1062f44306
    policy_bundles_readme: 77f59c399fbce668c916cbbc385009121d6169f4
    policy_runtime_namespace_readme: f5b89067c4a88ed756626f03ac8254c10089c358
    policy_contracts_readme: e7c409ead34b2062a8713f6f75e0b96f5c0eb318
    policy_decision_contract: ebfe97f98263e6309db6d2772cb2c5e548819650
    policy_schema_index: 5129bc970b8c87dc1350b09611c21dbd697c368e
    policy_decision_schema: 1472d26a42c73f17545b4464a275412ffa1d098e
    policy_decision_fixtures_readme: 0169614d568cfc32bc7fb257fb42f1e6b792bae3
    common_schema_fixture_test: b04342cc034d7f1cc554e155fdd02d6e972976e6
    policy_validator_index: 56ef4bd527ddfc8d726662092ca589ab2340b401
    boundary_constants: 6c61f8e9160faa6d91b9c3e0cb6713dad153d9b5
    control_plane_register_test: 05ebb49d07235ab77bd9dbf6717ee05a59e2f052
    explorer_web_boundary_test: 97d44069b0a5ab4a82b1e1fc48665e905c08a287
    pipeline_connector_non_publisher_test: c6164787bc848eb2347c347af203d76afae37a2b
    governed_api_boundary_test: d84ccd2a93bdf786e8fca11ee596dcc47e543fc2
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    root_pyproject: e3bd40e8e6ce14dfcde78ff5c09608095c3eca76
    policy_boundary_workflow: fb3d8c85baa9aa9dd44a6dcd622cf57fa47d3b2b
    generic_policy_workflow: 2bba88bb018600f54995d06b03cac02145b96fe7
    gitignore: 50e0e0e2485e6dbd6b7e1c2767350b459335b22b
    sampled_rego_scaffold: 5fa096c9d65183b0b3333e05434bbf6f2ab9c0b7
  direct_lane_files_confirmed:
    - tests/policy/README.md
    - tests/policy/boundary_constants.py
    - tests/policy/test_control_plane_register_meta_contract.py
    - tests/policy/test_explorer_web_adapter_boundary.py
    - tests/policy/test_pipeline_connector_non_publisher.py
  app_owned_companion_confirmed:
    - apps/governed-api/tests/test_boundary_guards.py
  checked_absent_paths:
    - tools/validators/validate_policy_decision.py
    - tools/validators/policy/validate_policy_decision.py
    - tools/validators/policy/validate_policy_input_bundle.py
    - policy/policy/README.md
  bounded_inventory_note: the listed direct files and companion test were individually verified; this does not prove exhaustive absence of additional policy tests in history, ignored files, generated workspaces, branch-local files, package-local tests, domain-local tests, external systems, or uninspected paths
related:
  - ../README.md
  - ../schemas/README.md
  - ../contracts/README.md
  - ../invalid/README.md
  - ../release/README.md
  - ../ui/README.md
  - ../pipelines/README.md
  - ../fixtures/README.md
  - ./boundary_constants.py
  - ./test_control_plane_register_meta_contract.py
  - ./test_explorer_web_adapter_boundary.py
  - ./test_pipeline_connector_non_publisher.py
  - ../../apps/governed-api/tests/test_boundary_guards.py
  - ../../policy/README.md
  - ../../policy/decision/README.md
  - ../../policy/bundles/README.md
  - ../../packages/policy-runtime/src/policy_runtime/README.md
  - ../../contracts/policy/README.md
  - ../../contracts/policy/policy_decision.md
  - ../../schemas/contracts/v1/policy/README.md
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../fixtures/contracts/v1/policy/policy_decision/README.md
  - ../../tools/validators/policy/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../.github/workflows/policy-boundary-guards.yml
  - ../../.github/workflows/policy-test.yml
  - ../../Makefile
  - ../../.gitignore
notes:
  - "v0.3 replaces stale presence-verification language with a commit-pinned executable boundary-suite inventory."
  - "The confirmed direct suite is substantive but primarily structural and static; it is not a policy evaluator or complete policy-behavior suite."
  - "The path-filtered policy-boundary-guards workflow runs the four-file suite and uploads JUnit XML, while the generic policy-test workflow remains TODO-only."
  - "The current Makefile default test and validate targets do not include tests/policy; make policy is TODO-only."
  - "PolicyDecision schema fixtures are exercised under tests/schemas, not by the direct tests/policy boundary suite."
  - "Policy runtime, bundle selection, dedicated validators, active evaluator binding, and production enforcement remain unestablished."
  - "This revision changes documentation only and creates no policy rule, bundle, evaluator, validator, fixture, test, workflow behavior, contract, schema, data object, receipt, proof, release record, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Boundary suite: confirmed" src="https://img.shields.io/badge/boundary__suite-CONFIRMED-success">
  <img alt="Coverage: structural and static" src="https://img.shields.io/badge/coverage-structural%20%2B%20static-informational">
  <img alt="Policy engine: not established" src="https://img.shields.io/badge/policy__engine-not__established-orange">
  <img alt="Default: fail closed" src="https://img.shields.io/badge/default-fail__closed-critical">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Release authority: none" src="https://img.shields.io/badge/release__authority-none-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-boundary) · [Inventory](#confirmed-executable-inventory) · [Coverage](#what-the-current-suite-proves) · [Limitations](#what-the-current-suite-does-not-prove) · [Routing](#placement-and-routing-law) · [Case contract](#minimum-policy-test-case-contract) · [Outcomes](#outcome-vocabularies-and-normalization) · [Inputs](#policy-input-evidence-rights-and-sensitivity) · [Obligations](#obligations-redaction-generalization-and-enforcement) · [Boundaries](#control-plane-api-ui-pipeline-and-connector-boundaries) · [Bundles](#policy-bundle-runtime-and-evaluator-boundary) · [Fixtures](#contracts-schemas-fixtures-and-validator-boundary) · [Security](#network-filesystem-secrets-and-sensitive-material) · [Determinism](#determinism-time-replay-and-idempotency) · [Artifacts](#reports-artifacts-and-receipts) · [CI](#runner-workflows-triggers-and-promotion) · [Corrections](#correction-supersession-withdrawal-and-rollback) · [Migration](#migration-deprecation-and-lane-retention) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Evidence snapshot:** `main@1852516d033a6180507c7ad0b4390689a401c988`
> **Prior target blob:** `e64e81df769ac9f6b398f40fd46875f30eda5c8f`
> **Direct policy-test inventory:** README, one constants module, and three executable test modules
> **App-owned companion:** `apps/governed-api/tests/test_boundary_guards.py`
> **Substantive workflow:** `.github/workflows/policy-boundary-guards.yml`
> **Generic policy workflow:** TODO-only
> **Default `make test`:** excludes policy tests

The repository has an executable governance-boundary suite. It does **not** yet have an established general policy-engine, policy-bundle, or policy-obligation enforcement suite.

### Safe conclusions

- **CONFIRMED:** all four files named by the previous README's command exist.
- **CONFIRMED:** `boundary_constants.py` supplies forbidden internal-store path literals shared by UI and API boundary tests.
- **CONFIRMED:** control-plane tests inspect nine required register files for metadata, dates, owners, doctrine refs, status values, and entries.
- **CONFIRMED:** Explorer Web boundary tests statically inspect JavaScript/TypeScript source for renderer-import placement and forbidden internal-store path literals.
- **CONFIRMED:** connector/pipeline tests statically inspect selected file extensions and lexical write contexts near forbidden publication targets.
- **CONFIRMED:** governed-api boundary tests exercise 404 and method behavior, assert the route manifest, and statically inspect forbidden imports and internal-store path literals.
- **CONFIRMED:** `make boundary-guards` runs the four-file suite.
- **CONFIRMED:** `make boundary-guards-ci` creates `artifacts/qa/` and emits JUnit XML to `artifacts/qa/policy-boundary-guards.xml`.
- **CONFIRMED:** `.gitignore` excludes local `artifacts/qa/*.xml` reports from version control.
- **CONFIRMED:** `policy-boundary-guards.yml` installs pytest, runs the CI target, and uploads the JUnit report even when tests fail.
- **CONFIRMED:** the generic `policy-test.yml` jobs only echo TODO messages.
- **CONFIRMED:** `make policy` only echoes a TODO OPA command.
- **CONFIRMED:** `make test` and therefore `make validate` do not include the policy boundary suite.
- **CONFIRMED:** PolicyDecision schema fixtures receive machine-shape coverage through `tests/schemas/test_common_contracts.py`, not through the direct boundary suite.
- **CONFIRMED:** the inspected policy runtime namespace is a placeholder and the inspected policy bundle lane is README-only.
- **CONFIRMED:** the sampled Rego file is a proposed default-deny scaffold, not evidence of a complete active bundle.
- **UNKNOWN:** complete policy-source inventory, active evaluator, selected bundle, runtime consumers, policy coverage, production enforcement, branch-protection dependency, and promotion blocking.
- **NEEDS VERIFICATION:** accepted outcome normalization, reason-code and obligation registries, trigger coverage, non-vacuous scan requirements, fixture completeness, and separation of root versus app/package/domain tests.

### Maturity matrix

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Direct README | `CONFIRMED` | Policy test boundary exists. |
| Direct executable files | `CONFIRMED` | Three tests plus shared constants exist. |
| Governed API companion | `CONFIRMED` | App-owned boundary tests exist. |
| Local boundary command | `CONFIRMED` | Exact pytest command is Makefile-backed. |
| CI boundary command | `CONFIRMED` | JUnit-emitting Makefile target exists. |
| Path-filtered boundary workflow | `CONFIRMED SUBSTANTIVE` | Installs pytest, runs suite, uploads report. |
| Generic policy workflow | `TODO-ONLY` | No OPA or fixture-coverage command runs. |
| Default Makefile test coverage | `EXCLUDED` | `make test` runs schemas and contracts only. |
| PolicyDecision shape fixtures | `MINIMAL / CONFIRMED` | One valid and one missing-field invalid case exist. |
| Policy engine evaluation | `NOT ESTABLISHED` | No accepted evaluator/bundle binding verified. |
| Policy runtime package | `PLACEHOLDER` | Empty initializer and comment-only core. |
| Policy bundle activation | `NOT ESTABLISHED` | No accepted bundle instance or selector verified. |
| Dedicated policy validators | `NOT FOUND AT CHECKED PATHS` | Schema-declared paths are unresolved. |
| Current boundary-suite pass rate | `NEEDS CURRENT RUN` | Repository-native PR workflow provides current evidence. |
| Policy behavior coverage | `UNKNOWN` | Structural/static suite is not full policy behavior. |
| Promotion blocking | `UNKNOWN` | No verified promotion dependency requires this suite. |

### Truth labels

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from current repository files, executable code, workflow definitions, or generated workflow results. |
| `PROPOSED` | A test, rule, contract, path, or procedure not yet accepted or implemented. |
| `CONFLICTED` | Competing vocabularies, paths, authorities, or trigger expectations exist. |
| `UNKNOWN` | Runtime, CI significance, production use, or complete inventory is not established. |
| `NEEDS VERIFICATION` | Checkable, but unresolved strongly enough to act as fact. |
| `DENY` | Disallowed because it weakens governance, leaks protected state, or bypasses an authority boundary. |

[Back to top](#top)

---

## Purpose

`tests/policy/` owns authored tests whose primary responsibility is **policy and governance boundary enforceability**.

The current suite focuses on whether repository control surfaces preserve responsibility boundaries:

```text
control-plane register metadata
  + Explorer Web renderer/store boundaries
  + connector/pipeline non-publisher boundaries
  + governed-api route/import/store boundaries
  -> deterministic pytest results
  -> optional JUnit QA report
```

A future complete policy test capability must additionally prove:

```text
explicit PolicyInputBundle
  -> accepted bundle/version/digest
  -> accepted evaluator profile
  -> finite engine-native result
  -> canonical PolicyDecision normalization
  -> reason codes and obligations
  -> downstream enforcement
  -> receipt/replay metadata
  -> release/correction/rollback gate
```

A passing test means only that the scoped assertion passed. It does **not** prove:

- the correct policy bundle ran;
- all policy rules are covered;
- rights are clear;
- sensitivity is correctly classified;
- consent is valid or unrevoked;
- redaction/generalization obligations were applied;
- evidence is complete;
- release is approved;
- public display is safe;
- production enforcement is active.

[Back to top](#top)

---

## Authority boundary

### Directory Rules basis

KFM separates meaning, shape, admissibility, execution, proof, and release:

```text
contracts/policy/             policy object meaning
schemas/contracts/v1/policy/  policy object machine shape
policy/                       policy rules, posture, and reviewed bundle source
packages/policy-runtime/      evaluator helper implementation
fixtures/                     synthetic valid/invalid inputs
tests/                        authored enforceability proof
tools/validators/             validation implementation
apps/governed-api/             public trust membrane
release/                      release, correction, withdrawal, rollback authority
data/receipts/ and proofs/    auditable process and evidence artifacts
```

| Responsibility | Authority home | This lane's role |
|---|---|---|
| Policy and governance tests | `tests/policy/` | Owns direct cross-cutting boundary assertions. |
| App-specific boundary tests | App-local test lane | Keeps implementation-owned route/API behavior close to the app. |
| Policy rules and bundle source | `policy/` | Tested, never authored here. |
| Policy semantic meaning | `contracts/policy/` | Referenced, never redefined here. |
| Policy object shape | `schemas/contracts/v1/policy/` | Validated, never authored here. |
| Evaluator helpers | `packages/policy-runtime/` | Tested when functional; never policy authority. |
| Validators | `tools/validators/` | Tested when implemented; not duplicated here. |
| Fixtures | `fixtures/` and accepted test-local fixture lanes | Consumed, not stored beside tests by default. |
| Evidence and citations | evidence/proof roots | Inputs to policy; not created by tests. |
| Release/correction/rollback | `release/` | Tests can block; they cannot approve or execute release. |
| QA reports | ephemeral CI or accepted artifact lane | Outputs, not test or policy authority. |

### Anti-collapse rules

This lane must not collapse:

```text
pytest PASS                   -> policy ALLOW
static scan PASS              -> runtime safety
schema-valid PolicyDecision   -> correct policy evaluation
default deny Rego scaffold    -> active policy bundle
workflow success              -> policy coverage
JUnit report                  -> release approval
file presence                 -> activation
policy README                 -> executable rule
PolicyDecision                -> ReleaseManifest
policy obligation             -> obligation enforcement
path-literal absence          -> absence of internal-store access
```

[Back to top](#top)

---

## Confirmed executable inventory

### Direct lane

The bounded direct inventory is:

```text
tests/policy/
├── README.md
├── boundary_constants.py
├── test_control_plane_register_meta_contract.py
├── test_explorer_web_adapter_boundary.py
└── test_pipeline_connector_non_publisher.py
```

### App-owned companion

```text
apps/governed-api/tests/test_boundary_guards.py
```

### Shared constants

`boundary_constants.py` defines these forbidden path literals:

```text
data/raw
data/work
data/quarantine
data/processed
data/catalog
data/published
release/
```

The tuple is a static lexical denylist. It is not a complete filesystem, API, database, object-store, symlink, URI, alias, environment-variable, or runtime-access policy.

### Control-plane register tests

The control-plane module requires nine register files and tests:

- top-level `meta:` start;
- `status`, `owner`, `last_reviewed`, and `related_doctrine` metadata;
- `entries:` presence;
- ISO-formatted review dates;
- no future review date relative to the test runner's date;
- existing related-doctrine paths;
- allowed status values `PROPOSED` or `CONFIRMED`;
- nonempty owner and doctrine entries.

These are structural governance checks. They do not parse full YAML semantics, validate register schemas, resolve every entry reference, enforce uniqueness, verify ownership identity, prove review occurred, or establish runtime authority.

### Explorer Web boundary tests

The Explorer module scans `.ts`, `.tsx`, `.js`, and `.jsx` files under `apps/explorer-web/src` and tests:

- MapLibre/Cesium import statements stay under the `adapters` directory;
- configured forbidden internal-store path literals are absent.

It does not currently assert a nonempty source inventory. It does not detect dynamic imports, aliases, computed URLs, network calls, database clients, generated code, runtime behavior, indirect dependencies, source maps, or data fetched through unlisted identifiers.

### Connector and pipeline non-publisher test

The non-publisher module scans selected `.py`, `.sh`, `.yaml`, and `.yml` files under `connectors/` and `pipelines/`. It identifies selected lexical write-call patterns and rejects nearby forbidden targets.

It does not prove complete side-effect safety. It may miss dynamic paths, wrappers, imported helpers, subprocesses, cloud SDKs, SQL, object stores, symlinks, aliases, templating, generated commands, alternate extensions, or writes outside its line window. It may also flag comments or strings. Future maturity requires explicit target manifests and runtime sandbox tests.

### Governed API boundary companion

The app-owned module tests:

- unknown routes return `404` with a fixed body;
- `POST`, `PUT`, and `DELETE` are rejected for scaffolded routes;
- forbidden MapLibre/Cesium/Ollama imports are absent from inspected Python code;
- route manifest is exactly `/bootstrap`, `/layers`, and `/evidence`;
- configured internal-store path literals are absent from API source.

This proves selected scaffold boundaries. It does not prove authentication, authorization, policy evaluation, evidence resolution, sensitivity handling, release validation, rate limiting, request-size limits, network isolation, data access behavior, or production deployment.

[Back to top](#top)

---

## What the current suite proves

| Assertion family | Current evidence | Safe claim |
|---|---|---|
| Control-plane metadata | Direct executable tests | Required files satisfy selected header/date/path checks when suite passes. |
| Explorer renderer boundary | Static source scan | Selected literal renderer imports stay in adapter paths when targets exist. |
| Explorer store boundary | Static source scan | Selected forbidden path literals are absent from scanned source. |
| Connector/pipeline non-publisher | Static lexical scan | Selected write contexts do not contain selected forbidden target literals. |
| Governed API route/method boundary | In-process WSGI calls | Scaffold route manifest and selected HTTP method behavior match assertions. |
| Governed API dependency/store boundary | Static source scan | Selected forbidden imports/path literals are absent. |
| JUnit report generation | Makefile + workflow | CI can emit and upload a pytest JUnit report. |
| PolicyDecision schema shape | Companion schema harness | Existing valid/invalid fixtures are discriminated when schema tests run. |

These are meaningful controls. They are **boundary guards**, not comprehensive policy evaluation.

[Back to top](#top)

---

## What the current suite does not prove

The confirmed suite does not establish:

- OPA/Rego parsing, compilation, bundle build, or bundle tests;
- accepted policy bundle identity, version, digest, signature, or dependency closure;
- active evaluator selection or runtime binding;
- `PolicyInputBundle` completeness;
- normalization from engine-native `ALLOW`, `RESTRICT`, or `HOLD` to canonical outcomes;
- stable reason-code and obligation registries;
- rights, license, terms, attribution, embargo, or redistribution behavior;
- living-person, DNA/genomic, archaeology, rare-species, infrastructure, cultural/tribal, or private-join sensitivity behavior;
- consent grant, scope, expiration, revocation, or downstream invalidation;
- redaction, generalization, staged access, delay, withhold, export block, or review obligations;
- policy conflict composition or most-restrictive-result propagation;
- evaluator timeout, crash, malformed output, stale bundle, missing bundle, or digest mismatch;
- receipt emission, replay, supersession, correction, withdrawal, or rollback;
- public UI/API policy explanations and no-leak behavior;
- release-gate dependency;
- production policy enforcement.

[Back to top](#top)

---

## Placement and routing law

Keep tests with the responsibility they primarily verify.

| Primary assertion | Preferred home | Reason |
|---|---|---|
| Cross-cutting governance boundary | `tests/policy/` | Neutral policy/governance invariant spans components. |
| Governed API route or serializer behavior | App-local API tests | App owns implementation behavior. |
| Explorer component/render behavior | App/package UI tests | UI implementation owns rendering and interaction. |
| Pipeline/connector domain behavior | Connector, pipeline, or domain test lane | Implementation owner should maintain detailed behavior tests. |
| Policy object shape | `tests/schemas/` | Shape authority is schemas. |
| Policy semantic contract | `tests/contracts/` | Meaning authority is contracts. |
| Policy runtime helper | Package-local policy-runtime tests | Package owns helper implementation. |
| OPA/Rego bundle behavior | Policy bundle test lane under accepted convention | Policy source/bundle owner maintains rule evaluation. |
| Release gate composition | `tests/release/` | Release owns promotion/publication decision flow. |
| Domain-specific sensitivity/rights | `tests/domains/<domain>/` | Domain owns risk context. |
| Full public flow | `tests/e2e/` | Composed behavior crosses API, UI, policy, evidence, release. |

### Admission requirements for a direct test

A new file belongs directly in `tests/policy/` only when:

1. the primary assertion is policy/governance boundary enforcement;
2. no app, package, connector, pipeline, release, schema, contract, E2E, or domain owner is more precise;
3. the system under test and authority boundary are explicit;
4. positive and negative controls exist;
5. target inventory cannot be empty silently;
6. fixtures are synthetic and public-safe;
7. no live network or production service is used;
8. side effects and cleanup are explicit;
9. CI runs the exact test;
10. a steward accepts maintenance and rollback.

Do not duplicate the same assertion in several lanes merely to increase apparent coverage.

[Back to top](#top)

---

## Minimum policy test case contract

Every consequential policy test should declare:

| Field | Required content |
|---|---|
| `case_id` | Stable deterministic identifier. |
| `owner` | Policy, app, package, connector, pipeline, release, or domain owner. |
| `system_under_test` | Exact rule, bundle, evaluator, adapter, register, route, or source set. |
| `policy_family` | Promotion, access, render, capability, consent, sensitivity, or accepted successor. |
| `operation` | Exact action being evaluated. |
| `audience` | Public, semi-public, steward, restricted, admin, service, or denied. |
| `input_ref` | Synthetic PolicyInputBundle or explicit equivalent. |
| `bundle_ref` | Accepted bundle id/version/digest when evaluation occurs. |
| `evidence_state` | Evidence/citation/resolver posture where material. |
| `rights_state` | License, terms, attribution, embargo, redistribution. |
| `sensitivity_state` | Classification, precision, protected category, review state. |
| `consent_state` | Scope, subject, grant, expiration, revocation when material. |
| `engine_result` | Native evaluator result if applicable. |
| `canonical_outcome` | Accepted PolicyDecision/runtime outcome. |
| `reason_codes` | Stable expected codes. |
| `obligations` | Required downstream enforcement. |
| `must_allow` | Explicit permitted behavior. |
| `must_deny` | Explicit prohibited behavior. |
| `must_not_expose` | Sensitive or internal canaries that must remain absent. |
| `network_posture` | Denied, local mock, or reviewed allowlist. |
| `side_effects` | Files, logs, reports, receipts, storage, requests. |
| `cleanup` | Deterministic restoration. |
| `correction_rollback` | Supersession and rollback expectation. |

### Positive and negative controls

A denial test needs a positive companion proving the evaluator or guard is selective. An allow/answer test needs negative companions proving missing, stale, denied, restricted, revoked, or malformed context fails closed.

### Non-vacuity

Static scans must fail when expected roots or minimum target files are absent. Test output should report scanned file counts, matched context counts, skipped paths, and exclusions. “Scanned zero files” is an error, not a pass.

[Back to top](#top)

---

## Outcome vocabularies and normalization

The repository currently exposes a material vocabulary split.

### Canonical schema-paired PolicyDecision outcomes

```text
ANSWER | ABSTAIN | DENY | ERROR
```

### Engine-native or policy-posture vocabulary in documentation

```text
ALLOW | DENY | RESTRICT | HOLD | ABSTAIN | ERROR
```

### Test outcomes

```text
PASS | FAIL | SKIP | XFAIL | XPASS | ERROR
```

Do not collapse these layers:

```text
pytest PASS       != PolicyDecision ANSWER
OPA allow=true    != release approval
RESTRICT          != DENY
HOLD              != ABSTAIN
ABSTAIN           != ERROR
schema-valid      != evaluated
```

An accepted normalization contract must define how engine-native results map into PolicyDecision outcomes and obligations. Example design direction, still `PROPOSED`:

| Engine-native result | Canonical carrier | Obligations |
|---|---|---|
| `ALLOW` | `ANSWER` | May be empty or scoped. |
| `RESTRICT` | `ANSWER` only when all restrictions are enforceable; otherwise `DENY` or `ABSTAIN` | Required and machine-interpretable. |
| `HOLD` | `ABSTAIN` or a separately accepted review carrier | Review requirement and unresolved authority. |
| `DENY` | `DENY` | Safe reason code. |
| insufficient support | `ABSTAIN` | Missing evidence/authority handles. |
| evaluator/process failure | `ERROR` | Failure metadata without secrets. |

No caller may invent its own mapping silently.

[Back to top](#top)

---

## Policy input, evidence, rights, and sensitivity

Policy evaluation must use explicit, inspectable inputs. It must not fetch missing facts from model memory, UI state, filenames, generated summaries, operator recollection, or undeclared network sources.

Required input families may include:

- object and operation identity;
- audience and capability;
- lifecycle and release state;
- source descriptor and source role;
- evidence and citation state;
- rights, license, attribution, embargo, and redistribution state;
- sensitivity classification and required precision;
- living-person and private-join posture;
- consent scope, validity, expiration, and revocation;
- review requirements and reviewer state;
- policy bundle identity/version/digest;
- evaluator identity/version;
- time and freshness;
- correction, supersession, withdrawal, and rollback state.

Missing or contradictory required context must produce a bounded fail-closed result. Tests must distinguish policy denial, insufficient support, pending review, and evaluator failure.

### Sensitive fixture posture

Use synthetic, minimized, transformed, generalized, or redacted inputs for:

- living-person information;
- DNA/genomic data;
- consent and revocation;
- private person-parcel joins;
- archaeology and cultural/tribal material;
- rare-species and protected ecological locations;
- critical infrastructure and security-relevant locations;
- proprietary commercial or contractual restrictions.

Never place real protected values in policy fixtures, expected-error text, JUnit reports, logs, snapshots, or PR descriptions.

[Back to top](#top)

---

## Obligations, redaction, generalization, and enforcement

Policy decisions may carry obligations such as:

- attach citation;
- redact coordinates;
- generalize geometry;
- withhold exact location;
- mask identifiers;
- require steward review;
- delay publication;
- attach rights notice;
- block export;
- restrict audience;
- require rollback readiness;
- reevaluate after expiration or source change.

An obligation is not satisfied merely because it appears in a list.

Tests should prove:

1. the obligation is recognized;
2. the downstream owner can enforce it;
3. unknown obligations fail closed;
4. contradictory obligations fail closed;
5. the applied transform is deterministic and recorded;
6. protected original values do not leak;
7. exported, cached, logged, and accessible representations preserve the obligation;
8. correction/rollback can restore or invalidate affected artifacts.

A caller unable to enforce an obligation must not proceed as `ANSWER` or public-safe.

[Back to top](#top)

---

## Control-plane, API, UI, pipeline, and connector boundaries

### Control plane

Registers are governance metadata, not runtime truth. Future tests should validate full YAML parsing, schema conformance, unique IDs, reference resolution, status transitions, owner identities, review recency policy, deprecation links, contradiction closure, and nonempty inventories where required.

### Governed API

The public trust membrane should test explicit audience/operation admission, PolicyInputBundle construction, bundle/evaluator selection, finite PolicyDecision output, evidence resolution, rights/sensitivity gates, obligation enforcement, safe explanations, no internal-store access, no direct model output, and release-state closure.

### Explorer Web and UI

Public UI tests should prove policy states render distinctly and accessibly without leaking denied values through DOM, ARIA, URL, logs, storage, clipboard, exports, screenshots, or diagnostics.

### Connectors and pipelines

Static lexical non-publisher checks should be supplemented by runtime filesystem/network sandboxes, explicit output roots, dry-run parity, symlink/path traversal protection, cloud/object-store client controls, and tests that publication requires a separate release authority.

### Public-client rule

Normal clients use governed APIs and released artifacts. Tests should deny direct reads from RAW, WORK, QUARANTINE, internal/canonical stores, proof stores, local source files, and direct model endpoints.

[Back to top](#top)

---

## Policy bundle, runtime, and evaluator boundary

Current evidence establishes:

- `policy/bundles/` is README-only in bounded evidence;
- no accepted bundle instance, manifest instance, lock, registry, selector, signature, or active deployment was verified;
- `packages/policy-runtime` is a `0.0.0` placeholder with no functional evaluator API or tests;
- the generic policy workflow does not run OPA;
- a sampled Rego file is a proposed default-deny scaffold;
- dedicated policy validators named by schemas are absent at checked paths.

A mature bundle/evaluator test matrix should cover:

| Area | Required cases |
|---|---|
| Bundle identity | Missing, malformed, unknown, stale, superseded, withdrawn. |
| Digest/signature | Match, mismatch, missing, unsupported algorithm, invalid signature. |
| Dependency closure | Complete, missing import/data, unexpected dependency, cycle. |
| Evaluator compatibility | Supported/unsupported version and profile. |
| Compilation | Valid source, syntax failure, forbidden built-in, unsafe capability. |
| Selection | Explicit allowlisted selection; no directory-order or caller-controlled activation. |
| Input validation | Complete, missing required context, unknown fields, stale context. |
| Native outcomes | Allow, deny, restrict, hold, undefined, multiple/conflicting. |
| Normalization | Accepted mapping to canonical PolicyDecision. |
| Obligations | Recognized/enforced, unknown, contradictory, unenforceable. |
| Timeout/failure | Timeout, crash, malformed output, nondeterministic result. |
| Replay | Same bundle/input/evaluator yields equivalent decision. |
| Supersession | New bundle does not rewrite prior decision history. |
| Rollback | Prior accepted bundle can be restored with explicit state. |

Bundle file presence never means activation. Public clients must not choose policy bundles.

[Back to top](#top)

---

## Contracts, schemas, fixtures, and validator boundary

### Contracts

`contracts/policy/` defines semantic meaning. Tests should verify PolicyInputBundle and PolicyDecision meanings remain aligned with executable behavior, but tests must not duplicate contract authority.

### Schemas

The policy schema family is mixed maturity:

- `policy_decision.schema.json` has six required fields, closed additional properties, and finite outcomes;
- `sensitivity_label.schema.json` is concrete but still proposed;
- `policy_input_bundle.schema.json` is permissive and requires only `id`;
- promotion/redaction shapes have overlap and naming drift.

A schema pass proves machine shape only.

### Fixtures

Current PolicyDecision fixture coverage is minimal:

- one valid `ABSTAIN` example;
- one invalid example missing `decision_id`;
- one broad expected-error matcher `required`.

Future coverage should include every outcome, every policy family, invalid enum, invalid ID, invalid timestamp, unexpected property, empty/unsafe reasons, obligation variants, rights/sensitivity/consent context, stale and superseded decisions, and safe public/internal explanation separation.

### Common schema harness

`tests/schemas/test_common_contracts.py` discovers policy schemas only when a matching fixture directory exists. It validates shape polarity. It does not run policy, ensure every schema has fixtures, require nonempty valid/invalid sets, enforce contract semantics, or evaluate obligations.

### Validators

Schema metadata names dedicated validator paths that are absent at checked locations. Until implemented and tested, validator maturity remains unestablished. Do not use README guidance or schema metadata as validator proof.

[Back to top](#top)

---

## Network, filesystem, secrets, and sensitive material

Default policy tests must be local, deterministic, and no-network.

Any allowed network test requires an explicit local/mock endpoint, reviewed allowlist, fixed response, timeout, retry limit, no credentials, no production services, redacted logs, cleanup, and separate nondefault marker/workflow.

Tests should fail on:

- direct external source/provider calls;
- public object-store or database access;
- direct model endpoints;
- environment-variable or secret-store leakage;
- writes outside temporary/sandbox/report roots;
- symlink escape or path traversal;
- world-readable sensitive artifacts;
- policy bundle selection from untrusted input;
- shell injection or unsafe dynamic evaluation;
- sensitive values in assertion messages or JUnit output.

Use synthetic canaries to prove protected values do not appear in files, stdout/stderr, logs, reports, URLs, request bodies, snapshots, or uploaded artifacts.

[Back to top](#top)

---

## Determinism, time, replay, and idempotency

Policy tests should control:

- clock and timezone;
- bundle and evaluator versions;
- input canonicalization;
- identity and hashing;
- source/release freshness;
- random IDs;
- ordering of sets/maps/files;
- environment and working directory;
- concurrency;
- retries and timeouts.

Given the same accepted bundle digest, evaluator profile, canonical input, and time context, evaluation should produce an equivalent canonical decision.

Re-running a guard or evaluator should not mutate policy source, activate bundles, publish, duplicate receipts, overwrite prior decisions, or change historical evaluated timestamps.

The current control-plane “not future” test uses the runner's `date.today()`. A future deterministic harness should define timezone and injectable clock semantics for boundary cases.

[Back to top](#top)

---

## Reports, artifacts, and receipts

### Current JUnit report

```text
artifacts/qa/policy-boundary-guards.xml
```

The Makefile creates this report; `.gitignore` excludes local QA XML; the workflow uploads it as `policy-boundary-guards-junit` with `if: always()`.

The report is execution evidence for the scoped pytest suite. It is not:

- a PolicyDecision;
- an EvidenceBundle;
- a policy-evaluation receipt;
- a release record;
- promotion approval;
- proof of complete policy coverage.

### Artifact safety

Generated reports should record commit, workflow/run, command, test counts, failures, skips, duration, and tool/runtime versions. They must be scanned for secrets and sensitive values, have explicit retention, and remain correctable/deletable.

### Policy-evaluation receipts

Consequential runtime evaluation may require a separate receipt containing input hash, bundle digest, evaluator identity, canonical outcome, reason codes, obligations, timestamps, caller/operation, and correction/rollback refs. Such receipts belong in accepted receipt/proof roots—not in `tests/policy/` and not inside JUnit as the canonical record.

[Back to top](#top)

---

## Runner, workflows, triggers, and promotion

### Local commands

```bash
make boundary-guards
make boundary-guards-ci
```

The root pytest configuration sets `pythonpath = ["."]`. The boundary workflow installs pytest directly on Python 3.11.

### Current workflow split

| Surface | Current command | Posture |
|---|---|---|
| `policy-boundary-guards.yml` | `make boundary-guards-ci` | Substantive structural/static suite. |
| `policy-test.yml` | `echo TODO opa-test`; `echo TODO policy-fixture-coverage` | Scaffold only. |
| `make policy` | `echo TODO: opa test policy/ -v` | Scaffold only. |
| `make test` | schemas + contracts only | Does not include policy boundary suite. |
| `make validate` | `make schemas test` | Does not include policy boundary suite or OPA. |

### Trigger gap

The substantive boundary workflow currently triggers for changes under:

- `tests/policy/**`;
- governed-api tests/source;
- Explorer Web source;
- connectors;
- pipelines;
- control plane.

It does **not** list these important policy-adjacent roots in its path filter:

- `policy/**`;
- `contracts/policy/**`;
- `schemas/contracts/v1/policy/**`;
- policy fixtures;
- policy runtime package;
- release policy/gate files;
- the Makefile or workflow file itself unless another listed path also changes.

Therefore a green boundary workflow cannot be assumed for every policy change. Trigger expansion or a dedicated substantive policy workflow is `PROPOSED` and requires review.

### CI graduation requirements

A mature policy CI plane should include:

1. structural boundary suite;
2. policy source format/lint/compile tests;
3. bundle manifest/digest/dependency tests;
4. PolicyInputBundle and PolicyDecision schema/contract tests;
5. rule-level positive/negative evaluation;
6. rights/sensitivity/consent/redaction matrices;
7. obligation enforcement;
8. timeout/error/undefined/conflict behavior;
9. no-network and sandbox controls;
10. zero-test/nonempty-target failure;
11. coverage and mutation thresholds;
12. artifact and secret scanning;
13. correction/rollback tests;
14. explicit branch-protection and promotion dependency.

Tests may block promotion. They never approve promotion or release.

[Back to top](#top)

---

## Correction, supersession, withdrawal, and rollback

Policy tests should preserve historical decisions and prove:

- corrected policy source produces a new bundle/version/digest;
- prior decisions remain traceable rather than silently rewritten;
- stale or superseded decisions are not treated as current;
- revoked consent invalidates dependent allowances and downstream artifacts;
- sensitivity upgrades propagate more-restrictive obligations;
- withdrawn bundles cannot remain selected;
- rollback restores an explicitly accepted prior bundle and records the transition;
- caches, clients, releases, and reports discover invalidation;
- protected correction/withdrawal reasons remain audience-safe.

Every new framework, bundle format, fixture family, workflow, report, or test home requires a mechanical rollback plan and migration note when authority or compatibility changes.

[Back to top](#top)

---

## Migration, deprecation, and lane retention

Retain `tests/policy/` for cross-cutting governance and policy boundary assertions without a more precise implementation owner.

Move tests when ownership becomes clear:

- app behavior to app-local tests;
- package helper behavior to package-local tests;
- schema shape to `tests/schemas/`;
- contract meaning to `tests/contracts/`;
- release composition to `tests/release/`;
- domain-specific sensitivity to domain tests;
- full flows to E2E.

When moving:

1. preserve history;
2. update Makefile/workflows/path filters;
3. update imports and fixtures;
4. remove duplicate assertions;
5. compare collection/results;
6. preserve JUnit/report consumers;
7. document rollback.

The lane may remain as a routing README even if executable assertions move. Do not delete it while commands, workflows, imports, or documentation reference it.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Records the direct executable inventory and app-owned companion.
- [x] Replaces stale “file presence needs verification” claims.
- [x] Documents exact current assertions and limitations.
- [x] Separates static boundary guards from policy evaluation.
- [x] Records the substantive workflow, Makefile commands, JUnit output, and gitignore posture.
- [x] Records TODO-only generic policy workflow and Makefile target.
- [x] Records default `make test` and `make validate` exclusion.
- [x] Documents PolicyDecision schema/contract/fixture companion coverage and vocabulary conflict.
- [x] Records placeholder policy runtime, README-only bundle lane, absent validators, and sampled Rego scaffold.
- [x] Defines test placement, case contract, non-vacuity, sensitive fixtures, obligations, CI graduation, correction, and rollback.
- [x] Changes documentation only.
- [ ] Record repository-native CI after PR creation.

### Future complete policy enforceability

The policy test capability is not complete until:

- owners are assigned;
- policy bundle/evaluator contracts are accepted;
- engine-native and canonical outcomes are mapped;
- reason-code and obligation registries exist;
- PolicyInputBundle is strengthened;
- dedicated validators exist;
- positive/negative policy fixtures cover all consequential families;
- static scans fail on empty targets;
- OPA/equivalent tests are substantive;
- rights/sensitivity/consent/revocation/redaction are tested;
- obligation enforcement is tested downstream;
- network/filesystem/secret controls are executable;
- receipts/replay/correction/rollback are tested;
- trigger coverage includes policy-adjacent roots;
- metrics and mutation testing are measured;
- branch protection and promotion dependencies are explicit.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `POL-TEST-001` | Is the bounded direct inventory complete? | `NEEDS VERIFICATION` |
| `POL-TEST-002` | Should app-owned boundary tests remain in the root command? | `NEEDS VERIFICATION` |
| `POL-TEST-003` | Which policy tests belong root-, package-, app-, release-, or domain-local? | `NEEDS VERIFICATION` |
| `POL-TEST-004` | What evaluator and bundle format are accepted? | `UNKNOWN` |
| `POL-TEST-005` | What bundle id/version/digest/signature contract is canonical? | `NEEDS VERIFICATION` |
| `POL-TEST-006` | Which policy bundle is active for each caller/operation? | `UNKNOWN` |
| `POL-TEST-007` | How are engine-native outcomes normalized to PolicyDecision? | `NEEDS VERIFICATION` |
| `POL-TEST-008` | What are canonical reason-code and obligation registries? | `NEEDS VERIFICATION` |
| `POL-TEST-009` | How is PolicyInputBundle strengthened beyond an id-only schema? | `NEEDS VERIFICATION` |
| `POL-TEST-010` | Which dedicated policy validators will be implemented? | `UNKNOWN` |
| `POL-TEST-011` | How are static scans made non-vacuous? | `NEEDS VERIFICATION` |
| `POL-TEST-012` | What target manifest and minimum file counts are required? | `NEEDS VERIFICATION` |
| `POL-TEST-013` | How are dynamic imports, wrappers, cloud writes, and runtime side effects tested? | `UNKNOWN` |
| `POL-TEST-014` | What is the complete rights and license matrix? | `NEEDS VERIFICATION` |
| `POL-TEST-015` | What is the sensitivity and precise-location matrix? | `NEEDS VERIFICATION` |
| `POL-TEST-016` | How are consent scope, expiration, revocation, and downstream invalidation tested? | `NEEDS VERIFICATION` |
| `POL-TEST-017` | How are redaction/generalization obligations proven across API/UI/export/map surfaces? | `UNKNOWN` |
| `POL-TEST-018` | What network, filesystem, and evaluator sandbox is accepted? | `UNKNOWN` |
| `POL-TEST-019` | What policy-evaluation receipt schema/home is accepted? | `NEEDS VERIFICATION` |
| `POL-TEST-020` | How are replay, supersession, withdrawal, and rollback tested? | `UNKNOWN` |
| `POL-TEST-021` | Should boundary guards join default `make test` or remain a separate target? | `NEEDS VERIFICATION` |
| `POL-TEST-022` | Which roots should trigger substantive policy CI? | `NEEDS VERIFICATION` |
| `POL-TEST-023` | What coverage and mutation thresholds are required? | `UNKNOWN` |
| `POL-TEST-024` | How long are JUnit and future policy artifacts retained? | `NEEDS VERIFICATION` |
| `POL-TEST-025` | Which policy checks block promotion and branch protection? | `UNKNOWN` |
| `POL-TEST-026` | What are current test counts, pass rate, runtime, flakes, and scanned target counts? | `UNKNOWN` |
| `POL-TEST-027` | How is the schema-declared `policy/policy/` path corrected or migrated? | `NEEDS VERIFICATION` |
| `POL-TEST-028` | What is the deprecation trigger for this lane or its command composition? | `NEEDS VERIFICATION` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| prior target blob `e64e81df…` | `CONFIRMED` | Existing v0.2 intent and historical command names. | Current maturity by itself. |
| Directory Rules `2affb080…` | `CONFIRMED DOCTRINE` | Responsibility roots and authority separation. | Policy runtime behavior. |
| tests root `5614de99…` | `CONFIRMED ROOT CONTRACT` | Tests are enforceability proof, not authority. | Direct policy coverage. |
| policy root `09cd966a…` | `CONFIRMED SHORT PROPOSED ROOT` | Singular policy authority path. | Active policy engine. |
| decision policy README `0f81c17a…` | `CONFIRMED PROPOSED DOC` | Finite policy posture and engine vocabulary. | Executable enforcement. |
| bundle README `77f59c39…` | `CONFIRMED README-ONLY BOUNDARY` | Bundle governance requirements and missing activation. | Bundle instance or selection. |
| policy runtime README `f5b89067…` | `CONFIRMED PLACEHOLDER` | Runtime package is unimplemented. | Evaluator API or consumers. |
| contracts policy README `e7c409ea…` | `CONFIRMED DRAFT CONTRACT BOUNDARY` | Meaning/shape/policy/test split. | Runtime behavior. |
| PolicyDecision contract `ebfe97f9…` | `CONFIRMED DRAFT/PROPOSED` | Canonical carrier semantics and vocabulary distinction. | Correct evaluation. |
| policy schema index `5129bc97…` | `CONFIRMED MIXED MATURITY` | Inventory and overlap/drift risks. | Policy execution. |
| PolicyDecision schema `1472d26a…` | `CONFIRMED PROPOSED SHAPE` | Required fields and finite enum. | Policy correctness or release. |
| fixture README `0169614d…` | `CONFIRMED MINIMAL FIXTURES` | One valid and one invalid shape case. | Policy-family behavior coverage. |
| schema harness `b04342cc…` | `CONFIRMED EXECUTABLE SHAPE TEST` | Fixture polarity for discovered schema families. | Policy evaluation or fixture completeness. |
| policy validator README `56ef4bd5…` | `CONFIRMED ROUTING DOC` | Proposed validator responsibility. | Executable validators. |
| boundary constants `6c61f8e9…` | `CONFIRMED CODE` | Selected forbidden literals. | Complete denylist. |
| control-plane test `05ebb49d…` | `CONFIRMED EXECUTABLE` | Selected register metadata/date/path checks. | Full YAML semantics or governance correctness. |
| Explorer test `97d44069…` | `CONFIRMED EXECUTABLE STATIC GUARD` | Selected imports and path literals. | Runtime/browser/data-access safety. |
| pipeline/connector test `c6164787…` | `CONFIRMED EXECUTABLE STATIC GUARD` | Selected lexical write contexts and targets. | Complete side-effect safety. |
| governed-api test `d84ccd2a…` | `CONFIRMED EXECUTABLE COMPANION` | Selected route/method/import/path boundaries. | Auth, policy, evidence, sensitivity, release, production. |
| Makefile `4dc8cf63…` | `CONFIRMED` | Exact commands, separate policy target, default exclusion. | Current pass result. |
| root pyproject `e3bd40e8…` | `CONFIRMED` | Python >=3.11, pytest optional dependency, root pythonpath. | Workflow dependency lock or full environment parity. |
| boundary workflow `fb3d8c85…` | `CONFIRMED SUBSTANTIVE` | Path-filtered suite and JUnit upload. | Policy-engine coverage or all trigger paths. |
| generic workflow `2bba88bb…` | `CONFIRMED TODO SCAFFOLD` | Generic workflow exists. | OPA or fixture coverage. |
| `.gitignore` `50e0e0e2…` | `CONFIRMED` | Local QA XML excluded. | Artifact retention or secret scanning. |
| sampled Rego `5fa096c9…` | `CONFIRMED PROPOSED DEFAULT-DENY SCAFFOLD` | One policy-as-code placeholder exists. | Active or complete policy bundle. |
| checked absent paths | `CONFIRMED BOUNDED RESULT` | Dedicated validators and declared policy/policy path are unresolved. | Permanent absence across history or branches. |

For implementation claims, prefer current policy source and accepted bundle manifests, evaluator code, direct rule tests, fixtures, workflow commands/logs, receipts/replay evidence, release records, repository documentation, then plans. README intent cannot outrank executable evidence.

[Back to top](#top)

---

## Maintainer note

Preserve the current boundary suite because it provides real structural safeguards. Do not overstate it.

A green static scan is not policy evaluation. A schema-valid PolicyDecision is not proof that the correct bundle ran. A default-deny scaffold is not an active policy program. A JUnit report is not a release decision. A workflow that echoes TODO is not coverage. A test that scans zero files is not a safeguard. A policy outcome without enforceable obligations is not safe authorization.

Expand one governed case at a time with explicit inputs, accepted bundle identity, deterministic evaluator behavior, positive and negative controls, stable reason codes, enforceable obligations, sensitive-safe fixtures, no-network execution, replay metadata, correction and rollback, and substantive CI.

<p align="right"><a href="#top">Back to top</a></p>
