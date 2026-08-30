<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://tests/data/readme
title: tests/data/ — Data Contract Test Lane
type: README
version: v0.1.0
status: draft; repository-grounded; executable; fixture-only; bounded; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; independent data, contract, and validation stewardship remain UNKNOWN"
created: 2026-08-30
updated: 2026-08-30
owning_root: tests/
policy_label: public; tests; data; deterministic; fixture-only; no-network; fail-closed; non-publisher
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: e65f9b1cdccbc9c81a911bc1a6d0a10a094bf73f
  direct_modules: 2
  source_defined_tests: 19
  synthetic_fixture_cases: 50
truth_posture: CONFIRMED two focused modules, two validators, two proposed contracts, two Draft 2020-12 schemas, 50 synthetic fixture cases, and two dedicated workflows / UNKNOWN complete data-lane coverage, required-check status, production consumers, accountable stewardship, correction propagation, and operational rollback
notes:
  - "This human-maintained index documents bounded executable evidence; it is not a dataset, baseline, panel, source record, policy decision, receipt, release record, or publication surface."
  - "A passing test establishes only the checked local profile at the tested revision."
[/KFM_META_BLOCK_V2] -->

# Data contract test lane

`tests/data/` exercises two fixture-first data contract profiles: a baseline
cohort assessment and a county-year panel. The tests bind checked-in contracts,
schemas, synthetic fixture matrices, and deterministic validators. They do not
load observations, establish a scientific baseline, classify a county, resolve
evidence, or authorize lifecycle movement, release, or publication.

> [!IMPORTANT]
> A green result means that the tested synthetic object satisfied the named
> schema and semantic checks. It does not prove that referenced sources exist,
> that observations are correct or current, that rights and sensitivity are
> resolved, or that a human approved any downstream use.

## Inventory

| Module | Tests | Implemented coverage |
|---|---:|---|
| [`test_baseline_cohort_assessment.py`](./test_baseline_cohort_assessment.py) | 10 | Draft 2020-12 schema validity, exact fixture size, hold-first states, count and missingness closure, discontinuity and rebuild lineage, deterministic identity, duplicate-key and symlink denial, value-free diagnostics, and forbidden network-client imports |
| [`test_county_year_panel.py`](./test_county_year_panel.py) | 9 | Schema validity, exact fixture expectations, panel-state and observation polarity, reference-only fixtures, deterministic identity, socket denial, value-free serialization, CLI replay, and duplicate/non-finite/symlink/oversize input errors |
| **Total** | **19** | Source-defined test functions at the pinned evidence revision |

This is not a complete inventory of all repository data validation. Other
validator tests remain under [`tests/validators/`](../validators/README.md), and
domain, source, ingest, evidence, pipeline, release, and UI suites have separate
responsibilities.

## Authority and placement

Accepted [Directory Rules](../../docs/doctrine/directory-rules.md) place
executable conformance evidence under `tests/`, reusable synthetic inputs under
`fixtures/`, semantic meaning under `contracts/`, machine shape under
`schemas/`, and repository-wide validators under `tools/`.

| Responsibility | Repository authority | Test-lane role |
|---|---|---|
| Baseline meaning | [`baseline_cohort_assessment.md`](../../contracts/data/baseline_cohort_assessment.md) | Exercise the proposed, fixture-first contract without accepting or redefining it |
| County-year meaning | [`county_year_panel.md`](../../contracts/data/county_year_panel.md) | Exercise the proposed, inactive candidate without classifying a county |
| Machine shapes | [`baseline_cohort_assessment.schema.json`](../../schemas/contracts/v1/data/baseline_cohort_assessment.schema.json) and [`county_year_panel.schema.json`](../../schemas/contracts/v1/data/county_year_panel.schema.json) | Check Draft 2020-12 validity and candidate shape |
| Synthetic cases | [`baseline_cohort_assessment/`](../../fixtures/contracts/v1/data/baseline_cohort_assessment/) and [`county_year_panel/`](../../fixtures/contracts/v1/data/county_year_panel/) | Provide deterministic positive, hold, and deny cases; never production records |
| Validators | [`validate_baseline_cohort_assessment.py`](../../tools/validators/data/validate_baseline_cohort_assessment.py) and [`validate_county_year_panel.py`](../../tools/validators/data/validate_county_year_panel.py) | Implement bounded local validation and CLI outcomes |
| Hosted orchestration | [`baseline-cohort-assessment.yml`](../../.github/workflows/baseline-cohort-assessment.yml) and [`county-year-panel.yml`](../../.github/workflows/county-year-panel.yml) | Run focused checks and report their status |

[`CODEOWNERS`](../../.github/CODEOWNERS) routes `tests/` review to
`@bartytime4life`. Routing does not prove stewardship, independent review,
approval, policy authority, or separation of duties.

## Fixture profiles

| Profile | Cases | Expected outcomes | Boundary |
|---|---:|---|---|
| Baseline cohort assessment | 19 | 9 `HOLD`, 10 `DENY` | Even a coherent candidate remains a review candidate or hold; there is no `ALLOW` outcome |
| County-year panel | 31 | 7 `PASS`, 24 `DENY` | `PASS` means the aggregate-only, reference-only fixture is internally coherent; it grants no execution or classification authority |
| **Total** | **50** | Hold/pass and negative polarity | Counts come from the checked-in fixture manifests, not dynamic production data |

The baseline matrix covers replayable, qualified, insufficient, and unresolved
discontinuity states plus malformed count, ordering, lineage, and identity
cases. The county-year matrix covers complete, partial, and insufficient panels;
availability states; geography alignment; required disclosures; and bounded
input failures.

