<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-inaturalist-tests-readme
title: connectors/inaturalist/tests/ — iNaturalist Connector Test Contract
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Test steward · Python/package steward · Source steward · Fauna steward · Flora steward · Biodiversity/taxonomy steward · Rights reviewer · Sensitivity/geoprivacy reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-12
policy_label: public-doctrine; test-contract; repository-present; implementation-unverified; no-network-by-default; synthetic-fixtures; descriptor-and-activation-gated; product-explicit; rights-gated; geoprivacy-preserving; sensitivity-fail-closed; raw-quarantine-receipt-boundary; no-publication
path: connectors/inaturalist/tests/README.md
truth_posture: CONFIRMED test-lane README and package scaffold / PROPOSED suite layout, fixtures, markers, test APIs, and implementation sequence / CONFLICTED descriptor, registry, schema, and adjacent documentation details / UNKNOWN executable coverage, package installability, CI enforcement, live-source behavior, and runtime results
related:
  - ../../README.md
  - ../README.md
  - ../pyproject.toml
  - ../observations/README.md
  - ../src/README.md
  - ../src/inaturalist/README.md
  - ../src/inaturalist/__init__.py
  - ../src/inaturalist/fetch.py
  - ../src/inaturalist/admit.py
  - ../src/inaturalist/descriptor.yaml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/inaturalist/README.md
  - ../../../docs/sources/catalog/inaturalist/research-grade-observations.md
  - ../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../contracts/domains/fauna/occurrence_evidence.md
  - ../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/
  - ../../../data/registry/fauna/sources/inaturalist.yaml
  - ../../../data/raw/fauna/inaturalist/README.md
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
tags: [kfm, connectors, inaturalist, tests, python, no-network, fixtures, observations, research-grade, rights, taxonomy, geoprivacy, sensitivity, replay, raw, quarantine, receipts, fail-closed, governance]
notes:
  - "At inspected base commit e7e3b18024f9eba9551ccc9627db8a4064961edc, this README existed as v0.1; the parent project remained kfm-connector-inaturalist version 0.0.0; fetch.py and admit.py remained one-line placeholders; and descriptor.yaml remained unresolved."
  - "Direct probes for tests/conftest.py, tests/test_import.py, tests/test_fetch.py, tests/test_admit.py, and tests/fixtures/README.md returned Not Found. An indexed search for test_inaturalist returned no result. These are bounded absence observations, not proof that no differently named or unindexed test exists."
  - "The package and observation-product READMEs are v0.2 contracts, but no executable iNaturalist connector test, package build/install/import proof, accepted SourceDescriptor, activation decision, source payload, source-run receipt, or live-source result was verified."
  - "The connector-local descriptor.yaml is not test authority or activation authority. Its role and rights are TBD, and sensitivity_floor: public conflicts with the source profile's fail-closed posture for unknown sensitivity."
  - "This revision defines the accepted test boundary and staged suite design. It creates no executable test, fixture payload, endpoint selection, credential, policy decision, source activation, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# iNaturalist Connector Test Contract

> Evidence-grounded test contract for the source-first iNaturalist connector family. This lane must prove that package mechanics remain deterministic, no-network by default, source-preserving, product-explicit, rights-aware, geoprivacy-preserving, sensitivity-fail-closed, and unable to publish.

<p>
  <img alt="Status: test contract draft" src="https://img.shields.io/badge/status-test__contract__draft-yellow">
  <img alt="Coverage: executable tests unverified" src="https://img.shields.io/badge/coverage-executable__tests__unverified-lightgrey">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: synthetic and minimized" src="https://img.shields.io/badge/fixtures-synthetic__and__minimized-blue">
  <img alt="Product: explicit routing" src="https://img.shields.io/badge/product-explicit__routing-purple">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-critical">
  <img alt="Lifecycle: RAW quarantine receipts" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20%7C%20receipts-orange">
  <img alt="Publication: forbidden" src="https://img.shields.io/badge/publication-forbidden-critical">
</p>

`connectors/inaturalist/tests/`

> [!IMPORTANT]
> **Inspected state:** at base commit `e7e3b18024f9eba9551ccc9627db8a4064961edc`, the test lane contained this v0.1 README, while common executable test paths directly probed in this update were absent. The parent project remained version `0.0.0`; `fetch.py` and `admit.py` were one-line placeholders; and no package build, install, import, parser, admission, fixture, source-run receipt, or live-source result was verified. This README defines tests that must exist before implementation claims are credible. It is not evidence that those tests run.

> [!CAUTION]
> **Do not make the local descriptor pass by treating it as authority.** `../src/inaturalist/descriptor.yaml` currently contains `role: TBD`, `rights: TBD`, and `sensitivity_floor: public`. Tests must prove that package code does not auto-load it and that it cannot activate source access or establish a public sensitivity posture.

> [!WARNING]
> **Default tests must be hermetic.** Importing modules or running the ordinary suite must not contact iNaturalist, resolve DNS, open sockets, read credentials, inspect the user's environment for activation, mutate lifecycle storage, refresh fixtures, or expose private or sensitive observation context.

> [!WARNING]
> **A green test is not publication authority.** Connector-local tests can prove mechanics and boundaries. They cannot approve source terms, rights, taxonomy, sensitivity, public precision, EvidenceBundle closure, release state, or a public biodiversity claim.

