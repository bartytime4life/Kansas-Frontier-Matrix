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

## Hosted navigation and source operations — October 14, 2026

The owner requested removal of PC data and the top-bar Data & downloads control.
Underground, 2D, Terrain 3D, Globe and Compare now share the Map menu on all screen
sizes. Layer selection, source status, retry/hide, dates, quality and free source
files remain in Layers. Source status is a view of that same panel, rather than
a second floating workbench. Keyboard dismissal retains the original Layers
return target. Existing PC-workbench URLs redirect to `/?layers=sources`; legacy
Local Atlas map links restore that hosted source view. The original private
Sites application and operator files on the owner's computer are unchanged.

The GoDaddy composition uses its existing Node 22 runtime and fixed, bounded
public provider handlers: source requests and downloadable envelopes carry
source/observation/retrieval clocks, units, missingness and limitations. Map
services retain their own provider-controlled coverage. These are hosted
external-context adapters, not a durable KFM ingestion/release pipeline. No
background archive is fabricated and no visitor is asked to connect to Intake
Desk or the PC download operator. Earth Engine recipe discovery remains
available; its hosted capture is explicitly unconfigured, with links to the
original provider catalog and source status. Free map/report exports remain.

The owner then selected scheduled capture, durable storage, owner-only GitHub
sign-in and an 80 GB archive cap. This candidate adds a separate Node/MySQL
capture adapter. `server/godaddy-env.ts` still deliberately leaves D1/R2 unbound;
the new archive neither migrates nor exposes those governed stores. A green
browser request does not provision services or release data. Captures remain
paused until configuration, schema and owner activation are verified.

Existing `app/`, `tests/` and `docs/` compatibility responsibilities are retained
under Directory Rules v2 and accepted ADR-0029. The change creates no parallel
data, policy, pipeline, registry or proof authority. It starts from the exact
published f44ce0c composition; the independent merged Underground repair #5137
on a0-godaddy-free-reports is neither replaced nor silently included. Revert
this UI change, or republish f44ce0c after separate deployment authorization,
without changing provider bytes, datasets, DNS, payments or the private Site.

### Hosted capture implementation and activation

`server/ingestion-sources.mjs` defines the first three fixed, versioned Kansas
adapters: hourly USGS streamflow (24-hour bounded query, max 1,000 rows), hourly
NWS active Kansas alerts, and six-hourly USGS earthquake catalog (rolling 30-day
bounds, max 250 events). Requests have a 20-second timeout and an 8 MiB decoded
entity limit. Redirects, arbitrary URLs and automatic paging are rejected.
Original decoded HTTP entity bytes are stored unchanged in 512 KiB chunks,
alongside SHA-256, source URL, request/retrieval/source clocks, original HTTP
ETag/Last-Modified, row-cap/paging limitations and versioned receipts. Malformed
JSON/structure remains privately quarantined for correction. No publisher or
promotion API exists. All captures carry pending rights/sensitivity review,
EXTERNAL_CONTEXT_ONLY and unreleased WORK/QUARANTINE state.

`server/ingestion-store.mjs` uses the official mysql2 driver, certificate-verified
TLS, prepared statements and an additive five-table migration. One transactional
lease fences replicas and stale workers. Capacity is reserved before provider
I/O; atomic capture/chunk/counter commits roll back together. Deterministic
source/time-bucket keys, bounded retries/backoff and capture existence checks
prevent duplicate successful capture. Latest buckets resume after downtime;
missed historical observations are not fabricated. The archive stops at
80,000,000,000 accounted bytes (entities, receipts and per-capture allowance);
provider allocation, index/log/backup overhead and actual capacity need separate
verification. No automatic deletion or retention purge is introduced.

`server/owner-auth.mjs` binds only immutable GitHub user ID `203533328`, verified
from the current authenticated connector on October 14. It uses empty-scope
OAuth, encrypted five-minute state with PKCE, bounded provider responses and a
four-hour opaque Secure/HttpOnly/SameSite session. Login replaces the single
stored owner session; logout revokes it. GitHub bearer tokens are not persisted.
Forged Sites headers and client role strings confer no access. Owner writes
require exact Origin and session checks. The separate random capture-worker
credential can trigger due sources only; it cannot read private captures,
change controls, sign in, release or publish. Preview-origin requests cannot
use it. Credentials must be entered directly in provider interfaces by the
owner, outside source/chat/artifacts.

There is no web-process timer: preview/live share storage and previews can sleep.
The narrow main-based scheduler change installs a fixed-origin GitHub Actions
cron, initially disabled, with no checkout or repository token permissions.
Its environment must restrict credential access to protected main. The template
in this candidate is documentation, not an activated schedule. GitHub cron may
be delayed; its first stored receipt and subsequent scheduled run need separate
acceptance. See the scheduler PR and its `docs/runbooks/godaddy-hosted-capture.md`.

