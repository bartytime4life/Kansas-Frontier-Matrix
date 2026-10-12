# Repository issue mutation intent fixtures

These fixtures exercise the inactive, fixture-only repository-control profile in
`contracts/governance/repository_issue_mutation_intent.md`.

- `cases.json` contains one closed base declaration plus bounded deep overrides.
  It covers all five receipt outcomes and the required stale-state, target,
  authority, replay, transport, and readback controls.
- `valid/valid_already_satisfied_no_op.json` is a fully rendered candidate.
- `invalid/` contains closed-schema controls for action chaining, ambiguous
  target identity, and an unsupported action.

`$CURRENT_INTENT_FINGERPRINT` is a fixture-builder token used only in replay
cases. The builder replaces it with the deterministic fingerprint of the
containing intent before schema validation.

Every example is synthetic. `DECLARED_GITHUB_API` models subject-side receipt
fields only; the validator performs no network call or external mutation.
