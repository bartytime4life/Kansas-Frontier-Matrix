<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/api-connections-20261014
title: KFM additional API connections and dual-host intake
type: runbook
version: v1
status: implementation candidate; credential, provider, storage, review and publication gates pending
owners: ["@bartytime4life"]
created: 2026-10-14
updated: 2026-10-14
policy_label: public
owning_root: docs/
responsibility: Operate and review bounded API intake on Sites and the separate GoDaddy Node composition
truth_posture: CONFIRMED source and local validation; hosted activation NEEDS VERIFICATION
[/KFM_META_BLOCK_V2] -->

# API connections on both hosts

The owner selected all 15 researched connections plus the previously implemented
NOAA NCEI products, across the owner-private Sites Explorer and separate GoDaddy
Node app q9r9beo47t. This change adds bounded backend acquisition and private
frontend inspection, rather than claiming source admission or public data release.

Both applications provide /connections and /api/connections. The interface
selects a provider, station/county/AOI, product and supported dates. It shows
native records, source geometry or georeferenced imagery, native-value plots,
partial/empty/error states, original provenance and verified saved replay.
Public callers can read connection metadata and host status. Receipt lists,
capture, raw/bundle download and data previews require existing owner authority.
A capture does not become a main-map evidence layer or a released export.

## Owning roots and deployment mirrors

Placement uses the checked Directory Rules v2 adopted by accepted ADR-0029:
source-specific request builders and parsers extend connectors/; source-agnostic
portable HTTP primitives extend packages/connectors-core/src/; orchestration
uses pipelines/ingest/shared/; the operator uses tools/local_data/; host
composition and user surfaces stay in the existing application; guidance uses
docs/runbooks/. No registry, schema, policy or release home is replaced.

The new ESM primitives coexist with the existing Python package. This is a
bounded runtime extension, not a migration of Python consumers. Existing source
lanes remain authoritative. The EPA AirNow/AQS adapter uses the existing EPA lane
without claiming to resolve the older informational AirNow lane authority.
KDOT uses existing connectors/kansas/kanplan provenance rather than claiming the
parallel informational kdot lane is an admitted registry.

tools/local_data/bundle_api_connections.mjs creates deterministic application
mirrors under app/api-connections-runtime/. manifest.json binds both canonical
and deployed hashes. These are packaging copies, never additional canonical
connector, contract, source-registry or rights authorities. Regenerate them from
the implementation roots and compare hashes; never fix an individual mirror.

The standalone Sites source starts from same-project 902c1f5c60bb90ed215fc94fdeda6c1c0784834d,
including its newer river-startup change after deployed v262. The Node copy
preserves navigation/capture candidate 1c2dc18a1d7e84787da75764aeba7ba6e3c084b7 and
the subsequent exact-host-proxy repair 2418fc31630e066142d485cd26ea216d26b3ac17
(replayed locally as 78146b5). These histories are separate from the monorepo.
Independent Underground repair fa27044c remains preserved in its own checkout;
it is not silently replaced or represented as included here.

## Provider profiles

