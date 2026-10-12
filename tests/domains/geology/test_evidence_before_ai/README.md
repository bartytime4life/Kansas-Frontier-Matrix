<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-test-evidence-before-ai-readme
title: Geology Evidence-Before-AI Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Governed-AI steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; geology; evidence-before-ai; no-network; cite-or-abstain; release-gated; source-role-aware
tags: [kfm, tests, geology, evidence-before-ai, governed-ai, EvidenceRef, EvidenceBundle, FocusModePayload, AIReceipt, ABSTAIN, DENY, ERROR, cite-or-abstain]
related:
  - ../../../../tests/README.md
  - ../../../../fixtures/domains/geology/README.md
  - ../../../../packages/domains/geology/evidence/README.md
  - ../../../../docs/focus-mode/state/payload-state.md
  - ../../../../docs/domains/geology/README.md
  - ../../../../docs/domains/geology/API_CONTRACTS.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../contracts/domains/geology/
  - ../../../../schemas/contracts/v1/domains/geology/
  - ../../../../policy/domains/geology/
  - ../../../../data/registry/sources/geology/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This file replaces a blank placeholder at tests/domains/geology/test_evidence_before_ai/README.md."
  - "This is a test-lane README only. It does not define AI runtime behavior, prompts, model adapters, evidence storage, schemas, policy rules, receipts, proofs, source descriptors, release decisions, or published artifacts."
  - "The tested invariant is evidence and policy context before AI interpretation: generated language must never create geology truth or bypass EvidenceRef -> EvidenceBundle resolution."
  - "The default posture is deterministic and no-network. Live model calls, live source checks, credentials, and real sensitive geology/resource locations do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology evidence-before-AI tests

> Deterministic, no-network test documentation for proving that Geology and Natural Resources AI-facing answers are blocked unless evidence, source role, policy, review, release, and citation closure are established first.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology%2Fnatural__resources-brown">
  <img alt="Invariant: evidence before AI" src="https://img.shields.io/badge/invariant-evidence__before__AI-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Outcome: cite or abstain" src="https://img.shields.io/badge/outcome-cite__or__abstain-success">
</p>

**Path:** `tests/domains/geology/test_evidence_before_ai/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `geology`  
**Test lane:** `test_evidence_before_ai`  
**Default execution posture:** deterministic, synthetic, no-network, no live model calls, public-safe  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED KFM testing doctrine places domain-specific tests under `tests/domains/<domain>/` · CONFIRMED Geology evidence package doctrine requires resolvable evidence support before authoritative claims · CONFIRMED Focus Mode payload-state doctrine requires citation closure and released evidence before `ANSWER` · NEEDS VERIFICATION for actual test modules, fixtures, governed-AI runtime adapters, schemas, validators, policy engine wiring, CI coverage, AIReceipt emission, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/geology/test_evidence_before_ai/` is the intended home for tests that prove AI-facing Geology behavior remains evidence-subordinate.

This lane should test that a Geology AI surface, Focus Mode answer, Evidence Drawer summary, or runtime envelope cannot produce an authoritative answer unless:

- every claim-bearing statement has an `EvidenceRef`;
- each required `EvidenceRef` resolves to an acceptable `EvidenceBundle` or produces a finite non-answer;
- source role supports the claim type;
- policy, sensitivity, review, and release context allow the requested exposure;
- citation closure holds for the requested area, time, subject, and claim class;
- the output preserves correction and rollback visibility when material.

A passing test here should **not** mean that an AI answer is wise, complete, publishable, or scientifically final. It should mean only that the AI boundary did not run ahead of governed evidence.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Geology appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Domain AI-boundary tests | `tests/domains/geology/test_evidence_before_ai/` | This directory. |
| Synthetic fixtures and expected outcomes | `fixtures/domains/geology/` | Preferred source for toy inputs and expected envelopes. |
| Evidence helper code | `packages/domains/geology/evidence/` | System under test where helper behavior exists. |
| Focus Mode state doctrine | `docs/focus-mode/state/` | Referenced for payload closure and finite outcomes. |
| Semantic object meaning | `contracts/domains/geology/` | Referenced by tests, not redefined here. |
| Machine shape | `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/focus_mode/` if accepted | Referenced by tests, not duplicated here. |
| Policy decisions | `policy/domains/geology/`, `policy/sensitivity/geology/` | Referenced by tests, not bypassed here. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Expected references; not authored as test truth here. |
| Release decisions | `release/` | Required before public answer; tests cannot replace it. |

