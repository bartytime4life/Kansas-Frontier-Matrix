<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/citation/readme
title: Flora Citation Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Evidence steward>
  - <PLACEHOLDER — Source steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, validators, evidence bundles, source descriptors, release manifests, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - fixtures/domains/flora/
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - data/registry/sources/flora/
  - data/receipts/
  - data/proofs/flora/
  - release/
tags:
  - kfm
  - tests
  - flora
  - citation
  - evidence-ref
  - evidence-bundle
  - cite-or-abstain
  - source-role
  - rights
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Citation Tests

> Test-lane contract for proving Flora claims, map details, species-page text, drawer payloads, and Focus answers cite governed evidence or abstain.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Fcitation-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Fcitation-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: cite--or--abstain-blue](https://img.shields.io/badge/posture-cite--or--abstain-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** citation test-lane README; not an evidence store, source registry, citation registry, schema, contract, policy bundle, fixture inventory, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `citation/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; cite-or-abstain for unsupported Flora claims  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **citation behavior**.

It exists to prove that Flora claims are not treated as public truth unless they resolve to governed evidence with valid source role, rights posture, sensitivity posture, release state, and citation metadata. When evidence support is missing, unresolved, stale, conflicted, restricted, or outside the requested scope, the expected result is `ABSTAIN`, `DENY`, `ERROR`, or another finite negative outcome — never an uncited answer.

A mature lane should prove:

1. Every Flora evidence-dependent claim carries an `EvidenceRef` or equivalent governed support reference.
2. `EvidenceRef` resolves to a complete `EvidenceBundle` before display, export, drawer projection, or Focus answer.
3. Source role is preserved so authority, observation, context, and model-derived support are not collapsed.
4. Rights, sensitivity, freshness, release, and correction state are checked before a citation is accepted.
5. AI-generated or UI-generated text remains downstream of evidence and never becomes evidence itself.
6. Unsupported Flora claims abstain rather than fill gaps with fluent language.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/citation/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora citation and cite-or-abstain behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `citation/` |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Source registry home | `data/registry/sources/flora/` when present. |
| Contract/schema homes | `contracts/domains/flora/` and `schemas/contracts/v1/domains/flora/` when present. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/flora/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second evidence store, citation registry, source registry, schema home, contract home, policy home, fixture home, receipt home, proof home, release home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows evidence-resolution, policy, lifecycle, receipt/proof, release-manifest, governed API, UI trust-state, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive material, live network calls, duplicate authority homes, trust-bearing receipts/proofs, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Flora docs state cite-or-abstain and EvidenceBundle outranks generated language | CONFIRMED from current repo docs. |
| Flora docs state source rights and source roles must be verified per source/claim | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual fixture inventory, validators, evidence bundle schemas, source descriptors, release manifests, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that citation tests, fixtures, validators, evidence bundles, or CI checks already exist.

---

## 4. Citation rule

**Rule:** A Flora claim may render as `ANSWER` only when its evidence support resolves, its source role is valid for the claim, its rights/sensitivity/release/correction state permits the requested use, and the public output carries an inspectable citation path.

Tests should fail or require a finite negative outcome when:

- a Flora claim lacks an evidence reference;
- an evidence reference cannot resolve to a complete evidence bundle;
- citation metadata lacks source identity, source role, retrieval/source time, rights posture, or claim scope where required;
- source role is incompatible with the claim being made;
- source rights, sensitivity, review, release, or correction state is unresolved;
- stale or superseded support is displayed as current without trust-visible state;
- AI or UI-generated text is treated as evidence;
- drawer, Focus, map, export, or species-page output hides missing citation state; or
- trust-bearing evidence, receipts, proofs, or release decisions are stored under `tests/`.

Tests may allow `ANSWER` only when the fixture is public-safe, evidence support resolves, policy permits it, citation validation passes, release state is current, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Evidence reference required | Claim fixture carries an evidence reference. | Schema/validator assertion. |
| Evidence resolution | Reference resolves to complete evidence support. | `ANSWER` or `ABSTAIN`. |
| Citation metadata | Source identity, source role, timing, rights, and scope are present where required. | Citation assertion. |
| Source-role fit | Source role is compatible with claim type. | `ABSTAIN`, `DENY`, `ERROR`, or validation failure if mismatched. |
| Rights posture | Unresolved rights block public use. | Fail closed. |
| Sensitivity posture | Policy-withheld detail is not exposed through citation text or output. | `DENY`, `ABSTAIN`, or redacted public-safe result. |
| Freshness/correction | Stale, superseded, or corrected support is visibly bounded. | Trust-state assertion. |
| AI/text boundary | Generated text cites evidence but is not evidence. | Boundary assertion. |
| Drawer/Focus continuity | Drawer and Focus surfaces preserve citation state. | Runtime envelope assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Flora citation tests.
- Tests that call canonical evidence, source, policy, release, citation, drawer, Focus, and validator code from owning roots.
- Negative tests for missing evidence reference, unresolved evidence, incompatible source role, unresolved rights, unresolved sensitivity, stale support, superseded support, and generated-text-as-evidence anti-patterns.
- Positive tests for public-safe claim fixtures with valid evidence support and citation metadata.
- Tiny test-local examples when documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain production evidence bundles, source descriptors, source records, reusable fixture inventories, schemas, contracts, policy definitions, receipts, proofs, release decisions, published artifacts, credentials, model prompts, model outputs, or default tests that require live network access.

---

## 8. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model citation and evidence-resolution states rather than include production source material or trust-bearing records.

Expected fixture families include valid cited claim, missing evidence reference, unresolved evidence reference, incompatible source role, unresolved rights, stale support, corrected support, policy denial, generated-text-as-evidence anti-pattern, drawer citation payload, and Focus abstention.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/citation
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical Flora evidence bundle schema/path? | NEEDS VERIFICATION | Must inspect schema roots. |
| Which validator owns Flora citation validation? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which source descriptor fields are required for citation display? | NEEDS VERIFICATION | Must inspect source registry/schema roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which UI/Focus routes consume Flora citation payloads? | NEEDS VERIFICATION | Must inspect API/UI implementation. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared citation tests live here or under a cross-domain evidence/citation test root? | OPEN | This lane should own Flora-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora citation tests run locally.
- [ ] Valid cited claim, missing evidence reference, unresolved evidence reference, incompatible source role, unresolved rights, stale support, corrected support, policy denial, and generated-text-as-evidence cases are tested.
- [ ] Positive public-safe fixtures prove allowed citation behavior without becoming release approval.
- [ ] Negative fixtures prove cite-or-abstain behavior for unsupported states.
- [ ] Tests call canonical evidence/source/policy/release validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora citation proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora citation test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for evidence/policy/lifecycle/receipt/release/API/UI/runtime/domain tests, and Flora cite-or-abstain doctrine; executable tests, fixtures, validators, schemas, evidence bundles, source descriptors, releases, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
