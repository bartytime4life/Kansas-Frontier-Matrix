# `tests/pipelines/` — Pipeline Test Inventory and Evidence Boundary

`tests/pipelines/` contains fixture-driven tests for three implemented domain
pipeline helpers. The tests exercise finite, local behavior; they do not fetch
live sources, write lifecycle stores, activate a source, or authorize review,
promotion, release, deployment, or publication.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-pipelines-readme
title: tests/pipelines/README.md — Pipeline Test Inventory and Evidence Boundary
type: readme; directory-readme; pipeline-test-index; enforceability-boundary
version: v0.3
status: draft; repository-grounded; three-executable-test-modules-confirmed; 23-source-defined-tests; three-workflow-bindings-confirmed
owners: "@bartytime4life — CONFIRMED CODEOWNERS review route; accountable pipeline-test stewardship UNKNOWN"
created: 2026-07-06
updated: 2026-08-30
supersedes: v0.2
policy_label: public-doctrine; tests; pipelines; fixture-only; non-publisher
current_path: tests/pipelines/README.md
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1ea6593ede80d5ce10f561c7eec72135d6ccf806
  target_prior_blob: 08fa70cd33af2c04f03aadbf7d973c6f4e29fbf3
  source_defined_test_count: 23
  executable_test_modules: 3
  empty_package_markers: 1
related:
  - ../README.md
  - ../../pipelines/README.md
  - ../../pipeline_specs/README.md
  - ../../fixtures/
  - ../../contracts/
  - ../../schemas/
  - ../../docs/doctrine/directory-rules.md
  - ../../.github/CODEOWNERS
  - ../../Makefile
notes:
  - "v0.3 corrects the obsolete README-only and no-dedicated-suite claims."
  - "Counts describe source-defined test functions at the pinned base commit, not a hosted collection receipt."
  - "The Makefile has no aggregate target for these modules at the pinned base commit."
  - "Each executable module is collected by a dedicated workflow, but those workflows exclude this parent README from their path filters."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

## Purpose and scope

This README helps maintainers find and run the implemented pipeline tests,
understand their dependencies, and interpret failures without expanding the
tests beyond what repository evidence supports.

The current lane has four Python files: an empty package marker and three
executable test modules defining 23 `test_*` functions. Earlier revisions
described the lane as README-only. That description is no longer true.

The tests are evidence about named implementation behavior. They are not the
authority for source meaning, contracts, schemas, pipeline specifications,
rights, sensitivity, lifecycle state, or release decisions.

## Current inventory

| Test module | Source-defined tests | System under test | Fixture or schema dependency |
|---|---:|---|---|
| [`domains/hydrology/test_wbd_huc12_ingest_candidate.py`](domains/hydrology/test_wbd_huc12_ingest_candidate.py) | 9 | [`produce_wbd_huc12_candidate.py`](../../pipelines/domains/hydrology/ingest_wbd_huc/produce_wbd_huc12_candidate.py) | [`fixtures/domains/hydrology/wbd_huc12_ingest/`](../../fixtures/domains/hydrology/wbd_huc12_ingest/) |
| [`domains/soil/mesonet_normalizer/test_fixture_normalizer.py`](domains/soil/mesonet_normalizer/test_fixture_normalizer.py) | 9 | [`fixture_normalizer.py`](../../pipelines/domains/soil/mesonet_normalizer/fixture_normalizer.py) | [`native_station_record.json`](../../fixtures/domains/soil/mesonet_normalizer/valid/native_station_record.json) |
| [`domains/soil/mesonet_station_health/test_evaluate_fixture.py`](domains/soil/mesonet_station_health/test_evaluate_fixture.py) | 5 | [`evaluate_fixture.py`](../../pipelines/domains/soil/mesonet_station_health/evaluate_fixture.py) | [`healthy_batch.json`](../../fixtures/domains/soil/mesonet_station_health/valid/healthy_batch.json) and [`mesonet_station_health.schema.json`](../../schemas/contracts/v1/domains/soil/mesonet_station_health.schema.json) |
| [`__init__.py`](__init__.py) | 0 | Package marker only | None |

