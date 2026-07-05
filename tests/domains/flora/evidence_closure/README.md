<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/evidence-closure/readme
title: Flora Evidence Closure Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Evidence steward>
  - <PLACEHOLDER — Validation steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, evidence bundles, validation reports, receipts, release manifests, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
  - tests/domains/flora/citation/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - fixtures/domains/flora/
  - data/registry/sources/flora/
  - data/receipts/
  - data/proofs/flora/
  - release/
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
tags:
  - kfm
  - tests
  - flora
  - evidence-closure
  - evidence-ref
  - evidence-bundle
  - validation-report
  - source-descriptor
  - release-manifest
  - cite-or-abstain
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Evidence Closure Tests

> Test-lane contract for proving Flora claims close over governed evidence before they can support public outputs, citations, drawer payloads, Focus answers, layers, or release candidates.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Fevidence__closure-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Fevidence__closure-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: cite--or--abstain-blue](https://img.shields.io/badge/posture-cite--or--abstain-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** evidence-closure test-lane README; not an evidence store, proof store, receipt home, source registry, fixture inventory, schema, contract, policy bundle, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `evidence_closure/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; cite-or-abstain when evidence closure is incomplete  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **evidence closure**.

It exists to prove that Flora claims are not promoted, rendered, cited, summarized, or released unless the required evidence chain closes. Evidence closure means the tested claim can resolve from source descriptor and claim context through evidence support, validation, receipt/proof references, release eligibility, and rollback/correction readiness where applicable.

A mature lane should prove:

1. A Flora claim has a resolvable evidence reference before public use.
2. The evidence reference resolves to a complete evidence bundle or the output abstains.
3. Evidence support carries source identity, source role, source/retrieval time, rights, sensitivity, and claim scope where required.
4. Validation reports and run/transform receipts are present where the tested lifecycle state requires them.
5. Evidence closure is distinct from release approval.
6. Missing, stale, conflicted, restricted, or corrected support produces a finite negative outcome.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/evidence_closure/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora evidence-closure behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `evidence_closure/` |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Source registry home | `data/registry/sources/flora/` when present. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/flora/`. |
| Contract/schema homes | `contracts/domains/flora/` and `schemas/contracts/v1/domains/flora/` when present. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second evidence store, proof home, receipt home, source registry, fixture inventory, schema home, contract home, policy home, release home, public artifact home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows evidence-resolution, lifecycle-state, receipt/proof, release-manifest, policy, governed API envelope, UI trust-state, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive material, live network calls, duplicate authority homes, trust-bearing receipts/proofs, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Flora docs anchor the lane to `SourceDescriptor → EvidenceBundle → ValidationReport → ReleaseManifest → RollbackCard` | CONFIRMED from current repo docs. |
| Flora docs state cite-or-abstain and evidence-first posture | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual evidence bundle schemas, validation reports, receipts, fixtures, validators, releases, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that evidence closure tests, evidence bundles, receipts, proofs, validation reports, release manifests, fixtures, validators, or CI checks already exist.

---

## 4. Evidence-closure rule

**Rule:** A Flora claim may pass evidence-closure tests only when its evidence reference resolves to complete governed support for the tested claim scope, and all required validation, receipt/proof, rights, sensitivity, freshness, correction, and release-eligibility checks are satisfied for that lifecycle state.

Tests should fail or require a finite negative outcome when:

- a claim has no evidence reference;
- an evidence reference cannot resolve;
- evidence support is incomplete for the claim scope;
- source identity, source role, rights, timing, sensitivity, or retrieval metadata is missing where required;
- validation report or receipt/proof references are missing for a lifecycle state that requires them;
- stale, conflicted, corrected, superseded, restricted, or unreleased support is treated as current evidence without visible state;
- release approval is treated as evidence closure or evidence closure is treated as release approval;
- generated text is treated as evidence; or
- trust-bearing evidence, receipts, proofs, or release decisions are stored under `tests/`.

Tests may allow closure only when the fixture is public-safe, evidence support resolves, claim scope matches the evidence bundle, required governance references are present, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Evidence ref required | Claim fixture carries a governed evidence reference. | Schema/contract assertion. |
| Evidence resolution | Reference resolves to complete support for the claim. | `ANSWER` or closure pass. |
| Abstain on missing support | Missing or unresolved support does not render as answer. | `ABSTAIN` or validation failure. |
| Source support | Source identity, role, timing, rights, and scope are present where required. | Source/evidence assertion. |
| Validation closure | Required validation report exists for the tested lifecycle state. | Validation assertion. |
| Receipt/proof reference | Required run, transform, integrity, or proof references are present where required. | Receipt/proof assertion. |
| Freshness/correction | Stale, corrected, or superseded support is visibly bounded. | Trust-state assertion. |
| Policy boundary | Rights/sensitivity/review state can block closure. | `DENY`, `ABSTAIN`, or validation failure. |
| Release boundary | Release state is checked separately from evidence closure. | Boundary assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Flora evidence-closure tests.
- Tests that call canonical evidence, source, validation, receipt/proof, policy, release, citation, and validator code from owning roots.
- Negative tests for missing evidence reference, unresolved evidence, incomplete evidence support, missing validation report, missing receipt/proof reference, stale support, corrected support, conflicting support, and release/evidence boundary collapse.
- Positive tests for public-safe claim fixtures with complete evidence closure.
- Tiny test-local examples when documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain production evidence bundles, trust-bearing receipts, proofs, release decisions, source descriptors, source records, reusable fixture inventories, schemas, contracts, policy definitions, published artifacts, credentials, model prompts, model outputs, or default tests that require live network access.

---

## 8. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model evidence-closure states rather than include production source material or trust-bearing records.

Expected fixture families include valid closed evidence, missing evidence reference, unresolved evidence reference, incomplete evidence bundle, missing validation report, missing receipt reference, stale support, corrected support, conflicting support, policy denial, release-without-evidence anti-pattern, evidence-without-release boundary, and generated-text-as-evidence anti-pattern.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/evidence_closure
pytest tests/domains/flora/citation
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical Flora EvidenceBundle schema/path? | NEEDS VERIFICATION | Must inspect schema roots. |
| What is the canonical ValidationReport schema/path? | NEEDS VERIFICATION | Must inspect schema roots. |
| Which receipt/proof references are required for each Flora lifecycle state? | NEEDS VERIFICATION | Must inspect receipts/proofs doctrine and implementation. |
| Which validator owns evidence-closure checks? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared evidence-closure tests live here or under a cross-domain evidence test root? | OPEN | This lane should own Flora-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora evidence-closure tests run locally.
- [ ] Valid closed evidence, missing evidence reference, unresolved evidence reference, incomplete evidence bundle, missing validation report, missing receipt/proof reference, stale support, corrected support, conflicting support, policy denial, and release/evidence boundary cases are tested.
- [ ] Positive public-safe fixtures prove allowed evidence closure without becoming release approval.
- [ ] Negative fixtures prove cite-or-abstain behavior for unsupported states.
- [ ] Tests call canonical evidence/source/validation/receipt/policy/release validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora evidence-closure proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora evidence-closure test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for evidence/lifecycle/receipt/release/policy/API/UI/runtime/domain tests, and Flora trust-spine doctrine; executable tests, fixtures, evidence bundles, validation reports, receipts, releases, validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
