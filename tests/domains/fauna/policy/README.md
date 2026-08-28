<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/policy/readme
title: Fauna Policy Test Lane README
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
verification_status: current-session path verified; executable tests, fixtures, policy modules, validators, receipts, release gates, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - tests/domains/fauna/policy/redaction/README.md
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
  - sensitivity
  - geoprivacy
  - redaction
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Policy Tests

> Parent test-lane contract for proving Fauna policy behavior fails closed, uses public-safe fixtures, preserves evidence and release boundaries, and never turns tests into policy, receipt, proof, or release authority.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Fpolicy-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Fpolicy-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** parent policy-test README; not a policy bundle, schema, fixture inventory, receipt, proof, release decision, source registry, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `policy/`  
**Default posture:** public-safe transformed fixtures; no-network by default; finite outcomes  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the parent Fauna test lane for **policy behavior**.

It exists to prove that Fauna policy gates are enforced before public exposure, map rendering, evidence display, Focus Mode answers, release promotion, or derived artifact use. The lane verifies behavior; it does not define policy, select disclosure parameters, create receipts, approve releases, or publish data.

A mature parent lane should prove:

1. Policy checks run before public exposure.
2. Missing rights, unresolved sensitivity, missing review, missing evidence, missing receipt, stale support, or missing release state produces a finite negative outcome.
3. Public-safe derived records remain bounded to the approved disclosure scope.
4. Tests call canonical policy, validation, release, evidence, and fixture code from owning roots.
5. Trust-bearing receipts, proofs, and release decisions remain outside `tests/`.
6. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/policy/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna policy behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Policy lane | `policy/` |
| Binding policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Release home | `release/`. |
| Documentation references | `docs/domains/fauna/SENSITIVITY.md` and `docs/domains/fauna/MAP_UI_CONTRACTS.md`. |

> [!WARNING]
> This directory must not become a second policy home, fixture home, receipt home, proof home, release home, source-data home, or public artifact home.

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

This README defines the parent policy test-lane contract. It does not claim that policy modules, fixtures, receipts, release manifests, or CI checks already exist.

---

## 4. Parent policy rule

**Rule:** Fauna policy tests must prove that public exposure is allowed only when policy, evidence, rights, review, receipt, release, and correction requirements are satisfied for the tested scope.

Tests should fail or produce a finite negative outcome when:

- rights are unknown or unresolved;
- sensitivity is unresolved;
- required review is absent;
- required evidence or receipt references are missing;
- release state is missing, withdrawn, stale, or out of scope;
- output exceeds its approved public-safe scope;
- policy behavior is implemented only in UI styling or presentation code;
- a public client would receive internal lifecycle material; or
- a denied case returns a public answer, public layer, or published state.

Tests may allow an output only when the fixture is public-safe, policy permits it, required governance references are present, and the test remains inside its validation scope.

---

## 5. Child lanes

| Child lane | Responsibility | Status boundary |
|---|---|---|
| `redaction/` | Prove redaction and public-safe disclosure policy behavior. | README work may exist in an open PR; executable tests NEEDS VERIFICATION. |
| `rights/` | Prove rights state blocks or permits use. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `review/` | Prove review-state gates are enforced. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `release/` | Prove policy works with release and rollback state. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `evidence/` | Prove evidence support is required before claims answer. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `ui-boundary/` | Prove UI styling is not policy enforcement. | PROPOSED / NEEDS VERIFICATION unless implemented. |

Additional child lanes may be added when they have a clear policy-test responsibility and do not duplicate an authority root.

---

## 6. Parent proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Missing rights state | Rights gap blocks public exposure. | `DENY`, `ABSTAIN`, `ERROR`, or validation failure. |
| Unresolved sensitivity | Policy cannot prove safe disclosure. | Fail closed. |
| Missing review | Required reviewer state absent. | `DENY`, `HOLD`, or validation failure. |
| Missing evidence support | Evidence-dependent answer cannot be supported. | `ABSTAIN`, `ERROR`, or validation failure. |
| Missing receipt reference | Required receipt is not linked. | `ABSTAIN`, `ERROR`, or validation failure. |
| Withdrawn or stale release | Public state no longer current. | `ABSTAIN`, `ERROR`, or correction-aware outcome. |
| Disclosure-scope overflow | Output exceeds approved public-safe scope. | Test failure or `DENY`. |
| UI-only protection | Presentation-only guard is treated as insufficient. | Test failure. |
| Public-safe allowed case | Required policy, review, evidence, receipt, and release hooks are present. | Allowed for test scope only. |
| No-network default | Test uses deterministic local fixtures only. | Harness guard. |

---

## 7. What belongs here

This directory may contain:

- README and parent-lane contract material for Fauna policy tests.
- Tests that call canonical policy and validator code from owning roots.
- Negative tests for missing rights, unresolved sensitivity, missing review, missing evidence, missing receipt, withdrawn release, stale support, and over-broad disclosure.
- Positive tests for public-safe fixtures with required governance references.
- Child-lane READMEs for focused policy concerns.
- Public-safe test-local examples when they are tiny, deterministic, and not reusable fixture inventory.

## 8. What does not belong here

This directory must not contain production policy definitions, source records, public artifacts, reusable fixture inventories, receipts, proofs, release decisions, rollback decisions, disclosure parameters, or default tests that require live network access.

---

## 9. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model governance states rather than include non-public source material.

Expected fixture families include allowed public-safe cases, unresolved rights, unresolved sensitivity, missing review, missing evidence, missing receipt, withdrawn release, stale support, and disclosure-scope boundary cases.

---

## 10. Suggested local commands

> [!NOTE]
> Command names, policy module names, validator names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna/policy
pytest tests/domains/fauna/policy/redaction
pytest tests/domains/fauna
python tools/validate_all.py
```

---

## 11. Open questions

| Question | Status | Notes |
|---|---|---|
| Which policy modules own Fauna policy decisions? | NEEDS VERIFICATION | Must inspect policy roots. |
| Which receipt schema/path is canonical for policy-gated disclosure? | NEEDS VERIFICATION | Do not invent payload shape here. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which validator command is canonical? | NEEDS VERIFICATION | Must inspect validator roots. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared cross-domain policy tests live here or under a cross-domain policy test root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 12. Definition of done

This parent lane is mature when:

- [ ] Fauna policy tests run locally.
- [ ] Redaction and other active child lanes have executable proof where implementation exists.
- [ ] Missing rights, unresolved sensitivity, missing review, missing evidence, missing receipt, withdrawn release, stale support, and disclosure-scope boundary cases are tested.
- [ ] Positive public-safe fixtures prove allowed behavior without becoming release approval.
- [ ] Tests call canonical policy/validator code rather than redefining policy locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Fauna policy proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 13. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna policy parent test lane. |

---

## 14. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy/domain tests, and Fauna sensitivity doctrine; executable tests, fixtures, policy modules, validators, receipts, release gates, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
