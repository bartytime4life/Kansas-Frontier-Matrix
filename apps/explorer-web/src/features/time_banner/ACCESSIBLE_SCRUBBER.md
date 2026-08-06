# Governed Accessible Time Scrubber

**Status:** PROPOSED implementation on a review branch  
**Owner root:** `apps/`  
**Public-release effect:** none

## Goal

Replace the Time Banner placeholder with a fixture-driven, single-handle time scrubber that is usable by mouse, touch, and keyboard while remaining subordinate to governed temporal state.

The source packet proposes Arrow-key second steps, Shift+Arrow minute steps, Home/End bounds, touch long-press timestamp details, copy support, explicit slider ARIA state, and a finite `{ t, source }` event. This slice implements those mechanics without creating a new time schema, policy decision, evidence contract, release path, or browser-side data source.

## Trust boundary

The module:

- accepts only a deliberately small app-local projection that is already `ANSWER / SUPPORTED`, `ALLOW`, `RELEASED`, `CURRENT`, UTC, second-precise, conflict-free, and in range;
- renders no slider for missing, malformed, abstained, denied, errored, held, stale, unreleased, policy-blocked, conflicted, or out-of-range state;
- treats selected time as interaction scope, never as evidence, source time, freshness truth, policy authority, or release authority;
- preserves an explicit `SELECTED_TIME`, `UTC`, `SECOND` label instead of collapsing time kinds into an unlabeled “current” value;
- emits only `{ t, source: "drag" | "key" | "touch" }` after user interaction;
- performs no network request and reads no RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, PUBLISHED, graph, vector, model-runtime, local-storage, or session-storage surface;
- uses DOM text nodes rather than HTML interpolation;
- exposes the full ISO timestamp through a keyboard button and touch long-press, with deterministic copy status.

This feature is not wired to a public map route in this slice.

## Input projection

```json
{
  "outcome": "ANSWER",
  "reason_code": "SUPPORTED",
  "time": {
    "minimum": "1850-06-01T00:00:00Z",
    "maximum": "1850-06-01T00:10:00Z",
    "selected": "1850-06-01T00:05:00Z",
    "kind": "SELECTED_TIME",
    "precision": "SECOND",
    "timezone": "UTC"
  },
  "trust_state": {
    "policy": "ALLOW",
    "release": "RELEASED",
    "freshness": "CURRENT",
    "temporal_conflict": false
  }
}
```

The parser is exact-key and fail-closed. This app-local shape is not a canonical KFM contract or schema; later route integration must adapt an accepted governed envelope into this bounded projection rather than make this module an authority surface.

## Interaction contract

- Arrow Left/Down: minus one second.
- Arrow Right/Up: plus one second.
- Shift+Arrow: plus or minus one minute.
- Home/End: minimum or maximum.
- Touch long-press: open exact timestamp details.
- Keyboard-accessible “Show exact timestamp” button: open the same details.
- Escape: close details.
- Copy: use an injected copy boundary, Clipboard API when available, or a hidden-textarea fallback.
- Slider ARIA: `role="slider"`, `aria-valuemin`, `aria-valuemax`, `aria-valuenow`, and UTC `aria-valuetext`.

## Files

- `index.tsx` — strict resolver and DOM controller.
- `../../../../../../fixtures/ui/time_scrubber_projection/` — synthetic positive, negative, conflict, and malformed projections.
- `../../../tests/time-banner.test.ts` — finite-state, parsing, trust-gate, no-leak, and no-network unit tests.
- `../../../tests/browser/time-banner.*` — keyboard, drag/touch source, long-press, copy, Escape, and negative-state browser tests.

## Directory Rules basis

`apps/explorer-web/src/features/time_banner/` already owns app-local Time Banner behavior. App-local tests remain under `apps/explorer-web/tests/`; reusable synthetic fixtures remain under `fixtures/ui/`; generated authoring provenance remains under `data/receipts/generated/`. No root, lifecycle phase, authority family, contract home, schema home, policy home, release home, or compatibility home is created or moved.

## Validation

```bash
cd apps/explorer-web
pnpm run build
pnpm run test:unit
pnpm run test:browser
```

The implementation is also suitable for isolated strict TypeScript compilation and deterministic source scans. Unit and browser tests use synthetic fixtures only and require no live source, map server, governed API, or model runtime.

## Rollback

Revert the feature commit. The change is additive except for replacing the one-line placeholder, and it is not wired into a released route, so rollback requires no data migration, cache invalidation, release withdrawal, source correction, or publication correction.
