# Bounded local water service templates

These user-service templates are repository delivery candidates, not installed
services. Host adoption remains HOLD. Directory Rules / ADR-0029 place deployment
configuration under infra; application code remains in apps/packages/tools.

`kfm-governed-api.service` uses an explicit working directory and virtualenv,
loopback-only application listener, read-only filesystem and private serving
store. `/healthz` is process/configuration status; it does not grant evidence
readiness. `kfm-water-candidate.service` is a bounded oneshot with a writable
external candidate store and no serving-store write access. Its timer proposes
hourly capture without missed-run catch-up; failed captures preserve earlier
candidates. Both declare resource limits, private temporary storage, safe umask
and finite shutdown. The API restarts on failure; acquisition does not retry
unboundedly at the service-manager layer.

Paths under `%h/Projects/Kansas-Frontier-Matrix`, `%h/KFM-data` and
`%h/KFM-release-serving` are template configuration. Review and render them for
an isolated adopted checkout before installation. Ensure the Python environment,
private stores and user namespace/hardening support exist. Do not copy these
units over current host configuration or enable duplicate acquisition jobs.

`ollama-loopback.conf.example` proposes loopback containment. The inspected host
has an explicit wildcard override. Active local connections do not prove there
are no remote consumers. Inventory consumers and obtain the appropriate host
change approval before installing the drop-in or restarting the shared service.

Static validation: `systemd-analyze verify` on rendered units; command, denial and
rollback tests are described in [the water runbook](../../docs/runbooks/water-pilot.md).
Static verification cannot prove a host's installed/enabled/active state.
Rollback before adoption is removal of the candidate units; after authorized
adoption, stop/disable only the specifically installed units and restore the
reviewed prior configuration. Preserve all source bytes and receipts.
