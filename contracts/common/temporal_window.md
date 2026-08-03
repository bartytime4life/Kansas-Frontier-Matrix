<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/temporal-window
title: contracts/common/temporal_window.md — TemporalWindow Contract
type: contract
version: v0.3
status: draft; proposed-schema-paired; executable-validator-profile
owners: OWNER_TBD — Contract steward · Schema steward · Temporal steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-08-03
policy_label: public; contracts; common; temporal-window; shared-kernel; time-aware; no-release-authority
related:
  - ./README.md
  - ../../schemas/contracts/v1/common/temporal_window.schema.json
  - ../../fixtures/contracts/v1/common/temporal_window/README.md
  - ../../tools/validators/validate_temporal_window.py
  - ../../tests/validators/test_validate_temporal_window.py
  - ../../tests/schemas/test_common_contracts.py
  - ../../.github/workflows/temporal-window-validation.yml
  - ../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md
  - ../../docs/architecture/briefing-integration.md
notes:
  - "v0.3 records the bounded no-network validator and non-vacuous fixture profile."
  - "The paired schema and its six enum values are unchanged and remain PROPOSED."
  - "The validator proves shape, aware timestamp syntax, bounded parsing, and start/end ordering only."
  - "ADR-0014 remains proposed and its vocabulary conflict is not resolved by this implementation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# TemporalWindow Contract

> `TemporalWindow` is a small shared value object that binds an interval to an explicit time kind. It prevents an observation, source publication, ingest, effective period, correction, or supersession interval from becoming an unlabeled generic timestamp.

**Status:** draft / schema-paired / executable bounded validator  
**Contract path:** `contracts/common/temporal_window.md`  
**Schema path:** `schemas/contracts/v1/common/temporal_window.schema.json`  
**Validator:** `tools/validators/validate_temporal_window.py`  
**Fixture root:** `fixtures/contracts/v1/common/temporal_window/`

> [!IMPORTANT]
> Passing validation proves only the tested shape, timezone-aware date-time syntax, safe local parsing, and interval ordering. It does not prove source truth, freshness, evidence closure, policy approval, review approval, correction closure, release, or publication authority.

## Purpose

KFM records can carry several materially different kinds of time. `TemporalWindow` keeps those meanings explicit while remaining a narrow, reusable object that domain contracts may reference.

It answers:

1. when the represented interval starts;
2. when it ends; and
3. what kind of time the interval represents.

It does **not** replace a domain event, advisory, observation, source record, correction notice, review record, policy decision, release manifest, or rollback record.

## Responsibility and placement

Directory placement follows existing responsibility roots:

| Responsibility | Owning surface |
|---|---|
| Semantic meaning | `contracts/common/temporal_window.md` |
| Machine shape | `schemas/contracts/v1/common/temporal_window.schema.json` |
| Synthetic cases | `fixtures/contracts/v1/common/temporal_window/` |
| Executable checks | `tools/validators/validate_temporal_window.py` |
| Focused tests | `tests/validators/test_validate_temporal_window.py` |
| Generic schema polarity | `tests/schemas/test_common_contracts.py` |
| Admissibility, exposure, freshness, and release | `policy/`, evidence, review, and release families |

No new root or parallel temporal authority is created by this profile.

## Current field surface

| Field | Required | Meaning |
|---|---:|---|
| `start` | yes | Beginning of the interval as a timezone-aware date-time. |
| `end` | yes | End of the interval as a timezone-aware date-time. |
| `time_kind` | yes | Closed schema enum identifying the current temporal role. |

The paired schema remains closed with `additionalProperties: false`.

## Current schema time kinds

The current **proposed schema** accepts:

- `observed`
- `published`
- `ingested`
- `effective`
- `corrected`
- `superseded`

These values describe the existing contract profile. They are not silently declared the final KFM-wide temporal vocabulary.

> [!CAUTION]
> ADR-0014 remains `proposed` and records a non-equivalent six-identifier vocabulary. The broader time-aware doctrine also names additional dimensions. This validator does not reconcile, translate, accept, or supersede those surfaces. Consumers must not infer a lossless mapping.

## Invariants

A valid candidate must satisfy all of the following:

- the JSON root is an object;
- `start`, `end`, and `time_kind` are present;
- no undeclared top-level property is present;
- both timestamps satisfy the schema date-time format and include timezone information;
- after timezone normalization, `start` is less than or equal to `end`;
- the time kind is one of the current schema enum values;
- input is finite UTF-8 JSON without duplicate object members;
- the candidate is a bounded regular file, not a symlink, FIFO, device, or oversized input.

Equal instants expressed through different offsets are valid. A syntactically valid timestamp can still represent the wrong kind of time for a consumer; the owning domain, evidence, and policy surfaces must decide that.

## Validation profile

The bounded validator:

- reads regular files only with no-follow and nonblocking safeguards where supported;
- limits candidate size and JSON nesting depth;
- rejects duplicate keys and non-finite number tokens;
- validates against JSON Schema Draft 2020-12 with a format checker;
- compares aware timestamps after UTC normalization;
- emits deterministic JSON diagnostics without candidate values;
- supports explicit files and a non-vacuous `--fixtures` profile;
- performs no network access;
- returns nonzero for malformed input, schema failure, semantic ordering failure, fixture polarity failure, or expected-error mismatch.

