<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-tests-readme
title: connectors/noaa/tests/ — NOAA Connector Test Boundary and Evidence Contract
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · NOAA steward · Hazards steward · Atmosphere steward · Climate steward · Soil steward · Validation steward · Security steward · CI steward · Docs steward
created: 2026-06-19
updated: 2026-07-15
policy_label: "public-doctrine; connector-tests; source-admission; multi-role; not-life-safety; no-network-by-default; fixture-first; descriptor-gated; rights-aware; sensitivity-aware; provenance-preserving; negative-path-first; deterministic; replayable; raw-quarantine-only; rollback-aware; no-secrets"
current_path: connectors/noaa/tests/README.md
truth_posture: CONFIRMED repository path, prior v0.1 README, merged NOAA source-root v0.2 README, merged NOAA package-boundary v0.1 README, empty package __init__.py, package project name and 0.0.0 version, absence of likely conftest.py test_import.py and test_noaa.py paths in bounded checks, absence of indexed test_noaa symbols, documentation-only live-test flag references, connector-gate TODO-only workflow, NOAA source-family catalog, connector-root contract, proposed source-admission ADR, and RAW-WORK/QUARANTINE-PROCESSED-CATALOG/TRIPLET-PUBLISHED lifecycle doctrine / PROPOSED connector-local test architecture, fixture taxonomy, marker vocabulary, package-import tests, configuration tests, transport tests, product-adapter tests, parser-preservation tests, admission-candidate tests, security tests, replay tests, live-test isolation, coverage expectations, CI wiring, and evidence artifacts / UNKNOWN complete tests-directory inventory, actual pytest configuration, package installability, executable package behavior, source descriptor IDs, active NOAA products, accepted endpoints, fixture inventory, test collection, CI enforcement, coverage, test logs, artifact retention, schedules, deployment, and runtime health / NEEDS VERIFICATION accepted owners, actual test runner, package namespace, package metadata hardening, fixture authority, source-schema home, activation states, rights and sensitivity bindings, live-test policy, network interception, validators, markers, coverage thresholds, CI gates, correction workflow, deprecation policy, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: cbc65b4bd3f7ecd7cb55cbae97da564cad5b5546
  prior_blob: eb0cf561f5596ae1d06c48dda240568fe177d185
  source_root_blob: 0422134d3d1ac6547b9536cd6e5de5e0dd93d314
  package_readme_blob: 1303a10954d16844557653e871f4c0592e87e2c1
  package_metadata_blob: 851976fa7a808ce8d5ebc93291c3ddde27a9c349
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  bounded_path_checks:
    - connectors/noaa/tests/README.md exists at v0.1 before this revision
    - connectors/noaa/tests/conftest.py was not found
    - connectors/noaa/tests/test_import.py was not found
    - connectors/noaa/tests/test_noaa.py was not found
    - bounded code search did not surface test_noaa symbols
    - KFM_ALLOW_LIVE_NOAA_TESTS was surfaced only in README documentation
    - connectors/noaa/src/noaa/__init__.py is empty
    - connectors/noaa/pyproject.toml contains only project name and version 0.0.0
    - .github/workflows/connector-gate.yml contains TODO echo steps
related:
  - ../README.md
  - ../src/README.md
  - ../src/noaa/README.md
  - ../pyproject.toml
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../docs/sources/catalog/noaa/README.md
  - ../../../docs/sources/catalog/noaa/storm-events.md
  - ../../../docs/sources/catalog/noaa/nws-api.md
  - ../../../docs/sources/catalog/noaa/hms-fire-smoke.md
  - ../../../docs/sources/catalog/noaa/hrrr-smoke.md
  - ../../../docs/sources/catalog/noaa/goes-abi-aod.md
  - ../../../docs/sources/catalog/noaa/viirs-hotspot.md
  - ../../../docs/sources/catalog/noaa/noaa-uscrn.md
  - ../../../docs/sources/catalog/noaa/station-climate-products.md
  - ../../../data/registry/sources/README.md
  - ../../../fixtures/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../contracts/
  - ../../../schemas/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
  - ../../../.github/workflows/connector-gate.yml
tags: [kfm, connectors, noaa, tests, pytest, offline, no-network, fixtures, source-admission, multi-role, ncei, nws, hms, hrrr, goes, viirs, uscrn, storm-events, hazards, atmosphere, climate, soil, raw, quarantine, provenance, import-safety, negative-paths, security, replay, governance]
notes:
  - "This revision changes only connectors/noaa/tests/README.md."
  - "The test path is CONFIRMED repository-present, but bounded inspection did not establish executable NOAA test modules, pytest configuration, fixtures, collection, coverage, or CI enforcement."
  - "The source package remains an empty shell with 0.0.0 metadata; test expectations in this README are contracts and implementation targets, not current coverage claims."
  - "The proposed KFM_ALLOW_LIVE_NOAA_TESTS flag is not accepted runtime configuration; it currently appears only in documentation."
  - "The connector-gate workflow is TODO-only; a green run cannot prove NOAA connector behavior."
  - "NOAA is a multi-role source family; tests must preserve product identity, source role, time kinds, units, quality, geometry, uncertainty, rights, sensitivity, and caveats."
  - "KFM is not an emergency alerting system."
  - "Connector tests may prove source-admission behavior and refusal paths only; they do not prove source truth, evidence closure, release readiness, or publication safety."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA Connector Test Boundary and Evidence Contract

`connectors/noaa/tests/`

