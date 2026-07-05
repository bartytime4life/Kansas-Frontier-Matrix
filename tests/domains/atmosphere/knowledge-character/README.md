<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/knowledge-character/readme
title: Atmosphere Knowledge Character Test Lane README
type: readme
version: v0.1
status: draft
owners: QA steward + Atmosphere/Air domain steward + policy reviewer (PLACEHOLDER — NEEDS VERIFICATION)
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - tests/README.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTER_REGISTRY.md
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - policy/domains/atmosphere/
  - fixtures/domains/atmosphere/
  - tools/validators/
  - docs/doctrine/directory-rules.md
tags: [kfm, tests, atmosphere, air, knowledge-character, anti-collapse, deny-tests, evidence, policy]
notes:
  - "Directory Rules basis: tests/ proves enforceability; domain appears as tests/domains/<domain>/; this sublane tests the Atmosphere knowledge-character anti-collapse rule."
  - "This README is not validator logic, not the machine registry, not a schema, and not a source catalog."
  - "The exact machine enum and registry home remain OPEN until the relevant ADR and mounted registry settle them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Knowledge Character Tests

> **One-line purpose.** This folder proves that Atmosphere records preserve their knowledge character through validation, evidence resolution, policy, publication, UI/API exposure, and correction without collapsing observations, AQI reports, regulatory archives, low-cost sensors, model fields, remote-sensing masks, climate context, fusion products, meteorological context, advisory context, or site metadata into one another.

