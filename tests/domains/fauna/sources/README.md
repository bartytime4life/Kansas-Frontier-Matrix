<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/sources/readme
title: Fauna Sources Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Source steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, source descriptors, source activation decisions, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/SOURCE_REGISTRY.md
  - docs/domains/fauna/SENSITIVITY.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - data/registry/sources/fauna/
  - fixtures/domains/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - data/receipts/
  - data/proofs/fauna/
tags:
  - kfm
  - tests
  - fauna
  - sources
  - source-descriptor
  - source-role
  - source-activation
  - source-intake
  - rights
  - freshness
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Sources Tests

> Test-lane contract for proving Fauna source admission, source-role boundaries, rights/freshness/sensitivity gates, and watcher behavior are governed before any source can support public claims.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Fsources-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Fsources-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** source test-lane README; not a source registry, source descriptor, activation decision, schema, policy bundle, fixture inventory, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `sources/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when source admission is unresolved  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Fauna domain test lane for **source governance**.

It exists to prove that Fauna sources are not accepted as authority merely because they are available, convenient, or well-known. Source material can support public claims only after source identity, role, rights, cadence, freshness, sensitivity, activation state, evidence closure, policy review, and release state are governed through the proper roots.

A mature lane should prove:

1. Source descriptors are required before source material enters governed intake.
2. Source activation decisions gate connector and watcher activation.
3. Source role is checked against claim type and cannot be inferred from convenience.
4. Rights, sensitivity, freshness, and contact/cadence metadata fail closed when unresolved.
5. Watchers produce candidate intake records only; they do not admit, promote, or publish.
6. Registry records remain in `data/registry/sources/fauna/`; tests only verify behavior.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/sources/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna source-governance behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Test lane | `sources/` |
| Machine source registry home | `data/registry/sources/fauna/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Documentation reference | `docs/domains/fauna/SOURCE_REGISTRY.md`. |

> [!WARNING]
> This directory must not become a second source registry, descriptor home, activation-decision home, fixture home, policy home, receipt home, proof home, release home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows policy, evidence-resolution, lifecycle, receipt/proof, governed API, UI trust-state, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` requires public-safe transformed fixtures for sensitive lanes and no live network by default | CONFIRMED from current repo docs. |
| Fauna Source Registry says source registry is an admission and authority-control surface, not a bibliography | CONFIRMED from current repo docs. |
| Fauna Source Registry says machine-readable descriptors belong under `data/registry/sources/fauna/` | CONFIRMED from current repo docs. |
| Fauna Source Registry says watchers do not promote or publish | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual source descriptor schemas, activation-decision schemas, and validators | NEEDS VERIFICATION. |
| Actual fixture inventory | NEEDS VERIFICATION. |
| Actual CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that source descriptor instances, activation decisions, validators, fixtures, or CI checks already exist.

---

## 4. Source rule

**Rule:** A Fauna source may support public claims only when descriptor, activation, role, rights, freshness, sensitivity, evidence, policy, and release requirements are satisfied for the tested scope.

Tests should fail or produce a finite negative outcome when:

- source identity is missing or unstable;
- source role is absent, ambiguous, or incompatible with the claim type;
- rights, attribution, or redistribution status is unresolved;
- sensitivity state is unresolved;
- source freshness or cadence is missing where material;
- source activation state is absent, denied, restricted beyond the requested use, or pending review;
- watcher output is treated as admitted truth;
- intake metadata is treated as evidence closure;
- registry records are duplicated under `tests/`; or
- public surfaces use source material before evidence closure and release state are complete.

Tests may allow source-supported output only when the fixture is public-safe, policy permits it, source role matches the claim, required governance references are present, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Descriptor required | Source fixture has governed identity, role, rights, cadence, contact, and source-head fields where required. | Schema/validator assertion. |
| Activation decision | Source use is allowed only by activation state for the tested use. | Activation assertion. |
| Role × claim match | Source role is compatible with claim type. | `DENY`, `ABSTAIN`, `ERROR`, or validation failure if mismatched. |
| Rights state | Unknown or restricted rights block public use unless policy permits the tested scope. | Fail closed. |
| Sensitivity state | Unresolved sensitivity blocks public support. | Fail closed. |
| Freshness/cadence | Stale or untracked source state is visible and bounded. | Freshness assertion. |
| Watcher boundary | Watcher emits candidate intake only. | No publication or admission side effect. |
| Evidence boundary | Intake/source metadata is not treated as EvidenceBundle support. | Evidence-resolution assertion. |
| Registry boundary | Tests reference registry fixtures but do not redefine registry authority. | Placement assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Fauna source-governance tests.
- Tests that call canonical source descriptor, activation, policy, evidence, and validator code from owning roots.
- Negative tests for missing descriptor fields, ambiguous roles, incompatible role/claim pairs, unresolved rights, stale source state, unresolved sensitivity, and watcher overreach.
- Positive tests for public-safe source fixtures with required governance references.
- Public-safe test-local examples when they are tiny, deterministic, and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain production source descriptors, activation decisions, raw source records, live source data, reusable fixture inventories, receipts, proofs, release decisions, policy definitions, schemas, credentials, or default tests that require live network access.

---

## 8. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model source-governance states rather than include live source material.

Expected fixture families include valid public-safe descriptor, missing role, incompatible role/claim pair, missing rights, unresolved sensitivity, stale source head, denied activation, restricted activation, watcher candidate, and synthetic source with explicit reality boundary.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, source validator names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna/sources
pytest tests/domains/fauna
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical SourceDescriptor schema/path? | NEEDS VERIFICATION | Must inspect source schema roots. |
| What is the canonical SourceActivationDecision schema/path? | NEEDS VERIFICATION | Must inspect source schema roots. |
| Which validator command owns source admission checks? | NEEDS VERIFICATION | Must inspect validator roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared source-descriptor tests live here or under a cross-domain source test root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Fauna source tests run locally.
- [ ] Missing descriptor, role mismatch, unresolved rights, unresolved sensitivity, stale source, denied activation, restricted activation, and watcher overreach cases are tested.
- [ ] Positive public-safe fixtures prove allowed source behavior without becoming admission or release approval.
- [ ] Tests call canonical source/policy/evidence validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Fauna source-governance proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna sources test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy/evidence/lifecycle/domain tests, and Fauna source registry doctrine; executable tests, fixtures, source descriptor schemas, activation decisions, validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
