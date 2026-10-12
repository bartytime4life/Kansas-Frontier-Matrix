<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-elapsed-time-unit-disclosure-source-map
title: Pass 18 Elapsed-Time Unit Disclosure Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Analytics steward · Query steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; temporal; metric; units
responsibility: Reconcile one supplied timestamp-difference idea with current repository evidence while preserving query, metric, evidence, policy, review, release, and publication boundaries.
truth_posture: "CONFIRMED supplied-card and bounded repository gap; PROPOSED inactive implementation profile; UNKNOWN runtime adoption; NEEDS VERIFICATION engine and timezone behavior, human review, and hosted CI"
related:
  - ../../../contracts/common/elapsed_time_unit_disclosure.md
  - ../../../contracts/common/rolling_metric_window_disclosure.md
  - ../../../contracts/common/temporal_window.md
  - ../../../contracts/governance/query_run_record.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Elapsed-Time Unit Disclosure Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-312` | SQL metrics comparing timestamps should record the extraction unit and conversion rule used to compute elapsed time. | `CONFIRMED` source statement |
| Source attribution `SRC-P18-003` | The card cites advanced SQL examples using epoch extraction, division by `3600`, and a `168`-hour filter, and proposes explicit elapsed-time unit and timezone-assumption fields. | `CONFIRMED` source lineage |
| Current `TemporalWindow`, `RollingMetricWindowDisclosureCandidate`, and `QueryRunRecord` profiles | Adjacent temporal interval, rolling-window, and query-run identities exist, but no exact timestamp-difference extraction/display unit, rational conversion, timezone, boundary, rounding, sign/null, and public-disclosure contract, schema, fixture suite, validator, workflow, branch, or PR was found before authoring. | `CONFIRMED` bounded gap |
| GitHub repository and PR/branch search at `main@fa244eb7bd11d8ff96e91f4925ca8abc5bdaa9fe` | Exact card, title, timestamp-difference, elapsed-unit, `TIMESTAMPDIFF`, conversion-rule, path, branch, and PR searches found no competing implementation. | `CONFIRMED` bounded search |

The connected Drive entry (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) identifies a Pass 18 dossier with the same title and source role. Only Drive metadata was inspected; byte identity with the supplied local copy and Drive card-level content were not asserted. The supplied local PDF SHA-256 is `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`; rendered physical page 258 was visually checked for card and continuation fidelity.

## Adaptation

The implementation is a closed synthetic common-contract profile. It carries timestamp field names plus opaque digest-bound query, method, timezone, boundary, engine, evidence, review, release, and parity-fixture references. It contains no timestamp values, elapsed values, source rows, SQL text, connection material, credentials, arbitrary generated prose, or runtime metric output.

Fixed-duration conversion is checked as an exact reduced rational relationship. Calendar units require calendar-boundary semantics and remain identity-only in this first profile, avoiding a false universal month/year duration. `ABSOLUTE_VALUE` and silent null-row `DROP` policies deny. `UNRESOLVED` timezone or engine parity abstains and `MISMATCH` denies; the profile invents no engine or timezone compatibility result.

## Directory Rules basis

Accepted ADR-0029 places reusable elapsed-time meaning under `contracts/common/`, machine shape under `schemas/contracts/v1/common/`, synthetic replay under `fixtures/contracts/v1/common/`, executable validation under `tools/validators/`, conformance proof under `tests/validators/`, orchestration under `.github/workflows/`, reconciliation under `docs/intake/exploratory/`, and generated authoring provenance under `data/receipts/generated/`.

No query runner, database adapter, metric store, evidence store, policy rule, review record, release lane, public panel, or new root is created.

## Non-effects and rollback

A local `PASS` is declaration coherence only. It is not query execution, elapsed-value correctness, metric fitness, evidence resolution, policy approval, human review, promotion, release, publication, or public-answer authority. Rollback is an additive commit revert with no external cleanup.
