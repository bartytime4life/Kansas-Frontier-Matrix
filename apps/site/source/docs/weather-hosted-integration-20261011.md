# Governed weather hosted integration — October 11, 2026

This change starts from the same owner-private Explorer's deployed v250,
source cb03d2b8d7f42cdc17b6597ace0785629ee6bb3a, and takes only the weather
implementation and required shared interfaces from GitHub main
687ca2816c87a423f36188b5a0e6f7286bb7eb94. PRs 5035/5036/5037 are merged;
that fact does not establish hosted release availability or activation.

## Verified baseline and bounded change

Sites deployment appgdep_6acc31715fe08191be976aa9f690f08b succeeded for v250.
The current live DB has 15 user tables: all weather tables are absent, water
packages/active/events are empty, and daily_archive_captures contains 21 rows.
Weather read, status and release-page requests return 404 behind supported
private service access. Runtime revision 5 contains no KFM_WATER owner or
staging settings. These are session observations, not admission or approval.

Retain project appgprj_6aa0b1c41bc08191bfd86003920f1631, owner-only audience,
DB and BUCKET bindings, all migrations 0000–0005, existing data/assets,
Underground navigation, private-location behavior, layer request lifecycle,
overlay composition and pointer sampling. Copy no soil routes or 0007 migration.
Append only 0006_governed_weather.sql and its exact journal entry. Its three
CREATE TABLE IF NOT EXISTS statements neither modify water nor insert rows.
No R2 package is uploaded by this deployment.

Application consumers belong in the existing app root, component tests and
synthetic fixtures in tests, documentation in docs, and the additive schema in
drizzle. This is a MIRROR into the existing deployable, applying the accepted
Directory Rules docs/doctrine/directory-rules.md §§5,10,18 and ADR-0029/0045;
no parallel contract, policy, registry or release home is created. The supplied
Directory Rules.pdf was not present in this synced project's sources; current
canonical doctrine and its accepted-ADR redirect were checked directly.

## Validation and scope

The production build passes. TypeScript and changed-area lint pass. All 1,131
Node tests pass with no failures or skips, including mandatory Python license
and station-local offset comparisons against the pinned repository. Synthetic
SQLite tests execute the actual gate and read code: empty and staged packages
return ABSTAIN/NO_APPROVED_SNAPSHOT; a denied decision refuses activation and
stored denied metadata returns ABSTAIN/RELEASE_NOT_APPROVED, with no data or
evidence. Existing synthetic water metadata and object bytes remain identical.
The isolated built Worker answers 503/RELEASE_STORE_UNAVAILABLE before local
0006, and 200/ABSTAIN/NO_APPROVED_SNAPSHOT after it. Sign-in and same-origin
refusals remain enforced. Synthetic packages are never uploaded to the Site.

The two weather parity tests originally assumed a monorepo directory layout.
KFM_WEATHER_REPOSITORY_ROOT now explicitly selects the absolute verified checkout
for standalone test runs; tests remain mandatory and runtime policy is unchanged.
GitHub fixture regeneration reports PASS with no drift on Python 3.11.

## Owner steps after deployment, before any real activation

1. Confirm the same private project and deployed source/version. In Sites Settings,
   inspect DB for weather_packages, weather_active and weather_activation_events.
   All three must remain empty after migration. Verify the three read views return
   ABSTAIN/NO_APPROVED_SNAPSHOT and contain no data or evidence_refs.
2. In this Site's runtime settings, set KFM_WATER_OWNER_EMAILS to the verified owner
   email (or KFM_WATER_OWNER_IDS to the Site-specific authenticated user id, never
   the workspace account id). Set KFM_WATER_WORKER_TOKEN to an owner-held random
   secret of at least 32 characters. These settings serve both existing water and
   weather; do not replace a pre-existing list or rotate an existing secret.
   No such settings were present during this integration. Keep these values out
   of source, logs, browser code and documentation. This configuration does not
   approve a weather package. Obtain KFM_SITES_BYPASS_TOKEN through supported
   same-Site service access for the owner's private staging tool.
3. Use a verified KFM checkout and its normal Python dependency environment. For
   authoring tests in the standalone Site, export KFM_WEATHER_REPOSITORY_ROOT to
   that checkout's absolute path. For real capture use an owner-private external
   acquisition store, preserving the lifecycle; never use the Site Git tree or
   its DB/R2 as a RAW acquisition store.
4. When the owner decides to prepare a real package, run the following command
   with the two tokens held only in environment variables:

   python tools/release/weather_release.py cycle --root "$KFM_WEATHER_STORE" --owner @bartytime4life --valid-days 7 --site-url https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site

   This reads the existing hosted weather pointer, captures four admitted federal
   stations, validates and packages the 30-day PRCP/TMAX/TMIN window, writes an
   eligible weather-specific decision, then stages. It never activates. Provider
   transfer bounds are 16 MiB metadata plus four 8 MiB compressed station files
   (48 MiB total ceiling per cycle before expansion); the public layer is bounded
   to 360 observations. Review the store/capture and actual byte receipts before
   reuse. Choosing a 30-day layer does not imply 30-day-only station downloads.
5. Inspect the returned package_id, decision_path, immutable capture, provenance,
   rights/sensitivity, time validity, correction/rollback references and staging
   result (STAGED, activated:false). Confirm weather_active remains empty and
   all read views still abstain. Source admission and a generated decision are
   separate from the authenticated owner action.
6. Only after explicit package review/authorization, sign in as the configured
   owner at /governed/weather-release, paste that exact eligible weather decision,
   and select Activate package. Read back the pointer/revision/event and verify
   the map, station selection, evidence and export against the same package.
   Retain public access unchanged. A successful private release is not public
   publication, comprehensive browser acceptance or source/overlay review.

## Rollback

Before activation, restore saved private v250 through deploy_private_site_version
using exact version id
appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_36ba73695928819198be0932905afb73.
Preserve later source work before reverting application behavior. Leave additive
weather tables and migration history in place; do not drop tables, undo the
journal, repoint bindings, reset data or reseed. v250 ignores weather storage.
The separate source archive and Git bundle are recovery artifacts outside the
application tree, not deployment assets or governed data.

After real activation, withdraw or roll back the weather release through the
owner page first; verify data is withheld (or the intended previous approved
package is served) and retain all events/objects. Application rollback and data
release rollback are different operations. A failed deployment can still apply
0006: inspect the live schema before retrying, never assume migration rollback.

Hosted readback, saved-version identity, database preservation and browser
observations are recorded separately in the task's final reconciliation evidence.
This source document makes no claim that the combined integration is accepted.
