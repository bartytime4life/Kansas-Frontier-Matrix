# GoDaddy Node preview candidate

This is a separate runtime composition of Explorer v259, source
`441c3e29581ffb0293d8e643e5c37eed50319032`. It does not alter the
preserved Sites deployment, its audience, storage, or source-data values.

Verified destination: GoDaddy Node.js app `q9r9beo47t`, named
Kansas-Frontier-Matrix, connected to
`bartytime4life/Kansas-Frontier-Matrix`. The app is attached to the owner's
Plus Launch plan and its deployed source branch is `a0-godaddy-node-preview`.
The initial import used monorepo `main` and failed its npm/runtime build;
this standalone root package repaired that composition. The prior deployed
revision is `49ccc422e7ddbb36f5abe0e16c04649b7c7f313f`.

The Node candidate keeps the same Vinext and MapLibre versions and
rendering path, uses a standalone package at the application root, keeps
build/start dependencies in `dependencies`, and listens on the assigned
`PORT` on `0.0.0.0`. It builds without the Cloudflare Vite plugin.
Run `npm ci`, `npm run build`, then `npm start`.

Sites identity headers are untrusted outside Sites. They cannot sign in or
grant a staff role here. Identity, staff assignments and D1/R2-compatible
storage migration require configured server adapters. Existing private and
administrative endpoints keep their access controls.

On 2026-10-13 the owner canceled pricing, checkout and payment setup and
requested free reports/downloads. The custom map report supports copy,
JSON and printable HTML downloads; the evidence/fire/research/underground
report workspace supports Markdown and JSON exports. These run on the
visitor's device without login, payment or private-store access. The unused
pricing endpoint is removed. Draft labels, source/time/uncertainty notes,
location redaction and controlled publication remain in place. Eligible
public-data and story downloads retain their existing free workflows.
Production deployment and browser download acceptance require separate proof.

GoDaddy's branch picker exposes only the first 100 alphabetical branches.
The hosting connection uses `a0-godaddy-node-preview`. It originally matched
`codex/godaddy-node-preview`, but the latter subsequently received the earlier
pricing-service PR. This free-export repair starts from the actual hosting
branch, without that pricing service. Preserve both histories and do not
replace the public monorepo's main branch or the private Sites history.

No stored data or credentials are included in this source package. The
scalar server environment is available to existing provider handlers;
D1 and R2 bindings remain explicitly unavailable until migration. Existing
routes preserve their unavailable responses. GoDaddy's preview and
published MySQL environments share a database; do not import SQLite
migrations or reset that database without a tested migration.

The owner explicitly excluded Airo. Deploy through the existing GoDaddy
Node hosting app and GitHub connection. The domain connection and original
email records were restored before this repair. Preserve those DNS values;
free report exports do not require routing, account or merchant changes.

## Camera interruption repair candidate — 2026-10-13

This change starts from the owner-approved free-export deployment,
`70ee84754af956bf958f706a17eba6cad7887872`, on
`a0-godaddy-free-reports`. Camera replacements can synchronously emit an older
`moveend` before starting the replacement movement. Updating the large Explorer
view, bounds, terrain status and history at each intermediate end creates work
that the next movement immediately supersedes. The camera callback now queues
one microtask and cancels it if movement restarts in the same task. A genuine
stop commits the latest camera and bounds before the next task; it does not
delay navigation, reduce map detail or modify source data. Teardown invalidates
pending work. Replay markers still clear at the original event boundary, so
interrupting a replay can record the final manual view. GPS-derived views retain
their history/export exclusions.

`tests/map-settled-view.test.mjs` executes the actual page callbacks, covering
48 interrupted ends, final bounds/history, cancellation, duplicate ends,
still-moving maps, GPS privacy and manual interruption of replay. The opt-in
`frameCheck=1` diagnostic additionally records canvas pixel dimensions,
movement-end count and maximum synthetic input-dispatch time. These are local
aggregate counts only; ordinary visits gain no diagnostic listeners or telemetry.
The existing 12-second workload and frame calculations are unchanged.

The unchanged live free-export build reproduces 46.8 FPS with ten selected
layers at zoom 10.5, 1280 × 576 CSS pixels, 144 visible style layers and 22
visible data features. Its matching local production build already reaches
60 FPS. Both keep the display-data signature unchanged. A live embedded
isolation test with explicit High detail on both pages removes the roughly
150 ms stalls (45.9 FPS top-level versus 58.8 FPS embedded), supporting the
history-update hypothesis. Embedded presentation differs from ordinary visits;
this is diagnostic evidence, not hosted acceptance of this candidate. Provider
empty/partial states remain visible. The signature covers uploaded GeoJSON and
source specifications, not every remote raster/vector tile's bytes.

GoDaddy preview/publication of the exact new revision and a repeated normal
top-level browser sample remain required before claiming the live repair.
Rollback returns the hosting connection to the approved free-export revision
above. DNS, merchant settings, public assets, dependencies, source values,
governed store boundaries and the private Sites deployment are unchanged.
Placement reuses this standalone application's existing `app/`, `tests/` and
`docs/` responsibilities under Directory Rules v2 and accepted ADR-0029; it
creates no parallel data, schema or release authority.
