<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-common-readme
title: tools/validators/_common/ — Shared Validator Runtime Boundary
type: readme; directory-readme; shared-validator-runtime; schema-resolution-helper; compatibility-boundary
version: v0.5
status: draft; repository-grounded; executable; widely-consumed; fixture-driven; bounded-public-safe-fixture-mechanics; ci-invoked; extraction-decision-open; non-authoritative
owners: OWNER_TBD — Validator steward · Schema steward · Contract steward · Test/fixture steward · Python tooling steward · Security steward · CI steward · Release steward · Docs steward
created: 2026-05-09
updated: 2026-08-02
supersedes: v0.3 shared-validator runtime guide
policy_label: "public-review; tools; validators; shared-runtime; json-schema; draft-2020-12; local-resolution; no-network; deterministic-intent; fail-closed; schema-authority-external; contract-authority-external; policy-authority-external; evidence-authority-external; release-authority-external; extraction-aware; correction-aware; rollback-aware"
current_path: tools/validators/_common/README.md
truth_posture: >
  CONFIRMED target v0.2 README; direct helper modules jsonschema_runner.py, local_resolver.py,
  and run_all.py; root jsonschema dependency; local recursive schemas/contracts/v1/**/*.schema.json
  indexing; $id skip and duplicate-$id failure behavior; Draft 2020-12 validator construction;
  seven hard-coded top-level fixture validators; Makefile schemas target; schema-validation and
  validator-suite workflows; focused standard-library runner tests; sorted, nonempty positive and
  negative fixture lanes; explicit EXPECTED_FAIL diagnostics for schema-invalid negative fixtures;
  bounded exact-import search surfacing twenty validator scripts and six test modules; the
  package/schema-registry placeholder with working implementation still under this lane; and no
  direct network calls in the inspected helper modules / PROPOSED stable helper contract,
  structured result envelope, explicit compatibility policy, resource limits, exhaustive direct
  tests, extraction parity contract, migration, correction, and rollback rules / CONFLICTED
  hard-coded aggregation versus the broader consumer set; working local registry under tools versus
  proposed reusable schema-registry package / UNKNOWN exhaustive consumers, accepted public/private
  API status, format-keyword
  enforcement, schema dialect coverage outside Draft 2020-12, operational scale limits, emitted
  machine reports, release consumers, and production use / NEEDS VERIFICATION owners, CODEOWNERS,
  exhaustive helper and aggregate coverage, error/result schema, path-security controls, resource
  budgets, compatibility policy, package extraction ADR, consumer migration, deprecation window,
  and rollback
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: cb8a46fff89861b8f0ca57c1c29bacf1fec885a5
  prior_blob: 12df3198498356b32bf309a314eb255604b37415
  jsonschema_runner_blob: ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6
  local_resolver_blob: 171a2b8251d10fcc276107459a41056cdedc8ff5
  run_all_blob: 7595f40bafb70f8eb4af51d73a74923cf77bcd5b
  validators_parent_blob: d94c63d3a57f309f739c034b0e2c388f798cfbe7
  root_pyproject_blob: 3bba45d49de489c221734ee2446b21083f84fb28
  makefile_blob: 898004b6bb7873543a431c3869a1b357e56d9eca
  schema_validation_workflow_blob: fd0e53722b9d8406c5fde052672f760f00f2626b
  validator_suite_workflow_prior_blob: 1694afdd762ce515b53fc8e9d7d51324c2d0929d
  common_schema_test_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
  schema_registry_namespace_readme_blob: 6c28c0152c8d17acec594e1442936b0a36f9f200
  schema_home_adr_blob: 3c520ea8f2f8bcb3d478329a87d98b135ea335fd
  bounded_direct_inventory:
    - tools/validators/_common/README.md
    - tools/validators/_common/jsonschema_runner.py
    - tools/validators/_common/local_resolver.py
    - tools/validators/_common/run_all.py
  hard_coded_run_all_entrypoints:
    - tools/validators/validate_source_descriptor.py
    - tools/validators/validate_evidence_ref.py
    - tools/validators/validate_evidence_bundle.py
    - tools/validators/validate_runtime_response_envelope.py
    - tools/validators/validate_decision_envelope.py
    - tools/validators/validate_run_receipt.py
    - tools/validators/validate_ingest_receipt.py
runner_hardening_change_evidence:
  base_commit: cb8a46fff89861b8f0ca57c1c29bacf1fec885a5
  runner_prior_blob: ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6
  workflow_prior_blob: 1694afdd762ce515b53fc8e9d7d51324c2d0929d
  focused_test: tests/validators/test_jsonschema_runner.py
  workflow: .github/workflows/validator-suite.yml
  local_result: PASS; 10 tests
related:
  - ../README.md
  - jsonschema_runner.py
  - local_resolver.py
  - public_safe_fixture.py
  - run_all.py
  - ../../../pyproject.toml
  - ../../../Makefile
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/validator-suite.yml
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../tests/schemas/test_hydrology_alias_contracts.py
  - ../../../tests/validators/test_jsonschema_runner.py
  - ../../../schemas/contracts/v1/
  - ../../../fixtures/contracts/v1/
  - ../../../contracts/
  - ../../../policy/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
  - ../../../packages/schema-registry/src/schema_registry/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, tools, validators, common, jsonschema, draft-2020-12, registry, resolver, fixtures, ci, fail-closed, deterministic, schema-registry, migration, correction, rollback]
