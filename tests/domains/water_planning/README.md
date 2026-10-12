<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-water-planning-readme
title: tests/domains/water_planning README
type: test-readme
version: v0.1
status: confirmed-test-surface; registry-records-not-released
owner: @bartytime4life (CODEOWNERS review routing only); local steward NEEDS VERIFICATION
created: 2026-07-30
updated: 2026-07-30
policy_label: repository-facing; water-planning; deterministic; no-network; fail-closed; non-authoritative
owning_root: tests/
responsibility: documents the bounded water-planning regression suite, fixture strategy, deterministic outcomes, no-network controls, CI integration, failure interpretation, authority limits, recovery, and maintenance expectations
truth_posture: cite-or-abstain; test claims are grounded in current repository modules and fixtures; passing tests are not source admission, evidence, proof, policy approval, release, deployment, publication, or public truth
related:
  - test_status_collapse.py
  - test_geometry_authority.py
  - test_rac_registry.py
  - ../README.md
  - ../../README.md
  - ../../../tools/validators/domains/water_planning/README.md
  - ../../../fixtures/domains/water_planning/
  - ../../../contracts/domains/water_planning/README.md
  - ../../../schemas/contracts/v1/domains/water_planning/README.md
  - ../../../.github/workflows/briefing-integration.yml
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This v0.1 replaces the one-newline placeholder introduced by merged pull request #1847."
  - "The suite contains three unittest modules and 20 declared test methods at the review snapshot; that inventory is not a claim that a current run passed."
  - "Status-collapse and geometry-authority fixtures are synthetic. RAC registry tests read pinned repository candidates whose release posture remains not-released."
  - "The no-network harness blocks selected Python socket and urllib entrypoints. It is a regression guard, not a general operating-system network sandbox."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Water-planning domain tests

