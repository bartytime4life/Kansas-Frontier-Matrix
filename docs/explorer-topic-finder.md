# Explorer topic discovery

This local candidate improves the existing welcome topic chooser, based on
`a0-hosted-ai-web-20261017` at `ca58af6a6282c7cbb3ac9026714e2fd8106b749e`.
It preserves the atlas, tablet grid and phone carousel rather than replacing
their layouts.

## What changed

1. **Find a topic.** Search words can appear in any order across a topic's
   title, description, facets, group and map name. Case, accents and punctuation
   are normalized. All words must match; the selected group narrows the results.
   For example, both `river network` and `network river` find Water & watersheds.
   This searches navigation metadata, not provider records or data availability.
2. **Preview a result.** When the current preview is filtered out, the first
   matching topic supplies the backdrop and chosen-map panel. No map is opened
   and no combined-map selection is changed. Full-screen previews retain their
   separate category navigation. Empty results hide the unrelated chosen-map panel.
3. **See and clear filters.** An active result count remains visible on the
   closed finder, with a separate Clear action. Visible field labels and live
   result and selection messages support orientation. Native selects and
   disclosures have explicit keyboard focus indicators and 44 px targets.
4. **Recover.** Empty results show their recovery action immediately before
   the unrelated record links. On phones the message and Show all topics action
   fit the existing 96 px card area. Clearing restores all topics and groups,
   retains combined-map choices, and returns focus to the filter input or the
   closed finder's summary. Escape first closes an open finder or Options menu
   and returns focus to its summary; a later Escape retains normal welcome behavior.

Implementation: `app/living-welcome/topic-search.mjs`, `welcome.jsx` and `welcome.css`.
Regressions: `tests/topic-search.test.mjs` and `tests/living-welcome.test.mjs`.

## Local verification

```bash
npm ci
npm run build
npx tsc --noEmit
node --test tests/topic-search.test.mjs tests/living-welcome.test.mjs
node --test --test-concurrency=4 tests/*.test.mjs
PORT=5187 npm start
```

The full Node suite completed with **2,807 passed, 25 skipped, zero failed**
(2,832 cases). Skips retain the suite's existing environment and source-parity
boundaries. Production build and TypeScript checks also completed successfully.

Chromium interaction checks covered 1440×900, 1280×800, 768×1024, 390×844,
320×740 and 844×390: filter matching, preview alignment, selection preservation,
Escape and focus return, Clear, empty-result recovery and horizontal overflow.
The run used reduced motion, isolated provider transport and unavailable API
responses. Screenshots were inspected separately, including the recovery button's
placement within the phone card area. These checks do not establish live map
coverage, scientific validity, screen-reader speech or full accessibility compliance.

The local run's captures and verification script are retained outside the source
tree at `/workspace/scratch/kfm-ux/`. They are UI test evidence, not provider data.
Open-PR overlap could not be independently checked: the GitHub CLI request was
denied with HTTP 403. This candidate has not been merged, published or deployed.

## Rollback

Revert this candidate's welcome changes and remove its new search helper and
regressions together. No stored workspaces, source datasets, database schemas,
provider configuration or persisted user preferences are migrated.
