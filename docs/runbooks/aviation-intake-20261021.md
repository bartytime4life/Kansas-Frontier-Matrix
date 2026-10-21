<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/aviation-intake-20261021
title: Aviation intake discovery and held implementation
version: v0.1
type: runbook
status: draft
owners: ["@bartytime4life"]
created: 2026-10-21
updated: 2026-10-21
owning_root: docs/
responsibility: Evidence-backed aviation discovery, placement, validation and remaining gates.
truth_posture: CONFIRMED source inspection and local implementation; PROPOSED infrastructure; no release.
policy_label: public
[/KFM_META_BLOCK_V2] -->

# Aviation intake: October 21, 2026

Implementation is a private FAA candidate lane and a held hosted control. It is
not a released aviation capability. No deployment, live database migration,
second-PC change, source activation or publication was performed. No OpenSky
payload, aircraft metadata, live tracking or sensitive contact fixture was fetched.

## Authority and scope

| Surface | Exact inspected checkpoint | Effect |
|---|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix`, `main@7f2f683e5267f76d40af6b609c6110a41758be42` | Main control/processing implementation |
| GoDaddy composition | `a0-hosted-ai-web-20261017@c27e2b2cd193a8a93ae14603fafda4514fd8fce5` | Separate authoritative hosted application source; root AGENTS read |
| Governed Site mirror | `apps/site/source/` on main | Preservation instructions read; no mirror edits |
| Directory authority | accepted ADR-0029; `docs/doctrine/directory-rules.md` | The supplied Directory Rules PDF is lineage, not the writable authority |
| Contributor reliability | current CONTRIBUTING.md and PR template; supplied Reliability System PDF | Exact heads, bounded tests, review separation, rollback |
| SQL intake packet | `KFM-GoDaddy-SQL-Intake-20261021.zip` reviewed privately | Prior SQLite metadata rehearsal, not a live MySQL migration |
| Placement decision | supplied September 10 Data Placement & Site Realization PDF | Control/data/public split retained; old runtime/status claims not carried forward |
| Existing NTAD | `connectors/ntad/README.md`; six-line placeholder `ingest_hifld_ntad.py` | No executable connector to extend; FAA is a separate source |
| Open PR overlap | GitHub open collection returned zero entries during initial check | Recheck immediately before draft creation; not proof about all active branches |

`AGENTS.md` was absent on main, present at hosted root and in the preserved Site
mirror. Hosted instructions retain app `urdng3v1vk`, existing AI configuration
and original Site bindings. These are repository instructions, not verification
of the currently deployed revision. GoDaddy tools in this session supported only
domain discovery; no live host configuration, DB version or storage was inspected.

Directory Rules basis: `DIR-PLACE-002/003`, `DIR-EXEC-001/002`,
`DIR-SOURCE-003`; existing `roads-rail-trade` lane (transport alias). Acquisition
belongs in `connectors/faa/`; transformation in the existing pipeline lane;
meaning/shape in existing contracts/schemas lanes; DDL/recovery in
`migrations/database/` and `migrations/rollback/`; tests/fixtures and discovery
documentation in their existing roots. Source-registry admission is held pending
an approved exact-product descriptor; this change does not add an unvalidated
assessment object to the source registry.
No new top-level root, policy store, evidence schema, release authority or warehouse
is created. The discovery matrix does not activate any source.

## Discovery and source-rights matrix

All URLs below were checked or followed from the requested discovery pages this
session unless explicitly marked inaccessible. Landing pages are not datasets.

| Product | Purpose / authority | Format and coverage | Time / cadence | Access and cost | Rights / sensitivity / activation |
|---|---|---|---|---|---|
| [FAA NASR APT](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/2026-10-01/) | Official landing-facility reference | ZIP; APT_BASE/RWY/RWY_END and other CSVs plus layouts; national, filter KS + configurable adjacent states | Effective 2026-10-01, exclusive end 2026-10-29; 28-day editions; source publication time unknown | Public exact APT download, no key/payment encountered | Captured privately; product rights and sensitivity review pending; contacts not parsed; HELD |
| [FAA NASR next cycle](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/) | Preview reference | Separate preview product | 2026-10-29 is future on inspection day | Public download is not activation | Disabled; never choose newest URL as current |
| FAA NASR NAV/FIX/AWY/CLS_ARSP and AIXM | Official navigation/fix/airway/airspace references | Exact CSV groups, AIXM 5.0/5.1, class airspace shapefiles linked from current cycle | Edition-specific | Public links verified; parser schemas not inspected | Follow-on held; airspace floor/ceiling units, references and geometry must be verified |
| [FAA ADDS](https://adds-faa.opendata.arcgis.com/) | Official geospatial delivery | Service landing page reached; exact item/service/schema not established | Item vintage/refresh unknown | Access, limits and exact terms need item review | Discovery only; no invented layer IDs, scale or feature-service endpoints |
| [FAA statistics/downloads](https://www.faa.gov/data_research/aviation_data_statistics/data_downloads) | Administrative/safety/statistical products | Product-specific, not automatically features | Product-specific | Product-specific | Separate assessment; no joining counts to observed aircraft or mapping personal registry data |
| [OpenSky REST](https://openskynetwork.github.io/opensky-api/rest.html) | Surveillance observations; incomplete receiver support | JSON state vectors, WGS84 lon/lat; separate barometric/geometric altitude in metres | time_position, last_contact and response time differ; recent state limits apply | OAuth2 client credentials, 30-minute token; tier/area-dependent credits, not a refresh guarantee | [Terms](https://opensky-network.org/about/terms-of-use) require written operational license; disabled ingestion/display/derivatives/AI |
| [OpenSky Trino/scientific/aircraft metadata](https://opensky-network.org/data) | Historical surveillance / supplemental products / mixed official-unofficial metadata | Trino/Minio and dataset-specific downloads, CSV metadata | Different snapshots, supplemental conditions; metadata irregular | University/government/aviation access eligibility; private/commercial license contact required | Each product requires its own agreement, retention and redistribution review; disabled |
| [mode-s directory](https://mode-s.org/atmdata/sources/) | Discovery only | Provider/tool links | Directory descriptions can lag | Not a service grant | Directory license does not govern provider data; never bulk-ingest directory |
| [adsb.lol historical](https://www.adsb.lol/docs/open-data/historical) | Independent surveillance candidate, Kansas history use case | Daily global split tar archives of gzip readsb traces/heatmap, not Kansas extracts | Actual observed days, provider gaps and replicas | Public archives; resource and download costs must be measured | Provider states ODbL 1.0. Attribution/share-alike and public/derivative obligations require review. Sensitivity and coverage unknown; disabled |
| [adsb.lol re-api](https://www.adsb.lol/docs/feeders-only/re-api/) | Independent moving-aircraft rendering candidate | readsb HTTP API; provider network | Bounded polling and latency not yet measured | Legacy API deprecated; feeder station IP restriction documented; [adhoc key request](https://www.adsb.lol/request) reviewed by provider. No guaranteed free operational entitlement | ODbL stated; no key requested, no account/receiver/tunnel set up; disabled |
| [OurAirports](https://ourairports.com/data/) | Community airport reference for cross-check, not FAA replacement | CSV and data dictionary | Community updates; no FAA cycle equivalence | Data landing page intermittently inaccessible during this session | Public-domain claim needs direct successful terms readback before activation; no ingestion |

OpenSky's [own description](https://opensky-network.org/about) identifies volunteer,
industrial and academic/government sensors receiving ADS-B and Mode S at 1090 MHz.
There is no single upstream public API to substitute. An independently owned
receiver could supply local observations without consuming OpenSky's database,
subject to its own radio, privacy, source and publication review. It would not
supply statewide historical completeness. A rendering, raster tile, delayed
animation or AI summary of OpenSky data remains subject to OpenSky's agreement.

OpenSky documentation at inspection listed 400 anonymous / 4,000 standard /
8,000 active-feeder daily credits per endpoint bucket, and licensed hourly
allocations; bounds alter request cost. These values do not establish KFM account
eligibility. Terms require publication citation, restricted redistribution,
de-identification, and expunging copies on termination subject to stated
reproducibility allowances. No KFM written agreement was available to verify.

## Physical placement and database reconciliation

CONFIRMED code evidence: hosted `server/ingestion-store.mjs` uses mysql2,
prepared statements, verified TLS, bounded connection pool and existing intake
transactions. `server/ingestion-schema.sql` is the existing intake schema. The
prior packet reports a MySQL dashboard but explicitly lacks live introspection.
Live engine version, schema, CHECK behavior, extensions, quota, grants, backup and
restore are UNKNOWN. No PostgreSQL or PostGIS installation is assumed.

PROPOSED: retain GoDaddy MySQL for bounded metadata/projections, with large
immutable captures/history/processing assets on the second AI Linux PC. Git
retains code, migrations, small synthetic/schema fixtures, digests and review
records. Public browsers receive only released projections via governed APIs.
No public DB port, private mount, raw archive, Ollama endpoint or admin service is
exposed. No alternate platform is deployed. If later spatial operations justify
PostGIS, propose a separately reviewed compatible processing stage and exchange
contract; do not replace MySQL or import SQLite/D1 migrations into it.

The earlier packet's 213.05 GB RAW inventory and 105 held KDOT PDF rehearsal are
historical observations from that packet, not remeasured here. They remain separate
from this aviation capture; prospective road classification maps are not current
measured road geometry. No local intake state was assumed on the second PC.

Proposed initial aviation budgets, requiring measured capacity before adoption:

- FAA reference: at most 13 retained 28-day editions, 16 MiB compressed cap per
  APT capture, 64 MiB expanded parsing cap; budget 1 GiB including receipts,
  candidate revisions and working overhead. No automatic purge in this change.
- Observations: disabled. Before any enablement, pilot one bounded Kansas
  interval; measure bytes/day and CPU/I/O/inference impact. Proposed 20 GiB pilot
  ceiling and 30-day retention only if rights and restore requirements permit.
- One capture/transform at a time; 128 MiB disk reserve is a minimal per-task
  stop threshold, not a verified host-wide AI reserve. Choose a larger host reserve
  after measuring model files, RAM/VRAM, inodes and peak inference I/O.
- Immutable content checksums, `.part`/temporary work followed by fsync and atomic
  completion. Retry restarts an incomplete small capture; byte-range resume and
  persistent scheduler backoff are not implemented. Respect provider 429/503.
- Verify a second copy in another failure domain, manifests and a real restore
  before relying on the second PC. Original copies remain until reviewed cutover.
  Backups of rights-limited observations must follow revocation/deletion terms.
- If the PC is unavailable or disk budget fails, capture fails explicitly;
  public aviation remains ABSTAIN and unrelated map functions continue. Future
  released caches must bind immutable digests, show age and expire under policy.

No target hostname, IP, mount, port, disk path or tunnel is invented. Second-PC
storage, connectivity, resource capacity and backup arrangements remain NEEDS
VERIFICATION; its AI configuration is unchanged.

## Concrete mapping and query model

The MySQL 8.0+ additive DDL is a candidate, not proof of the live engine. Its
`kfm_faa_captures` and `kfm_faa_airport_revisions` are private HELD candidate tables,
with no approval or release mutation API. Run only in a disposable tested database
before proposing application to the shared environment. DDL is not transactionally
reversible across all engines; use the paired manual rollback only after backup.

| Source field | Candidate / SQL destination | Semantics |
|---|---|---|
| Product URL, whole ZIP SHA-256, receipt clock | capture row / private RAW receipt | exact product/retrieval; no contact payload in SQL |
| EFF_DATE | edition / valid_to_exclusive | reference validity, not observation/release time |
| SITE_NO + SITE_TYPE_CODE | entity_id | original source strings preserved including variable fractional digits |
| Edition + allowlisted row digest | revision_id | correction changes revision; entity remains stable |
| ARPT_ID / ICAO_ID | faa_id / icao_id | distinct optional identifiers; IATA not inferred |
| ARPT_NAME | name | source reference name |
| STATE_CODE / COUNTY_NAME / COUNTY_ASSOC_STATE | state / county_name / county_state | provider association only; no Census join asserted |
| LAT_DECIMAL / LONG_DECIMAL | latitude / longitude | finite geographic coordinates; horizontal datum unverified, public geometry held |
| ELEV | elevation_ft_msl | explicit feet MSL, null preserved; no aircraft altitude conversion |
| use/ownership/status/type | public_candidate | only open public-use airports, known nonmilitary ownership; still HELD |
| record digest/capture digest/source URL | EvidenceRef + existing EvidenceBundle in record_json | quarantine evidence candidate, not approved answer |

Header schema changes stop the whole transform. Invalid rows preserve allowed
originals and reasons in private quarantine; partial coverage is explicit.
No station/aircraft identifier join is attempted. The schema uses existing
EvidenceRef and EvidenceBundle schemas, not the permissive hyphenated scaffold.

County lookup uses fixed prepared SQL, KS + county association and LIMIT 201 to
return at most 200 with a truncation flag. The composite candidate/state/county/
revision index supports the initial query pattern; there is no speculative
partitioning for 380 records. Production MySQL EXPLAIN/latency remains unrun.
The isolated SQLite rehearsal is explicitly labeled and cannot establish MySQL
performance. Reference editions and observation playback stay separate.

## Local workflow and validation

Install repository Python requirements, choose an existing private RAW directory,
and call `connectors/faa/capture.py:capture`. Then run from the repository root:

```bash
python3 tools/local_data/faa_airport_rehearsal.py /private/raw/faa-apt-2026-10-01 /private/new-review-output
python3 -m pytest tests/connectors/test_faa_airports.py -q
```

The paths above are operator placeholders, not a chosen second-PC placement.
The output directory must be new and private, outside Git. It contains a held
candidate and isolated rehearsal database. `inspect_selection` follows private
revision -> EvidenceRef -> bundle -> explicitly HELD review report; it is never
exposed to ordinary browsers. Revision correction preserves prior evidence.

Actual results and immutable candidate identity are recorded in Final local evidence.
Source capture/header/row processing, retry/deduplication, malformed records,
coordinates/elevation, future editions, disk reserve, SQL bounds, evidence tamper
and correction/rollback have targeted tests. Hosted tests cover denied queries,
AI tool bounds and retirement of delayed work on Present/date/selection/layer
changes. A separate aviation release profile remains a blocker, so the existing
map control and HTTP endpoint return ABSTAIN without acquiring a database client.
No synthetic real-looking aircraft are installed in the production layer catalog.

Unrun: live GoDaddy DB/host/engine introspection, MySQL migration/import/EXPLAIN,
second-PC outage/restore on the actual host, actual provider coverage, browser
visual/touch/keyboard acceptance, production report citation closure, approved
release verification-history replay and public withdrawal. A build or a held
control does not close these gates.

## Remaining work and rollback

Before public FAA rendering: product rights/sensitivity admission; horizontal
CRS/datum verification and transform; exact release-profile integration with
existing policy/verification-history replay; reviewer identity and valid release
binding; released projection; selection/drawer/report readback; correction and
withdrawal acceptance; desktop/mobile browser QA. No single environment flag may
bypass these gates. Main-map camera is untouched by the held control; its pending
requests are canceled/generation-checked when context changes or it closes.

Then implement runway and other FAA groups one verified schema at a time. Evaluate
one independent live surveillance source and one bounded historical interval with
source-specific terms, units and uncertainty. Do not derive traffic counts,
trajectories or comparisons until coverage, rights and method validation close.

Code rollback: revert either draft change independently; no data release exists.
Private rehearsal rollback: retain immutable RAW/receipt and remove only the
operator-created disposable review directory when no longer needed. Live rollback
is not required: no live writes occurred. Future migration recovery must preserve
captures, foreign-key order, backup digests and a tested restore; the paired DROP
script is for reviewed disposable use, not routine production rollback.

## Final local evidence

- FAA APT ZIP: SHA-256 `aba48ea877f249d9b8cd63988b14b3432a6a09ad1fbe9561a5e6443c99c03dd0`; 8,030,968 bytes, captured through the fixed-product adapter.
- Candidate `sha256:2f88f3f6ad34c199f119bb52bd935fc9d09f8d9826739a27e0a07f72ca0d5e6f`: 380 Kansas landing facilities, zero rejected records; 148 open public-use airport candidates, all HELD. Source edition 2026-10-01.
- Isolated SQLite 3.53.1: first insert 380, retry insert 0, integrity `ok`. Ellsworth provider-county lookup returned one record. Composite `faa_county` index used; observed query 0.179 ms and retry 0.065 ms on this disposable environment, not a production benchmark.
- Python targeted suite: 20 passed. Candidate and bundles validated with existing local schema resolver. Private selection/evidence/report tamper and correction checks pass.
- Hosted: eight targeted Node tests pass; final complete standalone suite 1,613 passed, 19 skipped, zero failures; Python-produced actual candidate passed JS digest/import preparation for all 380 records with a fake connection (no MySQL execution). Production build and generated-identity TypeScript check passed. Built Node HTTP checks returned 200 ABSTAIN for a valid county/edition query and 400 for a SQL parameter; both no-store.
- Public hold decision was emitted by the hosted adapter and recorded in `data/receipts/validation/aviation-public-hold-20261021.json`. It is an unauthenticated ABSTAIN process receipt, not a rights/release approval or accepted general policy-evaluator claim.
- Whole-repository topology: baseline and head both PASS with 89 identical inherited warnings, zero new drift/invariants and zero stale entries; no baseline edits. Hosted CI is pending exact-head execution; no inherited or unrun check is called passing.
