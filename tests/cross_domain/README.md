<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-cross-domain-readme
title: tests/cross_domain/ — Cross-Domain Test Inventory and Placement Boundary
type: readme; directory-readme; cross-domain-test-index; placement-boundary
version: v0.4
status: draft; repository-grounded; canonical-parent-namespace; seven-test-modules-confirmed; 46-source-defined-tests; mixed-child-documentation; dedicated-workflows-confirmed; non-authoritative
policy_label: public-doc; restricted-review-when-child-sensitivity-requires
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; independent QA, domain, sensitivity, policy, and release stewardship remain NEEDS VERIFICATION"
created: NEEDS VERIFICATION — placeholder expanded on 2026-07-05
updated: 2026-08-30
current_path: tests/cross_domain/README.md
truth_posture: CONFIRMED recursive repository inventory, accepted Directory Rules namespace, source-defined test methods, validator and fixture bindings, and focused workflow commands at the pinned snapshot / PROPOSED partial seam register / UNKNOWN required-check status, full semantic coverage, production enforcement, accountable stewardship, and operational correction or rollback evidence
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 1ea6593ede80d5ce10f561c7eec72135d6ccf806
  prior_blob: 93e91a9b8e5993a9078b394df36255c0c696cc88
related:
  - ../README.md
  - ./fauna_habitat/README.md
  - ./fauna_habitat/test_public_safe_assignment.py
  - ./soil_agriculture/test_public_safe_context.py
  - ./soil_hydrology/test_public_safe_context.py
  - ./test_classification_observation_boundary.py
  - ./test_conditions_source_role_readiness_matrix.py
  - ./test_environmental_observation_boundaries.py
  - ./test_temporal_support_acceptance_assessment.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../control_plane/cross_domain_seam_register.yaml
  - ../../tools/validators/cross_domain/
  - ../../fixtures/contracts/v1/joins/
  - ../../.github/workflows/
