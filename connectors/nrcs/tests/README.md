<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nrcs-tests-readme
title: connectors/nrcs/tests/ — NRCS Connector Test, Fixture, and Safety Boundary
type: readme
version: v0.2
status: draft; repository-grounded; test-envelope; implementation-empty; fixture-empty; ci-unproved; non-authoritative
owners: OWNER_TBD — Connector steward · Source steward · NRCS steward · Package steward · Test steward · Fixture steward · Soil steward · Agriculture liaison · Hydrology liaison · Atmosphere/Climate liaison · Tribal/sovereignty reviewer · Rights reviewer · Sensitivity reviewer · Security steward · Validation steward · Contract steward · Schema steward · Receipt steward · CI steward · Migration steward · Docs steward
created: 2026-06-20
updated: 2026-07-15
supersedes: v0.1 planning-oriented NRCS connector test guide (2026-06-20)
policy_label: "public-doctrine; connector-test-boundary; nrcs; implementation-empty; fixture-empty; no-network-by-default; live-tests-denied-by-default; deterministic; fail-closed; descriptor-gated; profile-pinned; product-isolated; rights-aware; sensitivity-aware; sovereignty-aware; archive-safe; resource-bounded; temp-only-writes; raw-quarantine-contract; no-publication; no-secrets; ci-unproved; rollback-aware"
current_path: connectors/nrcs/tests/README.md
truth_posture: CONFIRMED target v0.1 README, merged NRCS source-root and namespace v0.2 contracts, grounded SDA/SCAN/SSURGO/gSSURGO/gNATSGO product boundaries, kfm-connector-nrcs 0.0.0 placeholder metadata, empty namespace initializer, root pytest optional dependency and pythonpath configuration, TODO-only connector-gate workflow, and bounded absence of named safety/product tests, test conftest, fixture-root README, package-local pytest/tox configuration, and dedicated NRCS workflows / PROPOSED test architecture, marker vocabulary, fixture manifest, deterministic isolation, product-specific matrices, finite outcomes, negative tests, property/fuzz tests, live-test quarantine, CI admission, correction, migration, deprecation, and rollback / CONFLICTED rich test documentation versus absent executable suite, product-specific contracts versus no test collection, root pytest availability versus absent package-local build/discovery configuration, and green generic connector workflow versus echo-only commands / UNKNOWN accepted test owners, collection command, package installation mode, dependencies, marker registration, fixture authority, snapshot licensing, network interception mechanism, subprocess policy, coverage thresholds, CI matrix, live-test environment, emitted reports, flake posture, runtime duration, and enforcement / NEEDS VERIFICATION test ownership, fixture governance, source/profile references, package build and import behavior, product adapter implementation, negative-test coverage, schema/contract pinning, CI wiring, release-blocking status, correction, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 3bf8b1440669bd77bb2ad35d047b290bb3f9c5ca
  prior_blob: 7c65ba6ef85a8369e17c40d5e3fbc388b04a306b
  nrcs_source_root_blob: 7edac87aec3ff4ed5621dedd5c31ebaa2b04759a
  nrcs_namespace_blob: 00d12e0f07e53cff877e9ea4d396c96b3fb03658
  package_metadata_blob: c6bb1565db7df490bee52a597d04d694e2b9f8a4
  namespace_initializer_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  root_pyproject_blob: e3bd40e8e6ce14dfcde78ff5c09608095c3eca76
  sda_boundary_blob: 6f3ba95d70ae0779d00e26ad360f7b8737dbf77a
  scan_boundary_blob: 76eb5a0683e571d045d01d7e8dc387ef497ba958
  ssurgo_boundary_blob: 357efa694fb059ed91eed3bc2b78829b673f14c3
  gssurgo_boundary_blob: 3ad1db6721224232f4e5eb99440a7b031bdb7afa
  gnatsgo_boundary_blob: 83b3816033fc558fd552480edefdde978488ccfd
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  source_admission_adr_blob: 0e8d03786bcc99b19f179680890df9e30a27633a
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  bounded_path_checks:
    - connectors/nrcs/tests/README.md existed at version v0.1 before this revision
    - connectors/nrcs/tests/conftest.py was not found
    - connectors/nrcs/tests/fixtures/README.md was not found
    - connectors/nrcs/tests/test_import_safety.py was not found
    - connectors/nrcs/tests/test_descriptor_gates.py was not found
    - connectors/nrcs/tests/test_sda_parser.py was not found
    - connectors/nrcs/tests/test_scan_parser.py was not found
    - connectors/nrcs/tests/test_ssurgo_manifest.py was not found
    - connectors/nrcs/tests/test_gssurgo_metadata.py was not found
    - connectors/nrcs/tests/test_gnatsgo_metadata.py was not found
    - connectors/nrcs/pytest.ini was not found
    - connectors/nrcs/tox.ini was not found
    - .github/workflows/nrcs.yml was not found
    - .github/workflows/nrcs-connector.yml was not found
    - repository search for the named tests returned only this README
    - connectors/nrcs/pyproject.toml contains only project name kfm-connector-nrcs and version 0.0.0
    - connectors/nrcs/src/nrcs/__init__.py is empty
    - root pyproject declares pytest as an optional test dependency and pythonpath equals repository root
    - .github/workflows/connector-gate.yml contains TODO echo steps
related:
  - ../README.md
  - ../src/README.md
  - ../src/nrcs/README.md
  - ../pyproject.toml
  - ../sda/README.md
  - ../scan/README.md
  - ../ssurgo/README.md
  - ../gssurgo/README.md
  - ../gnatsgo/README.md
  - ../../../pyproject.toml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../.github/workflows/connector-gate.yml
tags: [kfm, connectors, nrcs, tests, pytest, fixtures, no-network, deterministic, import-safety, descriptor-gates, source-activation, rights, sensitivity, tribal-review, sda, scan, ssurgo, gssurgo, gnatsgo, archive-safety, lineage, grid, raw, quarantine, finite-outcomes, ci, correction, rollback]
notes:
  - "This revision changes only connectors/nrcs/tests/README.md."
  - "Current repository evidence establishes a README-only test lane; no executable NRCS test or connector-local fixture is claimed."
  - "The root repository exposes pytest as an optional dependency, but package collection, installation, product coverage, and CI enforcement remain unproved."
  - "Tests may prove implementation behavior against accepted profiles; they do not activate sources, establish source truth, close evidence, approve policy, or authorize release."
  - "Live network tests are denied by default and may never be a prerequisite for deterministic pull-request validation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS Connector Test, Fixture, and Safety Boundary

