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
