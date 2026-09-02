<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-memory-tests-readme
title: connectors/kansas_memory/tests/ — Kansas Memory Compatibility Connector Test Contract
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Archives steward · Rights reviewer · Sensitivity/privacy reviewer · CARE/cultural/sovereignty reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-12
policy_label: public-doctrine; test-contract; noncanonical-compatibility-lane; no-executable-tests-confirmed; no-network-default; synthetic-fixtures; rights-fail-closed; sensitivity-fail-closed; care-review; raw-quarantine-receipt-boundary; no-activation; no-publication
current_path: connectors/kansas_memory/tests/README.md
truth_posture: CONFIRMED README-only test lane and placeholder package / PROPOSED suite layout, fixtures, test APIs, outcomes, and implementation sequence / CONFLICTED package placement and SourceDescriptor authority / UNKNOWN executable coverage, runner, CI enforcement, source activation, and runtime behavior
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: adc74eaee2ba5c94844814acdf197f4f0149fb77
  prior_blob: be8c7dd3a918abfe43682126a30e324db77d5297
related:
  - ../../README.md
  - ../README.md
  - ../src/README.md
  - ../src/kansas_memory/README.md
  - ../pyproject.toml
  - ../../kansas/README.md
  - ../../../tests/README.md
  - ../../../fixtures/README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/kansas/kansas-memory.md
  - ../../../docs/sources/catalog/kansas_memory.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../data/raw/archives/
  - ../../../data/quarantine/archives/
  - ../../../data/receipts/
  - ../../../release/
tags: [kfm, connectors, kansas-memory, tests, python, archives, compatibility, placeholder, no-network, synthetic-fixtures, rights, sensitivity, care, privacy, raw, quarantine, receipts, fail-closed, governance]
notes:
  - "At the pinned base, this tests directory contains README.md; direct probes for test_admit.py, test_fetch.py, conftest.py, __init__.py, and fixtures/README.md returned Not Found."
  - "Indexed repository search found no Kansas Memory test implementation or workflow-specific wiring. These are bounded observations, not proof that no differently named or unindexed test exists."
  - "The adjacent package remains version 0.0.0 with an empty initializer, one-line admit.py and fetch.py placeholders, and a four-field descriptor.yaml placeholder."
  - "The package-local descriptor is not test authority or source authority. Its role and rights are unresolved, and its public sensitivity floor must fail closed."
  - "This revision defines a proposed test boundary only. It creates no executable test, fixture payload, endpoint selection, credential, source activation, policy decision, receipt, release object, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Memory Compatibility Connector Test Contract

> [!IMPORTANT]
> **Document lifecycle:** `draft`  
> **Component maturity:** README-only test scaffold; executable coverage `UNKNOWN`  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** `CONFIRMED` current README-only lane and package placeholders · `PROPOSED` suite design and outcomes · `CONFLICTED` package placement and descriptor authority  
> **Boundary:** connector-local tests may prove source-admission mechanics only. They do not activate Kansas Memory, decide source role or rights, approve sensitive archive material, establish historical truth, close evidence, authorize release, or publish content.

> [!WARNING]
> No runnable Kansas Memory test suite was confirmed. This document is a test contract, not evidence that tests exist, collect, pass, run in CI, or enforce the stated controls.

