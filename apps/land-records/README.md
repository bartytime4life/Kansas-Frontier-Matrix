<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/apps/land-records/readme
title: Private land-record review runtime
type: readme
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-10-13
updated: 2026-10-13
policy_label: public
owning_root: apps/
responsibility: Orientation for the loopback administrative land-record review process; no source admission or release authority.
truth_posture: "CONFIRMED local private runtime implementation; no hosted or public data release is established."
related: [docs/runbooks/land-records-ingest.md]
tags: [land-records, runtime, private-review]
[/KFM_META_BLOCK_V2] -->

# Private land-record review runtime

Loopback administrative review of individual Kansas land-instrument candidates.
Run `python3 apps/land-records/server.py --root /absolute/private/land-store` from
the repository root after importing and auditing records. The runtime is
standard-library Python, read-only, bearer-authenticated, bound to `127.0.0.1`
and blocked from publishing records. It provides filters, pagination, typed
amounts, source dates, evidence inspection and clear pending-review labels.

The external store holds all original/normalized records privately. The hosted
Explorer and its existing performance changes are untouched. This app does
not read production D1/R2, run model services or auto-start a host service.
See [the runbook](../../docs/runbooks/land-records-ingest.md) for access,
source limits, correction, rollback and validation.
