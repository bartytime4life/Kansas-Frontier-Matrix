# `runtime/release/` — Runtime Release Handoff Lane

Runtime handoff notes for release-adjacent behavior. This lane may document runtime support for release checks, finite outcomes, evidence/policy/release pointers, and receipt handoff, but it does not own release decisions, manifests, correction records, rollback records, lifecycle data, or public-client authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-release-readme
title: runtime/release/README.md — Runtime Release Handoff Lane
type: readme; directory-readme; runtime-release-guardrail; release-handoff-index
version: v0.1
status: draft; empty-path-expanded; no-runtime-release-implementation-confirmed; NEEDS VERIFICATION
owners: OWNER_TBD — Runtime steward · Release steward · Policy steward · Evidence steward · QA steward · Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-05
policy_label: public; runtime; release; handoff; receipts; no-release-authority
tags: [kfm, runtime, release, release-handoff, finite-outcomes, receipts, correction, rollback]
related:
  - ../README.md
  - ../AI/README.md
  - ../model_adapters/README.md
  - ../envelopes/README.md
  - ../../release/README.md
  - ../../data/
  - ../../policy/
  - ../../contracts/
  - ../../schemas/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
notes:
  - "Expanded from an empty runtime/release/README.md."
  - "Current-session search found no direct runtime/release files beyond this README."
  - "runtime/ is confirmed as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release."
  - "release/ is confirmed as the release-governance root for candidates, reviews, promotion decisions, manifests, decisions, policy review pointers, corrections, notices, changelog, signatures, and release-facing records."
  - "This README does not prove runtime-release implementation, release integration, policy enforcement, validation coverage, receipt emission, release readiness, or public-client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: runtime" src="https://img.shields.io/badge/root-runtime%2F-blue">
  <img alt="Lane: release handoff" src="https://img.shields.io/badge/lane-release__handoff-purple">
  <img alt="Boundary: not release authority" src="https://img.shields.io/badge/boundary-not__release__authority-critical">
</p>

**Status:** draft / runtime-release handoff guardrail
**Path:** `runtime/release/`
**Current role:** README-only runtime handoff/index lane for release-adjacent runtime behavior
**Truth posture:** CONFIRMED empty README path before this update; CONFIRMED no direct implementation files found in current search; CONFIRMED adjacent `runtime/`, `runtime/envelopes/`, and `release/` boundary docs; NEEDS VERIFICATION for implementation code, tests, fixtures, release records, receipt wiring, CI, and steward ownership.

## Purpose

`runtime/release/` documents runtime handoffs that support release-adjacent checks without becoming release governance.

Use this lane for notes about runtime calls that help prepare, check, summarize, or explain release readiness only when they preserve evidence pointers, policy posture, finite outcomes, receipts, correction state, rollback posture, and release authority separation.

This path is a handoff/index lane only. It should not become release records, release approval logic, or publication state.

## Authority boundary

| Responsibility | Correct home | This lane's role |
|---|---|---|
| Runtime wiring, adapters, and envelopes | `runtime/` | Documents runtime support posture. |
| Release governance, decisions, manifests, corrections, notices, changelog | `release/` | References release records only; cannot approve them. |
| Lifecycle records, receipts, proofs, catalog, published artifacts | `data/` and accepted trust-object homes | References governed objects by pointer only. |
| Semantic meaning | `contracts/` | References contracts only. |
| Machine-checkable shape | `schemas/` | References schemas only. |
| Policy/admissibility | `policy/` | Requires policy state; does not decide it. |
| Fixtures, tests, validators | `fixtures/`, `tests/`, `tools/validators/` | Requires proof before behavior is claimed. |

> [!IMPORTANT]
> A runtime-release handoff is not a release decision. Runtime output may support review or readiness checks, but release state changes require governed release records, steward review, validation support, policy support, correction/rollback posture, and auditable receipts.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `runtime/release/README.md` | present | Empty file expanded by this README. |
| `runtime/release/*` | no files found in current search | No implementation, release-handoff cards, tests, fixtures, or configs confirmed under this path. |
| `runtime/README.md` | present | Runtime root for local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release. |
| `runtime/AI/README.md` | present | Governed AI runtime compatibility/index lane. |
| `runtime/model_adapters/README.md` | present | Provider-neutral model adapter lane. |
| `runtime/envelopes/README.md` | present | Finite-outcome runtime envelope helper lane. |
| `release/README.md` | present | Canonical release governance root. |

