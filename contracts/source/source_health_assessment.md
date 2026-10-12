<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-health-assessment
title: SourceHealthAssessment Contract
type: contract
version: v0.4.0
status: proposed; offline-validation; non-authoritative
owners: OWNER_TBD — Source steward · Contract steward · Validation steward
created: 2026-08-07
updated: 2026-10-01
policy_label: public; source; source-health; non-publisher; no-network
owning_root: contracts/
responsibility: Define finite non-publishing source-health states and their fail-closed validation semantics.
truth_posture: CONFIRMED bounded offline validation / NEEDS VERIFICATION live source integration
related:
  - ../../schemas/contracts/v1/source/source_health_assessment.schema.json
  - ../../fixtures/contracts/v1/source/source_health_assessment/
  - ../../tools/validators/source/validate_source_health_assessment.py
  - ../../tests/source/test_source_health_assessment.py
  - ../../.github/workflows/source-health-assessment.yml
  - ./source_availability_watchlist.md
tags: [kfm, source-health, freshness, watcher, fail-closed, deterministic, offline]
notes:
  - "This assessment records a bounded observation about retrieval health; it does not establish source truth or scientific truth."
  - "The SourceAvailabilityWatchlist references this object family and does not replace it."
  - "PASS means the assessment is internally coherent; it does not mean the assessed source is healthy, admitted, or publishable."
[/KFM_META_BLOCK_V2] -->

# SourceHealthAssessment

`SourceHealthAssessment` records a bounded, non-publishing evaluation of source freshness and retrieval health. It is designed for watcher sidecars and material-change detection without granting source activation, truth, release, or publication authority.

## Source basis

The proposal source is `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`:

- Part I §6.2, `KFM-IDX-SRC-007 — Ecology Source-Health and Tile-Health Watchers`, proposes policy-bound, receipt-emitting, non-publishing health observations.
- Part I §6.6, `KFM-IDX-VAL-003 — CI Probes with Source Heads and Run Receipts`, proposes a no-network mock harness before live source checks.
- Part II §6.3.2, `KFM-IDX-SRC-005 — Environmental CI probes are source-health monitors, not scientific conclusions`, separates source availability from source truth.
- Part II §6.7, `KFM-IDX-VAL-002 — Environmental source probes need signed receipts`, calls for negative stale and unavailable-source fixtures.
- §10.1 and Appendix C.1, `EXP-003 — Source-watch registry for environmental probes`, define fixture validation as a proof-of-closure dependency while leaving live thresholds and source activation unresolved.

Those passages are proposal evidence. The current repository object family, accepted ADR-0029, adopted Directory Rules, executable behavior, and dependent `SourceAvailabilityWatchlist` determine this bounded implementation.

## Responsibility boundary

| This contract owns | It does not own |
|---|---|
| Meaning of a source-health observation | Network probing or connector transport |
| Finite retrieval and freshness states | Source admission, role, rights, or sensitivity |
| Fail-closed local consistency rules | Scientific or source-truth conclusions |
| Offline validation outcomes | Materiality policy or candidate-work execution |
| Optional captured ETag and Last-Modified values | Credential handling or live endpoint configuration |
| Review signal for unknown or unprobed state | Promotion, release, deployment, or publication |

`SourceAvailabilityWatchlist` remains the aggregate review projection over references to this family and `MaterialChangeAssessment`. It does not weaken these assessment-level rules.

## Fields and finite vocabularies

Each assessment records:

- stable `assessment_id` and `source_id` values;
- timezone-aware `probed_at`, optional prior-success time, and optional freshness deadline;
- optional ETag and Last-Modified observations;
- one retrieval `result_class`;
- one `health_outcome`;
- a material-change signal; and
- one or more finite reason codes.

Finite health outcomes are `HEALTHY`, `DEGRADED`, `STALE`, `UNAVAILABLE`, and `UNKNOWN`. Retrieval classes are `SUCCESS`, `NOT_MODIFIED`, `EMPTY`, `TIMEOUT`, `HTTP_ERROR`, `ACQUISITION_ERROR`, `PARSE_ERROR`, `AUTH_ERROR`, and `NOT_PROBED`. `ACQUISITION_ERROR` covers failed acquisition whose cause cannot be classified more precisely from the recorded evidence; it carries `RETRIEVAL_FAILED` and cannot be `HEALTHY`.

