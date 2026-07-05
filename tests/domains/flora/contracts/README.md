<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/flora/contracts/readme
title: Flora Contracts Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Flora steward>
  - <PLACEHOLDER — Contract steward>
  - <PLACEHOLDER — Schema steward>
  - <PLACEHOLDER — Test steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, contracts, schemas, validators, and CI not verified
related:
  - tests/README.md
  - tests/domains/flora/README.md
  - tests/domains/flora/citation/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/README.md
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - fixtures/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/registry/sources/flora/
  - release/
tags:
  - kfm
  - tests
  - flora
  - contracts
  - object-meaning
  - schema-contract-split
  - source-role
  - lifecycle-role
  - evidence
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Flora Contracts Tests

> Test-lane contract for proving Flora object meaning matches the domain contracts, stays separate from machine schema shape, and preserves evidence, source-role, lifecycle, policy, and release semantics.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fflora%2Fcontracts-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fflora%2Fcontracts-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** contracts test-lane README; not a contract home, schema home, policy bundle, source registry, fixture inventory, receipt, proof, release decision, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/flora/`  
**Lane:** `contracts/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when contract meaning is missing, ambiguous, or incompatible with lifecycle/policy/evidence roles  
**Last reviewed:** 2026-07-05

---

## 1. Purpose

This directory is the Flora domain test lane for **contract behavior**.

It exists to prove that Flora object meaning is stable, reviewable, and consistent with the semantic contracts under `contracts/domains/flora/`. Contract tests check vocabulary and lifecycle role; they do not define the contract, replace schemas, admit sources, approve releases, or publish data.

A mature lane should prove:

1. Flora object terms have a canonical contract entry before they are treated as governed objects.
2. Contract meaning and schema shape remain separate.
3. Source-role, evidence, lifecycle, rights, sensitivity, review, release, and correction semantics are preserved across object families.
4. Cross-domain relations keep ownership boundaries visible.
5. Generated text, UI labels, and map layer names do not redefine contract meaning.
6. Unsupported or ambiguous object meaning fails closed instead of silently passing.
7. Default tests use deterministic public-safe fixtures only.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/flora/contracts/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Flora contract semantics. |
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `contracts/` |
| Contract home | `contracts/domains/flora/` when present. |
| Schema home | `schemas/contracts/v1/domains/flora/` when present. |
| Fixture home | `fixtures/domains/flora/` unless tiny test-local examples are documented. |
| Policy homes | `policy/domains/flora/` and `policy/sensitivity/flora/`. |
| Source registry home | `data/registry/sources/flora/` when present. |
| Release home | `release/`. |

> [!WARNING]
> This directory must not become a second contract home, schema home, policy home, source registry, fixture inventory, receipt home, proof home, release home, public artifact home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows contract tests, schema tests, validator tests, policy tests, evidence-resolution tests, lifecycle-state tests, governed API envelope tests, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes production code, live network calls, duplicate authority homes, trust-bearing records, and release decisions from `tests/` | CONFIRMED from current repo docs. |
| Flora docs separate object meaning under `contracts/domains/flora/` from machine shape under `schemas/contracts/v1/domains/flora/` | CONFIRMED from current repo docs. |
| Flora docs place Flora tests under `tests/domains/flora/` | CONFIRMED from current repo docs. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual Flora contract files, schema files, validators, fixtures, and CI jobs | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that contract tests, semantic contract files, schemas, validators, fixtures, or CI checks already exist.

---

## 4. Contract rule

**Rule:** A Flora object, relation, UI label, API payload, or map-facing concept may pass contract tests only when its meaning aligns with the canonical Flora contract and does not collapse semantic meaning into schema shape, source metadata, generated text, or presentation.

Tests should fail or require a finite negative outcome when:

- a Flora object has no canonical contract entry;
- a schema field is treated as the semantic contract;
- object meaning conflicts with lifecycle role;
- source role is collapsed into a generic authority label;
- a derived product is treated as an observed object without contract support;
- cross-domain relations erase ownership boundaries;
- policy or release state changes the meaning of the object instead of governing its admissibility;
- generated text, UI labels, map layer names, or screenshots redefine object semantics; or
- contract fixtures are stored as reusable authority under `tests/` rather than the owning roots.

