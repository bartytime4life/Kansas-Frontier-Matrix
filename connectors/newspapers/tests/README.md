<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://connectors/newspapers/tests/readme
title: Newspaper Connector Test Lane
path: connectors/newspapers/tests/README.md
type: connector-test-readme
version: v0.2
prior_version: v0.1
prior_blob: ab7a7ea03cd1453ba98f273590a86855d0e9a44e
base_commit: 92ddac60a5dd7ec4c1f4704c651bd173423afbaf
status: draft
owners: OWNER_TBD — test steward · connector steward · source steward · archives steward · genealogy steward · people-dna-land steward · validation steward · rights steward · sensitivity steward
created: 2026-06-19
updated: 2026-07-14
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: connectors/
lifecycle_phase: source-admission-verification
source_family: newspapers
related:
  - ../README.md
  - ../src/README.md
  - ../src/newspapers/README.md
  - ../pyproject.toml
  - ../../../tests/README.md
  - ../../../tests/fixtures/README.md
  - ../../../tests/policy/test_pipeline_connector_non_publisher.py
  - ../../../fixtures/README.md
  - ../../../pyproject.toml
  - ../../../Makefile
  - ../../../.github/workflows/connector-gate.yml
  - ../../../docs/sources/catalog/newspapers/README.md
  - ../../../docs/sources/catalog/loc/README.md
  - ../../../docs/architecture/source-roles.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../data/registry/sources/README.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
tags:
  - kfm
  - connectors
  - newspapers
  - tests
  - pytest
  - no-network
  - synthetic-fixtures
  - ocr
  - iiif
  - provenance
  - source-admission
  - raw
  - quarantine
  - rights-review
  - sensitivity-review
notes:
  - "Only this README was verified under the connector-local test lane; expected test modules, conftest, and newspaper fixture payloads did not surface."
  - "The package remains an empty initializer with greenfield 0.0.0 metadata, so no newspaper runtime behavior is currently available for package-local tests."
  - "The root project declares pytest support, but the default Makefile test target does not include this lane and connector-gate remains a TODO echo scaffold."
  - "A root policy test scans connectors for prohibited publication writes; that cross-cutting guard is not newspaper package coverage."
  - "No live-test flag or command is implemented; future default package tests must remain deterministic, synthetic, no-network, and fail-closed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Newspaper connector tests