**Quick links:** [Purpose](#purpose) · [Current state](#current-repository-state) · [Authority](#test-authority-and-placement) · [Principles](#test-principles) · [Suite layout](#proposed-suite-layout) · [Fixtures](#fixture-contract) · [Import safety](#import-and-package-safety) · [Descriptor gates](#descriptor-and-activation-tests) · [Fetch](#fetch-and-transport-tests) · [Parsing](#parsing-and-preservation-tests) · [Admission](#admission-and-finite-outcome-tests) · [Rights and sensitivity](#rights-sensitivity-privacy-and-care-tests) · [Lifecycle](#lifecycle-side-effect-and-publication-boundaries) · [Security](#security-and-logging-tests) · [Migration](#compatibility-and-migration-tests) · [Running tests](#running-tests) · [Matrix](#validation-matrix) · [Definition of done](#definition-of-done) · [Evidence](#evidence-basis) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

<a id="scope"></a>

## Purpose

`connectors/kansas_memory/tests/` is the connector-local test lane for the repository-present `kansas_memory` compatibility package.

Its future responsibility is narrow: prove that package imports, parsing, admission, failure handling, and caller-owned handoff candidates remain deterministic, no-network by default, source-faithful, rights-aware, sensitivity-aware, and bounded to the connector edge.

This directory is not the canonical repository-wide test root, fixture authority, source registry, schema or contract home, policy engine, proof store, release test authority, public-output suite, or publication surface.

The current bytes prove only that this README exists. They do not prove an executable suite, a test runner, fixture safety, package installability, coverage, CI wiring, source activation, or live-source behavior.

[Back to top](#top)

---

## Current repository state

The following snapshot is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `adc74eaee2ba5c94844814acdf197f4f0149fb77`.

```text
connectors/kansas_memory/
├── pyproject.toml                         # project name + version 0.0.0 only
├── src/
│   ├── README.md                          # v0.2 source-layout boundary
│   └── kansas_memory/
│       ├── README.md                      # v0.2 package admission boundary
│       ├── __init__.py                    # empty
│       ├── admit.py                       # one-line greenfield placeholder
│       ├── fetch.py                       # one-line greenfield placeholder
│       └── descriptor.yaml                # unresolved local placeholder
└── tests/
    └── README.md                          # this file; confirmed current inventory
```

Direct probes returned `Not Found` for:

- `tests/test_admit.py`;
- `tests/test_fetch.py`;
- `tests/conftest.py`;
- `tests/__init__.py`;
- `tests/fixtures/README.md`.

Indexed search found no Kansas Memory test implementation or workflow-specific reference. These observations are path- and index-bounded; they do not prove that no differently named or unindexed file exists.

| Surface | Current status | What it does not prove |
|---|---:|---|
| This README | **CONFIRMED / v0.1 baseline** | Test execution or enforcement. |
| Test code | **NOT FOUND AT PROBED PATHS** | Absence of every possible differently named test. |
| Local fixtures | **NOT FOUND AT PROBED PATH** | A final fixture-home decision or absence of every shared fixture. |
| Package code | **GREENFIELD PLACEHOLDERS** | Callable interfaces or behavior to test. |
| Package metadata | **VERSION 0.0.0 PLACEHOLDER** | Build backend, dependencies, test extras, supported Python version, or runner. |
| Local descriptor | **UNSAFE PLACEHOLDER** | Descriptor validity, role, rights, sensitivity, activation, or release authority. |
| CI wiring | **UNKNOWN** | No package-specific workflow reference was found; generic repository checks do not prove suite collection. |
| Live source testing | **NOT AUTHORIZED / NOT VERIFIED** | Endpoint safety, terms, credentials, cadence, or source status. |

[Back to top](#top)

---

<a id="repo-fit"></a>

## Test authority and placement

Directory Rules distinguish the canonical repository-wide `tests/` root from connector-local tests.

| Concern | Owning surface | Kansas Memory test-lane role |
|---|---|---|
| Repository-wide test authority | [`../../../tests/`](../../../tests/README.md) | Cross-connector, contract, schema, policy, trust-spine, release, correction, rollback, and runtime-proof suites. |
| Shared operational and synthetic fixtures | [`../../../fixtures/`](../../../fixtures/README.md) | Reusable reviewed fixtures; not source evidence or release data. |
| Connector implementation | [`../src/`](../src/README.md) | Package mechanics under test; currently placeholders. |
| Connector-local tests | `connectors/kansas_memory/tests/` | Narrow import, parser, admission, transport-fake, failure, and compatibility tests. |
| Source identity and activation | Source registry and control-plane surfaces | Test inputs and fakes only; never decided by tests. |
| Contracts and schemas | `contracts/` and `schemas/` | Imported or validated authority; not duplicated here. |
| Rights and sensitivity policy | `policy/rights/` and `policy/sensitivity/` | Exercised through fakes/fixtures; not redefined here. |
| Process memory | `data/receipts/` | Receipt candidates may be asserted in memory; tests do not mint production receipts. |
| Release and publication | `release/` and governed delivery surfaces | Outside this lane; only negative boundary assertions belong here. |

The current top-level underscore package remains a noncanonical compatibility lane. This test contract does not ratify it, create the proposed `connectors/kansas/kansas-memory/` child, or decide where eventual tests should migrate.

[Back to top](#top)

---

## Test principles

Future tests must follow these rules:

1. **No network by default.** Unit and default integration tests use supplied bytes, fakes, or reviewed fixtures.
2. **No hidden side effects.** Import and test collection must not write files, register sources, read credentials, contact hosts, activate jobs, or mutate global state.
3. **Fail closed.** Missing, unresolved, conflicted, malformed, stale, or unsafe inputs produce finite deny, abstain, quarantine, or error outcomes.
4. **Preserve source meaning.** Archive metadata, digitized representations, OCR, transcription, entity matches, and generated summaries remain distinct.
5. **Preserve identity and time.** Source, collection, item, component, page, scan, file, retrieval, observation, correction, and supersession identities stay explicit where applicable.
6. **Keep outputs caller-owned.** Tests may assert in-memory `RAW`, `QUARANTINE`, or receipt candidates, never production writes.
7. **Treat sensitive material as hostile by default.** Living-person, cultural, sovereignty, CARE, archaeological, private-land, precise-location, and rights-restricted cases require negative fixtures and fail-closed expectations.
8. **Separate mechanics from authority.** A passing parser test does not validate source role, rights, sensitivity, activation, evidence closure, historical interpretation, or release.
9. **Make replay deterministic.** The same inputs and configuration produce the same identity, outcome, reason code, and candidate bytes where contracts require determinism.
10. **Keep evidence bounded.** Test success proves only the assertions exercised by that test and environment.

[Back to top](#top)

---

## Proposed suite layout

The following layout is **PROPOSED**. It does not exist at the pinned base and must not be created from this README alone.

```text
connectors/kansas_memory/tests/
├── README.md
├── conftest.py
├── test_import.py
├── test_descriptor.py
├── test_fetch.py
├── test_parse.py
├── test_admit.py
├── test_rights_sensitivity.py
├── test_lifecycle_boundary.py
├── test_security.py
├── test_replay.py
├── test_compatibility.py
└── fixtures/
    ├── README.md
    ├── valid/
    ├── invalid/
    └── expected/
```

Before adopting this layout, maintainers must verify the repository's runner, naming, fixture-home, package-discovery, marker, and CI conventions. A smaller accepted layout is preferable when it proves the same boundaries.

[Back to top](#top)

---

## Fixture contract

### Allowed fixture classes

Fixtures may be:

- synthetic shape-only records with conspicuous non-production identifiers;
- minimal public-domain samples whose reuse and repository redistribution were explicitly reviewed;
- redacted or generalized metadata approved for test use;
- fake transport responses that contain no real credential, cookie, token, session, or restricted endpoint;
- malformed and adversarial records designed to prove fail-closed behavior;
- deterministic expected-output objects that cannot be mistaken for production receipts or released archive records.

### Required fixture metadata

Each accepted fixture class should document:

- fixture ID and purpose;
- synthetic, reviewed-public, redacted, or generated classification;
- source and collection identity policy;
- rights and redistribution basis;
- sensitivity, privacy, cultural, sovereignty, CARE, archaeology, private-land, and precise-location review posture;
- creation or retrieval date where relevant;
- expected parser and admission outcome;
- allowed repository visibility;
- reviewer and expiration or re-review trigger when required.

### Forbidden fixture content

Do not commit:

- bulk source harvests or media collections;
- living-person personal data or genealogy-adjacent identity assertions;
- exact archaeological, sacred, culturally sensitive, burial, ecological, private-property, or security-relevant locations;
- unclear-rights, no-redistribution, licensed-only, embargoed, or access-controlled material;
- credentials, keys, cookies, authorization headers, signed URLs, session captures, or private endpoints;
- real production receipts, activation decisions, EvidenceBundles, review approvals, release manifests, or correction records;
- OCR, transcription, entity links, or generated text presented as verified source truth.

The shared [`fixtures/`](../../../fixtures/README.md) root is not automatically the Kansas Memory fixture home. Placement remains `NEEDS VERIFICATION` and must avoid parallel fixture authority.

[Back to top](#top)

---

## Import and package safety

Future import and packaging tests should prove:

- package import is deterministic and performs no network request;
- import performs no file write, environment mutation, source registration, activation, logging setup, thread start, or background job scheduling;
- import does not read credentials or secrets;
- placeholder configuration is not accepted as a valid descriptor;
- missing optional runtime configuration does not cause unsafe fallback;
- package metadata, supported Python versions, dependencies, entry points, and test extras match an accepted build contract;
- installed and source-tree imports resolve the same public API where intended;
- package version and compatibility warnings are explicit.

Current state: the initializer is empty and no build backend or dependency configuration was verified. That is evidence of a scaffold, not import safety.

[Back to top](#top)

---

## Descriptor and activation tests

The package-local `descriptor.yaml` contains unresolved `role` and `rights` fields plus `sensitivity_floor: public`. Tests must treat it as an invalid authority input.

Required future cases:

| Case | Expected outcome |
|---|---|
| Governed descriptor reference missing | `DENY` or `ABSTAIN`; no network. |
| Activation decision missing or inactive | `DENY`; no network. |
| Descriptor cannot validate against accepted schema | `ERROR` or `QUARANTINE`; no source use. |
| Descriptor role unresolved | `QUARANTINE` or `DENY`. |
| Rights unresolved | `QUARANTINE` or `DENY`. |
| Sensitivity defaults to public without policy approval | `DENY`; never silently accept. |
| Descriptor source ID and requested source disagree | `DENY` or `ERROR`. |
| Descriptor or activation is stale, superseded, corrected, or withdrawn | Fail closed with explicit lineage-aware outcome. |
| Valid reviewed descriptor and active decision | Permit the next bounded test stage only; do not imply release. |

Tests must import accepted contracts and schemas rather than copying their fields or enums into connector-local authority.

[Back to top](#top)

---

## Fetch and transport tests

No fetch implementation was confirmed. Future tests must use a fake transport by default and prove:

- zero network calls without explicit reviewed opt-in;
- no ambient credential discovery;
- allowed host, scheme, path, redirect, and response-size boundaries;
- timeout, retry, backoff, rate-limit, cancellation, and retry-after handling;
- response status, content type, encoding, byte limit, digest, source head, and retrieval time preservation;
- safe rejection of redirects to private, local, metadata-service, or unapproved hosts;
- safe handling of malformed, compressed, truncated, oversized, or unexpected content;
- no fallback from an unavailable approved surface to an unreviewed endpoint;
- no logging of secrets, query tokens, cookies, restricted URLs, or payloads;
- deterministic fake responses for success, unchanged source, not found, denied, throttled, transient failure, permanent failure, and drift.

Live-source smoke tests, if ever approved, must be separately marked, credential-safe, rate-limited, terms-reviewed, non-mutating, excluded from default CI, and incapable of producing public or canonical artifacts.

[Back to top](#top)

---

## Parsing and preservation tests

Future parser tests should prove preservation—not truth upgrade—for source-native fields that are actually verified.

Candidate dimensions include:

- source, collection, item, component, page, scan, file, and derivative identifiers;
- source URI, retrieval time, source head, digest, content type, and encoding;
- title, creator, contributor, date, description, subject, place, collection, and rights strings as supplied;
- original field names and lossless source fragments needed for audit;
- OCR and transcription identity, method, confidence, correction, and source-image relationship;
- name and place strings before entity resolution;
- temporal ambiguity, ranges, circa values, unknown values, and transcription uncertainty;
- rights statements, attribution text, access restrictions, and sensitivity flags;
- source order and repeated values where semantically meaningful.

Required anti-collapse cases:

- metadata is not treated as a verified historical claim;
- a digitized image is not treated as the original physical object;
- OCR is not treated as a source transcription without method and confidence lineage;
- transcription is not treated as authorial text when editorial intervention occurred;
- a name string is not treated as a resolved person;
- a place string is not treated as exact geometry;
- collection-level rights are not silently applied to every item;
- generated summaries are not treated as evidence;
- missing values remain missing rather than being invented or normalized into certainty.

[Back to top](#top)

---

## Admission and finite-outcome tests

The exact runtime outcome contract remains `NEEDS VERIFICATION`. A future accepted vocabulary should be finite and testable. Illustrative outcomes include:

- `RAW_CANDIDATE`;
- `QUARANTINE`;
- `DENY`;
- `ABSTAIN`;
- `NO_OP`;
- `ERROR`.

These names are **PROPOSED**, not an authoritative enum.

Tests should cover:

| Condition | Expected class of result |
|---|---|
| Valid, reviewed, activated, new source material | Caller-owned `RAW` candidate plus receipt candidate. |
| Valid source material already seen at same source head and digest | Deterministic no-op receipt candidate. |
| Missing identity, provenance, rights, sensitivity, or activation evidence | `QUARANTINE`, `DENY`, or `ABSTAIN` as the accepted contract requires. |
| Malformed or unsupported source shape | `QUARANTINE` or `ERROR` with bounded diagnostics. |
| Ambiguous collection or item identity | `QUARANTINE`; preserve candidate evidence. |
| Unexpected source-head change or parser drift | `QUARANTINE`, drift, or correction-aware outcome; no overwrite. |
| Restricted or unsafe material | `DENY` or restricted-review outcome; no public candidate. |
| Downstream or publication output requested | Refuse with explicit boundary reason. |

Every negative result should assert stable reason codes, no unsafe side effect, and enough bounded diagnostic context for review without exposing restricted content.

[Back to top](#top)

---

## Rights sensitivity privacy and CARE tests

Required future negative-path families include:

- unknown, conflicting, expired, collection-only, or item-specific rights;
- missing attribution or redistribution terms;
- unclear AI/OCR/transcription reuse rights;
- living-person names, residences, relationships, identity assertions, or contact details;
- sacred, cultural, community-controlled, tribal, sovereignty-related, or CARE-governed material;
- archaeological, burial, historic-site, private-land, ecological, infrastructure, or other harm-relevant precise locations;
- access restrictions that prohibit repository fixtures or public derivatives;
- source-requested takedown, withdrawal, correction, embargo, or supersession;
- public-sensitivity defaults that conflict with policy or steward review.

Tests must prove that uncertainty remains visible and that unsafe cases route to deny, abstain, quarantine, redaction/generalization review, or restricted handling. A test may not approve the policy decision it exercises.

[Back to top](#top)

---

## Lifecycle side effect and publication boundaries

Connector-local tests must assert that package code does not:

- write directly to `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, release, correction, withdrawal, or public-delivery stores;
- mint production `SourceDescriptor`, `SourceActivationDecision`, `EvidenceBundle`, policy decision, review record, receipt, proof, release manifest, or rollback card objects;
- mutate canonical registries, schemas, contracts, policies, or catalogs;
- publish map layers, tiles, timelines, search indexes, APIs, summaries, or AI narratives;
- treat a Git commit, passing test, pull request, merge, or release tag as KFM publication;
- expose fixture or quarantine material through public clients.

Tests may compare in-memory candidates with reviewed expected-output fixtures. They must not write production artifacts as part of normal execution.

[Back to top](#top)

---

## Security and logging tests

Future tests should verify:

- credentials and secrets are never required for default collection;
- errors and logs redact authorization headers, cookies, tokens, signed URLs, private endpoints, and sensitive payloads;
- path traversal, unsafe archive extraction, decompression bombs, oversized inputs, and unexpected encodings fail safely;
- temporary files, if later approved, use bounded permissions and deterministic cleanup;
- network fakes prevent accidental egress;
- test isolation prevents shared state, cross-test activation, or order dependence;
- failure diagnostics do not disclose living-person, cultural, archaeological, private-land, or precise-location data;
- test output cannot be mistaken for production receipts, evidence, approval, or release state.

[Back to top](#top)

---

## Compatibility and migration tests

If the underscore package is retained while implementation moves to a Kansas-family child, tests should prove:

- one accepted implementation owns behavior;
- compatibility imports delegate explicitly and emit reviewed deprecation behavior;
- descriptor, fixture, test, and source identities do not fork;
- both paths cannot activate independently;
- no duplicate fetch, receipt, or handoff occurs;
- references and callers migrate deterministically;
- sunset criteria and removal gates are testable;
- rollback restores the prior compatible import state without history rewrite.

No migration or compatibility behavior is implemented or approved by this README.

[Back to top](#top)

---

## Running tests

No repository-supported Kansas Memory test command was verified at the pinned base.

Do not infer a command from the Python package name or assume `pytest`, package installation, dependency extras, environment variables, network markers, or working directory. Before adding a runnable command, verify:

- accepted build backend and package discovery;
- supported Python version and dependencies;
- repository-wide runner and configuration;
- connector-local versus repository-root invocation;
- fixture locations and marker names;
- network-denial enforcement;
- CI job and required-check wiring.

Until those items are confirmed, test execution remains `NOT RUN / NEEDS VERIFICATION`.

[Back to top](#top)

---

## Failure handling

Tests must fail for assertion or contract violations, not silently skip trust-bearing cases.

- Missing dependencies or runner configuration: report `BLOCKED` or `NOT RUN`; do not call the suite passing.
- Missing fixtures: fail collection or the affected case explicitly unless the accepted contract defines a reviewed skip.
- Network attempted in default tests: fail immediately.
- Schema, descriptor, rights, sensitivity, or activation uncertainty: exercise the fail-closed result; do not patch the fixture into authority.
- Flaky source behavior: isolate behind fakes; do not make default CI depend on live availability.
- Sensitive diagnostic output: redact and fail the security assertion.
- Test failure after implementation: preserve logs and bounded evidence; do not weaken the assertion to obtain green CI.

[Back to top](#top)

---

## Validation matrix

| Validation target | Required assertion | Current status |
|---|---|---:|
| README structure | One H1, logical headings, balanced fences, final newline, valid relative links. | **APPLICABLE NOW** |
| Current inventory | README-only test lane and placeholder package described accurately. | **APPLICABLE NOW** |
| Import safety | No network, writes, activation, secret access, or global side effects. | **PROPOSED / NOT RUN** |
| Descriptor rejection | Local unresolved descriptor cannot authorize use. | **PROPOSED / NOT RUN** |
| No-network default | Fake transport receives all default calls; real egress fails. | **PROPOSED / NOT RUN** |
| Parser preservation | Source-native identity, fields, ambiguity, rights, and lineage preserved. | **PROPOSED / NOT RUN** |
| Admission outcomes | Finite results, stable reasons, deterministic replay, no unsafe side effects. | **PROPOSED / NOT RUN** |
| Rights and sensitivity | Unknown or unsafe material fails closed. | **PROPOSED / NOT RUN** |
| Lifecycle boundary | No writes or authority creation beyond caller-owned candidates. | **PROPOSED / NOT RUN** |
| Security and logging | Secrets and sensitive content never leak. | **PROPOSED / NOT RUN** |
| Compatibility | No duplicate authority, activation, fetch, or handoff across paths. | **PROPOSED / NOT RUN** |
| CI collection | Accepted job collects and runs the package suite. | **UNKNOWN** |

[Back to top](#top)

---

## Definition of done

### Documentation readiness

- [x] Current base, prior blob, path, and review date are recorded.
- [x] README-only inventory and direct absent-path probes are explicit.
- [x] Package placeholders are distinguished from executable behavior.
- [x] Proposed files, commands, fixtures, outcomes, and interfaces are labeled.
- [x] No-network, no-side-effect, fail-closed, rights, sensitivity, CARE, privacy, lifecycle, and publication boundaries are explicit.
- [x] No remote badges, tracking images, credentials, source payloads, personal records, or sensitive locations are introduced.
- [x] Rollback and unresolved work are reviewable.

### Executable-suite readiness

- [ ] Final package/test placement and compatibility class are accepted.
- [ ] Package build metadata, public API, supported Python version, dependencies, and runner are implemented.
- [ ] One governed descriptor/schema/registry/validator authority is accepted.
- [ ] Product descriptor, source ID, source-head strategy, review state, and activation decision exist.
- [ ] Fixture home, fixture metadata, rights, sensitivity, review, and retention rules are accepted.
- [ ] Import, descriptor, fetch, parser, admission, rights/sensitivity, lifecycle, security, replay, and compatibility tests exist.
- [ ] Default suite proves no network and no unsafe side effects.
- [ ] Negative fixtures cover all fail-closed boundaries.
- [ ] CI collects the intended tests and exposes results without overclaiming.
- [ ] Connector-specific owners and required reviewers are assigned.

Documentation readiness does not imply executable test readiness, package readiness, source activation, evidence closure, rights approval, sensitive-data approval, or public release.

[Back to top](#top)

---

## Related folders

| Surface | Relationship | Status at the pinned base |
|---|---|---:|
| [`../../README.md`](../../README.md) | Connector-root admission and lifecycle boundary. | **CONFIRMED file** |
| [`../README.md`](../README.md) | Parent Kansas Memory compatibility lane. | **CONFIRMED / noncanonical** |
| [`../src/README.md`](../src/README.md) | Source-layout boundary. | **CONFIRMED v0.2** |
| [`../src/kansas_memory/README.md`](../src/kansas_memory/README.md) | Package admission boundary. | **CONFIRMED v0.2** |
| [`../pyproject.toml`](../pyproject.toml) | Package metadata scaffold. | **CONFIRMED version 0.0.0 placeholder** |
| [`../../../tests/README.md`](../../../tests/README.md) | Canonical repository-wide test root. | **CONFIRMED file / implementation depth separately bounded** |
| [`../../../fixtures/README.md`](../../../fixtures/README.md) | Shared operational and synthetic fixture root. | **CONFIRMED file / not automatically this lane's fixture home** |
| [`../../kansas/README.md`](../../kansas/README.md) | Kansas source-family coordination lane. | **CONFIRMED / child topology provisional** |
| `../../kansas/kansas-memory/README.md` | Source-profile-proposed child path. | **CONFIRMED exact path absent at base** |
| [`../../../docs/sources/catalog/kansas/kansas-memory.md`](../../../docs/sources/catalog/kansas/kansas-memory.md) | Current nested source profile. | **CONFIRMED draft / implementation claims bounded** |
| [`../../../docs/sources/catalog/kansas_memory.md`](../../../docs/sources/catalog/kansas_memory.md) | Older flat catalog stub. | **CONFIRMED lineage / path drift** |
| [`../../../data/registry/sources/README.md`](../../../data/registry/sources/README.md) | Governed source-registry responsibility. | **CONFIRMED README / product entry unverified** |
| [`../../../control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | Machine source-authority register. | **CONFIRMED file / entries empty** |
| [`../../../policy/rights/`](../../../policy/rights/) | Rights and reuse decisions. | **Outside tests** |
| [`../../../policy/sensitivity/`](../../../policy/sensitivity/) | Sensitivity, privacy, redaction, and CARE-adjacent controls. | **Outside tests** |
| [`../../../data/raw/archives/`](../../../data/raw/archives/) | Potential caller-owned admitted candidate surface. | **Outside tests** |
| [`../../../data/quarantine/archives/`](../../../data/quarantine/archives/) | Potential caller-owned hold surface. | **Outside tests** |
| [`../../../data/receipts/`](../../../data/receipts/) | Process-memory receipts. | **Outside tests** |
| [`../../../release/`](../../../release/) | Release, correction, withdrawal, and rollback controls. | **Outside tests** |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence basis

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Target blob `be8c7dd3a918abfe43682126a30e324db77d5297` | Exact v0.1 baseline, proposed test families, remote badges, stale inventory, and rollback placeholder. | Executable tests or CI. |
| Exact conventional test probes | Named test and local fixture paths were absent. | Absence of every differently named or unindexed file. |
| Indexed `kansas_memory`, `test_admit`, and `test_fetch` searches | No Kansas Memory test implementation or workflow-specific wiring appeared in the indexed results. | Complete recursive inventory or private/external CI. |
| Empty initializer and one-line package modules | Package remains a greenfield scaffold. | Import safety or runtime behavior. |
| Local four-field descriptor | Unresolved placeholder exists. | Governed descriptor, activation, rights, sensitivity, or release authority. |
| Parent package metadata | Project name and version `0.0.0`. | Build, dependencies, runner, entry points, or installability. |
| Source-layout and package READMEs | Current v0.2 implementation boundaries and known conflicts. | Executable behavior or accepted migration. |
| Repository-wide tests and fixture READMEs | Canonical test-root and shared-fixture responsibilities. | Kansas Memory suite implementation. |
| Source profiles, descriptor schemas, registry README, and authority register | Source meaning, schema/registry conflict, and absence of active register entries. | Product activation or safe endpoint. |
| Directory Rules, connector root, contribution guidance, and CODEOWNERS | Placement, lifecycle boundary, smallest reversible change, truth labels, and fallback ownership. | Package-specific owner or semantic approval. |

Absence claims are bounded to exact paths, indexed search, and the pinned commit. No live source, package runner, test suite, or external CI system was inspected.

[Back to top](#top)

---

## Rollback

Rollback is required if this README is used to justify live-source testing, source activation, canonical path status, unsafe fixture commits, package maturity, rights or sensitivity approval, direct downstream writes, public archive claims, or passing CI without executable evidence.

Before merge, rollback is to leave the review branch unmerged and abandon the proposed change. Closing the pull request or deleting its branch requires separate authorization.

After merge, restore prior README blob `be8c7dd3a918abfe43682126a30e324db77d5297` from base `adc74eaee2ba5c94844814acdf197f4f0149fb77` through a transparent revert commit or revert pull request, then rerun applicable documentation and connector-boundary validation. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm complete test-lane inventory. | **UNKNOWN** | Non-truncated tree walk and import/test search. |
| Resolve final package and test path plus compatibility class. | **CONFLICTED** | Accepted ADR or migration record, reference inventory, deprecation plan, tests, and rollback. |
| Reconcile underscore and hyphen slugs plus flat/nested catalog lineage. | **CONFLICTED** | Stable identity and docs migration decisions. |
| Resolve descriptor schema, registry, validator, and local-placeholder disposition. | **CONFLICTED** | Accepted contract/ADR, one enforceable schema, registry entry, validator, and migration. |
| Create and validate product descriptor and activation. | **NEEDS VERIFICATION** | Source ID, authority entry, source head, reviews, activation, and validation report. |
| Confirm package build, import, dependency, configuration, and public API. | **UNKNOWN** | Implemented metadata and observed tests. |
| Confirm runner, commands, markers, fixture paths, and CI wiring. | **UNKNOWN** | Repository configuration, workflow jobs, and collected test logs. |
| Confirm fixture rights, sensitivity, CARE, privacy, provenance, and retention. | **NEEDS VERIFICATION** | Fixture registry and review receipts. |
| Confirm current source access method, terms, cadence, and source-head behavior. | **NEEDS VERIFICATION** | Current authoritative documentation and steward review. |
| Define accepted outcomes, reasons, envelopes, receipts, retries, replay, and drift behavior. | **NEEDS VERIFICATION** | Contracts, schemas, policy, fixtures, and implementation. |
| Implement negative-path coverage for archive meaning, rights, sensitivity, privacy, CARE, security, and lifecycle boundaries. | **PROPOSED** | Reviewed fixtures, tests, and logs. |
| Assign connector, source, archive, test, rights, sensitivity, and CARE reviewers. | **UNKNOWN** | CODEOWNERS or accepted ownership records. |

[Back to top](#top)

---

## Maintainer note

Build the smallest proof-bearing suite offline first: import safety, local-placeholder rejection, one synthetic valid record, a few malformed records, explicit rights and sensitivity denials, deterministic identity preservation, and a caller-owned quarantine outcome. Add fake transport before any live-source smoke test.

Tests here should make the compatibility path safer, not more authoritative. If the implementation moves, migrate or retire this suite with explicit ownership, reference updates, deprecation tests, and a transparent rollback target.

[Back to top](#top)
