# Current access: anonymous application

The owner removed all application login on 2026-10-19. ChatGPT redirects, PC
accounts/invitations/passwords, GitHub owner OAuth, session endpoints, and browser
capture controls are removed. Public chat/map/export remain available. Retired private browser destinations
and their navigation links are removed. `login-removal-20261019.md` supersedes the historical
account/access descriptions below. No previous account or session cookie grants
access. The original private Sites project is unchanged.

# GoDaddy Node preview candidate

## Private-workspace holding page · 2026-10-17

Public browser acceptance found `/stewards` redirecting to the unimplemented
`/signin-with-chatgpt` address and showing a 404. The standalone identity adapter
intentionally returns no Sites identity; hosted AI administrator accounts do
not grant private Site access. Anonymous `/data` and `/stewards` now reuse the
existing explanatory notice instead of sending visitors through that dead
sign-in path. Local-address wording and the existing separate private Site
link are retained. The host header chooses wording only. Identity, assignment,
store availability and API authorization remain authoritative and unchanged.

The built-handler regression failed on the unchanged base with a 307 redirect,
then passed with the holding page. It checks both hosted pages, retained local
wording and 401 denial for forged staff headers on submission/water/weather
administrator APIs. This is a UI repair, not a provisioned sign-in adapter,
storage connection or private-workspace activation. Existing `app/`, `tests/`
and `docs/` own the change under Directory Rules and accepted ADR-0029; no new
root or data authority is created. Rollback is application reversion and
redeployment, preserving all settings, model files, accounts and private stores.

## Browser asset staging — 2026-10-17

The final preview initially returned404 for the advertised browser hydration
module despite a healthy application status. Reload and preview restart did not
repair it. The emitted file existed in the verified local build, while the
host's durable public/assets directory was empty. The build now stages the
exact dist/client/assets browser files into that existing public directory.
This tests the host's public-file delivery path; hosted recovery still requires
browser readback and is not inferred from the diagnosis.

Prebuild first retains a prior compiled build when present; only an absent
prior build may be skipped. Postbuild requires the new emitted assets. The
staging script accepts bounded hashed browser filenames, rejects symlinks
and unexpected files, skips source maps, and verifies byte-identical existing
files. New files use an atomic no-clobber link; conflicting immutable bytes hold
the build. Older assets and unrelated files are retained for open tabs. There
is no deletion, data import, account change or source-value/geometry transform.
Generated assets are ignored in Git; the script and tests are authoritative.
Each build is bounded to4096 entries,64MiB per file and256MiB in total. A limit
or conflict needs operator review; it never silently prunes existing material.
Tests verify deterministic reruns, prior-version retention, tamper/symlink
denials, and every HTML-advertised module's actual HTTP response/staged digest.

## Selected-record accuracy repair — 2026-10-17

Hosted preview acceptance found the small model claiming that the 2026 map
display year was a core collection date and inventing its storage duration.
Subsurface questions now return a deterministic summary of the server-resolved,
digest-checked source record and its selected interval. Map display year,
source record time and archive edition remain separate; none establishes a
core collection/drilling date or recovery. Unsupported questions receive the
source limits rather than generated factual prose. The result stays ABSTAIN,
with null answer/interpretation and no EvidenceRefs; `sourceSummary` is an
optional presentation field, not evidence or source admission. The UI labels it
Source context. General discussion and released-evidence search remain separate.
The model, accounts, public source assets, geometry and detail controls do not
change. Rollback is the prior application revision; no store migration applies.
Regression coverage executes the real resolver/handler with a model fake that
would invent those dates, checks that inference is never called, and verifies
source-summary UI labeling, selector validation, source changes and denial.

The owner's follow-up request increases the old 48/64-token, 60-second reply
budget to 160 tokens/120 seconds for Brief and 384 tokens/240 seconds for More
detail, which is now the UI default. The worker has a 255-second hard deadline;
discussion jobs expire at 270 seconds. Cancellation, one inference at a time,
2 GiB sampled RSS containment, 512-token input context, 3 pending jobs,
30 process-wide requests/hour, 10 guest requests/hour and 15-minute retention
remain. These are bounded capacity increases, not a guarantee of complete or
correct model answers. Only the latest limited reply offers an enabled Continue reply while its
selection context is unchanged. Older reply controls remain disabled. Completed discussions and source summaries
include a safe next-step question without inventing additional facts or tools.

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

`server/capture-worker-access.mjs` accepts only the existing narrow machine
credential on the configured published origin. It can trigger due source capture;
it cannot read private captures, change controls, activate releases or publish.
There is no browser owner identity or session service.