`connectors/nrcs/tests/`

> Repository-present test envelope for the USDA NRCS connector family. Current evidence establishes this README only—not an executable test suite, governed fixture collection, package-installation proof, product coverage, or substantive CI gate.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![network](https://img.shields.io/badge/network-DENIED__by__default-critical)
![fixtures](https://img.shields.io/badge/fixtures-NOT__ESTABLISHED-orange)
![CI](https://img.shields.io/badge/CI-NOT__SUBSTANTIVE-red)
![lifecycle](https://img.shields.io/badge/lifecycle-TEMP__ONLY-blue)
![publication](https://img.shields.io/badge/publication-DENIED-red)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-and-directory-rules-basis) · [Split](#package-source-product-and-test-split) · [Tree](#confirmed-bounded-tree) · [Invariants](#keystone-invariants) · [Classes](#test-classes-and-markers) · [Fixtures](#fixture-governance) · [Isolation](#determinism-and-isolation) · [Security](#security-sensitive-data-and-observability) · [Contracts](#profile-contract-and-schema-pinning) · [Outcomes](#finite-outcomes-and-reason-codes) · [Products](#product-specific-test-matrices) · [Collapse](#cross-product-anti-collapse-tests) · [Build](#build-install-and-import-tests) · [Resources](#resource-and-adversarial-tests) · [Live](#live-integration-test-policy) · [CI](#ci-admission-and-reporting) · [Tree proposal](#proposed-future-tree) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Validation](#validation-commands) · [Ledger](#evidence-ledger) · [Checklist](#maintainer-checklist) · [Rollback](#rollback-correction-deprecation-and-migration)

> [!IMPORTANT]
> **This README is not proof that tests exist or pass.** Every proposed path, marker, fixture shape, command, and threshold below remains `PROPOSED` until backed by repository files, collection output, test results, and CI evidence.

> [!CAUTION]
> **A passing connector test is not source admission, source truth, EvidenceBundle closure, policy approval, release approval, or public safety.** Tests prove bounded software behavior against reviewed expectations. They do not confer authority on the source or its outputs.

---

<a id="purpose"></a>

## Purpose

This README governs test code and fixture use for the NRCS connector family.

A conforming test lane may eventually prove:

- package import is side-effect-free;
- network access is denied unless a test explicitly opts into an approved isolated transport;
- source and product profiles are required and pinned;
- parsers preserve source-native identity, time, quality, scale, units, keys, relationships, and digests;
- malformed, stale, ambiguous, oversized, sensitive, or policy-blocked inputs fail closed;
- connector-local results use finite outcomes and stable reason codes;
- connectors return RAW or QUARANTINE candidates and receipt-ready facts without writing governed stores directly;
- product-specific behavior remains isolated across SDA, SCAN, SSURGO, gSSURGO, and gNATSGO;
- no test creates public artifacts, release decisions, evidence closure, or authoritative claims.

This test root must not become:

- source or product doctrine;
- a `SourceDescriptor`, source-authority, contract, schema, policy, or release home;
- a hidden implementation package;
- a fixture-based substitute for live source admission;
- a credential store or private data cache;
- a lifecycle, receipt, proof, catalog, triplet, or published-data store;
- a public API, UI, map, notification, or AI-answer surface.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v0.1 before revision** | A planning-oriented test guide existed. |
| Direct test files | **NOT FOUND at checked paths** | No named NRCS safety or product test is established. |
| Fixture root | **NOT FOUND at checked path** | No connector-local fixture inventory or fixture contract is established. |
| Test `conftest.py` | **NOT FOUND** | No lane-specific network, filesystem, clock, environment, or marker guard is established. |
| Package metadata | **CONFIRMED minimal** | `kfm-connector-nrcs` is version `0.0.0`; test dependencies and package discovery are not declared there. |
| Namespace initializer | **CONFIRMED empty** | There is no executable package surface for tests to import. |
| Root pytest support | **CONFIRMED partial** | Root metadata includes pytest as an optional dependency and sets repository-root `pythonpath`; this does not prove NRCS collection or installation. |
| Package-local pytest/tox configuration | **NOT FOUND** | Marker registration, strictness, timeouts, warnings, and package matrix are not established locally. |
| Dedicated NRCS workflows | **NOT FOUND at checked paths** | No dedicated package/product test workflow is established. |
| Generic connector workflow | **CONFIRMED TODO-only** | A green run proves workflow execution only. |
| Product implementation | **NOT ESTABLISHED** | Product READMEs are grounded contracts, not executable adapter proof. |
| Source activation | **NOT ESTABLISHED** | The inspected authority register remains `PROPOSED` with no entries. |

### Truth labels

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Verified from current repository content, exact path checks, or generated validation in this work. |
| **PROPOSED** | Candidate test design requiring implementation and review. |
| **CONFLICTED** | Current evidence expresses competing paths, vocabularies, or authority claims. |
| **UNKNOWN** | Runtime, collection, fixture, source, or CI state was not established. |
| **NEEDS VERIFICATION** | Checkable before implementation or reliance, but unresolved. |

### What this revision does not establish

This README does not establish:

- test collection;
- a supported Python matrix;
- a buildable or installable `kfm-connector-nrcs` distribution;
- product adapters or exports;
- fixture files or fixture rights;
- marker registration;
- test coverage or pass rates;
- network interception;
- source activation;
- release-blocking CI;
- operational source behavior.

[Back to top](#top)

---

<a id="authority-and-directory-rules-basis"></a>

## Authority and Directory Rules basis

Directory Rules place source-specific implementation under `connectors/` and tests beside or under the implementation lane when they test connector behavior. The existing `connectors/nrcs/tests/` path is therefore a sound candidate test root for the NRCS connector package.

Placement does not confer authority.

| Concern | Owning surface | Test-lane posture |
|---|---|---|
| Connector implementation | [`../src/`](../src/README.md) | Import and exercise; do not duplicate implementation. |
| Namespace behavior | [`../src/nrcs/`](../src/nrcs/README.md) | Verify accepted API and import contracts once implemented. |
| Product source-edge contracts | [`../sda/`](../sda/README.md), [`../scan/`](../scan/README.md), [`../ssurgo/`](../ssurgo/README.md), [`../gssurgo/`](../gssurgo/README.md), [`../gnatsgo/`](../gnatsgo/README.md) | Derive test obligations; do not redefine product meaning. |
| Package build metadata | [`../pyproject.toml`](../pyproject.toml) | Verify once build/discovery is accepted. |
| Repository test runner | [`../../../pyproject.toml`](../../../pyproject.toml) | Consume reviewed configuration; do not silently override globally. |
| Source admission | [`ADR-0017`](../../../docs/adr/ADR-0017-source-descriptor-admission-process.md) and the authority register | Test gates; do not activate a source. |
| Contracts and schemas | `contracts/` and `schemas/` | Pin accepted versions and validate behavior; do not copy authority locally. |
| Rights and sensitivity | `policy/rights/` and `policy/sensitivity/` | Test fail-closed decisions with sanitized fixtures. |
| Lifecycle data | `data/raw/`, `data/quarantine/`, later lifecycle roots | Never write real stores; use temporary directories. |
| Receipts and proofs | `data/receipts/` and `data/proofs/` | Validate candidate shapes or returned facts; do not emit authority records in unit tests. |
| Release | `release/` | Test denial and handoff boundaries; do not approve release. |
| CI orchestration | [generic connector workflow](../../../.github/workflows/connector-gate.yml) or an accepted dedicated workflow | Require substantive commands before treating green as evidence. |

> [!IMPORTANT]
> Test files may encode assertions derived from accepted contracts and profiles. They must not become the only place where source rights, product identity, field meaning, policy, or release rules exist.

[Back to top](#top)

---

<a id="package-source-product-and-test-split"></a>

## Package, source, product, and test split

| Layer | Primary responsibility |
|---|---|
| `connectors/nrcs/` | Distribution and connector-family boundary. |
| `connectors/nrcs/src/` | Python source placement, discovery, dependency direction, and module admission. |
| `connectors/nrcs/src/nrcs/` | Proposed import namespace and shared source-admission behavior. |
| Product lanes | Product-specific source-edge contracts and anti-collapse rules. |
| `connectors/nrcs/tests/` | Executable tests, governed fixture adapters, test-only helpers, and software-behavior reports. |
| External fixture authority | An accepted fixture root and manifest contract, if governance selects one. |
| Pipelines | Downstream transformation and lifecycle progression. |
| Contracts, schemas, policy, registry, receipts, proofs, and release | Governing authority and auditable records. |

### Allowed dependencies

```text
tests -> public or explicitly testable package interfaces
tests -> reviewed fixtures / fixture manifests
tests -> accepted contracts, schemas, profiles, and policy test inputs
tests -> temporary filesystem and isolated process resources
```

### Forbidden dependency direction

```text
production package -> tests
production package -> test fixtures
source authority -> test implementation
policy authority -> test helper constants
release authority -> passing test status
public client -> connector tests
```

[Back to top](#top)

---

<a id="confirmed-bounded-tree"></a>

## Confirmed bounded tree

At the checked base, the directly verified test lane is:

```text
connectors/nrcs/tests/
└── README.md
```

The following are **not current repository facts**:

- `conftest.py`;
- a `fixtures/` directory;
- safety tests;
- product parser tests;
- marker definitions;
- snapshot manifests;
- golden outputs;
- property tests;
- fuzz targets;
- dedicated workflow files;
- package-local pytest or tox configuration.

Any future tree in this README is explicitly `PROPOSED`.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

Every future NRCS connector test must preserve these invariants.

1. **No network by default.**
2. **No source activation by test success.**
3. **No secrets, private sessions, or private source material.**
4. **No writes to governed lifecycle or authority stores.**
5. **No public artifacts, releases, or authoritative claims.**
6. **Products remain distinct.**
7. **Source authority role and domain support type remain distinct fields.**
8. **Native identity, time, scale, units, quality, relationships, and digests are preserved.**
9. **Unknown or unsupported behavior fails closed.**
10. **Finite outcomes and reason codes are asserted.**
11. **Fixtures are governed inputs, not source truth.**
12. **A green test proves only the behavior it actually exercised.**
13. **Live checks are optional, isolated, and never required for deterministic pull-request validation.**
14. **Every corrective test remains traceable to the defect, contract change, or incident it prevents.**

[Back to top](#top)

---

<a id="test-classes-and-markers"></a>

## Test classes and markers

The marker vocabulary below is **PROPOSED** and must be registered before use.

| Proposed marker | Purpose | Default CI |
|---|---|---:|
| `unit` | Pure function and value-object behavior. | Included |
| `contract` | Accepted schema, semantic contract, profile, and result-shape conformance. | Included |
| `fixture` | Parsing and preservation against governed local fixtures. | Included |
| `security` | Archive, path, redirect, decompression, secret, log, and resource misuse. | Included |
| `property` | Generated invariant checks over bounded input domains. | Included when deterministic |
| `fuzz` | Seeded malformed-input and parser-hardening campaigns. | Bounded subset |
| `integration_local` | Multiple local components without network or governed-store writes. | Included |
| `live_probe` | Explicit read-only external probe. | Excluded by default |
| `slow` | Deterministic test exceeding the accepted unit budget. | Separate job |
| `sensitive_review` | Sanitized tests requiring rights, sovereignty, or sensitivity reviewer approval. | Separate reviewed lane |

A proposed strict invocation after implementation is:

```bash
python -m pytest \
  connectors/nrcs/tests \
  -m "not live_probe" \
  --strict-markers \
  --strict-config
```

This command is **PROPOSED**. Current collection and marker configuration are not established.

### Test naming

Prefer names that state the boundary:

```text
test_import_does_not_open_network
test_inactive_descriptor_denies_live_request
test_sda_rejects_unapproved_query_text
test_scan_preserves_sensor_depth
test_ssurgo_rejects_archive_path_traversal
test_gssurgo_preserves_native_grid
test_gnatsgo_requires_product_identity
```

Avoid names that imply authority:

```text
test_source_is_authoritative
test_data_is_public
test_release_is_approved
test_fixture_proves_truth
```

[Back to top](#top)

---

<a id="fixture-governance"></a>

## Fixture governance

### Fixture posture

Fixtures must be one of:

- synthetic and source-shaped;
- minimized from a public source under reviewed terms;
- redacted and generalized;
- generated from an accepted schema/profile;
- an explicitly approved, immutable snapshot.

Fixtures must never include:

- credentials, cookies, tokens, private URLs, or session artifacts;
- private landowner, producer, customer, or operator records;
- restricted cultural or sovereign information;
- unreviewed Tribal station details;
- reconstructive rare-species, archaeology, infrastructure, or private-location content;
- uncontrolled full-size source packages;
- source material whose redistribution posture is unresolved.

### Proposed fixture manifest

Each fixture should have a sidecar manifest or equivalent record. This shape is illustrative and non-canonical:

```yaml
fixture_id: nrcs:<product>:<purpose>:<version>
product: sda | scan | ssurgo | gssurgo | gnatsgo
purpose: parser-positive | parser-negative | security | drift | correction
origin: synthetic | minimized-public | approved-snapshot
source_ref: null
profile_ref: null
created_or_retrieved_at: 2026-07-15T00:00:00Z
content_digest: sha256:<hex>
rights_review: pending | approved | denied
sensitivity_review: pending | approved | denied
sovereignty_review: not_applicable | pending | approved | denied
redaction_or_minimization: <summary>
expected_outcome: PASS | ABSTAIN | QUARANTINE | DENY | ERROR
expected_reason_codes: []
immutable: true
```

### Fixture identity

Fixture identity must include:

- product lane;
- purpose;
- source/profile context;
- content digest;
- fixture version;
- expected outcome;
- correction or supersession lineage.

Changing fixture bytes without changing the digest and reviewed fixture version is prohibited.

### Golden files

Golden outputs may be used only when:

- the output is deterministic;
- ordering and normalization rules are explicit;
- sensitive content is absent;
- the review can distinguish an intended contract change from accidental drift;
- the golden file is not mistaken for an authoritative source record.

[Back to top](#top)

---

<a id="determinism-and-isolation"></a>

## Determinism and isolation

### Network isolation

Default tests must fail before any DNS lookup, socket connection, HTTP request, cloud call, or source SDK call leaves the process.

Required proof should cover:

- package import;
- configuration construction;
- parser invocation;
- fixture loading;
- error formatting;
- retry setup;
- redirect handling;
- cache lookup;
- receipt-fact construction.

A test that merely avoids calling a mocked client does not prove network denial. The suite should install an explicit deny guard at the lowest practical transport boundary.

### Filesystem isolation

Tests may write only to isolated temporary directories.

They must not write to:

```text
data/raw/
data/quarantine/
data/work/
data/processed/
data/catalog/
data/triplets/
data/published/
data/receipts/
data/proofs/
release/
```

Tests should assert:

- no repository file changed;
- no cache escaped the temporary root;
- cleanup runs after success and failure;
- partial files do not remain after cancellation or parser error;
- symlinks and path traversal cannot escape the test root.

### Clock isolation

Tests involving time must inject or freeze:

- source time;
- valid time;
- retrieval time;
- fixture creation time;
- freshness reference time;
- correction time;
- retry/backoff time.

Wall-clock dependence without an explicit tolerance contract is prohibited.

### Randomness

Random or generated tests must:

- use recorded seeds;
- bound case counts and input sizes;
- emit the seed on failure;
- avoid nondeterministic ordering;
- support local reproduction.

### Environment and process isolation

Tests must not depend on:

- developer home-directory files;
- ambient credentials;
- mutable global environment variables;
- local timezone;
- locale-dependent parsing;
- external command availability unless the test explicitly checks and isolates it;
- current working directory outside a declared test root;
- editable-install path leakage.

[Back to top](#top)

---

<a id="security-sensitive-data-and-observability"></a>

## Security, sensitive data, and observability

### Secret handling

Tests must prove:

- secret-looking values are redacted from errors and logs;
- authorization headers are not persisted;
- query parameters or station identifiers are minimized where policy requires;
- fixture manifests do not embed credentials;
- failure reports do not dump full payloads by default.

### Log assertions

Logs should be tested for both presence and absence.

Expected presence may include:

- product lane;
- finite outcome;
- stable reason code;
- safe request or package identity;
- bounded byte/row/member counts;
- profile IDs;
- correction or quarantine status.

Expected absence includes:

- credentials;
- private URLs;
- cookies;
- unreviewed query text;
- raw sensitive coordinates;
- private party identities;
- full source payloads;
- unrestricted archive member content.

### Sensitive and sovereign material

Tests involving Tribal SCAN, precise stations, private land joins, cultural material, or reconstructive location risk require:

- synthetic or approved minimized fixtures;
- explicit sensitivity and sovereignty review;
- no exact operational coordinates unless specifically authorized;
- denial tests for unreviewed outward disclosure;
- verification that logs, snapshots, and failure artifacts remain safe.

[Back to top](#top)

---

<a id="profile-contract-and-schema-pinning"></a>

## Profile, contract, and schema pinning

A test must identify the contract it proves.

At minimum, product tests should pin or receive:

- source descriptor reference;
- activation-state vocabulary;
- source role;
- support type;
- endpoint, query, request, package, archive, or grid profile;
- contract/schema IDs and versions where accepted;
- rights and sensitivity posture;
- finite outcome and reason-code vocabulary.

### Drift behavior

Tests must not silently update expectations when:

- source fields change;
- package members change;
- column order changes;
- query result shape changes;
- CRS or resolution changes;
- quality or missingness vocabularies change;
- null/sentinel behavior changes;
- a schema becomes more permissive;
- profile IDs or versions change.

Drift should produce an explicit result such as:

```text
QUARANTINE / PROFILE_DRIFT
ABSTAIN / CONTRACT_UNRESOLVED
DENY / RIGHTS_UNRESOLVED
ERROR / PARSER_UNSUPPORTED
```

These values are illustrative until an accepted connector-result contract exists.

### Permissive schemas

A permissive schema does not prove semantic correctness. Tests must separately assert required invariants when a schema:

- declares no properties;
- permits arbitrary additional properties;
- does not encode relationships;
- does not distinguish source role from support type;
- does not encode time, scale, rights, sensitivity, or correction state.

[Back to top](#top)

---

<a id="finite-outcomes-and-reason-codes"></a>

## Finite outcomes and reason codes

The exact machine contract remains `NEEDS VERIFICATION`. A future test suite should require a finite connector-local outcome family.

| Proposed outcome | Meaning |
|---|---|
| `PASS` | Behavior satisfies the tested local contract; no authority or release implication. |
| `ABSTAIN` | Required profile, contract, or evidence is unavailable or unresolved. |
| `QUARANTINE` | Material may be preserved but must not progress without review. |
| `DENY` | Policy, rights, sensitivity, sovereignty, activation, or security rules prohibit the action. |
| `ERROR` | An operational or implementation failure occurred. |

Reason codes should be stable, namespaced, and non-secret-bearing.

Proposed families:

```text
NRCS_IMPORT_*
NRCS_NETWORK_*
NRCS_DESCRIPTOR_*
NRCS_PROFILE_*
NRCS_RIGHTS_*
NRCS_SENSITIVITY_*
NRCS_SOVEREIGNTY_*
NRCS_RESOURCE_*
NRCS_PARSE_*
NRCS_SCHEMA_*
NRCS_LINEAGE_*
NRCS_TIME_*
NRCS_CORRECTION_*
NRCS_OUTPUT_*
```

Tests should assert outcome and reason code separately from human-readable messages.

[Back to top](#top)

---

<a id="product-specific-test-matrices"></a>

## Product-specific test matrices

### SDA

SDA tests must prove:

- free-form user-, UI-, notebook-, agent-, or model-generated live SQL is denied;
- only accepted, versioned, read-only query profiles may reach transport;
- typed parameters cannot alter query syntax;
- mutation, DDL, multi-statement, comment, and unsupported expression paths fail closed;
- query text, parameter identity, request identity, response identity, and result identity remain distinct;
- expected columns, types, keys, row ordering, row/byte/cell limits, nulls, sentinels, and cardinality are checked;
- successful query execution does not imply complete SSURGO coverage or soil truth;
- sensitive query text and parameters are minimized in logs and reports.

Minimum negative cases:

```text
unapproved query profile
free-form SQL
mutation or DDL
unbounded result request
unexpected table or column
duplicate or missing key
cardinality explosion
ordering drift
unknown null/sentinel
response truncation
rights or activation unresolved
```

### SCAN

SCAN tests must prove:

- source, network, station, sensor, variable, time, units, quality, cadence, and depth remain distinct;
- no station observation becomes area, watershed, grid, forecast, alert, compliance, or management truth;
- sensor depths are not substituted or averaged silently;
- timezone and timestamp ambiguity routes to abstain or quarantine;
- missingness and quality flags are preserved rather than converted to measurements;
- freshness uses an accepted cadence/profile rather than a global constant;
- Tribal SCAN fixtures and outward behavior require sovereignty, rights, and sensitivity review;
- watcher candidates remain distinct from admitted observations.

Minimum negative cases:

```text
unknown station or network
missing timestamp or timezone
unsupported variable or unit
missing sensor depth where required
unknown quality flag
stale beyond accepted cadence
duplicate observation identity
Tribal review missing
station-to-area aggregation attempt
life-safety or management-advice misuse
```

### SSURGO

SSURGO tests must prove:

- source, collection, survey area, retrieval, package, asset, spatial, tabular, relationship, record, and correction identities remain distinct;
- archives reject traversal, unsafe links, collisions, nested-archive abuse, encryption when unsupported, and decompression bombs;
- package manifests preserve member name, media type, size, digest, and role;
- spatial members preserve CRS, geometry type, extent, layer identity, and topology findings;
- tabular members preserve encoding, field names, types, nulls, sentinels, row counts, and source-native keys;
- `MUKEY`, `COKEY`, and `CHKEY` lineage is complete and non-circular;
- map unit, component, and horizon are never collapsed;
- scale and source vintage constrain interpretation;
- a package is not parcel, current field, engineering, regulatory, hydrologic, crop, or public truth.

Minimum negative cases:

```text
archive path traversal
duplicate member collision
oversized or deeply nested archive
missing package member digest
unknown spatial CRS
invalid or repaired-without-receipt geometry
missing relationship table
orphan COKEY or CHKEY
duplicate source-native key
encoding or sentinel drift
mixed survey vintage without profile
silent package supersession
```

### gSSURGO

gSSURGO tests must prove:

- product/package/grid/band/attribute identity remains distinct from SSURGO vector/package identity;
- native CRS, transform, resolution, extent, nodata, band identity, and dtype are preserved;
- rasterization lineage and source-survey vintage remain visible;
- `MUKEY` joins do not imply vector geometry equivalence;
- no resampling, reprojection, nodata fill, or attribute rollup occurs without an explicit transform profile and receipt candidate;
- source authority role and gridded support type remain separate;
- grid cells are not field observations.

Minimum negative cases:

```text
unknown product or package identity
missing CRS or transform
resolution drift
nodata collision
band-name or dtype drift
unrecorded reprojection or resampling
missing source-survey vintage
ambiguous MUKEY join
vector/raster lineage collapse
field-verification claim
```

### gNATSGO

gNATSGO tests must prove:

- accepted upstream product identity is required;
- product/package/grid/band/attribute/generalization/fill lineage is preserved;
- native CRS, transform, resolution, nodata, and product-native join fields are explicit;
- generalized or modeled support is not silently upgraded to detailed SSURGO authority;
- gNATSGO and gSSURGO remain distinct products;
- unknown fill/generalization lineage routes to abstain or quarantine;
- national grid cells are not field observations or parcel truth.

Minimum negative cases:

```text
unresolved product naming
missing SourceDescriptor
unknown package or band profile
resolution or CRS drift
unknown fill source
generalization lineage missing
unsupported join field
gSSURGO/gNATSGO identity collapse
detailed-local-authority overclaim
field-verification claim
```

[Back to top](#top)

---

<a id="cross-product-anti-collapse-tests"></a>

## Cross-product anti-collapse tests

The suite should include explicit cross-product denial tests.

| Attempted collapse | Required test result |
|---|---|
| SDA response equals complete SSURGO package | Deny or quarantine unless a reviewed equivalence profile exists. |
| SSURGO vector package equals gSSURGO raster | Reject identity equivalence; preserve derivative lineage. |
| gSSURGO equals gNATSGO | Reject product identity collapse. |
| SCAN station equals county/watershed/grid condition | Deny area-truth promotion. |
| Source authority role equals support type | Reject field aliasing or silent conversion. |
| Fixture success equals source activation | Deny activation inference. |
| Parser success equals EvidenceBundle closure | Deny evidence inference. |
| CI green equals release approval | Deny release inference. |
| Test-generated data equals public-safe data | Deny publication inference. |
| Static survey equals current field condition | Abstain or deny unsupported temporal claim. |

[Back to top](#top)

---

<a id="build-install-and-import-tests"></a>

## Build, install, and import tests

Once package metadata is accepted, tests should prove behavior in more than an editable repository checkout.

Required future checks:

1. build the wheel and source distribution;
2. inspect included files;
3. install into a clean environment;
4. import the accepted namespace;
5. confirm no network, secret reads, filesystem writes, logging setup, or lifecycle access at import;
6. confirm only documented public exports exist;
7. confirm product adapters are registered explicitly;
8. run fixture tests against the installed artifact;
9. verify no test or fixture files leak into the runtime wheel unless intentionally packaged;
10. uninstall cleanly.

The package-level `pyproject.toml` currently does not establish a build backend, Python range, dependencies, discovery, or test extras. These checks remain blocked.

### Import collision

The accepted import name must be tested against the clean environment. Repository-root `pythonpath` can mask missing package discovery or import collisions and must not be the sole proof of installability.

[Back to top](#top)

---

<a id="resource-and-adversarial-tests"></a>

## Resource and adversarial tests

Tests should enforce accepted resource profiles for:

- request timeout;
- retry count and backoff;
- redirect count and host changes;
- response bytes;
- rows, columns, cells, and pages;
- archive members;
- nested depth;
- expanded bytes and compression ratio;
- raster dimensions, cells, bands, and memory estimate;
- geometry feature count and coordinate count;
- temporary disk use;
- parser recursion;
- log volume;
- test duration.

### Parser hardening

Seeded adversarial tests should include:

- truncated payloads;
- invalid encodings;
- duplicate keys;
- deeply nested objects;
- extreme numbers;
- NaN/infinity where prohibited;
- malformed CSV quoting;
- conflicting null and sentinel values;
- archive header inconsistencies;
- path normalization edge cases;
- invalid geometry;
- corrupt rasters;
- schema-version mismatch;
- unknown enum values.

Resource failures should return finite, sanitized outcomes rather than crash dumps containing payloads or secrets.

[Back to top](#top)

---

<a id="live-integration-test-policy"></a>

## Live integration test policy

Live external tests are denied by default.

A future `live_probe` test may run only when all of the following are true:

- an active source descriptor explicitly permits the probe;
- an accepted endpoint/acquisition profile exists;
- rights and attribution are resolved;
- the operation is read-only and non-mutating;
- credentials are not required, or approved secret handling is configured outside the repository;
- the test is rate-limited, bounded, and separately scheduled;
- the test does not expose source payloads or sensitive details in logs;
- failure does not block deterministic pull-request validation unless governance explicitly adopts that policy;
- probe results are treated as operational observations, not source truth or fixture updates;
- any snapshot promotion follows fixture review and immutable digesting.

Live tests must never auto-refresh golden files or committed fixtures.

[Back to top](#top)

---

<a id="ci-admission-and-reporting"></a>

## CI admission and reporting

### Current posture

The generic connector workflow currently executes placeholder echo commands. It does not collect or run this test lane.

A substantive NRCS test gate should not be declared until it proves:

- clean environment setup;
- package build or an explicitly documented source-mode test;
- deterministic no-network collection;
- strict markers and configuration;
- product-specific negative tests;
- filesystem-write denial;
- secret/log scanning;
- bounded resource tests;
- machine-readable reports;
- failure on zero collected tests when tests are expected.

### Proposed CI stages

```text
1. lint/test metadata
2. build package
3. install clean artifact
4. import safety
5. unit + contract + fixture tests
6. product negative matrices
7. security + resource tests
8. deterministic property/fuzz subset
9. report and artifact validation
10. optional separately governed live probes
```

### Required reports

Future CI should retain:

- test result report;
- collected-test count;
- package/build identity;
- Python and dependency lock identity;
- marker selection;
- fixture manifest summary;
- random seeds;
- duration and resource summary;
- coverage report if coverage policy is accepted;
- failed finite outcomes and reason codes;
- explicit statement that live probes were included or excluded.

A report is evidence of test execution. It is not a release manifest or EvidenceBundle.

[Back to top](#top)

---

<a id="proposed-future-tree"></a>

## Proposed future tree

This tree is **PROPOSED**, not current repository state.

```text
connectors/nrcs/tests/
├── README.md
├── conftest.py
├── helpers/
│   ├── network_guard.py
│   ├── filesystem_guard.py
│   ├── clock.py
│   ├── fixture_manifest.py
│   └── assertions.py
├── fixtures/
│   ├── README.md
│   ├── sda/
│   ├── scan/
│   ├── ssurgo/
│   ├── gssurgo/
│   └── gnatsgo/
├── test_import_safety.py
├── test_build_install.py
├── test_descriptor_gates.py
├── test_rights_sensitivity.py
├── test_finite_outcomes.py
├── test_lifecycle_write_denial.py
├── test_sda_query_profiles.py
├── test_scan_observations.py
├── test_ssurgo_packages.py
├── test_gssurgo_grids.py
├── test_gnatsgo_grids.py
├── test_cross_product_collapse.py
└── test_resource_security.py
```

Before adding any path:

- confirm ownership;
- verify Directory Rules placement;
- identify the accepted package API or profile under test;
- decide fixture authority and manifest shape;
- add deterministic negative cases;
- wire substantive CI;
- document rollback.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Stage 0 — preserve current honesty

- keep the lane documentation-only;
- do not claim tests, fixtures, collection, or CI;
- keep source activation and live network denied.

### Stage 1 — test harness guards

Add reviewed test-only guards for:

- network denial;
- temporary filesystem enforcement;
- clock and randomness control;
- secret and log sanitization;
- strict marker registration.

### Stage 2 — package import proof

After package metadata is accepted:

- build and install cleanly;
- test import safety;
- test documented exports;
- test absence of production dependency on tests.

### Stage 3 — descriptor and finite-outcome tests

Implement:

- inactive/missing descriptor denial;
- unresolved rights/sensitivity/sovereignty denial;
- finite outcomes and reason codes;
- RAW/QUARANTINE handoff and direct-write denial.

### Stage 4 — one product fixture slice

Choose one product only after its implementation and profiles exist. Prefer the narrowest reviewed fixture and prove both positive and negative behavior.

Do not implement all product suites against nonexistent adapters.

### Stage 5 — cross-product and security tests

Add:

- anti-collapse matrix;
- archive, grid, parser, and resource attacks;
- correction and supersession behavior;
- deterministic property/fuzz coverage.

### Stage 6 — substantive CI

Wire clean build/install/test/report jobs. Make zero-test collection and echo-only placeholder gates fail.

### Stage 7 — optional live probes

Admit separately governed, non-mutating probes only after source activation and operational review.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This test lane is not done until:

- [ ] owners and reviewers are accepted;
- [ ] the package build, Python range, dependencies, discovery, and import namespace are accepted;
- [ ] test and fixture homes are confirmed;
- [ ] marker vocabulary is registered;
- [ ] network denial is enforced at a low-level boundary;
- [ ] filesystem, clock, randomness, environment, and process isolation are proven;
- [ ] fixtures have immutable digests and reviewed rights/sensitivity metadata;
- [ ] source descriptor and activation gates fail closed;
- [ ] finite outcomes and reason codes are accepted and tested;
- [ ] product-specific positive and negative matrices exist for implemented adapters only;
- [ ] SDA free-form live SQL denial is tested;
- [ ] SCAN station/depth/cadence/quality/Tribal rules are tested;
- [ ] SSURGO archive and MUKEY/COKEY/CHKEY lineage rules are tested;
- [ ] gSSURGO native-grid and derivative-lineage rules are tested;
- [ ] gNATSGO identity/generalization/fill-lineage rules are tested;
- [ ] cross-product collapse attempts are rejected;
- [ ] direct writes to governed stores are denied;
- [ ] logs and failures are safe;
- [ ] resource bounds and adversarial cases are tested;
- [ ] clean build/install/import tests pass;
- [ ] substantive CI collects a nonzero expected suite;
- [ ] reports are retained and auditable;
- [ ] correction and rollback procedures are exercised;
- [ ] no test result is represented as source activation, evidence closure, policy approval, or release approval.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| # | Question | Status |
|---:|---|---|
| 1 | Who owns the NRCS test lane? | `UNKNOWN` |
| 2 | Who approves fixtures and fixture redistribution? | `UNKNOWN` |
| 3 | Is this the final canonical fixture home? | `NEEDS VERIFICATION` |
| 4 | What build backend and package discovery will `kfm-connector-nrcs` use? | `UNKNOWN` |
| 5 | Which Python versions are supported? | `UNKNOWN` |
| 6 | Which runtime and test dependencies are accepted? | `UNKNOWN` |
| 7 | What is the accepted import namespace and public API? | `UNKNOWN` |
| 8 | How will tests prove clean-wheel behavior rather than repository-path behavior? | `NEEDS VERIFICATION` |
| 9 | What marker vocabulary and strictness are accepted? | `UNKNOWN` |
| 10 | Which network-denial mechanism is approved? | `UNKNOWN` |
| 11 | Are subprocesses allowed in default tests? | `UNKNOWN` |
| 12 | What timeout and resource profiles apply? | `UNKNOWN` |
| 13 | What fixture manifest contract and schema are accepted? | `UNKNOWN` |
| 14 | Which public snapshots may be redistributed? | `UNKNOWN` |
| 15 | How are corrected or superseded fixtures represented? | `UNKNOWN` |
| 16 | Which source descriptor IDs are canonical for each product? | `CONFLICTED / UNKNOWN` |
| 17 | How are source authority role and support type mapped? | `CONFLICTED` |
| 18 | What finite connector result contract is accepted? | `UNKNOWN` |
| 19 | What reason-code namespace is accepted? | `UNKNOWN` |
| 20 | What SDA query-profile registry is accepted? | `UNKNOWN` |
| 21 | What SCAN station, variable, unit, depth, cadence, and quality profiles are accepted? | `UNKNOWN` |
| 22 | What Tribal SCAN fixture and review rules apply? | `UNKNOWN` |
| 23 | What SSURGO package, archive, asset, spatial, tabular, and relationship profiles are accepted? | `UNKNOWN` |
| 24 | What gSSURGO product, grid, band, attribute, and survey-vintage profiles are accepted? | `UNKNOWN` |
| 25 | What gNATSGO product identity, fill, and generalization profiles are accepted? | `UNKNOWN` |
| 26 | Which schema versions are enforceable rather than permissive scaffolds? | `UNKNOWN` |
| 27 | How will test reports reference contract and fixture versions? | `NEEDS VERIFICATION` |
| 28 | Is coverage measured, and what threshold is meaningful? | `UNKNOWN` |
| 29 | Which deterministic fuzz budget is accepted? | `UNKNOWN` |
| 30 | What test duration budget applies to pull requests? | `UNKNOWN` |
| 31 | Will zero collected tests be a hard failure? | `NEEDS VERIFICATION` |
| 32 | Which workflow owns substantive NRCS tests? | `UNKNOWN` |
| 33 | Are connector tests release-blocking? | `UNKNOWN` |
| 34 | How are flaky tests detected and governed? | `UNKNOWN` |
| 35 | Are live probes permitted for any product? | `UNKNOWN` |
| 36 | Where are live-probe observations and logs retained? | `UNKNOWN` |
| 37 | How are rights or source-behavior changes invalidated across fixtures and tests? | `UNKNOWN` |
| 38 | How are test regressions linked to correction notices or incidents? | `UNKNOWN` |
| 39 | How is fixture sensitivity re-reviewed over time? | `UNKNOWN` |
| 40 | What rollback restores the last reviewed test and fixture contract? | `NEEDS VERIFICATION` |

[Back to top](#top)

---

<a id="validation-commands"></a>

## Validation commands

The following commands are proposed for maintainers after implementation. They are not current pass claims.

```bash
# Inspect current lane
find connectors/nrcs/tests -maxdepth 4 -type f -print | sort

# Collect without live probes
python -m pytest connectors/nrcs/tests \
  -m "not live_probe" \
  --collect-only \
  --strict-markers \
  --strict-config

# Run deterministic suite
python -m pytest connectors/nrcs/tests \
  -m "not live_probe" \
  --strict-markers \
  --strict-config

# Verify package metadata and clean build once configured
python -m build connectors/nrcs

# Inspect workflow commands
sed -n '1,240p' .github/workflows/connector-gate.yml
```

A useful validation receipt should record:

```text
base commit
package artifact digest
Python version
dependency lock identity
test selection
collected count
fixture manifest digests
random seeds
live probes included/excluded
pass/fail/error counts
duration/resource summary
report digests
```

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Confirmed observation | Limitation |
|---|---|---|
| This README before revision | v0.1 planning-oriented test contract. | Did not inventory exact absences or align fully with grounded product contracts. |
| NRCS package metadata | Distribution name and version `0.0.0` only. | No package-local build, dependency, discovery, or test configuration. |
| Namespace initializer | Empty. | No importable behavior or exports established. |
| Root repository metadata | Pytest is an optional test dependency; repository root is added to pytest `pythonpath`. | Can mask package-discovery/install problems and does not prove NRCS collection. |
| Exact test paths | Core safety and product tests were not found. | Bounded path checks do not rule out differently named files elsewhere. |
| Fixture path | Fixture-root README was not found. | No governed fixture inventory established. |
| SDA boundary | Free-form live SQL denied; query profiles and result identities required. | Adapter, profiles, fixtures, and tests absent. |
| SCAN boundary | Station, depth, cadence, quality, time, and Tribal review must be preserved. | Adapter, profiles, fixtures, and tests absent. |
| SSURGO boundary | Archive/package safety and MUKEY/COKEY/CHKEY lineage required. | Adapter, fixtures, tests, and active descriptor absent. |
| gSSURGO boundary | Native grid, resolution, CRS, nodata, bands, and derivative lineage required. | Adapter, profiles, fixtures, and tests absent. |
| gNATSGO boundary | Product identity and fill/generalization lineage unresolved and required. | Product doctrine, adapter, profiles, fixtures, and tests absent. |
| Authority register | `PROPOSED` with no entries. | No NRCS source activation can be inferred. |
| Connector workflow | Echo-only placeholder jobs. | Green status does not prove test collection or connector behavior. |
| Directory Rules | Tests remain subordinate to implementation and governing roots. | Does not choose marker, fixture, or workflow implementation details. |
| Source-admission ADR | Defines descriptor-level and record-level fail-closed admission. | ADR status remains proposed and implementation depth varies. |

[Back to top](#top)

---

<a id="maintainer-checklist"></a>

## Maintainer checklist

Before adding or changing an NRCS connector test:

- [ ] identify the implemented behavior under test;
- [ ] cite the accepted product/profile/contract/schema/policy source;
- [ ] confirm the test belongs under the NRCS connector root;
- [ ] use a governed fixture with immutable digest;
- [ ] keep network denied unless the test is an approved `live_probe`;
- [ ] isolate filesystem, clock, randomness, environment, and subprocesses;
- [ ] assert finite outcome and reason code;
- [ ] include negative and anti-collapse cases;
- [ ] ensure logs and failure output are safe;
- [ ] avoid writes to governed stores;
- [ ] avoid source activation, evidence, policy, or release claims;
- [ ] update CI collection when a test class is added;
- [ ] record correction or rollback implications;
- [ ] verify the test fails before the implementation fix when it is a regression test.

Before approving the test lane as operational:

- [ ] inspect collected test names;
- [ ] inspect fixture rights and sensitivity reviews;
- [ ] prove clean build/install/import;
- [ ] verify nonzero collection;
- [ ] inspect workflow commands rather than status color alone;
- [ ] confirm live probes are excluded from default CI;
- [ ] retain auditable reports;
- [ ] exercise a rollback or fixture supersession case.

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-migration"></a>

## Rollback, correction, deprecation, and migration

### Documentation-only rollback

Before merge, close or abandon the review branch.

After merge, restore the prior blob for this README through a transparent revert:

```text
7c65ba6ef85a8369e17c40d5e3fbc388b04a306b
```

No runtime, fixture, source, lifecycle, receipt, proof, pipeline, release, deployment, or public rollback is required for this documentation-only revision.

### Future test rollback

When an executable test change is unsafe:

1. stop relying on the affected green result;
2. preserve the failing report, seed, fixture digest, package digest, and environment identity;
3. classify whether the defect is in implementation, test expectation, fixture, profile, contract, schema, or policy;
4. quarantine affected fixtures or reports when rights or sensitivity are implicated;
5. restore the last reviewed test/fixture version through a transparent revert;
6. rerun the deterministic suite;
7. record any product, lifecycle, evidence, policy, or release artifacts whose confidence depended on the invalid test;
8. issue correction, withdrawal, or supersession records in the owning roots where necessary.

### Fixture correction

Never overwrite a reviewed fixture silently. Create a new version, preserve the prior digest, record the reason, and identify all tests and reports affected.

### Deprecation and migration

Moving tests or fixtures requires:

- Directory Rules review;
- old/new path mapping;
- collection and workflow updates;
- fixture digest continuity;
- ownership and CODEOWNERS review where applicable;
- a compatibility period or explicit break;
- rollback instructions;
- proof that no duplicate suite is running with divergent expectations.

[Back to top](#top)

---

## Status summary

`connectors/nrcs/tests/` is a repository-present but implementation-empty test boundary. It may eventually prove deterministic connector behavior against governed profiles and fixtures. It is not source authority, product truth, policy authority, evidence closure, release approval, publication evidence, or proof that the NRCS connector package currently works.

<p align="right"><a href="#top">Back to top</a></p>