Directory contract for connector-local verification under `connectors/newspapers/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README%20only-lightgrey">
  <img alt="Package: scaffold only" src="https://img.shields.io/badge/package-scaffold%20only-lightgrey">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled%20by%20default-critical">
  <img alt="Coverage: not established" src="https://img.shields.io/badge/coverage-not%20established-orange">
  <img alt="Rights and privacy: fail closed" src="https://img.shields.io/badge/rights%20%2F%20privacy-fail%20closed-red">
</p>

> [!CAUTION]
> This lane may verify newspaper connector behavior. It is not source, OCR, transcription, person/entity/event/place, rights, privacy, sensitivity, evidence, proof, release, or publication authority. A passing connector-local suite would prove only the behavior exercised by its reviewed fixtures and assertions.

---

## Quick contract

| Question | Test-lane answer |
|---|---|
| What exists now? | This README only; no dedicated newspaper test module, `conftest.py`, or payload fixture surfaced. |
| Is there runtime code to test? | **No verified implementation.** The package contains a README and an empty `__init__.py`. |
| Does the repository support pytest? | **Yes at the root scaffold.** Root `pyproject.toml` declares pytest as a test extra and sets `pythonpath = ["."]`. |
| Does `make test` run this lane? | **No.** The current target runs `tests/schemas` and `tests/contracts` only. |
| Does connector CI test newspapers? | **No verified coverage.** `connector-gate.yml` currently echoes TODO messages. |
| Is any connector guard implemented? | **Yes, cross-cutting only.** A root policy test scans connector/pipeline code for prohibited publication-write contexts. |
| Are live tests available? | **No.** No live test directory, opt-in flag, credentials contract, or source activation was verified. |
| What is the default future posture? | Deterministic, synthetic, minimized, no-network, no-secret, no-write, and fail-closed. |

---

## Verified repository state

The table records observations at base commit `92ddac60a5dd7ec4c1f4704c651bd173423afbaf`. Expected-path probes and targeted search show what surfaced during this update; they are not exhaustive proof of absence.

| Surface | Observed state | Test-lane consequence |
|---|---|---|
| This README | Existing v0.1 at blob `ab7a7ea03cd1453ba98f273590a86855d0e9a44e`. | v0.2 replaces proposed commands, fixture IDs, and unknown inventory with pinned evidence. |
| [`connectors/newspapers/src/README.md`](../src/README.md) | Merged v0.2 source-root contract. | Future tests inherit its import/build, admission, product-separation, and no-publication boundaries. |
| [`connectors/newspapers/src/newspapers/README.md`](../src/newspapers/README.md) | Merged v0.2 package contract. | Future package tests must exercise its proposed module/product/outcome contract without treating it as implementation proof. |
| `src/newspapers/__init__.py` | Empty Git blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`. | No public import surface or runtime behavior is implemented. |
| Expected runtime modules | Client/parser and the other proposed modules were absent at inspected paths. | Meaningful package unit/integration coverage cannot yet be claimed. |
| Expected connector-local tests | `test_newspapers.py` and `conftest.py` were absent; targeted search surfaced documentation, not a suite. | This lane is a documentation scaffold. |
| Expected connector-local fixture lane | `tests/fixtures/README.md` and the v0.1 example payload path were absent. | The example fixture ID was illustrative only and is removed. |
| [`connectors/newspapers/pyproject.toml`](../pyproject.toml) | Greenfield distribution `kfm-connector-newspapers`, version `0.0.0`, with no declared test contract. | Package-local test dependencies, discovery, markers, and entry points are unverified. |
| [Root `pyproject.toml`](../../../pyproject.toml) | Root project is `0.0.0`; test extra declares `pytest>=9.1.1,<10`; pytest adds repository root to `pythonpath`. | Framework availability is scaffolded, but no newspaper suite or pass result follows from it. |
| [Root `Makefile`](../../../Makefile) | `make test` invokes only `tests/schemas` and `tests/contracts`. | The default test target does not discover this connector-local lane. |
| [`connector-gate.yml`](../../../.github/workflows/connector-gate.yml) | Both connector jobs check out the repository and echo TODO text. | Workflow success is not connector behavior, boundary, fixture, or coverage proof. |
| [`test_pipeline_connector_non_publisher.py`](../../../tests/policy/test_pipeline_connector_non_publisher.py) | Cross-cutting static test scans Python/shell write contexts in `connectors/` and `pipelines/` for selected forbidden targets. | It supplies a useful repository boundary canary, not newspaper-specific parsing, rights, sensitivity, or admission coverage. |
| [`tests/README.md`](../../../tests/README.md) | Root test doctrine is canonical and defines trust-spine coverage; executable depth remains mixed. | Cross-cutting enforcement belongs at the root; package-local behavior may remain adjacent here. |
| Fixture homes | Root doctrine distinguishes `tests/fixtures/` for unit-test-scoped fixtures from `fixtures/` for cross-cutting reusable fixtures. | Do not create a third fixture authority silently under this lane. |
| Expected newspaper/ChronAm SourceDescriptors | Checked descriptor paths were absent. | Live-source activation and descriptor-driven integration tests are not established. |
| `.github/CODEOWNERS` | No newspapers-specific or connector-test ownership rule surfaced. | Owners remain `OWNER_TBD`. |

> [!IMPORTANT]
> Pytest availability, a README, a workflow name, or an unrelated passing boundary test does not establish newspaper connector coverage. Coverage begins only when executable tests consume reviewed fixtures and assert implemented behavior.

