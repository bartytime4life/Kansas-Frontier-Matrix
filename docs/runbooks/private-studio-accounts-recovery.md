<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-private-studio-accounts-recovery
title: KFM Private Studio accounts and recovery evidence
type: runbook
version: v1
status: implementation-candidate
owners: ["@bartytime4life"]
created: 2026-11-15
updated: 2026-11-17
policy_label: public
owning_root: docs/
responsibility: Describe local identities, the protected workspace, recovery evidence, validation limits and rollback.
truth_posture: CONFIRMED bounded synthetic and HTTP-gateway tests; NEEDS VERIFICATION full Studio, browser, independent security review and installation.
[/KFM_META_BLOCK_V2] -->

# KFM Private Studio

One local workspace joins Intake, Working Data, read-only Library, Acceptance &
evidence, Backup & recovery, and Users & access. The public Explorer is a
separate product. This change does not add a public-map login or publish a web
service. The existing hosted Category Acceptance and Recovery Sites are not
changed, synchronized, or authenticated by these local accounts.

## Operating boundary

Supported entrypoints are `intake_server.py`, `private_server.py` and the existing
`start-local.sh` launcher. They require application-local accounts. The previous
backend is retained byte-for-byte as internal `intake_backend.py` to keep intake,
extraction and sensitivity behavior separate from authentication. It is not a
supported server entrypoint; do not start it directly. An operating-system owner
who can execute arbitrary Python or edit the database is outside this access
boundary and can bypass application controls. Local accounts are not Linux users.

The listener remains **literal 127.0.0.1**. Remote clients, nonexact Host values,
forwarded/proxy headers and cross-origin requests are rejected. Do not use a
reverse proxy, public tunnel, LAN binding or port forwarding with this candidate.
Remote use needs a separately reviewed HTTPS deployment with an appropriate
application server, Secure cookies, trusted-proxy rules and independent security
acceptance. This stdlib server is not offered as an internet-facing service.

The HTTP-only loopback session cookie is HttpOnly and SameSite=Strict; it does
not use the Secure flag because this mode deliberately uses loopback HTTP.
Passwords/data are not encrypted on disk by this module. Full-disk and backup
encryption require separately managed keys and procedures. The sign-in shell,
its static CSS/JavaScript, a boolean setup status and a minimal build-health
response are the only anonymous information. No inbox, user list, serial number,
private path, evidence receipt, export or session bearer is anonymous.

## First owner setup — only on the actual local machine

Following independent review and explicit installation approval, launch from the
complete repository checkout:

```sh
./tools/local_data/intake_studio/start-local.sh
```

The launcher opens `/studio`, redirects to sign-in when necessary, and prints a
one-time setup code only in its interactive terminal when no owner exists.
It does not print a password. It preserves/refuses an older running copy rather
than replacing it. Never run a second installation against an unqualified store.

For an explicitly selected existing private Studio root, generate a code from
the repository root using this local command:

```sh
python3 -m tools.local_data.intake_studio.accounts --store /ABSOLUTE/PRIVATE/STUDIO_ROOT setup-code
```

Replace the illustrative path with the verified Studio root. The command refuses
a nonexistent/unprotected root. The code expires after ten minutes and can create
one first owner. Enter it in the local first-time setup screen, choose a username
and passphrase, then sign in. There is no public self-registration, default admin
password, cloud identity provider, email service or credential in the repository.
Do not put a password/setup code into chat, a URL, a shell argument or a log.

Usernames are normalized ASCII identifiers, 3–48 characters. New passphrases are
15–128 Unicode characters, normalized to NFC, with spaces supported and a 512-byte
UTF-8 bound. A small offline common/context-password blocklist is used; it is **not
comprehensive compromised-password screening**. No periodic expiry or arbitrary
uppercase/symbol rules are imposed. Password-manager paste is allowed.

Passwords use salted scrypt at N=2^17, r=8, p=1, with 32-byte output. No plaintext
password or reversible old password is stored. The two-operation KDF semaphore
bounds concurrent KDF memory. Five failed attempts trigger persisted temporary
throttling with bounded backoff. Local attacker-induced denial of service remains
possible; account authentication does not defend the machine from its OS owner.

