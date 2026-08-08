<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/runtime-response-http-binding-v1
title: RuntimeResponseEnvelope HTTP Binding Profile v1
type: contract-profile
version: v0.1
status: draft; PROPOSED_INACTIVE; fixture-only; non-runtime
owners: OWNER_TBD — Runtime steward · API steward · Contracts steward · Schema steward · Policy steward · Evidence steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; runtime; api; transport; finite-outcomes; fail-closed
related:
  - ./runtime_response_envelope.md
  - ../../schemas/contracts/v1/runtime/runtime_response_http_binding_v1.schema.json
  - ../../tools/validators/runtime/validate_runtime_response_http_binding_v1.py
truth_posture: CONFIRMED RuntimeResponseEnvelope and four finite outcomes / PROPOSED inactive HTTP binding profile / UNKNOWN production API wiring and client behavior
[/KFM_META_BLOCK_V2] -->

# RuntimeResponseEnvelope HTTP Binding Profile v1

> **Purpose.** Make the transport relationship between HTTP response status and the existing `RuntimeResponseEnvelope.outcome` explicit enough to test, without allowing HTTP status alone to become KFM truth, evidence, policy, or release authority.

`contracts/runtime/runtime_response_envelope.md` remains the semantic parent. This profile does not add a runtime outcome and does not replace the existing envelope schema.

## v1 mapping

| HTTP status | KFM outcome | Transport meaning |
|---:|---|---|
| `200` | `ANSWER` | Request completed and a governed answer body is present. |
| `422` | `ABSTAIN` | Request was understood, but KFM cannot safely produce the requested answer under current evidence/context constraints. |
| `403` | `DENY` | Policy/governance denies delivery of the requested capability or payload. |
| `500` | `ERROR` | Bounded internal runtime failure. |
| `503` | `ERROR` | Required runtime dependency is unavailable or degraded. |

These values are **PROPOSED_INACTIVE** and fixture-only.

## Anti-collapse rules

1. HTTP status never substitutes for `RuntimeResponseEnvelope.outcome`.
2. Every mapped response requires a governed envelope body; a bare status is insufficient.
3. `ABSTAIN` is not `DENY`.
4. `DENY` is not `ERROR`.
5. `ERROR` must not imply requested facts are false.
6. `ANSWER` must not override stale, unresolved, denied, or failed governed state.
7. This profile grants no raw-store, lifecycle, promotion, release, deployment, publication, or public-use authority.

## Failure classes

- `NONE` for `ANSWER`;
- `INSUFFICIENT_EVIDENCE_OR_CONTEXT` for `ABSTAIN`;
- `POLICY_OR_GOVERNANCE_DENIAL` for `DENY`;
- `INTERNAL_RUNTIME_FAILURE` for `500` + `ERROR`;
- `DEPENDENCY_UNAVAILABLE` for `503` + `ERROR`.

## Directory Rules basis

This profile uses established responsibility roots only: `contracts/runtime/`, `schemas/contracts/v1/runtime/`, `fixtures/contracts/v1/runtime/`, `tools/validators/runtime/`, `tests/validators/`, and `.github/workflows/`. No new root or competing authority is created.

## Trust boundary

A passing fixture proves only HTTP/outcome/profile coherence. It does not prove that an API route exists, evidence resolves, policy executed correctly, an actor is authorized, or release/publication is approved.

## Rollback

Close the draft PR before merge or revert the additive profile after merge. No runtime or public state is mutated by this profile.
