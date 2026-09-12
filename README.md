# Kansas Frontier Matrix Explorer

A map-first Kansas explorer with real provider baselines, dated archive replay,
source downloads, and private data contribution and steward review workflows.

## Daily baseline and data commons — September 12, 2026

The initial map enables actual Census county boundaries/counts, USGS streamflow,
and hydrography. Synthetic interaction examples remain explicitly labeled in
collapsed legacy controls and do not start enabled. The archive defaults to
today in UTC, selects the latest available frame, and refreshes every five
minutes while following today. Choosing historical time pauses following.
All 24 hours remain visible; historical gaps and the older deep-time axis remain.
Population and housing retain their independent 2010/2020 Census edition.

Sources & data quality includes direct downloads and source-specific update
links. `/data` accepts authenticated proposals (up to 10 MB per file), stores
original bytes privately in R2 and metadata in D1, and shows contributor status.
`/stewards` exposes the review queue only to the server-configured steward
allowlist. Every decision requires a note and matching version; D1 atomically
records the decision and audit history. Acceptance means preparation candidate,
not automatic source admission or publication on the map. Unknown rights or
non-public sensitivity prevent acceptance.

`KFM_STEWARD_EMAILS` and optional `KFM_STEWARD_USER_IDS` are comma-separated
Sites runtime settings; never commit their values. The initial allowlist is
configured through Sites for the verified Site owner. No uploaded files or
contributor records are included in source control.

The hosted feed failure reported September 12 was an unsupported
`redirect: "error"` option in Cloudflare Workers. The bounded adapters now use
`manual` and reject redirect responses, retaining the fixed-provider boundary.

Verification: `node --test tests/data-intake.test.mjs tests/intake-worker.test.mjs`
checks real D1/R2 emulation, authentication, ownership, CSRF, uploads, download
integrity, review history, conflicting decisions, and unknown-rights holds.

This checkout is also the exact standalone Site source intended for the GitHub
mirror branch `agent/kfm-site-source-sync-20260912`. That branch is a Site source
snapshot, not a merge candidate for the distinct monorepo root. The monorepo's
package-owned renderer and newer dependency work retain their own history.

## Current public scope

- Real USGS, NOAA, Census, NWS, and Raspberry Shake connections provide attributed
  source context. Legacy synthetic examples are separately labeled and opt-in.
- The default Kansas Overview may show an attributed OpenStreetMap context basemap; it is display context, not evidence.
- Nothing in this build is a released operational KFM dataset.
- Evidence resolution fails closed: missing, stale, restricted, denied, and
  error states never become unsupported answers.
- Public-safe exports preserve evidence context and withhold protected geometry.
- “New from map” carries the current extent or selection, visible layers, time,
  representation, and evidence posture into the report or guided-story workflow.
- The repository and source briefing reports implementation boundaries; it does
  not release or publish data. When opened, it performs a bounded read-only
  current-main check against the fixed public GitHub repository endpoint and
  keeps the separately versioned Site source explicit.
- Candidate source records link to their checked official portals, while keeping
  source discovery explicitly separate from admission, activation, and release.

## Site, repository, and domain checkpoint

- The active runtime authority is OpenAI Sites / Vinext, Site slug
  `kansas-frontier-matrix-explorer`, project `appgprj_6aa0b1c41bc08191bfd86003920f1631`.
- Its canonical host is
  `https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site`; no custom
  domain was attached when this checkpoint was checked on 2026-09-12.
