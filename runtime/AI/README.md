# `runtime/AI/` — Governed AI Runtime Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-ai-readme
title: runtime/AI/ — Governed AI Runtime Lane
version: v1
status: draft
policy_label: public
owners:
  - <runtime-steward>
  - <governed-ai-steward>
  - <policy-steward>
  - <evidence-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, runtime, ai, governed-ai, ai-receipt, model-adapters, cite-or-abstain]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-runtime%2F-blue)
![lane](https://img.shields.io/badge/lane-governed--AI-blueviolet)
![posture](https://img.shields.io/badge/posture-cite--or--abstain-green)
![audit](https://img.shields.io/badge/audit-receipted-green)

## Purpose

`runtime/AI/` is a runtime documentation lane for governed AI wiring.

It may hold notes for model adapters, mock runtimes, receipt routing, runtime envelopes, and local test harnesses.

AI in KFM is interpretive. It is not root truth, not evidence, not a release decision, and not a substitute for policy, validation, citation, or steward review.

## Status & authority

| Field | Value |
|---|---|
| Document type | Runtime AI README |
| Owning root | `runtime/` |
| Requested path | `runtime/AI/` |
| Status | Draft |
| Authority level | Runtime guidance and index. Contracts, schemas, policy, evidence records, validation receipts, release records, and steward decisions outrank this README. |
| Path posture | Existing path confirmed in this session. Directory Rules list canonical runtime sublanes such as `model_adapters/`, `ollama/`, `mock/`, `service_configs/`, and `envelopes/`; the capitalized `AI/` lane needs maintainer confirmation. |
| Default posture | Require governed evidence, policy decision, citation validation, finite runtime outcome, and AIReceipt where applicable. |
| Required reviewers | Runtime steward, governed-AI steward, policy steward, evidence steward, and docs steward. |

## Placement basis

Current-session evidence confirms `runtime/README.md` describes `runtime/` as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release.

Directory Rules describe `runtime/` as a local-adapter root with sublanes for local wiring, provider-neutral model adapters, local model runtime, deterministic mock adapters, service configuration, and finite-outcome envelope helpers.

`runtime/AI/` should remain a draft compatibility or index lane until maintainers confirm whether it is canonical or should be migrated into those sublanes.

## Repo fit

```text
runtime/
├── README.md
├── AI/                   # you are here; draft compatibility/index lane
├── local/
├── model_adapters/
├── ollama/
├── mock/
├── service_configs/
└── envelopes/
```

## Governed AI runtime flow

```text
scope request
  -> retrieve governed evidence
  -> evaluate policy
  -> run allowed adapter/model
  -> validate citations
  -> return finite outcome
  -> emit AIReceipt
  -> emit RuntimeResponseEnvelope
```

The runtime lane may document adapter and receipt wiring. It must not decide truth or release state.

## Runtime responsibilities

| Responsibility | Expectation |
|---|---|
| Adapter boundary | Document adapter names, modes, and expected inputs/outputs. |
| Evidence boundary | Use evidence pointers and avoid treating generated text as evidence. |
| Policy boundary | Link policy decisions when runtime behavior depends on policy. |
| Citation boundary | Link citation validation when generated text cites evidence. |
| Receipt boundary | Emit or link `AIReceipt` for AI-mediated runtime events. |
| Envelope boundary | Return finite runtime outcomes through governed response envelopes. |
| Audit boundary | Preserve run IDs, adapter/model refs, digests, outcomes, and support pointers. |

## What belongs here

- Runtime AI README and sublane indexes.
- Adapter wiring notes and adapter inventories.
- Mock-runtime notes for deterministic tests.
- Receipt-routing notes for `AIReceipt` and runtime envelopes.
- Runtime handoff notes to `contracts/runtime/`, `schemas/contracts/v1/runtime/`, `policy/ai/`, `policy/runtime/`, fixtures, and validators.
- Review notes that keep AI downstream of evidence, policy, validation, and release state.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- EvidenceBundle contents or source records.
- Release manifests, release decisions, correction records, signatures, or notices.
- Canonical contracts, schemas, policy files, or validator source code.
- Credentials or provider keys.
- Private chain-of-thought or model internals.
- Generated text treated as evidence, policy, review, or publication authority.

## Runtime outcomes

| Outcome | Meaning |
|---|---|
| `ANSWER` | Runtime produced an answer supported by governed evidence, policy, and citation validation. |
| `ABSTAIN` | Runtime did not answer because support was insufficient. |
| `DENY` | Runtime denied the request because policy or governance state forbids response. |
| `ERROR` | Runtime could not complete due to validation, adapter, configuration, or envelope failure. |

## Required AI runtime fields

Runtime notes, adapter cards, or run-index records should capture:

- Runtime record ID
- Runtime lane or adapter name
- Adapter type
- Model reference or mock reference
- Runtime mode
- Allowed use case
- Evidence posture
- Policy decision pointer, when applicable
- Citation validation pointer, when applicable
- AIReceipt pointer, when applicable
- RuntimeResponseEnvelope pointer, when applicable
- Input digest, when applicable
- Output digest, when applicable
- Outcome
- Reviewer
- Review date
- Open blockers
- Follow-up items

## Minimal runtime note

```markdown
# <runtime-ai-note-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE / HELD / SUPERSEDED / RETIRED

## Runtime scope
<adapter, mock runtime, local runtime, envelope helper, receipt route, or N/A>

## Governed support pointers
- Contract: <path or N/A>
- Schema: <path or N/A>
- Policy: <path or N/A>
- Evidence: <path or N/A>
- Citation validation: <path or N/A>
- AIReceipt: <path or N/A>
- RuntimeResponseEnvelope: <path or N/A>
- Validator or fixture: <path or N/A>

## Runtime outcome posture
ANSWER / ABSTAIN / DENY / ERROR / N/A

## Boundary notes
<what this runtime path may do and must not do>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Runtime note names its scope.
- [ ] Adapter or runtime mode is clear.
- [ ] Evidence posture is explicit.
- [ ] Policy decision pointer is linked when needed.
- [ ] Citation validation pointer is linked when needed.
- [ ] AIReceipt pointer is linked when AI-mediated runtime behavior is involved.
- [ ] RuntimeResponseEnvelope pointer is linked when output reaches governed clients.
- [ ] Outcome is one of the finite runtime outcomes when applicable.
- [ ] No data payloads, credentials, provider keys, or private model internals are stored here.
- [ ] The note does not claim implementation maturity without tests, fixtures, runtime evidence, or code references.

## Naming guidance

Recommended runtime-note pattern:

```text
<YYYY-MM-DD>_<runtime-scope>_runtime-note.md
```

Examples:

```text
2026-07-03_mock-adapter_runtime-note.md
2026-07-03_ai-receipt-route_runtime-note.md
2026-07-03_runtime-envelope-helper_runtime-note.md
```

Use lowercase filenames for records even if this compatibility lane remains capitalized as `AI/`.

## Open verification

- [ ] Confirm whether `runtime/AI/` remains an accepted compatibility/index lane or should be migrated to canonical runtime sublanes.
- [ ] Confirm CODEOWNERS for `runtime/AI/`.
- [ ] Confirm adapter inventory paths.
- [ ] Confirm AIReceipt persistence path.
- [ ] Confirm RuntimeResponseEnvelope implementation path.
- [ ] Confirm policy package paths for AI/runtime decisions.
- [ ] Confirm citation-validation implementation path.
- [ ] Confirm fixture and validator paths for AIReceipt and runtime envelopes.
- [ ] Confirm whether runtime notes require schema validation.
- [ ] Confirm whether `runtime/README.md` should index `AI/` directly.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Runtime lane migration, adapter inventory update, AIReceipt schema update, policy update, citation validator update, envelope update, first runtime note, or public-surface integration review |
