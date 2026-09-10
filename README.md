# Kansas Frontier Matrix Explorer

A map-first spatial evidence demonstration for exploring how Kansas features,
time, provenance, correction state, access limits, and bounded Focus outcomes
fit together.

## Current public scope

- The map uses site-local synthetic or generalized GeoJSON demonstration data.
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

The application runs as a single-route Vinext site with MapLibre GL JS. D1 and
R2 are intentionally unbound in the current deployment.

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

The official context connections below expose only a current snapshot or a
rolling current window. They therefore fail closed outside the committed 2026
operational-present frame: MapLibre hides their layers but preserves the user's
visibility choices so the same sources return on Present. Historical playback
never relabels current Census, USGS, NWS, terrain, or radar context as archival
data.

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

The map can request four external display carriers. Their endpoints,
activation rules, attribution, fallbacks, and evidence exclusions live in one
typed registry: `app/external-context-sources.ts`. The Sources workbench shows
the same registry and distinguishes the carrier selected by the current view
from site-local GeoJSON sources.

| Carrier | Activation | Purpose | KFM evidence effect |
|---|---|---|---|
| OpenFreeMap Liberty | Default Standard basemap | Vector geography and provider-supplied building heights | Display context only; attribution only in outward artifacts |
| Esri World Imagery | User selects Satellite imagery | Raster imagery reference | Display context only; no acquisition or change claim |
| OpenStreetMap raster | User selects OpenStreetMap context | Normal interactive raster navigation reference; no offline or bulk fetching | Display context only; no routing or legal-status claim |
| AWS / Mapzen Terrarium | User selects Terrain 3D | Raster DEM terrain and hillshade | Display context only; no sampled elevation or KFM release claim |

The local Midnight and Prairie styles make no basemap request. A failed
external carrier preserves the site-local layers, evidence text, and report
path; terrain failure returns to the 2D evidence path.

## Official Kansas context adapters

The Layer Catalog also exposes six fixed, source-specific connections. Search
finds these sources directly, the Data action opens their controls, and the
connection pulse reports loaded feature counts and retrieval time. Browser
requests cannot supply an arbitrary upstream URL.

| Connection | Default | Added context | Explicit boundary |
|---|---:|---|---|
| Census counties + ACS population | On | 2026 TIGERweb geometry joined by GEOID to the 2024 ACS 5-year population estimate | Separate vintages; not a current population count or EvidenceBundle |
| USGS streamflow | On | Latest Kansas discharge values from a bounded rolling 24-hour request | Provisional context; not flood guidance |
| USGS earthquakes | Off | Bounded 30-day Kansas-area event catalog with magnitude and depth | Catalog values can change; not an alert or hazard forecast |
| USGS 3DEP hillshade | Off | Current multidirectional hillshade tiles | Rendered relief only; no elevation sample, datum, or accuracy claim |
| NWS alert areas | Off | Active Kansas alerts and bounded affected-zone geometry | Not a warning-delivery service or an all-clear |
| NOAA nowCOAST radar | Off | Recent CONUS base-reflectivity observations at exact NOAA-advertised times, with 30-minute, 1-hour, and 2-hour loop views | Context only; pixels do not establish rainfall rate, storm motion, warning status, forecast, or an emergency all-clear |

Every connection is `EXTERNAL_CONTEXT_ONLY`. It is excluded from KFM reports,
exports, source admission, release state, and EvidenceBundle resolution. Failed,
partial, empty, and refreshed states remain visible instead of being converted
into inferred facts.

## Backend connection posture

- `/api/live-context` is the allowlisted server adapter for four JSON feeds;
  the USGS 3DEP raster product is requested by MapLibre only when selected.
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
