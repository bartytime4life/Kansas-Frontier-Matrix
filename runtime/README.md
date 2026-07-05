# `runtime/` — Runtime Wiring Root

Local runtime wiring, model adapters, service harnesses, finite-outcome envelopes, and runtime handoff notes for KFM. This root is subordinate to evidence, policy, validation, release, correction, rollback, and public-client governance.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-readme
title: runtime/README.md — Runtime Wiring Root
type: root-readme; runtime-root; governance-index; trust-boundary-guardrail
version: v0.2
status: draft; canonical-runtime-root; mixed-maturity-sublanes; NEEDS VERIFICATION
owners: OWNER_TBD — Runtime steward · Governed-AI steward · Policy steward · Evidence steward · Security steward · Release steward · Docs steward
created: NEEDS VERIFICATION — compact root stub existed before v0.2 expansion
updated: 2026-07-05
policy_label: public; runtime; governed-ai; model-adapters; finite-outcomes; no-public-authority
tags: [kfm, runtime, local-runtime, model-adapters, mock, ollama, envelopes, service-configs, people, pipelines, release, finite-outcomes]
related:
  - ./AI/README.md
  - ./local/README.md
  - ./model_adapters/README.md
  - ./model_adapters/AdapterContract.md
  - ./model_adapters/mock/README.md
  - ./mock/README.md
  - ./ollama/README.md
  - ./envelopes/README.md
  - ./service_configs/README.md
  - ./people/README.md
  - ./pipelines/README.md
  - ./release/README.md
  - ../contracts/
  - ../schemas/
  - ../policy/
  - ../fixtures/
  - ../tests/
  - ../tools/validators/
  - ../data/
  - ../release/
notes:
  - "Expanded from the prior compact runtime root stub."
  - "The prior root purpose stated: local runtime wiring, model adapters, service harnesses, subordinate to evidence/policy/release."
  - "Direct fetches confirm runtime sublane READMEs for AI, local, model_adapters, mock, ollama, envelopes, service_configs, people, pipelines, and release."
  - "This README does not prove runtime implementation, adapter implementation, service deployment, model availability, CI wiring, policy enforcement, receipt emission, release readiness, or public-client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: runtime" src="https://img.shields.io/badge/root-runtime%2F-blue">
  <img alt="Authority: runtime wiring" src="https://img.shields.io/badge/authority-runtime__wiring-purple">
  <img alt="Maturity: mixed" src="https://img.shields.io/badge/maturity-mixed-orange">
  <img alt="Boundary: evidence policy release subordinate" src="https://img.shields.io/badge/boundary-evidence__policy__release-critical">
</p>

**Status:** draft / canonical runtime root / mixed maturity
**Path:** `runtime/`
**Root purpose:** local runtime wiring, model adapters, service harnesses, finite-outcome envelopes, and runtime handoff notes.
**Truth posture:** CONFIRMED prior compact root stub; CONFIRMED several child README boundaries by direct fetch; NEEDS VERIFICATION for full tree inventory, implementation files, route behavior, service configs, tests, fixtures, validators, CI, receipts, and deployment state.

## Purpose

`runtime/` is the KFM root for local runtime wiring, model-adapter handoffs, deterministic mocks, local model runtime notes, finite-outcome envelopes, non-secret service configuration templates, and sensitive/runtime-adjacent handoff notes.

Runtime is an execution-support layer. It is not root truth, not source authority, not lifecycle storage, not policy authority, not release authority, and not a normal public-client data path.

Runtime work must preserve this default flow:

```text
scope request
  -> governed evidence support
  -> policy / rights / sensitivity check
  -> allowed runtime adapter or service
  -> citation/support validation when answer-like output is produced
  -> finite outcome: ANSWER / ABSTAIN / DENY / ERROR
  -> receipt or envelope pointer where applicable
  -> governed caller decides next action
```

## Authority boundary

