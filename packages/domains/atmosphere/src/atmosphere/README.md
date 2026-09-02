<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-atmosphere-src-atmosphere-readme
title: Atmosphere Domain Package Source Module README
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
path: packages/domains/atmosphere/src/atmosphere/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/atmosphere/README.md
  - docs/domains/atmosphere/README.md
  - pipelines/domains/atmosphere/README.md
  - pipeline_specs/atmosphere/README.md
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - policy/domains/atmosphere/
  - tests/packages/domains/atmosphere/
  - fixtures/packages/domains/atmosphere/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, atmosphere, src, atmosphere-module, shared-library, air-quality, aqi, smoke, aod, weather, climate, forecast, sensors, governance]
notes:
  - "This README fills the empty packages/domains/atmosphere/src/atmosphere README with a governed source-module contract."
  - "packages/domains/atmosphere/src/atmosphere/ may contain internal source code for shared Atmosphere helpers only; it must remain subordinate to packages/domains/atmosphere/."
  - "Atmosphere source-module helpers can normalize, parse, map, preserve refs, and prepare caveat-aware DTOs. They cannot decide observation truth, issue emergency guidance, write lifecycle data, decide policy, create EvidenceBundles, or approve release."
  - "AQI is not concentration, AOD is not PM2.5, model fields are not observations, and advisory context is not official advice."
  - "Concrete language runtime, module exports, build scripts, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Source Module

