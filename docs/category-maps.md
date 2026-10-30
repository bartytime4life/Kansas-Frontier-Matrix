# Category maps

Each start-page category opens on a map with stated coverage and source limits. The category map
registry, `app/category-maps.ts`, gives every topic in `app/layer-workspaces.ts`
one map look:

| Field | Meaning |
|---|---|
| `name`, `lede` | The look's short name and one sentence on what the visitor will see. They are shown on the welcome card, the topic dialog and the map dock. |
| `basemap` | A `BASEMAPS` key in `app/map-runtime.ts`. |
| `scene` | `2d`, `terrain` (3D terrain) or `globe`. It is applied through the existing `activateMapRepresentation`. |
| `camera` | Center, zoom, pitch and bearing. Only 3D looks start tilted. |
| `starters` | Existing official provider-context ids that are switched **on**. Opening the map switches every other provider-context layer **off**, as a starter set does, so each map opens on its own subject. |
| `swatch` | Three colours used to sketch the basemap on the start card and the dock. |
| `light` | Optional scene recipe (`daylight`, `golden`, `blue`, `survey`) the look opens under. Only its atmosphere and sun azimuth are applied, through `changeStudioLight`, so the visitor's effect settings never change. Relief looks use a raking sun (Terrain golden, Geology/Engineering/Groundwater survey), weather and water a dark sky (`blue`), aviation `daylight`. **Reset view** restores it. While the visitor follows the real sun, the computed sun lights the map instead. |

Choosing a look is presentation and navigation only. Starters are the same
provider-context switches the Layers panel offers, with their own source clocks,
holds and limits. They are display context, not admitted evidence.

## Fauna and crime, justice & public safety

The shared taxonomy has 22 categories, including Flora (see below). **Fauna & wildlife** belongs to
Earth & environment; **Crime & justice** belongs to People &
place. The welcome, Layers topic selector, Topics index and restored `topic`
URLs use the same `fauna` and `public-safety` identifiers.

Fauna opens **Wildlife landscape**, a statewide 2D prairie basemap with no
provider starters. No reviewed animal-occurrence layer or governed Fauna
EvidenceBundle is connected to this map. Links lead to the existing Observatory
and its source catalogue, whose occurrence context has its own scope and
limitations. Landscape appearance does not establish species presence,
abundance or absence. The category does not expose sensitive wildlife sites.

Crime & justice opens **Public-safety context**, a statewide
2D civic basemap, also with no provider starters. The existing DeFlock reported
plate-reader areas can be enabled explicitly from the context controls or
Layers; they remain classified under Transport and Engineering too. Those
community reports are not crime reports, live camera activity or emergency
coverage. Crime, court and live incident feeds are not connected. Reports do
not establish guilt, and missing records do not establish safety.

Neither category has a verified recording, so both display an explicit capture
limitation and their own map glimpse. Source inventory, admission, rights,
sensitivity, review and release controls are unchanged. Domain classification
does not admit a registry record: Fauna rows can appear in both Ecology and
Fauna, and crime/justice/public-safety rows can appear in the new category only
through the existing registry path.

Placement uses the existing hosted composition's `app/` presentation and
navigation responsibilities, `tests/` regressions and this `docs/` explanation,
consistent with accepted Directory Rules / ADR-0029. No parallel domain,
schema, policy, source or release home is created. Rollback is a revert of the
category change; no data migration is needed.

## How a visitor gets there

- **Welcome.** Opening a category shows its map look. **Open the {map look}**
  calls `openCategoryMap`. **Explore {category} sources** still opens only the
  Layers catalogue.
