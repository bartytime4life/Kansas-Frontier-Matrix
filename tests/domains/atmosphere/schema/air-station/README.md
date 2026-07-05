<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/schema/air-station/readme
title: Atmosphere Schema Test Lane — AirStation README
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
  - docs/domains/atmosphere/SENSITIVITY.md
  - contracts/domains/atmosphere/AirStation.md
  - contracts/domains/atmosphere/AirObservation.md
  - schemas/contracts/v1/domains/atmosphere/AirStation.schema.json
  - schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json
  - fixtures/domains/atmosphere/
  - tools/validators/
  - policy/domains/atmosphere/
tags:
  - kfm
  - tests
  - atmosphere
  - schema
  - air-station
  - json-schema
  - contract-conformance
  - network-and-site-context
  - evidence
  - fail-closed
] -->

<a id="top"></a>

# Atmosphere Schema Tests — AirStation

> Test-lane contract for proving `AirStation` records conform to the governed Atmosphere schema and preserve the station/network site-context boundary defined by the `AirStation` contract.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere%2Fschema-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere%2Fschema-informational)
![object: AirStation](https://img.shields.io/badge/object-AirStation-blue)
![schema: proposed--scaffold](https://img.shields.io/badge/schema-proposed--scaffold-yellow)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)

**Status:** `draft`  
**Authority:** schema-test lane README; not a schema, contract, validator, policy, fixture inventory, release decision, receipt, or proof  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `schema/air-station/`  
**Schema under test:** `schemas/contracts/v1/domains/atmosphere/AirStation.schema.json`  
**Contract reference:** `contracts/domains/atmosphere/AirStation.md`  
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

This directory is the Atmosphere / Air test sublane for **AirStation schema conformance**.

Its job is to prove that candidate `AirStation` records are checked against the governed JSON Schema and do not quietly bypass the semantic boundary of the `AirStation` contract.

A mature test lane should support these claims:

1. **Shape conformance is explicit.** Candidate records are validated against the canonical `AirStation` schema path.
2. **Contract meaning is preserved.** The schema tests do not let a station/network context become an air-quality observation, PM2.5 measurement, ozone measurement, AQI report, low-cost sensor reading, forecast/model field, AOD/smoke proxy, advisory, evidence bundle, policy decision, release manifest, or public-release approval by field naming alone.
3. **Sensitivity posture remains visible.** Station/site context can expose siting, ownership, private-land, or infrastructure-adjacent details; tests should preserve policy hooks rather than normalize exact public disclosure.
4. **Schema maturity is visible.** The paired schema is currently a PROPOSED scaffold; tests must not pretend field-level requirements are final until the schema is expanded.
5. **Fixtures are governed.** Valid and invalid records are deterministic, public-safe, no-network, and tied to the fixture lane unless deliberately test-local.
6. **Validation failure is finite.** Invalid candidate records should fail with explicit schema or contract-alignment errors, not silent acceptance.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/schema/air-station/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove schema conformance behavior for an Atmosphere object family. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Parent lane | `schema/` |
| Sublane | `air-station/` |
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
| Atmosphere file-system plan names `air-station.schema.json` | CONFIRMED from current repo docs. |
| `contracts/domains/atmosphere/AirStation.md` exists | CONFIRMED from current repo evidence. |
| `schemas/contracts/v1/domains/atmosphere/AirStation.schema.json` exists | CONFIRMED from current repo evidence. |
| Paired schema maturity | CONFIRMED as `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`. |
| Contract says AirStation is `NETWORK_AND_SITE_CONTEXT` | CONFIRMED from current repo evidence. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual fixture inventory for AirStation | NEEDS VERIFICATION. |
| Canonical validator command/module | NEEDS VERIFICATION. |
| CI job names / pytest markers | NEEDS VERIFICATION. |

This README defines the schema-test lane contract. It does not claim that final AirStation fields, validators, fixtures, policy gates, or CI gates are implemented.

---

## 4. Schema under test

The schema under test is:

```text
schemas/contracts/v1/domains/atmosphere/AirStation.schema.json
```

Current-session evidence shows this schema is a proposed scaffold with:

| Schema element | Current evidence |
|---|---|
| Draft | JSON Schema draft 2020-12. |
| `$id` | `https://schemas.kfm.local/schemas/contracts/v1/domains/atmosphere/AirStation.schema.json`. |
| `title` | `Airstation` in current scaffold. |
| `type` | `object`. |
| `description` | PROPOSED scaffold. |
| `x-kfm.status` | `PROPOSED`. |
| `x-kfm.contract_doc` | `contracts/domains/atmosphere/AirStation.md`. |
| `properties` | Empty in current scaffold. |
| `additionalProperties` | `true` in current scaffold. |

> [!CAUTION]
> Until the schema defines required fields and properties, tests should focus on path resolution, schema metadata, validator wiring, scaffold posture, and contract-alignment TODOs rather than claiming strict field-level enforcement exists.

---

## 5. Contract boundary

The `AirStation` contract defines object meaning. It states that `AirStation` is the Atmosphere/Air-domain object for a governed station, monitoring site, network site, sensor node, station-location context, or comparable air-quality station record. Its knowledge character is `NETWORK_AND_SITE_CONTEXT`: station and siting metadata used to interpret observations, not an air-quality value by itself.

The contract also says `AirStation` is not, by itself:

- an air-quality observation,
- a PM2.5 measurement,
- an ozone measurement,
- an AQI report,
- a low-cost-sensor reading,
- a forecast/model field,
- a smoke or AOD proxy,
- an advisory or health/safety instruction,
- proof that any attached observation is true,
- permission to publish exact coordinates, private-land context, infrastructure-sensitive siting, station ownership, or access details,
- an EvidenceBundle,
- a PolicyDecision,
- a ReleaseManifest, or
- public release approval.

Schema tests should preserve those boundaries by checking that schema shape and metadata do not encourage station/observation, station/value, station/evidence, station/policy, or station/release collapse.

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for `AirStation` schema tests.
- Tests that resolve the canonical schema path and verify it is valid JSON Schema.
- Tests that verify schema metadata such as `$schema`, `$id`, `title`, `type`, and `x-kfm` fields.
- Tests that check valid fixture records pass the schema when fixtures exist.
- Tests that check invalid fixture records fail the schema when field requirements are defined.
- Tests that assert scaffold maturity is visible and not mistaken for final enforcement.
- Tests that compare schema posture against the AirStation semantic contract.
- Tests that ensure station/siting sensitivity hooks are not dropped when fields exist.
- Tests that call shared schema validators from `tools/validators/` or another canonical validator home.
- Tiny local test-only fixture records when reusable fixtures are not appropriate and the reason is documented.

---

## 7. What does not belong here

This directory must not contain:

- Schema definition files.
- Contract definition files.
- Production validators or transformation code.
- Source fetchers, scrapers, live station/network pulls, live observation pulls, geocoding requests, or downloaded source caches.
- Raw source payloads, processed datasets, catalog records, triplets, or published layers.
- Exact sensitive station coordinates, private-land access detail, station-owner personal identifiers, credentials, API keys, service accounts, cookies, signed URLs, or private endpoints.
- Policy definitions, source registry records, release decisions, receipts, or proofs.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Tests that run live network calls by default.

[↑ Back to top](#top)

---

## 8. Schema proof matrix

| Test concern | Required proof | Current maturity |
|---|---|---|
| Schema path resolution | Validator can locate `AirStation.schema.json`. | NEEDS VERIFICATION. |
| JSON parse | Schema parses as JSON. | PROPOSED test. |
| JSON Schema dialect | `$schema` is draft 2020-12 or approved project dialect. | PROPOSED test. |
| Stable `$id` | `$id` matches canonical schema URL pattern. | PROPOSED test. |
| Object type | Schema declares an object shape. | PROPOSED test. |
| KFM metadata | `x-kfm.status` and `x-kfm.contract_doc` remain present. | PROPOSED test. |
| Scaffold visibility | Tests expose that schema is not final field enforcement yet. | PROPOSED test. |
| Contract link | Schema points back to `contracts/domains/atmosphere/AirStation.md`. | PROPOSED test. |
| Valid fixture pass | Valid AirStation fixture passes. | NEEDS FIXTURES. |
| Invalid fixture fail | Invalid AirStation fixture fails once required fields exist. | NEEDS SCHEMA EXPANSION. |
| Object-family boundary | AirStation does not pass as observation, value, AQI, model, AOD/smoke proxy, advisory, evidence, policy, or release object by label. | NEEDS CONTRACT / POLICY TESTS. |
| Siting sensitivity boundary | Exact public disclosure is not normalized by schema/test fixtures without policy hooks. | NEEDS SCHEMA EXPANSION / POLICY TESTS. |

---

## 9. Fixture contract

Reusable fixtures should normally live under:

```text
fixtures/domains/atmosphere/
```

Expected fixture families for this lane include:

| Fixture kind | Example purpose |
|---|---|
| Valid minimal AirStation | Proves canonical required fields pass once schema is expanded. |
| Valid generalized public AirStation | Proves public-safe station context can be represented when fields exist. |
| Valid private/restricted AirStation | Proves restricted station/site context can carry policy hooks when fields exist. |
| Invalid missing station identity | Proves station identity requirement fails when encoded. |
| Invalid missing network/source role | Proves source/network lineage requirement fails when encoded. |
| Invalid exact-public-siting fixture | Proves public release posture must not expose sensitive siting without transform/review. |
| Invalid observation-as-station | Proves air-quality values do not pass as station/site context. |
| Invalid release/evidence/policy object | Proves non-station governed objects do not pass as AirStation. |

Fixture records should be deterministic, public-safe, no-network, and visibly test-only or governed fixture data. They must not be raw source payloads, exact sensitive station coordinates, private owner/access records, or release artifacts.

---

## 10. Expected validator behavior

A mature validator should:

- load the schema from the canonical schema root;
- validate JSON Schema syntax before validating records;
- preserve clear error messages for missing required fields, invalid enum values, and object-family mismatch when those constraints exist;
- avoid live network schema fetching in the default suite;
- report schema maturity when a schema is still a scaffold;
- preserve station identity, network/source lineage, siting class, sensitivity, rights, evidence, review, and release hooks when fields are defined;
- fail test setup if the schema file is missing or malformed; and
- avoid treating successful schema validation as exact-coordinate release approval, observation truth, evidence closure, policy approval, or publication.

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
| PUBLISHED | Tests never publish station/site details. |
| RECEIPTS / PROOFS | Do not store trust-bearing receipts or proofs here. |
| RELEASE | Release decisions remain under `release/`. |

A schema pass only means a record matched the checked schema constraints. It is not evidence closure, policy approval, release approval, exact-coordinate disclosure approval, or publication.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, schema validator names, marker names, and CI job names are **NEEDS VERIFICATION** until checked against the actual repository configuration.

Likely lane check:

```bash
pytest tests/domains/atmosphere/schema/air-station
```

Likely parent schema lane check:

```bash
pytest tests/domains/atmosphere/schema
```

Possible JSON Schema validation command if implemented:

```bash
python tools/validators/validate_schema.py schemas/contracts/v1/domains/atmosphere/AirStation.schema.json
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does the test lane resolve the canonical AirStation schema path?
- Does it distinguish schema syntax validity from field-level business completeness?
- Does it report the current schema scaffold posture honestly?
- Does it preserve the AirStation contract boundary?
- Does it avoid redefining the schema in tests?
- Are station/site sensitivity and exact-coordinate/public-release boundaries acknowledged?
- Are fixtures local, deterministic, public-safe, and no-network?
- Are reusable fixtures kept under the fixture root rather than duplicated here?
- Are receipts, proofs, release decisions, source registries, contracts, schemas, and policy definitions kept in their canonical roots?
- Are validator and CI gaps marked NEEDS VERIFICATION instead of hidden?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/domains/atmosphere/schema/` | Parent Atmosphere schema-test lane. | NEEDS VERIFICATION beyond this README. |
| `schemas/contracts/v1/domains/atmosphere/AirStation.schema.json` | Canonical schema under test. | CONFIRMED present; PROPOSED scaffold. |
| `contracts/domains/atmosphere/AirStation.md` | Semantic contract reference. | CONFIRMED present; draft contract. |
| `contracts/domains/atmosphere/AirObservation.md` | Adjacent observation contract that attaches to station context. | CONFIRMED present in contract related paths. |
| `fixtures/domains/atmosphere/` | Reusable valid/invalid fixture home. | Fixture inventory NEEDS VERIFICATION. |
| `tools/validators/` | Validator implementation home. | Specific validator module names NEEDS VERIFICATION. |
| `policy/domains/atmosphere/` | Policy checks linked to schema-admitted station/site objects. | Specific policy behavior NEEDS VERIFICATION. |
| `tests/domains/atmosphere/policy-deny/` | Negative policy tests for object-family and release-boundary collapse. | Related but separate responsibility. |
| `tests/domains/atmosphere/knowledge-character/` | Knowledge-character tests, including `NETWORK_AND_SITE_CONTEXT`. | Related but separate responsibility. |
| `tests/domains/atmosphere/source-role/` | Source-role tests. | Related but separate responsibility. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| What fields are required for `AirStation`? | NEEDS VERIFICATION | Paired schema currently has empty `properties`. |
| Should `title` be `AirStation` rather than `Airstation`? | NEEDS VERIFICATION | Current scaffold title casing may need correction in schema PR. |
| Should `additionalProperties` remain `true`? | NEEDS VERIFICATION | Current scaffold is permissive; strictness should be governed by schema steward. |
| Which validator command is canonical? | NEEDS VERIFICATION | Do not invent validator behavior. |
| Where do valid/invalid AirStation fixtures live exactly? | NEEDS VERIFICATION | Prefer `fixtures/domains/atmosphere/` with manifest/checksum discipline. |
| Which station/site fields are public, generalized, restricted, or private? | NEEDS VERIFICATION | Should align with Atmosphere sensitivity/release policy. |
| Which constraints belong in schema vs contract vs policy tests? | OPEN | Avoid overloading JSON Schema with policy behavior unless agreed. |
| Which CI job proves Atmosphere schema conformance? | NEEDS VERIFICATION | Must be checked against `.github/workflows/`. |

---

## 16. Definition of done

This lane is mature when:

- [ ] The canonical AirStation schema path resolves in tests.
- [ ] The schema parses and validates as the approved JSON Schema dialect.
- [ ] Schema metadata and KFM metadata are tested.
- [ ] Required fields and enum constraints are tested after the schema is expanded.
- [ ] Valid fixtures pass and invalid fixtures fail deterministically.
- [ ] AirStation contract boundaries are covered here or delegated to contract/policy lanes with links.
- [ ] Station/site sensitivity and public-release posture are covered here or delegated to policy/release tests with links.
- [ ] Tests call canonical validators rather than redefining validation locally.
- [ ] Tests run no-network by default.
- [ ] CI exposes the schema conformance proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the AirStation schema-test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the AirStation contract and paired schema path; the schema is still a PROPOSED scaffold, and executable tests, fixture inventory, validator behavior, policy behavior, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
