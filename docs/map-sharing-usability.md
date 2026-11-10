# Map sharing: recovery, privacy and keyboard access

This change improves the Explorer on `a0-hosted-ai-web-20261017`, integrated
with `06be94e26d9a3c9bde18c2fae1a851a8cc1560d2` (merged draft-saving PR #5802).
It uses the existing map-state serializer and browser-history ownership rules.

## Flow audit and changes

1. **Open Share current view — clear entry.** The existing More menu exposes
   sharing beside the research workspaces. Its label and position remain.
   Activating it still attempts clipboard copying directly from the click.
   A dialog now retains the exact captured link and copy feedback.
2. **Recover from copying failure — fixed dead end.** In the baseline, denying
   both clipboard and history writes produced only a disappearing error asking
   the user to try another browser. There was no link field or retry. The new
   dialog selects the complete readonly URL, offers Select link and Copy link,
   and keeps manual-copy instructions visible after denial. A retry copies
   that same captured URL; late completions cannot overwrite newer feedback or
   update an unmounted dialog. Clipboard calls do not send the link to anyone.
3. **Review and return — keyboard behavior checked.** A native modal keeps
   background controls inactive. Tab and Shift+Tab wrap across its controls;
   map shortcuts do not act behind it. Escape, Done and the close button dismiss
   sharing and return focus to the visible More summary. The redaction notice
   follows the captured URL's privacy marker, including a restored private view.
   It explains the existing statewide-camera replacement and omitted analysis
   area. Other links do not show that notice.

The dialog explains that a link reopens captured map settings while source
availability and observations can change. It does not claim an immutable data
snapshot or a release of scientific evidence. URL serialization, privacy
redaction, source acquisition, draft storage and provider settings are unchanged.

## Evidence and checks

The baseline was reproduced in hydrated Chromium at 1280×900 against
`38d537f642fc2cbedfd099b457daf3f8cc60a716`. Accepted screenshots show the menu
entry and the failed-copy toast with no link field. An initial loading capture
was rejected and replaced after the map reached its bounded degraded state.
Browser source traffic was intentionally unavailable; this is a sharing-flow
test, not a provider-availability finding.

Local screenshots, audit notes and logs are retained outside the app tree at
`/workspace/scratch/kfm-share/`. Automated checks cover helper failures, visible
feedback, captured-URL identity, retry races, unmount cleanup, keyboard ownership,
focus wrapping and redaction disclosure. The existing Back/Forward journey also
closes sharing before continuing and checks that sharing preserves its entry.

The integrated production build, TypeScript and ten focused regressions passed.
The final full suite completed with **2,844 passed, 25 existing skips and zero
failures** (2,869 cases). New component and test files have zero lint warnings
or errors. The Explorer page retains the same 43 baseline warnings with matching
warning signatures; the rendered-HTML test retains its two existing warnings.
All eight final browser journeys passed: three draft persistence checks, three
sharing recovery checks, and two startup Back/Forward checks. Sharing and draft
checks used 1280×800, 390×844 and 568×320; navigation used desktop and phone.

Hydrated Chromium checks passed at 1280×900, 768×1024, 390×844, 320×640 and
844×390. They exercised public-link copy success, disclosure, scrolling,
overflow, 44 px targets, and retaining an edited report when Share closes.
Desktop, phone, and short-screen captures were inspected. The short-screen
dialog scrolls internally so its heading, link and actions remain reachable.

The first acceptance run exposed a native Tab boundary; a later run exposed
document-level map/report shortcuts acting before React's delegated handler.
The final component owns keyboard events at the dialog itself. The browser
journey now explicitly checks those boundaries and preserves background Layers
and Reports. Earlier failed attempts are retained in the session logs rather
than treated as passing evidence.

```bash
npm run build
npx tsc --noEmit
node --test tests/map-share-dialog.test.mjs
node --test --test-concurrency=4 tests/*.test.mjs
KFM_TEST_CHROME=/path/to/chromium-wrapper \
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5199 \
node --test --test-concurrency=1 \
  --test-name-pattern='map sharing retains|startup category supports browser Back' \
  tests/explorer-startup.browser.mjs
```

The dialog's controls have a minimum 44 px height and a visible focus outline.
Browser checks exercise pointer and keyboard flows, not screen-reader speech or
physical devices. No accessibility certification, public deployment or live
source coverage is established by these fixtures.

## Scope and rollback

Revert the `app/page.tsx` integration and the new `map-share-dialog.tsx` and
scoped stylesheet together. Tests cover that integration and the existing
history contract. No database, draft-schema or saved-data migration is needed.