- **The map dock.** While a category's look is on screen, `CategoryMapDock`
  (`app/category-map-dock.tsx`) names it and offers:
  - 2D, 3D and Globe;
  - relief depth (3D only);
  - sun direction (not on the globe);
  - **Use the real sun now**, which switches on the Scene studio's "Follow
    real sun" effect. While it is on, the sun slider gives way to a reading of
    the computed sun over the map center, such as "52° up, from SW · 4:00 PM
    CDT", because a hand-set direction would have no effect. **Set light by
    hand** switches it back off. Only the visitor changes this setting; a look
    never does;
  - **Time**, shown while following the real sun: a quarter-hour slider
    through today in Kansas that relights the map for the sun at that moment.
    Watching it sweep from sunrise to sunset across the Flint Hills or the
    Smoky Hills shows how slope and aspect take the light. The reading then
    says "Sun at" rather than "Real sun", and **Now** returns to the clock.
    The chosen instant is registered per map (`registerSunInstant`), so the
    sky, relief, glow, buildings and Scene studio all read the same moment.
    Turning the real sun off or on from any control (the dock, the Scene
    studio checkbox, a recipe or a look preset) ends the study. The last
    step is 11:45 PM, so the slider never picks tomorrow's midnight.
  - **Play the day**, next to **Set light by hand** while following the real
    sun: a time-lapse that steps the study forward one quarter hour every
    200 ms (`SUN_PLAY_STEP_MS`) and stops at 11:45 PM, about 15 seconds from
    5:00 AM. It starts from the time shown, or from 5:00 AM once the day has
    been played out. Moving Time, pressing **Now**, turning the real sun off, or
    anything that takes its controls off screen stops it: hiding the dock,
    clearing the category, opening the guide or switching to the globe
    (`sunControlsShown`). Under reduced motion the button is disabled and
    only the slider moves the sun; It is display lighting only; no
    source time, archive date or evidence clock changes;
  - **Draw a cross-section**, on the Terrain, Geology and Engineering looks
    (`tools: ["transect"]`). It starts the existing terrain investigation
    (`startTerrainInvestigation`): 3D terrain, the Scene panel with its "Terrain tools"
    section opened and scrolled to the investigation steps, and a distance
    line. Finish the line, then **Preview display profile** samples the
    display DEM along it without the 3D exaggeration. It waits for terrain,
    and the profile stays display context, not survey measurement;
  - **Show river flow**, on the Water look (`tools: ["flow"]`). It switches the
    Scene studio's "Flowing water" effect on or off through
    `updateSceneEffects`: rivers flow downstream where USGS 3DHP maps a
    direction, and a USGS gauge reading lights its own reach. While it is on,
    the dock shows the effect's own reading, for example how many reaches have
    a flow direction and how many a gauge lights, or that it is loading or needs
    a closer zoom. When the map is degraded or still starting, or with reduced
    motion, ambient motion off or an efficient render budget (the same rule the
    animation uses), the rivers are drawn still and the dock names which applies. The flow reaches
    are display context, not measured discharge;
  - **Explore underground**, on the Aquifer and Geology looks
    (`tools: ["underground"]`). It opens the existing Underground view of
    recorded well logs, cores and aquifer sections (`enterUnderground`, the
    same entry the guide's Underground action uses), which switches to the 2D
    map and takes focus. The dock steps aside while Underground is open and
    returns when it closes, if the look's basemap is still on;
  - **Show day and night**, on the Sky globe and the Satellite view
    (`tools: ["daylight"]`). It switches the existing Daylight & twilight
    layer on or off through the layer card's own path
    (`toggleDaylightVisibility`): the calculated night side of the Earth and
    its civil, nautical and astronomical twilight bands. When the layer's
    chosen date range holds the current time, it opens at now
    (`showCategoryDaylight`); a past day chosen in the layer card keeps its own
    clock. While it is shown, the dock reads that clock in Kansas Central time
    and what it means at the look's center, for example "Kansas center: Sun 9°
    below the horizon · nautical twilight" (`daylightPhaseReading`, using the
    overlay's own band edges). **Play day and night** runs the layer's 60-second
    loop through the day; reduced motion disables it. It is calculated
    geometry, not observed brightness or cloud cover;
  - **Measure an area**, on the Field and Survey grid looks
    (`tools: ["area"]`). It starts the Map menu's own Polygon measurement
    (`beginMapMeasurement("area")`); pressed again while points are being
    added, it cancels. Click around a field or parcel and **Finish** in the
    measurement readout. Areas under one square mile read in acres (hectares
    in metric), larger ones in square miles with acres alongside
    (`formatMeasuredArea`), so a PLSS section reads "1.0 sq mi (640 acres)".
    The geometry stays in the browser and is an approximation, not a survey.
    While a measurement readout is on the map (from this tool or **Draw a
    cross-section**), the dock lifts above it; on a phone (760px or narrower)
    it steps aside instead, so the map can be tapped, and returns when the
    measurement is cleared;
  - **Watch the radar loop**, on the Storm desk (`tools: ["radar"]`). It
    turns radar on and opens its live loop controls (`watchRadarLoop`, shared
    with the radar layer card's "Watch live loop"); while they are open it
    reads **Close radar loop** (`closeLiveInstrument`). The live loop plays at
    the present map time, so the button waits until Time is at Present. Opening
    the Storm desk shows the latest scan without automatic playback. Press
    **Restart loop** to animate; closing the panel leaves radar selected. While a radar or lightning loop panel is open the dock
    sits above it; the taller river and satellite-flash panels, and any loop
    panel on a phone, have the bottom of the map to themselves and the dock
    returns when they close;
  - reset view and "Layers for this map".

  Every control reuses an existing handler: `activateMapRepresentation`,
  `changeTerrainDepth`, `changeStudioLight`, `updateSceneEffects`,
  `startTerrainInvestigation` (through `startCategoryTransect`),
  `enterUnderground`, `toggleDaylightVisibility` (through
  `showCategoryDaylight`), `beginMapMeasurement`, `watchRadarLoop`,
  `closeLiveInstrument` and `openAtlasPanel`. Turning river flow on or off also goes through
  `updateSceneEffects`. The dock can
  be hidden. It returns the next time a category map is opened.
- **Layers panel.** When a category is chosen in the Layers catalogue, its
  topic guide shows the same map-look card: name, scene and what you'll see.
  **Open this map** applies the look, and once the look is on the card reads
  "on the map now".
- **Shared URLs.** No new parameter is needed. `topic`, `base`, `proj` and
  `scene` already restore the category, basemap and renderer, and the dock
  follows the restored category when its basemap is on screen.

## Population in 3D (People)

The People map draws every Kansas county as a column (`app/population-prisms.ts`).
Each column is built from the same 2020 Census county record the Evidence
Drawer shows:

- **Height** is linear in density: 100 m for every person per square mile of
  land (`AREALAND`, water excluded). There is no logarithm and no exaggeration,
  so the metro counties stand as tall as their density says.
- **Colour** is the county's Kansas population density peer group, the KDHE
  classification: Frontier (under 6 people per square mile), Rural (6–19.9),
  Densely-settled rural (20–39.9), Semi-urban (40–149.9) and Urban (150 and
  over).
- The dock legend counts the counties in each group, and gives the statewide
  density (total people over total land, not an average of county ratios), from
  the loaded payload.
- A selected column opens its county record, which now carries
  `peoplePerSquareMile` and `densityGroup` beside the counts.
- The county layer's opacity slider fades the columns (as drawn at its
  default setting, gone at zero), and a shared link (`prisms=on`) reopens with
  them standing.

The columns replace the county outline while they stand, are hidden on the
globe, and appear in the start-page preview of the People map. Counts describe
areas, not people; a county's column says nothing about where in the county
people live.

### Change since 2010

**Show change since 2010** shades each county by its percent change in people
between the 2010 and 2020 Census counts (`app/population-change.ts`). The 2010
counts come from the existing `/api/event-atlas/counties?edition=2010` route,
the 2020 counts from the loaded county record, and the two are joined by
GEOID. Kansas's 105 counties kept their boundaries through the decade, so each
county is compared with itself.

- Six classes diverge at zero in ColorBrewer BrBG: losses brown (10% or more,
  5–10%, under 5%), gains blue-green (under 5%, 5–10%, 10% or more). Each lower
  bound is inclusive, so a county with no change counts as "grew under 5%".
- The dock gives both state totals, the net change, how many counties lost
  people, and the largest gain and loss in people. A bar chart sets all 105
  counties from largest gain to largest loss around the zero line, in their
  class colours. A keyboard list holds the same ranking.
- A county picked on the map, in the chart or in the list is outlined, and the
  dock gives both counts, the change and the county's rank.
- The change is drawn only when every county joins, with a count in both years
  and a non-zero 2010 count. A partial join would understate the state and
  misplace counties, so it is refused.
- One county encoding at a time: the change replaces the density columns. If
  the columns were up, they come back when the change closes. Raising the
  columns closes the change.

Both years are decennial counts, not estimates. The 2020 count carries the
Census Bureau's disclosure-avoidance noise, which matters little at county
totals.

## Soil moisture on the Field view (Agriculture)

The Field view opens on the 2024 Kansas aerial imagery at field scale. Its dock
adds **Show soil moisture**: NASA SMAP Level-4 (SPL4SMAU V008) modelled soil
moisture, through the Explorer's own soil-moisture control
(`app/soil-moisture-control.tsx`).

- SMAP cells are 9 km across; at field scale one cell would fill the screen and
  read as a per-field value it is not. Switching the tool on therefore pulls a
  closer view out to zoom 7.2, the region the cells describe.
- **Surface 0–5 cm** and **Root zone 0–100 cm** switch the modelled depth.
- The reading names the frame actually drawn (its UTC day and depth), or says
  plainly that NASA is unavailable and nothing is drawn; NASA's own colour scale
  sits beneath it.
- Soil moisture stays with the maps that offer it: opening another category map
  hides it.
- The control now checks NASA's available days whenever it is switched on from
  outside its own row (the dock, or a shared link that restores `soil=1`), not
  only from its switch.

## U.S. Drought Monitor on the Field view (Agriculture)

The Field view dock's **Show the Drought Monitor** draws the weekly U.S.
Drought Monitor (`app/drought-monitor.ts`, served by `/api/drought-monitor`
and `/api/drought-series`). The USDM is the drought assessment the National
Drought Mitigation Center, USDA and NOAA authors draw each week from many
indicators and local reports. Each map is valid for a Tuesday (8 a.m. Eastern)
and released that Thursday.

- **Source.** The week's national GeoJSON from droughtmonitor.unl.edu
  (`usdm_YYYYMMDD.json`), read through the bounded, allowlisted fetch and cut
  on the server to Kansas with about a degree around it (103.2–93.6°W,
  36.2–40.8°N) before it is sent. Only the five categories (`DM` 0–4) are kept.
  The newest map is the one released by Thursday 8:30 a.m. Eastern; when a
  release is late (a holiday), the week before is answered. A past week is
  kept as published, and the newest is read again hourly.
- **Symbols.** The USDM's own colours, nearly opaque, as the USDM draws its
  map: D0 abnormally dry (yellow), D1 moderate, D2 severe, D3 extreme and D4
  exceptional drought (dark red), worse categories over milder ones, with thin
  dark edges. The areas sit above the base and under the site's labels and
  overlays. Showing it from the field-scale view pulls the map out to the
  state.
- **Kansas over time.** The dock charts Kansas's weekly share of area in each
  category or worse since January 2000, from the USDM data services' state
  statistics, as the USDM draws its time series. A click on the chart, the
  Week slider, or Week before / Week after shows that week's map; Newest
  follows the newest release. A dragged slider settles before a week is read,
  and the last map drawn stays on screen while the next loads. **Play** steps
  forward a week at a time, holding each week 1.2 s once it is drawn, to the
  newest; from the newest it starts a year back. It stops on a week that does
  not answer, and choosing a week by hand pauses it. With reduced motion set,
  Play is off and the weeks are stepped by hand; the reading is not announced
  every week while it plays.
- **Counties.** With the map shown, the site reads the Census 2020 Kansas
  counties it already uses for search and People, and draws their lines over
  the categories, under the state line, as the USDM's state maps do. Each
  county's share in each category or worse is measured on the map at the
  centres of a 0.02° grid (about 200 points a county), weighted by area. The
  dock says how many counties each category reaches (any part of the county)
  and lists the counties most severe first (highest category, then the most of
  the county in it); choosing one outlines it, frames it, and gives its shares
  for the week. A click on a county on the map picks it too (without moving
  the map), and brings a closed dock back to show it. The shares are the map's, not the USDM's county statistics.
- **Change.** **4-week change** and **12-week change** compare the week shown
  with the week 4 or 12 weeks before it, as the USDM's own change maps do.
  Each county is shaded by its change in the Drought Severity and Coverage
  Index (NDMC): the sum of its shares in D0 or worse to D4, 0 to 500, so one
  number weighs both the area and the intensity of drought. The scale
  diverges from a pale neutral within 10 points: greens for less drought,
  browns for more, in steps at 10, 50 and 100. The dock gives the statewide
  DSCI then and now (from the USDM statistics for both weeks when they are in
  hand, else measured on the maps), lists the counties most worsened first,
  and adds the picked county's change to its reading. The earlier week is read
  like any other; if it does not answer, the categories stay on the map. A
  week with no whole interval behind it (before 1 Feb 2000 for 4 weeks, 28 Mar
  2000 for 12) has no change drawn, and the dock says so. During Play each
  week waits for its earlier week, and the change last drawn stays on the map
  while the next one loads.
- **Reading.** The valid date, Kansas's share in drought (D1–D4), and in D2,
  D3 and D4 or worse. The USDM's own statistics are used for the week when
  they are in hand. Otherwise the shares are measured on the map at the centres
  of a 0.05° grid inside the state outline, weighted by area, marked "≈", and
  the reading says so.
- **Limits.** The USDM is a weekly expert assessment at a broad scale, not a
  forecast or a measurement at a field. D0 is abnormally dry, not drought.
  The USDM does not draw its polygons to the field scale of the Kansas aerial
  beneath. The statistics are read whether the service answers JSON or CSV,
  cumulative or categorical; a categorical answer is accumulated.

## NWS flood forecasts on the River network (Water)

**Show flood forecasts** puts the NOAA National Water Prediction Service
(NWPS) river gauges for Kansas on the River network, read through the site's
hydrology adapter (`/api/hydrology/noaa`). It is the river forecast the
National Weather Service issues for each forecast point, drawn as the NWS
draws it.

- **Gauges.** Each gauge is coloured by its NWS flood category at the latest
  observation: major (purple), moderate (red), minor (orange), action or near
  flood stage (yellow), no flooding (green), and grey or blue where the data
  are not current or no category is defined. A ring marks a gauge with an
  official forecast. The key says this is gauge status, not a flood warning.
- **List.** The dock sums the network up (in flood, near flood stage,
  forecast to flood) and lists every gauge with the worst of its observed and
  forecast categories first. Choosing one, or clicking it on the map while
  the view is on, rings it and draws its hydrograph.
- **Hydrograph.** The past week of observed stage as a solid line, the
  official NWS forecast dashed with its points, and a line at now, over the
  gauge's own action, flood, moderate and major stages as coloured bands.
  The vertical range always reaches the flood stage, so the distance to
  flooding is read off the plot. Once the water reaches flood stage, the
  range opens to the next stage above. Days are marked at Central-time
  midnight and times are given in CST or CDT.
- **Reading.** The latest observation and its category, then the forecast:
  its crest, time and category, and when the forecast was issued (or that it
  falls or holds steady, or that no forecast is issued). It ends with the
  flood stage and the gauge's record crest, flagged when NWS lists it on an
  old datum.
- **Units.** Stages and crests are taken in the units of the plotted series.
  A gauge forecast in flow takes the flow thresholds. Units that match neither
  draw no flood stages.
- **Refresh.** The gauge picked is read again every ten minutes while shown.
  Observations arrive every 15 to 60 minutes and forecasts a few times a day.
  The network shows only at the present map time.
- **Limits.** NWPS is an operational service, not an archive. Values may be
  provisional or revised. The categories are the gauge's, at the gauge: they
  are not a flood-inundation map. Warnings come from the National Weather
  Service.

## Crop history at a point (Field view)

With **Show crops (USDA CDL)** on, a click in Kansas reads that point's
Cropland Data Layer class for every year from 2008 to 2024, not only the year on
show (`app/crop-history.ts`, `/api/cropland/history`).

- **Timeline:** one bar a year, coloured by crop family: corn, sorghum,
  soybeans, sunflower, winter wheat, double crop, alfalfa or hay, fallow, grass
  or pasture, other. An unanswered year is dashed; a year with no class is a tick.
- **Pattern:** read only when at least five years are classified, in this order:
  - **Continuous corn:** corn in at least 80% of years.
  - **Grassland or pasture:** grass in at least 80% of years. This is the
    persistent-pasture reading for ranching.
  - **Corn–soybean rotation:** corn and soybeans each in at least 25% of years,
    and at least 60% of back-to-back corn or soybean years alternate.
  - **Mostly {family}:** one family in at least 60% of years.
  - **Mixed cropping:** none of the above.
- **Partial histories:** a year CropScape does not answer for is shown dashed and
  counted, never read as an absence, and no pattern is claimed from a partial
  history. Click the point again to retry.
- **Limits:** the pattern describes what the CDL recorded at one 30 m cell. It is
  not agronomic advice, and the CDL is less certain for minor crops and small
  fields.

The route reads the years a few at a time and keeps a complete answer a day per
point. The map's point is rounded to five decimals, the same precision as the
request, so the answer matches the point it was asked for.

## Soil survey at a point (Field view)

With **Show crops (USDA CDL)** on, a click also reads the SSURGO soil-map unit at
that point from USDA Soil Data Access (`app/crop-soil.ts`,
`/api/cropland/soil`), shown under the crop history.

- **Components:** the map unit's components, most of the unit first (at most
  eight). Each reads with its share of the map unit, drainage class, hydrologic
  group, and non-irrigated capability class (1 has the fewest limitations, 8 the
  most).
