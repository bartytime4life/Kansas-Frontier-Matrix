# Keep the current work area through layout changes

This improvement uses the public Explorer composition at
`253b1528aa29b11e790f946a2e52c4774b1fafeb` on
`a0-hosted-ai-web-20261017`, including merged Places PR #5804.

## Reviewed flow and behavior

1. **Edit on desktop — existing entry retained.** Open Places and enter
   “Pending prairie investigation,” with characters 8–15 selected. The old
   1,100 px media-query handler unconditionally closed Places, evidence and the
   timeline when the viewport narrowed. The stored input value remained, but
   the panel disappeared and keyboard focus moved to the document body.
2. **Narrow or rotate — current work area retained.** The focused open work area
   now wins over the fallback stacking order when entering the compact layout.
   Competing panes close so they cannot install competing focus owners. The
   fallback order is map tools, chat, evidence, left navigation, then time.
   The listener uses the latest open state. It does not repeatedly dismiss
   panels during ordinary compact-layout interactions, and expanding does not
   reopen panes that were closed for the narrow layout.
3. **Continue and return — focus stays usable.** A visible focused control keeps
   its DOM identity and selection instead of being replaced by the first panel
   button. If compact styling hides the inspector's Close button, its visible
   fallback receives focus inside the same inspector. Retained controls are
   revealed by scrolling only their panel's scroll containers, including on
   height-only resizes. Scheduled reveals are coalesced and cancelled when focus
   changes or the listener is removed. The nonmodal layer sheet leaves map
   canvas focus alone. Expanding releases the compact modal background holds.

The visual review also found a closed Layers sheet painting over the retained
tools form in short landscape layouts. Those styles anchor Layers on the right,
so its closed leftward transform can still end inside the viewport. The sheet is
now explicitly invisible while `aria-hidden="true"`; its layout, scroll position
and saved setup remain mounted. The browser assertion checks painted viewport
intersection as well as hit-testing, because an `inert` opaque sheet can cover a
control while allowing hit-testing to reach it.

A separate foreground dialog or Reports/Stories workspace keeps ownership;
background map panels cannot become modal over it. Normal panel entry, Escape,
source inspection and explicit navigation continue to use their existing paths.

## Chat request lifetime

The assistant's `active=false` contract cancels a running request. A resize that
hides a competing chat pane now records a layout suspension rather than invoking
that close/cancel lifecycle. Its active binding remains true while Map is active.
Reopening clears suspension without an inactive intermediate state. Explicit
Close and leaving Map deactivate the assistant as before. Existing context and
source-policy invalidation still apply; this does not resubmit a question or
override request eligibility.

The lifecycle regression executes the actual page transition, close callback and
assistant active binding. Existing assistant tests check the inactive cancellation
contract. Browser resize checks use an unsent question, so they do not attest to
a real model request surviving a live provider or context change.

## Verification and evidence limits

The baseline was reproduced in hydrated Chromium at 1280×900 → 768×1024. The
candidate journeys cross 1,101/1,100 px and continue through 768×1024, 390×844,
320×640, 844×390 and back to 1280×900. They check retained controls, values,
selection, visibility, overflow, competing-pane closure and page scroll position.
Separate checks cover a desktop-only control disappearing, map canvas focus,
foreground sharing, report editing and the existing Places persistence flows.

Local results on the final production build:

- Build and TypeScript checks passed.
- Full test suite: 2,865 passed, 25 skipped, zero failures (2,890 total).
- Nine targeted Chromium journeys passed: five retained work areas, the
  Layers/share/report flow, and three Places persistence/recovery sizes.
- Scoped lint passed with zero errors or warnings. The existing large page has
  42 warnings and zero errors, down from 43 baseline warnings; none were added.

The Places regression now waits for the prior panel's deferred close handoff
and the utility's entry focus before editing, matching the real interaction.
Resize captures wait for surface transitions to settle before geometry checks.

```bash
npm run build
npx tsc --noEmit
node --test tests/compact-panels.test.mjs tests/modal-background.test.mjs \
  tests/scene-surface-integration.test.mjs tests/header-focus.test.mjs \
  tests/workspace-map-navigation.test.mjs tests/workspace-drafts.test.mjs \
  tests/assistant-status.test.mjs
node --test --test-concurrency=4 tests/*.test.mjs
KFM_TEST_CHROME=/path/to/chromium-wrapper \
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5207 \
node --test --test-concurrency=1 \
  --test-name-pattern='responsive work area|responsive layer sheet|Places preserve' \
  tests/explorer-startup.browser.mjs
```

Captures and logs are retained outside the app tree at
`/workspace/scratch/kfm-responsive/`. Baseline captures are `01-before-editing.png`
and `02-before-closed.png`; settled candidate captures use
`final-acceptance/resize-{places,chat,tools,time,evidence}-{width}x{height}.png`.
Each resize capture has a companion JSON geometry record. The pre-fix landscape
overlap is retained in `geometry-acceptance/resize-tools-844x390.{png,json}`.
Provider/API responses are isolated
unavailability fixtures. No real question is sent, clipboard written, provider
coverage certified or public deployment performed. These are emulated browser
checks, not physical-device or screen-reader speech certification.

## Scope and rollback

Revert the responsive controller and assistant lifecycle binding in `app/page.tsx`,
the closed-sheet visibility rule in `app/globals.css`, and
`app/compact-panels.ts` with their regressions. Existing focus fixtures gained
the DOM containment and state-setter behavior needed by the retained-control
checks. Storage schemas, source serialization and saved drafts are unchanged;
no data or database migration is needed.