tags: [kfm, tests, cross-domain, enforceability, ownership, source-role, sensitivity, deterministic, no-network, non-publishing]
notes:
  - "v0.4 replaces the stale one-module and unknown-CI posture with the complete current inventory."
  - "The accepted Directory Rules now establish tests/cross_domain/<seam_id>/; child seam IDs and register coverage remain incomplete."
  - "The deleted tests/cross-domain/ spelling remains historical only and must not be recreated as a compatibility tree."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/cross_domain/` — Cross-Domain Test Inventory and Placement Boundary

This directory contains executable tests whose assertions span multiple domain
or object-family boundaries. At the pinned snapshot it contains seven Python
test modules with 46 source-defined test methods across four parent-level
assessments and three pair-specific child lanes.

Passing these tests supports only the assertions encoded by the checked module,
fixtures, validators, and revision. It does not admit a source, establish a
canonical join, approve a policy decision, or authorize review, merge, release,
deployment, promotion, or publication.

## Placement and authority

[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
accepts the current
[Directory Rules](../../docs/doctrine/directory-rules.md). Section 12.5 places a
cross-domain test at:

```text
tests/cross_domain/<seam_id>/
```

This resolves the former dispute over the `tests/cross_domain/` parent
namespace. It does not resolve every child name:

- the current
  [cross-domain seam register](../../control_plane/cross_domain_seam_register.yaml)
  is `PROPOSED`, partial, and navigational only;
- the register's seam IDs do not provide complete registration for the three
  child directories inventoried below;
- four current tests live directly in the parent rather than a registered seam
  child;
- `tests/cross-domain/` was deleted and must not be recreated as a second
  implementation or redirect tree.

`cross_domain` is a test-routing namespace, not a semantic domain. Contracts,
schemas, fixtures, policies, validator implementations, proofs, receipts, and
release records remain in their responsibility roots.

## Current inventory

Counts below are source-defined `test_*` functions or methods at the pinned
commit. They are not a claim about parameterized cases, subtests, collection in
every environment, or historical pass rates.

| Test module | Source-defined tests | Directly checked boundary |
|---|---:|---|
| [`test_classification_observation_boundary.py`](./test_classification_observation_boundary.py) | 4 | Classification and Soil observation candidates pass only their own validators; source roles, support types, scale, and time semantics remain distinct. |
| [`test_conditions_source_role_readiness_matrix.py`](./test_conditions_source_role_readiness_matrix.py) | 12 | Draft 2020-12 schema validity, exact readiness outcomes, bound-path existence, role separation, stable identity, hostile input handling, and bounded CLI output. |
| [`test_environmental_observation_boundaries.py`](./test_environmental_observation_boundaries.py) | 3 | Soil, Atmosphere, and Hydrology fixtures pass only their own profiles; shared place and time do not transfer domain ownership. |
| [`test_temporal_support_acceptance_assessment.py`](./test_temporal_support_acceptance_assessment.py) | 8 | Exact temporal-assessment fixture replay, finite outcomes, subject-family coverage, stable profile hashing, payload exclusion, determinism, and no-network execution. |
| [`fauna_habitat/test_public_safe_assignment.py`](./fauna_habitat/test_public_safe_assignment.py) | 7 | Ten-case pair profile, generalized non-publishing candidate, sensitive and incomplete outcomes, provenance and relation-profile rejection, and fixture/validator safety. |
| [`soil_agriculture/test_public_safe_context.py`](./soil_agriculture/test_public_safe_context.py) | 6 | Seven-case pair profile, generalized non-publishing candidate, private-parcel and precision denial, finite incomplete outcomes, and fixture/validator safety. |
| [`soil_hydrology/test_public_safe_context.py`](./soil_hydrology/test_public_safe_context.py) | 6 | Seven-case pair profile, generalized non-publishing candidate, precision and operational-claim denial, finite incomplete outcomes, and fixture/validator safety. |
| **Total** | **46** | Source inventory only. |

The directory also contains:

- [`fauna_habitat/README.md`](./fauna_habitat/README.md), whose `readme-only`
  metadata is stale because an executable test now exists;
- `fauna_habitat/.gitkeep`, which has no test or authority effect;
- `soil_agriculture/` and `soil_hydrology/`, which have executable tests but no
  child README at the pinned snapshot.

Those child-documentation gaps do not make this parent inventory incomplete,
but they remain maintenance work.

## Implementation and fixture bindings

| Test surface | Validators or schemas exercised | Fixture evidence |
|---|---|---|
| Classification × observation | `tools/validators/validate_classification_release.py`; `tools/validators/domains/soil/validate_domain_observation.py` | Classification validator fixtures; `fixtures/domains/soil/domain_observation/cases.json` |
| Conditions source-role readiness | `tools/validators/validate_conditions_source_role_readiness_matrix.py`; common readiness schema; selected classification, forecast, and Soil validators | Readiness validator fixtures; Soil observation cases; valid observation/classification relation fixture |
| Environmental observation isolation | Soil public-safe, Atmosphere precipitation, and Hydrology flow validators | One public-safe fixture from each of the three domain fixture trees |
| Temporal support acceptance | `tools/validators/validate_temporal_support_acceptance_assessment.py`; common temporal-assessment schema | `fixtures/contracts/v1/common/temporal_support_acceptance_assessment/cases.json` |
| Fauna × Habitat | `tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py`; generic join-candidate evaluator | `fixtures/contracts/v1/joins/fauna_habitat_public_safe_assignment/cases.json` |
| Soil × Agriculture | `tools/validators/cross_domain/soil_agriculture/validate_public_safe_context.py`; generic join-candidate evaluator | `fixtures/contracts/v1/joins/soil_agriculture_public_safe_context/cases.json` |
| Soil × Hydrology | `tools/validators/cross_domain/soil_hydrology/validate_public_safe_context.py`; generic join-candidate evaluator | `fixtures/contracts/v1/joins/soil_hydrology_public_safe_context/cases.json` |

The tests consume these authorities; they do not become their canonical source.
Fixture references are repository evidence, not a statement that the represented
source is admitted, current, released, or suitable for public use.

## Focused commands

Run from the repository root with the project test dependencies installed.
These commands match current focused workflows:

```bash
python -m unittest tests.cross_domain.test_classification_observation_boundary --verbose
python -m unittest tests.cross_domain.test_conditions_source_role_readiness_matrix --verbose
python tests/cross_domain/test_environmental_observation_boundaries.py --verbose
python -m unittest tests.cross_domain.test_temporal_support_acceptance_assessment --verbose
python -m pytest tests/cross_domain/fauna_habitat/test_public_safe_assignment.py -q --strict-config --strict-markers
python -m pytest tests/cross_domain/soil_agriculture/test_public_safe_context.py -q --strict-config --strict-markers
python -m pytest tests/cross_domain/soil_hydrology/test_public_safe_context.py -q --strict-config --strict-markers
```

For local discovery of the whole lane:

```bash
python -m pytest --collect-only --strict-config --strict-markers tests/cross_domain
python -m pytest -q --strict-config --strict-markers tests/cross_domain
```

The whole-lane commands are convenience commands, not a confirmed dedicated
hosted workflow. A zero-test result, collection error, skip, or missing
dependency is not passing evidence.

## Hosted workflow bindings

| Test module | Confirmed workflow | Binding at the pinned snapshot |
|---|---|---|
| Classification × observation | `.github/workflows/classification-release.yml` | Exact test path filter and `unittest` command. |
| Conditions source-role readiness | `.github/workflows/conditions-source-role-readiness.yml` | Exact test path filter and `unittest` command. |
| Environmental observation isolation | `.github/workflows/domain-atmosphere.yml`; `.github/workflows/domain-hydrology.yml` | Both workflows list and execute the same test file. |
| Temporal support acceptance | `.github/workflows/temporal-support-acceptance.yml` | Exact test path filter, compile check, `unittest`, and validator fixture replay. |
| Fauna × Habitat | `.github/workflows/fauna-habitat-public-safe-assignment.yml` | Recursive child path filter, pair fixture replay, and focused pytest execution. |
| Soil × Agriculture | `.github/workflows/soil-agriculture-public-safe-context.yml` | Recursive child path filter, pair fixture replay, and focused pytest execution. |
| Soil × Hydrology | `.github/workflows/soil-hydrology-public-safe-context.yml` | Recursive child path filter, pair fixture replay, and focused pytest execution. |

No dedicated workflow was found that collects the entire directory. The four
parent-level focused workflows filter on exact test files, so a change only to
this parent README does not trigger them. The three child workflows use
recursive child filters, but those filters also exclude the parent README.
Documentation checks can validate this file without proving the seven executable
modules passed at the same head.

Workflow presence also does not prove that a job is required by branch rules,
that every relevant change triggers it, or that a passing historical run applies
to a different revision.

## Evidence boundaries

The implemented suite confirms bounded repository behavior:

- selected cross-role candidates fail closed under validator substitution;
- selected domain fixtures retain their domain ownership despite shared
  generalized place and time;
- readiness and temporal assessments preserve finite outcomes and stable
  identities for their fixture matrices;
- pair-specific public-safe candidates are deterministic and non-publishing;
- pair profiles reject harmful precision, unsupported provenance, wrong relation
  profiles, or operational claims where encoded;
- pair fixtures exclude coordinate or geometry payload fields from their base
  objects, and their validators are statically checked for common network and
  write clients.

The suite does **not** establish:

- complete cross-domain seam or source-role coverage;
- correctness of every validator, schema, fixture, or policy consumer;
- absence of all network, filesystem, subprocess, or side effects outside the
  specifically checked implementations;
- rights, consent, privacy, sovereignty, sensitivity, or harmful-precision
  clearance for real data;
- production runtime behavior or public-client isolation;
- required-check status, independent review, release approval, deployment,
  promotion, publication, correction propagation, or operational rollback.

## Failure interpretation

1. Identify the failing test and its bound validator, schema, and fixture.
2. Distinguish collection or dependency failure from an assertion failure.
3. Preserve the exact finite outcome and findings before changing expectations.
4. Determine whether the defect belongs to the test, fixture, validator,
   contract, schema, policy, or implementation authority.
5. Do not weaken an assertion solely to restore a green job.
6. Re-run the focused command and every workflow that consumes the changed
   authority.

A failed test is a hold on the bounded assertion. A passed test is not a release
decision.

## Maintenance

Update this README when a test module, child lane, fixture binding, validator,
schema, command, or workflow binding changes. During review:

1. inventory `tests/cross_domain/` recursively;
2. count source-defined tests and distinguish that count from collected cases;
3. verify every linked path at the reviewed commit;
4. compare focused commands with current workflow definitions;
5. check the accepted Directory Rules and seam register before adding or moving
   a child;
6. preserve the retirement of `tests/cross-domain/`;
7. record incomplete child documentation and unbound workflow coverage without
   inventing owners or adoption status.

Before merge, rollback is closing the pull request or reverting its unmerged
documentation commit. Test, fixture, validator, or path migrations require their
own reviewed correction and rollback plan.

## Unresolved gaps

- The seam register is proposed and partial; current child names are not fully
  reconciled with registered seam IDs.
- Four executable tests remain directly under the parent namespace.
- `fauna_habitat/README.md` still claims the child is README-only.
- `soil_agriculture/` and `soil_hydrology/` have no child README.
- No dedicated whole-directory workflow or Make target was found.
- Parent README changes do not trigger the focused executable workflows.
- Required-check status and accountable independent stewardship are unknown.
- Complete cross-domain coverage, production enforcement, correction
  propagation, and operational rollback remain unverified.

## Evidence basis

| Evidence | Supports | Limit |
|---|---|---|
| Recursive tree at `1ea6593ede80d5ce10f561c7eec72135d6ccf806` | Seven test modules, three child directories, and current documentation gaps. | Repository snapshot only. |
| Seven test module sources | 46 source-defined tests and the bounded assertions summarized here. | Source count is not a hosted pass result. |
| Bound validators, schemas, and fixtures | Exact implementation and test-data dependencies. | Their presence is not governance adoption or release evidence. |
| Seven focused workflow definitions | Direct hosted bindings and path-filter behavior. | Does not establish required-check status or success at every head. |
| Accepted ADR-0029 and Directory Rules | Canonical `tests/cross_domain/<seam_id>/` placement. | Does not register every current child. |
| Proposed cross-domain seam register | Partial seam vocabulary and explicit non-effects. | Navigational only; no join or publication authority. |
| `.github/CODEOWNERS` | Current GitHub review route for `tests/`. | Routing is not review, stewardship, or approval evidence. |

[Back to top](#top)
