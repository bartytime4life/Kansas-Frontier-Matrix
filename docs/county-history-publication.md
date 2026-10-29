# Historical counties: approved-context publication and map integration

Status, October 29, 2026: **implementation candidate; operational activation unperformed**. This completes the code path from checked county reports through the existing signed publication API to Government & civic's map controls. It does not claim a live county release, canonical source admission, production deployment or browser acceptance.

## Implemented behavior

The Government & civic dock offers reviewed historical-county snapshots. It reads only committed, currently approved releases from the existing `/api/curated/newberry-county-history` and history interfaces. The existing map renderer draws the source polygons and a distinct county-outline key, keeps selection through style recovery, and provides a keyboard list of up to 107 source areas. Selected records show the source name/type, exact day, validity interval, optional FIPS, original change/citation, source link and release download.

A **Set map to YYYY-MM-DD** button uses the existing calendar-seek path. Historical effective dates are separate from preparation and publication times. A county snapshot draws only on its exact day with a current build and unexpired approval; other days and Return to Present hide it. Available releases are ordered by their historical day, with publication time distinguishing editions. Selecting a stored snapshot seeks its date. County autoplay is disabled: missing dates are never manufactured. The history interface currently lists at most 20 releases, not every date in the source archive.

The initial real-data test is **1861-01-29: 50 mapped source areas**. That is not a count of organized Kansas counties. The archive includes predecessor and non-county jurisdictions outside today's Kansas; these extents, missing FIPS/state and unreviewed source classifications are retained. Dates **1873-03-20 through 1874-03-17** remain withheld because of the documented disputed coverage. There is no post-2000 continuation.

## Processing and release boundary

`server/county-history-candidate.mjs` remains private operator tooling. Its new `normalizeCountyCandidate()` converts a checked WORK packet into a bounded external-context **product candidate**, dropping WORK identities, internal bundle/status fields, aliases and events from the map product. Public reads do not import or call the private report reader. `server/county-history-release.mjs` owns the public transport validator: source/archive identity, source record locators, optional attributes, exact dates, geometry budgets and the declared EPSG:1188 operation. The byte hash binds the resulting JavaScript representation; the earlier Python report hash remains a separate provenance reference.

No projection function grants publication authority. The existing pipeline still requires a real owner Ed25519 delegation, authenticated worker transfer, current recipe, rights/sensitivity/review references, immutable chunks, integrity verification, CAS activation and an additive source-head row. Public reads/downloads/history recheck approval, expiry, revocation, committed state and payload integrity. Product data remains `EXTERNAL_CONTEXT_ONLY` / `evidenceEligible:false`, rather than admitted KFM EvidenceBundles. GEOS topology results remain in the checked report; the transport validators do not claim to repeat GEOS or verify every cited statute.

The registered-source reference, rights/sensitivity/review decisions and owner signing authority must be resolved through the existing governance process. The source-registry README inspected this session records a HOLD on guessing canonical child-record paths/writers. This patch therefore creates no parallel descriptor, fabricated canonical reference, approval key or registry writer. `newberry-county-history` is the hosted transport selector, not proof of canonical admission.

## Concrete operator commands

Run from the exact reviewed checkout. The report digest below is only for the previously qualified statehood report; a different date requires its own checked report and separately recorded digest.

```sh
python3 scripts/qualify-county-geometry.py /absolute/path/KS_AtlasHCB.zip --date 1861-01-29
node scripts/pc-pipeline/cli.mjs prepare-county /absolute/path/report.json 3e9da16b1379239e6f231e58ad6e2167bb1f7b6b627fcb349ce13133b644ed6a
node scripts/pc-pipeline/cli.mjs profile-template newberry-county-history
node scripts/migrate-pipeline.mjs
```

`prepare-county` is local-only and returns `candidate-only` / `releaseEligible:false`; it does not acquire data, sign, access production keys, write SQL or publish. Profile templates deliberately retain `REVIEW_REQUIRED` and blank governance references. Generated templates were inspected, but no operational approval was signed. A template or a passing test is insufficient release authority.

After the operational checks and explicit approval below, the existing owner/worker process can use:

```sh
node scripts/pc-pipeline/cli.mjs publish-county /absolute/path/approved-config.json /absolute/path/report.json 3e9da16b1379239e6f231e58ad6e2167bb1f7b6b627fcb349ce13133b644ed6a
```

This manual command requires qualified storage, the existing worker credential and a valid signed county profile. It uses the existing stage/chunk/commit/readback protocol and writes a publication receipt only after confirmed commit. It does not add counties to the hourly acquisition schedule or change PC source/priority settings.

## Required cutover before deployment or publication

This patch changes the shared signed recipe. **Deployment requires coordinated replacement approvals for configured publishers.** Every configured source that publishes under that recipe needs a reviewed replacement delegation; do not assume that only streamflow and alerts are configured. Existing committed snapshots can remain readable under their stored signed recipes while their other approval/integrity gates hold, but new old-recipe publications are refused.