---

## Placement and authority boundary

```text
connectors/newspapers/
├── README.md                         # connector-family boundary
├── pyproject.toml                    # 0.0.0 greenfield placeholder
├── src/
│   ├── README.md                     # source-root contract, v0.2
│   └── newspapers/
│       ├── README.md                 # package contract, v0.2
│       └── __init__.py               # empty at the pinned base
└── tests/
    └── README.md                     # this test-lane contract; no suite verified
```

Directory Rules §7.3 assigns source fetch/admission responsibility to `connectors/`, limits connector outputs to RAW or QUARANTINE, and forbids publication. The existing adjacent `tests/` path may hold package-local behavior checks, but it does not replace the canonical root [`tests/`](../../../tests/README.md) trust-spine authority.

Use the split deliberately:

| Verification class | Correct owner |
|---|---|
| Package imports, configuration, client/parser helpers, provenance preservation, and finite local failures | `connectors/newspapers/tests/` once implemented. |
| Source-role, lifecycle, policy, boundary, proof/release, governed API/UI, correction, and rollback enforcement spanning roots | Canonical root `tests/` lanes. |
| Unit-test-scoped synthetic fixtures | `tests/fixtures/<accepted-lane>/` under the canonical root. |
| Cross-cutting reusable runtime/golden fixtures | Root `fixtures/<accepted-lane>/`. |
| Source data, descriptors, schemas, policy, receipts/proofs, releases, and published artifacts | Their governed responsibility roots, never this test lane. |

Do not create a parallel `tests/connectors/newspapers/`, a second connector-test root, or a connector-local fixture authority merely to avoid a placement decision. Use an ADR or migration note if the accepted test home changes.

---

## What belongs here

When implementation lands, this lane may contain:

- deterministic connector-package tests;
- import/build/configuration tests scoped to the newspaper distribution;
- mocked client and parser tests with no network or credential dependency;
- page/image, OCR, correction, segmentation, extraction, and provenance-preservation assertions;
- descriptor/activation, rights/privacy/sensitivity, and RAW/QUARANTINE handoff tests that exercise package-local adapters;
- small helper modules that are test code only and do not become runtime utilities;
- markers/configuration owned by the connector package after repository test conventions accept them.

Do not place here:

- production implementation or source activation logic;
- real newspaper downloads, archive exports, bulk OCR, page-image corpora, credentials, cookies, tokens, signed URLs, or session state;
- canonical SourceDescriptors, schemas, contracts, policy decisions, evidence bundles, receipts, proofs, releases, corrections, or rollback cards;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle data;
- generated CI artifacts, coverage reports, public API/UI payloads, reports, maps, tiles, search/vector indexes, or AI answers;
- authoritative OCR corrections, identity resolution, relationship/event/place truth, or public claims.

---

## Default execution contract

Until executable tests exist, there is no verified newspaper package command that exercises a suite or produces a meaningful pass result. The repository framework and discovery wiring remain separate facts.

Future default execution must satisfy all of these conditions:

| Concern | Required behavior |
|---|---|
| Network | Disabled and actively blocked; an accidental request fails the test. |
| Credentials | Not read, required, logged, or inferred. |
| Filesystem | Temporary paths only; no repository lifecycle, policy, proof, release, or public writes. |
| Time/randomness | Frozen, injected, or seeded where behavior depends on it. |
| Payloads | Synthetic, minimized, deterministic, public-safe, and reviewable. |
| Source activation | Disabled unless a dedicated, reviewed integration tier explicitly supplies a synthetic/approved descriptor. |
| Outcomes | Explicit success/failure/abstention/quarantine expectations; no silent fallback or invented truth. |
| Logs/errors | Finite and secret-safe; no full copyrighted OCR or sensitive person/location detail. |
| Isolation | Tests pass without archive accounts, external services, caches, prior run state, or execution order. |
| Reproducibility | Same code, fixture, configuration, and version produce the same assertions and digests. |

