<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/focus/citation/readme
title: Fauna Focus Citation Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Focus Mode steward>
  - <PLACEHOLDER — Citation/evidence steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, Focus Mode route names, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - docs/domains/fauna/SENSITIVITY.md
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - fixtures/domains/fauna/
  - data/proofs/fauna/
  - data/receipts/
  - schemas/contracts/v1/ai/
  - schemas/contracts/v1/ui/
  - apps/governed-api/
  - apps/explorer-web/
tags:
  - kfm
  - tests
  - fauna
  - focus-mode
  - citation
  - evidence
  - evidence-ref
  - evidence-bundle
  - ai-receipt
  - cite-or-abstain
  - sensitivity
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Focus Citation Tests

> Test-lane contract for proving Fauna Focus Mode answers cite released, admissible evidence or produce a finite abstain/deny/error outcome.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Ffocus%2Fcitation-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Ffocus%2Fcitation-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: cite--or--abstain](https://img.shields.io/badge/posture-cite--or--abstain-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** Focus Mode citation test-lane README; not a model adapter, prompt, policy bundle, schema, fixture inventory, source registry, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `focus/citation/`  
**Default posture:** cite-or-abstain; public-safe fixtures; no-network by default  
**Last reviewed:** 2026-07-05

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [Citation rule](#4-citation-rule)
5. [What belongs here](#5-what-belongs-here)
6. [What does not belong here](#6-what-does-not-belong-here)
7. [Citation proof matrix](#7-citation-proof-matrix)
8. [Fixture posture](#8-fixture-posture)
9. [Expected outcomes](#9-expected-outcomes)
10. [Lifecycle and publication boundaries](#10-lifecycle-and-publication-boundaries)
11. [No-network default](#11-no-network-default)
12. [Suggested local commands](#12-suggested-local-commands)
13. [Review burden](#13-review-burden)
14. [Related folders and files](#14-related-folders-and-files)
15. [Open questions](#15-open-questions)
16. [Definition of done](#16-definition-of-done)
17. [Changelog](#17-changelog)
18. [Last reviewed](#18-last-reviewed)

---

## 1. Purpose

This directory is the Fauna Focus Mode test sublane for **citation validation**.

It exists to prove that Fauna Focus Mode does not answer from fluent generation, map feature properties, unreleased candidates, raw/source records, private indexes, or unvalidated citations. Every evidence-dependent answer should cite released, admissible evidence. If that cannot be proven, the answer should abstain, deny, or error with a finite reason.

A mature lane should support these claims:

1. **EvidenceBundle outranks generated language.** Focus Mode summarizes evidence; it does not create root truth.
2. **Citations are validated before display or export.** A cited `EvidenceRef` must resolve to an admissible evidence object for the current user/scope.
3. **Released evidence only.** Public Focus Mode answers use released Fauna evidence, not raw, work, quarantine, candidate, unpublished, or internal material.
4. **Policy gates run before answer emission.** Sensitivity, rights, release state, review state, and correction state can block an answer even when a source exists.
5. **Negative outcomes are first-class.** Missing, stale, conflicted, restricted, withdrawn, or inadmissible support produces `ABSTAIN`, `DENY`, or `ERROR`, not an uncited answer.
6. **AIReceipt remains separate.** AI receipts record the generated-answer event, but they do not replace evidence, policy, release, or proof.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/focus/citation/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna Focus Mode citation behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Parent lane | `focus/` |
| Sublane | `citation/` |
| Focus/API implementation home | `apps/governed-api/` as applicable. |
| Public UI home | `apps/explorer-web/` as applicable. |
| AI/schema homes | `schemas/contracts/v1/ai/` and `schemas/contracts/v1/ui/` when present. |
| Evidence/proof homes | `data/proofs/`, `data/receipts/`, and domain proof roots when present. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second prompt, model, evidence, proof, receipt, release, policy, schema, fixture, or source-data home. It verifies citation behavior against those authorities.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows evidence-resolution, governed API envelope, UI trust-state, e2e, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive Fauna coordinate data from tests | CONFIRMED from current repo docs. |
| Fauna Map UI contract says Focus Mode uses released EvidenceBundles and validated citations | CONFIRMED from current repo docs. |
| Fauna Map UI contract says browser must not call model runtime, vector index, graph store, or object store directly | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual Focus Mode route names, schema names, and adapter paths | NEEDS VERIFICATION. |
| Actual fixtures and evidence bundles | NEEDS VERIFICATION. |
| Actual CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that Focus Mode implementation, citation validators, fixtures, routes, schemas, or CI jobs already exist.

---

## 4. Citation rule

**Rule:** A Fauna Focus Mode answer must cite admissible released evidence or return a finite negative outcome.

Tests should fail when Focus Mode:

- emits an evidence-dependent claim without a citation;
- cites an `EvidenceRef` that does not resolve;
- cites evidence outside the current release, review, rights, or policy scope;
- cites a record whose support was withdrawn, superseded, or corrected without surfacing that state;
- cites map feature properties as if they were evidence;
- cites an AI-generated summary as if it were source evidence;
- leaks raw/work/quarantine/candidate/internal data into the response or receipt; or
- produces a public answer when the correct outcome is `ABSTAIN`, `DENY`, or `ERROR`.

Tests may allow an `ANSWER` only when the Focus Mode response includes resolvable, admissible citations and records the generated-answer event separately from the evidence.

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for Fauna Focus citation tests.
- Tests that verify every answer claim has a resolvable citation.
- Tests that verify missing citations produce `ABSTAIN` or validation failure.
- Tests that verify policy-denied or withheld support produces `DENY` without exposing withheld details.
- Tests that verify stale, conflicted, corrected, or withdrawn support is reflected in the answer outcome.
- Tests that verify `AIReceipt` references the generated response without replacing evidence support.
- Tests that call canonical Focus Mode, citation-validation, policy, schema, and evidence-resolution code from their owning roots.
- Public-safe fixtures for positive and negative citation cases.

---

## 6. What does not belong here

This directory must not contain:

- Model prompts, provider adapters, model-runtime code, or production Focus Mode implementation.
- Raw Fauna source records, candidate evidence, source caches, or unreleased records.
- Policy definitions, schema definitions, source registry records, receipts, proofs, release decisions, or rollback decisions.
- Reusable fixture inventories that belong under `fixtures/domains/fauna/`.
- Test snapshots, traces, or logs that include policy-withheld details.
- Tests that require live network access or live model calls by default.

[↑ Back to top](#top)

---

## 7. Citation proof matrix

| Test concern | Required proof | Preferred lane behavior |
|---|---|---|
| Claim has citation | Each evidence-dependent sentence or claim maps to an `EvidenceRef`. | Positive citation test. |
| Citation resolves | `EvidenceRef` resolves to an admissible evidence object. | Evidence-resolution assertion. |
| Citation is released | Public answer cites released evidence only. | Release-state assertion. |
| Citation is in scope | Rights, sensitivity, review, and user scope allow citation use. | Policy pre-check assertion. |
| Missing citation | Focus Mode does not answer from generation alone. | `ABSTAIN` or validation failure. |
| Missing evidence bundle | Citation cannot resolve. | `ABSTAIN`, `ERROR`, or validation failure. |
| Denied evidence | Evidence exists but is not public-scope admissible. | `DENY` without withheld detail. |
| Corrected/withdrawn support | Citation is superseded or withdrawn. | `ABSTAIN`, `ERROR`, or corrected-state answer. |
| Conflicting support | Sources disagree. | `ANSWER` with visible conflict or `ABSTAIN`. |
| AIReceipt linkage | Generated event is recorded separately from evidence. | Receipt assertion, not evidence substitution. |
| Browser boundary | Browser does not call model/index/store directly. | UI/API boundary assertion. |
| No-network default | Tests use local public-safe fixtures. | Harness guard. |

---

## 8. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Expected fixture families include:

| Fixture family | Purpose |
|---|---|
| Positive released evidence | Proves a cited public-safe answer can pass. |
| Missing citation | Proves uncited claims abstain or fail validation. |
| Missing evidence | Proves unresolved citation does not answer. |
| Denied support | Proves withheld support produces denial without detail exposure. |
| Stale support | Proves freshness state is surfaced. |
| Conflicted support | Proves source-role conflict is visible or answer abstains. |
| Corrected or withdrawn support | Proves answer does not cite stale release state as current truth. |
| AIReceipt-only fixture | Proves receipt alone cannot satisfy evidence support. |

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They must not include raw source payloads, unreleased evidence, or policy-withheld details.

---

## 9. Expected outcomes

Fauna Focus citation tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

| Condition | Preferred outcome |
|---|---|
| Released, admissible evidence supports the claim | `ANSWER` with citations and receipt linkage. |
| Citation missing | `ABSTAIN` or validation failure. |
| Citation unresolved | `ABSTAIN`, `ERROR`, or validation failure. |
| Evidence outside release or policy scope | `DENY` or `ABSTAIN`. |
| Support withdrawn or superseded | `ABSTAIN`, `ERROR`, or corrected-state answer. |
| Conflicting support | `ANSWER` with conflict visible or `ABSTAIN`. |
| Live model or source call attempted in default test | Test failure. |

---

## 10. Lifecycle and publication boundaries

This lane supports KFM verification but does not move records through the lifecycle:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Boundary | Rule |
|---|---|
| RAW | Do not store raw Fauna records here. |
| WORK / QUARANTINE | Do not store candidate or quarantined records here. |
| PROCESSED | Do not store processed Fauna products here. |
| CATALOG / TRIPLET | Do not treat citation-test fixtures as catalog or graph truth. |
| PUBLISHED | Tests never publish. |
| RECEIPTS / PROOFS | Tests may assert references; trust-bearing records stay in their roots. |
| RELEASE | Release decisions remain under `release/`. |

A passing Focus citation test proves behavior for the checked scenario. It is not evidence creation, policy approval, release approval, proof, or publication.

---

## 11. No-network default

Default Fauna Focus citation tests must avoid:

- live source services;
- internet access;
- live model calls;
- direct vector-index, graph-store, or object-store calls from the browser;
- local credential files;
- developer machine caches;
- mutable upstream API responses; and
- direct source-system side effects.

Live or integration checks, if ever needed, should be explicitly marked and excluded from the default suite.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, Focus Mode route names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

Likely lane check:

```bash
pytest tests/domains/fauna/focus/citation
```

Possible broader Fauna domain check:

```bash
pytest tests/domains/fauna
```

Possible UI/e2e check if configured:

```bash
npx playwright test --grep fauna
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does the test prove citation behavior rather than encode prompt or model behavior locally?
- Does every evidence-dependent answer cite released, admissible evidence?
- Do missing, unresolved, denied, stale, conflicted, corrected, or withdrawn citations produce finite outcomes?
- Does Focus Mode avoid treating map properties or generated summaries as evidence?
- Are `AIReceipt` records tested as generated-event receipts rather than evidence substitutes?
- Are fixtures deterministic, public-safe, and no-network?
- Are routes, schemas, validators, policies, evidence bundles, receipts, proofs, and releases kept in their canonical roots?
- Are implementation gaps marked **NEEDS VERIFICATION** instead of hidden?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/README.md` | Root test contract for evidence-resolution, API envelope, UI trust-state, e2e, and domain tests. | CONFIRMED. |
| `docs/doctrine/directory-rules.md` | Domain segment rule for `tests/domains/<domain>/`. | CONFIRMED. |
| `docs/domains/fauna/MAP_UI_CONTRACTS.md` | Focus Mode, Evidence Drawer, citation, and finite outcome obligations. | CONFIRMED. |
| `docs/domains/fauna/SENSITIVITY.md` | Fauna sensitivity and geoprivacy posture. | CONFIRMED. |
| `fixtures/domains/fauna/` | Reusable public-safe fixture home. | Inventory NEEDS VERIFICATION. |
| `data/proofs/fauna/` | Domain proof/evidence support, if present. | NEEDS VERIFICATION. |
| `data/receipts/` | Receipt home including AI/citation/process receipts where implemented. | NEEDS VERIFICATION. |
| `policy/domains/fauna/` | Domain policy home. | Behavior NEEDS VERIFICATION. |
| `policy/sensitivity/fauna/` | Sensitivity policy home. | Behavior NEEDS VERIFICATION. |
| `schemas/contracts/v1/ai/` | Focus/AI response schema home when present. | NEEDS VERIFICATION. |
| `apps/governed-api/` | Focus/API implementation home when present. | NEEDS VERIFICATION. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical Focus Mode response schema? | NEEDS VERIFICATION | Must inspect schema tree. |
| What is the canonical citation validation report shape? | NEEDS VERIFICATION | Do not invent fields beyond docs. |
| Which route or service owns Focus Mode citation validation? | NEEDS VERIFICATION | Must inspect implementation. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared Focus citation tests live here or in a cross-domain AI/runtime root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 16. Definition of done

This lane is mature when:

- [ ] Fauna Focus citation tests run locally.
- [ ] Positive answer fixtures prove citations resolve to released, admissible evidence.
- [ ] Missing, unresolved, denied, stale, conflicted, corrected, and withdrawn support paths are tested.
- [ ] AIReceipt linkage is tested without replacing evidence support.
- [ ] Browser/API/model boundary is tested where implementation exists.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] Tests call canonical validators, policies, schemas, and Focus code rather than redefining behavior locally.
- [ ] CI exposes the citation proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna Focus citation test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for evidence-resolution/API/UI/e2e/domain tests, and Fauna Map UI Focus Mode citation obligations; executable tests, fixtures, Focus route names, schemas, citation validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
