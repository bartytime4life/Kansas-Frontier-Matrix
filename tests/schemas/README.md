<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-schemas-readme
title: tests/schemas/ — Executable schema conformance and anti-collapse tests
type: README; directory-readme; schema-test-lane; executable-inventory
version: v0.5
status: draft; repository-grounded; executable-partial; workflow-bound; no-network-by-default; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; schema, contract, fixture, QA, security, and release stewardship remain NEEDS VERIFICATION"
created: 2026-07-07
updated: 2026-08-30
supersedes: v0.4 documentation at the same path
policy_label: repository-facing; tests; schemas; contracts; fixtures; anti-collapse; no-network; fail-closed
current_path: tests/schemas/README.md
owning_root: tests/
responsibility: executable conformance checks for selected schemas, fixtures, validators, and schema-adjacent governance boundaries
truth_posture: a passing test supports only its named assertion at the checked revision; it does not establish semantic truth, source authority, evidence closure, policy approval, rights or sensitivity clearance, release, deployment, or publication
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1ea6593ede80d5ce10f561c7eec72135d6ccf806
  direct_test_modules: 11
  source_defined_tests: 137
  aggregate_compatibility_validators: 9
  direct_workflow_binding: .github/workflows/schema-validation.yml
related:
  - ../README.md
  - ../contracts/README.md
  - ../../schemas/README.md
  - ../../schemas/contracts/v1/README.md
  - ../../contracts/README.md
  - ../../fixtures/README.md
  - ../../tools/validators/README.md
  - ../../tools/validators/_common/run_all.py
  - ../../tools/validators/_common/jsonschema_runner.py
  - ../../tools/validators/_common/local_resolver.py
  - ../../.github/workflows/schema-validation.yml
  - ../../.github/workflows/validator-suite.yml
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "v0.5 replaces the obsolete seven-module and seven-validator inventory with the current eleven-module and nine-validator boundary."
  - "The 137 count is the number of source-defined test functions or methods; pytest parametrization can produce a larger collected-case count."
  - "schema-validation directly collects tests/schemas and tests/contracts and separately checks all schema JSON, Draft 2020-12 meta-schema conformance, canonical v1 IDs, and the nine configured aggregate fixture families."
  - "This README is authored at its canonical test-lane path; it is not generated or mirrored."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/schemas/` — Executable schema conformance and anti-collapse tests

> This lane exercises selected KFM machine-shape, fixture, validator, identity,
> temporal, and anti-collapse boundaries. It does not own schemas, contracts,
> reusable fixtures, validators, source records, policy, evidence, or release
> decisions.

## Purpose and audience

Use this README to locate the direct tests, choose a focused command, understand
what each module checks, interpret failures, and identify the difference between
direct pytest coverage and the historical aggregate validator command.

The prior v0.4 README was materially stale. Current `main` contains eleven
direct test modules rather than seven, defines 137 test functions or methods in
source, and configures nine—not seven—validators behind `make schemas`.
`schema-validation` also performs Draft 2020-12 meta-schema checks that the prior
README described as absent.

## Authority and placement

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
makes the Directory Rules path authoritative. The [`tests/` root
contract](../README.md) assigns executable conformance evidence to `tests/`, so
this lane is correctly placed. The file is authored documentation at its
canonical same-path location; it is neither generated nor mirrored.

| Concern | Authority home | Role of this lane |
|---|---|---|
| Machine shape and `$id`/`$ref` declarations | [`schemas/`](../../schemas/README.md) | Load and test selected behavior; never redefine shape. |
| Semantic meaning | [`contracts/`](../../contracts/README.md) | Check selected pairing and anti-collapse rules; never replace contracts. |
| Reusable examples | [`fixtures/`](../../fixtures/README.md) | Consume bounded fixtures; never treat examples as production records. |
| Validator behavior | [`tools/validators/`](../../tools/validators/README.md) | Exercise entrypoints, diagnostics, and outcomes. |
| Executable schema proof | `tests/schemas/` | Own the direct tests documented here. |
| Policy, evidence, rights, sensitivity, release, and publication | Their accepted authority roots | Remain separate from schema or test success. |

Current [CODEOWNERS](../../.github/CODEOWNERS) routes `/tests/` to
`@bartytime4life`. That is a review route, not proof of independent review,
required code-owner approval, stewardship assignment, or release authority.

## Confirmed direct inventory

At `main@1ea6593ede80d5ce10f561c7eec72135d6ccf806`, the directory contains
eleven `test_*.py` modules and 137 source-defined test functions or methods.
Parameterized tests can expand into more collected cases, so 137 is not a
claimed pytest collection total or run result.

| Module | Source-defined tests | Implemented boundary |
|---|---:|---|
| [`test_common_contracts.py`](test_common_contracts.py) | 1 | Parameterized valid/invalid fixture polarity for immediate schemas in seven configured families. |
| [`test_corridor_route_contract.py`](test_corridor_route_contract.py) | 14 | Roads–rail–trade corridor schema, contract pairing, identity separation, authority limits, sensitive geometry, deterministic hash, and CLI fixture polarity. |
| [`test_drought_separation_contracts.py`](test_drought_separation_contracts.py) | 34 | Drought observation, declaration, and relationship separation; object types, time fields, forbidden fields, fixture polarity, and no-network/public-safe fixture assertions. |
| [`test_evidence_ref_validator.py`](test_evidence_ref_validator.py) | 2 | EvidenceRef CLI acceptance and missing-reference rejection. |
| [`test_gmd3_aem_survey_contracts.py`](test_gmd3_aem_survey_contracts.py) | 7 | GMD 3 AEM source-descriptor candidate, campaign schema and semantic validator, negative fixtures, sparse/time-scoped posture, and explicit socket/URL blocking. |
| [`test_hydrology_alias_contracts.py`](test_hydrology_alias_contracts.py) | 2 | Three Hydrology aliases accept their valid fixtures and reject an unexpected top-level property. |
| [`test_kdhe_hab_advisory_snapshot_contracts.py`](test_kdhe_hab_advisory_snapshot_contracts.py) | 10 | KDHE HAB snapshot shape, deterministic identity, lineage, scope, inactive source posture, denied publication/alerting, and freshness holds. |
| [`test_kgs_m118_source_descriptor.py`](test_kgs_m118_source_descriptor.py) | 9 | KGS M-118 registry descriptor shape, content-derived identity, scale/role bounds, unresolved rights, disabled access, and no embedded payload. |
| [`test_usdm_source_descriptor_contracts.py`](test_usdm_source_descriptor_contracts.py) | 31 | Inactive USDM descriptor and two connector-fixture governance boundaries, including no-network posture and forbidden downstream write targets. |
| [`test_verification_state_history.py`](test_verification_state_history.py) | 10 | Verification-state-history schema and semantic polarity, bitemporal replay, deterministic ordering/hash, parser limits, CLI behavior, and network denial. |
| [`test_water_planning_contracts.py`](test_water_planning_contracts.py) | 17 | Fifteen water-planning schema families, fixture polarity, distinct identities/titles, time-zone and region bounds, and anti-collapse rules. |

The count records source structure only. It does not prove that every test ran,
that every parametrized fixture was collected, or that every schema has direct
coverage.

## Run the lane

From the repository root:

```bash
# Focused direct lane.
python -m pytest -q tests/schemas

