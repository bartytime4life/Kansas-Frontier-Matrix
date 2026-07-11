<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-census-tests-readme
title: connectors/census/tests/ — Census Connector Tests
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Census source steward · QA steward · Data steward · Docs steward
created: 2026-07-10
updated: 2026-07-10
policy_label: public; tests; offline-first; source-admission-only
related:
  - ../README.md
  - ../src/README.md
  - ../src/census/README.md
  - ../../../connectors/README.md
  - ../../../tests/README.md
  - ../../../docs/sources/catalog/census/README.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../artifacts/
tags: [kfm, connectors, census, tests, fixtures, validation, vintage, uncertainty, geography, source-admission, governance]
notes:
  - "This lane validates Census connector behavior; it does not activate sources, admit records, publish artifacts, or prove release readiness."
  - "Tests should be offline-first and deterministic, using small non-sensitive fixtures where practical."
  - "Census product families must remain distinct: Decennial counts, ACS estimates, TIGER/Line geography, microdata, historical compilations, and crosswalks are not interchangeable."
  - "Current test modules, fixture inventory, commands, coverage, CI execution, and pass state remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Census Connector Tests

> Offline-first tests for Census source-admission behavior. This lane increases confidence in connector code; it does not establish source authority, lifecycle promotion, evidence closure, or release readiness.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: connector tests" src="https://img.shields.io/badge/scope-connector__tests-blue">
  <img alt="Network: offline first" src="https://img.shields.io/badge/network-offline--first-green">
  <img alt="Truth posture: test evidence only" src="https://img.shields.io/badge/truth-test__evidence__only-orange">
</p>

`connectors/census/tests/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted tests](#accepted-tests) · [Exclusions](#exclusions) · [Required test matrix](#required-test-matrix) · [Fixture posture](#fixture-posture) · [Live-service tests](#live-service-tests) · [Validation](#validation) · [Evidence limits](#evidence-limits) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/census/tests/`  
> **Responsibility:** Census connector-scoped tests and test documentation  
> **Truth posture:** the path and README are `CONFIRMED`; actual test modules, fixtures, commands, coverage, CI wiring, pass state, and live-integration behavior remain `NEEDS VERIFICATION`.

---

## Scope

Use this directory for tests that exercise Census connector behavior at the source-admission boundary.

Tests here should verify that connector code:

- imports without network, filesystem, credential, or activation side effects;
- requires explicit SourceDescriptor and runtime configuration inputs;
- preserves product family, vintage, geography, universe, aggregation, uncertainty, annotations, and suppression states;
- enforces raw, quarantine, and receipt-only handoffs;
- returns finite safe outcomes for failures and unresolved assumptions;
- does not imply processed, catalog, triplet, proof, release, API, UI, or publication behavior.

A passing connector test does not prove that a Census product is active, current, complete, rights-cleared, policy-approved, or safe for public release.

---

## Repo fit

```text
connectors/census/
├── README.md
├── src/
│   ├── README.md
│   └── census/
│       └── README.md
└── tests/
    └── README.md
```

Adjacent responsibility roots:

| Root | Relationship |
|---|---|
| `connectors/census/src/` | Implementation under test. |
| `data/registry/sources/` | SourceDescriptor and activation authority. Tests may reference validated fixtures, not replace registry authority. |
| `fixtures/` | Preferred home for reusable test fixtures. |
| `tests/` | Canonical cross-system enforceability and trust-spine tests. |
| `artifacts/` | Generated reports, coverage output, and QA summaries. |
| `release/` | Release and rollback authority; connector tests do not own it. |

---

## Accepted tests

| Test family | What it should verify |
|---|---|
| Import-safety tests | Import performs no network calls, writes, credential reads, or source activation. |
| Descriptor-gating tests | Missing, inactive, or incompatible SourceDescriptor/config inputs fail closed. |
| Request-builder tests | Dataset, vintage, geography, variable, pagination, and key parameters are explicit and testable. |
| Parser tests | Source fields, annotations, nulls, suppression states, and metadata are preserved. |
| Geography tests | Geography codes and vintages remain explicit; no implicit cross-vintage identity is created. |
| Uncertainty tests | ACS margins of error and related uncertainty fields remain attached to their estimates. |
| Product-family tests | Decennial, ACS, TIGER/Line, microdata, historical compilations, and crosswalks remain distinct. |
| Digest tests | Identical fixture bytes produce stable digests; changed bytes change digests. |
| Handoff tests | Outputs are limited to explicit raw, quarantine, and receipt targets. |
| Failure-mode tests | Denied, skipped, no-op, rate-limited, stale, malformed, and error outcomes are finite and reason-coded. |
| Logging tests | Credentials, API keys, personal data, restricted microdata, and full sensitive payloads are not logged. |

---

## Exclusions

| Does not belong here | Correct home |
|---|---|
| Production connector implementation | `connectors/census/src/census/` |
| SourceDescriptor records and activation decisions | `data/registry/sources/` |
| Raw, quarantine, processed, catalog, triplet, published, receipt, or proof records | owning `data/` lifecycle roots |
| Rights, privacy, or publication policy | `policy/` |
| Machine schemas and object contracts | `schemas/` and `contracts/` |
| Release decisions and rollback state | `release/` |
| Reusable fixture authority | accepted `fixtures/` roots |
| Generated coverage and QA reports | `artifacts/` |
| End-to-end trust-spine proof | canonical `tests/` suites |

---

## Required test matrix