**Quick jumps:** [Purpose](#purpose) · [Current repository state](#current-repository-state) · [Test authority and placement](#test-authority-and-placement) · [Test principles](#test-principles) · [Proposed suite layout](#proposed-suite-layout) · [Fixture contract](#fixture-contract) · [Import and packaging tests](#import-and-packaging-tests) · [Descriptor activation and product tests](#descriptor-activation-and-product-tests) · [Query fetch and transport tests](#query-fetch-and-transport-tests) · [Parsing and preservation tests](#parsing-and-preservation-tests) · [Admission and finite-outcome tests](#admission-and-finite-outcome-tests) · [Rights taxonomy geoprivacy and sensitivity tests](#rights-taxonomy-geoprivacy-and-sensitivity-tests) · [Time geometry replay and correction tests](#time-geometry-replay-and-correction-tests) · [Handoff receipt and lifecycle-boundary tests](#handoff-receipt-and-lifecycle-boundary-tests) · [Security logging and privacy tests](#security-logging-and-privacy-tests) · [Live-source test policy](#live-source-test-policy) · [Execution CI and evidence contract](#execution-ci-and-evidence-contract) · [Implementation sequence](#implementation-sequence) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog) · [Review and rollback](#review-and-rollback)

---

## Purpose

This README turns the iNaturalist test lane from a broad aspiration into a reviewable test contract that can support small, reversible implementation PRs.

The lane may eventually contain tests that:

- prove importing the package has no observable side effects;
- prove live access is disabled unless descriptor, activation, product, scope, and network enablement are explicit;
- exercise request normalization, pagination, response integrity, parsing, admission, finite outcomes, handoff candidates, and receipt candidates through fakes;
- preserve source identity, product identity, grade, rights, taxonomy, time, geometry/support, uncertainty, geoprivacy, media references, and lineage;
- prove research-grade and non-research-grade observations remain separate products or dispositions;
- prove missing, unknown, conflicting, or restricted governance inputs fail closed;
- prove fixtures are synthetic, minimized, non-sensitive, deterministic, and safe to commit;
- prove package code cannot write outside explicit RAW, QUARANTINE, or process-memory receipt interfaces;
- prove public applications cannot treat connector internals or unreleased material as truth;
- generate ordinary test reports suitable for review without turning them into source evidence, proof closure, or release authority.

The lane does **not**:

- prove the current package builds, installs, imports, fetches, parses, admits, or emits receipts;
- choose an endpoint, API version, authentication method, rate limit, cadence, or live-test credential source;
- create or approve SourceDescriptor, SourceActivationDecision, rights policy, taxonomy authority, sensitivity policy, public-precision profile, or release decision;
- contain unmanaged live observations, private coordinates, observer contact data, media bytes, production credentials, or source terms copied without review;
- normalize package tests into EvidenceBundle, ProofPack, catalog closure, PromotionDecision, ReleaseManifest, or public claims;
- authorize direct writes to WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, registry, release, API, UI, map, search, graph, vector-index, or AI surfaces.

[Back to top ↑](#top)

---

## Current repository state

This snapshot is bounded to base commit `e7e3b18024f9eba9551ccc9627db8a4064961edc`, the direct paths inspected, and indexed searches performed in this update.

```text
connectors/inaturalist/
├── README.md
├── pyproject.toml                         # project name + version 0.0.0 only
├── observations/
│   └── README.md                          # v0.2 product contract
├── src/
│   ├── README.md
│   └── inaturalist/
│       ├── README.md                      # v0.2 package contract
│       ├── __init__.py                    # empty
│       ├── fetch.py                       # one-line placeholder
│       ├── admit.py                       # one-line placeholder
│       └── descriptor.yaml                # unsafe unresolved placeholder; not authority
└── tests/
    └── README.md                          # this test contract
```

| Item | Observed state | Safe conclusion |
|---|---|---|
| `tests/README.md` | v0.1 at base; blob `5ec771892cd8e740a1fa862cc97828553fd983a6`. | The test documentation path exists. |
| `tests/conftest.py` | Not found in direct probe. | No shared pytest-style fixture module was observed at that path. |
| `tests/test_import.py` | Not found in direct probe. | No import-side-effect test was observed at that path. |
| `tests/test_fetch.py` | Not found in direct probe. | No fetch test was observed at that path. |
| `tests/test_admit.py` | Not found in direct probe. | No admission test was observed at that path. |
| `tests/fixtures/README.md` | Not found in direct probe. | No documented test-local fixture subtree was observed at that path. |
| Indexed search for `test_inaturalist` | No result surfaced. | No indexed test with that name was observed; differently named or unindexed tests remain possible. |
| `pyproject.toml` | Distribution name `kfm-connector-inaturalist`; version `0.0.0`; no verified build backend, dependencies, package discovery, Python constraint, or test command. | Package installability and the exact test runner remain unknown. |
| `__init__.py` | Empty. | No stable package API is implemented or exported. |
| `fetch.py` and `admit.py` | One-line greenfield placeholders. | No executable fetch or admission behavior exists at those inspected files. |
| `descriptor.yaml` | `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | It is not accepted descriptor or activation authority and conflicts with fail-closed sensitivity doctrine. |
| Observation-product README | v0.2 research-grade-default product contract. | Required product behavior is documented; no product runtime or test is proven. |
| Package README | v0.2 package contract. | Required implementation and test boundaries are documented; no executable coverage is proven. |
| Package build/install/import, connector tests, fixtures, CI proof, live request, source payload, source-run receipt | Not verified. | Do not infer readiness or operation. |

Absence claims above are deliberately narrow. A complete recursive tree, import graph, workflow search, and test collection report are still required before stating that no differently named implementation or test exists.

The v0.1 test README was introduced by commit `08e926208c16efbafdd4743119f32e34e849fd79`, replacing a three-line greenfield stub. That history does not justify describing the current file as blank or newly created.

[Back to top ↑](#top)

---

## Test authority and placement

| Question | Current safe decision | Evidence posture |
|---|---|---:|
| What is the owning responsibility root? | Connector-family implementation tests remain with the existing `connectors/inaturalist/` source-first family, while cross-repository policy, schema, release, and public-client tests remain in their owning roots. | **CONFIRMED path / PROPOSED detailed split**. |
| Why not `connectors/fauna/inaturalist/tests/`? | Fauna is a consumer domain, not the canonical source implementation lane; duplicating source tests there would create parallel connector authority. | **CONFIRMED doctrine / current compatibility path**. |
| Why not `observations/tests/`? | The observation product directory is documentation-only in the inspected state. No product-local package or test subtree was verified. | **CONFIRMED bounded probes / UNKNOWN future layout**. |
| May tests live only here forever? | Not necessarily. Shared contract, schema, policy, release, public-client, and end-to-end tests belong in their repository-standard authorities. This lane owns connector-local mechanics and safe test doubles. | **PROPOSED responsibility split**. |
| Does this README ratify pytest or a package command? | No. Filenames and commands below are proposed Python conventions until `pyproject.toml`, package discovery, dependencies, and CI are accepted. | **NEEDS VERIFICATION**. |
| Does adding tests activate the source? | No. Test presence, green CI, and endpoint reachability do not replace SourceDescriptor or SourceActivationDecision. | **CONFIRMED boundary**. |

Directory Rules basis:

- `connectors/` owns source-specific fetch and admission implementation.
- Tests and fixtures validate implementation but do not become schema, policy, registry, proof, release, or publication authority.
- Source-derived bytes belong in governed lifecycle or fixture authorities selected by an accepted design; they do not belong in a convenience folder merely because a test needs them.
- Creating a parallel schema, policy, registry, receipt, proof, or release home requires an ADR or migration decision.
- This update changes an existing README only; it creates no new canonical path or authority root.

[Back to top ↑](#top)

---

## Test principles

Every future test in this lane should obey these rules.

1. **Hermetic by default.** Ordinary test collection and execution require no live network, DNS, credentials, service availability, wall clock, external randomness, or mutable source state.
2. **Import safety is testable.** Imports perform no network, filesystem writes, environment-secret reads, descriptor discovery, clock reads, UUID generation, logging setup, threads/processes, cache mutation, or activation.
3. **Explicit authority inputs.** Descriptor, activation, product, scope, rights, taxonomy, sensitivity, review, clock, transport, and storage inputs are supplied explicitly or the operation fails closed.
4. **Source family is not product.** Research-grade observation routing, casual/non-research-grade routing, aggregates, models, and administrative metadata remain distinct.
5. **Preserve before normalize.** Tests assert source-native values and provenance remain available alongside normalized values.
6. **Unknown remains visible.** Missing, unsupported, conflicting, restricted, changed, and unknown values are never silently defaulted to permissive states.
7. **Finite outcomes.** Expected source and governance conditions converge to structured outcomes and reason codes; retries and pagination are bounded.
8. **Determinism where practical.** Same safe inputs produce the same normalized request digest, parsed representation, decision content, candidate identity, and receipt content except for explicitly injected nondeterminism.
9. **Mixed batches remain mixed.** Per-record results are retained; one valid record does not hide one denied, quarantined, or failed record.
10. **No sensitive snapshots.** Exact private/obscured/restricted coordinates, observer-private data, credentials, cookies, signed URLs, raw bodies, media bytes, and EXIF do not appear in snapshots, assertion messages, logs, CI artifacts, or PR text.
11. **No authority collapse.** Test doubles may emulate accepted decisions; they do not become accepted SourceDescriptor, policy, taxonomy, sensitivity, proof, catalog, or release records.
12. **No lifecycle shortcuts.** Tests may use in-memory or temporary fake sinks for RAW, QUARANTINE, and receipt candidates. No default test writes canonical lifecycle directories.
13. **No public truth from connector output.** Parser and admission tests do not assert species presence, range, habitat, conservation status, legal status, or public-safe geometry.
14. **Receipts are process memory.** Receipt-candidate tests prove facts and lineage; they do not prove EvidenceBundle closure, human review, promotion, or release.
15. **Small reversible increments.** Each implementation PR adds one coherent capability, fixtures, negative cases, documentation, and rollback.
16. **Green means bounded.** A passing connector-local suite proves only the behavior actually asserted at the tested commit and configuration.

[Back to top ↑](#top)

---

## Proposed suite layout

The following layout is **PROPOSED**, not implemented. Do not create all files at once merely to make the tree look complete.

```text
connectors/inaturalist/tests/
├── README.md
├── conftest.py                          # shared fakes only; no hidden activation
├── test_import_safety.py
├── test_packaging.py
├── test_descriptor_activation.py
├── test_product_routing.py
├── test_query.py
├── test_fetch.py
├── test_parse.py
├── test_validate.py
├── test_admit.py
├── test_rights.py
├── test_taxonomy.py
├── test_geoprivacy.py
├── test_sensitivity.py
├── test_handoff.py
├── test_receipts.py
├── test_replay_correction.py
├── test_logging_privacy.py
└── fixtures/
    ├── README.md
    ├── manifest.yaml                    # optional, if accepted
    ├── observations/
    │   ├── valid/
    │   └── invalid/
    ├── responses/
    │   ├── valid/
    │   └── invalid/
    └── decisions/
        ├── rights/
        ├── taxonomy/
        ├── sensitivity/
        └── activation/
```

### Layering

| Layer | Purpose | Default external I/O | Evidence it may produce |
|---|---|---:|---|
| Pure unit | Models, canonicalization, reason codes, parsing helpers, validation, admission assembly. | None | Assertions and ordinary test reports. |
| Contract/fixture | Validate source-shaped fixtures, schema expectations, serialization, and negative cases. | None | Fixture-validation report in CI artifacts where supported. |
| Adapter integration | Exercise fake transport, fake clock, in-memory handoff sink, bounded retries, and failure conversion. | None | Ordinary test report and safe structured logs. |
| Repository boundary | Assert forbidden imports, paths, dependencies, and public-client coupling are absent. | None | Boundary-test report. |
| Live-source probe | Narrowly verify current source behavior after governance closure. | Explicitly enabled only | Source-run receipt and review evidence in governed locations, never ordinary fixture refresh. |

### Proposed naming rules

- Test names state the invariant and expected disposition, for example `test_missing_activation_denies_before_transport`.
- Negative tests name the failure condition rather than merely `invalid_1`.
- Parameterized cases retain readable case IDs such as `rights-missing`, `geo-obscured`, and `grade-casual`.
- Golden files are avoided when field-level assertions are clearer; snapshots are allowed only after sensitive-field allowlisting.
- Shared fixtures are explicit arguments, not module-import side effects or hidden global singletons.
- Time, IDs, randomness, transport, and sinks are injected.
- No test order dependency is permitted.
- No default retry sleeps or real clock delays are permitted.

The exact framework syntax, plugin list, marker names, and coverage tooling remain **NEEDS VERIFICATION**.

[Back to top ↑](#top)

---

## Fixture contract

Fixtures are test inputs, not source authority and not a shadow RAW store.

### Allowed fixture classes

| Class | Meaning | Default posture |
|---|---|---|
| `synthetic` | Invented values that exercise source-shaped structure without copying a live record. | Preferred. |
| `minimized` | Retains only fields needed for the assertion. | Preferred. |
| `generalized` | Spatial or temporal precision reduced to remove sensitivity. | Allowed with transform note. |
| `redacted` | Sensitive or personal fields removed or replaced. | Allowed with transform note. |
| `approved` | Externally derived snippet reviewed for rights, sensitivity, attribution, and committed use. | Exceptional; requires evidence. |

### Minimum fixture metadata

A future fixture registry or sidecar may record the following **PROPOSED** fields:

```yaml
fixture_id: inat-observation-research-grade-open-v1
classification: synthetic
source_family: inaturalist
product_id: research-grade-observations
case_purpose:
  - product-routing
  - rights
  - geoprivacy
expected_outcome: ADMIT_RAW
contains_real_person_data: false
contains_real_sensitive_geometry: false
contains_media_bytes: false
rights_posture: synthetic-no-external-rights
transform_notes: []
review_state: proposed
```

These fields are illustrative and do not establish a new schema. Reuse an accepted repository fixture contract if one exists.

### Required fixture dimensions

The eventual corpus should include minimal paired cases for:

- research-grade, casual/non-research-grade, unknown grade, captive/cultivated, disputed date/location, and other reviewed quality flags;
- recognized Creative Commons variants, missing rights, unrecognized rights, all-rights-reserved, conflicting rights, NonCommercial, ShareAlike, revoked rights, missing attribution, and separate media rights;
- open, obscured, private, generalized/place-only, missing, invalid, changed, and policy-restricted geometry states;
- controlled-taxonomy agreement, unresolved name, authority disagreement, changed identification, and taxon-rank change;
- observed time, source-created time, source-updated time, retrieval time, snapshot time, correction time, and invalid/ambiguous time;
- success, malformed body, partial body, duplicate page, cursor loop, timeout, forbidden, not-found, rate-limit, outage, and retry exhaustion;
- unchanged content/no-op, record update, source deletion, rights change, grade change, identification change, and geoprivacy change;
- valid admit, quarantine, abstain, deny, rate-limited, no-op, and error outcomes;
- mixed batches containing more than one disposition.

### Forbidden fixture content

- live credentials, API tokens, authorization headers, cookies, signed URLs, or private query values;
- unmanaged complete live responses;
- real exact rare-taxon, nest, den, roost, hibernaculum, breeding-site, cultural-site, archaeological, infrastructure-sensitive, or private-property coordinates;
- observer contact information, private profile data, user history, private-place descriptions, or re-identifying joins;
- media bytes, EXIF, embedded location, or copied profile images;
- source terms or license text copied beyond what is necessary and permitted;
- hidden fixture-refresh scripts that contact the source during ordinary tests;
- fixture values represented as current source facts.

Fixtures must be deterministic, reviewable, small, and safe to include in a public repository.

[Back to top ↑](#top)

---

## Import and packaging tests

Before package behavior is trusted, tests must prove:

### Import safety

- importing `inaturalist`, `inaturalist.fetch`, and `inaturalist.admit` makes no network or DNS call;
- imports do not open or write files;
- imports do not read environment variables for credentials, endpoints, activation, or descriptor location;
- imports do not read `descriptor.yaml`;
- imports do not access the clock, generate IDs, seed randomness, configure logging, emit logs, start threads/processes, or mutate caches;
- imports do not register public routes, map layers, plugins, watchers, or source jobs;
- imports succeed or fail deterministically under the accepted packaging configuration.

Tests should use monkeypatched or sentinel implementations that fail immediately if a forbidden side effect occurs.

### Packaging

Once packaging is implemented, tests must verify:

- accepted build backend and package discovery include only intended package files;
- the import name and distribution name are documented and stable;
- supported Python versions are explicit;
- runtime and test dependencies are declared;
- package data does not silently include `descriptor.yaml` as runtime authority;
- building a wheel or source distribution does not contact the network;
- installation into an isolated environment succeeds;
- the installed package exposes only the reviewed public surface;
- version metadata is deterministic and does not imply production readiness merely because it exceeds `0.0.0`.

No package build or install test was verified in this documentation update.

[Back to top ↑](#top)

---

## Descriptor activation and product tests

Tests must distinguish four separate concepts:

1. source-family identity;
2. product identity and version;
3. accepted SourceDescriptor;
4. SourceActivationDecision and allowed scope.

Required negative cases:

| Case | Required assertion | Expected posture |
|---|---|---|
| Descriptor missing | Transport is never called. | `DENY` or accepted equivalent. |
| Descriptor malformed | Validation failure remains visible. | `DENY` / `ERROR`, never allow. |
| Descriptor reference unresolved | No local fallback is loaded. | `ABSTAIN` or `DENY`. |
| Activation missing | Transport is never called. | `DENY`. |
| Activation expired/revoked | Transport is never called. | `DENY`. |
| Product missing | No request is built or sent. | `DENY` / `ABSTAIN`. |
| Product unsupported | Product is not silently coerced. | `PRODUCT_UNSUPPORTED`. |
| Scope exceeds activation | Query is rejected before transport. | `SCOPE_NOT_ALLOWED`. |
| Local `descriptor.yaml` present | It is not auto-discovered or loaded. | Test passes only when ignored. |
| Local `sensitivity_floor: public` | It cannot produce an admit or public posture. | `DESCRIPTOR_CONFLICT` / `SENSITIVITY_UNKNOWN`. |

Product-routing tests must prove:

- research-grade observation records use the current promotion-track product only when every supplied gate allows;
- casual or otherwise non-research-grade records are not upgraded, discarded without disposition, or routed through the research-grade product;
- product ID and version remain in request, parsed record, decision, candidate, and receipt;
- source-family metadata does not substitute for product metadata;
- aggregate or modeled derivatives cannot be labeled observed;
- administrative or recordset metadata cannot be labeled biological occurrence evidence;
- product rule changes are versioned and do not silently reinterpret prior outputs.

`OPEN-INAT-01` remains unresolved for non-research-grade observations; tests must preserve that unresolved posture rather than inventing a policy.

[Back to top ↑](#top)

---

## Query fetch and transport tests

### Query construction

Tests should prove that explicit query specifications:

- carry product, geographic, taxonomic, temporal, sort, page/cursor, limit, and scope fields;
- canonicalize deterministically;
- produce a stable safe digest;
- reject unbounded or contradictory scope;
- exclude credentials, authorization material, volatile timestamps, and private parameters from logs and public digest material;
- distinguish omitted, empty, unknown, and wildcard values;
- preserve user-supplied bounds without silently broadening them.

### Network default

- network is disabled unless `network_enabled` is explicitly true;
- an accepted descriptor and activation are still required when the flag is true;
- endpoint reachability alone does not activate access;
- tests do not infer activation from environment variables;
- fake transport is the default test path.

### Fake transport matrix

A fake transport should cover:

- success;
- redirects under an accepted redirect policy;
- forbidden and unauthorized;
- not found;
- timeout and connection failure;
- rate limit with safe retry metadata;
- source outage;
- malformed body;
- unsupported content type;
- partial body;
- duplicate page;
- repeated cursor / pagination loop;
- page-count, record-count, byte-count, timeout, retry, and total-work exhaustion;
- source schema drift;
- integrity mismatch;
- cancellation or caller stop.

Required assertions:

- retries are bounded and deterministic;
- backoff does not sleep in unit tests;
- rate-limit and retry evidence remains visible;
- credentials and response bodies do not enter exception text or logs;
- response digest and retrieval context are captured before parsing;
- a fetch result never claims admission, public safety, or source truth;
- transport failure converges to a finite result rather than an infinite retry or permissive fallback.

No endpoint, API version, auth mechanism, query grammar, pagination contract, rate-limit value, or current source behavior is ratified by this README.

[Back to top ↑](#top)

---

## Parsing and preservation tests

Parser tests must use approved source-shaped fixtures and assert preservation before normalization.

When present, parser output should preserve:

- source family and product ID/version;
- native observation ID, stable source URL/reference, and record version/modification marker;
- quality grade and quality flags, including captive/cultivated or disputed states;
- source taxon ID, names, rank, identifications, and source taxonomy context;
- observed/event time, source-created time, source-updated time, retrieval time, and snapshot time as distinct values;
- source geometry/support, positional accuracy or uncertainty, place support, and geoprivacy state;
- observation-level license, normalized token if mechanically available, attribution, and rights holder;
- media-reference IDs and media-specific rights separately from observation rights;
- source deletion or withdrawal marker where represented;
- request digest, response digest, page/cursor, connector version, parser version, and source lineage;
- unknown, missing, unsupported, and conflicting values without invented replacements.

Parser negative tests must prove it does not:

- infer research-grade from media or generated-language judgment;
- upgrade casual/non-research-grade records;
- resolve taxonomy silently;
- infer exact coordinates from text, photos, timestamps, nearby records, user history, or joins;
- replace private or obscured geometry with a centroid presented as exact;
- treat missing rights as permissive;
- merge observation and media rights;
- collapse source, observed, retrieval, snapshot, release, and correction times;
- treat parse success as admission or public-safe status;
- emit public occurrence objects, map features, range claims, habitat claims, or release-ready geometry.

Malformed or partial records should retain safe error context and finite reason codes without leaking payloads.

[Back to top ↑](#top)

---

## Admission and finite-outcome tests

Admission tests should be pure or use explicit fakes. They must not perform network access or choose storage paths.

### Required inputs

Tests should require explicit:

- parsed record and request/response lineage;
- source-family and product identity;
- accepted descriptor and activation references;
- product-rule reference;
- rights result;
- taxonomy result;
- source geoprivacy state;
- KFM sensitivity result;
- review requirement/disposition;
- target-interface request or candidate-only mode.

### Proposed outcome vocabulary

Until an accepted contract supersedes it, tests should exercise:

| Outcome | Minimum condition to assert |
|---|---|
| `ADMIT_RAW` | Every required source, product, rights, taxonomy, sensitivity, integrity, and review gate allows bounded RAW admission. |
| `QUARANTINE` | Material may be retained for review/remediation but is not promotion-track eligible. |
| `NO_OP` | Accepted request/source/content identity is unchanged and duplicate RAW material is not needed. |
| `RATE_LIMITED` | Source throttling is explicit with bounded retry evidence. |
| `ABSTAIN` | Scope or support is insufficient for a safe connector decision. |
| `DENY` | Descriptor, activation, product, rights, sensitivity, or policy blocks the operation. |
| `ERROR` | Transport, parsing, integrity, handoff, contract, or unexpected implementation failure occurs. |

### Core admission cases

- research-grade + recognized normalized Creative Commons rights + required attribution + accepted taxonomy resolution + preserved geoprivacy + allowed sensitivity + complete identity/time/geometry/integrity may reach `ADMIT_RAW`;
- removing any required gate from that case fails closed;
- casual/non-research-grade routes to candidate/quarantine under the current product;
- captive/cultivated or disputed-quality flags remain visible and route according to an accepted disposition;
- missing or conflicting rights, taxonomy, geoprivacy, sensitivity, identity, time, geometry, integrity, or review cannot admit;
- mixed batches retain per-record outcomes and batch summary counts;
- reason-code serialization is stable;
- identical explicit inputs yield deterministic decision content where practical;
- one record's success cannot suppress another record's error;
- no decision creates EvidenceBundle, proof, catalog, release, public-safe geometry, or public claim.

Expected source or governance conditions should not be tested only as free-text exceptions. Programmer errors may raise internally, but the package boundary must convert them into a finite safe result.

[Back to top ↑](#top)

---

## Rights taxonomy geoprivacy and sensitivity tests

### Rights and attribution

Tests must prove:

- original observation license and normalized token remain separate;
- media rights remain separate from observation rights;
- missing, unrecognized, conflicting, all-rights-reserved, or revoked rights fail closed;
- NonCommercial and ShareAlike obligations remain visible for downstream review;
- required attribution is preserved and minimized;
- missing attribution cannot be invented;
- one permissive record does not create source-wide permission;
- caching, mirroring, redistribution, republication, and model-training permission are not inferred from observation metadata;
- a license change triggers changed-source-state, correction, withdrawal, or re-evaluation behavior;
- observer-private fields do not enter logs, snapshots, receipts, or public output.

Mechanical token normalization can be unit-tested. Legal reuse permission remains policy/review-owned.

### Taxonomy and quality

Tests must prove:

- source taxon identity and identification context are preserved;
- taxonomy resolution requires an accepted authority/version result supplied by the caller;
- conflicting ITIS/GBIF or other authority results remain explicit;
- unresolved taxonomy fails closed under the current product;
- observation identity remains stable across taxonomic change;
- legal or conservation status is not inferred from taxonomy;
- research-grade is a source quality state, not KFM truth or public-release approval;
- grade and quality-flag changes produce version/correction lineage.

`OPEN-INAT-02` remains unresolved for taxonomy tie-breaking; tests should represent disagreement, not settle it.

### Geoprivacy

Cases must distinguish:

- open;
- obscured;
- private;
- generalized/place-only;
- missing;
- invalid;
- platform/observer restriction;
- changed geoprivacy state.

Tests must prove the connector never:

- deobscures;
- back-fills exact coordinates;
- treats private geometry as missing data to repair;
- derives precise geometry from media, descriptions, time, nearby records, user history, or joins;
- labels a centroid or place boundary as exact;
- exposes restricted geometry in logs, exceptions, snapshots, reports, or CI artifacts.

### KFM sensitivity

Tests must use caller-supplied decisions and cover:

- unknown sensitivity;
- rare or protected taxa;
- nests, dens, roosts, hibernacula, spawning sites, colonies, breeding sites, or other sensitive-site classes;
- private property;
- cultural or archaeological joins;
- infrastructure-sensitive joins;
- media location metadata;
- re-identification risk from combined fields;
- changed sensitivity-register state;
- unresolved public precision or reviewer requirement.

Unknown sensitivity must not inherit the local descriptor's `public` value. Connector tests may verify RAW/QUARANTINE dispositions; they must not generate final public geometry or `RedactionReceipt`.

[Back to top ↑](#top)

---

## Time geometry replay and correction tests

### Time separation

Tests should assert that these concepts do not collapse:

| Time | Required distinction |
|---|---|
| Observed/event time | When the organism or evidence was observed. |
| Source creation time | When the platform created or accepted the record. |
| Source update time | When source content, grade, identification, rights, or geoprivacy changed. |
| Retrieval time | When the connector fetched or referenced the response. |
| Snapshot/run time | When the bounded response set was materialized. |
| Release time | Downstream public release; outside connector authority. |
| Correction/withdrawal time | Downstream supersession; outside connector authority but linkable. |

Tests should cover precision, timezone, missing timezone, ambiguous dates, invalid ranges, source updates, and caller-supplied clocks. Retrieval time must never replace observed time.

### Geometry/support

Tests should distinguish:

- exact/open point support;
- obscured region;
- place or administrative boundary;
- generalized support;
- missing support;
- invalid coordinate;
- positional accuracy/uncertainty.

Bounds checking may prove numerical validity; it cannot establish truth, sensitivity approval, or public safety.

### Replay and no-op

Tests should verify that a replayable record can preserve:

- normalized request identity and digest;
- product identity;
- page/cursor state;
- retrieval/snapshot time;
- response digest or approved source reference;
- native record ID/version;
- connector/parser version;
- decision and reason codes;
- RAW/QUARANTINE/receipt references returned by a fake or caller-owned sink;
- prior-run, correction, withdrawal, and no-op lineage.

Required cases include:

- identical accepted content produces `NO_OP` where supported;
- changed record version or digest produces a new candidate linked to prior lineage;
- source deletion/withdrawal does not erase prior evidence silently;
- rights, grade, identification, and geoprivacy changes trigger re-evaluation;
- live re-fetch is not treated as replay of the bytes/reference originally used;
- ordering and pagination differences do not change identity when the accepted canonicalization says they are equivalent;
- canonicalization differences that are semantically material remain distinct.

Replay storage and identity contracts remain **NEEDS VERIFICATION**.

[Back to top ↑](#top)

---

## Handoff receipt and lifecycle-boundary tests

The safest default package behavior is candidate construction with no write.

### Allowed fake interfaces

Tests may use in-memory or temporary caller-supplied methods equivalent to:

```python
class HandoffSink:
    def write_raw(self, candidate): ...
    def write_quarantine(self, candidate): ...
    def write_receipt(self, candidate): ...
```

The signatures are illustrative, not accepted contracts.

### Required assertions

- default behavior returns candidates without filesystem writes;
- only explicit RAW, QUARANTINE, and process-memory receipt methods are callable;
- package code does not choose canonical destination paths internally;
- every write attempt requires explicit caller-owned sink and target class;
- candidate content includes source/product identity, digests, lineage, disposition, and safe review reasons;
- repeated identical writes are idempotent where the accepted interface requires it;
- handoff failure returns `ERROR` without losing prior lineage;
- partial batch handoff remains visible and does not report full success;
- receipt candidates preserve request, response, parser, decision, count, duration, retry, outcome, and lineage facts;
- receipt candidates do not assert EvidenceBundle, proof, catalog, promotion, human review, release, or public citation closure.

### Forbidden boundary assertions

Tests must prove there is no package path to:

```text
data/work/
data/processed/
data/catalog/
data/triplets/
data/published/
data/proofs/ as closure authority
data/registry/
release/
apps/ public API or UI
maps / tiles / search / graph / vector index / AI
```

Temporary directories used by tests must be isolated and removed. Ordinary test reports belong to CI/test tooling, not lifecycle truth stores.

[Back to top ↑](#top)

---

## Security logging and privacy tests

Use an allowlist, not a denylist alone.

### Safe fields to test

- run ID;
- source-family and product IDs;
- connector/parser version;
- safe request and response digests;
- page ordinal or cursor hash;
- safe endpoint-family label;
- response status class;
- counts;
- duration;
- bounded retry count;
- finite outcome and reason codes;
- non-sensitive temporary RAW/QUARANTINE/receipt references.

### Forbidden fields to test against

- API keys, tokens, authorization headers, cookies, signed URLs, credentials, or secret-bearing query strings;
- raw response bodies or oversized payload excerpts;
- exact private, obscured, restricted, or sensitive coordinates;
- observer contact information, private profiles, private-place context, or user history;
- media bytes, EXIF, embedded location, or binary snippets;
- unredacted exception locals or object representations;
- local descriptor contents presented as authority;
- statements that data is public-safe, confirmed, released, or authoritative without downstream evidence.

Required negative tests:

- errors and `repr()` values are scrubbed;
- assertion failures do not print sensitive fixtures;
- structured logs omit forbidden keys;
- snapshot serializers apply the allowlist;
- secrets do not enter request digests;
- fake credentials are recognizable test values and never sourced from the environment;
- importing modules does not configure root logging or emit a log line;
- CI artifacts do not retain forbidden fields.

[Back to top ↑](#top)

---

## Live-source test policy

Live-source tests are a separate governed activity, not an extension of the default unit suite.

They may be considered only after:

- an accepted SourceDescriptor exists in the accepted registry home;
- a SourceActivationDecision permits the exact product, query scope, environment, and test purpose;
- current endpoint, API version, auth, pagination, limits, rate limits, source terms, and outage behavior are reviewed;
- rights and sensitivity reviewers approve the test posture;
- credentials are supplied through an approved secret mechanism;
- request, page, record, byte, retry, timeout, and total-work limits are explicit;
- safe logging and source-run receipt behavior are implemented;
- the test is separately marked and excluded by default;
- a steward explicitly enables the run;
- rollback and disablement are documented.

Live tests must:

- use the smallest possible non-sensitive query;
- never auto-refresh committed fixtures;
- never commit source payloads or credentials;
- record finite outcomes, source state, and rate-limit evidence;
- produce no public artifact;
- leave ordinary unit-test success independent of source availability;
- be disabled immediately if rights, sensitivity, endpoint behavior, or source terms become unclear.

No live test flag, marker, endpoint, credential source, or workflow is ratified here.

[Back to top ↑](#top)

---

## Execution CI and evidence contract

### Local command

The exact local command remains **NEEDS VERIFICATION** because the parent `pyproject.toml` has no verified build backend, dependencies, package discovery, or test configuration.

A future accepted command might resemble:

```bash
python -m pytest connectors/inaturalist/tests
```

This is illustrative only.

### Required CI behavior

When executable tests exist, CI should:

- install the package into an isolated environment using the accepted package configuration;
- run import-safety tests before connector behavior tests;
- block live network through sandboxing or a fail-fast socket guard;
- run synthetic fixture and negative cases;
- run descriptor/activation/product, rights, taxonomy, geoprivacy, sensitivity, replay, handoff, receipt, logging, and boundary tests;
- fail if test collection is empty when the workflow claims connector coverage;
- publish ordinary machine-readable test reports;
- report skipped live-source tests explicitly;
- avoid uploading sensitive fixture contents or logs;
- distinguish substantive tests from placeholder `echo TODO` steps;
- pin the commit, package version, test command, environment, and result;
- avoid treating green tests as merge approval or KFM publication.

### Evidence language

A valid status statement should say:

```text
CONFIRMED at <commit>: <command> collected N tests and completed with <result>.
The suite covers <named assertions>. Live-source tests were <skipped/not configured>.
This does not establish source activation, rights approval, public precision, release,
or runtime behavior outside the tested environment.
```

Do not say “the connector is working” merely because repository-level `make test` or a placeholder connector workflow is green.

### Test result artifacts

- JUnit, coverage, or boundary reports are build/test artifacts.
- A source-run receipt is a governed process record for a source interaction.
- A generated AI-authorship receipt records documentation/code generation.
- None of these is an EvidenceBundle, proof closure, review approval, release manifest, or public citation.

[Back to top ↑](#top)

---

## Implementation sequence

Use one coherent capability per pull request.

| Step | Smallest useful change | Required proof | Rollback |
|---|---|---|---|
| 0 | Inventory the package/test tree and resolve or isolate local `descriptor.yaml`. | Commit-pinned inventory, migration/decision record, test proving no auto-load. | Restore prior placeholder; keep network disabled. |
| 1 | Complete package metadata and add import-side-effect tests only. | Build/install/import report; no-network and no-secret assertions. | Revert packaging and import-test commit. |
| 2 | Add immutable outcome/reason types and deterministic query canonicalization tests. | Unit tests and digest fixtures. | Revert pure-core files and fixtures. |
| 3 | Add parser with synthetic observation fixtures. | Field-preservation, malformed-input, unknown-value, and no-sensitive-log tests. | Revert parser and fixtures. |
| 4 | Add pure validation and admission assembly using supplied decisions. | Product, grade, rights, taxonomy, geoprivacy, sensitivity, mixed-batch, and negative tests. | Revert validation/admission modules. |
| 5 | Add candidate and receipt builders with in-memory sinks. | Candidate-only default, idempotency, no-op, integrity, boundary, and failure tests. | Revert handoff/receipt modules. |
| 6 | Add injected fake transport and bounded fetch mechanics. | Timeout, retry, rate-limit, pagination, partial-response, cursor-loop, and schema-drift tests. | Revert transport adapter. |
| 7 | Add correction, deletion, withdrawal, and replay tests. | Prior-lineage, changed-source-state, and no-op behavior. | Revert replay/correction capability. |
| 8 | Consider a separately activated live-source probe. | Current source review, descriptor/activation, rights/sensitivity approval, bounded run, receipt, safe logs, disable switch. | Disable workflow/flag and revert live adapter. |
| 9 | Add product-specific tests only after module/layout decision. | Accepted product ID/version, module decision, migration note if needed, test coverage. | Revert product module/tests without changing family authority. |

Do not pre-create empty test modules or fixtures for later steps. Empty scaffolds make maturity look deeper than it is.

[Back to top ↑](#top)

---

## Definition of done

### This documentation revision

- [x] Target, base commit, prior blob, and prior history are pinned.
- [x] Current package metadata, placeholder modules, unsafe local descriptor, and v0.2 adjacent contracts are recorded.
- [x] Common test paths and the indexed `test_inaturalist` search are reported with bounded absence language.
- [x] Stale “previously blank” and unresolved rollback-SHA language is removed.
- [x] Test authority is separated from source, product, descriptor, policy, schema, proof, catalog, release, and public-client authority.
- [x] No-network, import safety, product routing, rights, taxonomy, geoprivacy, sensitivity, replay, finite outcome, handoff, receipt, logging, fixture, CI, and rollback contracts are defined.
- [x] RAW, QUARANTINE, and process-memory receipt test support is reconciled with package and connector doctrine.
- [x] Test names, files, fixture metadata, commands, markers, and interfaces are visibly PROPOSED rather than represented as implemented.
- [x] No executable test, fixture payload, endpoint, credential, source interaction, or public artifact is created.

### Executable test lane

- [ ] Owners and reviewers are assigned.
- [ ] Complete recursive package and repository-wide test/import inventory is recorded.
- [ ] `descriptor.yaml` is removed, migrated, or formally classified and cannot activate access.
- [ ] SourceDescriptor schema and registry-path conflicts are resolved.
- [ ] Stable source-family and product IDs/versions are accepted.
- [ ] Build backend, package discovery, Python versions, dependencies, install command, test framework, and markers are accepted.
- [ ] Import-side-effect tests exist and pass.
- [ ] Deterministic query, parser, validation, admission, finite outcome, handoff, receipt, and replay tests exist.
- [ ] Product routing covers research-grade and non-research-grade cases.
- [ ] Rights, attribution, taxonomy, quality, geoprivacy, sensitivity, time, geometry, integrity, and mixed-batch negative cases fail closed.
- [ ] Synthetic fixture corpus is reviewed, safe, minimized, and documented.
- [ ] Fake transport covers success and bounded failure conditions.
- [ ] Fake sinks prove candidate-only default and RAW/QUARANTINE/receipt-only boundaries.
- [ ] Logging and CI artifacts exclude sensitive/private material.
- [ ] CI collects substantive tests and reports the exact command, count, and result.
- [ ] Live tests, if any, are separately governed, disabled by default, bounded, receipt-bearing, and reversible.
- [ ] Public applications are proven unable to use connector internals or unreleased source material directly.

[Back to top ↑](#top)

---

## Verification backlog

| Item | Status | Evidence required |
|---|---:|---|
| Complete recursive inventory under `connectors/inaturalist/tests/` and repository-wide iNaturalist test/import search. | **NEEDS VERIFICATION** | Current tree, code search, import graph, and test collection. |
| Confirm whether differently named or unindexed executable tests exist. | **UNKNOWN** | Recursive tree and local/CI collection report. |
| Confirm package build backend, discovery, Python versions, dependencies, install command, and test framework. | **NEEDS VERIFICATION** | Accepted `pyproject.toml`, build logs, isolated install, import test. |
| Confirm test authority split between connector-local, root `tests/`, fixtures, policy, schema, release, and end-to-end suites. | **NEEDS VERIFICATION / ADR-class if authority moves** | Directory review, ADR/migration note, imports, workflows. |
| Resolve connector-local `descriptor.yaml` disposition. | **CONFLICTED / high priority** | Registry decision, migration/deletion/classification, negative auto-load test. |
| Resolve singular/plural SourceDescriptor schema paths and substantive validation. | **CONFLICTED** | Accepted schema/ADR, fixtures, validator, migration. |
| Reconcile fauna-scoped registry template with current source-registry doctrine. | **NEEDS VERIFICATION / drift** | Registry inventory, accepted descriptor, validator output. |
| Confirm stable source-family and observation-product IDs, versions, and aliases. | **NEEDS VERIFICATION** | Source catalog/registry decision. |
| Resolve non-research-grade product `OPEN-INAT-01`. | **OPEN** | Source, Fauna, and Flora steward decision; accepted product contract. |
| Resolve taxonomy tie-breaking `OPEN-INAT-02`. | **OPEN** | Biodiversity/taxonomy decision and deterministic fixtures/tests. |
| Resolve captive/cultivated and other quality-flag dispositions. | **NEEDS VERIFICATION** | Product contract and test cases. |
| Verify current endpoint, API version, auth, query, pagination, limits, rate limits, cadence, source terms, outage, deletion, and correction behavior. | **NEEDS VERIFICATION** | Current official-source review and bounded governed tests. |
| Verify observation and media rights, attribution, caching, redistribution, training, revocation, and withdrawal. | **NEEDS VERIFICATION** | Rights review, source terms, fixtures, policy tests. |
| Confirm geoprivacy states, sensitive-taxa/site inputs, join-induced sensitivity, public precision, and media-location handling. | **NEEDS VERIFICATION** | Policy bundles, redaction contracts, fixtures, tests. |
| Confirm request/response digest, replay reference/storage, no-op identity, record deletion, and withdrawal contracts. | **NEEDS VERIFICATION** | Receipt/replay contracts and integration tests. |
| Confirm RAW, QUARANTINE, and process-memory receipt interfaces and sink ownership. | **NEEDS VERIFICATION** | Contracts, schemas, adapters, idempotency tests. |
| Confirm substantive connector CI rather than placeholder workflow steps. | **UNKNOWN** | Workflow definitions, job steps, test counts, logs, artifacts. |
| Confirm no public API/UI, map, tile, report, search, graph, vector index, or AI imports connector internals or reads unreleased observations. | **NEEDS VERIFICATION** | App/import graph, access policy, boundary tests, runtime evidence. |
| Reconcile parent and source-root README inventories and older receipt-store exclusions. | **NEEDS VERIFICATION / drift** | Focused documentation follow-up and link validation. |

[Back to top ↑](#top)

---

## Review and rollback

Before merge, rollback means closing the draft pull request and abandoning its scoped branch.

After merge, transparently revert the commit introducing this v0.2 test contract and its paired generated receipt, then rerun applicable documentation, package/import, connector, descriptor, schema, rights, taxonomy, geoprivacy, sensitivity, validation, receipt, lifecycle-boundary, citation, correction, and rollback checks. Do not rewrite shared history.

Concrete prior-state target: v0.1 blob `5ec771892cd8e740a1fa862cc97828553fd983a6` at base commit `e7e3b18024f9eba9551ccc9627db8a4064961edc`.

Rollback or correction is required if this README is used to justify:

- claiming executable tests, fixtures, package installation, import success, connector behavior, live access, or CI coverage without evidence;
- auto-loading the connector-local descriptor or treating `sensitivity_floor: public` as authority;
- making ordinary tests require network, credentials, source availability, or fixture refresh;
- introducing real sensitive coordinates, observer-private data, media bytes, credentials, or secret-bearing logs;
- silently upgrading casual/non-research-grade observations;
- treating research-grade as KFM truth, canonical taxonomy, legal status, species presence, or public-release approval;
- collapsing observation rights and media rights;
- deobscuring or inferring exact coordinates;
- allowing unbounded retries, pagination, source scope, or test work;
- writing beyond explicit temporary RAW, QUARANTINE, or receipt test interfaces;
- treating test reports or receipt candidates as EvidenceBundle, proof, review, catalog, promotion, release, or publication closure;
- allowing public applications, maps, search, graphs, indexes, or AI to use connector internals or unreleased material directly.

Required reviewers are **NEEDS VERIFICATION** because current CODEOWNERS coverage for this path has not been established as role-specific. At minimum, review should cover connector/source ownership, Python packaging/testing, Fauna or Flora semantics, biodiversity/taxonomy, rights, sensitivity/geoprivacy, validation, and documentation.

---

## Maintainer note

Build the suite in the same order as the package: import safety and authority gates first, pure deterministic mechanics next, synthetic parsing and admission after that, fake handoff/receipt and replay later, and live access last—if it is ever justified.

A connector test lane is credible when it makes failure, uncertainty, source role, product identity, rights, taxonomy, geoprivacy, sensitivity, lineage, and lifecycle boundaries more visible. It is not credible when a green check merely proves that a placeholder command ran.

<p align="right"><a href="#top">Back to top</a></p>