# Same direct schema-and-contract scope used by the root test target.
python -m pytest -q tests/schemas tests/contracts

# Root convenience target for that same two-lane pytest scope.
make test

# Historical nine-validator compatibility aggregate; not direct pytest.
make schemas
```

For one module or test:

```bash
python -m pytest -q tests/schemas/test_drought_separation_contracts.py
python -m pytest -q \
  tests/schemas/test_corridor_route_contract.py::test_all_negative_fixtures_are_denied
```

These commands assume the root project test dependencies declared in
[`pyproject.toml`](../../pyproject.toml) are installed. Default tests must remain
deterministic and repository-local. A live fetch is not an acceptable hidden
success path for `$ref` resolution, fixture loading, source state, or semantic
validation.

## What the generic fixture harness covers

[`test_common_contracts.py`](test_common_contracts.py) scans immediate
`*.schema.json` children in these seven families:

```text
evidence
runtime
common
policy
source
governance
release
```

For `schemas/contracts/v1/<family>/<name>.schema.json`, it includes a case only
when `fixtures/contracts/v1/<family>/<name>/` exists. It then checks matching
`valid/valid_*.json` and `invalid/invalid_*.json` fixtures, with optional
expected-error sidecars.

This harness is intentionally incomplete:

- its schema glob is not recursive;
- families outside the seven-name allowlist are omitted;
- a schema without a matching fixture directory is omitted;
- domain schemas depend on dedicated modules or remain uncovered;
- its single source-defined test expands through parametrization;
- it does not itself prove complete schema-to-contract pairing.

The [`schema-validation` workflow](../../.github/workflows/schema-validation.yml)
adds broader inventory checks, but those checks do not turn the generic harness
into complete fixture coverage.

## Historical aggregate validator boundary

[`tools/validators/_common/run_all.py`](../../tools/validators/_common/run_all.py)
is a compatibility entrypoint. It invokes the canonical validator orchestrator
with exactly these nine legacy-core validator IDs:

| Validator ID | Compatibility entrypoint |
|---|---|
| `source-descriptor` | `validate_source_descriptor.py` |
| `evidence-ref` | `validate_evidence_ref.py` |
| `evidence-bundle` | `validate_evidence_bundle.py` |
| `layer-manifest` | `validate_layer_manifest.py` |
| `dataset-version` | `validate_dataset_version.py` |
| `runtime-response-envelope` | `validate_runtime_response_envelope.py` |
| `decision-envelope` | `validate_decision_envelope.py` |
| `run-receipt` | `validate_run_receipt.py` |
| `ingest-receipt` | `validate_ingest_receipt.py` |

The entrypoint requires fixture mode for every selected validator and keeps
historical `make schemas` semantics narrower than the canonical orchestrator's
full profile. It is not dynamic discovery of all schemas, validators, or test
modules.

The shared [`jsonschema_runner.py`](../../tools/validators/_common/jsonschema_runner.py)
distinguishes successful positive fixtures (`OK`), expected schema rejection
(`EXPECTED_FAIL`), and harness or polarity failures (`FAIL`). It requires at
least one JSON fixture in both configured valid and invalid lanes.

## Schema resolution

[`local_resolver.py`](../../tools/validators/_common/local_resolver.py)
recursively reads `schemas/contracts/v1/**/*.schema.json`, registers schemas
that declare `$id`, and rejects duplicate IDs. A schema without `$id` is skipped
by that resolver.

The registry is broader than the seven-family generic pytest scan. A schema can
therefore resolve as a `$ref` target without receiving its own direct fixture
case.

## CI binding

[`schema-validation`](../../.github/workflows/schema-validation.yml) runs on
every pull request, pushes to `main`, and manual dispatch with read-only
repository permissions. It directly performs all of the following:

1. parses every JSON file under `schemas/`;
2. calls `Draft202012Validator.check_schema` for every `*.schema.json`;
3. requires every canonical v1 schema to declare Draft 2020-12 and a unique
   `$id`;
4. checks nonempty valid and invalid lanes plus reviewed rejection evidence for
   the nine aggregate validators;
5. runs focused DatasetVersion and aggregate-selection checks;
6. runs `make schemas`;
7. runs `python -m pytest -q tests/schemas tests/contracts`.

[`validator-suite`](../../.github/workflows/validator-suite.yml) also runs
`make schemas`, registry checks, and other repository guardrails. It does not
replace the direct `tests/schemas` collection performed by `schema-validation`.

Workflow presence or a green run does not prove required-check status,
independent review, semantic acceptance, evidence closure, release readiness,
deployment, or publication.

## Failure interpretation

| Failure location | First interpretation | Do not infer |
|---|---|---|
| Collection/import | A dependency, import path, syntax, or test discovery problem blocked assertions. | Schema invalidity or valid coverage. |
| Missing schema/fixture/contract | A checked repository relationship is absent or moved. | That another path is automatically authoritative. |
| Valid fixture rejected | Checked fixture and schema/validator behavior disagree. | The fixture or schema should be weakened automatically. |
| Invalid fixture accepted | A reviewed negative boundary no longer fails closed. | Release or publication must proceed. |
| Semantic/anti-collapse assertion | A specialized invariant drifted even if JSON shape remains valid. | Schema shape alone can settle the meaning. |
| Aggregate inventory | The nine-validator compatibility set, registry, or fixture expectations changed. | Every schema or validator is broken. |
| CI installation | The test did not reach substantive execution. | The schema lane passed or failed. |

Preserve the primary diagnostic and identify whether the mismatch belongs to a
schema, semantic contract, fixture, validator, test, or workflow. Do not edit a
trust-bearing schema merely to make a mistaken fixture or stale assertion pass.

## Safety and authority limits

Fixtures and diagnostics must remain synthetic, minimal, public-safe, and free
of credentials, signed URLs, private endpoints, living-person sensitive data,
genomic records, precise protected locations, restricted cultural knowledge,
or critical-infrastructure detail.

A passing test establishes only the checked assertion at the checked revision.
In particular:

```text
schema-valid != semantically correct
schema-valid != evidence-supported
schema-valid != source-authoritative
schema-valid != rights-cleared or sensitivity-safe
schema-valid != reviewed, released, deployed, or published
```

## Maintenance

When adding or changing a direct module:

1. keep executable code under `tests/schemas/` unless accepted placement says
   otherwise;
2. link exact schemas, contracts, fixtures, and validators;
3. add meaningful positive and negative cases;
4. keep network access denied by default;
5. state whether the module checks shape, semantic behavior, governance state,
   or more than one of those boundaries;
6. update the module count, source-defined test count, and inventory table;
7. verify `schema-validation` still collects the path;
8. report parametrized collection totals only from an actual run;
9. preserve authority separation and correction/rollback guidance.

When changing the historical aggregate, update `run_all.py`, the validator
registry, configured schemas and fixtures, workflow inventory assertions,
expected-error evidence, tests, and this README together. Do not silently widen
`make schemas` to the full validator profile.

## Open verification

- Exact pytest collection and focused pass state were not recorded by this
  documentation edit.
- The generic harness still omits nested, unlisted-family, and fixture-less
  schemas.
- Complete schema-to-contract and schema-to-fixture closure is not established.
- Required-check and branch-protection coupling remain unverified.
- Accountable schema, fixture, QA, security, and release stewardship beyond
  CODEOWNERS routing remains unverified.
- Production consumers and correction propagation remain outside this lane's
  proof boundary.

## Correction and rollback

If this inventory drifts, re-count from the pinned repository tree, narrow the
claim, and preserve the superseded commit or blob in review history. If schema
behavior changes, review affected contracts, fixtures, `$id`/`$ref` consumers,
validators, direct tests, compatibility entrypoints, and downstream consumers
before changing claims.

For this documentation-only change, close the unmerged pull request or revert
its single commit. Do not rewrite shared history. Documentation rollback does
not roll back schema, validator, policy, release, deployment, or publication
state.

[Back to top](#top)