> Internal source-code module area for the `packages/domains/atmosphere/` shared helper package. This directory may hold reusable Atmosphere helpers, but it must not become Atmosphere doctrine, observation-truth authority, emergency-advisory authority, schema authority, policy engine, lifecycle writer, EvidenceBundle authority, release authority, or public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Fatmosphere%2Fsrc%2Fatmosphere%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20module-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Fatmosphere%2F-d62728)
![alert](https://img.shields.io/badge/not%20life--safety%20alert-d62728)

**Status:** Draft  
**Path:** `packages/domains/atmosphere/src/atmosphere/README.md`  
**Parent package:** `packages/domains/atmosphere/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/atmosphere/`  
**Executable domain-pipeline root:** `pipelines/domains/atmosphere/`  
**Declarative pipeline-spec root:** `pipeline_specs/atmosphere/`  
**Contract/schema/policy roots:** `contracts/domains/atmosphere/`, `schemas/contracts/v1/domains/atmosphere/`, and `policy/domains/atmosphere/`  
**Placement posture:** source code for reusable Atmosphere helpers only. Runtime, exports, package manifest, and active tests are `NEEDS VERIFICATION` until checked by current repo evidence.  
**Slug posture:** `atmosphere` is used here under Directory Rules lane form; `air` slug drift remains `NEEDS VERIFICATION / ADR` where referenced by older crosswalks.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Atmosphere boundary](#3-atmosphere-boundary)
- [4. Module anti-collapse rules](#4-module-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Expected module families](#7-expected-module-families)
- [8. Inputs and outputs](#8-inputs-and-outputs)
- [9. Minimal module contract shape](#9-minimal-module-contract-shape)
- [10. Tests and fixtures](#10-tests-and-fixtures)
- [11. Definition of done](#11-definition-of-done)
- [12. Open questions](#12-open-questions)

---

## 1. Purpose

`packages/domains/atmosphere/src/atmosphere/` may hold internal source modules for the shared Atmosphere helper package.

It may support reusable helpers for:

- air-quality station, parameter, unit, and observation mapping;
- AQI report-context mapping that does not treat AQI as pollutant concentration;
- smoke, plume, aerosol, and AOD adapters that preserve caveats;
- weather and mesonet station/observation adapters;
- wind, precipitation, temperature, climate-normal, climate-anomaly, and departure helpers;
- forecast, model-field, and advisory-context DTO adapters that preserve source role and official-source redirection;
- low-cost sensor caveat, correction, confidence, and limitation helper fields;
- source role, source time, valid time, limitation, caveat, access state, and release-ref preservation helpers;
- schema-bound validation adapters and safe errors;
- no-network fixture builders for package tests.

It does **not** define Atmosphere objects, decide observation truth, issue emergency alerts, assert life-safety guidance, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/atmosphere/`? | Parent package is the shared Atmosphere helper-code lane. | CONFIRMED parent package contract |
| Why `src/atmosphere/`? | This is a plausible internal module path for Atmosphere-specific helper source. | PROPOSED / NEEDS VERIFICATION |
| Is this Atmosphere doctrine? | No. Atmosphere doctrine and scope belong under `docs/domains/atmosphere/`. | CONFIRMED boundary posture |
| Is this executable Atmosphere pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/atmosphere/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, emergency state, or release? | No. It may preserve refs, caveats, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> Source modules here can normalize, parse, map, and prepare caveat-aware payloads. They cannot turn helper output into observation truth, emergency advice, policy approval, EvidenceBundle closure, or release approval.

[⬆ Back to top](#top)

---

## 3. Atmosphere boundary

Atmosphere helper code must preserve these domain boundaries:

- emergency and hazard event truth belongs to Hazards and official issuing authorities;
- NWS or agency advisory context must carry official-source redirection and must not become KFM advice;
- AQI report context is not pollutant concentration;
- AOD is not PM2.5;
- model fields and forecasts are not observations;
- low-cost sensor data requires correction, caveats, confidence, and limitations before public release;
- smoke, heat, drought, and advisory context may support other domains but cannot overwrite their canonical claims;
- public release requires evidence, policy, review, ReleaseManifest, correction path, and rollback posture outside this module.

[⬆ Back to top](#top)

---

## 4. Module anti-collapse rules

Disallowed collapses:

```text
source module -> Atmosphere doctrine
AQI helper -> pollutant concentration truth
AOD helper -> PM2.5 truth
model field helper -> observation
forecast helper -> official forecast authority
advisory context helper -> emergency advice
sensor parser -> public release approval
validation helper -> validation pass
successful module test -> lifecycle promotion
```

Required separations:

- reusable helper source stays under `packages/domains/atmosphere/src/atmosphere/`;
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

Appropriate source modules include helpers for:

- air-station and weather-station normalization;
- pollutant parameter, unit, and observation mapping;
- AQI context helpers with explicit caveats;
- smoke, plume, AOD, and aerosol adapters;
- weather, wind, precipitation, temperature, climate-normal, and climate-anomaly DTO adapters;
- forecast/model/advisory context adapters that preserve source role and official-source redirection;
- low-cost sensor caveat, correction, confidence, and limitation helpers;
- crosswalk helpers that preserve native classifications and source roles;
- schema-bound validation adapters and safe errors;
- deterministic helper ids when policy and schema allow;
- package-only fixture builders.

A good placement test:

> If the module is reusable Atmosphere helper code and does not decide observation truth, issue emergency guidance, write lifecycle data, decide policy, or approve release, it may belong here.

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
| Tests | `tests/packages/domains/atmosphere/` |
| Fixtures | `fixtures/packages/domains/atmosphere/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 7. Expected module families

| Module family | Responsibility | Status |
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
| Module source | `packages/domains/atmosphere/src/atmosphere/` | Shared helper source only. |
| Package entrypoint | `packages/domains/atmosphere/` | Language-specific entrypoint is not verified. |
| Domain doctrine | `docs/domains/atmosphere/` | Scope and human-facing control plane. |
| Domain contracts | `contracts/domains/atmosphere/` | Object meaning authority unless ADR says otherwise. |
| Domain schemas | `schemas/contracts/v1/domains/atmosphere/` | Machine shape authority unless ADR says otherwise. |
| Domain policy | `policy/domains/atmosphere/` | Admissibility/exposure authority. |
| Executable pipeline | `pipelines/domains/atmosphere/` | Runs transformations. |
| Declarative spec | `pipeline_specs/atmosphere/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/atmosphere/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/atmosphere/` | Package validation. |
| Fixtures | `fixtures/packages/domains/atmosphere/` | No-network synthetic or sanitized fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal module contract shape

```yaml
module_id: kfm.packages.domains.atmosphere.src.atmosphere
status: draft
authority: package_source_module
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
├── test_atmosphere_module_boundaries.py    # PROPOSED
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

- fills the empty `packages/domains/atmosphere/src/atmosphere/README.md` file;
- identifies this directory as package source for shared Atmosphere helpers;
- keeps Atmosphere doctrine, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, official-advisory, Hazards, and release in their own authority roots;
- blocks helper modules from becoming doctrine, observation truth, emergency guidance, policy engine, lifecycle writer, EvidenceBundle creator, release approver, schema authority, contract authority, or public trust membrane;
- defines expected module families, boundary posture, slug conflict posture, inputs/outputs, tests, fixtures, and open questions.

Future source files in this module are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Atmosphere lifecycle, evidence, policy, advisory, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-ATM-SRC-001` | Which language/runtime owns `packages/domains/atmosphere/src/atmosphere/`? | UNKNOWN |
| `PKG-DOM-ATM-SRC-002` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-DOM-ATM-SRC-003` | Should fixture builders live in source, tests, or `fixtures/packages/domains/atmosphere/` only? | NEEDS VERIFICATION |
| `PKG-DOM-ATM-SRC-004` | Which canonical schemas own air-quality, smoke, AOD, weather, climate, forecast, and advisory helper shapes? | NEEDS VERIFICATION |
| `PKG-DOM-ATM-SRC-005` | Which CI workflow validates helper determinism, AQI/AOD/model/advisory boundary rules, and no hidden lifecycle writes? | UNKNOWN |
| `PKG-DOM-ATM-SRC-006` | Should compatibility helpers for the `air` alias live here or in a migration/compatibility package? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this module helper-focused and subordinate to Atmosphere governance. Do not add Atmosphere doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, emergency advice, release decisions, public API routes, UI behavior, live advisory examples, or generated truth claims here.
