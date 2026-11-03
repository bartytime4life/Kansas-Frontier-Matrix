# SQL archive layers in the Explorer

The unpublished map candidate adds 42 selectable archive/reference layers to the existing layer browser: 34 Census TIGER/Line 2025 geometries plus weather stations, airport weather stations, historical storm begin points, captured warning polygons, captured earthquakes, captured stream gauges, NWM v3.0 reference reaches and monthly PRISM county climate shading.

They participate in the existing topic search, combined-card context, selected-layer count and card/pipeline registry. They are optional additions to a topic's starting map, not 42 automatically enabled overlays. The data-library addition below is linked from this same layer browser. No capture schedule or database migration is introduced.

## Using the data accurately

- Every one of the 17 existing public SQL dataset endpoints has a use or an explicit hold in `ARCHIVE_DATASET_USES`. Station observations, climate-index definitions, climate indices, wind observations/summaries, five-minute airport readings and gauge readings are record drilldowns rather than invented continuous surfaces.
- Geometry comes from the provider's stored coordinates. Nulls, malformed coordinates, unclosed polygon rings and out-of-region point placeholders are withheld; records remain inspectable. Duplicate feature identifiers do not create duplicate markers. Source geometry can extend beyond Kansas.
- A reported storm begin point is not a storm footprint or tornado track. Warning records without provider polygons receive no invented county geometry.
- PRISM uses one explicitly selected month, variable and 4 km AN grid. The county join is exact TIGER 2025 GEOID. These are means over grid-cell centres, not station measurements or area-weighted means. Zero remains zero; missing numeric values or zero valid cells receive no fill. The legend carries the actual unit and loaded range.
- Dates, quality flags, original units, provisional status and source notes remain accessible. Cache and response timestamps describe delivery, not observation freshness. Archive controls are independent of the main map timeline. An empty month is not silently replaced by another month.
- NCEI ASOS local standard time remains distinct from IEM UTC; five-minute drilldowns are restricted to the five exact archived airport identifiers. An unavailable station/date range is shown as empty, not fabricated.
- NWM v3.1 numerical output is not painted onto v3.0 reference geometry. That correspondence remains unverified.
- Census reference geography is not a survey, ownership determination, population count or navigation aid. Statistical-area vintages remain explicit.

## Interaction and query bounds

Local reference queries cover a labelled one-degree square around the map centre. Users can pan and reload, page through results and inspect the original attributes. Matching/loaded counts, omitted geometry and duplicate counts make partial coverage visible. At most 1,000 map records are retained per archive layer; reading tables page through the gateway's bounded results. No provider-wide completeness is implied.

Reads use the existing same-origin public allowlist, with a 1 MB response limit and two concurrent client requests. Oversized geometry pages retry with smaller limits while preserving filters and offsets. Selection removal aborts pending/queued work and removes owned map layers, sources and listeners. Basemap/style changes redraw retained results. Archive shading is inserted below archive point markers; only the top visible feature owns the click.

Shared links store the applied archive dates, climate measure and search area. Unsubmitted form edits do not replace a displayed query. Reopening queries the first page again, so revisions may change results. Browser-location-derived search areas are redacted along with the main camera. Selected records and extra loaded pages are not frozen snapshots or exported evidence.

## Recovered-data accounting and owner clarification — 2026-11-03

The owner confirmed that the recovered datasets are public and authorized using all of them. Earlier hypothetical sensitivity/publication holds are superseded by that instruction. Source attribution and factual geometry/time limitations remain; public availability alone is not an exclusion criterion.

The `/data-library` route exposes all **189 domain tables** from the inventoried observations and bulk stores through two signed, read-only adapters. Operational import paths/build state and duplicate full-text-search implementation tables are not dataset collections. The existing 17 specialized endpoints remain, including TIGER and NWM GeoPackages. The source registries contain 206 source/database entries (203 distinct source IDs); these are not 203 independent maps or 203 complete imports.

The library supports collection search, original record fields, keyset pagination, page JSON downloads, provenance, and selecting multiple geometry collections for a combined map. There is no arbitrary SQL/table/path endpoint, whole-table count, offset ceiling or broad query scan. Exceptionally large text/polygon fields are explicitly marked and readable in 32,768-character parts; a page download includes that marker rather than claiming to include omitted text.

An additional **56 geometry collection options** join the earlier 42 archive options (98 total). They draw stored GeoJSON from loaded record pages. They are explicitly not viewport queries or complete statewide layers. The map retains at most 1,000 records per collection; every further record page remains accessible in the library. Attribution includes OpenStreetMap contributors and ODbL. Original dates and collection identities remain separate; overlapping editions are not summed.