Fixtures contain synthetic references and governance limits. Do not replace
them with private, personal, restricted, culturally sensitive, or
harmful-precision source payloads.

## Run the focused checks

From the repository root, install the declared project-test dependencies, then
run the workflow-matching commands.

### Baseline cohort assessment

```bash
python tools/ci/install_python_ci.py project-test
python tools/validators/data/validate_baseline_cohort_assessment.py --fixtures
python -m pytest tests/data/test_baseline_cohort_assessment.py -q \
  --strict-config --strict-markers
```

### County-year panel

```bash
python tools/ci/install_python_ci.py project-test
python -m unittest -v tests.data.test_county_year_panel
python tools/validators/data/validate_county_year_panel.py --fixtures
```

The dedicated county-year workflow also runs adjacent geography-version,
frontier-definition, and indicator-definition tests. Use the workflow file as
the exact source for that broader command set; this README does not collapse
those separate owners into `tests/data/`.

## CLI outcomes

The two validators intentionally expose different finite profiles.

| Validator | Successful fixture replay | Candidate outcomes | Exit behavior |
|---|---|---|---|
| Baseline cohort | Fixture matrix matches all expected `HOLD`/`DENY` cases | `HOLD` or `DENY` | Coherent `HOLD` returns 0; `DENY` or a fixture mismatch returns 1; argument parsing errors return 2 |
| County-year panel | Fixture matrix reports `suite_match: true` | `PASS`, `DENY`, or input `ERROR` | `PASS` returns 0, `DENY` returns 1, and `ERROR` returns 2 |

Do not normalize these vocabularies in documentation. A future shared outcome
contract would require an implementation and governance decision.

## Hosted workflows

Both workflows use Python 3.11, read-only repository permissions,
deterministic environment settings, and `KFM_NO_NETWORK=1`.

| Workflow | Direct lane execution | Additional checks | README trigger state |
|---|---|---|---|
| `baseline-cohort-assessment` | 19-case validator replay and the 10 focused tests | Generated authoring-receipt integrity | `tests/data/README.md` is not in the current path filter |
| `county-year-panel` | 9 focused tests and 31-case validator replay | Geography-version, frontier-definition, indicator-definition, and generated authoring-receipt checks | `tests/data/README.md` is not in the current path filter |

Because this README is excluded from both focused path filters, a
documentation-only edit does not by itself schedule either workflow. That is a
workflow-coverage gap, not evidence that the checks failed or passed for the
documentation head. Repository-wide documentation checks may still run.

Workflow definitions prove configured commands and boundaries, not hosted
results, required-check status, or production parity. Inspect the exact-head run
before reporting a hosted conclusion.

## Failure interpretation

| Failure | Maintainer response |
|---|---|
| Schema validity or shape failure | Reconcile the proposed contract and schema before changing fixtures or weakening assertions |
| Fixture count or polarity drift | Review the fixture manifest and validator together; preserve a non-vacuous positive/hold and negative matrix |
| Count, missingness, availability, alignment, or disclosure failure | Keep the candidate held and correct the owning contract, fixture, or validator |
| Identity mismatch | Investigate canonicalization inputs and hashing behavior; do not rewrite a digest merely to match unexplained bytes |
| Symlink, size, duplicate-key, non-finite, or malformed-input failure | Preserve fail-closed behavior and value-free diagnostics |
| Network-denial failure | Treat as a boundary regression; do not enable live source access for an ordinary fixture test |
| Receipt integrity failure | Distinguish workflow-byte or dependency drift from the data-contract assertions |
| Dependency or runner failure | Classify separately from a focused assertion failure and retain the exact revision and logs |

## Safety and non-effects

- Validation is local and fixture-first. The tests do not fetch a source,
  observation, crosswalk, evidence bundle, or production record.
- The baseline profile creates no scientific threshold, anomaly conclusion,
  source role, or accepted baseline.
- The county-year profile loads no observation values, computes no aggregate,
  resolves no geography, and classifies no frontier status.
- A schema, contract, test, or workflow pass is not policy evaluation, human
  review, lifecycle promotion, proof issuance, release, deployment, or
  publication.
- Test output is designed to report finding codes and pointers without echoing
  candidate values; preserve that boundary when adding diagnostics.
- Public clients must use governed released interfaces or public-safe artifacts,
  not this internal fixture and validator lane.

## Maintenance

Update this README when a direct module, source-defined test count, fixture case
or polarity, contract or schema binding, validator outcome, command, workflow
path filter, receipt check, or authority boundary changes. Keep implementation,
contract, schema, and fixture links synchronized.

For a failed documentation change, close the unmerged pull request or revert its
commit. Do not delete tests, fixtures, contracts, schemas, validators, receipts,
or downstream records merely to make this index agree with an unsupported
claim.

## Known gaps

- The two focused workflows do not currently trigger on this README.
- Complete data-contract and data-validator coverage is **UNKNOWN**; this lane
  contains only two focused modules.
- Required-check and branch-protection significance are **UNKNOWN**.
- Both semantic contracts remain **PROPOSED**; passing tests do not accept them.
- Production writers, consumers, source resolution, observation computation,
  policy composition, and production parity are **UNKNOWN**.
- Accountable independent data, contract, validation, privacy, and security
  stewardship remains **NEEDS VERIFICATION**.
- Correction propagation, withdrawal, cache invalidation, retention, and
  operational rollback are not established by this lane.

See the [test-root contract](../README.md) for the surrounding test-system
boundaries.
