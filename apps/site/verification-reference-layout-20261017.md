# Explorer reference layout verification — October 17, 2026

This repository-only follow-up carries the owner's verified local layout into a
draft PR from current main. Its application diff is limited to
`source/app/page.tsx` and `source/app/inspection-panel.css`. The corresponding
mirror receipt binds the exact repository base and the selected predecessor;
historical receipts remain unchanged.

## Observable result

The existing flat 2D map and standard light basemap were selected through the
working controls. Their defaults, restoration schema and provider data are
unchanged. Above 960 CSS pixels, Evidence opens on an ordinary map visit and
extends from the header to the viewport bottom. Explicit closed links, Globe,
restored utility views and compact layouts keep their existing behavior.

The bottom timeline stays inside the map column as the drawers change its
available width. Its year preview, slider, Commit and Present controls remain
available; Time in the global toolbar opens the full details. A closed compact
timeline is hidden, and opening Time restores the interactive controls.

## Visual and interaction evidence

The owner-supplied reference and rendered local Explorer were compared together.
The reference is cropped and has no recorded CSS viewport or device scale, so
this records the requested composition rather than pixel-identical framing or
historical provider observations. Private screenshots and local storage backups
remain outside Git and deployment assets.

At a 1045 × 899 CSS viewport, the final local capture showed a 54-pixel header,
a 745 × 755 map, a 300 × 845 Evidence drawer extending from y=54 to y=899,
and a 745 × 62 bottom timeline above the map status row. There was no page
overflow. The light map, navy/gold panels, five existing layers and Harper county
hover preview matched the requested visual hierarchy. Phone 390 × 844 and
compact 900 × 844 checks confirmed Time/Close visibility and usable controls.

Verified interactions: Effects opens and Escape dismisses it; Layers opens and
closes; private Chat with KFM opens and returns to Evidence without sending a
prompt; year preview 2025 enables Commit and returning to 2026 disables it.
No year was committed. Reload preserves the desktop drawer behavior. The final
browser console had no errors, and the normal viewport was restored.

## Validation

The two application files in this candidate are byte-identical to the verified
local preview. The current-main versions before applying them matched the
pre-layout baseline exactly. In the isolated follow-up checkout:

- Production build and static delivery containment: PASS.
- TypeScript `tsc --noEmit`: PASS.
- Existing inspection-panel, GoDaddy layout port, menu dismissal, map navigation,
  scene studio and rendered-HTML suites: 63 passed, zero failed or skipped.
- Mirror provenance, generated receipt and staged topology checks: recorded in
  the draft PR after validation. Exact-head hosted CI is a separate result.

No new effect, event listener, fetching behavior, dependency or state schema was
introduced. The selected mirror receipt records exactly the two presentation
deltas, retaining source digests and all other inventory entries. Content parity
does not establish hosted equivalence or source/overlay approval: review remains
pending, human acceptance false, and hosted equivalence false.

## Preservation and placement

The original preview checkout and its unrelated changes are preserved. No
credentials, private storage, D1/R2 bindings, schema, saved Places, provider
refresh, archive authorization or source admission behavior changed. All 258
withheld paths remain absent. Neither hosted Site is deployed by this work.

Application files retain their existing `apps/site/source` ownership. This dated
record follows the existing `apps/site/verification-*.md` lane; the compatible
full manifest and authoring receipt remain in `data/receipts/generated`, and
the selector and regressions remain under `tools/qa` and `tests/qa`. Directory
Rules v2, adopted by ADR-0029, and ADR-0048 retain those responsibility boundaries.
No new canonical root, authority mechanism or schema is introduced.

Rollback the two layout files and receipt selector together to the exact
predecessor recorded in the new manifest. This restores the earlier geometry
without a data migration. Review, merge, source activation and deployment remain
separate actions; this delivery is a draft PR only.
