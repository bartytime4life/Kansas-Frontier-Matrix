<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-blm-tests-readme
title: connectors/blm/tests/ — BLM Connector Tests
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · QA steward · Data steward · Policy reviewer · Docs steward
created: 2026-06-16
updated: 2026-07-10
policy_label: public; test-sublane; connector-confidence; no-network-default
related:
  - ../README.md
  - ../src/README.md
  - ../src/blm/README.md
  - ../../../connectors/README.md
  - ../../../tests/README.md
  - ../../../docs/sources/catalog/blm.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../tools/
  - ../../../artifacts/
tags: [kfm, connectors, blm, tests, fixtures, validation, source-admission, no-network, bounded-outcomes, governance]
notes:
  - "v0.2 preserves the v0.1 connector-test boundary and expands offline testing, import safety, descriptor gating, anti-collapse, sensitive-data, evidence-limit, and rollback requirements."
  - "connectors/blm/tests/ is for BLM connector-scoped tests and test notes only."
  - "Tests support connector confidence but do not admit sources, close evidence, approve release, or prove end-to-end trust-spine enforcement."
  - "Live-network calls are disabled by default; any integration test must be separately marked, credential-safe, rate-aware, and non-authoritative."
  - "Fixture payloads and generated reports belong in accepted fixture/artifact roots unless a documented local exception is intentionally tiny and non-sensitive."
  - "Actual test modules, fixture coverage, test commands, CI wiring, and current pass state remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BLM Connector Tests

> Offline-first tests for BLM connector admission behavior. This lane verifies connector boundaries; it does not prove source activation, evidence closure, release readiness, or public safety.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: connector tests" src="https://img.shields.io/badge/scope-connector__tests-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-green">
  <img alt="Authority: not release proof" src="https://img.shields.io/badge/authority-not__release__proof-orange">
</p>

`connectors/blm/tests/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted tests](#accepted-tests) · [Exclusions](#exclusions) · [Required test matrix](#required-test-matrix) · [Fixture posture](#fixture-posture) · [Live-service tests](#live-service-tests) · [Evidence limits](#evidence-limits) · [Validation](#validation) · [Safe change pattern](#safe-change-pattern) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/blm/tests/`  
> **Responsibility:** BLM connector-scoped unit, contract, parser, boundary, and failure-mode tests  
> **Truth posture:** `CONFIRMED` README path and test-lane boundary; actual test files, fixtures, commands, coverage, CI execution, pass state, and runtime behavior remain `NEEDS VERIFICATION`.

> [!CAUTION]
> A passing connector test proves only the tested behavior under the tested inputs. It does not prove that a BLM source is activated, authoritative, rights-cleared, current, complete, policy-safe, publicly releasable, or suitable for legal, cadastral, access, cultural-resource, ecological, or operational decisions.

---

## Scope

`connectors/blm/tests/` contains tests and test documentation for the BLM connector implementation under `connectors/blm/src/blm/`.

Tests here may verify:

- import safety and side-effect-free package loading;
- explicit SourceDescriptor and runtime configuration requirements;
- request construction without hidden activation;
- endpoint, service, layer, dataset-family, cadence, timeout, retry, and pagination configuration;
- metadata and source-role preservation;
- source-native identifier preservation;
- retrieval time, source vintage, scale, resolution, generalization, and limitation handling;
- digest/checksum stability;
- raw, quarantine, and receipt-only output boundaries;
- bounded outcomes for success, deny, quarantine, no-op, skipped, rate-limited, stale, and error conditions;
- failure-closed behavior for rights, sensitivity, exact-location, cultural-resource, ecological, infrastructure, or private-location concerns.

This lane must not become source registry authority, fixture authority, lifecycle data authority, policy authority, schema authority, proof authority, release authority, generated-report storage, or a substitute for the canonical `tests/` trust-spine suite.

---

## Repo fit

```text
connectors/
└── blm/
    ├── README.md
    ├── src/
    │   ├── README.md
    │   └── blm/
    │       └── README.md
    └── tests/
        └── README.md
```

Adjacent responsibility roots:

| Root | Relationship to this test lane |
|---|---|
| `connectors/blm/src/blm/` | Code under test. Tests do not become implementation authority. |
| `data/registry/sources/` | SourceDescriptor and activation authority. Tests may use copies or builders, never replace registry records. |
| `fixtures/` | Preferred home for reusable, reviewed, non-sensitive test fixtures. |
| `tests/` | Canonical system-wide enforceability and trust-spine tests. |
| `policy/` | Rights, sensitivity, and admissibility rules. Tests may assert outcomes but do not define policy. |
| `schemas/contracts/`, `contracts/` | Machine shape and object meaning. Tests validate against them but do not create parallel authority. |
| `artifacts/` | Generated test reports, coverage outputs, logs, and QA products. |
| `release/` | Release and rollback decisions; outside connector-test authority. |

---

## Accepted tests

