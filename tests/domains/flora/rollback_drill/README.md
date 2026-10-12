<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/rollback-drill/readme
title: Flora Rollback Drill Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Release steward>
  - <PLACEHOLDER — Correction steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, rollback cards, correction notices, release manifests, receipts, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
  - tests/domains/flora/release_manifest/README.md
  - tests/domains/flora/policy/README.md
  - tests/domains/flora/policy_deny/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - fixtures/domains/flora/
  - release/
  - data/receipts/
  - data/proofs/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
tags:
  - kfm
  - tests
  - flora
  - rollback-drill
  - correction
  - release-manifest
  - invalidation
  - audit
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Rollback Drill Tests

> Test-lane contract for proving Flora rollback procedures can be rehearsed safely, verify release targets, preserve audit history, emit correction/invalidation expectations, and fail closed without deleting or hiding published lineage.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Frollback__drill-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Frollback__drill-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** rollback-drill test-lane README; not a rollback decision, rollback-card store, correction-notice store, release home, receipt home, proof home, fixture inventory, production recovery script, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `rollback_drill/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when rollback target, correction notice, invalidation list, release manifest, review state, receipt/proof reference, or policy state is unresolved  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **rollback drills**.

It exists to prove that a Flora rollback can be rehearsed as a governed validation flow before any real release recovery is needed. Rollback drills test that the system can identify the affected release, verify the rollback target, require correction and invalidation records, preserve audit history, and block public-surface changes when prerequisites are missing. They do not perform production rollback and do not create trust-bearing rollback records.

A mature lane should prove:

1. A rollback drill starts from a known release fixture and a target prior release fixture.
2. Rollback is treated as a governed transition, not deletion or manual file recovery.
3. Required correction, invalidation, review, receipt/proof, and release-manifest references are present where required.
4. Dependent public surfaces are identified for invalidation or rebind.
5. Rollback drills preserve prior release lineage and do not rewrite history.
6. Missing rollback prerequisites produce finite negative outcomes.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/rollback_drill/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora rollback-drill behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `rollback_drill/` |
| Release home | `release/`. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/flora/`. |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Policy homes | `policy/domains/flora/` and `policy/sensitivity/flora/`. |
| Related release tests | `tests/domains/flora/release_manifest/`. |

> [!WARNING]
> This directory must not become a second release home, rollback-card store, correction-notice store, receipt home, proof home, fixture inventory, production recovery script home, policy home, public artifact home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows lifecycle, receipt/proof, release-manifest, policy, governed API, UI trust-state, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes trust-bearing receipts, proofs, release decisions, live network calls, duplicate authority homes, and generated artifacts from `tests/` | CONFIRMED from current repo docs. |
| Flora docs anchor Flora to the trust spine ending in `ReleaseManifest → RollbackCard` | CONFIRMED from current repo docs. |
| Flora publication docs say correction is governed forward transition, not silent edit | CONFIRMED from current repo docs. |
| Flora publication docs say rollback emits `RollbackCard`, `CorrectionNotice`, invalidation list, and reverts the `ReleaseManifest` to a prior release | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual rollback-card schema, correction-notice schema, release manifests, fixtures, validators, receipts, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that rollback-drill tests, fixtures, validators, rollback cards, correction notices, release manifests, receipts, proofs, or CI checks already exist.

---

## 4. Rollback-drill rule

**Rule:** A Flora rollback drill may pass only when the rollback target is explicit and resolvable, correction and invalidation expectations are present, release-manifest effects are bounded, policy/review requirements are checked, and no audit history is deleted or hidden.

Tests should fail or require a finite negative outcome when:

