<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-experiments-readme
title: tests/experiments/README.md — Temporal Storage Experiment Test Lane
type: README
version: v0.3
status: draft; repository-grounded; one-executable-test-module-confirmed; 8-source-defined-tests; one-direct-workflow-binding-confirmed; readme-path-filter-gap
owners: "@bartytime4life — CONFIRMED CODEOWNERS review route; accountable experiment-test stewardship UNKNOWN"
created: 2026-08-30
updated: 2026-08-31
policy_label: repository-facing; tests; experiments; synthetic; no-network; non-publisher
owning_root: tests/
responsibility: executable temporal-storage experiment test inventory and bounded no-network interpretation guidance without deciding contract, schema, source, evidence, policy, lifecycle, review, release, deployment, publication, or production-storage authority
truth_posture: CONFIRMED repository-grounded inventory and direct briefing-workflow binding at the pinned base / PROPOSED maintenance and stewardship claims / NEEDS VERIFICATION current execution, contract-schema compatibility, production consumers, required-check status, and accountable review
current_path: tests/experiments/README.md
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 8aab826f80e798301ae86430b6334644e1ca62bd
source_defined_test_count: 8
executable_test_modules: 1
direct_workflow_bindings: 1
related:
  - ../README.md
  - ./test_temporal_slice_store.py
  - ../../tools/experiments/temporal_slice_store.py
  - ../../contracts/data/temporal_slice.md
  - ../../schemas/contracts/v1/data/temporal_slice.schema.json
  - ../validators/test_validate_temporal_slice.py
  - ../../.github/workflows/temporal-slice.yml
  - ../../.github/workflows/briefing-implementation-campaign.yml
  - ../../docs/doctrine/directory-rules.md
  - ../../.github/CODEOWNERS
notes:
  - "Counts describe source-defined test methods at the pinned base commit, not a collected-case or hosted-run receipt."
  - "The experiment uses a reduced SQL row model and is not asserted to implement the proposed TemporalSlice contract or schema."
  - "The briefing-implementation-campaign workflow directly collects this module and its self-test, but its path filters do not include this README."
[/KFM_META_BLOCK_V2] -->

# `tests/experiments/` — Temporal Storage Experiment Test Lane

`tests/experiments/` contains executable evidence for one deterministic,
in-memory temporal-slice storage experiment. The lane tests a bounded SQL
index and selection model; it does not establish a production repository,
contract conformance, source truth, policy approval, promotion, release, or
publication.

<a id="top"></a>

## Purpose and scope

This README helps maintainers locate, run, and interpret the experiment test
without confusing a local proof of behavior with a supported storage service.

The lane contains one Python module defining eight `unittest` methods. It
exercises [`TemporalSliceStore`](../../tools/experiments/temporal_slice_store.py),
whose default database is an in-memory standard-library SQLite connection. The
test records are constructed in code and identify themselves as synthetic test
values; the lane reads no source observations or committed fixture files.

The implementation is explicitly an experiment. Its SQL row shape is smaller
than the separate proposed
[`TemporalSlice` contract](../../contracts/data/temporal_slice.md), and this
test module does not invoke the contract schema or validator. Treat those as
distinct evidence surfaces unless a later reviewed change establishes and
tests a mapping.

## Current inventory

| Test module | Tests | System under test | Direct input |
|---|---:|---|---|
| [`test_temporal_slice_store.py`](test_temporal_slice_store.py) | 8 | [`tools/experiments/temporal_slice_store.py`](../../tools/experiments/temporal_slice_store.py) | Synthetic `StoredTemporalSlice` values built by the test helper |

The count is a static inventory of methods whose names begin with `test_` at
the pinned base. It does not prove collection completeness, a passing result,
coverage, mutation resistance, workflow enforcement, or production parity.

## Tested behavior

The module checks that the experiment:

- creates the two expected lookup and change indexes;
- selects records using a half-open interval, including the start and
  excluding the end;
- returns `AMBIGUOUS` instead of choosing silently when unsuperseded slices
  overlap;
- resolves that tested overlap after explicit predecessor-to-successor
  supersession;
- orders changed slices by descending magnitude, then ascending start time,
  then stable slice identity;
- isolates dataset-version and grid-key partitions;
- rejects reversed windows and negative deltas before inserting a row; and
- rejects a duplicate primary identity.

These assertions are narrower than the implementation. For example, they do
not exhaustively exercise timestamp normalization, every governed change
state, every supersession rejection path, connection injection, the command
line self-test, or persistence across processes.

## Run the lane

From the repository root with Python 3.11 or later:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 KFM_NO_NETWORK=1 \
  python -m unittest discover \
    --start-directory tests/experiments \
    --pattern 'test_temporal_slice_store.py' \
    --verbose
```

Beyond the repository-local implementation import, this lane uses only Python
standard-library modules. The environment variables make the intended
deterministic, no-network posture visible; they are not a repository-wide
network sandbox.

The implementation also exposes a separate synthetic smoke check:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 KFM_NO_NETWORK=1 \
  python tools/experiments/temporal_slice_store.py --self-test
```

That command exercises one ambiguity-to-supersession path and emits compact
JSON. It is not collected by the test module, is not a substitute for the
eight tests, and must not be pointed at a production database.

## Contract and workflow relationship

The similarly named contract family is a separate proposed surface:

