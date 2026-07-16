# `tests/pipelines/` — Governed Pipeline Behavior Test Boundary

> Repository-grounded test boundary for proving that executable KFM pipeline logic preserves lifecycle, source-role, evidence, policy, receipt, release, correction, rollback, idempotency, and no-publication controls without turning test success, pipeline completion, or publish-readiness into truth or release authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-pipelines-readme
title: tests/pipelines/README.md — Governed Pipeline Behavior Test Boundary
type: readme; directory-readme; pipeline-test-parent; enforceability-boundary
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; no-dedicated-pipeline-suite-established; distributed-negative-coverage-confirmed
owners: OWNER_TBD — QA steward · Pipeline steward · Pipeline-spec steward · Domain pipeline stewards · Connector steward · Contract/schema steward · Policy steward · Evidence/receipt steward · Release steward · Security reviewer · CI steward · Docs steward
created: 2026-07-06
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doctrine; tests; pipelines; no-network-default; synthetic-only; lifecycle-governed; non-publisher; evidence-bound; policy-gated; receipt-aware; correction-aware; rollback-aware; no-publication
current_path: tests/pipelines/README.md
truth_posture: CONFIRMED target README, Directory Rules, canonical tests root, pipelines root, pipeline_specs root, runtime/pipelines README, pipelines_core namespace README, representative placeholder pipeline modules, minimal empty-stage soil pipeline spec, pipeline/connector non-publisher policy test, Makefile test target limited to tests/schemas plus tests/contracts, TODO-only policy workflow, checked absence of tests/pipelines/conftest.py, tests/pipelines/test_pipelines.py, tests/pipelines/pytest.ini, and tests/pipeline_specs/README.md, and bounded search that did not establish a dedicated tests/pipelines executable suite / PROPOSED shared pipeline behavior case contract, lifecycle transition matrix, spec-to-implementation agreement checks, source-role preservation, deterministic transform and idempotency tests, declared side-effect and filesystem sandbox rules, receipt-candidate assertions, watcher non-publisher cases, correction and rollback cases, substantive CI, zero-collection failure, and promotion blocking / CONFLICTED central tests/pipelines ownership versus package-local and domain-local pipeline test homes for specific code; pipeline_specs declaring tests/pipeline_specs as a related path while that README is absent; pipeline root documentation describing broad executable lanes while sampled Python files remain placeholders / UNKNOWN exhaustive pipeline implementation inventory, dynamic test collection, active consumers, accepted runner, full spec inventory, current pass rates, coverage, mutation score, runtime, flake rate, emitted receipt instances, deployment use, and promotion dependency / NEEDS VERIFICATION owners, lane-retention rule, package-local versus root test placement, accepted pipeline/spec contract, lifecycle-state representation, reason-code vocabulary, receipt schema bindings, no-network mechanism, filesystem sandbox, sensitive-fixture review, CI ownership, artifact retention, and migration plan
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 7bf6f95e531300dd421a0e871fdba7a48f5485e6
  target_prior_blob: ae89298b39b7d0a7e3e0c2fb4220df88cefa0232
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    tests_root_readme: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
    pipelines_root_readme: 9fb38acf5a67ca43608617d73a273d06f5f84db5
    pipeline_specs_root_readme: 3a6599898606126604298a281de53e39fdba98ce
    runtime_pipelines_readme: 08d50e84b9df765f564f92e6e7d4d9627ce90818
    pipelines_core_namespace_readme: f1b069c91289890f371a2bd640dba31d7432659e
    roads_rail_trade_generalize_placeholder: 8f47d77d248d73474caae895c170a9ec4b5042f9
    roads_rail_trade_ingest_placeholder: 6b08b2d1e5478db96bc835b8d4f5cf0bfd43ebca
    soil_ingest_spec: 1507c2d908da99646aac536a57bb7217c1d71ec8
    pipeline_connector_non_publisher_test: c6164787bc848eb2347c347af203d76afae37a2b
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    policy_test_workflow: 2bba88bb018600f54995d06b03cac02145b96fe7
  direct_lane_files_confirmed:
    - tests/pipelines/README.md
  checked_absent_paths:
    - tests/pipelines/conftest.py
    - tests/pipelines/test_pipelines.py
    - tests/pipelines/pytest.ini
    - tests/pipeline_specs/README.md
  bounded_inventory_note: repository search and representative path checks did not establish a dedicated executable suite under tests/pipelines; this does not prove absence from history, ignored files, generated files, branch-local files, dynamically collected suites, package-local tests, connector-local tests, or external systems
related:
  - ../README.md
  - ../policy/test_pipeline_connector_non_publisher.py
  - ../domains/
  - ../release/
  - ../e2e/
  - ../schemas/
  - ../contracts/
  - ../fixtures/README.md
  - ../../pipelines/README.md
  - ../../pipeline_specs/README.md
  - ../../runtime/pipelines/README.md
  - ../../packages/pipelines-core/src/pipelines_core/README.md
  - ../../fixtures/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../data/receipts/pipeline/
  - ../../data/proofs/
  - ../../release/
  - ../../docs/doctrine/directory-rules.md
  - ../../Makefile
notes:
  - "v0.2 replaces a planning-heavy proposed test tree with a commit-pinned current-state and routing boundary."
  - "The direct tests/pipelines lane is README-only at the bounded snapshot."
  - "Pipeline-related negative coverage exists under tests/policy, but no dedicated pipeline behavior suite was established."
  - "Sampled executable pipeline modules and the shared pipelines_core package remain placeholders; sampled pipeline specs are minimal scaffolds."
  - "The current Makefile default test target excludes tests/pipelines."
  - "This revision changes documentation only and creates no executable test, fixture, pipeline, spec, schema, contract, policy, receipt, proof, release object, workflow behavior, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Pipeline suite: not established" src="https://img.shields.io/badge/pipeline__suite-not__established-orange">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Lifecycle: governed" src="https://img.shields.io/badge/lifecycle-governed-blue">
  <img alt="Publication authority: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Routing](#placement-and-routing-law) · [System under test](#pipeline-system-under-test) · [Case contract](#minimum-pipeline-test-case-contract) · [Lifecycle](#lifecycle-and-promotion-invariants) · [Specs](#pipeline-spec-and-implementation-agreement) · [Determinism](#determinism-idempotency-replay-and-no-op) · [Inputs](#fixtures-source-roles-and-sensitive-material) · [Effects](#filesystem-network-security-and-side-effects) · [Receipts](#receipts-proofs-evidence-and-observability) · [Watchers](#watchers-connectors-and-non-publisher-rules) · [Failure](#failure-cancellation-retry-and-partial-state) · [Correction](#correction-withdrawal-and-rollback) · [Outcomes](#test-results-pipeline-outcomes-and-release-decisions) · [Runner](#runner-ci-and-promotion-boundary) · [Migration](#migration-deprecation-and-rollback-of-this-lane) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Evidence snapshot:** `main@7bf6f95e531300dd421a0e871fdba7a48f5485e6`