---

## Invariant under test

> **Evidence before AI.** The AI layer may interpret released, policy-admitted evidence, but it must not create root truth, fill missing citations, upgrade weak source roles, override sensitivity decisions, or answer from unpublished/internal records.

For this test lane, the invariant decomposes into eight checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Evidence presence | Claim candidate includes required `EvidenceRef` values before answer shaping. | `ABSTAIN` or validation failure. |
| Evidence resolution | Required `EvidenceRef` values resolve to an acceptable `EvidenceBundle`. | `ABSTAIN` / `ERROR`. |
| Source-role support | Source role can support the requested geology claim class. | `DENY`, `RESTRICT`, or validation failure. |
| Policy posture | Rights, sensitivity, geometry exposure, and review state are explicit. | `DENY`, `RESTRICT`, or `ABSTAIN`. |
| Release state | AI answer uses released or explicitly allowed public-safe payloads only. | `ABSTAIN (not_yet_released)` or failure. |
| Citation closure | Every answer claim is citable within subject/time/area scope. | `ABSTAIN (evidence_insufficient)` or failure. |
| AI receiptability | Runtime can emit or reference receipt-ready metadata for replay. | validation failure / NEEDS VERIFICATION. |
| No generated truth | Generated text never becomes evidence, source authority, policy authority, or release authority. | test failure. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- evidence helper behavior for `EvidenceRef` presence and resolution gates;
- Focus Mode payload state behavior for `fresh`, `stale`, `not-yet-released`, `revoked-but-cached`, and `unknown` states;
- runtime envelope behavior for `ANSWER`, `ABSTAIN`, `DENY`, `RESTRICT`, and `ERROR` outcomes;
- refusal to answer when a geology claim lacks source-role support;
- refusal to answer when exact sensitive geology/resource geometry lacks an approved public-safe transform;
- refusal to answer from `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, or unreleased `CATALOG / TRIPLET` records;
- refusal to use AI text as a substitute for missing citations;
- citation-bearing answer shaping when all evidence, policy, review, and release checks pass.

Live LLM/provider calls are out of scope for the default suite. Use mocks or deterministic stub envelopes.

---

## Fixture posture

Use fixture material from `fixtures/domains/geology/` when possible.

Fixture requirements:

- synthetic and public-safe;
- no live model calls;
- no live source calls;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source-role posture;
- explicit evidence-resolution state;
- explicit policy/release state;
- no real exact borehole, private-well, mineral, extraction, reclamation, infrastructure-sensitive, or resource-location detail.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Fully supported public-safe claim | `fixtures/domains/geology/valid/` or `golden/` | `ANSWER` allowed with citations, policy permitting. |
| Missing EvidenceRef | `fixtures/domains/geology/invalid/` | `ABSTAIN (evidence_missing)`. |
| Unresolved EvidenceBundle | `fixtures/domains/geology/invalid/` | `ABSTAIN` or `ERROR`, depending resolver semantics. |
| Source-role mismatch | `fixtures/domains/geology/source_role/` | `DENY`, `RESTRICT`, or closure failure. |
| Sensitive exact geometry | `fixtures/domains/geology/tier-transitions/` | `DENY` / `RESTRICT` unless public-safe transform is present. |
| Payload not released | `fixtures/domains/geology/map-ui/` or `golden/` | `ABSTAIN (not_yet_released)`. |
| Stale or revoked payload | `fixtures/domains/geology/tier-transitions/` | `ABSTAIN` or `ERROR`, never `ANSWER`. |

---

## Assertions

A good evidence-before-AI test should make the forbidden shortcut obvious.

### Positive path

- all claim-bearing answer fragments include citations or evidence bindings;
- evidence bundle references resolve in the test context;
- policy context permits public-safe answer shaping;
- payload state is fresh or equivalent accepted state;
- AI output remains a downstream carrier;
- AIReceipt or receipt-ready metadata records evidence touched, answer outcome, and non-answer reasons where material.

### Negative path

- missing evidence produces `ABSTAIN`, not a guessed explanation;
- unresolved evidence produces `ABSTAIN` or `ERROR`, not a fluent answer;
- unreleased evidence produces `ABSTAIN (not_yet_released)`;
- stale evidence produces `ABSTAIN (payload_stale)` or rebinds to a newer released bundle;
- revoked evidence produces `ABSTAIN`, never `ANSWER`;
- sensitive exact geometry produces `DENY` or `RESTRICT` unless a public-safe transform is approved;
- model output is never accepted as evidence input;
- public UI/API payloads never read raw/work/quarantine/internal records directly.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Evidence resolves, policy permits, release state is public-safe | `ANSWER` with citations. |
| Evidence is missing | `ABSTAIN (evidence_missing)` or repo-accepted equivalent. |
| Evidence cannot resolve | `ABSTAIN` or `ERROR`, depending resolver semantics. |
| Evidence is not yet released | `ABSTAIN (not_yet_released)`. |
| Evidence is stale | `ABSTAIN (payload_stale)` unless safely rebound. |
| Evidence is revoked | `ABSTAIN (revoked_no_alternative)` or repo-accepted equivalent. |
| Source role cannot support claim | `DENY`, `RESTRICT`, or validation failure. |
| Rights/sensitivity forbids exposure | `DENY` or `RESTRICT`. |
| Runtime invariant breaks | `ERROR` or test failure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- call live LLM providers;
- call local model runtimes as part of the default suite;
- fetch live upstream source systems;
- store credentials or tokens;
- store real source exports;
- store exact sensitive geology/resource locations;
- redefine schemas, policies, contracts, source descriptors, receipts, proofs, evidence bundles, or release decisions;
- bypass `EvidenceRef -> EvidenceBundle` resolution;
- bypass policy with a fixture flag;
- let generated text patch missing citations;
- treat AI summaries, graph edges, map layers, tiles, screenshots, or public-safe geometry as root truth;
- publish, promote, or release anything.

Any test that requires a real provider belongs in a separately gated runtime-integration suite with explicit policy, credentials, logging, and receipt controls.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/geology/test_evidence_before_ai/
├── README.md
├── test_evidence_required_before_answer.py       # missing/unresolved evidence -> non-answer
├── test_focus_payload_state_blocks_answer.py     # stale/not-yet-released/revoked/unknown payloads
├── test_source_role_before_interpretation.py     # source-role anti-collapse before AI text
├── test_policy_release_before_ai_answer.py       # sensitivity/release gates before ANSWER
└── test_no_generated_truth.py                    # model text cannot become evidence or release authority
```

