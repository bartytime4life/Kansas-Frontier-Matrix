<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://tests/map/readme
title: Map Assessment Test Lane
type: test-lane-readme
version: v0.1.0
status: draft; repository-grounded; synthetic-fixture-only; no-network; six-module-inventory; 74-source-defined-tests
owners: @bartytime4life — CONFIRMED CODEOWNERS review route; accountable map assessment stewardship UNKNOWN
created: 2026-08-30
updated: 2026-08-30
policy_label: repository-facing; tests; map; non-publisher
owning_root: tests/
responsibility: Document the bounded synthetic proof surface for implemented georeference, IIIF overlay, and map release-manifest assessments.
truth_posture: cite-or-abstain
evidence_base: c50f28749ff34a3c8349cabea5d58f1da5b805f1
[/KFM_META_BLOCK_V2] -->

# Map assessment test lane

`tests/map/` contains six executable modules with 74 source-defined tests over
95 synthetic fixture cases. Five modules assess bounded georeference or historic
overlay readiness. One checks the fixture-first `MapReleaseManifest` profile.

Passing these tests proves only deterministic behavior against the checked-in
contracts, schemas, fixtures, and helper implementations. It does not authenticate
control points, fetch or georeference imagery, resolve evidence or rights, evaluate
policy, release a map, invalidate a cache, deploy a service, or publish data.

## Inventory

| Test module | Tests | Fixture cases and expected polarity |
| --- | ---: | --- |
| [`test_georeference_control_point_evidence_assessment.py`](test_georeference_control_point_evidence_assessment.py) | 14 | [34 cases](../../fixtures/contracts/v1/map/georeference_control_point_evidence_assessment/cases.json): 1 `PASS`, 8 `ABSTAIN`, 19 `DENY`, 6 `ERROR` |
| [`test_georeference_control_point_set.py`](test_georeference_control_point_set.py) | 11 | [11 cases](../../fixtures/contracts/v1/map/georeference_control_point_set/cases.json): 2 `VALID`, 9 `ERROR` |
| [`test_georeference_spatial_distribution.py`](test_georeference_spatial_distribution.py) | 11 | [11 cases](../../fixtures/contracts/v1/map/georeference_spatial_distribution/cases.json): 1 `READY`, 3 `HOLD`, 7 `ERROR` |
| [`test_georeference_transform_quality.py`](test_georeference_transform_quality.py) | 10 | [10 cases](../../fixtures/contracts/v1/map/georeference_transform_quality/cases.json): 2 `READY`, 3 `HOLD`, 5 `ERROR` |
| [`test_iiif_historic_overlay_readiness.py`](test_iiif_historic_overlay_readiness.py) | 11 | [11 cases](../../fixtures/contracts/v1/map/iiif_historic_overlay_readiness/cases.json): 1 `READY`, 3 `HOLD`, 3 `DENY`, 4 `ERROR` |
| [`test_map_release_manifest.py`](test_map_release_manifest.py) | 17 | [18 cases](../../fixtures/contracts/v1/map/map_release_manifest/cases.json): 7 valid, 11 invalid |

The test count is the number of `test_*` functions or `unittest` methods defined
in these six files. It is not a claim about every case collected by a broader
repository test command.

## Implementation bindings

| Assessment | Validator | Contract | Schema |
| --- | --- | --- | --- |
| Control-point evidence | [validator](../../tools/validators/map/validate_georeference_control_point_evidence_assessment.py) | [contract](../../contracts/map/georeference_control_point_evidence_assessment.md) | [schema](../../schemas/contracts/v1/map/georeference_control_point_evidence_assessment.schema.json) |
| Control-point-set identity | [validator](../../tools/validators/map/validate_georeference_control_point_set.py) | [contract](../../contracts/map/georeference_control_point_set.md) | [schema](../../schemas/contracts/v1/map/georeference_control_point_set.schema.json) |
| Spatial distribution | [validator](../../tools/validators/map/validate_georeference_spatial_distribution.py) | [contract](../../contracts/map/georeference_spatial_distribution.md) | [schema](../../schemas/contracts/v1/map/georeference_spatial_distribution.schema.json) |
| Transform quality | [validator](../../tools/validators/map/validate_georeference_transform_quality.py) | [contract](../../contracts/map/georeference_transform_quality.md) | [schema](../../schemas/contracts/v1/map/georeference_transform_quality.schema.json) |
| IIIF historic-overlay readiness | [validator](../../tools/validators/map/validate_iiif_historic_overlay_readiness.py) | [contract](../../contracts/map/iiif_historic_overlay_readiness.md) | [schema](../../schemas/contracts/v1/map/iiif_historic_overlay_readiness.schema.json) |
| Map release manifest | [validator](../../tools/validators/map/validate_map_release_manifest.py) | [canonical semantic contract](../../contracts/release/map_release_manifest.md) | [schema](../../schemas/contracts/v1/map/map_release_manifest.schema.json) |

The map release tests also verify the compatibility
[contract pointer](../../contracts/map/map_release_manifest/README.md) and the
[map schema-family README](../../schemas/contracts/v1/map/README.md). Those
references do not create a second semantic authority.

## Covered boundaries

### Georeference control points

The control-point modules check:

- deterministic resource, target, and complete-set identities;
- canonical point ordering and numeric normalization;
- exact evidence-summary derivation and upstream set binding;
- visibility, contrast, scale, matching, and reference posture;
- resource-space hull coverage, extrapolation, centroid offset, and quadrant
  occupancy;
- affine coefficients, residuals, leave-one-out quality, and redundancy; and
- fail-closed handling for duplicate keys, non-finite values, symlinks,
  malformed geometry, identity drift, and declared-metric mismatch.

