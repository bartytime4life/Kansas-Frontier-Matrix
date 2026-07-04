# `runtime/log/` — Runtime Review Notes

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-runtime%2F-blue)
![lane](https://img.shields.io/badge/lane-log-blueviolet)

## Purpose

`runtime/log/` is a draft index for runtime review notes related to local run output, observability summaries, and handoff notes.

Use this lane for lightweight review documentation only. Durable process records belong under `data/receipts/` or a more specific receipt lane.

## Status & authority

| Field | Value |
|---|---|
| Document type | Runtime log README |
| Owning root | `runtime/` |
| Requested path | `runtime/log/` |
| Status | Draft |
| Authority level | Index guidance. Runtime contracts, schemas, receipt lanes, validation records, tests, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a blank file before this update. Directory Rules do not list `runtime/log/` as a canonical runtime sublane. |
| Default posture | Treat this as a draft pointer lane until maintainers confirm placement. |

## Placement basis

Current-session evidence confirms `runtime/README.md` describes `runtime/` as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release.

Directory Rules list canonical runtime sublanes such as `local/`, `model_adapters/`, `ollama/`, `mock/`, `service_configs/`, and `envelopes/`; `runtime/log/` is not listed there.

Current-session evidence also confirms `data/receipts/` is the process-memory receipt root, while `data/receipts/telemetry/` is the telemetry receipt lane.

## Repo fit

```text
runtime/
├── README.md
├── log/                  # you are here; draft review/index lane
├── local/
├── model_adapters/
├── ollama/
├── mock/
├── service_configs/
└── envelopes/

data/
└── receipts/
    └── telemetry/
```

## What belongs here

- Runtime log README and index notes.
- Local run review notes.
- Runtime observation summaries.
- Handoff notes to receipt lanes.
- Pointers to tests, fixtures, validators, dashboards, and runtime contracts.
- Notes that help maintainers decide whether this path should remain or migrate.

## What does not belong here

- Lifecycle data payloads.
- Durable receipt records.
- EvidenceBundle contents.
- Release records.
- Canonical contracts, schemas, policy files, or validator source code.
- Generated text treated as evidence, review, or publication authority.

## Suggested note fields

Each note should capture:

- Note ID
- Status
- Runtime scope
- Summary class
- Support pointers
- Reviewer
- Review date
- Open blockers
- Follow-up items

## Minimal note

```markdown
# <runtime-log-note-id>

## Status
DRAFT / READY_FOR_REVIEW / ACTIVE_LOCAL / HANDOFF / HELD / MIGRATE / SUPERSEDED / RETIRED

## Runtime scope
<runtime component, local harness, envelope helper, service config, test support, or N/A>

## Summary class
<local run / validation / handoff / dashboard-support / other / N/A>

## Support pointers
- Validation: <path or N/A>
- Receipt: <path or N/A>
- Dashboard or report: <path or N/A>

## Boundary notes
<what this note may support and what it must not become>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Runtime scope is clear.
- [ ] Summary class is clear.
- [ ] Support pointers are present or marked N/A.
- [ ] Receipt material is linked to `data/receipts/` rather than stored here.
- [ ] No lifecycle data payloads, durable receipt records, contracts, schemas, policy files, or validator source code are stored here.
- [ ] The note does not claim implementation maturity without tests, fixtures, runtime evidence, or code references.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<runtime-scope>_runtime-note.md
```

Examples:

```text
2026-07-03_runtime-envelope_runtime-note.md
2026-07-03_local-harness_runtime-note.md
2026-07-03_receipt-handoff_runtime-note.md
```

## Open verification

- [ ] Confirm whether `runtime/log/` remains a runtime review lane or should migrate to another runtime/receipt lane.
- [ ] Confirm CODEOWNERS for `runtime/log/`.
- [ ] Confirm relationship to `data/receipts/`.
- [ ] Confirm relationship to `data/receipts/telemetry/`.
- [ ] Confirm note ID format.
- [ ] Confirm filename convention.
- [ ] Confirm support pointer formats.
- [ ] Confirm whether `runtime/README.md` should index `log/` directly.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Runtime log lane decision, first note, receipt update, validation update, dashboard/report update, or runtime placement review |
