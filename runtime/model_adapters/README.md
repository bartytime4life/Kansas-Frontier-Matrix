# `runtime/model_adapters/` — Model Adapter Runtime Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-model-adapters-readme
title: runtime/model_adapters/ — Model Adapter Runtime Lane
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
tags: [kfm, runtime, model-adapters, governed-ai, provider-neutral, ai-receipt, finite-outcomes]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-runtime%2F-blue)
![lane](https://img.shields.io/badge/lane-model--adapters-blueviolet)
![posture](https://img.shields.io/badge/posture-provider--neutral-orange)
![audit](https://img.shields.io/badge/audit-receipted-green)

## Purpose

`runtime/model_adapters/` is the canonical runtime lane for provider-neutral model adapter notes and adapter handoff documentation.

It may hold model adapter indexes, adapter cards, runtime port notes, mock-to-live migration notes, finite-outcome behavior notes, and review records that explain how model adapters remain downstream of evidence, policy, citation validation, runtime envelopes, receipts, and release state.

This lane is not a model provider home by itself, not a lifecycle data home, not a contract/schema/policy home, not a validator-code home, and not release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Model adapter runtime README |
| Owning root | `runtime/` |
| Lane | `runtime/model_adapters/` |
| Status | Draft |
| Authority level | Runtime-lane guidance and index. Runtime contracts, schemas, policy, fixtures, validation records, tests, receipt records, runtime envelopes, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was a greenfield stub before this update. Directory Rules name `runtime/model_adapters/` as the provider-neutral adapter lane. |
| Default posture | Adapter records must preserve provider neutrality, finite outcomes, evidence posture, policy posture, validation posture, and receipt linkage where applicable. |
| Required reviewers | Runtime steward, governed-AI steward when AI adapter behavior is involved, policy steward when behavior is gated, evidence steward when evidence pointers are involved, and docs steward. |

## Placement basis

Current-session evidence confirms `runtime/README.md` describes `runtime/` as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release.

Directory Rules list `runtime/model_adapters/` under `runtime/` as the lane for provider-agnostic model adapter interfaces.

Current-session evidence also confirms `runtime/adapters/README.md` is a draft compatibility/index lane that points to `runtime/model_adapters/` as the Directory Rules lane. This README is therefore the canonical adapter lane unless a future ADR or migration note says otherwise.

Governed-AI architecture also identifies `runtime/model_adapters/`, `runtime/mock/`, `runtime/ollama/`, and `runtime/envelopes/` as implementation homes for adapters and related runtime pieces.

## Repo fit

```text
runtime/
├── README.md
├── model_adapters/       # you are here; provider-neutral adapter lane
├── adapters/             # compatibility/index lane; should point here
├── mock/
├── ollama/
├── local/
├── service_configs/
└── envelopes/
```

## Model-adapter responsibilities

| Responsibility | Expectation |
|---|---|
| Adapter identity | Name the adapter, adapter family, and owning steward. |
| Provider neutrality | Keep the adapter contract stable across mock, local, and provider-backed implementations. |
| Runtime mode | State whether the adapter is mock, local, provider-backed, or other. |
| Contract posture | Link runtime contracts when adapter input or output is contract-shaped. |
| Schema posture | Link schema paths when adapter records are validated. |
| Policy posture | Link policy references when adapter behavior is gated. |
| Evidence posture | State how the adapter receives governed evidence pointers or approved inputs. |
| Citation posture | Link citation-validation support when generated text cites evidence. |
| Receipt posture | Link AIReceipt, RunReceipt, validation receipt, or runtime envelope records when applicable. |
| Test posture | Link fixtures, mock behavior, or validator evidence when behavior is claimed. |
| Migration posture | Record whether an adapter note was migrated from `runtime/adapters/`, `runtime/mock/`, or `runtime/ollama/`. |

## What belongs here

- Model adapter README and indexes.
- Provider-neutral adapter cards.
- Adapter interface notes and runtime port notes.
- Mock-to-live migration notes.
- Adapter outcome coverage notes.
- Adapter receipt and envelope handoff notes.
- Pointers to `runtime/mock/`, `runtime/ollama/`, `runtime/envelopes/`, `contracts/runtime/`, `schemas/contracts/v1/runtime/`, `policy/runtime/`, `policy/ai/`, fixtures, tests, validators, and receipt lanes.
- Review notes explaining how adapter behavior remains downstream of evidence, policy, validation, and release state.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- EvidenceBundle contents or source records.
- Release manifests, release decisions, correction records, signatures, or notices.
- Canonical contracts, schemas, policy files, or validator source code.
- Provider credentials, private runtime values, or private configuration values.
- Private model internals.
- Generated text treated as evidence, policy, review, or publication authority.
- Public claims based only on adapter output.

## Adapter status values

Use finite adapter status values where possible:

| Status | Meaning |
|---|---|
| `DRAFT` | Adapter note exists but is not ready for review. |
| `READY_FOR_REVIEW` | Adapter note is ready for maintainer or steward review. |
| `ACTIVE_ADAPTER` | Adapter note is accepted for the named runtime lane. |
| `MOCK_ONLY` | Adapter note is limited to deterministic or test usage. |
| `LOCAL_ONLY` | Adapter note is limited to local runtime use. |
| `PROVIDER_BOUND` | Adapter note depends on a provider-specific implementation. |
| `VALIDATION_REQUIRED` | Adapter note needs validator, fixture, or test evidence before use. |
| `HELD` | Adapter note is blocked pending contract, schema, policy, fixture, receipt, or placement review. |
| `MIGRATE` | Adapter note should move to another runtime lane. |
| `SUPERSEDED` | A newer adapter note replaces this one. |
| `RETIRED` | Adapter note is no longer active. |

## Required adapter-card fields

Every model adapter card or adapter note should capture:

- Adapter card ID
- Adapter name
- Adapter status
- Adapter family
- Runtime mode
- Canonical home
- Allowed use case
- Provider posture
- Evidence posture
- Policy posture
- Citation posture, when applicable
- Receipt posture
- Runtime outcome posture
- Contract pointer, when applicable
- Schema pointer, when applicable
- Policy pointer, when applicable
- AIReceipt pointer, when applicable
- RuntimeResponseEnvelope pointer, when applicable
- Fixture or validator pointer, when applicable
- Reviewer
- Review date
- Open blockers
- Follow-up items

## Minimal adapter card

```markdown
# <model-adapter-card-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE_ADAPTER / MOCK_ONLY / LOCAL_ONLY / PROVIDER_BOUND / VALIDATION_REQUIRED / HELD / MIGRATE / SUPERSEDED / RETIRED

## Adapter name
<adapter name>

## Adapter family
<mock / local / provider-neutral / provider-specific / other / N/A>

## Runtime mode
<mock / local / provider / other / N/A>

## Canonical home
<runtime/model_adapters/ / runtime/mock/ / runtime/ollama/ / runtime/envelopes/ / other / N/A>

## Allowed use
<short governed use case or N/A>

## Governed support pointers
- Contract: <path or N/A>
- Schema: <path or N/A>
- Policy: <path or N/A>
- Citation validation: <path or N/A>
- AIReceipt: <path or N/A>
- RuntimeResponseEnvelope: <path or N/A>
- Fixture or validator: <path or N/A>

## Boundary notes
<what this adapter may do and what it must not become>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Adapter name is present.
- [ ] Adapter family is clear.
- [ ] Runtime mode is clear.
- [ ] Canonical home is explicit.
- [ ] Provider posture is explicit.
- [ ] Evidence posture is explicit.
- [ ] Policy posture is explicit when adapter behavior is gated.
- [ ] Citation posture is explicit when generated text cites evidence.
- [ ] Receipt posture is explicit when the adapter participates in receipted runtime events.
- [ ] RuntimeResponseEnvelope or AIReceipt pointers are linked when applicable.
- [ ] Fixtures, tests, or validators are linked when behavior is claimed.
- [ ] No data payloads, private provider values, contracts, schemas, policy files, or validator source code are stored here.
- [ ] The entry does not claim implementation maturity without tests, fixtures, runtime evidence, or code references.

## Naming guidance

Recommended adapter-card pattern:

```text
<YYYY-MM-DD>_<adapter-name>_model-adapter-card.md
```

Examples:

```text
2026-07-03_mock-adapter_model-adapter-card.md
2026-07-03_ollama-local_model-adapter-card.md
2026-07-03_provider-neutral-port_model-adapter-card.md
```

Use lowercase filenames and hyphenated adapter names.

## Open verification

- [ ] Confirm CODEOWNERS for `runtime/model_adapters/`.
- [ ] Confirm adapter-card ID format.
- [ ] Confirm adapter-card filename convention.
- [ ] Confirm relationship to `runtime/adapters/` compatibility lane.
- [ ] Confirm relationship to `runtime/mock/`.
- [ ] Confirm relationship to `runtime/ollama/`.
- [ ] Confirm relationship to `runtime/envelopes/`.
- [ ] Confirm runtime contract pointers.
- [ ] Confirm schema pointer format.
- [ ] Confirm policy pointer format.
- [ ] Confirm AIReceipt and RuntimeResponseEnvelope pointer formats.
- [ ] Confirm fixture and validator paths.
- [ ] Confirm whether adapter cards require schema validation.
- [ ] Confirm whether `runtime/README.md` should index `model_adapters/` directly with this README.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First model adapter card, adapter interface update, mock adapter update, local/provider adapter update, runtime contract update, policy update, receipt update, validator update, or adapter implementation review |
