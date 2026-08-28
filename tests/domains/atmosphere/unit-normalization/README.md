<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/unit-normalization/readme
title: Atmosphere Unit Normalization Test Lane README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Atmosphere steward>
  - <PLACEHOLDER — Normalization steward>
  - <PLACEHOLDER — Unit steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Evidence/governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; executable tests, fixtures, validator behavior, and CI not verified
related:
  - tests/README.md
  - tests/domains/atmosphere/README.md
  - docs/doctrine/directory-rules.md
  - pipelines/domains/atmosphere/normalize/README.md
  - data/receipts/atmosphere/unit_conversion/README.md
  - contracts/domains/atmosphere/AirObservation.md
  - contracts/domains/atmosphere/PM25Observation.md
  - contracts/domains/atmosphere/OzoneObservation.md
  - contracts/domains/atmosphere/AODRaster.md
  - schemas/contracts/v1/domains/atmosphere/
  - fixtures/domains/atmosphere/
  - tools/validators/
  - policy/domains/atmosphere/
  - data/receipts/
  - data/proofs/
  - release/
tags:
  - kfm
  - tests
  - atmosphere
  - unit-normalization
  - unit-conversion
  - normalization
  - units
  - transform-receipt
  - evidence
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Atmosphere Unit Normalization Tests

