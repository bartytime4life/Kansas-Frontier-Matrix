<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/kfm-reconciliation-20261010
title: KFM Site v213, local installation and repository reconciliation
type: report
version: v1.0-draft
status: draft; deployed-owner-private; repository-review-pending
owners: ["@bartytime4life via CODEOWNERS"]
created: 2026-10-10
updated: 2026-10-10
policy_label: repository-facing
owning_root: docs/
responsibility: Record the source reconciliation, executed validation, recovery and remaining review boundaries.
truth_posture: CONFIRMED observations are scoped below; code delivery does not approve data or mirror review.
related:
  - docs/reports/kfm-synchronization-20261009.md
  - docs/runbooks/water-pilot.md
  - apps/site/source/docs/governed-water.md
  - data/receipts/generated/site-v213-reconciliation-20261010.json
[/KFM_META_BLOCK_V2] -->

# Explorer reconciliation — 2026-10-10

The owner-private Site and local installation now share the tested source and build.
This authored observation record follows the existing synchronization report;
it creates no generated-report writer or release authority. Directory Rules and
ADR-0029 place application behavior in `apps/site/source`, canonical local tooling
in `tools/local_data`, and candidate comparison receipts in `data/receipts/generated`.

## Identities and retained work

| Surface | Observed identity |
|---|---|
| Repository base and clean primary PC `main` | `631e8f6a93d1fdf053bedbd980b4bd7a5b77748c`, including merged #5013 |
| Authoritative starting Site | v212, `5a8478e93d6d3a4e859f0da9efe1ec892facc0f9` |
| Combined Site | v213, `9d5578e53ff9930e72947f72f1ee504e6ae218af` |
| Confirmed private deployment | `appgdep_6aca9989773881919fdad08fd3905124`, succeeded; environment revision 5 |
| Audience | Existing owner-only access preserved |
| Local alias | `~/Projects/KFM-Explorer-Site-current` → `KFM-Explorer-Site-reconciled-20261010-v213` |
| Previous installation | `KFM-Explorer-Site-cache-budget-20261009-v4`, preserved |
| Existing state | `KFM-Explorer-Site-v109/.wrangler/local-state`, retained at its original path |
| Recovery directory | `~/Projects/KFM-sync-recovery-20261010T2002` |

Reconciliation compared the Site and repository against shared v192 source
`424e62cd429ba3ea13a109e6e37953eea857857f`. The local-only delta was compared
against its recorded repository base `8d6cbcd279372b240b8e7ab326635bf60d8884ab`.
Three separate source archives and the local source manifest were preserved.
The original local manifest was rechecked before installation; no concurrent
local edit was overwritten. Other worktrees and synced project sources were untouched.

The combined source retains the Site's direct Crop-CASMA preview and aquifer/cutaway
repairs, repository water-flow, terrain, night-sky and owner-water administration
changes, and local-only Atlas/cache-budget controls. Local Atlas remains available
from the compact Map menu and Advanced tools. Download workspace integration,
Earth Engine inventory controls and the established compact HUD remain present.
No model or companion service was started, restarted or reconfigured.

The [candidate receipt](../../data/receipts/generated/site-v213-reconciliation-20261010.json)
accounts for 923 tracked Site paths: 921 byte-identical mirrored paths and two
canonical local-tool mappings. The basemap-cache script matches exactly; its test
only changes the import path to the repository's canonical tool home. No unexpected
mirror deletion or unexplained difference remains. Inventory digest:
`ed093291ffe37e0ebe2ef0376a797f89710134f20451273b798aa6962cc274aa`.

The selected v192 receipt in `tools/qa/site_mirror.py` remains unchanged. Main's
content-parity check passed before this change. The new candidate intentionally
requires reconciliation review; a resulting `MIRROR_REVIEW_REQUIRED` is attributable
to this candidate, not an inherited failure. The v213 receipt does not record human
approval, select itself, establish hosted equivalence, or authorize data release.

## Executed validation

- TypeScript type checking and production build passed.
- Focused tests: 81 passed. Full Site suite: 985 passed, zero failed or skipped.
- `git diff --check` passed. Installation checksums match all 923 source files and
  all 426 build files; the dependency lock stayed unchanged.
- A bounded live 3DHP route probe returned HTTP 200 in 1.602 seconds with 400
  reaches and explicit `truncated: true`; this is one probe, not a benchmark.
- Browser smoke on the isolated preview rendered station dots and directed channel
  geometry. The flow panel reported 3,497 reaches, two with gauge cues, and incomplete
  area coverage. Directional animation is not measured water velocity and does not
  establish that every mapped channel currently contains water.
- The final port-4173 browser rendered the map and connected Local Atlas to the
  existing PRISM catalog. The observed browser error log was empty. Startup and
  automation interactions sometimes took several seconds; sustained performance,
  low-resource devices, mobile/touch and complete accessibility remain unverified.
- The local Site alone was stopped while copying its existing store: 18,429 files,
  918,716,718 bytes, with matching SHA-256 inventories. Candidate startup, rollback
  to the previous application, and return to the candidate each returned HTTP 200.
  This rehearsed application rollback; no data package activation or data rollback
  was performed. Hosted application rollback was not executed.

The Site documentation correction followed the frozen security snapshot and did
not change build inputs. Full tests/build were not repeated for that prose-only edit.

## Security disposition

Codex Security diff scan `8cc59242-fea4-49c3-bf55-382012bc5474` completed against
v212 plus frozen reconciliation snapshot
`9272702ba11ac175de2dd6580b1497e77577a903211a2e60f487ff61c5efb86b`.
All 57 changed source files were reviewed; zero confirmed new findings were retained.
The scan is a diff review, not a full audit of unchanged Site code. Hosted identity
header enforcement, external Atlas/download server enforcement and actual macOS
installer execution were outside its verified scope.

A fresh audit reports eight high dependency chains rooted in `braces@3.0.3`
([GHSA-vfj7-8cjw-p6xm](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm)).
There is no patched version in the inspected advisory. The recursive expansion
risk is present in development tooling; reviewed application paths do not supply
untrusted glob patterns, and Vite disables globbing for its watcher. Hosted Worker
request reachability was not established. This remains an inherited dependency
risk, not a clean audit or eight separately confirmed application vulnerabilities.
An incompatible ESLint downgrade was not applied. Older successful CI audits do
not supersede this fresh result.

## Recovery and next review

For application recovery, stop only `kfm-explorer-local.service`, atomically
repoint `KFM-Explorer-Site-current` to the preserved previous installation and start
that service. The existing data store stays in place. `installation.json`,
`state-backup-digests.json` and `switch-receipt.json` in the recovery directory
identify exact files and verification. Do not restore an older data snapshot over
new work without separately assessing subsequent writes.

The previous hosted version is v212. A hosted rollback would use that saved
version through the private Sites operation, preserving audience and storage.
Source admission, approved water package creation, configured hosted owner/token
settings, staging, review, activation, withdrawal and publication of data remain
separate operations. No new water acquisition schedule or operational service
was installed by this reconciliation.

Next: review the exact candidate and receipt, resolve the selected mirror checkpoint
through its review process, monitor a compatible dependency fix, and measure map
startup/interaction performance against a fixed device/view baseline. The repository
changes remain a draft until independently reviewed and merged.
