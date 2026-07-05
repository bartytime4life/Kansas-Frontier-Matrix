<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/release/readme
title: Fauna Release Test Lane README
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
verification_status: current-session path verified; executable tests, fixtures, release manifests, rollback cards, validators, public-surface checks, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - tests/domains/fauna/release/rollback/README.md
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
  - evidence-bundle
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Release Tests

> Parent test-lane contract for proving Fauna release behavior is governed, evidence-linked, policy-aware, rollback-addressable, public-safe, and downstream of release decisions rather than hidden file moves.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Frelease-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Frelease-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** parent release test-lane README; not a release manifest, rollback card, correction notice, policy bundle, fixture inventory, receipt, proof, public artifact, or release decision  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `release/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed for sensitive-lane release defects  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the parent Fauna test lane for **release behavior**.

It exists to prove that Fauna release surfaces honor KFM governance before public exposure. A valid release test should verify release-state handling, release-manifest requirements, evidence support, policy gates, correction state, rollback targets, published-artifact boundaries, and public-surface invalidation.

A mature parent lane should prove:

1. Public Fauna outputs are reachable through a governed release decision.
2. Release manifests carry required evidence, proof, correction path, and rollback target references.
3. Published artifacts remain separate from release decisions.
4. Candidate, review, withdrawn, superseded, or invalid releases do not appear as current public truth.
5. Sensitive-lane release defects fail closed.
6. Downstream API, UI, map, Evidence Drawer, Focus Mode, tile, and index surfaces do not continue serving invalidated support.
7. Tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/release/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna release behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Release lane | `release/` |
| Release decision home | `release/` when present. |
| Published artifact home | `data/published/layers/fauna/` when present. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Human runbook/index references | `docs/domains/fauna/RELEASE_INDEX.md` and `docs/runbooks/fauna/ROLLBACK_RUNBOOK.md`. |

> [!WARNING]
> This directory must not become a second release home, published-artifact home, rollback-card home, correction-notice home, fixture home, receipt home, proof home, policy home, or source-data home.

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
| Fauna Release Index says every published Fauna claim needs a ReleaseManifest with rollback target | CONFIRMED from current repo docs. |
| Fauna Release Index says release state, review state, and correction state are distinct vocabularies | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual ReleaseManifest schema/path and validator command | NEEDS VERIFICATION. |
| Actual fixtures and release test manifests | NEEDS VERIFICATION. |
| Actual CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the parent release test-lane contract. It does not claim that release implementation, release manifests, rollback cards, fixtures, validators, or CI checks already exist.

---

## 4. Parent release rule

**Rule:** A Fauna public surface may treat a record, layer, claim, answer, or artifact as released only when the release decision, evidence support, policy state, review state, correction state, rollback target, and published artifact boundary are valid for the tested scope.

Tests should fail or require a finite negative outcome when:

- a release lacks a ReleaseManifest or equivalent governed release decision;
- a release lacks evidence, proof, correction path, or rollback target references;
- published artifacts are treated as release decisions;
- candidate or review-state material appears as public truth;
- withdrawn or superseded material is served as current truth;
- review state, release state, and correction state are silently merged;
- a public client receives internal lifecycle material;
- sensitive-lane policy, rights, review, or receipt requirements are unresolved; or
- downstream surfaces continue serving invalidated support after release correction or withdrawal.

Tests may allow public exposure only when the fixture is public-safe, policy permits it, required governance references are present, and the test remains inside its validation scope.

---

## 5. Child lanes

| Child lane | Responsibility | Status boundary |
|---|---|---|
| `rollback/` | Prove rollback target, correction lineage, and downstream invalidation behavior. | README work may exist in an open PR; executable tests NEEDS VERIFICATION. |
| `manifest/` | Prove ReleaseManifest requirements for Fauna releases. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `correction/` | Prove correction and withdrawal state behavior. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `published-artifact-boundary/` | Prove release decisions and published artifacts remain separate. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `public-surface/` | Prove API/UI/map/Focus surfaces honor release state. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `state-vocabulary/` | Prove release/review/correction vocabularies are not collapsed. | PROPOSED / NEEDS VERIFICATION unless implemented. |

Additional child lanes may be added when they have a clear release-test responsibility and do not duplicate another authority root.

---

## 6. Parent proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Release decision exists | Public fixture links to governed release decision. | Validation passes for test scope. |
| Evidence support | Release references resolvable support. | Evidence-resolution assertion. |
| Proof/receipt boundary | Tests assert references but do not store trust-bearing records. | Placement assertion. |
| Correction path | Release has correction path before public use. | Release-manifest assertion. |
| Rollback target | Release has rollback target before public use. | Release-manifest assertion. |
| Published-artifact split | Artifact location is not treated as release authority. | Boundary assertion. |
| Candidate exclusion | Candidate/review material does not appear publicly. | `DENY`, `ABSTAIN`, `ERROR`, or validation failure. |
| Withdrawn/superseded state | Non-current release is not served as current truth. | Correction-aware outcome. |
| Vocabulary separation | Release/review/correction state fields stay distinct. | State assertion. |
| Sensitive-lane gate | Policy, rights, review, and receipt requirements are enforced. | Fail closed if unresolved. |
| Downstream invalidation | API/UI/map/Focus surfaces stop serving invalidated support. | Finite negative or correction state. |
| No-network default | Tests use deterministic local public-safe fixtures. | Harness guard. |

---

## 7. What belongs here

This directory may contain:

- README and parent-lane contract material for Fauna release tests.
- Tests that call canonical release, rollback, correction, policy, evidence, and validator code from owning roots.
- Negative tests for missing release decision, missing evidence, missing proof, missing correction path, missing rollback target, invalid state, and dangling downstream public surfaces.
- Positive tests for public-safe release fixtures with required governance references.
- Child-lane READMEs for focused release concerns.
- Public-safe test-local examples when they are tiny, deterministic, and not reusable fixture inventory.

## 8. What does not belong here

This directory must not contain production release manifests, release decisions, rollback cards, correction notices, published artifacts, source records, reusable fixture inventories, receipts, proofs, policy definitions, or default tests that require live network access.

---

## 9. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model release, correction, and rollback states without carrying trust-bearing decisions or non-public source material.

Expected fixture families include valid release, missing manifest, missing evidence, missing correction path, missing rollback target, candidate release, withdrawn release, superseded release, state-vocabulary conflict, invalidated evidence, and downstream stale public surface.

---

## 10. Suggested local commands

> [!NOTE]
> Command names, release validator names, rollback schema names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/fauna/release
pytest tests/domains/fauna/release/rollback
pytest tests/domains/fauna
python tools/validate_all.py
```

---

## 11. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical ReleaseManifest schema/path? | NEEDS VERIFICATION | Must inspect release schema roots. |
| Which validator command owns release checks? | NEEDS VERIFICATION | Must inspect validator roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which public surfaces are included in release invalidation tests? | NEEDS VERIFICATION | Must inspect API/UI/layer implementation. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared release tests live here or in a cross-domain release test root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 12. Definition of done

This parent lane is mature when:

- [ ] Fauna release tests run locally.
- [ ] Rollback and other active child lanes have executable proof where implementation exists.
- [ ] Missing release decision, missing evidence, missing proof, missing correction path, missing rollback target, invalid state, and downstream stale public surface cases are tested.
- [ ] Positive public-safe fixtures prove allowed release behavior without becoming release approval.
- [ ] Tests call canonical release/rollback/policy/evidence validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Fauna release proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 13. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna release parent test lane. |

---

## 14. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for release/lifecycle/receipt/proof/domain tests, and Fauna release doctrine; executable tests, fixtures, ReleaseManifest shape, rollback cards, validators, public-surface invalidation, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
