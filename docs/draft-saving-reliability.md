# Report and story draft saving

This improvement uses the public Explorer composition on
`a0-hosted-ai-web-20261017`, integration base
`38d537f642fc2cbedfd099b457daf3f8cc60a716` (merged collection-browser PR #5801).

## Reproduced loss and resulting behavior

The story Guiding question accepted 25,027 characters and autosave reported
“Saved on this device.” Returning to the map and reopening Stories restored
the default question: the existing restore validator rejected text over
24,000 characters. Saving also did not enforce the reader's 2,000,000-character
serialized payload ceiling.

The writer now validates the serialized value with the same validator and
size ceiling used for reopening. It replaces the previous saved copy only
after those checks pass. Invalid, oversized and browser-denied writes report
distinct failures, retain the pending draft, and keep existing exports usable.
The Guiding question enforces the shared 24,000-character limit in both the
textarea and its update handler. Existing restore and privacy checks remain.

Reports and Stories each offer Save now and Ctrl+S / ⌘S. The shortcut applies
only inside the active workspace; it leaves the assistant, other page scopes,
composition and modified shortcuts alone. Saving flushes the latest committed
edit. The 300 ms autosave, hidden-page/pagehide and unmount flushes remain.
Save feedback is visible on narrow screens, with a 44 px save/retry control.

Drafts remain device-local and unpublished. A successful write does not protect
against later browser-data clearing, storage eviction, another tab overwriting
the same key, or a future incompatible schema. Exports remain the portable copy.
This change does not recover a draft that was already replaced after a rejected
restore, or add cross-device synchronization.

## Verification

```bash
npm run build
npx tsc --noEmit
node --test tests/workspace-drafts.test.mjs tests/snapshot-workflows.test.mjs
node --test --test-concurrency=4 tests/*.test.mjs
KFM_TEST_CHROME=/path/to/chromium-wrapper \
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5196 \
node --test --test-concurrency=1 --test-name-pattern='draft workspaces preserve' \
  tests/explorer-startup.browser.mjs
```

The focused suite has 23 passing tests, including nine added regressions for
write/read compatibility, size and serialization failures, preservation of the
previous saved copy, immediate saves, shortcut scope, lifecycle timing and the
question limit. The browser journey now checks long-question reopening and
visible storage failures at its desktop, phone and short-landscape sizes.
The full suite passed with **2,834 passed, 25 existing skips and zero failures**
(2,859 cases). All three draft browser journeys passed at 1280×800, 390×844 and
568×320. TypeScript and the production build passed. Scoped lint had zero errors
and the existing report-preview `<img>` warning.

Additional hydrated Chromium checks exercised long-question reopening, storage
failure/retry, report/story isolation, both shortcut modifiers and Save now
before the debounce. Responsive checks used 1280×900, 768×1024, 390×844,
320×640 and 844×390. Screenshots and session logs are outside the app tree in
`/workspace/scratch/kfm-drafts/`.

Browser provider/API traffic was replaced with synthetic unavailability
responses. These checks establish local editing behavior, not live source
coverage, scientific validity, screen-reader speech or physical-device testing.
No publication, hosting change, source admission or database migration occurs.

## Scope and rollback

The change is confined to `app/report-story-workspaces.tsx`,
`app/workspace-storage.ts`, the scoped save-status stylesheet and their tests.
Revert those changes together to restore the previous behavior. Storage keys
and draft schema are unchanged; existing compatible drafts remain readable.
