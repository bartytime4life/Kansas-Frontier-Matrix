<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/openfema-fixture-ingest
title: OpenFEMA Fixture Ingest
type: runbook
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Hazards steward · FEMA source steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-administrative-context; not-for-life-safety; no-eligibility-authority
owning_root: docs/
responsibility: explain deterministic administrative-context walk checks and their limits
truth_posture: CONFIRMED bounded supplied-page replay; PROPOSED candidate profile; NEEDS VERIFICATION human review, source admission and any downstream use
[/KFM_META_BLOCK_V2] -->

# OpenFEMA fixture ingest

The [implementation](../../pipelines/domains/hazards/openfema_ingest.py) composes
the existing FEMA page parser and counted keyset reconciler into private held
administrative-context candidates. It never fetches, schedules, stores or publishes.

## Reproduce

Use Python 3.11 or 3.12 with the existing locked profiles:

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_python_ci.py connectors-core
export KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
python -B -m pipelines.domains.hazards.openfema_ingest complete
python -B -m pipelines.domains.hazards.openfema_ingest count-drift
python -B -m pipelines.domains.hazards.openfema_ingest empty
python -B -m unittest discover -s connectors/fema/tests -p 'test_*.py' -v
python -B -m pytest tests/pipelines/domains/hazards/test_openfema_ingest.py -q --strict-config --strict-markers
```

All three CLI commands return aggregate `HOLD`. The complete supplied walk has
three invented administrative records, including one explicit quarantine and two
flagged records. The drifting case retains the same records but is incomplete.
The empty case has zero records and unestablished coverage. These are not FEMA
declarations, hazard footprints, absence evidence or eligibility decisions.

## Source repairs

The existing parser previously dropped `.123` source and `.456` capture fractions
when formatting timestamps. It now preserves them through UTC normalization.
It also accepted Boolean/floating-point `skip` and `top` metadata through numeric
equality; these fields now require actual integers where present. Source and
pipeline regression tests retain evidence of both defects and their fixes.

## Input and proof boundaries

The [contract](../../contracts/domains/hazards/openfema_ingest_candidate.md) gives
all byte, page, count and output limits. Requests must be canonical Kansas planner
URLs. Invalid metadata, non-200 responses, temporal inconsistencies and oversized
inputs are refused. Missing cursor links or terminal pages and inconsistent
remaining counts become explicit incomplete captures. No response is truncated.

An internally consistent reported walk is not a provider snapshot or completeness
proof. Unknown record fields remain source-faithful and flagged; unknown incident
ends remain null. Exact original body hashes stay separate from provider `hash`
fields. Caller-supplied real bodies and record snapshots require private handling;
the CLI exposes only aggregate status and writes no files.

The existing proposed domain descriptor remains unresolved even though the family
connector's provisional routing is implemented. Rights, sensitivity, source
admission, live keyset support, persistence, evidence closure, release and any
public use require separate review.

## CI and correction

The [dedicated workflow](../../.github/workflows/openfema-pipeline.yml) installs
locked profiles, runs the full FEMA connector suite, declaration checks, new
intake tests and all three goldens under the Python network guard on 3.11/3.12.
The existing FEMA offline workflow continues to qualify source-level changes.
Local tests, hosted CI, main merge and deployed/runtime source behavior remain
separate evidence lanes. Roll back the bounded commit through a reviewed revert;
retain the earlier source-authoring and nesting-bound receipts unchanged.
