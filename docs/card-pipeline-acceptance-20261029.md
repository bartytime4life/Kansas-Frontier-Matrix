# Card pipeline implementation checkpoint — October 29, 2026

## Reconciled integration candidate

The candidate is reconciled onto hosted source `05bd00f2ca`, preserving newer
Flora, Fauna, aviation, civic/public-safety, earthquake and manual county-history
work. It maps the current 22 topic cards and six recipes, including every
category-map control. The older question guide is not reintroduced.

The candidate production build, TypeScript and changed-file lint passed.
Focused regression checks including the built HTTP routes: 126 passed, zero
failures, three skipped (two live-MySQL tests and one real county source packet).
The separate private-health candidate passes 59 Python tests after reconciliation
onto main. Installed-kit loading, earthquake behavior, outage recovery, source
approval/revocation, budget deferrals and connection-only guards are covered.
The local browser shows 22 welcome topics and six recipes, no horizontal
overflow, and publication setup-pending. This is local acceptance, not a hosted
deployment or real-MySQL acceptance claim.

Read-only PC checks at 22:32 Chicago on October 29 show both originally
configured sources complete with valid candidates, publication disabled,
connection-only mode, indexed intake and a matching working-backup/restore
checkpoint. Capture, analysis, working-backup and working-restore timers remain
scheduled. This integration work does not replace the running PC worker.

The following sections preserve the earlier installed-version checkpoint.
Its 45-card inventory and test totals describe that earlier version, not the
reconciled 28-card candidate. See the updated [implementation order](explorer-card-pipelines.md#reconciliation-with-the-current-repository).

## Earlier delivered local checkpoint

The registry maps 22 question cards, six map recipes and 17 welcome topics to
existing official context, specialty controls, calculated daylight, permitted
knowledge search and 17 explicitly proposed domain lanes. The generated
[dependency map](explorer-card-pipeline-map.md) is produced from that registry.
The new `/pipelines` view and read-only `/api/pipeline/v1/cards` route expose
coverage metadata; public source status reuses the existing release-serving gates.
Question drafts and source activation behavior remain unchanged.

The active `dev` user-level capture service now records actual attempt, capture
and completion clocks, validates candidates and writes the private operator
report. **KFM Working Data** and `kfm-data pipelines` show capture validation,
retry/exhaustion, storage, intake, backup and restore status. The private API
rejects anonymous requests and nonlocal origins; it is unavailable from the
catalog-only imported library. Both v1 and normalized v2 configurations retain
the same two implemented capture adapters. Publication remains false and
connection-only. All four original timers are active.

The scheduled 03:00 UTC October 30 run (22:00 October 29 in Chicago) completed
both source captures with valid candidates and populated the new clocks. This is
actual local scheduler/capture acceptance, not hosted publication acceptance.

## Existing candidate correction

A real-data check found USGS array qualifiers had been normalized to null entries.
The normalizer now preserves scalar/array qualifiers with finite bounds and
validates its entire output before completing a product. Read-only private health
checks validate the latest content-addressed candidate as well.

An offline audit found 156 invalid USGS candidates and 156 valid NWS candidates.
Under the existing shared operation lock, all 156 USGS candidates were rebuilt
from exact preserved raw bytes and matching immutable receipts. Originals and
old candidate bytes remain intact; correction receipts bind old/new product
hashes, raw hashes and the changed recipe. Only unpublished job pointers changed.
A subsequent audit found all 312 checkpoint candidates valid. New scheduled
captures also pass the validator. No source or publication approval was issued.

## Verification

- Production build, TypeScript check and changed-file lint passed.
- Focused JavaScript regression run: 79 passed; one live-MySQL integration check
  skipped because no test database was configured. Checks include built HTTP
  routes, metadata/source parity, disabled publication, authentication, approval
  expiry/revocation, partial/empty/stale states, job recovery, private revalidation
  and v2 configuration compatibility.
- Python intake/session/library/report checks: 59 passed.
- Browser checks verified 22/6/17 filters, specialty/index coverage, desktop
  rendering and a 390 px layout without horizontal overflow.
- A fresh working-store backup and full restore test passed for 1,278 files.
  Restore inventory matches the latest backup inventory. Later hourly captures
  remain subject to the normal backup schedule; this is a checkpoint, not a
  claim that future captures are already backed up.
- Active capture, backup and restore services returned success; timers resumed.
  Existing unrelated working-tree edits and original data were preserved, with
  local implementation recovery snapshots outside both Git/public trees.

## Remaining plan work and acceptance gates

This completes shared infrastructure, card mapping and local operating-health
integration. The broader plan is not fully implemented or accepted:

- Proposed domain lanes still need exact product qualification, source-specific
  adapters/validators and source/rights/sensitivity review before activation.
- Signed profiles, verified hosted storage/SQL, actual GoDaddy deployment and
  hosted activation/withdrawal/rollback acceptance remain pending. The
  [USGS/NWS review packet](pipeline-source-review.md) contains concrete private
  candidate hashes and the current recipe digest. It is unsigned.
- The preserved imported archive still needs a full-size independent backup;
  the smaller working-backup SSD does not establish that coverage.
- Reboot acceptance has not been exercised. Do it at the PC with recovery access
  and after preserving any unsaved work.

The test PC, inference services, DNS and preserved Sites application have no new
production role or configuration change. See [operations](explorer-card-pipelines.md)
for commands, source gates and offline correction behavior.
