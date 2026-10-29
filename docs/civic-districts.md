# Kansas congressional districts through time

Next proposed civic slice: [historical county source qualification](county-history-qualification.md). Real archive checks passed; public reuse and integration remain held. This does not add a county-history layer or extend the congressional coverage below.

## Behavior and evidence status

Government & civic opens **Kansas representation**. Present shows Census 119th Congress geography. A Congress selector covers **36–119**; calendar dates and year controls select the applicable term. Historical plans reach back to **Kansas statehood, January 29, 1861**. The welcome glimpse retains the four present districts and points to history in the full map.

Colors identify district numbers, not parties or continuous identities. An at-large constituency is statewide and may elect multiple representatives. Where it coexists with numbered districts, its fill and label are withheld and its outline is dashed; it remains keyboard-selectable. A sole statewide constituency receives a fill and label. The UI counts constituencies, never infers seats from polygons. The dock offers selected-plan GeoJSON, retry, Return to Present, source links and optional county comparison.

**CONFIRMED this session:** all 18 pinned historical files were retrieved through GitHub; exact Git blob identities and SHA-256 digests were checked; their real geometries passed the structural parser. Offline qualification exercised **83 Congresses, 36–118**, with 12 concurrent calls per term and only 18 acquisitions. Congress 119 uses the existing direct Census adapter separately.

**NEEDS VERIFICATION:** successful live Census query, deployed raw-GitHub acquisition, desktop/mobile rendering, label collisions, frame rate and deployment. Connector retrieval and offline qualification do not prove these. No independent security review or full-repository test run is claimed.

## Sources and historical interpretation

