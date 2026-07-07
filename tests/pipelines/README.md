<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-pipelines-readme
title: Pipeline Tests README
type: test-readme
version: v0.1
status: draft; greenfield-stub-replaced; pipeline-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - Pipeline steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; pipelines; lifecycle; trust-spine; no-network; synthetic-only; evidence-aware; policy-aware; release-gated; rollback-aware
tags: [kfm, tests, pipelines, lifecycle, trust-spine, pipeline-tests, ingest, normalize, validate, catalog, triplets, publish-readiness, rollback-readiness, watchers, receipts, proofs, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../fixtures/README.md
  - ../../pipelines/README.md
  - ../../pipeline_specs/README.md
  - ../../data/receipts/pipeline/
  - ../../data/proofs/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../release/
notes:
  - "This README replaces the greenfield stub at tests/pipelines/README.md."
  - "This lane documents executable pipeline behavior tests, not pipeline implementation. Pipeline code belongs under pipelines/; declarative specs belong under pipeline_specs/."
  - "Pipeline tests should prove lifecycle, evidence, policy, receipt, release, correction, and rollback gates without turning a pipeline run into public truth or release approval."
  - "Executable test inventory, actual runner/framework, fixture consumption, schema bindings, policy/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipeline tests

> Test-lane README for executable pipeline behavior checks under `tests/pipelines/`. This directory should prove that KFM pipeline logic preserves lifecycle, evidence, policy, receipt, release, correction, and rollback boundaries without becoming pipeline implementation, lifecycle data, proof storage, policy authority, or release approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: pipeline tests" src="https://img.shields.io/badge/lane-pipeline__tests-purple">
  <img alt="Lifecycle: governed" src="https://img.shields.io/badge/lifecycle-governed-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/pipelines/README.md`  
**Status:** draft / greenfield stub replaced / pipeline test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `pipelines`  
**Implementation companion:** `pipelines/`  
**Spec companion:** `pipeline_specs/`  
**Default posture:** deterministic, synthetic, no-network, public-safe pipeline tests only  
**Truth posture:** CONFIRMED target file existed as a greenfield stub before replacement; CONFIRMED `tests/README.md` lists `tests/pipelines/` as executable pipeline behavior tests; CONFIRMED `pipelines/README.md` defines `pipelines/` as executable logic and separates it from specs, data, policy, tests, fixtures, and release decisions; NEEDS VERIFICATION for executable test inventory, actual runner/framework, fixtures, schema bindings, policy/runtime wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/pipelines/` for tests that verify pipeline behavior and pipeline-boundary discipline.

In scope:

- ingest, normalize, validate, catalog, triplet, publish-readiness, rollback-readiness, watcher, and proof-harness behavior checks;
- tests that verify `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` is not skipped;
- tests that verify failed validation or policy routes to blockers, quarantine, abstention, denial, or error;
- tests that verify pipeline outputs carry receipts, hashes, input refs, blocker reasons, correction refs, and rollback refs where material;
- tests that prove publish-readiness is not release approval;
- tests that prove rollback-readiness is not rollback approval;
- tests that consume synthetic fixtures from `tests/fixtures/`, root `fixtures/`, or domain fixture lanes after verification.

Out of scope:

- executable pipeline implementation;
- declarative pipeline specs or schedules;
- lifecycle data, receipts, proofs, or release records;
- schemas, contracts, policies, or source registries;
- public API/UI code, generated artifacts, production logs, source credentials, or live network calls.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Pipeline behavior tests | `tests/pipelines/` | This lane. |
| Pipeline implementation | `pipelines/` | Code under test; not owned here. |
| Declarative pipeline specs | `pipeline_specs/` | Configuration under test; not owned here. |
| Unit-test fixtures | `tests/fixtures/` | Test-local inputs; not owned here. |
| Cross-cutting fixtures | `fixtures/` | Shared synthetic/golden inputs; not owned here. |
| Lifecycle data | `data/` phase roots | Referenced only through governed synthetic/test refs. |
| Pipeline receipts | `data/receipts/pipeline/` | Trust artifacts; not authored here. |
| Evidence/proof data | `data/proofs/` | Proof authority; not authored here. |
| Release/correction/rollback | `release/` | Publication authority; tests verify readiness/blockers only. |
| Contracts, schemas, policy | `contracts/`, `schemas/`, `policy/` | Authority roots; tests reference and verify. |

> [!IMPORTANT]
> `tests/pipelines/` must not become pipeline implementation, `pipeline_specs/`, lifecycle data, receipt/proof storage, policy authority, schema authority, source registry, release authority, or generated artifact storage.

---

## Pipeline-test rule

Pipeline tests should prove that a pipeline run remains subordinate to KFM governance. Passing tests should demonstrate boundary discipline, not claim publication or truth.

Core expectations:

| Expectation | Required posture |
|---|---|
| Lifecycle discipline | No test permits direct `RAW` or `WORK` to `PUBLISHED` promotion. |
| No-network default | Default tests use synthetic fixtures and do not call live sources, APIs, tiles, models, or external services. |
| Evidence discipline | Pipeline outputs reference or require evidence support; they do not fabricate EvidenceBundles. |
| Policy discipline | Unknown rights, unresolved sensitivity, missing review, stale source, or denied policy fails closed. |
| Receipt discipline | Pipeline behavior emits or expects receipt/blocker posture where material; tests do not store real receipts. |
| Release discipline | Publish-readiness checks never equal release approval. |
| Rollback discipline | Rollback-readiness checks never equal rollback approval; rollback targets remain visible where material. |
| Root discipline | Code stays in `pipelines/`; specs stay in `pipeline_specs/`; tests stay here. |

---

## Expected test families

| Family | What it proves | Expected outcome |
|---|---|---|
| `ingest_admission` | Source intake routes to RAW, WORK, or QUARANTINE with required refs. | `PASS` / blocker. |
| `normalize_receipt` | Normalization emits deterministic transform/receipt posture. | `PASS`. |
| `validate_blocker` | Invalid schema, contract, geometry, time, source-role, or policy state blocks promotion. | validation failure / `ERROR`. |
| `quarantine_on_failure` | Failed validation or policy sends material to quarantine with reason. | `PASS` / `DENY`. |
| `catalog_closure` | Catalog/triplet handoff requires evidence, source role, rights, policy, and validation support. | `PASS` / `ABSTAIN`. |
| `publish_readiness_not_release` | Readiness pass does not create release approval. | `PASS`. |
| `rollback_readiness` | Rollback/correction prerequisites are checked without silently editing history. | `PASS` / validation failure. |
| `watcher_non_publisher` | Watcher/source-refresh logic detects or proposes but does not publish. | `PASS` / `DENY`. |
| `no_direct_public_path` | Pipeline cannot bypass governed API/release gates into public UI or published artifacts. | validation failure / `DENY`. |
| `receipts_and_proofs_separate` | Receipts/proofs remain separate object families and are not collapsed into data or release. | `PASS` / validation failure. |

---

## Accepted inputs

Accepted material is limited to executable tests, lane-local notes, and minimal synthetic inline values when they are too small to justify a fixture file.

Preferred fixture inputs should be referenced from:

- `tests/fixtures/` for unit-test-scoped fixtures;
- `fixtures/` for cross-cutting shared fixtures;
- `fixtures/domains/<domain>/` for domain-specific golden/valid/invalid fixtures;
- `pipeline_specs/` for declarative specs under test after placement is verified.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| pipeline implementation code | `pipelines/` |
| declarative pipeline specs, schedules, profiles, or run contracts | `pipeline_specs/` |
| lifecycle records or data outputs | `data/` lifecycle roots |
| pipeline receipts, proof packs, EvidenceBundles | `data/receipts/`, `data/proofs/` |
| release manifests, correction notices, rollback cards | `release/` roots |
| schema definitions | `schemas/` |
| contract definitions | `contracts/` |
| policy rules | `policy/` |
| fixtures and fixture payload collections | `tests/fixtures/` or `fixtures/` |
| source credentials, production logs, generated artifacts, public exports, or direct model output | not allowed in repository tests |

---

## Suggested layout

```text
tests/pipelines/
|-- README.md
|-- ingest_admission.test.PROPOSED
|-- normalize_receipt.test.PROPOSED
|-- validate_blocker.test.PROPOSED
|-- quarantine_on_failure.test.PROPOSED
|-- catalog_closure.test.PROPOSED
|-- publish_readiness_not_release.test.PROPOSED
|-- rollback_readiness.test.PROPOSED
|-- watcher_non_publisher.test.PROPOSED
|-- no_direct_public_path.test.PROPOSED
`-- receipts_and_proofs_separate.test.PROPOSED
```

The layout is schematic. Actual test filenames, extensions, package manager, runner, and framework remain NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/pipelines
```

Default runs should be deterministic, local, no-network, public-safe, and finite-outcome only. Replace the command once the repo's actual test runner and naming convention are verified.

---

## Maintenance checklist

- [ ] Keep this lane focused on executable pipeline behavior tests.
- [ ] Keep pipeline code in `pipelines/` and declarative specs in `pipeline_specs/`.
- [ ] Keep fixtures in `tests/fixtures/` or `fixtures/` and reference them from tests.
- [ ] Assert lifecycle phase order and quarantine/blocker routing.
- [ ] Assert evidence, policy, receipt, release, correction, and rollback separation.
- [ ] Assert no pipeline test treats a successful run as publication or public truth.
- [ ] Do not store real source data, receipts, proofs, release records, policy rules, schemas, contracts, implementation code, secrets, production logs, generated artifacts, or direct model output here.
- [ ] Link tests to fixtures, specs, pipeline lanes, contracts, schemas, policy gates, and release gates after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; greenfield stub replaced. |
| `tests/pipelines/` placement | CONFIRMED in `tests/README.md` proposed tree. |
| Pipeline root boundary | CONFIRMED in `pipelines/README.md`. |
| Executable test inventory | NEEDS VERIFICATION. |
| Actual runner/framework | NEEDS VERIFICATION. |
| Fixture consumption | NEEDS VERIFICATION. |
| Pipeline/spec bindings | NEEDS VERIFICATION. |
| Schema bindings | NEEDS VERIFICATION. |
| Policy/runtime wiring | NEEDS VERIFICATION. |
| CI wiring and pass rates | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
