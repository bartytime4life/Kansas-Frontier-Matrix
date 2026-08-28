<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-aggregate-grouping-disclosure-source-map
title: Pass 18 Aggregate Grouping Disclosure Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Analytics steward · Evidence steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; aggregate; subtotal; disclosure
responsibility: Reconcile one supplied aggregate-grouping idea with current repository evidence while preserving query, evidence, policy, review, release, and publication boundaries.
truth_posture: "CONFIRMED supplied-card and bounded repository gap; PROPOSED inactive implementation profile; UNKNOWN runtime adoption; NEEDS VERIFICATION cross-engine behavior, human review, and hosted CI"
related:
  - ../../../contracts/common/aggregate_grouping_disclosure.md
  - ../../../contracts/common/aggregate_statistic.md
  - ../../../contracts/common/rolling_metric_window_disclosure.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Aggregate Grouping Disclosure Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-480` | Aggregate outputs should distinguish detail/raw group rows, subtotal rows, and grand-total rows when `ROLLUP`, `CUBE`, or equivalent semantics are used. | `CONFIRMED` source statement |
| Source attribution `SRC-P18-003` | The card cites advanced SQL grouping features, proposes explicit `aggregate_level` and `grouping_keys`, and leaves cross-engine normalization unresolved. | `CONFIRMED` source lineage |
| Current `AggregateStatistic`, `RollingMetricWindowDisclosureCandidate`, `QueryRunRecord`, and indicator profiles | Adjacent aggregate, temporal-window, and query identities exist, but no exact aggregate-grouping disclosure contract, schema, fixture suite, validator, workflow, branch, or PR was found before authoring. | `CONFIRMED` bounded gap |
| GitHub repository and PR/branch search at `main@97b9cb77bf57b1d1cf75c2768f8e550e399a1345` | Exact card, subtotal, `ROLLUP`, `CUBE`, title, path, branch, and PR searches found no competing implementation. | `CONFIRMED` bounded search |

The Drive copy of the Pass 18 dossier (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) and the supplied local copy identify the same source artifact. The local PDF SHA-256 is `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`; rendered physical pages 291-292 were visually checked for card and continuation fidelity.

## Adaptation

The implementation is a closed synthetic common-contract profile. It carries grouping-dimension names and opaque digest-bound references only. It contains no group values, aggregate values, source rows, SQL text, credentials, coordinates, arbitrary generated prose, or statistical thresholds.

The profile defines one deterministic external grouping mask so fixture semantics can be reviewed. It does not claim that a database's native `GROUPING_ID`, null treatment, ordering, or cross-engine behavior matches that mask. `UNRESOLVED` parity abstains and `MISMATCH` denies.

## Directory Rules basis

Accepted ADR-0029 places reusable aggregate meaning next to `AggregateStatistic` under `contracts/common/`, machine shape under `schemas/contracts/v1/common/`, synthetic replay under `fixtures/contracts/v1/common/`, executable validation under `tools/validators/`, conformance proof under `tests/validators/`, orchestration under `.github/workflows/`, reconciliation under `docs/intake/exploratory/`, and generated authoring provenance under `data/receipts/generated/`.

No analytics engine, query store, aggregate dataset, evidence store, policy rule, review record, release lane, public panel, or new root is created.

## Non-effects and rollback

A local `PASS` is declaration coherence only. It is not query execution, aggregate truth, evidence resolution, statistical fitness, policy approval, human review, promotion, release, publication, or public-answer authority. Rollback is an additive commit revert with no external cleanup.