The count is a static inventory of functions defined at the pinned base. It
does not establish current pass status, dynamic collection completeness, code
coverage, mutation coverage, production parity, or required-check status.

## What the modules prove

### WBD HUC12 ingest candidate

The hydrology module exercises deterministic captured-package projection:

- unchanged and HTTP-not-modified inputs produce bounded no-change receipts;
- material change, addition, and removal produce RAW candidates;
- duplicate HUC12 values and digest/spec-hash mismatches fail closed; and
- the CLI is deterministic, refuses to overwrite an existing output, and
  reports that network, lifecycle writes, activation, promotion, release, and
  publication are disabled.

Its six committed JSON fixtures cover one invalid duplicate case and five
valid add, remove, material-change, no-change, and not-modified cases. These
fixtures are captured test inputs, not admitted source observations.

### Mesonet fixture normalizer

The soil normalizer module exercises one synthetic station record. It checks
deterministic normalization, native cadence and context preservation, explicit
aggregation receipts, station-health holds, deny precedence, rights and
operator-consent restrictions, support-type separation, harmful-precision
rejection, and safe handling of non-object input.

The emitted candidate remains fixture-only and not promotion-eligible. A test
pass does not admit Mesonet data, establish current rights or consent, or make
the candidate public-safe outside the tested fixture boundary.

### Mesonet station health

The station-health module exercises one synthetic ten-station batch. It checks
determinism, Draft 2020-12 schema validity, the exact roster-degradation
threshold, anomaly holds, harmful-precision rejection, and safe handling of
non-object input.

The assessment is a fixture result. It is not evidence of live station health,
network availability, operational monitoring, or production readiness.

## Run the tests

From the repository root, install the same declared test dependency profile
used by all three dedicated workflows:

```bash
python tools/ci/install_python_ci.py project-test
```

Run the complete direct lane:

```bash
python -m pytest \
  tests/pipelines/domains/hydrology/test_wbd_huc12_ingest_candidate.py \
  tests/pipelines/domains/soil/mesonet_normalizer/test_fixture_normalizer.py \
  tests/pipelines/domains/soil/mesonet_station_health/test_evaluate_fixture.py \
  -q --strict-config --strict-markers
```

Run one module by passing only its path. The combined command is a convenient
local aggregate assembled from the three workflow commands; it is not a
current Make target or a claim that every pipeline test in the repository is
included.

The tests read committed fixtures and implementations. The hydrology CLI test
uses a pytest temporary directory for its output-safety assertion. Do not
replace these fixtures with live requests, credentials, private observations,
or exact sensitive locations.

## Hosted workflow bindings

| Workflow | Direct test command | Trigger coverage relevant to the module | Parent README trigger |
|---|---|---|---|
| [`hydrology-wbd-huc12-ingest-candidate.yml`](../../.github/workflows/hydrology-wbd-huc12-ingest-candidate.yml) | Hydrology module plus its material-change validator | Workflow, contract, pipeline spec, implementation, two schemas, fixtures, test module, generated receipt | No |
| [`soil-mesonet-fixture-normalizer.yml`](../../.github/workflows/soil-mesonet-fixture-normalizer.yml) | Normalizer module | Workflow, implementation file, fixture tree, test subtree, generated receipt | No |
| [`soil-mesonet-station-health.yml`](../../.github/workflows/soil-mesonet-station-health.yml) | Station-health module | Workflow, contract, schema, implementation tree, fixture tree, test subtree, generated receipt | No |

Each workflow installs the `project-test` dependency profile and invokes
pytest with strict configuration and marker handling. Each also validates a
named generated authoring receipt after the tests.

