# Capability welcome acceptance · 2026-10-21

Final design-QA result: **BLOCKED**. No rendered-candidate fidelity or browser
interaction pass is claimed. Baseline: the current public Explorer welcome was
inspected in Chrome, including its eight footage-backed topic tiles. Requested
target: borderless ten-second hourglass and software-capability animations with
expanded categories. The generated hourglass strip was visually inspected as
an asset; it is not a rendered-control acceptance capture.

## Executed engineering checks

- Production build: passed, with browser-asset staging completed.
- TypeScript `--noEmit --incremental false`: passed.
- Changed component lint: zero errors and zero warnings.
- Direct Node changed-area checks: 31 passed, zero failed/skipped: welcome (15),
  capability/asset integrity (4), playback lifecycle (6), preserved demo contracts (6).
- All 16 WebP animations were decoded with Pillow. Optimized frame counts vary
  from 53 to 61 (duplicate frames combine); each retains exactly 7,000 ms.
- Source and delivered-image hashes are checked in the regression suite.
- `git diff --check`: passed.
- Whole-suite attempt: incomplete; no aggregate suite pass is claimed. The
  sandbox's network/listener restrictions prevent the production preview from
  listening (`EPERM` on `0.0.0.0:4187`). Two HTTP files explicitly report
  loopback-listener EPERM (`build-identity-http`, `godaddy-node-runtime`).
  `build-identity` and `daily-archive` each fail one launcher assertion because
  expected subprocess output is empty; both failures were reproduced on the
  unchanged, tree-verified base. The attempt has no final aggregate result;
  other whole-suite outcomes remain unverified.

## Required browser acceptance before readiness

At desktop, 390-pixel and 320-pixel widths, inspect all category rows, scrolling,
text contrast, source captions, detail choices, keyboard focus, touch selection,
Return/Pause/Escape in expanded viewing, the exact ten-second sand drain and
flip continuity, reduced motion and hidden-tab resumption. Capture the current
candidate with the matching reference viewport and compare full and focused
surfaces. Inspect network/console failures and verify no legacy footage/video
player is mounted by the welcome. No rendered screenshots exist for this
candidate because its preview listener was denied.

## Open scope

Sky and Evidence have real workspace destinations but no verified animation.
Context-only reused captures remain labeled; they are not domain coverage.
Independent review and exact-head hosted checks remain pending. No merge,
deployment, publication, source admission, database or home-PC change occurs.
Rollback is one candidate-commit revert with no migration.
