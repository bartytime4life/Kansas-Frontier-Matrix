# Identity and Time Semantics

## Identity

Each entity type MUST define:

- Canonical identifier shape
- De-duplication/equivalence rules
- Merge/split behavior over time

## Time

Entity and event documents SHOULD distinguish:

- Event time
- Valid time
- Transaction/processing time

When time is ambiguous, policy and evidence checks MUST fail closed.
