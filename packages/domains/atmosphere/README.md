<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-atmosphere-readme
title: Atmosphere Domain Package README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <atmosphere-domain-steward>
  - <schema-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/atmosphere/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/README.md
  - docs/domains/atmosphere/README.md
  - packages/README.md
  - packages/domains/README.md
  - pipelines/domains/atmosphere/README.md
  - pipeline_specs/atmosphere/README.md
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - policy/domains/atmosphere/
  - tests/packages/domains/atmosphere/
  - fixtures/packages/domains/atmosphere/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, atmosphere, air, weather, climate, smoke, aod, air-quality, mapping-helpers, observation-parsers, adapters, governance]
notes:
  - "This README expands the short packages/domains/atmosphere scaffold into a governed domain-helper package contract."
  - "packages/domains/atmosphere/ may contain reusable Atmosphere helper code only; it is not Atmosphere doctrine, schema authority, contract authority, policy authority, lifecycle data, executable pipeline logic, evidence closure, or release approval."
  - "Atmosphere is evidence-labeled context, not emergency advice or life-safety direction; official advisories must redirect to the issuing authority and Hazards lane where applicable."
  - "Atmosphere helpers must preserve observation/model/source-role distinctions: AQI is not concentration, AOD is not PM2.5, model fields are not observations, and low-cost sensor output needs caveats before public release."
  - "Concrete modules, language runtime, package manifests, exports, build scripts, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Domain Package

