# policy_decision

> Status: PROPOSED
> Schema: https://schemas.kfm.local/contracts/v1/policy/policy_decision.schema.json
> Schema file: schemas/contracts/v1/policy/policy_decision.schema.json
> Validator: PROPOSED — not yet wired
> Authority: contracts/ owns meaning; schemas/contracts/v1/ owns shape (ADR-0001, ADR-0002).

## 1. Purpose
`policy_decision` records the canonical policy outcome for a single policy evaluation event. It answers what family decided, what outcome was reached, and what reasons/obligations apply at that decision point. It is not the runtime transport wrapper (`decision_envelope`) used to carry decision context through API responses.

## 2. Lifecycle role
Policy decisions are produced during promotion and runtime checks spanning WORK / QUARANTINE to PROCESSED and release gating into PUBLISHED. They are validated as contract objects before being relied on by governed API responses and release workflows. Supersession occurs by issuing a new decision record at a later `evaluated_at` point, not by mutating prior decisions.

## 3. Fields
| field | type | required | meaning | examples or enum | policy/sensitivity notes |
|---|---|---|---|---|---|
| `decision_id` | string | yes | Unique identifier for this decision event. | `poldec:2026-05-08:run-001:access` | Audit key for policy traceability. |
| `outcome` | string | yes | Finite decision outcome used by callers and envelopes. | enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Governs allow/deny/abstain behavior; ABSTAIN is first-class (ADR-0020). |
| `policy_family` | string | yes | Policy lane that produced the decision. | enum: `promotion`, `access`, `render`, `capability`, `consent`, `sensitivity` | Determines applicable obligation interpreter and reviewers. |
| `reasons` | array | yes | Machine/human-readable reason codes or explanations. | `['missing_citation']` | Drives transparency and challenge workflows. |
| `obligations` | array | yes | Conditions required if/when outcome permits further action. | `['redact_coordinates','attach_notice']` | Obligations can force restricted rendering rather than full deny. |
| `evaluated_at` | string | yes | Decision evaluation timestamp (`date-time`). | `2026-05-08T21:14:00Z` | Used for freshness/re-evaluation logic. |

## 4. Invariants
- All required fields must be present (enforced by schema `required` — CONFIRMED).
- `outcome` must be one of `ANSWER | ABSTAIN | DENY | ERROR` (enforced by schema `enum` — CONFIRMED).
- `policy_family` must be one of `promotion | access | render | capability | consent | sensitivity` (enforced by schema `enum` — CONFIRMED).
- `evaluated_at` must parse as `date-time` (enforced by schema `format` — CONFIRMED).
- PROPOSED: `reasons` SHOULD be non-empty for `DENY`, `ABSTAIN`, and `ERROR` outcomes.
  - NEEDS VERIFICATION: enforce in `policy/` decision logic or dedicated `validate_policy_decision.py` follow-up.
- PROPOSED: `policy_decision` remains canonical decision content, while `contracts/runtime/decision_envelope.md` wraps runtime transport metadata.
  - NEEDS VERIFICATION: verify full field mapping in `apps/governed-api/` adapter layer.

## 5. Cross-references
- Sibling contracts: `contracts/policy/policy_input_bundle.md`, `contracts/policy/sensitivity_label.md`.
- Runtime distinction: `contracts/runtime/decision_envelope.md`.
- Schema file: `schemas/contracts/v1/policy/policy_decision.schema.json`.
- Governing ADRs: `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`, `docs/adr/ADR-0002-contracts-vs-schemas-split.md`, `docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md`, `docs/adr/ADR-0020-abstain-is-a-first-class-decision.md`.
- Policy paths: `policy/` family lanes (PROPOSED — current repo policy files are scaffold-level).
- Validator: `tools/validators/validate_policy_decision.py` (PROPOSED — not wired in `tools/validators/_common/run_all.py`).

## 6. Status
- Doc status: PROPOSED until reviewed and merged.
- Schema status: PROPOSED (from schema `x-kfm.status` — CONFIRMED).
- NEEDS VERIFICATION: lock canonical mapping boundaries between `policy_decision` and runtime `decision_envelope` in validator/policy checks.