- **Water storage:** the map unit's water to 150 cm, a weighted average over all
  its components. It is shown once for the unit, not for each component.
- **No coverage:** a point with no SSURGO map unit says so; nothing is inferred.
- **Source unavailable:** the dock says so and no soil is inferred. Click the
  point again to retry; a failure is not kept.
- **Limits:** components are alternatives within the mapped area, not the soil at
  the point. Survey editions vary, and this reading carries no field history.

The route queries the point to five decimals, the same precision the page uses,
and marks an answer cacheable for a day; a failed answer is sent no-store.

## Growing degree days at a point (Field view)

With **Show crops (USDA CDL)** on, a click reads a fixed April 1–October 31
corn-method heat index at the nearest eligible Kansas ASOS airport station.
This is station context, not field conditions, a planting-date accumulation,
or a maturity prediction for the crop classified by USDA.

- **Method:** Fahrenheit daily high capped at 86, low floored at 50, average
  minus 50, floored at zero. Sum before rounding to whole °F-days for display.
  [Purdue Extension](https://www.agry.purdue.edu/ext/corn/news/timeless/HeatUnits.html)
  describes the modified corn method. Other crops require different methods.
- **Provider contract:** [IEM daily summary](https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?help)
  with `network=KS_ASOS`, the catalog's `sid`, inclusive dates,
  `var=max_temp_f,min_temp_f,precip_in`, `format=csv`, and `na=M`.
  Responses must identify the requested station/network/dates. Duplicate or
  invalid dates, malformed rows and identity mismatches fail closed.
- **Station discovery:** the [Kansas network GeoJSON](https://mesonet.agron.iastate.edu/geojson/network/KS_ASOS.geojson)
  supplies `sid`, `sname`, point coordinates, `tzname`, `archive_begin` and
  `archive_end`. Selection is within 150 km among archives overlapping the
  requested interval. Closed stations remain eligible for historical years.
  Archive overlap does not prove observation availability or coverage quality;
  the route does not silently substitute a farther station after missing data.
- **Precipitation:** `precip_in` is liquid-equivalent precipitation, including
  frozen precipitation. The IEM sentinel `0.0001` means trace: count trace days
  separately, never add it as measured depth. Missing values are never zero.
  A precipitation-only response can still be shown when temperatures are absent.
- **Day boundaries:** IEM combines local-calendar summaries and reported totals;
  airport summaries typically use local standard time (01:00–01:00 during DST).
  KFM preserves provider date labels. It conservatively waits until 02:00 in
  the catalog's Central or Mountain timezone to include the previous day.
  This time guard cannot prove source arrival or quality control. Due dates with
  absent observations remain missing; current/future dates are not yet due.
- **Uncertainty:** incomplete totals say **Partial**, with separate missing and
  pending counts. No-station, all-missing and provider-error states infer no value.
  Neither 214 returned rows nor zero missing fields proves full subdaily coverage,
  certified climate quality, uniform field weather, or suitability for decisions.
- **Caching:** only a fully elapsed season with every temperature and precipitation
  day is cached for one day in both browser and shared caches. Other results are
  `no-store`. The client uses `v=2` to avoid prior cached calculations. Legacy
  responses without rainfall fields remain readable and explicitly say precipitation
  is unavailable; partially present or inconsistent fields are rejected.
- **Provider load:** GDD and frost daily requests share a bounded per-process queue,
  in-flight deduplication and a 2.1-second gap after each request. Multiple runtime
  processes still require a shared egress limiter to meet IEM's per-IP policy.
- **Year:** change the crop year, then click again. Source retrieval time is not
  an observation time or evidence that a historical series will never be revised.

See [the source verification record](iem-field-verification-2026-10-30.md) for
captured source-format fixtures, independent totals, checks and deployment limits.

## Frost dates at a point (Field view)

With **Show crops (USDA CDL)** on, a click also reads the frost dates for the crop
year on show, at the nearest Kansas airport weather station (ASOS)
(`app/frost-dates.ts`, `/api/farming/frost-dates`).

- **Freeze:** a daily low at or below 32 °F. The reading gives the last spring
  freeze before July 1 and the first fall freeze from July 1 on, and the days
  between them.
- **Missing days:** a day with no reading could hide a freeze. A spring date is
  certain only when no day after it is missing; a fall date only when no day
  before it is missing. Otherwise the dock says that the freeze is not certain.
- **Days not yet due:** days after today are not counted as missing.
- **Source:** the Iowa Environmental Mesonet's daily summary for the station, for
  the whole year, and its network list of Kansas stations, which the degree-day
  reading now shares.
- **Limit:** a station's low, not the field's. A freeze can differ across a county.

A finished year with both freezes certain is kept a day; anything else is sent no-store.

## Season rain against normal at a point (Field view)

With **Show crops (USDA CDL)** on, a click also reads the season's rain for the crop
year on show against the normal at the nearest Kansas airport station
(`app/rain-normal.ts`, `/api/farming/rain-normal`).

- **Season:** the rain from April 1 to October 31 of the year on show, totalled in inches.
- **Normal:** the average of the ten years before it. A year counts only when every
  day in it was read, and a normal needs at least five such years.
- **Share:** the season as a percentage of the normal, shown only when the season
  has every day read.
- **Caching:** each complete station-year is kept on the server, so repeat clicks
  read only the years that could not be read before.
- **Limit:** a station's rain, not the field's. Rain varies across a county.

## Daylight through the year (Sky globe)

**Daylight through the year** charts every day of the current year at one
Kansas place (`app/sun-chart.ts`). It starts at the geographic centre of Kansas
in Barton County. Click the map or enter latitude and longitude with the keyboard
and submit **Chart location** to select another place. Coordinates use decimal
degrees, with negative longitude in Kansas. It is pure calculation: no source is read.

- **Method:** the NOAA solar equations (after Meeus) give the Sun's
  declination and the equation of time. Each event is solved from the hour
  angle and refined twice at its own time.
- **Altitudes:** sunrise and sunset are the Sun's centre 0.833° below a
  sea-level horizon (refraction and the Sun's radius). Civil, nautical and
  astronomical twilight end at 6°, 12° and 18° below it.
- **Check:** `tests/sun-chart.test.mjs` places NREL's Solar Position Algorithm
  Sun at every event within 0.01° of the intended altitude, which is a few
  seconds of time.
- **Chart:**
  - Days run across and Central clock time runs up, with midnight at the
    foot.
  - Daylight is gold between the sunrise and sunset curves. Civil, nautical
    and astronomical twilight are deepening blues, and solar noon is dashed.
  - Today is marked.
  - The steps in March and November are the clock changing, not the Sun.
- **Reading:** gives today's first light, sunrise, solar noon, sunset and last
  light, the day's length and its change from yesterday, and the year's
  longest and shortest days.
- **Mountain time:** Sherman, Wallace, Greeley and Hamilton counties keep
  Mountain time. All solar and Moon displays deliberately use Central time
  (CDT/CST), including for these counties: their local clocks read an hour
  earlier. The panel states this for every selection and does not infer a time
  zone from longitude. Central DST follows `America/Chicago`.
- **Outside Kansas:** map clicks and coordinate submissions use the existing
  simplified Census display outline in `app/kansas-orientation.ts`, including
  the Missouri River edge. Outside selections preserve the prior chart and
  marker and show a message. This is display scope, with the outline's stated
  simplification limits; it is not a legal boundary determination.

### The Moon

The same panel gives the Moon at the same place (`app/moon.ts`).

- **Tonight:** its phase name and lit fraction at 9 PM, and when it rises and
  sets that day.
- **Strip:** the next 30 evenings as discs, each lit as it will be. The lit
  limb is on the right while waxing, as seen from Kansas. The terminator is an
  ellipse of half-width r·|1 − 2f|.
- **Phases:** the next four principal phases, in Central clock time.

How it is calculated:

- **Phases:** Meeus, *Astronomical Algorithms*, ch. 49, with its periodic and
  planetary terms, converted to UT with the Espenak–Meeus ΔT. The tests
  reproduce his examples 49.a (new moon, February 1977) and 49.b (first
  quarter, January 2044) to a second.
- **Position:** the Astronomical Almanac's low-precision series gives the
  Moon's position for rising, setting and illumination. It agrees with
  Meeus's example 47.a to within 0.1°, and it puts every phase of a hundred at
  its 0°, 90°, 180° or 270° elongation within 0.5°.
- **Rising and setting:** these are the Moon's centre at 0.7275 π − 0.5667°,
  for parallax, refraction and the Moon's radius. They are found on a
  10-minute grid and refined by bisection, which puts them within a few
  minutes.

## Surface observations (Storm desk)

**Show surface observations** plots each Kansas-area airport observation
(METAR) as a meteorologist's station model (`app/surface-obs.ts`). It reuses
the site's own METAR route, `/api/aviation/metar` (Aviation Weather Center,
the latest observation per station, under 90 minutes old), so no new source
is added.

- **Station circle:** sky cover fills it by quarters: open for clear, a quarter
  for few, half for scattered, three-quarters for broken, full for overcast.
  An X marks an obscured sky and an M a missing report.
- **Wind barb:** points into the wind in knots, rounded to 5. Pennants are 50
  kt, full barbs 10 and half barbs 5. The barbs sit on the staff's clockwise
  side, toward lower pressure in the Northern Hemisphere. The barbs turn with
  the map because METAR directions are from true north. Calm and variable
  winds draw no barb and are labelled.
- **Text:** temperature (°F) is upper left in red and dew point lower left in
  green. The first present-weather group sits between them.
- **Picked station:** picking one, from the plot or a keyboard list, rings it.
  The dock decodes it:
  - temperature, dew point and relative humidity (Magnus);
  - the NWS heat index (Rothfusz with its adjustments, from 80 °F);
  - the NWS 2001 wind chill (50 °F or colder, wind over 3 mph);
  - wind, visibility, altimeter, ceiling or sky, and weather, followed by the
    raw METAR.
- **Current only:** away from the present map time the plots are held. While
  shown they are read again every five minutes, and a failed read clears
  them rather than leave old plots standing.

A station describes its own airfield; nothing is interpolated between
stations.

## Tornado record since 1950 (Storm desk)

**Tornado record since 1950** turns the Storm desk from current alerts and
radar to the record: every Kansas tornado in the Storm Prediction Center's
severe weather database. It uses the "actual tornadoes" file, one row per
tornado covering the whole track. Alerts and radar are hidden while it is
shown, and only those that were on come back.

- **Source.** `/api/tornado-record` reads the newest yearly file that
  answers (`1950-YYYY_actual_tornadoes.csv`, released each spring for the
  year before, trying back four years), cuts it to Kansas on the server, and
  keeps it for a day.
  - Columns are read by name, so a reordered file reads the same.
  - Kansas's rows are kept, together with multi-state tracks that start or
    end in Kansas.
  - Unknown values (-9) stay unknown, and an end point of 0,0 means no
    lift-off was recorded.
- **Tracks.** Each track is the straight line from touchdown to lift-off,
  the only path the database records. It is coloured by F/EF rating from
  light to dark red, is wider for stronger ratings, and the strongest are
  drawn last. Tornadoes with no lift-off point are drawn as touchdown points.
- **Ratings.** The F scale was used before February 1, 2007 and EF after,
  and the labels follow the date.
- **History.** Tornadoes per year as bars stacked by rating, weakest at the
  base. Clicking a bar, or choosing a year, narrows the map. A rating filter
  shows F/EF1 or stronger up to F/EF5.
- **Strongest and deadliest.** Up to 60, strongest first, then deadliest,
  then longest. Choosing one, or clicking its track, outlines and frames it.
  The dock then gives the date and time (CST), deaths and injuries,
  touchdown and lift-off, length and width, and whether it crossed states.
- **Limits.** Ratings come from damage, so a tornado over open country may
  be rated low. Reporting has grown since 1950, so counts of weak tornadoes
  are not comparable across decades.

## Kansas Legislature districts (Kansas representation)

The Government map's **District plan** group switches between the U.S.
House districts (Congress by Congress, as before), the 40 **Kansas Senate**
districts, and the 125 **Kansas House** districts.

- **Source.** The chambers are layers 8 (upper) and 9 (lower) of TIGERweb's
  `Generalized_ACS2025/Legislative` service. This is the same service and
  vintage as the 119th Congress districts: the 2024 plans, January 1, 2025
  geography, generalized to 1:500,000. They are read through
  `/api/state-legislature?chamber=senate|house` and kept for a day.
- **Complete edition or none.** Every district must arrive once, with
  Kansas's state code, and as a valid Kansas polygon, checked with the same
  rules as the congressional districts. A missing, repeated or extra
  district refuses the whole answer rather than drawing part of a plan.
  Areas in no district ("ZZZ") are dropped.
- **Map.** A faint fill to click, district outlines, the picked district in
  orange with a stronger fill, and district numbers. All of it sits under
  the site's own overlays. While a chamber is shown, the U.S. House
  districts are hidden, and they come back only if they were on.
- **Districts.** They are listed by number. Choosing one, or clicking it,
  outlines it and frames it.
- **Limits.** This is generalized display geography, not for deciding which
  district an address is in. Officeholders and elections are not shown.
  The Kansas Secretary of State publishes the official maps.

## USDA Cropland Data Layer (Field view)

**Show crops (USDA CDL)** draws the USDA NASS Cropland Data Layer: what was
planted in each 30 m cell, year by year from 2008 to the newest released
(`CDL_LATEST_YEAR`, raised once NASS releases a year, about February). It
is served by CropScape (`nassgeodata.gmu.edu`).

- **Map.** CropScape's WMS offers EPSG:4326 and Albers, not Web Mercator.
  `/api/cropland/tile` therefore takes a Web Mercator tile, asks CropScape
  for its corners in longitude and latitude, and passes the PNG through.
  - It draws from zoom 8 only: at that scale the two projections agree to
    under a pixel across a tile at Kansas's latitude, and the CDL is a
    field-scale map.
  - Tiles outside Kansas and its margin are answered empty without asking
    CropScape. A year's tiles are kept, since a released CDL does not
    change.
  - Cells are drawn sharp at 88%, under every overlay. The Drought Monitor
    stays on top.
- **Key.** Kansas's main classes in CropScape's colours: corn, sorghum,
  soybeans, sunflower, winter wheat, double-crop wheat/soybeans, alfalfa,
  fallow/idle cropland, and grassland/pasture. The note says the CDL has
  more than a hundred classes.
- **At a point.** While crops are shown, every click also reads the class
  of the field under it from CropScape's GetCDLValue, with CropScape's own
  colour as a swatch. For example: "At 37.980°N, 100.870°W, 2024: Winter
  Wheat (24)".
  - GetCDLValue takes NAD83 Conus Albers (EPSG:5070) coordinates. The site
    converts with the ellipsoidal Albers equal-area formulas and is tested
    against PROJ to the centimetre.
  - Choosing another year reads the last point again for that year.
- **Limits.** The CDL is classified from satellite imagery each season and
  checked against USDA farm records. It is accurate for the main crops and
  less so for minor ones, and single cells can be wrong.

## NLCD 2021 land cover (Landscape imagery, Field view)

**Show land cover (NLCD 2021)** draws the USGS National Land Cover
Database 2021. It is land cover classified from Landsat at 30 m, served by
the MRLC consortium's GeoServer (`mrlc_display:NLCD_2021_Land_Cover_L48`)
and drawn in NLCD's own colours.

- **Map.** 512-pixel Web Mercator WMS tiles. Cells are drawn sharp at 85%,
  over the base and other rasters and under every overlay, so watershed
  lines stay on top.
- **Key.** The 15 NLCD classes that occur in Kansas, each with its official
  code, name and colour. Perennial ice/snow (12) is left out.
- **At a point.** While land cover is shown, every click also reads the
  class of the 30 m cell under it, and whatever the click selects still
  selects. For example: "At 37.980°N, 100.870°W: Cultivated crops (82) ·
  planted/cultivated".
  - The lookup is MRLC's GetFeatureInfo through `/api/land-cover/point`, in
    or near Kansas only. Answers are kept for a day, since NLCD is a fixed
    product.
  - A new click replaces the last.
- **Limits.** NLCD gives a mapped class for each 30 m cell, not a field
  survey. Single cells can be wrong, field edges blur across cells, and it
  shows 2021.

## Rainfall, observed and forecast (River network, Field view, Storm desk)

**Show rainfall** has two views, as the NWS map services
(`mapservices.weather.noaa.gov`) render them:

- **Observed (MRMS).** The NWS Multi-Radar Multi-Sensor quantitative
  precipitation estimate (`obs/mrms_qpe`). It is the rain of the past 1, 3,
  6, 12, 24, 48 or 72 hours on a 1 km grid, in inches.
- **Forecast (WPC).** The Weather Prediction Center's quantitative
  precipitation forecast (`precip/wpc_qpf`). It is the liquid precipitation
  expected over the next 6 hours, Day 1, or 2, 3, 5 or 7 days from Day 1, in
  inches, issued twice a day.
  - Each window is one layer of the service: 7, 1, 8, 9, 10 and 11, drawn
    with the service's own symbols through its `export`.
  - The forecast areas are smooth polygons, so they are drawn with linear
    resampling.
  - The key is the window's layer from the service's legend.
  - Each view keeps its own window when you switch between them.

- **Map.** Tiles come from the service's `exportImage`, 512 pixels at a time
  in Web Mercator, drawn with the service's own raster function for the
  window (`rft_1hr` … `rft_72hr`).
  - Cells are drawn sharp (nearest neighbour) at 82% opacity, under the
    site's overlays.
  - Tiles are asked for again every quarter hour while shown, so the hourly
    update is picked up soon after it lands.
- **Key.** It is the service's own legend for the window, read through
  `/api/mrms-rainfall/legend` and kept for a day. Each class shows its label
  and the swatch the service drew, so the key and the map share colours
  exactly.
- **Present only.** The service keeps no history. Away from the present map
  time the rainfall is held, and the dock says so.
- **Limits.** The forecast is a forecast, not a measurement. The observed
  rain is a radar-only estimate, not corrected to rain gauges.
  It can be wrong under the melting layer, where the beam is blocked or
  overshoots, and in snow. It is an estimate of rain that fell, not a
  forecast or a measurement at a point.

## FEMA disaster record on Hazard watch (Disaster)

**FEMA disaster record since 1953** turns Hazard watch from current hazards
to the record: every Kansas declaration in OpenFEMA's Disaster Declarations
Summaries, read through `/api/fema-record`. The route reads OpenFEMA a page
at a time and keeps the record for 12 hours.

- **Declarations.** Rows are gathered by disaster number. A declaration's
  date is its earliest row's, and its counties are all its rows'.
  - A Kansas county code designates that county.
  - A statewide designation counts for every county.
  - Tribal designations are counted as skipped and not drawn.
- **Hazard families.** OpenFEMA incident types are gathered into severe
  storms and tornadoes, floods, winter storms, fire, drought, biological,
  and other. Each family has one colour.
- **Counties.** Each county is shaded by how many of the declarations in the
  view designated it. There are five equal classes of a round width, from
  one to the most, and none in a pale colour. The key gives the classes.
- **History.** Declarations per year are shown as bars stacked by family,
  which is also the family key. Clicking a bar, or choosing a year in the
  select, narrows the map to that year.
- **Filters.**
  - Major disasters (DR) only by default; a checkbox adds emergency (EM)
    and fire-management (FM) declarations.
  - A hazard select narrows to one family.
- **Counties list.** Counties are listed with the most declarations first.
  Choosing one, or clicking it on the map, outlines it. Its reading gives the
  count, the most frequent family and the latest declaration, and lists its
  declarations, newest first, each linked to its FEMA page.
- **Current hazards.** The alerts, fire detections and fire reports that
  were on are hidden while the record is shown, and only those come back
  when it closes.
- **Limits.** A county designation names a county as eligible for
  assistance. It is not a footprint of the damage. Declarations reflect
  federal policy as well as hazards: more counties are designated in recent
  decades.

## Saturated thickness on the Aquifer map (Groundwater)

The Aquifer map opens on the Kansas Geological Survey's 2022–2024 saturated
thickness of the High Plains aquifer: how many feet of the aquifer still hold
water. It is centred on western Kansas, where the aquifer is. Its dock switches
one KGS view at a time:

- **Thickness**, classes from under 50 to over 300 feet;
- **Depth to water**, from under 25 to over 350 feet below the land surface;
- **Extent**, where the aquifer is mapped.

The legend lists the KGS classes in feet with the colours the snapshots carry
(`GROUNDWATER_CLASS_LEGENDS`); `tests/aquifer-legend.test.mjs` keeps it equal to
the snapshot files in `public/data/groundwater/`. These are regional classified
estimates, not well measurements; Explore underground opens the recorded well
logs and cores.

### Water levels at wells

**Water levels at wells** shows the 2026 KGS monitoring network
(`kgs-monitoring-wells`) and makes each well pickable, by click or from a
keyboard list of the 40 wells nearest the map centre (refreshed when the map
stops moving). A picked well is ringed. The dock then reads its measured depth
to water from the USGS Water Data `field-measurements` collection
(`app/well-levels.ts`, served by `/api/well-levels?site=`). The measurements
are parameter 72019, in feet below land surface, and most are the January
readings KGS and USGS take while irrigation pumps are off.

- **Route:** follows the collection's `next` pages (same host and collection
  only, at most five pages of 1,000) and keeps a well six hours.
- **Missing values:** a measurement without a value (a dry, obstructed or
  pumping well), another parameter or another unit is left out, never read as
  zero.
- **Reading:** gives the latest depth (marked provisional when it is), the
  number of measurements and their years, and the net change in water level
  since the first measurement. It also gives the least-squares trend in feet
  per year over the whole record. Separately, it gives the trend over the
  last ten calendar years, when the record reaches further back and holds at
  least three measurements over five years.
- **Hydrograph:** plots depth increasing downward, as hydrogeologists draw
  it, so a falling water level runs down the chart. Each measurement is a
  dot, hollow while provisional, and the record's trend is dashed across it.
- **Dates known only to the month or year:** USGS writes `01` placeholders
  for an unknown month or day and gives null `month` or `day` fields. Such a
  measurement keeps that precision. It is labelled "1958" or "Mar 1962",
  never as a placeholder day. It is placed at the middle of its period for
  the trend, and the hydrograph draws a bar across the whole period. The
  reading says how many there are.
- **Links:** the dock links the well's USGS and KGS WIZARD records.
- **Failure:** if USGS does not answer, the dock says so and infers no
  level.

The wells the tool showed are hidden again when it closes. Wells that were
already on stay on. One well is one point in the aquifer: neighbouring wells
can differ by tens of feet.

## Reviewed snapshots from the site database

The River network, Storm desk, Hazard watch and Landform relief docks offer
**Reviewed … snapshots**: the hourly USGS discharge, NWS alert and USGS
earthquake captures that the site's
publishing pipeline normalized, checked against their signed manifest and
committed to the site's MySQL database (`server/pipeline-*.mjs`), read through
`/api/curated/{source}` and its `/history` (up to 20 releases).

- Gauges are circles whose area grows with discharge: radius = 3 + 0.06·√Q px
  (Q in ft³/s), from a 3 px floor and capped at 62,500 ft³/s. Provisional USGS
  values carry an amber ring, approved values a white one; a gauge without a
  value is not drawn as zero. While a snapshot is drawn, the dock keys the
  scale at 100, 1,000, 10,000 and 62,500+ ft³/s at the sizes drawn, and the
  two rings (`REVIEWED_DISCHARGE_KEY` in `app/map-keys.ts`, which the gauge
  layer also reads). Reviewed alert snapshots share the live NWS severity key.
- Alert areas take their NWS severity colour; alerts that have expired leave
  the display, as on `/curated`.
- Earthquakes draw as the live catalog does (colour and size by magnitude),
  ringed amber for an automatic USGS solution and white once an analyst has
  reviewed it (`REVIEWED_EARTHQUAKE_KEY`). Retracted events are not published.
  See `docs/second-pc-pipeline.md` for what the release keeps and the owner
  steps before it publishes.
- Selecting a gauge, alert area or earthquake in a shown snapshot shows it in
  the dock in its own source's terms (discharge with unit and approval status;
  alert severity, urgency, certainty, effective and expiry times and areas;
  magnitude, place, depth, time and USGS review state), outlines it on the map,
  and names the release it belongs to with that release's signed JSON download.
  It is a released record, so it is not opened as basemap context. Links are
  built only from identifiers the pipeline checked (the USGS station page from
  a `USGS-` site number, the event page from the event id). The selection lapses
  when the shown snapshot no longer holds the feature.
  **Features in this snapshot** lists up to 40 of the shown release's features,
  most significant first (earthquakes by magnitude, gauges by discharge, alerts
  by NWS severity), and says when the release holds more; choosing one selects
  it as a map click does and moves the map to it, or to the middle of an alert
  area's extent.
