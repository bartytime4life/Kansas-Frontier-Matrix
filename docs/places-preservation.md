# Places: preserve saved stops and recover removals

This change uses the public Explorer composition at
`61c04d9196e7fb222e3f64f063fc48eb11970b65` on
`a0-hosted-ai-web-20261017`, including merged sharing PR #5803.

## Reviewed flow and resulting behavior

1. **Save a named investigation — limit now explicit.** Saving twelve places
   and then “Test place 13” replaced “Test place 01” without notice. The writer
   had silently sliced the list to twelve. The save handler and persistence
   boundary now reject over-capacity additions before writing, so the existing
   stops and entered name remain. Both save forms show the count and twelve-place
   limit, disable adding when full, and explain how to make room. The shared
   handler also protects save actions in research, Underground and inspection.
2. **Remove and recover — Undo added.** A successful removal offers Undo removal
   and focuses it in the originating control surface. Undo restores the same
   record at its original list position, preserving its source settings,
   redaction, report setup and saved timestamp. It returns focus to that
   surface's name field without moving the map or replacing a subsequently
   selected place. Failed writes retain the saved list and pending undo, with
   persistent feedback and the existing announcement.
3. **Continue and reopen — deliberate changes persist.** Undo applies to the
   latest removal in this tab. A successful addition or reorder ends that undo;
   a later removal replaces it, and reload ends it. The UI states this lifetime.
   After deliberately removing a stop, a new save uses that free slot. Reload
   restores the resulting list with the existing storage key and schema.

The shared controls give the optional name an explicit label and make Enter
submit the form. Save and undo controls are at least 44 px high. The Places
reorder/delete controls use 44×44 px targets below the place summary, keeping
the name readable in a narrow panel. The older saved-workspace control uses the
same form, limit, feedback and undo behavior. Hidden or other-surface controls
do not claim a focus request.

The maximum remains twelve. Existing camera redaction, provider-context
boundaries, time handling and observation refresh behavior remain unchanged.
Undo is transient UI state; saved-place records keep their existing format.

## Evidence and verification

The baseline was reproduced in a disposable hydrated Chromium page using
twelve actual save actions. Stored names changed from `12 … 01` to `13 … 02`
after the thirteenth save. Screenshots show the still-enabled Add place action
and its ordinary success message. No real user's saved places were edited.

The focused checks execute the actual page handlers and shared form. They
cover capacity rejection, preservation on storage failure, exact restoration
and order, retry, active-place behavior, undo lifetime, keyboard submission,
labeling and focus ownership. Browser journeys exercise both save surfaces,
Enter-to-save, a full list, removal, undo, denied writes, retry, deliberate
replacement and reload. Sharing regressions run alongside Places.

```bash
npm run build
npx tsc --noEmit
node --test tests/saved-place-sources.test.mjs tests/places-save-controls.test.mjs
node --test --test-concurrency=4 tests/*.test.mjs
KFM_TEST_CHROME=/path/to/chromium-wrapper \
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5202 \
node --test --test-concurrency=1 \
  --test-name-pattern='Places preserve|map sharing retains' \
  tests/explorer-startup.browser.mjs
```

Accepted captures and logs are outside the application tree in
`/workspace/scratch/kfm-places/`. Browser provider/API traffic is synthetic and
unavailable, and quota failures are intentionally injected on disposable pages.
These checks establish local editing behavior rather than provider coverage,
screen-reader speech or physical-device accessibility.

The production build and TypeScript passed. Sixteen focused checks passed,
including twelve added regressions. All six hydrated browser journeys passed:
Places at 1280×900, 390×844 and 568×320, plus the existing sharing journeys at
desktop, phone and short-landscape sizes. Additional checks opened Places at
768×1024, 320×640 and 844×390 and verified recovery, overflow and control sizes.
The input, Save and Undo controls were at least 44 px high, with 44×44 px list
actions. The page retains its 43 baseline lint warnings with matching signatures;
new component, model and focused tests have zero lint warnings or errors.
The final full suite completed with **2,856 passed, 25 existing skips and zero
failures** (2,881 cases). The rendered-HTML check retains its two existing lint
warnings and has zero lint errors.

An initial full run found an existing source assertion that required a static
class attribute. It now accepts the scoped Places style while retaining the
existing list class and accessible label. An extra resize-based check could not
find the open panel after entering the compact layout; the additional sizes were checked
by opening Places through their visible controls in fresh pages.

## Scope and rollback

Revert the Places handlers and control integration in `app/page.tsx`, the
addition to `places-trail.ts`, the shared save controls and scoped stylesheet
together. No database migration, stored-data conversion, hosting change or
publication is required for this candidate.
