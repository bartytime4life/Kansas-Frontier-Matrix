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

## Browser-contract repair candidate · 2026-10-22

Base: standalone composition `1000a5c4521bb3055e3863110754e924cdda801e`.
The exact-base [public-core run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39795910744/job/119883031548)
reports 23 startup-browser passes and 14 failures: three nested-dialog focus
cases and eleven geometry cases. Its build, type checking, ordinary Node suite,
HTTP boundary, county browser and aviation browser checks passed. These are
dated base results, not validation of this candidate or a deployed application.

Two distinct defects are addressed. The nested welcome dialog selected controls
by layout boxes alone. Chromium can retain boxes for descendants of closed
`details`; trying to focus such a button can leave focus on Close. The existing
modal helper now lists native Tab candidates, including summaries, and excludes
closed disclosure content, disabled or negative-tab-index controls, hidden/inert
ancestors and CSS-hidden elements. Controls below the scroll viewport remain
eligible so keyboard focus can reveal them. A notes-only dialog has only its
Close control; forward and reverse Tab both stay there.

The browser harness still expected eight native-footage cards, a River tile,
motion portals, a history footage timeline and a footer that the capability
welcome no longer renders. Its replacement derives ordered identities, titles,
facets and limitations from the existing seventeen-domain `TOPIC_STRUCTURE`.
It measures actual rows, overlaps, horizontal overflow, scroll reachability and
hit areas; uses native keyboard, pointer and touch input; and exercises current
details, source attribution, Return, Pause, Escape and toolbar exit controls.
Captured previews retain source clocks and scope; contextual reuse stays labeled,
and Sky/Evidence retain their missing-capture disclosure. No video-player or
domain-coverage claim is inferred from these fixtures.

The first fresh candidate browser run passed all three modal-focus cases and
all three topic-geometry cases. Its eight composition cases exposed an actual
attribution-layout conflict: the ordinary map theme's fixed 44-pixel compact
control extended above the welcome's reserved 24-pixel closed strip. The theme
also positioned its source text as an absolute popup. These failures identified
a conflict with the measured source boundary.

A welcome-scoped CSS correction removes that fixed size from the closed strip,
keeps the open strip at 48 pixels, and places its text inside the reserved row.
Desktop source text scrolls within its available height; phones retain the
existing horizontal source row. The ordinary map's button and popup rules are
unchanged. Two explicitly labeled fixture credit links now need positive text
geometry, containment inside the reserved strip and actual hit-test visibility
in both states. Their fixture labels establish no provider rights or accepted
data. Fresh composition execution passes all eight viewports.

The change stays in the existing UI helper, welcome component/style, regression
and documentation lanes described above. It changes no taxonomy, asset,
dependency, data binding or publication state. Rollback is a single candidate
revert; no storage migration or deployment is involved.

Local checks for this candidate:

- `node --check tests/explorer-startup.browser.mjs`: passed.
- `node --check tests/living-welcome.test.mjs`: passed.
- `node --test tests/modal-background.test.mjs tests/living-welcome.test.mjs tests/capability-preview.test.mjs`:
  all three files passed, with zero failures or skips.
- `git diff --check`: passed.

The helper regressions separately cover closed/nested disclosures, summary
descendants, hidden/disabled controls and retained controls outside the viewport.
The production build, TypeScript check and changed-source lint also pass. The
complete ordinary Node suite reports 1,643 passed, zero failed and 17 skipped
(1,660 tests reported).
After that build, the complete `tests/explorer-startup.browser.mjs` run passed
all 37 tests with zero failures or skips. It used Chrome 156.0.8078.47 and Node
22.13.1 against the built loopback Vinext production server with the committed
delivery middleware. The eight composition layouts include desktop, tablet,
320-pixel phone and a 640-by-360 layout at device scale factor 2. That scale
fixture does not establish native browser-zoom or device acceptance.
Independent read-only code review found no blocking focus or isolation regression;
that review did not run the tests or approve rendered fidelity.

The expanded Return and Pause controls retain their existing CSS minimum heights
of 36 and 40 pixels. The browser checks do not establish 44-pixel targets for
those controls or comprehensive accessibility conformance.

Screenshots, rendered fidelity, comprehensive accessibility acceptance and
exact-head hosted CI remain separate verification. This record does not
claim a rendered audit or replace the earlier blocked design-QA result.