Tests may allow a contract assertion only when the fixture is public-safe, meaning is anchored to the relevant contract, schema references remain shape-only, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Contract entry exists | Object term maps to canonical Flora contract where present. | Contract assertion. |
| Contract/schema split | Machine fields do not replace semantic meaning. | Split assertion. |
| Lifecycle role | Object meaning matches RAW/WORK/PROCESSED/CATALOG/PUBLISHED role. | Lifecycle assertion. |
| Source-role semantics | Authority, observation, context, and model roles remain distinct. | Source-role assertion. |
| Evidence semantics | Evidence support remains distinct from object definition. | Evidence-boundary assertion. |
| Relation ownership | Cross-domain relation preserves owner domain and source role. | Relation assertion. |
| Policy boundary | Policy gates admissibility without redefining meaning. | Policy-boundary assertion. |
| Release boundary | Release state permits exposure but does not redefine the object. | Release-boundary assertion. |
| Presentation boundary | UI/map/generated text cannot redefine contract terms. | Presentation-boundary assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Flora contract tests.
- Tests that call canonical contract, schema, source, evidence, policy, release, and validator code from owning roots.
- Negative tests for missing contract entry, schema-as-contract, source-role collapse, lifecycle mismatch, relation ownership collapse, and presentation redefining meaning.
- Positive tests for public-safe object fixtures that match canonical Flora contract meaning.
- Tiny test-local examples when documented and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain contract definitions, schemas, source descriptors, source records, reusable fixture inventories, policy definitions, receipts, proofs, release decisions, published artifacts, production code, generated model output, credentials, or default tests that require live network access.

---

## 8. Fixture posture

Reusable Flora fixtures should normally live under:

```text
fixtures/domains/flora/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model object-meaning and relation-semantics states rather than become canonical contract records.

Expected fixture families include valid plant taxon, valid occurrence, valid specimen record, valid vegetation community, valid range product, missing contract entry, schema-as-contract anti-pattern, source-role collapse, relation ownership collapse, policy-as-meaning anti-pattern, release-as-meaning anti-pattern, and presentation-label anti-pattern.

---

## 9. Suggested local commands

> [!NOTE]
> Command names, validators, test runners, markers, workflow names, and exact package commands are **NEEDS VERIFICATION** until checked against actual repository configuration.

```bash
pytest tests/domains/flora/contracts
pytest tests/domains/flora
python tools/validate_all.py
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| Which Flora contract files are canonical? | NEEDS VERIFICATION | Must inspect `contracts/domains/flora/`. |
| Which schema files should contract tests cross-check without replacing semantics? | NEEDS VERIFICATION | Must inspect schema roots. |
| Which validator owns contract-vs-schema checks? | NEEDS VERIFICATION | Must inspect validator/tool roots. |
| Which fixture families already exist? | NEEDS VERIFICATION | Must inspect `fixtures/domains/flora/`. |
| Which cross-domain relation tests belong outside this Flora segment? | OPEN | Shared relation tests may require a cross-domain root. |
| Which CI job runs this lane? | NEEDS VERIFICATION | Must inspect `.github/workflows/`. |

---

## 11. Definition of done

This lane is mature when:

- [ ] Flora contract tests run locally.
- [ ] Missing contract entry, schema-as-contract, source-role collapse, lifecycle mismatch, relation ownership collapse, policy-as-meaning, release-as-meaning, and presentation-label cases are tested.
- [ ] Positive public-safe fixtures prove allowed contract behavior without becoming contract authority.
- [ ] Tests call canonical contract/schema/source/evidence/policy/release validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Flora contract proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Flora contracts test lane. |

---

## 13. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, root test allowance for contract/schema/validator/policy/evidence/lifecycle/API/domain tests, and Flora contract/schema responsibility split; executable tests, fixtures, contracts, schemas, validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
