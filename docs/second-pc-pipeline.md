# Second-PC acquisition, curation and GoDaddy publication

Implementation candidate, 2026-10-22. The public application remains app
`urdng3v1vk`. This kit does not change the preserved Sites application, its
bindings, the installed inference services, DNS, or existing archive tables.

## Implemented path and authority

`scripts/pc-pipeline/worker.mjs` checks a qualified data filesystem, claims
durable SQLite jobs, acquires the existing bounded Kansas USGS/NWS feeds,
preserves exact decoded entities and receipts, and builds deterministic,
allowlisted GeoJSON products. One transform runs at a time. The timer checks
every five minutes; adapters remain hourly. Missed buckets are not fabricated.

The first products are **EXTERNAL_CONTEXT_ONLY**, never admitted factual evidence.
They retain original USGS values/units and source clocks; missing discharge
remains missing. NWS is a dated snapshot, not warning delivery or an all-clear.
Null alert geometry is retained. Expired alerts are labeled and omitted from the
active map. A pagination/row-cap limit produces an explicit partial product.

Existing water and GHCN-Daily packages have a separate `stage-package` command.
Its receiver calls the existing package parser, serving gate, and evidence replay
before committing. MySQL-backed readers repeat those checks. A signed transport
delegation cannot bypass a withheld domain release. Existing Python source,
normalization, evidence and decision tools remain the producer of those packages.

The unattended PC holds a dedicated HMAC transfer credential. The original PC
holds the Ed25519 approval private key; GoDaddy holds its public key only.
Delegations bind source, role, recipe digest, rights/sensitivity review references,
maximum payload/rows, freshness, and at most 30 days. Changed recipes or expired,
revoked, or altered approvals are denied. This transport projection does not
replace the monorepo's source/evidence/release authorities.

## Commands and local rehearsal

Use Node 22.13+; SQLite uses Node's built-in experimental `node:sqlite` module.
No new npm runtime dependency is required for the PC kit.

```sh
node scripts/pc-pipeline/cli.mjs inventory
node scripts/pc-pipeline/cli.mjs rehearse /absolute/private/pilot-store
node scripts/pc-pipeline/install.mjs
node scripts/migrate-pipeline.mjs
node tests/pc-pipeline.test.mjs
```

For the separate read-only hosted SQL connectivity check, use
`npm run --silent kfm-data -- connection` from this checkout. See
[connection-only instructions](database-connection-only.md) for private local
receipts, verified TLS acceptance and failure states. This manual command does
not initialize a data mount, capture feeds or enable publication.

`rehearse` attempts all three bounded feeds into an external private directory,
including earthquakes even when the scheduled worker has not opted into them.
It never schedules, signs approvals, pairs credentials, writes SQL or publishes.
Its per-source results must be inspected: process success alone is not proof
that all acquisitions succeeded. Invalid captures remain private for correction.

## Qualify storage and backup before installing

The October 22 host readback found about 143 GiB free on the system disk and
several unmounted ext4 drives, including an approximately 1.4 TiB HDD. Their
contents and health were **not verified**: raw-filesystem inspection required
sudo authentication unavailable to this session. Do not format them.

1. Inspect existing disk contents and SMART health. Select a healthy drive with
   measured free space; mount it by UUID at `/srv/kfm-data`.
2. Keep originals on the original workstation. Inventory and hash holdings before
   any copy; use the existing monorepo local-store tools for governed captures.
3. Prepare a private store below that mount, for example `/srv/kfm-data/store`.
   Initialize with `cli.mjs init ROOT MOUNT CONFIG_OUTPUT`. The command records
   filesystem device identity and a random store marker; it refuses an unmounted
   directory on the root filesystem.
   Run the bounded `rehearse` against this store before its first backup so the
   restore exercise includes captured payloads, not only configuration records.
4. Qualify an independent backup filesystem, mounted at `/srv/kfm-backup` from
   the original PC/NAS. Initialize a separate backup root/config the same way.
   Source and backup must be different devices. A second directory is insufficient.