The v0.1 commands and `KFM_ALLOW_LIVE_NEWSPAPER_TESTS` flag were proposals, not verified interfaces. Do not restore or consume them until code, package configuration, test markers, CI exclusion, ownership, and rollback behavior implement the contract.

---

## Minimum future coverage

| Test class | Required proof | Must not imply |
|---|---|---|
| Scaffold/import | Package builds/imports without network, secret lookup, cache mutation, writes, or logging side effects. | Functional connector implementation or source activation. |
| Configuration | Defaults are offline/fail-closed; invalid or missing configuration produces a finite result. | A live endpoint is approved. |
| Client behavior | Timeout, retry, rate-limit, paging/cursor/job, partial response, cancellation, and drift behavior are bounded. | Remote availability, completeness, or terms permission. |
| Product separation | Issue/page/image, raw OCR, corrected transcription, article/clipping, legal notice, obituary, event report, and extraction candidates remain distinct. | OCR, segmentation, or extraction truth. |
| Provenance | Provider, collection, product, issue/page/article identity, source URL/ref, retrieval time, digest, and transform/run metadata survive. | Evidence closure or publication eligibility. |
| Source role | Only canonical enum values are accepted per product/claim; unresolved or conflicting role quarantines/abstains. | One family-wide newspaper role. |
| Descriptor/activation | Missing, stale, inactive, mismatched, or incomplete descriptors block live behavior. | Descriptor authority inside package code. |
| Rights | Unknown/conflicting copyright, license, citation, excerpt, reuse, retention, deletion, or platform terms fail closed. | Public availability equals reuse permission. |
| Privacy/sensitivity | Living-person, minor, medical/legal/crime/reputational, adoption/parentage, tribal/cultural, sacred/burial, archaeology, repatriation, exact-location, and mosaic risks restrict, deny, or quarantine. | Test fixtures authorize real-world disclosure. |
| Admission handoff | Typed output is bounded to run-scoped RAW or QUARANTINE candidates and preserves reasons/metadata. | Direct lifecycle writes by arbitrary parser code. |
| Output escape | Package code cannot write or serve WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, release, API, UI, report, map, search, vector, or AI-answer output. | Cross-cutting trust-spine closure from a package suite alone. |
| Error/log safety | Malformed, empty, duplicate, drifted, oversized, hostile, or secret-bearing inputs produce bounded, redacted outcomes. | Bad input can be silently discarded or promoted. |

Each implemented behavior needs positive, invalid, partial, duplicate, drift, deny/restrict, abstain/quarantine, and regression cases where applicable. Passing happy-path tests alone is insufficient.

---

## Fixture contract

No dedicated newspaper fixture payload surfaced at the pinned base.

Before adding one, select the accepted home:

| Fixture scope | Preferred home | Rule |
|---|---|---|
| Owned by a specific unit/source test | `tests/fixtures/<accepted-newspaper-lane>/` | Synthetic, minimal, deterministic, public-safe, expected outcome explicit. |
| Shared by several tests, validators, pipelines, or runtime checks | `fixtures/<accepted-newspaper-lane>/` | Cross-cutting reuse and generation/source/rights notes required. |
| Real source material | Governed lifecycle/source roots | Never disguise it as a fixture; apply admission, rights, privacy, and sensitivity review. |

Minimum fixture metadata, once a schema or accepted convention exists:

- synthetic/public-safe status and generator/note;
- intended consuming tests and expected finite outcome;
- source family/product/surface without inventing an active descriptor;
- provider/collection/page/article identity fields needed by the case;
- source-role state, including unresolved/conflicted cases;
- OCR/correction/segmentation/extraction provenance needed by the assertion;
- rights/privacy/sensitivity posture and review state;
- stable digest and schema/contract version refs where accepted;
- explicit redactions/generalizations and why they are safe.