Finite finding codes include:

| Code | Meaning |
|---|---|
| `SCHEMA_INVALID` | A reviewed JSON Schema constraint failed. |
| `TEMPORAL_ORDER_INVALID` | `end` precedes `start` after timezone normalization. |
| `DUPLICATE_KEY` | A JSON object repeats a member name. |
| `NONFINITE_NUMBER` | The candidate uses a non-standard non-finite token. |
| `UNSAFE_FILE` | The input is not a safe regular file. |
| `FILE_TOO_LARGE` | The candidate exceeds the bounded parser budget. |
| `JSON_COMPLEXITY_LIMIT` | Parser or schema complexity exceeds the bounded profile. |
| `FIXTURE_POLARITY_ERROR` | A reviewed invalid fixture unexpectedly passes. |
| `EXPECTED_REJECTION_MISMATCH` | Actual findings do not match the sidecar evidence. |

## Fixture profile

The fixture family contains:

| Lane | Cases | Purpose |
|---|---:|---|
| `valid/` | 2 | UTC interval and offset-equivalent boundary case. |
| `invalid/` | 3 | Missing kind, unknown kind, and additional-property rejection. |
| `semantic_invalid/` | 2 | Reversed interval and timezone-naive timestamp. |

`semantic_invalid/` is deliberately separate because the repository generic schema harness does not attach a format checker and cannot prove semantic ordering. The dedicated validator owns those checks.

## Commands

```bash
PYTHONPATH=. KFM_NO_NETWORK=1 \
  python tools/validators/validate_temporal_window.py --fixtures

PYTHONPATH=. KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_temporal_window.py' \
  --verbose

PYTHONPATH=. \
  python -m pytest -q tests/schemas/test_common_contracts.py
```

## Accepted uses and exclusions

| Use | Posture |
|---|---|
| Carry an explicit interval inside another governed object | Allowed when the owning contract cites this profile. |
| Distinguish observation, publication, ingest, effective, correction, and supersession intervals | Allowed within the current proposed schema profile. |
| Use interval ordering as evidence that an event occurred | Denied; chronology shape is not evidence. |
| Treat `published` as KFM release approval | Denied; a timestamp is not a release decision. |
| Treat `corrected` as correction closure | Denied; correction objects and review remain separate. |
| Treat `superseded` as rollback completion | Denied; rollback and release lineage remain separate. |
| Collapse all source, valid, observed, retrieval, release, or correction times into one window | Denied; use domain-specific structures where one window is insufficient. |

## Compatibility and migration

The schema shape and enum are unchanged in this slice. Any future change to enum membership, open-ended intervals, precision, uncertain time, recurring intervals, or boundary inclusivity is compatibility-significant and requires:

1. a reviewed semantic-contract update;
2. a schema version or compatible extension decision;
3. positive, negative, and migration fixtures;
4. validator and consumer updates;
5. explicit reconciliation with proposed ADR-0014 and time-aware doctrine;
6. rollback instructions.

## Lifecycle and authority boundary

```text
source or domain object
  -> TemporalWindow candidate
  -> bounded schema and ordering validation
  -> evidence/source resolution
  -> domain and policy interpretation
  -> review/release decision, when applicable
  -> receipt and correction lineage
```

The validator never creates evidence, policy, review, release, correction, rollback, lifecycle, or public state.

## Validation status

**CONFIRMED in this implementation slice:**

- dedicated validator replaces the `NotImplementedError` placeholder;
- valid, schema-invalid, and semantic-invalid fixture lanes are non-empty;
- focused standard-library tests cover parsing, ordering, unsafe files, deterministic output, no-network behavior, and fixture polarity;
- the dedicated TemporalWindow workflow runs the focused suite, while the existing schema-validation lane discovers the new schema fixture family.

**Still UNKNOWN or NEEDS VERIFICATION:**

- production consumers;
- policy thresholds for freshness or embargo;
- accepted KFM-wide temporal vocabulary;
- full domain migration;
- API/UI usage;
- release and correction integration;
- stewardship assignments.

## Correction and rollback

Before merge, close the draft pull request and abandon the branch. After merge, revert the implementation commits. Rollback restores the former placeholder and removes this fixture/test profile; it does not alter production records, source evidence, release state, or published data because this slice creates none.

Previous contract blob before v0.3: `80b0c9514ff8adba2f8e71611289c15de2f5e95b`.

## Definition of done

- [x] Dedicated validator is implemented.
- [x] Valid, schema-invalid, and semantic-invalid fixtures exist.
- [x] Ordering and timezone-aware behavior are tested.
- [x] No-network and unsafe-file behavior are tested.
- [x] Dedicated workflow and generic schema-test discovery include the profile.
- [x] The proposed vocabulary conflict remains explicit.
- [ ] Temporal vocabulary is ratified through a separate decision.
- [ ] Production consumers and policy integration are verified.
- [ ] Owners and independent review routes are confirmed.

<p align="right"><a href="#top">Back to top</a></p>
