<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://tests/generators/readme
title: Generator Test Lane
type: readme; directory-readme; test-index
version: v0.1.0
status: draft; repository-present-executable-tests
policy_label: public-doc
owners: CODEOWNERS review route @bartytime4life; accountable stewardship UNKNOWN
created: 2026-08-30
updated: 2026-08-30
current_path: tests/generators/README.md
truth_posture: CONFIRMED from current repository files at main@a98eb4b20c0c003087a9953df5ea0d609cbe0d28; hosted collection for this README-only change NEEDS VERIFICATION
related:
  - ../README.md
  - ../../tools/generators/
  - ../../.github/CODEOWNERS
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, tests, generators, deterministic, no-network, write-safety]
notes:
  - This is a human-maintained test-lane index, not a generated artifact or authority record.
[/KFM_META_BLOCK_V2] -->

# Generator test lane

`tests/generators/` verifies four repository generators that turn bounded local
inputs into deterministic candidate projections or reviewer indexes. This lane
helps maintainers find the implementation, fixtures, commands, and hosted
workflow for each suite without treating generated output as policy, evidence,
release approval, or published truth.

The directory is executable conformance evidence under the canonical `tests/`
responsibility root. Generator implementations remain under
[`tools/generators/`](../../tools/generators/), while contracts, schemas, and
fixtures retain their own authority.

## Current inventory

| Test module | Tests | Generator under test | Primary behavior |
| --- | ---: | --- | --- |
| [`governance_health/test_compile_governance_health_projection.py`](./governance_health/test_compile_governance_health_projection.py) | 9 | [`compile_governance_health_projection.py`](../../tools/generators/governance_health/compile_governance_health_projection.py) | Compiles bounded governance observations into a schema-valid, non-authoritative health projection. |
| [`test_build_output_lane_split.py`](./test_build_output_lane_split.py) | 10 | [`build_output_lane_split.py`](../../tools/generators/build_output_lane_split.py) | Validates an output-lane manifest and optionally writes payload-free reviewer indexes. |
| [`test_build_soil_yearly_diff.py`](./test_build_soil_yearly_diff.py) | 8 | [`build_soil_yearly_diff.py`](../../tools/generators/build_soil_yearly_diff.py) | Builds a fixture-only, canonical yearly soil-diff candidate with source-role and year guards. |
| [`test_project_georeference_transform_quality.py`](./test_project_georeference_transform_quality.py) | 7 | [`project_georeference_transform_quality.py`](../../tools/generators/project_georeference_transform_quality.py) | Projects an accepted synthetic control-point set into a deterministic transform-quality candidate. |

The four modules define **34 tests** in current source. That number describes
test functions and `unittest` methods in the files; it is not a claim about
hosted collection, required-check status, or production coverage.

## Contract and fixture map

| Suite | Contract or profile | Schema and fixtures | Dedicated workflow |
| --- | --- | --- | --- |
| Governance health | [`governance_health_projection.md`](../../contracts/governance/governance_health_projection.md) | [`governance_health_projection.schema.json`](../../schemas/contracts/v1/governance/governance_health_projection.schema.json) and three fixture cases in [`cases.json`](../../fixtures/contracts/v1/governance/governance_health_projection/cases.json) | [`governance-health-projection.yml`](../../.github/workflows/governance-health-projection.yml) |
| Output-lane split | [`output_lane_split_manifest.md`](../../contracts/data/output_lane_split_manifest.md) | [`output_lane_split_manifest.schema.json`](../../schemas/contracts/v1/data/output_lane_split_manifest.schema.json) and nine polarity cases in [`cases.json`](../../fixtures/contracts/v1/data/output_lane_split_manifest/cases.json) | [`output-lane-splitter.yml`](../../.github/workflows/output-lane-splitter.yml) |
| Soil yearly diff | [`ssurgo_yearly_diff_profile.md`](../../contracts/domains/soil/ssurgo_yearly_diff_profile.md) | [`ssurgo_yearly_diff_profile.schema.json`](../../schemas/contracts/v1/domains/soil/ssurgo_yearly_diff_profile.schema.json) and two synthetic snapshots under [`yearly_diff/snapshots/`](../../fixtures/domains/soil/yearly_diff/snapshots/) | [`soil-ssurgo-yearly-diff.yml`](../../.github/workflows/soil-ssurgo-yearly-diff.yml) |
| Georeference quality | [`georeference_control_point_set.md`](../../contracts/map/georeference_control_point_set.md) and [`georeference_transform_quality.md`](../../contracts/map/georeference_transform_quality.md) | The corresponding schemas and bounded inputs under [`fixtures/contracts/v1/map/`](../../fixtures/contracts/v1/map/) | [`map-georeference-quality-projection.yml`](../../.github/workflows/map-georeference-quality-projection.yml) |

These links establish implementation relationships only. A passing generator
test does not establish that an input is authentic, rights-cleared, current,
public-safe, or approved for a later lifecycle state.

## Run the tests

Install the repository's declared project-test dependencies, then run the
complete directory collector:

