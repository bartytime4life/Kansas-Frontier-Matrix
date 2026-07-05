<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/schema/readme
title: Atmosphere Schema Test Lane README
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
verification_status: current-session path verified; schema family listed in plan; executable tests and validator behavior not verified
related:
  - tests/README.md
  - tests/domains/atmosphere/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - docs/domains/atmosphere/CANONICAL_PATHS.md
  - docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - fixtures/domains/atmosphere/
  - tools/validators/
  - policy/domains/atmosphere/
  - release/
  - data/receipts/
  - data/proofs/
tags:
  - kfm
  - tests
  - atmosphere
  - schema
  - json-schema
  - contract-conformance
  - object-family
  - fixtures
  - no-network
  - fail-closed
] -->

<a id="top"></a>

# Atmosphere Schema Tests

> Parent test-lane contract for Atmosphere / Air schema conformance tests. This directory proves that Atmosphere candidate records resolve to canonical schemas, remain aligned with semantic contracts, and do not drift into policy, fixture, release, receipt, proof, source-registry, or production-validator authority.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere%2Fschema-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere%2Fschema-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![schema-family: atmosphere](https://img.shields.io/badge/schema--family-atmosphere-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** parent schema-test README; not a schema, contract, validator, policy, source registry, fixture inventory, release decision, receipt, or proof  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `schema/`  
**Canonical schema root:** `schemas/contracts/v1/domains/atmosphere/`  
**Last reviewed:** 2026-07-05

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [Schema family under test](#4-schema-family-under-test)
5. [Schema and contract boundary](#5-schema-and-contract-boundary)
6. [What belongs here](#6-what-belongs-here)
7. [What does not belong here](#7-what-does-not-belong-here)
8. [Parent schema proof matrix](#8-parent-schema-proof-matrix)
9. [Child lane map](#9-child-lane-map)
10. [Fixture contract](#10-fixture-contract)
11. [Expected validator behavior](#11-expected-validator-behavior)
12. [Lifecycle and publication boundaries](#12-lifecycle-and-publication-boundaries)
13. [No-network default](#13-no-network-default)
14. [Suggested local commands](#14-suggested-local-commands)
15. [Review burden](#15-review-burden)
16. [Related folders and files](#16-related-folders-and-files)
17. [Open questions](#17-open-questions)
18. [Definition of done](#18-definition-of-done)
19. [Changelog](#19-changelog)
20. [Last reviewed](#20-last-reviewed)

---

## 1. Purpose

This directory is the Atmosphere / Air parent lane for **schema conformance tests**.

Its job is to prove that Atmosphere records are checked against canonical schema files and that schema validation does not collapse object meaning, policy, release, evidence, or fixture responsibilities.

A mature parent schema lane should support these claims:

1. **Canonical schema paths resolve.** Every Atmosphere object-family schema is loaded from `schemas/contracts/v1/domains/atmosphere/`.
2. **Schemas are valid schemas.** Schema files parse as JSON and satisfy the approved JSON Schema dialect or project schema standard.
3. **KFM metadata is visible.** Schema metadata, including `x-kfm` fields where present, remains available for governance review.
4. **Contract alignment is testable.** Schema tests reference object-meaning contracts instead of inventing semantic meaning locally.
5. **Scaffold maturity is honest.** PROPOSED scaffolds are not treated as final field-level enforcement.
6. **Fixtures are controlled.** Valid and invalid records are deterministic, public-safe, no-network, and live in the governed fixture lane unless intentionally test-local.
7. **Validation is not publication.** Passing a schema test does not prove evidence closure, policy approval, release approval, receipt/proof validity, or public publication.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/schema/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove schema conformance behavior for Atmosphere governed object families. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Parent lane | `schema/` |
| Schema home | `schemas/contracts/v1/domains/atmosphere/` |
| Contract home | `contracts/domains/atmosphere/` |
| Validator home | `tools/validators/` |
| Fixture home | `fixtures/domains/atmosphere/` unless tiny local test-only samples are documented. |
| Policy home | `policy/domains/atmosphere/` |
| Release home | `release/` |
| Receipts/proofs home | `data/receipts/` and `data/proofs/` |

> [!WARNING]
> This directory must not become a second schema, contract, policy, validator, fixture, source-registry, release, receipt, or proof home. It proves behavior against those authorities.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows schema tests under `tests/` | CONFIRMED from current repo docs. |
| Atmosphere file-system plan names `tests/domains/atmosphere/schema/` | CONFIRMED from current repo docs. |
| Atmosphere file-system plan lists the schema family under canonical schema root | CONFIRMED from current repo docs. |
| Child README branches for `air-observation/` and `air-station/` | Created in current session as open PRs; not assumed merged on `main`. |
| Actual executable tests in this directory | UNKNOWN in this README. |
| Actual fixture inventory for all Atmosphere schemas | NEEDS VERIFICATION. |
| Canonical schema validator command/module | NEEDS VERIFICATION. |
| CI job names / pytest markers | NEEDS VERIFICATION. |
| Runtime/API/UI behavior | NEEDS VERIFICATION unless proven by tests outside this README. |

This README defines the parent schema-test lane contract. It does not claim that final schemas, validators, fixtures, CI jobs, or runtime integrations are complete.

---

## 4. Schema family under test

The Atmosphere file-system plan lists the canonical schema family under:

```text
schemas/contracts/v1/domains/atmosphere/
```

Planned or expected schema files include:

| Schema file | Object / envelope family | Parent-lane posture |
|---|---|---|
| `air-station.schema.json` | `AirStation` / station-network site context | Schema path should resolve; field maturity NEEDS VERIFICATION. |
| `air-observation.schema.json` | `AirObservation` / general air-quality observation | Schema path should resolve; field maturity NEEDS VERIFICATION. |
| `pm25-observation.schema.json` | PM2.5 observation | Schema path and contract alignment NEEDS VERIFICATION. |
| `ozone-observation.schema.json` | Ozone observation | Schema path and contract alignment NEEDS VERIFICATION. |
| `smoke-context.schema.json` | Smoke context | Schema path and contract alignment NEEDS VERIFICATION. |
| `aod-raster.schema.json` | AOD raster / remote-sensing context | Schema path and contract alignment NEEDS VERIFICATION. |
| `weather-station.schema.json` | Weather station context | Schema path and contract alignment NEEDS VERIFICATION. |
| `weather-observation.schema.json` | Weather observation | Schema path and contract alignment NEEDS VERIFICATION. |
| `wind-field.schema.json` | Wind field | Schema path and contract alignment NEEDS VERIFICATION. |
| `precipitation-observation.schema.json` | Precipitation observation | Schema path and contract alignment NEEDS VERIFICATION. |
| `temperature-observation.schema.json` | Temperature observation | Schema path and contract alignment NEEDS VERIFICATION. |
| `climate-normal.schema.json` | Climate normal | Schema path and contract alignment NEEDS VERIFICATION. |
| `climate-anomaly.schema.json` | Climate anomaly | Schema path and contract alignment NEEDS VERIFICATION. |
| `forecast-context.schema.json` | Forecast/model context | Schema path and contract alignment NEEDS VERIFICATION. |
| `advisory-context.schema.json` | Advisory context | Schema path and contract alignment NEEDS VERIFICATION. |
| `atmosphere-decision-envelope.schema.json` | Atmosphere decision/runtime envelope | Schema path and envelope semantics NEEDS VERIFICATION. |

> [!NOTE]
> The file-system plan lists lowercase hyphenated schema filenames. Some current schema files may use PascalCase names or scaffold naming conventions. Treat filename normalization as **NEEDS VERIFICATION** until checked against the live schema tree and any ADRs.

---

## 5. Schema and contract boundary

Schema tests prove machine-shape behavior. They do not define object meaning by themselves.

Each schema lane should preserve this split:

| Concern | Canonical home | Test-lane role |
|---|---|---|
| Machine shape | `schemas/contracts/v1/domains/atmosphere/` | Load and validate against canonical schemas. |
| Object meaning | `contracts/domains/atmosphere/` | Reference contracts and ensure tests do not contradict them. |
| Policy admissibility | `policy/domains/atmosphere/` | Call or delegate to policy tests; do not redefine policy in schema tests. |
| Evidence support | EvidenceRef / EvidenceBundle homes and receipts/proofs roots | Verify references only when in scope; do not store proofs here. |
| Valid/invalid examples | `fixtures/domains/atmosphere/` | Consume deterministic fixtures; do not create a duplicate fixture warehouse. |
| Publication | `release/` and `data/published/` | Schema pass is not release approval. |
| Validator implementation | `tools/validators/` | Invoke canonical validators when available. |

A schema can reject bad shape. It cannot, alone, authorize a public claim, release, correction, rollback, evidence proof, or policy decision.

---

## 6. What belongs here

This directory may contain:

- README and parent-lane contract material for Atmosphere schema tests.
- Parent-level tests that discover and validate the Atmosphere schema family.
- Tests that assert schema files parse as JSON and conform to the approved JSON Schema dialect.
- Tests that assert required KFM metadata is present where required.
- Tests that verify schema-to-contract references resolve.
- Tests that expose PROPOSED scaffold posture instead of masking it.
- Tests that check valid and invalid Atmosphere fixtures when fixtures exist.
- Tests that call shared schema validators from `tools/validators/` or another canonical validator home.
- Tiny local test-only fixture records when reusable fixtures are not appropriate and the reason is documented.

---

## 7. What does not belong here

This directory must not contain:

- Schema definition files.
- Contract definition files.
- Production validators, pipelines, connectors, adapters, or transformation code.
- Source fetchers, scrapers, live source pulls, live model pulls, live tile requests, geocode calls, or downloaded source caches.
- Raw source payloads, processed datasets, catalog records, triplets, or published layers.
- Exact sensitive station coordinates, private-land access detail, station-owner personal identifiers, credentials, API keys, service accounts, cookies, signed URLs, or private endpoints.
- Policy definitions, source registry records, release decisions, receipts, or proofs.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Tests that run live network calls by default.

[↑ Back to top](#top)

---

## 8. Parent schema proof matrix

| Test concern | Required proof | Current maturity |
|---|---|---|
| Parent lane discovery | `tests/domains/atmosphere/schema/` exists and is documented. | README CONFIRMED; executable tests UNKNOWN. |
| Canonical schema root | `schemas/contracts/v1/domains/atmosphere/` is the schema home. | CONFIRMED from plan; exact file inventory NEEDS VERIFICATION. |
| Schema parse | Each target schema parses as JSON. | PROPOSED test. |
| JSON Schema dialect | Each schema declares approved `$schema` dialect. | PROPOSED test. |
| Stable IDs | `$id` values match approved KFM schema URL/path pattern. | PROPOSED test. |
| Object type | Object-family schemas declare expected shape type. | PROPOSED test. |
| KFM metadata | Required `x-kfm` fields remain present where required. | PROPOSED test. |
| Contract links | Schemas link to matching contract docs. | PROPOSED test. |
| Scaffold visibility | PROPOSED schemas are identified as scaffolds. | PROPOSED test. |
| Valid fixtures pass | Valid domain fixtures pass their target schemas. | NEEDS FIXTURES. |
| Invalid fixtures fail | Invalid domain fixtures fail when required fields exist. | NEEDS SCHEMA EXPANSION. |
| Object-family boundaries | Schema tests do not collapse station, observation, forecast, AOD, advisory, evidence, policy, release, or envelope roles. | NEEDS CONTRACT / POLICY COORDINATION. |
| No-network validation | Schema tests do not fetch remote schemas or live source data by default. | PROPOSED test. |

---

## 9. Child lane map

Expected or active child lanes include:

| Child lane | Purpose | Status boundary |
|---|---|---|
| `air-station/` | AirStation schema conformance and station/network site-context boundary. | README work may exist in an open PR; implementation depth NEEDS VERIFICATION. |
| `air-observation/` | AirObservation schema conformance and general observation boundary. | README work may exist in an open PR; implementation depth NEEDS VERIFICATION. |
| `pm25-observation/` | PM2.5 observation schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `ozone-observation/` | Ozone observation schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `smoke-context/` | Smoke context schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `aod-raster/` | AOD raster schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `weather-station/` | Weather station schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `weather-observation/` | Weather observation schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `wind-field/` | Wind field schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `precipitation-observation/` | Precipitation observation schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `temperature-observation/` | Temperature observation schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `climate-normal/` | Climate normal schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `climate-anomaly/` | Climate anomaly schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `forecast-context/` | Forecast/model context schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `advisory-context/` | Advisory context schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |
| `atmosphere-decision-envelope/` | Atmosphere decision/envelope schema conformance. | PROPOSED / NEEDS VERIFICATION unless implemented. |

Child README files document sublane intent. They do not prove tests exist unless actual test files and CI/runtime evidence are verified.

---

## 10. Fixture contract

Reusable schema fixtures should normally live under:

```text
fixtures/domains/atmosphere/
```

Expected fixture families include:

| Fixture family | Example use |
|---|---|
| `valid/air-station/` | Valid station/network site-context records. |
| `invalid/air-station/` | Station records missing required identity, source, sensitivity, or lineage fields after schema expansion. |
| `valid/air-observation/` | Valid general air-quality observations. |
| `invalid/air-observation/` | Invalid observations missing required source role, knowledge character, units, observed time, or evidence hooks after schema expansion. |
| `valid/pm25-observation/` | Valid PM2.5 observation records. |
| `invalid/aqi-as-concentration/` | AQI/report records that must not pass as concentration observations. |
| `invalid/aod-as-pm25/` | AOD/raster records that must not pass as PM2.5 observations. |
| `invalid/model-as-observed/` | Forecast/model records that must not pass as observed sensor measurements. |
| `invalid/release-or-proof-as-observation/` | Non-observation governed objects that must not pass as observations. |

Fixture records should be deterministic, public-safe, no-network, and visibly test-only or governed fixture data. They must not be raw source payloads, exact sensitive station coordinates, private owner/access records, or release artifacts.

---

## 11. Expected validator behavior

A mature schema validator should:

- load schemas from the canonical schema root;
- validate JSON Schema syntax before validating records;
- avoid live network schema fetching in the default suite;
- resolve schema-to-contract links where required;
- preserve clear error messages for missing required fields, invalid enum values, malformed evidence references, and object-family mismatch when those constraints exist;
- report schema maturity when a schema is still a scaffold;
- preserve source role, knowledge character, caveat, freshness, sensitivity, rights, evidence, review, and release hooks when fields are defined;
- fail test setup if a required schema file is missing or malformed; and
- avoid treating successful schema validation as evidence closure, policy approval, release approval, or publication.

---

## 12. Lifecycle and publication boundaries

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

A schema pass only means a record matched the checked schema constraints. It is not contract approval, evidence closure, policy approval, release approval, correction approval, rollback proof, or publication.

---

## 13. No-network default

Default Atmosphere schema tests must avoid:

- live source services,
- internet access,
- remote JSON Schema fetching,
- live tile or geocode requests,
- local credential files,
- developer machine caches,
- private endpoints,
- mutable upstream API responses, and
- direct source-system side effects.

Remote-schema, live-source, or integration checks, if ever needed, should be explicitly marked and excluded from default CI.

---

## 14. Suggested local commands

> [!NOTE]
> Command names, schema validator names, marker names, and CI job names are **NEEDS VERIFICATION** until checked against the actual repository configuration.

Likely parent lane check:

```bash
pytest tests/domains/atmosphere/schema
```

Likely full Atmosphere domain check:

```bash
pytest tests/domains/atmosphere
```

Possible schema validation command if implemented:

```bash
python tools/validators/validate_schema.py schemas/contracts/v1/domains/atmosphere
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 15. Review burden

Reviewers should be able to answer:

- Does this lane test schema conformance rather than define schemas?
- Do tests resolve canonical schema paths under `schemas/contracts/v1/domains/atmosphere/`?
- Does the lane distinguish schema syntax validity from final field-level business completeness?
- Are PROPOSED scaffold schemas reported honestly?
- Do schema tests reference contracts without rewriting object meaning locally?
- Are fixtures local, deterministic, public-safe, and no-network?
- Are reusable fixtures kept under the fixture root rather than duplicated here?
- Are sensitive station/site details, credentials, source data, receipts, proofs, release decisions, source registries, contracts, schemas, and policy definitions kept in their canonical roots?
- Are validator and CI gaps marked NEEDS VERIFICATION instead of hidden?

---

## 16. Related folders and files

| Path | Relationship |
|---|---|
| `tests/domains/atmosphere/` | Parent Atmosphere test lane. |
| `tests/domains/atmosphere/schema/air-station/` | AirStation schema-test sublane. |
| `tests/domains/atmosphere/schema/air-observation/` | AirObservation schema-test sublane. |
| `tests/domains/atmosphere/policy-deny/` | Negative policy tests for object-family and release-boundary collapse. |
| `tests/domains/atmosphere/knowledge-character/` | Knowledge-character tests. |
| `tests/domains/atmosphere/source-role/` | Source-role tests. |
| `schemas/contracts/v1/domains/atmosphere/` | Canonical Atmosphere schema home. |
| `contracts/domains/atmosphere/` | Semantic contract home. |
| `fixtures/domains/atmosphere/` | Reusable valid/invalid fixture home. |
| `tools/validators/` | Validator implementation home. |
| `policy/domains/atmosphere/` | Policy implementation home. |
| `release/` | Release decisions and candidates. |
| `data/receipts/` | Trust-bearing receipts. |
| `data/proofs/` | Proof artifacts. |

---

## 17. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the exact live schema file inventory under `schemas/contracts/v1/domains/atmosphere/`? | NEEDS VERIFICATION | The file-system plan lists expected lowercase hyphenated names; live files may differ. |
| Which schemas are final enough for required-field tests? | NEEDS VERIFICATION | Some paired schemas are known scaffolds. |
| Which validator command is canonical? | NEEDS VERIFICATION | Do not invent validator behavior. |
| Which schema metadata fields are mandatory for all Atmosphere schemas? | NEEDS VERIFICATION | Candidate: `$schema`, `$id`, `title`, `type`, `x-kfm.status`, `x-kfm.contract_doc`. |
| Where do valid/invalid fixtures live exactly? | NEEDS VERIFICATION | Prefer `fixtures/domains/atmosphere/` with manifest/checksum discipline. |
| Which constraints belong in schema vs contract vs policy tests? | OPEN | Avoid overloading JSON Schema with policy behavior unless agreed. |
| Which CI job proves Atmosphere schema conformance? | NEEDS VERIFICATION | Must be checked against `.github/workflows/`. |
| Should parent discovery tolerate PROPOSED scaffolds or fail until expanded? | OPEN | Depends on current build phase and release gate expectations. |

---

## 18. Definition of done

This lane is mature when:

- [ ] The parent schema lane runs locally.
- [ ] The canonical Atmosphere schema root is discovered without live network access.
- [ ] Each schema parses and validates as the approved JSON Schema dialect.
- [ ] Schema metadata and KFM metadata are tested.
- [ ] Schema-to-contract links resolve for every governed object family.
- [ ] Required fields and enum constraints are tested after schemas are expanded.
- [ ] Valid fixtures pass and invalid fixtures fail deterministically.
- [ ] Object-family boundaries are covered here or delegated to contract/policy lanes with links.
- [ ] Tests call canonical validators rather than redefining validation locally.
- [ ] Tests run no-network by default.
- [ ] CI exposes the schema conformance proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 19. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere parent schema-test lane. |

---

## 20. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the tests root, Directory Rules domain-segment rule, and Atmosphere schema-family plan; executable tests, live schema inventory, fixture inventory, validator behavior, policy behavior, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
