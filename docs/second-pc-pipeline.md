# Second-PC acquisition, curation and GoDaddy publication

Runbook for the KFM source pipeline on the `dev` PC. Read **Current state**
first. The later sections describe the gated path to a system install and
publication; none of those gates has been passed yet.

Implementation candidate, 2026-10-22. The public application remains app
`urdng3v1vk`. This kit does not change the preserved Sites application, its
bindings, the installed inference services, DNS, or existing archive tables.

## Current state

Read back on 2026-10-30 from `systemctl --user`, the unit files and the active
config. Re-verify before relying on it. Relative paths in this section are
under `/home/dev/Documents/ChatGPT/Kansas-Frontier-Matrix/`.

| Item | State |
| --- | --- |
| Pipeline host | `dev` PC. `devil` is a test PC with no production role. |
| Deployment | User-level systemd units that run `pc-pipeline-data/runtime/run.sh`. The system install (`install.mjs`, `/opt/kfm-pipeline`, `/srv/kfm-data`, `kfm-pipeline.timer`) has **not** been applied. |
| Publication | `publish: false` and `remoteMode: "connection-only"`. Nothing is uploaded. |
| Normal tick output | The first tick in each hour records `candidate-only` for each source; later ticks in that hour report `already-complete-or-held`. |
| Data store | `KFM-pipeline/` on the 1.4 TiB HDD at `/run/media/dev/f975f1e2-a926-4040-8bc5-cbea4335d8bf` |
| Working backup | `KFM-pipeline-backup/` on the 180 GB SSD at `/run/media/dev/55568f6e-e770-4dcd-9c96-2060157e850e` |
| Active config | `pc-pipeline-data/transfer-access/local-pipeline-config.json` (backup: `pc-pipeline-data/backup-config.json`) |
| Kernel lock | `pc-pipeline-data/run/pipeline.lock`, shared by capture, analysis, backup and restore |

### Deployed code: pinned releases

Capture, backup and restore run a commit-named copy of the kit, not a Git
working tree:

- `kfm-source-pipeline` runs `capture.mjs`, and `kfm-working-backup` and
  `kfm-working-restore` run `cli.mjs` through `runtime/backup.sh`, from one
  directory under `pc-pipeline-data/runtime/releases/` named by its source
  commit. `run.sh` names that directory as `hosted=`, `backup.sh` names its
  `cli.mjs` as `cli=`, and the `pipelines` case of the `kfm-data` helper names
  its `health.mjs`. Each `release.json` records the source commit and the
  SHA-256 of every kit file.
- `kfm-intake-analyze`, `kfm-intake` and `kfm-library` still run
  `tools/local_data/intake.py` and `tools/local_data/intake_service.py` from the
  `pipeline-implementation` checkout. An edit, `git switch`, `git stash`, rebase
  or pull there changes those services at their next run or restart.

Editing a kit checkout does not change the running pipeline. To deploy a kit
change:

