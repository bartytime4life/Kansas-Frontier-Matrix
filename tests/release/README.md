<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-release-readme
title: Release Tests README
type: test-readme
version: v0.1
status: draft; placeholder-replaced; release-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - QA steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; release; release-gates; promotion; correction; rollback; no-network; synthetic-only; evidence-aware; policy-aware; fail-closed
tags: [kfm, tests, release, promotion, release-manifest, rollback, correction, withdrawal, supersession, release-gates, no-network, HELD, APPROVED, RELEASED, CORRECTED, SUPERSEDED, WITHDRAWN, DENY, ERROR]
related:
  - ../README.md
  - ../fixtures/README.md
  - ../../release/README.md
  - ../../contracts/release/README.md
  - ../../schemas/contracts/v1/release/
  - ../../policy/release/
  - ../../policy/promotion/
  - ../../data/receipts/release/
  - ../../data/proofs/
  - ../../fixtures/release/
notes:
  - "This README replaces placeholder content at tests/release/README.md."
  - "This lane documents executable release-governance tests. It is not release authority; release decisions, manifests, correction records, notices, changelog entries, and rollback records belong under release/."
  - "Release tests should prove gate behavior without turning a passing test, generated report, fixture, manifest shape, or readiness check into release approval or publication."
  - "Executable test inventory, actual runner/framework, fixture consumption, schema bindings, policy/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Release tests

> Test-lane README for release-governance checks under `tests/release/`. This lane proves that release candidates, reviews, promotion decisions, manifests, corrections, withdrawals, supersessions, rollback posture, and publication gates behave as governed state transitions without becoming release records or release approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: release tests" src="https://img.shields.io/badge/lane-release__tests-purple">
  <img alt="Invariant: not a file move" src="https://img.shields.io/badge/promotion-not__a__file__move-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/release/README.md`  
**Status:** draft / placeholder replaced / release test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `release`  
**Release authority root:** `release/`  
**Default posture:** deterministic, synthetic, no-network, release-gate tests only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/` validates `release/` manifests, rollback, corrections, and promotion gates; CONFIRMED `release/` is the release-governance root distinct from `data/published/`; NEEDS VERIFICATION for executable test inventory, actual runner/framework, fixtures, schema bindings, policy/runtime wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/release/` for tests that verify release-governance behavior.

In scope:

- release-manifest validation tests;
- promotion-decision and release-decision gate tests;
- candidate, review, manifest, decision, correction, notice, changelog, signature, withdrawal, supersession, and rollback-card tests;
- tests that prove release records require evidence, validation, policy, stewardship, correction, and rollback pointers where material;
- tests that prove candidates, reviews, manifests, publish-readiness checks, and changelog entries do not become release approval by themselves;
- tests that prove release states are finite and auditable;
- tests that consume synthetic fixtures from `tests/fixtures/`, root `fixtures/`, or `fixtures/release/` after verification.

Out of scope:

- actual release records or release decisions;
- published artifacts or data payloads;
- schemas, contracts, policy rules, or release implementation code;
- lifecycle data, source records, EvidenceBundles, receipts, proofs, production logs, secrets, public exports, or generated CI artifacts.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Release-governance tests | `tests/release/` | This lane. |
| Release records and decisions | `release/` | Authority root; tests verify behavior, not decisions. |
| Release object meaning | `contracts/release/` | Semantic authority; tests reference. |
| Release schemas | `schemas/contracts/v1/release/` | Machine-shape authority; tests reference. |
| Release and promotion policy | `policy/release/`, `policy/promotion/`, and related policy roots | Gate authority; tests assert behavior. |
| Release receipts/proofs | `data/receipts/`, `data/proofs/` | Auditable trust artifacts; not authored here. |
| Unit-test fixtures | `tests/fixtures/` | Test-local inputs. |
| Cross-cutting fixtures | `fixtures/` and `fixtures/release/` | Shared synthetic examples. |
| Published payloads | `data/published/` and governed artifact roots | Release target outputs; not stored here. |

> [!IMPORTANT]
> `tests/release/` must not become a release record store, publication lane, schema home, policy home, contract home, evidence/proof store, fixture archive, or generated artifact authority. Tests can block promotion; they do not approve release.

---

## Release-test rule

Release tests prove that release governance is enforceable. A passing test may support a gate, but it is not release approval.

Core expectations:

| Expectation | Required posture |
|---|---|
| Governed transition | Promotion and publication are state transitions, not file moves. |
| Evidence linkage | Release claims that depend on evidence require evidence pointers. |
| Validation linkage | Release targets require validation pointers where validation is material. |
| Policy linkage | Rights, sensitivity, access, and public-surface posture require policy review pointers. |
| Steward decision | Release-state changes require steward decision records where material. |
| Rollback/correction | Correction, withdrawal, supersession, rollback, and notice paths remain visible. |
| Finite state | Expected release states are explicit and bounded. |
| No-network default | Default tests use synthetic fixtures and no live source, API, tile, model, vendor, or public-service calls. |