> **Prior target blob:** `ae89298b39b7d0a7e3e0c2fb4220df88cefa0232`
> **Direct lane:** `tests/pipelines/README.md` only at the bounded snapshot
> **Checked absent:** `conftest.py`, `test_pipelines.py`, `pytest.ini`, and `tests/pipeline_specs/README.md`
> **Makefile:** `make test` runs `tests/schemas` and `tests/contracts`, not this lane
> **Dedicated pipeline workflow:** not established by the inspected paths and bounded search

`tests/pipelines/` is currently a documented pipeline-test boundary, not an established executable suite.

### Safe conclusions

- **CONFIRMED:** `tests/pipelines/README.md` exists.
- **CONFIRMED:** the canonical `tests/` root assigns pipeline behavior tests to this lane.
- **CONFIRMED:** `pipelines/` is the executable-logic root and `pipeline_specs/` is the declarative-spec root.
- **CONFIRMED:** the inspected direct lane contains no checked `conftest.py`, representative test module, or lane-local pytest configuration.
- **CONFIRMED:** the sampled `roads-rail-trade` pipeline Python files are placeholder docstrings, not functional pipeline implementations.
- **CONFIRMED:** the sampled soil ingest spec contains an empty `stages` list.
- **CONFIRMED:** the shared `pipelines_core` namespace is a placeholder with no established functional API or package-local tests.
- **CONFIRMED:** a static non-publisher guard exists in `tests/policy/` and inspects both `connectors/` and `pipelines/`.
- **CONFIRMED:** the default Makefile test target excludes `tests/pipelines`.
- **PROPOSED:** shared cross-cutting pipeline behavior tests may live here after placement review.
- **UNKNOWN:** complete executable pipeline inventory, dynamic test collection, pass rates, coverage, runtime, flakes, receipt emission, deployment use, and release-gate dependency.
- **NEEDS VERIFICATION:** the accepted test-home split between this lane, package-local tests, connector-local tests, and domain-local tests.

### Maturity matrix

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Parent README | `CONFIRMED` | A pipeline-test boundary exists. |
| Direct executable pipeline tests | `NOT ESTABLISHED` | No representative direct module was found. |
| Lane-local harness | `NOT FOUND AT CHECKED PATHS` | No independent fixture or collection contract is established. |
| Shared pipeline implementation | `MIXED / PLACEHOLDER-HEAVY` | Root and child READMEs exist; sampled code is placeholder-only. |
| Shared `pipelines_core` API | `UNRATIFIED PLACEHOLDER` | Namespace exists without functional API or tests. |
| Pipeline specs | `CONFIRMED SCAFFOLDS` | Declarative files exist; sampled spec has no stages. |
| Non-publisher guard | `CONFIRMED EXECUTABLE` | Static write-context guard exists under `tests/policy/`. |
| Default Makefile collection | `NOT ESTABLISHED` | Current `test` target excludes this lane. |
| Dedicated pipeline CI | `NOT ESTABLISHED` | No substantive dedicated workflow was verified. |
| Current pass rate / coverage | `UNKNOWN` | No dedicated report was verified. |
| Promotion blocking | `UNKNOWN` | No verified promotion dependency targets this lane. |

### Truth labels

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current repository files, representative path checks, or executable code. |
| `PROPOSED` | A test contract, path, or procedure not yet established in implementation. |
| `CONFLICTED` | Repository structure or documentation exposes competing ownership or naming choices. |
| `UNKNOWN` | Not established by the inspected repository, CI, runtime, or release evidence. |
| `NEEDS VERIFICATION` | Checkable, but unresolved strongly enough to act as fact. |
| `DENY` | Disallowed because it bypasses a responsibility boundary, lifecycle gate, policy, evidence, or release control. |