## Administrator quick start — local admin program

Everything below runs **on the PC that hosts Studio**, from the repository root.
The admin program has no HTTP route: its authority is owning the private Studio
files on this machine, the same boundary as the break-glass reset. Passwords are
typed only at its hidden terminal prompt (twice); they are never command
arguments, environment variables or files, and are never printed or logged.

```sh
./tools/local_data/intake_studio/studio-admin.sh
```

With no arguments it opens a menu. The same actions are available as commands:

| Task | Command |
|---|---|
| Show Studio, accounts and data workspace | `studio-admin.sh status` |
| Create the first administrator (one-time code) | `studio-admin.sh setup-code` |
| Change any account's password | `studio-admin.sh password USERNAME` (add `--temporary` to force a change at next sign-in) |
| Add a user with a temporary password | `studio-admin.sh add-user USERNAME --role operator` |
| Enable, disable or change a role | `studio-admin.sh enable USERNAME`, `disable USERNAME`, `role USERNAME viewer` |
| Clear lockouts after failed sign-ins | `studio-admin.sh unlock` |
| Sign out every browser session | `studio-admin.sh sign-out-all` |
| Recent account activity | `studio-admin.sh audit` |
| Connect Working Data / Library | `studio-admin.sh workspace setup` (guided), `workspace init PATH`, `workspace set KEY VALUE [KEY VALUE ...]`, `workspace unset KEY`, `workspace show` |
| Stop a launcher-started Studio so new settings apply | `studio-admin.sh stop` |

Changing a password signs that account out everywhere and clears its sign-in
limit. The last active administrator cannot be disabled, demoted or given a
temporary password from this program either. Every change is recorded in the
account audit as `local-console`. The web **Users & access** page remains the
admin-only browser equivalent and still requires the administrator's current
password for each change.

### Connect the data workspace so held reviews can move

Intake reviews stay held in the private preparation inbox until an administrator
chooses **Send to KFM**. That button only works when Studio is started with a
Working Data store. Earlier, `start-local.sh` never passed one, so the button
always reported that Working Data was not connected. The launcher now reads
owner-private settings from `~/.config/kfm-intake-studio/workspace.json`
(mode 600, outside Git) and passes them to the server:

| Setting | Server option | Meaning |
|---|---|---|
| `kfm_root` | `--kfm-root` | Working Data store; receives items sent from held reviews. Required for **Send to KFM**. |
| `library_root` | `--library-root` | Read-only Data Library catalog. |
| `archive_root` | `--archive-root` | Original archive for Library file locations (needs `library_root`). |
| `inbox` | `--inbox` | Read-only downloads folder scanned by Working Data. |
| `raster_python`, `pipeline_lock`, `store_check`, `working_connection`, `qwen_model` + `qwen_digest` | same names | Optional advanced settings documented in the [intake runbook](local-intake-studio.md#handoff-to-the-existing-governed-workflow). |

1. Run `studio-admin.sh workspace setup`. Enter your existing Working Data store
   (for example the private `KFM-pipeline` store) or a new empty folder; the
   program offers to initialize a new folder as a private KFM data store. Add the
   Library and inbox folders if you use them.
2. The program checks every path before saving: folders must exist, data stores
   must be initialized, owned by you with mode 700 and outside the Git checkout.
   Nothing is saved when a check fails.
3. Apply it: `studio-admin.sh stop`, then `./tools/local_data/intake_studio/start-local.sh`.
   The launcher re-checks the settings and refuses to start, with a plain
   explanation, if a drive is unmounted or a path changed.
4. Sign in. The Overview shows **Data workspace: Connected**; Working Data and
   Data Library open in the sidebar, and **Send to KFM** is available to
   administrators for saved **Ready for integration review** records.

Sending still follows the [intake handoff rules](local-intake-studio.md#handoff-to-the-existing-governed-workflow):
sensitivity holds, unknown rights and unsaved edits still block it; the original
becomes a source-bound quarantine object, and nothing is admitted or published.
Set the optional Qwen pair in one change with `workspace set qwen_model NAME qwen_digest DIGEST`; clearing either one clears both. Remove a setting with `workspace unset KEY`, or delete the settings file to return
to the previous unconnected behavior.

## Roles and owner control

| Role | Scope |
|---|---|
| Admin/owner | Manage accounts, reset passwords, change roles, disable accounts; existing private intake/Qwen operations; configure recorded drive identities; review evidence. |
| Operator | Read private workspace records, upload intake files, import acceptance receipts and append observations. Cannot manage users, make intake clearance/send decisions, run Qwen administrative actions or accept evidence. |
| Viewer | Read/download permitted private workspace records and evidence; no mutation. |

These are workspace-wide roles, not per-file tenant isolation. Granting Viewer
therefore grants access to private records in this Studio. The Library remains
read-only; no role gains publication, source-admission, sensitivity-clearance or
recovery-command execution authority from the new modules.

**Users & access** lets an admin create users, assign roles, disable/enable users
and set temporary passwords. The owner's current password is required for these
changes. Temporary-password users must choose a new password before private data
becomes accessible. Reset, disable and role changes revoke that user's sessions.
The last enabled administrator with a permanent password cannot be removed or
made temporary through the web interface. Passwords cannot be displayed; they
can only be changed or reset. An owner changes their own password in My account.

Server-side sessions have a 30-minute idle limit and an eight-hour absolute limit.
Tokens are random, represented by keyed hashes in the database, never stored in
web storage or evidence exports. Restarting the process invalidates existing
browser sessions. POST operations require the exact Origin and per-session CSRF
value. All protected legacy APIs are behind the gateway, including original-file
and evidence downloads. Old bearer tokens alone no longer authenticate.

Working Data's scoped JavaScript requests now include same-origin credentials;
its standalone Desk asset is not changed. New recovery actors and acceptance
actors are assigned from the signed-in account, not trusted from a form.
Historical free-text attributions remain historical; no prior record is rewritten.

## Recovery evidence, not a disk-execution panel

Backup & recovery starts with the owner's intended **14TB main source / 1.5TB
backup** labels and no confirmed serials, UUIDs or mount paths. Those labels are
not measurements. An admin records both physical identities, filesystem and
mount details, LVM membership, capacity and reserve floors from actual evidence.
A smaller backup cannot be assumed to cover all data on the larger drive: record
used bytes, selected coverage, exclusions and capacity requirements separately.

The seven review stages cover positive device identity; mount/capacity; drive and
filesystem health; original archive layout; database/snapshot and WAL/SHM/journal
completeness; backup coverage; and a separately approved disposable restore rehearsal.
Read-only command examples are **display/copy plans only**. Device-specific
placeholders are never filled by guessing. There is no subprocess, format,
restore, mount-change, service-enable or command-execution route in this module.

An observation records a real timestamp, steps, expectations, result, evidence
references/output, risks and the current storage-record revision. A PASS needs
positive identity and evidence; a capacity PASS also needs measured free space
above the declared reserve. These checks validate declarations, not the truth of
what an operator typed. Reviews are separate admin events; only the newest PASS
for the current storage revision can be accepted as evidence. A changed storage
identity invalidates the current gate projection but preserves all history.

The UI uses **REVIEWED EVIDENCE**, not an automatic VERIFIED-machine claim.
Operational authorization remains **HOLD**, including after all seven evidence
checks have been reviewed. Restoring or changing drives needs a separate exact
plan, explicit owner approval, target identity, backups and rollback evidence.
No actual backup, SMART check, filesystem repair or restore occurs on import/save.

## Records, backups and recovery of accounts

New local files below the private Studio root:

- `studio-accounts.sqlite3` — password hashes, account state, session representations,
  rate limits and bounded account audit history; **secret-bearing**.
- `.studio-accounts-required` — binds the account database identity. A missing
  initialized database or mismatched identity fails closed rather than reopening
  public owner signup.
- `studio-recovery.sqlite3` — separate append-only recovery observations and reviews.

Existing `intake.sqlite`, objects, `acceptance.sqlite3`, Working Data and Library
remain separate. Root/file ownership and restrictive permissions are checked for
the new stores; unexpected links/sidecars fail closed. Writes are transactional.
Recovery export is canonical JSON with a payload hash and no account secrets.
The original acceptance export remains available unchanged. Hash chains/digests
provide content consistency, not signatures or protection against an OS owner
who can rewrite the whole ledger.

Include the account database **and its identity marker** in an access-restricted,
consistent backup together with the relevant private Studio data and evidence.
Do not put the auth database, setup code or password hashes into GitHub, Drive,
Notion, a public receipt, a screenshot or an ordinary evidence export. Backups of
SQLite require a consistent snapshot procedure; copying a changing DB while
omitting its journal/WAL is not qualified. Record backup time, snapshot method,
coverage, exclusions and restore evidence. Account audit export is not a complete
credential backup, and the current UI displays only a bounded audit window.

For forgotten administrator access, use `studio-admin.sh password YOUR_ADMIN`
(see the quick start above). The original break-glass command remains available
and has no HTTP equivalent:

```sh
python3 -m tools.local_data.intake_studio.accounts --store /ABSOLUTE/PRIVATE/STUDIO_ROOT reset-admin --username YOUR_EXISTING_ADMIN
```

It prompts privately twice, resets only an existing admin, revokes every session
and records the reset. It neither deletes an inbox nor clears evidence holds.
Do not remove the account database/marker to reset a password. A missing or
corrupt database needs separately reviewed recovery from a qualified backup.

## Validation and remaining gates

Executed in a scoped source workspace using synthetic data:

- 84 account/recovery/gateway tests, including actual HTTP requests against the
  new gateway with an explicitly stubbed legacy data handler.
- 50 unchanged acceptance-module regression tests.
- One of the 84 tests exercises the production scrypt cost; most other account
  tests deliberately lower its cost in the test process only, to keep the suite
  bounded. Runtime configuration cannot request the test cost.
- Repository no-network environment mode: 55 passed and 29 explicitly skipped
  loopback-gateway tests; no failures. This is not the full repository no-network
  harness or `make local-data-check`.
- Python AST parsing, JavaScript syntax and static HTML checks.

These are not rendered Chrome tests, a full native Studio server run, independent
security acceptance, actual storage inspection, backup qualification or installed
machine verification. The unchanged backend is retained by Git blob identity,
not independently re-executed in this preparation environment.

Before approval: execute full `make local-data-check`; update any prior component
fixtures that assumed anonymous sessions **without weakening the new gateway**;
exercise the real facade with full native dependencies; verify old token denial,
all shared navigation/downloads, cookie expiry/revocation, role checks, setup and
break-glass procedures. Test desktop/mobile keyboard/scrolling, form failures,
reconnect/restart and no external requests. Check new account files are backed up
consistently, secrets stay out of exports and the observed source fingerprint
matches the reviewed candidate. A passing CI count alone cannot qualify these.

## Design basis and researched references

The original design is a private KFM operations workspace: forest/ivory identity,
a split first-owner/sign-in screen, task navigation, explicit environment and
signed-in identity, two drive cards, numbered recovery stages, and evidence
history that does not look like a disk-operation button. Empty states report
unknowns rather than fabricated telemetry. The existing Intake layout remains.

Reviewed official references on 2026-11-15:

- [Cockpit](https://cockpit-project.org/) — integrated task-oriented server
  navigation. KFM does not copy its system-user authentication or expose a terminal.
- [Kopia guide](https://kopia.io/docs/getting-started/) — distinguish storage,
  snapshots and policies. This module does not implement Kopia or its encryption,
  scheduling or backup engine.
- [OWASP password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
  — slow salted password hashing and the documented scrypt work factor where
  Argon2id is unavailable in the stdlib-only local runtime.
- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) — long
  passphrases, Unicode/paste support and password lifecycle guidance. This is not
  a claim of NIST assurance-level compliance, MFA, FIPS validation or certification.

No provider credentials, third-party UI source, paid service or cloud account
requirement is introduced. Visual rendering remains unverified.

## Rollback

This is a draft source change, not an installed or hosted change. Do not silently
install or restart it. Before merge, revise/close the draft. After an approved
installation, stop the protected service deliberately, preserve databases and
original files, and recover with a separately reviewed retained release.
**Do not run the old anonymous server against this private store as a rollback.**
Keep access disabled until the restored release enforces the approved boundary.
No disk, data layout, public Explorer, hosted Site or account-access policy was
changed by authoring this candidate.