- The scrubber runs oldest to newest; each step names the hour the capture is
  for, when it was published and how many features it holds, and says when it
  is older than two hours. Play steps forward and stops at the newest.
- A release is shown only while its publication approval holds: the history
  is read again every minute, so a release whose approval lapses or is revoked
  leaves the scrubber, and a shown release leaves the map the moment its own
  `approvalExpiresAt` passes. With no release picked, the newest is followed as
  new ones are published.
- A newly picked release reads as loading until it is drawn, and Play steps on
  only after each release has been drawn.
- When the pipeline is not switched on, has no approved release, or the
  database is unavailable, the dock says so and nothing is drawn.

The snapshots are drawn by the context renderer (`app/reviewed-snapshot-layers.ts`)
and are approved context releases, not admitted evidence.

## Map keys

A map whose starter layers encode a value shows a key for each one in its
dock, while that layer is on (`app/map-keys.ts`). The layer styles and the keys
read the same constants, so the two cannot drift apart:

- **Earthquake magnitude** (Landform relief): USGS magnitude; colour and
  circle size both rise with it. The key draws M 0, 2, 4 and 6+ at their
  statewide (zoom 4) sizes.
- **NWS alert severity** (Storm desk, Hazard watch): the alert's CAP severity,
  as one ordinal palette for live and reviewed alerts alike. It runs from pale
  yellow (Minor) through orange and red to magenta (Extreme, the Storm
  Prediction Center's colour for its highest risk), each step more salient on
  the dark storm base. An alert without a recognised severity is neutral grey,
  off the scale.

- **Satellite fire detections (VIIRS)** and **Reported fire incidents
  (NIFC)** (Hazard watch): a detection is a dot at its pixel centre coloured
  by detection confidence (with the dashed scan × track pixel close in); a
  reported incident is a ring coloured by incident type. The two datasets no
  longer share a symbol, and nothing animates (`docs/fire-close-zoom.md`).
- **KDOT roads and rail** (Network map) and **1918 roads and former rail**
  (Historic atlas): the lines KDOT's service draws with our symbols
  (`KDOT_LINE_SYMBOLS`), so the request and the key share them. Public roads
  are amber, active railroads teal, 1918 state highways brick red, and
  abandoned railroads violet and dashed; dashes mean former rail only. The
  KDOT colours had been chosen for the dark default map: on the Network map's
  near-white ground and the Historic atlas's parchment they reached only
  1.04–1.3:1, and the 1918 roads and abandoned rail were the same orange dash.
  Each colour now has at least 3:1 against both the light category grounds
  and the dark ones, and no two datasets share one. Lines of one map are
  keyed together under one title.
- **Elevation** (Relief model, Landform relief, Aviation chart): the basemaps
  that colour the ground by height show their ramp as a bar, first in the
  dock, while that basemap is drawn. The bar is built from the same stops the
  style uses (`RELIEF_RAMP`, `AVIATION_TINT_BANDS` in
  `app/category-basemaps.ts`). The relief key is continuous, in metres above
  sea level (200–1,300 m, ticks every 300 m). The aviation chart's key is
  stepped into its 1,000 ft bands and labelled in feet, as sectional charts
  are. Both notes give the state's span, 207 m (679 ft) where the Verdigris
  River leaves Kansas to 1,231 m (4,039 ft) at Mount Sunflower, so a reader
  can turn a colour into a height. The key is gone when the basemap is not
  (photo-real ground, or the local fallback style).

Radar keeps its dBZ legend in its own panel, and stream gauges keep theirs in
River Pulse.

## Earthquake record (Landform relief)

The Landform relief dock's **Earthquake record since 1973** replaces the rolling
30-day catalog with every USGS ComCat earthquake of magnitude 2.5 or more whose
epicentre lies inside Kansas, from 1 January 1973 to now
(`app/earthquake-record.ts`, served by `/api/earthquake-record`).

- **Source and clip.** One FDSN event query over the state's bounding box,
  oldest first, kept on the server for six hours. Events in the box but outside
  the Census state outline (northern Oklahoma, north-west Missouri) are dropped
  and counted; the outline is accurate to a few hundred metres, finer than the
  catalog's epicentre uncertainty. If the provider returns more than 6,000
  events the reading says the answer was cut short.
- **Symbols.** Size is magnitude, on the record's own scale (it holds far more
  events than 30 days). Colour is the year: 1973–2009 share one dark violet,
  when Kansas had few seismometers and few M2.5+ events, then the perceptually
  ordered "plasma" ramp runs from 2010 to the current year, so the rise in
  south-central Kansas after 2013 is read by colour as well as by place. Larger
  events draw on top.