| Belongs here | Required posture |
|---|---|
| Unit tests | Deterministic and offline by default. |
| Parser tests | Preserve source fields, identifiers, timestamps, scale, vintage, rights, and caveats. |
| Request-builder tests | Require explicit descriptor/config input; assert no hidden source activation. |
| Import-safety tests | Assert no network, filesystem mutation, credential access, or source activation during import. |
| Contract-style tests | Reference canonical schemas/descriptors; do not redefine them. |
| Boundary tests | Assert that outputs cannot target processed, catalog, triplet, published, proof-closure, or release paths. |
| Failure-mode tests | Assert finite, reviewable outcomes and reason codes. |
| Anti-collapse tests | Keep PLSS, parcels, title, access, roads, mineral records, recreation, ecology, and cultural-resource claims distinct. |
| Sensitive-data tests | Use synthetic/generalized fixtures; assert fail-closed handling and safe logging. |
| Test-plan notes | May describe intended coverage; must not claim tests run or pass without evidence. |

---

## Exclusions

| Does not belong here | Correct home |
|---|---|
| Production connector modules | `../src/blm/` |
| SourceDescriptor authority or activation records | `../../../data/registry/sources/` |
| Reusable fixture authority | `../../../fixtures/` |
| Raw, quarantine, work, processed, catalog, triplet, proof, receipt, or published lifecycle records | respective `../../../data/` subtrees |
| Rights, sensitivity, or release policy | `../../../policy/` and `../../../release/` |
| Machine schemas or human contract authority | `../../../schemas/contracts/`, `../../../contracts/` |
| Generated reports, coverage files, snapshots, or QA bundles | `../../../artifacts/` |
| End-to-end trust-spine proof | `../../../tests/` |
| Live credentials, tokens, cookies, API keys, or private endpoints | approved secret/runtime configuration; never fixtures or docs |
| Sensitive exact-location records | restricted governed fixtures only, or synthetic/generalized substitutes |

---

## Required test matrix

### Import and configuration

- [ ] Import performs no network calls.
- [ ] Import performs no filesystem writes.
- [ ] Import does not read credentials or activate a source.
- [ ] Missing SourceDescriptor/config input fails safely.
- [ ] Endpoint, service, layer, cadence, timeout, retry, pagination, and rate-limit settings are injectable.

### Source identity and provenance

- [ ] Source-family and dataset-family IDs are preserved.
- [ ] Source-native identifiers remain distinct from normalized KFM identifiers.
- [ ] Source locator, retrieval time, vintage, release/version, digest, and limitation notes are preserved.
- [ ] Source role and authority scope are not strengthened by parsing or normalization.

### BLM anti-collapse cases

- [ ] PLSS reference geometry is not treated as county parcel or title truth.
- [ ] Surface-management data is not treated as private ownership or legal-title proof.
- [ ] Road or trail layers are not treated as current legal access authority.
- [ ] Mineral occurrence, claim, lease, or administrative records remain distinct from ownership and production truth.
- [ ] Recreation, range, fire, vegetation, wildlife, and conservation products retain their own source role, scale, vintage, and fitness limits.
- [ ] Historic records remain historically scoped and are not silently promoted to present status.

### Sensitive and policy-significant cases

- [ ] Exact cultural-resource, archaeological, ecological, infrastructure, or private-location details fail closed when policy is unresolved.
- [ ] Logs and assertion messages do not expose secrets, exact restricted locations, or protected payload content.
- [ ] Rights-unknown or sensitivity-unknown inputs return `deny`, `quarantine`, or `needs_review` rather than admit.
- [ ] Synthetic/generalized fixtures are used for sensitive-path tests whenever practical.

### Lifecycle and finite outcomes

- [ ] Allowed handoffs are limited to explicit raw, quarantine, and receipt envelopes.
- [ ] Processed, catalog, triplet, published, proof-closure, and release outputs are rejected.
- [ ] Tests cover `admit_raw`, `quarantine`, `deny`, `needs_review`, `no_op`, `skipped`, `rate_limited`, `stale`, and `error` outcomes where supported.
- [ ] Every non-success outcome carries a deterministic reason code or reviewable explanation.
- [ ] Receipt assertions do not confuse run evidence with evidence closure or release proof.

---

## Fixture posture

Prefer small, deterministic, no-network fixtures stored under an accepted fixture root.

Fixtures must be:

- reviewable and license/rights appropriate;
- stripped of credentials, tokens, cookies, and private endpoint details;
- non-sensitive, synthetic, redacted, or generalized where exact locations could create risk;
- pinned to a known source shape or schema version;
- clearly labeled as test material, never source authority;
- small enough to review in Git;
- accompanied by expected digest or normalization output where useful.

A tiny local fixture may live beside a test only when repository convention permits it and the test documents why. Local convenience does not create fixture authority.

---

## Live-service tests

> [!WARNING]
> Live-service tests are not the default and must never run silently during ordinary unit tests or imports.

A live integration test, when explicitly approved, must:

- be separately marked and opt-in;
- use runtime-injected credentials or public endpoints without committing secrets;
- respect source terms, robots guidance, rate limits, timeouts, and retry budgets;
- avoid destructive requests or broad harvesting;
- record endpoint, source version, request window, and test time;
- tolerate expected network instability without converting it into source truth;
- avoid writing lifecycle records outside an isolated temporary location;
- emit no claim of activation, completeness, authority, or release readiness.