5. Run `cli.mjs backup DATA_CONFIG BACKUP_CONFIG`, then
   `cli.mjs verify-backup MANIFEST BACKUP_ROOT` and
   `cli.mjs restore-test MANIFEST BACKUP_ROOT EMPTY_RESTORE_ROOT`.
   The restore produces a receipt binding store ID, source/backup device and
   inventory digest. It copies and checks every selected data object, not just
   the manifest. Preserve the original copies until these checks pass.

Jobs check the actual mount and marker before writes, reserve expansion/output
space, require 20% data-disk free space and 30 GiB system-disk free space, and
defer heavy work below 3 GiB available RAM. Device changes require deliberate
requalification. There is no automatic deletion of originals, releases or receipts.

Backups stream files in 1 MiB buffers, hash the source and copy, refuse conflicts,
and preserve captures, processed objects, receipts and operational config copies.
SQLite uses a consistent `VACUUM INTO` snapshot; its database/WAL are never copied
as unrelated live files. Approval private keys remain backed up separately on
the original PC. No credentials are added to data inventories.

## Install without activating publication

Review `scripts/pc-pipeline/install.mjs` first. With a qualified mount and restore
receipt, run it as root with `--apply --config=ABSOLUTE_CONFIG`
and `--backup-receipt=ABSOLUTE_RESTORE_RECEIPT`. It installs only this kit under
`/opt/kfm-pipeline`, a dedicated system account, config under `/etc/kfm-pipeline`,
and four systemd unit files. It refuses pre-existing installation targets and
requires `publish:false`. Ensure the account can traverse the selected mount.
No inference service is restarted or edited.

The installer leaves both timers disabled. Run one capture-only service and
inspect its journal first. Then enable `kfm-pipeline.timer`. Configure and verify
`/etc/kfm-pipeline/backup.json` before enabling `kfm-pipeline-backup.timer`.
The latter runs nightly at 02:30 local time and retains failed/incomplete copies
for investigation. Repeat restore tests monthly. Both units have CPU/memory/I/O
limits; tune only after measuring coexistence with real inference traffic.
Acquisition and backup services hold the same kernel `flock` for their complete
operation. Backup waits for an active capture; capture ticks defer while backup
holds the lock. This prevents a backup from collecting a new receipt while
missing the immutable object it references. The kernel releases the lock on
process death. Pause the timers before manual acquisition/package/backup commands,
or run those commands under that same lock. Backup is a complete selected-object
copy, not a scan racing an active writer.

## GoDaddy database and artifact qualification

Preview and Published share MySQL. Before any application of SQL, obtain a
recoverable backup, inspect the real engine/grants/schema/quota and rehearse in
a disposable compatible database. The SQL is additive. A new control row starts
paused; `INSERT IGNORE` preserves an existing control row's pause/resume state.
Re-running the migration does not pause an already running pipeline.
There is no reset, SQLite import, DROP, or replacement of existing capture rows.

`scripts/migrate-pipeline.mjs` prints the SQL and digest by default. `--apply`
requires both `KFM_MIGRATION_SHA256` and
`KFM_PIPELINE_DATABASE_BACKUP_VERIFIED=true`. DDL is not transactionally
reversible; preserve partially created tables on failure.

Server setup requires the existing DB_* values, a certificate-matching DNS host,
`KFM_DB_TLS=verified` and `KFM_DB_CA_PEM`. Verification is never disabled.
Configure a **new** `KFM_PIPELINE_WORKER_SECRET` (32 random bytes, hex), the
approver public PEM in `KFM_PIPELINE_APPROVER_PUBLIC_KEY`, and explicitly scoped
`KFM_PIPELINE_ENABLED=true`, `KFM_RUNTIME_ROLE=published`. Preview must remain
disabled. Never reuse gateway/polling keys or print secret values.