There is no web-process timer: preview/live share storage and previews can sleep.
The narrow main-based scheduler change installs a fixed-origin GitHub Actions
cron, initially disabled, with no checkout or repository token permissions.
Its environment must restrict credential access to protected main. The template
in this candidate is documentation, not an activated schedule. GitHub cron may
be delayed; its first stored receipt and subsequent scheduled run need separate
acceptance. See the scheduler PR and its `docs/runbooks/godaddy-hosted-capture.md`.

Hosting setup must supply DB_HOST/PORT/NAME/USER/PASSWORD, a verified database CA
in KFM_DB_CA_PEM with KFM_DB_TLS=verified and a DNS DB_HOST matching its certificate
(IP-only endpoints stay unavailable rather than skip identity verification), a separate random base64url KFM_CAPTURE_WORKER_TOKEN (43–256 characters). Set
KFM_PUBLIC_ORIGIN=https://kansasfrontiermatrix.com,
VINEXT_TRUSTED_HOSTS=kansasfrontiermatrix.com (exact allowlist for the hosting TLS
proxy; never a wildcard), KFM_RUNTIME_ROLE=published,
KFM_INGEST_ENABLED=true and KFM_ARCHIVE_CAPACITY_CONFIRMED_BYTES=80000000000 only
after capacity and configuration are confirmed. Shared secrets alone do not
start any worker. The SQL seed stays paused. Browser pause/resume controls are removed; no schedule or database state is changed by the login removal.

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

## Public crawler discovery — October 15, 2026

This bounded change starts from the published GoDaddy app `q9r9beo47t` at
`2c6db1f77ba16cb7dfa494e84c58d5f927c3c00f`. The configured branch has newer
unpublished work; updating it wholesale is outside this crawler-only package.

`/robots.txt` permits ordinary public pages and assets while asking crawlers
to avoid APIs, operational views, record views, and query-specific URLs.
`/sitemap.xml` lists only the existing public homepage and About page on
`https://kansasfrontiermatrix.com`. No source records, exact locations, private
storage, authenticated routes, or data releases are added to the sitemap.
The GoDaddy layout uses that verified domain for social metadata; the historical
Sites identity snapshot and original Site's audience/bindings remain unchanged.

Placement reuses this standalone composition's existing `app/` implementation
root, `tests/`, and hosting documentation. `app/crawler-discovery.ts` owns the
public text; the two route handlers provide the standard media types because
the pinned Vinext static server treats TXT/XML files as octet-stream downloads.
This follows the responsibility rule in the adopted Directory Rules v2
(ADR-0029); it creates no new repository root, registry, policy, source, or release authority.

Crawler instructions are advisory, not authentication, a safety certificate, or
a vendor category decision. Existing server authorization and release controls
remain authoritative. Verify live GET/HEAD media types, public-page metadata,
and anonymous admin denial after deployment. Local checks do not prove GoDaddy
publication or that a classifier has recrawled the site. Rollback is a revert
and redeployment of this crawler change, with no data/storage migration.

Validation: the production build, TypeScript, the changed canonical-metadata
assertion, and all 14 actual Node HTTP checks pass. The HTTP checks cover crawler
GET/HEAD responses, literal public metadata, anonymous operational denial, forged
identity rejection, and existing free report/map downloads. This is changed-area
validation, not a claim that the legacy full test suite passes.

## Browser policy, public contact and login admission — October 16, 2026

This bounded repair starts from published crawler revision `2c10fd8`, preserving
all unrelated development branches and the original Sites audience/bindings.
The existing `server/`, `app/`, `tests/` and `docs/` homes own runtime, public UI,
validation and behavior documentation under Directory Rules v2 / ADR-0029.
There is no new data, policy, schema or release authority.

Node startup and route configuration now share browser headers. The startup
listener covers static assets and early framework errors; route-specific
stricter headers can still replace defaults. CSP allows same-origin scripts,
inline hydration/style and WebAssembly required by the current map runtime,
HTTPS provider resources and same-origin/blob workers. It denies objects,
restricts forms/base URLs and permits framing only by this origin and the
verified GoDaddy dashboard parent. This is a compatible baseline, not a strict
nonce-based script policy. HSTS has a one-day lifetime without preload or
subdomain enrollment. The homepage uses a server Link canonical; About and the
new Privacy page retain distinct HTML canonicals. The owner supplied
Andy.barta.pro@gmail.com for public contact/privacy questions. Historical Sites
identity remains preserved and is explicitly distinguished from this public
GoDaddy composition. Privacy is included in the sitemap and map navigation.

