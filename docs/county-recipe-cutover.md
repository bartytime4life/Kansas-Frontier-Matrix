# County recipe cutover reconciliation — October 29, 2026

**Source qualified; operational cutover held.** This record supplements
[county publication](county-history-publication.md) and the
[second-PC procedure](second-pc-pipeline.md). It is not an owner delegation.

## Exact source and prior work

Inspected hosted commit: `ec9104adfe22cab6f5806fd3270a1096bf66972d`.
PR #5577 merged as `c8b8838c526afa60318c4c916386e8e5166a6d6f`.
Earlier earthquake qualification PR #5548 is **already merged** as
`96f60dc22e9c440a635eac7c31999fedaa75764a`; retain its regression tests and
operator corrections. Its evidence recorded operational signing, DB migration,
service/config changes and live continuity as unperformed/unknown. Neither
that report nor this source checkout proves their present installed state.

| Identity | SHA-256 |
| --- | --- |
| Previous earthquake-era recipe | `e8b85ea8ff6414e9dc46030835d2102ce7439cf7811615512b422b2386d5fab3` |
| Recomputed target recipe | `fb8f071a9172493daf46322eb64dd227cf0ba52ce385b72f183d5660dd5526a3` |
| Previous SQL | `5c5049c2c1a9c932b928c96bdb2195114f0e7a8f2df84b6c6f38b61597c254f5` |
| Target SQL | `595fe8153ac7e0d1473d959681d9958b8ef4edc5b1c63140ea9d33463b03e9b4` |

`recipeDigest()` hashes the canonical ordered name/SHA-256 pairs for
`pipeline-contract.mjs`, `pipeline-normalize.mjs`, `ingestion-sources.mjs`,
`county-history-candidate.mjs` and `county-history-release.mjs`. These five
files were copied with Git blob identity verification. This qualification
changes no recipe input, runtime publisher or migration SQL.

## Approval replacement scope

| Transport source | Producer path | Delegation role | Required action if actually publishing |
| --- | --- | --- | --- |
| `usgs-streamflow` | Hourly worker when configured | `external-context` | Replace any older-recipe delegation |
| `nws-alerts` | Hourly worker when configured | `external-context` | Replace any older-recipe delegation |
| `usgs-earthquakes` | Hourly worker, explicit opt-in | `external-context` | Replace any older-recipe delegation; do not add it merely for this cutover |
| `water` | Manual `stage-package` | `governed-package` | Replace transport delegation if used; retain separate domain evidence/serving decisions |
| `weather` | Manual `stage-package` | `governed-package` | Replace transport delegation if used; retain separate domain evidence/serving decisions |
| `newberry-county-history` | Manual `publish-county` | `external-context` | New real source/rights/review authority and target delegation before first release |

This is the complete current transport allowlist, not an inventory of installed
publishers. Source-head rows and available CLI templates do not prove activation.
The hourly config still accepts at most three sources, only the three feed IDs.
Do not add county, water or weather to that list. The separate hosted ingestion
archive is not itself a signed publication producer; do not enable it to perform
this cutover. Any other actual producer using this API must use a registered
selector and be included in the operational inventory.

Precisely replace profiles whose source is in use and whose signed
`recipeSha256` differs from the target, plus expired/revoked/otherwise invalid
target profiles. Already valid target delegations need no redundant renewal.
Never edit a signed recipe field in place. A transport recipe change alone does
not require recreating an unchanged domain release decision; validate its actual
rights, integrity, expiry and serving gates separately.

## Deterministic behavioral qualification

`tests/pipeline-county-cutover.test.mjs` fixes the receipt clock and uses a
public test-only Ed25519 seed. It exercises the actual previous digest against
all five prior sources: `RECIPE_CHANGED` for an old transfer with its matching
old delegation, `APPROVAL_INVALID` for a target transfer with an old delegation,
and refusal of signature forgery. Release records and heads remain unchanged.

All six selectors admit a source-specific valid target delegation at staging;
staging is not content admission. Governed water/weather still require the
existing domain validator at commit and read. The three feed types additionally
traverse normalization, signed stage/chunk/commit/readback and public downloads.
Old committed fixture downloads remain byte-identical after a replacement head
is published. Revoked and expired profiles remain refused. Fixture authority
does not establish owner approval or live provider/DB health.

Focused local run: **46 passed**, including the prior cutover, PC worker,
earthquake, installed-kit subprocess and three new deterministic cases. A
separate domain test could not load the missing TypeScript dependency in this
reduced snapshot; it is not counted as passing. No local full build was run.

## Database backup, migration and restoration rehearsal

The pinned pre-county schema fixture is copied from PR #5577's parent
`01a2330bc280dde590a58deedd3ca437c5850e96`; its blob and SHA-256 match the
merged earthquake-era schema. SQL comparison shows only the county head added
to `INSERT IGNORE`. Table definitions and old head rows are unchanged.

The new opt-in MySQL test uses the existing CI **MySQL 8.4.13** service,
loopback port and fixed disposable credentials. The workflow supplies only its
service container ID. With both active and paused control states, it:

1. Creates the old schema, five populated heads with revisions/previous IDs,
   committed/withdrawn release rows, events, nonce, heartbeat and unrelated data.
