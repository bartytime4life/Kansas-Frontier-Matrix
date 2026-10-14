# PC inference storage qualification

This isolated candidate starts from the exact hosted source
`f44ce0cf0d72c019252bb93efc4f138f671107de`. It adds a preview-startup probe only.
GoDaddy app: `q9r9beo47t`. No publication, DNS, billing, private-source admission,
accounts, worker credentials or inference activation is part of this probe.

Directory Rules section 10.1 and accepted ADR-0029 place these runtime adapters
in the existing deployable application's `server/`; tests remain in `tests/`.
This composition creates no parallel canonical contracts or policy authority.

GoDaddy's authenticated File Manager describes `/private` as private, excluded
from source ZIPs, durable across deploys and suitable for SQLite. On October 14,
the private store listed no files. Those provider statements do not prove actual
locking, restart recovery, replica topology or live durability.

The probe writes only a fixed non-secret identity and boot counter under
`/private/kfm-pc-storage-probe-20261014/`. It verifies database ownership and
permissions, cross-process writer exclusion, killed-writer transaction rollback,
SQLite integrity and persistent sentinel continuity. It has no HTTP route and
logs only bounded diagnostic metadata. It does not read or modify other stores.

Local validation: `node --test tests/pc-storage-probe.test.mjs` passes both tests.
Hosted qualification requires the logged first boot, successful re-open after
preview restart and source redeploy, public-path denial, and verification of
replica/shared-volume behavior. Do not treat a local pass as hosted acceptance.

Keep published source unchanged. Restore preview to the saved hosting branch
after qualification. The disposable probe bytes may remain private as evidence;
they never become an account database or a release receipt.
