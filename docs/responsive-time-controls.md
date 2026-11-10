# Keep keyboard context in the time toolbar

This change starts at public composition
`b424173183a79dfe8c2692e66bed4111eff104bb`, including merged PR #5805.
That merge has the same tree as `f79d7b8a31`, used for the baseline browser server.

## Reviewed flow

1. **Open Time and focus a date part — healthy on desktop.** The existing clock
   opens the time window, with explicit UTC dates, source limits and keyboard
   focus styling. The baseline capture at 1280×900 shows Month focused.
2. **Narrow the toolbar — focus loss repaired.** Container styles replace the
   Year/Month/Day selectors with “Choose map date” below 420 px. The baseline
   390×844 capture and DOM check showed focus on the document body, even though
   the date and open time window remained. Focus now moves to the visible date
   button. Frame-step, scrubber and Compare controls that disappear below
   760 px hand focus to the visible time-settings button.
3. **Expand or leave — keyboard ownership retained.** Expanding restores the
   original date part when it is available. A toolbar first opened on a phone
   falls back to Year on desktop. Deliberate outside focus or pointer actions,
   a hidden time surface and a hidden document prevent focus recovery. Escape
   still closes Time and returns to the clock. Visible controls retain focus.

The observer watches the actual timeline container, so container queries work
even when the browser window does not resize. Window resize is also observed.
The controller coalesces focus work into one animation frame and cancels pending
work, observers and listeners when Time closes or unmounts. It only focuses
existing controls; it does not change date, range, playback or source state.

## Evidence and verification

The production build and TypeScript checks pass. Scoped lint has zero errors
and warnings. The full suite passes with 2,871 passed and 25 skipped (2,896 total);
the focused calendar/focus checks pass 18 tests.
All 14 hydrated Chromium journeys pass: eight time-control cases and the six
existing responsive work-area/dialog cases.

Current-run screenshots and logs are outside the application tree in
`/workspace/scratch/kfm-time/`:

| Step | Baseline | Candidate |
| --- | --- | --- |
| Desktop Month | `01-before-month.png` | `03-after-month.png` |
| Phone replacement | `02-before-focus-lost.png` | `04-after-phone-focus.png` |
| Return to desktop | — | `05-after-month-restored.png` |

The captures were saved and inspected. Provider requests use isolated
unavailability fixtures, which explain the visible basemap/source notices. The
checks establish local focus and layout behavior, not live provider coverage or
screen-reader speech behavior. No calendar data or source eligibility is changed.

```bash
npm run build
npx tsc --noEmit
npx eslint app/time-controls-focus.ts app/compact-time-sweep.tsx \
  tests/time-controls-focus.test.mjs tests/calendar-playback.test.mjs \
  tests/explorer-startup.browser.mjs
node --test tests/time-controls-focus.test.mjs \
  tests/calendar-playback.test.mjs tests/calendar-sweep.test.mjs
node --test --test-concurrency=4 tests/*.test.mjs
KFM_TEST_CHROME=/path/to/chromium-wrapper \
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5209 \
node --test --test-concurrency=1 \
  --test-name-pattern='responsive time control|responsive work area|responsive layer sheet' \
  tests/explorer-startup.browser.mjs
```

The new unit checks cover date-part round trips, default Year fallback, hidden
transport controls, explicit focus/pointer ownership, container-only changes,
coalescing, cleanup and hidden/disconnected surfaces. Browser journeys check
all three date parts, Previous, Compare and the scrubber, plus intentional map
focus and an isolated container-width change without a window resize. The prior
six responsive work-area/dialog journeys are retained in the acceptance run.

## Rollback

Revert `app/time-controls-focus.ts`, its effect/import in
`app/compact-time-sweep.tsx` and their regressions. No storage migration or saved
data recovery is required.
