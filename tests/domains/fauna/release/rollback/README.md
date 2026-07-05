<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/release/rollback/readme
title: Fauna Release Rollback Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Release steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, rollback cards, release manifests, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/RELEASE_INDEX.md
  - docs/domains/fauna/SENSITIVITY.md
  - docs/runbooks/fauna/ROLLBACK_RUNBOOK.md
  - release/
  - release/candidates/fauna/
  - data/published/layers/fauna/
  - data/receipts/
  - data/proofs/fauna/
  - fixtures/domains/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
tags:
  - kfm
  - tests
  - fauna
  - release
  - rollback
  - correction
  - release-manifest
  - rollback-card
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Release Rollback Tests

> Test-lane contract for proving Fauna release rollback behavior is governed, reversible, evidence-preserving, policy-aware, and never reduced to a hidden file move.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Frelease%2Frollback-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Frelease%2Frollback-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** rollback test-lane README; not a rollback card, release manifest, correction notice, policy bundle, fixture inventory, receipt, proof, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `release/rollback/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed for sensitive-lane defects  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Fauna release test sublane for **rollback behavior**.

It exists to prove that a Fauna release can be withdrawn, superseded, corrected, or rolled back through governed records and public-safe state transitions. The lane verifies rollback behavior; it does not execute rollback, create rollback cards, alter release state, publish artifacts, or store trust-bearing receipts/proofs.

A mature lane should prove:

1. Every public Fauna release has a rollback target before publication.
2. Rollback is a governed state transition, not a file move.
3. Correction and rollback preserve lineage, evidence, review, policy, and release state.
4. Public surfaces fail closed when a rollback-triggering defect is detected.
5. Rollback target artifacts are re-checked under current policy before reuse.
6. Downstream public surfaces, Focus Mode answers, evidence drawers, tiles, indexes, and derived layers do not continue serving invalidated support.
7. Tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/release/rollback/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna rollback behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Release lane | `release/rollback/` |
| Release decision home | `release/` when present. |
| Published artifact home | `data/published/layers/fauna/` when present. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Human runbook/index references | `docs/runbooks/fauna/ROLLBACK_RUNBOOK.md` and `docs/domains/fauna/RELEASE_INDEX.md`. |

> [!WARNING]
> This directory must not become a second release home, rollback-card home, correction-notice home, published-artifact home, fixture home, receipt home, proof home, policy home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows release-manifest, receipt/proof, lifecycle-state, governed API, UI trust-state, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive exact data and trust-bearing release decisions from `tests/` | CONFIRMED from current repo docs. |
| Fauna Release Index says release decisions, published artifacts, rollback cards, and correction notices live in separate authority homes | CONFIRMED from current repo docs. |
| Fauna sensitivity doc says release transitions are governed, reviewed, and reversible | CONFIRMED from current repo docs. |
| Fauna rollback runbook says rollback is governed and not a hidden-file-copy procedure | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual rollback card schema/path and validator command | NEEDS VERIFICATION. |
| Actual fixtures and rollback test manifests | NEEDS VERIFICATION. |
| Actual CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that rollback implementation, release manifests, rollback cards, fixtures, validators, or CI checks already exist.

---

## 4. Rollback rule

**Rule:** A Fauna release can be rolled back only through governed rollback/correction/release state, with evidence, review, policy, and downstream invalidation preserved.

Tests should fail or require a finite negative outcome when:

- a release lacks a rollback target;
- a rollback target cannot be resolved or verified;
- rollback is represented as an undocumented artifact swap;
- a prior target is reused without current policy/review checks;
- invalidated evidence remains available to public Focus Mode, Evidence Drawer, layer catalog, or API surfaces;
- a correction or withdrawal does not leave auditable lineage;
- trust-bearing rollback records are stored under `tests/`; or
- public output continues after a rollback-triggering defect should have blocked it.

Tests may allow rollback behavior only when the fixture demonstrates public-safe, auditable, reversible state transitions with required references present for the tested scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Rollback target exists | Release fixture links to a prior safe target. | Validation passes for test scope. |
| Target resolves | Referenced target can be resolved by canonical code. | Resolution assertion. |
| Target rechecked | Current policy/review gates are applied before reuse. | Fail closed if unresolved. |
| Release lineage | Superseded/withdrawn/corrected state preserves lineage. | Lineage assertion. |
| Public surface invalidation | API/UI/layer/Focus surfaces stop serving invalidated support. | `DENY`, `ABSTAIN`, `ERROR`, or safe correction state. |
| Evidence boundary | Invalidated evidence is not cited as current support. | Evidence-resolution assertion. |
| Receipt/proof boundary | Tests assert references but do not store trust-bearing records. | Placement assertion. |
| Sensitive-lane defect | Public surface fails closed first. | Deny/disable behavior for test scope. |
| No-network default | Tests use deterministic local public-safe fixtures. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Fauna rollback tests.
- Tests that call canonical release, rollback, correction, policy, evidence, and validator code from owning roots.
- Negative tests for missing rollback targets, unresolved targets, stale targets, invalidated evidence, missing lineage, missing review, and dangling downstream public surfaces.
- Positive tests for public-safe rollback fixtures with required governance references.
- Public-safe test-local examples when they are tiny, deterministic, and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain production release manifests, rollback cards, correction notices, published artifacts, source records, reusable fixture inventories, receipts, proofs, policy definitions, rollback decisions, or default tests that require live network access.

---

## 8. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model release and rollback states without carrying trust-bearing decisions or non-public source material.

Expected fixture families include valid rollback target, missing rollback target, unresolved target, withdrawn release, superseded release, invalidated evidence, downstream stale answer, current-policy recheck failure, and successful public-safe rollback lineage.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, release validator names, rollback schema names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna/release/rollback
pytest tests/domains/fauna/release
pytest tests/domains/fauna
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical rollback-card schema/path? | NEEDS VERIFICATION | Must inspect release schema roots. |
| Which validator command owns rollback checks? | NEEDS VERIFICATION | Must inspect validator roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which public surfaces are included in rollback invalidation tests? | NEEDS VERIFICATION | Must inspect API/UI/layer implementation. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared release rollback tests live here or in a cross-domain release test root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Fauna rollback tests run locally.
- [ ] Missing target, unresolved target, stale target, invalidated evidence, missing lineage, missing review, and dangling downstream surface cases are tested.
- [ ] Positive public-safe fixtures prove allowed rollback behavior without becoming release approval.
- [ ] Tests call canonical release/rollback/policy/evidence validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Fauna rollback proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna release rollback test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for release/lifecycle/receipt/proof/domain tests, and Fauna rollback doctrine; executable tests, fixtures, rollback cards, release manifests, validators, public-surface invalidation, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
