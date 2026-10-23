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
existing `KFM_DB_CA_PEM`. Certificate verification is never bypassed in this
default mode.

A separate provider-private option is disabled unless
`KFM_DATABASE_CONNECTION_TRANSPORT=provider-private-network` is explicitly set.
It follows the provider's documented standard MySQL connection without TLS,
only after resolving the injected hostname to RFC1918 IPv4 addresses and
pinning the connection to a validated address. Empty, public or mixed IPv4
answers are rejected before connecting. It never falls back after a TLS error.
This sends SQL authentication over an unencrypted internal network leg, so the
owner must explicitly approve that encryption change before activation. The
PC-to-website HTTPS connection and the fixed SELECT-only behavior remain.
The owner explicitly approved this guarded transport on October 23, 2026.
Activation still requires the runtime setting and a successful private-address
check. This mode does not enable any existing ingestion or publication route.

The October 23 preview recheck still reports a certificate hostname mismatch.
The owner chose the website's existing managed MySQL and left FTP unpaired.
The owner-created FTP account has zero usage; the owner subsequently changed
its quota to unlimited. Its credentials have not been collected and no file
transfer is enabled.

The dev PC's `kfm-data connection` makes this small check on demand and saves a
local receipt. A successful result establishes connectivity only. It does not
approve dataset publication or enable automatic SQL/FTP updates. The existing
`publish:false` setting remains in force.

This additive source starts from deployed commit
`3d24f4ae1866f9b9407cdb07e8390b18c23371c4`, preserving its application inputs.
Before deployment, compare the current live build identity again and reconcile
any intervening source update. Rollback removes this route/module and redeploys
the prior code; no database recovery is needed because the check never writes.
