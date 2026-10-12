<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-readme
title: tests/domains/ — Domain Test Package Index
type: README
version: v0.3
status: draft; repository-grounded; exact-child-inventory; mixed-execution-maturity; non-authoritative
owners: OWNER_TBD — QA steward · Domain stewards · Contracts steward · Schema steward · Evidence steward · Policy steward · Release steward
created: 2026-05-08
updated: 2026-08-31
policy_label: public-doc; tests; domains; enforceability; mixed-maturity; sensitivity-aware; non-publisher
owning_root: tests/
responsibility: current navigation, execution guidance, and bounded maturity disclosure for domain-specific test packages without granting domain, source, evidence, policy, review, release, deployment, promotion, or publication authority
truth_posture: CONFIRMED 18 direct child directories, 14 test-bearing child directories, 148 direct-or-nested test modules, 151 child README files, 31 workflow files with literal tests/domains references, and nine representative inspected workflow bindings at the pinned snapshot / UNKNOWN complete semantic coverage, broad-suite collection result, required-check status, production parity, and accountable stewardship
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 5d835798e09a4dd14735779cb44206a8a3e8b2d3
evidence_prior_blob: d84d692e15cc1882e4eff9771c091e8a6a872911
child_directory_count: 18
test_bearing_child_directory_count: 14
test_module_count: 148
child_readme_count: 151
literal_workflow_reference_count: 31
documented_representative_workflow_count: 9
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/domain-placement-law.md
  - ../../docs/domains/README.md
  - agriculture/README.md
  - air/README.md
  - archaeology/README.md
  - atmosphere/README.md
  - fauna/README.md
  - flora/README.md
  - geology/README.md
  - habitat/README.md
  - hazards/README.md
  - hydrology/README.md
  - people-dna-land/README.md
  - people/README.md
  - roads-rail-trade/README.md
  - roads/README.md
  - settlement/README.md
  - settlements-infrastructure/README.md
  - soil/README.md
  - water_planning/README.md
notes:
  - "Counts describe tracked files at the pinned Git tree, not collected pytest cases, coverage, hosted execution, or required-check state."
  - "Air, People, Roads, and Settlement are documentation-only compatibility or unresolved-placement lanes at the pinned snapshot."
  - "Tests and workflows provide bounded conformance evidence; they do not create domain truth or lifecycle authority."
[/KFM_META_BLOCK_V2] -->

# Domain test packages

`tests/domains/` is the parent navigation and execution guide for
domain-specific test packages under the canonical `tests/` responsibility
root. These packages can reject bounded contract, schema, source-role,
evidence, policy, sensitivity, lifecycle, and carrier drift. They do not define
domain meaning or authorize source admission, review, release, deployment,
promotion, or publication.

<a id="top"></a>

## Navigation

