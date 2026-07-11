<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-epa-tests-readme
title: connectors/epa/tests/ — EPA Connector Test Lane
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-07-11
policy_label: public
related:
  - ../README.md
  - ../src/README.md
  - ../src/epa/README.md
  - ../../../tests/README.md
  - ../../../fixtures/README.md
  - ../../../data/registry/sources/
  - ../../../docs/sources/catalog/epa/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/
  - ../../../release/
tags: [kfm, connectors, epa, tests, source-admission, no-network, validation, quarantine]
notes:
  - "This README documents a connector-local test lane, not a canonical test authority or proof of implemented tests."
  - "At the inspected base commit, connectors/epa/tests/ contains only README.md."
  - "The adjacent EPA package contains documentation plus placeholder fetch.py, admit.py, and descriptor.yaml files; runtime behavior and CI wiring remain UNKNOWN."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EPA Connector Test Lane

> Connector-local test boundary for EPA fetch and admission behavior under `connectors/epa/`.

> [!IMPORTANT]
> **Document lifecycle:** draft  
> **Component maturity:** experimental documentation scaffold  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** the path and current one-file inventory are confirmed at base commit `7fb1a6b`; test implementation, runnable commands, CI wiring, endpoint behavior, and emitted artifacts remain unverified.

`connectors/epa/tests/`

## Quick navigation

