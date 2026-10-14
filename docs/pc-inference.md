# KFM PC inference — owner operating guide

This GoDaddy composition adds invited-user research at `/assistant`, a private
account/job database, and an outbound PC worker. It introduces no paid service,
new hosting plan, tunnel, DNS change, model download or source admission. The
existing local companion and dormant `/api/qwen` route retain their behavior.

## Storage evidence and bounded qualification

GoDaddy app `q9r9beo47t` explicitly documents `/private` as nonpublic, excluded
from source ZIPs, durable across deployment and intended for SQLite. The hosted
probe at `bf45476486712501bc3d495214877cc5fb5f5f58` successfully acquired writer
locks across processes, recovered a killed transaction and passed integrity
checks on Node 22.23.3. Its private receipt recorded boot 3 with the prior
sentinel after redeployment; an explicit preview restart recorded boot 4 with
the same sentinel and successful checks. Runtime logs report the successful
checks. No accounts, passwords, jobs or inference were used in that probe.

The filesystem magic is `0x00c36400` (Ceph). These observations qualify the
tested single-writer runtime, not cross-host failover or horizontal scaling.
SQLite's network-filesystem guidance warns that sync/locking reliability
depends on deployment: https://www.sqlite.org/useovernet.html . This adapter
uses DELETE rollback journaling, FULL synchronization and an exclusive
connection held for the process lifetime; a competing connection refuses
startup. Preview and published namespaces are separate. Lock failure holds AI
without affecting map routes. No WAL, remote PC database mount or automatic
lock breaking is permitted. Multi-replica/partition/power-loss qualification
remains open; do not scale this feature without requalification or a separately
reviewed store adapter. The volume's free-space reading is not a hosting quota.

Directory Rules section 10.1 and accepted ADR-0029 assign these adapters to
the existing application's `server/`, user surface to `app/`, invocation tools
to `scripts/`, and tests to `tests/`. This standalone composition is not a new
canonical policy, contract or release home. Its bounded application protocol is
proposed hosted-AI compatibility work, not acceptance of unrelated AI ADRs.

## What is stored and who can act

The private database is `/private/kfm-pc-ai-v1/{preview|published}/accounts-jobs.sqlite`.
Directories are owner-only; the database is mode 0600, checks ownership,
symlinks, integrity, schema identity and the encryption-key fingerprint.
It is limited to 8192 SQLite pages (normally 32 MiB). Do not copy the open
database or remove its journal. Preserve the key with an owner-controlled
backup; a different key holds startup instead of reseeding or dropping data.

Passwords use salted scrypt. Invitations are single-use, expire after 24 hours
and are stored as SHA-256 hashes. Sessions are opaque, hashed in storage and
expire after four hours; cookies are Secure, HttpOnly, SameSite=Strict and
host-scoped. No public registration exists. Owner tools can invite/revoke;
revocation invalidates sessions and cancels jobs. The owner capability does not
grant data publication authority. The worker credential can heartbeat, claim,
check leases and return results only, and cannot invite, revoke or publish.
Owner and worker credentials must be different; the worker configuration has
no owner credential or data-encryption key.

Question/evidence/result payloads use AES-256-GCM and expire after 24 hours.
Minimal job metadata expires after 30 days. Passwords, questions, packets,
answers and credentials are not logged. These retention rules affect only the
new account/job namespace, never existing data stores or source receipts.

## Owner configuration — no credentials in chat or Git

After reviewing the exact implementation, run from this checkout:

```sh
node scripts/pc-ai-owner.mjs prepare /absolute/private/path/owner.secret.json published
```

Use a fresh private destination outside the source and deployment tree. The
tool creates owner configuration, a separate `.worker.secret.json`, and a
`.hosting.txt` provider-entry file with mode 0600. It prints no secrets and
refuses to overwrite an existing file. Preserve any partial output if an error
occurs; choose a fresh path rather than overwriting it. Use a separate fresh
configuration with role `preview` for any preview account experiment.

Enter the seven `.hosting.txt` settings directly in GoDaddy's secret/settings
interface for the intended variant. Do not paste them into chat, logs, public
files or source. Publish and activate only the reviewed exact head after owner
acceptance. Required settings:

