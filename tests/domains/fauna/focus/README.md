<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/focus/readme
title: Fauna Focus Mode Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Fauna steward>
  - <PLACEHOLDER — Focus Mode steward>
  - <PLACEHOLDER — Citation/evidence steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; child citation and deny-sensitive lanes have open PRs; executable tests, fixtures, Focus route names, schemas, and CI not verified
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - tests/domains/fauna/focus/citation/README.md
  - tests/domains/fauna/focus/deny_sensitive/README.md
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
  - citation
  - deny-sensitive
  - evidence
  - evidence-ref
  - evidence-bundle
  - ai-receipt
  - finite-outcome
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Fauna Focus Mode Tests

> Parent test-lane contract for Fauna Focus Mode behavior: cite released evidence, deny or abstain when policy or evidence does not permit an answer, and keep AI-generated text downstream of governed evidence and policy.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Ffocus-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Ffocus-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: cite--or--abstain](https://img.shields.io/badge/posture-cite--or--abstain-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** parent Focus Mode test-lane README; not a model adapter, prompt, policy bundle, schema, fixture inventory, source registry, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `focus/`  
**Default posture:** cite-or-abstain; fail closed; public-safe fixtures; no-network by default  
**Last reviewed:** 2026-07-05

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [Parent Focus rule](#4-parent-focus-rule)
5. [Child lanes](#5-child-lanes)
6. [What belongs here](#6-what-belongs-here)
7. [What does not belong here](#7-what-does-not-belong-here)
8. [Parent proof matrix](#8-parent-proof-matrix)
9. [Fixture posture](#9-fixture-posture)
10. [Expected outcomes](#10-expected-outcomes)
11. [Lifecycle and publication boundaries](#11-lifecycle-and-publication-boundaries)
12. [No-network default](#12-no-network-default)
13. [Suggested local commands](#13-suggested-local-commands)
14. [Review burden](#14-review-burden)
15. [Related folders and files](#15-related-folders-and-files)
16. [Open questions](#16-open-questions)
17. [Definition of done](#17-definition-of-done)
18. [Changelog](#18-changelog)
19. [Last reviewed](#19-last-reviewed)

---

## 1. Purpose

This directory is the parent Fauna test lane for **Focus Mode** behavior.

It exists to prove that Fauna Focus Mode remains an interpretive, governed surface. It may summarize released evidence, explain public-safe derivatives, compare admissible evidence items, and expose finite negative outcomes. It must not become a root truth source, a publication gate, a policy engine, a source reader, or a route around the governed API.

A mature parent lane should support these claims:

1. **Focus Mode uses released evidence.** Public answers are grounded in released, admissible Fauna evidence.
2. **Citations are validated.** Evidence-dependent claims cite resolvable support or produce `ABSTAIN`, `DENY`, or `ERROR`.
3. **Policy gates run before answer emission.** Sensitivity, rights, release state, review state, and correction state can block or bound an answer.
4. **The browser is not a model client.** Public UI does not call a model runtime, vector index, graph store, object store, or source system directly.
5. **Negative outcomes are first-class.** Denied, abstained, stale, conflicted, withdrawn, or error states are testable outputs, not failures to be hidden.
6. **Receipts remain separate.** `AIReceipt` records an AI answer event; it does not replace evidence, proof, policy, or release state.
7. **Fixtures are public-safe.** Default tests use deterministic local fixtures and do not contain policy-withheld detail.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/focus/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna Focus Mode behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Test lane | `focus/` |
| Focus/API implementation home | `apps/governed-api/` as applicable. |
| Public UI home | `apps/explorer-web/` as applicable. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Schema homes | `schemas/contracts/v1/ai/` and `schemas/contracts/v1/ui/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second prompt, model, policy, evidence, proof, receipt, release, schema, fixture, or source-data home. It verifies Focus Mode behavior against those authorities.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows policy, evidence-resolution, governed API envelope, UI trust-state, e2e, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive Fauna location data from tests | CONFIRMED from current repo docs. |
| Fauna Map UI contract says Focus Mode uses released EvidenceBundles and validates citations before display/export | CONFIRMED from current repo docs. |
| Fauna Map UI contract says sensitivity, rights, and release state govern `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | CONFIRMED from current repo docs. |
| Child README branches for `citation/` and `deny_sensitive/` | Created in current session as open PRs; not assumed merged on `main`. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual Focus Mode route names, policy module names, schema names, and adapter paths | NEEDS VERIFICATION. |
| Actual fixtures and fixture manifests | NEEDS VERIFICATION. |
| Actual CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the parent test-lane contract. It does not claim that Focus Mode implementation, policy modules, citation validators, fixtures, routes, schemas, or CI jobs already exist.

---

## 4. Parent Focus rule

**Rule:** Fauna Focus Mode may answer only inside governed evidence, policy, release, and citation bounds.

Tests should fail when Focus Mode:

- answers from generated language alone;
- answers from map feature properties as if they were evidence;
- answers from raw, work, quarantine, candidate, unpublished, or internal material;
- skips sensitivity, rights, release, review, or correction checks;
- emits an evidence-dependent answer without validated citations;
- hides a required `ABSTAIN`, `DENY`, or `ERROR` outcome;
- treats an AI receipt as evidence support;
- leaks policy-withheld detail through text, citations, receipts, logs, snapshots, or traces; or
- routes the browser directly to a model, index, graph, object store, source system, or credentialed backend.

Tests may allow an `ANSWER` only when the request is within public-safe scope, citations are admissible, and the answer remains bounded to released evidence.

---

## 5. Child lanes

Expected or active child lanes include:

| Child lane | Responsibility | Status boundary |
|---|---|---|
| `citation/` | Prove cite-or-abstain behavior for Fauna Focus Mode answers. | README work may exist in an open PR; executable tests NEEDS VERIFICATION. |
| `deny_sensitive/` | Prove fail-closed denial behavior for policy-limited requests. | README work may exist in an open PR; executable tests NEEDS VERIFICATION. |
| `evidence_scope/` | Prove Focus Mode only uses admissible released evidence for current scope. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `receipt/` | Prove `AIReceipt` records generated-answer events without replacing evidence. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `browser_boundary/` | Prove browser routes through governed API and does not call model/index/store directly. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `negative_outcomes/` | Prove finite outcomes are surfaced consistently. | PROPOSED / NEEDS VERIFICATION unless implemented. |

Additional child lanes may be added when they have a clear test responsibility and do not duplicate another authority root.

---

## 6. What belongs here

This directory may contain:

- README and parent-lane contract material for Fauna Focus Mode tests.
- Parent-level tests that verify Focus Mode envelope behavior for Fauna.
- Tests that verify citation, evidence-resolution, policy pre-check, release-state, and finite-outcome behavior.
- Tests that verify public Focus Mode calls go through governed API surfaces.
- Tests that verify `AIReceipt` linkage without evidence substitution.
- Tests that coordinate child lanes such as `citation/` and `deny_sensitive/`.
- Public-safe fixtures for positive and negative Focus Mode cases.
- Tiny local examples when they are not reusable fixture records and the reason is documented.

---

## 7. What does not belong here

This directory must not contain:

- Model prompts, provider adapters, model-runtime code, or production Focus Mode implementation.
- Raw Fauna source records, candidate evidence, source caches, or unreleased records.
- Policy definitions, schema definitions, source registry records, receipts, proofs, release decisions, or rollback decisions.
- Reusable fixture inventories that belong under `fixtures/domains/fauna/`.
- Test snapshots, traces, or logs that include policy-withheld details.
- Tests that require live network access or live model calls by default.

[↑ Back to top](#top)

---

## 8. Parent proof matrix

| Test concern | Required proof | Preferred lane behavior |
|---|---|---|
| Governed API boundary | Browser/UI does not call model/index/store directly. | API/UI boundary assertion. |
| Citation validation | Every evidence-dependent answer cites admissible support. | `citation/` or parent assertion. |
| Evidence release scope | Public answers use released evidence only. | Evidence-resolution assertion. |
| Policy pre-check | Sensitivity, rights, release, review, and correction state can block answer. | `deny_sensitive/` or policy assertion. |
| Finite outcomes | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` are explicit. | Runtime envelope assertion. |
| Negative outcome visibility | Denied/abstained/error states are exposed to UI without hidden fallback answer. | UI trust-state assertion. |
| Receipt boundary | AI receipt records event but does not become evidence support. | Receipt assertion. |
| Public-safe derivative bound | Answer stays within release/transform scope. | Positive bounded-answer test. |
| No hidden detail | Text, citations, receipts, logs, traces, and snapshots omit policy-withheld detail. | Safety/snapshot guard. |
| No-network default | Tests use local public-safe fixtures and no live model/source calls. | Harness guard. |

---

## 9. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Expected fixture families include:

| Fixture family | Purpose |
|---|---|
| Public-safe allowed Focus query | Proves allowed Focus answer with citations. |
| Missing citation query | Proves uncited claim abstains or fails validation. |
| Missing evidence query | Proves unresolved support does not answer. |
| Policy-denied query | Proves denied requests produce safe `DENY`. |
| Rights/review blocked query | Proves governance state blocks public answer. |
| Withdrawn/corrected support query | Proves stale support is not treated as current truth. |
| Public-safe derivative query | Proves explanation remains bounded to released scope. |
| Browser-boundary fixture | Proves Focus requests use governed API fixtures only. |
| AIReceipt fixture | Proves receipt linkage without evidence substitution. |

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They must not include raw source payloads, unreleased evidence, or policy-withheld details.

---

## 10. Expected outcomes

Fauna Focus tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

| Condition | Preferred outcome |
|---|---|
| Public-safe request with released admissible evidence | `ANSWER` with citations and receipt linkage. |
| Citation missing or unresolved | `ABSTAIN`, `ERROR`, or validation failure. |
| Evidence missing | `ABSTAIN` or validation failure. |
| Policy blocks answer | `DENY`, `ABSTAIN`, or workflow-facing `HOLD`. |
| Release state withdrawn or superseded | `ABSTAIN`, `ERROR`, or corrected-state answer. |
| Conflicting support | `ANSWER` with conflict visible or `ABSTAIN`. |
| Browser attempts direct model/source call in default test | Test failure. |
| Output contains policy-withheld detail | Test failure. |

---

## 11. Lifecycle and publication boundaries

This lane supports KFM verification but does not move records through the lifecycle:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Boundary | Rule |
|---|---|
| RAW | Do not store raw Fauna records here. |
| WORK / QUARANTINE | Do not store candidate or quarantined records here. |
| PROCESSED | Do not store processed Fauna products here. |
| CATALOG / TRIPLET | Do not treat Focus test fixtures as catalog or graph truth. |
| PUBLISHED | Tests never publish. |
| RECEIPTS / PROOFS | Tests may assert references; trust-bearing records stay in their roots. |
| RELEASE | Release decisions remain under `release/`. |

A passing Focus Mode test proves behavior for the checked scenario. It is not evidence creation, policy approval, release approval, proof, or publication.

---

## 12. No-network default

Default Fauna Focus tests must avoid:

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

## 13. Suggested local commands

> [!NOTE]
> Command names, Focus Mode route names, markers, and CI jobs are **NEEDS VERIFICATION** until checked against actual repository configuration.

Likely parent lane check:

```bash
pytest tests/domains/fauna/focus
```

Likely child lane checks:

```bash
pytest tests/domains/fauna/focus/citation
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

## 14. Review burden

Reviewers should be able to answer:

- Does this lane verify Focus Mode behavior rather than define prompts or model behavior locally?
- Does Focus Mode use released, admissible evidence for public answers?
- Are citations validated before display/export?
- Do sensitivity, rights, release, review, and correction states block or bound answers?
- Are `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` explicit and testable?
- Does the browser avoid direct model/index/store/source calls?
- Do fixtures remain deterministic, public-safe, and no-network?
- Are routes, schemas, validators, policies, evidence bundles, receipts, proofs, releases, and production code kept in canonical roots?
- Are implementation gaps marked **NEEDS VERIFICATION** instead of hidden?

---

## 15. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/README.md` | Root test contract for policy, evidence-resolution, API envelope, UI trust-state, e2e, runtime-proof, and domain tests. | CONFIRMED. |
| `docs/doctrine/directory-rules.md` | Domain segment rule for `tests/domains/<domain>/`. | CONFIRMED. |
| `docs/domains/fauna/MAP_UI_CONTRACTS.md` | Focus Mode, Evidence Drawer, citation, policy, and finite outcome obligations. | CONFIRMED. |
| `docs/domains/fauna/SENSITIVITY.md` | Fauna sensitivity and geoprivacy posture. | CONFIRMED. |
| `tests/domains/fauna/focus/citation/` | Citation validation sublane. | README may exist in open PR; executable tests NEEDS VERIFICATION. |
| `tests/domains/fauna/focus/deny_sensitive/` | Deny-sensitive sublane. | README may exist in open PR; executable tests NEEDS VERIFICATION. |
| `fixtures/domains/fauna/` | Reusable public-safe fixture home. | Inventory NEEDS VERIFICATION. |
| `policy/domains/fauna/` | Domain policy home. | Behavior NEEDS VERIFICATION. |
| `policy/sensitivity/fauna/` | Sensitivity policy home. | Behavior NEEDS VERIFICATION. |
| `data/receipts/` | Receipt home including AI/process receipts where implemented. | NEEDS VERIFICATION. |
| `data/proofs/fauna/` | Domain proof/evidence support, if present. | NEEDS VERIFICATION. |
| `schemas/contracts/v1/ai/` | Focus/AI response schema home when present. | NEEDS VERIFICATION. |
| `apps/governed-api/` | Focus/API implementation home when present. | NEEDS VERIFICATION. |
| `apps/explorer-web/` | Public UI home when present. | NEEDS VERIFICATION. |

---

## 16. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical Focus Mode response schema? | NEEDS VERIFICATION | Must inspect schema tree. |
| What is the canonical AIReceipt shape? | NEEDS VERIFICATION | Do not invent fields beyond docs. |
| Which route or service owns Focus Mode for Fauna? | NEEDS VERIFICATION | Must inspect implementation. |
| Which policy module owns Fauna Focus pre-checks? | NEEDS VERIFICATION | Must inspect policy roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/fauna/`. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared Focus Mode tests live here or in a cross-domain AI/runtime root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 17. Definition of done

This parent lane is mature when:

- [ ] Fauna Focus Mode tests run locally.
- [ ] Citation and deny-sensitive child lanes have executable proof where implementation exists.
- [ ] Positive public-safe fixtures prove allowed responses remain within release and evidence scope.
- [ ] Missing, unresolved, denied, stale, conflicted, corrected, withdrawn, and out-of-scope support paths are tested.
- [ ] AIReceipt linkage is tested without replacing evidence support.
- [ ] Browser/API/model boundary is tested where implementation exists.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] Tests call canonical validators, policies, schemas, and Focus code rather than redefining behavior locally.
- [ ] CI exposes the Focus proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 18. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Fauna Focus Mode parent test lane. |

---

## 19. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for policy/evidence/API/UI/e2e/runtime/domain tests, and Fauna Map UI Focus Mode obligations; executable tests, fixtures, Focus route names, policy modules, schemas, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