![status: draft](https://img.shields.io/badge/status-draft-yellow)
![lane: tests/domains/atmosphere](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere-purple)
![truth: cite-or-abstain](https://img.shields.io/badge/truth-cite--or--abstain-success)
![default: no-network](https://img.shields.io/badge/default-no--network-blue)
![outcomes: deny-abstain](https://img.shields.io/badge/outcomes-DENY%20%2F%20ABSTAIN-critical)
![last reviewed: 2026-07-05](https://img.shields.io/badge/last__reviewed-2026--07--05-lightgrey)

**Status:** draft · **Authority:** test-lane README · **Implementation depth:** README present; individual test files and runner wiring **NEEDS VERIFICATION** · **Default execution tier:** deterministic, no-network.

> [!IMPORTANT]
> Atmosphere is **not** an emergency alerting system. Tests in this folder must preserve that boundary: advisory and smoke context can be carried as evidence-labeled context, but KFM must not become the official life-safety authority.

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Status and evidence boundary](#3-status-and-evidence-boundary)
4. [What belongs here](#4-what-belongs-here)
5. [What does not belong here](#5-what-does-not-belong-here)
6. [Knowledge-character test matrix](#6-knowledge-character-test-matrix)
7. [Fixture contract](#7-fixture-contract)
8. [Expected validator behavior](#8-expected-validator-behavior)
9. [Lifecycle and publication gates](#9-lifecycle-and-publication-gates)
10. [Suggested local commands](#10-suggested-local-commands)
11. [Review burden](#11-review-burden)
12. [Related folders](#12-related-folders)
13. [Open questions](#13-open-questions)
14. [Definition of done](#14-definition-of-done)
15. [Changelog](#15-changelog)
16. [Last reviewed](#16-last-reviewed)

---

## 1. Purpose

This folder is the domain-specific test lane for the Atmosphere / Air **knowledge-character** rule.

Knowledge character answers a narrow but critical question:

> **What kind of knowledge is this Atmosphere record?**

Examples include direct instrument readings, public AQI reports, regulatory archives, low-cost sensor readings, model fields, remote-sensing masks, climate anomaly context, derived fusion products, meteorological context, advisory context, and network/site metadata.

The tests here should prove that:

- every Atmosphere object carries exactly one valid knowledge character once normalized;
- missing or unknown knowledge character fails closed;
- AQI is never treated as concentration;
- AOD is never treated as PM2.5;
- model fields and fusion products are never relabeled as direct observations;
- low-cost sensor data cannot be public without correction, caveats, confidence, and limitations;
- advisory context never becomes official alerting authority;
- re-characterization creates a new identity and correction path, not an in-place mutation.

[Back to top](#top)

---

## 2. Directory fit and authority

`tests/domains/atmosphere/knowledge-character/` exists because this file family's primary responsibility is **enforceability proof**.

| Placement question | Answer |
|---|---|
| Responsibility root | `tests/` — proves rules are enforceable. |
| Domain segment | `domains/atmosphere/` — Atmosphere is a lane inside the responsibility root, not a root folder. |
| Sublane | `knowledge-character/` — focused test set for the Atmosphere epistemic-kind vocabulary and anti-collapse guards. |
| Fixture partner | `fixtures/domains/atmosphere/` for reusable valid and invalid samples. |
| Validator partner | `tools/validators/` for reusable validator logic. |
| Policy partner | `policy/domains/atmosphere/` for deny/restrict/abstain decisions. |

This README documents the test lane. It does **not** define object meaning, schema shape, machine registry values, or release policy. Those belong in the related responsibility roots.

[Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status | Notes |
|---|---|---|
| README file | **CONFIRMED** | This document defines the lane contract. |
| Individual test files | **NEEDS VERIFICATION** | Add or verify test modules in later PRs. |
| Knowledge-character terms | **CONFIRMED doctrine / PROPOSED field realization** | Terms are documented in the Atmosphere lane docs. |
| Machine enum | **OPEN** | Do not freeze exact enum casing here until the ADR/registry settles it. |
| Machine registry home | **OPEN** | `data/registry/` vs `control_plane/` vs schema-adjacent home remains ADR-class. |
| Validator names | **PROPOSED** | Names below are stable test-intent labels, not proof of existing Python/Rego modules. |
| CI wiring | **NEEDS VERIFICATION** | CI must be inspected before claiming enforcement. |

> [!NOTE]
> This README may name proposed test classes and fixtures before those files exist. Treat those names as a to-build checklist unless a mounted repo inspection confirms them.

[Back to top](#top)

---

## 4. What belongs here

Accepted content in this folder:

- test modules for the Atmosphere knowledge-character registry;
- tests that load valid and invalid knowledge-character fixtures;
- tests proving DENY / ABSTAIN behavior for anti-collapse conditions;
- tests that call shared validators under `tools/validators/`;
- tests that check policy decisions from `policy/domains/atmosphere/`;
- tests that verify emitted payloads preserve knowledge character in layer manifests, Evidence Drawer payloads, governed API envelopes, and Focus Mode / AI receipts;
- small test-only helpers local to this folder when they are not reusable validator logic.

[Back to top](#top)

---

## 5. What does not belong here

Do **not** place the following here:

- production validator logic that should live under `tools/validators/`;
- machine-readable registry authority that should live in its ADR-approved registry home;
- JSON Schemas that belong under `schemas/contracts/v1/domains/atmosphere/`;
- object meaning files that belong under `contracts/domains/atmosphere/`;
- policy rules that belong under `policy/domains/atmosphere/`;
- reusable fixtures that belong under `fixtures/domains/atmosphere/`;
- live network calls, credentials, or default tests that depend on current external services;
- emergency guidance, alert issuance, or life-safety instruction logic;
- generated receipts, proofs, release manifests, or rollback cards.

[Back to top](#top)

---

## 6. Knowledge-character test matrix

| Test intent | Positive fixture | Negative fixture | Required outcome |
|---|---|---|---|
| `knowledge-character-registry-tests` | valid object with one recognized character | missing, unknown, or multiple characters | fail closed; promotion blocked |
| `aqi-as-concentration-denial` | AQI report stored as index/report context | AQI value mapped into concentration field | `DENY` publication; AI `ABSTAIN` |
| `aod-as-pm25-denial` | AOD raster labeled as remote-sensing mask | AOD raster exposed as PM2.5 concentration | `DENY` publication; AI `ABSTAIN` |
| `model-as-observed-denial` | model field labeled as model/forecast context | model or fusion product relabeled as direct observation | `DENY` publication; AI `ABSTAIN` |
| `low-cost-sensor-caveat-tests` | low-cost sensor with correction, caveats, confidence, limitations | raw low-cost sensor published without caveat closure | `DENY` until closure |
| `aggregate-not-per-place-denial` | climate anomaly with baseline and aggregate unit | aggregate cited as station/per-place reading | `DENY` or `ABSTAIN` depending surface |
| `derived-fusion-lineage-tests` | fusion product with per-input lineage and uncertainty | fusion product presented as observation | `DENY` publication |
| `advisory-not-alert-denial` | advisory context with official-source redirect | KFM text presented as official alert instruction | `DENY`; redirect to issuing authority |
| `re-characterization-creates-new-identity` | corrected object with new identity and `CorrectionNotice` | in-place character mutation | fail validation |
| `knowledge-character-surface-exposure` | API/UI payload carries character and source role | payload omits character | fail trust-state validation |

[Back to top](#top)

---

## 7. Fixture contract

Reusable fixtures SHOULD live under `fixtures/domains/atmosphere/`, grouped by validity and rule family.

```text
fixtures/domains/atmosphere/
├── valid/
│   └── knowledge-character/
│       ├── observed-sensor.json
│       ├── public-aqi-report.json
│       ├── remote-sensing-mask.json
│       ├── atmospheric-model-field.json
│       └── low-cost-sensor-with-caveats.json
└── invalid/
    └── knowledge-character/
        ├── missing-character.json
        ├── multiple-characters.json
        ├── aqi-as-concentration.json
        ├── aod-as-pm25.json
        ├── model-as-observed.json
        ├── low-cost-without-caveats.json
        └── advisory-as-alert-authority.json
```

Fixture rules:

- default fixtures are deterministic and no-network;
- fixtures use small synthetic or public-safe examples only;
- fixtures must include enough evidence, source-role, time, and release-state fields to test the rule being asserted;
- invalid fixtures should fail for one clear reason whenever practical;
- fixture names should describe the failure mode, not the implementation language.

[Back to top](#top)

---

## 8. Expected validator behavior

The tests in this folder should call validator logic rather than embedding production rules in the test body.

Expected behavior:

1. Load the machine registry from the ADR-approved registry home once that exists.
2. Validate object shape through schemas before applying knowledge-character guards.
3. Check the character against source role, evidence, time, release state, and policy posture.
4. Emit finite outcomes: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` where runtime envelopes are involved.
5. Fail closed for missing character, unknown character, registry unavailability, forbidden collapse, or missing caveat closure.
6. Preserve a correction path when re-characterization is required.

> [!WARNING]
> A test that passes by redefining the knowledge-character enum locally is a parallel-authority defect. Tests may assert expected outcomes, but registry authority must come from the governed registry once it exists.

[Back to top](#top)

---

## 9. Lifecycle and publication gates

Knowledge character must survive the full KFM lifecycle.

| Stage | Test expectation |
|---|---|
| `RAW` | Source role constrains possible character; no public exposure. |
| `WORK / QUARANTINE` | character is assigned or record is held with reason. |
| `PROCESSED` | character is frozen and participates in identity/hash checks. |
| `CATALOG / TRIPLET` | EvidenceBundle and projections carry the character. |
| `PUBLISHED` | LayerManifest, Evidence Drawer, governed API, and Focus Mode expose the character. |
| `CORRECTION` | mis-characterization emits new identity and correction notice. |
| `ROLLBACK` | rollback target restores the prior released state without inventing a new character. |

Promotion must not upgrade a candidate, model, aggregate, or advisory product into an observation.

[Back to top](#top)

---

## 10. Suggested local commands

The exact runner is **NEEDS VERIFICATION**. When wired, expected commands should be documented here.

```bash
# Proposed focused suite
pytest tests/domains/atmosphere/knowledge-character

# Proposed repo-wide validation entry point, if available
python tools/validate_all.py
```

Default expectations:

- no live network calls;
- no source credentials;
- no writes outside temporary test output;
- deterministic fixtures;
- negative cases included beside positive cases.

[Back to top](#top)

---

## 11. Review burden

Changes to this folder should be reviewed by:

- QA/test steward;
- Atmosphere / Air domain steward;
- policy reviewer when DENY / ABSTAIN behavior changes;
- schema or contract reviewer when object shape or object meaning assumptions change;
- release steward when publication, correction, or rollback gates are affected.

Reviewers should ask:

- Does the test prove a KFM trust rule, or only local code behavior?
- Does it avoid redefining schema, policy, or registry authority locally?
- Does every invalid fixture fail for the intended reason?
- Does the public path remain governed API / released artifact only?
- Does the test preserve the non-emergency boundary?

[Back to top](#top)

---

## 12. Related folders

| Folder | Relationship |
|---|---|
| `docs/domains/atmosphere/` | Human-facing domain doctrine and knowledge-character explanation. |
| `contracts/domains/atmosphere/` | Object-family meaning. |
| `schemas/contracts/v1/domains/atmosphere/` | Machine-checkable object shape. |
| `policy/domains/atmosphere/` | Deny / restrict / abstain rules. |
| `fixtures/domains/atmosphere/` | Valid and invalid samples loaded by this suite. |
| `tools/validators/` | Shared validator logic called by this suite. |
| `data/registry/sources/atmosphere/` | Source descriptors and source authority inputs. |
| `data/receipts/` and `data/proofs/` | Cross-domain emitted evidence of runs and proof closure, not test source files. |
| `release/candidates/atmosphere/` | Candidate release decisions affected by these tests. |
| `apps/governed-api/` and `apps/explorer-web/` | Public surfaces that must expose knowledge character rather than infer it. |

[Back to top](#top)

---

## 13. Open questions

| ID | Question | Status | What settles it |
|---|---|---|---|
| ATM-KC-TST-01 | Exact machine enum values and casing. | OPEN | Accepted enum ADR + mounted registry. |
| ATM-KC-TST-02 | Registry home. | OPEN | Placement ADR for machine-readable registry authority. |
| ATM-KC-TST-03 | Exact validator module names. | NEEDS VERIFICATION | Mounted `tools/validators/` inspection. |
| ATM-KC-TST-04 | Exact CI job name. | NEEDS VERIFICATION | Mounted `.github/workflows/` inspection. |
| ATM-KC-TST-05 | Whether `SmokeContext` is shared or projected between Atmosphere and Hazards. | OPEN | Cross-lane join policy ADR. |
| ATM-KC-TST-06 | Radar-derived precipitation character. | OPEN | Atmosphere contract or ADR. |

[Back to top](#top)

---

## 14. Definition of done

This folder is done enough for a first enforceability slice when:

- this README is present and linked from the Atmosphere docs or test index;
- reusable fixtures exist under `fixtures/domains/atmosphere/{valid,invalid}/knowledge-character/`;
- focused tests cover every row in the test matrix;
- tests call shared validators instead of redefining registry authority;
- negative tests prove DENY / ABSTAIN behavior;
- CI or the repo validation entry point runs the focused suite;
- documentation links to the accepted enum and registry-home ADRs once they exist;
- reviewers can trace each test back to a contract, schema, policy, fixture, or doctrine source.

[Back to top](#top)

---

## 15. Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-05 | Created README for the Atmosphere knowledge-character test sublane. | draft |

---

## 16. Last reviewed

2026-07-05