Do not copy the v0.1 illustrative `newspapers-synthetic-admission-001` identifier into code as if it were registered. Do not use real names, protected locations, copyrighted bulk text, or private archive material to make a fixture realistic.

---

## Live and integration testing

No live test tier is implemented or approved.

If one is later proposed, it must be separate from default tests and require all of the following before execution:

- accepted owners and placement;
- active product-specific SourceDescriptor and source role;
- current provider terms, rights, citation, privacy, sensitivity, retention/deletion, and intended-use decisions;
- explicit opt-in marker/flag defined in code and CI, not only prose;
- default skip in local, PR, fork, and ordinary CI runs;
- bounded request count, concurrency, paging, timeout, retry, rate-limit, cache, and cost behavior;
- isolated credentials supplied by an approved secret mechanism and never printed;
- minimal response retention with deletion/quarantine rules;
- receipts/logs that are useful without exposing copyrighted or sensitive content;
- a kill switch and rollback path.

Live smoke success must not be used as truth, completeness, rights, sensitivity, release, or service-reliability proof.

---

## CI and repository integration

Current state:

```text
root pytest dependency:        present as project test extra
root pytest pythonpath config: present
default make test coverage:    schemas + contracts only
newspaper test files:          not surfaced
newspaper fixtures:            not surfaced
connector-gate implementation: TODO echo scaffold
cross-cutting no-publish test: implemented, not package-specific
newspaper pass rate/coverage:  not established
```

Before this lane can become a required gate:

- [ ] Package metadata declares the accepted test dependency/discovery contract.
- [ ] Executable tests and reviewed fixtures exist.
- [ ] A local command runs the same suite CI runs and fails when no tests are collected.
- [ ] Default execution actively blocks network, secrets, and unsafe writes.
- [ ] Connector CI replaces TODO steps with substantive checks and reports its exact test selection.
- [ ] Cross-cutting root tests cover output escape and trust-spine boundaries without duplicating local unit assertions.
- [ ] CI emits reviewable results without committing generated artifacts to authority roots.
- [ ] Coverage thresholds, ownership, required/optional status, flaky-test policy, and rollback are documented.

---

## Evidence and change ledger

| Claim | Status | Evidence / limit |
|---|---|---|
| The connector-local test path exists. | **CONFIRMED** | This README exists. |
| A newspaper test suite exists. | **UNKNOWN / not surfaced** | Expected test files were absent and targeted search returned documentation only. |
| Newspaper tests pass. | **DENY** | No executable newspaper suite or run result was verified. |
| Newspaper fixtures exist. | **UNKNOWN / not surfaced** | Expected local fixture paths and v0.1 example ID were absent. |
| The root repository supports pytest. | **CONFIRMED scaffold** | Root `pyproject.toml` declares a pytest test extra and root pythonpath. |
| The newspaper package declares a test contract. | **DENY** | Connector `pyproject.toml` remains a minimal `0.0.0` placeholder. |
| `make test` includes newspaper tests. | **DENY** | It selects `tests/schemas` and `tests/contracts` only. |
| Connector CI exercises newspaper behavior. | **DENY** | `connector-gate.yml` echoes TODO messages. |
| A connector no-publication guard exists. | **CONFIRMED, cross-cutting** | Root policy test scans selected connector/pipeline write contexts; it is not full output-escape or package coverage. |
| Live newspaper tests are implemented. | **DENY** | No live directory, marker, flag, descriptor activation, or command was verified. |
| Package runtime behavior is implemented. | **DENY** | Empty initializer only; inspected runtime module paths were absent. |
| Passing local tests would prove newspaper-derived truth or publication readiness. | **DENY** | Evidence, policy, proof, release, and public governance remain downstream. |

### What changed from v0.1

