<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/geometry/readme
title: Flora Geometry Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Spatial data steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, validators, spatial schemas, transform receipts, release manifests, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
  - tests/domains/flora/evidence_closure/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - fixtures/domains/flora/
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/receipts/
  - data/proofs/flora/
  - release/
tags:
  - kfm
  - tests
  - flora
  - geometry
  - spatial-validation
  - topology
  - uncertainty
  - public-safe
  - map-ui
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Geometry Tests

> Test-lane contract for proving Flora spatial data is valid, bounded, uncertainty-aware, policy-safe, evidence-linked, and public-safe before it supports public KFM outputs.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Fgeometry-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Fgeometry-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** geometry test-lane README; not a spatial data store, schema home, policy bundle, fixture inventory, receipt, proof, release decision, map artifact, or public layer  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `geometry/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when spatial validity, uncertainty, policy, evidence, or release state is unresolved  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **spatial validation and map-safe geometry behavior**.

It exists to prove that Flora spatial objects are valid for their lifecycle role before they become evidence-backed map features, layer inputs, drawer context, Focus context, or release candidates. Geometry tests check spatial validity, bounds, coordinate reference expectations, uncertainty, public-safe representation, and policy gates. They do not store production spatial data or approve public release.

A mature lane should prove:

1. Flora occurrence, specimen, range, vegetation, and distribution geometries validate against expected object meaning and lifecycle state.
2. Coordinate reference, bounds, geometry type, dimensionality, and uncertainty are explicit where required.
3. Public map geometry is already public-safe before renderer styling or tiles are involved.
4. Policy-controlled spatial detail fails closed unless governed public-safe transformation and review requirements are satisfied.
5. Spatial transforms are documented through governance references where required.
6. Geometry validation is distinct from evidence closure and release approval.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/geometry/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora spatial validation and public-safe map geometry behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `geometry/` |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Contract/schema homes | `contracts/domains/flora/` and `schemas/contracts/v1/domains/flora/` when present. |
| Policy homes | `policy/domains/flora/` and `policy/sensitivity/flora/`. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/flora/`. |
| Release home | `release/`. |
| Public artifact home | `data/published/layers/flora/` when present. |

> [!WARNING]
> This directory must not become a second spatial data store, schema home, contract home, policy home, fixture inventory, receipt home, proof home, release home, public artifact home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows schema, contract, validator, policy, evidence-resolution, lifecycle, governed API, UI trust-state, e2e, runtime-proof, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive material, live network calls, duplicate authority homes, trust-bearing records, generated artifacts, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Flora docs say the domain includes occurrences, specimens, vegetation surfaces, range/distribution products, and public-safe botanical outputs | CONFIRMED from current repo docs. |
| Flora docs say some Flora spatial outputs require public-safe representation before public exposure | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual geometry schemas, validators, transform receipts, fixtures, release manifests, map artifacts, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that geometry tests, fixtures, validators, transform receipts, spatial schemas, map artifacts, or CI checks already exist.

---

## 4. Geometry rule

**Rule:** A Flora spatial object may pass geometry tests only when its geometry type, coordinate-reference expectation, bounds, uncertainty, lifecycle role, evidence support, policy state, transformation lineage, and release eligibility are valid for the tested scope.

Tests should fail or require a finite negative outcome when:

- geometry is missing where the object contract requires it;
- geometry type is incompatible with object meaning;
- coordinate reference, dimensionality, bounds, or uncertainty are missing where required;
- topology or validity checks fail for polygonal objects;
- spatial uncertainty is treated as exactness;
- policy-controlled spatial detail reaches a public fixture or output;
- public-safe derivative geometry lacks transformation lineage where required;
- renderer styling is the only thing preventing exposure;
- geometry validation is treated as evidence closure or release approval; or
- trust-bearing records are stored under `tests/`.

Tests may allow a spatial object only when the fixture is public-safe, geometry is valid for the object meaning, evidence and policy references are sufficient for the tested state, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Geometry required | Object fixture carries geometry when contract requires it. | Schema/contract assertion. |
| Geometry type | Point, line, polygon, grid, or surface form matches object meaning. | Geometry assertion. |
| CRS and bounds | Coordinate reference expectation and bounds are explicit where required. | Spatial validation assertion. |
| Topology validity | Polygonal fixtures are valid for the tested operation. | Validator assertion. |
| Uncertainty | Spatial uncertainty is recorded and not treated as exactness. | Uncertainty assertion. |
| Public-safe derivative | Public map geometry is policy-safe before style/tile rendering. | Policy/spatial assertion. |
| Transformation lineage | Public-safe derivative links to governance reference where required. | Receipt/reference assertion. |
| Evidence boundary | Geometry validity does not replace evidence closure. | Boundary assertion. |
| Release boundary | Geometry validity does not approve publication. | Release-boundary assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain README material and tests that call canonical spatial, schema, contract, evidence, policy, transform, release, and validator code from owning roots.

It may include negative tests for missing geometry, wrong geometry type, invalid topology, missing uncertainty, invalid bounds, missing transformation lineage, style-only protection, and geometry/evidence/release boundary collapse.

It may include positive tests for public-safe spatial fixtures with required governance references and tiny test-local spatial examples when documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain production spatial data, source records, reusable fixture inventories, schemas, contracts, policy definitions, trust-bearing receipts, proofs, release decisions, published layers, production tiles, credentials, generated model output, or default tests that require live network access.

---

## 8. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model spatial validation states rather than include production source material or trust-bearing records.

Expected fixture families include valid occurrence point, valid specimen-derived point with uncertainty, valid vegetation polygon, valid range polygon, valid public-safe derivative, missing geometry, wrong geometry type, invalid polygon, missing uncertainty, out-of-bounds coordinate, style-only protection anti-pattern, missing transformation lineage, and geometry-without-release boundary.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, spatial validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/geometry
pytest tests/domains/flora/evidence_closure
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which Flora spatial schemas are canonical? | NEEDS VERIFICATION | Must inspect schema roots. |
| Which spatial validator owns geometry checks? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which transform receipt family records public-safe spatial derivatives? | NEEDS VERIFICATION | Must inspect receipt/proof roots and policy docs. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which map layer artifacts depend on Flora geometry validation? | NEEDS VERIFICATION | Must inspect publication roots. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |
| Should shared spatial tests live here or under a cross-domain spatial test root? | OPEN | This lane should own Flora-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora geometry tests run locally.
- [ ] Valid occurrence, specimen, vegetation polygon, range polygon, public-safe derivative, missing geometry, wrong type, invalid topology, missing uncertainty, out-of-bounds coordinate, missing transformation lineage, and style-only protection cases are tested.
- [ ] Positive public-safe fixtures prove allowed geometry behavior without becoming publication approval.
- [ ] Negative fixtures prove fail-closed behavior for unresolved or unsafe spatial states.
- [ ] Tests call canonical spatial/schema/contract/evidence/policy/release validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora geometry proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora geometry test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for schema/contract/validator/policy/evidence/lifecycle/API/UI/e2e/runtime/domain tests, and Flora public-safe spatial doctrine; executable tests, fixtures, spatial schemas, validators, transform receipts, release manifests, map artifacts, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
