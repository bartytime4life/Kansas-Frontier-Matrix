# `runtime/flora/` — Flora Runtime Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-flora-readme
title: runtime/flora/ — Flora Runtime Review Lane
version: v1
status: draft
policy_label: public
owners:
  - <runtime-steward>
  - <flora-domain-steward>
  - <policy-steward>
  - <evidence-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, runtime, flora, domain-runtime, governed-ai, receipts, validation, geoprivacy]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-runtime%2F-blue)
![domain](https://img.shields.io/badge/domain-flora-green)
![posture](https://img.shields.io/badge/posture-domain--runtime--review-orange)
![audit](https://img.shields.io/badge/audit-receipted-green)

## Purpose

`runtime/flora/` is a draft runtime review lane for Flora-specific runtime notes.

It may hold Flora runtime handoff notes, adapter notes, envelope notes, receipt-routing notes, mock-runtime notes, and validation notes that explain how Flora runtime behavior stays downstream of governed evidence, policy, sensitivity review, and release state.

This lane is not the Flora doctrine home, not the Flora package home, not a pipeline home, not a schema or contract home, not a policy home, and not a lifecycle data home.

## Status & authority

| Field | Value |
|---|---|
| Document type | Flora runtime README |
| Owning root | `runtime/` |
| Requested path | `runtime/flora/` |
| Status | Draft |
| Authority level | Runtime review guidance and index. Flora doctrine, contracts, schemas, policy, pipelines, packages, evidence records, validation receipts, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a blank file before this update. Directory Rules list functional runtime sublanes such as `local/`, `model_adapters/`, `ollama/`, `mock/`, `service_configs/`, and `envelopes/`; a domain-specific runtime lane needs maintainer confirmation. |
| Default posture | Treat this lane as a draft domain-runtime pointer and review lane until maintainers confirm whether Flora runtime notes should live here or under functional runtime sublanes. |
| Required reviewers | Runtime steward, Flora domain steward, policy steward when access or sensitivity posture is involved, evidence steward when evidence pointers are involved, and docs steward. |

## Placement basis

Current-session evidence confirms `runtime/README.md` describes `runtime/` as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release.

Directory Rules describe `runtime/` as a runtime root with functional sublanes for local wiring, provider-neutral model adapters, local model runtime, mock adapters, service configuration, and finite-outcome envelope helpers.

Current-session evidence also confirms `packages/domains/flora/README.md` is the shared helper-code lane for Flora. That package README states that Flora helper code is not Flora doctrine, schema authority, contract authority, policy authority, lifecycle data, evidence closure, or release approval.

## Repo fit

```text
runtime/
├── README.md
├── flora/                # you are here; draft domain-runtime review lane
├── local/
├── model_adapters/
├── ollama/
├── mock/
├── service_configs/
└── envelopes/

packages/
└── domains/
    └── flora/            # shared Flora helper-code lane, not runtime authority
```

## Flora runtime responsibilities

| Responsibility | Expectation |
|---|---|
| Runtime scope | State whether the note concerns a Flora adapter, mock, envelope, receipt route, service configuration, or local runtime handoff. |
| Canonical home | State whether the item belongs in `runtime/flora/`, a functional runtime sublane, `packages/domains/flora/`, or another governed root. |
| Evidence posture | Link evidence pointers when Flora runtime behavior depends on evidence. |
| Policy posture | Link policy decisions or policy notes when Flora access, sensitivity, or public posture affects runtime behavior. |
| Geoprivacy posture | Link geoprivacy, generalization, or redaction support when sensitive Flora location posture affects runtime output. |
| Receipt posture | Link AIReceipt, run receipt, validation receipt, or runtime envelope records when applicable. |
| Release posture | Link release manifests, decisions, correction records, or notices when runtime behavior depends on release state. |
| Validation posture | Link tests, fixtures, validators, or review receipts when behavior is claimed. |
| Migration posture | Record whether the note should move to a functional runtime lane or remain here as a Flora runtime pointer. |

## What belongs here

- Flora runtime README and index notes.
- Flora runtime handoff notes.
- Flora adapter or mock-runtime notes that are not canonical package code.
- Flora runtime envelope and receipt-routing notes.
- Runtime review notes that explain evidence, policy, sensitivity, geoprivacy, release, validation, or correction posture for Flora runtime behavior.
- Pointers to `packages/domains/flora/`, `policy/domains/flora/`, `policy/sensitivity/flora/`, `contracts/domains/flora/`, `schemas/contracts/v1/domains/flora/`, `data/receipts/ai/flora/`, `runtime/envelopes/`, and functional runtime sublanes.

## What does not belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Flora occurrence, specimen, plot, vegetation, taxon, or source records.
- Exact sensitive Flora location payloads.
- Canonical Flora doctrine, contracts, schemas, policy files, or package implementation code.
- Executable pipeline logic.
- Release manifests, release decisions, correction records, signatures, or notices.
- Credentials, tokens, provider keys, or private configuration values.
- Generated text treated as evidence, policy, review, or publication authority.
- A parallel Flora runtime authority without a migration note or ADR.

## Runtime outcomes

Use finite runtime outcomes where possible:

| Outcome | Meaning |
|---|---|
| `ANSWER` | Runtime produced supported Flora response posture. |
| `ABSTAIN` | Runtime did not answer because evidence, policy, sensitivity, citation, or release support was insufficient. |
| `DENY` | Runtime denied the request because policy or governance state forbids response. |
| `ERROR` | Runtime could not complete due to validation, adapter, configuration, or envelope failure. |
| `HELD_FOR_REVIEW` | Runtime note requires steward review before use or migration. |

## Required Flora runtime fields

Every Flora runtime note should capture:

- Runtime note ID
- Runtime note status
- Runtime scope
- Flora domain scope
- Canonical home
- Runtime mode
- Evidence posture
- Policy posture
- Geoprivacy posture, when applicable
- Receipt pointer, when applicable
- Runtime envelope pointer, when applicable
- Release pointer, when applicable
- Validation pointer, when applicable
- Outcome posture
- Reviewer
- Review date
- Open blockers
- Follow-up items

## Minimal Flora runtime note

```markdown
# <flora-runtime-note-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE / HELD_FOR_REVIEW / MIGRATE / SUPERSEDED / RETIRED

## Runtime scope
<adapter, mock runtime, local runtime, envelope helper, receipt route, service config, or N/A>

## Flora domain scope
<taxonomy, occurrence, specimen, vegetation, phenology, invasive plants, geoprivacy, sensitivity, public aggregate, or N/A>

## Canonical home
<runtime/flora/ / runtime/model_adapters/ / runtime/envelopes/ / runtime/mock/ / packages/domains/flora/ / other / N/A>

## Governed support pointers
- Evidence: <path or N/A>
- Policy: <path or N/A>
- Geoprivacy or sensitivity review: <path or N/A>
- Receipt: <path or N/A>
- Runtime envelope: <path or N/A>
- Release: <path or N/A>
- Validation: <path or N/A>

## Outcome posture
ANSWER / ABSTAIN / DENY / ERROR / HELD_FOR_REVIEW / N/A

## Boundary notes
<what this runtime note may support and what it must not become>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Runtime scope is clear.
- [ ] Flora domain scope is clear.
- [ ] Canonical home is explicit.
- [ ] Evidence posture is linked or marked N/A.
- [ ] Policy posture is linked or marked N/A.
- [ ] Geoprivacy or sensitivity posture is linked or marked N/A.
- [ ] Receipt and runtime-envelope pointers are linked when applicable.
- [ ] Release-state pointer is linked when runtime behavior depends on release state.
- [ ] Validation support is linked when behavior is claimed.
- [ ] No data payloads, sensitive location payloads, credentials, package implementation code, schemas, contracts, or policy files are stored here.
- [ ] The note does not claim implementation maturity without tests, fixtures, runtime evidence, or code references.

## Naming guidance

Recommended runtime-note pattern:

```text
<YYYY-MM-DD>_<flora-runtime-scope>_runtime-note.md
```

Examples:

```text
2026-07-03_flora-mock-adapter_runtime-note.md
2026-07-03_flora-geoprivacy-envelope_runtime-note.md
2026-07-03_flora-ai-receipt-route_runtime-note.md
```

Use lowercase filenames and hyphenated scope names.

## Open verification

- [ ] Confirm whether `runtime/flora/` remains a domain-runtime lane or should migrate to functional runtime sublanes.
- [ ] Confirm CODEOWNERS for `runtime/flora/`.
- [ ] Confirm relationship to `packages/domains/flora/`.
- [ ] Confirm relationship to `data/receipts/ai/flora/`.
- [ ] Confirm Flora runtime adapter paths.
- [ ] Confirm Flora runtime envelope paths.
- [ ] Confirm Flora geoprivacy and sensitivity review pointer formats.
- [ ] Confirm evidence pointer format.
- [ ] Confirm policy pointer format.
- [ ] Confirm receipt and validation pointer formats.
- [ ] Confirm whether Flora runtime notes require schema validation.
- [ ] Confirm whether `runtime/README.md` should index `flora/` directly.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Domain-runtime placement decision, first Flora runtime note, Flora adapter update, Flora receipt update, Flora envelope update, policy update, sensitivity/geoprivacy update, validator update, or package/runtime integration review |
