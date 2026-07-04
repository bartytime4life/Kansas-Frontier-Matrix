# `runtime/mock/` — Mock Runtime Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-mock-readme
title: runtime/mock/ — Mock Runtime Lane
version: v1
status: draft
policy_label: public
owners:
  - <runtime-steward>
  - <test-steward>
  - <governed-ai-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, runtime, mock, deterministic-tests, mock-adapter, finite-outcomes, receipts]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-runtime%2F-blue)
![lane](https://img.shields.io/badge/lane-mock-blueviolet)
![posture](https://img.shields.io/badge/posture-mock--first-orange)
![audit](https://img.shields.io/badge/audit-testable-green)

## Purpose

`runtime/mock/` is the runtime lane for deterministic mock-runtime notes and mock adapter handoff documentation.

It may hold mock runtime indexes, mock adapter notes, fixture-routing notes, finite-outcome coverage notes, and review records that explain how mock behavior supports KFM tests without becoming evidence, release material, or production truth.

This lane is not a live provider home, not a lifecycle data home, not a contract/schema/policy home, not a validator-code home, and not release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Mock runtime README |
| Owning root | `runtime/` |
| Lane | `runtime/mock/` |
| Status | Draft |
| Authority level | Runtime-lane guidance and index. Runtime contracts, schemas, policy, fixtures, validation records, tests, receipt records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was a greenfield stub before this update. Directory Rules name `runtime/mock/` as the MockAdapter lane for deterministic tests. |
| Default posture | Mock runtime records must be visibly mock-only, deterministic, testable, and downstream of contracts, schemas, fixtures, policy, and validation. |
| Required reviewers | Runtime steward, test steward, governed-AI steward when AI mock behavior is involved, and docs steward. |

## Placement basis

Current-session evidence confirms `runtime/README.md` describes `runtime/` as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release.

Directory Rules list `runtime/mock/` under `runtime/` as the lane for MockAdapter and deterministic tests.

Current-session evidence also confirms the governed-AI mock-first doctrine says the first useful governed-AI slice should run on contract-valid mocks before live model providers, real source endpoints, or production bindings are admitted.

## Repo fit

```text
runtime/
├── README.md
├── mock/                 # you are here
├── local/
├── model_adapters/
├── ollama/
├── service_configs/
└── envelopes/
```

## Mock-runtime responsibilities

| Responsibility | Expectation |
|---|---|
| Mock identity | Name the mock adapter, fixture route, or deterministic runtime slice. |
| Determinism | State what input produces what expected output or outcome class. |
| Contract posture | Link runtime contracts when mock output is contract-shaped. |
| Schema posture | Link schema paths when mock records are validated. |
| Fixture posture | Link fixtures used by tests. |
| Policy posture | Link policy references when mock behavior exercises policy gates. |
| Outcome posture | Cover finite outcomes where relevant: `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. |
| Receipt posture | Link AIReceipt, RunReceipt, validation receipt, or runtime envelope records when applicable. |
| Migration posture | Record when mock notes graduate to adapter, envelope, local, or service-config lanes. |

## What belongs here

- Mock runtime README and index notes.
- Mock adapter notes.
- Mock fixture-routing notes.
- Deterministic outcome coverage notes.
- Mock-first review notes.
- Pointers to `fixtures/`, `tests/`, `contracts/runtime/`, `schemas/contracts/v1/runtime/`, `policy/runtime/`, `runtime/envelopes/`, `runtime/model_adapters/`, and receipt lanes.
- Notes explaining how mock outputs remain test material and do not become evidence, release records, or publication authority.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- EvidenceBundle contents or source records.
- Live provider implementation records.
- Release manifests, release decisions, correction records, signatures, or notices.
- Canonical contracts, schemas, policy files, or validator source code.
- Private runtime values.
- Generated text treated as evidence, policy, review, or publication authority.
- Mock outputs presented as released truth.

## Mock runtime status values

Use finite mock-runtime status values where possible:

| Status | Meaning |
|---|---|
| `DRAFT` | Mock note exists but is not ready for review. |
| `READY_FOR_REVIEW` | Mock note is ready for maintainer or steward review. |
| `ACTIVE_MOCK` | Mock note is accepted for deterministic test use. |
| `FIXTURE_REQUIRED` | Mock note needs a paired fixture before use. |
| `VALIDATION_REQUIRED` | Mock note needs validator or test evidence before use. |
| `HELD` | Mock note is blocked pending contract, schema, policy, fixture, or placement review. |
| `MIGRATE` | Mock note should move to another runtime lane. |
| `SUPERSEDED` | A newer mock note replaces this one. |
| `RETIRED` | Mock note is no longer active. |

## Required mock-runtime fields

Every mock runtime note should capture:

- Mock runtime note ID
- Mock status
- Mock adapter or fixture name
- Runtime scope
- Contract pointer, when applicable
- Schema pointer, when applicable
- Fixture pointer, when applicable
- Test pointer, when applicable
- Policy pointer, when applicable
- Receipt pointer, when applicable
- Expected finite outcome
- Determinism note
- Reviewer
- Review date
- Open blockers
- Follow-up items

## Minimal mock runtime note

```markdown
# <mock-runtime-note-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE_MOCK / FIXTURE_REQUIRED / VALIDATION_REQUIRED / HELD / MIGRATE / SUPERSEDED / RETIRED

## Runtime scope
<mock adapter, fixture route, envelope helper, receipt route, test support, or N/A>

## Mock target
<adapter name, fixture name, contract family, or N/A>

## Expected finite outcome
ANSWER / ABSTAIN / DENY / ERROR / N/A

## Governed support pointers
- Contract: <path or N/A>
- Schema: <path or N/A>
- Fixture: <path or N/A>
- Test: <path or N/A>
- Policy: <path or N/A>
- Receipt: <path or N/A>
- Envelope: <path or N/A>

## Determinism note
<what is fixed, repeatable, or still NEEDS VERIFICATION>

## Boundary notes
<what this mock may support and what it must not become>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Mock runtime scope is clear.
- [ ] Mock target is clear.
- [ ] Expected finite outcome is explicit or marked N/A.
- [ ] Contract pointer is linked when output is contract-shaped.
- [ ] Schema pointer is linked when output is schema-validated.
- [ ] Fixture pointer is linked when fixture behavior is claimed.
- [ ] Test pointer is linked when implementation behavior is claimed.
- [ ] Policy pointer is linked when mock behavior exercises policy gates.
- [ ] Receipt or envelope pointer is linked when applicable.
- [ ] No lifecycle data payloads, live provider records, contracts, schemas, policy files, or validator source code are stored here.
- [ ] The note does not claim implementation maturity without tests, fixtures, runtime evidence, or code references.

## Naming guidance

Recommended mock-runtime-note pattern:

```text
<YYYY-MM-DD>_<mock-scope>_mock-runtime-note.md
```

Examples:

```text
2026-07-03_mock-adapter_mock-runtime-note.md
2026-07-03_runtime-envelope-mock_mock-runtime-note.md
2026-07-03_ai-receipt-mock_mock-runtime-note.md
```

Use lowercase filenames and hyphenated scope names.

## Open verification

- [ ] Confirm CODEOWNERS for `runtime/mock/`.
- [ ] Confirm mock runtime note ID format.
- [ ] Confirm mock runtime note filename convention.
- [ ] Confirm relationship to `runtime/model_adapters/`.
- [ ] Confirm relationship to `runtime/envelopes/`.
- [ ] Confirm relationship to `fixtures/` and `tests/`.
- [ ] Confirm runtime contract pointer format.
- [ ] Confirm schema pointer format.
- [ ] Confirm policy pointer format.
- [ ] Confirm receipt pointer format.
- [ ] Confirm whether mock runtime notes require schema validation.
- [ ] Confirm whether `runtime/README.md` should index `mock/` directly with this README.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First mock runtime note, mock adapter update, fixture update, test update, runtime contract update, schema update, policy update, receipt update, envelope update, or runtime placement review |