| Connection | Bounded support | Live verification / remaining gate |
|---|---|---|
| WQP | WQX 3.0 station preflight, fullPhysChem CSV, one public surface-water station, three allowlisted parameters, <=31 days | Header-only result verified; zero samples stays empty. Full-profile qualifiers, methods, fractions and limits retained |
| NASS Quick Stats | Kansas county wheat, Survey/Census, year/statistic, count-first <=5,000 rows | NASS key and terms acceptance required; native suppression stays a string |
| U.S. Drought Monitor | Kansas FIPS 20, categorical/cumulative area percentages, <=366 days | Capture/replay verified; weekly validity intervals retained; no polygon fabrication |
| DASC imagery | Fixed NG911 2024 natural-color service, small AOI, 768×768 PNG plus service metadata | Raster capture/replay verified; item/vintage rights and per-pixel dates still reviewed separately |
| USGS terrain transect | 21 explicit 3DEP multipoint samples; optional bounded NLDI process | 3DEP capture/replay verified, actual 1 m raster and reported NAVD88; NLDI upstream timed out |
| Planetary Computer | Five Landsat/NAIP STAC scene records, dates/AOI, footprints and asset names | Empty selected-date response verified. No SAS asset downloads, license clearance or synthesized pixels |
| NRCS SCAN | One of four Kansas SCAN stations, two sensor depths, daily <=31 days, QC/QA/original fields | Capture/replay verified. Depth inches, stored pct, derived daily status preserved; Tribal SCAN excluded |
| USDA SDA | Fixed numeric-coordinate SQL, <=100 horizons; texture, AWC, OM, pH, drainage, conductivity | Capture/replay verified; alternatives/components and depth semantics retained |
| AirNow + EPA AQS | Current reporting-area AQI; distinct AQS county January daily PM2.5 profile | Service credentials required; AirNow archive authorization also required |
| OSM Overpass | Small AOI roads/buildings, <=250 ways; native IDs/versions/time, restricted classes omitted from view | Provider returned 406 in this environment; no successful live capture claim. ODbL duties pending review |
| Census ACS | Kansas county 5-year estimate/MOE/annotation pairs, selected vintage | Current API requires Census key; anonymous call redirects to missing_key.html and is never followed |
| EIA v2 | Kansas monthly generation, selected year, fixed facets, <=500 rows | EIA key required; returned native units/fuel classes stay separate; paging remains partial |
| Library of Congress | Ten Kansas map catalog records per page, pages 1–20 | Capture/replay verified; pagination/rights/date limitations retained. No resource assets fetched |
| IEM ASOS | Four Kansas airports, explicit temperature/wind/METAR columns, <=7 days, UTC/end-exclusive | Capture/replay verified; M/T and limited QC retained; one-second request pause |
| KDOT KanPlan | Seven existing allowlisted layers, small AOI, <=100 GeoJSON features plus metadata | Layer metadata verified. Empty copyright/edit metadata does not clear rights; review flag required |
| NOAA NCEI | Six selected products, four Kansas first-order stations, native fields/flags; hosted <=2 MiB/entity | Capture/replay verified. Daily <=366 days, annual summaries <=10 years; normal baselines remain explicit |

NLDI's current executor accepts the legacy named-input list; its documentation
shows an object that returned immediate InvalidParameterValue in this session.
The list reached processing but the provider's elevation call timed out.
The direct 3DEP adapter is the verified primary path; NLDI successful output
remains NEEDS VERIFICATION.

