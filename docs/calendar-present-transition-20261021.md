# Calendar exit and source identity

The hosted branch at `64a9db8f700406baec6f108f0759d33a2eb0e723`
retained dated-source payloads and archive-day locks when the advanced Present
button or another annual control cleared the calendar. In particular, a date
in the build's present year did not change the annual frame, so the current
source hydration effect did not run. A pending archive request could still
commit after the calendar disappeared. The compact Present control had its own
cleanup, which did not retire hidden archive sources or same-day pending-load
memoization.

The shared annual commit now aborts and forgets dated acquisitions, removes
archive-day identity and both archive/display payloads, clears their map
sources, and retires a selected record from those feeds. It retains unrelated
selected places, layer choices, source clocks and provider payloads from other
feeds. Calendar-internal commits retain their dated identity. Present hydration
observes calendar and archive identity changes as well as the annual frame;
loading or failure cannot carry an archived payload forward. Annual playback
uses the same transition. Earlier annual frames continue to hold current
sources. The compact Present action delegates to this shared path.

The adjacent compact skip-empty playback regression is bounded to stopping
play intent when no unchecked/nonempty next frame remains. It does not change
source availability, empty-response meaning or automatic layer selection.

## Verification

`tests/calendar-transition.test.mjs` executes the actual production callbacks
with controlled source reads, including abort-insensitive late responses,
repeat same-day transitions, unavailable current responses, hidden archives,
selection retirement and unrelated selected-place preservation.
`tests/calendar-playback.test.mjs` executes the component hooks and rendered
controls for exhausted skip-empty playback. These tests failed before the
corresponding changes. They are state/component evidence, not live-map QA.

`tests/calendar-transition.browser.mjs` is explicit hydrated loopback acceptance
for advanced Present, compact Present, annual stepping and repeated entry/exit.
It uses a local earthquake fixture, blocks off-origin requests and holds the
current response while checking archive identity retirement. Playwright must
be available to Node (for example through NODE_PATH), with Chromium supplied
by KFM_TEST_CHROME. Run against a built local server with KFM_NODE_TEST_ORIGIN;
the default is http://127.0.0.1:5182. It does not verify real provider coverage,
live hosted publication, or scientific correctness of fixture geometry.

Run the build, `npx tsc --noEmit`, `node --test --test-concurrency=4
tests/*.test.mjs`, and the explicit browser suite after committing the final
revision. `/api/build` must match that clean revision and its application-input
digest. The PR records exact outcomes and any inherited broad-suite failures.

No source admission, persisted data, auth, free-export rules, original Sites
bindings, home-PC configuration or deployment is changed. Rollback is a source
revert; no data migration applies. Deployment and runtime activation require a
separate decision.
