# `runtime/ollama/` — Ollama Local Model Runtime Lane

Local Ollama runtime wiring and handoff notes for KFM governed-AI experiments. This lane is for local model runtime integration only; it is not evidence authority, policy authority, provider authority, publication authority, or a public runtime path.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-ollama-readme
title: runtime/ollama/README.md — Ollama Local Model Runtime Lane
type: readme; directory-readme; local-model-runtime-guardrail; governed-ai-runtime-index
version: v0.1
status: draft; greenfield-stub-expanded; local-only; implementation-not-confirmed; NEEDS VERIFICATION
owners: OWNER_TBD — Runtime steward · Governed-AI steward · Security steward · Policy steward · Evidence steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-05
policy_label: public; runtime; ollama; local-model; governed-ai; no-public-provider-authority
tags: [kfm, runtime, ollama, local-model, model-adapters, governed-ai, finite-outcomes, ai-receipt, runtime-envelope]
related:
  - ../README.md
  - ../model_adapters/README.md
  - ../model_adapters/AdapterContract.md
  - ../mock/README.md
  - ../AI/README.md
  - ../envelopes/README.md
  - ../local/
  - ../service_configs/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../data/
  - ../../release/
notes:
  - "Expanded from a greenfield stub containing only '# runtime/ollama' and 'Greenfield stub.'."
  - "Current-session evidence confirms runtime/ is for local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release."
  - "Adjacent runtime docs treat model adapters as provider-neutral, AI as interpretive only, and envelopes as finite-outcome carriers."
  - "This README does not prove Ollama installation, model availability, adapter implementation, service configuration, test coverage, policy enforcement, citation validation, AIReceipt emission, RuntimeResponseEnvelope behavior, CI wiring, or release readiness."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: runtime" src="https://img.shields.io/badge/root-runtime%2F-blue">
  <img alt="Lane: ollama" src="https://img.shields.io/badge/lane-ollama__local-purple">
  <img alt="Maturity: implementation not confirmed" src="https://img.shields.io/badge/maturity-implementation__not__confirmed-orange">
  <img alt="Boundary: not public runtime" src="https://img.shields.io/badge/boundary-not__public__runtime-critical">
</p>

**Status:** draft / local-model runtime guardrail
**Path:** `runtime/ollama/`
**Current role:** local Ollama runtime notes and adapter handoff documentation
**Truth posture:** CONFIRMED stub existed before this update; CONFIRMED adjacent runtime, model-adapter, AI, and envelope README boundaries; NEEDS VERIFICATION for real Ollama config, installed models, adapter code, tests, fixtures, service config, receipts, and CI integration.

## Quick jumps