- replaced unknown test inventory with the confirmed README-only lane and absent expected files;
- synchronized test requirements with the merged source-root and package v0.2 contracts;
- distinguished root pytest availability from connector package wiring and actual tests;
- recorded that `make test` excludes this lane and connector CI remains a TODO scaffold;
- documented the existing cross-cutting connector no-publication canary without overstating its coverage;
- removed guessed runnable commands, the unimplemented live-test flag, and the illustrative fixture ID as an example payload;
- aligned fixture placement with the canonical `tests/fixtures/` versus root `fixtures/` split;
- added product separation, source-role, descriptor, rights/privacy/sensitivity, admission, output-escape, error/log, live-tier, CI, and activation requirements;
- preserved v0.1's deterministic no-network, no-secret, synthetic-fixture, RAW/QUARANTINE-only, candidate-only, no-publication, and fail-closed boundaries.

---

## Activation checklist

- [ ] Owners and accepted connector-local test placement are confirmed.
- [ ] Runtime modules and package/build configuration exist before tests claim their behavior.
- [ ] Test discovery, dependencies, markers, and local/CI parity are implemented.
- [ ] Reviewed synthetic valid/invalid/partial/drift/sensitive fixtures exist in an accepted fixture home.
- [ ] Default tests prove network, secret, cache, filesystem, and source activation isolation.
- [ ] Product, provenance, canonical source-role, descriptor, and finite-outcome assertions pass.
- [ ] Rights/privacy/sensitivity denial, restriction, abstention, quarantine, and redaction/generalization cases pass.
- [ ] RAW/QUARANTINE-only handoff and package-local output-escape checks pass.
- [ ] Cross-cutting root tests cover the trust-spine boundaries that local tests cannot establish.
- [ ] Connector CI performs substantive work and fails on zero collected tests.
- [ ] Live tests remain absent or separately reviewed, opt-in, bounded, secret-safe, and disabled by default.
- [ ] Coverage/pass-rate claims link to a current run and exact commit.
- [ ] Rollback can disable the connector/test gate without deleting fixtures, receipts, proofs, corrections, releases, or review history.

---

## Rollback

This is a documentation-only update. Restore the exact prior README from blob:

```text
ab7a7ea03cd1453ba98f273590a86855d0e9a44e
```

Rolling back this document does not create, remove, run, enable, disable, or pass tests. It must not alter source code, package metadata, workflows, fixtures, SourceDescriptors, lifecycle data, rights/privacy/sensitivity decisions, receipts, proofs, corrections, or releases.

---

## Related files

- [`connectors/newspapers/README.md`](../README.md)
- [`connectors/newspapers/src/README.md`](../src/README.md)
- [`connectors/newspapers/src/newspapers/README.md`](../src/newspapers/README.md)
- [`connectors/newspapers/pyproject.toml`](../pyproject.toml)
- [Root `tests/README.md`](../../../tests/README.md)
- [`tests/fixtures/README.md`](../../../tests/fixtures/README.md)
- [`tests/policy/test_pipeline_connector_non_publisher.py`](../../../tests/policy/test_pipeline_connector_non_publisher.py)
- [Root `fixtures/README.md`](../../../fixtures/README.md)
- [Root `pyproject.toml`](../../../pyproject.toml)
- [Root `Makefile`](../../../Makefile)
- [`connector-gate.yml`](../../../.github/workflows/connector-gate.yml)
- [`docs/sources/catalog/newspapers/README.md`](../../../docs/sources/catalog/newspapers/README.md)
- [`docs/sources/catalog/loc/README.md`](../../../docs/sources/catalog/loc/README.md)
- [`docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md)
- [`data/registry/sources/README.md`](../../../data/registry/sources/README.md)
- [`schemas/contracts/v1/source/source_descriptor.schema.json`](../../../schemas/contracts/v1/source/source_descriptor.schema.json)

---

KFM rule: `connectors/newspapers/tests/` may verify bounded connector behavior only. It does not create source, OCR, transcription, identity, relationship, event, place, rights, privacy, sensitivity, evidence, proof, release, publication, public-presentation, or generated-answer truth.

[Back to top](#top)
