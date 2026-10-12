# Conditional-write attempt receipt fixtures

This family exercises the proposed, inactive `ConditionalWriteAttemptReceiptCandidate`.

`cases.json` contains ten deterministic source-preflight and attempt-transcript cases covering applied declarations, idempotent no-action, preflight conflict/hold, HTTP precondition failure, transport error, omitted attempts, header mismatch, and inconsistent response state.

`valid/valid_applied.json` is the exact generated `create_applied` record. `invalid/invalid_authority_overreach.json` changes only `claims.published` to `true` and must fail JSON Schema. Its sidecar gives the repository-wide schema-fixture test the exact expected field and keyword.

All targets, identifiers, headers, response codes, digests, and states are synthetic. Passing fixtures authenticate no external request, target state, write, lifecycle transition, release, publication, or public use.
