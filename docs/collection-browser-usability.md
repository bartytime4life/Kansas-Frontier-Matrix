# Collection browser: discovery, context and focus

This candidate improves the Explorer's existing data-library collection browser
on `a0-hosted-ai-web-20261017`, integration base
`b2ac5ef80e644c1b95650da5e815c45c01090f16` (merged archive-search PR #5800).
It retains the existing catalog, record reader and map-layer handoff.

## Observable changes

1. **Find a collection.** Words match in any order across collection titles,
   source identities and field names. For example, `KGS API number` and
   `number API KGS` find collections whose metadata includes those terms.
   Case, accents and punctuation are normalized. This searches catalog
   metadata, not record values or scientific evidence. Source order is retained.
2. **Narrow or recover.** With map geometry filters on the catalog's existing
   geometry field. The live count says how many of all 189 collections match;
   it does not certify retained coverage or current service availability. Empty
   searches show an explanation and Show all collections. Clear and recovery
   reset both filters, preserve the chosen collection and map selection, and
   return focus to the finder.
3. **Choose and return.** A deliberate choice focuses and scrolls to the committed
   collection heading, including when choosing the same collection again.
   Back to collection finder restores the input. Filtering, freshness updates
   and record completion do not redirect focus. Choosing metadata still requires
   an explicit Read first page to retrieve collection records.
4. **Keep the search context.** Choosing a collection preserves the text query,
   source, year bounds, unrelated URL parameters, hash fragment and router history
   state. Collection filters are bookmarkable as `find` and `mapped=1`; clearing
   them also clears those parameters. Reload restores filters and the chosen
   collection without automatically reading its records. A browser that refuses
   history updates can still browse and read collections.
5. **Keep records uncovered.** The selected-map summary sits in document flow
   above the collection browser. Its existing explanation, map action and Clear
   control remain. The chosen collection also offers Open selected map when a
   selection exists. The earlier fixed summary could cover the reading controls
   on phones and short landscape screens. Map selection stays in this tab's
   memory; its map link carries the chosen collection identities.

No catalog rows, stored data, provider configuration, access rules or release
state change. Geometry is a metadata property; availability is checked on read.

## Local validation

```bash
npm ci
npm run build
npx tsc --noEmit
node --test tests/collection-browser.test.mjs
node --test --test-concurrency=4 tests/*.test.mjs
```

The integrated production build and TypeScript check passed. Nine new model and
component regressions passed. The final full suite completed with **2,825 passed,
25 existing skips and zero failures** (2,850 cases), including both earlier
Explorer improvement PRs. An earlier run overlapped a rebuild and saw a server
startup exit; the completed-build integration run passed that same startup test.

Hydrated Chromium checks passed at 1280×900, 768×1024, 390×844, 320×740 and
844×390. They exercised matching, geometry filtering, empty recovery, heading
focus and return, URL/history preservation, reload restoration, map-selection
retention and explicit record reads. They also checked overflow, the checkbox
label's 44 px target, and that map selection does not cover the reading control.
Desktop, phone and short-screen screenshots were inspected. Captures and the
session verifier are retained at `/workspace/scratch/kfm-collections/` outside
the application tree.

The browser run used the actual catalog with synthetic record transport and an
unavailable archive service. It establishes interface behavior, not live PC
coverage, scientific validity, screen-reader speech or an accessibility certification.

## Scope and rollback

Implementation lives in `app/data-library/page.tsx`, `collection-browser.ts`
and `collection-browser.module.css`; regressions live in
`tests/collection-browser.test.mjs`. Revert the page changes and new helper,
stylesheet and regressions together. No database migration or saved-data
rollback is needed. Publication remains separate.
