<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/focus/deny-sensitive/readme
title: Fauna Focus Deny-Sensitive Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Focus Mode steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, Focus Mode route names, policy behavior, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - docs/domains/fauna/SENSITIVITY.md
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - fixtures/domains/fauna/
  - data/receipts/
  - data/proofs/fauna/
  - schemas/contracts/v1/ai/
  - schemas/contracts/v1/ui/
  - apps/governed-api/
  - apps/explorer-web/
tags:
  - kfm
  - tests
  - fauna
  - focus-mode
  - deny-sensitive
  - sensitivity
  - geoprivacy
  - policy-deny
  - finite-outcome
  - evidence
  - ai-receipt
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Focus Deny-Sensitive Tests

> Test-lane contract for proving Fauna Focus Mode refuses sensitive, restricted, unreleased, rights-unclear, or otherwise inadmissible requests with finite governed outcomes.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Ffocus%2Fdeny__sensitive-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Ffocus%2Fdeny__sensitive-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** Focus Mode denial test-lane README; not a model adapter, prompt, policy bundle, schema, fixture inventory, source registry, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `focus/deny_sensitive/`  
**Default posture:** fail closed; public-safe fixtures; no-network by default  
**Last reviewed:** 2026-07-05

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [Deny-sensitive rule](#4-deny-sensitive-rule)
5. [What belongs here](#5-what-belongs-here)
6. [What does not belong here](#6-what-does-not-belong-here)
7. [Denial proof matrix](#7-denial-proof-matrix)
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

This directory is the Fauna Focus Mode test sublane for **deny-sensitive behavior**.

It exists to prove that Focus Mode refuses requests that would expose protected Fauna information, use unreleased evidence, bypass release state, ignore rights/review state, or turn a policy-limited public-safe derivative into an over-specific answer.

A mature lane should support these claims:

1. **Policy pre-check happens first.** Sensitivity, rights, release state, and review state are checked before evidence retrieval or answer generation.
2. **Denied means denied.** A denied Focus Mode request emits a finite `DENY` outcome with a safe reason, not a partial answer.
3. **Abstain remains available.** If support is missing or unresolved rather than policy-denied, the answer is `ABSTAIN` or `ERROR`, not a guessed response.
4. **No hidden disclosure.** Denial responses, receipts, logs, snapshots, traces, labels, and UI text must not include policy-withheld details.
5. **Public-safe derivatives stay bounded.** A generalized or transformed public record may be explained only within its approved scope.
6. **AIReceipt records the blocked event.** A receipt may document that a request was denied, but it does not replace policy, evidence, proof, or release state.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/focus/deny_sensitive/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna Focus Mode denial behavior for sensitive or inadmissible requests. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Parent lane | `focus/` |
| Sublane | `deny_sensitive/` |
| Focus/API implementation home | `apps/governed-api/` as applicable. |
| Public UI home | `apps/explorer-web/` as applicable. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Schema homes | `schemas/contracts/v1/ai/` and `schemas/contracts/v1/ui/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second policy, prompt, model, evidence, proof, receipt, release, schema, fixture, or source-data home. It verifies denial behavior against those authorities.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows policy, evidence-resolution, governed API envelope, UI trust-state, e2e, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive Fauna location data from tests | CONFIRMED from current repo docs. |
| Fauna Map UI contract says Focus Mode pre-checks sensitivity, rights, and release state | CONFIRMED from current repo docs. |
| Fauna Map UI contract names required Focus Mode denials and abstentions | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual Focus Mode route names, policy module names, schema names, and adapter paths | NEEDS VERIFICATION. |
| Actual fixtures and fixture manifests | NEEDS VERIFICATION. |
| Actual CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that Focus Mode implementation, policy modules, fixtures, routes, schemas, or CI jobs already exist.

---

## 4. Deny-sensitive rule

**Rule:** Fauna Focus Mode must deny or abstain before answer emission when the requested answer is outside public-safe policy scope.

Tests should fail when Focus Mode:

- answers a policy-denied request;
- turns a generalized public-safe record into a more specific claim than the release permits;
- uses unreleased or candidate evidence in a public answer;
- ignores unknown rights, missing review, withdrawn release state, or missing policy decision;
- exposes policy-withheld details through the answer, reason, citation, receipt, log, trace, snapshot, or UI text;
- routes the browser directly to model, index, graph, object store, or source data; or
- returns an unconstrained answer where the governed result should be `DENY`, `ABSTAIN`, or `ERROR`.

Tests may allow `ANSWER` only when the request is within public-safe scope, citations are admissible, and policy permits the response.

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for Fauna Focus deny-sensitive tests.
- Tests that verify Focus Mode pre-checks policy before answering.
- Tests that verify denied requests emit `DENY` with safe reason codes.
- Tests that verify withheld support does not appear in text, citations, logs, receipts, or snapshots.
- Tests that verify unreleased, rights-unclear, review-missing, withdrawn, or out-of-scope support does not produce public answers.
- Tests that verify public-safe derivatives can be explained only within approved scope.
- Tests that call canonical Focus Mode, policy, citation-validation, schema, evidence-resolution, and receipt code from their owning roots.
- Public-safe fixtures for positive and negative denial cases.

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

## 7. Denial proof matrix

| Test concern | Required proof | Preferred lane behavior |
|---|---|---|
| Policy pre-check | Sensitivity, rights, review, and release state are evaluated before answer generation. | Policy/API assertion. |
| Sensitive request denied | Request outside public-safe scope returns `DENY`. | Negative Focus test. |
| Missing release support | Unreleased support does not produce an answer. | `ABSTAIN`, `DENY`, or validation failure. |
| Rights unresolved | Rights-unclear support does not produce a public answer. | `DENY` or validation failure. |
| Review missing | Review-required content without review does not answer publicly. | `DENY` or `HOLD` in workflow-facing tests. |
| Public-safe derivative bounded | Answer stays within approved transform/release scope. | Positive bounded-answer test. |
| Denial reason safe | Reason is accessible and useful but omits withheld detail. | UI/API assertion. |
| AIReceipt safe | Receipt records the denial event without becoming evidence or leaking detail. | Receipt assertion. |
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
| Public-safe allowed query | Proves an allowed Focus request can answer with citations. |
| Policy-denied query | Proves denied requests produce `DENY`. |
| Unreleased evidence query | Proves unreleased support abstains or denies. |
| Rights-unresolved query | Proves rights uncertainty blocks public answer. |
| Review-missing query | Proves review gate is enforced. |
| Withdrawn release query | Proves withdrawn support is not treated as current truth. |
| Public-safe derivative query | Proves explanation remains bounded to released scope. |
| Receipt-safety fixture | Proves denial receipts avoid withheld detail. |

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They must not include raw source payloads, unreleased evidence, or policy-withheld details.

---

## 9. Expected outcomes

Fauna Focus deny-sensitive tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

| Condition | Preferred outcome |
|---|---|
| Public-safe request with admissible evidence | `ANSWER` with citations and receipt linkage. |
| Request outside public-safe policy scope | `DENY` with safe reason. |
| Evidence missing or unresolved | `ABSTAIN`, `ERROR`, or validation failure. |
| Evidence unreleased or out of scope | `ABSTAIN` or `DENY`. |
| Rights/review/release state blocks answer | `DENY`, `ABSTAIN`, or workflow `HOLD`. |
| Denial text includes withheld detail | Test failure. |
| Live model/source call attempted in default test | Test failure. |

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
| CATALOG / TRIPLET | Do not treat denial-test fixtures as catalog or graph truth. |
| PUBLISHED | Tests never publish. |
| RECEIPTS / PROOFS | Tests may assert references; trust-bearing records stay in their roots. |
| RELEASE | Release decisions remain under `release/`. |

A passing deny-sensitive test proves behavior for the checked scenario. It is not evidence creation, policy approval, release approval, proof, or publication.

---

## 11. No-network default

Default Fauna Focus deny-sensitive tests must avoid:

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
pytest tests/domains/fauna/focus/deny_sensitive
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

- Does the test prove denial behavior rather than encode prompt or model behavior locally?
- Does Focus Mode pre-check sensitivity, rights, review, and release state before answering?
- Do denied, unreleased, rights-unclear, review-missing, withdrawn, or out-of-scope requests produce finite outcomes?
- Do denial messages, citations, receipts, logs, traces, and snapshots avoid withheld detail?
- Does Focus Mode avoid treating map properties or generated summaries as evidence?
- Are fixtures deterministic, public-safe, and no-network?
- Are routes, schemas, validators, policies, evidence bundles, receipts, proofs, and releases kept in their canonical roots?
- Are implementation gaps marked **NEEDS VERIFICATION** instead of hidden?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/README.md` | Root test contract for policy, evidence-resolution, API envelope, UI trust-state, e2e, and domain tests. | CONFIRMED. |
| `docs/doctrine/directory-rules.md` | Domain segment rule for `tests/domains/<domain>/`. | CONFIRMED. |
| `docs/domains/fauna/MAP_UI_CONTRACTS.md` | Focus Mode pre-check, deny/abstain, citation, and finite outcome obligations. | CONFIRMED. |
| `docs/domains/fauna/SENSITIVITY.md` | Fauna sensitivity and geoprivacy posture. | CONFIRMED. |
| `fixtures/domains/fauna/` | Reusable public-safe fixture home. | Inventory NEEDS VERIFICATION. |
| `policy/domains/fauna/` | Domain policy home. | Behavior NEEDS VERIFICATION. |
| `policy/sensitivity/fauna/` | Sensitivity policy home. | Behavior NEEDS VERIFICATION. |
| `data/receipts/` | Receipt home including AI/process receipts where implemented. | NEEDS VERIFICATION. |
| `data/proofs/fauna/` | Domain proof/evidence support, if present. | NEEDS VERIFICATION. |
| `schemas/contracts/v1/ai/` | Focus/AI response schema home when present. | NEEDS VERIFICATION. |
| `apps/governed-api/` | Focus/API implementation home when present. | NEEDS VERIFICATION. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical Focus Mode denial schema or response envelope? | NEEDS VERIFICATION | Must inspect schema tree. |
| Which policy module owns deny-sensitive behavior? | NEEDS VERIFICATION | Must inspect policy roots. |
| Which route or service performs Focus Mode pre-checks? | NEEDS VERIFICATION | Must inspect implementation. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared Focus denial tests live here or in a cross-domain AI/runtime root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 16. Definition of done

This lane is mature when:

- [ ] Fauna Focus deny-sensitive tests run locally.
- [ ] Positive public-safe fixtures prove allowed responses remain within release scope.
- [ ] Denied, unreleased, rights-unclear, review-missing, withdrawn, and out-of-scope support paths are tested.
- [ ] Denial text, citations, receipts, logs, traces, and snapshots are checked for withheld-detail safety.
- [ ] Browser/API/model boundary is tested where implementation exists.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] Tests call canonical validators, policies, schemas, and Focus code rather than redefining behavior locally.
- [ ] CI exposes the denial proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna Focus deny-sensitive test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy/evidence/API/UI/e2e/domain tests, and Fauna Map UI Focus Mode denial obligations; executable tests, fixtures, Focus route names, policy modules, schemas, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