2. Uses the service's real `mysqldump --single-transaction --skip-lock-tables
   --no-tablespaces --set-gtid-purged=OFF --hex-blob` and restores into a separate
   empty disposable database using `mysql`.
3. Compares every fixture table's DDL and all rows before applying target SQL.
4. Applies target SQL twice; requires exactly one empty county head, with every
   old record, revision and pause state preserved.
5. Dumps the migrated database and restores into a third empty database;
   compares all table definitions and rows again and emits backup/SQL digests.

This is a compatible fixture rehearsal, not a backup of hosting. It does not
qualify hosting grants, TLS, quotas, triggers/routines or external artifacts.
The local executor has no MySQL server/client or Docker; package setup failed
under its system permissions. Therefore local SQL/restore execution is **not
qualified**; inspect the new exact-head CI result before operational work.
The test deliberately skips unless both disposable-DB opt-ins are present.

For production, independently back up the actual shared DB and restore to an
isolated compatible destination; inventory its extra objects and use appropriate
backup options for them. Preserve the worker journal, raw captures, artifact
chunks, config and receipts with their independent recovery manifests. A database
dump alone cannot restore those files. Never restore a fixture or blindly import
a pre-cutover dump over shared production. Reapplying SQL does not pause an
existing system, and MySQL DDL is not transactionally reversible.

## Operational evidence and dependency order

No attached managed-environment status capability, installed `/etc/kfm-pipeline`,
`/opt/kfm-pipeline`, `/srv/kfm-data`, operational DB variables or signed profiles
were available in this executor. Available GoDaddy tools expose domain functions,
not app runtime/configuration. Integration discovery did not expose a usable
hosting operation. Public status and three curated feed endpoints were
inaccessible to the web reader; no outage or configuration inference follows.
Private key files were not searched or read. No operational change was made.

1. On the actual hosts, record installed kit, signing checkout and deployed
   server commit/recipe; current heads/revisions, receipts, schema, control state,
   scheduler ownership, configured feed source/priority lists and manual package
   producers. Public status alone does not enumerate manual publishers or prove
   profile validity. The CLI `inventory` command also reports `configured:false`
   generically; it is not an installed-config audit.
2. For every used source, record profile ID, source, recipe, validity/expiry,
   revocation state, role and real governance references; verify signatures with
   the actual trusted public key. Compare against the matrix above. If this
   target is already installed and approved, preserve it and verify continuity.
3. Resolve policy changes, then use `profile-template SOURCE` and the existing
   `approve PROFILE ORIGINAL_KEY OUTPUT` process on the authorized signing PC.
   Keep the private key there. Transfer signed profiles only to the worker;
   retain prior profiles and all immutable transfers/receipts. Never run `keys`
   to replace trust as a renewal shortcut.
4. Obtain an independently recoverable backup and completed compatible restore
   rehearsal. Under authorized maintenance controls, apply only missing additive
   SQL via the existing exact-digest, verified-backup and verified-TLS gates.
   The migration process needs its own enabled flag; this does not authorize
   enabling Preview or starting a publisher. If the head already exists, verify
   schema/data instead of claiming another migration is needed.
5. Coordinate the authorized pause, matching server/worker target builds and
   new profiles before resuming the previously configured producers. Preserve
   source/priority settings and credential ownership. Old immutable jobs retain
   old approvals; allow eligible new jobs to use renewed profiles. Do not reset
   retries, delete journals or rewrite transfer manifests.
6. Require one new committed release, receipt, payload hash and governed readback
   per actual producer, followed by a subsequent scheduled update for continuing
   feeds. Inspect source timestamps, partial/stale state, expiry and head CAS.
   A readable old snapshot is not proof of continuing publication.

## Exact remaining gate for one historical-county release

Only after existing-feed continuity is demonstrated: resolve the county source
registration and actual rights/sensitivity/interpretation references through the
existing governance process (registry writer/path HOLD remains unresolved here).
Obtain the real owner-signed county target delegation, verify qualified storage,
worker credential, deployed/installed recipe parity and additive head availability,
and explicitly authorize the manual release.

Regenerate/check the `1861-01-29` report with digest
`3e9da16b1379239e6f231e58ad6e2167bb1f7b6b627fcb349ce13133b644ed6a`.
It represents **50 historical archive areas**, not necessarily 50 organized
Kansas counties. Preserve predecessor extents, citations and missing attributes;
exclude disputed dates `1873-03-20` through `1874-03-17`. Prepare within the
two-hour commit window, then use the documented `publish-county` command.
Historical boundary age is separate from preparation freshness.

Verify the immutable release/receipt and download hashes, source locators, exact
effective day, expiry/revocation/withdrawal, desktop/mobile rendering, Set map to
date, another day, Return to Present and style recovery. Do not put county history
on the hourly schedule. This session did not regenerate the private report,
publish a historical release or establish native-browser acceptance.

Rollback preserves additive SQL rows, release history, raw data, chunks and
receipts. Use existing owner-signed pause/withdraw/rollback controls with their
normal approval/integrity gates and the matching reviewed build/profile set.
Code rollback cannot authorize obsolete profiles for new transfers.