- `KFM_PC_ENABLED=true`
- `KFM_PC_STORAGE_MODE=single-writer-confirmed`
- `KFM_PC_ROLE=published` (or `preview` in an isolated preview)
- `KFM_PC_ORIGIN=https://kansasfrontiermatrix.com` (exact preview origin for preview)
- `KFM_PC_ADMIN_TOKEN_HASH`, `KFM_PC_WORKER_TOKEN_HASH`, `KFM_PC_DATA_KEY`

Retain the existing exact `VINEXT_TRUSTED_HOSTS` hosting-proxy configuration.
Missing settings produce a visible disabled state with no account/store
creation. Never reuse production secrets or accounts in preview. GoDaddy's
preview is additionally protected by its own owner login, so an ordinary PC
worker cannot treat it as an anonymously reachable machine endpoint. Do not
export a GoDaddy browser cookie or bypass that protection to test the worker.

Start the worker explicitly after the published API is accepted:

```sh
node scripts/pc-ai-worker.mjs /absolute/private/path/owner.secret.json.worker.secret.json
```

It calls only fixed HTTPS KFM routes and loopback Ollama at 127.0.0.1:11434.
It verifies Ollama's release floor and the existing qwen3:8b full digest before
and after inference, supplies a 16384-token context and a 512-token output cap,
and never pulls a model or executes model tools. It checks cancellation while
generating. Stop with Ctrl+C; no automatic system service or sleep-policy change
is installed. Computer sleep/offline means AI offline while the map remains
usable. There is no cloud fallback.

Create an invitation yourself:

```sh
node scripts/pc-ai-owner.mjs invite /absolute/private/path/owner.secret.json username
```

The invitation is saved beside your protected config. Deliver it privately
yourself; no email/Slack service is involved. The recipient opens `/assistant`
and sets their own password. `revoke` with the same arguments revokes access.

## Evidence, limits and interfaces

Only the existing governed Kansas knowledge reader resolves records. Browser
requests contain a question, search terms and optional named-place/date filters,
never trusted evidence or release state. Date filters exclude undated records.
Retrieval is bounded to 20 records / 40 documented assertions / 24 KiB; truncation
is visible. Sensitive/precise-location questions are withheld before inference.
No RAW, quarantine, private files, capture archive or external context imagery
is made into evidence. The current Node composition has no released knowledge
storage binding: research therefore abstains until an independently governed
release becomes available. Existing source capture is not release authority.

The model may select exact supplied documented assertions and provide a
separate interpretation. The server reconstructs supported facts and citation
links, rejects invented/modified assertions and precise-location/URL content
in interpretation, and rechecks the evidence snapshot before result commit and
every answer read. Generated prose never becomes evidence, review or release.

The application protocol is `/api/pc-ai`: status, sign-in, activate, sign-out;
authenticated job submission/read/cancel; owner invite/revoke; worker
heartbeat/claim/check/result. JSON requests are bounded; browser writes require
the exact Origin; credentials and sessions are server-validated. Jobs have
opaque identifiers and user isolation. One inference runs at a time, five jobs
may wait/run globally, one per user, ten submissions per user per hour, and 50
invited accounts. Worker health expires after 15 seconds. Inference has a
90-second limit, its lease 100 seconds, and a job's total deadline three minutes.
Expired/cancelled jobs and stale/duplicate results are not automatically retried.

## Acceptance and rollback

Changed-area tests cover identity, one-use invitations, cookies, private encrypted
payloads, user/worker/owner separation, CSRF, cancellation, queue/rate limits,
expiry, release withdrawal, invented citations, model mismatch and exclusive
database contention. Production HTTP and browser checks must use the exact new
build. Synthetic packets are test material, never released evidence.

Hosted preview of disabled behavior, live credential configuration, actual
worker heartbeat, invited-user sign-in and a real released-evidence answer are
separate acceptance steps. Do not claim the latter from local unit tests or a
synthetic Ollama answer. Back up the closed private store and key through
owner-controlled means before upgrades. No paid backup provider is introduced.

Rollback sets `KFM_PC_ENABLED=false`, stops the PC worker and restores the
previous accepted GoDaddy source. Preserve the private database, encryption key
and disposable probe evidence. It does not remove Ollama, shared models, source
data, original Sites or other applications. No destructive down migration exists.
