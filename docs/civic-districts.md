# Kansas representation: Census congressional districts

## Behavior and status

Government & civic opens **Kansas representation** with four labeled, independently colored Kansas U.S. House districts. Selecting an area or one of the four keyboard buttons opens the existing source-context drawer and focuses the map on that district. The dock offers district visibility, optional Census county comparison, and the Kansas Secretary of State's official district-map page. Colors identify district numbers; they carry no party or election-result meaning.

The welcome glimpse uses this same category starter, fixed adapter and map styles. It does not draw illustrative district shapes. Source loading or failure remains visible. Counties remain available, but their filled overlay starts off in Government. Other categories' starters are unchanged.

**Implemented:** fixed-edition source adapter, bounded validation, rendering and source keys, map/keyboard selection, attribution, source traces, and a source-download link. **NEEDS VERIFICATION:** successful real provider query, visual desktop/mobile acceptance, label collisions, rendered frame rate and deployment. Source metadata was retrieved, but the query was unavailable through the research tools and Chrome reported a client block. Synthetic tests do not prove actual Kansas geometry or live availability. No source payload or screenshot is represented as a verified production capture.

## Source and meaning

- U.S. Census Bureau, [Generalized ACS 2025 Legislative layer 5](https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2025/Legislative/MapServer/5): **119th Congressional Districts 500K**, January 1, 2025 vintage. Metadata inspected October 29, 2026 confirms polygon geometry, the `STATE`, `GEOID` and `CDSESSN` fields and GeoJSON query support.
- [Census 119th Congress documentation](https://www.census.gov/programs-surveys/decennial-census/about/rdo/congressional-districts.119th_Congress.html) identifies the Congress as January 2025–2027. The implementation deliberately avoids the mutable service's top-level “current” congressional layer, which currently names the 120th Congress. A future edition requires an explicit change and validation.
- [Kansas official district maps](https://www.sos.ks.gov/elections/district-maps.html) links congressional, House, Senate and Board of Education maps. This page is offered for authoritative follow-up; the implementation does not assert that Census display geometry settles address-level voting questions.
- Attribution names the Census Bureau, product, vintage and Congress, following [Census citation guidance](https://www.census.gov/about/policies/citation.html). No copyrighted basemap imagery or third-party district dataset is repackaged. Confirm applicable rights during any later source admission; this addition does not grant a new license or approve a KFM release.

The 1:500,000 generalized geography is for orientation, not cadastral, jurisdictional or voting adjudication. No officeholders, party affiliation, demographics, polling places, election results or ballot eligibility are joined or inferred. Retrieval time is distinct from boundary vintage; `upstreamUpdatedAt` remains null because no actual update timestamp is supplied. The shared atlas clock holds the layer outside its Present frame; the visible edition remains explicitly 119th Congress, never silently relabeled as the selected year.

## Bounds and failure handling

The browser requests `/api/live-context?feed=census-congress-119`. The server fixes the Census origin, service edition, layer, Kansas state filter, output fields and coordinate system. Extra/duplicate parameters and historical dates are rejected before fetching. Redirects are not followed. A read has a 25-second deadline, a 2 MiB streaming budget and a five-record query ceiling. Exactly the distinct GEOIDs `2001`–`2004`, `STATE=20`, and `CDSESSN=119` must survive validation; any missing, duplicate, extra, wrong-edition or malformed feature rejects the whole response.

Polygon/MultiPolygon rings must be finite, closed, nondegenerate and within broad Kansas bounds, with at most 50,000 vertices in total. These are defensive structural checks, not a proof of topology or boundary correctness. Six decimal output places do not improve the generalized source's accuracy. Only the validated geometry and constructed display properties leave the adapter; provider names, HTML and arbitrary attributes are dropped.

Concurrent callers share one bounded request per process. Validated results are cached for up to 24 hours; a failed refresh clears expired content and applies a one-minute retry cooldown. HTTP responses are `no-store`; no additional HTTP stale cache is introduced. Cache coordination across multiple replicas is unverified. The existing preview has its own short-lived consumer cache and request timeout; no new polling loop or third-party renderer is added. Hiding the layer, source failure, temporal holds and style replacement use the existing context lifecycle.

## Placement, authority and rollback

Initial base: standalone hosted branch `a0-hosted-ai-web-20261017` at `80d09b1ffdd5638e3edc3f95ed8bfb79f59f59d1`, tree `92d3fd04492a447f0d0eb6adce78cb2a1f8282ab`. The isolated local starting tree was verified against this remote tree. The subsequent docs/test-only merges #5548 and #5549 were incorporated at base `10cf8838117a48011229914c90af82524780c9d8`, tree `0012242bfc2312a3c730e7b1996519774b30ee34`. They do not change the application runtime. The hosted composition differs from the monorepo's layout.

Directory Rules v2, adopted by ADR-0029, §§5 and 10–12: **PLACE** within existing owners. App-specific source projection belongs in `app/civic-districts.ts`, acquisition extends the existing `app/api/live-context/` boundary, UI and source traces extend their current files, behavior documentation belongs in `docs/`, and regression checks in `tests/`. This is an application display adapter, not a new canonical connector, source registry, policy home or released-data store. No parallel authority is created. `DIR-PLACE-002`, `DIR-DATA-004` and `DIR-SOURCE-003` preserve the separate source-admission and publication lifecycle.

Signed publication recipes, source approvals, EvidenceBundles, persistence and the second-PC worker are unchanged. This reference layer is `EXTERNAL_CONTEXT_ONLY`. No merge, deployment or publication authority follows from passing tests or creating a PR.

Rollback: revert this addition, restoring Government's county starter and prior glimpse. No migration or persisted source payload requires cleanup. Record any later deployment or source correction separately.

## Validation

`tests/civic-districts.test.mjs` uses explicitly synthetic geometry to exercise the complete-edition contract, malformed/capped responses, fixed endpoint, request coalescing, cache expiry, sanitized errors, route inputs, keyboard actions and map-style restoration/visibility. Category, preview, temporal, source registry and existing context tests provide adjacent coverage. See the PR for commands and actual results; this document does not stand in for an execution receipt or browser acceptance.