> Test-lane contract for proving Atmosphere unit normalization preserves source units, normalized units, conversion method, pollutant or variable identity, averaging-period context, evidence hooks, and receipt boundaries.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere%2Funit--normalization-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere%2Funit--normalization-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: no--network](https://img.shields.io/badge/posture-no--network-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** test-lane README; not a unit registry, normalization implementation, schema, contract, policy, fixture inventory, receipt, proof, or release decision  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `unit-normalization/`  
**Default posture:** fail closed on unit ambiguity; cite-or-abstain for unsupported claims  
**Last reviewed:** 2026-07-05

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [Rule statement](#4-rule-statement)
5. [What belongs here](#5-what-belongs-here)
6. [What does not belong here](#6-what-does-not-belong-here)
7. [Normalization proof matrix](#7-normalization-proof-matrix)
8. [Fixture contract](#8-fixture-contract)
9. [Expected outcomes](#9-expected-outcomes)
10. [Lifecycle and authority boundaries](#10-lifecycle-and-authority-boundaries)
11. [No-network default](#11-no-network-default)
12. [Suggested local commands](#12-suggested-local-commands)
13. [Review burden](#13-review-burden)
14. [Related folders and files](#14-related-folders-and-files)
15. [Open questions](#15-open-questions)
16. [Definition of done](#16-definition-of-done)
17. [Changelog](#17-changelog)
18. [Last reviewed](#18-last-reviewed)

---

## 1. Purpose

This directory is the Atmosphere / Air test lane for **unit normalization** behavior.

It exists to prove that unit conversion and normalization are governed transformations, not silent edits. Tests in this lane should verify that source-unit values are normalized only when the method, target unit, factor or formula reference, object meaning, and downstream receipt expectations are explicit.

A mature lane should support these claims:

1. **Original units travel.** Source units are retained or referenced after normalization.
2. **Target units are explicit.** Normalized values declare the target unit and parameter identity.
3. **Conversion method is auditable.** The conversion factor, formula, method ID, method version, or equivalent method reference is recorded.
4. **Object meaning is preserved.** Unit conversion does not turn one object family or knowledge character into another.
5. **Averaging-period context is preserved.** Units are tested with temporal and parameter context where those fields affect interpretation.
6. **Receipts remain separate.** Transform receipt records support auditability but do not become proofs, catalog truth, or release approval.
7. **Ambiguity fails closed.** Missing or conflicting units produce finite failure or review outcomes.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/unit-normalization/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Atmosphere unit normalization behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Test lane | `unit-normalization/` |
| Normalization logic home | `pipelines/domains/atmosphere/normalize/` |
| Receipt home | `data/receipts/atmosphere/unit_conversion/` or accepted receipt layout. |
| Contract home | `contracts/domains/atmosphere/` |
| Schema home | `schemas/contracts/v1/domains/atmosphere/` |
| Validator home | `tools/validators/` |
| Fixture home | `fixtures/domains/atmosphere/` unless tiny local test-only samples are documented. |
| Policy home | `policy/domains/atmosphere/` |
| Release home | `release/` |

> [!WARNING]
> This directory tests normalization behavior. It must not define canonical units, conversion policy, production transformation code, source registries, receipts, proofs, or release decisions.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows domain-specific tests under `tests/domains/<domain>/` | CONFIRMED from current repo docs. |
| `tests/README.md` allows validator, schema, policy, lifecycle, and evidence-resolution tests | CONFIRMED from current repo docs. |
| Atmosphere normalize README discusses units, conversions, receipts, and anti-collapse rules | CONFIRMED from current repo evidence. |
| Unit-conversion receipt README exists | CONFIRMED from current repo evidence. |
| PM2.5 and ozone contracts require units and source-role separation | CONFIRMED from current repo evidence. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Canonical unit registry or conversion table | NEEDS VERIFICATION. |
| Canonical validator command/module | NEEDS VERIFICATION. |
| Fixture inventory | NEEDS VERIFICATION. |
| CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the test-lane contract. It does not claim that conversion logic, unit registries, fixtures, validators, receipt payloads, or CI gates are implemented.

---

## 4. Rule statement

**Rule:** Atmosphere unit normalization must be explicit, reversible enough to audit, and bounded by object meaning.

Tests should fail, hold, deny, or require review when:

- source unit is missing;
- target unit is missing;
- conversion method or factor is missing;
- pollutant or variable identity is missing;
- averaging period or time context is required but missing;
- normalized value overwrites the source value without trace;
- unit conversion changes object family, source role, or knowledge character;
- receipt expectations are missing where the normalization lane requires them;
- unit strings conflict with the schema or contract lane; or
- downstream outputs strip unit provenance or method context.

Tests may allow normalized values when source units, target units, method reference, object meaning, evidence hooks, validation state, and receipt expectations are all present and consistent.

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for Atmosphere unit-normalization tests.
- Unit conversion tests for known Atmosphere variables and pollutant-specific object families.
- Tests that verify original source units remain available after normalization.
- Tests that verify target units, conversion methods, and formula/factor references are present.
- Tests that verify PM2.5 and ozone units remain separate and pollutant-specific.
- Tests that verify AQI/report values are not treated as concentration by unit conversion alone.
- Tests that verify AOD, smoke, model, forecast, advisory, station, and observation roles remain separate through normalization.
- Tests that assert receipt references are emitted or preserved when required.
- Tests that call canonical validators or normalization helpers from their owning roots.
- Deterministic public-safe fixtures for valid and invalid unit cases.
- Tiny local test-only examples when they are not reusable fixtures and the reason is documented.

---

## 6. What does not belong here

This directory must not contain:

- Production normalization code.
- Unit registry definitions or canonical conversion tables.
- Source fetchers, live source pulls, tile requests, or downloaded source caches.
- Raw source payloads, processed datasets, catalog records, triplets, or published layers.
- Credentials, private endpoints, or developer-local cache material.
- Schema, contract, policy, source registry, receipt, proof, release, or rollback definitions.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Tests that run live network calls by default.

[↑ Back to top](#top)

---

## 7. Normalization proof matrix

| Scenario | Expected result | Rationale |
|---|---|---|
| Source unit missing | `DENY`, `HOLD`, `ERROR`, or validation failure | Cannot normalize without knowing the source unit. |
| Target unit missing | `DENY`, `HOLD`, `ERROR`, or validation failure | Normalized value has no declared interpretation. |
| Conversion factor/method missing | `DENY`, `HOLD`, `ERROR`, or validation failure | Conversion cannot be audited. |
| Original value overwritten without trace | Validation failure | Normalization must not be a silent edit. |
| Pollutant or variable identity missing | Validation failure | Units alone do not identify object meaning. |
| PM2.5 value normalized with ozone semantics | `DENY` or validation failure | Pollutant-specific object families remain separate. |
| AQI/report value treated as concentration through units only | `DENY` or `ABSTAIN` | Report/index posture remains distinct from concentration. |
| AOD or model context converted into observed concentration | `DENY` or `ABSTAIN` | Normalization cannot change knowledge character. |
| Low-cost sensor caveat removed during normalization | `DENY`, `HOLD`, or validation failure | Caveat and confidence context must travel. |
| Receipt reference missing where required | `HOLD`, `ERROR`, or validation failure | Transformation audit trail missing. |
| Valid source unit, target unit, method, context, and receipt reference | Allowed for the test scope | Normalization is explicit and inspectable. |

---

## 8. Fixture contract

Reusable fixtures should normally live under:

```text
fixtures/domains/atmosphere/
```

Expected fixture families include:

| Fixture kind | Example purpose |
|---|---|
| Valid PM2.5 unit normalization | Proves source and target concentration units are preserved with method context. |
| Valid ozone unit normalization | Proves ozone units are normalized without losing pollutant identity. |
| Valid weather variable normalization | Proves unit conversion works for temperature, precipitation, wind, or pressure when supported. |
| Invalid missing source unit | Proves unit ambiguity fails closed. |
| Invalid missing target unit | Proves target interpretation is required. |
| Invalid missing conversion method | Proves conversion audit trail is required. |
| Invalid AQI-as-concentration conversion | Proves unit conversion cannot create concentration semantics from report/index values. |
| Invalid model-as-observed conversion | Proves normalization cannot change knowledge character. |
| Invalid receipt-missing case | Proves receipt expectations are enforced when required. |

Fixture records should be deterministic, public-safe, no-network, and visibly test-only or governed fixture data. They must not be raw source payloads or release artifacts.

---

## 9. Expected outcomes

Unit-normalization tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

Pipeline or review paths may also use:

```text
ALLOW | RESTRICT | DENY | HOLD | ERROR | NEEDS_REVIEW | QUARANTINE
```

| Condition | Preferred outcome |
|---|---|
| Missing unit or method context | `DENY`, `HOLD`, `ERROR`, or validation failure. |
| Unsupported conversion | `ABSTAIN`, `DENY`, `HOLD`, or validation failure. |
| Conflicting unit metadata | `ERROR`, `HOLD`, or validation failure. |
| Object-family or knowledge-character change by unit conversion | `DENY` or validation failure. |
| Receipt expectation missing | `HOLD`, `ERROR`, or validation failure. |
| Valid governed normalization case | Allowed only for normalization scope; not publication approval. |

---

## 10. Lifecycle and authority boundaries

This lane supports validation across the KFM lifecycle but does not move records through it:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Boundary | Rule |
|---|---|
| RAW | Do not place raw source payloads in this directory. |
| WORK / QUARANTINE | Tests may reference work/quarantine behavior but do not store work records here. |
| PROCESSED | Do not store normalized processed products here. |
| CATALOG / TRIPLET | Do not treat test outputs as catalog or graph truth. |
| PUBLISHED | Tests never publish. |
| RECEIPTS / PROOFS | Tests may assert references, but trust-bearing records stay in their roots. |
| RELEASE | Release decisions remain under `release/`. |

A unit-normalization pass only means a checked normalization case behaved as expected. It is not evidence closure, policy approval, release approval, proof, or publication.

---

## 11. No-network default

Default unit-normalization tests must avoid:

- live source services,
- internet access,
- remote unit registries,
- live tile or geocode requests,
- local credential files,
- developer machine caches,
- mutable upstream API responses, and
- direct source-system side effects.

Live-source or external-registry checks, if ever needed, should be marked as integration/manual and excluded from default CI.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, validator names, marker names, and CI job names are **NEEDS VERIFICATION** until checked against the actual repository configuration.

Likely lane check:

```bash
pytest tests/domains/atmosphere/unit-normalization
```

Likely full Atmosphere test check:

```bash
pytest tests/domains/atmosphere
```

Possible validator check if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does the lane test behavior rather than define production conversion logic?
- Are original source units and normalized units both preserved or referenced?
- Is the conversion method, factor, formula, or method reference explicit?
- Are pollutant/variable identity and averaging-period context preserved where required?
- Does unit normalization avoid object-family, source-role, and knowledge-character collapse?
- Are TransformReceipt or equivalent receipt references handled without storing receipts here?
- Are fixtures local, deterministic, public-safe, and no-network?
- Are reusable fixtures kept under the fixture root rather than duplicated here?
- Are schemas, contracts, policy, receipts, proofs, releases, source registries, and production code kept in their canonical roots?
- Are validator and CI gaps marked NEEDS VERIFICATION instead of hidden?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `pipelines/domains/atmosphere/normalize/` | Normalization logic home. | CONFIRMED README exists; executable behavior NEEDS VERIFICATION. |
| `data/receipts/atmosphere/unit_conversion/` | Receipt lane for unit-conversion process memory. | CONFIRMED README exists; receipt payloads NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/AirObservation.md` | General air-quality observation contract. | CONFIRMED present. |
| `contracts/domains/atmosphere/PM25Observation.md` | PM2.5 observation contract with unit/source-role boundary. | CONFIRMED present. |
| `contracts/domains/atmosphere/OzoneObservation.md` | Ozone observation contract with unit/source-role boundary. | CONFIRMED present. |
| `schemas/contracts/v1/domains/atmosphere/` | Machine-readable schema home. | Inventory NEEDS VERIFICATION. |
| `fixtures/domains/atmosphere/` | Reusable fixture home. | Fixture inventory NEEDS VERIFICATION. |
| `tools/validators/` | Validator implementation home. | Specific validator module names NEEDS VERIFICATION. |
| `policy/domains/atmosphere/` | Policy implementation home. | Specific behavior NEEDS VERIFICATION. |
| `tests/domains/atmosphere/policy-deny/` | Negative policy lanes for object-family collapse. | Related, separate responsibility. |
| `tests/domains/atmosphere/schema/` | Schema conformance lanes. | Related, separate responsibility. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| What unit registry or conversion table is canonical? | NEEDS VERIFICATION | Do not invent unit authority in tests. |
| Which conversions are in scope for Atmosphere v0.1? | NEEDS VERIFICATION | Likely pollutant, weather, wind, precipitation, and model/context variables. |
| Which fields are mandatory for conversion auditability? | NEEDS VERIFICATION | Candidate fields: source unit, target unit, method, factor/formula ref, value refs, receipt ref. |
| Where exactly do unit-normalization fixtures live? | NEEDS VERIFICATION | Prefer `fixtures/domains/atmosphere/`. |
| Which receipt schema or payload shape is canonical? | NEEDS VERIFICATION | Receipt README is documentation; payload implementation not verified. |
| Which validator command is canonical? | NEEDS VERIFICATION | Must be checked against actual validator modules. |
| Which CI job proves this lane? | NEEDS VERIFICATION | Must be checked against `.github/workflows/`. |

---

## 16. Definition of done

This lane is mature when:

- [ ] Unit-normalization tests run locally.
- [ ] Source units, target units, conversion method, and parameter identity are tested.
- [ ] Valid normalization fixtures pass and invalid fixtures fail deterministically.
- [ ] Original source values and normalized values remain auditable.
- [ ] Receipt references are emitted or preserved where required.
- [ ] Object-family, source-role, knowledge-character, and policy boundaries are preserved.
- [ ] Tests call canonical validators or normalization helpers rather than redefining conversion behavior locally.
- [ ] Tests run no-network by default.
- [ ] CI exposes the unit-normalization proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere unit-normalization test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, Atmosphere normalization README, unit-conversion receipt README, and pollutant-specific contract references; executable tests, fixtures, validators, conversion tables, receipt payloads, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