- **Histogram.** The dock charts events per year in each year's map colour, so
  the chart is also the colour key. A bar, or the Year list, shows one year on
  the map; the reading gives the count and the busiest year.
- **Selection.** Selecting an event shows its magnitude and magnitude type,
  UTC time, USGS place, depth and review status in the dock, with a link to the
  USGS event page. The basemap beneath is not inspected. The dock also lists
  events as buttons, so one can be chosen by keyboard or screen reader: with a
  year shown, that year's events newest first; across all years, the 40
  largest. The list says when it holds fewer than all ("40 of 89"). Choosing one selects it and moves the map to it (without motion when
  reduced motion is set).
- **Depth section.** Under the histogram the dock draws the record (or the
  chosen year) as a west–east cross-section of Kansas: each event at its
  longitude and USGS depth, sized by magnitude and coloured by year as on the
  map, with the selected event ringed; a click on an event selects it. Depth
  is the least certain coordinate of a Kansas earthquake: where USGS could not
  resolve it, it is often held at a set value, so the caption counts events at
  exactly 5 or 10 km and those without a depth.
- **Magnitude–frequency.** A Gutenberg–Richter plot of how many events were of
  each magnitude or larger (log scale), with the maximum-likelihood line
  log10 N = a − bM. b is the Aki–Utsu estimate for magnitudes binned to 0.1
  above the record's M2.5 floor, with the Shi & Bolt (1982) standard error,
  given only from 50 events. The record mixes magnitude types (mb_lg, ml,
  Mw), and M2.5 was not complete before the post-2013 stations, which flattens
  b for the whole record; the plot says the types are mixed.