Hosting setup must supply DB_HOST/PORT/NAME/USER/PASSWORD, a verified database CA
in KFM_DB_CA_PEM with KFM_DB_TLS=verified and a DNS DB_HOST matching its certificate
(IP-only endpoints stay unavailable rather than skip identity verification), identity-only OAuth client ID/secret,
random base64url KFM_SESSION_KEY and separate KFM_CAPTURE_WORKER_TOKEN. Set
KFM_PUBLIC_ORIGIN=https://kansasfrontiermatrix.com,
VINEXT_TRUSTED_HOSTS=kansasfrontiermatrix.com (exact allowlist for the hosting TLS
proxy; never a wildcard), KFM_RUNTIME_ROLE=published,
KFM_INGEST_ENABLED=true and KFM_ARCHIVE_CAPACITY_CONFIRMED_BYTES=80000000000 only
after capacity and configuration are confirmed. Shared secrets alone do not
start any worker. Resume is an owner action; the SQL seed stays paused.

Review `npm run archive:migration` output first. After the shared database is
backed up and the exact schema digest approved, run the same script with
KFM_MIGRATION_SHA256 set to that digest and `--apply`. DDL is additive and
idempotent, but MySQL DDL is not a transactional rollback; preserve partially
created tables and repair/reapply rather than reset/drop. Pause capture and
disable the scheduled trigger before returning the app to f44ce0c. Keep the
archive and its receipts intact. The database guide was inspected this session;
table introspection was unavailable while preview was unreachable, so schema,
live DB connection, TLS CA and hosting capacity are still NEEDS VERIFICATION.

Implementation validation uses a disposable MariaDB 11.8.6 compatibility server
from official Ubuntu packages, not the live GoDaddy MySQL database. Transactions,
fencing, budget edges, interrupted chunk rollback, corruption detection and
owner-session revocation pass there. Exact GoDaddy MySQL/TLS compatibility,
credential configuration, OAuth round-trip and scheduled capture remain pending.

### Candidate acceptance evidence — October 14

Build and TypeScript pass. Changed-area lint has no errors and 42 inherited
warnings; the new capture/auth components have no lint warnings. Changed-area
callback/history/capture tests and 12 actual Node HTTP checks pass. Three separate
scheduler execution checks pass in draft PR #5146 at
`d6337b6fead686ec6fbfab714c3daf51bb4ce68c` (base
`e3a38d535b1e2947d9b76150acdf9276747c3146`).

Browser acceptance confirms all five menu choices open, 2D exits Underground or
Compare, the active-view badge follows the selected view, source status survives
reload, and Escape in Map preserves the Layers source view and restores menu
focus. The narrow-screen menu exposes all five views. Actual free county,
report JSON and report HTML downloads succeed. All 105 county features,
properties and geometry equal the previously published f44 county download;
only its envelope retrieval timestamp changes. Report HTML contains no script
and preserves the no-released-domain-records limitation.

The initial local 14-layer flowing-water interrupted-pan sample measured 29.25
FPS with other test maps open, and 39.25 FPS after those test maps were closed;
both preserved the display-data signature. These results do not pass the 60 FPS
target. The first native Chrome published-baseline sample ran at about 1.33 FPS
with 1,000 ms browser frame intervals. After the owner foreground handoff, the
published sample still measured 1.42 FPS (40 visible data features), while native
Chrome on the local candidate measured 1.33 FPS (16 visible data features). The
document reported visible, but these one-second frame intervals remain consistent
with browser/window throttling. Their actual map canvases also differed:
1280×576 pixels published versus 1066×420 local. These are not a comparable GPU
acceptance pair; neither proves the 60 FPS target. No performance pass or
production acceptance is claimed for this candidate. Review artifacts are in
`/tmp/kfm-hosted-source-review-20261014`; they are local verification receipts,
not a governed release or durable application archive.

Broader test inspection exposed old Local Atlas/toolbar assertions, which now
follow the intentional hosted navigation change. The legacy rendered-HTML suite
also assumes a Cloudflare `worker.fetch` entry rather than this Node build (five
incompatible cases); two report-label assertions fail on both the exact f44 base
and this candidate. They are recorded separately, not reported as passing or as
new capture/navigation failures. Actual Node HTTP checks pass against the rebuilt
candidate. No full-suite pass is claimed.

### Phone-control repair — October 14

