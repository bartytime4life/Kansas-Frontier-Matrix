<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/hydrology/drought-multiclock
title: Synthetic drought multi-clock rehearsal
type: readme
version: v1.0
status: draft; synthetic-only; non-authoritative
owner: "@bartytime4life — review route; accountable domain acceptance pending"
created: 2026-11-17
updated: 2026-11-17
policy_label: repository-facing
owning_root: fixtures/
responsibility: Document immutable synthetic inputs for the issue-specific drought observation, successor forecast and correction rehearsal.
truth_posture: "CONFIRMED bounded fixture behavior; UNKNOWN live authority, cadence and rights; independent acceptance pending"
[/KFM_META_BLOCK_V2] -->

# Synthetic drought multi-clock rehearsal

This is the bounded fixture slice for
[#3390](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3390)
and [#2899](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2899),
following the temporal replay integrated through
[#5888](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5888).
Every identity and payload digest is synthetic. The July/August/November dates
illustrate the issue's separated clocks; they do not assert real source content,
an official issuance instant, a condition, or admitted geography.

## Inputs and existing consumers

| File | Purpose |
|---|---|
| [observations.json](observations.json) | Seven source records evaluated at the frozen August 17 checkpoint, with native support, units, method, precision and separate observation/valid/publication/retrieval fields. |
| [forecast.json](forecast.json) | A separately identified ForecastProduct: cutoff August 18, issue August 20, retrieval August 21 and validity through November 30; uncertainty remains unknown and geometry unresolved. |
| [correction.json](correction.json) | A corrected streamflow record retaining observation/validity/support fields and explicitly referencing its original source version. |
| [bindings.json](bindings.json) | Rehearsal metadata: exact input digests, both evaluation times, source-correction time and unknown uncertainty. This is not a governed migration or release receipt. |

The [rehearsal runner](../../../../../tools/validators/evidence/rehearse_drought_multiclock.py)
constructs in-memory candidates for the existing
[WesternKansasObservationAssessment](../../../../../contracts/domains/hydrology/western_kansas_observation_assessment.md)
and [ForecastProduct](../../../../../contracts/common/forecast_product.md)
validators. It checks 27 exact outcomes; a negative case cannot pass merely by
returning a nonzero exit. The [tests](../../../../../tests/validators/test_drought_multiclock_replay.py)
also change bindings, clock values, identity, source support and confidence to
verify that an invalid proof is refused. The earlier independent
[case matrix](../cases.json) remains unchanged.

## Source-family boundary

| Family | Synthetic support / method | Permitted bounded claim |
|---|---|---|
| USDM | Polygon; categorical classification | Classification only; no groundwater condition. |
| USGS_STREAMFLOW | Station; provisional mean, then explicit correction | Streamflow at that station; no aquifer inference. |
| KGS_GROUNDWATER | Point; synthetic well measurement | Groundwater at the declared support only. |
| PRECIP_EDDI | 12 km grid cell; evaporative-demand index | Demand context; no crop-loss inference. |
| SOIL_MOISTURE | 9 km grid cell; explicit synthetic estimate method | Soil-moisture context; no crop-loss inference. |
| AGRICULTURE_CONTEXT | County aggregate context | Context only, preserving its aggregate support. |
| WATER_MANAGEMENT_BOUNDARY | Management-area reference geometry | Reference context only; no condition or cause. |

For **every family**, live authority and cadence are `NOT_ASSESSED`, rights are
`UNKNOWN`, and uncertainty is `NOT_PROVIDED` with a null value. These synthetic
checks do not complete the live seven-family matrix or quantify uncertainty.
The report retains those limitations rather than borrowing another family's
cadence, rights, precision or confidence.

## Behavior proved

Each family is evaluated separately against its directly supported claim. A
two-source soil/EDDI context retains both tuple evidence references and source
supports. Declared conflict remains `CONFLICT`; it does not select a winner.
A recent publication/retrieval still returns `STALE` for an old observation
under the declared seven-day view. Missing or superseded sources remain
`ABSTAIN`; neither becomes zero or normal.

The successor forecast is **context only**. It cannot correct or refresh the
observation history, become direct measurement, or upgrade unknown confidence.
Its future valid end is allowed; an issuance or retrieval after the evaluation
checkpoint is refused. Source cutoff is not copied into each observation time.

The separate streamflow correction binds the prior source version and input
digest, preserves fractional timestamps and native support, and produces a new
tuple digest. Source-correction, corrected publication and retrieval times stay
distinct. This is an in-memory correction rehearsal, not a persisted migration.
The prior fixture bytes are read back unchanged. Withdrawal and rollback are
covered separately by the existing temporal release rehearsal; no store is
created here.

USDM/streamflow-to-groundwater, soil/EDDI-to-crop-loss, boundary-to-condition,
county-uniformity, causal-attribution, support-erasure and missing-tuple cases
retain exact abstain/error outcomes. These checks do not adjudicate real
conflict, establish spatial overlap, or provide an agricultural-loss finding.

## Run and interpret

```bash
python tools/ci/install_python_ci.py project-test
PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD" KFM_NO_NETWORK=1 \
  python tools/validators/evidence/rehearse_drought_multiclock.py --fixtures
PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD" KFM_NO_NETWORK=1 \
  python -m pytest -q tests/validators/test_drought_multiclock_replay.py
```

The CLI accepts only `--fixtures`. `PASS`/0 means this fixed rehearsal passed;
`FAIL`/1 is a bounded proof mismatch; `ERROR`/2 means the proof was unavailable.
Output binds input, schema and consumer hashes. It is deterministic for the
same bytes and has no network, file-write or production-store interface.
The [dedicated workflow](../../../../../.github/workflows/western-kansas-observation-assessment.yml)
runs the focused suites and CLI under the Python process network guard.

Real evidence closure, live source authority/cadence/rights, quantitative
uncertainty propagation, authenticated API/UI/AI replay and independent
acceptance remain open. All authority flags stay false. Source admission,
data activation, lifecycle writes, policy, review, release and public use are
not granted by a fixture result.

Rollback is a focused revert or forward correction of this additive rehearsal,
retaining historical receipts and predecessor bytes. No production state needs
restoration. Directory Rules assign the reusable inputs to `fixtures/`, checking
code to `tools/`, conformance to `tests/` and CI to `.github/`; no semantic,
schema, policy or proof authority is added.