[Census's current key requirement](https://api.census.gov/data/missing_key.html)
supersedes the older anonymous-access assumption in the initial research note.
The UI includes the provider's required no-endorsement notice.

## Transport, identity and storage

Every request comes from a fixed provider builder. No caller-supplied URL, SQL,
STAC asset href, pagination walk, redirect, archive root or key-bearing
provenance URL is accepted. JSON duplicate keys, nesting, nonfinite values,
structural surprises, byte/row caps and invalid geography fail closed.
One provider acquisition has a 30-second total deadline. No automatic HTTP
retry occurs. The shared lease serializes writes; IEM uses at least a one-second
pause and LoC a three-second pause. Provider failures remain explicit.

Plan identity binds version, provider, exact normalized selection, requests and
time bucket. The archive stores a reversible response bundle with per-entity
digests, metadata and a whole-bundle digest. It preserves anonymous decoded HTTP
entities unchanged. Some credential-based providers echo keys in their metadata:
those exact credential tokens are redacted before storage, with received/stored
digests and redaction counts. Such bundles are explicitly transformed, not
byte-identical original responses. Keys are never kept in plans, receipts,
browser state, source or public artifacts.

Replay rebuilds the canonical request and checks the plan identity, stored
lengths, whole-bundle and entity hashes, field structures and source scope.
A successful fetch alone never produces a frontend review result: capture reads
back the durable store, then replays the stored bytes. Invalid bounded responses
remain private for correction and cannot supply a data view.

Node uses the existing MySQL ingestion store: verified TLS/hostname, owner-only
GitHub identity, transactions, capacity reservations, fencing, chunked bytes and
a shared 80,000,000,000 accounted-byte cap. The prior schema needs no new Node
table for these bundles. Provider disk, database, index/log/backup capacity and
real MySQL behavior still require hosted verification. D1/R2 remain unbound in
this Node composition; that has not been disguised as governed-release support.

Sites adds only drizzle/0010_api_connections.sql and its journal entry. The
receipt index shares daily_archive_captures, its budget and writer lease; it
does not allocate a second 80 GB archive. Its limit is the lesser of existing
archive budget and 80,000,000,000 bytes. D1 tracks an R2 object before writing it
and verifies exact object readback before a receipt can be served. Interrupted
writes retain their reservation. Failed same-bucket D1 selections remain held,
without deleting history or silently overwriting failed attempts.

## Configuration handoff

Enter values directly in each host's server settings, never in chat or source:

- NASS_QUICK_STATS_KEY; KFM_NASS_TERMS_ACCEPTED=true only after actual acceptance.
- CENSUS_API_KEY.
- EIA_API_KEY.
- AIRNOW_API_KEY; KFM_AIRNOW_ARCHIVE_AUTHORIZED=true only after documented provider authorization.
- EPA_AQS_EMAIL and EPA_AQS_KEY for the AQS profile.
- KFM_KDOT_RIGHTS_REVIEWED=true only after rights/currentness/sensitivity review.

Consent-gated Kansas Mesonet remains outside these 15 executable profiles.
No registration, email, paid subscription, terms acceptance or consent is
fabricated by source changes.

Node's existing DB/TLS/public-origin/trusted-host/owner-OAuth/published-role/
capacity/enablement requirements remain in server/ingestion-config.mjs.
Configure the additive MySQL migration from the prior candidate only after
review; do not reset MySQL or import D1 migrations. Sites keeps its existing
owner access, DB and BUCKET bindings. Apply its additive migration through the
same reviewed Site workflow; do not reseed or replace persisted datasets.

## Scheduled profiles

/api/connections/run is a capture-only POST for existing owner or capture-worker
authority. It never returns source bytes. A worker cannot choose a URL, source
or query in its request. Configuration is disabled by default:

- KFM_API_SCHEDULE_ENABLED=true only after exact-head/runtime/profile review.
- KFM_API_CAPTURE_PROFILES: <=4,096 characters, at most 16 objects containing
  sourceId, query and optional rollingDays (1–31, only date-enabled profiles).
- A tick attempts at most two validated profiles; its hourly rotation provides
  bounded progress. Cached exact plans do not reacquire. Missed historical
  windows are not synthesized. Each capture uses its own fenced lease.

Example non-secret configuration:

~~~json
[{"sourceId":"usdm-statistics","query":{"mode":"2"},"rollingDays":7},
 {"sourceId":"nrcs-scan","query":{"station":"2092:KS:SCAN"},"rollingDays":7}]
~~~

The existing three-feed scheduler remains unchanged. The new configured-profile
endpoint is an additional ready-to-wire trigger; no cron, cloud automation or
profile activation is claimed. Verify the published host's authorization envelope
and trigger credentials before scheduling it. Preview workers remain disabled
on the shared Node database.

## Validation, promotion and rollback

Validation evidence is retained separately from source and deployment assets.
Synthetic tests are fixture evidence; live captures stay in a private task-local
evidence directory. Neither class grants source admission, EvidenceBundle
qualification, publication review, main-map activation or released exports.

Before production activation: reconcile each host's current source, review exact
heads and migrations, configure credentials/consent, verify native storage and
owner denial cases, run real owner capture/replay, complete rendered keyboard/
mobile/WebGL acceptance, and apply existing rights, sensitivity, provenance,
review and release controls. GitHub incident #4024 remains branch-only for this
writing path; do not create or merge a successor PR as a shortcut.

Rollback removes the new routes/UI/profiles or pauses capture, preserving all
captures, receipts, reservations, hashes and existing source histories. Revert
the code through reviewed lifecycle controls. Do not drop either host's tables,
delete R2 objects, reset MySQL, modify DNS/audiences, overwrite the private Site,
or roll back unrelated pending Underground work.
