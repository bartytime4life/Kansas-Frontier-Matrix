# Denial reason explorer

Status: **fixture-first Explorer component; not production-wired**.

This feature adapts Pass 32 card `KFM-P32-FEAT-0017` into a read-only release
review surface for four source-named denial families:

- `MISSING_RECEIPT`;
- `ZOOM_TOO_FINE`;
- `LOW_COUNT_CELL`; and
- `INVALID_ATTESTATION`.

Each code maps to fixed public-safe title, category, explanation, and next-step
copy. The component never reflects upstream prose, counts, thresholds,
coordinates, sensitivity facts, attestation diagnostics, credential material,
or override instructions.

## Projection boundary

The app-local profile `kfm.explorer.denial-reason.public-safe.v1` accepts only:

- a bounded review identifier;
- the finite `DENY` outcome;
- one to four unique allowlisted reason codes;
- digest-bound release-candidate and PolicyDecision references; and
- a canonical whole-second UTC evaluation time.

Unknown fields, unknown or duplicate reasons, mutable references, empty reason
sets, non-`DENY` outcomes, and invalid timestamps fail closed to fixed `ERROR`
copy with no review detail.

## Authority boundary

The explorer is a projection consumer. It does not evaluate policy, validate a
receipt or attestation, calculate a disclosure threshold, approve a zoom,
change a PolicyDecision, mutate a release candidate, create an override, or
publish an artifact. It performs no network or lifecycle-store access.

The view exposes no button, link, or callback that can override `DENY`. The
suggested next steps only route work back through governed build or review
paths.

## Placement

- `apps/explorer-web/src/adapters/` owns strict app-local parsing.
- `apps/explorer-web/src/features/denial_reason_explorer/` owns fixed display
  behavior.
- `fixtures/ui/denial_reason_projection/` owns synthetic examples.
- `apps/explorer-web/tests/` owns unit and browser proof.

These are established responsibility roots under accepted ADR-0029 and
Directory Rules v2. No parallel policy, reason registry, release, receipt,
attestation, schema, or contract authority is created.

## Production hold

Production wiring remains **HOLD** until a reviewed governed API emits this
exact public-safe projection from an accepted PolicyDecision/release-review
boundary. The browser must not ingest canonical policy engine output or
steward-only explanations directly.

## Validation

The existing `ui-build` workflow runs the Explorer build, unit suite, and
headless-browser suite. Focused commands are:

```text
pnpm --filter explorer-web exec vitest run tests/denial-reason-explorer.test.ts
pnpm --filter explorer-web exec playwright test --config=playwright.config.ts tests/browser/denial-reason-explorer.spec.ts
pnpm --filter explorer-web build
```

## Rollback

Revert the adapter, feature, fixtures, tests, source map, and authoring receipt
together. This read-only slice creates no policy, review, release, deployment,
or publication state to restore.
