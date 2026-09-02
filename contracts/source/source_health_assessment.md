<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-health-assessment
title: SourceHealthAssessment Contract
type: semantic-contract; source-health; watcher-sidecar
version: v0.2.0
status: proposed; offline-validation; non-authoritative
owners: OWNER_TBD — Source steward · Contract steward · Validation steward
created: 2026-08-07
updated: 2026-08-14
policy_label: public; source; source-health; non-publisher; no-network
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

Finite health outcomes are `HEALTHY`, `DEGRADED`, `STALE`, `UNAVAILABLE`, and `UNKNOWN`. Retrieval classes are `SUCCESS`, `NOT_MODIFIED`, `EMPTY`, `TIMEOUT`, `HTTP_ERROR`, `PARSE_ERROR`, `AUTH_ERROR`, and `NOT_PROBED`.

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

The focused suite covers healthy, stale, unavailable, and unknown observations; exact negative cases; Draft 2020-12 schema validity; bounded input; symbolic links; duplicate keys; non-finite numbers; root shape; value-minimized findings; deterministic JSON output; credential-free execution; and a no-network assertion.

## Directory Rules basis

Accepted ADR-0029 adopts `docs/doctrine/directory-rules.md`. Under its responsibility split, semantic meaning stays in `contracts/source/`; machine shape in `schemas/contracts/v1/source/`; reusable synthetic cases in `fixtures/contracts/v1/source/`; repository-wide validation in `tools/validators/source/`; executable conformance in `tests/source/`; read-only orchestration in `.github/workflows/`; and AI-authoring provenance in `data/receipts/generated/`. This packet creates no new root or parallel authority home.

## Compatibility and rollback

The object name, required core fields, existing enums, optional ETag/Last-Modified posture, and documented fail-closed rules remain compatible with v0.1. The validator CLI now emits a deterministic finite JSON envelope instead of free-form `valid` or error text; repository search found no caller other than its focused test at the implementation baseline.

Before merge, close the draft pull request and retire its branch. After an authorized merge, revert the additive workflow, fixtures, receipt, contract expansion, schema constraints, validator, and tests together. No live source, external state, lifecycle record, release, or public artifact requires operational rollback.
