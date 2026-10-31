# Category capability recovery · 2026-10-31

## Scope and observed gap

Source base: public Node composition `6691a41736bdad91ded7a6824e73d8cac11d92d5`.
Chrome independently read GoDaddy Preview and Published at
`7ca063e32e7f630b0fec661e19a1fa33d7920036`. The live Science card opened a
satellite starter with only daylight in its dock; its Layers catalogue still
listed 35 sources/controls. The Science Lab was on another page. Crop history,
SSURGO, growing degree days, frost and season rain remained implemented but were
revealed only after enabling crops and choosing a point. These are navigation
and discovery gaps, not evidence that source data was deleted.

All 22 card definitions, their starter layers, map tools, official source-topic
memberships, specialist controls, imagery recipes and the 18 Science Lab
phenomena were inspected. This is a code/UI capability inventory, not an audit
of all private databases, source rights, physical caches or installed runtimes.

## Implemented recovery

- Layers → Browse now searches both existing source layers and a separate
  **Tools & workbenches** index. All categories have an entry. Counts remain
  separate because a tool or recipe is not an enabled observation layer.
- Tool shortcuts reveal the current map's existing controls and move keyboard
  focus there. They do not invoke `openCategoryMap`, replace starter layers,
  change camera/basemap, reset stores, or turn a tool on. Existing topic-driven
  water-animation restrictions remain in force.
  Tool-only presentation is explicit even when the retained map happens to use
  the category's basemap; that match does not imply its source layers are on.
  The separate **Open default view** action applies the actual category setup;
  the existing preset's **Reset view** remains a camera reset.
  The topic guide always retains **Open this map**. A matching basemap style
  no longer hides that action or claims that the category's data layers are on.
- Science Lab links open its existing panel and optionally filter a phenomenon.
  Workbenches open in a separate tab so the current map remains available.
  Navigation does not enable additional tracks or authorize data capture.
- Farming controls explain the point workflow before crops are enabled. Once
  enabled, **Inspect crops & season at map center** uses the existing six bounded
  point readers, with their existing cancellation and source/date validation.
  It is an explicit keyboard alternative to the map click, not an automatic
  background sweep. Changing year still requires choosing/inspecting the point
  again, as before.
- Agriculture now includes the existing alert/radar/wind/satellite context,
  reviewed daily-weather control and compatible imagery catalogue entries.
  This is catalogue membership only; defaults and data eligibility are unchanged.

## All-card matrix

“Existing” means code and a navigation path exist. A provider may be unavailable;
an imagery recipe or reviewed snapshot still needs eligible installed data.
The last column is a proposed next refinement, not a delivered new product.

