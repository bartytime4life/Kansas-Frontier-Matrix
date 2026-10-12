<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/kfm-projects-consolidation
title: Workstation inventory and reversible KFM consolidation
type: runbook
version: v1.0
status: draft; operator implemented; host migration incomplete
owners: ["@bartytime4life"]
created: 2026-10-11
updated: 2026-10-11
policy_label: public-documentation
owning_root: docs/
responsibility: Explain bounded folder inventory, explicit verified copies, discovery limits and independent storage boundaries.
truth_posture: NEEDS VERIFICATION
[/KFM_META_BLOCK_V2] -->

# Inventory and consolidate workstation folders

Start with every directory beneath the selected Projects directory, including
folders with unrelated names. The operator assigns each an explicit disposition
and recognizes KFM name/remotes, the canonical checkout, and the initialized
external store. These are discovery signals, not proof that every file belongs
to KFM. Confirm purpose, rights and consumers before selecting a copy.

`tools/local_data/consolidate.py inventory` records exact regular-file sizes at
their observation times, counts hidden/runtime/dependency files, reports links
without following them, and reads Git identity without refreshing indexes or
running configured filesystem monitors/hooks. Limits or directory changes mark
the result incomplete. This is metadata inspection, not content integrity or a
globally atomic snapshot. It does not establish that a folder is inactive.

Keep the full inventory private: filenames, Git status and source locators can
be sensitive. Record only a safe summary in public review artifacts.

## Responsibilities and placement

Accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and
[Directory Rules](../doctrine/directory-rules.md) route the operator to `tools/`,
its tests to `tests/`, and this procedure to `docs/`. DIR-EXEC-007 owns repository
operators; DIR-STORAGE-001 separates logical authority from physical bytes;
DIR-STORAGE-003 protects restricted bytes; section 13.4 preserves identity across
path changes. No new canonical source, schema, registry or release home is made.

Reconcile verified code differences into the existing owning source root.
Rebuildable executable distributions may use the existing `artifacts/build/`
lane with explicit ignore policy; that lane cannot hold trust-bearing data,
receipts, rollback decisions or source-evidence archives. Git checkouts retain
their distinct identity and need supported Git/worktree migration. An archived
receipt remains in its governed evidence store, not beside build output.

The current local-data importer rejects stores inside, equal to, or containing
the checkout. Selecting the canonical repository as the desired organization
center does not authorize bypassing that guard. Keep source bytes and lifecycle
stores external until a separately reviewed storage-boundary migration resolves
the conflict. Canonical manifests can reference the external store.

## Inspect and prepare an explicit copy

Use literal absolute paths. Save plans and receipts outside both source and
destination trees. Supply active paths from a fresh service/process readback;
service definitions alone do not prove that a writer is currently running.

```bash
python3 tools/local_data/consolidate.py inventory \
  --projects /absolute/projects --repository /absolute/projects/kfm \
  --active-path /absolute/current-service-source \
  --output /private/operator-records/inventory.json
python3 tools/local_data/consolidate.py plan \
  --source /absolute/selected-source \
  --destination /absolute/approved-parent/absent-copy \
  --allowed-root /absolute/approved-parent \
  --repository /absolute/projects/kfm \
  --owning-root tools/ --placement-basis 'recorded responsibility decision' \
  --max-bytes 10000000 --output /private/operator-records/copy-plan.json
python3 tools/local_data/consolidate.py copy \
  --plan /private/operator-records/copy-plan.json \
  --receipts /private/operator-records/copy-receipts
python3 tools/local_data/consolidate.py verify \
  --plan /private/operator-records/copy-plan.json
```

Planning hashes each regular file and rejects Git metadata, runtime/credential
trees, links, special files, overlaps, existing destinations and byte overflow.
The plan records ownership and placement rationale; those strings are operator
inputs, not policy approval. Applying never executes source scripts or deletes
originals. Copies are private and preserve owner executable bits.

Interrupted copies can resume only against the same plan marker. Existing files
must already match their planned digest; they are never overwritten. Verification
checks source/destination hashes, source metadata, and exact destination members.
Immutable attempt/success receipts remain distinct. A verified copy has no
effect on source admission, release, consumers or publication.

Consumer switches require a separate, exact before/after configuration record,
active-writer check, state-preservation verification and rollback test. The
operator intentionally leaves consumers on the original path: rollback before a
switch needs no data change. It is not a defense against a hostile process
concurrently replacing directory ancestors in caller-owned trees; do not run
copies into shared/writable untrusted ancestry.

## Let intake cover the actual holdings

The default intake discovery ceiling remains 200,000 candidates. Select a larger
bounded ceiling explicitly when the inventory requires it:

```bash
python3 tools/local_data/intake.py --root /private/external-store analyze \
  --max-files 3000000
python3 tools/local_data/intake_service.py --root /private/external-store \
  --max-files 3000000
```

The allowed range is 1 through 5,000,000. The selected ceiling appears in run
summaries and service status and is unrelated to local byte/cache budgets.
Exceeding it remains a failed scan, not complete coverage. A complete scan is
required to upgrade legacy quarantine bindings; unknown rights stay held.

Transient transfers and SQLite sidecars are skipped. A database with writer
sidecars is not profiled as an immutable source. PRISM completed rows need a
transactional reader. Acquiring the intake writer lock can mark abandoned
`running` rows interrupted; a state row alone cannot prove a live writer.

The guarded service includes the existing local atlas endpoints, PRISM completed
frame grouping, private vector/raster previews and extent pagination. Their
read-only intake surfaces share the legacy source-binding reanalysis hold.
Preview results keep review holds and unknown units; they grant no admission,
evidence, release or publication authority. Optional spatial workers use the
operator-selected trusted Python, resource/time limits, offline projection grids,
bounded archive members and driver restrictions. They never run source scripts.

## GitHub budget versus local capacity

The owner ceiling is **100,000,000,000 bytes across GitHub-hosted KFM material**,
including repository history/Site source, release assets and recorded CI storage.
Local PC holdings may exceed it. The existing 20 GB code/interface reserve remains
conservative headroom; it is not additional permission to exceed the total cap.
No paid LFS acquisition or billing change is authorized.

The ledger includes all release metadata assets, not only archives. Its baseline
check compares the separate data-archive portion with the preserved baseline
manifest. GitHub repository `size` is provider-reported and approximate; caches
and CI artifacts are mutable snapshots. Reconcile fresh totals before uploads
and include any LFS objects if used; absence in the current checkout does not
prove absence from historical/account storage.

GitHub's [repository limits](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits)
recommend a 10 GB compressed Git repository and enforce a 2 GB push limit.
[Ordinary file limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
block files over 100 MiB. [Release assets](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
have their own limits. The owner's 100 GB ceiling is not a blanket GitHub
open-source repository quota and does not make large Git blobs appropriate.

## Validation and open work

```bash
python3 -m unittest tests.local_data.test_consolidate \
  tests.local_data.test_intake_limits tests.local_data.test_intake \
  tests.local_data.test_atlas -v
```

These tests cover limits, source/destination changes, interrupted copies, resume,
collisions, links/special files, traversal, digest closure, original retention,
source-bound quarantine review, transient files and interrupted intake jobs.
They do not prove every workstation folder is safe to move or that a full live
scan completed. Host consolidation, rollback after service switches, full
collection curation, new web acquisition, GitHub distribution and browser
acceptance must retain their own evidence.
