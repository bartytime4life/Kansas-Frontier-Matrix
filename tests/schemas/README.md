<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-schemas-readme
title: tests/schemas/ — Executable Schema Conformance, Fixture Coverage, and Drift Guardrail
type: readme; directory-readme; schema-test-root; json-schema-conformance-contract; fixture-coverage-index; ci-boundary
version: v0.3
status: draft; repository-grounded; executable; pytest-collected; fixture-driven; partial-family-coverage; hydrology-alias-coverage; schema-ci-present; coverage-gaps-visible; non-authoritative; NEEDS VERIFICATION
policy_label: public-doc; tests; schemas; machine-shape; synthetic-only; no-network; fail-closed; coverage-aware; compatibility-aware; trust-spine
owners: OWNER_TBD — QA steward · Schema steward · Contract steward · Fixture steward · Validator steward · Domain stewards · CI steward · Security reviewer · Docs steward
created: 2026-07-07
updated: 2026-08-01
supersedes: v0.2 schema-test boundary guide
current_path: tests/schemas/README.md
truth_posture: CONFIRMED target README and prior blob, canonical tests responsibility root, schema authority root, schemas/tests compatibility index, six directly surfaced executable schema-test modules, focused shared-runner fixture tests, generic top-level fixture harness behavior, bounded Hydrology, Hazards, USDM SourceDescriptor, and water-planning coverage, shared JSON Schema runner, recursive local schema registry, seven-validator aggregate runner, root Makefile schema/test targets, root Python and pytest dependencies, schema-validation workflow, validator-suite workflow, and mixed-maturity v1 schema family index at the pinned snapshot / PROPOSED complete schema inventory contract, recursive family discovery, required fixture manifests, metaschema validation beyond the configured workflow, contract-pairing enforcement, namespace policy, compatibility-lane migration, coverage report, required promotion check, and branch-protection status / CONFLICTED executable ownership under tests/schemas versus README-only compatibility placement under schemas/tests, generic harness top-level family allowlist versus the much broader v1 family tree, direct pytest coverage versus the seven-validator make schemas path, and schema-shape success versus evidence-policy-release truth / UNKNOWN exhaustive ignored/generated test inventory, exact collected case count, hosted pass state, full schema count, full fixture count, dynamic consumers, required-check configuration, promotion dependency, and production behavior / NEEDS VERIFICATION owners, CODEOWNERS, accepted schema family registry, all schema and fixture inventories, every schema-to-contract pairing, every schema-to-validator binding, current hosted logs, correction consumers, and migration plan
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: cb8a46fff89861b8f0ca57c1c29bacf1fec885a5
  prior_blob: 895e892294ac5d81df683e2dcc7cbf4b2ed88308
  direct_test_modules:
    - tests/schemas/test_common_contracts.py
    - tests/schemas/test_evidence_ref_validator.py
    - tests/schemas/test_hydrology_alias_contracts.py
    - tests/schemas/test_kdhe_hab_advisory_snapshot_contracts.py
    - tests/schemas/test_usdm_source_descriptor_contracts.py
    - tests/schemas/test_water_planning_contracts.py
  focused_runner_test:
    - tests/validators/test_jsonschema_runner.py
  compatibility_index:
    - schemas/tests/README.md
  execution_surfaces:
    - Makefile
    - .github/workflows/schema-validation.yml
    - .github/workflows/source-descriptor-validate.yml
    - .github/workflows/validator-suite.yml
  runner_change_evidence:
    runner_prior_blob: ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6
    aggregate_runner_blob: 7595f40bafb70f8eb4af51d73a74923cf77bcd5b
    schema_validation_workflow_prior_blob: fd0e53722b9d8406c5fde052672f760f00f2626b
    source_descriptor_workflow_prior_blob: fc808375a73e0d4ddfdc80fd5f0199a0486c93ce
    validator_suite_workflow_prior_blob: 1694afdd762ce515b53fc8e9d7d51324c2d0929d
    local_result: PASS; 10 focused tests
  shared_validator_surfaces:
    - tools/validators/_common/jsonschema_runner.py
    - tools/validators/_common/local_resolver.py
    - tools/validators/_common/run_all.py
  schema_surfaces:
    - schemas/README.md
    - schemas/contracts/v1/README.md
  bounded_inventory_note: direct connector search and exact path reads establish only the checked snapshot; they do not prove permanent absence from history, ignored files, generated workspaces, branch-local changes, dynamically generated tests, or uninspected paths
related:
  - ../README.md
  - ../contracts/README.md
  - ../fixtures/README.md
  - ../../schemas/README.md
  - ../../schemas/contracts/v1/README.md
  - ../../schemas/tests/README.md
  - ../../contracts/README.md
  - ../../fixtures/README.md
  - ../../tools/validators/README.md
  - ../../tools/validators/_common/README.md
  - ../../tools/validators/_common/jsonschema_runner.py
  - ../../tools/validators/_common/local_resolver.py
  - ../../tools/validators/_common/run_all.py
  - ../validators/test_jsonschema_runner.py
  - ../../Makefile
  - ../../pyproject.toml
  - ../../.github/workflows/schema-validation.yml
  - ../../.github/workflows/source-descriptor-validate.yml
  - ../../.github/workflows/validator-suite.yml
tags: [kfm, tests, schemas, json-schema, draft-2020-12, fixtures, validators, pytest, schema-ids, refs, aliases, hydrology, contracts, ci, drift, coverage, no-parallel-authority]
notes:
  - "v0.3 reconciles the seven-entry aggregate and shared fixture runner with focused regression coverage and current workflow behavior while preserving the schema-test authority boundary."
  - "The generic harness discovers only immediate *.schema.json files in seven hard-coded top-level families and only when a matching fixture directory exists."
  - "The Hydrology alias module explicitly covers decision_envelope, run_receipt, and evidence_bundle aliases with one valid fixture each and one added-property negative."
  - "make test runs tests/schemas plus tests/contracts; make schemas runs seven dedicated validator entry points. These are overlapping but non-identical proof paths."
  - "schema-validation executes make schemas and pytest tests/schemas plus tests/contracts; validator-suite executes focused shared-runner tests, make schemas, and an EvidenceBundle rejection canary."
  - "This README documents paired runner, test, workflow, and generated-receipt changes; it creates no schema, semantic contract, fixture payload, policy, proof, release record, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/schemas/` — Executable Schema Conformance, Fixture Coverage, and Drift Guardrail

> **Purpose.** Prove that selected KFM JSON Schema surfaces load through the repository-local Draft 2020-12 resolver, accept bounded valid fixtures, reject bounded invalid fixtures, preserve alias strictness, and fail visibly when tested shape expectations drift—without turning test success into semantic truth, evidence closure, policy approval, release authority, or public-safety approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Implementation: executable partial" src="https://img.shields.io/badge/implementation-executable__partial-orange">
  <img alt="Runner: pytest" src="https://img.shields.io/badge/runner-pytest-blue">
  <img alt="Schema draft: 2020-12" src="https://img.shields.io/badge/JSON__Schema-2020--12-informational">
  <img alt="Coverage: incomplete" src="https://img.shields.io/badge/coverage-INCOMPLETE-red">
  <img alt="Authority: shape proof only" src="https://img.shields.io/badge/authority-shape__proof__only-purple">