> Shared helper-code lane for the Atmosphere / Air / Climate domain: mapping helpers, observation parsers, station and parameter normalizers, weather/smoke/AOD/climate DTO adapters, model-context helpers, caveat preservation, and fixture utilities. This package supports governed apps, pipelines, workers, tests, and tools, but it does not define Atmosphere truth, own schemas/contracts/policy, write lifecycle data, close EvidenceBundles, issue alerts, or approve public release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Fatmosphere%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20code-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Fatmosphere%2F-d62728)
![alert](https://img.shields.io/badge/not%20life--safety%20alert-d62728)

**Status:** Draft  
**Path:** `packages/domains/atmosphere/README.md`  
**Parent package root:** `packages/domains/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/atmosphere/`  
**Executable domain-pipeline root:** `pipelines/domains/atmosphere/`  
**Declarative pipeline-spec root:** `pipeline_specs/atmosphere/`  
**Contract/schema/policy roots:** `contracts/domains/atmosphere/`, `schemas/contracts/v1/domains/atmosphere/`, and `policy/domains/atmosphere/`  
**Placement posture:** helper code only. Runtime, exports, package manifest, child modules, and active tests are `NEEDS VERIFICATION` until verified by repo evidence.  
**Slug posture:** `atmosphere` is used here under Directory Rules lane form; `air` slug drift remains `NEEDS VERIFICATION / ADR` where referenced by older crosswalks.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Atmosphere boundary](#3-atmosphere-boundary)
- [4. Package anti-collapse rules](#4-package-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Expected helper families](#7-expected-helper-families)
- [8. Inputs and outputs](#8-inputs-and-outputs)
- [9. Minimal package contract shape](#9-minimal-package-contract-shape)
- [10. Tests and fixtures](#10-tests-and-fixtures)
- [11. Definition of done](#11-definition-of-done)
- [12. Open questions](#12-open-questions)

---

## 1. Purpose

`packages/domains/atmosphere/` may contain reusable Atmosphere helper code that supports KFM domain processing without becoming an authority root.

It may support:

- air-quality station, parameter, unit, and observation mapping helpers;
- AQI report-context helpers that do not treat AQI as concentration;
- smoke, aerosol, and AOD DTO adapters that preserve caveats;
- weather and mesonet station/observation helpers;
- wind, precipitation, temperature, climate-normal, and climate-anomaly adapters;
- forecast/model/advisory context helpers that preserve source role and official-source redirection;
- low-cost sensor caveat, confidence, correction, and limitation helper fields;
- source role, source time, valid time, limitation, caveat, and access-state preservation helpers;
- schema-bound validation adapters that call canonical schema tooling;
- no-network fixture builders for tests.

It does **not** define Atmosphere objects, issue emergency alerts, assert life-safety guidance, decide advisory truth, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/domains/atmosphere/`? | Atmosphere helper code belongs under the packages root when reusable across apps, pipelines, workers, and tests. | CONFIRMED root pattern / NEEDS VERIFICATION for implementation |
| Is this Atmosphere doctrine? | No. Atmosphere doctrine and scope belong under `docs/domains/atmosphere/`. | CONFIRMED boundary posture |
| Is this executable pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/atmosphere/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, emergency state, or release? | No. It may preserve refs, caveats, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> Atmosphere helper code can normalize, map, and translate. It cannot turn helper output into observation truth, emergency advice, policy approval, EvidenceBundle closure, or release approval.

[⬆ Back to top](#top)

---

## 3. Atmosphere boundary

Atmosphere is a context and observation domain, not a life-safety system. Helper code must preserve these boundaries:

- emergency and hazard event truth belongs to Hazards and official issuing authorities;
- NWS or agency advisory context must carry official-source redirection and must not become KFM advice;
- AQI report context is not pollutant concentration;
- AOD is not PM2.5;
- model fields and forecasts are not observations;
- low-cost sensor data requires correction, caveats, confidence, and limitations before public release;
- smoke, heat, drought, and advisory context may support other domains but cannot overwrite their canonical claims;
- public release requires evidence, policy, review, ReleaseManifest, correction path, and rollback posture outside this package.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
atmosphere helper -> Atmosphere doctrine
AQI helper -> pollutant concentration truth
AOD helper -> PM2.5 truth
model field -> observation
forecast helper -> official forecast authority
advisory context helper -> emergency advice
low-cost sensor parser -> public release approval
validation helper -> validation pass
successful package test -> lifecycle promotion
```

Required separations:

- helper code stays under `packages/domains/atmosphere/`;
- Atmosphere doctrine stays under `docs/domains/atmosphere/`;
- Atmosphere meaning stays under `contracts/domains/atmosphere/`;
- Atmosphere schemas stay under `schemas/contracts/v1/domains/atmosphere/` unless an ADR resolves slug drift differently;
- Atmosphere policy stays under `policy/domains/atmosphere/` and accepted policy roots;
- executable transformations stay under `pipelines/domains/atmosphere/`;
- declarative run profiles stay under `pipeline_specs/atmosphere/`;
- lifecycle records and receipts stay under `data/`;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`;
- emergency and life-safety authority stays with official issuing authorities and the Hazards lane.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate source files include:

- air-station and weather-station normalization helpers;
- pollutant parameter, unit, and observation mapping helpers;
- AQI context helpers with explicit caveats;
- smoke, plume, AOD, and aerosol adapter helpers;
- weather, wind, precipitation, temperature, climate-normal, and climate-anomaly DTO adapters;
- forecast/model/advisory context adapters that preserve source role and official-source redirection;
- low-cost sensor caveat/confidence helper utilities;
- crosswalk helpers that preserve native classifications and source roles;
- schema-generated adapters with generation provenance;
- safe fixture builders and mock helpers for package tests;
- compatibility helpers for Atmosphere helper migrations.

A good placement test:

> If the file is reusable Atmosphere helper code and does not decide observation truth, issue emergency guidance, write lifecycle data, decide policy, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Atmosphere doctrine and source scope docs | `docs/domains/atmosphere/` |
| Atmosphere object contracts | `contracts/domains/atmosphere/` or ADR-approved equivalent |
| Atmosphere schemas | `schemas/contracts/v1/domains/atmosphere/` or ADR-approved equivalent |
| Atmosphere policy decisions/rules | `policy/domains/atmosphere/` and accepted policy roots |
| Executable Atmosphere pipelines | `pipelines/domains/atmosphere/` |
| Declarative Atmosphere specs | `pipeline_specs/atmosphere/` |
| Source descriptors | `data/registry/sources/atmosphere/` |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Runtime receipts | `data/receipts/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Emergency advisories/life-safety direction | official issuing authority and Hazards lane |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| UI-only rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/atmosphere/` |
| Package fixtures | `fixtures/packages/domains/atmosphere/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 7. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `air_quality` | Air-quality station, parameter, unit, and observation helpers. | PROPOSED |
| `aqi` | AQI report-context helpers, not concentration truth. | PROPOSED |
| `smoke` | Smoke plume and smoke-context adapter helpers. | PROPOSED |
| `aod` | AOD/aerosol adapter helpers with PM2.5 caveats. | PROPOSED |
| `weather` | Weather/mesonet observation adapters. | PROPOSED |
| `climate` | Climate normal, anomaly, and departure helpers. | PROPOSED |
| `forecast` | Forecast/model/advisory context helpers, not official advice. | PROPOSED |
| `sensors` | Low-cost sensor caveat/correction/confidence helpers. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Package-only fixture builders, if accepted by package convention. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/atmosphere/` | Shared helper source only. |
| Domain doctrine | `docs/domains/atmosphere/` | Scope and human-facing control plane. |
| Domain contracts | `contracts/domains/atmosphere/` | Object meaning authority unless ADR says otherwise. |
| Domain schemas | `schemas/contracts/v1/domains/atmosphere/` | Machine shape authority unless ADR says otherwise. |
| Domain policy | `policy/domains/atmosphere/` | Admissibility/exposure authority. |
| Executable domain pipeline | `pipelines/domains/atmosphere/` | Runs transformations. |
| Declarative domain spec | `pipeline_specs/atmosphere/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/atmosphere/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/atmosphere/` | Package validation. |
| Fixtures | `fixtures/packages/domains/atmosphere/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.atmosphere
status: draft
authority: shared_domain_helper_package
slug: atmosphere
slug_conflict:
  observed_alias: air
  status: NEEDS_VERIFICATION_OR_ADR
not_authority_for:
  - atmosphere_doctrine
  - emergency_advisory
  - life_safety_guidance
  - observation_truth
  - object_contract
  - schema_home
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - air quality mapping helpers
  - AQI context helpers
  - smoke and AOD adapters
  - weather and climate adapters
  - forecast and advisory context helpers
  - low cost sensor caveat helpers
  - schema-bound adapters
  - safe fixture builders
required_invariants:
  no_emergency_advice: true
  no_aqi_as_concentration: true
  no_aod_as_pm25: true
  no_model_field_as_observation: true
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  helper_output_is_not_truth: true
```

[⬆ Back to top](#top)

---

## 10. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/atmosphere/
├── test_package_boundaries.py              # PROPOSED
├── test_aqi_not_concentration.py           # PROPOSED
├── test_aod_not_pm25.py                    # PROPOSED
├── test_model_field_not_observation.py     # PROPOSED
├── test_advisory_context_not_advice.py     # PROPOSED
├── test_low_cost_sensor_caveats.py         # PROPOSED
├── test_no_hidden_lifecycle_writes.py      # PROPOSED
├── test_no_policy_or_release_decisions.py  # PROPOSED
├── test_generated_types_match_schema.py    # PROPOSED
└── test_slug_conflict_guard.py             # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/atmosphere/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and should not be presented as live air-quality, weather, smoke, climate, advisory, or life-safety information.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- replaces the scaffold `packages/domains/atmosphere/README.md`;
- identifies this path as shared Atmosphere helper-code space;
- preserves docs, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, official-advisory, Hazards, and release roots as separate authorities;
- blocks Atmosphere helpers from becoming doctrine, schema, contract, policy, lifecycle, evidence, release, observation-truth, emergency-advisory, or public-trust authority;
- defines expected helper families, boundary posture, slug conflict posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Atmosphere lifecycle, evidence, policy, advisory, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-ATM-001` | Which language/runtime owns `packages/domains/atmosphere/`? | UNKNOWN |
| `PKG-DOM-ATM-002` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-ATM-003` | Which helper modules are actually exported today? | UNKNOWN |
| `PKG-DOM-ATM-004` | Should child package aliases use `air`, `atmosphere`, or both with compatibility adapters? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-ATM-005` | Which canonical schemas own air-quality, smoke, AOD, weather, climate, forecast, and advisory helper shapes? | NEEDS VERIFICATION |
| `PKG-DOM-ATM-006` | Which CI workflow validates AQI/AOD/model/advisory boundary rules? | UNKNOWN |

---

## Maintainer note

Keep this package helper-focused and subordinate to Atmosphere governance. Do not add Atmosphere doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, emergency advice, release decisions, public API routes, UI behavior, live advisory examples, or generated truth claims here.
