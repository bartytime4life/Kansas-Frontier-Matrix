# Daily source archive

`/daily-archive` retains bounded Kansas adapter responses in the existing R2
binding and indexes each attempt in the existing D1 binding. The Explorer's
Time panel links to it. The map reads only the exact selected stored object,
checks its SHA-256 and geometry, and never replaces missing days with live data.
The county underlay is the same day's captured **2020** reference edition.

## Capture and curation

Nine existing adapters are captured sequentially: county reference, river
observations, earthquakes, active alerts, smoke, satellite fire points, incident
reports, seismic station metadata, and disaster declarations. Provider time,
source day (when supplied), retrieval time, source limitations, quality/truncation,
feature properties and units are preserved. Files are the exact normalized
adapter response bytes, **not original provider downloads**. Raster imagery,
radar, full river time series, and restricted/consent-dependent sources are not
archived by this job. Existing provider-history tools remain available.

Snapshots use their actual UTC retrieval day. They are not daily summaries;
short-lived alerts and changes between captures can be missed. No automatic
historical backfill is inferred. The source adapter version is the deployed Site
version; archive schema/object prefix is `daily-archive/v1`.

Each source/day has at most four attempts. A ready or empty capture is idempotent;
partial/failed attempts can be retried, preserving prior versions. Only validated
and readback-verified objects become map-visible. A ten-minute D1 lease serializes
writers. Crashed attempts become failed on a subsequent writer, retaining their
conservative byte reservation. Resolve uncertain objects with their recorded key
and hash before releasing any reservation; there is no automatic cleanup.

Pending captures can be inspected as external context. Human review appends a
note against the exact capture. A hold hides that capture from the map while
retaining its downloadable bytes. Review never grants source admission, evidence
status, release, or scientific acceptance. Review history is append-only.

## Storage and controls

The initial storage ceiling is 2,000,000,000 bytes per archive; each capture
reserves up to 16 MiB before provider access. The archive screen shows exact
usage/reservations and allows an owner to pause collection or change the ceiling
(up to 1 TB). Nothing is deleted automatically. This limit accounts for retained
payloads/reservations; D1 index/review overhead is additional. Local and hosted
D1/R2 stores are separate and are not silently synchronized.

## Unattended runtime

`node scripts/capture-daily-archive.mjs` captures the running loopback Site at
127.0.0.1:4173, then reads the catalog back. Exit 1 means one or more sources failed or could not be verified. Exit 2 means
every response was stored and verified but some sources have partial coverage;
the systemd service accepts exit 2 while the log and map retain those gaps. Re-run is safe. A paused archive
returns a paused result without provider calls. A missed day remains missing.

The Linux user timer runs daily at 23:15 UTC, with a retry at 23:45 UTC and
`Persistent=true` for the next login/resume. The local Explorer must be running;
local capture cannot operate while the machine is off. Hosted scheduling is
separate and continues independently of this computer.

For hosted execution, obtain current service access from Sites `get_site` for
`appgprj_6aa0b1c41bc08191bfd86003920f1631`, verify it remains owner-private, and
run this script with `--hosted-stdin`, passing `{ "token": "…" } through hidden
stdin. Never save/print the token or put it in a command line or schedule prompt.
The writer uses Sites' private dispatch boundary; do not share or make the Site
public without adding explicit writer authorization. Browser writes also require
a same-origin request and `X-KFM-Archive-Writer: daily-v1`; no CORS is granted.

Apply only the additive `0005_daily_archive.sql` migration to an existing local
store after backing it up. Hosted publication applies the appended migration.
No existing admission tables, objects, datasets, or receipts are modified.

To pause: use the archive screen. To disable the local schedule:
`systemctl --user disable --now kfm-daily-archive.timer`.