notes:
  - "v0.4 pairs the shared-runner correction with ten deterministic standard-library tests, validator-suite execution, owning documentation, and a generated-work receipt."
  - "The correction sorts both fixture lanes, requires each lane to be nonempty, labels expected schema rejection as EXPECTED_FAIL, keeps malformed or exceptional negative fixtures as FAIL, and removes the dead fixture-mode return-code branch."
  - "No schema, semantic contract, policy, fixture payload, package, lifecycle object, proof, release object, application runtime, or public artifact is modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/_common/` — Shared Validator Runtime Boundary

> **One-line purpose.** Provide repository-local JSON Schema loading, `$id` registry, bounded synthetic fixture mechanics, and aggregate-runner plumbing used by validator entrypoints—without becoming schema authority, semantic contract authority, policy, evidence, release approval, or public truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.4" src="https://img.shields.io/badge/version-v0.4-informational">
  <img alt="Maturity: executable" src="https://img.shields.io/badge/maturity-executable-success">
  <img alt="Schema dialect: Draft 2020-12" src="https://img.shields.io/badge/schema-Draft__2020--12-blue">
  <img alt="Network: none in helpers" src="https://img.shields.io/badge/network-none__in__helpers-success">
  <img alt="Authority: plumbing only" src="https://img.shields.io/badge/authority-plumbing__only-lightgrey">
  <img alt="Extraction: unresolved" src="https://img.shields.io/badge/extraction-NEEDS__DECISION-orange">
</p>

> [!IMPORTANT]
> **This lane contains working code.** At the pinned repository snapshot it contains a local schema resolver, a shared JSON Schema runner, and a seven-entrypoint aggregate runner. The parent README's general warning that executable behavior needs verification does not erase the implementation evidence in this directory.

> [!CAUTION]
> **A successful schema check proves only machine-shape conformance for the configured schema and instance.** It does not prove semantic correctness, evidence closure, source authority, rights, sensitivity safety, policy permission, release readiness, or public truth.

> [!WARNING]
> **Shared-helper changes have a broad blast radius.** A bounded exact-import search surfaced twenty validator scripts and six test modules importing `tools.validators._common.jsonschema_runner`. Treat signatures, output text, exit codes, registry behavior, path handling, and exception behavior as compatibility-sensitive until a formal migration says otherwise.