### Import and configuration

- [ ] Package import is side-effect-free.
- [ ] Network clients require explicit runtime construction.
- [ ] API keys and credentials are not read during import.
- [ ] Missing SourceDescriptor input returns a safe failure.
- [ ] Inactive or incompatible descriptors are rejected.

### Product-family separation

- [ ] Decennial counts are treated as aggregate counts.
- [ ] ACS values are treated as estimates and keep margins of error where supplied.
- [ ] TIGER/Line data remains administrative geography, not demographic truth.
- [ ] Microdata is not collapsed into aggregate products.
- [ ] Historical compilations retain compilation provenance and caveats.
- [ ] Crosswalks remain mappings, not proof of identity across vintages.

### Time, geography, and uncertainty

- [ ] Dataset vintage is explicit.
- [ ] Geography type and code are explicit.
- [ ] Universe and aggregation unit are preserved.
- [ ] Estimate, count, margin-of-error, annotation, null, and suppression states remain distinct.
- [ ] Cross-vintage joins require an explicit mapping or fail closed.
- [ ] Retrieval time and source time are preserved where available.

### Lifecycle boundary

- [ ] Connector helpers cannot write directly to processed, catalog, triplet, proof, published, or release surfaces.
- [ ] Raw and quarantine destinations must be explicit.
- [ ] Receipt payloads identify run outcome and reason code.
- [ ] Test success never implies source activation or publication approval.

### Safe outcomes

Tests should cover, where supported:

```text
admit_candidate
quarantine
needs_review
deny
skip
no_op
rate_limited
stale
malformed
error
```

Outcome vocabulary must match accepted contracts when those contracts are verified. Until then, exact enum names remain `NEEDS VERIFICATION`.

---

## Fixture posture

Prefer small, deterministic, no-network fixtures.

Fixtures should:

- contain only the minimum fields needed for the test;
- avoid real API keys, restricted microdata, living-person detail, or sensitive records;
- retain the Census product family and vintage needed to test semantics;
- include edge cases for annotations, suppressed values, nulls, missing fields, and invalid geography combinations;
- be stored in the accepted fixture root when reusable;
- carry a short provenance note and synthetic/redacted status.

> [!CAUTION]
> Publicly available source material is not automatically suitable as a committed fixture. Review privacy, rights, size, sensitivity, and repository-retention implications before adding it.

---

## Live-service tests

Live Census endpoint tests, if they exist, must be opt-in and separated from default offline tests.

They should:

- require explicit environment configuration;
- never expose API keys or credentials in logs;
- use bounded requests and conservative pagination;
- honor rate limits and service terms;
- produce no lifecycle promotion or publication side effects;
- record failures as test evidence, not as source truth;
- remain excluded from CI unless explicitly governed and documented.

Current live-test availability is `UNKNOWN`.

---

## Validation

Before relying on this test lane, verify:

- [ ] Actual test files are inventoried.
- [ ] Test runner and commands are documented.
- [ ] Package import paths are verified.
- [ ] Fixture paths and provenance notes are current.
- [ ] SourceDescriptor and schema references resolve.
- [ ] Offline tests cover import, parsing, vintage, geography, uncertainty, and failure outcomes.
- [ ] Sensitive or restricted material is absent from fixtures and logs.
- [ ] CI runs the intended test set or explicitly marks it manual.
- [ ] Generated reports land under `artifacts/` or another accepted report root.
- [ ] Canonical `tests/` suites cover any required cross-system trust-spine behavior.

---

## Evidence limits

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| `connectors/census/tests/README.md` | `CONFIRMED` | Test-lane contract and intended boundaries | Actual test coverage or passing status |
| `connectors/census/src/README.md` | `CONFIRMED` | Source-root boundary | Installability or runtime correctness |
| `connectors/census/src/census/README.md` | `CONFIRMED` | Package-level contract | Implemented modules or endpoint behavior |
| `connectors/census/README.md` | `CONFIRMED` | Parent source-family admission posture | Source activation or release readiness |
| Test modules, fixtures, CI logs | `NEEDS VERIFICATION` | Implementation evidence when inspected | Nothing until directly verified |

---

## Rollback

Rollback is required if this README is used to justify:

- source activation or admission authority;
- live-network dependency in default tests;
- use of restricted or sensitive fixture data;
- direct lifecycle writes or release decisions;
- collapse of Census product families, vintages, geographies, or uncertainty fields;
- claims of CI success, coverage, or release readiness without evidence.

Rollback target: prior greenfield stub blob `32183eedc5f76f7dcf00a99e58401de196564829`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual tests are inventoried.
- [ ] Test commands and dependency setup are documented.
- [ ] Imports are verified side-effect-free.
- [ ] SourceDescriptor/config gating is tested.
- [ ] Product-family, vintage, geography, universe, and uncertainty distinctions are tested.
- [ ] Raw/quarantine/receipt-only boundaries are tested.
- [ ] Safe finite outcomes and reason codes are tested.
- [ ] Fixtures are offline, reviewable, non-sensitive, and provenance-labeled.
- [ ] No production, registry, policy, schema, lifecycle, proof, release, or report authority lives here.
- [ ] CI execution and current pass state are verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/census/tests/` is the offline-first test lane for Census connector behavior. It supports validation of source-admission code but is not source authority, fixture authority, lifecycle authority, proof closure, release authority, or a substitute for canonical cross-system tests.

<p align="right"><a href="#top">Back to top</a></p>