- current release fixture is missing or ambiguous;
- target prior release is missing, unresolved, or incompatible;
- rollback reason, correction notice, invalidation list, review state, or rollback card reference is missing where required;
- release-manifest change is not bounded to the intended prior target;
- dependent artifacts, layers, tiles, caches, drawer payloads, Focus outputs, or exports are not listed for invalidation where required;
- rollback is modeled as file deletion, silent edit, or floating latest-pointer change;
- rollback drill bypasses policy, evidence, rights, sensitivity, review, receipt/proof, or release checks;
- production rollback records, trust-bearing receipts, proofs, or release decisions are stored under `tests/`; or
- default tests require live services, credentials, or production artifacts.

Tests may allow a drill pass only when the fixture is public-safe, no-network, fully bounded, and the rollback remains a rehearsal rather than a production state transition.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Current release known | Drill starts from a resolvable release fixture. | Release assertion. |
| Target release known | Prior target is explicit and resolves. | Rollback target assertion. |
| Correction notice required | Correction expectation is present where required. | Correction assertion. |
| Invalidation list | Dependent outputs are listed for invalidation. | Invalidation assertion. |
| Review state | Required review state exists before rollback authorization. | Review assertion. |
| Receipt/proof reference | Drill checks required audit references without storing them here. | Receipt/proof boundary assertion. |
| Manifest rebind | Release manifest effect points to intended prior target only. | Manifest assertion. |
| No silent deletion | Prior/current lineage remains auditable. | Audit assertion. |
| Public surface hold | Public surface remains held when prerequisites fail. | `DENY`, `ABSTAIN`, `ERROR`, or hold assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Flora rollback-drill tests.
- Tests that call canonical release, rollback, correction, evidence, policy, review, receipt/proof, UI/API, and validator code from owning roots.
- Negative tests for missing target, unresolved target, missing correction notice, missing invalidation list, missing review, missing receipt/proof reference, silent deletion, floating latest-pointer rollback, and direct public-surface mutation.
- Positive drill tests using public-safe fixtures that prove bounded rollback readiness without performing production rollback.
- Tiny test-local examples when documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain production rollback records, rollback cards, correction notices, release decisions, release manifests, trust-bearing receipts, proofs, production evidence, reusable fixture inventories, production recovery scripts, schemas, contracts, policy definitions, published artifacts, credentials, generated model output, or default tests that require live network access.

---

## 8. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model rollback states rather than become release decisions, rollback cards, correction notices, receipts, proofs, or production recovery records.

Expected fixture families include valid rollback drill, missing current release, missing target release, unresolved target release, incompatible target release, missing correction notice, missing invalidation list, missing review state, missing receipt reference, silent deletion anti-pattern, floating latest-pointer anti-pattern, direct public-surface mutation, and valid hold outcome.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/rollback_drill
pytest tests/domains/flora/release_manifest
pytest tests/domains/flora/policy
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which rollback-card schema is canonical for Flora? | NEEDS VERIFICATION | Must inspect release/schema roots. |
| Which correction-notice schema is canonical? | NEEDS VERIFICATION | Must inspect release/schema roots. |
| Which validator owns rollback drill checks? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which public-surface invalidation contracts are canonical? | NEEDS VERIFICATION | Must inspect UI/API/release contracts. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared rollback-drill tests live here or under a cross-domain release/rollback test root? | OPEN | This lane should own Flora-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora rollback-drill tests run locally.
- [ ] Valid rollback drill, missing current release, missing target release, unresolved target, incompatible target, missing correction notice, missing invalidation list, missing review state, missing receipt reference, silent deletion, floating latest-pointer, and direct public-surface mutation cases are tested.
- [ ] Positive public-safe fixtures prove bounded rollback readiness without becoming production rollback approval.
- [ ] Negative fixtures prove fail-closed behavior for incomplete rollback prerequisites.
- [ ] Tests call canonical release/rollback/correction/policy/review/API validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora rollback-drill proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora rollback-drill test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for lifecycle/receipt/release/policy/API/UI/runtime/domain tests, and Flora correction/rollback doctrine; executable tests, fixtures, rollback cards, correction notices, release manifests, receipts, validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