- [Scope](#scope)
- [Repository fit](#repository-fit)
- [Confirmed current state](#confirmed-current-state)
- [What these tests may prove](#what-these-tests-may-prove)
- [What these tests must not prove](#what-these-tests-must-not-prove)
- [Proposed test classes](#proposed-test-classes)
- [Fixture and mock-data rules](#fixture-and-mock-data-rules)
- [No-network default](#no-network-default)
- [Proposed local layout](#proposed-local-layout)
- [Running tests](#running-tests)
- [Failure handling](#failure-handling)
- [Definition of done](#definition-of-done)
- [Verification backlog](#verification-backlog)
- [Rollback](#rollback)

---

## Scope

`connectors/epa/tests/` is reserved for tests that exercise EPA connector behavior at the source-admission edge.

This lane may eventually verify that EPA-specific helpers:

- accept explicit configuration and source references;
- avoid network access by default;
- parse supplied fixture payloads deterministically;
- preserve source identity, retrieval metadata, timestamps, and digests;
- produce bounded RAW or QUARANTINE admission candidates;
- fail closed on malformed, incomplete, rights-unclear, sensitive, stale, or drifted input;
- return finite, reviewable failure outcomes;
- avoid writing to processed, catalog, triplet, published, proof, receipt, or release stores.

This lane is not a second canonical `tests/` root. Cross-connector, contract, schema, policy, release, integration, end-to-end, and publication tests belong in the repository-wide testing structure.

---

## Repository fit

Directory Rules place source-specific fetchers and admitters under `connectors/`. Connector-local tests may live beside that implementation when they remain narrow and do not create parallel test authority.

```text
connectors/
└── epa/
    ├── README.md
    ├── src/
    │   ├── README.md
    │   └── epa/
    │       ├── README.md
    │       ├── fetch.py          # confirmed greenfield placeholder
    │       ├── admit.py          # confirmed greenfield placeholder
    │       └── descriptor.yaml   # confirmed placeholder; role and rights unresolved
    └── tests/
        └── README.md             # this file; current confirmed inventory
```

Related responsibility homes:

```text
tests/                              # repository-wide test authority
fixtures/                           # shared and governed fixtures
data/registry/sources/              # canonical source descriptors and activation state
schemas/contracts/v1/source/        # source/admission machine shapes
policy/                             # rights, sensitivity, and admissibility policy
release/                            # release, correction, withdrawal, and rollback decisions
docs/sources/catalog/epa/           # EPA source-family documentation
```

> [!CAUTION]
> Connector-local tests must not silently duplicate canonical fixtures, schemas, policy decisions, release gates, or end-to-end acceptance tests.

---

## Confirmed current state

At base commit `7fb1a6b72d4cc36e7a3a9e15629cdf96aab01966`:

| Item | Status | Evidence boundary |
|---|---:|---|
| `connectors/epa/tests/README.md` | **CONFIRMED** | The file exists. |
| Additional files under `connectors/epa/tests/` | **UNKNOWN / not observed** | Repository code search returned no test modules for this lane. Absence is bounded to the inspected search and ref. |
| `connectors/epa/src/epa/fetch.py` | **CONFIRMED scaffold** | One-line greenfield placeholder; no fetch behavior is proven. |
| `connectors/epa/src/epa/admit.py` | **CONFIRMED scaffold** | One-line greenfield placeholder; no admission behavior is proven. |
| `connectors/epa/src/epa/descriptor.yaml` | **CONFIRMED scaffold** | Placeholder descriptor with unresolved `role` and `rights`. |
| Runnable EPA connector tests | **UNKNOWN** | No executable test modules or results were verified. |
| CI integration | **UNKNOWN** | No workflow run, job, check, or status proves this lane is executed. |
| Live EPA endpoint configuration | **NEEDS VERIFICATION** | Must be grounded in canonical descriptors and source-steward review. |

The existence of this README does not prove the connector is implemented, activated, rights-cleared, or production-ready.

---

## What these tests may prove

Connector-local tests may prove only bounded behavior that they directly exercise.

They may verify:

- imports do not trigger network access;
- placeholder modules remain inert until implementation is added;
- configuration parsing rejects missing or unsafe values;
- live behavior requires an explicit source descriptor and opt-in flag;
- mocked responses map to explicit connector outcomes;
- request fingerprints, retrieval timestamps, source identifiers, and digests are preserved where the contract requires them;
- malformed or changed payloads route to `QUARANTINE`, `ABSTAIN`, `DENY`, or `ERROR` rather than silent success;
- connector outputs are limited to RAW or QUARANTINE handoff;
- retries, timeouts, rate-limit handling, and pagination are bounded;
- logs and exceptions do not expose credentials or excessive source payloads.

A passing test proves only the behavior that test exercises at the inspected commit.

---

## What these tests must not prove

These tests must not claim that:

- EPA-derived facts are true;
- a source is authoritative merely because a fetch succeeded;
- rights, terms, or sensitivity are cleared;
- a source descriptor is activated;
- processed domain records are valid;
- EvidenceBundle closure exists;
- catalog, triplet, proof, receipt, or release closure exists;
- data is publishable;
- a map, dashboard, export, or AI answer is trustworthy;
- CI coverage is complete because one connector-local suite passes.

Truth support and publication readiness require downstream evidence, schema validation, policy, review, catalog closure, release state, correction, and rollback support.

---

## Proposed test classes

The following classes are **PROPOSED** until executable files are added and verified.

### Configuration and activation tests

Verify that:

- source identity and activation state are explicit;
- unresolved `role` or `rights` blocks live behavior;
- imports do not read secrets or contact endpoints;
- unsafe defaults fail closed;
- source-specific configuration does not become a duplicate SourceDescriptor.

### No-network unit tests

Verify that:

- default test execution performs no external HTTP requests;
- all HTTP clients are mocked or blocked;
- fixture parsing works without credentials;
- network attempts fail with a clear, bounded outcome.

### Fetch behavior tests

When fetch behavior exists, verify:

- requests use bounded timeouts and explicit parameters;
- pagination and retries are finite;
- rate-limit, forbidden, timeout, not-found, and server-error cases are handled explicitly;
- ambiguous or partial responses do not become admitted success;
- request metadata is safe to log.

### Admission tests

When admission behavior exists, verify:

- only RAW or QUARANTINE candidates are emitted;
- unresolved rights, sensitivity, source role, or schema drift routes to quarantine or denial;
- no code writes directly to later lifecycle stores;
- admission outcomes preserve source references and review context.

### Descriptor-boundary tests

Verify that connector-local descriptor material:

- is not treated as canonical authority unless repository governance explicitly says so;
- does not override `data/registry/sources/`;
- exposes unresolved fields as blockers rather than silently filling them;
- remains compatible with accepted source/admission schemas.

### Error and drift tests

Verify handling for:

- empty payloads;
- malformed payloads;
- added, removed, or renamed fields;
- changed units or timestamp formats;
- unexpected geometry or identifier changes;
- oversized payloads;
- stale or revised source products;
- repeated failures that should emit a reviewable drift signal.

### Optional live smoke tests

Live checks, if ever added, must be:

- opt-in;
- isolated from default CI;
- source-steward approved;
- bounded in request count and response retention;
- prevented from writing publication artifacts;
- recorded as reachability or shape checks, not truth validation.

---

## Fixture and mock-data rules

Use the smallest fixture that proves the intended behavior.

Fixture rules:

1. Prefer synthetic fixtures that preserve required structure without copying unnecessary source volume.
2. Label every fixture as synthetic, minimized, redacted, or source-derived.
3. Preserve provenance and rights notes for any source-derived fixture.
4. Include successful, empty, malformed, forbidden, rate-limited, timeout, and drifted cases where applicable.
5. Keep shared fixtures in the repository fixture authority rather than duplicating them across connectors.
6. Do not include credentials, private URLs, personal data, sensitive locations, or unrestricted raw dumps.
7. Do not auto-refresh committed fixtures from live endpoints.
8. Record the connector or schema version a fixture is intended to exercise.

Illustrative fixture metadata:

```yaml
fixture_id: epa-synthetic-valid-001
fixture_status: synthetic
source_family: epa
supports_tests:
  - no_network_parse
  - raw_admission_candidate
rights_posture: non_authoritative_test_fixture
sensitivity_posture: public_safe_synthetic
review_state: draft
```

This example is not a machine contract.

---

## No-network default

> [!CAUTION]
> Default EPA connector tests must pass without internet access and without credentials.

Required posture:

- no live calls during import or test collection;
- no endpoint access unless an explicit, reviewed opt-in is present;
- no hidden fixture refresh;
- no retry loops that create unexpected endpoint pressure;
- no secrets in test files, snapshots, logs, or failure messages;
- no writes to `data/processed/`, `data/catalog/`, `data/published/`, `release/`, or other governed stores.

A possible future environment flag may be used for isolated smoke tests, but its exact name is **NEEDS VERIFICATION** against repository convention.

---

## Proposed local layout

No executable test layout is currently confirmed. A future narrow layout might be:

```text
connectors/epa/tests/
├── README.md
├── test_import_safety.py
├── test_configuration.py
├── test_fetch_failures.py
├── test_admission_boundary.py
├── test_descriptor_boundary.py
├── test_no_network_default.py
└── fixtures/
    ├── README.md
    ├── valid.json
    ├── empty.json
    ├── malformed.json
    └── drifted.json
```

Before creating local fixtures, verify whether the repository requires them under root `fixtures/` or another established compatibility home.

---

## Running tests

No command is confirmed runnable for this lane because no executable test modules were observed.

A likely future command is:

```bash
python -m pytest connectors/epa/tests
```

This remains **PROPOSED** until the repository’s package manager, Python path, test configuration, dependencies, and CI workflow are verified.

Prefer the repository-native command when one exists. Do not add an invented command merely to make this README appear complete.

---

## Failure handling

| Condition | Expected test result |
|---|---|
| Test requires live network during default execution | **FAIL** |
| Test requires committed credentials | **FAIL** |
| Missing or unresolved source descriptor | **DENY** live activation or **ABSTAIN** from the live test |
| Malformed fixture | Explicit expected parser or quarantine outcome |
| Source-shape drift | **FAIL** or emit a reviewable drift result; never auto-accept |
| Rights or sensitivity unresolved | Quarantine-safe or denied outcome |
| Connector writes to later lifecycle stores | **FAIL** |
| Expected code remains a placeholder | Skip or xfail only with an explicit reason; do not report implemented behavior |
| Required dependency or runner unavailable | **NOT RUN** or **ERROR**, not PASS |

Tests should fail loudly and safely. They must not convert uncertainty into success.

---

## Definition of done

This test lane is ready for implementation review when:

- [ ] Actual test modules exist and are listed in this README.
- [ ] Default execution performs no network I/O.
- [ ] Imports do not require secrets or endpoint access.
- [ ] Tests exercise the implemented EPA modules rather than hypothetical names.
- [ ] Placeholder behavior is clearly separated from implemented behavior.
- [ ] RAW and QUARANTINE output boundaries are tested.
- [ ] Later lifecycle stores cannot be written by connector-local tests.
- [ ] Source role, rights, sensitivity, and activation blockers fail closed.
- [ ] Fixtures are minimal, attributed, and stored in the correct authority home.
- [ ] Error, timeout, forbidden, rate-limit, empty, malformed, and drift cases are covered where relevant.
- [ ] The exact repository-native command is documented and verified.
- [ ] CI wiring is confirmed by workflow or check evidence.
- [ ] No secrets, private URLs, sensitive data, or excessive source payloads are committed.

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Confirm actual files below `connectors/epa/tests/`. | **CONFIRMED only for README** | Complete tree listing at the current ref. |
| Confirm whether executable EPA tests exist elsewhere. | **NEEDS VERIFICATION** | Repository search, test collection, and CI configuration. |
| Confirm Python package and import wiring for `connectors/epa/src/epa/`. | **NEEDS VERIFICATION** | Package metadata, workspace configuration, and import tests. |
| Replace placeholder fetch and admit modules with implemented behavior before testing claims are upgraded. | **PROPOSED** | Reviewed code and tests. |
| Resolve canonical ownership of `descriptor.yaml`. | **NEEDS VERIFICATION** | Directory Rules, source registry, schemas, and accepted ADRs. |
| Resolve `role: TBD` and `rights: TBD` before live activation. | **NEEDS VERIFICATION** | Source-steward and policy review. |
| Confirm accepted connector outcome vocabulary. | **NEEDS VERIFICATION** | Contracts and schemas. |
| Confirm fixture authority and local-fixture allowance. | **NEEDS VERIFICATION** | Root fixture guidance and adjacent conventions. |
| Confirm test runner and exact command. | **NEEDS VERIFICATION** | `pyproject.toml`, pytest config, Makefile, task runner, or CI. |
| Confirm CI executes this lane. | **UNKNOWN** | Workflow definitions and successful check evidence. |
| Confirm live EPA test policy and opt-in flag. | **NEEDS VERIFICATION** | Source policy, test config, and steward approval. |

---

## Rollback

Before merge, rollback means closing the draft pull request and abandoning the scoped branch. After merge, create a transparent revert of the implementation commit and re-run the applicable documentation checks. Do not rewrite shared history.

---

## Maintainer note

Keep this lane narrow and honest. It should prove that EPA connector code behaves safely at the admission edge. It must not become a substitute for source authority, EvidenceBundle closure, domain validation, policy review, release approval, publication, or end-to-end system verification.