- **Limits.** Detection improved as seismometers were added after 2013, so early
  decades miss some small events and counts across decades are not directly
  comparable. Locations, magnitudes and review status can be revised by USGS.
  Hiding the record brings the 30-day catalog back; leaving the map closes it.

## SPC convective outlook (Storm desk)

The Storm desk dock's **Show the SPC severe outlook** draws the NOAA Storm
Prediction Center's convective outlooks (`app/spc-outlook.ts`, served by
`/api/spc-outlook?day=&product=`), beside radar and alerts: the categorical
**Risk** for Day 1, 2 or 3, and the **Tornado**, **Wind** and **Hail**
probability outlooks for Day 1 or 2.

- **Source.** SPC's own `dayNotlk_cat.lyr.geojson` and, for a hazard,
  `dayNotlk_{torn,wind,hail}.lyr.geojson` with its conditional-intensity file
  `dayNotlk_cig{torn,wind,hail}.lyr.geojson`. Each is kept ten minutes on the
  server and re-read in the browser once shown for a quarter-hour, since SPC
  reissues Day 1 several times a day. Only SPC's six categories (TSTM, MRGL,
  SLGT, ENH, MDT, HIGH), SPC's probability bands (tornado 2, 5, 10, 15, 30, 45
  and 60%; wind 5, 15, 30, 45, 60, 75 and 90%; hail 5, 15, 30, 45 and 60%, read from `DN` or the `LABEL`
  fraction) and the intensity groups CIG1–CIG3 (hail CIG1–CIG2) with valid
  polygons are drawn; provider properties other than the band do not travel.
  An empty outlook, which SPC sends as a bare GeometryCollection, reads as
  below the lowest band. If the intensity file does not answer, the
  probabilities are drawn without it.
- **Intensity.** Since March 2026 SPC marks conditional intensity instead of
  the hatched "significant" areas: level 1 where significant severe weather is
  possible (EF2+ tornadoes, 65 kt+ gusts, 2 in+ hail), higher levels where
  storms that form could be more intense. An older `SIGN` area is read as
  CIG1.
- **Symbols.** Outlines, not fills, so radar reflectivity keeps its colours.
  Categories are drawn in SPC's category fill colours; probabilities in SPC's
  hazard hues (tornado green, brown, yellow, red, magenta, purple, blue; wind
  and hail brown, yellow, red, magenta, purple, with wind's 75% and 90% in blue
  and cyan), lightened where needed to stay
  legible on the dark storm base. Intensity areas are dashed white lines,
  heavier with each level. Higher bands lie inside lower ones, as SPC layers
  them. The key lists the bands drawn for the product shown.
- **Reading.** The highest category, or the highest probability within 25
  miles of a point, reaching Kansas (tested every 0.1°, about 10 km, inside the
  Census outline), the highest intensity level reaching Kansas, the outlook's
  issue time and valid period in UTC, and a link to SPC's outlook page.
- **Limits.** The outlook is a forecast of risk, not an observation, a watch or
  a warning. Day 3's probability of any severe weather and Days 4–8 are not
  drawn; a hazard chosen on Day 3 shows the categorical risk until Day 1 or 2
  is chosen. Leaving the map closes the outlook and returns it to Risk.

### High wind probability regression coverage

