# `runtime/adapters/` — Runtime Adapter Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-adapters-readme
title: runtime/adapters/ — Runtime Adapter Index
version: v1
status: draft
policy_label: public
owners:
  - <runtime-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, runtime, adapters, model-adapters, receipts, envelopes]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-runtime%2F-blue)
![lane](https://img.shields.io/badge/lane-adapters-blueviolet)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)

## Purpose

`runtime/adapters/` is a draft index for runtime adapter notes.

It may hold adapter inventories, adapter-card templates, and migration notes while maintainers decide whether this path remains active or points to the Directory Rules lane `runtime/model_adapters/`.

This README should not create a second adapter authority. It should help reviewers see the current adapter naming situation and move records to the accepted home when that decision is made.

## Status & authority

| Field | Value |
|---|---|
| Document type | Runtime adapter index README |
| Owning root | `runtime/` |
| Requested path | `runtime/adapters/` |
| Status | Draft |
| Authority level | Index guidance. Runtime contracts, schemas, policy, validation records, `runtime/model_adapters/`, runtime envelope records, tests, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a blank file before this update. Directory Rules name `runtime/model_adapters/`, not `runtime/adapters/`, as the provider-neutral adapter lane. |
| Default posture | Treat this as a compatibility/index lane until maintainers confirm the canonical adapter path. |
| Required reviewers | Runtime steward and docs steward; governed-AI, policy, or evidence stewards when adapter behavior touches those surfaces. |

## Placement basis

Current-session evidence confirms `runtime/README.md` describes `runtime/` as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release.

Directory Rules describe `runtime/` as a runtime root with sublanes for local wiring, provider-neutral model adapters, local model runtime, mock adapters, service configuration, and envelope helpers.

Current-session evidence also confirms `runtime/model_adapters/README.md` exists but is still a greenfield stub. Until maintainers decide naming, use `runtime/adapters/` as a compatibility/index lane only.

## Repo fit

```text
runtime/
├── README.md
├── adapters/             # you are here; draft compatibility/index lane
├── model_adapters/       # Directory Rules provider-neutral adapter lane
├── local/
├── ollama/
├── mock/
├── service_configs/
└── envelopes/
```

## Adapter-index responsibilities

| Responsibility | Expectation |
|---|---|
| Adapter identity | Name the adapter and owner. |
| Canonical home | State whether the adapter belongs here temporarily or under `runtime/model_adapters/`. |
| Runtime mode | State whether the adapter is mock, local, provider-backed, or other. |
| Contract linkage | Link relevant runtime contracts when applicable. |
| Schema linkage | Link schema paths when adapter records are validated. |
| Policy linkage | Link policy packages or decisions when behavior is gated. |
| Receipt linkage | Link run receipts or AI receipts when applicable. |
| Test linkage | Link fixtures, mock behavior, or validator evidence when available. |
| Migration posture | Record whether the note should move to `runtime/model_adapters/` or remain as a pointer. |

## What belongs here

- Runtime adapter index README.
- Temporary adapter inventory notes.
- Adapter-card templates.
- Migration notes from `runtime/adapters/` to `runtime/model_adapters/` if maintainers choose that path.
- Links to runtime contracts, schemas, policy packages, fixtures, validators, receipts, and envelope helpers.
- Review notes that keep adapters downstream of evidence, policy, validation, and release state.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Source records or EvidenceBundle contents.
- Release manifests, release decisions, correction records, signatures, or notices.
- Canonical contracts, schemas, policy files, or validator source code.
- Credentials, tokens, keys, or private configuration values.
- Private model internals.
- Generated text treated as evidence, policy, review, or publication authority.
- A second adapter authority parallel to `runtime/model_adapters/` without a migration note or ADR.

## Adapter status values

Use finite adapter status values where possible:

| Status | Meaning |
|---|---|
| `DRAFT` | Adapter note exists but is not ready for review. |
| `READY_FOR_REVIEW` | Adapter note is ready for maintainer or steward review. |
| `ACTIVE` | Adapter note is accepted for the named runtime lane. |
| `MOCK_ONLY` | Adapter is only for deterministic or test usage. |
| `LOCAL_ONLY` | Adapter is only for local runtime use. |
| `HELD` | Adapter is blocked pending evidence, policy, validation, or placement review. |
| `MIGRATE_TO_MODEL_ADAPTERS` | Adapter note should move or point to `runtime/model_adapters/`. |
| `SUPERSEDED` | A newer adapter note replaces this one. |
| `RETIRED` | Adapter note is no longer active. |

## Required adapter-card fields

Every adapter card or adapter note should capture:

- Adapter card ID
- Adapter name
- Adapter status
- Adapter type
- Runtime mode
- Canonical home
- Allowed use case
- Evidence posture
- Policy posture
- Receipt posture
- Runtime outcome posture
- Contract pointer, when applicable
- Schema pointer, when applicable
- Policy pointer, when applicable
- Receipt pointer, when applicable
- Fixture or validator pointer, when applicable
- Reviewer
- Review date
- Open blockers
- Follow-up items

## Minimal adapter card

```markdown
# <adapter-card-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE / MOCK_ONLY / LOCAL_ONLY / HELD / MIGRATE_TO_MODEL_ADAPTERS / SUPERSEDED / RETIRED

## Adapter name
<adapter name>

## Runtime mode
<mock / local / provider / other / N/A>

## Canonical home
<runtime/adapters/ / runtime/model_adapters/ / N/A>

## Allowed use
<short governed use case or N/A>

## Governed support pointers
- Contract: <path or N/A>
- Schema: <path or N/A>
- Policy: <path or N/A>
- Receipt: <path or N/A>
- Envelope: <path or N/A>
- Fixture or validator: <path or N/A>

## Boundary notes
<what this adapter may do and must not do>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Adapter name is present.
- [ ] Runtime mode is clear.
- [ ] Canonical home is explicit.
- [ ] Evidence posture is explicit.
- [ ] Policy posture is explicit when behavior is gated.
- [ ] Receipt posture is explicit when the adapter participates in receipted runtime events.
- [ ] Envelope or receipt pointers are linked when applicable.
- [ ] Fixtures, tests, or validators are linked when behavior is claimed.
- [ ] No data payloads, credentials, keys, or private model internals are stored here.
- [ ] The entry does not create a parallel authority against `runtime/model_adapters/` without an ADR or migration note.

## Naming guidance

Recommended adapter-card pattern:

```text
<YYYY-MM-DD>_<adapter-name>_adapter-card.md
```

Examples:

```text
2026-07-03_mock-adapter_adapter-card.md
2026-07-03_ollama-local_adapter-card.md
2026-07-03_receipt-adapter_adapter-card.md
```

Use lowercase filenames and hyphenated adapter names.

## Open verification

- [ ] Confirm whether `runtime/adapters/` remains a compatibility/index lane or should migrate to `runtime/model_adapters/`.
- [ ] Confirm CODEOWNERS for `runtime/adapters/`.
- [ ] Expand `runtime/model_adapters/README.md` so the Directory Rules lane is not a greenfield stub.
- [ ] Confirm adapter-card ID format.
- [ ] Confirm adapter-card filename convention.
- [ ] Confirm runtime contract pointers.
- [ ] Confirm schema pointer format.
- [ ] Confirm policy pointer format.
- [ ] Confirm receipt and envelope pointer formats.
- [ ] Confirm fixture and validator paths.
- [ ] Confirm whether adapter cards require schema validation.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical adapter-lane decision, `runtime/model_adapters/README.md` expansion, first adapter card, runtime contract update, policy update, receipt update, validator update, or adapter implementation review |
