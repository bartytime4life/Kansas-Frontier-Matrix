# Archive search: query identity and recovery

This candidate targets the public Explorer composition at
`a0-hosted-ai-web-20261017`, with integration base
`d80a3e351a1c4e63caca08808df5e4ffcda80819` (merged welcome PR #5799).
The archive-search scope remains independent of that welcome change.

## Problem and resulting behavior

Previously, changing a newspaper search's form to Archive texts immediately
relabeled the old facets as text parts. Next then sent the edited query at the
old offset. A short response also advanced by 20 rather than its returned row
count, leaving unseen hits between pages.

1. **Search and edit.** Each accepted page keeps its submitted words, collection,
   year bounds and title filter together with the response. A results heading
   identifies that query. Editing the form displays an unapplied-changes notice;
   it does not relabel the old results or send a request. Search applies the form
   at the first page and clears its old title filter.
2. **Browse.** Next and Previous use the displayed page's submitted query.
   Next advances by the number of returned rows; Previous retraces actual page
   starts. Title facets use the same submitted query, including its original
   year range, even if the form has been edited. The final request is limited
   to the remaining hits within the stated 1,000-hit browsing boundary.
3. **Wait, cancel and retry.** Previous results remain explicitly labeled while
   a request is pending or fails. Cancel releases the form and returns focus to
   the words field. Retry last search repeats the failed request, not subsequent
   unsent edits, and also returns focus to that persistent field. A cancelled,
   superseded, timed-out or unmounted request cannot replace the results later.
4. **Correct input and inspect limits.** Reversed year ranges produce an inline
   alert before contacting the archive. Search status is polite and atomic;
   the result region has a name and busy state. Empty pages retain Previous
   where applicable and never announce an inverted range such as “Showing 1–0.”

This preserves query identity, not a database snapshot across page requests.
Archive editions and retained coverage can change between reads. OCR, original
source links, retrieval dates, count caps and missing-coverage limitations remain
attached. No source admission, provider activation or data migration is added.

## Verification

```bash
npm ci
npm run build
npx tsc --noEmit
node --test tests/archive-search-ui.test.mjs
node --test --test-concurrency=4 tests/*.test.mjs
```

Production build and TypeScript checks passed. The component suite has nine
passing regressions covering submitted-query labels and facets, short pages,
the 1,000-hit boundary, invalid years, cancellation/focus, retry, stale responses,
deep links, empty pages and timeout recovery. The full suite completed with
**2,816 passed, 25 existing skips and zero failures** (2,841 cases),
including the merged welcome regressions. The standalone archive-search pass
also completed with 2,810 passed, 25 skipped and zero failures.

Chromium checks at 1280×900, 390×900 and 320×900 exercised the hydrated library
with synthetic archive responses, partial pages, held requests and a service
outage. They verified query and facet labels, exact request offsets, Previous,
retry, cancellation/focus, validation, empty results and horizontal overflow.
Screenshots were inspected for desktop and phone readability. Captures and the
session's browser verifier are at `/workspace/scratch/kfm-library/`, outside
the application tree. These are interface fixtures, not retained observations
or scientific evidence; live archive coverage and screen-reader speech were
not verified.

## Scope and rollback

Implementation is confined to `app/data-library/search.tsx` and its existing
stylesheet. Regressions live in `tests/archive-search-ui.test.mjs`. Revert these
changes together to restore the earlier UI. No database, saved workspace or
deployment rollback is needed for this local candidate. Publication is separate.