Private artifact storage defaults to `/private/kfm-pipeline/artifacts`. Verify
its persistence across restart and source deployment, filesystem behavior,
available capacity, and public-path denial before placing its qualification
marker `.qualified` with content `kfm-private-artifacts-v1`. This marker is an
operator assertion backed by those tests, not a durability test by itself.
Initial reservations cap total staged/committed artifact payloads at 1 GiB and
10,000 releases, with an additional 256 MiB free-space stop. Provider database,
index, log and backup headroom must be measured separately. No retention purge
is automatic.

## Approvals and cutover

On the original PC, `cli.mjs keys PRIVATE_DIRECTORY` creates the owner key pair.
Create a review draft with `profile-template SOURCE`; review the exact source,
role, recipe digest and policy references, fill the deliberately unapproved
fields, then `approve PROFILE PRIVATE_KEY SIGNED_OUTPUT`. Copy only the public
key to GoDaddy and the signed delegation to the PC's root-owned approval
directory. Files need group-read access for `kfm-pipeline`, not worker write access.
The private key never belongs on the unattended second PC.

Owner `control COMMAND_JSON PRIVATE_KEY` sends a signed, short-lived, replay-
protected command for pause/resume, withdrawal, or rollback. The command JSON
contains `action`; withdrawal/rollback also require `releaseId` and
`expectedActive`. Only a still-valid, approved previous release may be rolled
back. `KFM_PIPELINE_REVOKED_PROFILES` is a comma-separated denylist checked again
on public reads. Revocation withholds affected data without deleting history.

After pairing credentials, install the worker's secret through systemd
`LoadCredential` and set PC config `publish:true`. Resume the SQL pipeline only
after a synthetic end-to-end rehearsal, real source approval, database backup,
artifact qualification and service/resource acceptance. Disable any overlapping
hosted/GitHub capture schedule for the transferred sources. One scheduler owns
each source/product. The original hosted archive remains separate and intact.

## USGS earthquakes as a third released source (2026-10-29)

`usgs-earthquakes` is now a released external-context source beside streamflow
and alerts. The capture is the existing fixed request (USGS FDSN, Kansas window
-102.1 to -94.5, 36.9 to 40.1, rolling 30 days, at most 250 events), now hourly
so a release stays within the profiles' two-hour freshness. The normalizer
(`server/pipeline-normalize.mjs`) keeps only magnitude, magnitude type, place,
depth in km (moved out of the coordinates, so published points stay 2D), event
time, update time, USGS review status, the event page built from the checked
event id, and that id. Events USGS marks `deleted` are left out; any other
status or event type, an id outside `[a-z0-9]`, a magnitude outside −2 to 10, a
depth outside −10 to 800 km, an event outside the window or older than 30 days
fails closed (`EARTHQUAKE_SCHEMA_CHANGED`, `GEOGRAPHIC_SCOPE_INVALID`,
`OBSERVATION_OUTSIDE_WINDOW`), as streamflow does.

Owner steps, in order, before earthquakes publish:

1. **Record the current installation and protect the two existing feeds.**
   Verify the installed worker and deployed server revisions independently.
   The worker must include the three-source `loadConfig()` correction from
   PR #5543 before changing its configuration. Record the current active release
   IDs, approval IDs/expiry times, pause state and scheduler owner. Preserve
   existing public-key trust, signed profiles, release records and raw captures.
   Coordinate any maintenance pause through the owner-signed control path;
   a source merge or this document is not activation authority.
2. **Renew the existing source profiles for the exact target recipe.** On the
   original signing PC, run `profile-template usgs-streamflow` and
   `profile-template nws-alerts` from the reviewed target source, complete the
   real rights/sensitivity/review references, then use `approve` with the
   existing owner's private key. Give each source/version a distinct profile
   ID. Never copy that private key to the unattended PC or hosting. Compare
   `inventory`'s `recipeSha256` on the signing checkout and installed worker
   against the reviewed server build before cutover. Recipe identity hashes,
   in order, `pipeline-contract.mjs`, `pipeline-normalize.mjs` and
   `ingestion-sources.mjs`; editing any of these requires renewed approvals.
   Keep old profiles with historical manifests. Public reads validate each
   release's own signed recipe, integrity, expiry and revocation; they do not
   require the current recipe digest. A valid old release can remain readable
   (and become stale), but expired, revoked or withdrawn releases are withheld.
   New transfers with the old recipe fail `RECIPE_CHANGED`; a current-recipe
   transfer carrying an old profile fails `APPROVAL_INVALID`.