</p>

> [!IMPORTANT]
> `tests/schemas/` owns **executable schema conformance proof**. It does not own schema definitions, semantic contracts, reusable fixtures, validator implementation, policy, evidence, receipts, lifecycle data, release decisions, public payloads, or generated truth.

> [!WARNING]
> Current test and CI surfaces do **not** establish full v1 schema coverage. A schema can be absent from the hard-coded family allowlist, nested below an unscanned directory, missing a matching fixture directory, or represented only by README/scaffold material and therefore receive no direct assertion from the generic harness.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-scope) · [Placement](#placement-and-authority) · [Inventory](#confirmed-repository-inventory) · [Commands](#current-execution-surfaces) · [Generic harness](#generic-contract-fixture-harness) · [Hydrology aliases](#hydrology-alias-tests) · [Resolver](#schema-resolution-and-validator-runtime) · [Coverage](#coverage-boundary-and-known-blind-spots) · [Fixtures](#fixture-contract) · [IDs and refs](#schema-id-reference-and-namespace-tests) · [Contracts](#contract-pairing-and-semantic-boundary) · [Compatibility](#schemas-tests-compatibility-boundary) · [CI](#ci-and-gate-acceptance) · [Security](#security-rights-sensitivity-and-data-minimization) · [Authoring](#test-authoring-contract) · [Validation](#validation) · [Done](#definition-of-done) · [Migration](#smallest-sound-improvement-sequence) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Changelog](#changelog) · [Evidence](#evidence-basis)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `tests/schemas/README.md` | **CONFIRMED** | v0.3 updates the v0.2 guide in place; the prior blob is pinned in metadata. |
| `tests/schemas/test_common_contracts.py` | **CONFIRMED executable pytest module** | Provides fixture-driven validation for a hard-coded set of immediate v1 schema families. |
| `tests/schemas/test_evidence_ref_validator.py` | **CONFIRMED executable pytest module** | Exercises the EvidenceRef CLI with one valid and one missing-ref fixture. |
| `tests/schemas/test_hydrology_alias_contracts.py` | **CONFIRMED executable pytest module** | Provides explicit positive and extra-property-negative coverage for three Hydrology aliases. |
| `tests/schemas/test_kdhe_hab_advisory_snapshot_contracts.py` | **CONFIRMED executable pytest module** | Covers KDHE HAB snapshot shape, deterministic identity, lineage, scope, and fail-closed release posture. |
| `tests/schemas/test_usdm_source_descriptor_contracts.py` | **CONFIRMED executable pytest module** | Covers the inactive USDM SourceDescriptor candidate and synthetic no-network connector fixtures. |
| `tests/schemas/test_water_planning_contracts.py` | **CONFIRMED executable pytest module** | Covers fifteen water-planning schemas, positive/negative fixtures, identity separation, and bounded acceptance criteria. |
| Other direct executable modules in `tests/schemas/` | **NOT SURFACED in complete tracked-lane inspection** | Ignored, generated, branch-local, or dynamic consumers remain unknown. |
| Root Python project | **CONFIRMED scaffold** | Requires Python 3.11+, `jsonschema>=4.26,<5`, and optional `pytest>=9.1.1,<10`; sets `pythonpath = ["."]`. |
| `schemas/` | **CONFIRMED machine-shape authority root** | Tests reference schemas; they do not define them. |
| `schemas/contracts/v1/` | **CONFIRMED mixed-maturity tree** | Contains many family lanes, compatibility surfaces, scaffolds, domain paths, and schema files. |
| `schemas/tests/` | **CONFIRMED README-only compatibility index in inspected evidence** | Executable ownership remains with accepted test roots unless formally migrated. |
| Shared resolver/runner | **CONFIRMED executable Python** | Builds a repository-local registry and creates Draft 2020-12 validators. |
| Aggregate validator runner | **CONFIRMED executable Python** | Runs seven selected top-level validators with `--fixtures`; not a complete schema-tree traversal. |
| `make test` | **CONFIRMED executable target** | Runs `python -m pytest tests/schemas tests/contracts -q`. |
| `make schemas` | **CONFIRMED executable target** | Runs `python tools/validators/_common/run_all.py`. |
| `schema-validation` workflow | **CONFIRMED** | Installs declared test dependencies, checks schema/fixture inventory, runs `make schemas`, and runs `pytest tests/schemas tests/contracts`. |
| `validator-suite` workflow | **CONFIRMED proposed-head wiring** | Runs ten focused shared-runner tests before `make schemas`, plus one EvidenceBundle invalid-fixture canary; hosted execution remains unverified. |
| Direct workflow invocation of `pytest tests/schemas` | **CONFIRMED in `schema-validation`** | Direct pytest coverage remains distinct from the focused shared-runner unit suite and aggregate validators. |
| Current test counts and pass state | **UNKNOWN** | Files and workflow definitions are not execution logs. |
| Branch-protection or promotion requirement | **UNKNOWN** | Workflow presence does not prove required-check status. |
| Production/public safety | **UNKNOWN** | Schema conformance is not evidence, policy, review, release, or deployment proof. |

**Authority of this README:** lane placement, executable inventory, observed behavior, coverage warnings, test/fixture requirements, CI acceptance criteria, correction guidance, and rollback guidance.

The following outrank this README for their responsibilities:

- accepted Directory Rules and ADRs;
- canonical schema files;
- paired semantic contracts;
- fixture payloads and fixture manifests;
- validator implementation;
- policy, rights, sensitivity, evidence, review, release, correction, and rollback records;
- executable tests and workflow logs;
- steward decisions.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from commit-pinned repository files, test code, runner code, workflow definitions, or schema shape. |
| **PROPOSED** | A test, registry, coverage rule, migration, or gate not yet accepted or implemented. |
| **CONFLICTED** | Two repository surfaces define overlapping or inconsistent ownership or coverage. |
| **NEEDS VERIFICATION** | Checkable, but not sufficiently proven for reliance or promotion. |
| **UNKNOWN** | Not established by the inspected evidence. |

[Back to top](#top)

---

<a id="purpose-and-scope"></a>

## Purpose and scope

This lane answers nine questions:

1. Which executable schema tests are actually present?
2. Which schema families can the current harness discover?
3. Which fixtures are required for a schema to become a test case?
4. How are `$id` and `$ref` values resolved?
5. Which alias and domain schemas receive explicit coverage?
6. Which schema families are silently outside current collection?
7. Which commands and workflows run validators versus pytest?
8. What does a green shape test prove—and what does it not prove?
9. How can coverage be corrected or expanded without creating parallel schema authority?

### In scope

- JSON parsing and Draft 2020-12 validator construction;
- repository-local `$ref` resolution;
- duplicate `$id` detection during registry construction;
- bounded valid/invalid fixture polarity;
- expected-error matching;
- Hydrology alias compatibility and strictness;
- schema family and fixture discovery behavior;
- test collection and zero-case prevention;
- coverage manifests and drift checks;
- CI routing and failure semantics;
- deterministic, synthetic, no-network test data;
- schema/contract/fixture/validator linkage;
- correction, migration, deprecation, and rollback guidance.

### Out of scope

- authoring canonical schemas;
- defining semantic meaning;
- admitting sources or evidence;
- evaluating policy or rights;
- approving sensitive disclosure;
- writing lifecycle records;
- creating receipts or proofs;
- approving release or publication;
- storing production payloads or exact sensitive data;
- treating a green test as truth or permission.

[Back to top](#top)

---

<a id="placement-and-authority"></a>

## Placement and authority

### Directory Rules basis

KFM places files by primary responsibility:

```text
schemas/                         machine-checkable shape authority
contracts/                       semantic meaning authority
fixtures/                        reusable deterministic examples
tests/schemas/                   executable schema conformance proof
schemas/tests/                   compatibility and placement index
tools/validators/                validator implementation
policy/                          admissibility and obligations
data/                            lifecycle, evidence, receipts, proofs
release/                         promotion, correction, withdrawal, rollback
```

`tests/schemas/` is correctly placed beneath the canonical `tests/` enforceability root.

### Responsibility routing

| Concern | Owning home | Role of this lane |
|---|---|---|
| JSON Schema definitions | `schemas/contracts/v1/` and accepted schema lanes | Load and assert; never redefine. |
| Semantic contracts | `contracts/` | Reference and check pairing metadata; never replace meaning. |
| Shared valid/invalid examples | `fixtures/` | Consume as test inputs. |
| Test-local tiny examples | `tests/fixtures/` when accepted | Consume or define only under the test-fixture contract. |
| Validator implementation | `tools/validators/` | Exercise and inspect behavior. |
| Schema-test code | `tests/schemas/` | Primary executable responsibility. |
| Compatibility guardrails | `schemas/tests/` | Index and migration notes only unless formally adopted. |
| Policy and disclosure | `policy/` | Assert separation; do not decide. |
| Evidence and proof | governed `data/` roots | Never synthesize or store here. |
| Release/correction/rollback | `release/` | Assert references and gating; never approve. |
| Test reports | accepted QA artifact lane | Emit only when a governed report contract exists. |

### Anti-collapse rules

This lane must never imply:

```text
schema-valid        = semantically correct
schema-valid        = evidence-supported
schema-valid        = source-authoritative
schema-valid        = policy-allowed
schema-valid        = rights-cleared
schema-valid        = sensitivity-safe
schema-valid        = released
schema-valid        = public-safe
schema-valid        = implementation-complete
schema-valid        = production behavior
```

[Back to top](#top)

---

<a id="confirmed-repository-inventory"></a>

## Confirmed repository inventory

### Direct lane

```text
tests/schemas/
├── __init__.py
├── README.md
├── test_common_contracts.py
├── test_evidence_ref_validator.py
├── test_hydrology_alias_contracts.py
├── test_kdhe_hab_advisory_snapshot_contracts.py
├── test_usdm_source_descriptor_contracts.py
└── test_water_planning_contracts.py
```

This is a bounded inventory from connector search and exact path reads. It does not prove the permanent absence of ignored, generated, branch-local, or unindexed files.

### Supporting execution surfaces

```text
tools/validators/_common/
├── jsonschema_runner.py
├── local_resolver.py
└── run_all.py

Makefile
pyproject.toml
.github/workflows/schema-validation.yml
.github/workflows/source-descriptor-validate.yml
.github/workflows/validator-suite.yml
```

### Authority and compatibility surfaces

```text
schemas/README.md
schemas/contracts/v1/README.md
schemas/tests/README.md
contracts/README.md
fixtures/README.md
tools/validators/README.md
```

### Direct module matrix

| Module | Confirmed responsibility | Confirmed limits |
|---|---|---|
| `test_common_contracts.py` | Parameterizes selected immediate v1 schemas that have matching fixture directories; checks valid fixtures pass and invalid fixtures fail. | Hard-coded seven-family allowlist; non-recursive schema glob; missing fixture directories omit cases; no explicit minimum fixture count. |
| `test_evidence_ref_validator.py` | Runs the EvidenceRef validator CLI against one valid and one missing-ref fixture and asserts exact exit/output polarity. | Narrow two-case entrypoint check; not full EvidenceRef semantics. |
| `test_hydrology_alias_contracts.py` | Validates three Hydrology alias fixtures and rejects an injected unknown top-level property. | Only three aliases; one valid fixture per alias; no broad missing-field, ref, namespace, or expected-keyword matrix. |
| `test_kdhe_hab_advisory_snapshot_contracts.py` | Exercises KDHE HAB snapshot schema fixtures plus deterministic identity, correction lineage, scope, and denied publication/alerting posture. | Bounded synthetic fixture family; no connector activation or live source verification. |
| `test_usdm_source_descriptor_contracts.py` | Checks the inactive USDM SourceDescriptor candidate and deterministic no-network connector fixtures. | Candidate/fixture governance only; no live source, rights, release, or publication proof. |
| `test_water_planning_contracts.py` | Exercises fifteen water-planning schema families and explicit identity, time, version, geometry, and region constraints. | Bounded fixtures and selected acceptance criteria; not source-truth or publication proof. |

[Back to top](#top)

---

<a id="current-execution-surfaces"></a>

## Current execution surfaces

### Confirmed commands

```bash
# Direct schema-lane pytest execution.
python -m pytest tests/schemas -q

# Current root test target.
make test

# Equivalent current root test command.
python -m pytest tests/schemas tests/contracts -q

# Selected dedicated validators and their fixture families.
make schemas

# Equivalent aggregate validator command.
python tools/validators/_common/run_all.py
```

### What each command proves

| Command | What it actually runs | What it does not prove |
|---|---|---|
| `python -m pytest tests/schemas -q` | Direct pytest collection beneath this lane. | Validator CLI wiring outside imported runner behavior; full schema inventory; release safety. |
| `make test` | `tests/schemas` and `tests/contracts`. | Policy, API, UI, E2E, runtime proof, release, and domain suites. |
| `make schemas` | Seven selected top-level validator wrappers with `--fixtures`. | Every schema file, every family, direct pytest modules, domain aliases beyond selected wrappers. |
| `schema-validation` workflow | Declared test dependency install, schema/fixture inventory checks, `make schemas`, and `pytest tests/schemas tests/contracts`. | Complete semantic, evidence, policy, release, or public-safety coverage; branch-protection requirement. |
| `validator-suite` workflow | Ten focused shared-runner tests before `make schemas`, plus an EvidenceBundle invalid-fixture canary. | Comprehensive schema-lane collection or all invalid families. |

### Confirmed seven-validator aggregate

`run_all.py` currently executes:

1. `validate_source_descriptor.py`
2. `validate_evidence_ref.py`
3. `validate_evidence_bundle.py`
4. `validate_runtime_response_envelope.py`
5. `validate_decision_envelope.py`
6. `validate_run_receipt.py`
7. `validate_ingest_receipt.py`

The runner stops on the first nonzero return code. It does not dynamically discover every validator or every schema family.

### Workflow distinction

```text
pytest tests/schemas     executable test-lane proof
make schemas             selected validator-wrapper fixture proof
schema-validation CI     inventory + make schemas + schema/contract pytest
validator-suite CI       focused runner tests + make schemas + one negative canary
```

These paths overlap but are not interchangeable.

[Back to top](#top)

---

<a id="generic-contract-fixture-harness"></a>

## Generic contract-fixture harness

`test_common_contracts.py` is the broadest confirmed direct test in this lane.

### Hard-coded family allowlist

The module currently scans only:

```python
[
    "evidence",
    "runtime",
    "common",
    "policy",
    "source",
    "governance",
    "release",
]
```

### Discovery rule

For each family, it performs an immediate-child glob equivalent to:

```text
schemas/contracts/v1/<family>/*.schema.json
```

For a schema named `<name>.schema.json`, it expects:

```text
fixtures/contracts/v1/<family>/<name>/
```

A schema becomes a pytest parameter only when that fixture directory exists.

### Valid fixture behavior

The test scans:

```text
valid/valid_*.json
```

Each valid fixture must produce no validator errors.

### Invalid fixture behavior

The test scans:

```text
invalid/invalid_*.json
```

Each invalid fixture must produce at least one validator error.

When an adjacent expected-error text file exists, the harness compares lowercased error messages using one of these modes:

- special `enum|pattern|date-time` handling;
- exact enum-style message detection;
- regular expression matching when the expected text contains `|`;
- line-by-line substring matching otherwise.

### Confirmed strengths

- deterministic local fixture reads;
- Draft 2020-12 validation through the shared runner;
- valid/invalid polarity;
- optional bounded diagnostic matching;
- registry-backed `$ref` resolution;
- fail-on-valid-fixture error;
- fail-on-invalid-fixture acceptance.

### Confirmed gaps

The current module does not explicitly assert:

- every selected family contains at least one schema;
- every schema has a fixture directory;
- every fixture directory contains at least one valid fixture;
- every fixture directory contains at least one invalid fixture;
- every invalid fixture has an expected-error file;
- every schema has `$id`;
- every schema passes metaschema validation;
- every schema has a paired contract;
- every schema is registered in an accepted manifest;
- every fixture is consumed by exactly one intended schema;
- every family in the v1 tree is represented;
- nested schemas beneath selected families are discovered;
- domain schemas are discovered;
- compatibility-lane duplicates are reconciled.

### Zero-case risk

A matching fixture directory with empty `valid/` and `invalid/` patterns can allow the parameterized function to complete without asserting any payload case.

A schema without a matching fixture directory is omitted from `_schema_cases()` and therefore does not fail the test merely because coverage is absent.

These are coverage gaps, not proof that the affected schema is valid.

[Back to top](#top)

---

<a id="hydrology-alias-tests"></a>

## Hydrology alias tests

`test_hydrology_alias_contracts.py` adds explicit coverage outside the generic top-level family allowlist.

### Covered aliases

```text
schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json
schemas/contracts/v1/domains/hydrology/run_receipt.schema.json
schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json
```

### Fixture inputs

```text
fixtures/domains/hydrology/<name>/valid/valid_1.json
```

### Positive assertion

For each alias, the fixture must produce no validation errors.

### Negative assertion

The test injects:

```json
{
  "unexpected_field": "should-fail"
}
```

and requires at least one validation error.

### What this proves

- the three exact alias paths load;
- their one confirmed valid fixture each is accepted;
- an added unknown top-level property is rejected;
- the shared local registry can resolve their references at the checked snapshot.

### What this does not prove

- all Hydrology domain schemas are covered;
- alias metadata and shared target versions are current;
- missing required fields are rejected for each alias;
- wrong enums, hashes, identifiers, or dates are rejected;
- nested unknown properties are rejected;
- the exact failure keyword is stable;
- invalid Hydrology fixture directories exist;
- alias and shared schema behavior are semantically equivalent;
- evidence, policy, release, or runtime behavior is correct.

[Back to top](#top)

---

<a id="schema-resolution-and-validator-runtime"></a>

## Schema resolution and validator runtime

### `load_validator`

The shared runner:

1. reads the selected schema as JSON;
2. resolves the repository root;
3. builds a local registry from the v1 schema tree;
4. creates a `Draft202012Validator`.

### Local registry behavior

`local_resolver.py` recursively scans:

```text
schemas/contracts/v1/**/*.schema.json
```

For every discovered schema:

- JSON is parsed;
- `$id` is read;
- schemas without `$id` are skipped from the registry;
- duplicate `$id` values raise an error;
- schemas with `$id` become `Resource` entries.

### Important boundary

The registry is broader than the generic pytest family allowlist:

```text
registry scan      = recursive across all v1 *.schema.json
pytest case scan   = immediate files in seven selected families
```

A schema may therefore be available as a `$ref` target without receiving its own direct fixture parameter.

### No explicit metaschema assertion

The inspected test and runner code do not explicitly call a schema metaschema check such as:

```python
Draft202012Validator.check_schema(schema)
```

Do not claim that every schema is itself validated against the Draft 2020-12 metaschema merely because a validator object was constructed or a fixture was checked.

### CLI runner behavior

The shared CLI runner:

- accepts explicit files or `--fixtures`;
- returns `2` before schema loading when neither input mode is supplied;
- preserves explicit-file validation and its first-error diagnostics;
- sorts `valid/*.json`, then sorts `invalid/*.json`;
- requires both fixture lanes to be nonempty;
- emits `OK` for a schema-valid positive fixture;
- emits `EXPECTED_FAIL` for a well-formed negative fixture rejected by the schema;
- reserves `FAIL` for polarity failures, malformed JSON, validator exceptions, or fixture configuration/non-vacuity failures;
- returns `1` when any fixture-mode failure occurs.

`EXPECTED_FAIL` records schema rejection only. Expected-error sidecar matching remains a separate schema-test or workflow assertion.

[Back to top](#top)

---

<a id="coverage-boundary-and-known-blind-spots"></a>

## Coverage boundary and known blind spots

The v1 schema index documents a much broader tree than the generic pytest allowlist.

### Selected by generic harness

```text
common/
source/
evidence/
runtime/
policy/
governance/
release/
```

### Confirmed v1 lanes outside the generic allowlist

The parent schema index documents additional lanes including:

```text
sources/
exposure/
ui/
map/
layers/
domains/
joins/
relations/
receipts/
review/
transport/
trade-routes/
spatial-foundation/
stac/
smoke/
```

Some are compatibility indexes or scaffolds, but their presence must not be mistaken for direct pytest coverage.

### Non-recursive blind spot

Within a selected family, the generic harness uses an immediate-file glob. Nested schema files beneath subdirectories are outside that discovery rule.

### Fixture-gated blind spot

A schema file without:

```text
fixtures/contracts/v1/<family>/<name>/
```

is not parameterized by the generic harness.

### Domain blind spot

Domain schemas under:

```text
schemas/contracts/v1/domains/<domain>/
```

are outside the generic harness. Dedicated modules provide bounded Hydrology,
KDHE Hazards, and water-planning coverage, while the USDM module checks a
cross-domain SourceDescriptor candidate. These explicit cases do not establish
complete domain-schema coverage.

### Compatibility blind spot

Flat compatibility paths and canonical domain paths can both exist. Current tests do not establish that duplicate or alias schemas:

- resolve to one accepted authority;
- remain synchronized;
- reject conflicting versions;
- carry migration metadata;
- are retired on schedule.

### Scaffold blind spot

A syntactically valid schema with permissive or empty shape can pass a narrow fixture test while remaining semantically incomplete.

### Namespace blind spot

The v1 index records mixed `$id` namespaces. Duplicate IDs are detected, but the current lane does not enforce one accepted namespace convention or require every schema to have `$id`.

[Back to top](#top)

---

<a id="fixture-contract"></a>

## Fixture contract

### Required future polarity

Every schema promoted as fixture-covered should have, at minimum:

```text
fixtures/contracts/v1/<family>/<name>/
├── README.md
├── valid/
│   └── valid_1.json
└── invalid/
    ├── invalid_1.json
    └── invalid_1.expected_error.txt
```

Domain profiles may use an accepted domain fixture lane only when the ownership and consumer link are explicit.

### Valid fixtures

A valid fixture should:

- contain all required fields;
- use deterministic identifiers and timestamps;
- avoid credentials and real private records;
- remain small and reviewable;
- declare the schema/profile version it represents when material;
- include realistic boundary values without becoming production truth;
- pass the intended schema and no incompatible profile.

### Invalid fixtures

An invalid fixture should isolate one primary failure where practical:

- missing required field;
- invalid enum;
- invalid identifier pattern;
- invalid hash;
- invalid date-time;
- unresolved reference;
- forbidden additional property;
- invalid nested type;
- incompatible version/profile;
- alias drift;
- sensitive field where the public profile forbids it.

### Nonempty requirement

Shared aggregate fixture mode now fails when either configured valid or invalid
lane is empty. `schema-validation` also asserts nonempty lanes for the same
seven configured families. The generic `test_common_contracts.py` glob can
still complete vacuously for an empty matching family, so repository-wide
fixture non-vacuity remains incomplete.

### Expected-error requirement

Expected-error assertions should prefer stable validator concepts over brittle whole-message equality:

```text
required
enum
pattern
format
type
additionalProperties
unevaluatedProperties
$ref resolution
```

Where exact path matters, assert both the validator keyword and the instance/schema path.

### Fixture authority boundary

Fixtures are examples, not:

- source records;
- EvidenceBundles;
- PolicyDecisions;
- release manifests;
- receipts;
- proof packs;
- public payloads;
- production snapshots;
- legal, cultural, or operational authority.

[Back to top](#top)

---

<a id="schema-id-reference-and-namespace-tests"></a>

## Schema ID, reference, and namespace tests

### Confirmed current behavior

The local registry:

- recursively discovers v1 schema files;
- skips schemas without `$id`;
- rejects duplicate `$id` values;
- resolves registered references through the `referencing` registry.

### Required future tests

| Test family | Required behavior |
|---|---|
| `all_schema_json_parses` | Every `.schema.json` file parses as JSON. |
| `all_schemas_check_metaschema` | Every promoted schema passes Draft 2020-12 metaschema validation. |
| `all_promoted_schemas_have_id` | Missing `$id` fails for schemas in an accepted active registry. |
| `schema_ids_unique` | Duplicate `$id` fails with both paths reported. |
| `schema_id_namespace_allowed` | `$id` uses an accepted namespace/profile. |
| `all_refs_resolve` | Every local `$ref` resolves under the pinned registry. |
| `no_forbidden_remote_ref` | Default tests do not fetch external schemas. |
| `alias_target_pinned` | Alias schemas reference an accepted target/version. |
| `compatibility_cycle_forbidden` | Alias/mirror references do not form cycles. |
| `deprecated_id_has_redirect_record` | Retired identifiers retain a governed compatibility record. |

### Network rule

Reference resolution in the default suite must remain repository-local and fail closed when a required resource is unavailable. A live network fetch must never be the hidden success path for schema validation.

[Back to top](#top)

---

<a id="contract-pairing-and-semantic-boundary"></a>

## Contract pairing and semantic boundary

Schema shape and contract meaning are separate.

### Minimum pairing assertion

For consequential schemas, tests should verify that declared metadata points to an existing semantic contract or an explicit unresolved record.

A pairing test may verify:

- contract path exists;
- schema and contract names align;
- version/profile identifiers are compatible;
- deprecation state is not contradictory;
- alias or compatibility status is explicit;
- missing pairing is surfaced as `NEEDS VERIFICATION`, not silently accepted.

### What pairing does not prove

A path existing does not prove:

- the contract is accepted;
- fields have matching semantics;
- policy obligations are implemented;
- evidence resolves;
- release is permitted;
- clients honor restrictions.

### Domain anti-collapse

A generic/shared schema and a domain profile must not silently become interchangeable when domain meaning, rights, sensitivity, time, source role, or disclosure posture differs.

[Back to top](#top)

---

<a id="schemas-tests-compatibility-boundary"></a>

## `schemas/tests/` compatibility boundary

`schemas/tests/` is a confirmed compatibility/index tree with README guardrails for valid and invalid placement.

Current routing posture:

```text
tests/schemas/   executable pytest schema tests
schemas/tests/   README-only compatibility/index guidance by default
schemas/         canonical schema definitions
fixtures/        reusable valid/invalid examples
```

### Confirmed compatibility inventory

The compatibility index documents README lanes for:

- `valid/` and `invalid/`;
- domain indexes for Fauna, Flora, Habitat, Hydrology, and Transport;
- non-domain Hazards and Roads–Rail–Trade paths whose placement remains unresolved.

### No parallel executable authority

Do not add matching executable suites under both:

```text
tests/schemas/
schemas/tests/
```

without an accepted split, migration note, and CI ownership contract.

### Migration rule

When executable files are discovered under `schemas/tests/`:

1. inventory consumers and workflow paths;
2. select an accepted executable home;
3. preserve history;
4. move tests and fixtures separately according to responsibility;
5. add temporary compatibility documentation where needed;
6. run old and new commands during a bounded window;
7. remove duplicate collection;
8. retain rollback instructions.

[Back to top](#top)

---

<a id="ci-and-gate-acceptance"></a>

## CI and gate acceptance

### Current workflow matrix

| Workflow | Current command | Coverage meaning |
|---|---|---|
| `schema-validation` | inventory checks, `make schemas`, `pytest tests/schemas tests/contracts` | Seven configured validator families plus the direct schema and contract pytest lanes. |
| `validator-suite` / `run-validators` | focused shared-runner unit suite, then `make schemas` | Ten fixture-mode regression cases plus the same seven-validator aggregate. |
| `validator-suite` / `ensure-fail-closed` | explicit invalid EvidenceBundle validation | One negative CLI canary. |
| Root `make test` | `pytest tests/schemas tests/contracts -q` | Direct schema and contract pytest lanes when invoked. |

### Current gap

`schema-validation` directly collects `tests/schemas` together with
`tests/contracts`. `validator-suite` instead exercises the shared runner's
fixture contract and aggregate wrappers. The two paths overlap, but neither is
a complete schema-tree, semantic-contract, policy, evidence, or release gate.

### Required mature gate

A mature schema gate should:

1. install pinned/test dependencies;
2. parse every registered schema file;
3. check the accepted metaschema;
4. build the local registry;
5. reject missing/duplicate/forbidden IDs;
6. resolve every local reference;
7. inventory registered schemas and fixture families;
8. fail on missing required fixtures;
9. fail on zero valid or zero invalid cases;
10. run direct `tests/schemas`;
11. run dedicated validator wrappers;
12. run at least one canary proving invalid payloads fail;
13. report collected schema, fixture, and test counts;
14. preserve the primary failure;
15. emit no release approval.

### Forbidden green patterns

- `|| true` on trust-bearing schema commands;
- echo-only schema jobs presented as validation;
- empty parameter sets presented as coverage;
- skipped schemas treated as passing;
- invalid fixtures absent from a promoted family;
- generated coverage reports without input hashes;
- network fallback for unresolved `$ref`;
- workflow success treated as schema acceptance or release permission.

### Suggested coverage report fields

```json
{
  "schema_files_discovered": 0,
  "schema_files_registered": 0,
  "schemas_missing_id": 0,
  "duplicate_ids": 0,
  "refs_checked": 0,
  "fixture_families": 0,
  "valid_cases": 0,
  "invalid_cases": 0,
  "schemas_without_fixtures": [],
  "fixtures_without_schema": [],
  "pytest_tests_collected": 0,
  "outcome": "PASS | FAIL | ERROR"
}
```

This would be a QA report, not a release manifest or proof of truth.

[Back to top](#top)

---

<a id="security-rights-sensitivity-and-data-minimization"></a>

## Security, rights, sensitivity, and data minimization

Schema tests are structural, but their inputs can still leak sensitive material.

### Default fixture posture

Use:

- synthetic identifiers;
- generalized geometry;
- fake names and organizations;
- non-routable/example endpoints;
- fixed timestamps;
- non-secret hashes and tokens;
- minimal fields needed for the assertion.

### Prohibited fixture content

- live credentials;
- signed URLs;
- private API endpoints;
- exact rare-species locations;
- exact archaeological locations;
- private landowner data;
- living-person sensitive data;
- DNA/genomic records;
- precise critical-infrastructure detail;
- restricted cultural knowledge;
- production logs or stack traces;
- private prompts or model chain-of-thought.

### Side-channel checks

Invalid diagnostics and CI logs must not expose:

- secret values;
- full restricted payloads;
- filesystem paths revealing private environments;
- internal network topology;
- exact protected coordinates;
- raw source records.

### Public-safe does not mean releasable

A synthetic fixture can be public-safe while the corresponding production object remains restricted. Tests must preserve that distinction.

[Back to top](#top)

---

<a id="test-authoring-contract"></a>

## Test-authoring contract

Every new schema test should state:

| Field | Required content |
|---|---|
| Test responsibility | Shape, ID, ref, fixture, alias, compatibility, or pairing behavior. |
| Schema path/profile | Exact canonical or explicitly compatibility-marked path. |
| Contract reference | Paired semantic contract or unresolved marker. |
| Fixture source | Exact fixture lane and fixture identity. |
| Positive cases | At least one meaningful accepted shape where applicable. |
| Negative cases | At least one targeted rejection where applicable. |
| Expected diagnostic | Stable keyword/path assertion. |
| Network posture | No network by default. |
| Sensitivity posture | Synthetic/public-safe input. |
| Authority boundary | Passing does not imply policy/release/truth. |
| CI consumer | Workflow/target that collects the test, or `NEEDS VERIFICATION`. |
| Correction path | How changed schema behavior invalidates fixtures/tests. |
| Rollback target | Prior schema/test/fixture lineage where material. |

### Naming

Prefer descriptive pytest names:

```text
test_all_registered_schema_ids_are_unique
test_promoted_schemas_have_nonempty_valid_and_invalid_fixtures
test_all_local_refs_resolve_without_network
test_hydrology_aliases_reject_unknown_top_level_properties
test_compatibility_alias_target_is_pinned
```

### Test independence

Tests should not depend on:

- execution order;
- live network state;
- current wall-clock time;
- random unseeded values;
- mutable production data;
- previously emitted artifacts;
- hidden local environment variables.

### Failure quality

Failures should identify:

- schema path;
- fixture path;
- instance path;
- schema path/keyword;
- expected versus observed behavior;
- migration/compatibility profile when relevant.

Do not print full restricted payloads.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### Confirmed repository commands

```bash
python -m pytest tests/schemas -q
python -m pytest tests/schemas tests/contracts -q
python tools/validators/_common/run_all.py
make schemas
make test
```

### Proposed bounded diagnostics

These commands are **PROPOSED review diagnostics**, not confirmed CI contracts:

```bash
# Show collected direct schema tests.
python -m pytest tests/schemas --collect-only -q

# Inventory schema files.
find schemas/contracts/v1 -type f -name '*.schema.json' | sort

# Inventory shared fixture JSON.
find fixtures/contracts/v1 -type f -name '*.json' | sort

# Search for compatibility test code that may be misplaced.
find schemas/tests -type f ! -name 'README.md' | sort

# Search for schemas missing a visible $id declaration.
python - <<'PY'
import json
from pathlib import Path

missing = []
for path in sorted(Path("schemas/contracts/v1").rglob("*.schema.json")):
    doc = json.loads(path.read_text(encoding="utf-8"))
    if not doc.get("$id"):
        missing.append(str(path))

for path in missing:
    print(path)
raise SystemExit(1 if missing else 0)
PY
```

### Validation interpretation

| Result | Safe interpretation |
|---|---|
| Pytest passes | Collected assertions passed against the checked repository state. |
| `make schemas` passes | Seven selected validator fixture families passed the aggregate runner. |
| Registry builds | Registered `$id` values were parseable and unique among included resources. |
| Invalid fixture rejected | That fixture violated at least one tested schema rule. |
| All checks green | Necessary structural proof only; policy/evidence/release remain separate. |

### This implementation slice

- the focused standard-library shared-runner suite passed all ten cases locally;
- Python compilation and workflow YAML parsing passed locally;
- dependency-backed aggregate and schema/contract pytest execution were not run locally because `jsonschema`, `referencing`, and `pytest` are unavailable in the isolated runtime;
- hosted workflow results remain **NEEDS VERIFICATION**;
- no schema, semantic contract, fixture payload, policy, release, or publication behavior changes.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This lane is mature only when:

### Inventory and ownership

- [ ] Direct test inventory is recursively verified.
- [ ] `tests/schemas/` is accepted as executable authority.
- [ ] `schemas/tests/` is formally compatibility-only, migrated, or assigned a documented split.
- [ ] CODEOWNERS and reviewers are defined.
- [ ] Schema family registry or equivalent inventory is accepted.

### Schema coverage

- [ ] Every promoted schema parses.
- [ ] Every promoted schema passes the accepted metaschema.
- [ ] Every promoted schema has an accepted `$id`.
- [ ] `$id` values are unique and namespace-conformant.
- [ ] Every required local `$ref` resolves without network.
- [ ] Nested and domain schemas are included by a declared discovery rule.
- [ ] Compatibility aliases have pinned targets and migration status.
- [ ] Empty/permissive scaffolds cannot be mislabeled active.

### Fixture acceptance complete

- [ ] Every promoted schema has at least one valid fixture.
- [ ] Every promoted schema has at least one invalid fixture.
- [ ] Fixture directories cannot be empty and green.
- [ ] Invalid fixtures have stable expected diagnostics.
- [ ] Orphan fixtures fail inventory checks.
- [ ] Fixture identity, version, and generator lineage are reviewable.
- [ ] Sensitive fixtures are synthetic and public-safe.

### Contract and governance boundary

- [ ] Consequential schemas link to paired contracts.
- [ ] Missing contracts are explicit.
- [ ] Schema tests do not encode policy as shape accidentally.
- [ ] Evidence, rights, sensitivity, review, release, correction, and rollback remain separate.
- [ ] Public clients consume governed released interfaces, not schema fixtures.

### CI acceptance complete

- [x] Direct schema pytest runs in `schema-validation`.
- [x] The dedicated validator aggregate runs in both schema workflows.
- [x] An EvidenceBundle negative canary proves the reviewed rejection path.
- [x] The seven configured aggregate fixture families fail on an empty valid or invalid lane.
- [ ] Direct pytest collection has an explicit fail-on-zero-test assertion.
- [ ] Every promoted schema family fails on zero fixture cases.
- [ ] Coverage counts and omissions are visible.
- [ ] Schema, fixture, validator, and test path triggers are complete.
- [ ] Required-check and promotion significance are documented.
- [ ] Current green status is verified from logs before acting on it.

### Rollback acceptance complete

- [ ] Schema changes identify affected fixtures, tests, validators, contracts, and consumers.
- [ ] Corrected schemas invalidate stale coverage reports.
- [ ] Compatibility aliases have retirement and rollback rules.
- [ ] Revert procedures preserve shared history.
- [ ] A tested rollback exists for trust-bearing schema changes.

[Back to top](#top)

---

<a id="smallest-sound-improvement-sequence"></a>

## Smallest sound improvement sequence

### Phase 1 — Freeze claims, not development

- keep this README grounded;
- do not call current coverage complete;
- do not promote schemas solely because current checks pass.

### Phase 2 — Emit a deterministic inventory

- list every `.schema.json`;
- list `$id`, family, path, status, and paired contract;
- list matching fixture directories and validator entry points;
- record compatibility/alias status.

### Phase 3 — Add coverage closure checks

- fail on promoted schemas outside the seven configured families when fixtures are absent;
- extend current aggregate nonempty-lane enforcement to the accepted promoted inventory;
- fail on orphan fixtures;
- fail on missing expected diagnostics where required.

### Phase 4 — Add schema self-validation

- parse all schema JSON;
- call Draft 2020-12 metaschema validation;
- enforce accepted `$id` namespace;
- resolve all local refs offline.

### Phase 5 — Expand discovery

Choose and document one approach:

```text
manifest-driven discovery
or
recursive convention-driven discovery
```

Do not silently broaden collection without reviewing compatibility and scaffold lanes.

### Phase 6 — Reconcile domain and compatibility schemas

- inventory `domains/` and flat mirrors;
- identify alias versus duplicate authority;
- pin targets and versions;
- add drift tests;
- retire losers through migration notes.

### Phase 7 — Align CI

- preserve the implemented direct schema pytest and validator-wrapper checks;
- report counts;
- fail on zero cases;
- add complete path triggers;
- decide promotion significance.

### Phase 8 — Verify and record rollback

- run full schema checks;
- verify negative canaries;
- review reports;
- document correction/rollback lineage;
- retain prior schema and fixture references.

### Stop conditions

Stop promotion when:

- schema home is conflicted;
- `$id` namespace is unresolved for the affected profile;
- contract pairing is missing for a consequential object;
- refs do not resolve offline;
- valid or invalid fixture coverage is empty;
- test collection is zero;
- alias targets disagree;
- sensitive fixtures are not public-safe;
- CI omits affected paths;
- rollback impact is unknown.

[Back to top](#top)

---

<a id="correction-and-rollback"></a>

## Correction and rollback

### Documentation correction

When this README overstates coverage:

1. narrow the claim;
2. identify the exact evidence that changed;
3. update status and inventory tables;
4. preserve the prior blob/commit;
5. do not rewrite shared history.

### Schema behavior correction

When a schema changes:

1. identify its paired contract and authority status;
2. identify all `$id` and `$ref` consumers;
3. update valid and invalid fixtures;
4. update direct tests and validators;
5. run compatibility and alias checks;
6. invalidate stale reports;
7. verify policy/release consumers separately;
8. record rollback target.

### Fixture correction

When a fixture was mislabeled:

- move it between valid and invalid only with a reviewed schema/contract rationale;
- update expected diagnostics;
- preserve fixture identity or record supersession;
- check every consumer;
- do not change the schema merely to make a mistaken fixture pass.

### Compatibility rollback

When a migration breaks consumers:

- restore the prior accepted alias/ID mapping through a normal commit;
- preserve the failed migration record;
- keep both profiles explicit during a bounded compatibility window;
- do not silently merge incompatible shapes.

### Safety rollback triggers

Rollback is required when a change:

- allows formerly invalid sensitive/public payloads without governance review;
- weakens `additionalProperties` or `unevaluatedProperties` posture unintentionally;
- drops required evidence, policy, release, freshness, or correction references;
- hides unresolved refs;
- permits duplicate IDs;
- makes zero cases green;
- creates parallel executable test authority;
- removes negative fixtures or fail-closed canaries;
- bypasses correction or rollback visibility.

### README rollback target

Before merge, leave the review unmerged or restore prior blob:

```text
895e892294ac5d81df683e2dcc7cbf4b2ed88308
```

After merge, revert the implementation commit or pull request through normal Git history. Do not reset or rewrite shared history.

When rolling back this runner slice, restore the runner, focused tests, workflow
diagnostics, and owning documentation together. Do not leave `EXPECTED_FAIL`
prose attached to code that emits the prior ambiguous fixture output.

[Back to top](#top)

---

<a id="open-verification-backlog"></a>

## Open verification backlog

### Direct inventory

- [ ] Recursively verify every file beneath `tests/schemas/`.
- [ ] Confirm whether ignored/generated tests exist.
- [ ] Confirm exact pytest collection count.
- [ ] Confirm current pass/fail state from logs.
- [ ] Confirm CODEOWNERS and reviewers.

### Schema inventory

- [ ] Count all v1 schema files.
- [ ] Classify canonical, alias, compatibility, scaffold, and deprecated paths.
- [ ] Confirm accepted active schema registry.
- [ ] Confirm `$id` namespace decision.
- [ ] Confirm metaschema posture for every promoted schema.
- [ ] Confirm nested schema discovery.

### Fixture coverage verification

- [ ] Count schemas with and without fixture directories.
- [ ] Count empty valid/invalid sets.
- [ ] Find orphan fixture families.
- [ ] Require stable expected diagnostics.
- [ ] Confirm domain fixture routing.
- [ ] Confirm sensitive fixture review.

### Contracts and validators

- [ ] Verify every consequential schema-to-contract pairing.
- [ ] Verify every declared validator path.
- [ ] Compare direct pytest coverage with `run_all.py`.
- [ ] Decide whether aggregate validator discovery should be manifest-driven.
- [ ] Confirm validator exit-code and output contracts.

### Compatibility and aliases

- [ ] Resolve `schemas/tests/` long-term role.
- [ ] Inventory flat versus domain schema mirrors.
- [ ] Add alias target/version drift tests.
- [ ] Add deprecation and redirect records.
- [ ] Resolve singular/plural and hyphen/underscore path drift.

### CI verification

- [x] Direct `pytest tests/schemas tests/contracts` runs in `schema-validation`.
- [x] Configured aggregate families fail on an empty valid or invalid fixture lane.
- [ ] Add an explicit fail-on-zero-direct-test control and extend fixture non-vacuity to every promoted family.
- [ ] Add complete path filters.
- [ ] Emit schema/fixture/test counts.
- [ ] Confirm required-check status.
- [ ] Confirm promotion-gate dependency.
- [ ] Inspect current logs separately from workflow definitions.

### Governance and release

- [ ] Confirm which schema statuses may block promotion.
- [ ] Confirm correction and rollback consumers.
- [ ] Confirm public-client compatibility testing.
- [ ] Confirm no-network enforcement.
- [ ] Record one tested schema migration rollback.

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-08-01 | v0.3 | Reconciled six direct schema-test modules, the seven-entry aggregate, sorted nonempty fixture lanes, `EXPECTED_FAIL`/`FAIL` semantics, ten focused runner tests, and current CI definitions. |
| 2026-07-16 | v0.2 | Replaced the planning-oriented predecessor with a repository-grounded account of the then-inspected direct modules, coverage limits, and CI surfaces. |

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior v0.2 `tests/schemas/README.md` | **CONFIRMED** | Existing lane purpose, prior blob, and verification lineage. | Did not reflect all six executable modules or current runner/CI behavior. |
| `tests/README.md` | **CONFIRMED** | Canonical tests root and machine-shape test responsibility. | Root README still marks broad implementation depth as needing verification. |
| `schemas/README.md` | **CONFIRMED** | Machine-shape authority and separation from tests/contracts/policy/data/release. | Does not prove complete schema inventory or coverage. |
| `schemas/contracts/v1/README.md` | **CONFIRMED mixed-maturity index** | Broad family tree, compatibility drift, scaffolds, and promotion expectations. | Parent index is not schema-file proof. |
| `schemas/tests/README.md` | **CONFIRMED compatibility index** | README-only valid/invalid placement tree and executable-home warning. | Does not prove absence of all executable files recursively. |
| `test_common_contracts.py` | **CONFIRMED executable test** | Seven-family immediate schema discovery, fixture gating, valid/invalid assertions, expected-error matching. | Non-recursive; omits schemas without fixture dirs; no nonempty-case assertion. |
| `test_evidence_ref_validator.py` | **CONFIRMED executable test** | Exact CLI success/failure polarity for two EvidenceRef fixtures. | Narrow entrypoint coverage. |
| `test_hydrology_alias_contracts.py` | **CONFIRMED executable test** | Three alias positives and added-property negatives. | Narrow Hydrology-only coverage. |
| `test_kdhe_hab_advisory_snapshot_contracts.py` | **CONFIRMED executable test** | KDHE HAB snapshot schema, identity, lineage, scope, and denied-publication conditions. | Synthetic fixtures; no live source or connector proof. |
| `test_usdm_source_descriptor_contracts.py` | **CONFIRMED executable test** | Inactive USDM descriptor and no-network fixture posture. | Candidate governance checks; no source, rights, release, or publication proof. |
| `test_water_planning_contracts.py` | **CONFIRMED executable test** | Fifteen water-planning schemas and selected domain invariants. | Bounded fixtures and acceptance criteria only. |
| `jsonschema_runner.py` | **CONFIRMED executable runner** | Draft 2020-12 validator construction, file/fixture validation, exit codes. | No explicit metaschema check in inspected code. |
| `local_resolver.py` | **CONFIRMED executable resolver** | Recursive v1 registry, missing-ID skip, duplicate-ID rejection. | Does not require all schemas to have IDs or define namespace policy. |
| `run_all.py` | **CONFIRMED executable aggregate** | Seven selected validator wrappers and fail-fast execution. | Not dynamic and not complete schema-tree coverage. |
| Root `Makefile` | **CONFIRMED** | `make test` and `make schemas` command definitions. | Help text calls the repo a greenfield scaffold; target presence is not pass evidence. |
| Root `pyproject.toml` | **CONFIRMED** | Python 3.11+, jsonschema and pytest dependency posture, pytest path config. | Does not prove installed environment or current run. |
| `schema-validation.yml` | **CONFIRMED workflow definition** | Inventory checks, aggregate validators, and direct schema/contract pytest execution. | Hosted proposed-head result remains unverified. |
| `source-descriptor-validate.yml` | **CONFIRMED workflow definition** | SourceDescriptor validation and aligned shared-runner diagnostics. | Does not establish source activation, rights, release, or publication authority. |
| `validator-suite.yml` | **CONFIRMED proposed-head workflow definition** | Ten focused shared-runner tests, aggregate validators, and one negative EvidenceBundle canary. | Not complete direct schema-test coverage. |
| `tests/validators/test_jsonschema_runner.py` | **CONFIRMED focused unit suite** | Ten deterministic cases cover fixture ordering, lane non-vacuity, polarity, malformed JSON, validator exceptions, missing inputs, and missing fixture configuration. | Uses synthetic validator doubles; dependency-backed aggregate behavior remains a separate check. |
| Current-session execution | **PASS / LIMITED** | Ten focused tests and Python/workflow syntax checks passed locally. | Dependency-backed aggregate and hosted workflow results remain unverified. |

[Back to top](#top)
