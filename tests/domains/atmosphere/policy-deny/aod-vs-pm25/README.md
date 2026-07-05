<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/policy-deny/aod-vs-pm25/readme
title: Atmosphere Policy-Deny Test Lane — AOD vs PM2.5 README
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
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md
  - policy/domains/atmosphere/aod-not-pm25.rego
  - policy/domains/atmosphere/aod_is_not_pm25.rego
  - contracts/domains/atmosphere/aod-raster.md
  - contracts/domains/atmosphere/pm25-observation.md
  - fixtures/domains/atmosphere/objects/AODRaster.invalid.tagged_as_pm25.json
  - tools/validators/
tags:
  - kfm
  - tests
  - atmosphere
  - policy-deny
  - aod
  - pm25
  - anti-collapse
  - evidence
  - fail-closed
] -->

<a id="top"></a>

# Atmosphere Policy-Deny Tests — AOD vs PM2.5

> Test-lane contract for proving KFM denies attempts to treat **Aerosol Optical Depth (AOD)** as **PM2.5 concentration** without an explicit, governed transformation, evidence trail, uncertainty/caveat model, and separate object identity.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational)
![rule: AOD%E2%89%A0PM2.5](https://img.shields.io/badge/rule-AOD%E2%89%A0PM2.5-red)
![policy: fail--closed](https://img.shields.io/badge/policy-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)
![sensitivity: public--safe](https://img.shields.io/badge/sensitivity-public--safe-green)

**Status:** `draft`  
**Authority:** test-lane README; not a schema, policy implementation, validator, source registry, release decision, receipt, proof, or fixture inventory  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `policy-deny/aod-vs-pm25/`  
**Default posture:** deny by default; cite-or-abstain; preserve source/knowledge-character separation  
**Last reviewed:** 2026-07-05

> [!IMPORTANT]
> KFM Atmosphere is **not** an emergency alerting or life-safety system. This test lane may verify smoke, aerosol, and air-quality interpretation boundaries, but it must not issue emergency guidance or imply that KFM is the official source for health instructions.

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Rule statement](#3-rule-statement)
4. [Status and evidence boundary](#4-status-and-evidence-boundary)
5. [What belongs here](#5-what-belongs-here)
6. [What does not belong here](#6-what-does-not-belong-here)
7. [Policy-deny proof matrix](#7-policy-deny-proof-matrix)
8. [Allowed transformation boundary](#8-allowed-transformation-boundary)
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

This directory is the Atmosphere / Air test sublane for the **AOD vs PM2.5 policy-deny rule**.

It exists to prove that KFM does not collapse two different atmospheric knowledge objects:

- **AOD raster / aerosol context** — a remote-sensing or model/context product describing aerosol optical properties along an atmospheric column or scene.
- **PM2.5 observation / concentration** — a particulate matter concentration observation or derived concentration product with units, station/context, evidence, and admissibility controls.

The lane should verify that an AOD value, raster, mask, or context layer is denied when it is mislabeled, surfaced, cataloged, mapped, summarized, or published as PM2.5 without a governed conversion process.

A passing suite should support these claims:

1. **AOD is not PM2.5 by label change.** Renaming a field, layer, slug, legend, or claim does not convert AOD into PM2.5 concentration.
2. **AOD-derived PM2.5 requires a new governed object.** A conversion or fusion output must carry separate identity, lineage, evidence, caveats, model assumptions, uncertainty/confidence, and review state.
3. **Public UI and AI surfaces must not overclaim.** AOD context may be shown as aerosol/smoke context, but not as measured PM2.5 unless the published object is actually governed as PM2.5.
4. **Catalog and release gates fail closed.** Mischaracterized AOD-as-PM2.5 candidates should produce `DENY`, `ABSTAIN`, or validation failure, not quiet promotion.
5. **Fixtures are public-safe and deterministic.** Tests use local valid/invalid samples and do not fetch live satellite, air-quality, or model services by default.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/policy-deny/aod-vs-pm25/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove a specific Atmosphere policy denial. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Parent lane | `policy-deny/` |
| Sublane | `aod-vs-pm25/` |
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

**Rule:** AOD must not be treated as PM2.5 concentration unless a governed transformation creates a separate, reviewable, evidence-backed output.

Deny by default when any of the following occur:

- An `AODRaster`, AOD layer, aerosol mask, smoke context, or remote-sensing product is tagged as `PM25Observation` without transformation evidence.
- A field, legend, tooltip, API claim, AI response, catalog title, or layer name labels AOD as “PM2.5” or “PM2.5 concentration” without the correct object family and evidence trail.
- A derived/fusion output lacks lineage from AOD input to PM2.5-like output.
- A derived output lacks uncertainty, confidence, calibration method, caveats, or review state required by the governing contract/policy.
- A public map/AI/client response presents AOD context as an observed ground concentration.
- A release candidate attempts to publish AOD-as-PM2.5 without policy approval and rollback/correction path.

Allow only when the test subject is explicitly a governed derived product and passes the required contract, schema, policy, evidence, and release checks.

---

## 4. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| Parent test root allows policy negative cases | CONFIRMED from `tests/README.md`. |
| Atmosphere file-system plan names `aod-not-pm25.rego` | CONFIRMED; policy file is marked PROPOSED in the plan. |
| `policy/domains/atmosphere/aod-not-pm25.rego` exists | CONFIRMED; scaffold only in current evidence. |
| `policy/domains/atmosphere/aod_is_not_pm25.rego` exists | CONFIRMED; scaffold only in current evidence. |
| Invalid fixture placeholder for tagged AOD exists | CONFIRMED; placeholder only in current evidence. |
| Actual tests in this directory | UNKNOWN in this README. |
| Canonical policy module name | NEEDS VERIFICATION due to both hyphenated and underscored scaffold filenames. |
| Canonical object schemas and runtime validator names | NEEDS VERIFICATION. |
| CI job names / pytest markers | NEEDS VERIFICATION. |

This README is a lane contract. It does not claim that the full policy logic, fixtures, validators, schemas, or CI gates are implemented.

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for AOD-vs-PM2.5 policy-deny tests.
- Tests that reject AOD records labeled as PM2.5 observations.
- Tests that reject AOD-derived PM2.5 claims without lineage, uncertainty, caveat, method, and review state.
- Tests that verify public API/UI/AI surfaces do not call AOD “PM2.5 concentration.”
- Tests that assert AOD context can be surfaced only as aerosol/smoke/remote-sensing context unless a governed derived object exists.
- Tests that reference invalid fixtures such as `AODRaster.invalid.tagged_as_pm25.json`.
- Tests that call policy/validator implementations from their canonical homes.
- Tiny local test-only examples when they are not reusable fixtures and the reason is documented.

---

## 6. What does not belong here

This directory must not contain:

- Policy implementation files.
- Production validators or transformation code.
- Source fetchers, scrapers, live satellite pulls, live AQI/PM2.5 pulls, or downloaded source caches.
- Raw AOD rasters, PM2.5 observations, processed datasets, catalog records, triplets, or published layers.
- Real credentials, API keys, service accounts, cookies, signed URLs, or private endpoints.
- Schema, contract, source registry, release, receipt, or proof definitions.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Tests that run live network calls by default.
- Emergency or health guidance that presents KFM as the issuing authority.

> [!CAUTION]
> The denial is about knowledge integrity, not just units. Even if a derived estimate uses AOD as an input, the derived object must not be treated as a raw AOD layer or an observed PM2.5 station concentration.

[↑ Back to top](#top)

---

## 7. Policy-deny proof matrix

| Scenario | Expected result | Rationale |
|---|---|---|
| AOD object has `object_family = PM25Observation` | `DENY` or validation failure | Object-family collapse. |
| AOD layer title says “PM2.5 concentration” | `DENY` or UI trust-state failure | Public overclaim. |
| AOD raster has PM2.5 units without transformation | `DENY` or validation failure | Unit/meaning mismatch. |
| AOD-derived PM2.5 lacks lineage | `DENY` | Missing EvidenceRef / transformation trace. |
| AOD-derived PM2.5 lacks uncertainty/caveat | `DENY` or `ABSTAIN` | Unsupported derived claim. |
| AOD context is surfaced as smoke/aerosol context with caveat | Allowed if evidence and policy pass | Contextual use is not a PM2.5 concentration claim. |
| AI answer says “AOD proves PM2.5 level” | `ABSTAIN` or corrected answer with caveat | Generated language cannot overrule evidence. |
| Catalog candidate maps AOD into PM2.5 catalog lane without review | `DENY` | Publication gate must fail closed. |
| Release candidate includes rollback/correction but lacks transformation evidence | `DENY` | Governance packaging cannot replace evidence. |
| Valid derived/fusion object with lineage, method, uncertainty, caveat, review, and policy approval | Allowed only under derived identity | New governed object, not relabeled AOD. |

---

## 8. Allowed transformation boundary

AOD may be an input to a governed derived or fusion product, but only under a separate identity and with explicit supporting records.

A valid derived/fusion object should make these visible when required by the governing contract and policy:

| Requirement | Purpose |
|---|---|
| Separate stable ID | Prevents mutation of AOD into PM2.5 by relabeling. |
| Input lineage | Shows AOD source, time, spatial footprint, processing stage, and source role. |
| Transformation method | Names the conversion, model, calibration, or fusion approach. |
| EvidenceRef / EvidenceBundle linkage | Allows cite-or-abstain behavior. |
| Knowledge character | Distinguishes observed, modeled, remote-sensing, derived/fusion, or contextual evidence. |
| Source role | Prevents primary/corroborating/context/restricted collapse. |
| Uncertainty/confidence | Prevents false precision and overclaiming. |
| Caveats and admissibility | Shows limits of use and review state. |
| Policy decision | Shows whether the claim is allowed, denied, or requires abstention. |
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
| Invalid AOD tagged as PM2.5 | Proves relabeling is denied. |
| Invalid AOD with PM2.5 UI legend | Proves public overclaim fails. |
| Invalid derived output missing lineage | Proves conversion claims require provenance. |
| Invalid derived output missing uncertainty | Proves derived claims require caveats/confidence. |
| Valid AOD context | Proves AOD can be used as aerosol/smoke context without PM2.5 claim. |
| Valid derived/fusion candidate | Proves a properly governed derived object can pass under separate identity. |

Fixture records should be deterministic, public-safe, no-network, and visibly test-only or governed fixture data. They must not be raw source payloads or release artifacts.

---

## 10. Expected outcomes

Policy-deny tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

| Condition | Preferred outcome |
|---|---|
| Mischaracterized AOD-as-PM2.5 | `DENY` or validation failure. |
| AI/user asks for PM2.5 from AOD only | `ABSTAIN` or qualified answer that AOD is not PM2.5. |
| EvidenceRef missing | `ABSTAIN` or validation failure. |
| Policy module missing or ambiguous | `ERROR` in test setup, not silent pass. |
| Fixture missing | Test failure with clear path. |
| Derived/fusion evidence incomplete | `DENY` or `ABSTAIN`. |
| Valid governed derived product | Allowed only as derived/fusion product with separate identity. |

---

## 11. Lifecycle and publication gates

This lane supports the KFM lifecycle but does not move records through it:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Gate | AOD-vs-PM2.5 rule |
|---|---|
| RAW | AOD source payloads remain raw source material; do not relabel as PM2.5. |
| WORK / QUARANTINE | Suspect AOD-as-PM2.5 mappings should remain work/quarantine until resolved. |
| PROCESSED | Processed output must preserve object meaning and evidence lineage. |
| CATALOG / TRIPLET | Catalog/graph projection must not collapse AOD context into PM2.5 observation. |
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
pytest tests/domains/atmosphere/policy-deny/aod-vs-pm25
```

Likely parent policy-deny check:

```bash
pytest tests/domains/atmosphere/policy-deny
```

Possible policy engine check if configured:

```bash
opa test policy/domains/atmosphere tests/domains/atmosphere/policy-deny/aod-vs-pm25
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does the test fail when AOD is relabeled as PM2.5?
- Does the test distinguish AOD context from PM2.5 observation/concentration?
- Does a derived/fusion PM2.5-like output require separate identity and lineage?
- Are uncertainty, caveat, method, review state, and evidence visible where required?
- Are AI/UI/API/catalog labels prevented from overclaiming?
- Does the test call policy/validator code from canonical homes rather than reimplementing it here?
- Are fixtures local, deterministic, public-safe, and no-network?
- Are receipts, proofs, release decisions, and source data kept out of this directory?
- Are policy scaffold gaps marked NEEDS VERIFICATION rather than hidden?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/domains/atmosphere/policy-deny/` | Parent policy-deny test lane. | NEEDS VERIFICATION beyond this README. |
| `policy/domains/atmosphere/aod-not-pm25.rego` | Proposed policy scaffold for this denial. | CONFIRMED present; scaffold only. |
| `policy/domains/atmosphere/aod_is_not_pm25.rego` | Alternate/duplicate-looking scaffold name. | CONFIRMED present; canonical name NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/aod-raster.md` | Object-meaning contract for AOD raster/context. | Present in search results; content not verified in this README. |
| `contracts/domains/atmosphere/pm25-observation.md` | Object-meaning contract for PM2.5 observations. | Present in search results; content not verified in this README. |
| `fixtures/domains/atmosphere/objects/AODRaster.invalid.tagged_as_pm25.json` | Candidate invalid fixture placeholder. | CONFIRMED present; placeholder only. |
| `tools/validators/` | Validator implementation home. | Specific module names NEEDS VERIFICATION. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | Planning source naming AOD-not-PM2.5 policy lane. | CONFIRMED; plan language includes PROPOSED paths. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| Which policy filename is canonical: `aod-not-pm25.rego` or `aod_is_not_pm25.rego`? | NEEDS VERIFICATION | Both scaffold files exist in current evidence. |
| What is the canonical policy package name? | NEEDS VERIFICATION | Must align with final OPA/Rego conventions. |
| What schema fields distinguish AOD raster/context from PM2.5 observation? | NEEDS VERIFICATION | Check contracts and schemas before writing tests. |
| What derived/fusion object family represents AOD-derived PM2.5, if allowed? | OPEN | May require contract/schema/policy work. |
| What uncertainty/caveat fields are mandatory for derived outputs? | NEEDS VERIFICATION | Should be defined by contracts/schemas/policy. |
| Should AI/UI/API trust-state tests live here or in API/UI lanes? | OPEN | This lane may own policy unit tests; UI/API lanes may own surface rendering. |
| Are there approved real-world public fixtures, or only synthetic placeholders? | NEEDS VERIFICATION | Prefer public-safe transformed or synthetic fixtures by default. |

---

## 16. Definition of done

This lane is mature when:

- [ ] A canonical AOD-not-PM2.5 policy module is selected.
- [ ] Tests deny AOD objects labeled or surfaced as PM2.5 observations.
- [ ] Tests deny AOD-derived PM2.5 claims without lineage, method, uncertainty, caveat, evidence, and review state.
- [ ] Tests allow AOD only as AOD/aerosol/smoke/remote-sensing context when policy permits.
- [ ] Fixtures are deterministic, public-safe, no-network, and stored in the governed fixture lane unless test-local.
- [ ] Tests call canonical validators/policies rather than redefining them.
- [ ] UI/API/AI overclaim paths are covered here or delegated to the appropriate lane with links.
- [ ] CI or local validation exposes the denial clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere AOD-vs-PM2.5 policy-deny test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms policy scaffold files and an invalid fixture placeholder, but policy implementation depth, canonical module name, tests, schemas, validators, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