| Responsibility | Correct home | Runtime role |
|---|---|---|
| Local runtime wiring and service-harness notes | `runtime/` | Owns runtime handoff documentation and local wiring notes. |
| Provider-neutral adapter notes | `runtime/model_adapters/` | Documents adapter cards, port notes, and adapter handoff posture. |
| Deterministic mock runtime notes | `runtime/mock/` and `runtime/model_adapters/mock/` | Supports fixture-backed tests; never released truth. |
| Local model runtime notes | `runtime/ollama/` and accepted local lanes | Local/development runtime only unless separately reviewed. |
| Non-secret runtime service configuration templates | `runtime/service_configs/` | Documents safe templates and handoff notes only. |
| Semantic meaning | `contracts/` | Runtime references contracts; it does not define them. |
| Machine-checkable shape | `schemas/` | Runtime references schemas; it does not define them. |
| Policy decisions and access rules | `policy/` | Runtime obeys policy; it does not decide policy. |
| Fixtures, tests, validators | `fixtures/`, `tests/`, `tools/validators/` | Runtime behavior claims require proof. |
| Lifecycle data, receipts, proofs, catalogs, published artifacts | `data/` and accepted trust-object roots | Runtime references governed objects by pointer only. |
| Release, correction, rollback, notices, changelog | `release/` | Runtime may support review, but cannot approve release or rollback. |
| Public API/UI behavior | accepted app, API, UI, web, or public-client roots | Public clients must not read runtime internals directly. |

> [!IMPORTANT]
> Runtime can help answer, abstain, deny, or fail safely. It cannot turn generated text, model output, service config, adapter output, or local runtime behavior into evidence, policy, review, release, correction, rollback, or public truth.

## Current lane index

| Lane | Role | Current posture |
|---|---|---|
| `AI/` | Governed AI runtime notes and compatibility/index lane. | Draft; path posture needs maintainer confirmation because canonical sublanes are lower-level runtime lanes. |
| `local/` | Local runtime wiring, service-harness notes, adapter handoff, receipt handoff, and local test notes. | Draft; runtime-lane guidance. |
| `model_adapters/` | Provider-neutral model adapter notes and adapter handoff documentation. | Draft; canonical provider-neutral adapter lane. |
| `model_adapters/AdapterContract.md` | Runtime adapter contract note: `FocusRequest` in, `DecisionEnvelope` out, cite-or-abstain. | Draft; descriptive note, not canonical contract authority. |
| `model_adapters/mock/` | Mock-only model adapter lane for deterministic adapter behavior. | Draft; README-only in current pass. |
| `mock/` | Deterministic mock runtime notes and mock adapter handoff documentation. | Draft; mock-only/test material. |
| `ollama/` | Local Ollama runtime notes and local model adapter handoff. | Draft; local/development only, implementation not confirmed. |
| `envelopes/` | Runtime envelope helper notes and finite-outcome handoff documentation. | Draft; helper/index lane. |
| `service_configs/` | Non-secret runtime service configuration templates and handoff notes. | Draft; no direct config files confirmed in current pass. |
| `people/` | Sensitive People / Genealogy / DNA / Land runtime guardrail lane. | Draft; deny-by-default / restricted-review posture. |
| `pipelines/` | Runtime-pipeline handoff notes. | Draft; README-only handoff lane, not pipeline authority. |
| `release/` | Runtime-release handoff notes. | Draft; README-only handoff lane, not release authority. |

## Repo fit

```text
runtime/
├── README.md                         # this file; runtime root index
├── AI/                               # governed AI compatibility/index lane
├── local/                            # local runtime wiring lane
├── model_adapters/                   # provider-neutral adapter lane
│   ├── README.md
│   ├── AdapterContract.md
│   └── mock/
├── mock/                             # deterministic mock runtime lane
├── ollama/                           # local Ollama runtime lane
├── envelopes/                        # finite-outcome envelope helper lane
├── service_configs/                  # non-secret service config templates
├── people/                           # sensitive people-runtime guardrail lane
├── pipelines/                        # runtime-pipeline handoff lane
└── release/                          # runtime-release handoff lane

contracts/                            # semantic meaning
schemas/                              # machine-checkable shape
policy/                               # allow / deny / restrict / abstain posture
fixtures/                             # deterministic examples
tests/                                # executable proof of behavior
tools/validators/                     # validator implementation
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
release/                              # release, correction, rollback authority
apps/                                 # deployable/public API and UI boundaries
```

## Runtime responsibilities

