<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-valid-readme
title: Valid Tests README
type: test-readme
version: v0.1
status: draft; blank-placeholder-replaced; valid-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Schema steward
  - OWNER_TBD - Contract steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-doc; tests; valid; positive-path-tests; no-network; synthetic-only; trust-spine
tags: [kfm, tests, valid, positive-path, fixtures, PASS, ANSWER, NEEDS_VERIFICATION]
related:
  - ../README.md
  - ../invalid/README.md
  - ../fixtures/README.md
  - ../../fixtures/
  - ../../schemas/
  - ../../contracts/
  - ../../policy/
  - ../../release/
notes:
  - "This README replaces blank placeholder content at tests/valid/README.md."
  - "This lane documents positive-path executable tests, not fixture payloads or authority records."
  - "`tests/valid/` is not listed in the proposed tests tree, so this path remains PROPOSED / NEEDS VERIFICATION until maintainers accept it or redirect it to a more specific test lane."
  - "A valid test proves only the gate being tested; it does not by itself prove truth, policy approval, release approval, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Valid tests

> Positive-path test lane for `tests/valid/`. Use this directory only when maintainers want a cross-cutting home for executable tests that prove accepted inputs pass the specific gate under test.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: valid tests" src="https://img.shields.io/badge/lane-valid__tests-2ea44f">
  <img alt="Placement: needs verification" src="https://img.shields.io/badge/placement-NEEDS__VERIFICATION-yellow">
</p>

**Path:** `tests/valid/README.md`  
**Status:** draft / blank placeholder replaced / PROPOSED until placement and executable tests are verified  
**Owning root:** `tests/`  
**Companion lane:** `tests/invalid/`  
**Default posture:** deterministic, synthetic, no-network, public-safe positive-path tests only  
**Truth posture:** CONFIRMED target file existed as blank placeholder content before replacement; CONFIRMED `tests/` is the canonical enforceability root; CONFIRMED `tests/README.md` does not list `tests/valid/` in its proposed tree; CONFIRMED `tests/invalid/` exists as the fail-closed companion lane; NEEDS VERIFICATION for accepted placement, executable inventory, fixture use, runner, CI, and pass rates.

---

## Scope

In scope:

- cross-cutting positive-path tests;
- tests that demonstrate a payload, transition, envelope, or UI state passes the specific gate under test;
- tests that pair with invalid, denied, abstain, or error cases where material;
- lane-local notes that identify expected fixtures and target gates.

Out of scope:

- fixture payload collections;
- schema, contract, policy, release, evidence, proof, receipt, or data authority;
- implementation code;
- generated outputs or production records.

---

## Placement rule

Prefer the most specific test lane when ownership is clear.

| Need | Preferred lane |
|---|---|
| Schema positive path | `tests/schemas/` |
| Contract positive path | `tests/contracts/` |
| Policy allow/restrict path | `tests/policy/` |
| Release gate positive path | `tests/release/` |
| Governed API positive path | `tests/api/` |
| UI trust-state positive path | `tests/ui/` |
| Runtime `ANSWER` proof | `tests/runtime_proof/` |
| Domain-owned positive path | `tests/domains/<domain>/` |
| Cross-cutting positive path | `tests/valid/` if accepted |

---

## Valid-test rule

A valid test proves that a positive path passes one or more named gates. It must not claim more than the gates it exercises.

| Expectation | Required posture |
|---|---|
| Gate-limited claim | Passing one gate does not imply all gates passed. |
| Synthetic inputs | Use toy values or accepted fixtures. |
| Fixture separation | Reusable examples live in `tests/fixtures/` or `fixtures/**/valid/`. |
| Paired coverage | Important positive cases should have negative companions. |
| No bypass | Positive tests still preserve evidence, policy, review, release, correction, and rollback boundaries where material. |

---

## Expected test families

| Family | What it proves |
|---|---|
| `schema_shape_valid` | Shape validation accepts a well-formed payload. |
| `contract_semantics_valid` | Object meaning matches the contract. |
| `evidence_resolves` | Evidence support resolves for the tested scope. |
| `policy_allows` | Policy permits the modeled use. |
| `release_manifest_complete` | Release gate has required support refs. |
| `runtime_answer_valid` | Runtime returns a bounded `ANSWER`. |
| `ui_trust_state_valid` | UI renders trust state visibly. |
| `lifecycle_transition_valid` | Lifecycle transition follows governed phases. |
| `receipt_or_proof_valid` | Receipt/proof object matches the tested run. |
| `rollback_drill_valid` | Rollback target is available in the modeled scenario. |

---

## Suggested layout

```text
tests/valid/
|-- README.md
|-- schema_shape_valid.test.PROPOSED
|-- contract_semantics_valid.test.PROPOSED
|-- evidence_resolves.test.PROPOSED
|-- policy_allows.test.PROPOSED
|-- release_manifest_complete.test.PROPOSED
|-- runtime_answer_valid.test.PROPOSED
|-- ui_trust_state_valid.test.PROPOSED
|-- lifecycle_transition_valid.test.PROPOSED
|-- receipt_or_proof_valid.test.PROPOSED
`-- rollback_drill_valid.test.PROPOSED
```

The layout is schematic. Actual filenames, runner, framework, and CI wiring remain NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/valid
```

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; blank placeholder replaced. |
| `tests/` authority | CONFIRMED as canonical enforceability root. |
| `tests/valid/` placement | NEEDS VERIFICATION; not listed in proposed `tests/README.md` tree. |
| `tests/invalid/` companion lane | CONFIRMED. |
| Shared valid fixture pattern | CONFIRMED from inspected valid fixture README example. |
| Executable test inventory | NEEDS VERIFICATION. |
| Fixture inventory | NEEDS VERIFICATION. |
| Runner and CI | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
