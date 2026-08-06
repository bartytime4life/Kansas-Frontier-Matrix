# Conditional-write preflight fixtures

This fixture family exercises the proposed, inactive, fixture-only `ConditionalWritePreflightCandidate` profile.

The ten cases cover:

| Case family | Expected outcome | Purpose |
|---|---|---|
| create when absent | `PROPOSE_WRITE` | Models `If-None-Match: *` without emitting a request. |
| replace with matching ETag | `PROPOSE_WRITE` | Models `If-Match` when the observed target matches the declared precondition. |
| already-applied content | `NO_ACTION` | Suppresses a replay when the proposed content digest is already present. |
| create/replace concurrency drift | `CONFLICT` | Detects existing, absent, or stale target state without overwriting it. |
| incomplete policy/review/promotion/release closure | `HOLD` | Prevents a mutation proposal when upstream declarations are not complete. |

`valid/valid_propose_write.json` is the exact deterministic output for the create-if-absent case. `invalid/invalid_authority_overreach.json` intentionally sets `claims.published=true` and must fail JSON Schema validation.

All target references, ETags, digests, policy/review/promotion states, release references, and rollback references are synthetic. A passing fixture does not resolve external state, authenticate upstream records, emit a request, write bytes, change lifecycle state, release, deploy, publish, or authorize public use.
