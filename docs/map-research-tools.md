# Map research tools

## Behavior and scope

The provider catalog adds **All / Selected / Needs attention** filters beside
its existing topic filters and text search. Filtering only changes listed rows;
it never selects, hides or clears a map layer. Expanded Options keep existing
source controls. Earth Engine and specialized layer controls stay in their
established workspaces. Source time remains separate from response retrieval.
A selected source can be loading, held by time/projection, unavailable, empty,
or ready for display. Opacity, map style readiness and minimum zoom also affect
display status. “Displayed” describes an enabled ready carrier, not complete
coverage, a fresh observation at every point, or admitted evidence.

**Near here** opens a place dossier in the Evidence Drawer. Start with an
eligible registry record or loaded provider point. The anchor remains fixed
while another result is inspected. **Start new dossier here** explicitly
replaces it. Reopening Near here returns focus to the inspected result when it
is still present; otherwise the dossier heading receives focus. The established
Drawer close/Escape behavior returns to the invoking control or the map.

The initial radius is 25 miles; choices are 25, 50, 100 and 200 miles. The
available inventory includes selected, temporally compatible public-safe
registry anchors and loaded point responses from existing provider adapters,
including the loaded KGS monitoring-location snapshot. Provider reads reuse
application responses or MapLibre's public `getData()` for that snapshot.
Canceled reads cannot replace a newer inventory. Loading, failed and held
responses are excluded; a selected archive day must match the response day.
The existing River Pulse frame and other source clocks retain their own
semantics. There is no new source download service or historical collection.

Records without a stable identity or valid supplied point coordinates are
excluded. Registry anchors are labeled as display-anchor distances; provider
points use supplied coordinates. Raster pixels, polygon centroids, geometry
edges, route lengths and unindexed streamed tiles are not proximity inputs.
Deduplication uses source and feature identity, with newest retrieval and stable
content tie-breaking. Great-circle distances are sorted by distance then
identity; the nearest 50 display with the full matching count. The count is
bounded by available loaded data, not all records in Kansas. Coverage lists
selected sources, partial responses, held/unavailable sources and excluded
carriers. An empty result means none in the available eligible data.

The selection summary keeps source, time, evidence posture, support and limits
beside inspection actions. Provider context does not become admitted KFM
evidence, an EvidenceBundle, or a claim of causal relationship.

**Search reviewed knowledge** is a separate, editable place-name form. It opens
the existing `/knowledge` search view and uses its existing reviewed-knowledge
read endpoint. Knowledge records have no radius-compatible coordinates here
and never enter the distance-sorted dossier.

## Saving and exports

`ResearchContext` is an optional, validated version-1 field on existing
workspace/report records. It contains an anchor, supported radius, source
identities, map-time label, capture/retrieval times and explicit coverage limits.
Unknown structural fields, invalid coordinates/links, oversized records,
invalid distance values, duplicate neighbors and provider evidence promotion
are rejected. Older records without this field remain readable.

**Save investigation** stores settings through existing device-local Places.
It saves no nearby response rows. Reopening restores source selections, reloads
eligible feeds, and identifies unavailable anchors or retired source IDs.
Saved context is not replayed as current provider data. Storage denial or quota
failure leaves the saved list unchanged and announces failure.

**Create report** copies a dated snapshot into the existing report builder.
Provider context stays separate from `includedEvidenceIds`; JSON, Markdown and
print output preserve source links, observation/retrieval labels and coverage
limits. Editing or refreshing the map does not rewrite the captured snapshot.
Context captured from a browser-location-derived view retains its redaction
marker for the life of that dossier. Saving or reporting while location
redaction applies omits the entire dossier and its automatic place-name title.
A new explicit dossier can replace the old context after the map is reset.
No backend API or database schema changes are introduced.

## Global search readiness — hosted follow-up, 2026-10-18

Global search reports the state of the current query and available county
coverage. Editing a query hides results belonging to its previous debounced
value and announces that search is updating. Idle county data is described as
not ready without claiming a request is active. Loading data is described as
loading; unavailable, empty and partial county responses are described as
limited county coverage. Valid current-query matches from other search
categories remain usable while county data loads or is unavailable.

A complete no-match message is shown only for a settled query with complete
county search coverage. It describes the currently searchable inventory, not
the absence of a real place or evidence in Kansas. Partial or unavailable
county coverage must not be presented as a complete search. County records
retain their Census source-context label and do not become admitted evidence.

Feedback uses a noninteractive polite status row in the existing dropdown.
The search input is busy only while query debounce or a county request is pending.
Idle, empty, unavailable and partial county states are not busy. Clearing
the query or closing the dropdown removes its feedback. This change reuses
existing responses and adds no source request, gazetteer, admission, release,
or persistent state.

Application behavior and regression coverage belong in the existing
`app/county-search.ts`, `app/page.tsx` and `tests/` families. The existing hosted
CI job includes the readiness regression file alongside county-search tests. This dated
hosted-source note does not refresh the historical Site identities, validation,
publication or rollback claims elsewhere in this document. Current validation
and final-head review are recorded with this follow-up's draft PR; reverting
the bounded follow-up restores the previous search behavior.

## Placement, provenance and compatibility

This is a standalone Site UI change: application modules stay under `app/`,
regressions under `tests/`, and behavior documentation under `docs/`. Its review
mirror stays under `apps/site/source`, the existing application responsibility
root, consistent with accepted ADR-0029 and the adopted
`docs/doctrine/directory-rules.md`. It creates no registry, contract, evidence,
source-admission or release store.

The attached “Kansas Frontier Matrix.zip” informed compact catalog rows,
expandable details, filter chips and place-centered inspection. Prototype data,
simulated services and document instructions were not imported or executed.

The implementation starts from owner-private Site v153, source
`da94de300c1b20dc98e9f527ba54613cfd696f8b`. The GitHub review patch is applied
selectively on `43ef1c22976b2114ec9a936b97651fba4970bed5`; the newer repository
maintenance and local `87bd864caf113cd341303fa3394dc643852d0ced` candidate are
separate preserved work. The resulting Site and GitHub tree need not be
byte-equivalent. A historical mirror receipt must not be rewritten to imply
otherwise. The local installed service is outside this change.

## Verification and rollback

`tests/research-context.test.mjs` exercises filters without visibility mutation,
source/time holds, missing coordinates, non-point exclusions, radius edges,
deduplication and deterministic limits, pinned anchors, canceled/stale reads,
workspace/report compatibility, storage refusal, source-labelled exports and
location redaction. Existing snapshot and runtime regressions remain applicable.
Run TypeScript checking, the production build and the standalone Node suite.
Repository topology and mirror checks apply separately to the review patch.

Desktop/mobile layout, actual keyboard focus, map interactions and provider
rendering require browser acceptance; pure/model tests do not establish that.
Deployment and browser acceptance are separate observations. Keep the existing
owner-private audience and DB/R2 bindings. Site v153 is the preceding saved
rollback target. Revert the bounded review patch to reverse the repository
change; existing saved records remain compatible and new optional context can
be ignored by the prior UI.
