# Reveal session HUD and expiry teardown

Status: **fixture-first Explorer component; not production-wired**.

This feature adapts Pass 32 cards `KFM-P32-FEAT-0010`,
`KFM-P32-IDEA-0015`, and `KFM-P32-PROG-0019` into one bounded browser slice:

- show active reveal state, whole-second time remaining, fixed consent-scope
  labels, and an immediate revoke control;
- expire at the governed UTC deadline without a grace period;
- discard the controller-local opaque key reference before attempting caller
  effects;
- attempt overlay removal, obfuscated-state restoration, and audit
  finalization in order even when an earlier effect fails; and
- finish in a non-revealing `ABSTAIN` state with no re-open action.

## Projection boundary

The app-local adapter accepts only the profile
`kfm.explorer.reveal-session.public-safe.v1`. An active projection contains
bounded KFM references, four allowlisted scope codes, and a canonical UTC
interval no longer than 24 hours. Negative projections contain no layer,
scope, time, key-handle, audit, or policy-decision detail.

The projection never contains key bytes, bearer credentials, consent tokens,
DNA/genomic material, row-level data, exact sensitive geometry, or free-form
denial text. Unknown fields, contradictory outcomes, duplicate scopes, invalid
timestamps, and overlong TTLs fail closed.

## Teardown boundary

`createRevealSessionController` owns the timer and local key-handle reference.
On expiry, viewer revocation, or component destruction it:

1. clears the scheduled timer;
2. nulls its local key-handle reference;
3. requests `DISCARD_KEY_MATERIAL` through the caller-owned key store;
4. attempts `REMOVE_OVERLAY`;
5. attempts `RESTORE_OBFUSCATED_STATE`; and
6. attempts `FINALIZE_AUDIT` with a bounded event.

Every action is attempted. Missing or throwing caller wiring produces
`teardownStatus: INCOMPLETE`, but it cannot keep the HUD active or expose a
re-open control. `COMPLETE` means only that all four callbacks returned; it is
not cryptographic proof, audit-store confirmation, consent authority, release
approval, or publication authority.

## Placement and authority

- `apps/explorer-web/src/adapters/` owns the strict app-local projection.
- `apps/explorer-web/src/features/reveal_session/` owns browser lifecycle and
  accessible rendering.
- `fixtures/ui/reveal_session_projection/` owns synthetic examples.
- `apps/explorer-web/tests/` owns unit and browser proof.

These are existing responsibility roots under accepted ADR-0029 and Directory
Rules v2. This slice creates no contract, schema, policy, credential, key,
consent, audit, release, or proof authority.

## Production hold

Production wiring remains **HOLD** until a governed API projection, vetted key
store, overlay controller, obfuscation transition, and append-only audit sink
are separately reviewed. All four teardown callbacks are mandatory for a
production integration. The fixture component performs no network request and
does not activate a reveal session.

## Validation

The existing `ui-build` workflow runs the Explorer build, Vitest suite, and
headless Chromium suite. Focused commands are:

```text
pnpm --filter explorer-web exec vitest run tests/reveal-session.test.ts
pnpm --filter explorer-web exec playwright test --config=playwright.config.ts tests/browser/reveal-session.spec.ts
pnpm --filter explorer-web build
```

## Rollback

Revert the adapter, feature, synthetic fixtures, tests, source map, and authoring
receipt together. This fixture-first slice creates no external key, consent,
overlay, audit, release, deployment, or publication state to restore.
