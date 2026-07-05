<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/policy/redaction/readme
title: Fauna Policy Redaction Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Sensitivity reviewer>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, policy modules, validators, receipts, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/SENSITIVITY.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - fixtures/domains/fauna/
  - data/receipts/
  - data/proofs/fauna/
  - release/
tags:
  - kfm
  - tests
  - fauna
  - policy
  - redaction
  - geoprivacy
  - sensitivity
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Policy Redaction Tests

> Test-lane contract for proving Fauna redaction policy fails closed, uses public-safe fixtures, requires governed review/receipt boundaries, and never turns tests into policy, receipt, proof, or release authority.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Fpolicy%2Fredaction-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Fpolicy%2Fredaction-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** policy-test README; not a policy bundle, schema, fixture inventory, receipt, proof, release decision, source registry, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `policy/redaction/`  
**Default posture:** public-safe transformed fixtures; no-network by default; finite outcomes  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Fauna policy test lane for **redaction behavior**.

It exists to prove that Fauna policy decisions involving sensitive or protected records fail closed unless the required governance conditions are present. The lane verifies behavior; it does not define policy, choose transform parameters, create receipts, approve release, or publish data.

A mature lane should prove:

1. Redaction policy is checked before public exposure.
2. Missing rights, unresolved sensitivity, missing review, missing receipt, or missing release state blocks public promotion.
3. Public-safe derived records remain bounded to the approved disclosure scope.
4. Redaction receipts and review records are required where policy requires them, but trust-bearing records do not live in this test tree.
5. Negative outcomes are finite and inspectable: `ABSTAIN`, `DENY`, or `ERROR`, not guessed-safe answers.
6. Tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/policy/redaction/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna redaction policy behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Policy lane | `policy/redaction/` |
| Binding policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Release home | `release/`. |
| Documentation references | `docs/domains/fauna/SENSITIVITY.md` and `docs/domains/fauna/MAP_UI_CONTRACTS.md`. |

> [!WARNING]
> This directory must not become a second policy home, fixture home, receipt home, proof home, release home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows policy tests and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` requires public-safe transformed fixtures for sensitive lanes | CONFIRMED from current repo docs. |
| Fauna sensitivity doc says binding rules live under policy roots | CONFIRMED from current repo docs. |
| Fauna sensitivity doc says exposure-aiding parameters should not be stated in docs | CONFIRMED from current repo docs. |
| Fauna sensitivity doc says governed transitions require artifacts and review and are reversible | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual policy modules and validator commands | NEEDS VERIFICATION. |
| Actual fixture inventory | NEEDS VERIFICATION. |
| Actual receipt payloads and release gates | NEEDS VERIFICATION. |
| Actual CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that redaction policy modules, fixtures, receipts, release manifests, or CI checks already exist.

---

## 4. Redaction policy rule

**Rule:** A Fauna record may move toward public exposure only when policy, review, receipt, rights, and release requirements are satisfied for the tested scope.

Tests should fail or produce a finite negative outcome when:

- rights are unknown or unresolved;
- sensitivity is unresolved;
- required review is absent;
- required receipt references are missing;
- release state is missing, withdrawn, or out of scope;
- a public-safe derivative exceeds its approved disclosure scope;
- policy behavior is implemented only in UI styling or presentation code;
- test fixtures contain non-public source material; or
- a policy-denied case returns a public answer or published layer state.

Tests may allow an output only when the fixture is public-safe, policy permits it, required governance references are present, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Missing rights state | Rights gap blocks public exposure. | `DENY`, `ABSTAIN`, `ERROR`, or validation failure. |
| Unresolved sensitivity | Policy cannot prove safe disclosure. | Fail closed. |
| Missing review | Required reviewer state absent. | `DENY`, `HOLD`, or validation failure. |
| Missing receipt reference | Required transform/process receipt not linked. | `ABSTAIN`, `ERROR`, or validation failure. |
| Withdrawn or stale release | Public state no longer current. | `ABSTAIN`, `ERROR`, or correction-aware outcome. |
| Disclosure-scope overflow | Output exceeds approved public-safe scope. | Test failure or `DENY`. |
| UI-only protection | Presentation-only guard is treated as insufficient. | Test failure. |
| Public-safe allowed case | All required policy, review, receipt, and release hooks present. | Allowed for test scope only. |
| No-network default | Test uses deterministic local fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Fauna redaction policy tests.
- Tests that call canonical policy and validator code from owning roots.
- Negative tests for missing rights, unresolved sensitivity, missing review, missing receipt, withdrawn release, and over-broad disclosure.
- Positive tests for public-safe fixtures with required governance references.
- Public-safe test-local examples when they are tiny, deterministic, and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain production policy definitions, source records, public artifacts, reusable fixture inventories, receipts, proofs, release decisions, rollback decisions, transform parameters, or default tests that require live network access.

---

## 8. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model governance states rather than include non-public source material.

Expected fixture families include allowed public-safe cases, unresolved rights, unresolved sensitivity, missing review, missing receipt, withdrawn release, and disclosure-scope boundary cases.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, policy module names, validator names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna/policy/redaction
pytest tests/domains/fauna/policy
pytest tests/domains/fauna
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which policy module owns Fauna redaction decisions? | NEEDS VERIFICATION | Must inspect policy roots. |
| Which receipt schema/path is canonical for redaction evidence? | NEEDS VERIFICATION | Do not invent payload shape here. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which validator command is canonical? | NEEDS VERIFICATION | Must inspect validator roots. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Fauna redaction policy tests run locally.
- [ ] Missing rights, unresolved sensitivity, missing review, missing receipt, withdrawn release, and disclosure-scope boundary cases are tested.
- [ ] Positive public-safe fixtures prove allowed behavior without becoming release approval.
- [ ] Tests call canonical policy/validator code rather than redefining policy locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the redaction-policy proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna policy redaction test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy/domain tests, and Fauna sensitivity/redaction doctrine; executable tests, fixtures, policy modules, validators, receipts, release gates, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