Live endpoint success is operational evidence for that run only. It is not proof of continuing availability or admissibility.

---

## Evidence limits

| Evidence | May support | Does not prove |
|---|---|---|
| Passing unit test | Tested function behavior for supplied inputs | Source activation, rights clearance, completeness, or release readiness |
| Passing parser fixture | Compatibility with one captured shape | Compatibility with all versions or live endpoint variants |
| Stable digest test | Determinism for tested bytes and algorithm | Source authenticity or legal admissibility |
| Passing boundary test | Rejection of tested prohibited targets | Full system enforcement outside tested paths |
| Passing policy-outcome test | Expected decision for supplied policy fixture | Current production policy configuration |
| Passing live probe | Endpoint response during one run | Future availability, correctness, authority, or publication safety |

---

## Validation

Before relying on this test lane, verify:

- actual test modules are inventoried;
- the test runner and exact commands are documented;
- package import paths and dependency installation are verified;
- fixture paths and expected hashes are current;
- SourceDescriptor, schema, policy, and contract references resolve;
- offline tests fail when unexpected network access occurs;
- sensitive data cannot leak through fixtures, logs, snapshots, or assertion messages;
- coverage includes success and finite failure outcomes;
- CI invokes the relevant tests or clearly marks them manual;
- generated outputs land under `artifacts/` or another accepted report root;
- connector tests complement rather than replace canonical `tests/` enforcement.

---

## Safe change pattern

For changes under `connectors/blm/tests/`:

1. Tie each test to a named connector behavior, boundary, contract, or failure mode.
2. Keep tests offline and deterministic by default.
3. Confirm fixtures are non-sensitive, rights-appropriate, and stored in an accepted location.
4. Confirm no test embeds source, schema, policy, registry, receipt, proof, or release authority.
5. Cover import safety, descriptor/config gating, source-role preservation, and output boundaries when affected.
6. Cover relevant BLM anti-collapse and sensitive-location cases.
7. Update CI/test commands or mark execution `NEEDS VERIFICATION`.
8. Store generated reports outside this directory.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `connectors/blm/tests/README.md` v0.1 | `CONFIRMED` prior baseline | Connector-scoped test boundary, no-network preference, fixture/report exclusions, finite failures, and canonical-test distinction | Did not prove current tests, fixtures, CI, or pass state |
| `connectors/blm/README.md` | `CONFIRMED` documentation boundary | BLM source-admission scope, source-role limits, dataset-family posture, and raw/quarantine boundary | Does not prove activated sources or implementation behavior |
| `connectors/blm/src/README.md` | `CONFIRMED` documentation boundary | Python source-root placement, importability, descriptor/config injection, and downstream exclusions | Does not prove package discovery or imports |
| `connectors/blm/src/blm/README.md` | `CONFIRMED` package boundary | Package-level allowed code, import safety, anti-collapse, sensitive-data, and bounded-output expectations | Does not prove module implementation or tests |
| Current repository test files, fixtures, workflows, and logs | `NEEDS VERIFICATION` | Actual coverage, commands, CI execution, pass/fail state, and runtime behavior | Not inventoried in this README update |

---

## Rollback

Rollback this documentation change if it:

- implies connector tests admit or activate a source;
- treats passing tests as evidence closure, release approval, or public-safety proof;
- permits network access by default;
- allows credentials or protected exact-location data in fixtures or logs;
- creates fixture, policy, schema, registry, proof, receipt, or release authority under this directory;
- weakens raw/quarantine/receipt-only output tests;
- replaces canonical system-wide tests with connector-local tests.

**Rollback target:** prior blob `3f8f7437e8cb082b98b78efb7c64a71f9dfe160d`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual test files are inventoried.
- [ ] Test runner and copy/paste commands are documented.
- [ ] Package import and discovery work in the test environment.
- [ ] Imports are verified side-effect-free.
- [ ] Descriptor/config gating is covered.
- [ ] BLM source-role and dataset-family anti-collapse cases are covered.
- [ ] Sensitive-location, rights-unknown, and policy-unknown cases fail closed.
- [ ] Raw/quarantine/receipt-only boundaries are covered.
- [ ] Success and finite failure outcomes are covered.
- [ ] Fixtures are non-sensitive, rights-appropriate, deterministic, and stored correctly.
- [ ] No live-network test runs by default.
- [ ] No source registry, lifecycle, release, policy, schema, proof, receipt, fixture, generated-report, or production-code authority lives here.
- [ ] CI/test-runner behavior and current pass state are verified or explicitly marked `NEEDS VERIFICATION`.
- [ ] Canonical `tests/` coverage remains present for system-wide enforcement.

---

## Status summary

`connectors/blm/tests/` is the offline-first BLM connector test sublane. It verifies bounded connector behavior and failure-safe admission boundaries; it is not source activation authority, fixture authority, lifecycle authority, policy authority, schema authority, evidence closure, release authority, generated-report storage, or a replacement for KFM's canonical trust-spine tests.

<p align="right"><a href="#top">Back to top</a></p>