## Repo fit

```text
runtime/
├── README.md
├── release/
│   └── README.md                     # this file; runtime release handoff/index lane
├── AI/
├── model_adapters/
├── mock/
├── envelopes/
├── ollama/
├── local/
└── service_configs/

release/                              # release governance, decisions, corrections, rollback, notices
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
policy/                               # allow / deny / restrict / abstain posture
contracts/                            # semantic meaning
schemas/                              # machine-checkable shape
fixtures/                             # deterministic examples
tests/                                # executable proof of behavior
tools/validators/                     # validator implementation
```

## Runtime-release responsibilities

| Responsibility | Requirement |
|---|---|
| Preserve release authority | Release decisions, manifests, corrections, rollback, notices, and changelog remain under `release/`. |
| Preserve lifecycle state | Runtime does not move or publish data; it references governed `data/` records by pointer. |
| Preserve finite outcomes | Runtime support should return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` where applicable. |
| Preserve policy posture | Runtime support must honor policy, rights, sensitivity, access, stale-state, correction, and release checks. |
| Preserve evidence posture | Evidence support must resolve before answer-like release summaries are produced. |
| Preserve receipt posture | Link AIReceipt, RunReceipt, validation receipt, or RuntimeResponseEnvelope when behavior is claimed. |
| Preserve correction and rollback posture | Runtime notes may surface correction/rollback status, but cannot change it. |
| Preserve fail-closed behavior | Missing evidence, policy, release decision, correction state, or validation support should produce finite blockers, not release claims. |

## Allowed handoff flow

```text
release candidate / review / manifest / correction context
  -> runtime support checks scope, evidence, policy, validation, correction, and release state
  -> adapter/local/mock runtime runs only if allowed
  -> finite RuntimeResponseEnvelope / DecisionEnvelope is returned
  -> receipt or run pointer is emitted/linked where applicable
  -> release steward or governed release process consumes it as support material
  -> release/ remains authoritative for release state
```

Runtime output can support a release review, but it cannot itself approve release, publish data, correct a release, withdraw a release, or authorize rollback.

## What belongs here

- This README.
- Runtime-release handoff notes.
- Runtime support cards for release-readiness explanations or review support.
- Notes mapping runtime outcomes to release blockers, review material, or readiness summaries.
- Pointers to release records, runtime envelopes, AIReceipt/RunReceipt records, validation receipts, fixtures, tests, and validators.
- Notes explaining how runtime behavior stays subordinate to evidence, policy, validation, review, release, correction, and rollback gates.

## What does not belong here

| Do not put this in `runtime/release/` | Correct home |
|---|---|
| Release manifests, promotion decisions, release decisions, correction notices, rollback records, changelog entries | `release/` |
| Lifecycle data, emitted artifacts, receipts, proofs, catalogs, published payloads | accepted `data/` lifecycle/proof/receipt/catalog roots |
| Canonical semantic contracts | `contracts/` |
| JSON Schema definitions | `schemas/` |
| Policy rules or policy decisions | `policy/` and governed review/release roots |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` |
| Validator source code | `tools/validators/` |
| Model adapter implementation | accepted runtime adapter lane |
| Public API routes or UI components | accepted app or UI roots |
| Generated text treated as evidence, validation, review, release, correction, rollback, or publication authority | nowhere |

## Validation

```bash
find runtime/release -maxdepth 4 -type f | sort
find runtime release data policy contracts schemas fixtures tests tools/validators -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/runtime tests/release tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once accepted runtime-release test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `runtime/release/` remain as a runtime handoff lane, or should all release-adjacent runtime notes live under `runtime/AI/`, `runtime/envelopes/`, and `release/`? | NEEDS VERIFICATION |
| Which release lanes are allowed to request runtime support? | NEEDS VERIFICATION |
| Which receipt family records runtime support inside a release review? | NEEDS VERIFICATION |
| Which tests prove runtime output cannot approve release, publish artifacts, correct releases, or authorize rollback? | NEEDS VERIFICATION |
| Which CI workflow, if any, validates runtime-release handoff behavior? | NEEDS VERIFICATION |