The phone screenshot still shows published `f44ce0c`. GoDaddy preview now runs
`bf45476486712501bc3d495214877cc5fb5f5f58`, which contains the merged #5157
navigation/capture candidate and the separate private-storage probe. This repair
starts at the current hosting source `f93a545446a23d4057661f09daf2359afac44a01`
(merged #5159), then rebased onto
`0608b34004eee67793c4fe39627ff298d38aae77` after the separate PC-inference
#5163 merged. Its PC research routes, worker, handler, store and private-storage
probe are retained byte-for-byte. Other chats' unfinished PC/AI work is not
edited or overwritten; a new preview change must be coordinated.

Map and More previously closed on a focus-out event with a null destination.
That can hide a command between touch pointer-down and click. They now dismiss
on a real outside pointer or a known outside keyboard-focus target; inside taps
and null focus hops keep the command available. Escape and focus return remain.
Both menus use opaque backgrounds in the later-loaded theme as well as base
styles; the theme previously overrode the base repair with transparent glass. Layers and Places explicitly leave the
retained Source status view, and Places counts all selected map layers rather
than reporting only the empty governed-domain registry as "0 visible layers."
A temporary phone-test Place was saved and deleted successfully. Saved-place
cards label their retained count as domain layers: public-source selections are
not persisted by the existing workspace snapshot, so no source-restoration
capability is claimed.

The dependency-closed Underground repair from merged #5137 is composed here:
the hash-verified kfm.2 runtime serves standalone gzip data without treating it
as a transport variant, retains all original dataset bytes and compressed script
negotiation, fits valid deeper recorded intervals within the existing 12 km
ceiling, and distinguishes source delivery failures from absent geology. The
existing 50-record/400-interval budgets and source depth references remain.

Compare now offers a real 2010/2020 Census count comparison through the existing
bounded county-edition APIs. Both complete 105-county editions must validate and
join by FIPS before totals appear. Population and housing counts retain units;
missing values stay missing and zero denominators have no percentage change.
County selection, reversing A/B and a free provenance-bearing JSON download are
supported. One successful public-source pair is cached for this page, with an
explicit refresh; closing the panel aborts pending reads. No map-draw polling,
archive write, source admission or release transition is added. Optional local
road-linework comparison is collapsed; governed swipe comparison remains held.
New files belong to the existing app/ display-model/component responsibility and
tests/ validation responsibility under Directory Rules and ADR-0029; they create
no new registry, contract, policy or release authority.

Actual source checks matched all 105 FIPS: population 2,853,118 (2010) versus
2,937,880 (2020), and housing 1,233,215 versus 1,275,689. Browser selection of Allen
County and reversed years produced the matching free comparison download with
source URLs, retrieval times and external-context/non-release labels. At 390 px
the page has no horizontal overflow. The local High Plains cutaway reports 4/4
files loaded, 224 eligible records, the bounded 50-record sample and 28 plotted
columns; the high-detail surface reports 2048×2011 pixels. Coverage still labels
the record cap and any unavailable selector-map image separately. A real gzip
URL returns HTTP 200/application-gzip, no Content-Encoding, and the original
210,103 bytes with SHA-256
`d4a9897aa6bc291d0326c9b8454cb3b6579792d80d8d0207fe2d5ecc11889cce`.

Browser command acknowledgments occasionally timed out even after an action
completed; fresh accessibility state verified the result. An inspection timeout
reset the browser-control session, recovered on the same existing tab. The
cutaway renderer inspection retains its existing demand-driven frame scheduler;
no speculative rendering change was made. Physical iPhone/Safari acceptance,
new hosted-preview acceptance and 60 FPS remain separate open checks. Build,
types, changed-area lint, unit and HTTP results must be recorded at the final
head; no new deployment, publication, capture activation, DNS or payment change
is established by this source repair.

Final application-source validation at
`c0b5cd6834dc6ec6c946bc34489b663efe9e8c45` on the #5163 base: production build
and TypeScript pass; changed-area ESLint has zero errors and the same 41
inherited page warnings. All 93 focused tests pass (79 phone, comparison,
cutaway, gzip and capture checks plus 14 preserved PC-inference checks), and
12 actual Node HTTP checks pass. The prior restricted run could not create its
temporary gzip-test listener; the successful run used local-network permission.
No inherited or unrun full-suite result is relabeled passing.

The final rebuilt browser shows an opaque menu with all five map commands,
working outside-pointer/Escape dismissal, Layers returning to Browse after
Sources, Places reporting five selected map layers, and Map controls opening
Explore. A final real statewide free JSON download contains all 105 counties,
exact dated population/housing totals, source URLs and non-release flags.
Source-data files and the preserved PC-inference implementation are unchanged
relative to the exact base. Screenshots and download evidence are local review
artifacts; they establish neither physical Safari acceptance nor hosted
publication. Rollback is the exact prior hosting revision; archive captures,
DNS, payments and publication remain outside this repair.
