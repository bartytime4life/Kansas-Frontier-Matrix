<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registers/m22-m29-inventory-overlap-20261118
title: M22 and M29 inventory and overlap map
type: register
version: v1.0
status: draft; repository-inventory only; independent review pending
owners: ["@bartytime4life"]
created: 2026-11-18
updated: 2026-11-18
policy_label: public
current_path: docs/registers/m22-m29-inventory-overlap-20261118.md
owning_root: docs/
responsibility: Record the milestone-specific inventory and overlap map named by the completion boundaries of #3390 (M22) and #3394 (M29).
truth_posture: cite-or-abstain; repository paths at main 2aaf6626 only; no hosted, live-source, external-consumer or human-acceptance claim
related:
  - milestone-progress-2026-10-08.md
  - ../../fixtures/domains/hydrology/western_kansas_observation_assessment/multiclock/README.md
  - ../../fixtures/release/temporal_replay/README.md
[/KFM_META_BLOCK_V2] -->

# M22 and M29 inventory and overlap map — 2026-11-18

Both [#3390](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3390)
(M22) and [#3394](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3394)
(M29) can close only after three things are recorded:

1. the milestone-specific inventory and overlap map;
2. a verified dependency, path, validation and rollback contract for the first slice;
3. an explicit list of every unresolved item.

This register supplies item 1 and points to the existing slice contracts for
item 2. It does not close either issue. That remains the owner's decision, and
independent review is still pending.

Status labels follow the issues: `IMPLEMENTED`, `PARTIAL`, `ABSENT`,
`SUPERSEDED`, `CONFLICTED`, `DEPRECATED` and `NOT_INSPECTED`. The repository pin
is `main@2aaf6626`, and every path is relative to the repository root. For the
local validation limits, see the [ledger](milestone-progress-2026-10-08.md).

## M22: drought, water supply, soil and agriculture observation proof

| Surface | Path | Status | Notes |
|---|---|---|---|
| Synthetic multi-clock fixture | `fixtures/domains/hydrology/western_kansas_observation_assessment/multiclock/` | IMPLEMENTED | Observation, forecast, correction and binding inputs. Every identity is synthetic. |
| Rehearsal runner | `tools/validators/evidence/rehearse_drought_multiclock.py` | IMPLEMENTED | 27 exact outcomes, including refused negative cases. |
| Focused tests | `tests/validators/test_drought_multiclock_replay.py` | IMPLEMENTED | Locally they need the hash-locked test profile. Without it, the hashing cases fail with `HASHING_UNAVAILABLE` (an environment limit). |
| Assessment contract | `contracts/domains/hydrology/western_kansas_observation_assessment.md` | IMPLEMENTED | Clocks, joins, prohibited shortcuts and material change. |
| Forecast contract | `contracts/common/forecast_product.md` | IMPLEMENTED | Cutoff, issue, retrieval and validity are separate. |
| Earlier case matrix | `fixtures/domains/hydrology/western_kansas_observation_assessment/cases.json` | IMPLEMENTED | Unchanged by the multi-clock slice. |
| Drought family validators | `tools/validators/hazards/validate_drought_families.py`, `fixtures/domains/hazards/drought_*` | IMPLEMENTED | An observation and a declaration are never collapsed into each other. |
| Rehearsal receipt | `data/receipts/generated/genrec-drought-multiclock-20261117.json` | PARTIAL | Records the run. Human review is pending. |
| CI workflow | `.github/workflows/western-kansas-observation-assessment.yml` | IMPLEMENTED | Runs the synthetic rehearsal only. |
| Source-family authority, cadence and rights | — | ABSENT | All seven families are `NOT_ASSESSED`, and their rights are `UNKNOWN`. |
| Live source admission or snapshot | — | ABSENT | Gated by design. No live ingest happens. |
| Explorer context | `apps/site/source` (CPC drought outlook, MRMS, WPC QPF, streamflow, High Plains aquifer) | PARTIAL | External context only. These are not M22 evidence and do not satisfy M22. |
| Soil and agriculture observation proof | `fixtures/domains/soil`, `fixtures/domains/agriculture` | NOT_INSPECTED | This register does not include them in the multi-clock slice. |

**Overlap:**

- [#2899](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2899) shares the fixture and the contract.
- [#3383](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3383) and M29 share the clock vocabulary.
- [#3369](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3369) gates any live admission.
- [#3370](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3370) covers identity.

**First-slice contract:** see the multi-clock fixture README for its
dependencies, paths and run commands. Rollback means reverting the fixture, the
runner, the tests and the receipt together; there is no data or store migration.

**Unresolved:**

- source-family authority, cadence and rights;
- steward acceptance;
- live-source admission;
- hosted acceptance of the exact head;
- soil and agriculture observation coverage.

## M29: temporal replay, correction and cross-version migration

| Surface | Path | Status | Notes |
|---|---|---|---|
| Cross-version replay fixture | `fixtures/release/temporal_replay/` | IMPLEMENTED | Covers the legacy, successor, common v1 and v2, successor-receipt and withdrawn records. |
| Replay tool | `tools/release/temporal_replay.py` | IMPLEMENTED | Validates the fixture, then exercises withdrawal and rollback on disposable copies. |
| Focused tests | `tests/release/test_temporal_replay.py` | IMPLEMENTED | 24 tests pass locally. |
| Rollback drill job | `.github/workflows/rollback-drill.yml` (`temporal-replay`) | IMPLEMENTED | Synthetic recovery only. |
| Temporal envelopes | `contracts/common/temporal_authority_envelope.md`, `contracts/evidence/temporal_authority_envelope.md` | IMPLEMENTED | Kept as separate families. The fixture performs no translation between them. |
| Split-support validator | `tools/validators/governance/temporal_authority_split_support.py` | IMPLEMENTED | Rejects cross-family false acceptance. |
| Replay receipt | `data/receipts/generated/genrec-temporal-replay-20261117.json` | PARTIAL | Human review is pending. The external-consumer gate is skipped. |
| Universal temporal vocabulary (ADR-0014) | — | CONFLICTED | The fixture explicitly does not resolve it. |
| Persisted-store migration | — | ABSENT | The proof is a dual-read-only boundary. No store is migrated. |
| External and persisted consumer inventory | — | NOT_INSPECTED | Legacy removal remains `HOLD_EXTERNAL_INVENTORY_REQUIRED`. |

**Overlap:**

- [#3383](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3383) covers temporal semantics and shares the same envelopes.
- [#3370](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3370) covers identity and namespaces.
- [#4024](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024) covers delivery containment.
- M22 reuses the clock separation.

**First-slice contract:** see the temporal-replay fixture README for its
dependencies, paths and run commands. Rollback means reverting the fixture, the
tool, the tests, the workflow job and the receipt together. History is preserved
and no store is migrated.

**Unresolved:**

- the external and persisted consumer inventory;
- the ADR-0014 vocabulary decision;
- any real migration and its receipt;
- temporal and compatibility reviewer acceptance;
- hosted acceptance of the exact head.

## Non-effects

This register is not a review, an acceptance or a closure. It does not admit a
source, migrate a store, release anything or change a workflow.
