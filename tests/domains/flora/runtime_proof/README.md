<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/runtime-proof/readme
title: Flora Runtime Proof Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Runtime steward>
  - <PLACEHOLDER — Governed API steward>
  - <PLACEHOLDER — Evidence steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, runtime envelopes, validators, governed API routes, and CI not verified
related:
  - tests/README.md
  - tests/runtime_proof/
  - tests/domains/flora/README.md
  - tests/domains/flora/citation/README.md
  - tests/domains/flora/evidence_closure/README.md
  - tests/domains/flora/policy/README.md
  - tests/domains/flora/policy_deny/README.md
  - tests/domains/flora/release_manifest/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - docs/domains/flora/API_CONTRACTS.md
  - fixtures/domains/flora/
  - contracts/runtime/runtime_response_envelope.md
  - contracts/runtime/decision_envelope.md
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - release/
tags:
  - kfm
  - tests
  - flora
  - runtime-proof
  - finite-outcome
  - runtime-response-envelope
  - decision-envelope
  - governed-api
  - evidence
  - cite-or-abstain
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Runtime Proof Tests

> Test-lane contract for proving Flora runtime surfaces return finite, inspectable outcomes and preserve governed boundaries before any claim, drawer payload, Focus answer, map detail, export, or public response reaches a user.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Fruntime__proof-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Fruntime__proof-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: finite--outcome-blue](https://img.shields.io/badge/posture-finite--outcome-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** runtime-proof test-lane README; not a runtime implementation, governed API route, schema home, contract home, policy bundle, fixture inventory, evidence store, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `runtime_proof/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; cite-or-abstain; public outputs use governed responses only  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **runtime proof**.

It exists to prove that Flora runtime surfaces produce one of the governed finite outcomes and do not bypass evidence, policy, release, sensitivity, rights, review, or lifecycle gates. Runtime-proof tests check behavior at the public response boundary. They do not implement routes, define envelopes, create evidence, publish releases, or authorize policy decisions.

A mature lane should prove:

1. Flora runtime responses use a finite outcome vocabulary.
2. `ANSWER` is emitted only when evidence resolves, policy permits, release state allows, and review state is valid where required.
3. `ABSTAIN` is emitted when evidence or citation support is insufficient.
4. `DENY` is emitted when policy, rights, sensitivity, or release state forbids the response.
5. `ERROR` is bounded, diagnostic, and does not expose unsupported claims.
6. Runtime responses preserve trust-state metadata, citations, release references, and negative reasons where required.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/runtime_proof/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora finite-outcome runtime behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `runtime_proof/` |
| Cross-domain runtime proof root | `tests/runtime_proof/` when present. |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Runtime contract homes | `contracts/runtime/` when present. |
| Domain contract/schema homes | `contracts/domains/flora/` and `schemas/contracts/v1/domains/flora/` when present. |
| Policy homes | `policy/domains/flora/` and `policy/sensitivity/flora/`. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second runtime implementation, route home, schema home, contract home, policy home, fixture inventory, evidence store, receipt home, proof home, release home, public artifact home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows runtime-proof tests and governed API envelope tests | CONFIRMED from current repo docs. |
| `tests/README.md` says governed API envelope tests must return finite `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` outcomes and never expose internal-store content | CONFIRMED from current repo docs. |
| `tests/README.md` excludes live network calls, duplicate authority homes, trust-bearing records, release decisions, and sensitive production data from `tests/` | CONFIRMED from current repo docs. |
| Flora API docs define governed Flora runtime outcomes as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, with optional `HOLD`, `NARROWED`, and `BOUNDED` handling where applicable | CONFIRMED from current repo docs. |
| Flora API docs state public clients use governed APIs and do not directly read internal lifecycle stores or runtime engines | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual runtime envelope schemas, governed API routes, validators, fixtures, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that runtime-proof tests, fixtures, routes, validators, runtime schemas, or CI checks already exist.

---

## 4. Runtime-proof rule

**Rule:** A Flora runtime response may pass only when it returns a finite outcome, carries required trust-state metadata for that outcome, and does not expose unsupported claims or bypass governed lifecycle boundaries.

Tests should fail or require a finite negative outcome when:

- a response has no outcome;
- outcome value is outside the governed finite vocabulary;
- `ANSWER` is returned without resolved evidence, policy allow, release state, and required review state;
- `ABSTAIN` emits a claim despite missing evidence or citation support;
- `DENY` is hidden from the caller;
- `ERROR` is unbounded or emits unsupported claim material;
- runtime output bypasses governed response boundaries;
- stale, superseded, or corrected support lacks trust-visible state;
- generated text is treated as evidence; or
- fixtures, receipts, proofs, release decisions, or production runtime outputs are stored under `tests/`.

Tests may allow a response only when the fixture is public-safe, no-network, governed by canonical contracts/validators, and bounded to the test scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Outcome required | Runtime response always carries a finite outcome. | Envelope assertion. |
| Allowed outcome set | Outcome is in governed vocabulary. | Contract assertion. |
| Answer proof | `ANSWER` requires evidence, policy, release, and review support where required. | `ANSWER` with citations/trust state. |
| Abstain proof | Missing evidence or citation support does not produce a claim. | `ABSTAIN`. |
| Deny proof | Policy/rights/sensitivity/release block returns visible denial. | `DENY`. |
| Error proof | Malformed input or evaluator failure is bounded. | `ERROR`. |
| Boundary proof | Public runtime uses governed response boundaries. | Boundary assertion. |
| Stale/correction state | Stale, corrected, or superseded support is visible and bounded. | Trust-state assertion. |
| AI boundary | Generated text is downstream of evidence and not evidence itself. | Boundary assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain README material and tests that call canonical runtime, governed API, evidence, policy, release, citation, UI/API, and validator code from owning roots.

It may include negative tests for missing outcome, invalid outcome, answer-without-evidence, abstain-with-claim, hidden denial, unbounded error, boundary bypass, stale-state omission, and generated-text-as-evidence.

It may include positive tests for public-safe runtime fixtures that prove allowed `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior.

## 7. What does not belong here

This directory must not contain runtime implementation, governed API route definitions, schemas, contracts, policy definitions, production evidence, source records, reusable fixture inventories, trust-bearing receipts, proofs, release decisions, published artifacts, production runtime outputs, generated model output, or default tests that require live network access.

---

## 8. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model runtime outcome states rather than become evidence bundles, policy decisions, receipts, proofs, release decisions, or production outputs.

Expected fixture families include valid answer, missing evidence abstain, citation failure abstain, policy denial, rights denial, release-state denial, malformed request error, schema error, stale support bounded answer, corrected support bounded answer, boundary-bypass anti-pattern, hidden-denial anti-pattern, unbounded-error anti-pattern, and generated-text-as-evidence anti-pattern.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/runtime_proof
pytest tests/runtime_proof
pytest tests/domains/flora/policy
pytest tests/domains/flora/evidence_closure
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which runtime envelope schema is canonical? | NEEDS VERIFICATION | Must inspect `contracts/runtime/` and schema roots. |
| Which governed API routes, if any, are implemented for Flora? | NEEDS VERIFICATION | Must inspect app/API roots. |
| Which validator owns finite-outcome checks? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which UI surfaces consume Flora runtime outcomes? | NEEDS VERIFICATION | Must inspect UI/API implementation. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared finite-outcome tests live here or under `tests/runtime_proof/`? | OPEN | This lane should own Flora-specific runtime expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora runtime-proof tests run locally.
- [ ] Valid answer, missing evidence abstain, citation failure abstain, policy denial, rights denial, release-state denial, malformed request error, schema error, stale support, corrected support, boundary bypass, hidden denial, unbounded error, and generated-text-as-evidence cases are tested.
- [ ] Positive public-safe fixtures prove allowed runtime behavior without becoming release approval.
- [ ] Negative fixtures prove finite outcomes and governed-boundary enforcement.
- [ ] Tests call canonical runtime/evidence/policy/release/citation validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora runtime proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora runtime-proof test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for runtime-proof/governed API envelope/domain tests, and Flora finite-outcome/governed-boundary doctrine; executable tests, fixtures, runtime schemas, validators, governed API routes, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
