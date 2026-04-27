<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/soil/open-verification
title: Soil Open Verification Backlog
type: standard
version: v1
status: draft
owners: TODO-VERIFY
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO-VERIFY
related: [kfm://doc/TODO-VERIFY-uuid]
tags: [kfm, soil, verification, backlog]
notes: [Action backlog for unresolved soil-lane verification work.]
[/KFM_META_BLOCK_V2] -->

# Soil Open Verification Backlog

Track unresolved decisions required to move the soil lane from draft domain docs to enforceable implementation.

## Priority queue

| Priority | Item | Why it matters | Exit criteria |
|---|---|---|---|
| P0 | Confirm canonical directory naming (`soil/` vs `soils/`) | Avoid split implementations and broken links | one canonical path documented and applied |
| P0 | Confirm schema/contract home | Prevent machine contract drift | soil contract path exists and is referenced by README |
| P0 | Confirm source-descriptor home + format | Required for source admission | at least one concrete descriptor template merged |
| P0 | Confirm policy engine + test convention | Needed for fail-closed behavior | passing policy tests and deny-path examples |
| P1 | Confirm validator locations and output envelope | Required for deterministic review outcomes | validator docs + fixtures + output schema linked |
| P1 | Confirm map layer registry + drawer payload contract | Needed for UI trust posture | documented payload contract with sample fixture |
| P1 | Confirm governed API route naming | Needed for stable consumers | route contract doc or schema updated |
| P2 | Confirm terms/rate limits/auth for each external source | Rights and reliability risk reduction | source-by-source terms table with review date |
| P2 | Confirm offline-first CI coverage | Prevent flaky PR validation | CI job(s) prove no live network dependency by default |

## Evidence needed for closure

Each closed item should include:

- a commit/PR reference,
- the owning steward/team,
- verification date (UTC),
- link to authoritative file(s),
- note describing any residual risk.
