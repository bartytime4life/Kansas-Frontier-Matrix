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

## Run the check from the development PC

Use the reviewed hosted-branch checkout and Node 22.13 or later. The command
belongs to the existing PC CLI. No separate repository utility was found;
this repository does not register a bare `kfm-data` executable. The package script provides
the supported invocation from the checkout directory:

```sh
npm run --silent kfm-data -- connection
```

The equivalent direct invocation needs no npm dependency installation:

```sh
node scripts/pc-pipeline/cli.mjs connection
```

Both default to `$HOME/.local/state/kfm-data` as the private receipt root. To
choose another root, pass one absolute path outside the checkout, for example:

```sh
node scripts/pc-pipeline/cli.mjs connection "$HOME/.local/state/kfm-connection-checks"
```

The CLI creates missing directories with mode `0700` and rejects a root with
group/other permissions, symlink components, the checkout, or a parent of the
checkout. An existing root must already be private; inspect it before changing
permissions. This tiny health receipt does not require initializing a data
mount, installing the pipeline service, loading a pipeline config, signing an
approval or enabling a timer. No root/sudo operation is needed.

Do not pass SQL credentials, API keys, URLs or insecure flags. The command uses
only `https://kansasfrontiermatrix.com/api/database-connection`, with an empty
GET body, `Accept: application/json`, no cookies/authorization, no redirects,
no retry and a ten-second deadline covering response headers and body. It
accepts at most 8 KiB of JSON, validates the version, time, status, transport
and disabled-write/upload flags, and cancels rejected or timed-out responses.
It does not read local `DB_*`, systemd credentials, dataset or archive files.
The PC's normal HTTPS trust verification remains enabled; an ambient
`NODE_TLS_REJECT_UNAUTHORIZED=0` is rejected before any request.

## Receipts and exit status

After each attempted check, including a hosting failure, the CLI writes a
content-addressed, non-replacing `0600` JSON receipt below the private root:

```text
data/receipts/pipeline/connection/<sha256>.json
```

The existing PC immutable-file helper creates and syncs the file. Its contents
record the fixed public endpoint, local request/completion times, HTTP status
or null, bounded result and (when valid) the server's original `checkedAt`
and 60-second cache period. The local completion time is not a new SQL-query
time. Neither raw response/error text nor database connection details enter
the receipt. Standard output contains the receipt fields plus `receiptPath`.
Receipts stay on the PC; they are not dataset evidence or publication approval.

Exit `0` requires a valid `200` response reporting `connected:true` and
`transport:verified-tls`, **and** a saved local receipt. All unavailable or held
results exit `1`. An invalid invocation, unsafe/unwritable root or failed
receipt write also exits `1` with a bounded reason on standard error; no
receipt is promised when local storage cannot safely save it. Receipt-write
failure reports `CONNECTION_RECEIPT_WRITE_FAILED` even if SQL was reachable.

| Result / reason | Meaning and operator action |
| --- | --- |
| `connected` / `verified-tls` | The hosted check reports connectivity over verified SQL TLS. No tables, datasets or publication readiness were checked. |
| `configuration-missing` | Required hosted `DB_*` settings or port are missing/invalid. Configure them privately inside the existing host; never copy them to the PC command. |
| `hosting-unreachable` | HTTPS could not complete, including DNS, connection or certificate failures. Check website reachability and its certificate separately from SQL. |
| `request-timeout` | The one request exceeded ten seconds, including body transfer. Inspect hosting health; there is no automatic retry. |
| `invalid-response` | Unexpected HTTP status (including redirects/login pages), MIME type, oversized/incomplete body or incompatible JSON. Verify that the intended route is deployed. No response text is printed. |
| `verified-tls-unavailable` | Hosted SQL TLS failed. The bounded `tlsFailure` distinguishes provider trust, TLS support and hostname configuration. |
| `authentication-failed` / `connection-unavailable` / `private-provider-network-required` | The server could not establish its configured connection. Inspect the hosting settings privately. |
| `held` / `verified-tls-required` | The server reports `connected:true` over `host-loopback` or `provider-private-network`. The receipt preserves that transport, but the PC command exits `1`: this does not qualify as verified SQL TLS. |
| `held` / `tls-verification-disabled` | The PC environment disables HTTPS certificate verification. Remove that override before checking. |

## Separate TLS and publication prerequisites

`certificate-hostname-mismatch` is a hosting-configuration prerequisite for the
verified SQL TLS path, not a missing-CLI defect. Obtain provider-confirmed SQL
DNS and trust settings whose certificate matches the hostname; do not disable
certificate verification or switch transport to make this command pass.
The independently merged [PR #5442](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5442)
added the explicit provider-private mode described above. This CLI neither
activates nor alters it and deliberately holds its result under the verified
TLS acceptance requirement.

Source tests use synthetic endpoint responses and establish neither production
connectivity nor installation on the physical development PC. Update that PC's
reviewed checkout separately, run the command there, and retain the resulting
private receipt. Verify the public build identity and hosting Published/Preview
revisions separately before claiming production publication. A merged source
PR is not proof that the corresponding runtime is published.

The existing `publish:false` setting remains in force. The CLI enables no SQL,
FTP, capture or dataset workflow. Reverting the PC CLI correction only removes
the package script, connection branch/helper and installer copy entry; preserve
existing private receipts. No server change or database recovery is needed.