[![briefing-integration](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml/badge.svg?branch=main)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml)
[![Test surface: 3 modules](https://img.shields.io/badge/test_surface-3_modules-1f883d)](#suite-index)
[![Posture: deterministic and no-network](https://img.shields.io/badge/posture-deterministic_%7C_no--network-0969da)](#determinism-and-no-network-controls)
[![Release: not authorized](https://img.shields.io/badge/release-not_authorized-b42318)](#authority-boundary)

> **Purpose.** `tests/domains/water_planning/` holds deterministic regression tests for water-planning semantic anti-collapse, region and geometry authority references, and the pinned Kansas Water Office Regional Advisory Committee registry slice.

> [!IMPORTANT]
> A green test result means only that the tested revision satisfied these bounded assertions. It is not source admission, source freshness, rights clearance, evidence or proof closure, a policy decision, governance approval, release, deployment, publication, or public truth.

## Quick navigation

- [Scope and placement](#scope-and-placement)
- [Authority boundary](#authority-boundary)
- [Directory map](#directory-map)
- [Suite index](#suite-index)
- [Quick start](#quick-start)
- [Inputs and fixture strategy](#inputs-and-fixture-strategy)
- [Coverage by test family](#coverage-by-test-family)
- [Determinism and no-network controls](#determinism-and-no-network-controls)
- [Outcome semantics](#outcome-semantics)
- [CI integration](#ci-integration)
- [Failure interpretation](#failure-interpretation)
- [Limitations and open verification](#limitations-and-open-verification)
- [Maintenance](#maintenance)
- [Related authority](#related-authority)
- [Rollback](#rollback)

## Scope and placement

| Field | Current posture |
|---|---|
| Purpose | Prove bounded water-planning validator behavior without defining domain truth or publishing data. |
| Inherited parent | [`tests/domains/`](../README.md) |
| Test-root index | [`tests/`](../../README.md) |
| Owning responsibility root | `tests/` |
| Scope identifier | `water_planning` |
| Runner | Python standard-library `unittest` discovery |
| Direct test modules | Three modules with 20 declared test methods at the pinned review snapshot |
| Inputs | Synthetic JSON fixtures and explicitly pinned, checked-in registry/GeoJSON candidates |
| Outputs | Test-runner assertions, stdout capture, and process status; no repository artifacts are written |
| Exposure | Public repository tests; synthetic fixtures and checked-in public-source-derived candidates only |
| Review routing | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) routes `tests/` review to `@bartytime4life`; routing is not proof of independent review or approval |
| Local steward | **NEEDS VERIFICATION.** No separate water-planning test steward is established here |
| Review snapshot | Code, fixtures, workflow, and adjacent authority inspected on 2026-07-30 at [`main@af782516`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/af782516085171962c0063b688b3e0b42ee8523b) |

This existing path is a `PLACE` outcome under the accepted [Directory Rules](../../../docs/doctrine/directory-rules.md) and [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md): `tests/` owns executable conformance evidence, and `water_planning` is a domain lane inside that responsibility root. The compact boundary profile applies because this directory changes scope and validation responsibility. Relevant rules include `DIR-SCOPELANE-001`, `DIR-SCOPELANE-003`, `DIR-README-001` through `DIR-README-004`, and the test dependency boundary in §14.

[Back to top](#top)

## Authority boundary

| This lane may | This lane must not |
|---|---|
| Assert finite behavior for the linked validators. | Define canonical water-planning meaning; semantic authority belongs in `contracts/`. |
| Exercise valid, invalid, malformed, missing, drifted, and overclaiming inputs. | Author machine shapes; schema authority belongs in `schemas/`. |
| Pin expected identities, digests, counts, ordering, and release-denial posture for a bounded repository snapshot. | Fetch or activate a source, silently refresh a baseline, or claim source freshness. |
| Fail when selected Python network entrypoints are used. | Present the regression harness as a complete network sandbox. |
| Check that protected values are not echoed by validator findings or CLI output. | Store credentials, private portal data, real applicants or recipients, restricted records, or exact sensitive locations. |
| Supply executable conformance evidence to a read-only workflow. | Treat a test, workflow, badge, commit, or merge as evidence, proof, review, release, deployment, or publication authority. |

Current truth states:

- **CONFIRMED:** three test modules, their imported validator entrypoints, referenced fixture/data inputs, selected no-network patches, and a read-only workflow job exist at the review snapshot.
- **CONFIRMED:** the status-collapse and geometry-authority lanes use synthetic fixtures; the RAC registry lane reads checked-in candidate records and geometry whose asserted release posture is `not-released`.
- **NEEDS VERIFICATION:** independent stewardship, effective branch-protection requirements, current hosted check results for any future revision, source freshness, rights clearance, governance membership, broader evidence closure, and public-release eligibility.
- **UNKNOWN:** whether external consumers depend on the exact test names or diagnostic strings beyond the repository evidence inspected here.

[Back to top](#top)

## Directory map

The current direct children are:

```text
water_planning/
├── README.md
├── test_geometry_authority.py
├── test_rac_registry.py
└── test_status_collapse.py
```

Reusable fixtures, validators, contracts, schemas, registry records, processed candidates, and workflow configuration remain in their own responsibility roots.

[Back to top](#top)

## Suite index

| Module | Declared methods | Primary subject | Input class | Key regression burden |
|---|---:|---|---|---|
| [`test_status_collapse.py`](./test_status_collapse.py) | 3 | [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) | One valid and 13 invalid synthetic fixtures | Exact finding sets, anti-collapse rules, unresolved-state posture, lineage, blocked behavior, and protected-value non-echo |
| [`test_geometry_authority.py`](./test_geometry_authority.py) | 9 | [`validate_geometry_authority.py`](../../../tools/validators/domains/water_planning/validate_geometry_authority.py) | Valid/invalid synthetic authority envelopes plus in-memory mutations | RAC identity inventory, digest and correction lineage, reference-only geometry/crosswalk authority, project/region separation, deterministic CLI output, and finite missing-input behavior |
| [`test_rac_registry.py`](./test_rac_registry.py) | 8 | [`validate_rac_registry.py`](../../../tools/validators/domains/water_planning/validate_rac_registry.py) | Pinned checked-in dataset, crosswalk, GeoJSON, and source records | Geometry digest, 14-region identity, 105-county coverage, ordered 209-row mapping baseline, overlap classes, duplicate rejection, disabled connectors, and not-released posture |

The method count is a source inventory, not a pass-rate claim. `subTest` cases and in-memory mutations exercise more scenarios than the method count alone represents.

[Back to top](#top)

## Quick start

Run from the repository root with Python 3.11 or the repository-supported equivalent:

```bash
python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_*.py' \
  --verbose
```

At the review snapshot, discovery should find the three modules and 20 declared test methods listed above. Treat the observed runner output—not this documentation—as the result for a particular revision.

To inspect validator commands and stdout contracts, use the [water-planning validator README](../../../tools/validators/domains/water_planning/README.md). The hosted workflow separately invokes the RAC registry CLI after the Python suite.

[Back to top](#top)

## Inputs and fixture strategy

### Synthetic semantic fixtures

[`test_status_collapse.py`](./test_status_collapse.py) reads:

- [`status_collapse/valid/valid_1.json`](../../../fixtures/domains/water_planning/status_collapse/valid/valid_1.json);
- 13 targeted files under [`status_collapse/invalid/`](../../../fixtures/domains/water_planning/status_collapse/invalid/meeting_is_approval.json), each bound to an exact expected finding set.

The invalid family covers forbidden lifecycle/status collapse, guessed identities and geometries, collapsed amount facts, erased lineage, and blocked portal/personal-data/connector/proof/release/publication behavior.

### Synthetic authority fixtures

[`test_geometry_authority.py`](./test_geometry_authority.py) reads:

- [`geometry_authority/valid/valid_1.json`](../../../fixtures/domains/water_planning/geometry_authority/valid/valid_1.json);
- [`geometry_authority/invalid/invalid_1.json`](../../../fixtures/domains/water_planning/geometry_authority/invalid/invalid_1.json).

The suite deep-copies or reloads the valid document, applies one bounded mutation, recomputes digests when the scenario requires it, and asserts the resulting finite finding code and JSON path. The [fixture notes](../../../fixtures/domains/water_planning/geometry_authority/README.md) describe the synthetic, reference-only authority boundary.

### Pinned registry candidates

[`test_rac_registry.py`](./test_rac_registry.py) reads five checked-in inputs:

| Input | Repository path | Test posture |
|---|---|---|
| Dataset record | [`kwo_rac_regions_2026-06-24.json`](../../../data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json) | Candidate registry metadata; expected `not-released` |
| County crosswalk record | [`kwo_rac_counties_2026-06-24__tiger2025.json`](../../../data/registry/crosswalks/water_planning/kwo_rac_counties_2026-06-24__tiger2025.json) | Geometry-overlap crosswalk; not governance membership |
| Geometry bytes | [`kwo_rac_regions_2026-06-24.geojson`](../../../data/processed/water_planning/rac_regions/kwo_rac_regions_2026-06-24.geojson) | Digest- and byte-count-pinned processed candidate |
| KWO source record | [`kwo_rac_feature_service.source.json`](../../../data/registry/sources/water_planning/kwo_rac_feature_service.source.json) | Connector expected disabled; public release expected false |
| Census source record | [`census_tigerweb_counties_2025.source.json`](../../../data/registry/sources/water_planning/census_tigerweb_counties_2025.source.json) | Connector expected disabled; public release expected false |

These tests deliberately do not refetch public services or independently reconstruct spatial intersections. A changed source observation requires a separate governed update to the owning records, digests, lineage, validation, and review.

### Rights and sensitivity posture

- Keep default fixtures synthetic, minimized, and public-safe.
- Do not add credentials, cookies, portal exports, living-person data, real applicant/recipient details, private addresses, restricted source payloads, or harmful precision.
- Treat checked-in public-source-derived candidates as repository inputs with their recorded rights, review, connector, and release posture; test presence does not clear those gates.
- Diagnostics must expose finite codes and paths rather than protected values.

[Back to top](#top)

## Coverage by test family

### Semantic anti-collapse

The status-collapse suite checks that:

- meetings, applications, recommendations, awards, payments, construction, completion, program versions, scoring matrices, and project outcomes remain distinct;
- applicant identity, recipient identity, project geometry, and regional geometry are not guessed;
- requested, recommended, awarded, agreed, paid, and expended amounts remain separate;
- correction and supersession lineage fields remain present;
- authenticated portal, personal-data, real-applicant, real-project, connector, proof, release, and publication behaviors remain blocked in synthetic candidates;
- invalid output does not echo protected canary values.

### Region and geometry authority

The geometry-authority suite checks that:

- the ordered identity inventory remains exactly `kwo-rac-01` through `kwo-rac-14` with the pinned names and KFM-assigned ordinals;
- those ordinals are not represented as KWO-native numeric identifiers;
- foreign namespaces, gaps, duplicates, out-of-range identifiers, name drift, digest drift, and incomplete correction lineage fail closed;
- region geometry and county crosswalks remain reference-only;
- regional membership and project location geometry remain separate facts;
- unresolved, approximate, and confirmed states require coherent references;
- inline addresses and coordinates are rejected without value echo;
- valid and invalid CLI output is deterministic, and missing input yields a finite finding.

### RAC registry baseline

The registry suite checks that:

- processed geometry bytes match the pinned dataset digest and size;
- feature identity remains the expected 14-region inventory;
- the crosswalk covers all 105 Kansas county GEOIDs through 209 ordered positive-area intersections;
- overlap-class counts and the mapping digest remain stable;
- a boundary sliver cannot be relabeled as dominant membership;
- duplicate mapping keys and renamed regions fail;
- dataset and crosswalk records cannot claim release;
- KWO and Census source descriptors cannot silently activate connectors or allow public release.

[Back to top](#top)

## Determinism and no-network controls

| Control | Verified implementation |
|---|---|
| Selected network denial | Every module patches `socket.socket.connect`, `socket.create_connection`, and `urllib.request.urlopen` so use raises `AssertionError`. |
| Local-only inputs | Tests read repository files through `pathlib.Path`; no source service is called. |
| Stable expected findings | Tests compare exact `(code, path)` sets or tuples where order is part of the contract. |
| Stable CLI rendering | Geometry tests run valid and invalid CLI paths twice and compare exact stdout. |
| Protected-value non-echo | Status and geometry tests assert selected canary values are absent from rendered output. |
| In-memory mutation | Drift cases modify loaded copies rather than changing repository files. |
| Read-only workflow token | The linked workflow declares only `contents: read` and checks out without persisted credentials. |
| Bounded files | Validator-side file-size limits and finite missing/malformed findings are covered where declared. |

The socket and URL patches are targeted Python-level guards. They do not prove that every possible network mechanism, subprocess, native extension, or operating-system path is blocked. Run the suite in a network-denied environment when a stronger execution boundary is required.

[Back to top](#top)

## Outcome semantics

Keep these vocabularies separate:

| Surface | Success | Non-success | Meaning boundary |
|---|---|---|---|
| Python `unittest` runner | Process exit `0` and runner `OK` | Assertion failure, test error, collection/import error, interruption, or nonzero exit | The declared tests completed for that revision |
| Status-collapse validator | JSON `outcome: "PASS"` | JSON `outcome: "FAIL"` with finite findings | Synthetic semantic envelope only |
| Geometry-authority validator | JSON `outcome: "VALIDATOR_PASS"` | JSON `outcome: "VALIDATOR_FAIL"` with finite findings | Synthetic identity/reference authority only |
| RAC registry CLI | `RAC_REGISTRY_OK ...` and exit `0` | Sorted tab-separated findings and nonzero exit | Pinned checked-in registry slice only |
| GitHub Actions job | Hosted job success | Hosted job failure, cancellation, timeout, or platform error | Workflow execution state; not KFM truth or release state |

Do not translate a runner result into `ANSWER`, `ABSTAIN`, `DENY`, `ALLOW`, `HOLD`, promotion, release, or publication state unless an owning contract explicitly defines that transition.

[Back to top](#top)

## CI integration

The read-only [`briefing-integration`](../../../.github/workflows/briefing-integration.yml) workflow includes the `preserve-water-planning-anti-collapse` job. Changes under `tests/domains/water_planning/**` trigger it for pull requests and pushes to `main`.

The job:

1. checks out the tested revision without persisted credentials;
2. sets up Python 3.11;
3. runs `unittest` discovery across every `test_*.py` module in this directory;
4. invokes `validate_rac_registry.py` against its checked-in defaults; and
5. records an explicit summary that green CI is not source freshness, rights clearance, governance membership, evidence closure, release, deployment, or publication.

The workflow declares `contents: read`, uses GitHub-hosted `ubuntu-latest`, and sets `KFM_NO_NETWORK=1` at workflow scope. The module-level patches remain the directly inspected no-network regression guard. This README does not claim that the workflow is a required branch-protection check or that its latest run passed.

[Back to top](#top)

## Failure interpretation

| Symptom | Likely class | Safe next action |
|---|---|---|
| Import or discovery error | Test environment, module path, or dependency drift | Reproduce from repository root; inspect the first collection/import error before changing assertions. |
| `AssertionError` from `_unexpected_network` | Test or imported code attempted a blocked Python network path | Remove the live dependency or move it behind a separately governed integration test; do not weaken the default guard. |
| Expected finding set changed | Validator behavior, fixture shape, or finding vocabulary drift | Compare contract/schema/validator intent; update implementation and the smallest matching fixture/test atomically when authorized. |
| Protected canary appears in output | Diagnostic redaction/non-echo regression | Treat as a fail-closed privacy defect; remove value echo and add a targeted regression. |
| Geometry digest or byte count changed | Pinned baseline drift or accidental file mutation | Stop; verify source, version, derivation, rights, lineage, digest, and correction posture before accepting new bytes. |
| Region, county, mapping, or overlap count changed | Identity/crosswalk derivation drift | Recompute only through the governed source and derivation process; never edit expected counts merely to make the test green. |
| Connector or release assertion changed | Authority-state regression | Restore disabled/not-released posture or route a separately authorized governance change through its owning roots. |
| Hosted job fails while local tests pass | Workflow, runner, checkout, platform, or environment difference | Inspect the exact hosted job and step; do not classify it as a content regression without evidence. |

Do not bypass a failing assertion, delete a negative fixture, loosen an expected code, or repin a digest solely to obtain green status.

[Back to top](#top)

## Limitations and open verification

Passing this suite does **not** prove:

- that KWO or Census source observations are current, complete, licensed for every use, or independently reviewed;
- that the RAC geometry or county-overlap derivation is authoritative for governance membership;
- that a meeting caused approval, an award caused payment, or payment caused construction or completion;
- that any applicant, recipient, project, location, or benefit has been resolved;
- that semantic contracts or schemas are accepted, complete, or backward compatible;
- that policy, evidence, proof, review, promotion, release, correction, withdrawal, rollback, API, UI, map, search, graph, export, Focus Mode, or AI behavior is closed;
- that every network mechanism is blocked;
- that performance, concurrency, fuzzing, property-based behavior, hostile resource exhaustion, or platform-specific behavior has been tested;
- that hosted checks are required, passing, or immune to repository-control divergence.

Open verification:

- establish an independently reviewable stewardship route when an eligible identity exists;
- verify effective branch protection, required-check names, and bypass actors outside this README;
- observe hosted checks on the exact future PR head;
- review fixture and registry rights/sensitivity posture whenever source or exposure changes;
- add new test families only with a grounded contract, validator behavior, public-safe input strategy, and bounded failure vocabulary.

[Back to top](#top)

## Maintenance

- Keep the direct-child tree and suite index synchronized with committed modules.
- Update declared method counts only after inspecting the exact source; never use the count as a coverage or pass-rate badge.
- Preserve deterministic ordering, finite finding codes, JSON paths, non-echoing diagnostics, read-only execution, and selected network-denial patches.
- Keep reusable synthetic inputs under [`fixtures/domains/water_planning/`](../../../fixtures/domains/water_planning/) rather than embedding large fixture payloads in test modules.
- Keep contracts, schemas, policy, source records, processed candidates, receipts, proofs, release decisions, and published carriers in their owning roots.
- When a validator contract changes, update the validator, smallest relevant valid/invalid case, regression assertion, validator documentation, and this README in the same authorized review unit when paths permit.
- Treat pinned identity, geometry, source, digest, county, mapping, overlap, connector, rights, and release expectations as governed baseline changes.
- Do not replace a negative test with a weaker assertion merely to accommodate drift.
- Rerun the complete domain suite after focused tests pass.
- Reverify links and workflow routing when paths or names change.

[Back to top](#top)

## Related authority

| Surface | Role |
|---|---|
| [`tests/domains/`](../README.md) | Parent domain-test boundary and inherited posture |
| [`tests/`](../../README.md) | Repository test-root contract |
| [`tools/validators/domains/water_planning/`](../../../tools/validators/domains/water_planning/README.md) | Validator responsibility, CLI contracts, finite findings, and recovery guidance |
| [`fixtures/domains/water_planning/`](../../../fixtures/domains/water_planning/geometry_authority/README.md) | Reusable synthetic/public-safe inputs and fixture-specific notes |
| [`contracts/domains/water_planning/`](../../../contracts/domains/water_planning/README.md) | Semantic meaning and anti-collapse boundaries |
| [`schemas/contracts/v1/domains/water_planning/`](../../../schemas/contracts/v1/domains/water_planning/README.md) | Machine-readable shapes |
| [`data/registry/`](../../../data/registry/README.md) | Source, dataset, crosswalk, and release-posture records |
| [`data/processed/water_planning/rac_regions/`](../../../data/processed/water_planning/rac_regions/README.md) | Pinned processed RAC geometry candidate |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Accepted repository placement authority through ADR-0029 |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption decision for the canonical Directory Rules bytes |
| [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) | GitHub review routing only |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only pull-request and `main` validation |

[Back to top](#top)

## Rollback

Before merge, close the draft pull request and abandon its branch to retain the one-newline baseline. After merge, revert the single documentation commit through a reviewed corrective pull request. Do not rewrite shared history.

No test code, fixture, validator, contract, schema, workflow, registry record, processed candidate, source activation, proof, release, deployment, or publication state changes with this README-only update.

[Back to top](#top)
