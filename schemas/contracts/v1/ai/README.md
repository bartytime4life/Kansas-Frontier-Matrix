# `schemas/contracts/v1/ai/` — AI Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-ai-readme
title: schemas/contracts/v1/ai/ — AI Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <governed-ai-steward>
  - <runtime-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, ai, governed-ai, runtime, compatibility, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![lane](https://img.shields.io/badge/lane-ai-blueviolet)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/ai/` is a draft compatibility and index lane for AI-related schema notes.

It should help maintainers decide whether AI-shaped schema objects belong here, under `schemas/contracts/v1/runtime/`, or under another accepted schema family. Current-session evidence points the main governed-AI response and receipt shapes toward the runtime schema family.

This README is documentation only. It is not a schema file, not contract prose, not policy, not validator code, and not lifecycle data.

## Status & authority

| Field | Value |
|---|---|
| Document type | AI schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/ai/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, contracts, schema registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical schema home | NEEDS VERIFICATION. Current-session governed-AI architecture points AIReceipt and RuntimeResponseEnvelope shapes to `schemas/contracts/v1/runtime/...`. |
| Default posture | Do not create new canonical AI schema definitions directly under `schemas/contracts/v1/ai/` unless an ADR or migration note explicitly confirms this as the accepted schema family. |
| Required reviewers | Schema steward, governed-AI steward, runtime steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session governed-AI architecture identifies `AIReceipt` meaning at `contracts/runtime/ai_receipt.md` and its proposed shape at `schemas/contracts/v1/runtime/ai_receipt.schema.json`. It also identifies `RuntimeResponseEnvelope` meaning at `contracts/runtime/runtime_response_envelope.md` and its proposed shape at `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── ai/                         # you are here; compatibility/index lane
        └── runtime/                    # likely canonical runtime AI shape lane; NEEDS VERIFICATION

contracts/
└── runtime/
    ├── ai_receipt.md
    └── runtime_response_envelope.md

runtime/
├── model_adapters/
├── mock/
├── ollama/
└── envelopes/
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/ai/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home. |
| Search for AI schema paths | Did not confirm a canonical `schemas/contracts/v1/ai/README.md` beyond this blank file. |
| Governed-AI architecture | Points AIReceipt and RuntimeResponseEnvelope shapes to `schemas/contracts/v1/runtime/...`. |
| Search for AI object surfaces | Found `contracts/runtime/ai_receipt.md`, `contracts/runtime/runtime_response_envelope.md`, governed-AI docs, adapter docs, and runtime envelope fixtures. |

This README does not verify schema contents, registry entries, fixture coverage, validator wiring, CI behavior, or whether `schemas/contracts/v1/ai/` should remain as a compatibility path.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether AI schemas belong here, under `schemas/contracts/v1/runtime/`, or under another accepted family. |
| Drift prevention | Prevent duplicate canonical schemas under `schemas/contracts/v1/ai/`. |
| Runtime alignment | Keep AI receipt, response-envelope, adapter, and policy-related shapes aligned with runtime contracts when applicable. |
| Migration notes | Record migration notes if compatibility files need to move. |
| Contract linkage | Point to paired runtime or AI-related contracts when verified. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to canonical AI or runtime schema files once confirmed.
- Migration notes for moving AI schema files into the accepted schema-home path.
- Drift notes about duplicate or stale AI schema paths.
- Links to canonical schemas, contracts, fixtures, validators, registry records, and tests.
- Notes explaining whether an AI-shaped object is actually a runtime object, policy object, UI object, or separate AI family.

## What does not belong here

- New canonical AI schema definitions.
- Duplicate copies of canonical schema files.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Generated text treated as evidence, policy, review, or publication authority.
- Claims that this path is canonical without ADR, registry, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate canonical schema locations. |
| `ALIAS_CANDIDATE` | This path may be an alias for `schemas/contracts/v1/runtime/` or another accepted family. |
| `TRANSITIONAL` | Content is awaiting migration to canonical schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_RUNTIME` | Content should move under `schemas/contracts/v1/runtime/` if that lane is confirmed. |
| `MIGRATE_TO_AI` | Content should remain under `schemas/contracts/v1/ai/` if this lane is accepted by ADR or steward decision. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <ai-schema-compatibility-note-id>

## Status
INDEX_ONLY / ALIAS_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_RUNTIME / MIGRATE_TO_AI / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/ai/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/runtime/... / schemas/contracts/v1/ai/... / NEEDS VERIFICATION>

## Paired contract
<contracts/runtime/... / contracts/ai/... / N/A>

## Fixtures
<fixtures/contracts/v1/runtime/... / fixtures/contracts/v1/ai/... / N/A>

## Validator
<tools/validators/... or N/A>

## Family decision
<runtime / ai / policy / ui / other / NEEDS VERIFICATION>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] Object family decision is recorded.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] No duplicate canonical schema definitions are placed under `schemas/contracts/v1/ai/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_compatibility-note.md
```

Examples:

```text
2026-07-03_ai-receipt_compatibility-note.md
2026-07-03_runtime-response-envelope_compatibility-note.md
2026-07-03_model-adapter-output_compatibility-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/ai/`.
- [ ] Confirm whether `schemas/contracts/v1/ai/` should remain an index-only compatibility lane.
- [ ] Confirm whether canonical schema home should be `schemas/contracts/v1/runtime/`, `schemas/contracts/v1/ai/`, or another accepted family.
- [ ] Confirm whether `schemas/contracts/v1/runtime/README.md` exists or should be expanded.
- [ ] Confirm paired AI/runtime contract paths.
- [ ] Confirm AI/runtime schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/README.md` should index this compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical-home decision, new AI/runtime schema, AI schema migration, validator update, fixture update, schema registry update, ADR update, or compatibility-lane decision |