Read checks on all 189 collections found 180 nonempty and nine empty tables: six ASR tables, Wikidata events/people, and newspaper OCR pages. Newspaper titles/batches do contain records. An empty import table is reported as empty, not as a completed archive. These additions make all existing SQL domain records accessible; they do not claim that every raw file on the 1.5 TB volume has been imported.

Technical work remaining for richer thematic maps:

| Data | Actual representation requirement |
|---|---|
| ACS, Census, CDC, agriculture and energy statistics | Exact geography/edition join; measure, denominator, margin and suppression semantics. Original tables are readable now. |
| Water, wells and other coordinate-only tables | Resolve the stored horizontal datum and location precision before adding markers. For example, sampled USGS station metadata explicitly says NAD27; raw latitude/longitude must not be assumed to be WGS84. |
| NWM numerical output | Verify v3.1 model identifiers against v3.0 reference geometry. Values remain readable as records. |
| Historical and cultural data | Preserve event/edition dates and source precision; georeference scanned sheets independently. Records without geometry remain available. |
| Unimported or empty collections | Recover/import the underlying source bytes before claiming their contents are available. |

Raw archives and audit artifacts remain outside deployment assets. Provider text/measurement data are delivered through bounded signed queries; this change does not bulk-copy the recovery volume into the website.

## Runtime integration

The source now defines 19 public dataset endpoints. Install this same candidate's `scripts/local-data` code and `recovered-catalog.json` together on the gateway and relay worker, and configure the gateway's optional `KFM_LOCAL_DATA_BULK_DB` to the recovered `kfm-bulk.sqlite`. The hosted application must use the same route allowlist. Preserve all existing keys and database settings; no GoDaddy credential rotation or database migration is needed. Production activation has not been performed by these local changes.

## Earlier 42-layer validation on 2026-11-03

- Read-only bounded queries exercised all 42 adapters against the PC's actual databases. The initial central-Kansas sample contained 838 rows: 823 usable geometries and 15 unlocated records (two storms, 13 alerts), with no duplicate identifiers or query errors.
- Seven reference layers had no records in that centre window. Separate queries confirmed their retained geometries elsewhere; an empty local window is not treated as a missing statewide dataset.
- All 105 county geometries joined to all 105 September 2026 PRISM precipitation summaries; there were no missing numeric fills in that edition. This is a checked edition, not a blanket quality assertion for every grid.
- First/cold reads of block-suffix geometry and gauge summaries took about 29.5 s and 21.2 s respectively. Warm block-suffix reads took about 0.02 s. The production relay has a shorter timeout, so cold I/O remains a deployment/performance acceptance item; the UI reports failure and permits retry rather than announcing a successful layer.
- Unit/component tests cover invalid geometry, missing versus zero values, exact joins, public-query contracts, shared dates/privacy, bounded pagination, stale responses, cancellation, style redraw, click ownership and card reachability. Browser verification uses the real databases through a loopback-only read-only preview, not a simulated production relay.

The production app and root-owned gateway are unchanged. Hosted signed-relay acceptance and production publication remain separate from local map verification.

Earlier candidate checks: 219 tests passed; one hosted-endpoint test was skipped because no built production test origin was configured. TypeScript and production build passed. ESLint reported zero errors and the existing 41 page warnings. Manual browser checks at 390 px and desktop width verified combined station/climate display, date entry, missing-month behavior, county values, independent layer removal and a real shared URL reopening with 146 station points, 105 climate polygons and the saved 2008/September 2026 dates. The mobile document width equalled the 390 px viewport. The standalone browser regression suite was not executed.


## Expanded library validation — 2026-11-03

- All 189 collection adapters were read against the real read-only databases, including a second page when present: zero query errors, overlapping page identities or null cursor keys. There were 180 populated collections and nine empty tables.
- A 20-record sample per geometry collection examined 1,038 records: 1,020 valid map features, 18 records without usable/displayable geometry and no duplicate record identities. Valid recorded locations outside Kansas remain usable; zero-coordinate placeholders are not drawn.
- An actual large historical-county query exceeded the response budget at 20 rows and successfully retried at 10, with continuation intact. Exceptionally large individual fields have a separately tested exact Unicode chunk reader.
- The final focused/adjacent suite passed 174 tests; one hosted-endpoint check was skipped. TypeScript, production build and targeted ESLint passed. `git diff --check` passed.
- Browser verification at 390 px found no document overflow, read records from both databases, advanced FAA pages from records 1–20 to 21–40, selected FAA and NBI together and loaded both map collections. Map pagination loaded 40 FAA records. Unit coverage verifies that a failed next-page read preserves the existing map features.
- The loopback-only review surface is `http://127.0.0.1:4188/data-library`. This is a local QA proxy over the real databases, not production acceptance. No production service, credential, feed schedule or hosted app was modified.