| Surface | Current responsibility | Relationship to this lane |
|---|---|---|
| [`contracts/data/temporal_slice.md`](../../contracts/data/temporal_slice.md) and its [schema](../../schemas/contracts/v1/data/temporal_slice.schema.json) | Proposed metadata meaning and machine shape for derived temporal views | The SQL experiment borrows identifiers and change concepts, but this lane does not prove schema compatibility |
| [`tests/validators/test_validate_temporal_slice.py`](../validators/test_validate_temporal_slice.py) | Contract fixture, identity, time, reference, and lineage validation | Separate test module; it does not import or exercise `TemporalSliceStore` |
| [`temporal-slice.yml`](../../.github/workflows/temporal-slice.yml) | Runs the contract validator tests, fixture polarity, and generated-receipt integrity | Does not include `tests/experiments/`, `tools/experiments/`, or this README in its path filters or commands |
| [`briefing-implementation-campaign.yml`](../../.github/workflows/briefing-implementation-campaign.yml) | Directly collects all eight experiment tests and runs the implementation self-test | Triggers for the experiment test and implementation paths, but not for this README; a README-only change leaves the lane `NOT_RUN` |

No current Make target names this experiment test. The shared
`briefing-implementation-campaign` workflow directly runs the eight-test module
and the implementation self-test when its experiment code or test path filters
match. Its filters do not include this README, so documentation-only changes do
not produce fresh hosted evidence for the lane. The separate `temporal-slice`
workflow does not collect the experiment and must not be reported as its result.

## Evidence and authority boundary

| A passing lane supports | It does not establish |
|---|---|
| The eight asserted behaviors for the checked implementation and synthetic records | Correctness for untested inputs, concurrency, durable storage, migration, backup, or recovery |
| Fail-closed ambiguity in the tested overlap | Complete temporal conflict resolution or policy evaluation |
| Partition isolation for the tested dataset/grid values | Tenant isolation, access control, privacy, sovereignty, or harmful-precision protection |
| Deterministic ordering for the tested changes | Real-world change, evidentiary weight, or source freshness |
| Rejection of the tested invalid records | Full contract or schema conformance |
| Default in-memory execution and standard-library imports | Production confinement or repository-wide network denial |

The default lifecycle remains
`RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`.
This experiment does not perform any lifecycle transition. References stored in
a synthetic row are strings only; the store does not resolve evidence or run
receipts, evaluate rights or sensitivity, authorize exposure, or publish an
artifact. Public clients must use governed interfaces or released public-safe
artifacts rather than this internal experiment.

## Failure interpretation

| Failure | First inspect | Do not infer automatically |
|---|---|---|
| Import or collection error | Repository root, Python version, module paths, and file movement | Temporal evidence is false |
| Expected index missing or renamed | SQL DDL and query-plan intent | The proposed contract schema failed |
| Boundary-time assertion fails | UTC normalization and half-open comparison operators | A source observation changed |
| Overlap returns one record | Supersession filter and ambiguity branch | Selection was authorized by policy |
| Change ordering differs | SQL `ORDER BY`, null handling, and fixture values | A material-change assessment is wrong |
| Invalid record reaches SQLite | Pre-insert validation and transaction boundary | Every persisted record is unsafe |
| `briefing-implementation-campaign` is absent on a README-only change | Confirm its path filters exclude this README, then use the last exact code/test-triggered run only as historical evidence | The experiment lane failed or that a fresh hosted run occurred |
| `temporal-slice` workflow passes | Inspect its commands and path filters | This experiment lane ran or passed |

Record the exact revision and command when reporting a failure. Keep test
failure separate from evidence correction, review, merge, promotion, release,
deployment, publication, and operational rollback decisions.

## Maintenance

Update this README in the same reviewable change when any of the following
changes materially:

- module or source-defined test inventory;
- SQL table, index, ordering, interval, partition, or supersession behavior;
- synthetic-input construction or an external fixture dependency;
- local command, Python requirement, or dependency profile;
- Make target, workflow command, path filter, or required-check status;
- contract/schema mapping or validator integration; or
- network, filesystem, lifecycle, rights, sensitivity, privacy, publication,
  or production posture.

Keep executable tests under `tests/` and experimental implementation under
`tools/experiments/` while that placement matches the accepted
[Directory Rules](../../docs/doctrine/directory-rules.md). The current
[`CODEOWNERS`](../../.github/CODEOWNERS) file confirms a review route; it does
not establish independent stewardship or prove that review occurred.

## Known gaps

- No Make target aggregates or names this lane.
- The shared briefing workflow collects the module and self-test, but its path
  filters do not include this README; documentation-only changes leave that
  focused execution `NOT_RUN`.
- Required-check status and accountable experiment stewardship are unknown.
- The static count is not a dependency-complete collection or execution
  receipt.
- Contract/schema compatibility and shared fixture parity are unproven.
- Concurrency, durable file-backed behavior, migrations, backup, restore,
  correction propagation, and operational rollback are untested.
- Production consumers, performance bounds, and public-client isolation are
  not established.

## Documentation correction and rollback

This file documents existing behavior and changes no test, implementation,
contract, schema, workflow, data, or release state. Before merge, close the
draft pull request or remove this new file from its feature branch. After an
authorized merge, revert the documentation commit or submit a forward
correction pinned to current repository evidence.

Removing this README does not roll back an experiment, database, lifecycle
object, release, deployment, promotion, or publication. Those require their
own governed correction paths.

[Back to top](#top)