Keep helpers local only when they are test-specific. Shared evidence, policy, runtime-envelope, or Focus Mode behavior belongs under its accepted implementation root, not duplicated here.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/geology/test_evidence_before_ai
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that the test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- no live model/provider calls;
- fail closed on missing evidence, unresolved evidence, missing policy, missing release state, stale payloads, revoked payloads, or sensitive public exposure;
- provider/runtime checks: separate gated job only;
- release gate: evidence-before-AI failures should block public AI answer promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/geology/test_evidence_before_ai/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default suite should avoid sensitive data and live network calls. | Does not prove this lane's modules or pass rate. |
| `packages/domains/geology/evidence/README.md` | CONFIRMED doctrine / PROPOSED implementation | Evidence helpers require resolvable evidence support, citation closure, finite outcomes, and evidence-subordinate Focus Mode preparation. | Does not prove imports, helper code, tests, or runtime behavior. |
| `docs/focus-mode/state/payload-state.md` | CONFIRMED doctrine / PROPOSED implementation | Focus Mode payload state requires citation closure; only fresh, released, non-revoked evidence can allow `ANSWER`, policy permitting. | File notes path placement is itself PROPOSED / drift-tracked; does not prove runtime enforcement. |
| `docs/domains/geology/README.md` | CONFIRMED doctrine / PROPOSED implementation | Geology scope, anti-collapse rules, lifecycle invariant, public trust path, and test/fixture placement. | Does not prove evidence-before-AI tests exist. |
| `fixtures/domains/geology/README.md` | CONFIRMED | Synthetic, public-safe fixture posture and child fixture lanes for Geology. | Does not prove all fixture payloads or consumers. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for supported answer, missing evidence, unresolved evidence, source-role mismatch, unreleased payload, stale payload, revoked payload, sensitive geometry, and generated-truth rejection.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] Focus Mode payload-state behavior is available to tests or safely stubbed.
- [ ] PolicyDecision behavior is available to tests or safely stubbed.
- [ ] AI/runtime envelope schema or contract path is accepted.
- [ ] AIReceipt or receipt-ready metadata expectations are defined before enforcing them.
- [ ] CI runs the no-network evidence-before-AI suite.
- [ ] Failures block public AI answer promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes an AI-runtime implementation root, prompt library, model-output store, source registry, fixture root, lifecycle data store, proof store, receipt store, release-decision root, schema authority, policy authority, public map/API surface, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