| Identity | SHA-256 |
| --- | --- |
| Previous recipe | `e8b85ea8ff6414e9dc46030835d2102ce7439cf7811615512b422b2386d5fab3` |
| County integration recipe | `fb8f071a9172493daf46322eb64dd227cf0ba52ce385b72f183d5660dd5526a3` |
| Reviewed additive SQL | `595fe8153ac7e0d1473d959681d9958b8ef4edc5b1c63140ea9d33463b03e9b4` |

The recipe now includes the two county adapter/validator files as well as the three previous inputs. Recompute all identities if any recipe input changes. The SQL change only adds the county head to the existing `INSERT IGNORE`; it preserves table definitions, releases, existing heads and control state. Reapplying SQL does not pause an existing worker.

1. Review the exact source and county source/rights/sensitivity/interpretation limits. Resolve actual canonical governance references; do not invent identifiers or reuse an unrelated review as county approval.
2. Inventory actual installed/deployed recipe identities, configured sources, signed profiles/expiry and active heads. Operational state is UNKNOWN here. Preserve the current journal, settings, artifacts, approvals and unrelated records.
3. Prepare replacement profiles for every configured source from the exact target checkout. Use the existing owner signing process and original owner key; never move its private key to the unattended worker or hosting. Coordinate an authorized pause/cutover where needed. Existing immutable transfer manifests retain their old profiles; do not edit them or reset retry history.
4. Obtain an independently recoverable shared-DB backup and test restore. Rehearse the additive SQL on a compatible disposable copy, comparing old heads/revisions/control state and unrelated records. Only then apply the exact approved SQL through the existing migration command's digest/backup/TLS gates. No migration was applied in this session.
5. Match the installed kit, server build and signed delegations to the reviewed recipe, preserving existing service configuration. Verify continued old-feed publication before activating counties. The profile's two-hour window applies to product preparation for commit; historical boundary age is not misreported as fresh measurement data.
6. Publish one reviewed county snapshot through the explicit manual command. Verify the committed read/download hashes, effective day, source locators, expiry/withdrawal behavior and the desktop/mobile map. Test Set map to date, another day, Return to Present, source inspection and style recovery before broader county publication.

The prior [publication cutover procedure](second-pc-pipeline.md) remains applicable. Tests with ephemeral fixture signatures do not substitute for real approvals or operational readback.

## Validation, limits and rollback

The actual pinned statehood report was regenerated and matched SHA-256 `3e9da16b1379239e6f231e58ad6e2167bb1f7b6b627fcb349ce13133b644ed6a`. A fixed preparation time of `2026-10-29T17:00:00.000Z` produces a 636,212-byte canonical product with SHA-256 `5af667e63a250c615a5e550d93d90391445f5c72d94e04f06c1664e16c312e99`. Its 50 coordinate arrays and citations were compared with the checked private input; live publication preparation time is newly recorded, not silently reused from this fixture.

The regression exercises normalized real geometry, temporary Ed25519 approvals, authenticated transfer, immutable chunk assembly, commit/read/history/download and client date gates using a test-only memory store. It also covers unsigned/wrong-recipe/expired/revoked/corrupted/withdrawn records, quarantine dates, preparation-time limits, WORK rejection, source-card fields and keyboard/date controls. The old-to-new recipe test uses the actual previous recipe and proves rejection without losing an existing synthetic NWS head. These are real code paths with fixture authority; no production key, SQL, service or release was used.

Production build and typecheck passed. The focused pipeline/reviewed-snapshot tests passed, and ESLint reported no errors. The existing installed-kit subprocess test fails before useful child output in this environment; earlier sessions reproduced that failure on base and head. A fresh native browser attempt was blocked at server startup with `listen EPERM` on `127.0.0.1:4186`; browser rendering, mobile/performance acceptance and live activation are not established. No alternate listener or policy bypass was attempted.

Placement follows accepted Directory Rules v2/ADR-0029: hosted `server/` processing/validation, existing SQL/PC tooling, `app/` presentation, `tests/` verification and `docs/` explanation. No canonical contract, registry, policy or release home was duplicated. The standalone GoDaddy composition and preserved Sites bindings remain separate.

Before activation, rollback is a revert of this patch; no persistent migration has occurred. After a later authorized activation, use existing signed withdraw/rollback controls and the matching reviewed recipe/profile set. Preserve the additive head row, SQL tables, source captures, receipts and immutable artifacts; do not delete data or bypass current rights/approval checks to make old code run.

Validation base: hosted `01a2330bc280dde590a58deedd3ca437c5850e96`, tree `db49fca3f504c66ae54a8720b27b0cb38264ab14`. The intervening flood-date/chart changes overlap two presentation files; they were retained through a three-way merge and the flood tests were included in repeat validation. Eight new integration tests passed with the real-report case enabled; eight focused test files passed. The changed-area lint run had zero errors and 45 warnings; the page retained exactly its baseline 42 diagnostic messages, with no new page diagnostics.