The scoped server review found that 30 anonymous attempts against nonexistent
PC AI usernames could exhaust all accounts' shared login budget. Unknown-name
dummy hashing now has its own 30/minute bucket; enabled accounts retain their
five-attempt/15-minute budgets. Hashing is asynchronous, with two real-account
slots/eight waiting requests and one unknown-name slot/two waiting requests.
One real account can have only one pending verification. All ordinary failed
credentials/admission denials return the same 401/SIGN_IN_DENIED response;
production failures have a 250–300 ms minimum randomized response floor without
extra hashing. This does not establish perfect timing indistinguishability.
Concurrent revocation and invitation activation are rechecked after hashing.
Existing password encodings, sessions, roles, evidence and storage remain intact.
No client forwarding header is used as identity. A targeted attacker knowing a
username can still consume that account's budget; distributed floods and host
resource exhaustion remain provider/operational concerns. The new hash budget
is 30 unknown hashes/minute plus at most 250 real-account hashes/15 minutes,
with bounded concurrency, rather than the prior universal 30/minute lockout.

Validation covers real built HTTP policy/canonical/privacy responses and
protected-route denial, unknown-name flooding, independent accounts, bounded
asynchronous hashing, original PC-role/session/job tests, type checks and the
production build. Full suite and hosted/browser results must be recorded
separately; passing these checks does not certify a vendor category or corporate
network access. An npm audit identified the unpatched upstream braces recursion
advisory GHSA-vfj7-8cjw-p6xm through build tooling; no unrelated framework
downgrade or unreviewed dependency fork is included. No malicious live use is
inferred from that advisory.

Rollback is redeployment of the prior pinned revision; no data migration or
credential rotation is introduced. Browser HSTS can persist for one day after
its last receipt. Account attempt rows added under the reserved @unknown bucket
expire through the existing cleanup path. No support ticket, vendor review
submission, DNS change or broad firewall disable is part of this repair.

Final local comparison: production build and TypeScript pass. The complete
candidate suite reports 1,161 passing, 49 failing and one skipped test. All 49
failure names reproduce on an isolated, freshly built worktree at the unchanged
published `2c10fd8` baseline; no new failure names remain. The obsolete source-text
assertion forbidding any framing restriction is replaced by real built HTTP
coverage of the explicit GoDaddy framing policy. The focused HTTP/authentication
checks pass, including the new asynchronous-revocation regression case. CDN
email obfuscation was observed live on Barta; no-transform preserves public
contact HTML and prevents mutation of React-rendered contact text on KFM.

Live read-only checks also confirmed the configured PC service answers status on
the apex but correctly holds www with PC_AI_ORIGIN_HOLD. An exact www-to-apex 308
redirect now canonicalizes navigation before browser sign-in, preserving path
and query. This keeps authentication's exact origin requirement; it does not
accept an additional origin or change DNS. Actual built HTTP tests cover root,
query-bearing About and API status redirects.
# Verified-local publication reconciliation — 2026-10-17

The owner requested a preview check and conditional publication of the verified
local improvements. The starting live GoDaddy revision is `4b3cc837e9c131e5eb214427e0a55646fc76e52a`.
The candidate preserves its successor hosted AI/login work through `04dd130`,
including server-resolved selected-record context, then reconciles the reviewed
public navigation branch `0887e47` with the installed local composition `cd10ee6`.

Starter previews, explicit layer selection, retained source/time limits and the
Science lab search are carried from the compatible public navigation commits.
The one CSS conflict keeps both the hosted phone-login rules and Science lab
styles. The local water terrain-upload optimization and its regression test are
copied exactly; unchanged Float32 heights avoid redundant GPU buffer uploads,
while every vertex, sample and draw remains eligible. Synthetic upload counts
are not an FPS, real-GPU or hosted latency measurement.

The Node server, authentication, account/job stores, model configuration, shipped
subsurface assets, provider geometry, numeric values and independent 2048/4096
controls are preserved. Local diagnostic exports and native Worker-only data or
runtime overlays are not imported. Original private Sites history and the
separate Public Staging Site remain outside this GoDaddy publication.

Validation, security review, hosted preview and publication are separate gates.
This source note records candidate composition, not completion of those gates.
The current task's verification report records their final outcomes. Roll back
application source using the retained GoDaddy revision without resetting stored
accounts, model files or data; account/state rollback is not needed here.