> Connector-local test boundary for the NOAA source-admission family. This lane should prove import safety, no-network defaults, product-specific preservation, fail-closed admission behavior, and refusal to publish or issue alerts. It does not establish NOAA truth, activate a source, certify evidence, approve release, or make the connector production-ready.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![fixtures](https://img.shields.io/badge/fixtures-synthetic__first-orange)
![source role](https://img.shields.io/badge/source--role-multi--role-purple)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-blue)
![life safety](https://img.shields.io/badge/life__safety-NOT__ALERT__AUTHORITY-red)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-boundary) · [Directory basis](#repository-fit-and-directory-rules-basis) · [Snapshot](#confirmed-repository-snapshot) · [Test contract](#test-lane-contract) · [Taxonomy](#test-taxonomy) · [Offline](#offline-and-no-network-contract) · [Fixtures](#fixture-and-golden-sample-contract) · [Imports](#package-import-and-build-tests) · [Configuration](#configuration-tests) · [Transport](#transport-and-resource-tests) · [Products](#product-lane-anti-collapse-tests) · [Parsing](#parsing-and-preservation-tests) · [Admission](#source-admission-handoff-tests) · [Outcomes](#outcome-and-reason-code-tests) · [Provenance](#provenance-time-and-integrity-tests) · [Policy](#rights-sensitivity-and-life-safety-tests) · [Security](#security-and-data-minimization-tests) · [Replay](#isolation-determinism-and-replay-tests) · [Live tests](#live-test-isolation) · [CI](#ci-coverage-and-evidence) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-correction-deprecation-and-supersession)

> [!IMPORTANT]
> **Tests are evidence about implementation behavior, not source authority.** A passing fixture test can show that one parser preserves one field or refuses one unsafe path. It cannot prove that NOAA data are true, current, complete, authoritative for a claim, licensed for release, safe to publish, or suitable for life-safety use.

> [!CAUTION]
> **Repository presence is not test coverage.** The test README exists, but bounded inspection did not establish test modules, a `conftest.py`, pytest configuration, fixtures, coverage, CI enforcement, or retained test artifacts. The package under test remains an empty shell with `0.0.0` metadata.

---

<a id="purpose"></a>

## Purpose

This README defines what connector-local NOAA tests should prove, what they must never claim, and what evidence is required before maintainers describe the test lane as implemented.

The test lane should eventually provide inspectable proof that NOAA connector code:

- imports without network, secret, cache, clock, or filesystem side effects;
- requires explicit source activation and request configuration;
- remains no-network by default;
- preserves product-specific identity and source-role semantics;
- preserves source-native time kinds, units, quality flags, geometry, uncertainty, and version metadata;
- handles malformed, stale, incomplete, ambiguous, oversized, redirected, rate-limited, or unavailable source material with finite outcomes;
- creates only RAW or QUARANTINE admission candidates;
- does not write directly to downstream lifecycle or release stores;
- does not emit KFM-issued alerts, emergency instructions, or public truth claims;
- is deterministic and replayable from captured test payloads;
- keeps secrets and sensitive payloads out of logs, snapshots, fixtures, and assertion messages.

The test lane must not become:

- a NOAA source catalog;
- an active `SourceDescriptor` registry;
- an endpoint allowlist authority;
- a source activation decision;
- a schema or semantic-contract authority;
- a rights, sensitivity, or release decision point;
- a substitute for EvidenceBundle closure;
- an operational monitoring dashboard;
- a live NOAA availability guarantee;
- a production readiness certificate;
- a life-safety validation program;
- a publication approval.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| `connectors/noaa/tests/README.md` | **CONFIRMED v0.1 before this revision** | A draft test contract exists. |
| `connectors/noaa/tests/conftest.py` | **NOT FOUND in bounded check** | Shared pytest fixtures or network guards are not established at this path. |
| `connectors/noaa/tests/test_import.py` | **NOT FOUND in bounded check** | Import-safety coverage is not established at this path. |
| `connectors/noaa/tests/test_noaa.py` | **NOT FOUND in bounded check** | A general NOAA test module is not established at this path. |
| Indexed `test_noaa` symbols | **NOT SURFACED** | Bounded code search did not establish executable NOAA tests. |
| `KFM_ALLOW_LIVE_NOAA_TESTS` | **DOCUMENTATION-ONLY** | The proposed flag was surfaced in READMEs, not accepted configuration or code. |
| `connectors/noaa/src/README.md` | **CONFIRMED v0.2** | Defines the source-root, package, security, transport, parsing, and admission contracts that tests should eventually prove. |
| `connectors/noaa/src/noaa/README.md` | **CONFIRMED v0.1** | Defines the package boundary and records an empty package shell. |
| `connectors/noaa/src/noaa/__init__.py` | **CONFIRMED empty** | A package marker exists, but no public API or behavior is established. |
| `connectors/noaa/pyproject.toml` | **CONFIRMED placeholder** | Project name is `kfm-connector-noaa`; version is `0.0.0`; test dependencies and tooling are not declared. |
| `.github/workflows/connector-gate.yml` | **CONFIRMED TODO-only** | Current jobs echo TODO; a green workflow cannot prove connector behavior. |
| NOAA source catalog | **CONFIRMED draft doctrine** | Product families and anti-collapse rules are documented. |
| Source-admission ADR | **CONFIRMED repository-present; status proposed** | Fixture-before-live and RAW/QUARANTINE admission doctrine are documented. |
| Actual fixture inventory | **UNKNOWN** | No accepted NOAA fixture family was established in this bounded pass. |
| Test collection, execution, coverage, logs, artifacts | **UNKNOWN** | No runtime or CI evidence was established. |

### Evidence boundary

This README may confidently state that:

- the test path and README exist;
- the source-root and package-boundary READMEs exist;
- the package marker is empty;
- package metadata is `0.0.0`;
- likely local test entry points checked above were absent;
- the proposed live-test flag is documentation-only;
- the connector-gate workflow is a TODO scaffold;
- NOAA is multi-role and not a KFM alert authority.

This README must not claim:

- executable test coverage;
- pytest collection success;
- package installability;
- a working import path;
- a working client or parser;
- network isolation enforcement;
- accepted fixtures;
- source descriptor activation;
- endpoint approval;
- CI enforcement;
- coverage thresholds;
- production connector health;
- public release safety.

Those claims remain `UNKNOWN`, `PROPOSED`, or `NEEDS VERIFICATION` until code, configuration, fixtures, tests, workflow logs, or retained artifacts prove them.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority boundary

### This test lane may own

If implemented and reviewed:

- connector-local pytest modules;
- connector-local fixture builders;
- synthetic and minimized fixture payloads;
- network-blocking test helpers;
- fake clocks and deterministic time providers;
- fake transports and recorded-response readers;
- package import and side-effect tests;
- configuration validation tests;
- product adapter and parser tests;
- admission-candidate tests;
- security and resource-limit tests;
- replay and determinism tests;
- connector-local test markers;
- test-only utility functions;
- README and test-running guidance.

### This test lane does not own

| Concern | Owning boundary |
|---|---|
| NOAA source-family or product meaning | `docs/sources/catalog/noaa/` |
| Source activation and SourceDescriptor authority | `data/registry/sources/` and accepted source-governance artifacts |
| Package behavior | `connectors/noaa/src/noaa/` |
| Source-root architecture | `connectors/noaa/src/` |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/` |
| Rights and sensitivity decisions | `policy/rights/`, `policy/sensitivity/` |
| Lifecycle data | `data/raw/`, `data/quarantine/`, downstream lifecycle roots |
| Receipts and proof closure | `data/receipts/`, `data/proofs/` |
| Release decisions and rollback authority | `release/` |
| Public API, UI, map, search, or AI behavior | governed application roots after policy and release gates |
| CI workflow authority | `.github/workflows/` |
| Production monitoring | operational observability roots, not test fixtures |

Tests may reference these authorities through stable IDs, synthetic examples, adapters, or fixtures. Tests do not replace them.

[Back to top](#top)

---

<a id="repository-fit-and-directory-rules-basis"></a>

## Repository fit and Directory Rules basis

The file remains in the existing connector-family test lane:

```text
connectors/
└── noaa/
    ├── README.md
    ├── pyproject.toml
    ├── src/
    │   ├── README.md
    │   └── noaa/
    │       ├── README.md
    │       └── __init__.py
    └── tests/
        └── README.md
```

`connectors/` is the responsibility root for source-specific fetch, parse, provenance, and admission implementation. The connector-local `tests/` lane exists to prove that implementation boundary without creating new authority.

Directory and lifecycle rules applied here:

1. **Responsibility root:** test code for the NOAA connector stays with the connector package unless it becomes broadly shared.
2. **No parallel schema or policy home:** tests consume contracts, schemas, and policy results; they do not define competing authority.
3. **Lifecycle boundary:** tests may assert RAW or QUARANTINE candidate behavior but must not create persistent downstream lifecycle state.
4. **Trust membrane:** tests must prove that connector code cannot directly serve public clients or bypass governed APIs.
5. **Watcher-as-non-publisher:** network or refresh code, if later tested, may observe and admit source material but cannot publish.
6. **Promotion remains governed:** a test cannot turn connector output into PROCESSED, CATALOG, TRIPLET, or PUBLISHED authority.
7. **Reversible change:** test layout, fixtures, markers, and CI integration should be introduced in small, independently revertible changes.

No new root, schema home, policy home, source registry, release lane, or proof home is proposed by this README.

[Back to top](#top)

---

<a id="confirmed-repository-snapshot"></a>

## Confirmed repository snapshot

### Confirmed

```text
connectors/noaa/tests/README.md
connectors/noaa/src/README.md
connectors/noaa/src/noaa/README.md
connectors/noaa/src/noaa/__init__.py
connectors/noaa/pyproject.toml
.github/workflows/connector-gate.yml
```

### Checked and not found

```text
connectors/noaa/tests/conftest.py
connectors/noaa/tests/test_import.py
connectors/noaa/tests/test_noaa.py
connectors/noaa/src/noaa/client.py
```

### Not surfaced by bounded code search

```text
test_noaa*
executable uses of KFM_ALLOW_LIVE_NOAA_TESTS
```

### Unknown without stronger inventory evidence

- additional non-indexed test files;
- ignored or generated test files;
- external test suites;
- local-only fixtures;
- package installation behavior;
- pytest configuration elsewhere in the repository;
- CI matrix entries specific to NOAA;
- retained coverage reports;
- test result artifacts;
- downstream integration tests.

The snapshot is intentionally narrow. It prevents absence claims from exceeding the inspected evidence.

[Back to top](#top)

---

<a id="test-lane-contract"></a>

## Test lane contract

A NOAA connector test should be:

- **offline by default**;
- **synthetic or minimized by default**;
- **deterministic**;
- **product-specific**;
- **source-role-aware**;
- **time-kind-aware**;
- **rights- and sensitivity-aware**;
- **not-life-safety**;
- **negative-path-first**;
- **safe to run without credentials**;
- **safe to run in public CI**;
- **bounded in CPU, memory, disk, decompression, retries, and duration**;
- **explicit about what it proves and does not prove**.

Each executable test should be traceable to:

1. a package or source-root invariant;
2. a product-specific doctrine or anti-collapse rule;
3. a synthetic or approved fixture;
4. an expected package-local outcome;
5. an explicit assertion about side effects;
6. a correction or rollback path when the contract changes.

A passing test proves only its assertion over its supplied fixture and configuration.

[Back to top](#top)

---

<a id="test-taxonomy"></a>

## Test taxonomy

| Test family | Minimum purpose | Current status |
|---|---|---:|
| Import safety | Prove imports do not access network, secrets, clocks, caches, or files unexpectedly. | **PROPOSED** |
| Package metadata | Prove package discovery, build backend, dependencies, and wheel contents once metadata exists. | **PROPOSED** |
| Configuration | Prove no-network, descriptor-gated, bounded defaults. | **PROPOSED** |
| Transport | Prove endpoint allowlists, timeouts, redirects, retries, rate limits, payload limits, and cancellation. | **PROPOSED** |
| Product dispatch | Prove explicit product selection and unknown-product refusal. | **PROPOSED** |
| Parser preservation | Prove native identifiers, fields, units, geometry, quality, uncertainty, and versions survive parsing. | **PROPOSED** |
| Time semantics | Prove observation, issue, valid, expiry, retrieval, file-vintage, and correction times stay distinct. | **PROPOSED** |
| Source-role anti-collapse | Prove NOAA products cannot inherit one family-wide role. | **PROPOSED** |
| Admission candidate | Prove only RAW or QUARANTINE candidates are produced. | **PROPOSED** |
| Rights and sensitivity | Prove unknown or restricted posture fails closed. | **PROPOSED** |
| Not-life-safety | Prove connector outputs cannot become KFM alerts or instructions. | **PROPOSED** |
| Security | Prove SSRF, archive, payload, logging, deserialization, and secret controls. | **PROPOSED** |
| Replay and determinism | Prove identical captured inputs and config yield equivalent outputs. | **PROPOSED** |
| Contract drift | Prove changed fields or formats produce explicit drift outcomes. | **PROPOSED** |
| Live smoke isolation | Prove any live tests are separately approved, skipped by default, and non-authoritative. | **PROPOSED** |
| CI evidence | Prove tests are actually collected and enforced. | **NOT ESTABLISHED** |

[Back to top](#top)

---

<a id="offline-and-no-network-contract"></a>

## Offline and no-network contract

Default test execution must not require:

- DNS resolution;
- external HTTP or FTP access;
- cloud object storage;
- live NOAA APIs or file servers;
- API keys, tokens, cookies, accounts, or sessions;
- mutable external clocks;
- private fixture stores;
- source-side writes;
- public internet access.

Offline enforcement should be active rather than aspirational.

Proposed enforcement options, pending repository convention:

- monkeypatch socket creation and common HTTP clients;
- inject a transport interface and use a fake transport;
- fail when unapproved URL schemes or hosts are requested;
- set a test-only environment marker proving live access is disabled;
- run a dedicated no-network test job in a network-restricted environment;
- verify import does not initialize a client or resolve endpoints;
- verify retries cannot hide accidental network calls.

The exact mechanism is `NEEDS VERIFICATION`. A README statement alone is not a network guard.

### Required negative assertions

- an unconfigured transport cannot access the network;
- a parser test never constructs a live transport;
- import does not read live endpoint configuration;
- missing network permission yields a finite local outcome;
- test failures do not fall back to live data;
- snapshots do not contain live response payloads unless explicitly approved and minimized.

[Back to top](#top)

---

<a id="fixture-and-golden-sample-contract"></a>

## Fixture and golden-sample contract

### Fixture classes

| Fixture class | Intended use | Default posture |
|---|---|---|
| `synthetic` | Hand-authored minimal source-shaped payload. | Preferred |
| `generated` | Deterministically generated edge-case payload. | Preferred |
| `minimized` | Small subset derived from an approved source payload. | Review required |
| `redacted` | Sensitive or operational fields removed or generalized. | Review required |
| `recorded-public` | Captured public response retained for replay. | Rights, minimization, and freshness review required |
| `malformed` | Deliberately invalid payload. | Preferred for negative tests |
| `drifted` | Deliberately changed schema/version payload. | Preferred for drift tests |
| `oversized-simulated` | Metadata or stream simulating resource limits without bulk data. | Preferred |
| `live` | Not a committed fixture; produced during an approved live smoke test. | Isolated and ephemeral |

### Required fixture metadata

Every nontrivial fixture should identify:

- fixture ID;
- fixture status;
- NOAA product lane;
- source-role candidate;
- source format and version;
- creation or capture method;
- minimization or redaction method;
- rights posture;
- sensitivity posture;
- intended test IDs;
- expected parser version or compatibility profile;
- expected outcome;
- content digest;
- reviewer and review state where required;
- whether network access is required;
- expiration or re-review date when freshness matters.

### Fixture prohibitions

Do not commit:

- credentials, API keys, bearer tokens, cookies, private URLs, or signed query strings;
- private or restricted source exports;
- bulk NOAA archives merely to make tests convenient;
- precise sensitive infrastructure or private-person details without policy review;
- unredacted request headers;
- local absolute paths;
- timestamps or random values that make fixtures nondeterministic without need;
- source content whose rights posture is unresolved;
- live warning text represented as KFM guidance.

### Golden files

Golden files should be used sparingly. A golden output is safe only when:

- the output schema is intentional;
- ordering and canonicalization are stable;
- volatile fields are normalized explicitly;
- diffs remain reviewable;
- sensitive fields are absent;
- the golden file does not become a parallel contract authority.

[Back to top](#top)

---

<a id="package-import-and-build-tests"></a>

## Package import and build tests

The package metadata is currently a `0.0.0` placeholder, so build and install tests remain implementation targets.

### Import-safety assertions

A future import test should prove that importing the package:

- performs no network I/O;
- reads no credentials or secret files;
- writes no files;
- creates no lifecycle directories;
- starts no background thread, timer, scheduler, or watcher;
- does not configure global logging;
- does not mutate environment variables;
- does not resolve live endpoints;
- does not create a transport client;
- does not emit public claims or warnings;
- exposes only the reviewed public import surface.

### Packaging assertions

Once package metadata is implemented, tests should verify:

- an explicit build backend;
- source-tree package discovery;
- intended Python compatibility;
- declared runtime and test dependencies;
- reproducible wheel and source distribution contents;
- no fixture, secret, cache, local path, raw payload, or generated artifact leaks into distributions;
- namespace collision risk is reviewed;
- editable and non-editable installs behave consistently;
- package version and compatibility policy are explicit;
- import works from an installed artifact, not only the repository root.

### Namespace risk

The import name `noaa` is short and potentially collision-prone. Before treating it as accepted:

- check dependency and environment collisions;
- test clean virtual-environment imports;
- verify distribution name versus import namespace;
- document any compatibility alias;
- prefer an ADR or migration note for a breaking namespace change.

[Back to top](#top)

---

<a id="configuration-tests"></a>

## Configuration tests

Configuration tests should prove that:

- defaults disable live network access;
- product lane is explicit;
- endpoint or distribution identity is explicit;
- source descriptor reference is required before live activation;
- request timeout is finite;
- retry count is finite;
- backoff is bounded;
- maximum response size is bounded;
- maximum decompressed size is bounded;
- redirect behavior is explicit;
- allowed URL schemes and hosts are explicit;
- user-agent and attribution requirements are preserved where applicable;
- test mode cannot silently become live mode;
- unknown configuration keys fail or warn according to a documented compatibility policy;
- secrets are referenced externally and never serialized into logs or fixtures;
- configuration objects can be hashed or compared deterministically where practical.

### Invalid configuration cases

At minimum:

- missing product lane;
- unknown product lane;
- missing descriptor reference for live mode;
- invalid timeout;
- negative retry count;
- unsupported URL scheme;
- host outside allowlist;
- live enabled without steward-approved profile;
- conflicting product and endpoint;
- output target outside RAW or QUARANTINE candidate semantics;
- logging configured to include secrets;
- payload limit absent or unbounded.

[Back to top](#top)

---

<a id="transport-and-resource-tests"></a>

## Transport and resource tests

Transport tests should use fake or recorded transports by default.

### Required behaviors

- finite connect and read timeouts;
- finite retries;
- rate-limit response handling;
- cancellation propagation;
- bounded redirect following;
- content-length and streamed-size enforcement;
- decompression-size enforcement;
- content-type validation;
- checksum or digest capture;
- ETag and Last-Modified preservation when present;
- partial-response handling;
- empty-response handling;
- server-error and client-error classification;
- request metadata redaction;
- deterministic request canonicalization.

### Required security cases

- loopback and link-local target rejection unless explicitly test-authorized;
- private-network SSRF prevention;
- DNS rebinding-resistant host validation where applicable;
- credential leakage prevention across redirects;
- archive path traversal prevention;
- zip/tar symlink handling;
- decompression bomb limits;
- content-type confusion;
- unsafe pickle or object deserialization refusal;
- malformed Unicode and log-injection handling;
- excessive nesting or record-count limits;
- temporary-file cleanup;
- no unbounded retry loop.

### Resource budget assertions

Each test should bound:

- wall-clock duration;
- memory use where practical;
- disk use;
- payload size;
- decompressed size;
- record count;
- retry count;
- redirect count;
- concurrency.

[Back to top](#top)

---

<a id="product-lane-anti-collapse-tests"></a>

## Product-lane anti-collapse tests

NOAA is not one epistemic role. Tests must reject family-wide role collapse.

| Product lane | Positive preservation tests | Required negative tests |
|---|---|---|
| Storm Events | Event and episode IDs, table type, file vintage, event type, narrative, magnitude, damage, casualty fields, geometry, correction markers. | Do not treat as a current alert, direct sensor measurement, flood extent, disaster declaration, or complete event truth. |
| NWS API | Product type, office, issue time, effective/valid/expiry times, geometry, status, message identifiers, update/cancel semantics. | Do not issue KFM warnings, instructions, evacuation advice, or life-safety determinations. |
| HMS Fire and Smoke | Fire detections and smoke polygons remain separate; qualitative density and analysis time preserved. | Do not convert smoke density to concentration, PM2.5, exposure, health risk, or ground-fire authority. |
| HRRR-Smoke | Model run, initialization, forecast hour, valid time, grid/version, variable, units, modeled role. | Do not present forecast fields as observed truth or omit run/valid time. |
| GOES ABI AOD | Platform, instrument, product/version, retrieval time, quality flags, geometry, AOD units/meaning. | Do not convert AOD directly to PM2.5 or regulatory air-quality truth. |
| VIIRS Hotspot | Platform, instrument, acquisition time, confidence/quality, detection geometry, uncertainty. | Do not assert a confirmed ground fire, perimeter, cause, or impact. |
| USCRN | Station ID, observation time, variable, units, quality flags, cadence, soil depth, raw/derived state, file vintage. | Do not treat station values as area truth or collapse depths, cadences, or derived/raw fields. |
| Station climate products | Station/product identity, observation versus normal/aggregate role, period, baseline, units, revision. | Do not collapse observations, normals, anomalies, reanalysis, forecasts, and aggregates. |

### Cross-product denial cases

Tests should also deny:

- joining unrelated products solely because they are NOAA;
- inheriting a source role from the family name;
- replacing missing product metadata with guessed defaults;
- dropping product version or file vintage;
- collapsing issue time, observation time, valid time, and retrieval time;
- normalizing units without recording the transform;
- converting qualitative categories to quantitative measurements without a governed downstream transform;
- treating an official source as sufficient for KFM publication.

[Back to top](#top)

---

<a id="parsing-and-preservation-tests"></a>

## Parsing and preservation tests

Parser tests should operate on supplied bytes, text, records, or streams. They should not open the network.

### Required preservation families

- source-native IDs;
- product and sub-product identity;
- source format and version;
- file or distribution identity;
- observation time;
- issue time;
- valid time;
- expiry time;
- retrieval time;
- correction or revision time;
- file vintage;
- units;
- quality flags;
- uncertainty and confidence;
- geometry and coordinate reference metadata;
- station, depth, level, model run, forecast hour, platform, and instrument identifiers;
- rights, citation, attribution, and sensitivity context references;
- raw-versus-derived status;
- missing-value semantics;
- source role candidate;
- content digest.

### Parser failure cases

- malformed record;
- truncated record;
- unexpected delimiter;
- invalid encoding;
- unknown field;
- missing required product identity;
- invalid timestamp;
- conflicting time fields;
- unknown units;
- invalid geometry;
- excessive coordinates or nesting;
- unsupported product version;
- duplicate identifiers;
- empty payload;
- mixed product types;
- schema drift.

### No silent repair

A parser must not silently:

- invent missing identifiers;
- infer a source role from NOAA alone;
- coerce invalid values into plausible values;
- replace unknown units;
- repair geometry without a transform record;
- fill missing times from retrieval time;
- convert qualitative categories into measurements;
- strip caveats or quality flags;
- discard unknown fields without an explicit compatibility policy.

[Back to top](#top)

---

<a id="source-admission-handoff-tests"></a>

## Source-admission handoff tests

Connector-local tests should prove candidate construction, not persistent lifecycle writes.

### Allowed candidate targets

```text
RAW candidate
QUARANTINE candidate
```

### Forbidden direct targets

```text
WORK
PROCESSED
CATALOG
TRIPLET
PUBLISHED
release manifests
public API payloads
public UI layers
map tiles
alert feeds
EvidenceBundle closure
```

### Required candidate assertions

A candidate should carry, where applicable:

- source family and product lane;
- source descriptor reference;
- request or distribution identity;
- retrieval metadata;
- source-native identifiers;
- product version and file vintage;
- source-role candidate;
- time kinds;
- units and quality metadata;
- geometry metadata;
- content digest;
- rights and sensitivity context;
- parser/adapter version;
- outcome;
- quarantine reasons;
- replay reference or captured-input digest;
- no public-release claim.

### Quarantine cases

- descriptor missing or inactive;
- rights unknown;
- sensitivity unknown;
- endpoint or product unapproved;
- source role unresolved;
- product metadata missing;
- schema drift;
- invalid integrity metadata;
- malformed or partial payload;
- stale or contradictory time context;
- unsupported version;
- security/resource limit reached;
- not-life-safety guard triggered;
- unexpected parser exception.

[Back to top](#top)

---

<a id="outcome-and-reason-code-tests"></a>

## Outcome and reason-code tests

Package-local connector outcomes are implementation details and must remain distinct from canonical `PolicyDecision` outcomes.

### Proposed package-local outcomes

| Outcome | Meaning |
|---|---|
| `ADMIT_RAW_CANDIDATE` | Parser and connector-local gates support a RAW candidate handoff. |
| `QUARANTINE_CANDIDATE` | Material is preserved for review but blocked from outward progression. |
| `SKIP_NO_CHANGE` | The source response or manifest indicates no new admissible payload. |
| `ABSTAIN_UNSUPPORTED` | The package cannot safely interpret the supplied product/version/context. |
| `RETRY_LATER` | A bounded transient condition may be retried by orchestration. |
| `ERROR` | An integrity, configuration, parser, transport, or process failure occurred. |

These values are **PROPOSED**, not verified code or schema.

### Proposed reason-code families

```text
NOAA_CFG_*
NOAA_DESCRIPTOR_*
NOAA_NETWORK_*
NOAA_RATE_LIMIT_*
NOAA_TIMEOUT_*
NOAA_REDIRECT_*
NOAA_PAYLOAD_*
NOAA_ARCHIVE_*
NOAA_PRODUCT_*
NOAA_ROLE_*
NOAA_TIME_*
NOAA_UNITS_*
NOAA_GEOMETRY_*
NOAA_QUALITY_*
NOAA_RIGHTS_*
NOAA_SENSITIVITY_*
NOAA_LIFE_SAFETY_*
NOAA_PARSE_*
NOAA_DRIFT_*
NOAA_INTEGRITY_*
NOAA_INTERNAL_*
```

Tests should prove that:

- failures resolve to finite outcomes;
- reason codes are stable enough for review;
- sensitive details are not embedded in reason strings;
- retryable and non-retryable conditions remain distinct;
- unknown errors fail closed;
- package outcomes are not serialized as release or policy approval;
- test runner `PASS`/`FAIL` status is not confused with connector outcome.

[Back to top](#top)

---

<a id="provenance-time-and-integrity-tests"></a>

## Provenance, time, and integrity tests

### Provenance assertions

Tests should prove preservation of:

- source family;
- product lane;
- source descriptor reference;
- endpoint or distribution key;
- request parameters after redaction;
- retrieval timestamp;
- response status;
- response headers selected for provenance;
- file or object identity;
- content length;
- content digest;
- parser and adapter version;
- fixture or replay identity.

### Time-kind separation

The following must remain distinct when present:

| Time kind | Example meaning |
|---|---|
| observation time | When a sensor or event observation applies. |
| issue time | When a forecast, alert, analysis, or product was issued. |
| valid time | When a forecast or product field applies. |
| expiry time | When a product or warning ceases to apply. |
| retrieval time | When KFM fetched or received the source payload. |
| file vintage | Which source file revision or distribution snapshot was used. |
| correction time | When the source corrected or replaced a prior item. |
| release time | Downstream KFM release time; not connector-owned. |

Required negative tests:

- retrieval time used as observation time;
- issue time used as valid time;
- file timestamp treated as event time without product support;
- timezone discarded;
- ambiguous local time silently accepted;
- correction overwrites prior lineage;
- expired product treated as current;
- stale product accepted without an explicit posture.

### Integrity assertions

- identical bytes produce identical content digests;
- canonicalization, if used, is versioned;
- compressed and decompressed digests are not confused;
- partial reads do not produce a successful full-payload digest;
- digest mismatch routes to quarantine or error;
- fixture digests are stable and reviewable.

[Back to top](#top)

---

<a id="rights-sensitivity-and-life-safety-tests"></a>

## Rights, sensitivity, and life-safety tests

### Rights tests

- missing terms or rights reference fails closed;
- required attribution is preserved;
- redistribution restrictions are propagated;
- source-side terms are not inferred from federal-source identity alone;
- test fixtures document their own rights posture;
- recorded responses are not committed without review;
- downstream public eligibility is never asserted by connector tests.

### Sensitivity tests

- exact infrastructure or private-person content routes to review when applicable;
- casualty or damage narratives are handled without unnecessary replication;
- request and response logs are minimized;
- sensitive geometry is not copied into assertion messages;
- test snapshots do not leak raw restricted payloads;
- unknown sensitivity fails closed.

### Not-life-safety tests

Tests must prove that connector code does not:

- issue warnings, watches, advisories, or emergency instructions;
- rebrand NOAA/NWS text as KFM guidance;
- state that a user is safe or unsafe;
- recommend evacuation, sheltering, travel, firefighting, or health action;
- convert smoke products into health exposure advice;
- present historical storm records as current hazards;
- suppress official-source attribution or redirection requirements;
- make a KFM alert feed.

A test may confirm that official source context is preserved. It cannot certify life-safety fitness.

[Back to top](#top)

---

<a id="security-and-data-minimization-tests"></a>

## Security and data-minimization tests

Minimum security families:

| Threat | Required test posture |
|---|---|
| SSRF | Block unapproved schemes, hosts, loopback, link-local, and private-network targets. |
| Redirect abuse | Do not leak credentials or bypass allowlists across redirects. |
| Secret leakage | Redact headers, query parameters, environment values, and exception context. |
| Archive traversal | Reject `../`, absolute paths, symlink escapes, and device paths. |
| Decompression bomb | Enforce compressed/decompressed size and member-count limits. |
| Content-type confusion | Validate expected format independently of filename. |
| Unsafe deserialization | Never use unsafe object deserialization for source payloads or fixtures. |
| Log injection | Normalize or escape untrusted control characters and line breaks. |
| Dependency confusion | Pin and review package sources and names once dependencies exist. |
| Fixture poisoning | Validate fixture status, digest, and intended product lane. |
| Resource exhaustion | Bound records, coordinates, nesting, retries, concurrency, and duration. |
| Path escape | Ensure test temporary paths cannot target repository or lifecycle stores unintentionally. |
| Snapshot leakage | Prevent secrets, private URLs, or bulk payloads in snapshots and failure output. |

Test assertions and exception messages should include enough context to fix a defect without echoing entire source records.

[Back to top](#top)

---

<a id="isolation-determinism-and-replay-tests"></a>

## Isolation, determinism, and replay tests

### Isolation

Each test should:

- use a temporary directory;
- clean up created files;
- restore environment variables;
- restore monkeypatches and fake clocks;
- avoid shared mutable global state;
- avoid ordering dependencies;
- avoid reliance on the developer’s locale or timezone;
- avoid external caches;
- avoid repository lifecycle directories.

### Determinism

For the same:

- fixture bytes;
- connector configuration;
- adapter version;
- parser version;
- fake clock;
- product profile;

the package should produce an equivalent parsed result or finite outcome.

Volatile values must be:

- injected;
- normalized;
- asserted separately;
- or explicitly excluded with justification.

### Replay

A replay test should prove that a captured payload can be reprocessed without live access while preserving:

- payload digest;
- product identity;
- source-native IDs;
- time kinds;
- parser version;
- expected outcome;
- quarantine reasons;
- correction lineage where applicable.

Replay evidence does not prove that the live source still behaves the same.

[Back to top](#top)

---

<a id="live-test-isolation"></a>

## Live-test isolation

No accepted live-test implementation was established in this session.

The current README’s example flag, `KFM_ALLOW_LIVE_NOAA_TESTS`, is documentation-only. It must not be treated as accepted configuration until code, policy, CI, and steward review establish it.

If live smoke tests are later approved, they must be:

- in a separate directory or marker class;
- skipped by default;
- excluded from ordinary pull-request CI;
- source-descriptor-gated;
- rights- and sensitivity-reviewed;
- rate-limited;
- bounded by strict timeout, payload, retry, and concurrency limits;
- non-mutating at the source;
- unable to publish or write downstream lifecycle state;
- explicit about official-source attribution;
- redacted in logs;
- recorded with run metadata;
- safe when the source is unavailable;
- clearly non-authoritative for life safety or production readiness.

A live smoke test may answer “did this approved source surface respond under this profile at this time?” It cannot answer “is the source complete, current, safe, or publishable?”

[Back to top](#top)

---

<a id="ci-coverage-and-evidence"></a>

## CI, coverage, and evidence

### Current state

`.github/workflows/connector-gate.yml` currently contains TODO echo steps for:

- connector output gating;
- ingest receipt presence.

A successful run of that workflow does not currently prove NOAA connector behavior.

### Required CI evidence before claiming enforcement

- test dependencies install successfully;
- package installs or imports under the intended method;
- NOAA tests are collected;
- offline/network-blocking controls are active;
- tests execute rather than echo;
- failures block the required branch or merge path;
- artifacts identify commit, environment, test command, and result;
- coverage reports refer to executable package code;
- skipped tests and reasons are visible;
- live tests remain excluded unless separately approved;
- CI logs avoid secrets and bulk payloads.

### Coverage posture

A numeric coverage threshold is not established.

Before adopting one:

1. implement meaningful package code;
2. identify critical invariants;
3. require branch coverage for fail-closed paths;
4. measure mutation or negative-path quality where practical;
5. avoid treating line coverage as behavioral proof;
6. record exclusions with reasons;
7. separate package-unit, connector-integration, and live-smoke coverage.

### Evidence artifacts

Proposed, subject to repository convention:

- test result summary;
- collected-test inventory;
- coverage report;
- fixture manifest;
- environment/tool version record;
- network-isolation assertion;
- skipped/live-test report;
- failure artifact with minimized context.

These are test evidence, not EvidenceBundles or release receipts.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

Each step should be a small, reversible PR.

### Step 1 — Test tooling and package metadata

- choose the test runner;
- harden `pyproject.toml`;
- declare test dependencies;
- establish package discovery;
- document the import namespace;
- add one collection smoke test.

**Stop if:** package discovery or namespace ownership is unresolved.

### Step 2 — Active network denial

- add a connector-local network-blocking fixture or fake transport;
- prove import and parser tests cannot use live network;
- prove no credential requirement.

**Stop if:** tests can silently fall back to live access.

### Step 3 — Import and side-effect tests

- add package import test;
- assert no network, files, threads, logging, or lifecycle writes;
- assert the reviewed import surface.

**Stop if:** import initializes runtime behavior.

### Step 4 — Fixture manifest and synthetic samples

- define fixture metadata;
- add one minimal synthetic fixture;
- add malformed, drifted, and oversized-simulated variants;
- record digests.

**Stop if:** fixture rights, sensitivity, or source shape is unclear.

### Step 5 — Product profile and parser slice

Choose one product lane and implement:

- explicit product identity;
- parser interface;
- native-field preservation;
- time-kind preservation;
- source-role candidate;
- negative cases.

**Stop if:** product doctrine or version semantics are unresolved.

### Step 6 — Admission-candidate tests

- build RAW/QUARANTINE candidate objects;
- assert forbidden downstream targets;
- add finite outcomes and reason codes;
- test descriptor, rights, and sensitivity failures.

**Stop if:** candidate schema or authority boundary is unclear.

### Step 7 — Security and resource limits

- endpoint allowlist;
- SSRF denial;
- timeout/retry/rate-limit bounds;
- payload and decompression limits;
- archive safety;
- log redaction.

**Stop if:** transport behavior cannot be bounded.

### Step 8 — CI collection and enforcement

- replace TODO-only workflow steps with real commands;
- surface collection count and skipped tests;
- block merge on failures where governance accepts;
- retain minimized evidence.

**Stop if:** CI can pass without collecting NOAA tests.

### Step 9 — Additional product lanes

Add product lanes one at a time with independent fixtures and anti-collapse tests.

**Stop if:** code attempts a single NOAA-wide role or schema.

### Step 10 — Optional live smoke profile

Only after explicit policy, source descriptor, CI, and steward approval.

**Stop if:** live tests are required for ordinary correctness or can publish.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

The NOAA connector test lane is not implementation-complete until:

- [ ] owners are assigned;
- [ ] package metadata declares the actual test tooling;
- [ ] package discovery and import namespace are accepted;
- [ ] at least one executable test module exists;
- [ ] test collection is demonstrated;
- [ ] default tests actively block network access;
- [ ] imports are proven side-effect-free;
- [ ] tests require no credentials;
- [ ] fixture classes and metadata are accepted;
- [ ] fixtures are synthetic/minimized/redacted/approved and digest-addressed;
- [ ] product-specific source roles are tested;
- [ ] time kinds are tested separately;
- [ ] units, quality, geometry, uncertainty, and product versions are preserved;
- [ ] RAW/QUARANTINE candidate behavior is tested;
- [ ] direct downstream lifecycle and publication writes are denied;
- [ ] rights and sensitivity uncertainty fail closed;
- [ ] not-life-safety behavior is tested;
- [ ] malformed, stale, empty, partial, drifted, oversized, and unsupported inputs are tested;
- [ ] SSRF, redirect, archive, decompression, secret, logging, and resource controls are tested;
- [ ] replay and determinism are tested;
- [ ] package-local outcomes and reason codes are tested;
- [ ] connector outcomes remain distinct from `PolicyDecision`;
- [ ] the connector-gate workflow executes real tests;
- [ ] CI cannot pass with zero collected NOAA tests;
- [ ] coverage posture is documented without overclaiming;
- [ ] live tests, if any, are separately approved and skipped by default;
- [ ] correction, deprecation, and rollback paths are documented;
- [ ] documentation matches the implemented inventory;
- [ ] no test or fixture creates source truth, release authority, or public guidance.

[Back to top](#top)

---

<a id="review-burden"></a>

## Review burden

Changes require review proportional to consequence.

| Change | Minimum review |
|---|---|
| README clarification only | Connector or docs steward |
| Synthetic fixture | Connector + product/domain steward |
| Recorded public fixture | Connector + source/rights steward |
| Sensitive or exact-location fixture | Connector + sensitivity/security steward |
| Network-blocking mechanism | Connector + security/CI steward |
| Product anti-collapse rule | Connector + relevant domain steward |
| Package outcome/reason-code change | Connector + downstream consumer steward |
| CI enforcement change | Connector + CI/governance steward |
| Live-test profile | Connector + source + rights + sensitivity + security + CI stewards |
| Test that writes lifecycle data | Reject or redesign; requires explicit architecture decision |

Where practical, the author of a consequential connector change should not be the sole reviewer of the test that claims to prove it.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Verification item | Status | Evidence needed |
|---|---|---:|---|
| NOAA-TEST-001 | Confirm complete `connectors/noaa/tests/` inventory. | NEEDS VERIFICATION | Recursive repository tree or checkout. |
| NOAA-TEST-002 | Confirm actual test runner. | NEEDS VERIFICATION | Root/package config and workflow. |
| NOAA-TEST-003 | Confirm pytest or alternative configuration. | NEEDS VERIFICATION | Config files and collection output. |
| NOAA-TEST-004 | Confirm test dependencies. | NEEDS VERIFICATION | Hardened package metadata/lockfile. |
| NOAA-TEST-005 | Confirm package installability. | NEEDS VERIFICATION | Build/install logs. |
| NOAA-TEST-006 | Confirm accepted Python import namespace. | NEEDS VERIFICATION | ADR or package review. |
| NOAA-TEST-007 | Confirm network-blocking mechanism. | NEEDS VERIFICATION | Fixture/plugin/code and failing proof. |
| NOAA-TEST-008 | Confirm actual offline test command. | NEEDS VERIFICATION | CI/local logs. |
| NOAA-TEST-009 | Confirm fixture root and ownership. | NEEDS VERIFICATION | Directory Rules/ADR and fixture manifest. |
| NOAA-TEST-010 | Confirm approved fixture statuses. | NEEDS VERIFICATION | Review records. |
| NOAA-TEST-011 | Confirm active NOAA SourceDescriptor IDs. | NEEDS VERIFICATION | Source registry and activation decisions. |
| NOAA-TEST-012 | Confirm accepted endpoint/distribution inventory. | NEEDS VERIFICATION | Descriptor and transport config. |
| NOAA-TEST-013 | Confirm first implemented product lane. | NEEDS VERIFICATION | Package code and tests. |
| NOAA-TEST-014 | Confirm parser interface and parsed-record model. | NEEDS VERIFICATION | Code/contracts/tests. |
| NOAA-TEST-015 | Confirm admission-candidate shape. | NEEDS VERIFICATION | Contract/schema/adapter/tests. |
| NOAA-TEST-016 | Confirm connector outcome vocabulary. | NEEDS VERIFICATION | Code or accepted contract. |
| NOAA-TEST-017 | Confirm reason-code registry. | NEEDS VERIFICATION | Code/docs/tests. |
| NOAA-TEST-018 | Confirm source-role vocabulary and mapping. | NEEDS VERIFICATION | Accepted source-role authority. |
| NOAA-TEST-019 | Confirm time-kind contract. | NEEDS VERIFICATION | Contract/schema/product docs. |
| NOAA-TEST-020 | Confirm rights and attribution bindings. | NEEDS VERIFICATION | Policy/source descriptor/tests. |
| NOAA-TEST-021 | Confirm sensitivity bindings. | NEEDS VERIFICATION | Policy/source descriptor/tests. |
| NOAA-TEST-022 | Confirm not-life-safety enforcement. | NEEDS VERIFICATION | Code/tests/runtime boundary. |
| NOAA-TEST-023 | Confirm SSRF and endpoint allowlist controls. | NEEDS VERIFICATION | Transport code/security tests. |
| NOAA-TEST-024 | Confirm retry, timeout, and rate-limit policy. | NEEDS VERIFICATION | Config/code/tests. |
| NOAA-TEST-025 | Confirm payload and decompression limits. | NEEDS VERIFICATION | Config/code/security tests. |
| NOAA-TEST-026 | Confirm archive safety. | NEEDS VERIFICATION | Parser code/tests. |
| NOAA-TEST-027 | Confirm secret/log redaction. | NEEDS VERIFICATION | Logging code/tests. |
| NOAA-TEST-028 | Confirm replay and deterministic output. | NEEDS VERIFICATION | Captured fixtures/tests. |
| NOAA-TEST-029 | Confirm schema-drift behavior. | NEEDS VERIFICATION | Drift fixtures/tests. |
| NOAA-TEST-030 | Confirm CI collects NOAA tests. | NEEDS VERIFICATION | Workflow logs with collection count. |
| NOAA-TEST-031 | Confirm CI failure blocks governed merge path. | NEEDS VERIFICATION | Branch protection/workflow evidence. |
| NOAA-TEST-032 | Confirm coverage method and threshold posture. | NEEDS VERIFICATION | Coverage config/report. |
| NOAA-TEST-033 | Confirm retained CI/test artifacts. | NEEDS VERIFICATION | Artifact policy and run output. |
| NOAA-TEST-034 | Confirm live-test policy. | NEEDS VERIFICATION | Accepted policy and steward approval. |
| NOAA-TEST-035 | Confirm live-test flag or marker names. | NEEDS VERIFICATION | Implemented config/tests. |
| NOAA-TEST-036 | Confirm live tests are excluded from PR CI. | NEEDS VERIFICATION | Workflow and marker evidence. |
| NOAA-TEST-037 | Confirm test data retention and purge. | NEEDS VERIFICATION | Retention policy. |
| NOAA-TEST-038 | Confirm fixture correction/supersession process. | NEEDS VERIFICATION | Fixture manifest and runbook. |
| NOAA-TEST-039 | Confirm test deprecation process. | NEEDS VERIFICATION | Governance docs and examples. |
| NOAA-TEST-040 | Confirm rollback automation or documented manual path. | NEEDS VERIFICATION | Workflow/runbook. |

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-supersession"></a>

## Rollback, correction, deprecation, and supersession

### Documentation rollback

For this README revision:

- revert the documentation commit; or
- restore the prior blob recorded in the metadata block.

A documentation rollback does not roll back package code, fixtures, workflows, source activation, or runtime state.

### Test rollback

A test change should be independently revertible when it:

- causes false failures;
- encodes an unaccepted contract;
- leaks source or sensitive content;
- depends on unstable live behavior;
- masks network access;
- creates nondeterminism;
- blocks correction or compatibility work without evidence.

Do not simply delete a failing governance test when implementation violates an accepted invariant. Fix the implementation, or explicitly supersede the invariant through the proper governance path.

### Fixture correction

When a fixture is wrong:

1. preserve the prior fixture digest in history;
2. state the defect;
3. create a corrected fixture with a new digest;
4. update affected tests;
5. identify prior test conclusions that may be invalid;
6. re-run relevant test families;
7. record supersession in the fixture manifest or accepted equivalent.

### Deprecation

A deprecated test or fixture should state:

- deprecation reason;
- replacement;
- first deprecated version/date;
- removal condition;
- downstream impact;
- rollback path.

### Contract supersession

If a package contract, source-role vocabulary, product version, schema, or policy changes:

- update the authority first;
- add compatibility fixtures where required;
- update tests in the same governed change or explain sequencing;
- preserve old-version behavior long enough for migration where policy permits;
- do not silently rewrite goldens to make a breaking change appear passing.

[Back to top](#top)

---

<details>
<summary><strong>Appendix A — illustrative test layout</strong></summary>

The following is **PROPOSED** and not a repository inventory.

```text
connectors/noaa/tests/
├── README.md
├── conftest.py
├── fixtures/
│   ├── manifest.yaml
│   ├── storm_events/
│   ├── nws_api/
│   ├── hms_smoke/
│   ├── hrrr_smoke/
│   ├── goes_abi_aod/
│   ├── viirs_hotspot/
│   ├── uscrn/
│   └── station_climate/
├── test_import_safety.py
├── test_configuration.py
├── test_transport_bounds.py
├── test_product_dispatch.py
├── test_parser_preservation.py
├── test_time_kinds.py
├── test_source_role_anti_collapse.py
├── test_admission_candidates.py
├── test_rights_sensitivity.py
├── test_not_life_safety.py
├── test_security.py
├── test_replay_determinism.py
└── live/
    └── README.md
```

Do not create this tree mechanically. Add the smallest files needed for the first implemented product slice, and verify placement before each addition.

</details>

<details>
<summary><strong>Appendix B — illustrative fixture metadata</strong></summary>

This example is non-canonical and inactive.

```yaml
fixture_id: noaa-uscrn-synthetic-observation-001
fixture_status: synthetic
source_family: noaa
product_lane: uscrn
source_role_candidate: observed
source_format: illustrative-text
source_version: test-v1
rights_posture: test-only
sensitivity_posture: public-safe-synthetic
network_required: false
expected_outcome: ADMIT_RAW_CANDIDATE
supports_tests:
  - import-safety
  - parser-preservation
  - time-kind-separation
  - source-role-anti-collapse
content_digest: sha256:TBD
review:
  state: draft
  reviewers: []
```

</details>

<details>
<summary><strong>Appendix C — illustrative offline test command</strong></summary>

No command is accepted yet. A future repository-approved command may resemble:

```bash
python -m pytest connectors/noaa/tests -m "not live"
```

A future network-isolation wrapper may be required. Do not infer that this command currently collects or executes NOAA tests.

</details>

<details>
<summary><strong>Appendix D — minimum negative-path matrix</strong></summary>

| Condition | Expected test assertion |
|---|---|
| Import triggers network | Fail |
| Live mode enabled implicitly | Fail |
| Missing descriptor | Quarantine/refuse |
| Unknown product | Abstain/refuse |
| Family-wide NOAA role | Fail |
| Retrieval time used as observation time | Fail |
| AOD converted directly to PM2.5 | Fail |
| HMS density treated as concentration | Fail |
| USCRN station treated as area truth | Fail |
| Storm Events treated as current alert | Fail |
| NWS content emitted as KFM guidance | Fail |
| Unsupported product version | Drift/quarantine |
| Malformed payload | Finite parse error |
| Oversized payload | Resource-limit outcome |
| Redirect to unapproved host | Security denial |
| Secret appears in log | Fail |
| Direct PUBLISHED write attempted | Fail |
| Test silently accesses live source | Fail |
| CI collects zero NOAA tests | Fail once CI enforcement exists |

</details>

---

## Maintainer summary

Keep NOAA connector tests offline, product-specific, negative-path-first, deterministic, and honest about what they prove. The first useful milestone is not a large suite—it is one installed package slice, one actively network-blocked test runner, one synthetic fixture, one product-specific parser contract, and one RAW/QUARANTINE admission path with explicit refusal tests.

<p align="right"><a href="#top">Back to top</a></p>