**Quick links:** [Purpose](#purpose) · [Evidence](#current-evidence-and-maturity) · [Inventory](#confirmed-inventory) · [Architecture](#runtime-architecture) · [API](#current-helper-api) · [Registry](#local-schema-registry-contract) · [Runner](#json-schema-runner-contract) · [Aggregate](#aggregate-runner-contract) · [Outcomes](#exit-codes-outcomes-and-output) · [Fixtures](#fixture-mode) · [Consumers](#current-consumers-and-blast-radius) · [Authority](#authority-and-anti-collapse) · [Security](#path-security-resource-and-privacy-posture) · [Testing](#tests-and-ci) · [Gaps](#known-gaps-and-conflicts) · [Migration](#schema-registry-package-extraction-boundary) · [Belongs](#what-belongs-here) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#maintenance-correction-migration-and-rollback) · [Evidence ledger](#evidence-ledger)

---

## Purpose

`tools/validators/_common/` is the current repository-local runtime shared by JSON Schema validator entrypoints.

Its responsibilities are narrow:

1. discover local canonical-candidate schema files;
2. construct a `referencing.Registry` keyed by schema `$id`;
3. create a `jsonschema.Draft202012Validator`;
4. validate explicit JSON files;
5. exercise paired `valid/` and `invalid/` fixture directories;
6. run a small hard-coded set of top-level validators for `make schemas`.

The durable question is:

> Can shared validator mechanics remain deterministic, local, testable, and fail-closed while every schema, contract, policy, fixture, evidence, and release decision remains visible in its owning root?

This lane is not a generic domain utility bucket. It is not a hidden schema registry authority, policy engine, evidence resolver, release gate, pipeline, or application library.

[Back to top](#top)

---

## Current evidence and maturity

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| `tools/validators/_common/README.md` | **CONFIRMED v0.3 before revision** | Documentation identified the fixture-mode defects corrected in v0.4. |
| `local_resolver.py` | **CONFIRMED executable** | Builds an in-memory local registry from `schemas/contracts/v1/**/*.schema.json`. |
| `jsonschema_runner.py` | **CONFIRMED executable** | Loads Draft 2020-12 validators, validates files, and supports fixture mode. |
| `run_all.py` | **CONFIRMED executable** | Runs seven hard-coded top-level validator entrypoints with `--fixtures`. |
| Root dependency | **CONFIRMED** | `jsonschema>=4.26.0,<5`; Python `>=3.11`. |
| `make schemas` | **CONFIRMED wired** | Invokes `python tools/validators/_common/run_all.py`. |
| `schema-validation` workflow | **CONFIRMED wired** | Installs the root project and runs `make schemas`. |
| `validator-suite` workflow | **CONFIRMED wired** | Runs the focused runner tests, `make schemas`, and a fail-closed invalid-fixture check. |
| Generic contract fixture tests | **CONFIRMED executable test code** | Uses `load_validator()` across selected schema families with fixture directories. |
| Import consumers | **CONFIRMED bounded search** | Twenty validator scripts and six test modules import the shared runner. |
| Structured machine report | **NOT ESTABLISHED** | Current output is line-oriented `OK` / `EXPECTED_FAIL` / `FAIL` text plus process exit status. |
| Focused shared-runner test suite | **CONFIRMED executable** | Ten standard-library cases cover explicit polarity, fixture polarity, ordering, non-vacuity, malformed input, exception containment, configuration, and no-input behavior; resolver and aggregate coverage remains partial. |
| Stable public API | **UNKNOWN** | Imports are widespread, but no semantic-version or compatibility policy is accepted. |
| Production/runtime use | **UNKNOWN** | CI use is verified; deployed service or production release use is not. |

**Current determination:** this directory is an implemented, CI-invoked internal validator runtime with broad repository consumers. It remains non-authoritative and has unresolved compatibility, testing, output, and extraction questions.

[Back to top](#top)

---

## Confirmed inventory

```text
tools/validators/_common/
├── README.md
├── jsonschema_runner.py
├── local_resolver.py
├── public_safe_fixture.py
└── run_all.py
```

### File roles

| File | Confirmed responsibility | Current boundary |
|---|---|---|
| `README.md` | Human-facing contract, evidence boundary, maintenance guidance | Cannot establish implementation by itself. |
| `local_resolver.py` | Build a local `$id` registry from canonical-candidate schema files | Does not decide schema admission, status, aliases, or canonicality. |
| `jsonschema_runner.py` | Construct validator, validate explicit files, exercise fixture directories | Does not produce a governed `ValidationReport` object. |
| `public_safe_fixture.py` | Bounded regular-file JSON parsing, duplicate/non-finite rejection, stable findings, and deterministic CLI reporting for synthetic public-safe profiles | Does not define any domain field, meaning, source role, evidence, policy, or release state. |
| `run_all.py` | Sequentially invoke seven top-level validators in fixture mode | Not dynamic discovery and not the complete validator inventory. |

No `_common/__init__.py` was surfaced in bounded search. Current imports rely on the repository's Python path/package layout rather than an explicitly exported `_common` API module.

[Back to top](#top)

---

## Runtime architecture

```mermaid
flowchart LR
  ENTRY["Validator entrypoint"] --> RUN["jsonschema_runner.run(...)"]
  RUN --> LOAD["load_validator(schema_path)"]
  LOAD --> RES["local_resolver.build_registry(repo_root)"]
  RES --> ROOT["schemas/contracts/v1/**/*.schema.json"]
  RES --> REG["referencing.Registry keyed by $id"]
  LOAD --> VAL["Draft202012Validator(schema, registry=REG)"]
  RUN --> MODE{"explicit files or --fixtures?"}
  MODE --> FILES["validate_files(...)"]
  MODE --> FIX["valid/ + invalid/ expectation checks"]
  FILES --> TEXT["OK / EXPECTED_FAIL / FAIL lines + exit code"]
  FIX --> TEXT
```

### Dependency direction

```text
validator entrypoints
  -> tools/validators/_common/
  -> jsonschema + referencing
  -> schemas/contracts/v1/
  -> fixture JSON

NOT:

_common -> domain meaning
_common -> policy decisions
_common -> evidence authority
_common -> release authority
_common -> public runtime
```

The shared runtime should remain read-only with respect to schemas, fixtures, lifecycle data, receipts, proofs, and release records.

[Back to top](#top)

---

## Current helper API

The following functions are confirmed by code.

### `build_registry(repo_root: Path) -> Registry`

Located in `local_resolver.py`.

Observed behavior:

- resolves `repo_root / "schemas" / "contracts" / "v1"`;
- raises `FileNotFoundError` if that root is absent;
- recursively scans sorted `*.schema.json` paths;
- parses each file as UTF-8 JSON;
- reads `$id`;
- skips schemas without `$id`;
- raises `ValueError` on duplicate `$id`;
- converts each schema with `Resource.from_contents`;
- returns `Registry().with_resources(...)`.

### `load_validator(schema_path: Path)`

Located in `jsonschema_runner.py`.

Observed behavior:

- parses the requested schema as UTF-8 JSON;
- resolves repository root from `Path(__file__).resolve().parents[3]`;
- builds the full local registry;
- returns `Draft202012Validator(schema, registry=registry)`.

### `validate_files(validator, files) -> int`

Observed behavior:

- parses each file as JSON;
- sorts validation errors by instance path;
- prints the first validation error per invalid file;
- prints `OK <path>` for valid files;
- catches broad exceptions per input file;
- returns `0` only when every file validates;
- otherwise returns `1`.

### `run(schema_path: Path, fixtures_dir: Path | None, argv) -> int`

Observed behavior:

- accepts positional files;
- accepts `--fixtures`;
- returns `2` before schema loading when neither explicit files nor fixture mode is supplied;
- delegates explicit files to `validate_files`;
- in fixture mode, discovers sorted `valid/*.json` followed by sorted `invalid/*.json`;
- requires at least one JSON fixture in each lane;
- prints `OK` for valid fixtures, `EXPECTED_FAIL` for schema-invalid negative fixtures,
  and `FAIL` for a polarity mismatch, malformed JSON, validator exception, or missing lane;
- returns `0` only when every fixture satisfies its declared polarity, otherwise `1`.

The private `_validate_fixture_files(...)` helper contains fixture parsing,
validation, and polarity-specific diagnostics. It is implementation detail, not
an established import contract.

### `main() -> int` in `run_all.py`

Observed behavior:

- invokes seven top-level validator scripts sequentially;
- passes `--fixtures`;
- stops at the first non-zero exit code;
- returns `0` only when all seven complete successfully.

These functions are currently import-consumed. Renaming, moving, changing signatures, changing exit codes, or changing output should be treated as a compatibility change.

[Back to top](#top)

---

## Local schema registry contract

### Confirmed scope

The resolver indexes only:

```text
schemas/contracts/v1/**/*.schema.json
```

It does not currently establish support for:

- `*.json` schemas without the `.schema.json` suffix;
- YAML schemas;
- JSON-LD contexts;
- schemas outside `schemas/contracts/v1/`;
- aliases or supersession;
- schema status or admission state;
- semantic version selection;
- generated registry snapshots;
- network retrieval.

### `$id` posture

| Condition | Current behavior | Governance interpretation |
|---|---|---|
| Schema has unique `$id` | Added to registry | Resolvable locally; not thereby canonical or approved. |
| Schema has no `$id` | Silently skipped | File may still be the primary schema passed to `load_validator`, but cannot be referenced through this registry entry. |
| Duplicate `$id` | Raises `ValueError` | Correct fail-closed behavior for ambiguous identity. |
| Invalid JSON | Exception propagates during registry construction | Run fails; no structured reason code is emitted. |
| Schema root absent | Raises `FileNotFoundError` | Run fails before validation. |

### Authority boundary

The registry is a **resolution mechanism**, not a schema-governance register.

It must not decide:

- which schema is accepted;
- whether a schema is draft, active, deprecated, or retired;
- whether a `$id` is canonical;
- whether compatibility aliases are allowed;
- whether semantic contracts and schemas agree;
- whether an instance is policy-allowed or releasable.

Those decisions belong to accepted ADRs, schema/contract governance, validation policy, reviews, and release controls.

[Back to top](#top)

---

## JSON Schema runner contract

### Supported mode: explicit files

Example:

```bash
python tools/validators/validate_evidence_bundle.py \
  path/to/candidate.json
```

Current output:

```text
OK path/to/candidate.json
```

or:

```text
FAIL path/to/candidate.json: <first validation or parse error>
```

### Supported mode: fixtures

Example:

```bash
python tools/validators/validate_evidence_bundle.py --fixtures
```

Expected directory convention:

```text
fixtures/contracts/v1/<family>/<object>/
├── valid/
│   └── *.json
└── invalid/
    └── *.json
```

Fixture mode separately verifies:

- every `valid/*.json` has no validation errors;
- every `invalid/*.json` has at least one validation error.

### Working-directory assumption

The top-level entrypoints pass relative schema and fixture paths. The current commands therefore assume execution from repository root unless absolute paths are supplied by a caller.

The local registry root is independently derived from `__file__`; the primary schema and fixture paths are not.

### Error surface

Current errors are human-readable text and exit codes. The runner does not emit a schema-backed result envelope with:

- validator id and version;
- schema id and digest;
- instance digest;
- all errors;
- JSON Pointer locations;
- reason-code families;
- timestamps;
- policy or evidence refs;
- correction or rollback refs.

Do not treat the current console line as a governed `ValidationReport`.

[Back to top](#top)

---

## Aggregate runner contract

`run_all.py` currently invokes:

```text
validate_source_descriptor.py
validate_evidence_ref.py
validate_evidence_bundle.py
validate_runtime_response_envelope.py
validate_decision_envelope.py
validate_run_receipt.py
validate_ingest_receipt.py
```

### Confirmed callers

- `make schemas`;
- `.github/workflows/schema-validation.yml`;
- `.github/workflows/validator-suite.yml`.

### Current behavior

```text
for each hard-coded validator:
  run Python entrypoint with --fixtures
  if return code != 0:
    stop and return that code
return 0
```

### Boundary

`run_all.py` is a **curated smoke/fixture aggregator**, not:

- automatic validator discovery;
- a registry of every validator;
- a proof that every schema family is covered;
- a complete release gate;
- a parallel CI configuration authority.

A bounded import search shows more shared-runner consumers than the seven aggregate entries. The seven-entrypoint list is therefore a selected subset, not the complete shared-runtime consumer inventory.

[Back to top](#top)

---

## Exit codes, outcomes, and output

### Current process exit codes

| Code | Confirmed meaning |
|---:|---|
| `0` | Requested validation or fixture-polarity checks completed successfully. |
| `1` | One or more explicit files failed; a fixture lane was empty; a valid fixture failed; an invalid fixture passed; a fixture could not be parsed or validated; or an aggregate child returned `1`. |
| `2` | `run()` was called without explicit files and without `--fixtures`. |

Uncaught schema-loading, registry-construction, argument-parsing, or aggregate-subprocess errors may terminate with other interpreter/process behavior. They are not normalized into the table above.

### Console tokens

| Token | Current meaning | Limitation |
|---|---|---|
| `OK` | One explicit instance or declared-valid fixture produced no schema errors. | Does not mean evidence/policy/release success. |
| `EXPECTED_FAIL` | A declared-invalid fixture was rejected by its schema as required. | Expected polarity only; not a governed denial, policy result, or proof. |
| `FAIL` | An explicit instance failed, fixture polarity was wrong, a fixture lane was empty, or fixture parsing/validation raised. | The first available diagnostic remains human-oriented and may include a path or schema message. |
| `No files provided` | No files and no fixture flag were supplied. | Human text only; no reason-code object. |

### Proposed stable reason-code families

The following are documentation proposals, not current emitted values:

```text
VALIDATOR_PASS
VALIDATOR_INSTANCE_INVALID
VALIDATOR_INSTANCE_PARSE_ERROR
VALIDATOR_SCHEMA_NOT_FOUND
VALIDATOR_SCHEMA_PARSE_ERROR
VALIDATOR_SCHEMA_ID_MISSING
VALIDATOR_DUPLICATE_SCHEMA_ID
VALIDATOR_REGISTRY_BUILD_ERROR
VALIDATOR_FIXTURE_ROOT_MISSING
VALIDATOR_VALID_FIXTURE_FAILED
VALIDATOR_INVALID_FIXTURE_PASSED
VALIDATOR_NO_INPUT
VALIDATOR_CONFIG_ERROR
VALIDATOR_INTERNAL_ERROR
```

A future result envelope should distinguish invalid candidate data from validator infrastructure failure.

[Back to top](#top)

---

## Fixture mode

### Current positive/negative contract

```text
valid/*.json   must validate
invalid/*.json must fail validation
```

This is a useful fail-closed polarity check and is exercised by CI through `make schemas`.

### Confirmed lane and diagnostic behavior

Fixture mode now:

1. sorts the `valid/*.json` lane and requires it to be nonempty;
2. sorts the `invalid/*.json` lane and requires it to be nonempty;
3. processes all valid fixtures before all invalid fixtures;
4. prints `OK` only when a declared-valid fixture validates;
5. prints `EXPECTED_FAIL` only when a well-formed declared-invalid fixture is
   rejected by the schema;
6. prints `FAIL` for empty lanes, polarity mismatches, malformed JSON, or
   validator exceptions;
7. returns `0` only when both nonempty lanes satisfy their declared polarity.

Fixture JSON is parsed once in this path. A malformed negative fixture is a
harness failure, not evidence of expected schema rejection. The prior combined
validation pass and its unreachable `rc == 2` branch have been removed.

The registry scan and both fixture lanes are explicitly sorted. Ten focused
standard-library tests pin this order, diagnostic polarity, non-vacuity, and
bounded error behavior. Filesystem-order effects for these discovered fixtures
are therefore **CONFIRMED corrected** for the tested path semantics.

[Back to top](#top)

---

## Current consumers and blast radius

A bounded exact-import search surfaced:

- **20 validator scripts** importing the shared runner;
- **6 test modules** importing the shared runner or loader.

Confirmed consumer classes include:

- top-level contract validators;
- release validators;
- Hydrology alias validators;
- MapLibre performance governance validators;
- schema fixture tests.

### Compatibility-sensitive surfaces

Treat these as internal-but-shared interfaces:

```text
tools.validators._common.local_resolver.build_registry
tools.validators._common.jsonschema_runner.load_validator
tools.validators._common.jsonschema_runner.validate_files
tools.validators._common.jsonschema_runner.run
```

Compatibility includes more than Python signatures:

- repository-root derivation;
- schema scan root and suffix;
- `$id` duplicate behavior;
- skipped missing `$id` behavior;
- exception types;
- console prefixes;
- first-error selection;
- fixture naming and directory conventions;
- exit codes;
- aggregate ordering and fail-fast behavior.

### Change discipline

Before changing shared behavior:

1. inventory all imports and subprocess callers;
2. classify behavior as bug fix, compatible extension, or breaking change;
3. add direct regression tests;
4. preserve or intentionally version output and exit codes;
5. update wrappers, Makefile, workflows, and docs together;
6. define rollback;
7. avoid dual implementations.

[Back to top](#top)

---

## Authority and anti-collapse

### Owning roots

| Responsibility | Owning home |
|---|---|
| Shared validator implementation | `tools/validators/_common/` |
| Validator entrypoints | `tools/validators/` and accepted sublanes |
| Semantic meaning | `contracts/` |
| Machine shape | `schemas/` |
| Policy decisions | `policy/` |
| Fixtures | `fixtures/` |
| Tests | `tests/` |
| Source authority | accepted registry/control-plane homes |
| Evidence and proofs | `data/proofs/` and accepted evidence homes |
| Process receipts | `data/receipts/` |
| Release/correction/rollback | `release/` |
| Public serving | governed applications and released artifacts |

### Disallowed collapses

```text
schema found                  -> schema accepted
schema validates              -> semantic contract satisfied
instance validates            -> evidence complete
instance validates            -> policy allowed
instance validates            -> release approved
fixture suite passes          -> all schemas covered
run_all passes                -> all validators passed
console OK                    -> public truth
registry entry exists         -> canonical schema identity
shared helper                 -> schema authority
```

### Fail-closed rule

Infrastructure errors must not become validation passes. Missing schemas, duplicate identities, parse failures, unresolved references, and unexpected exceptions must result in non-zero or explicit abstain/error outcomes.

[Back to top](#top)

---

## Path, security, resource, and privacy posture

### Confirmed current properties

The inspected `_common` Python modules:

- read local files;
- construct in-memory schema resources;
- perform no direct network calls;
- do not write lifecycle data;
- do not emit receipts or proofs;
- do not mutate schemas or fixtures.

### Path considerations

Current APIs accept `Path` values from validator entrypoints and CLI file arguments.

Before accepting untrusted or externally supplied paths, verify:

- repository-root containment where required;
- symlink behavior;
- traversal outside allowed roots;
- file type and extension;
- maximum file size;
- maximum file count;
- permission and access posture;
- error-message redaction.

### Resource considerations

No explicit limits were verified for:

- schema count;
- schema size;
- instance size;
- nesting depth;
- number of validation errors;
- validation time;
- aggregate subprocess duration.

Large or adversarial JSON/Schema inputs may require separate resource controls before this runtime is used with untrusted data.

### Privacy and sensitivity

Validation errors can echo schema messages, instance-derived values, or file paths. Do not send sensitive locations, credentials, living-person data, DNA/genomic material, archaeology, infrastructure details, private-land information, or restricted source content into public CI logs without a reviewed minimization strategy.

[Back to top](#top)

---

## Tests and CI

### Confirmed test coverage

`tests/schemas/test_common_contracts.py`:

- imports `load_validator`;
- discovers selected schema families;
- pairs schemas with fixture directories;
- asserts valid fixtures pass;
- asserts invalid fixtures fail;
- optionally checks expected error text or patterns.

`tests/schemas/test_hydrology_alias_contracts.py` also imports the shared runner.

### Confirmed CI wiring

```text
Makefile schemas
  -> python tools/validators/_common/run_all.py

schema-validation workflow
  -> pip install -e .
  -> make schemas

validator-suite workflow
  -> pip install -e .
  -> focused test_jsonschema_runner.py suite
  -> make schemas
  -> explicit invalid EvidenceBundle must return non-zero
```

### Confirmed focused runner coverage

`tests/validators/test_jsonschema_runner.py` contains ten deterministic,
synthetic, standard-library cases for:

- explicit valid and invalid exit/output polarity;
- no-input exit `2` before schema loading;
- sorted valid-then-invalid fixture order;
- `EXPECTED_FAIL` diagnostics for schema-invalid negative fixtures;
- nonempty valid and invalid lanes;
- reversed fixture polarity;
- malformed negative JSON as a harness `FAIL`;
- contained validator exceptions;
- missing fixture configuration.

### Direct tests still needed

Additional `_common` coverage should include:

- missing schema root;
- invalid schema JSON;
- schema without `$id`;
- duplicate `$id`;
- reference resolution;
- registry ordering;
- primary schema outside the scan root;
- malformed instance JSON;
- aggregate order and fail-fast behavior;
- child exit-code propagation;
- path containment and symlinks;
- resource limits;
- error redaction;
- format-keyword enforcement posture.

### Current verification commands

```bash
python tools/validators/_common/run_all.py
make schemas
python -m unittest discover --start-directory tests/validators --pattern 'test_jsonschema_runner.py' --verbose
python -m pytest tests/schemas/test_common_contracts.py -q
python -m pytest tests/schemas tests/contracts -q
make test
```

Passing these commands is implementation evidence for their declared scope only.

[Back to top](#top)

---

## Known gaps and conflicts

| ID | Gap or conflict | Status |
|---|---|---|
| COMMON-01 | v0.2 said `run_all.py` needed code verification; current code is confirmed. | Corrected in v0.3 |
| COMMON-02 | Fixture mode prints expected invalid fixtures as `FAIL` while the run may succeed. | Corrected in v0.4 with `EXPECTED_FAIL` |
| COMMON-03 | `if rc == 2` after `validate_files()` is unreachable. | Corrected in v0.4; branch removed |
| COMMON-04 | Aggregate runner is hard-coded to seven entrypoints while shared imports are broader. | CONFIRMED |
| COMMON-05 | No structured `ValidationReport` output is emitted. | CONFIRMED absence |
| COMMON-06 | Only the first validation error per explicit file is printed. | CONFIRMED |
| COMMON-07 | Format-keyword enforcement is not explicitly configured in `load_validator()`. | NEEDS VERIFICATION |
| COMMON-08 | Fixture iteration was not explicitly sorted in the CLI runner. | Corrected and directly tested in v0.4 |
| COMMON-09 | Direct unit coverage for registry, aggregate, and remaining CLI error branches is incomplete. | PARTIAL; ten runner cases added in v0.4 |
| COMMON-10 | Relative schema/fixture paths assume repository-root execution. | CONFIRMED wrappers |
| COMMON-11 | Working registry logic overlaps a proposed `packages/schema-registry` extraction. | CONFLICTED |
| COMMON-12 | Stable API, output, exit-code, and deprecation policy are absent. | NEEDS VERIFICATION |
| COMMON-13 | Resource, path, symlink, timeout, and log-redaction limits are not established. | NEEDS VERIFICATION |
| COMMON-14 | ADR-0001 declares the intended schema home but remains `proposed`. | CONFIRMED status |

This README records the remaining conditions and the bounded v0.4 corrections;
it does not claim the unresolved items are repaired.

[Back to top](#top)

---

## Schema-registry package extraction boundary

The repository contains a proposed reusable package namespace:

```text
packages/schema-registry/src/schema_registry/
```

Its current README confirms that:

- the package namespace is a placeholder;
- its initializer is empty;
- its `core.py` is comment-only;
- no accepted package API or consumers are established;
- working local registry logic remains in `_common/local_resolver.py`.

### No-dual-implementation rule

Do not independently evolve equivalent registry logic in both locations.

Until an accepted extraction decision:

```text
working implementation = tools/validators/_common/
package namespace       = proposed placeholder
```

### Extraction requirements

A future move to `packages/schema-registry` must define:

1. accepted package API and version;
2. schema-root and `$id` parity;
3. skip/duplicate/error behavior;
4. deterministic ordering;
5. path and resource security;
6. tests covering both old and new behavior;
7. all import and subprocess consumers;
8. compatibility shim or coordinated cutover;
9. deprecation window;
10. rollback to the prior `_common` implementation;
11. documentation and generated receipts.

The package must remain a resolution utility, not schema authority.

[Back to top](#top)

---

## What belongs here

Good fits:

- repository-local schema registry construction used only by validator tooling;
- Draft 2020-12 validator construction;
- common JSON parsing and validation plumbing;
- deterministic error normalization;
- shared fixture polarity helpers;
- internal CLI/exit-code utilities;
- aggregate fixture-runner support;
- compatibility adapters during an approved extraction;
- helper-local documentation.

A helper belongs here only when it is:

- shared across multiple validators;
- subordinate to external schemas/contracts/policy;
- deterministic or explicitly bounded;
- no-network by default;
- read-only with respect to governed records;
- directly tested;
- free of domain-specific meaning and release decisions.

[Back to top](#top)

---

## What does not belong here

| Do not put here | Correct home |
|---|---|
| Domain-specific validation rules | accepted domain validator lane |
| Top-level user-facing validator entrypoints | `tools/validators/` or accepted sublane |
| Canonical schemas or `$id` authority records | `schemas/` and accepted governance registers |
| Semantic object meaning | `contracts/` |
| Allow/deny/restrict/abstain policy | `policy/` |
| Fixture payloads | `fixtures/` |
| Test suites | `tests/` |
| Source descriptors or activation decisions | accepted registry/control-plane homes |
| Validation report records | accepted `data/` report/receipt home |
| EvidenceBundles or proof packs | `data/proofs/` |
| Release decisions or rollback cards | `release/` |
| Ingest, transform, catalog, or publication workflows | `connectors/`, `pipelines/`, release tooling |
| Public API/UI behavior | governed application roots |
| Credentials, private endpoints, exact sensitive data | denied |

[Back to top](#top)

---

## Smallest sound improvement sequence

1. **Completed in v0.4:** add focused direct tests for runner behavior.
2. **Completed in v0.4:** distinguish expected invalid cases from operational failure.
3. **Completed in v0.4:** remove the unreachable fixture-mode `rc == 2` branch.
4. **Completed in v0.4:** sort fixture discovery and require nonempty lanes.
5. Define stable result and exit-code contracts.
6. Decide whether all errors or only the first error are reported.
7. Pin format-keyword enforcement posture.
8. Add path, resource, timeout, and redaction controls.
9. Reconcile the seven-entrypoint aggregate list with intended coverage.
10. Decide retain-versus-extract for `packages/schema-registry`.
11. Migrate consumers with parity tests and rollback.
12. Update parent docs, workflows, and runbooks with verified behavior.

Each item should be a small, reviewable change. Do not combine package extraction, output redesign, and validator behavior changes without an ADR/migration plan and broad regression coverage.

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Direct implementation files are identified.
- [x] Current helper functions and exit codes are documented.
- [x] CI, Makefile, aggregate runner, and generic fixture test wiring are grounded.
- [x] Fixture-output, non-vacuity, ordering, and removed dead-branch behavior are documented.
- [x] Schema authority, policy, evidence, release, and public boundaries are explicit.
- [x] Package extraction conflict is visible.

### Implementation quality

- [ ] Direct tests cover every helper function and error branch.
- [x] Fixture output has unambiguous expected-invalid semantics.
- [x] Fixture ordering is deterministic.
- [ ] Result/exit-code compatibility is documented and tested.
- [ ] Format-keyword posture is explicit and tested.
- [ ] Path, symlink, size, count, depth, timeout, and redaction controls are accepted.
- [ ] Structured result reporting is accepted or explicitly rejected.
- [ ] Aggregate-runner scope is intentional and tested.
- [ ] CODEOWNERS and reviewer burden are enforced.

### Extraction and lifecycle

- [ ] Retain-versus-extract decision is accepted.
- [ ] No dual registry implementation exists.
- [ ] Consumer inventory is complete.
- [ ] Compatibility/deprecation window is defined.
- [ ] Correction and rollback are exercised.
- [ ] Documentation and receipts match implementation.

Until these close: **working internal shared runtime; compatibility-sensitive; non-authoritative; extraction unresolved**.

[Back to top](#top)

---

## Open verification register

| ID | Item | Status |
|---|---|---|
| VCOMMON-01 | Assign validator/schema/Python tooling owners. | NEEDS VERIFICATION |
| VCOMMON-02 | Confirm exhaustive direct inventory and all consumers. | NEEDS VERIFICATION |
| VCOMMON-03 | Define stable API and compatibility policy. | NEEDS VERIFICATION |
| VCOMMON-04 | Define structured result/report posture. | NEEDS VERIFICATION |
| VCOMMON-05 | Resolve fixture console semantics. | CONFIRMED corrected in v0.4 |
| VCOMMON-06 | Resolve unreachable return-code branch. | CONFIRMED corrected in v0.4 |
| VCOMMON-07 | Confirm deterministic fixture ordering on supported systems. | CONFIRMED by sorted discovery and focused tests in v0.4 |
| VCOMMON-08 | Confirm format-keyword enforcement requirements. | NEEDS VERIFICATION |
| VCOMMON-09 | Add direct registry, runner, and aggregate tests. | PARTIAL; focused runner suite added, registry and aggregate remain |
| VCOMMON-10 | Define allowed path roots and symlink behavior. | NEEDS VERIFICATION |
| VCOMMON-11 | Define schema/instance resource budgets. | NEEDS VERIFICATION |
| VCOMMON-12 | Define sensitive error/log redaction. | NEEDS VERIFICATION |
| VCOMMON-13 | Reconcile aggregate runner with intended validator coverage. | NEEDS VERIFICATION |
| VCOMMON-14 | Decide `_common` retention versus package extraction. | NEEDS VERIFICATION |
| VCOMMON-15 | Define migration, deprecation, correction, and rollback. | NEEDS VERIFICATION |
| VCOMMON-16 | Confirm ADR-0001 acceptance or successor status. | NEEDS VERIFICATION |

[Back to top](#top)

---

## Maintenance, correction, migration, and rollback

### Maintenance triggers

Update this README when:

- helper files, signatures, or behavior change;
- registry scan roots, suffixes, `$id` behavior, or dialect change;
- output text, error selection, fixture conventions, or exit codes change;
- aggregate entrypoints change;
- tests or workflows change;
- `schema-registry` extraction advances;
- security/resource controls change;
- correction or rollback reveals undocumented behavior.

### Documentation correction

1. preserve the prior blob and evidence snapshot;
2. identify the incorrect statement and affected consumers;
3. correct through review;
4. update parent validator, package, workflow, and test documentation;
5. preserve supersession and changelog history.

### Code migration

A behavior or package migration must:

1. inventory imports, subprocess calls, Make targets, and workflows;
2. capture current behavior with regression tests;
3. define compatibility and breaking changes;
4. implement one authoritative path;
5. provide a time-bounded shim only when necessary;
6. prevent dual execution and dual registry behavior;
7. validate positive, negative, error, path, and resource cases;
8. update consumers and CI;
9. document deprecation and removal;
10. verify rollback.

### Rollback for the v0.4 runner slice

Before merge, close the review branch. After merge, revert the complete v0.4
commit through a reviewed pull request: restore runner blob
`ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6`, workflow blob
`1694afdd762ce515b53fc8e9d7d51324c2d0929d`, and this README's prior blob
`12df3198498356b32bf309a314eb255604b37415`; restore the paired test-lane and
workflow documentation preimages; and remove the focused test and generated
receipt. Do not restore the ambiguous fixture output without also restoring its
matching tests, documentation, and workflow expectations.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Supports | Does not prove |
|---|---|---|
| Current `_common` README | Prior scope and documentation lineage | Current code behavior by itself |
| `local_resolver.py` | Registry root, sorted scan, `$id` skip, duplicate failure | Schema acceptance or alias policy |
| `jsonschema_runner.py` | Validator construction, explicit file mode, fixture mode, output, exit paths | Semantic correctness or release readiness |
| `run_all.py` | Seven hard-coded aggregate entries and fail-fast behavior | Complete validator coverage |
| Top-level validator wrappers | Relative schema/fixture paths and shared-runner imports | All consumers or supported CWDs |
| Exact-import search | Twenty validator and six test consumers surfaced | Exhaustive dependency graph |
| `test_jsonschema_runner.py` | Ten synthetic cases for explicit and fixture polarity, order, non-vacuity, errors, configuration, and exit behavior | Resolver internals, aggregate subprocess behavior, complete path/resource controls, or semantic validity |
| `test_common_contracts.py` | Generic fixture polarity tests using `load_validator` | Direct coverage of every helper branch |
| Makefile | `make schemas` invokes aggregate runner | Overall repository correctness |
| Schema workflows | CI invokes the focused runner suite, `make schemas`, and a fail-closed invalid check | Production use or complete policy enforcement |
| Root `pyproject.toml` | Python and `jsonschema` dependency bounds | Full supported environment matrix |
| Schema-registry package README | Placeholder package and extraction conflict | Accepted extraction or working package |
| ADR-0001 | Proposed schema-home decision | Accepted status or field-level schema quality |
| Directory Rules | Responsibility-root placement | Exact helper API or implementation correctness |

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Status |
|---|---|---|---|
| v0.2 | 2026-07-07 | Expanded shared-helper documentation while retaining implementation uncertainty. | Superseded |
| v0.3 | 2026-07-16 | Grounded direct implementation, consumers, CI, exit/output behavior, fixture semantics, known defects, security/resource posture, and schema-registry extraction conflict. | Draft / repository-grounded |
| v0.4 | 2026-08-01 | Corrected fixture ordering, non-vacuity, expected-invalid diagnostics, dead-branch behavior, direct runner tests, CI wiring, and current consumer/aggregate evidence. | Draft / repository-grounded |

---

> **Final rule:** `_common` may normalize validator mechanics. It must never normalize away the evidence, authority, uncertainty, policy, sensitivity, review, release, correction, or rollback boundaries that validators are supposed to enforce.

[Back to top](#top)
