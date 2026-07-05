<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/policy-deny/aqi-vs-concentration/readme
title: Atmosphere Policy-Deny Test Lane — AQI vs Concentration README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Atmosphere steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Evidence/governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; policy implementation, fixtures, and test runner not verified
related:
  - tests/README.md
  - tests/domains/atmosphere/README.md
  - tests/domains/atmosphere/policy-deny/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - docs/domains/atmosphere/POLICY.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md
  - policy/domains/atmosphere/aqi_is_not_concentration.rego
  - contracts/domains/atmosphere/pm25-observation.md
  - contracts/domains/atmosphere/ozone-observation.md
  - docs/sources/catalog/epa/airnow-api.md
  - fixtures/domains/atmosphere/
  - tools/validators/
tags:
  - kfm
  - tests
  - atmosphere
  - policy-deny
  - aqi
  - concentration
  - anti-collapse
  - public-aqi-report
  - evidence
  - fail-closed
] -->

<a id="top"></a>

# Atmosphere Policy-Deny Tests — AQI vs Concentration

> Test-lane contract for proving KFM denies attempts to treat **Air Quality Index (AQI)** reports, categories, colors, or index values as **pollutant concentration observations** without an explicit, governed source object, concentration units, pollutant identity, evidence trail, caveats, and separate object meaning.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational)
![rule: AQI%E2%89%A0concentration](https://img.shields.io/badge/rule-AQI%E2%89%A0concentration-red)
![policy: fail--closed](https://img.shields.io/badge/policy-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)
![sensitivity: public--safe](https://img.shields.io/badge/sensitivity-public--safe-green)

**Status:** `draft`  
**Authority:** test-lane README; not a schema, policy implementation, validator, source registry, release decision, receipt, proof, or fixture inventory  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `policy-deny/aqi-vs-concentration/`  
**Default posture:** deny by default; cite-or-abstain; preserve AQI/report/concentration separation  
**Last reviewed:** 2026-07-05

> [!IMPORTANT]
> KFM Atmosphere is **not** an emergency alerting or life-safety system. AQI policy-deny tests may verify air-quality reporting boundaries, but they must not issue health instructions or imply that KFM is the official authority for protective action.

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Rule statement](#3-rule-statement)
4. [Status and evidence boundary](#4-status-and-evidence-boundary)
5. [What belongs here](#5-what-belongs-here)
6. [What does not belong here](#6-what-does-not-belong-here)
7. [Policy-deny proof matrix](#7-policy-deny-proof-matrix)
8. [Allowed concentration boundary](#8-allowed-concentration-boundary)
9. [Fixture contract](#9-fixture-contract)
10. [Expected outcomes](#10-expected-outcomes)
11. [Lifecycle and publication gates](#11-lifecycle-and-publication-gates)
12. [Suggested local commands](#12-suggested-local-commands)
13. [Review burden](#13-review-burden)
14. [Related folders and files](#14-related-folders-and-files)
15. [Open questions](#15-open-questions)
16. [Definition of done](#16-definition-of-done)
17. [Changelog](#17-changelog)
18. [Last reviewed](#18-last-reviewed)

---

## 1. Purpose

This directory is the Atmosphere / Air test sublane for the **AQI vs concentration policy-deny rule**.

It exists to prove that KFM does not collapse two different atmospheric knowledge objects:

- **Public AQI report** — an agency-published index, category, color, forecast/reporting product, or public communication summary.
- **Pollutant concentration observation** — an observed, archived, modeled, or derived pollutant concentration object with pollutant identity, units, method, evidence, source role, and admissibility controls.

The lane should verify that AQI values, categories, color bands, textual descriptors, or public reports are denied when they are mislabeled, surfaced, cataloged, mapped, summarized, or published as concentrations such as PM2.5, ozone, or other pollutant readings without the required governed object meaning and evidence.

A passing suite should support these claims:

1. **AQI is not concentration by label change.** Renaming an AQI value, category, color, legend, tooltip, or field does not make it a pollutant concentration.
2. **Concentration claims require concentration objects.** A concentration record must carry pollutant identity, units, source/evidence, method, time, location/context, caveats, and review state as required by the governing contract/policy.
3. **AQI context can be surfaced only as AQI context.** Public AQI reports may appear as public index/report context, not as observed sensor concentration unless supported by a separate governed concentration object.
4. **Public UI and AI surfaces must not overclaim.** Generated text, map labels, tooltips, layer names, and summaries must not translate AQI into concentration without evidence.
5. **Catalog and release gates fail closed.** Mischaracterized AQI-as-concentration candidates should produce `DENY`, `ABSTAIN`, or validation failure, not quiet promotion.
6. **Fixtures are public-safe and deterministic.** Tests use local valid/invalid samples and do not fetch live AQI, sensor, regulatory, or model services by default.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/policy-deny/aqi-vs-concentration/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove a specific Atmosphere policy denial. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Parent lane | `policy-deny/` |
| Sublane | `aqi-vs-concentration/` |
| Policy home | `policy/domains/atmosphere/` |
| Validator home | `tools/validators/` |
| Object meaning home | `contracts/domains/atmosphere/` |
| Machine shape home | `schemas/contracts/v1/domains/atmosphere/` when schemas exist. |
| Fixture home | `fixtures/domains/atmosphere/` unless tiny local test-only samples are documented. |
| Release home | `release/` |
| Receipts/proofs home | `data/receipts/` and `data/proofs/` |

> [!WARNING]
> This directory must not become a second policy home. It tests policy behavior; policy definitions stay under `policy/domains/atmosphere/`.

[↑ Back to top](#top)

---

## 3. Rule statement

**Rule:** AQI must not be treated as pollutant concentration unless a separate, governed concentration object exists and passes the required evidence, contract, schema, policy, and release checks.

Deny by default when any of the following occur:

- A `PUBLIC_AQI_REPORT`, AQI category, AQI color, AQI forecast/report, or AQI summary is tagged as an observed concentration object.
- An AQI value is used as if it were a PM2.5, ozone, or other pollutant concentration measurement.
- A field, legend, tooltip, API response, AI answer, catalog title, or layer name labels AQI as “concentration” without the correct concentration object family and evidence trail.
- AQI context is presented as an `OBSERVED_SENSOR` record without station/source/evidence/method support.
- A derived output lacks pollutant identity, units, method, source lineage, uncertainty/caveats, or review state required by governing contracts and policy.
- A release candidate attempts to publish AQI-as-concentration without policy approval and rollback/correction path.

Allow only when the test subject is explicitly a governed concentration object or derived/fusion product and passes the required contract, schema, policy, evidence, and release checks.

---

## 4. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| Parent test root allows policy negative cases | CONFIRMED from `tests/README.md`. |
| Atmosphere file-system plan names `aqi-not-concentration.rego` | CONFIRMED; planning path is marked PROPOSED in the plan. |
| `policy/domains/atmosphere/aqi_is_not_concentration.rego` exists | CONFIRMED; scaffold only in current evidence. |
| `policy/domains/atmosphere/aqi-not-concentration.rego` exists | NOT FOUND in this session; planning path may be stale or pending. |
| Doctrine says AQI must not be presented as concentration | CONFIRMED from current Atmosphere policy/knowledge-character docs. |
| Actual tests in this directory | UNKNOWN in this README. |
| Canonical policy module/file name | NEEDS VERIFICATION due to plan/file-name drift. |
| Canonical object schemas and runtime validator names | NEEDS VERIFICATION. |
| CI job names / pytest markers | NEEDS VERIFICATION. |

This README is a lane contract. It does not claim that the full policy logic, fixtures, validators, schemas, or CI gates are implemented.

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for AQI-vs-concentration policy-deny tests.
- Tests that reject AQI values, categories, color bands, public reports, or forecast summaries labeled as concentration observations.
- Tests that reject AQI-derived concentration claims without pollutant identity, units, lineage, method, uncertainty/caveat, and review state.
- Tests that verify public API/UI/AI surfaces do not call AQI “PM2.5 concentration,” “ozone concentration,” or generic pollutant concentration.
- Tests that assert AQI context can be surfaced only as AQI/report/context unless a governed concentration object exists.
- Tests that call policy/validator implementations from their canonical homes.
- Tests that use deterministic, public-safe invalid fixtures for AQI-as-concentration cases.
- Tiny local test-only examples when they are not reusable fixtures and the reason is documented.

---

## 6. What does not belong here

This directory must not contain:

- Policy implementation files.
- Production validators, AQI conversion code, or concentration derivation code.
- Source fetchers, scrapers, live AQI pulls, live concentration pulls, or downloaded source caches.
- Raw AQI reports, sensor observations, processed datasets, catalog records, triplets, or published layers.
- Real credentials, API keys, service accounts, cookies, signed URLs, or private endpoints.
- Schema, contract, source registry, release, receipt, or proof definitions.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Tests that run live network calls by default.
- Emergency or health guidance that presents KFM as the issuing authority.

> [!CAUTION]
> The denial is about knowledge integrity, not only units. AQI may be derived from pollutant measurements in outside systems, but KFM must not let a public index/report object masquerade as a concentration observation.

[↑ Back to top](#top)

---

## 7. Policy-deny proof matrix

| Scenario | Expected result | Rationale |
|---|---|---|
| AQI report has `object_family = PM25Observation` | `DENY` or validation failure | Object-family collapse. |
| AQI report has `knowledge_character = OBSERVED_SENSOR` | `DENY` or validation failure | Knowledge-character collapse. |
| AQI category is used as a PM2.5 concentration value | `DENY` or validation failure | Index/category is not concentration. |
| AQI color band is rendered as concentration legend | `DENY` or UI trust-state failure | Public overclaim. |
| API response maps AQI to concentration field without evidence | `DENY` or `ERROR` | Field meaning mismatch. |
| AI answer converts AQI to pollutant concentration without cited evidence | `ABSTAIN` or corrected answer with caveat | Generated language cannot overrule evidence. |
| Derived concentration lacks pollutant identity/units | `DENY` | Incomplete concentration object. |
| Derived concentration lacks method, lineage, uncertainty, or caveat | `DENY` or `ABSTAIN` | Unsupported derived claim. |
| AQI context is surfaced as public AQI/report context with issuer/freshness | Allowed if evidence and policy pass | Contextual AQI reporting is not concentration. |
| Release candidate includes rollback/correction but lacks concentration evidence | `DENY` | Governance packaging cannot replace evidence. |
| Valid concentration object with evidence, units, pollutant identity, method, review, and policy approval | Allowed only as concentration object | Separate governed object, not relabeled AQI. |

---

## 8. Allowed concentration boundary

AQI may be displayed as public reporting context. Concentration may be displayed only when a separate concentration object exists and passes governance.

A valid concentration or derived/fusion object should make these visible when required by the governing contract and policy:

| Requirement | Purpose |
|---|---|
| Separate stable ID | Prevents mutation of AQI into concentration by relabeling. |
| Pollutant identity | Names the pollutant represented, such as PM2.5 or ozone. |
| Units | Distinguishes concentration units from AQI index/category values. |
| Source/evidence lineage | Shows source, time, station/context, method, source role, and evidence path. |
| Measurement or derivation method | Distinguishes observed, modeled, derived, regulatory, or public-report context. |
| EvidenceRef / EvidenceBundle linkage | Allows cite-or-abstain behavior. |
| Knowledge character | Distinguishes `PUBLIC_AQI_REPORT`, `OBSERVED_SENSOR`, `REGULATORY_ARCHIVE`, `LOW_COST_SENSOR`, `DERIVED_FUSION`, or other character. |
| Source role | Prevents primary/corroborating/context/restricted collapse. |
| Uncertainty/confidence/caveat | Prevents false precision and overclaiming. |
| Policy decision | Shows whether the claim is allowed, denied, restricted, or requires abstention. |
| Release metadata | Provides correction and rollback paths if published. |

Without those controls, the safest result is denial or abstention.

---

## 9. Fixture contract

Reusable fixtures should normally live under:

```text
fixtures/domains/atmosphere/
```

Expected fixture families for this lane include:

| Fixture kind | Example purpose |
|---|---|
| Invalid AQI tagged as concentration | Proves relabeling is denied. |
| Invalid AQI with concentration units | Proves unit/meaning mismatch fails. |
| Invalid AQI legend as PM2.5 concentration | Proves public UI overclaim fails. |
| Invalid AI/API answer fixture | Proves generated/API surface cannot infer concentration from AQI alone. |
| Invalid derived output missing pollutant identity | Proves concentration claims require pollutant identity. |
| Invalid derived output missing lineage/caveat | Proves derived claims require provenance and caveats. |
| Valid AQI context | Proves AQI can be used as public AQI/report context with issuer/freshness. |
| Valid concentration observation | Proves a correctly governed concentration object can pass under separate identity. |

Fixture records should be deterministic, public-safe, no-network, and visibly test-only or governed fixture data. They must not be raw source payloads or release artifacts.

---

## 10. Expected outcomes

Policy-deny tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

| Condition | Preferred outcome |
|---|---|
| Mischaracterized AQI-as-concentration | `DENY` or validation failure. |
| AI/user asks for concentration from AQI only | `ABSTAIN` or qualified answer that AQI is not concentration. |
| EvidenceRef missing | `ABSTAIN` or validation failure. |
| Policy module missing or ambiguous | `ERROR` in test setup, not silent pass. |
| Fixture missing | Test failure with clear path. |
| Derived concentration evidence incomplete | `DENY` or `ABSTAIN`. |
| Valid governed concentration product | Allowed only as concentration object with separate identity. |

---

## 11. Lifecycle and publication gates

This lane supports the KFM lifecycle but does not move records through it:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Gate | AQI-vs-concentration rule |
|---|---|
| RAW | AQI source payloads remain raw source material; do not relabel as concentration. |
| WORK / QUARANTINE | Suspect AQI-as-concentration mappings should remain work/quarantine until resolved. |
| PROCESSED | Processed output must preserve object meaning, pollutant identity, units, and evidence lineage. |
| CATALOG / TRIPLET | Catalog/graph projection must not collapse AQI context into concentration observation. |
| PUBLISHED | Published claims must carry correct identity, caveat, evidence, policy, correction, and rollback. |
| RECEIPTS / PROOFS | Tests may check references but do not store trust-bearing receipts/proofs here. |
| RELEASE | Release decisions remain under `release/`, not `tests/`. |

Publication is a governed state transition. A passing test is not a release approval.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, policy test runners, marker names, and CI job names are **NEEDS VERIFICATION** until checked against the actual repository configuration.

Likely lane check:

```bash
pytest tests/domains/atmosphere/policy-deny/aqi-vs-concentration
```

Likely parent policy-deny check:

```bash
pytest tests/domains/atmosphere/policy-deny
```

Possible policy engine check if configured:

```bash
opa test policy/domains/atmosphere tests/domains/atmosphere/policy-deny/aqi-vs-concentration
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does the test fail when AQI is relabeled as concentration?
- Does the test distinguish public AQI reports from observed/derived concentration objects?
- Does a concentration claim require pollutant identity, units, method, evidence, and review state?
- Are uncertainty, caveat, source role, and knowledge character visible where required?
- Are AI/UI/API/catalog labels prevented from overclaiming?
- Does the test call policy/validator code from canonical homes rather than reimplementing it here?
- Are fixtures local, deterministic, public-safe, and no-network?
- Are receipts, proofs, release decisions, and source data kept out of this directory?
- Are policy scaffold gaps and filename drift marked NEEDS VERIFICATION rather than hidden?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/domains/atmosphere/policy-deny/` | Parent policy-deny test lane. | NEEDS VERIFICATION beyond this README. |
| `policy/domains/atmosphere/aqi_is_not_concentration.rego` | Proposed policy scaffold for this denial. | CONFIRMED present; scaffold only. |
| `policy/domains/atmosphere/aqi-not-concentration.rego` | Planning-name variant from file-system plan. | NOT FOUND in this session; canonical name NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/pm25-observation.md` | Object-meaning contract for PM2.5 observations. | Present in search results; content not verified in this README. |
| `contracts/domains/atmosphere/ozone-observation.md` | Object-meaning contract for ozone observations. | Present in search results; content not verified in this README. |
| `docs/sources/catalog/epa/airnow-api.md` | Source catalog profile likely relevant to AQI/report context. | Present in search results; content not verified in this README. |
| `fixtures/domains/atmosphere/` | Reusable valid/invalid fixture home. | Fixture families for this lane NEED VERIFICATION. |
| `tools/validators/` | Validator implementation home. | Specific module names NEEDS VERIFICATION. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | Planning source naming AQI-not-concentration policy lane. | CONFIRMED; plan language includes PROPOSED paths. |
| `docs/domains/atmosphere/POLICY.md` | Human-facing policy doctrine naming AQI ≠ concentration. | CONFIRMED in current evidence. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| Which policy filename is canonical: `aqi_is_not_concentration.rego` or `aqi-not-concentration.rego`? | NEEDS VERIFICATION | The underscored scaffold exists; the hyphenated planning path was not found in this session. |
| What is the canonical policy package name? | NEEDS VERIFICATION | Must align with final OPA/Rego conventions. |
| Which object family represents public AQI reports? | NEEDS VERIFICATION | The knowledge character is confirmed as `PUBLIC_AQI_REPORT`; exact object family/schema needs confirmation. |
| What schema fields distinguish AQI report/context from concentration observation? | NEEDS VERIFICATION | Check contracts and schemas before writing tests. |
| What derived/fusion object family represents any permitted AQI-derived concentration, if allowed? | OPEN | May require contract/schema/policy work. |
| What concentration units and pollutant identifiers are mandatory? | NEEDS VERIFICATION | Should be defined by contracts/schemas/policy. |
| Should AI/UI/API trust-state tests live here or in API/UI lanes? | OPEN | This lane may own policy unit tests; UI/API lanes may own surface rendering. |
| Are approved AQI fixtures synthetic, transformed public samples, or source-derived fixture records? | NEEDS VERIFICATION | Prefer public-safe transformed or synthetic fixtures by default. |

---

## 16. Definition of done

This lane is mature when:

- [ ] A canonical AQI-not-concentration policy module is selected.
- [ ] Tests deny AQI values, categories, colors, or reports labeled or surfaced as concentration observations.
- [ ] Tests deny concentration claims without pollutant identity, units, method, evidence, caveat, and review state.
- [ ] Tests allow AQI only as AQI/report/context when policy permits.
- [ ] Fixtures are deterministic, public-safe, no-network, and stored in the governed fixture lane unless test-local.
- [ ] Tests call canonical validators/policies rather than redefining them.
- [ ] UI/API/AI overclaim paths are covered here or delegated to the appropriate lane with links.
- [ ] CI or local validation exposes the denial clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere AQI-vs-concentration policy-deny test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the underscored policy scaffold and policy doctrine, while the hyphenated planning filename, policy implementation depth, tests, schemas, validators, fixtures, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