The workflow definitions establish collection intent, not a current hosted
result or branch-protection rule. Their pull-request path filters do not include
`tests/pipelines/README.md`; a documentation-only edit here therefore does not
exercise the three focused workflows unless another matching path changes.

## Evidence and authority boundary

| A passing test supports | It does not establish |
|---|---|
| Deterministic behavior for the committed fixture and named implementation | Live-source accuracy, freshness, completeness, or availability |
| The asserted finite outcome and reason codes | Policy adoption or semantic authority beyond accepted contracts |
| Schema validity where the station-health test invokes the schema | Complete semantic, rights, sensitivity, or release fitness |
| No lifecycle write or publication in the tested execution path | Repository-wide or production no-side-effect enforcement |
| Harmful-precision rejection for the tested latitude fields | Complete sensitive-location protection |
| Output overwrite refusal in the hydrology CLI case | A complete filesystem or operational rollback guarantee |
| A workflow definition that names and invokes a module | A passing run, required check, completed review, promotion, or release |

The default lifecycle remains
`RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`.
These tests inspect candidate or assessment behavior around that lifecycle;
they do not perform a lifecycle transition. Public clients must continue to use
governed interfaces or released public-safe artifacts rather than these test
fixtures, internal implementations, or candidate objects.

## Failure interpretation

| Failure | First inspect | Do not infer automatically |
|---|---|---|
| Import or collection error | Dependency installation, moved paths, Python compatibility | Domain evidence is wrong |
| Valid fixture fails | Fixture shape, implementation, contract/schema, threshold or reason-code drift | Source admission must be reversed |
| Invalid or restricted fixture passes | Fail-closed guard, fixture polarity, precedence logic | A policy decision has been approved |
| Schema assertion fails | Schema and assessment shape changes together | Live stations are unhealthy |
| Hydrology CLI output differs between runs | Serialization, ordering, time, or environment leakage | Publication or deployment failed |
| Focused workflow does not run | Pull-request path filters and changed paths | The module passed |
| Generated-receipt validation fails | Receipt path, validator, implementation/spec drift | The test module itself necessarily failed |

Preserve failing inputs when they are public-safe, report the exact command and
revision, and keep test failure separate from review, merge, promotion, release,
deployment, publication, correction, and operational rollback decisions.

## Maintenance

Update this README in the same reviewable change when any of the following
changes materially:

- direct module or source-defined test inventory;
- implementation, fixture, schema, contract, or pipeline-spec binding;
- local invocation or dependency profile;
- workflow command, path filter, job boundary, or generated-receipt check;
- network, filesystem, precision, rights, consent, lifecycle, or publication
  posture; or
- module placement, CODEOWNERS routing, or an accepted aggregate target.

Keep tests beside the lane only while that placement matches the accepted
[Directory Rules](../../docs/doctrine/directory-rules.md). Implementation stays
under `pipelines/`; declarative pipeline specifications stay under
`pipeline_specs/`; shared fixtures, contracts, schemas, policy, data objects,
and release decisions stay in their governed roots.

## Known gaps

- No Make target aggregates these three modules.
- The three focused workflow path filters exclude this parent README.
- Required-check status and accountable operational stewardship are unknown.
- The static count is not a dependency-complete collected-case receipt.
- This inventory does not prove complete pipeline, connector, package-local,
  domain-local, correction, rollback, or production coverage.
- Live-source behavior, production filesystem confinement, and operational
  rollback have not been established by this lane.

## Documentation correction and rollback

This revision changes documentation only. Before merge, close the draft pull
request or restore prior blob
`08fa70cd33af2c04f03aadbf7d973c6f4e29fbf3` on the feature branch. After merge,
revert the documentation commit or submit a correction pinned to current
repository evidence.

Reverting this README does not revert a pipeline, fixture, workflow, lifecycle
object, release, deployment, or publication. Those require their own governed
correction and rollback paths.

[Back to top](#top)