The missing 75% and 90% wind bands in PR #5536 were corrected by
[PR #5537](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5537),
merged as `ddafc3d1410bc7e2d23ed9ae6164f71a3e07ba38` on October 28, 2026.
The follow-up inspection at hosted-branch source revision
`b09a9b5fa2c62999d4c228573a69fcfbdbbecbb1` confirmed that correction.
[NOAA's wind renderer](https://mapservices.weather.noaa.gov/vector/rest/services/outlooks/SPC_wx_outlks/MapServer/15)
lists both bands, blue then cyan; the application's lightened colors are
`#5f9fe0` and `#4fe3e3`.

Deterministic synthetic tests in `tests/spc-outlook.test.mjs` cover each
band through DN and LABEL-only parsing for Days 1 and 2, compact and ISO forecast
clocks, Kansas-crossing Polygon/MultiPolygon contours, out-of-state maxima,
polygon holes, feature ordering, client validation, evaluated MapLibre paint,
legend agreement, intensity separation and unchanged tornado/hail ladders.
`tests/outlook-verification.test.mjs` checks high-band report counts and
excludes other hazards and reports outside the forecast's valid period.

Run both with:

```sh
node --test tests/spc-outlook.test.mjs tests/outlook-verification.test.mjs
```

These fixtures establish behavior for those inputs. They are not a current
Kansas forecast, a live SPC acquisition check, native GPU/browser acceptance,
or proof of public deployment. Kansas-wide maxima retain the 0.1° sampling
limit above: a contour narrower than that spacing can be missed. This follow-up
adds tests and documentation only; it does not change runtime behavior or
publish an application.

## SPC storm reports (Storm desk)

The Storm desk dock's **Show SPC storm reports** draws the Storm Prediction
Center's preliminary local storm reports for **Today** or **Yesterday**
(`app/storm-reports.ts`, served by `/api/storm-reports?day=`), so the outlook
and what was reported can be read on one map, as SPC verifies its outlooks.

- **Source.** SPC's `today_filtered.csv` and `yesterday_filtered.csv`: reports
  to the National Weather Service for one convective day, 12:00 to 11:59 UTC,
  with duplicates near in time and place removed by SPC. The file has three
  sections (tornado, wind, hail), each opened by its own header row; columns
  are time (HHMM UTC), magnitude (EF rating, gust in mph, or hail size in
  hundredths of an inch), location, county, state, latitude, longitude and
  comments. Times before 12:00 UTC are placed on the morning that ends the
  convective day. Coordinates written as hundredths with west longitude
  positive are read as SPC means them; rows without a position are left out.
  Today's file is kept five minutes on the server and re-read every five in
  the browser; yesterday's, thirty.
- **Symbols.** Points in SPC's report-map colours (tornado red, wind blue, hail
  green), tornadoes drawn over wind over hail. Significant reports, at SPC's
  thresholds of EF2 or stronger, 75 mph (65 kt) or more and hail 2 inches or
  larger, are larger and ringed in white. The points sit above the outlook
  lines and under the site's labels.
- **Reading.** Kansas reports by kind with the significant count, the national
  total and the convective day in UTC. Selecting a report shows its kind,
  magnitude as SPC states it, time, place and the NWS office's remarks.
  **Kansas reports** in the dock lists the Kansas reports newest first (up to
  40), each a button with its time, kind, magnitude and place, so a report can
  be chosen by keyboard or screen reader as well as on the map; choosing one
  selects it and moves the map to it (without motion when reduced motion is
  set).
- **Against the outlook.** With today's reports and the Day 1 outlook both
  on the map, the dock adds how the reports fall against it, as SPC verifies
  its outlooks: only reports made inside the outlook's valid period count; the
  categorical outlook is checked against every report and a tornado, wind or
  hail outlook against reports of its own hazard; each band counts the reports
  inside it or a higher band, since SPC's areas nest, with the rest counted
  outside every area (`app/outlook-verification.ts`). Day 2 and 3 outlooks and
  yesterday's reports are not compared: they do not cover the same period.
- **Limits.** Preliminary and unverified: reports can be revised, merged or
  removed, an unknown EF rating or gust speed stays unknown, and positions are
  where the report was made, not a damage track. Storm Data and NWS damage
  surveys are the verified record. Leaving the map closes the reports.

## High-definition rendering and real ground

Every map draws at the screen's own density and on real terrain.

- **Render density.** The map renders at the device pixel ratio: up to 2× on
  Balanced (desktop and touch alike; it had been capped at 1.5× and 1.25×), up
  to 3× on High detail, and 1× only on Battery saver or with the browser's
  Save-Data preference (`app/map-performance.ts`). The wind-arrow and water
  motion canvases draw at up to 2×.
- **Provider overlays.** ArcGIS MapServer exports (KDOT, KGS aquifers, BLM,
  FEMA, WBD, NWM and the rest) are requested at 512 px and 192 dpi on screens
  of 1.5× or more, so each CSS pixel has two image pixels and ArcGIS keeps the
  symbols their on-screen size (`app/hd-rasters.ts`).
- **Imagery.** Esri world imagery and the 2024 Kansas one-foot aerial are
  declared at half their tile size on those screens, so MapLibre draws the
  next, finer zoom level. The USGS topographic map and OpenStreetMap keep their
  tile size: their labels and symbols are baked into the tiles, and the next
  zoom level would draw them at half size.
- **Real ground everywhere.** The local styles (Prairie dusk, under the Aquifer
  map, and Midnight navy, the fallback when the vector basemap cannot load)
  now shade the Terrarium DEM under the state line, so no map sits on an empty
  colour; the outline still draws offline. Every category base's hillshade is
  at least 0.38 exaggeration (the storm base's had been 0.18, too faint to
  read on its dark ground). The basemap DEM loads to zoom 12, about 38 m per
  pixel, for crisper valleys and breaks at county and city scales.
- **Satellite and 3D views.** NOAA GOES GeoColor and visible frames (the
  Satellite view's subject) are requested at 512 px on those screens; they are
  imagery without symbols, so they only gain detail. The Explore underground 3D
  view renders at up to 2× (it was capped at 1.5×), like the aquifer volume.
- **Close 3D relief.** The 3D views open on the Mapzen display DEM, capped at
  zoom 11. Past zoom 11.5 over Kansas, where that DEM is only overzoomed, the
  map moves to the live USGS 3DEP mosaic (the "Kansas detail" carrier the
  photo-real view uses) and says so. If 3DEP fails to load there, the map goes
  back to the display DEM once and says so, instead of staying degraded; a DEM
  chosen by hand in Appearance is never overridden.
- **Not changed.** NOAA radar keeps nearest-neighbour 256-pixel frames, so each
  radar cell stays an exact cell and the loop's downloads stay bounded. NOAA
  lightning density stays at 256 px: its density cells are about 8 km.

## Photo-real 3D (Terrain)

The Relief model dock's **Photo-real 3D** drapes the photographed ground on the
measured one: the 2024 Kansas NG911 one-foot aerial (over Esri world imagery,
which carries oblique views past the state line) on the USGS 3DEP bare-earth DEM
(`/api/3dep-dem-tile`), at **true vertical scale** (1×), lit by the real sun at
the map centre, with OpenStreetMap buildings raised to the heights OpenMapTiles
records (`render_height`, from `render_min_height`). The style is the
`photoreal` basemap: no labels, painted shading or stylisation over the
photograph. The photograph carries the real light of its flight, so the DEM
hillshade is not drawn while it is loaded, and the USGS 3DEP hillshade, if
switched on, is switched off on entry and back on with "Back to relief
colours".

It flies to six real landscapes (`app/photoreal-landscapes.ts`), each captioned
with what the ground is: the Red Hills (Permian red beds capped by gypsum),
Monument Rocks and Little Jerusalem (Niobrara Chalk), Konza Prairie in the
Flint Hills (Permian limestone and chert under tallgrass prairie), the Arikaree
Breaks (canyons in loess), and downtown Wichita on the Arkansas River. The
reading always states the vertical scale: "True vertical scale (1×)" or the
exaggeration chosen with Relief. The status bar's DEM readout gives the 3DEP
height under the pointer. "Back to relief colours" restores the look's own map,
the Mapzen relief and the default depth.

## What is not on every map

County boundaries, USGS river gauges, the USGS 3DHP stream network and the fire
layers (NOAA-20 fire detections and NIFC fire reports) are **off by default**;
the plain Explorer starts with no provider layer. They appear on the maps whose
subject they are (the civic map starts with 119th Congress districts, community and reference maps with counties;
the water map with its gauges; Hazard watch with alert areas, fire detections
and fire reports) or when a visitor turns them on. The county payload still loads once
in the background so **Find a county** works; loaded but hidden layers are not
drawn (`searchNeedsCounties`).

The category basemaps follow the same rule. County lines are drawn only on the
civic style; river lines only on the river network and, as chart landmarks, the
aviation chart. Lakes stay in every style as water fill.

## In the Evidence Drawer

A selected record now opens with the category it belongs to, then the same
three questions for every source (`app/evidence-summary.ts`):

- **What it is** is the record's own summary. A provider basemap record is
  labelled as the provider's mapped record.
- **Where & when** gives the spatial scope and display anchor, then the
  observation or source time. The second clause is labelled by what it is:
  "retrieved …" for an official feature's retrieval time, "listed freshness: …"
  when only the source's cadence is known, and "record updated …" for a
  registry record. A provider basemap record gets no update clause.
- **Source & limits** gives the organization, the evidence state (a basemap
  record stays "External context only · no KFM EvidenceBundle") and the
  recorded generalization and uncertainty.

  When no limitation is recorded, the drawer says so rather than implying
  none.

Categories come from the same source-identity rules as the Layers catalogue:
`officialSourceTopics` or `registryLayerTopics`. When that category's map look
is not already on screen, the drawer offers **Open the {map look}**. The
summary only restates fields the selection already carries; the existing
Data, Metadata, Trace and Focus tabs are unchanged.

## Specialized basemaps

Seven category styles live in `app/category-basemaps.ts`, listed with their
picker title, network note and legend in `CATEGORY_BASEMAPS`. Their keys are in
the import-free `app/category-basemap-keys.ts`, which the allow-lists share.
They are built only from carriers already listed in
`app/external-context-sources.ts`:

- OpenFreeMap vector tiles and fonts (`openfreemap-liberty`);
- the Terrarium display DEM (`aws-mapzen-terrarium`), for relief;
- the bundled Census Kansas boundary (simplified for state-scale display) and graticule.

Both carriers disclose every category key in `activatesWhen`. No sprite is
requested: symbols such as airport circles and peak triangles are drawn or set
in text.

| Key | Map look | Used by |
|---|---|---|
| `aviation-chart` | Aviation chart | Aviation |
| `civic` | Government & civic | Government, People, Places |
| `hydro` | River network | Water |
| `relief` | Relief model | Terrain, Geology |
| `storm` | Storm desk | Weather, Hazards |
| `network` | Network map | Transport, Engineering |
| `historic` | Historic atlas | History |

### Aviation chart (`aviation-chart`)

A reading of a VFR sectional chart:

- elevation bands at 1,000 ft steps (`AVIATION_TINT_BANDS`), drawn as a
  `color-relief` whose interpolate stops pair one metre apart for hard chart
  edges, plus hillshade;
- yellow built-up areas, quiet blue water and magenta roads;
- a dashed state line and a dashed 1° graticule;
- OpenMapTiles `aeroway` runways, taxiways and aprons;
- `aerodrome_label` airports as circled symbols, coloured by class (military,
  private, other), with ICAO/IATA identifiers and, from zoom 10, the airport
  name.

It is display context. It is **not for navigation**, flight planning or drone
authorization, and it does not replace current FAA charts, NOTAMs or TFRs.

### Government & civic (`civic`)

A light reference map:

- state, county (`admin_level` 6) and municipal (`admin_level` 8) boundaries
  are the subject;
- land, water and roads recede, with a faint hillshade;
- place labels are sized by rank, and state capitals carry a star.

Government & civic opens **Kansas representation** with Census 119th Congress districts at Present. Its Congress selector and shared calendar reach back to Kansas statehood on January 29, 1861. Earlier plans use pinned Lewis–DeVine–Pitcher–Martis historical reconstructions; they are not labeled as direct government observations. The welcome preview retains the four present districts and points to history in the full map. Colors identify district numbers, not parties or continuous identities. At-large constituencies are explicitly labeled, may elect multiple members, and use a dashed statewide outline when numbered districts coexist. Map selection and the variable keyboard list open dated source details; the dock offers selected-plan GeoJSON, retry, source links and optional county comparison. People and Places retain their county starter.

Congress choices span 36–119. Historical terms use March 4 before 1935 and January 3 thereafter; the first Kansas interval is clipped to statehood. Year-only frames use January 1, so the 1861 annual frame is withheld until a supported exact date is selected. Missing, mismatched or failed plans clear/withhold old geometry. Pre-statehood territorial geometry remains unverified; no future Congress is inferred. See [sources, request bounds and verification limits](civic-districts.md). Display geography does not determine voting eligibility or legal boundaries.

### River network (`hydro`)

- deep-water ground with a lifted hillshade, so the drainage pattern reads even
  before vector tiles load;
- rivers, canals and streams scaled by class, each with a soft glow, canals
  dashed;
- lakes and wetlands;
- river names follow their courses, and towns are labelled quietly.

It shows display geography, not measured flow or watershed boundaries.

### Relief model (`relief`)

- a smooth hypsometric tint (`RELIEF_RAMP`, a `color-relief` from about 150 m
  to 2,500 m) under the strongest hillshade of the set;
- lakes, main roads, peaks and towns stay quiet.

It is mixed-source display elevation, not survey measurement.

### Storm desk (`storm`)

- a neutral charcoal ground; every colour in the style has low chroma, so
  radar, alert and fire colours stay distinguishable;
- the state line and town labels show where weather is hitting.

Weather layers keep their own clocks.

### Network map (`network`)

- road classes in colour (motorway, trunk, primary, secondary), white-cased,
  with darker casing on bridges;
- route numbers from `transportation_name`;
- classic dark rail with white ties, plus runways.

It is display context, not traffic, condition or access.

### Historic atlas (`historic`)

- a parchment ground with a sepia hillshade and the bundled 1° graticule;
- railroads are the subject: an ink line crossed by ties, the way atlases drew
  the lines that placed Kansas towns;
- the state line is dash-dot;
- modern roads, urban areas and water recede;
- city names are letter-spaced capitals.

It is present-day OpenMapTiles geography drawn in an atlas style, not a
historical map. The History look adds the dated layers on top: the digitized
1918 road map and abandoned railroads, each with its own source limitation.
OpenFreeMap provides only Noto Sans, so the atlas feel comes from spacing,
case and colour rather than a serif face.

### Shared behaviour

- **Fallback.** All seven styles use the `openmaptiles` source id. If that carrier
  fails, the existing fallback swaps to the local Midnight style
  (`VECTOR_BASEMAPS`, `shouldFallbackStandardBasemap`).
- **Globe.** Vector basemaps stay on the globe. Raster ones still hand over to
  the standard style there.
- **Relief.** Each style draws its own hillshade under
  `CATEGORY_BASEMAP_HILLSHADE_LAYER_ID`. The 2D relief scene effect and, in
  3D, the terrain hillshade (`kfm-terrain-hillshade`) both defer to it, so
  shading is never doubled. The overlay sync lights it as the scene is lit:
  from the sun's direction and at its height (held between 12° and 60°), so
  the real sun lengthens and turns its shadows. The Relief model no longer
  starts with the USGS 3DEP hillshade, whose fixed multidirectional light
  would contradict the scene's sun; it stays in Layers for finer detail.
- **Contrast.** `LIGHT_CATEGORY_BASEMAPS` marks the light grounds, so wind
  arrows draw dark strokes there and light strokes on `hydro` and `storm`.
- **Persistence.** Saved views, snapshots, report attribution and wind-arrow
  contrast all accept the new keys.

## Limits

- The vector layers of all seven styles were validated against the MapLibre
  style specification and by tests. Their relief, tint and outline layers were
  rendered in a browser. It was not rendered against live
  OpenFreeMap tiles in the build container, which cannot reach that host.
- The aviation chart basemap draws airports from OpenStreetMap data, not the
  FAA NASR airport list, and carries no airspace itself. The Aviation look
  switches on the separate airspace layer (`overlays: ["aviation"]`, see
  `docs/aviation-layers.md`), which draws FAA NASR airspace as 3D volumes or a
  2D chart, airports, drone ceilings, TFRs, weather and live traffic.


## Storm desk startup and resource budget (October 27, 2026)

The starting set is **NOAA radar + active NWS alerts**, in 2D over the existing
neutral dark base. Radar opens on the latest advertised exact scan, paused and
following the latest manifest. The user starts playback explicitly. Radar
reflectivity, an issued alert and forecast risk are different products; they
retain separate source clocks, limitations and legends. Missing imagery is
never an all-clear. KFM is not an emergency warning service.

The dock shows separate starting-layer switches and a collapsed **Add related
context** group. GOES GeoColor, forecast wind, 15-minute ground-network lightning
density, HMS smoke footprints and USGS river gauges use existing provider
handlers. They start off. Smoke and streamflow also appear in the Weather
catalogue, so they remain discoverable on phones when the radar panel occupies
the dock's space. SPC Day 1/2/3 outlook and reviewed alert snapshots remain
separate, optional tools. The historical NASA lightning climatology remains in
the full catalogue rather than the short current-storm list.

| Layer | Reason for placement | Interpretation limit |
|---|---|---|
| Radar, on | Recent observed reflectivity is the map's primary storm view | Not a ground rain gauge, forecast, warning or complete coverage proof |
| NWS alerts, on | Issued event, severity and expiry complement radar | Inspect the official message; KFM is not the issuing authority |
| SPC outlook, off | Optional forward risk context | Forecast risk, not a warning |
| GOES satellite, off | Cloud structure beyond radar echoes | Has its own scan time and may obscure radar |
| Forecast wind, off | Wind-field context | Modeled guidance, not measured storm motion |
| Ground-network lightning density, off | Dated electrical-activity context | Aggregated density, not individual strike locations |
| HMS smoke, off | Nearby atmospheric context | Imagery interpretation, not surface air quality |
| USGS gauges, off | Rainfall's possible river context | Provisional point discharge, not flood extent or a causal attribution |

The two radar raster sources remain bounded to the confirmed image and one
pending image. Once a frame settles, the inactive layer is **hidden by layout**
rather than merely transparent, so it is not eligible to acquire new viewport
tiles. An explicitly staged frame becomes eligible until committed or discarded.
Reapplying visibility preserves a pending load; failure retains the prior scan.
An unchanged manifest does not stage the already confirmed timestamp again.

The four-minute manifest scheduler skips hidden tabs, aborts an active manifest
read when hidden or deselected, and checks on return to visibility through the
existing one-minute retry guard. Existing hidden-tab playback pause remains.
Manifest JSON now uses the shared 512 KiB bounded reader. Exact-time URLs,
nearest-neighbour 256-pixel radar tiles, 15-minute freshness refusal, and the
no-interpolation/no-untimed-fallback contract are retained.

These are source and deterministic-test properties, not measured FPS, bandwidth
savings or target-device capacity. Native WebGL2 desktop/mobile, actual provider
tile traffic, slow network and long-session acceptance remain separate checks.


The same review repaired the welcome-map entry path at baseline
`6180f438d63f1f813a00a4baabe5834bf6edc24b`. Its unmodified engine (SHA-256
`3e42fa2cec1c88522f2c50aea0a72257d975ffd9e53129201cab6bb956c06a0b`)
referenced missing state variables (`view`, `paused`, `settle`, and others),
and the already-loaded-style branch omitted its camera movement. The patch
restores the prior state initialization and camera handling, retains the newer
pending-style epoch ownership, and tracks an interrupted flight so pausing
still lands on the selected category. Existing welcome-engine regressions
exercise Storm preview freshness, paused polling, camera selection and disposal.


## Flora and vegetation

The 22-category starting page includes **Flora & vegetation**. Its map opens
NLCD 2021 land cover, offers annual GBIF plant-record hexagons and USDA crop
layers, and keeps source dates, rights and occurrence limits explicit. See
[Flora data, controls and boundaries](flora-map.md).