3. **Qualify and apply the additive schema.** Verify a recoverable backup of
   the actual shared MySQL database and restore it into a disposable compatible
   database. PC data-store backups alone do not establish database recovery.
   Run `node scripts/migrate-pipeline.mjs` to review SQL and its digest. With
   the approved database credentials and verified TLS, `--apply` requires the
   exact `KFM_MIGRATION_SHA256`, the operator assertion
   `KFM_PIPELINE_DATABASE_BACKUP_VERIFIED=true`, and
   `KFM_PIPELINE_ENABLED=true` in the migration process so `getPipelineStore()`
   can open the pool. The assertion does not itself verify a backup. Use
   process-scoped settings; do not enable Preview or change service settings
   merely to run this command. The change from the preceding schema is the
   `usgs-earthquakes` head row; statements use `IF NOT EXISTS`/`INSERT IGNORE`.
   Existing heads, revisions and pause state must be unchanged after application.
   DDL is not transactionally reversible; preserve partial results on failure.
4. **Approve the earthquake profile and qualify all three releases privately.**
   Use `profile-template usgs-earthquakes`, review, then `approve` on the original
   signing PC. Install only signed profiles in the protected approval directory.
   In an isolated compatible environment, verify for every source: normalized
   payload validation, approval source/recipe binding, staging, chunk hashes,
   commit, independent release and payload digests, and governed readback.
   Synthetic signing keys prove mechanics, never owner approval or deployment.
   Capture-only `rehearse` does not establish a signed release.
5. **Opt the PC in only after the operational gates and applicable approvals.**
   Preserve all existing private config fields and `publish` state. Add
   `"usgs-earthquakes"` to `sources` and, when explicitly set, to
   `storagePolicy.priority`. Keeping only two priority entries with three
   configured sources makes `tick()` fail `SOURCE_NOT_ALLOWED` before capture;
   `loadConfig()`/`plan` alone do not detect this cross-field mismatch. Keep
   the one-attempt/8 MiB default budget unless separately qualified: all three
   sources can publish over successive eligible ticks. New installs still
   default to two sources and `publish:false`. Verify three distinct committed
   releases, public readback, old-feed continuity and resource acceptance in the
   authorized environment before considering public earthquake activation.

Profile replacement does not rewrite an already saved transfer. A job's
`transfer_path` binds its immutable approval and recipe. Such a held job may
continue to fail after installing a renewed profile, with at most three
validation attempts; a new hourly job can read the new profile. Inspect local
status and remote heads, allow the next current slot, and preserve held products,
transfer receipts and journal history. Do not delete the journal, alter signed
manifests, reset retry counters or edit immutable transfers to force a retry.

`tests/pipeline-cutover.test.mjs` rehearses three independently identified signed
releases, old-profile rejection with historical-head preservation, the worker's
one-attempt budget, incomplete priorities, frozen transfers, installed-kit
recipe parity and migration preconditions. It uses synthetic keys, an in-memory
release store and injected acquisition/transport/storage guards. It does not
qualify actual MySQL execution, physical storage, backups, installed services,
owner signatures, real provider data or public publication.

The Landform relief dock then offers **Reviewed USGS earthquake snapshots**.

## Transfer, website and recovery

`POST /api/pipeline/v1/{heartbeat,stage,chunk,release,commit}` accepts signed,
bounded machine requests on the exact apex origin. Browser-origin calls are
rejected. Nonces persist in MySQL across restarts/replicas. Transfers use 256 KiB
immutable chunks and a maximum 8 MiB public product. Private originals have no
upload route. Staging and chunk verification precede SQL activation. A
transaction changes the active pointer and records its event together. Retries
look up the immutable release ID; stale publishers cannot replace a newer head.