---

## Expected test families

| Family | What it proves | Expected outcome |
|---|---|---|
| `candidate_not_release` | Candidate review packet is not public release by itself. | validation failure if treated as release. |
| `review_not_approval` | Review support record is not approval by itself. | `HELD` / validation failure. |
| `promotion_decision_required` | Promotion needs explicit decision record. | `HELD` / validation failure. |
| `manifest_required_refs` | Manifest includes required target, evidence, validation, policy, decision, correction, and rollback refs where material. | `PASS` / validation failure. |
| `policy_review_required` | Rights, sensitivity, access, or public-surface release requires policy review. | `HELD` / `DENY`. |
| `release_state_finite` | Release state is one of the accepted finite states. | `PASS` / `ERROR`. |
| `rollback_card_required` | Public-facing release target has rollback target where material. | `PASS` / validation failure. |
| `correction_visible` | Correction and notice paths remain linked and visible. | `CORRECTED` / `PASS`. |
| `withdrawal_or_supersession` | Withdrawal or supersession is explicit, auditable, and reversible where possible. | `WITHDRAWN` / `SUPERSEDED`. |
| `published_payload_separate` | `release/` records do not duplicate published data payloads. | validation failure if duplicated. |

---

## Accepted inputs

Accepted material is limited to executable tests, lane-local notes, and tiny synthetic inline values when they are too small to justify fixture files.

Preferred fixture inputs should be referenced from:

- `tests/fixtures/` for test-local fixtures;
- `fixtures/release/` for shared release fixtures;
- `fixtures/release/promotion_decision/` for promotion-decision examples when applicable;
- `schemas/contracts/v1/release/` for schema references;
- `contracts/release/` for semantic contract references;
- `policy/release/` and `policy/promotion/` for gate behavior references.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| release records, manifests, decisions, correction notices, rollback cards, changelog entries | `release/` |
| release object contracts | `contracts/release/` |
| release schemas | `schemas/contracts/v1/release/` |
| release or promotion policy rules | `policy/release/`, `policy/promotion/` |
| fixture payload collections | `tests/fixtures/`, `fixtures/`, or `fixtures/release/` |
| receipts, proofs, EvidenceBundles | `data/receipts/`, `data/proofs/` |
| raw/work/quarantine/processed/catalog/triplet/published data payloads | governed `data/` lifecycle roots |
| release implementation code | `packages/release/`, `apps/`, `pipelines/`, or accepted implementation roots |
| generated CI reports, public exports, screenshots, secrets, production logs, direct model output | not allowed in this test lane |

---

## Suggested layout

```text
tests/release/
|-- README.md
|-- candidate_not_release.test.PROPOSED
|-- review_not_approval.test.PROPOSED
|-- promotion_decision_required.test.PROPOSED
|-- manifest_required_refs.test.PROPOSED
|-- policy_review_required.test.PROPOSED
|-- release_state_finite.test.PROPOSED
|-- rollback_card_required.test.PROPOSED
|-- correction_visible.test.PROPOSED
|-- withdrawal_or_supersession.test.PROPOSED
`-- published_payload_separate.test.PROPOSED
```

The layout is schematic. Actual test filenames, extensions, package manager, runner, and framework remain NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/release
```

Default runs should be deterministic, local, no-network, public-safe, and finite-state only. Replace the command once the repo's actual test runner and naming convention are verified.

---

## Maintenance checklist

- [ ] Keep release decisions and release records under `release/`, not `tests/release/`.
- [ ] Keep fixtures in `tests/fixtures/` or `fixtures/` and reference them from tests.
- [ ] Assert that candidate, review, manifest, readiness, and changelog records do not equal release approval by themselves.
- [ ] Assert evidence, validation, policy, steward decision, correction, notice, signature, and rollback pointers where material.
- [ ] Assert finite release states and fail-closed behavior for missing support.
- [ ] Do not store real source data, published artifacts, release records, receipts, proofs, schemas, contracts, policy rules, implementation code, secrets, production logs, generated artifacts, or direct model output here.
- [ ] Link tests to fixtures, contracts, schemas, policy gates, release lanes, receipts, and proofs after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| `tests/` authority | CONFIRMED as canonical enforceability root. |
| `release/` authority | CONFIRMED as release-governance root. |
| Release contract boundary | CONFIRMED as semantic-contract lane, not release authority. |
| Executable test inventory | NEEDS VERIFICATION. |
| Actual runner/framework | NEEDS VERIFICATION. |
| Fixture consumption | NEEDS VERIFICATION. |
| Schema bindings | NEEDS VERIFICATION. |
| Policy/runtime wiring | NEEDS VERIFICATION. |
| CI wiring and pass rates | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
