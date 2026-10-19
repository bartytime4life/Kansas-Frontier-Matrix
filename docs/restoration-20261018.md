# Explorer restoration — 2026-10-18

## Status and source identity

This is a bounded source reconciliation for GoDaddy Node app `q9r9beo47t`,
prepared at the owner's request to recover missing visual and programming work.
It is not evidence of deployment, data promotion or production acceptance.

| Checkpoint | Exact identity | Meaning |
| --- | --- | --- |
| Observed GoDaddy preview/published source | `b50b74403c72219f4dbbe86b5c5dd6e2127217ae` | Deployment alias `a0-reconciliation-preview-20261018`; historical rollback checkpoint, not a claim of healthy service |
| Newer hosted source used for this candidate | `6020814b9adb9cd6a41c59d46fc3a98add190bb6` | `a0-hosted-ai-web-20261017`; preserves the newer Prairie Field Desk, hosted accounts/workspaces and hosted chat composition |
| Local `current` snapshot | `46d0f0ca73843bc6e9490595ec19a10693b0f1b5` plus 54 working-tree entries | Includes local runtime and uncommitted feature work; not a replacement hosting baseline |
| Local `explorer-publish-20261017` snapshot | `9e0e9270ef284076800f50b77081c5abedf40de2` plus 38 working-tree entries | Includes bounded public-source recovery and alternate layout work |

Every entry in both local snapshots has a recorded disposition. The counts
include overlapping work; they must not be added into a count of distinct
missing features. “Untracked locally” and “absent from the compared refs” do not
prove that a file was never pushed to any branch.

The task retains `local-current-reconciliation-audit.json`,
`snapshot-38-classification.json`, source snapshots, comparison patches and
hash manifests outside this application's Git and deployment trees. The earlier
`explorer-port-backup-20261017` snapshot also verified all 1,088 files against its
recorded SHA-256 manifest, with no missing or mismatched files. Preserved originals
remain unchanged; excluded local work is retained, not silently discarded.

## Recovered behavior

- Keep the newer Prairie Field Desk opening popup and its existing mission/place
  entry points. A versioned opt-out makes it visible again on startup unless the
  visitor explicitly chooses “Don’t show on start”; opening help preserves that
  choice. The previous preference key and unrelated local data are left intact.
  The existing quick-start dismissal preference is device-local;
  its presence is not evidence that the popup source was deleted. Reopening and
  startup behavior are checked separately from deployment state.
- Restore 17 subject topics, grouped selectors, source-specific membership,
  `/topics`, and a discovery link from Layers. Topic/view URL serialization owns
  only `topic` and `layerView`; unrelated camera, source and evidence parameters
  remain untouched. The public catalogue lists only specialist controls present
  in this hosted composition.
- Recover bounded opt-in retry for the exact current Census and compact statewide
  River Pulse GETs, shared-consumer cancellation, busy-response cooldowns and the
  deferred URL/history startup guard. Private reads and writes remain one-shot;
  malformed or oversized successful responses remain failures. Source times and
  values are never rewritten to imply freshness.
- Limit flowing-water cell reads to nine concurrent requests per map. Remaining
  selected cells wait; queue refill preserves the existing selection and stops
  on effect-off/removal, or pauses during camera movement. Retain the hosted
  detail-aware protocol, identity checks, coverage labels and terrain fixes.
- Restore mobile point/line/polygon measurement handoff to the map canvas and
  focus, using the existing measurement owner and browser-local privacy boundary.

The older local flowline v2 implementation, alternate inspector breakpoints,
local Worker launcher, loopback Qwen knowledge/evaluation work and monorepo
contracts are preserved separately. They do not replace the newer hosted
protocol, Node server, account controls, private storage bindings or governance
roots. Existing daily-archive authorization changes were already byte-identical
in the newer hosted source and are retained.

## Boundaries and validation

This reconciliation changes application code, tests and behavior-linked docs.
It does not admit source data, change evidence status, migrate/reset/reseed
storage, copy private records, alter the original Sites audience or bindings,
activate Earth Engine, or change release authority. Source/provider identities,
rights, sensitivity, timestamps, review, publication and rollback controls remain
with their existing owners. Free public report/export policy remains in force.

The final production build and TypeScript check passed in Node.js 22.23.3.
The 50-file core selection initially reported 425 passing tests and seven local
environment failures (sandbox-denied test sockets and a macOS temporary-path
alias). The five affected files then passed all 12 tests with loopback permission
and a canonical temporary directory. The production Node HTTP boundary passed
all 16 tests. These runs cover the changed areas and retained hosted boundaries;
they are not an exhaustive security audit. Browser checks confirmed the opening
popup, its default unchecked opt-out, successful dismissal, rendered map, and
Layers filtering to 11 aquifer/groundwater layers. Provider coverage remains
source-specific; one selected upstream source reported attention during the check.
GitHub CI and hosted preview/live acceptance are separate gates and must be
recorded against the final deployment identity.

Placement follows the accepted Directory Rules authority at
`docs/doctrine/directory-rules.md` and ADR-0029 in the inspected monorepo, together
with this standalone application's `AGENTS.md`, `docs/SITE_PRESERVATION.md` and
`docs/godaddy-node-preview.md`. Existing `app/`, `tests/` and `docs/` own these
changes. Recovery archives stay outside the source/deployment trees; this creates
no parallel canonical source, policy, registry, proof or release home.

## Rollback procedure

1. Record the actual current GoDaddy deployment identity, source commit, runtime
   configuration and health before changing anything. Preserve any newer source
   or work since this candidate was prepared. Do not reset an active checkout.
2. For source-only reversal of this reconciliation, start a separate clean
   checkout at `6020814b9adb9cd6a41c59d46fc3a98add190bb6`, or revert only these
   bounded changes on the current branch while preserving later independent work.
   Re-run the relevant checks; source reversal does not roll back private data.
3. If the owner chooses the previous GoDaddy release, the recorded checkpoint is
   `b50b74403c72219f4dbbe86b5c5dd6e2127217ae` on
   `a0-reconciliation-preview-20261018`. Verify the exact saved release/artifact
   and health first. Its historical publication is not proof that it is healthy
   or that it contains all recovered features; do not substitute it for the newer
   `6020814…` source without that explicit comparison.
4. Use the same GoDaddy app and existing runtime/private-store bindings. Do not
   create a replacement Site, repoint storage or restore databases as an incidental
   part of a source rollback. Verify startup, the opening popup, map/topic flows,
   source recovery, account/chat boundaries and observable errors after any
   authorized deployment, and record the result against the exact deployed pin.

The saved GoDaddy `godaddy-preview-export-before.zip` is **incomplete**: its
observed contents cover public assets and root configuration, not a complete
source/deployment or private-store backup. Private storage and credentials are
excluded. It must not be treated as a database recovery image or sufficient
standalone rollback artifact. Source archives and Git pins likewise do not prove
transactional recovery of hosted private state.