`/curated` links from the map Source status panel. It shows source snapshots,
an orientation map, selectable records, provenance, honest empty/partial/stale
states and JSON downloads. Source geometry is preserved. It never labels
external context as evidence. `/api/pipeline-status` reports bounded worker and
release status, separately from `/api/source-pipeline/status`'s legacy archive.
`/api/curated/SOURCE?release=DIGEST` reads retained history only while approval
and release state permit it; `/api/curated/SOURCE/history` lists up to 20 such
releases. Approved domain packages feed the existing governed water/weather
map controls, selection, evidence and export paths through a new MySQL reader.

PC outage stops updates but leaves hosted snapshots available under their
approval limits. Withdrawal or expiry withholds data, rather than falling back
to private data or a different store. Pause the new timer and server control to
stop writes. Code rollback disables `KFM_PIPELINE_ENABLED`, preserving new tables,
files and receipts. D1/R2 and the original Sites application are never migrated.

## Optional GoDaddy FTPS mirror

The Node filesystem and cPanel FTP filesystem must not be assumed identical.
Qualify the actual account, TLS certificate, passive transfer, directory scope,
private staging, rename semantics, quota and HTTPS mapping first. Ordinary
unencrypted FTP and certificate bypass are unsupported.

`ftps-mirror CONFIG RELEASE_ID PUBLIC_PRODUCT` mirrors an already committed
public release only. It reads `pipeline-worker-key` and `ftps.json` from systemd
credentials, puts credentials in curl stdin rather than arguments/logs, uploads
to private staging, downloads and hashes the bytes, renames complete bytes into
the qualified public directory, then verifies public HTTPS delivery. It records
the mirror receipt. It never transfers raw originals or deploys application code.

The credential JSON uses format `kfm-qualified-ftps-v1`, `qualified:true`, DNS
`host`, `username`, `password`, distinct absolute `privateDirectory` and
`publicDirectory`, and an HTTPS `httpsBase` mapping. Keep it private; examples
must contain no real credentials. Missing/unqualified FTP does not block the
default HTTPS path. FTPS mirroring is an explicit operator command in this
version, rather than an automatically scheduled replacement transport.

## Verification limits

The implementation includes direct Node tests for curation, approval tampering,
replay, chunking, ambiguous commit recovery, SQLite restart/fencing, immutable
storage, streamed copying and encrypted-transfer behavior. A separate
`pipeline-mysql.test.mjs` requires an explicit disposable localhost MySQL fixture:
`KFM_PIPELINE_MYSQL_TEST=1`, optional `KFM_PIPELINE_MYSQL_PORT`; it never uses DB_*
or the production database. Existing domain gates retain their regression tests.

Physical disk qualification, independent backup/restore, actual MySQL execution,
FTP credentials, hosted durability and production activation require real-host
evidence. Source/build/unit success cannot stand in for those steps.

## Storage priorities and publication budget (2026-10-23)

The second PC remains the capture/processing authority: original objects, full
history, private receipts and the local SQLite journal stay there. GoDaddy MySQL
stores approved projections and release metadata for public reads. This is
one-way application publication, not SQL replication; no remote database port,
shared SQLite file or raw-archive upload is introduced.

The automatic worker defaults to NWS context first, USGS streamflow second,
one release attempt per tick and 8 MiB of normalized payload. Each source still
has its existing hourly capture slot. The lower-priority candidate is captured
and saved even when publication is deferred. A subsequent eligible tick can
publish it without repeating acquisition. Reviewed water/weather packages keep
the separate manual `stage-package` workflow; its transfers are **not** governed
by this automatic-worker budget. Additional pipeline adapters are not implied.

Optional configuration (merge into the existing private config; preserve all
other properties and do not turn on `publish` merely to edit priorities):

```json
"storagePolicy": {
  "priority": ["nws-alerts", "usgs-streamflow"],
  "maxPublicationsPerTick": 1,
  "maxBytesPerTick": 8388608
}
```

