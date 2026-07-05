<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/schema/air-observation/readme
title: Atmosphere Schema Test Lane — AirObservation README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Atmosphere steward>
  - <PLACEHOLDER — Schema steward>
  - <PLACEHOLDER — Contract steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Evidence/governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; paired schema is PROPOSED scaffold; executable tests not verified
related:
  - tests/README.md
  - tests/domains/atmosphere/README.md
  - tests/domains/atmosphere/schema/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - contracts/domains/atmosphere/AirObservation.md
  - schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json
  - schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json
  - schemas/contracts/v1/domains/atmosphere/OzoneObservation.schema.json
  - fixtures/domains/atmosphere/
  - tools/validators/
  - policy/domains/atmosphere/
tags:
  - kfm
  - tests
  - atmosphere
  - schema
  - air-observation
  - json-schema
  - contract-conformance
  - evidence
  - fail-closed
] -->

<a id="top"></a>

# Atmosphere Schema Tests — AirObservation

> Test-lane contract for proving `AirObservation` records conform to the governed Atmosphere schema and preserve the semantic boundary defined by the `AirObservation` contract.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere%2Fschema-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere%2Fschema-informational)
![object: AirObservation](https://img.shields.io/badge/object-AirObservation-blue)
![schema: proposed--scaffold](https://img.shields.io/badge/schema-proposed--scaffold-yellow)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)

**Status:** `draft`  
**Authority:** schema-test lane README; not a schema, contract, validator, policy, fixture inventory, release decision, receipt, or proof  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `schema/air-observation/`  
**Schema under test:** `schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json`  
**Contract reference:** `contracts/domains/atmosphere/AirObservation.md`  
**Last reviewed:** 2026-07-05

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [Schema under test](#4-schema-under-test)
5. [Contract boundary](#5-contract-boundary)
6. [What belongs here](#6-what-belongs-here)
7. [What does not belong here](#7-what-does-not-belong-here)
8. [Schema proof matrix](#8-schema-proof-matrix)
9. [Fixture contract](#9-fixture-contract)
10. [Expected validator behavior](#10-expected-validator-behavior)
11. [Lifecycle and publication boundaries](#11-lifecycle-and-publication-boundaries)
12. [Suggested local commands](#12-suggested-local-commands)
13. [Review burden](#13-review-burden)
14. [Related folders and files](#14-related-folders-and-files)
15. [Open questions](#15-open-questions)
16. [Definition of done](#16-definition-of-done)
17. [Changelog](#17-changelog)
18. [Last reviewed](#18-last-reviewed)

---

## 1. Purpose

This directory is the Atmosphere / Air test sublane for **AirObservation schema conformance**.

Its job is to prove that candidate `AirObservation` records are checked against the governed JSON Schema and do not quietly bypass the semantic boundary of the `AirObservation` contract.

A mature test lane should support these claims:

1. **Shape conformance is explicit.** Candidate records are validated against the canonical `AirObservation` schema path.
2. **Contract meaning is preserved.** The schema tests do not let a general air-quality observation become a PM2.5 observation, ozone observation, AQI report, model field, AOD raster, advisory, evidence bundle, policy decision, or release manifest by field naming alone.
3. **Schema maturity is visible.** The paired schema is currently a PROPOSED scaffold; tests must not pretend field-level requirements are final until the schema is expanded.
4. **Fixtures are governed.** Valid and invalid records are deterministic, public-safe, no-network, and tied to the fixture lane unless deliberately test-local.
5. **Validation failure is finite.** Invalid candidate records should fail with explicit schema or contract-alignment errors, not silent acceptance.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/schema/air-observation/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove schema conformance behavior for an Atmosphere object family. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Parent lane | `schema/` |
| Sublane | `air-observation/` |
| Schema home | `schemas/contracts/v1/domains/atmosphere/` |
| Contract home | `contracts/domains/atmosphere/` |
| Validator home | `tools/validators/` |
| Fixture home | `fixtures/domains/atmosphere/` unless tiny local test-only samples are documented. |
| Policy home | `policy/domains/atmosphere/` |
| Release home | `release/` |
| Receipts/proofs home | `data/receipts/` and `data/proofs/` |

> [!WARNING]
> This directory must not become a second schema home. It tests the canonical schema; it does not define the schema.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows schema tests under `tests/` | CONFIRMED from current repo docs. |
| Atmosphere file-system plan names `air-observation.schema.json` | CONFIRMED from current repo docs. |
| `contracts/domains/atmosphere/AirObservation.md` exists | CONFIRMED from current repo evidence. |
| `schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json` exists | CONFIRMED from current repo evidence. |
| Paired schema maturity | CONFIRMED as `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual fixture inventory for AirObservation | NEEDS VERIFICATION. |
| Canonical validator command/module | NEEDS VERIFICATION. |
| CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the schema-test lane contract. It does not claim that final AirObservation fields, validators, fixtures, or CI gates are implemented.

---

## 4. Schema under test

The schema under test is:

```text
schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json
```

Current-session evidence shows this schema is a proposed scaffold with:

| Schema element | Current evidence |
|---|---|
| Draft | JSON Schema draft 2020-12. |
| `$id` | `https://schemas.kfm.local/schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json`. |
| `title` | `Airobservation` in current scaffold. |
| `type` | `object`. |
| `description` | PROPOSED scaffold. |
| `x-kfm.status` | `PROPOSED`. |
| `x-kfm.contract_doc` | `contracts/domains/atmosphere/AirObservation.md`. |
| `properties` | Empty in current scaffold. |
| `additionalProperties` | `true` in current scaffold. |

> [!CAUTION]
> Until the schema defines required fields and properties, tests should focus on path resolution, schema metadata, validator wiring, scaffold posture, and contract-alignment TODOs rather than claiming strict field-level enforcement exists.

---

## 5. Contract boundary

The `AirObservation` contract defines object meaning. It states that `AirObservation` is a governed general air-quality observation normally tied to station/network context and carrying an observed-sensor posture unless admitted under a more specific or caveated source role.

The contract also says `AirObservation` is not, by itself:

- a dedicated PM2.5 observation,
- a dedicated ozone observation,
- an AQI report,
- a regulatory archive measurement by default,
- an uncaveated low-cost sensor record when caveats are required,
- a model field,
- an AOD raster or smoke mask,
- an advisory or health/safety instruction,
- an EvidenceBundle,
- a PolicyDecision,
- a ReleaseManifest, or
- permission to disclose stale, rights-unclear, source-role-unclear, station-location-sensitive, or unsupported claims.

Schema tests should preserve those boundaries by checking that schema shape and metadata do not encourage object-family collapse.

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for `AirObservation` schema tests.
- Tests that resolve the canonical schema path and verify it is valid JSON Schema.
- Tests that verify schema metadata such as `$schema`, `$id`, `title`, `type`, and `x-kfm` fields.
- Tests that check valid fixture records pass the schema when fixtures exist.
- Tests that check invalid fixture records fail the schema when field requirements are defined.
- Tests that assert scaffold maturity is visible and not mistaken for final enforcement.
- Tests that compare schema posture against the AirObservation semantic contract.
- Tests that call shared schema validators from `tools/validators/` or another canonical validator home.
- Tiny local test-only fixture records when reusable fixtures are not appropriate and the reason is documented.

---

## 7. What does not belong here

This directory must not contain:

- Schema definition files.
- Contract definition files.
- Production validators or transformation code.
- Source fetchers, scrapers, live AQI/observation pulls, live model pulls, or downloaded source caches.
- Raw source payloads, processed datasets, catalog records, triplets, or published layers.
- Real credentials, API keys, service accounts, cookies, signed URLs, private endpoints, or device-owner details.
- Policy definitions, source registry records, release decisions, receipts, or proofs.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Tests that run live network calls by default.

[↑ Back to top](#top)

---

## 8. Schema proof matrix

| Test concern | Required proof | Current maturity |
|---|---|---|
| Schema path resolution | Validator can locate `AirObservation.schema.json`. | NEEDS VERIFICATION. |
| JSON parse | Schema parses as JSON. | PROPOSED test. |
| JSON Schema dialect | `$schema` is draft 2020-12 or approved project dialect. | PROPOSED test. |
| Stable `$id` | `$id` matches canonical schema URL pattern. | PROPOSED test. |
| Object type | Schema declares an object shape. | PROPOSED test. |
| KFM metadata | `x-kfm.status` and `x-kfm.contract_doc` remain present. | PROPOSED test. |
| Scaffold visibility | Tests expose that schema is not final field enforcement yet. | PROPOSED test. |
| Contract link | Schema points back to `contracts/domains/atmosphere/AirObservation.md`. | PROPOSED test. |
| Valid fixture pass | Valid AirObservation fixture passes. | NEEDS FIXTURES. |
| Invalid fixture fail | Invalid AirObservation fixture fails once required fields exist. | NEEDS SCHEMA EXPANSION. |
| Object-family boundary | AirObservation does not pass as PM2.5, ozone, AQI, model, AOD, advisory, evidence, policy, or release object by label. | NEEDS CONTRACT / POLICY TESTS. |

---

## 9. Fixture contract

Reusable fixtures should normally live under:

```text
fixtures/domains/atmosphere/
```

Expected fixture families for this lane include:

| Fixture kind | Example purpose |
|---|---|
| Valid minimal AirObservation | Proves canonical required fields pass once schema is expanded. |
| Valid caveated low-cost AirObservation | Proves low-cost posture can pass when caveat requirements are represented. |
| Invalid missing source role | Proves source-role requirement fails when encoded. |
| Invalid missing knowledge character | Proves knowledge-character requirement fails when encoded. |
| Invalid AQI-as-AirObservation | Proves AQI/report object does not pass as general observation if policy/schema disallow it. |
| Invalid model-as-AirObservation | Proves model context does not pass as observed record. |
| Invalid release/evidence/policy object | Proves non-observation governed objects do not pass as AirObservation. |

Fixture records should be deterministic, public-safe, no-network, and visibly test-only or governed fixture data. They must not be raw source payloads or release artifacts.

---

## 10. Expected validator behavior

A mature validator should:

- load the schema from the canonical schema root;
- validate JSON Schema syntax before validating records;
- preserve clear error messages for missing required fields, invalid enum values, and object-family mismatch when those constraints exist;
- avoid live network schema fetching in the default suite;
- report schema maturity when a schema is still a scaffold;
- preserve `EvidenceRef`, source-role, knowledge-character, caveat, freshness, and policy hooks when fields are defined;
- fail test setup if the schema file is missing or malformed; and
- avoid treating successful schema validation as publication approval.

---

## 11. Lifecycle and publication boundaries

This lane supports validation across the KFM lifecycle but does not move records through it:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Boundary | Rule |
|---|---|
| RAW | Do not place raw source payloads in this directory. |
| WORK / QUARANTINE | Do not use this directory as scratch processing storage. |
| PROCESSED | Do not store processed Atmosphere products here. |
| CATALOG / TRIPLET | Do not treat schema-test outputs as catalog or graph truth. |
| PUBLISHED | Tests never publish. |
| RECEIPTS / PROOFS | Do not store trust-bearing receipts or proofs here. |
| RELEASE | Release decisions remain under `release/`. |

A schema pass only means a record matched the checked schema constraints. It is not evidence closure, policy approval, release approval, or publication.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, schema validator names, marker names, and CI job names are **NEEDS VERIFICATION** until checked against the actual repository configuration.

Likely lane check:

```bash
pytest tests/domains/atmosphere/schema/air-observation
```

Likely parent schema lane check:

```bash
pytest tests/domains/atmosphere/schema
```

Possible JSON Schema validation command if implemented:

```bash
python tools/validators/validate_schema.py schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does the test lane resolve the canonical AirObservation schema path?
- Does it distinguish schema syntax validity from field-level business completeness?
- Does it report the current schema scaffold posture honestly?
- Does it preserve the AirObservation contract boundary?
- Does it avoid redefining the schema in tests?
- Are fixtures local, deterministic, public-safe, and no-network?
- Are reusable fixtures kept under the fixture root rather than duplicated here?
- Are receipts, proofs, release decisions, source registries, contracts, schemas, and policy definitions kept in their canonical roots?
- Are validator and CI gaps marked NEEDS VERIFICATION instead of hidden?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/domains/atmosphere/schema/` | Parent Atmosphere schema-test lane. | NEEDS VERIFICATION beyond this README. |
| `schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json` | Canonical schema under test. | CONFIRMED present; PROPOSED scaffold. |
| `contracts/domains/atmosphere/AirObservation.md` | Semantic contract reference. | CONFIRMED present; draft contract. |
| `fixtures/domains/atmosphere/` | Reusable valid/invalid fixture home. | Fixture inventory NEEDS VERIFICATION. |
| `tools/validators/` | Validator implementation home. | Specific validator module names NEEDS VERIFICATION. |
| `policy/domains/atmosphere/` | Policy checks linked to schema-admitted objects. | Specific policy behavior NEEDS VERIFICATION. |
| `tests/domains/atmosphere/policy-deny/` | Negative policy tests for object-family collapse. | Related but separate responsibility. |
| `tests/domains/atmosphere/knowledge-character/` | Knowledge-character tests. | Related but separate responsibility. |
| `tests/domains/atmosphere/source-role/` | Source-role tests. | Related but separate responsibility. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| What fields are required for `AirObservation`? | NEEDS VERIFICATION | Paired schema currently has empty `properties`. |
| Should `title` be `AirObservation` rather than `Airobservation`? | NEEDS VERIFICATION | Current scaffold title casing may need correction in schema PR. |
| Should `additionalProperties` remain `true`? | NEEDS VERIFICATION | Current scaffold is permissive; strictness should be governed by schema steward. |
| Which validator command is canonical? | NEEDS VERIFICATION | Do not invent validator behavior. |
| Where do valid/invalid AirObservation fixtures live exactly? | NEEDS VERIFICATION | Prefer `fixtures/domains/atmosphere/` with manifest/checksum discipline. |
| Which constraints belong in schema vs contract vs policy tests? | OPEN | Avoid overloading JSON Schema with policy behavior unless agreed. |
| Which CI job proves Atmosphere schema conformance? | NEEDS VERIFICATION | Must be checked against `.github/workflows/`. |

---

## 16. Definition of done

This lane is mature when:

- [ ] The canonical AirObservation schema path resolves in tests.
- [ ] The schema parses and validates as the approved JSON Schema dialect.
- [ ] Schema metadata and KFM metadata are tested.
- [ ] Required fields and enum constraints are tested after the schema is expanded.
- [ ] Valid fixtures pass and invalid fixtures fail deterministically.
- [ ] AirObservation contract boundaries are covered here or delegated to contract/policy lanes with links.
- [ ] Tests call canonical validators rather than redefining validation locally.
- [ ] Tests run no-network by default.
- [ ] CI exposes the schema conformance proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the AirObservation schema-test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the AirObservation contract and paired schema path; the schema is still a PROPOSED scaffold, and executable tests, fixture inventory, validator behavior, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