[Back to top](#top)

---

## Purpose

`tests/pipelines/` is the parent boundary for **cross-cutting executable pipeline behavior proof**.

A complete pipeline behavior test proves that bounded inputs move through the intended pipeline control path while preserving KFM governance:

```text
synthetic or approved fixture input
  -> source and run identity checks
  -> declared pipeline spec/profile
  -> executable pipeline step
  -> lifecycle transition or blocker
  -> schema / contract / source-role / policy checks
  -> receipt candidate and observability output
  -> catalog / triplet / publish-readiness handoff
  -> correction / withdrawal / rollback posture
  -> finite test result
```

A passing pipeline test means only that the scoped control behaved as expected. It does **not** prove:

- source authority;
- factual truth;
- evidence closure;
- policy approval;
- review approval;
- release approval;
- publication;
- deployed behavior;
- current data;
- legal status;
- title, ownership, consent, or sovereignty;
- a successful rollback in production.

### Primary users

- pipeline and pipeline-spec maintainers;
- QA and test stewards;
- domain stewards with executable pipeline lanes;
- connector, evidence, policy, receipt, release, security, and CI reviewers;
- maintainers deciding whether a test belongs here, in a domain lane, in a package, or with a connector.

### Non-goals

This README does not:

- create pipeline code;
- create a pipeline spec;
- establish a runner;
- define an accepted lifecycle state machine;
- approve a RunReceipt schema;
- authorize network access;
- create release or publication authority;
- claim current test coverage.

[Back to top](#top)

---

## Authority boundary

`tests/pipelines/` owns test organization and enforceability assertions only.

| Responsibility | Authority home | This lane's role |
|---|---|---|
| Test assertions | `tests/` | May own shared pipeline behavior tests. |
| Executable pipeline logic | `pipelines/` | System under test; not implemented here. |
| Declarative pipeline intent | `pipeline_specs/` | Configuration under test; not authored here. |
| Shared pipeline library | `packages/pipelines-core/` if retained | Package under test; package API remains unratified. |
| Runtime coordination | `runtime/` | Optional support under test; not pipeline authority. |
| Connector/source access | `connectors/` | Admission boundary; not duplicated here. |
| Object meaning | `contracts/` | Tested, not rewritten here. |
| Machine shape | `schemas/` | Validated, not defined here. |
| Policy and admissibility | `policy/` | Exercised, not invented here. |
| Source descriptors | source registry | Referenced by stable synthetic or reviewed IDs. |
| Lifecycle state and outputs | governed `data/` roots | Simulated or sandboxed; not stored here. |
| Receipts and proofs | governed receipt/proof roots | Shape and linkage may be tested; no actual authority is created here. |
| Release, correction, rollback | `release/` | Readiness and denial tested; approvals remain outside tests. |
| CI orchestration | `.github/workflows/` | Calls tests; green status is not authority. |

### Anti-collapse rules

This lane must not collapse:

```text
pipeline test PASS -> source truth
pipeline run SUCCESS -> release approval
publish-readiness -> publication
rollback-readiness -> rollback approval
schema-valid output -> policy permission
fixture -> evidence
receipt candidate -> receipt authority
ValidationReport -> EvidenceBundle
catalog projection -> public catalog
triplet projection -> graph truth
watcher signal -> source admission
runtime summary -> evidence
README -> implementation
workflow success -> substantive coverage
```

### No shadow implementation

Tests may use minimal fakes, adapters, and harnesses, but they must not become:

- a second pipeline engine;
- a second spec registry;
- a hidden connector;
- an unreviewed lifecycle writer;
- a policy evaluator with divergent rules;
- a receipt or proof store;
- a release controller;
- a public API.

[Back to top](#top)

---

## Confirmed current state

### Direct test lane

```text
tests/pipelines/
└── README.md
```

The bounded inspection did not establish additional direct files.

### Adjacent implementation and control surfaces

```text
pipelines/                                      # executable-logic responsibility root
pipeline_specs/                                 # declarative-spec responsibility root
packages/pipelines-core/src/pipelines_core/     # placeholder shared namespace
runtime/pipelines/                              # README-only runtime coordination boundary
tests/policy/test_pipeline_connector_non_publisher.py
```

### Sampled implementation evidence

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| `pipelines/README.md` | v0.2 governed root contract | Root responsibility is documented. |
| `pipelines/domains/roads-rail-trade/generalize_for_public.py` | placeholder docstring only | No generalization behavior is established. |
| `pipelines/domains/roads-rail-trade/ingest_stb_class1.py` | placeholder docstring only | No STB ingest behavior is established. |
| `pipeline_specs/soil/ingest.yaml` | name, version, empty `stages` | Spec path exists; executable stage contract is absent. |
| `pipelines_core/__init__.py` | empty | No public package API is established. |
| `pipelines_core/core.py` | comment-only placeholder | No shared helper behavior is established. |
| `runtime/pipelines/README.md` | README-only | No runtime-pipeline implementation or dedicated tests established. |
| policy non-publisher test | executable static scan | Certain direct publish-target write contexts are rejected. |

### What current evidence does not establish

- a complete recursive pipeline code inventory;
- any pipeline that executes end to end;
- a canonical pipeline request/response contract;
- spec-to-code binding;
- actual lifecycle storage;
- actual receipt emission;
- successful catalog or triplet closure;
- current source ingestion;
- production scheduling;
- network behavior;
- deployment;
- operational rollback;
- dedicated pipeline test collection.

[Back to top](#top)

---

## Placement and routing law

### Directory Rules basis

Where a test lives is determined by the **primary assertion responsibility**, not merely by the word “pipeline.”

| Test concern | Preferred owner | Reason |
|---|---|---|
| Shared lifecycle transition helper used across pipelines | `tests/pipelines/` | Cross-cutting pipeline behavior. |
| Domain-specific pipeline behavior | `tests/domains/<domain>/` | Domain owns meaning, sensitivity, and expected behavior. |
| Connector admission/fetch behavior | connector-local tests | Connector owns upstream access and source admission. |
| Shared package unit behavior | package-local tests or accepted package test lane | Package owns its public API and internal invariants. |
| Pipeline spec schema shape | `tests/schemas/` | Machine shape is the primary assertion. |
| Pipeline spec semantic meaning | `tests/contracts/` or accepted spec contract lane | Contract semantics are primary. |
| Policy denial or non-publisher rule | `tests/policy/` | Policy/boundary enforcement is primary. |
| Validator behavior | `tests/validators/` | Reusable validator implementation is primary. |
| Release/promotion gate behavior | `tests/release/` | Release control is primary. |
| Public API or UI behavior | API/UI test lane | Public carrier boundary is primary. |
| End-to-end composed flow | `tests/e2e/` | Cross-root composition is primary. |
| Multi-domain pipeline composition | accepted cross-domain test lane | No one domain should own the shared relation. |
| Truly cross-cutting shared pipeline orchestration | `tests/pipelines/` | This is the residual canonical use case. |

### Admission test for this lane

A test belongs here only when all are true:

1. the primary system under test is executable pipeline behavior;
2. the assertion spans more than one package or domain-local implementation concern;
3. moving it to schema, contract, policy, release, connector, API, E2E, package, or domain ownership would obscure the true responsibility;
4. the test does not duplicate an existing assertion;
5. fixture and side-effect boundaries are explicit;
6. the test remains subordinate to lifecycle, evidence, policy, and release authorities;
7. an owner and rollback path are identified.

### Denied placements

Do not place here:

- all negative tests merely because a pipeline is involved;
- connector fetch tests;
- domain semantics;
- policy rules;
- schema definitions;
- fixture collections;
- release manifests;
- actual receipt or proof instances;
- generated pipeline output;
- production data;
- deployment scripts;
- secrets;
- live service credentials.

[Back to top](#top)

---

## Pipeline system under test

A pipeline test should name the exact system under test.

### Candidate system classes

| Class | Example responsibility | Test focus |
|---|---|---|
| Admission runner | Convert connector result into governed intake candidate | identity, source role, rights, quarantine route |
| Normalizer | Convert admitted shape into canonical candidate shape | determinism, transform receipt, no authority inflation |
| Validator coordinator | Run machine and semantic checks | finite blockers, no silent success |
| Catalog closer | Assemble catalog candidate | evidence, source role, policy, integrity closure |
| Triplet projector | Build derived relation candidate | provenance, no graph-truth inflation |
| Publish-readiness checker | Evaluate release prerequisites | readiness only, no release mutation |
| Rollback-readiness checker | Validate prior target and correction state | readiness only, no silent history edit |
| Watcher | Detect upstream change | non-publisher, no automatic promotion |
| Receipt helper | Build receipt candidate | identity, inputs, outputs, blockers, hashes |
| Shared pipeline-control helper | idempotency, replay, transition checks | deterministic bounded behavior |
| Runtime handoff adapter | request optional interpretive support | minimized context, finite outcomes, no evidence creation |

### Required identity

Every case should identify:

- pipeline or helper ID;
- pipeline version;
- spec/profile ID and version;
- source descriptor refs;
- source roles;
- run ID;
- fixture ID;
- time controls;
- expected input and output lifecycle state;
- expected outcome;
- expected side effects;
- prohibited side effects.

### No unnamed integration

A test that invokes “the pipeline” without specifying the code path, spec, inputs, and authority boundaries is not reviewable enough for trust-bearing use.

[Back to top](#top)

---

## Minimum pipeline test case contract

Every substantive case should declare at least:

```yaml
case_id: pipe-case-001
owner: OWNER_TBD
system_under_test:
  path: pipelines/example/runner.py
  symbol: run
  version_ref: synthetic-or-pinned
spec:
  path: pipeline_specs/example/profile.yaml
  profile_id: example-profile
  version: 1
inputs:
  fixture_refs:
    - fixture://example/input
  source_descriptor_refs:
    - source://example
  source_roles:
    - primary
  initial_lifecycle_state: RAW
controls:
  network: denied
  clock: fixed
  random_seed: 0
  filesystem: temporary-sandbox
  environment: allowlisted
expected:
  test_result: PASS
  pipeline_outcome: BLOCKED
  next_lifecycle_state: QUARANTINE
  reason_codes:
    - RIGHTS_UNKNOWN
  writes:
    - sandbox/receipts/run.json
  forbidden_writes:
    - data/published/
    - release/
  emitted_candidates:
    - RunReceiptCandidate
  must_not_emit:
    - ReleaseManifest
    - EvidenceBundle
cleanup:
  required: true
rollback:
  integration_revert: documented
```

### Required fields

1. stable case identity;
2. named system under test;
3. named spec or explicit “no spec” reason;
4. exact fixture and source refs;
5. source-role expectations;
6. fixed time and randomness;
7. network posture;
8. filesystem sandbox;
9. expected test result;
10. expected pipeline outcome;
11. expected lifecycle state;
12. expected reason codes;
13. allowed writes;
14. forbidden writes;
15. expected candidate object families;
16. forbidden authority objects;
17. cleanup;
18. rollback of the test integration.

### Positive and negative controls

Trust-bearing tests should include:

- at least one supported positive control;
- at least one invalid or denied case;
- one changed input that proves the assertion is selective;
- explicit proof that the test does not always pass or always reject.

[Back to top](#top)

---

## Lifecycle and promotion invariants

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

### Required transition assertions

| Transition | Required test posture |
|---|---|
| source result → RAW | identity, source descriptor, rights, provenance, checksum, and receipt candidate |
| RAW → WORK | declared transform or review purpose |
| RAW/WORK → QUARANTINE | finite blocker, reason, owner, and recovery path |
| WORK → PROCESSED | schema, contract, source-role, temporal, geometry, and domain checks |
| PROCESSED → CATALOG/TRIPLET | evidence, policy, integrity, and projection provenance |
| CATALOG/TRIPLET → release candidate | review and release prerequisites assembled |
| release candidate → PUBLISHED | **not performed by ordinary pipeline tests**; release authority is separate |
| PUBLISHED → corrected/superseded/withdrawn | release and correction controls, not silent mutation |

### Forbidden lifecycle behavior

Tests must fail when a pipeline:

- writes directly from RAW or WORK into a published surface;
- treats quarantine as a warning-only state;
- discards blocker reasons;
- silently promotes a failed candidate;
- rewrites a released object without correction lineage;
- constructs a release manifest as a side effect of ordinary processing;
- treats a filesystem move as promotion;
- overwrites a rollback target;
- deletes historical evidence or receipts to make a run pass.

### Publication denial

A pipeline may produce:

- candidates;
- validation reports;
- blocker reports;
- receipt candidates;
- proof candidates;
- catalog/triplet candidates;
- publish-readiness reports;
- rollback-readiness reports.

It may not, through this test lane, approve or perform publication.

[Back to top](#top)

---

## Pipeline spec and implementation agreement

`pipeline_specs/` owns declarative intent. `pipelines/` owns executable behavior.

### Agreement checks

A future substantive suite should verify:

- target implementation path exists;
- spec version is supported;
- declared stages map to real executable stages;
- undeclared stages do not run;
- required source descriptors resolve;
- source roles match the spec;
- lifecycle input/output states match;
- policy and review gates are not omitted;
- fixture refs exist and are admitted;
- receipt expectations match emitted candidates;
- release-readiness and rollback-readiness behavior match the spec;
- unknown fields and incompatible versions fail closed;
- hidden defaults do not weaken risk-bearing controls.

### Sampled current limitation

The inspected `pipeline_specs/soil/ingest.yaml` contains:

```yaml
name: soil-ingest
version: 1
stages: []
```

This proves a file exists. It does not prove:

- a stage contract;
- implementation binding;
- source admission;
- execution;
- validation;
- lifecycle transition;
- receipt emission;
- CI coverage.

### Spec drift

Tests should distinguish:

| Drift | Expected behavior |
|---|---|
| spec names nonexistent implementation | fail |
| implementation runs undeclared stage | fail |
| implementation ignores required gate | fail |
| spec omits required risk field | fail closed |
| spec version unsupported | fail with stable reason |
| harmless documentation field changes | accept if contract allows |
| spec and implementation hash mismatch | block or require review |
| stale spec points to retired source | block |

### No spec laundering

A valid spec is not evidence that:

- code exists;
- code ran;
- data passed;
- a receipt exists;
- policy allowed publication;
- release occurred.

[Back to top](#top)

---

## Determinism, idempotency, replay, and no-op

### Deterministic inputs

Default tests must control:

- clock;
- timezone;
- random seed;
- environment variables;
- locale;
- ordering;
- filesystem root;
- network;
- concurrency where material;
- source-vintage metadata;
- fixture hashes.

### Deterministic outputs

For identical admitted inputs and configuration, tests should expect stable:

- object IDs where identity is deterministic;
- stage ordering;
- reason codes;
- blocker ordering;
- normalized payloads;
- receipt-candidate fields;
- hashes;
- no-op decisions;
- log event classes.

Volatile values must be isolated and normalized explicitly.

### Idempotency

A repeated run should not:

- duplicate canonical candidates;
- duplicate published objects;
- create conflicting receipts;
- mutate prior output unexpectedly;
- change IDs without a declared identity change;
- bypass validation because a prior run succeeded.

### Replay

Replay tests should verify:

- pinned inputs;
- pinned spec/profile version;
- pinned code version or declared compatibility;
- fixed clock behavior;
- stable output or explained drift;
- no network;
- no use of current mutable source state;
- preserved reason codes and blocker posture.

### No-op

When no material change exists, the pipeline should produce an explicit no-op posture rather than:

- rewriting output;
- regenerating different IDs;
- creating a false “new data” signal;
- triggering release;
- erasing prior blockers.

### Mutation sensitivity

A trust-bearing case should change when the relevant input or gate changes. If removing the tested guard does not fail the test, the test is too weak.

[Back to top](#top)

---

## Fixtures, source roles, and sensitive material

### Fixture homes

| Fixture class | Preferred home | This lane's role |
|---|---|---|
| test-local compact fixture | `tests/fixtures/` or lane-local inline value | consume |
| shared cross-cutting fixture | `fixtures/` | consume |
| domain-owned fixture | `fixtures/domains/<domain>/` | consume |
| pipeline-spec fixture | accepted spec fixture lane | consume |
| real source data | governed lifecycle store | never default test material |
| actual receipt/proof/release object | governed trust/release root | do not copy here |

### Fixture requirements

Fixtures should be:

- synthetic;
- compact;
- deterministic;
- public-safe;
- reviewable;
- explicitly marked as test-only;
- schema-bound where applicable;
- linked to the case;
- paired with expected outcomes.

### Source-role preservation

Tests must verify that pipelines do not silently change:

- primary;
- corroborating;
- contextual;
- restricted;
- modeled;
- derived;
- observed;

or any accepted project vocabulary.

A contextual or modeled source cannot become an observed primary source merely because a pipeline normalized it.

### Sensitive domains

For living-person, DNA/genomic, land ownership, archaeology, rare species, critical infrastructure, and other high-risk material:

- use synthetic canaries only;
- deny exact sensitive locations by default;
- test generalization/redaction obligations;
- test consent and revocation where applicable;
- test rights and sovereignty uncertainty;
- verify denial responses do not leak protected inputs;
- avoid realistic private identifiers;
- require appropriate reviewers.

### No fixture authority

A fixture is not:

- a source record;
- an EvidenceBundle;
- a receipt;
- a policy decision;
- a review record;
- a release object;
- public truth.

[Back to top](#top)

---

## Filesystem, network, security, and side effects

### Filesystem sandbox

Tests should execute in a temporary sandbox with an allowlisted write set.

Required assertions:

- all writes occur inside the sandbox;
- no writes target repository-governed data roots unless an explicit synthetic adapter intercepts them;
- no symlink escape;
- no absolute-path escape;
- no parent traversal;
- no modification of checked-in fixtures;
- no modification of source code;
- cleanup occurs after success and failure.

### Forbidden direct write targets

Ordinary pipeline tests should reject writes to:

```text
data/published/
release/
data/catalog/                 # unless a synthetic sandbox adapter owns the path
data/triplets/                # unless a synthetic sandbox adapter owns the path
data/proofs/
data/receipts/                # actual trust store; use sandbox candidate output
```

The confirmed policy test already scans connectors and pipelines for selected direct publish-target write contexts. That check is useful but limited: it is a static heuristic, not full runtime side-effect proof.

### Network posture

Default suite:

```text
network = DENIED
```

Tests should fail on:

- HTTP/HTTPS;
- DNS;
- raw sockets;
- cloud SDK calls;
- database connections;
- object-store access;
- remote model calls;
- live map/tile/geocoder services;
- package installation during test execution;
- implicit credential lookup.

### Explicit network integration tests

A live integration test requires:

- separate marker and workflow;
- explicit opt-in;
- approved source and rights posture;
- rate limits;
- credentials from secure CI;
- sanitized logs;
- bounded cost;
- retry and timeout rules;
- no promotion or publication side effects;
- rollback and disable path.

### Secrets

Never store:

- API keys;
- passwords;
- tokens;
- private endpoint credentials;
- cookies;
- connection strings;
- private certificates;
- production identifiers.

### Process and concurrency controls

Tests should manage:

- subprocess allowlist;
- timeouts;
- cancellation;
- cleanup;
- lock files;
- parallel write isolation;
- race conditions;
- deterministic worker count when ordering matters.

[Back to top](#top)

---

## Receipts, proofs, evidence, and observability

### Receipt candidate assertions

A pipeline test may assert that a candidate receipt contains:

- run ID;
- pipeline ID and version;
- spec/profile ID and version;
- code ref;
- input refs and hashes;
- source descriptor refs;
- source roles;
- timestamps and time kinds;
- stage results;
- validation results;
- policy results;
- blockers;
- output refs and hashes;
- no-op status;
- retry/cancellation status;
- correction and rollback refs.

### Receipt non-authority

A test-created receipt candidate is not:

- an accepted RunReceipt;
- proof of source truth;
- an EvidenceBundle;
- release approval;
- publication evidence.

### Evidence discipline

Pipelines may reference or require evidence. Generic pipeline helpers must not fabricate EvidenceBundles.

Tests should fail when:

- an evidence-dependent candidate lacks an EvidenceRef;
- the EvidenceRef cannot resolve in the synthetic harness;
- evidence scope does not match the claim;
- evidence is stale or withdrawn;
- generated text is used as evidence;
- a receipt is substituted for evidence.

### Proof separation

A proof candidate may summarize checks, but tests must preserve:

```text
receipt != proof
proof != evidence
evidence != policy permission
policy permission != release
release != truth
```

### Observability

Logs and events should be:

- structured;
- bounded;
- sanitized;
- free of secrets and sensitive payloads;
- correlated by run ID;
- stable enough for assertions;
- explicit about stage and outcome;
- non-authoritative.

[Back to top](#top)

---

## Watchers, connectors, and non-publisher rules

### Connector boundary

Connectors own source access and admission behavior. Pipeline tests should consume synthetic connector results rather than reimplement connector clients.

### Watcher invariant

Watchers may:

- detect change;
- compare source metadata;
- propose refresh;
- produce a material-change candidate;
- emit a notification or review item.

Watchers must not:

- admit a source automatically;
- write PUBLISHED output;
- approve policy;
- create evidence;
- release data;
- override quarantine;
- bypass review.

### Confirmed current guard

`tests/policy/test_pipeline_connector_non_publisher.py` scans connector and pipeline files for selected write contexts near:

- `data/catalog`;
- `data/published`;
- `release/`.

This is **CONFIRMED executable coverage**, but its limitations must remain visible:

- text-pattern based;
- selected file extensions only;
- selected write-call patterns only;
- selected target strings only;
- no runtime execution;
- no symlink or indirect path analysis;
- no cloud/database write detection;
- no guarantee that all pipeline files are functional.

### Required future behavior tests

Add behavioral tests for:

- watcher no-op;
- watcher material change;
- connector result rejected by source-role gate;
- quarantined input not promoted;
- indirect write attempt blocked;
- release adapter unavailable;
- duplicate refresh idempotency;
- stale source handling;
- source withdrawal propagation.

[Back to top](#top)

---

## Failure, cancellation, retry, and partial state

### Failure classes

| Class | Example | Expected posture |
|---|---|---|
| input invalid | malformed fixture | validation failure |
| source unresolved | missing descriptor | blocked / error |
| rights unknown | no permission basis | quarantine / deny |
| sensitivity unresolved | unsafe precision | quarantine / deny |
| schema failure | shape invalid | blocked |
| contract failure | semantics invalid | blocked |
| policy denial | prohibited use | deny |
| evidence missing | unresolved EvidenceRef | abstain / blocked |
| stage exception | implementation error | error with cleanup |
| timeout | stage exceeds budget | error / retry-eligible |
| cancellation | operator or deadline cancels | cancelled with receipt candidate |
| partial failure | some stages complete | partial state, no promotion |
| output collision | deterministic identity conflict | blocked |
| write violation | undeclared path | test failure |
| network attempt | external call in default suite | test failure |

### Atomicity

Tests should verify either:

- atomic commit after all required checks; or
- explicit partial state with resumable/recoverable posture.

They must reject hidden partial writes.

### Retries

Retry tests should verify:

- finite maximum;
- backoff policy;
- retryable reason classes;
- non-retryable policy denials;
- idempotent writes;
- no duplicate receipts or candidates;
- cancellation propagation;
- final outcome after exhaustion.

### Cancellation

Cancellation should:

- stop future stages;
- avoid promotion;
- record completed stages;
- clean up temporary resources;
- preserve recoverable state;
- emit bounded reason;
- not masquerade as success.

### Error leakage

Errors must not expose:

- secrets;
- private source payloads;
- exact sensitive coordinates;
- internal policy details that create exploitation risk;
- filesystem paths beyond safe review needs;
- production connection data.

[Back to top](#top)

---

## Correction, withdrawal, and rollback

### Correction cases

Tests should cover:

- input correction before processing;
- corrected source descriptor;
- corrected source role;
- corrected geometry or time;
- corrected catalog candidate;
- evidence supersession;
- policy change;
- release correction propagation.

### Withdrawal cases

A withdrawn source or evidence item should:

- stop new promotion;
- invalidate dependent candidates where required;
- preserve audit history;
- surface finite reason;
- avoid deleting history silently.

### Rollback-readiness

Pipeline tests may verify:

- prior release target exists;
- rollback target identity is stable;
- affected outputs are enumerated;
- correction and withdrawal dependencies are known;
- rollback plan is reversible;
- no unrelated state is touched.

They may not approve or execute production rollback.

### Test integration rollback

Every new pipeline test integration should document:

- files added;
- runner changes;
- workflow changes;
- fixture changes;
- artifact paths;
- how to revert;
- how to confirm the prior suite is restored.

[Back to top](#top)

---

## Test results, pipeline outcomes, and release decisions

Do not collapse vocabularies.

### Test framework results

```text
PASS
FAIL
SKIP
XFAIL
ERROR
```

These describe the test process.

### Pipeline run outcomes

The accepted vocabulary is **NEEDS VERIFICATION**. Candidate examples include:

```text
SUCCESS
PARTIAL
FAIL
BLOCKED
QUARANTINED
NOOP
CANCELLED
ERROR
```

A README must not silently canonize an enum. Tests should bind to accepted contracts and schemas.

### Runtime response outcomes

Where a governed runtime envelope is involved:

```text
ANSWER
ABSTAIN
DENY
ERROR
```

These are not pipeline run outcomes and not pytest statuses.

### Policy decisions

Policy vocabulary may include:

```text
ALLOW
RESTRICT
DENY
HOLD
ERROR
```

Use only accepted policy contracts.

### Release states

```text
candidate
approved
published
corrected
superseded
withdrawn
rolled_back
```

Exact vocabulary remains contract-bound.

### Required non-collapse assertions

- pytest `PASS` does not mean pipeline `SUCCESS`;
- pipeline `SUCCESS` does not mean policy `ALLOW`;
- policy `ALLOW` does not mean release approval;
- release approval does not prove claim truth;
- runtime `ANSWER` does not mean pipeline success;
- `BLOCKED` is not necessarily an error;
- `QUARANTINED` is not publication;
- `NOOP` is not missing execution evidence.

[Back to top](#top)

---

## Runner, CI, and promotion boundary

### Current state

No accepted direct runner for `tests/pipelines/` was established.

A candidate future command is:

```bash
python -m pytest tests/pipelines -q
```

It remains `PROPOSED / NEEDS VERIFICATION`.

The current Makefile default test target is:

```bash
python -m pytest tests/schemas tests/contracts -q
```

It does not establish pipeline-test collection.

### Activation requirements

Before any direct runner is described as authoritative:

1. substantive tests exist;
2. collection count is nonzero;
3. a positive control exists;
4. negative cases exist;
5. fixtures resolve;
6. package imports work;
7. spec bindings are validated;
8. no-network is enforced;
9. filesystem sandboxing is enforced;
10. sensitive canaries are scanned;
11. cleanup is verified;
12. skips and xfails are bounded;
13. exit codes are meaningful;
14. reports are sanitized;
15. owners are assigned.

### Zero collection

A command that collects zero tests must fail in CI.

### CI workflow requirements

A substantive pipeline workflow should:

- install declared dependencies;
- validate collection;
- execute exact test paths;
- report collected/passed/failed/skipped counts;
- enforce no-network;
- use temporary directories;
- preserve sanitized reports only;
- fail on missing fixtures;
- fail on missing required package imports;
- fail on zero collection;
- clean up subprocesses;
- report runtime and flaky retries;
- avoid live source and release side effects.

### TODO and echo workflows

A workflow that only checks out the repository and echoes TODO is a scaffold, not pipeline proof.

### Promotion posture

Once accepted, failures of material lifecycle, evidence, policy, non-publisher, correction, or rollback tests should block promotion.

A passing suite cannot approve promotion.

[Back to top](#top)

---

## Migration, deprecation, and rollback of this lane

### Retention rule

Retain `tests/pipelines/` for truly shared pipeline behavior tests that do not have a clearer package, connector, domain, policy, release, or E2E owner.

### Move when ownership becomes specific

1. identify the owning responsibility;
2. move the test with history;
3. preserve case IDs;
4. update fixture refs;
5. update runner and workflow collection;
6. remove duplicate assertions;
7. compare before/after behavior;
8. document rollback;
9. retain a pointer only if active callers require it.

### Package-local conflict

The correct home for future `pipelines_core` unit tests is unresolved. Options include:

- `packages/pipelines-core/tests/`;
- an accepted centralized package test lane;
- `tests/pipelines/` only for shared integration behavior.

Do not create parallel copies while this remains unresolved.

### Pipeline-spec test conflict

`pipeline_specs/README.md` references `tests/pipeline_specs/`, but the checked README path was absent. Do not create that lane merely to satisfy documentation. Resolve whether spec shape and semantics belong in existing schema/contract lanes or a dedicated accepted lane.

### Retirement

If every executable case gains a clearer owner, `tests/pipelines/` may remain a routing README or be retired through a documented migration.

Do not delete the lane while:

- inbound links remain;
- CI references it;
- fixtures depend on it;
- case IDs remain unresolved;
- migration evidence is incomplete.

### README rollback triggers

Revert or correct this README if it:

- claims a dedicated suite that does not exist;
- treats sampled placeholders as functional implementations;
- centralizes all pipeline-related tests here;
- weakens no-network or lifecycle controls;
- permits direct published/release writes;
- treats readiness as approval;
- creates parallel authority;
- canonizes unaccepted enums or contracts.

[Back to top](#top)

---

## Directory map

### Confirmed bounded map

```text
tests/
├── README.md
├── pipelines/
│   └── README.md
├── policy/
│   └── test_pipeline_connector_non_publisher.py
├── schemas/
└── contracts/

pipelines/
├── README.md
└── domains/
    └── roads-rail-trade/
        ├── generalize_for_public.py     # placeholder docstring
        └── ingest_stb_class1.py         # placeholder docstring

pipeline_specs/
├── README.md
└── soil/
    └── ingest.yaml                      # stages: []

packages/pipelines-core/src/pipelines_core/
├── README.md
├── __init__.py                          # empty
└── core.py                              # comment-only placeholder

runtime/pipelines/
└── README.md
```

This is not a complete recursive inventory.

### Proposed future direct lane

```text
tests/pipelines/
├── README.md
├── conftest.py                          # only if shared harness is accepted
├── _harness/                            # only if no existing package owns it
├── test_lifecycle_transition.py
├── test_quarantine_and_blockers.py
├── test_spec_implementation_agreement.py
├── test_determinism_idempotency_replay.py
├── test_receipt_candidate.py
├── test_watcher_non_publisher.py
├── test_publish_readiness_not_release.py
├── test_correction_withdrawal.py
├── test_rollback_readiness.py
├── test_no_network.py
└── test_declared_side_effects.py
```

Do not create these files merely to complete a tree.

### Material that does not belong here

| Material | Correct responsibility root |
|---|---|
| executable pipeline code | `pipelines/` |
| declarative pipeline specs | `pipeline_specs/` |
| package implementation | `packages/` |
| connector logic | `connectors/` |
| contracts | `contracts/` |
| schemas | `schemas/` |
| policy | `policy/` |
| reusable fixtures | `fixtures/` |
| lifecycle data | `data/` phase roots |
| actual receipts/proofs | governed trust roots |
| release decisions | `release/` |
| public artifacts | released publication roots |
| secrets or production data | never in tests |

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Records the direct lane as README-only without claiming exhaustive absence.
- [x] Records checked-absent harness, representative test, config, and spec-test README paths.
- [x] Separates pipeline implementation, declarative specs, runtime coordination, tests, fixtures, trust artifacts, and release authority.
- [x] Records sampled placeholder implementation and minimal spec evidence.
- [x] Records the `pipelines_core` placeholder state.
- [x] Identifies the confirmed policy non-publisher test without relabeling it as direct pipeline-suite coverage.
- [x] Records Makefile exclusion.
- [x] Replaces schematic placeholder files with routing and admission rules.
- [x] Defines lifecycle, spec agreement, determinism, idempotency, replay, no-op, side-effect, receipt, correction, and rollback requirements.
- [x] Separates test, pipeline, runtime, policy, and release vocabularies.
- [x] Changes documentation only.
- [ ] Record repository-native CI after PR creation.

### Future active direct lane

The lane is not operationally complete until:

- owners are assigned;
- retention and placement are accepted;
- substantive tests exist;
- collection is nonzero;
- positive and negative controls exist;
- shared harness placement is accepted;
- pipeline/spec bindings are real;
- fixtures are synthetic and reviewed;
- lifecycle transitions are asserted;
- network denial is executable;
- filesystem side effects are sandboxed;
- sensitive data cannot leak;
- receipt candidates are schema-bound;
- correction and rollback cases exist;
- the exact suite runs in CI;
- pass rate, runtime, coverage, and flake rate are measured;
- promotion dependency is explicit;
- migration and rollback are documented.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PIPE-TEST-001` | Should this parent retain shared executable tests or remain a routing README? | `NEEDS VERIFICATION` |
| `PIPE-TEST-002` | Is the bounded direct inventory complete? | `NEEDS VERIFICATION` |
| `PIPE-TEST-003` | Are tests dynamically collected from another path? | `UNKNOWN` |
| `PIPE-TEST-004` | What is the accepted split among root, package-local, connector-local, and domain-local pipeline tests? | `NEEDS VERIFICATION` |
| `PIPE-TEST-005` | What is the accepted shared pipeline harness? | `UNKNOWN` |
| `PIPE-TEST-006` | What is the canonical pipeline spec contract and schema? | `NEEDS VERIFICATION` |
| `PIPE-TEST-007` | Should `tests/pipeline_specs/` exist? | `NEEDS VERIFICATION` |
| `PIPE-TEST-008` | What lifecycle-state vocabulary is canonical in executable tests? | `NEEDS VERIFICATION` |
| `PIPE-TEST-009` | What pipeline outcome vocabulary is accepted? | `NEEDS VERIFICATION` |
| `PIPE-TEST-010` | What reason-code vocabulary is accepted? | `NEEDS VERIFICATION` |
| `PIPE-TEST-011` | What RunReceipt contract/schema binds pipeline tests? | `NEEDS VERIFICATION` |
| `PIPE-TEST-012` | How is deterministic identity calculated? | `NEEDS VERIFICATION` |
| `PIPE-TEST-013` | How is no-network enforced? | `UNKNOWN` |
| `PIPE-TEST-014` | How is filesystem sandboxing enforced? | `UNKNOWN` |
| `PIPE-TEST-015` | What source-role vocabulary is accepted? | `NEEDS VERIFICATION` |
| `PIPE-TEST-016` | How are sensitive fixtures reviewed? | `NEEDS VERIFICATION` |
| `PIPE-TEST-017` | What is the accepted runner, and does zero collection fail? | `UNKNOWN` |
| `PIPE-TEST-018` | Which workflow owns pipeline tests? | `UNKNOWN` |
| `PIPE-TEST-019` | Which pipeline tests block promotion? | `UNKNOWN` |
| `PIPE-TEST-020` | What artifacts and retention are allowed? | `NEEDS VERIFICATION` |
| `PIPE-TEST-021` | What are current counts, pass rate, coverage, mutation score, runtime, and flake rate? | `UNKNOWN` |
| `PIPE-TEST-022` | Which pipeline modules are functional rather than placeholders? | `NEEDS VERIFICATION` |
| `PIPE-TEST-023` | Which pipeline specs are active rather than empty scaffolds? | `NEEDS VERIFICATION` |
| `PIPE-TEST-024` | Does `pipelines_core` become a real shared package, and where are its tests? | `NEEDS VERIFICATION` |
| `PIPE-TEST-025` | How are correction, withdrawal, and rollback propagated through active pipelines? | `UNKNOWN` |
| `PIPE-TEST-026` | What is the deprecation trigger for this lane? | `NEEDS VERIFICATION` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| prior target blob `ae89298b…` | `CONFIRMED` | Existing v0.1 pipeline-test intent. | Executable direct suite. |
| Directory Rules `2affb080…` | `CONFIRMED DOCTRINE` | Responsibility-root placement and lifecycle separation. | Current runtime behavior. |
| tests root `5614de99…` | `CONFIRMED ROOT CONTRACT` | `tests/pipelines/` is the documented pipeline behavior lane. | Direct collection or coverage. |
| pipelines root `9fb38acf…` | `CONFIRMED ROOT CONTRACT` | Executable logic belongs under `pipelines/`. | Functional child implementation. |
| pipeline_specs root `3a659989…` | `CONFIRMED ROOT CONTRACT` | Declarative intent belongs under `pipeline_specs/`. | Spec activation or execution. |
| runtime pipelines `08d50e84…` | `CONFIRMED README-ONLY` | Runtime coordination is separate and unimplemented. | Runtime-pipeline behavior. |
| pipelines_core README `f1b069c9…` | `CONFIRMED PLACEHOLDER` | Shared namespace, package metadata, and missing tests/API state. | Functional shared helpers. |
| generalize placeholder `8f47d77d…` | `CONFIRMED PLACEHOLDER` | Sampled pipeline module is documentation-only. | Generalization behavior. |
| ingest placeholder `6b08b2d1…` | `CONFIRMED PLACEHOLDER` | Sampled ingest module is documentation-only. | STB ingest behavior. |
| soil ingest spec `1507c2d9…` | `CONFIRMED MINIMAL SCAFFOLD` | Spec file exists with empty stages. | Executable stages or binding. |
| non-publisher test `c6164787…` | `CONFIRMED EXECUTABLE` | Selected direct publish-target write contexts are rejected. | Full runtime side-effect safety. |
| Makefile `4dc8cf63…` | `CONFIRMED` | Default test target excludes this lane. | Dynamic or external collection. |
| policy workflow `2bba88bb…` | `CONFIRMED TODO SCAFFOLD` | Workflow exists. | Pipeline or policy execution. |
| checked paths and bounded search | `CONFIRMED BOUNDED RESULT` | README-only direct-lane conclusion. | Exhaustive absence across history, branches, ignored files, generators, or external CI. |

### Evidence hierarchy

For implementation claims, prefer:

1. current executable pipeline code;
2. direct tests and collection output;
3. fixtures and schemas;
4. workflow commands and logs;
5. emitted receipts/proofs;
6. release records;
7. repository documentation;
8. planning documents.

README intent cannot outrank code, tests, logs, or generated evidence.

[Back to top](#top)

---

## Maintainer note

Keep pipeline assertions close to the responsibility that owns them. Use this lane only for genuinely shared executable pipeline behavior.

A passing pipeline test is not publication. A successful run is not truth. A publish-readiness result is not release approval. A receipt candidate is not evidence. A static grep is not complete side-effect proof. An empty `stages` list is not a pipeline. A placeholder Python module is not implementation. A green workflow that collects zero tests or echoes TODO is not coverage.

Add one complete, reviewable case at a time with an accepted owner, real system under test, synthetic fixture, positive and negative controls, deterministic execution, no-network enforcement, declared side effects, cleanup, and rollback.

<p align="right"><a href="#top">Back to top</a></p>
