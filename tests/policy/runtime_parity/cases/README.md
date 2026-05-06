# Runtime parity case index

This directory documents the executable case set used by `test_runtime_parity.py`.

## Case set

- `answer_public_safe`
- `abstain_missing_evidence`
- `deny_unresolved_rights`
- `error_schema_fault`

Each case has:

1. A policy-facing fixture in `../fixtures/*.input.json`.
2. An expected runtime envelope fragment in `../expected/*.runtime_response.json`.
3. Assertions in `../test_runtime_parity.py` that enforce finite outcomes and reason/obligation parity.