1. Commit it and run the [local checks](#verify-a-change-locally).
2. [Pause the timers](#pause-and-resume) and wait for the lock as in
   [Run a CLI command by hand](#run-a-cli-command-by-hand).
3. From a clean checkout at that commit, build the release:
   `node scripts/pc-pipeline/release.mjs /home/dev/Documents/ChatGPT/Kansas-Frontier-Matrix/pc-pipeline-data/runtime/releases`.
   It refuses a modified or untracked kit file and an existing release.
4. Point `run.sh`, `backup.sh` and `kfm-data` at the new directory, run
   `verify-backup` on the latest manifest and one capture by hand under the
   lock, then resume the timers.

Keep earlier release directories. A rollback points the three scripts back at
the previous commit; captures, backups and journal rows are never rewritten.

Until October 30 the backup and restore units ran `cli.mjs` from the
`pipeline-hosted` working tree. Its backup format v2 and connection-only
refusals existed only as uncommitted changes there. That state is preserved as
commit `7f337349c7` on that checkout's runbook branch, and this branch now
carries both.

### Active units

| Unit | Schedule (America/Chicago) | `run.sh` task | What it runs |
| --- | --- | --- | --- |
| `kfm-source-pipeline.timer` | every 5 minutes | `capture` | The live `capture.mjs` wrapper: one tick, then the health report. Takes the lock without waiting; exit 75 (busy) counts as success. |
| `kfm-intake-analyze.timer` | hourly at :10 | `analyze` | `intake.py analyze` on `KFM-pipeline`. Waits up to 600 s for the lock. |
| `kfm-working-backup.timer` | daily 02:30 | `backup` | `cli.mjs backup`, then `cli.mjs verify-backup`. |
| `kfm-working-restore.timer` | 1st of the month, 03:30 | `restore` | `cli.mjs restore-test` into a new `KFM-restore-tests/<UTC time>/` on the SSD. |
| `kfm-intake.service` | always on | `intake` | Working desk on 127.0.0.1:8772. |
| `kfm-library.service` | always on | `library` | Catalog-only library on 127.0.0.1:8771. |

Timers are `Persistent=true` with up to 20 s of randomized delay. Every task
first runs `runtime/mounts.sh`, which mounts the drives by UUID and refuses a
path mismatch. Backup and restore wait up to 900 s for the lock, stop
`kfm-intake.service` so its SQLite writers close, and restart it on exit.

## Operate the active deployment

Run these as `dev`. `kfm-data` is on `PATH` through `~/.local/bin/kfm-data`,
a link to `/home/dev/Documents/ChatGPT/Kansas-Frontier-Matrix/kfm-data`.

### Check health

```sh
kfm-data status
journalctl --user -u kfm-source-pipeline.service -n 20 -o cat
cat ~/Documents/ChatGPT/Kansas-Frontier-Matrix/pc-pipeline-data/run/backup-last.json
cat ~/Documents/ChatGPT/Kansas-Frontier-Matrix/pc-pipeline-data/run/restore-last.json
```

A healthy tick logs one `kfm-pc-pipeline-tick-v1` JSON line whose outcomes are
`candidate-only` or `already-complete-or-held`. Node 22 also logs an SQLite
`ExperimentalWarning` on every run; that is expected. A failed tick logs
`{"reason":"CODE","state":"held"}` and the unit result becomes `exit-code`.
`backup-last.json` holds the latest backup result; `restore-last.json` holds
the latest restore receipt (`state: "verified"`).

### `kfm-data` commands

| Command | Effect |
| --- | --- |
| `kfm-data status` | Unit states, last results and next timer runs. |
| `kfm-data pipelines` | Prints the private capture, retry, storage and backup health report. |
| `kfm-data refresh` | Starts one capture and one analysis now. |
| `kfm-data backup` | Starts one working-store backup now. |
| `kfm-data library`, `kfm-data intake` | Print the current private connection link. Do not share it. |
| `kfm-data open library`, `kfm-data open intake` | Start that service and open its link. App-menu entries: **KFM Data Library**, **KFM Working Data**. |
| `kfm-data connection` | One on-demand HTTPS connection check; saves a local receipt. |
| `kfm-data ftp-connect`, `kfm-data ftp-status` | Run `pc-pipeline-data/setup-ftps-connection.py` to set up or check the FTPS connection profile. |
| `kfm-data files` | Prints the preserved import path. |

Reopen the working desk link after any restart of `kfm-intake.service`,
including the automatic restart after backup and restore. This host helper is
unrelated to the repository's `npm run kfm-data -- COMMAND`, which is an alias
for `node scripts/pc-pipeline/cli.mjs COMMAND`.

### Pause and resume

```sh
systemctl --user stop kfm-source-pipeline.timer kfm-intake-analyze.timer \
  kfm-working-backup.timer kfm-working-restore.timer
systemctl --user list-timers 'kfm-*' --no-pager   # lists nothing once paused
```

Resume with `systemctl --user start` and the same four timers. Stopping a timer
does not interrupt a run already in progress; to wait for one, take the lock as
shown below. The timers are `Persistent=true`, so a schedule missed while paused
runs once as soon as its timer starts again. For example, a backup starts
immediately if 02:30 passed during the pause. `kfm-intake.service` and
`kfm-library.service` keep running; stop them separately if their code is
changing.

### Run a CLI command by hand

Manual commands must hold the same lock as the scheduled units, or a backup can
race a capture. Mount the drives first, as `run.sh` does, and use the deployed
release rather than a checkout:

```sh
cd ~/Documents/ChatGPT/Kansas-Frontier-Matrix/pc-pipeline-data
runtime/mounts.sh all
kit="$(sed -n 's/^hosted=//p' runtime/run.sh)"
flock --exclusive --wait 900 run/pipeline.lock \
  node "$kit/scripts/pc-pipeline/cli.mjs" status transfer-access/local-pipeline-config.json
```

### Troubleshoot a held run

Failures surface at two levels:

- **Whole tick or command.** Config and storage checks run before the tick and
  again before each source; the memory check runs only before a source whose
  slot still needs work, so a tick with nothing to do never needs it. A failure
  prints `{"reason":"CODE","state":"held"}`, exits 1 and fails the unit. The
  source that was about to run is not claimed and keeps its attempts.
- **One source.** An acquisition, normalization or validation failure is
  recorded on that source's journal row as `held` with its reason. The tick
  still exits 0 and reports `{"reason":"CODE","sourceId":"…","state":"held"}`.
- **Deferred publication.** With `publish: true` only, a source whose capture is
  saved but cannot publish this tick reports `state: "deferred"` with
  `HOSTING_UNAVAILABLE` or `PUBLICATION_BUDGET`. That is not a failure.

See [Job journal](#job-journal) for retries and deferrals.

Reasons are fixed codes; unexpected errors print `PIPELINE_OPERATION_FAILED`
and deliberately omit details. Common codes:

| Reason | Meaning | Action |
| --- | --- | --- |
| `STORAGE_IDENTITY_CHANGED` | The mount is missing or is not the device recorded in the config, or `.kfm-pipeline-store` does not match `storeId`. | Run `runtime/mounts.sh all` and check `findmnt`. A replaced drive needs deliberate requalification, never a config edit. |
| `DISK_RESERVE_REQUIRED` | The data disk would drop below 20% free after the job's reserve, or the system disk has under 30 GiB free. | Free space. Nothing is deleted automatically. |
| `MEMORY_RESERVE_REQUIRED` | Under 3 GiB of free RAM when a source's slot still needs work, usually from inference or desktop load. The tick stops before claiming. | None; the next tick retries. An hour that stays below the reserve throughout is lost, because missed hours are not back-filled. Repeated holds mean the host is overcommitted. |
| `DURABLE_FILESYSTEM_REQUIRED` | The store is on tmpfs, overlay or another filesystem outside the allowlist. | Use the qualified disk. |
| `DEDICATED_DATA_MOUNT_REQUIRED` | The root is not strictly inside the mount, or the mount is not a separate device. | Fix the mount or config. |
| `CONFIG_INVALID` | The config fails validation (format, 32-hex `storeId`, up to three known sources, `publish`, `device`, `approvalDirectory`). | Compare with the active config. Do not hand-edit `storeId` or `device`. |
| `STORAGE_POLICY_INVALID` | `storagePolicy` has an unknown key, a priority list that is not 2–3 distinct known sources, or attempts or bytes out of range. | Fix the policy; see [Storage priorities and publication budget](#storage-priorities-and-publication-budget-2026-10-23). |
| `SOURCE_NOT_ALLOWED` | A configured source is missing from the priority list, or a command was given an unknown source. | Name every configured source in `storagePolicy.priority`, or remove the policy to use the defaults. |
| `CONNECTION_ONLY_UPLOADS_DISABLED` | A `publish: true` tick met `remoteMode: "connection-only"`, or `stage-package`, `ftps-mirror` or `publish-county` ran under connection-only mode or `publish: false`. | None while the connection-only scope applies. |
| `INDEPENDENT_BACKUP_REQUIRED` | The backup root is on the same device as the store. | Point the backup config at the separate SSD. |
| `BACKUP_INPUT_CHANGED` | A source file changed while it was being copied. | A writer ran outside the lock. Check that manual commands hold it, then rerun. |
| `BACKUP_CONFLICT`, `IMMUTABLE_CONFLICT` | An existing content-addressed file holds different bytes than expected. | Investigate. Never delete or overwrite the existing file. |
| `BACKUP_INTEGRITY_FAILED` | Copied or stored bytes do not match the manifest hash. | Treat that backup as suspect, keep the originals, run `verify-backup`. |
| `RESTORE_TARGET_MUST_BE_EMPTY` | The restore directory is not empty. | Use a new, empty mode-0700 directory. |
| `LEASE_LOST` | The job's 10-minute lease expired or another run claimed it. | Look for overlapping runs. The lock should prevent them. |
| `PIPELINE_OPERATION_FAILED` | An unclassified error, such as a network or provider failure. | Rerun by hand under the lock and read `journalctl`. |

## Owner decisions and history

These dated records hold the owner's decisions and the migration history. They
constrain every procedure in this runbook.

### Owner correction, October 22

This `dev` PC is the active KFM pipeline host.
`devil` is a separate test PC and must have no production dependency or role:
no production storage, backup target, signing authority, scheduler, publishing,
or credentials. Network discovery made no changes to that machine. Use a
separate physical disk on the active PC for the initial backup qualification;
do not configure a share or service on `devil`.

### One-time import from `devil`, October 22

The owner subsequently authorized a one-time import of meaningful existing
holdings from `devil`'s home/projects/KFM data folder. This is a migration source,
not a runtime dependency. Confirm the exact account/path, inventory sizes and
hashes before transfer, preserve the original tree and source copies, and verify
all destination hashes. Do not delete or reorganize the remote originals.
Keep the receiving copy private and outside all Git/public trees. After transfer,
reuse `tools/local_data/intake.py` from the main repository to profile formats,
geography, dates, domains, provenance and review holds. Preserve the exact imported
tree as the migration snapshot; organize catalog entries and review copies rather
than renaming the only copy. Reference documents, code/recovery material and actual
provider data need distinct destinations based on their contents. Imported bytes
are not automatically approved for MySQL, FTP, publication or factual evidence.
Any temporary transfer access must not become a production service dependency.

The confirmed migration source is
`bartytime@devil:/home/bartytime/Projects/KFM-data/data/` (LAN address observed
as `192.168.86.22`). Read-only discovery found 252,588,531,712 allocated bytes
and 2,756,465 regular files. The existing intake index contains 2,711,226
present records, all held for review; its historical SHA-256 values are not a
fresh destination verification. These counts describe different inventories.
The 1.4 TiB drive was mounted without formatting through the desktop storage
service at `/run/media/dev/f975f1e2-a926-4040-8bc5-cbea4335d8bf`.
The preserved incoming collection is `kfm-imports/devil-20261022/data/` beneath
that mount; new operational work uses the separate `KFM-pipeline/` store.
Copy and a full rsync checksum comparison precede the final local catalog and
receipt. Their existence must be checked before reporting migration complete.
The session-managed mount is not a production boot mount. No unattended timer,
publication, or independent backup qualification follows from this copy.

### Active local setup, October 23

The owner applied and readback verified UUID-based `/etc/fstab` entries for the
large data drive and the separate 180 GB backup SSD. Both keep `nosuid,nodev,noexec`
and use systemd automounts at their existing `/run/media/dev/<UUID>` paths.
The `dev` user manager has lingering enabled. No inference units were changed.

Private stores below the data mount are:

- `kfm-imports/devil-20261022`: verified preserved collection, about 244 GB of
  logical file bytes. Imported data is not automatically admitted or published.
- `KFM-pipeline`: new bounded USGS/NWS captures, originals, products, receipts,
  the operational intake index and SQLite job journal. `publish` remains false.

`KFM-library` lives on the separate SSD beside the working-backup store, keeping
metadata queries off the older HDD. It is a searchable working copy of the
existing intake index. Its catalog-only service uses SQLite immutable/query-only
reads and disables all mutations. Local-file locators point back to the preserved
import on the HDD. Three exact-hash-pinned water/map review packages are attached
for bounded private inspection; their original pending-review states remain.

The active user units are `kfm-source-pipeline.timer` (checks every five minutes,
hourly source slots), `kfm-intake-analyze.timer` (hourly at minute 10),
`kfm-working-backup.timer` (02:30 America/Chicago) and
`kfm-working-restore.timer` (first of each month, 03:30 America/Chicago).
`kfm-intake.service` serves the working desk at loopback port 8772;
`kfm-library.service` serves the imported catalog at port 8771 after its search
index is ready. Both require the owner's private connection capability.

The `kfm-data` helper installed alongside these units is described in
[Operate the active deployment](#operate-the-active-deployment).

The SSD backup covers the new `KFM-pipeline` working store, not the full imported
archive or library metadata copy. Originals on the test PC are preserved as the
one-time migration source; there is no scheduled access to that PC. A full-size
independent archive backup is still outstanding. Do not delete the source copies.
Initial and repeated working-store backups, hash checks and actual restores passed.
Capture, analysis and backup operations share a kernel lock; the working desk is
paused during backup to close its SQLite writers, then restarted automatically.

Backup format v2 uses SHA-256 object storage so successive versions of mutable
working files can coexist. Verification/restoration still read format v1. Journal
snapshots and their receipts now use stable digest-based identities, preventing
repeat-backup collisions. No previous backup or archive object was overwritten.
Format v2 ran only from an uncommitted checkout until October 30; see
[Deployed code: pinned releases](#deployed-code-pinned-releases).

### Connection-only owner scope, October 23

The owner explicitly prohibited moving the bulk collection to GoDaddy or adding
costs. The active PC config now has `remoteMode: "connection-only"` as well as
`publish:false`. The local scheduler rejects an inconsistent enabled-publishing
config before any storage or network access. Package publication and FTPS mirror
commands reject connection-only or disabled-publishing configs before reading
payloads or credentials. No import, migration or FTP transfer is enabled.
The later `publish-county` command refuses the same way.

`kfm-data connection` performs one small on-demand HTTPS connection check and
saves a local receipt; it never reads a dataset or sends an upload body. The
hosted candidate runs exactly `SELECT 1` using the provider-injected DB settings,
shares concurrent checks, caches results for 60 seconds, and exposes no database
credentials or data. No recurring remote poller or new paid resource is created.
The original bulk collection, library metadata, captures and backups remain on
the active PC. The hosted check requires deployment and actual acceptance before
connectivity can be reported. Its reviewed source is PR #5438, commit
`6da1e5cf2642eb07768842bce791832fba821d95`.

## Implemented path and authority

`scripts/pc-pipeline/worker.mjs` checks a qualified data filesystem, claims
durable SQLite jobs, acquires the existing bounded Kansas USGS/NWS feeds (plus
`usgs-earthquakes` when configured; see its section below),
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

The unattended worker holds a dedicated HMAC transfer credential. An owner-controlled
signing environment, isolated from the worker, holds the Ed25519 approval private
key; GoDaddy holds its public key only. The test PC is not that environment.
Delegations bind source, role, recipe digest, rights/sensitivity review references,
maximum payload/rows, freshness, and at most 30 days. Changed recipes or expired,
revoked, or altered approvals are denied. This transport projection does not
replace the monorepo's source/evidence/release authorities.

## CLI reference and rehearsal

Use Node 22.13+; SQLite uses Node's built-in experimental `node:sqlite` module.
No new npm runtime dependency is required for the PC kit.

`node scripts/pc-pipeline/cli.mjs COMMAND ARGS` prints one canonical JSON
result on stdout. On failure it prints `{"reason":"CODE","state":"held"}` on
stderr and exits 1; see [Troubleshoot a held run](#troubleshoot-a-held-run).

| Command | Arguments | Effect | Under the current scope |
| --- | --- | --- | --- |
| `inventory` | none | Reports Node version, system-disk free bytes and recipe digest. Writes nothing. | Safe |
| `plan` | `CONFIG` | Validates the config and explains source priority and publication budget. No network or writes. | Safe |
| `status` | `CONFIG` | Verifies storage, then prints the plan and the latest 100 job rows. | Safe; hold the lock |
| `tick` | `CONFIG` | One scheduled capture pass, the same as `worker.mjs CONFIG`. | Scheduled; use `kfm-data refresh` |
| `rehearse` | `PRIVATE_ROOT` | Captures all three feeds into a mode-0700 directory outside the checkout. | Safe; needs 30 GiB + 64 MiB free there |
| `init` | `ROOT MOUNT CONFIG_OUTPUT` | Writes a store marker and a two-source, `publish: false` config for a new store on a dedicated mount. | New stores only |
| `backup` | `CONFIG BACKUP_CONFIG` | Journal snapshot, then a verified v2 copy of every file under `data/`. Its result includes `manifestSha256` and `completedAt`. | Scheduled; use `kfm-data backup` |
| `verify-backup` | `MANIFEST BACKUP_ROOT` | Re-hashes every object a v1 or v2 backup manifest lists. Writes nothing. | Safe |
| `restore-test` | `MANIFEST BACKUP_ROOT EMPTY_RESTORE_ROOT` | Restores a v1 or v2 backup into an empty private directory and writes a restore receipt. | Monthly timer, or by hand |
| `connection` | `[ROOT]` | One read-only hosted connection check; writes a receipt under `ROOT` (default `~/.local/state/kfm-data`). Exits 1 unless connected. | Safe |
| `county-history` | `REPORT SHA256` | Reads a county history report pinned by its SHA-256. Exits 2 if its geometry is quarantined. | Safe |
| `prepare-county` | `REPORT SHA256` | Prints the normalized `candidate-only` county product. No writes. | Safe |
| `publish-county` | `CONFIG REPORT SHA256` | Publishes an approved county release. | Rejected with `CONNECTION_ONLY_UPLOADS_DISABLED`; see [Historical county context](#historical-county-context-implementation-candidate-2026-10-29) |
| `profile-template` | `SOURCE` | Prints an unapproved delegation draft for a stream, alert, earthquake, county, water or weather source. | Safe |
| `keys` | `PRIVATE_DIRECTORY` | Creates the owner Ed25519 key pair. | Owner signing environment only; not provisioned |
| `approve` | `PROFILE PRIVATE_KEY SIGNED_OUTPUT` | Signs a delegation. | Owner signing environment only |
| `control` | `COMMAND_JSON PRIVATE_KEY` | Sends a signed pause, resume, withdrawal or rollback command to the site. | Owner only; needs the deployed pipeline API |
| `stage-package` | `CONFIG water\|weather SNAPSHOT DECISION` | Publishes a governed water or weather package. | Rejected with `CONNECTION_ONLY_UPLOADS_DISABLED` |
| `ftps-mirror` | `CONFIG RELEASE_ID PUBLIC_PRODUCT` | Mirrors a committed release over FTPS. | Rejected with `CONNECTION_ONLY_UPLOADS_DISABLED` |

Other entry points:

```sh
node scripts/pc-pipeline/cli.mjs rehearse /absolute/private/pilot-store
node scripts/pc-pipeline/release.mjs /absolute/releases   # pinned kit copy from a clean checkout
node scripts/pc-pipeline/install.mjs   # review-only report unless --apply
node scripts/migrate-pipeline.mjs      # prints SQL and digest unless --apply
node --test tests/pc-pipeline.test.mjs
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

## Store layout, job journal and backup format

### Store layout

Every write is content-addressed and immutable: a file is written to a
temporary name, synced and hard-linked into place. An existing file with
different bytes is a conflict, never an overwrite.

```text
KFM-pipeline/                                    config "root"
  .kfm-pipeline-store                            store marker, equal to storeId
  pipeline-journal.sqlite                        job journal (WAL)
  data/
    quarantine/SOURCE/objects/sha256/DIGEST/payload   exact provider bytes
    processed/SOURCE/DIGEST.json                      normalized product
    receipts/ingest/pc-pipeline/DIGEST.json           acquisition receipt
    receipts/pipeline/configs/DIGEST.json             config copy taken by each backup
    receipts/pipeline/journal-snapshots/DIGEST.sqlite journal snapshot (VACUUM INTO)
    receipts/pipeline/journal-backups-v2/DIGEST.json  snapshot receipt naming that file
    receipts/pipeline/{transfers,published,ftps}/     publication receipts; unused while publish is false
```

The same `data/` tree also holds the `tools/local_data` lifecycle store
(`catalog/`, `raw/`, `work/`, `registry/` and others) that `intake.py analyze`
maintains, so backups include its working index. Older backups named snapshots
by a random ID and left their receipts in `receipts/pipeline/journal-backups/`;
both directories remain on the live store.

### Job journal

`pipeline-journal.sqlite` has one row per source per hourly slot. A tick
claims a row only when it is not complete, not leased, not waiting for a retry
and has fewer than three attempts. A claim leases the row for 10 minutes, so a
crashed run is retried after the lease expires. A failed attempt becomes `held`
with its reason and is retried after 5 minutes, then 10 minutes; after the
third failure the slot stays held. The next hourly slot starts fresh, and
missed hours are never back-filled. A retry reuses an already-saved product
rather than acquiring again.

With `publish: true`, a deferral (`HOSTING_UNAVAILABLE` or
`PUBLICATION_BUDGET`) returns the row to `pending` for at least 5 minutes and
gives back the attempt it used, so outages and budget limits never exhaust
the three tries. A row whose product was saved but never released is claimed
again while publishing is on, even if it was marked complete.

### Backup format

```text
KFM-pipeline-backup/
  objects/sha256/DIGEST/payload           format v2: one object per distinct content
  data/PATH                               format v1: path-named copies, read-only legacy
  backup-manifests/DIGEST.json            one manifest per backup run
```

A manifest lists every file as `{path, sha256, bytes}` together with
`storeId`, `sourceDevice`, `backupDevice` and `inventorySha256`, the SHA-256 of
the canonical file list. `backup` writes format `kfm-pc-data-backup-v2`: objects
are stored by content, so successive versions of a mutable file such as the
intake index coexist, and the manifest is named by the SHA-256 of the canonical
`{format, files}`, returned as `manifestSha256`. Format v1 manifests are named
by `inventorySha256`; their path-named copies refuse changed bytes
(`BACKUP_CONFLICT`), which is why v1 is no longer written. `verify-backup` and
`restore-test` read both formats and reject a duplicate, absolute or `..` path.

`backup-last.json` carries the backup's `completedAt`, which the health report
uses as its age; receipts written before October 30 lack it, so the report
falls back to the file's modification time and shows `receiptTime: null`.

## Verify a change locally

Kit changes reach the units only through a new release (see
[Deployed code: pinned releases](#deployed-code-pinned-releases)); intake and
library changes in `pipeline-implementation` still need the timers paused. For a
pipeline-only change, the fast check is:

```sh
node --test tests/pc-pipeline.test.mjs tests/pipeline-*.test.mjs tests/storage-policy.test.mjs
```

Before pushing, run the local mirror of the CI workflow
`.github/workflows/public-core-repair.yml`. That workflow runs on every pull
request and on pushes to `a0-hosted-ai-web-20261017` and
`codex/fix-public-core-visibility-20261014`. From the checkout being changed:

```sh
bash scripts/ci-local.sh
```

`scripts/ci-local.sh` runs the `verify-core-delivery` job's steps in order:
`npm ci`, build, typecheck, the Node suite, the MySQL checks when a disposable
server listens on 127.0.0.1:13317, the fire-renderer browser comparison, the
HTTP boundary and browser suites on port 5182, and the preview on port 5183.
It then runs the separate `welcome-performance` job against the same build.
Unlike CI it continues after a failure, so one run reports every broken step,
and it stops the servers it starts. It prints a summary and keeps per-step
logs, screenshots and measurements in `.sites-runtime/ci-local/<UTC time>/`, or
in the directory given as its argument. If `npm` is not on `PATH`, it uses the
pinned copy in `../development-tools/bin`. Exit status 0 means every step that
ran passed; 69 means a required tool is missing; 75 means another run holds
`.sites-runtime/ci-local.lock` or port 5182 or 5183 is taken. When the workflow
changes, update the script to match.

The browser suites drive headless `google-chrome`; set `KFM_TEST_CHROME` to
use another binary.

`tests/second-pc-pipeline-doc.test.mjs` runs in the Node suite, locally and in
CI. It fails if this runbook skips a heading level, links to a missing section,
or cites a `scripts/`, `server/`, `tests/`, `docs/` or `.github/` path that no
longer exists. On the pipeline PC it also checks the cited `tools/` and
`pc-pipeline-data/` paths. Update the runbook in the same change that moves or
renames a file it cites.

Results on this PC, 2026-10-29 (Node 22.22.1; CI pins 22.23.3):

| Workflow step | Local result | Time |
| --- | --- | --- |
| `npm ci`, build, typecheck | Pass | about 2 min |
| Node suite, `tests/*.test.mjs` | Pass: 2,282 tests, 0 failed, 22 skipped | about 3 min |
| Disposable MySQL checks | **Not run**: no Docker or MySQL on this PC | none |
| Fire renderer comparison | Pass | about 75 s |
| HTTP boundary and browser suites | Pass | about 13 min |
| Preview on port 5183 | Pass | about 30 s |
| `welcome-performance` job | Pass | about 2 min |

CI provides the MySQL check through a `mysql:8.4.13` service container on
127.0.0.1:13317. Without `KFM_PIPELINE_MYSQL_TEST=1` and `KFM_MYSQL_TEST=1`,
`tests/pipeline-mysql.test.mjs` and `tests/hosted-ingestion-mysql.test.mjs`
skip, so a local pass does not cover them; rely on the pull request run.

Running this suite does not disturb the live units. `npm ci` replaces
`node_modules`, but the pipeline imports only Node built-ins and repository
modules. Ports 5182 and 5183 do not collide with the desk (8772) or the
library (8771).

## Qualify storage and backup before installing

This section and the next describe the **system install** under `/srv/kfm-data`
and `/opt/kfm-pipeline`. It has not been applied; the running deployment is
described in [Current state](#current-state).

The October 22 host readback found about 143 GiB free on the system disk and
several unmounted ext4 drives, including an approximately 1.4 TiB HDD. Their
contents and health were **not verified**: raw-filesystem inspection required
sudo authentication unavailable to this session. Do not format them.

1. Inspect existing disk contents and SMART health. Select a healthy drive with
   measured free space; mount it by UUID at `/srv/kfm-data`.
2. Preserve existing originals at their current locations. Inventory and hash
   holdings before any copy; use the existing monorepo local-store tools for
   governed captures. Do not introduce a dependency on the test PC.
3. Prepare a private store below that mount, for example `/srv/kfm-data/store`.
   Initialize with `cli.mjs init ROOT MOUNT CONFIG_OUTPUT`. The command records
   filesystem device identity and a random store marker; it refuses an unmounted
   directory on the root filesystem.
   Run the bounded `rehearse` against this store before its first backup so the
   restore exercise includes captured payloads, not only configuration records.
4. Qualify a separate physical backup disk on the active PC, mounted at
   `/srv/kfm-backup`. Initialize a separate backup root/config the same way.
   Source and backup must be different devices. A second directory is insufficient.
   Limit retained source data to what that backup disk can hold with the required
   reserves. This local copy does not protect against loss of the whole PC.
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
as unrelated live files. Approval private keys require a separate owner-controlled
backup, inaccessible to the worker. No credentials are added to data inventories.

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

In the owner-controlled signing environment, `cli.mjs keys PRIVATE_DIRECTORY`
creates the owner key pair. The CLI's older original-PC hint does not designate
`devil`; that machine remains test-only.
Create a review draft with `profile-template SOURCE`; review the exact source,
role, recipe digest and policy references, fill the deliberately unapproved
fields, then `approve PROFILE PRIVATE_KEY SIGNED_OUTPUT`. Copy only the public
key to GoDaddy and the signed delegation to the PC's root-owned approval
directory. Files need group-read access for `kfm-pipeline`, not worker write access.
The worker must never have access to the private key. Qualify that isolation
before creating or installing keys; no signing key has been provisioned yet.

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
   default to two sources and `publish:false`. When the existing config has
   `publish:true`, adding earthquakes is itself publication activation: obtain
   explicit activation authority before applying it. Qualify all three signed
   releases in an isolated environment without public exposure first. After
   the authorized cutover, verify three distinct committed releases, public
   readback, old-feed continuity and resource acceptance.

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

## Historical county context (implementation candidate, 2026-10-29)

The [county publication path](county-history-publication.md) adds manual `prepare-county` / `publish-county` commands and an approved-context map consumer. It changes the shared signed recipe and adds one source-head row. Follow that cutover procedure before deployment: regenerate and review replacement delegations for every configured source, preserve existing transfers/heads/settings, verify backup and migration on a disposable copy, and use the existing owner signing process. County history is not added to the hourly acquisition schedule. No operational approval, migration or activation is performed by the code change.
## Card coverage and private pipeline health — October 29

The additive card registry maps the current 22 welcome topics and six recipes. `/pipelines` and `GET /api/pipeline/v1/cards` expose public-safe
coverage metadata and check existing release gates; they do not expose the
local journal or intake inventory. See [card pipeline operations](explorer-card-pipelines.md)
and [the generated dependency map](explorer-card-pipeline-map.md).

The active user capture wrapper now invokes `scripts/pc-pipeline/capture.mjs`
under the same kernel lock. After the existing tick it writes an atomic private
`data/work/pipeline-health.json` report. **KFM Working Data** shows its capture,
retry, storage and working-backup/restore status. Reopen its current connection
link after the service restart. The imported **KFM Data Library** remains
catalog-only and does not expose the operator report.

`kfm-data pipelines` prints the same read-only diagnostics directly. Historical
job clocks remain unknown until actual new attempts/captures occur. The current
v1 source configuration, hourly slots, five-minute timer, disabled publication,
connection-only policy, backup/restore schedules, mounts and inference services
are retained. V2 configuration support does not activate candidate sources.
Source profiles and hosted publication acceptance remain pending owner review.

The report's `intake` block counts this pipeline's own captures apart from
other intake items. `intake.pipelineCaptures` (`state: "held-for-source-profile"`)
covers the undeclared quarantine payloads of `usgs-streamflow`, `nws-alerts` and
`usgs-earthquakes`. They carry no intake rights declaration, so the intake router
holds each for unknown rights and sensitivity, and each configured source adds
one an hour. They need no file-by-file review: each source's rights and
sensitivity are decided once, when its profile is signed (see
[Approvals and cutover](#approvals-and-cutover)). `intake.byStatus` counts
everything else, including declared captures, other sources' quarantine
payloads and raw files. The **KFM Working Data** desk's own intake overview
still lists the captures under review.
