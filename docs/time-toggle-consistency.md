# One Time transition per activation

This change starts at public composition
`38caa5502cf32663489b8181bd0e86e906025443`, including merged PR #5806.
The baseline server uses its identical source tree at `0d7e1c2734`.

## Reviewed interaction

1. **Open Time — healthy.** Clicking the desktop Time action opens the settings
   window and marks the action active. The baseline screenshot records this
   ordinary first activation at 1280×900.
2. **Click Time again — repaired.** The baseline document-level `pointerdown`
   listener dismissed Time before the header button's `click` handler ran.
   That handler then toggled the newly closed state back open. The second click
   therefore left the window open. The candidate lets that controlling button
   own its click transition, so the second click closes the settings once and
   leaves focus on the header action.
3. **Continue by keyboard or touch — healthy.** Enter opens and Space closes
   the same desktop settings. The clock still controls the whole transport,
   while its More button can hide settings and keep the transport available.
   Phone and tablet checks cover real touch input through the Map menu,
   outside dismissal, repeated entry, keyboard entry and Escape/clock return.

The desktop and Map-menu Time actions now declare their relationship to
`compact-time-settings`. Their expanded state reflects settings visible in Map,
including when another workspace or the guide owns the foreground. Pointer
events on these controllers, including their nested labels, bypass only the
outside-pointer dismissal. Other outside pointers still dismiss Time.

## Verification

- Production build and TypeScript checks pass.
- Scoped lint has zero errors or warnings. The existing page retains its same
  42 warnings and zero errors; no warnings were added or removed.
- Full suite: 2,874 passed, 25 skipped, zero failures (2,899 total).
- Focused calendar, focus and navigation checks: 32 passed.
- All 12 hydrated Chromium journeys pass: four mouse/touch toggle cases at
  1280, 1101, 390 and 768 px, plus eight responsive time-control regressions.

```bash
npm run build
npx tsc --noEmit
npx eslint app/compact-time-sweep.tsx tests/calendar-playback.test.mjs \
  tests/explorer-startup.browser.mjs
node --test --test-concurrency=4 tests/*.test.mjs
KFM_TEST_CHROME=/path/to/chromium-wrapper \
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5211 \
node --test --test-concurrency=1 \
  --test-name-pattern='Time pointer toggle|Time touch|responsive time control' \
  tests/explorer-startup.browser.mjs
```

Screenshots and logs are outside the app tree at
`/workspace/scratch/kfm-time-toggle/`. The numbered baseline captures show the
first click, unsuccessful second click and successful keyboard toggle; the
corresponding candidate captures show the corrected result. All accepted
captures were saved and inspected during this pass. Browser click targeting
waits for the time surface's finite transitions to settle.

Provider/API responses are isolated unavailability fixtures, explaining the
visible basemap/source notices. The checks establish local input, state and
focus behavior; they do not certify live provider coverage, physical-device
behavior or screen-reader speech. No date, range or source policy is changed.

## Rollback

Revert the controller exception in `app/compact-time-sweep.tsx` and the Time
action attributes in `app/page.tsx`, with their regressions. No storage or data
migration is required.