- The independently read GitHub checkpoint is
  `bartytime4life/Kansas-Frontier-Matrix@f636df86eb4314b6a0c658bee8b9b11b5a3b99ed`
  (`main`, merged PR #4522). The Site's older in-app repository briefing is a
  historical snapshot and separately offers a current-main lookup.
- The Site and GitHub repository retain separate source histories. This Site’s
  `.openai/hosting.json` is authoritative for its current binding; the GitHub
  child manifest still names legacy project `appgprj_6a870a079c1c8191abb7401ef092a181`
  and is not used by this Site.
- No automatic source sync, release, deployment, or publication follows from
  a repository currentness check.

The application runs as a Vinext site with MapLibre GL JS. `DB` and `BUCKET`
are declared in `.openai/hosting.json` for durable data intake and review.

## Site capability registry

The map-first UI, official context adapters, and workbench actions are kept
aligned through a small typed registry layer:

- `app/site-features.ts` maps user-facing features to status, source ids, action
  ids, owning code paths, and boundaries.
- `app/site-connections.ts` normalizes the fixed official context allowlist into
  provider, adapter, freshness, action, and evidence-boundary records.
- `app/site-actions.ts` describes visible control and handoff contracts without
  replacing the handlers that own behavior.
- `app/site-architecture.ts` maps coding surfaces and routes to verification
  paths.
- `app/site-registry.ts` validates cross-file references and exposes counts used
  by the Layer Catalog.

The companion map is `docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md`. It is a
traceability surface, not a new source authority: alignment with the repository,
Drive, and Notion preserves separate version histories and does not activate
held integrations, release external context, merge repository code, or deploy
the Site.

## Date-bound Event Observatory

`/observatory` is the real-data animation workspace within this existing Site,
linked from the map command bar and navigation drawer. It is separate from the
synthetic atlas/evidence clock, so no current-only atlas context can leak into
historical replay. `/observatory/sources` contains the cited source and coverage
research from primary providers, Drive, Notion, GitHub and supplied references.

The event clock supports 1/6/24-hour intervals since 1995, starts paused, uses
actual radar artifacts and observation/interval boundaries, shows coverage gaps,
and provides layer opacity/order, stepping, speed, loop, Central/UTC labels,
reduced-motion controls and query replay links. Live access is an explicit Recent
hour refresh, not an automatically refreshing/follow-latest stream. Replay links
do not freeze provider revisions and are not KFM EvidenceBundles.

Connected external-only carriers:

- NOAA/NWS-derived IEM N0R/N0Q mosaics, admitted by exact archive filenames before
  WMS rendering. TIME is mandatory; no latest or nearest-frame fallback. Upstream
  data are rendered in Mercator to match the fixed Kansas image-source bounds.
- NOAA HMS actual KML polygons, filtered by Start/End and Kansas intersection;
  actual footprint changes, not invented wind vectors or surface PM2.5.
- USGS API v1 selected-station continuous discharge with an absolute historical
  end time, a 30-minute bounded hold and a gap-aware hydrograph.
- NASA Terra MODIS daily satellite backgrounds; both advertised date and tile
  actual-time header are verified. These are not historical boundary maps.
- KGS cached surface-geology raster and its actual unit legend; cache edition
  remains unconfirmed, and the cache is not relabeled as newer GeMS data.
- GBIF annual Plantae/Animalia record-density hexagons. Source zoom is capped at
  six before delivery; no exact occurrence points or sensitive-taxon drilldown.
- USGS historical mine-map symbols grouped by county upstream, then joined to
  modern Census county geometry. The independent 1934–1996 edition control is
  not an operating-date or reserve claim. This is an older source compilation.

HRRR modeled smoke transport, surface air-quality observations, native NOAA scan
decoding, georeferenced historical cartographic editions, qualified
habitat/migration products, and Raspberry Shake waveform retrieval remain
explicit next integrations. HMS smoke polygons, station metadata, and dynamic
3DEP LiDAR-derived hillshade/slope are context connections only; they do not
create a KFM release, alert, measurement, or evidence answer.

Validation: `node --test tests/event-atlas.test.mjs tests/streamflow.test.mjs
tests/rendered-html.test.mjs` plus the standard Sites build and TypeScript check.
Live route checks on 2026-09-10 confirmed a June 7, 2023 manifest (72 radar frames,
two Kansas-intersecting smoke intervals), a May 5, 2007 radar image, dated NASA
and GBIF tiles, the 1984 county aggregate (26 symbols), and 97 USGS continuous
samples for a May 2024 station interval. No browser visual QA was performed.

## Temporal sweep

The shared map clock now supports committed snapshot, moving-window,
event-stepping, accumulation, and A/B comparison modes. A user can bound the
sweep range, choose event dates or every atlas tick, step forward or backward,
set playback speed and boundary behavior, and capture the committed frame in a
report, workspace, URL, or story draft. The frame readout lists entered and
exited records and describes cross-domain co-presence as an association only.

`app/temporal-sweep.ts` owns the pure sequence, interval, accumulation,
playback, and frame-summary rules. `app/map-runtime.ts` translates the same
query into MapLibre filters, while every catalog, evidence, nearby, report, and
selection surface uses that query rather than a separate display-only clock.
No mode interpolates geometry or values, carries an exact observation forward,
or treats co-presence as correlation or causation.

The atlas timeline and provider observation clocks are separate. Operational
context therefore fails closed outside the committed 2026 operational-present
atlas frame, even when a provider can return recent or station-specific
history. MapLibre hides those layers but preserves the user's visibility
choices so the same sources return on Present. This prevents a USGS observation
from being relabeled as an atlas edition merely because their calendar years
match.

Each adapter keeps the clocks it can support distinct: observation or forecast
valid time, provider publication or last-modified time, Site retrieval time,
and KFM release time. A missing clock remains missing. Spatial overlap between
radar, gauges, modeled guidance, watersheds, and other domains is an inspection
cue only; it does not establish correlation, lag, direction, or causation.

### River Pulse and temporal hydrology

River Pulse uses the fixed `/api/hydrology/streamflow` adapter for the USGS
Water Data APIs' OGC API v1 collections. The statewide view requests discharge
parameter `00060` for a rolling 24-hour window and deterministically samples at
most 72 geographically distributed Kansas stream gauges. Selected-station
views provide 7-day and 30-day continuous series; the 1-year view uses daily
mean statistic `00003`. These ranges are bounded displays, not an all-stations
inventory or a permanent local archive.

The display sequence is sampled from actual returned observation timestamps;
it inserts no synthetic frame times. At a frame cursor, a station's most recent
sample is usable only within the declared tolerance, with its true observation
time and age retained. Outside that tolerance the marker becomes explicitly
missing. Hydrograph paths break at nulls and large time gaps. No linear, spline,
spatial, or cross-source interpolation is performed, and provisional USGS
values remain labeled as subject to revision.

Marker size uses a bounded logarithmic display of discharge to keep low and
high flows legible together. It is not flood severity: raw cubic-feet-per-second
values are not directly comparable across differently sized basins and are
never painted onto 3DHP reaches or generalized into WBD watershed conditions.
Flood categories are displayed only when NOAA supplies them.

The fixed `/api/hydrology/noaa` adapter establishes three distinct NWPS modes:
a Kansas gauge-status network, one-gauge observed and official NWS forecast
series, and one-reach National Water Model analysis-assimilation and short-range
series. The latter are modeled guidance, not gauge observations or official
River Forecast Center forecasts. NWPS is an operational service rather than a
durable general history archive, so all valid, issue, generation, and retrieval
times remain explicit and gaps are not backfilled.

### NOAA observed-radar loop

The optional radar control uses the NOAA nowCOAST WMS endpoint
`https://nowcoast.noaa.gov/geoserver/weather_radar/wms` and its NWS/OAR MRMS
`conus_base_reflectivity_mosaic` product. The fixed server adapter at
`/api/noaa-radar/frames` reads the product's WMS capabilities document and
accepts only its explicit advertised ISO observation times. MapLibre then asks
for each selected image with that exact `TIME`; the Site does not invent
intermediate times, interpolate imagery, or make an untimed “latest” request.

The dock can step or play up to 32 available observations from a rolling
30-minute, 1-hour, or 2-hour view. Its default is 1 hour. Availability,
retention, and cadence remain controlled by NOAA and can change; the interface
reports the discovered median cadence and gaps rather than promising a fixed
archive. The frame manifest is checked every four minutes while radar is
selected, with retries bounded to no more than once per minute.

An upstream, contract, or tile failure pauses the loop and either freezes the
last still-valid exact observation with a visible error or withholds radar.
Radar is also withheld once NOAA's newest advertised observation is more than
15 minutes old. No synthetic image, nearest-time substitution, or prior frame
relabeled as current is used. This layer is observational display context only:
rendered colors are not converted to rainfall, storm motion, warning status, or
forecast, and the loop is not an emergency or warning-delivery service. Use
official NWS products for weather decisions.

## External network disclosure

The map can request five external display carriers. Their endpoints,
activation rules, attribution, fallbacks, and evidence exclusions live in one
typed registry: `app/external-context-sources.ts`. The Sources workbench shows
the same registry and distinguishes the carrier selected by the current view
from site-local GeoJSON sources.

| Carrier | Activation | Purpose | KFM evidence effect |
|---|---|---|---|
| OpenFreeMap Liberty | Default Standard basemap | Vector geography and provider-supplied building heights | Display context only; attribution only in outward artifacts |
| Esri World Imagery | User selects Satellite imagery | Raster imagery reference | Display context only; no acquisition or change claim |
| OpenStreetMap raster | User selects OpenStreetMap context | Normal interactive raster navigation reference; no offline or bulk fetching | Display context only; no routing or legal-status claim |
| USGS National Map Topo | User selects USGS topo | Raster topographic reference | Display context only; no feature, contour, or legal-status claim |
| AWS / Mapzen Terrarium | User selects Terrain 3D | Raster DEM terrain and hillshade | Display context only; no sampled elevation or KFM release claim |

The local Midnight and Prairie styles make no basemap request. A failed
external carrier preserves the site-local layers, evidence text, and report
path; terrain failure returns to the 2D evidence path.

## Official Kansas context adapters

The Layer Catalog also exposes fourteen fixed, source-specific connections. Search
finds these sources directly, the Data action opens their controls, and the
connection pulse reports loaded feature counts and retrieval time. Browser
requests cannot supply an arbitrary upstream URL.

| Connection | Default | Added context | Explicit boundary |
|---|---:|---|---|
| Census counties + ACS population | On | 2026 TIGERweb geometry joined by GEOID to the 2024 ACS 5-year population estimate | Separate vintages; not a current population count or EvidenceBundle |
| USGS River Pulse | On | Bounded Kansas discharge `00060` observations from USGS Water Data API v1, with exact-frame playback and selected-station history | Samples may be provisional, qualified, delayed, revised, missing, or truncated; not flood guidance or an all-stations inventory |
| NOAA NWPS gauges + forecast | Off | Operational Kansas gauge status plus separately labeled observations and forecasts | NWPS is not a durable general archive or warning-delivery service; flood categories appear only when supplied by NOAA |
| USGS 3DHP hydrography | On | Provider-rendered flowlines and waterbodies for network orientation | Transitional/current image carrier, not queryable analysis topology; gauge values are never extended along it |
| USGS/NRCS WBD watersheds | Off | Scale-dependent HUC8, HUC10, and HUC12 boundary context from the published legacy service | USGS no longer maintains WBD as a current product; image carrier, not selected-vector geometry or a basin condition estimate |
| NOAA NWM high-flow analysis | Off | Provider-current modeled analysis-guidance snapshot | Not a gauge observation or warning; the map service advertises no selectable historical time axis |
| NOAA NWM 18-hour outlook | Off | Provider-current maximum modeled high-flow guidance for the next-18-hour window | Not an official RFC forecast or deterministic outcome; the map service advertises no selectable historical time axis |
| USGS earthquakes | Off | Bounded 30-day Kansas-area event catalog with magnitude and depth | Catalog values can change; not an alert or hazard forecast |
| NOAA HMS smoke footprints | Off | Dated qualitative smoke polygons from the rolling 24-hour provider window | Not surface PM2.5, plume altitude, measured transport, a fire perimeter, warning, health advisory, or all-clear |
| Raspberry Shake stations | Off | Kansas-bounded FDSN AM station metadata with StationView handoff | Not realtime waveforms, an event catalog, alert, calibrated measurement, or KFM evidence |
| USGS 3DEP LiDAR hillshade | Off | Dynamic multidirectional hillshade from the current 3DEP elevation mosaic | Rendered relief only; no work-unit, point-cloud, datum, pulse-spacing, or accuracy claim |
| USGS 3DEP LiDAR slope | Off | Dynamic slope visualization from the same 3DEP service | Image context only; no numeric slope/elevation or source-artifact claim |
| NWS alert areas | Off | Active Kansas alerts and bounded affected-zone geometry | Not a warning-delivery service or an all-clear |
| NOAA nowCOAST radar | Off | Recent CONUS base-reflectivity observations at exact NOAA-advertised times, with 30-minute, 1-hour, and 2-hour loop views | Context only; pixels do not establish rainfall rate, storm motion, warning status, forecast, or an emergency all-clear |

Every connection is `EXTERNAL_CONTEXT_ONLY`. It is excluded from KFM reports,
exports, source admission, release state, and EvidenceBundle resolution. Failed,
partial, empty, and refreshed states remain visible instead of being converted
into inferred facts.

## Backend connection posture

- `/api/hydrology/streamflow` is the fixed, read-only USGS Water Data API v1
  adapter for bounded statewide discharge and selected-station history. It
  allowlists OGC collection paths and query shapes, limits response size and
  records, validates station identifiers, and returns no synthetic, zero-flow,
  or stale fallback.
- `/api/hydrology/noaa` is the fixed, read-only NOAA NWPS adapter for Kansas
  network, validated gauge, and validated NWM reach modes. Observed, official
  forecast, analysis-assimilation, and short-range model records retain distinct
  roles and valid times; sentinel values are normalized to missing.
- `/api/live-context` remains an allowlisted adapter for six JSON feeds,
  including the bounded NOAA HMS smoke and Raspberry Shake station connections;
  River Pulse now uses the dedicated USGS v1 route above. USGS 3DHP, WBD, 3DEP
  LiDAR-derived hillshade/slope, and NOAA NWM raster products are requested by
  MapLibre only when selected.
- `/api/noaa-radar/frames` is a fixed, read-only NOAA nowCOAST capabilities
  adapter. It accepts no caller-supplied endpoint, bounds time and response
  size, and returns no synthetic or untimed fallback. Exact-time WMS radar
  images are requested by MapLibre only when the user selects the layer.
- `/api/repository-status` reads only the public `main` branch identity for
  `bartytime4life/Kansas-Frontier-Matrix`. It accepts no caller-supplied URL,
  bounds response size and time, caches briefly, and fails closed.
- The GitHub repository and this Site have separate source histories. The
  currentness check does not synchronize trees, write issues, mutate data,
  deploy a version, or publish the Site.
- `/api/qwen` remains unavailable until a server-reachable endpoint is
  configured. No hosted Qwen variables are currently required for the map.
- D1 and R2 remain unbound; reports, stories, places, and investigation
  workspaces are device-local drafts.

## Prerequisites

- Node.js `>=22.13.0`
- Linux with `flock`, `curl`, and GNU `timeout`

## Sites Lifecycle

The Sites lifecycle CLI runs the locked dependency install before returning this checkout. Edit the source under `app/`, then checkpoint when a coherent milestone is ready to inspect or share. The remote Sites builder runs `npm run build` against the pushed commit. Do not repeat install or build as a normal pre-checkpoint step.

This project does not use `wrangler.jsonc`.

`install:ci` is intentionally a single, non-retrying `npm ci`. It refuses a concurrent install for the same project, consumes a matching image-seeded npm cache with `--prefer-offline` while retaining registry fallback for a missing cache object, otherwise downloads and verifies the complete vinext tarball recorded in `package-lock.json`, limits npm to one socket, and terminates a stalled install. `build` applies a short timeout. These helpers target Linux and use GNU `timeout`; they are not native macOS scripts.

Scripts that need writable project-scoped home, npm, XDG, and temporary paths use `scripts/sites-env.sh`. The `dev` and `start` scripts honor the caller's runtime environment and keep Wrangler logs inside the checkout. The generated `.sites-runtime/` directory is disposable and ignored by Git.

## Implementation shape

- edit site code under `app/`
- `app/external-context-sources.ts` is the single inventory for every
  browser-requested basemap and terrain carrier
- `app/api/live-context/route.ts` contains the fixed official-context adapter
- `app/streamflow.ts` validates USGS bundles, selects actual frame times, builds
  tolerance-bounded map frames, and breaks hydrographs across gaps
- `app/hydrology-observatory.tsx` owns the accessible River Pulse transport,
  completeness readout, legends, station selection, and hydrograph
- `app/api/hydrology/streamflow/route.ts` exposes bounded USGS Water Data API v1
  network and selected-station queries
- `app/noaa-hydrology.ts` validates the bounded NOAA Kansas gauge network for
  MapLibre
- `app/api/hydrology/noaa/route.ts` exposes bounded NWPS network, gauge, and NWM
  reach modes without caller-supplied upstream URLs
- `app/noaa-radar.ts` owns the NOAA nowCOAST product contract, explicit-time
  parsing, recent-window selection, and exact-time WMS request construction
- `app/api/noaa-radar/frames/route.ts` exposes the bounded radar frame manifest
- `app/api/repository-status/route.ts` contains the fixed read-only GitHub
  currentness check
- `app/chatgpt-auth.ts` provides optional dispatch-owned ChatGPT sign-in helpers
- `.openai/hosting.json` declares optional Sites D1 and R2 bindings
- `vite.config.ts` simulates declared bindings for local development
- `db/index.ts` reads the D1 binding from the Cloudflare Worker environment
- `db/schema.ts` starts intentionally empty
- `examples/d1/` contains an optional D1 example surface
- `drizzle.config.ts` supports local migration generation when needed
- `docs/KFM_SOURCE_GAP_REGISTER.md` records implemented, context-only, and held
  source boundaries; it is not a release ledger

## Workspace Auth Headers

OpenAI workspace sites can read the current user's email from
`oai-authenticated-user-email`.

SIWC-authenticated workspace sites may also receive
`oai-authenticated-user-full-name` when the user's SIWC profile has a non-empty
`name` claim. The full-name value is percent-encoded UTF-8 and is accompanied by
`oai-authenticated-user-full-name-encoding: percent-encoded-utf-8`.

Treat the full name as optional and fall back to email when it is absent:

```tsx
import { headers } from "next/headers";

export default async function Home() {
  const requestHeaders = await headers();
  const email = requestHeaders.get("oai-authenticated-user-email");
  const encodedFullName = requestHeaders.get("oai-authenticated-user-full-name");
  const fullName =
    encodedFullName &&
    requestHeaders.get("oai-authenticated-user-full-name-encoding") ===
      "percent-encoded-utf-8"
      ? decodeURIComponent(encodedFullName)
      : null;

  const displayName = fullName ?? email;
  // ...
}
```

## Optional Dispatch-Owned ChatGPT Sign-In

Import the ready-to-use helpers from `app/chatgpt-auth.ts` when the site needs
optional or required ChatGPT sign-in:

- Use `getChatGPTUser()` for optional signed-in UI.
- Use `requireChatGPTUser(returnTo)` for server-rendered pages that should send
  anonymous visitors through Sign in with ChatGPT.
- Use `chatGPTSignInPath(returnTo)` and `chatGPTSignOutPath(returnTo)` for
  browser links or actions.
- Pass a same-origin relative `returnTo` path for the destination after sign-in
  or sign-out. The helper validates and safely encodes it.
- Mark protected pages with `export const dynamic = "force-dynamic"` because
  they depend on per-request identity headers.

Dispatch owns `/signin-with-chatgpt`, `/signout-with-chatgpt`, `/callback`, the
OAuth cookies, and identity header injection. Do not implement app routes for
those reserved paths. Routes that do not import and call the helper remain
anonymous-compatible.

SIWC establishes identity only; it does not prove workspace membership. Use the
Sites hosting platform's access policy controls for workspace-wide restrictions,
or enforce explicit server-side membership or allowlist checks.

Use SIWC for account pages, user-specific dashboards, saved records, and write
actions tied to the current ChatGPT user. Leave public content anonymous.

## Diagnostic Commands

- `npm run install:ci`: perform the one bounded lockfile install
- `npm run dev`: start the Vite/Vinext development server
- `npm run build`: build the deployable Sites artifact
- `npm run start`: start the built Vinext application
- `npm test`: build and verify the rendered development-preview metadata
- `npm run db:generate`: generate Drizzle migrations after schema changes

Use build commands for targeted diagnosis after a remote failure, not as part of the normal checkpoint path.

The timeout defaults can be overridden for a controlled canary with `SITES_INSTALL_TIMEOUT`, `SITES_INSTALL_KILL_AFTER`, `SITES_BUILD_TIMEOUT`, and `SITES_BUILD_KILL_AFTER`. A timeout fails the command; the helpers never retry an unchanged install or build.

## Learn More

- [vinext Documentation](https://github.com/cloudflare/vinext)
- [Drizzle D1 Guide](https://orm.drizzle.team/docs/get-started/d1-new)

## Current map-to-draft work

The React Explorer includes inherited map snapshots, validated device-local report
and story drafts, attributed print and Markdown exports, and synchronized A/B
snapshot maps. Synthetic ANSWER/CORRECTED fixtures retain their demonstration
trust label. Source-backed counts do not count synthetic support states.

This replacement packages the Vinext Worker output (`dist/server` and
`dist/client`). Legacy static build files are excluded. Source dependencies,
package manager, feature registries, and unbound D1/R2 settings are preserved.

The user authorized this replacement on 2026-09-09 after the original project
was inaccessible to Sites. The original local checkout and its project binding
remain unchanged. The replacement has its own Sites identity in its manifest.

Verification: TypeScript and 29 existing/focused checks passed before transfer.
Browser checks verified draft reload, story stepping, Escape, the comparison
fallback, and desktop overflow. The test browser lacked WebGL2; terrain, globe,
and rendered comparison remain unverified by this session.
