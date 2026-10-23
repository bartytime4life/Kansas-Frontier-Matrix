# Existing GoDaddy SQL connection, October 23, 2026

Owner scope: keep bulk data on the active dev PC, use the existing subscription,
and add no paid resources or fees. No raw data, library database, archive, model
files, backups or imports are uploaded. Automatic publication and FTPS mirroring
remain disabled. No SQL migration, import or write is part of this connection.

`GET /api/database-connection` checks the injected `DB_*` credentials inside the
existing GoDaddy app with exactly `SELECT 1 AS connection_ok`. Credentials never
leave the runtime. Its coarse public response contains no host, database name,
username, password, table names or records. Query parameters are rejected and
other methods have no handler. Concurrent checks share one operation and results
are cached for 60 seconds; there is no poller, pool, paid service or retry loop.
The request closes its connection after a five-second connection/two-second
query budget. Only exact loopback addresses may use the local host transport;
other connections require verified TLS using the system trust store or the
existing `KFM_DB_CA_PEM`. Certificate verification is never bypassed.

The dev PC's `kfm-data connection` makes this small check on demand and saves a
local receipt. A successful result establishes connectivity only. It does not
approve dataset publication or enable automatic SQL/FTP updates. The existing
`publish:false` setting remains in force.

This additive source starts from deployed commit
`3d24f4ae1866f9b9407cdb07e8390b18c23371c4`, preserving its application inputs.
Before deployment, compare the current live build identity again and reconcile
any intervening source update. Rollback removes this route/module and redeploys
the prior code; no database recovery is needed because the check never writes.
