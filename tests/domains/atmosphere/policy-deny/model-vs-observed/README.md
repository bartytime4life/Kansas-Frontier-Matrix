<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/policy-deny/model-vs-observed/readme
title: Atmosphere Policy-Deny Test Lane — Model vs Observed README
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
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - docs/domains/atmosphere/POLICY.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md
  - policy/domains/atmosphere/model-as-observed-deny.rego
  - contracts/domains/atmosphere/ForecastContext.md
  - contracts/domains/atmosphere/SmokeContext.md
  - contracts/domains/atmosphere/wind-field.md
  - contracts/domains/atmosphere/AirObservation.md
  - contracts/domains/atmosphere/PM25Observation.md
  - contracts/domains/atmosphere/OzoneObservation.md
  - fixtures/domains/atmosphere/
  - tools/validators/
tags:
  - kfm
  - tests
  - atmosphere
  - policy-deny
  - model
  - observed
  - atmospheric-model-field
  - anti-collapse
  - evidence
  - fail-closed
] -->

<a id="top"></a>

# Atmosphere Policy-Deny Tests — Model vs Observed

> Test-lane contract for proving KFM denies attempts to treat **ATMOSPHERIC_MODEL_FIELD** records, forecasts, or modeled contexts as observed sensor measurements without a governed transformation, evidence trail, uncertainty/caveat model, and separate object identity.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational)
![rule: model%E2%89%A0observed](https://img.shields.io/badge/rule-model%E2%89%A0observed-red)
![policy: fail--closed](https://img.shields.io/badge/policy-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)
![sensitivity: public--safe](https://img.shields.io/badge/sensitivity-public--safe-green)

**Status:** `draft`  
**Authority:** test-lane README; not a schema, policy implementation, validator, source registry, release decision, receipt, proof, or fixture inventory  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `policy-deny/model-vs-observed/`  
**Default posture:** deny by default; cite-or-abstain; preserve modeled/observed separation  
**Last reviewed:** 2026-07-05

> [!IMPORTANT]
> KFM Atmosphere is **not** an emergency alerting or life-safety system. This test lane may verify model, forecast, smoke, wind, and concentration-claim boundaries, but it must not issue official guidance or make KFM the authoritative source for protective action.

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

This directory is the Atmosphere / Air test sublane for the **model vs observed policy-deny rule**.

It exists to prove that KFM does not collapse two different atmospheric knowledge objects:

- **Atmospheric model field / forecast context** — a modeled, forecast, simulation, reanalysis, or context product with model identity, run time, valid time, inputs, and uncertainty/caveats.
- **Observed sensor measurement** — a direct instrument/platform observation with station/platform context, observed time, units, source role, QA/calibration, evidence, and admissibility controls.

The lane should verify that a model field, forecast, simulated value, gridded product, smoke forecast, wind field, or derived context is denied when it is mislabeled, surfaced, cataloged, mapped, summarized, or published as an observed measurement without a governed transformation process.

A passing suite should support these claims:

1. **Model is not observed by label change.** Renaming a field, layer, slug, legend, or claim does not convert modeled data into an observed sensor measurement.
2. **Observation claims require observation objects.** An observation record must carry observation identity, observed time, source/evidence, method, units, station/platform context, QA/caveats, and review state as required by the governing contract/policy.
3. **Modeled context can be surfaced only as modeled context.** Forecasts, reanalysis, smoke/wind/model fields, and context layers may be displayed as modeled/contextual products, not as observations unless a governed observed object exists.
4. **Public UI and AI surfaces must not overclaim.** Generated text, map labels, tooltips, layer names, and summaries must not translate model output into observed measurement language without evidence.
5. **Catalog and release gates fail closed.** Mischaracterized model-as-observed candidates should produce `DENY`, `ABSTAIN`, or validation failure, not quiet promotion.
6. **Fixtures are public-safe and deterministic.** Tests use local valid/invalid samples and do not fetch live model, forecast, observation, tile, or sensor services by default.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/policy-deny/model-vs-observed/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove a specific Atmosphere policy denial. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Parent lane | `policy-deny/` |
| Sublane | `model-vs-observed/` |
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

**Rule:** Modeled Atmosphere records must not be treated as observed measurements unless a separate, governed observed object exists and passes required evidence, contract, schema, policy, and release checks.

Deny by default when any of the following occur:

- An `ATMOSPHERIC_MODEL_FIELD`, `ForecastContext`, modeled `SmokeContext`, `WindField`, reanalysis, or gridded model product is tagged as an observed sensor measurement.
- A model field is used as if it were a station/platform observation.
- A field, legend, tooltip, API response, AI answer, catalog title, or layer name labels modeled data as “observed” without the correct observed object family and evidence trail.
- A forecast valid time is presented as an observed time.
- A derived output lacks model identity, run time, valid time, method, input lineage, uncertainty/caveats, or review state required by governing contracts and policy.
- A release candidate attempts to publish model-as-observed without policy approval and rollback/correction path.

Allow only when the test subject is explicitly a governed observed object or derived/fusion product and passes the required contract, schema, policy, evidence, and release checks.

---

## 4. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| Parent test root allows policy negative cases | CONFIRMED from `tests/README.md`. |
| Atmosphere file-system plan names `model-as-observed-deny.rego` | CONFIRMED; planning path is marked PROPOSED in the plan. |
| `policy/domains/atmosphere/model-as-observed-deny.rego` exists | CONFIRMED; scaffold only in current evidence. |
| `policy/domains/atmosphere/model_as_observed_deny.rego` exists | NOT FOUND in this session; package name uses underscores inside the hyphenated file. |
| Doctrine says model fields must not be presented as observations | CONFIRMED from current Atmosphere policy/knowledge-character docs. |
| Contracts for ForecastContext, SmokeContext, WindField, and observation objects are present in search results | CONFIRMED as search results; content not fully verified in this README. |
| Actual tests in this directory | UNKNOWN in this README. |
| Canonical policy module/file name | NEEDS VERIFICATION due to filename/package convention questions. |
| Canonical object schemas and runtime validator names | NEEDS VERIFICATION. |
| CI job names / pytest markers | NEEDS VERIFICATION. |

This README is a lane contract. It does not claim that the full policy logic, fixtures, validators, schemas, or CI gates are implemented.

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for model-vs-observed policy-deny tests.
- Tests that reject modeled records labeled as observations.
- Tests that reject forecast/model values presented as station/platform observations.
- Tests that reject model-derived observed claims without model identity, valid time, lineage, method, uncertainty/caveat, and review state.
- Tests that verify public API/UI/AI surfaces do not call modeled data “observed.”
- Tests that assert modeled context can be surfaced only as modeled/forecast/context unless a governed observation object exists.
- Tests that call policy/validator implementations from their canonical homes.
- Tests that use deterministic, public-safe invalid fixtures for model-as-observed cases.
- Tiny local test-only examples when they are not reusable fixtures and the reason is documented.

---

## 6. What does not belong here

This directory must not contain:

- Policy implementation files.
- Production validators, model-processing code, forecast adapters, or observation derivation code.
- Source fetchers, scrapers, live forecast/model pulls, live observation pulls, tile requests, or downloaded source caches.
- Raw model fields, observation payloads, processed datasets, catalog records, triplets, or published layers.
- Real credentials, API keys, service accounts, cookies, signed URLs, or private endpoints.
- Schema, contract, source registry, release, receipt, or proof definitions.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Tests that run live network calls by default.
- Emergency or life-safety guidance that presents KFM as the issuing authority.

> [!CAUTION]
> The denial is about knowledge integrity, not only units. A model can be useful context, but KFM must preserve modeled identity, run/valid time, lineage, uncertainty, and caveats rather than treating it as an observation.

[↑ Back to top](#top)

---

## 7. Policy-deny proof matrix

| Scenario | Expected result | Rationale |
|---|---|---|
| Model field has `object_family = AirObservation` | `DENY` or validation failure | Object-family collapse. |
| Forecast context has `knowledge_character = OBSERVED_SENSOR` | `DENY` or validation failure | Knowledge-character collapse. |
| Model valid time is treated as observed time | `DENY` or validation failure | Time-kind collapse. |
| Forecast layer title says “observed” | `DENY` or UI trust-state failure | Public overclaim. |
| API response maps modeled value to observation field without evidence | `DENY` or `ERROR` | Field meaning mismatch. |
| AI answer says model output is an observed measurement | `ABSTAIN` or corrected answer with caveat | Generated language cannot overrule evidence. |
| Derived observation lacks model/input lineage | `DENY` | Missing EvidenceRef / transformation trace. |
| Derived observation lacks uncertainty/caveat | `DENY` or `ABSTAIN` | Unsupported derived claim. |
| Modeled context is surfaced as model/forecast context with caveat | Allowed if evidence and policy pass | Contextual use is not an observed measurement claim. |
| Release candidate includes rollback/correction but lacks observed evidence | `DENY` | Governance packaging cannot replace evidence. |
| Valid observed object with evidence, observed time, method, units, review, and policy approval | Allowed only as observed object | Separate governed object, not relabeled model output. |

---

## 8. Allowed transformation boundary

Model output may inform a governed derived or fusion product, but only under a separate identity and with explicit supporting records.

A valid derived/fusion or observed object should make these visible when required by the governing contract and policy:

| Requirement | Purpose |
|---|---|
| Separate stable ID | Prevents mutation of model output into an observation by relabeling. |
| Input lineage | Shows model source, run time, valid time, spatial footprint, processing stage, and source role. |
| Model identity | Names the forecast/model/reanalysis system and product version. |
| Transformation method | Names the conversion, calibration, or fusion approach. |
| EvidenceRef / EvidenceBundle linkage | Allows cite-or-abstain behavior. |
| Knowledge character | Distinguishes `ATMOSPHERIC_MODEL_FIELD`, `OBSERVED_SENSOR`, `DERIVED_FUSION`, or other character. |
| Source role | Prevents primary/corroborating/context/restricted collapse. |
| Uncertainty/confidence | Prevents false precision and overclaiming. |
| Caveats and admissibility | Shows limits of use and review state. |
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
| Invalid model tagged as observed | Proves relabeling is denied. |
| Invalid forecast with observed-time field | Proves time-kind collapse fails. |
| Invalid model layer with observed UI label | Proves public UI overclaim fails. |
| Invalid AI/API answer fixture | Proves generated/API surface cannot infer observation from model output alone. |
| Invalid derived output missing model lineage | Proves derived claims require provenance. |
| Invalid derived output missing uncertainty/caveat | Proves derived claims require caveats/confidence. |
| Valid model context | Proves modeled data can be used as model/forecast/context with caveat. |
| Valid observed measurement | Proves a correctly governed observation object can pass under separate identity. |

Fixture records should be deterministic, public-safe, no-network, and visibly test-only or governed fixture data. They must not be raw source payloads or release artifacts.

---

## 10. Expected outcomes

Policy-deny tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

| Condition | Preferred outcome |
|---|---|
| Mischaracterized model-as-observed | `DENY` or validation failure. |
| AI/user asks for observed value from model only | `ABSTAIN` or qualified answer that model output is not an observation. |
| EvidenceRef missing | `ABSTAIN` or validation failure. |
| Policy module missing or ambiguous | `ERROR` in test setup, not silent pass. |
| Fixture missing | Test failure with clear path. |
| Derived/fusion evidence incomplete | `DENY` or `ABSTAIN`. |
| Valid governed observation product | Allowed only as observation object with separate identity. |

---

## 11. Lifecycle and publication gates

This lane supports the KFM lifecycle but does not move records through it:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Gate | Model-vs-observed rule |
|---|---|
| RAW | Model source payloads remain raw source material; do not relabel as observed. |
| WORK / QUARANTINE | Suspect model-as-observed mappings should remain work/quarantine until resolved. |
| PROCESSED | Processed output must preserve model identity, source role, time-kind, and evidence lineage. |
| CATALOG / TRIPLET | Catalog/graph projection must not collapse modeled context into observed measurement. |
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
pytest tests/domains/atmosphere/policy-deny/model-vs-observed
```

Likely parent policy-deny check:

```bash
pytest tests/domains/atmosphere/policy-deny
```

Possible policy engine check if configured:

```bash
opa test policy/domains/atmosphere tests/domains/atmosphere/policy-deny/model-vs-observed
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does the test fail when modeled data is relabeled as observed?
- Does the test distinguish model/forecast context from observed sensor measurement?
- Does an observation claim require observed time, source/evidence, method, units, and review state?
- Are model identity, run time, valid time, uncertainty, and caveat visible where required?
- Are AI/UI/API/catalog labels prevented from overclaiming?
- Does the test call policy/validator code from canonical homes rather than reimplementing it here?
- Are fixtures local, deterministic, public-safe, and no-network?
- Are receipts, proofs, release decisions, and source data kept out of this directory?
- Are policy scaffold gaps and filename/package conventions marked NEEDS VERIFICATION rather than hidden?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/domains/atmosphere/policy-deny/` | Parent policy-deny test lane. | NEEDS VERIFICATION beyond this README. |
| `policy/domains/atmosphere/model-as-observed-deny.rego` | Proposed policy scaffold for this denial. | CONFIRMED present; scaffold only. |
| `policy/domains/atmosphere/model_as_observed_deny.rego` | Underscore filename variant. | NOT FOUND in this session; package name uses underscores inside hyphenated file. |
| `contracts/domains/atmosphere/ForecastContext.md` | Object-meaning contract for forecast/model context. | Present in search results; content not verified in this README. |
| `contracts/domains/atmosphere/SmokeContext.md` | Object-meaning contract for smoke context. | Present in search results; content not verified in this README. |
| `contracts/domains/atmosphere/wind-field.md` | Object-meaning contract for wind/model context. | Present in search results; content not verified in this README. |
| `contracts/domains/atmosphere/AirObservation.md` | Object-meaning contract for air observations. | Present in search results; content not verified in this README. |
| `contracts/domains/atmosphere/PM25Observation.md` | Object-meaning contract for PM2.5 observations. | Present in search results; content not verified in this README. |
| `contracts/domains/atmosphere/OzoneObservation.md` | Object-meaning contract for ozone observations. | Present in search results; content not verified in this README. |
| `fixtures/domains/atmosphere/` | Reusable valid/invalid fixture home. | Fixture families for this lane NEED VERIFICATION. |
| `tools/validators/` | Validator implementation home. | Specific module names NEEDS VERIFICATION. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | Planning source naming model-as-observed policy lane. | CONFIRMED; plan language includes PROPOSED paths. |
| `docs/domains/atmosphere/POLICY.md` | Human-facing policy doctrine naming model-is-not-observation. | CONFIRMED in current evidence. |
| `docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md` | Knowledge-character documentation for `ATMOSPHERIC_MODEL_FIELD`. | CONFIRMED in current evidence. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| Is `model-as-observed-deny.rego` the canonical policy filename? | NEEDS VERIFICATION | The hyphenated file exists; the package name uses underscores. |
| What is the canonical policy package name? | NEEDS VERIFICATION | Must align with final OPA/Rego conventions. |
| Which object families may carry `ATMOSPHERIC_MODEL_FIELD`? | NEEDS VERIFICATION | Likely ForecastContext, SmokeContext forecast role, WindField, and model products; confirm contracts/schemas. |
| What fields are mandatory: model identity, run time, valid time, uncertainty, caveat, ensemble, method, or input lineage? | NEEDS VERIFICATION | Should be defined by contracts/schemas/policy. |
| How are reanalysis and derived/fusion products classified? | OPEN | May require separate `DERIVED_FUSION` vs `ATMOSPHERIC_MODEL_FIELD` handling. |
| Should AI/UI/API trust-state tests live here or in API/UI lanes? | OPEN | This lane may own policy unit tests; UI/API lanes may own surface rendering. |
| Are approved fixtures synthetic, transformed public samples, or source-derived fixture records? | NEEDS VERIFICATION | Prefer public-safe transformed or synthetic fixtures by default. |

---

## 16. Definition of done

This lane is mature when:

- [ ] A canonical model-as-observed policy module is selected.
- [ ] Tests deny model/forecast/context records labeled or surfaced as observations.
- [ ] Tests deny observation claims without observed time, evidence, source role, method, units, and review state.
- [ ] Tests allow model output only as model/forecast/context when policy permits.
- [ ] Fixtures are deterministic, public-safe, no-network, and stored in the governed fixture lane unless test-local.
- [ ] Tests call canonical validators/policies rather than redefining them.
- [ ] UI/API/AI overclaim paths are covered here or delegated to the appropriate lane with links.
- [ ] CI or local validation exposes the denial clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere model-vs-observed policy-deny test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the hyphenated policy scaffold, model-is-not-observation doctrine, and related contract search results; policy implementation depth, canonical module name, tests, schemas, validators, fixtures, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
