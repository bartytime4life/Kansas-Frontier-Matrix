# runtime_response_envelope

> Status: PROPOSED
> Schema: https://schemas.kfm.local/contracts/v1/runtime/runtime_response_envelope.schema.json
> Schema file: schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
> Validator: tools/validators/validate_runtime_response_envelope.py (CONFIRMED — wired in tools/validators/_common/run_all.py)
> Authority: contracts/ owns meaning; schemas/contracts/v1/ owns shape (ADR-0001, ADR-0002).

## 1. Purpose
`runtime_response_envelope` is the governed API-facing response contract that carries outcome, provenance pointers, and state indicators needed for safe client rendering. It answers what the caller may treat as answer/abstain/deny/error and what governance conditions apply to display. It is not raw evidence storage and not a substitute for canonical internal lifecycle stores.

## 2. Lifecycle role
This object is emitted at the trust membrane when serving PUBLISHED-safe outputs derived from upstream PROCESSED/CATALOG evidence and policy state. It is validated before API exposure and may be superseded by later envelopes when freshness or correction posture changes. It must not imply direct RAW/WORK/QUARANTINE reads by public clients.

## 3. Fields
| field | type | required | meaning | examples or enum | policy/sensitivity notes |
|---|---|---|---|---|---|
| `id` | string | yes | Envelope identifier for traceability and client reconciliation. | `resp:focus:2026-05-08:abc123` | Used for correction/supersession tracking. |
| `spec_hash` | string | yes | Contract/spec hash binding envelope to governed schema/spec lineage. | `sha256:<64 hex>` | Guards against serving responses from mismatched contract baselines. |
| `version` | string | yes | Envelope version token. | `v1` | Used for compatibility and migration handling. |
| `issued_at` | string | yes | Emission timestamp (`date-time`). | `2026-05-08T21:20:00Z` | Supports freshness and replay controls. |
| `outcome` | string | yes | Finite runtime outcome. | enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Directly gates client behavior and messaging. |
| `reason_code` | string | yes | Primary reason classification for the outcome. | `insufficient_evidence` | Helps UI show denied/abstained rationale safely. |
| `evidence_refs` | array | yes | Evidence pointers supporting the envelope outcome. | array of `evidence_ref` objects | Enables cite-or-abstain rendering and traceability. |
| `policy_state` | string | yes | Governance state summary from policy evaluation. | `allow_with_obligations` | Governance-bearing state used by UI to show constrained results. |
| `freshness` | string | yes | Freshness/staleness status for the response payload. | `fresh`, `stale` | Governance-bearing state; stale signals caution or re-query expectations. |
| `correction_state` | string | yes | Correction/withdrawal posture for this response lineage. | `none`, `corrected`, `withdrawn` | Governance-bearing state; UI must reflect corrections/withdrawals. |

## 4. Invariants
- All required fields must be present (enforced by schema `required` — CONFIRMED).
- `spec_hash` must match `^sha256:[a-f0-9]{64}$` (enforced by schema pattern — CONFIRMED).
- `issued_at` must be `date-time` format (enforced by schema format — CONFIRMED).
- `outcome` must be one of `ANSWER | ABSTAIN | DENY | ERROR` (enforced by schema enum — CONFIRMED).
- PROPOSED: `evidence_refs` SHOULD be non-empty whenever `outcome == ANSWER`.
  - NEEDS VERIFICATION: enforce in `tools/validators/validate_runtime_response_envelope.py` or `policy/runtime/` follow-up.
- PROPOSED: `policy_state`, `freshness`, and `correction_state` values should be constrained to a controlled vocabulary.
  - NEEDS VERIFICATION: add enum constraints in future schema/ADR-aligned change if adopted.

## 5. Cross-references
- Sibling contracts: `contracts/runtime/decision_envelope.md`, `contracts/runtime/run_receipt.md`, `contracts/runtime/ai_receipt.md`.
- Schema file: `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`.
- Governing ADRs: `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`, `docs/adr/ADR-0002-contracts-vs-schemas-split.md`, `docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md`, `docs/adr/ADR-0020-abstain-is-a-first-class-decision.md`, `docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md`.
- Policy paths: `policy/runtime/` (PROPOSED — scaffold-level).
- Validator: `tools/validators/validate_runtime_response_envelope.py` (CONFIRMED — wired in `tools/validators/_common/run_all.py`).

## 6. Status
- Doc status: PROPOSED until reviewed and merged.
- Schema status: PROPOSED (from schema `x-kfm.status` — CONFIRMED).
- NEEDS VERIFICATION: confirm canonical vocabulary for `policy_state`, `freshness`, and `correction_state` before tightening shape.
