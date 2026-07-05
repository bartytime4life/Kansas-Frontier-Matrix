# `runtime/pipelines/` — Runtime Pipeline Handoff Lane

Runtime handoff notes for pipeline-adjacent behavior. This lane may document runtime invocation boundaries, run-context handoff, finite outcomes, and receipts, but it does not own executable pipeline logic, declarative pipeline specs, lifecycle data, release decisions, or public-client authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-pipelines-readme
title: runtime/pipelines/README.md — Runtime Pipeline Handoff Lane
type: readme; directory-readme; runtime-pipeline-guardrail; handoff-index
version: v0.1
status: draft; empty-path-expanded; no-runtime-pipeline-implementation-confirmed; NEEDS VERIFICATION
owners: OWNER_TBD — Runtime steward · Pipeline steward · Policy steward · Evidence steward · Release steward · Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-05
policy_label: public; runtime; pipelines; handoff; receipts; no-release-authority
tags: [kfm, runtime, pipelines, pipeline-handoff, finite-outcomes, receipts, lifecycle]
related:
  - ../README.md
  - ../AI/README.md
  - ../model_adapters/README.md
  - ../envelopes/README.md
  - ../../pipelines/README.md
  - ../../pipeline_specs/README.md
  - ../../data/
  - ../../release/
  - ../../policy/
  - ../../contracts/
  - ../../schemas/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
notes:
  - "Expanded from an empty runtime/pipelines/README.md."
  - "Current-session search found no direct runtime/pipelines files beyond this README."
  - "runtime/ is confirmed as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release."
  - "pipelines/ is confirmed as executable pipeline logic — the HOW; pipeline_specs/ is confirmed as declarative configuration — the WHAT."
  - "This README does not prove runtime-pipeline implementation, CI wiring, pipeline execution, lifecycle transition, policy enforcement, receipt emission, release readiness, or public-client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: runtime" src="https://img.shields.io/badge/root-runtime%2F-blue">
  <img alt="Lane: pipeline handoff" src="https://img.shields.io/badge/lane-pipeline__handoff-purple">
  <img alt="Boundary: not pipeline authority" src="https://img.shields.io/badge/boundary-not__pipeline__authority-critical">
</p>

**Status:** draft / runtime-pipeline handoff guardrail
**Path:** `runtime/pipelines/`
**Current role:** README-only runtime handoff/index lane
**Truth posture:** CONFIRMED empty README path before this update; CONFIRMED no direct implementation files found in current search; CONFIRMED nearby `runtime/`, `pipelines/`, and `pipeline_specs/` boundary docs; NEEDS VERIFICATION for implementation code, tests, fixtures, receipts, CI, service configs, and release integration.

## Purpose

`runtime/pipelines/` documents runtime handoffs that are triggered by, support, or report back to governed KFM pipeline activity.

Use this lane for notes about runtime context passed into pipeline-adjacent operations, model-adapter or local-runtime calls made during review or validation support, finite runtime outcome handling, run IDs, digests, receipt pointers, envelope pointers, and runtime failure behavior visible to pipeline operators.

This path is a handoff/index lane only. It should not become pipeline execution code or pipeline configuration.

## Authority boundary

| Responsibility | Correct home | This lane's role |
|---|---|---|
| Runtime wiring and adapter handoff | `runtime/` | Documents runtime handoff posture. |
| Executable pipeline logic | `pipelines/` | Points to execution lanes; does not implement them. |
| Declarative pipeline configuration | `pipeline_specs/` | Points to configured intent; does not define specs. |
| Lifecycle records and emitted artifacts | `data/` | References outputs only by governed pointer. |
| Release decisions, rollback, correction | `release/` | Cannot approve, publish, correct, or roll back. |
| Contracts, schemas, policy | `contracts/`, `schemas/`, `policy/` | References support only. |
| Fixtures, tests, validators | `fixtures/`, `tests/`, `tools/validators/` | Requires proof before behavior is claimed. |

> [!IMPORTANT]
> A runtime-pipeline handoff is not a lifecycle transition. A successful runtime call may support a pipeline run, but it does not admit a source, validate data, approve release, publish a payload, or authorize rollback.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `runtime/pipelines/README.md` | present | Empty file expanded by this README. |
| `runtime/pipelines/*` | no files found in current search | No implementation, handoff cards, tests, fixtures, or configs confirmed under this path. |
| `runtime/README.md` | present | Runtime root for local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release. |
| `runtime/AI/README.md` | present | Governed AI runtime compatibility/index lane. |
| `runtime/model_adapters/README.md` | present | Provider-neutral model adapter lane. |
| `runtime/envelopes/README.md` | present | Finite-outcome runtime envelope helper lane. |
| `pipelines/README.md` | present | Canonical executable pipeline logic root, the HOW. |
| `pipeline_specs/README.md` | present | Canonical declarative pipeline configuration root, the WHAT. |