[Purpose](#purpose) · [Boundary](#boundary) · [Current inventory](#current-inventory) · [Repo fit](#repo-fit) · [Ollama runtime responsibilities](#ollama-runtime-responsibilities) · [Allowed flow](#allowed-flow) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Runtime notes](#runtime-notes) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

`runtime/ollama/` is the KFM local model runtime lane for Ollama-related notes, local adapter handoff records, and development-only configuration guidance.

Use this lane to document how a local Ollama runtime may be wired behind KFM governed model-adapter boundaries. It should help developers test local model behavior without weakening evidence, policy, citation, finite-outcome, receipt, and release controls.

This lane should work with, not replace:

- `runtime/model_adapters/` for provider-neutral adapter boundaries;
- `runtime/model_adapters/AdapterContract.md` for the runtime adapter contract note;
- `runtime/mock/` and `runtime/model_adapters/mock/` for deterministic mock-first behavior;
- `runtime/envelopes/` for finite-outcome runtime envelope handoff;
- `policy/`, `contracts/`, `schemas/`, `fixtures/`, `tests/`, and `tools/validators/` for governed support.

## Boundary

This path is not a public model endpoint, not a live provider authority, not a model registry, not an evidence store, not a source registry, not a lifecycle data root, not a policy engine, not a contract/schema home, not validator implementation, not a receipt/proof root, and not release authority.

Ollama output is model output. It is interpretive and downstream. It must not be treated as evidence, citation support, policy approval, steward review, release decision, public truth, or implementation proof unless accepted evidence, policy, citation validation, runtime envelope, receipt, tests, and review records say so.

> [!IMPORTANT]
> Local does not mean safe by default. Local model execution still needs scope control, evidence control, policy control, citation validation when answering, finite outcomes, receipts where applicable, and deny-by-default handling for sensitive or unsupported requests.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `runtime/ollama/README.md` | present | Greenfield stub expanded by this README. |
| `runtime/ollama/*` | not confirmed by current search | No Ollama model cards, configs, adapter cards, test fixtures, or implementation files confirmed under this path in this pass. |
| `runtime/model_adapters/README.md` | present | Provider-neutral adapter lane. |
| `runtime/model_adapters/AdapterContract.md` | present | Runtime adapter boundary note: `FocusRequest` in, `DecisionEnvelope` out, cite-or-abstain. |
| `runtime/mock/README.md` | present | Broader deterministic mock runtime lane. |
| `runtime/AI/README.md` | present | Governed AI compatibility/index lane. |
| `runtime/envelopes/README.md` | present | Runtime envelope helper lane. |

## Repo fit

```text
runtime/
├── README.md
├── ollama/
│   └── README.md                     # this file; local Ollama guardrail
├── model_adapters/                   # provider-neutral adapter lane
│   ├── README.md
│   ├── AdapterContract.md
│   └── mock/
├── mock/                             # deterministic mock runtime lane
├── AI/                               # governed AI compatibility/index lane
├── envelopes/                        # finite-outcome envelope helper lane
├── local/                            # local runtime wiring
└── service_configs/                  # service configuration templates

contracts/                            # semantic meaning
schemas/                              # machine-checkable shape
policy/                               # policy and access posture
fixtures/                             # deterministic examples and expected cases
tests/                                # executable proof of behavior
tools/validators/                     # validator implementation
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
release/                              # release, correction, rollback authority
```

## Ollama runtime responsibilities

| Responsibility | Requirement |
|---|---|
| Local-only posture | Make clear that Ollama notes are for local/development runtime unless separately reviewed. |
| Adapter boundary | Route behavior through `runtime/model_adapters/` and the adapter contract note. |
| Evidence posture | Use governed evidence pointers or approved test fixtures; do not pass raw stores into normal runtime. |
| Policy posture | Respect policy, rights, sensitivity, release, stale-state, and access checks before answering. |
| Citation posture | Cite-or-abstain for answer-like output that depends on evidence. |
| Finite outcome posture | Return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`, not unbounded free text alone. |
| Receipt posture | Emit or link AIReceipt, RunReceipt, validation receipt, or RuntimeResponseEnvelope when applicable. |
| Security posture | Keep model files, credentials, tokens, private config, and local secrets out of the repo. |
| Test posture | Claim behavior only when supported by fixtures, tests, validators, runtime logs, or review records. |

## Allowed flow

```text
FocusRequest or governed runtime request
  -> scope and access check
  -> evidence/support resolution
  -> policy and sensitivity check
  -> adapter selects local Ollama runtime only if allowed
  -> local model produces bounded candidate text
  -> citation/support validation where required
  -> finite RuntimeResponseEnvelope / DecisionEnvelope
  -> AIReceipt or run receipt pointer where applicable
  -> governed caller decides next action
```

The local model never decides truth, release, policy, rights, sensitivity, correction, rollback, or publication state.

## What belongs here

- This README.
- Local Ollama runtime notes.
- Ollama adapter handoff notes that point back to `runtime/model_adapters/`.
- Local model card notes that record model name, digest/checksum if available, local-only status, use case, and review status.
- Local service configuration notes that point to `runtime/service_configs/` when templates are needed.
- Test-only or development-only setup notes that avoid secrets and private config.
- Migration notes from mock adapter behavior to local Ollama runtime behavior.
- Pointers to fixtures, tests, validators, policy, contracts, schemas, runtime envelopes, and receipts.

## What does not belong here

| Do not put this in `runtime/ollama/` | Correct home |
|---|---|
| Provider credentials, API keys, tokens, local `.env`, private config, or secrets | never in repo |
| Model weights or large downloaded model files | local machine or approved artifact storage outside repo |
| Canonical semantic contracts | `contracts/` |
| JSON Schema definitions | `schemas/` |
| Policy rules or policy decisions | `policy/` and governed review/release roots |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` |
| Validator source code | `tools/validators/` |
| Generic provider-neutral adapter cards | `runtime/model_adapters/` |
| Deterministic mock-only notes | `runtime/mock/` or `runtime/model_adapters/mock/` |
| Service config templates | `runtime/service_configs/` unless this lane only points to them |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, SourceDescriptors, receipts, proofs, catalogs, or release manifests | accepted `data/`, source-registry, proof, receipt, catalog, or release roots |
| Release decisions, correction notices, rollback records, or publication approvals | `release/` |
| Generated text treated as truth, evidence, policy, review, release, correction, rollback, or publication authority | nowhere |

## Runtime notes

A local Ollama runtime note should include:

```markdown
# <ollama-runtime-note-id>

## Status
DRAFT / READY_FOR_REVIEW / LOCAL_ONLY / VALIDATION_REQUIRED / HELD / MIGRATE / SUPERSEDED / RETIRED

## Runtime mode
local-ollama

## Model reference
<local model name, digest/checksum if available, or NEEDS VERIFICATION>

## Adapter boundary
<runtime/model_adapters card or AdapterContract.md pointer>

## Allowed use
<development-only test, fixture replay, local Focus Mode experiment, or N/A>

## Expected finite outcomes
ANSWER / ABSTAIN / DENY / ERROR / N/A

## Governed support pointers
- Contract: <path or N/A>
- Schema: <path or N/A>
- Policy: <path or N/A>
- Evidence fixture: <path or N/A>
- Citation validation: <path or N/A>
- RuntimeResponseEnvelope: <path or N/A>
- AIReceipt: <path or N/A>
- Test: <path or N/A>
- Validator: <path or N/A>

## Security notes
<no secrets, no model weights in repo, local-only exposure, network posture, or NEEDS VERIFICATION>

## Boundary notes
<what this local runtime may support and what it must not become>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Validation

```bash
find runtime/ollama -maxdepth 4 -type f | sort
find runtime/model_adapters runtime/mock runtime/envelopes runtime/service_configs -maxdepth 4 -type f 2>/dev/null | sort
find contracts schemas policy fixtures tests tools/validators -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/runtime tests/api tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once the accepted local runtime test commands are confirmed.

## Review checklist

- [ ] Ollama use is marked local-only or otherwise explicitly reviewed.
- [ ] Adapter boundary is linked to `runtime/model_adapters/` or the adapter contract note.
- [ ] Runtime output uses finite outcomes.
- [ ] Evidence and policy posture are explicit before answer-like output is allowed.
- [ ] Citation validation is linked when generated text cites evidence.
- [ ] RuntimeResponseEnvelope or DecisionEnvelope handoff is linked when applicable.
- [ ] AIReceipt or run receipt posture is linked when applicable.
- [ ] No model weights, credentials, tokens, local `.env`, private config, private model internals, or private chain-of-thought are stored here.
- [ ] No generated text is treated as evidence, policy, review, release, correction, rollback, or publication authority.
- [ ] Behavior claims are supported by fixtures, tests, validators, runtime logs, or review records.

## Open questions

| Question | Status |
|---|---|
| Which Ollama models, if any, are approved for local KFM development use? | NEEDS VERIFICATION |
| Should local Ollama model cards live here, under `runtime/model_adapters/`, or under a separate model registry lane? | NEEDS VERIFICATION |
| Which service configuration templates belong in `runtime/service_configs/` for Ollama? | NEEDS VERIFICATION |
| Which fixtures and tests prove local Ollama `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior? | NEEDS VERIFICATION |
| Should local Ollama runtime ever be callable from public UI/API paths, or remain developer-only? | NEEDS VERIFICATION / default DENY until reviewed |
| Which CI workflow, if any, can safely test local Ollama behavior without relying on a developer machine? | NEEDS VERIFICATION |
