# Give opened header menus the foreground

This change starts at public composition
`8529e3c664cf49789be01cebcd6f0781f5a2a13c`, including merged PR #5807.
The baseline server uses its identical source tree at `529dae0374`.

## Reviewed keyboard flow

1. **Open Time — healthy.** The clock opens its UTC settings and transport.
   Pointer dismissal and the controlling Time buttons already behave
   consistently after PR #5807.
2. **Open Map or More with the keyboard — overlap repaired.** Moving focus to
   either summary and pressing Enter opens its native menu without a pointer
   event. The baseline left Time above that menu. At 390 px, Map's Time action
   was covered by the exact-date input; More's Map action was covered by Time's
   header. Both menus were open but their actions failed pointer hit-testing.
3. **Enter, dismiss and return — ownership retained.** An opened header menu
   now dismisses Time and its expanded transport without scheduling a focus
   return. The summary keeps focus, Tab enters visible menu items, and Escape
   closes the menu and returns to its summary. Time can be reopened normally.
   Selecting Time from Map is not cancelled by the menu's later close event.

The Time component captures native `toggle` events while its surface is shown;
these events do not bubble. Only open `details.map-dock-menu` and
`details.header-overflow-menu` inside `.topbar` take ownership. Closed menus,
unrelated details and local Time source-clock disclosures do not dismiss Time.
The listener is removed on close/unmount. The existing outside-pointer path
uses the same dismissal function, preserving the second-click fix.

## Verification and evidence

The production build, TypeScript check and scoped lint pass. The focused
calendar, focus, menu and navigation suite passes 39 tests. The new component
checks cover both header menus, no competing focus return, transport-only mode,
capturing registration/cleanup and ignored local/closed/unrelated disclosures.
The full suite passes with 2,877 passed, 25 skipped and zero failures
(2,902 total).

Browser acceptance covers Map and More at 390×844, 768×1024 and 1280×900;
native keyboard opening; visible action hit-testing; Tab/Escape; unchanged
dates, URLs and page scroll; Time re-entry; transport-only dismissal; and local
Time disclosures. The four earlier mouse/touch toggle journeys are retained.
All 12 browser journeys pass: eight new menu-ownership cases and four existing
mouse/touch toggle cases.

```bash
npm run build
npx tsc --noEmit
npx eslint app/compact-time-sweep.tsx tests/calendar-playback.test.mjs \
  tests/explorer-startup.browser.mjs
node --test --test-concurrency=4 tests/*.test.mjs
KFM_TEST_CHROME=/path/to/chromium-wrapper \
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5213 \
node --test --test-concurrency=1 \
  --test-name-pattern='keyboard header|local Time details|Time pointer toggle|Time touch' \
  tests/explorer-startup.browser.mjs
```

Current-run screenshots and logs are outside the app tree at
`/workspace/scratch/kfm-menu-ownership/`. Baseline captures
`02-before-{map,more}-opened.png` show the covered menus; accepted settled phone
captures are `02-after-{map,more}-opened.png`. Additional browser captures are
under `acceptance/`. The settled audit captures wait for the map's startup
overlay to finish and were saved and inspected before acceptance.

Provider/API requests use isolated unavailability fixtures, explaining the
visible source notices and degraded basemap. These checks establish local
input, focus and layout behavior, not live coverage, physical-device behavior
or screen-reader speech. The event routing does not change dates or source
policy and does not introduce a new dismissal on ordinary focus departure.

## Rollback

Revert the native header-menu listener and shared dismissal function in
`app/compact-time-sweep.tsx`, with their regressions. No storage or data
migration is required.