Priority must name each source once: the two original sources, optionally
with `usgs-earthquakes` as a third. Attempts may be 1–3; byte budget may
be 256 KiB–16 MiB. The existing per-product ceiling stays 8 MiB. Failed attempts
also consume the run's budget. A product larger than the chosen budget remains
private and deferred; increase the budget within bounds or prepare a smaller
approved product. Counts exclude HTTP/base64 overhead and are **not** MySQL
capacity measurements. Existing 1 GiB/10,000 release admission caps still apply;
index, log, backup and provider quota headroom must be measured before activation.

A failed heartbeat no longer stops collection. After an unavailable/busy host,
the worker holds further publication for that run and retries eligible candidates
on later ticks with a five-minute minimum delay. Such deferrals do not consume
validation retries. Signature, approval, integrity and source errors still hold
the affected job under the existing retry limit. Publication has a two-minute
aggregate timeout in addition to each call's 30-second timeout. Signed release
identity and readback remain mandatory after ambiguous delivery.

The scheduler intentionally considers the **current hourly slot**. Older
candidates remain private and are not automatically replayed after an extended
outage: replaying all history could overload hosting or replace current context
with stale data. No raw objects or releases are deleted by this change. An
explicit reviewed historical release workflow remains future work.

`node scripts/pc-pipeline/cli.mjs plan CONFIG` validates and explains placement
and budgets without network calls or storage writes. `status CONFIG` verifies
local storage and returns a timestamped snapshot of the latest 100 journal rows,
including deferred reasons/retry times, plus the plan. Local status does not
prove remote availability, hosting capacity, or deployment success. The public
Acquisition page offers an accessible configuration planner; its controls only
prepare text for the operator's private configuration, never mutate a server.

Activation still requires verified host transport, actual MySQL quota/grants,
qualified PC and hosted storage, independent backup/restore evidence, current
signed release approval and a verified deployed revision. Existing enabled flags
are unchanged. No production migration or live load test was run for this change.
Roll back by restoring the previous code and removing the optional storagePolicy
property. Existing journal rows remain compatible; do not delete the journal or
releases. Pause publication before rollback if needed using the signed control.

Technical references: [SQLite WAL](https://www.sqlite.org/wal.html) describes its
single-writer and local-filesystem constraints; [MySQL connection limits](https://dev.mysql.com/doc/refman/8.0/en/too-many-connections.html)
explain why client concurrency must fit measured server limits. The existing
three-connection/eight-waiter hosting pool is unchanged; no unsupported claim of
visitor capacity or database latency improvement is made.

## Installation and failure-classification checks (2026-10-23)

The installed kit includes `storage-policy.mjs`, which both its worker and CLI
load. `tests/pipeline-install.test.mjs` copies the same kit as the installer into
an isolated tree and runs its planner and worker import without access to the
checkout's modules. Run this before root installation:

```sh
node --test tests/pipeline-install.test.mjs tests/pc-pipeline.test.mjs tests/storage-policy.test.mjs
node scripts/pc-pipeline/install.mjs
```

The second command remains review-only. These source tests neither qualify a
real mount nor install services. The systemd units use `/usr/bin/node`; verify
that exact executable is Node 22.13+ on the development PC before installation.

Publication transport failures have explicit remote error codes. A malformed,
empty or mismatched worker key is held under the bounded validation retry policy,
while capture bytes stay private. A missing local approval file is also held;
it does not mark healthy hosting unavailable or block another eligible source
when the run's budget permits it. Transient network failures and busy hosting
remain deferred without consuming validation retries. Error output contains
bounded codes, never arbitrary transport errors or credential contents.

Synthetic checks cover the payload budget, the 8 MiB product ceiling, deferred
candidate reuse, lost commit responses, replay denial and installed-tree loading.
They use injected acquisition/transport and do not establish real MySQL
transactions, provider capacity, PC storage/restore, or a live release approval.
Keep `publish:false`, both timers disabled, and hosting publication disabled
until the infrastructure and approval qualifications above are independently
recorded. Preview and Published sharing a database does not qualify its TLS,
backup or restore. Read-only connection success through a provider-private
network does not satisfy the publishing store's verified-TLS requirement.
