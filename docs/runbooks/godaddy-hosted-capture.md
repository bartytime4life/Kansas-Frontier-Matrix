<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/godaddy-hosted-capture
title: GoDaddy Node source capture scheduler
type: runbook
version: v1
status: implementation candidate; deployment, identity, database migration and scheduled capture activation pending
owners: ["@bartytime4life"]
created: 2026-10-14
updated: 2026-10-14
policy_label: public
current_path: docs/runbooks/godaddy-hosted-capture.md
owning_root: docs/
responsibility: Activate and verify the capture-only scheduler for the separate GoDaddy Node Explorer composition
truth_posture: CONFIRMED owner scope and current Node dashboard; PROPOSED runtime activation until exact heads and provider configuration pass review
[/KFM_META_BLOCK_V2] -->

# GoDaddy Node source capture scheduler

This runbook belongs to existing `docs/runbooks/`; the runner belongs to the
existing `.github/workflows/` platform responsibility. Placement follows
Directory Rules v2, accepted by ADR-0029. It creates no parallel pipeline,
source-admission, policy or release authority. The separate Node application
keeps its implementation under `server/` and its composition-owned migration
under `server/ingestion-schema.sql`.

The owner selected scheduled ingestion, durable storage, owner-only GitHub
sign-in and an 80 GB maximum archive. The Node candidate's first adapters are
Kansas USGS streamflow, active NWS Kansas alerts and the USGS earthquake catalog.
Capture bytes and provenance remain private in WORK/QUARANTINE. A structural
check does not release data or satisfy rights/sensitivity review. This workflow
only triggers a fixed capture endpoint; it cannot promote, publish, deploy,
delete captures or access the database, owner's reports or repository contents.

## Activation gates

1. Review and separately approve the exact Node application head, additive shared
   MySQL migration and environment configuration. Verify provider storage
   capacity, certificate-verified MySQL connectivity and owner sign-in. Preview
   and published environments share the database: keep preview workers disabled.
2. Deploy that reviewed Node head and check public free exports and private
   archive denial. The archive initially remains paused. These steps have no
   relationship to the older cPanel static-site deployment workflow.
3. Approve this scheduler head for merge into the default `main` branch. A cron
   workflow on a non-default branch is not active. Do not deploy monorepo `main`
   into the standalone Node hosting app.
4. Create the `kfm-hosted-capture` GitHub environment with deployment branches
   restricted to protected `main`. Configure its sole secret,
   `KFM_CAPTURE_WORKER_TOKEN`, to the same newly generated capture-only token in
   GoDaddy's server secrets. The owner enters new credentials directly in the
   provider interfaces; never put them in source, chat, URLs or artifacts.
   Do not reuse a GitHub PAT, repository token or owner login session.
5. Set repository variable `KFM_HOSTED_CAPTURE_ENABLED=true` only after these
   gates pass. This workflow has no GITHUB_TOKEN permissions, no checkout, no
   pull-request trigger, no code download, and no configurable destination URL.
6. The owner resumes the pipeline in Source operations. Dispatch this workflow
   once from `main`, then verify a stored receipt, original-byte hash, quarantine
   state and the next scheduled run. Keep incomplete activation labeled pending.

GitHub cron is a trigger with possible delays, not an exact-time SLA. Each tick
uses MySQL fencing, capacity reservation and deterministic source/time-bucket
identity. Duplicate invocations cannot append duplicate captures. Provider
errors retry with bounded backoff; missed windows after downtime stay missing
instead of being invented. NWS active alerts are captured at actual retrieval
time, not reconstructed for the bucket start. See [GitHub schedule behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## Storage and rollback

The Node archive enforces 80,000,000,000 accounted bytes across original decoded
entities, serialized receipts and a per-capture overhead allowance. The provider
must independently supply sufficient disk/database capacity; allocation, indexes,
transaction logs and backups are not fabricated as available capacity by that
application counter. Stop on either provider failure or the archive limit;
never delete captures automatically to make room.

Pause capture in the owner workspace and set `KFM_HOSTED_CAPTURE_ENABLED=false`
before rollback. Remove or rotate the capture-worker token if necessary. Revert
this workflow to disable its trigger; preserve the shared database, captures,
hashes and receipts. Returning the Node application to its prior published head
does not erase the archive. Do not reset MySQL or import Cloudflare SQLite/D1
migrations. DNS, email, checkout, payments and the original private Sites project
remain outside this change.
