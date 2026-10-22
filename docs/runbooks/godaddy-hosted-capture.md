<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/godaddy-hosted-capture
title: GoDaddy Node source capture scheduler
type: runbook
version: v2
status: source implementation confirmed; live schema, capacity and scheduled activation unverified
owners: ["@bartytime4life"]
created: 2026-10-14
updated: 2026-10-21
policy_label: public
current_path: docs/runbooks/godaddy-hosted-capture.md
owning_root: docs/
responsibility: Explain the existing private capture store, machine controls, scheduler gates and non-destructive recovery
truth_posture: CONFIRMED inspected main 91ca0314 and hosted 65d56575; live configuration and capture operation NEEDS VERIFICATION
[/KFM_META_BLOCK_V2] -->

# GoDaddy Node source capture scheduler

This guide describes the implementation inspected on **October 21, 2026**:
monorepo `main@91ca0314f0158736f69f953d7973457c19442fde` and standalone hosted
`65d5657536e4c42a7a8ea0772ed12ca0b78bc939`. Source presence is confirmed;
production configuration, live migration, stored captures and scheduler enablement
were not inspected in this documentation review. Use the
[Node source/deployment runbook](godaddy-node-hosting.md) to identify the actual
Published revision before any later authorized operation.

The current public app has **no owner sign-in or Source operations page**.
The October 14 instructions that depended on those pages are superseded here.
Capture run/pause/resume use a separate server-side machine capability; a
browser session, role header or anonymous visitor grants no capture authority.
This correction does not enable the scheduler or apply a database migration.

## Implemented path and limits

| Component | Inspected implementation | Boundary |
|---|---|---|
| Scheduler | [`.github/workflows/godaddy-hosted-capture.yml`](../../.github/workflows/godaddy-hosted-capture.yml) on main; runs at minutes 17 and 47, or manual dispatch | Job requires `refs/heads/main`, `KFM_HOSTED_CAPTURE_ENABLED=true` and the `kfm-hosted-capture` environment. It calls one fixed HTTPS run endpoint; no checkout or repository-token permissions. |
| Machine access | [capture-worker-access.mjs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/server/capture-worker-access.mjs) | Requires complete ingestion configuration, exact canonical origin and constant-time bearer-token comparison; rejects cross-site requests. |
| Run and control | [run route](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/app/api/source-pipeline/run/route.ts), [control route](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/app/api/source-pipeline/control/route.ts) | `POST /api/source-pipeline/run`; `POST /api/source-pipeline/control?action=pause` or `action=resume`. Both require the machine capability. The scheduler only invokes run. |
| Status | [status route](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/app/api/source-pipeline/status/route.ts) | Public bounded status is separate from capture bytes and control. Removed capture-download browser routes do not become public again. |
| Storage | [MySQL store](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/server/ingestion-store.mjs), [schema](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/server/ingestion-schema.sql) | Parameterized writes, transaction fencing, capacity reservation, deterministic capture identity and hash-checked private chunks/receipts. Captures remain WORK/QUARANTINE. |
| Schema review | [migration script](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/scripts/migrate-hosted-ingestion.mjs) | `npm run archive:migration` is review-only by default; applying needs a separately reviewed exact SQL digest and authorization. Do not apply from this guide alone. |

The initial capture adapters cover Kansas USGS streamflow, active NWS Kansas
alerts and USGS earthquakes. Structural checks, original-byte hashes and a
successful capture do not admit a source, close an EvidenceBundle, release a
layer or publish an answer. No FAA or OpenSky activation is supplied by this
scheduler; [aviation intake](aviation-intake-20261021.md) has separate holds.

## Activation gates

Activation remains a later authorized operation. Reconcile all of the following
against the actual Published source, with preview workers disabled:

1. Verify the app identity, deployed input digest, database engine/version,
   current schema, existing rows and a recoverable backup. Review the additive
   migration in a disposable compatible database before applying it to shared
   storage. Preserve the original tables and data. The initial control row is
   paused; no login page is needed or available.
2. Verify the current
   [ingestion configuration](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/server/ingestion-config.mjs).
   Its exact guards are summarized below. A configured flag is a declaration;
   independently measure the capacity and verify TLS/identity.
