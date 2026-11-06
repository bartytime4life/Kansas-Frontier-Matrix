# Map key and source dates

Opening a startup category intentionally hides its instrument dock. The crop
map therefore drew a dated classification while its key required finding and
opening the farming tools. The existing Map menu now has an expandable Map key,
using the same renderer and palettes as the category dock. It gathers keys for
enabled, temporally eligible official layers plus active tools and the current
elevation basemap. It does not change map selections, camera, source dates or
browser history. Missing keys are disclosed rather than invented.

The menu retains its existing bounded scroll area. The disclosure has a 44 px
minimum target, wrapping class labels, and the existing Escape/focus return.
Browser acceptance covers touch at 320×568, 390×844 and 568×320, plus desktop
1280×800. This is emulation, not physical iPhone qualification.

The official-source drawer labels retrieval as “Retrieved by KFM / response
state”, rather than “Last update / freshness”. Source-status rows separately
show the provider timestamp, explicitly disclose its absence, and include a
timezone on both clocks. A recent download does not establish a new observation.
No acquisition date or provider timestamp is inferred from the retrieval clock.

Source data, refresh behavior, map styles, stored state and provider boundaries
remain unchanged. Rollback is a code revert; there is no data migration.
Build, tests, review and hosted verification are recorded in the pull request;
this document does not assert publication or completed browser acceptance.