`CAPTURE_INCOMPLETE` records that the shared capture did not produce a closed
candidate. If a station's last retrieval succeeded, its result is `SUCCESS`
and usable health is `UNKNOWN`, without copying another station's timeout.
An unattempted station remains `NOT_PROBED` / `UNKNOWN`. A successful attempt
in this capture may populate `last_success_at` even when a later page fails;
`NO_PRIOR_SUCCESS` means no successful attempt is recorded in this capture.
This producer does not infer success from historical captures.
For the local water producer, `last_success_at` is the latest successful
retrieval-attempt timestamp for that station. `probed_at` is the capture's
completion timestamp; it must not be substituted for an earlier attempt time.

## Fail-closed consistency rules

The validator denies an assessment when any of these conditions are present:

- a failed retrieval or empty response is labeled `HEALTHY`;
- `UNAVAILABLE` lacks a failed retrieval result;
- failed, parse, authentication, empty, material-change, or freshness states omit their corresponding finite reason;
- a false material-change signal retains `MATERIAL_CHANGE`;
- `NOT_PROBED` is presented as anything other than `UNKNOWN` or omits `NOT_PROBED`;
- `last_success_at` occurs after `probed_at`;
- an elapsed freshness deadline is labeled `HEALTHY`; or
- a healthy assessment lacks `WITHIN_FRESHNESS`.
- `CAPTURE_INCOMPLETE` is labeled `HEALTHY`.

An empty or failed probe never clears a prior condition. An `UNKNOWN` or `NOT_PROBED` assessment is internally valid but returns `ABSTAIN`, so downstream review cannot mistake missing observation evidence for health.

## Validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape and semantic consistency passed. The source itself may still be degraded, stale, or unavailable. |
| `ABSTAIN` | A coherent `UNKNOWN` or `NOT_PROBED` record requires further observation or review. |
| `DENY` | Schema or semantic consistency failed. |
| `ERROR` | The input or schema could not be read or evaluated safely. |

Output findings contain finite codes and JSON-pointer paths only. They do not echo assessment values. Input is bounded to 1 MiB; symbolic links, duplicate JSON keys, non-finite numbers, invalid UTF-8/JSON, and non-object roots fail before schema evaluation.

## Governance posture

The validator is offline and credential-free. It performs no network request, source activation, lifecycle write, candidate creation, policy or review decision, promotion, release, deployment, publication, or public use. A validator `PASS` creates no authority and must not be interpreted as `HEALTHY`.

Rights, sensitivity, security, and publication posture are unchanged because the fixtures are synthetic and no source payload, endpoint, credential, precise location, living-person information, or sensitive domain material is introduced.

## Validation

```bash
python -m py_compile tools/validators/source/validate_source_health_assessment.py
python -m py_compile tests/source/test_source_health_assessment.py
python -m unittest tests.source.test_source_health_assessment -v
python tools/validators/source/validate_source_health_assessment.py \
  fixtures/contracts/v1/source/source_health_assessment/valid/healthy_not_modified.json
```

The focused suite covers healthy, stale, unavailable, unknown, and unclassified acquisition observations; exact negative cases; Draft 2020-12 schema validity; bounded input; symbolic links; duplicate keys; non-finite numbers; root shape; value-minimized findings; deterministic JSON output; credential-free execution; and a no-network assertion. The workflow replays the immutable 2026-08-14 authoring receipt against its exact ancestor commit; current behavior is checked by the current tests, not inferred from that historical receipt.

## Directory Rules basis

Accepted ADR-0029 adopts `docs/doctrine/directory-rules.md`. Under its responsibility split, semantic meaning stays in `contracts/source/`; machine shape in `schemas/contracts/v1/source/`; reusable synthetic cases in `fixtures/contracts/v1/source/`; repository-wide validation in `tools/validators/source/`; executable conformance in `tests/source/`; read-only orchestration in `.github/workflows/`; and AI-authoring provenance in `data/receipts/generated/`. This packet creates no new root or parallel authority home.

## Compatibility and rollback

The v0.3 addition of `ACQUISITION_ERROR` preserves existing values and fields, but consumers that exhaustively switch on `result_class` must handle the new value. Repository search at `main@a1c92e239a260751ee16c9d37e5bc92830cece51` found no such consumer beyond the water producer and this validator; external consumers remain `NEEDS VERIFICATION`.

Version 0.4 adds only the `CAPTURE_INCOMPLETE` reason and station-scoped water
producer behavior. Existing result and outcome values remain unchanged, but
consumers of water health receipts must handle a previously misreported station
as `SUCCESS` / `UNKNOWN` with an explicit capture-incomplete reason. External
consumer readiness remains `NEEDS VERIFICATION`.

Rollback is a revert of the enum, water producer, validator, tests, and behavior-linked documentation together. The historical authoring receipt stays immutable. Existing lifecycle objects are not relabeled or rewritten by a code revert; correction of any emitted assessment requires its own governed action.