3. Confirm GitHub's scheduler environment is restricted to the intended protected
   main branch. Its sole secret is `KFM_CAPTURE_WORKER_TOKEN`, matching the
   server's dedicated capture token. Never reuse an AI gateway key, polling
   worker key, personal GitHub token or retired login credential. Inspect
   settings without printing secret values.
4. Through a trusted operator client, use the authenticated control endpoint to
   resume the reviewed capture configuration. Keep bearer credentials in a
   protected header/input channel, never a URL, source file, chat or shell
   command argument. An anonymous or retired browser credential must remain
   denied. This runbook does not issue that request.
5. Only after separate activation approval, set
   `KFM_HOSTED_CAPTURE_ENABLED=true`, dispatch once from main, and verify the
   stored original-byte digest, receipt, quarantine state and next scheduled
   run. Distinguish GitHub trigger success from persisted capture success.

| Server guard | Required value or condition in inspected source |
|---|---|
| `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` | Present; hostname must support certificate identity verification. `DB_PORT` is separately validated by the store. |
| `KFM_DB_TLS`, `KFM_DB_CA_PEM` | `verified` and the database CA; TLS rejects invalid certificates and identities. |
| `KFM_PUBLIC_ORIGIN` | Exactly `https://kansasfrontiermatrix.com`. |
| `VINEXT_TRUSTED_HOSTS` | Includes the apex and contains only the permitted apex/www hostnames; preview hostnames fail this capture guard. |
| `KFM_CAPTURE_WORKER_TOKEN` | Dedicated 43–256 character base64url-style machine secret. No value belongs in documentation. |
| `KFM_INGEST_ENABLED`, `KFM_RUNTIME_ROLE` | `true` and `published`. |
| `KFM_ARCHIVE_CAPACITY_CONFIRMED_BYTES` | `80000000000`, only after independent capacity verification. |

GitHub cron can be delayed; its definition is not an exact-time service promise.
Each capture tick uses MySQL fencing, capacity reservations and deterministic
source/time-bucket identity. Provider errors retry with bounded backoff. Missed
windows stay missing. Active alerts are captured at retrieval time, not
reconstructed for the start of a time bucket.

## Storage and rollback

The current store enforces **80,000,000,000 accounted bytes**, including original
decoded entities, receipts and a per-capture allowance. That application counter
is not a provider allocation: database overhead, indexes, transaction logs and
backups require separate capacity evidence. Captures stop on provider failure
or the archive limit; they are not automatically deleted to make room.

Large-file placement on the second AI Linux PC is the owner's intended physical
layout, subject to verifying capacity, connectivity, resource contention and a
separate backup/restore path. The present MySQL chunk store does not implement
that relocation. Preserve the AI installation and original copies; use the
[placement assessment](aviation-intake-20261021.md#physical-placement-and-database-reconciliation)
before choosing paths or changing storage.

For an authorized operational stop, disable the GitHub trigger with
`KFM_HOSTED_CAPTURE_ENABLED=false` and pause through the authenticated machine
control. If that path is unavailable, use separately authorized server settings
to disable capture; do not attempt a retired browser sign-in. Rotating or
revoking the dedicated token invalidates both control and scheduler access.
Preserve the shared database, chunks, receipts and hashes through source rollback.

A source revert does not undo already applied SQL or delete captures. Do not
reset MySQL, import SQLite/D1 migrations, reseed stores, change DNS or modify
the original Sites bindings as capture recovery. Database restore and any later
bulk-file migration need their own reviewed procedure and evidence.

## Evidence, placement and verification

Inspected regression sources include
[hosted-ingestion tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/tests/hosted-ingestion.test.mjs)
and [machine-control denial tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/tests/login-cleanup-review.test.mjs).
They were not executed in this docs-only review. Live MySQL, scheduler settings,
capacity, captures, outage recovery and second-PC storage remain unverified.

This existing runbook belongs to `docs/runbooks/`; implementation remains in
its standalone `server/`, `app/` and `scripts/` roots, and scheduler orchestration
in monorepo `.github/`. The adopted [Directory Rules](../doctrine/directory-rules.md)
and [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) retain
those boundaries. No new source registry, policy, data authority or release
lane is introduced. Roll back this documentation change with a focused Git
revert; that requires no live-data rollback.
