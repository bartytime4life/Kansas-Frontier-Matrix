# I-70 Junction City: 2024 Phase Two pilot

**Review candidate, 2026-10-22 (America/Chicago).** One Kansas corridor, three dated KDOT reports, no inferred daily construction. Factual admission, historical survey qualification and public publication remain separate.

## Load and scope

Use Construction through time's local-file input with [the pilot study](../data/work/transport/junction-city-i70-2024.study.json). It is version 1 with additive milestone mode. Report dates appear as time advances; the corridor remains context with unknown progress. No candidate is auto-loaded, copied to public assets, registered as evidence or sent to AI.

[Geometry derivation](../data/work/transport/junction-city-i70-2024.geometry.json) and [source identities](../data/work/transport/junction-city-i70-2024.sources.json) accompany the study. Placement follows accepted ADR-0029 and Directory Rules §§9–11: candidate transformation in existing `data/work/`, explanation in `docs/`, standalone application behavior in `app/`, regressions in `tests/`, authoring receipt in `data/receipts/generated/`. No new authority root or canonical transport contract.

## Evidence and limits

| Source report | Supported observation | Held interpretation |
|---|---|---|
| [KDOT, 2024-04-29](https://www.ksdot.gov/Home/Components/News/News/1597/712) | Construction is progressing; westbound entrance 299 and exit 298 remain closed at report time | Proposed May 2 reopenings are tentative; no exact closure start or surveyed front |
| [KDOT, 2024-05-02](https://www.ksdot.gov/Home/Components/News/News/1595/712) | Updated single-lane crossover configuration | May 8 ramp changes and later durations are conditional schedules |
| [KDOT, 2024-11-22](https://www.ksdot.gov/Home/Components/News/News/658/712) | Phase Two completion reported by this date | Exact completion day unknown; winter reopening scheduled later that day, not confirmed; later phases separate |

Report-window endpoints are **not** actual construction start/end dates. A phase completion does not mean the whole project is complete or every ramp reopened. Ramp observations remain textual: they cannot justify coloring the whole interstate closed.

The [current project page](https://www.ksdot.gov/projects/i-70-pavement-replacement-in-junction-city) identifies KA-6062-01 and describes Phase Two westbound pavement work between markers 296 and 300, with separate month-level phase completions and later work. Current content is not backdated daily progress evidence. The [2024 ramp-planning flyer](https://www.ksdot.gov/home/showpublisheddocument/11503/638942156092530000) supports intended staging, not actual closure dates.

Search-index copies of the March 12 notice and May 2024 Translines conflict on the 2024 carriageway; a November 2023 advance notice also describes a different future arrangement. Their legacy PDF links returned 404 during research. The source manifest retains those failed leads. Indexed text is not admitted evidence. The retrieved project page, flyer and April/May reports support a westbound-reference **context** trace, but no dated machinery is assigned to either carriageway. Reconcile daily reports, as-built plans and dated geolocated photographs before reconstruction.

## Geometry and chainage

The 79 vertices follow KDOT's current [State Route network](https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/LRS_State/MapServer/0), object 4, StateRouteId `10700100000`, EPSG:4326. The saved excerpt retains the source M values and original starting vertex index 2343. Clip anchors are consistent westbound [reference posts](https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Layers/KDOT_reference_post_markers/MapServer/0) 296 and 300, route `0311000700100000`.

Reproduce the clip by projecting each anchor onto its recorded excerpt segment, weighting longitude by cosine of anchor latitude, clamping the fraction to [0,1], and retaining every intermediate source vertex. The geometry JSON contains fractions and projected endpoints. Sum geodesic segment distances with the renderer's 6,371,000 m Earth radius. This cartographic derivation is not a survey.

- Indexing runs west to east, 296 → 300. Construction direction and westbound vehicle travel direction are separate.
- Length is approximately **6.427 km**. Marker numbers, state-route M, county-route measures and renderer chainage are distinct. KDOT warns that markers do not necessarily represent consistent traveled mileage.
- Selected marker projections agree with the related reference trace within 1 m, and with their recorded coordinates within 15 m. Agreement between related datasets is not independent or certified accuracy.
- Excluded eastbound marker object `7225030` says 300 but its geometry is over 8 km from its recorded coordinates. It is recorded as an anomaly, not silently repaired.
- The inspected [KDOT project-area map](https://www.ksdot.gov/home/showpublishedimage/4414/638947417700830000) corroborates the corridor at Washington Street, Chestnut Street, J-Hill Road and K-57. It is not a georeferenced engineering survey.

This is geographically grounded **current corridor context**. Historical as-built epoch, exact engineering station limits, work width, survey accuracy and the precise 2024 alignment remain unestablished. They cannot qualify metre-scale worksite placement. The modern basemap remains independent.

## Rendering and validation

No equipment appears for this pilot: actual task types, machinery, workforce and dated positions are missing. A plausible modern excavator cannot establish a real worksite. Existing unlocated representative models and supported advancing-front animation remain available and unchanged.

Milestone geometry uses a fixed cartographic line, never an invented pavement width. Observed front records retain their established behavior; explicit interpolation is labeled and tinted separately; milestone progress stays unknown. Playback reveals only reports dated at or before the selected day; reverse seeking removes future reports and stops at the last report. Reduced motion retains manual controls.

Focused checks cover importer compatibility, unsafe/contradictory reports, source scope, geometry reconstruction, distance/LOD, metre-scale models, styles and forward/reverse component playback. Exact results and browser observations belong in the PR and receipt. Full production build, independent cartographic review, GPU/device acceptance and production publication remain separate.

## Qualification and rollback

Before an advancing front: admit durable public-safe source captures through normal intake; resolve rights and sensitivity; crosswalk contract/phase/station identities; obtain dated as-built geometry; reconcile carriageway conflicts and marker anomalies; establish actual work and closure intervals at source precision; acquire spatial progress observations. Multiple crews need separately supported fronts. Calendar duration and completion milestones never establish a linear daily rate.

The manifest records retrieval hashes and their scopes. Mutable HTML hashes identify retrieved bytes, not permanent upstream versions. Full captures are not admitted to RAW; no source registry, EvidenceBundle, policy approval or release decision is created. Public retrieval is not reuse clearance. Candidate files are for repository review and manual local study only.

Rollback: revert the focused pilot, importer/render/control/test support, guide and generated receipt together. No persisted-data migration, original Site synchronization, hosting or public dataset changes.