- [Purpose and authority](#purpose-and-authority)
- [Current inventory](#current-inventory)
- [Run and inspect](#run-and-inspect)
- [Confirmed workflow bindings](#confirmed-workflow-bindings)
- [Interpret results](#interpret-results)
- [Safety and authority boundaries](#safety-and-authority-boundaries)
- [Maintenance](#maintenance)
- [Known gaps](#known-gaps)

## Purpose and authority

Directory Rules place enforceability proof under `tests/`. Domain names below
that root organize assertions by subject; they do not create new top-level
authority roots.

| Concern | Authority remains with | Role of this tree |
|---|---|---|
| Domain meaning and exclusions | `docs/domains/` and accepted decisions | Exercise selected documented invariants. |
| Semantic contracts | `contracts/` | Test contract relationships without copying or redefining meaning. |
| Machine shape | `schemas/` | Exercise declared schemas and fixtures. |
| Source admission and rights | source governance and accountable review | Reject selected role, rights, provenance, or sensitivity violations. |
| Evidence and proof | governed evidence, receipt, and proof homes | Test resolution and closure rules with bounded inputs. |
| Policy and lifecycle decisions | policy, review, release, correction, and rollback authorities | Exercise finite outcomes without performing a transition. |
| Public carriers | governed APIs and released public-safe artifacts | Test selected no-leak and projection rules; never publish. |

A passing test establishes only that the executed assertions passed for the
checked-out revision and inputs. It is not proof that a claim is true, complete,
current, public-safe, reviewed, released, deployed, promoted, or published.

## Current inventory

The pinned tree contains 18 direct child directories. Fourteen contain one or
more `test_*.py` modules; four are documentation-only compatibility or
unresolved-placement lanes.

| Package | Child READMEs | Test modules | Repository-grounded boundary |
|---|---:|---:|---|
| [`agriculture/`](agriculture/README.md) | 9 | 8 | Test-bearing package; field-, operator-, and parcel-level exposure remains policy-sensitive. |
| [`air/`](air/README.md) | 1 | 0 | Compatibility guardrail; new work is directed to `atmosphere/` pending slug resolution. |
| [`archaeology/`](archaeology/README.md) | 3 | 14 | Test-bearing sensitive-domain package; exact-location, rights, cultural-review, and sovereignty boundaries remain visible. |
| [`atmosphere/`](atmosphere/README.md) | 13 | 15 | Test-bearing package; observations, models, advisories, and life-safety claims remain distinct. |
| [`fauna/`](fauna/README.md) | 15 | 13 | Test-bearing sensitive-domain package; occurrence precision and public exposure remain bounded. |
| [`flora/`](flora/README.md) | 17 | 14 | Test-bearing sensitive-domain package; taxonomy, specimen, rights, and location handling remain bounded. |
| [`geology/`](geology/README.md) | 16 | 9 | Test-bearing package with focused hosted bindings; production material and sensitive geometry remain held. |
| [`habitat/`](habitat/README.md) | 25 | 9 | Test-bearing package; modeled, critical-habitat, occurrence, and corridor roles remain distinct. |
| [`hazards/`](hazards/README.md) | 7 | 16 | Test-bearing package with focused hosted bindings; tests are not emergency or life-safety authority. |
| [`hydrology/`](hydrology/README.md) | 9 | 14 | Test-bearing package with focused hosted bindings; flow, flood, identity, and public-safe transforms remain bounded. |
| [`people-dna-land/`](people-dna-land/README.md) | 17 | 3 | Test-bearing sensitive-domain package; consent, living-person, DNA, genealogy, and land exposure default to narrow handling. |
| [`people/`](people/README.md) | 2 | 0 | Documentation-only unresolved naming surface beside `people-dna-land/`; not a parallel authority. |
| [`roads-rail-trade/`](roads-rail-trade/README.md) | 11 | 12 | Test-bearing package; legal status, temporal state, graph projection, and public precision remain distinct. |
| [`roads/`](roads/README.md) | 1 | 0 | Documentation-only compatibility slice subordinate to `roads-rail-trade/`. |
| [`settlement/`](settlement/README.md) | 1 | 0 | Conflicted documentation-only compatibility slice subordinate to `settlements-infrastructure/`. |
| [`settlements-infrastructure/`](settlements-infrastructure/README.md) | 2 | 8 | Test-bearing package; restricted geometry and critical-infrastructure exposure remain bounded. |
| [`soil/`](soil/README.md) | 1 | 9 | Test-bearing package; observation, support type, depth, lineage, and catalog closure remain distinct. |
| [`water_planning/`](water_planning/README.md) | 1 | 4 | Test-bearing package; registry candidates and geometry references remain not-released. |
| **Total** | **151** | **148** | Counts are tracked-file inventory, not collected cases or coverage. |

The package and module counts come from the exact Git trees at the metadata
snapshot. A file named `test_*.py` proves only that a candidate test module is
tracked; collection and execution are separate evidence.

## Run and inspect

There is no broad `Makefile` target for `tests/domains/` at the pinned
snapshot. The root `make test` target collects `tests/schemas` and
`tests/contracts`, not this parent lane.

Use a focused package command when changing one domain:

```bash
python -m pytest -q -p no:cacheprovider tests/domains/<domain>
```

A broad collection command is available for investigation:

```bash
python -m pytest -q -p no:cacheprovider tests/domains
```

Treat the broad command as an operator-invoked collection surface, not as a
documented green baseline. Its exact collected-case count and result were not
established for this snapshot. Domain packages can have different dependency,
fixture, and runner expectations; consult the child README and the test module
before relying on a command.

Inspect tracked inventory without executing tests:

```bash
git ls-tree -d --name-only HEAD tests/domains/
git ls-files 'tests/domains/**/README.md'
git ls-files 'tests/domains/**/test_*.py'
```

Do not run real source feeds, private services, public writes, release actions,
or AI providers merely to satisfy a domain test. A live or integration test
requires its own explicit boundary and authorization.

## Confirmed workflow bindings

Repository-wide code search identified 31 workflow files with literal
`tests/domains/` references at the pinned snapshot. The table below documents
nine representative bindings whose relevant test commands and safe conclusions
were inspected. It is intentionally non-exhaustive and is not a complete
required-check or coverage map.

Reproduce the literal-reference inventory without executing workflows:

```bash
git grep -l 'tests/domains/' -- '.github/workflows/*.yml' | sort
```

| Workflow | Explicit domain-test scope | Safe conclusion |
|---|---|---|
| [`domain-geology.yml`](../../.github/workflows/domain-geology.yml) | Selected Geology tests plus package inspection | Runs bounded Geology validation and records broader proof/release holds. |
| [`drinking-water-advisory.yml`](../../.github/workflows/drinking-water-advisory.yml) | Two Hazards advisory modules | Runs the focused advisory profile when its path filters match. |
| [`domain-hazards.yml`](../../.github/workflows/domain-hazards.yml) | Hazards smoke, materiality, and workflow-binding checks | Runs bounded Hazards validation; proof and release remain separate. |
| [`soil-moisture-observation.yml`](../../.github/workflows/soil-moisture-observation.yml) | One Soil observation module | Runs a focused deterministic soil-moisture profile. |
| [`briefing-implementation-campaign.yml`](../../.github/workflows/briefing-implementation-campaign.yml) | One Hazards materiality module | Runs a focused campaign validation, not the whole Hazards package. |
| [`archaeology-evidence-bundle-convergence.yml`](../../.github/workflows/archaeology-evidence-bundle-convergence.yml) | One Archaeology no-network module and shared fixtures | Runs a focused convergence profile. |
| [`domain-hydrology.yml`](../../.github/workflows/domain-hydrology.yml) | Selected Hydrology tests and package inspection | Runs bounded Hydrology validation and records broader holds. |
| [`habitat-critical-habitat-source-role.yml`](../../.github/workflows/habitat-critical-habitat-source-role.yml) | One Habitat source-role module | Runs a focused source-role profile. |
| [`rollback-drill.yml`](../../.github/workflows/rollback-drill.yml) | Hazards rehearsal and Agriculture drill-path inspection | Exercises bounded rollback mechanics; it does not authorize rollback or release. |

A workflow filename, path filter, queued run, skipped run, or green result does
not prove that every package or module was collected. Required-check and
branch-protection state must be verified from live repository settings.

## Interpret results

| Observation | Interpretation | Next check |
|---|---|---|
| Import or collection failure | The package did not reach its assertions. | Check declared dependencies, module layout, and child instructions. |
| Missing fixture or schema | The asserted dependency is absent or misrouted. | Verify the owning fixture/schema root; do not recreate authority under `tests/`. |
| Expected valid case fails | A bounded invariant, fixture, validator, or implementation may have drifted. | Compare the test, input, and authority source at the same revision. |
| Expected invalid case passes | Fail-closed or negative-case coverage may have regressed. | Hold the affected change and inspect validator/test logic. |
| Network or external-service access | The local profile is not self-contained. | Stop unless the test has an explicit integration boundary and authorization. |
| Focused workflow passes | Its executed scope passed at that head. | Read steps and logs before making a broader claim. |
| No dedicated workflow found | Hosted coverage is unknown. | Do not infer that the package is untested or required. |

Do not repair a failing test by weakening a contract, schema, policy rule,
sensitivity boundary, or finite outcome merely to obtain green output.

## Safety and authority boundaries

- Use synthetic or explicitly admitted public-safe fixtures for default tests.
- Keep real personal, genomic, archaeological, ecological, infrastructure, and
  precise-location data out of ordinary fixtures.
- Preserve source identity, source role, provenance, rights, temporal scope,
  sensitivity, and transform history when an assertion touches them.
- Enforce `DENY`, `ABSTAIN`, `ERROR`, quarantine, redaction, or generalization
  where the governing contract or policy requires it.
- A no-network claim is valid only when a test or workflow enforces it; folder
  placement and prose are not proof.
- Maps, tiles, dashboards, indexes, AI output, tests, and workflows remain
  downstream evidence or carriers, not sovereign truth.
- Test success is not review, merge, source admission, release, deployment,
  promotion, publication, correction approval, withdrawal approval, or
  rollback authorization.

## Maintenance

When a direct child package, child README, or `test_*.py` module changes:

1. Recompute the tracked inventory at the exact revision.
2. Update only the affected table row and aggregate counts.
3. Verify the child README's purpose, authority boundary, commands, and
   sensitivity posture.
4. Recheck explicit workflow references and path filters.
5. Run the focused package command where its dependencies are available.
6. Keep unknown ownership, required-check state, and production coupling
   explicit.

Useful count commands:

```bash
git ls-tree -d --name-only HEAD tests/domains/ | wc -l
git ls-files 'tests/domains/**/README.md' | wc -l
git ls-files 'tests/domains/**/test_*.py' | wc -l
```

## Known gaps

- The repository has no broad Make target for this parent lane at the pinned
  snapshot.
- A complete collected-case count and broad-suite result are not established.
- Repository-wide search finds 31 workflow files with literal `tests/domains/`
  references; the table documents nine representative inspected bindings. The
  remaining 22 literal matches are not classified here, and complete hosted
  coverage and required-check coupling remain unknown.
- `air/`, `people/`, `roads/`, and `settlement/` contain no `test_*.py` modules
  at the pinned snapshot and remain compatibility or unresolved-placement
  documentation.
- Child README maturity and metadata vary; this index does not silently upgrade
  their status.
- Production consumers, independent stewardship, correction propagation,
  operational rollback, and public read-back remain unverified.

Rollback this documentation change by reverting its commit or closing the
unmerged branch. That changes only the index; it does not remove test modules,
alter policy, transition lifecycle state, or withdraw a released artifact.

<p align="right"><a href="#top">Back to top</a></p>
