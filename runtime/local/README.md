# `runtime/local/` — Local Runtime Wiring Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-local-readme
title: runtime/local/ — Local Runtime Wiring Lane
version: v1
status: draft
policy_label: public
owners:
  - <runtime-steward>
  - <ops-steward>
  - <policy-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, runtime, local, service-harnesses, adapters, receipts, validation]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-runtime%2F-blue)
![lane](https://img.shields.io/badge/lane-local-blueviolet)
![posture](https://img.shields.io/badge/posture-local--wiring-orange)

## Purpose

`runtime/local/` is the local runtime wiring lane for KFM.

It may hold local runtime notes, harness notes, adapter handoff notes, local test notes, and review records that explain how local runtime behavior stays downstream of evidence, policy, validation, review, and release state.

This lane is not a lifecycle data home, contract home, schema home, policy home, validator home, release home, or source-record home.

## Status & authority

| Field | Value |
|---|---|
| Document type | Local runtime README |
| Owning root | `runtime/` |
| Lane | `runtime/local/` |
| Status | Draft |
| Authority level | Runtime-lane guidance and index. Runtime contracts, schemas, policy, evidence records, validation receipts, release records, tests, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was a greenfield stub before this update. Directory Rules name `runtime/local/` as the local runtime wiring lane. |
| Default posture | Local runtime notes remain subordinate to evidence, policy, validation, review, and release state. |
| Required reviewers | Runtime steward, ops steward, policy steward when runtime behavior is gated, and docs steward. |

## Placement basis

Current-session evidence confirms `runtime/README.md` describes `runtime/` as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release.

Directory Rules list `runtime/local/` under `runtime/` as the lane for local runtime wiring.

## Repo fit

```text
runtime/
├── README.md
├── local/                # you are here
├── model_adapters/
├── ollama/
├── mock/
├── service_configs/
└── envelopes/
```

## Local-runtime responsibilities

| Responsibility | Expectation |
|---|---|
| Runtime identity | Name the local runtime note, harness, or local wiring target. |
| Scope | State whether the note covers local harness wiring, adapter handoff, envelope handoff, receipt handoff, service config, or test support. |
| Evidence posture | Link evidence pointers when local behavior depends on evidence. |
| Policy posture | Link policy decisions or policy notes when local behavior is gated. |
| Receipt posture | Link run receipts, validation receipts, AIReceipt, or envelope records when applicable. |
| Validation posture | Link fixtures, tests, or validators when behavior is claimed. |
| Config posture | Point to safe templates or examples only. |
| Migration posture | Record whether local wiring should move to `runtime/service_configs/`, `runtime/model_adapters/`, `runtime/mock/`, or another functional lane. |

## What belongs here

- Local runtime README and index notes.
- Local runtime wiring notes.
- Service-harness notes that are safe for repository documentation.
- Adapter-handoff and envelope-handoff notes.
- Receipt-routing notes for local runs.
- Local validation and fixture notes.
- Pointers to `runtime/model_adapters/`, `runtime/mock/`, `runtime/service_configs/`, `runtime/envelopes/`, `contracts/runtime/`, `schemas/contracts/v1/runtime/`, `policy/runtime/`, fixtures, tests, and validators.

## What does not belong here

- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Canonical contracts, schemas, policy files, or validator source code.
- Private configuration values.
- Private model internals.
- Generated text treated as evidence, policy, review, or publication authority.

## Local runtime status values

Use finite local-runtime status values where possible:

| Status | Meaning |
|---|---|
| `DRAFT` | Local runtime note exists but is not ready for review. |
| `READY_FOR_REVIEW` | Local runtime note is ready for maintainer or steward review. |
| `ACTIVE_LOCAL` | Local runtime note is accepted for local use. |
| `MOCK_ONLY` | Local runtime note is only for deterministic mock or test usage. |
| `HELD` | Local runtime note is blocked pending evidence, policy, validation, or placement review. |
| `MIGRATE` | Local runtime note should move to a more specific runtime lane. |
| `SUPERSEDED` | A newer local runtime note replaces this one. |
| `RETIRED` | Local runtime note is no longer active. |

## Required local-runtime fields

Every local runtime note should capture:

- Local runtime note ID
- Local runtime status
- Runtime scope
- Runtime mode
- Canonical home
- Allowed local use case
- Evidence posture
- Policy posture
- Receipt posture
- Validation posture
- Config posture
- Runtime outcome posture, when applicable
- Contract pointer, when applicable
- Schema pointer, when applicable
- Policy pointer, when applicable
- Receipt pointer, when applicable
- Fixture or validator pointer, when applicable
- Reviewer
- Review date
- Open blockers
- Follow-up items

## Minimal local runtime note

```markdown
# <local-runtime-note-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE_LOCAL / MOCK_ONLY / HELD / MIGRATE / SUPERSEDED / RETIRED

## Runtime scope
<local harness, adapter handoff, envelope handoff, receipt route, service config, test support, or N/A>

## Runtime mode
<local / mock / test / other / N/A>

## Canonical home
<runtime/local/ / runtime/service_configs/ / runtime/model_adapters/ / runtime/mock/ / runtime/envelopes/ / other / N/A>

## Allowed local use
<short governed local use case or N/A>

## Governed support pointers
- Contract: <path or N/A>
- Schema: <path or N/A>
- Policy: <path or N/A>
- Receipt: <path or N/A>
- Envelope: <path or N/A>
- Fixture or validator: <path or N/A>
- Config template: <path or N/A>

## Boundary notes
<what this local runtime note may support and what it must not become>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Runtime scope is clear.
- [ ] Runtime mode is clear.
- [ ] Canonical home is explicit.
- [ ] Evidence posture is linked or marked N/A.
- [ ] Policy posture is linked or marked N/A.
- [ ] Receipt and envelope pointers are linked when applicable.
- [ ] Fixture, test, or validator support is linked when behavior is claimed.
- [ ] Config pointers reference templates or examples only.
- [ ] No lifecycle data payloads, private values, contracts, schemas, policy files, or validator source code are stored here.
- [ ] The note does not claim implementation maturity without tests, fixtures, runtime evidence, or code references.

## Naming guidance

Recommended local-runtime-note pattern:

```text
<YYYY-MM-DD>_<local-runtime-scope>_local-runtime-note.md
```

Examples:

```text
2026-07-03_local-harness_local-runtime-note.md
2026-07-03_mock-handoff_local-runtime-note.md
2026-07-03_receipt-route_local-runtime-note.md
```

Use lowercase filenames and hyphenated scope names.

## Open verification

- [ ] Confirm CODEOWNERS for `runtime/local/`.
- [ ] Confirm local runtime note ID format.
- [ ] Confirm local runtime note filename convention.
- [ ] Confirm relationship to `runtime/service_configs/`.
- [ ] Confirm relationship to `runtime/model_adapters/`.
- [ ] Confirm relationship to `runtime/mock/`.
- [ ] Confirm relationship to `runtime/envelopes/`.
- [ ] Confirm runtime contract pointer format.
- [ ] Confirm schema pointer format.
- [ ] Confirm policy pointer format.
- [ ] Confirm receipt and validation pointer formats.
- [ ] Confirm whether local runtime notes require schema validation.
- [ ] Confirm whether `runtime/README.md` should index `local/` directly with this README.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First local runtime note, local harness update, service config update, adapter update, mock update, envelope update, receipt update, validator update, or runtime placement review |