| Card | Existing data and useful controls | Visual/effect use and limits | Next refinement to review |
|---|---|---|---|
| Engineering | KDOT bridges, roads, hydrography, PLSS; terrain transect and measurement | Relief/light reveal crossings; no structural-safety inference | Save a bridge + valley profile investigation with source dates |
| Transportation | Current/1918 roads, active/abandoned rail, bridge classes, optional DeFlock | Compare dated networks; no simulated trains or inferred closures | A dated corridor comparison using existing historical controls |
| Aviation | FAA zones, airports/runways, drone ceilings, weather and existing traffic controls | 2D chart/3D volumes/altitude slices; display only, not flight authorization | A source-date checklist beside a saved airport view |
| Weather | Radar, alerts, GOES, wind, lightning, station observations, outlooks/reports, rain | Timestamped scan playback; model wind remains forecast context | A station/radar/rain comparison with visibly separate clocks |
| Hazards | Fire detections/reports, smoke, FEMA history and optional flood/seismic sources | Distinct point/area symbols; missing feed is not all-clear | A hazard chronology retaining observation, report and declaration roles |
| Water | USGS discharge, NWS stage/forecasts, hydrography, basins, MRMS | Optional flow effect with existing direction/coverage limits, not velocity | Pair a gauge hydrograph with basin rainfall without inferring ungauged flow |
| Groundwater | KGS aquifer classes, monitoring wells and recorded Underground columns | Thickness/depth classes and measured well timelines; gaps remain unknown | Compare one well's dated measurements against its aquifer-map vintage |
| Geology | USGS earthquakes, relief, transects, cores; Observatory surface geology/resources | Recorded-column glimpse and source-bounded sections, no continuous invented geology | Pin a log, surface unit and earthquake depth as three separate evidence views |
| Terrain | DEM, slope/hillshade, aerial terrain, transect | Raking light, 2D/3D and true-scale profiles | A reusable two-place profile comparison; quantitative change needs paired qualified surveys |
| Ecology | NLCD classes, watersheds, imagery, coarse plant context | Classification and imagery comparison, not habitat/species proof | Compare land cover along a selected watershed with dates and resolution shown |
| Agriculture | CDL history, SSURGO, SMAP/Crop-CASMA, GDD, frost, season rain, drought, MRMS | Year steps, crop-history strips, weekly drought change and field measurement | A single exportable field-context dossier retaining station distance, missing days and model scale |
| Flora | NLCD vegetation/wetlands, GBIF annual hexagons, CDL | Coarse density by year; no abundance/absence or precise sensitive locations | Side-by-side cover and sampling-density views without causal claims |
| Fauna | Landscape context; existing generalized Observatory animal records | Coarse occurrence counts only; no exact sites or movement paths | An effort/coverage explanation before comparing annual counts; reviewed Fauna releases remain separate |
| History | Dated KDOT maps/rail, original historical accounts, map-sheet tools | Date comparison; source browsing retained while pending catalogues remain held | A source-edition timeline linking an account to an eligible map sheet |
| Land | PLSS, bounded BLM lease context, imagery, area measurement | Survey pattern and land cover; neither proves ownership | A map-unit/land-cover worksheet with explicit ownership-evidence gaps |
| People | Aggregate Census density and 2010–2020 change, civic references | Area-level prisms and choropleth, never individual profiling | Pair density/change with published area counts and uncertainty/context notes |
| Government | Historical congressional plans, Kansas chambers, civic records | District selection by Congress/date, not party or election predictions | Save a jurisdiction/date dossier with official record links |
| Places | Counties, watersheds, survey references, saved investigations | Compare boundary systems without treating them as interchangeable | A reusable place context stack with source editions |
| Crime & justice | Civic reference and optional community plate-reader areas | No crime/court/live incident layer is connected; no safety inference | Keep unavailable feeds visible; any later incident intake needs privacy/review first |
| Science | 35 catalogue entries at the observed live version; Science Lab's 18 phenomena, imagery recipes | Station snow, static geology, resource aggregates, radar and separate clocks; ice/erosion remain unconnected products | A method-first comparison workspace selecting units, support and clock before an effect |
| Sky | Calculated daylight/twilight, sun-year and Moon tools | Terminator, seasonal daylight and lighting; not weather/visibility observations | Link a place's daylight chart to an explicitly chosen map time |
| Evidence | Inspect, compare, sources, released knowledge, reports/downloads | Evidence state and source status remain separate from attractive map effects | An export checklist that preserves each view's source/time/limits and unresolved gaps |

The existing Notion/Drive roadmap (last edited October 8) likewise separates
source clocks, performance proof and release authority. It is design lineage,
not proof that a planned layer is live. No new provider, science model, exact
wildlife location, private intake or unreleased catalogue is enabled here.

## Boundaries, validation and rollback

Application navigation belongs under existing `app/`, regressions under `tests/`,
and this explanation under `docs/`, consistent with the existing standalone
composition and Directory Rules v2 adopted by ADR-0029. No new data, contract,
registry authority, dependency, schema or storage root is created.

Validation is recorded with the PR and private delivery evidence: types/build,
changed-file lint, ordinary/focused regressions, real Chrome desktop/narrow
navigation and the bounded security diff review. Passing these does not qualify
every provider, all scientific interpretations or full multi-runtime parity.
Revert the focused commit to undo navigation/UI changes. No database rollback or
migration is required. Public publication remains on hold; merge, private
deployment and publication are separate actions.

The inherited population-change test assumed its reset statements immediately
preceded the aviation branch; the existing aviation reset broke that adjacency.
Concurrent owner-merged #5642 repaired that anchor and is preserved here. Our
category-session regression additionally seeds all four population state/ref
values and executes every category opener, requiring each value to reset.
Removing a reset fails that behavioral check; no assertion about population
ownership is waived. Dock binding checks inspect JSX attributes independently
of prop order and also require the retained-map presentation flag.

## Browser journey follow-up

The final #5643 head passed ordinary tests and welcome performance, but its
delivery job failed seven startup-browser cases. Existing exact-base CI at
`9bed7041691731459503e827622435c9d7e150dd` fails the same seven cases: two
direct-card search checks, three compact Sky keyboard journeys, and two compact
welcome failure/recovery journeys. The test selector chose the first search
input in the panel (the hidden Living Atlas input), rather than the visible
**Search map layers** field. The compact journeys then attempted to focus
background map/header controls while the newly opened Layers modal owned focus.

The follow-up scopes the search assertion by its accessible name and exits
compact Layers through its visible close control before the next background
action. It verifies close-button focus, panel closure and release of inert
background controls, then waits for the existing map-focus return to complete.
Pointer targets are hit-tested again after the intentional slow-hover interval;
the earlier pre-hover coordinate is not reused after a scroll/reflow. The
original direct-entry, search visibility, daylight
geometry/contrast, failure/recovery and exact focus-return assertions remain.
No application, provider, data, runtime or access behavior changes in that
test-only reconciliation. Local before/after and exact-head CI results are
recorded in the follow-up PR; they do not qualify every startup timing case.