| Responsibility | Requirement |
|---|---|
| Preserve evidence hierarchy | EvidenceBundle and source records outrank runtime output and generated text. |
| Preserve policy hierarchy | Runtime behavior must honor policy, rights, sensitivity, access, release, stale-state, and correction posture. |
| Preserve finite outcomes | Runtime results should resolve to `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` where applicable. |
| Preserve citation posture | Answer-like runtime output that depends on evidence must cite support or abstain. |
| Preserve adapter boundaries | Mock, local, Ollama, and provider-backed behavior should route through documented adapter boundaries. |
| Preserve envelope posture | Runtime responses should use or link finite runtime envelopes when behavior is claimed. |
| Preserve receipt posture | Link AIReceipt, RunReceipt, validation receipt, or runtime envelope records when applicable. |
| Preserve private material boundary | Keep credentials, provider keys, private config, private URLs, model internals, private chain-of-thought, and local secrets out of repo. |
| Preserve release boundary | Runtime output cannot publish, correct, withdraw, approve release, or authorize rollback. |
| Preserve public-client boundary | Public clients use governed APIs and released artifacts, not runtime internals. |

## Runtime outcomes

| Outcome | Meaning |
|---|---|
| `ANSWER` | Runtime produced an answer supported by governed evidence, policy, citation validation, and finite-envelope posture. |
| `ABSTAIN` | Runtime did not answer because support, source authority, freshness, citation, scope, or confidence was insufficient. |
| `DENY` | Runtime denied because policy, rights, sensitivity, access, release, or governance state forbids response. |
| `ERROR` | Runtime could not complete due to adapter, configuration, validation, dependency, envelope, or service failure. |

## What belongs here

- Runtime root README and child-lane indexes.
- Local runtime wiring notes.
- Model adapter notes and adapter handoff documentation.
- Deterministic mock runtime notes and mock adapter notes.
- Local model runtime notes.
- Runtime envelope helper notes.
- Non-secret runtime service configuration templates.
- Runtime handoff notes for people-sensitive, pipeline-adjacent, and release-adjacent behavior.
- Pointers to contracts, schemas, policy, fixtures, tests, validators, receipts, data records, and release records.
- Review notes that keep runtime downstream of evidence, policy, validation, review, release, correction, and rollback state.

## What does not belong here

| Do not put this in `runtime/` | Correct home |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data payloads | `data/` lifecycle roots |
| EvidenceBundle contents, SourceDescriptors, source registries, proofs, receipts, catalogs, or published artifacts | accepted `data/`, registry, proof, receipt, catalog, or published roots |
| Canonical semantic contracts | `contracts/` |
| JSON Schema definitions | `schemas/` |
| Policy rules or policy decisions | `policy/` and governed review/release roots |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` |
| Validator source code | `tools/validators/` |
| Release manifests, promotion decisions, correction notices, rollback records, changelog entries, publication approvals | `release/` |
| Public API routes or UI components | accepted app, API, UI, web, or package roots |
| Private credentials, local configuration values, model files, or signing material | never in repo |
| Generated text treated as evidence, policy, review, release, correction, rollback, legal/title conclusion, or publication authority | nowhere |

## Validation

```bash
find runtime -maxdepth 4 -type f | sort
find contracts schemas policy fixtures tests tools/validators data release apps -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/runtime tests/api tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once accepted runtime validation commands are confirmed.

## Review burden

Maintainer review is required for ordinary runtime documentation changes.

Steward review is required when runtime work touches evidence, policy, release, correction, rollback, sensitive domains, public exposure, model adapters, service configs, receipts, runtime envelopes, or generated text that may be mistaken for governed truth.

## Open questions

| Question | Status |
|---|---|
| Which runtime sublanes are canonical and which are compatibility/index lanes pending migration? | NEEDS VERIFICATION |
| Which runtime DTOs and envelopes have accepted semantic contracts and schemas? | NEEDS VERIFICATION |
| Which tests and CI workflows validate runtime outcomes, adapter boundaries, policy denial, and receipt emission? | NEEDS VERIFICATION |
| Which runtime services, if any, are safe for public-callable paths? | NEEDS VERIFICATION / default deny until reviewed |
| Which owner signs off on runtime-to-release, runtime-to-pipeline, and runtime-to-public API handoffs? | NEEDS VERIFICATION |