A `PASS` or `READY` result means only that the synthetic candidate reached the
assessment's review boundary. It does not prove coordinate accuracy or authorize
a warp, release, or publication.

### IIIF historic overlays

The IIIF module checks exact embedded annotation-byte digests, GCP and mask
coherence, finite decision precedence, IIIF 2.1 normalization references,
presentation-API readiness, plugin declarations, and consent requirements for
CARE authority claims. It performs no live IIIF request or remote JSON-LD
validation.

### Map release manifests

The manifest module checks deterministic identity, immutable artifact metadata,
catalog/evidence/policy/review/attestation references, rights and sensitivity
posture, public-boundary denial, correction, cache-invalidation, and rollback
closure. Its `PUBLISHED` fixture is synthetic test input, not evidence that a map
was released or published.

## Run locally

From the repository root, run the focused tests with the same collectors used by
the dedicated workflows:

```bash
python -m pytest -q tests/map/test_georeference_control_point_evidence_assessment.py
python -m pytest -q tests/map/test_georeference_control_point_set.py
python -m pytest -q tests/map/test_georeference_spatial_distribution.py
python -m pytest -q tests/map/test_georeference_transform_quality.py
python -m pytest -q tests/map/test_iiif_historic_overlay_readiness.py
python -m unittest tests.map.test_map_release_manifest --verbose
```

Replay every reviewed fixture matrix:

```bash
python tools/validators/map/validate_georeference_control_point_evidence_assessment.py --fixtures
python tools/validators/map/validate_georeference_control_point_set.py --fixtures
python tools/validators/map/validate_georeference_spatial_distribution.py --fixtures
python tools/validators/map/validate_georeference_transform_quality.py --fixtures
python tools/validators/map/validate_iiif_historic_overlay_readiness.py --fixtures
python tools/validators/map/validate_map_release_manifest.py --fixtures
```

The repository `Makefile` has no target that names or collects this complete
six-module lane. Use the focused commands when changing the lane.

## Hosted workflow coverage

| Workflow | Test collector |
| --- | --- |
| [`map-georeference-control-point-evidence`](../../.github/workflows/map-georeference-control-point-evidence.yml) | focused `pytest` module plus fixture replay |
| [`map-georeference-control-point-set`](../../.github/workflows/map-georeference-control-point-set.yml) | focused `pytest` module plus fixture replay |
| [`map-georeference-spatial-distribution`](../../.github/workflows/map-georeference-spatial-distribution.yml) | focused `pytest` module plus fixture replay |
| [`map-georeference-transform-quality`](../../.github/workflows/map-georeference-transform-quality.yml) | focused `pytest` module plus fixture replay |
| [`map-iiif-historic-overlay-readiness`](../../.github/workflows/map-iiif-historic-overlay-readiness.yml) | focused `pytest` module plus fixture replay |
| [`map-release-manifest`](../../.github/workflows/map-release-manifest.yml) | focused `unittest` module plus fixture replay |

All six workflows use Python 3.11, read-only repository permissions,
`KFM_NO_NETWORK=1`, and the declared project-test dependency profile. Each also
validates a checked-in generated authoring receipt.

None of their path filters includes `tests/map/README.md`. A README-only change
therefore does not collect any of the six focused modules in hosted CI. Treat that
as unavailable focused evidence, not a pass. Documentation, link, metadata, and
repository-wide checks may still run.

## Safety and authority boundary

| Evidence from this lane | What it does not establish |
| --- | --- |
| Synthetic fixtures match their reviewed finite outcomes | Truth of a real map, source, location, control point, or overlay |
| Schemas are meta-valid and validators fail closed for covered cases | Complete semantic coverage or production parity |
| Covered helpers avoid live network and geospatial execution runtimes | Runtime confinement outside the tested process |
| Stored receipts agree with their declared artifacts when validated | Current source rights, independent review, release, or publication |
| Release fixtures exercise correction and rollback fields | An operational correction, cache invalidation, or rollback rehearsal |

Evidence, provenance, source rights, sensitivity, sovereignty, privacy, harmful
precision, policy, review, correction, release, and rollback remain separate
requirements. A test result or generated receipt cannot grant those states.

## Interpreting failures

1. For a fixture mismatch, inspect the test, validator, contract, schema, and
   named fixture case together before changing the expected outcome.
2. Treat an unexpected permissive result as safety-significant and hold
   downstream use until evidence, rights, sensitivity, authority, and public
   boundary fields are reconciled.
3. Treat identity, digest, metric, geometry, or schema drift as a fail-closed
   contract disagreement rather than silently recalculating the expected value.
4. Treat a workflow that did not run as unavailable evidence.
5. Keep reproductions synthetic; do not substitute real identities, precise
   sensitive locations, restricted imagery, or live service credentials.

## Maintenance

When this lane changes:

- keep each test, validator, contract, schema, fixture, and workflow binding
  synchronized;
- update test and fixture counts only from current repository evidence;
- preserve finite outcomes, deterministic identity, no-network execution, and
  non-publisher authority;
- add synthetic positive and negative cases for new decision branches; and
- record workflow collection gaps explicitly.

Current unresolved gaps are parent-README path-filter coverage, a complete-lane
Make target, required-check status, complete semantic coverage, production
confinement, independent stewardship, source-rights review, operational
correction propagation, and rollback rehearsal.

## Rollback

This README changes no validator, contract, schema, fixture, workflow, receipt,
runtime, release, or publication state. Before merge, rollback is closing the
pull request or reverting its documentation commit.