```bash
python tools/ci/install_python_ci.py project-test
python -m pytest -q tests/generators
```

To reproduce the collectors used by the dedicated workflows:

```bash
python -m pytest -q tests/generators/governance_health/test_compile_governance_health_projection.py --strict-config --strict-markers
python -m unittest tests.generators.test_build_output_lane_split -v
python -m unittest tests.generators.test_build_soil_yearly_diff --verbose
python -m unittest tests.generators.test_project_georeference_transform_quality --verbose
```

The repository `Makefile` does not currently expose one target that collects all
four suites. Use the commands above rather than assuming a generator-lane Make
target exists.

## Replay bounded generator inputs

The dedicated workflows also exercise the generators directly:

```bash
python tools/generators/governance_health/compile_governance_health_projection.py --fixtures
python tools/generators/build_output_lane_split.py --fixtures
python tools/generators/build_soil_yearly_diff.py fixtures/domains/soil/yearly_diff/snapshots/ssurgo-2025.json fixtures/domains/soil/yearly_diff/snapshots/ssurgo-2026.json
python tools/generators/project_georeference_transform_quality.py fixtures/contracts/v1/map/georeference_control_point_set/valid.json fixtures/contracts/v1/map/georeference_transform_quality/projection_request.json
```

These invocations use tracked synthetic or fixture-only inputs. Do not replace
them with real source payloads merely to run the test lane.

## Output and write safety

| Generator | Default mode | Explicit write behavior |
| --- | --- | --- |
| Governance health projection | Prints a projection to standard output. | No file-writing option is implemented. |
| Output-lane splitter | Validates or prints a split result without moving or copying referenced payload bytes. | `--write --output-dir PATH` writes six JSON reviewer indexes only and refuses a nonempty destination. |
| Soil yearly-diff builder | Prints a candidate result to standard output. | `--write PATH` creates one result; an existing file is refused unless `--force` is supplied. |
| Georeference quality projection | Prints a candidate projection to standard output. | `--write PATH` creates one projection; an existing file is refused unless `--force` is supplied. |

Use temporary destinations for test execution. Generated test output does not
belong in canonical contract, evidence, receipt, proof, release, or published
homes unless a separate governed process admits it there.

## Network and authority boundary

The output-lane, soil yearly-diff, and georeference suites explicitly replace
socket entry points and fail if the tested operation attempts network access.
Their workflows also set `KFM_NO_NETWORK=1`. The governance-health compiler
reads local fixture and schema files and its workflow sets the same environment
flag, but its current suite does not include an explicit socket-denial test.

None of these suites may:

- activate or retrieve a source;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED state;
- make a policy or evidence-resolution decision;
- authenticate control points or establish geodetic truth;
- promote, release, deploy, publish, or authorize public use;
- turn a projection, index, test result, or generated receipt into sovereign truth.

## Workflow coverage

Each module has a dedicated workflow that installs the declared Python test
dependencies and runs its focused collector. The workflows use Python 3.11,
read-only repository permissions, and `KFM_NO_NETWORK=1`.

The current pull-request path filters cover the exact test modules (or the
`governance_health/` child directory), implementations, fixtures, schemas, and
contracts. They do **not** include `tests/generators/README.md`. A README-only
change therefore does not directly trigger these four focused workflows.

Workflow presence or a green run proves only the behavior actually collected.
It does not establish required-check status, complete generator coverage,
production execution, or operational approval.

## Failure interpretation

Start with the first failing layer:

1. Dependency installation failure: classify the environment or dependency
   issue before interpreting generator behavior.
2. Import or compile failure: inspect the generator path and declared package
   dependencies.
3. Fixture or schema failure: preserve the failing input and stable reason; do
   not weaken the negative case to make the suite green.
4. Determinism or hash failure: compare canonical input bytes, ordering, and the
   repository hashing profile.
5. Write-safety failure: stop and inspect the destination before retrying;
   never delete or overwrite unrelated content.
6. Network-denial failure: treat the attempted connection as a boundary breach,
   not as permission to enable live access.

## Maintenance

When a generator, fixture family, contract, schema, or workflow changes:

1. update the matching inventory row and command;
2. keep positive and negative fixture counts accurate;
3. preserve default no-write behavior and overwrite guards;
4. keep network and authority assertions explicit;
5. update workflow path filters when files move or new suites are added;
6. validate relative links and the complete directory collector;
7. record unsupported or uncollected behavior as a gap rather than implied proof.

Review routing comes from [CODEOWNERS](../../.github/CODEOWNERS). That route does
not prove review occurred or assign accountable stewardship. Placement and
authority follow [Directory Rules](../../docs/doctrine/directory-rules.md).

## Known gaps

- No complete-lane Make target is present.
- The root README is outside all four focused workflow path filters.
- The governance-health suite lacks an explicit socket-denial regression.
- Required-check status and independent stewardship are unverified.
- Complete generator coverage, production consumers, correction propagation,
  and operational rollback are unverified.