- [National Archives: Kansas statehood](https://www.archives.gov/legislative/features/kansas) establishes January 29, 1861. [Kansas Historical Society territorial records](https://www.kansashistory.gov/archives/216356) documents the preceding territory. Territorial delegate geometry is **unverified** here; no modern state outline substitutes for it. Earlier territorial, Indigenous and sovereignty histories are not inferred.
- [U.S. Senate: Congress dates](https://www.senate.gov/legislative/DatesofSessionsofCongress.htm) establishes March 4 term boundaries before Congress 74 and January 3 thereafter. Congress 73 ends January 3, 1935. The first Kansas interval is clipped to statehood. These are representation terms, not election, enactment or session dates. A transition day uses the incoming Congress; intraday/noon precision is not modeled.
- [Lewis, DeVine, Pitcher and Martis](https://cdmaps.polisci.ucla.edu/) supplies scholarly reconstructions, with Census-derived recent plans. The authors describe historical county aggregation and district-specific source research. Restricted detailed worksheets were not inspected. Parser success does not independently certify every boundary.
- Congresses 36–112 use [original files pinned at a72f5836](https://github.com/JeffreyBLewis/congressional-district-boundaries/tree/a72f5836d0de4ad5aa94a18b6b725b46bf71b39e). Congresses 113–118 use [newer files pinned at 3c663a80](https://github.com/JeffreyBLewis/congressional-district-boundaries/tree/3c663a8098b58156601e0893f0e67b502f7f8354/GeoJson). The 18-file allowlist, expected district sets and SHA-256 identities are in `app/civic-history.ts`.
- The newer `Kansas_036_to_055` statewide shape compresses a broad interval. Original plan files distinguish at-large representation in Congresses 36–43, 48 and 53–59 from intervening plans without it. This adapter retains those original memberships; it does not interpret a compressed interval as uninterrupted validity or claim an upstream correction.
- [Census Generalized ACS 2025 Legislative layer 5](https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2025/Legislative/MapServer/5) supplies **119th Congressional Districts 500K**, January 1, 2025 vintage. Metadata was verified. The entire historical series must not be described as direct government-published geometry.
- The historical collection's [MIT license](https://github.com/JeffreyBLewis/congressional-district-boundaries/blob/a72f5836d0de4ad5aa94a18b6b725b46bf71b39e/LICENSE) accompanies historical API responses in full and is served at `/civic-history-license.txt`. Attribution names all four authors. No restricted worksheets or map scans are redistributed. Census attribution follows its [citation guidance](https://www.census.gov/about/policies/citation.html).

Provider NAD83 coordinates retain the documented zero-shift display approximation to WGS84; no survey precision is claimed. The original files are lower resolution than the newer collection; detail differences do not establish legal change. No interpolation, officeholder/party join, election result or ballot eligibility is inferred. [Kansas Secretary of State maps](https://www.sos.ks.gov/elections/district-maps.html) remain the official follow-up.

## Request and temporal contracts

The compatibility feed ID remains `census-congress-119`; its default request still serves the current Census edition. `/api/live-context?feed=census-congress-119&day=YYYY-MM-DD` selects a term. Invalid, unsupported, future, duplicate and additional parameters are rejected before acquisition. The 119th edition is never extended past January 2, 2027; new Congress coverage requires a reviewed update.

Annual frames use January 1, so the 1861 annual frame is withheld until a supported exact date/Congress is selected. Calendar views require an exact checked response day. Date changes clear incompatible selections and geometry; late replies cannot replace newer requests. Failure never substitutes another plan.

Historical reads use fixed immutable URLs, reject redirects, enforce a 25-second deadline and a 2 MiB streamed byte cap, verify SHA-256, and require the complete expected constituency set. Polygon/MultiPolygon rings must be finite, closed, nondegenerate, within broad Kansas bounds and under 50,000 total vertices. These checks are structural, not a topology proof. Provider member fields, arbitrary names and HTML are dropped.

At most four validated plans are cached per process for 24 hours. Same-plan requests coalesce; failed refreshes clear expired data and apply a 60-second cooldown. HTTP remains `no-store`. Retrieval, term and source revision clocks stay separate; no provider update time is invented. Cross-replica coordination remains unverified. There is no new polling loop, dependency or renderer.

## Placement, lifecycle and rollback

Base: hosted `a0-hosted-ai-web-20261017` at merge `212ea078b7b95c920dcc29e712d09054ebaff260`, tree `eedea5ea67234e14738b4f5b841f7297ad6391eb`; the local starting tree matches. This extends merged #5552.

Directory Rules v2, adopted by ADR-0029, §§5 and 10–12: PLACE within existing owners. `app/civic-history.ts` owns this application's projection/date contract; `app/api/live-context/civic-history.ts` extends the existing acquisition boundary. Calendar, UI, keys and source traces stay in their current modules. Verification belongs under existing `scripts/` and `tests/`, documentation under `docs/`, and the distributable license under existing `public/`. No new canonical source registry, schema/policy home or release store is introduced.

Public clients use the bounded API. Historical source files are not bundled into application assets. This is **EXTERNAL_CONTEXT_ONLY**, without source admission or EvidenceBundle/release approval. RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and DIR-PLACE-002 / DIR-DATA-004 / DIR-SOURCE-003 remain separate. Signed recipes, source approvals, persistence and second-PC workers are unchanged.

Rollback: revert this extension to restore #5552's fixed 119th Congress behavior. No migration or persistent source payload needs cleanup. Branch/PR authority does not authorize merge, deployment or publication.

## Validation

`tests/civic-history.test.mjs` uses explicitly synthetic boxes for date and identity rejection, provenance, route validation, temporal eligibility, actual production archive-loader races and keyboard controls. Existing civic rendering checks validate all four MapLibre styles; key tests check that only selected constituencies appear.

`node scripts/verify-civic-history.mjs /path/to/provider-files` verifies the 18 exact upstream files named by the allowlist. It downloads and publishes nothing. It passed this session for all 18 files / 83 historical terms, including coalescing, cache expiry and cooldown recovery. Real retrieved geometry bytes were used; input files remain temporary verification material.

See the PR for final commands and actual results. Parser, renderer-harness, typecheck and build success do not establish live acquisition, browser acceptance, source admission or deployment.