## Repo fit

```text
runtime/
├── README.md
├── pipelines/
│   └── README.md                     # this file; runtime handoff/index lane
├── AI/
├── model_adapters/
├── mock/
├── envelopes/
├── ollama/
├── local/
└── service_configs/

pipelines/                            # executable pipeline logic — HOW
pipeline_specs/                       # declarative configuration — WHAT
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
release/                              # release, correction, rollback authority
contracts/                            # semantic meaning
schemas/                              # machine-checkable shape
policy/                               # allow / deny / restrict / abstain posture
fixtures/                             # deterministic examples
tests/                                # executable proof of behavior
tools/validators/                     # validator implementation
```

## Runtime-pipeline responsibilities

| Responsibility | Requirement |
|---|---|
| Preserve root split | Runtime handoff notes stay here; executable pipeline logic stays in `pipelines/`; specs stay in `pipeline_specs/`. |
| Preserve lifecycle state | Do not write lifecycle records here; reference governed `data/` outputs by pointer. |
| Preserve finite outcomes | Runtime handoffs must return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` where applicable. |
| Preserve policy posture | Runtime calls must honor policy, sensitivity, rights, access, stale-state, and release checks. |
| Preserve evidence posture | Evidence support is required before answer-like output is used by a pipeline. |
| Preserve receipt posture | Link RunReceipt, AIReceipt, validation receipt, or RuntimeResponseEnvelope when behavior is claimed. |
| Preserve fail-closed behavior | Missing evidence, missing policy, missing release state, or validation failure should produce finite blockers, not silent success. |

## Allowed handoff flow

```text
pipeline spec or pipeline run context
  -> executable pipeline determines whether runtime support is needed
  -> runtime handoff checks scope, evidence, policy, release, and test posture
  -> adapter/local/mock runtime runs only if allowed
  -> finite RuntimeResponseEnvelope / DecisionEnvelope is returned
  -> receipt or run pointer is emitted/linked where applicable
  -> pipeline consumes the finite result as support, blocker, or review material
  -> release authority remains separate
```

## What belongs here

- This README.
- Runtime-pipeline handoff notes.
- Runtime support cards for pipeline-adjacent model-adapter calls.
- Notes mapping runtime outcomes to pipeline blockers or review material.
- Pointers to pipeline run IDs, pipeline specs, runtime envelopes, AIReceipt/RunReceipt records, validation receipts, fixtures, tests, and validators.
- Notes explaining how runtime behavior stays subordinate to pipeline, policy, evidence, release, correction, and rollback gates.

## What does not belong here

| Do not put this in `runtime/pipelines/` | Correct home |
|---|---|
| Executable pipeline runners, transforms, receipt emitters, blocker builders | `pipelines/` |
| Declarative pipeline specs, schedules, scopes, release-readiness config | `pipeline_specs/` |
| Lifecycle data, emitted artifacts, receipts, proofs, catalogs, published payloads | accepted `data/` lifecycle/proof/receipt/catalog roots |
| Release manifests, promotion decisions, correction notices, rollback records | `release/` |
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
find runtime/pipelines -maxdepth 4 -type f | sort
find runtime pipelines pipeline_specs -maxdepth 5 -type f 2>/dev/null | sort
find data release policy contracts schemas fixtures tests tools/validators -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/runtime tests/pipelines tests/pipeline_specs tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once accepted runtime-pipeline test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `runtime/pipelines/` remain as a runtime handoff lane, or should all runtime-pipeline notes live directly under `runtime/AI/`, `runtime/model_adapters/`, and `pipelines/`? | NEEDS VERIFICATION |
| Which pipeline lanes are allowed to call runtime adapters or local model runtimes? | NEEDS VERIFICATION |
| Which receipt family records runtime support inside a pipeline run? | NEEDS VERIFICATION |
| Which tests prove runtime output cannot promote lifecycle state or approve release? | NEEDS VERIFICATION |
| Which CI workflow, if any, validates runtime-pipeline handoff behavior? | NEEDS VERIFICATION |
