<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/connector-query-input-validation
title: Connector Query Input Validation
type: runbook
version: v0.1.0
status: repository-grounded; offline-regression-backed
owners: OWNER_TBD — Connector steward · GBIF steward · BLM steward · NRCS steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; no-source-activation; no-network-tests
owning_root: docs/
responsibility: reproduce finite planner errors for malformed GBIF, BLM and NRCS inputs
truth_posture: CONFIRMED reproduced query-planner defects and bounded source fixes; NEEDS VERIFICATION hosted CI and any operational caller impact
[/KFM_META_BLOCK_V2] -->

# Connector query input validation

These repairs concern malformed programmatic inputs to three offline request
planners. They do not change valid query encodings, bounds, source scope, transport,
source-role/rights decisions, candidate routing, activation or lifecycle authority.
No provider request or deployed failure was demonstrated.

## Reproductions and repairs

| Planner | Reproduced behavior before repair | Result after repair |
|---|---|---|
| [GBIF](../../connectors/gbif/src/gbif/occurrence_api.py) | Non-string country input reached regex; dictionary/list basis inputs reached set membership and raised raw TypeError. Null required state scope encoded as literal stateProvince=None. | Validate country/basis types first; require non-null state text. Raise finite COUNTRY_CODE, BASIS_OF_RECORD or TEXT_SHAPE. |
| [BLM](../../connectors/blm/src/blm/plss_cadnsdi.py) | Dictionary/list layers raised unhashable TypeError in page/count planning and count-response entry validation. | Require a recognized string layer before dictionary membership; raise finite LAYER. |
| [NRCS SCAN](../../connectors/nrcs/src/nrcs/scan_awdb.py) | Dictionary/list tuple members reached set construction before member validation; dictionary/list durations reached mapping membership. | Validate station/element members before duplicate checks and require a string duration; raise finite STATION, ELEMENT or DURATION. |

Some already-invalid scalar cases previously had finite errors; the regressions
retain those alongside the newly repaired container cases. Existing canonical URL,
round-trip, duplicate, page/window/date bounds, parsing and injected transport tests
continue to run. Optional GBIF basis remains optional; required state scope does not.

## Reproduce validation

Use Python 3.11 or 3.12. The complete source suites are standard-library unittest
cases; adapters import the existing connectors-core source shim. Run from the
repository root with the Python network guard:

```bash
export KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
python -B -m unittest discover -s connectors/gbif/tests -p 'test_*.py' -v
python -B -m unittest discover -s connectors/blm/tests -p 'test_*.py' -v
python -B -m unittest discover -s connectors/nrcs/tests -p 'test_*.py' -v
```

The focused [GBIF](../../connectors/gbif/tests/test_occurrence_api.py),
[BLM](../../connectors/blm/tests/test_plss_cadnsdi.py) and
[NRCS](../../connectors/nrcs/tests/test_scan_awdb.py) modules can also run through
the existing locked project-test pytest profile. All three new regression methods
fail against the unmodified parent; they pass after these narrow guards.

Existing [GBIF](../../.github/workflows/gbif-occurrence-offline.yml),
[BLM](../../.github/workflows/blm-connector-offline.yml) and
[NRCS](../../.github/workflows/nrcs-connector-offline.yml) workflows already watch
the changed source/tests and run their complete suites on Python 3.11 and 3.12.
No workflow, dependency, permission or source descriptor changes are needed.

## Proof and correction boundary

These tests prove finite rejection and preserve supported request behavior. They
are not source authentication, a live fetch, descriptor admission, survey/title
review, station review, sensitivity approval, pipeline activation or deployment.
Revert this bounded commit through review if correction is needed; preserve the
new authoring receipt and older source evidence. No migration is involved.
