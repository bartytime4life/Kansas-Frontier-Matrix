<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/atmosphere/object-family-map
title: Atmosphere/Air — Object Family Map
type: standard
version: v1
status: draft
owners: TODO-atmosphere-domain-steward, TODO-docs-steward
created: 2026-05-29
updated: 2026-05-29
policy_label: public
contract_version: 3.0.0
related:
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/UBIQUITOUS_LANGUAGE.md
  - docs/domains/atmosphere/SOURCE_FAMILIES.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md
  - contracts/OBJECT_MAP.md
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - docs/doctrine/directory-rules.md
  - ai-build-operating-contract.md
tags: [kfm, atmosphere, air, object-family, identity, temporal, knowledge-character]
notes:
  - CONTRACT_VERSION 3.0.0 pinned; doctrine-adjacent map.
  - Object roster is CONFIRMED from Atlas 11.B owns-list; field realization is PROPOSED.
  - No mounted repo this session; every contract/schema path is PROPOSED.
  - Meta Block v2 carries no nested HTML comments; inline annotation uses # only.
[/KFM_META_BLOCK_V2] -->

# Atmosphere/Air — Object Family Map

> Canonical per-object reference for the Atmosphere/Air domain: the 15 object families the domain owns, their knowledge character, identity rule, temporal handling, sensitivity hooks, and crosswalk to contracts and schemas.

[![Status: Draft](https://img.shields.io/badge/status-draft-orange)](#)
[![Domain: Atmosphere / Air](https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff)](./README.md)
[![Objects: 15 owned](https://img.shields.io/badge/objects-15_owned-1f883d)](#3-object-family-roster)
[![Truth posture: roster CONFIRMED · realization PROPOSED](https://img.shields.io/badge/truth-roster_CONFIRMED%20%C2%B7%20realization_PROPOSED-yellow)](#2-truth-posture-and-evidence-basis)
[![CONTRACT_VERSION: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blue)](#)
[![Last Reviewed: 2026-05-29](https://img.shields.io/badge/last_reviewed-2026--05--29-informational)](#footer)

> **Status:** draft · **Owners:** TODO-atmosphere-domain-steward · TODO-docs-steward · **Updated:** 2026-05-29 · **CONTRACT_VERSION = "3.0.0"**

---

## Table of Contents

- [1. Scope and Purpose](#1-scope-and-purpose)
- [2. Truth Posture and Evidence Basis](#2-truth-posture-and-evidence-basis)
- [3. Object Family Roster](#3-object-family-roster)
- [4. Knowledge-Character Binding](#4-knowledge-character-binding)
- [5. Identity and Temporal Discipline](#5-identity-and-temporal-discipline)
- [6. Per-Object Detail](#6-per-object-detail)
  - [6.1 Network and site context](#61-network-and-site-context)
  - [6.2 Air-quality observations](#62-air-quality-observations)
  - [6.3 Remote-sensing and smoke](#63-remote-sensing-and-smoke)
  - [6.4 Weather observations](#64-weather-observations)
  - [6.5 Climate context](#65-climate-context)
  - [6.6 Model and advisory context](#66-model-and-advisory-context)
- [7. Object Relationships (Diagram)](#7-object-relationships-diagram)
- [8. Cross-Lane Ownership Boundaries](#8-cross-lane-ownership-boundaries)
- [9. Contract and Schema Crosswalk](#9-contract-and-schema-crosswalk)
- [10. Anti-Collapse Rules](#10-anti-collapse-rules)
- [Open questions register](#open-questions-register)
- [Open verification backlog](#open-verification-backlog)
- [Changelog](#changelog)
- [Definition of done](#definition-of-done)
- [Related Docs](#related-docs)
- [Footer](#footer)

---

## 1. Scope and Purpose

This map is the single per-object reference for Atmosphere/Air. It exists so that contracts, schemas, validators, and the Evidence Drawer all draw object definitions from one place rather than re-deriving them.

**This map covers** the 15 object families the Atmosphere/Air domain owns, each mapped where possible to a knowledge-character vocabulary term, an identity rule, temporal handling, sensitivity hooks, and the contract/schema files that will realize it.

**This map does not cover** object-family *shape* (that lives in `schemas/contracts/v1/domains/atmosphere/`), object *meaning* prose (that lives in `contracts/domains/atmosphere/`), or source rights and cadence (that lives in `docs/domains/atmosphere/SOURCE_FAMILIES.md` and `data/registry/sources/atmosphere/`). It crosswalks to all three.

> [!NOTE]
> This is a doctrine-adjacent reference, not a creation order. Every contract/schema path named here is **PROPOSED** until verified against a mounted repository. The object roster itself is **CONFIRMED** from Atlas §11.B.

[Back to top](#table-of-contents)

---

## 2. Truth Posture and Evidence Basis

> [!IMPORTANT]
> **Roster is CONFIRMED; field realization is PROPOSED.** The 15-object owns-list is CONFIRMED doctrine from the Atlas §11.B scope statement. The identity rule (`source_id + object_role + temporal_scope + normalized_digest`) is labeled **PROPOSED deterministic basis** in the Atlas. The six-time temporal-distinctness rule is **CONFIRMED**. No mounted repository was inspected this session, so all `contracts/` and `schemas/` paths are PROPOSED.

Evidence used to build this map, all CONFIRMED in indexed project knowledge:

- **Atlas §11.B (scope & ownership)** — the authoritative 15-object owns-list. **[CONFIRMED]**
- **Atlas §11.C (ubiquitous language)** — knowledge-character vocabulary terms. **[CONFIRMED term / PROPOSED field realization]**
- **Atlas §11.E (main object families)** — identity rule and temporal handling. **[PROPOSED identity / CONFIRMED temporal]**
- **Atlas §11.F (cross-lane relations)** and **§11.B (Hazards)** — cross-lane and SmokeContext deconfliction. **[CONFIRMED]**
- **Atlas §11.I (sensitivity & publication posture)** — AQI≠concentration, AOD≠PM2.5, model≠observation, low-cost-sensor caveats. **[CONFIRMED / PROPOSED]**
- **`ai-build-operating-contract.md` v3.0** — truth labels, invariants. **[CONFIRMED — CONTRACT_VERSION 3.0.0]**

> [!CAUTION]
> **Source discrepancy surfaced.** The Atlas §11.B owns-list enumerates **15** objects (through `Advisory Context`). The Atlas §11.E *detail table* and Appendix C *object-family spine* truncate the enumeration at `Precipitation Observation` / `Climate Normal` respectively, omitting `Temperature Observation`, `Climate Anomaly`, `Forecast Context`, and `Advisory Context` from those two surfaces. This map treats the **§11.B owns-list as canonical** (it is the explicit ownership statement) and flags the truncation as a verification item (OQ-AIROBJ-01). Do not infer the missing four are unowned.

[Back to top](#table-of-contents)

---

## 3. Object Family Roster

The 15 objects the Atmosphere/Air domain owns, per Atlas §11.B. **[CONFIRMED roster / PROPOSED implementation]**

| # | Object family | Knowledge character (primary) | Group |
|---|---|---|---|
| 1 | AirStation | `NETWORK_AND_SITE_CONTEXT` | Network & site |
| 2 | AirObservation | `OBSERVED_SENSOR` | Air quality |
| 3 | PM2.5 Observation | `OBSERVED_SENSOR` / `PUBLIC_AQI_REPORT` (role-dependent) | Air quality |
| 4 | Ozone Observation | `OBSERVED_SENSOR` / `PUBLIC_AQI_REPORT` (role-dependent) | Air quality |
| 5 | SmokeContext | `REMOTE_SENSING_MASK` / `ATMOSPHERIC_MODEL_FIELD` (source-dependent) | Remote-sensing & smoke |
| 6 | AODRaster | `REMOTE_SENSING_MASK` | Remote-sensing & smoke |
| 7 | Weather Station | `NETWORK_AND_SITE_CONTEXT` | Weather |
| 8 | Weather Observation | `OBSERVED_SENSOR` / `METEOROLOGICAL_CONTEXT` | Weather |
| 9 | WindField | `OBSERVED_SENSOR` / `ATMOSPHERIC_MODEL_FIELD` (role-dependent) | Weather |
| 10 | Precipitation Observation | `OBSERVED_SENSOR` / `METEOROLOGICAL_CONTEXT` | Weather |
| 11 | Temperature Observation | `OBSERVED_SENSOR` / `METEOROLOGICAL_CONTEXT` | Weather |
| 12 | Climate Normal | `CLIMATE_ANOMALY_CONTEXT` (baseline) | Climate |
| 13 | Climate Anomaly | `CLIMATE_ANOMALY_CONTEXT` | Climate |
| 14 | Forecast Context | `ATMOSPHERIC_MODEL_FIELD` | Model & advisory |
| 15 | Advisory Context | `ALERT_AND_ADVISORY_CONTEXT` | Model & advisory |

> [!NOTE]
> Knowledge-character assignments are **INFERRED** mappings from Atlas §11.C vocabulary onto the §11.B objects; the Atlas does not publish a one-to-one object→character table. Several objects carry a role-dependent character (e.g., a PM2.5 value may be `OBSERVED_SENSOR` from a regulatory monitor or `PUBLIC_AQI_REPORT` from an agency feed). The frozen one-to-one binding is an ADR item (see OQ-AIROBJ-02 and `ADR-XXXX-atmosphere-knowledge-character-vocabulary`).

[Back to top](#table-of-contents)

---

## 4. Knowledge-Character Binding

Knowledge character is the anti-collapse spine: it constrains what an object's value may be presented as. The vocabulary is CONFIRMED in Atlas §11.C; the per-object binding below is INFERRED.

| Knowledge character | Meaning (constrained by source role, evidence, time, release state) | Objects bound | Collapse it prevents |
|---|---|---|---|
| `OBSERVED_SENSOR` | A direct sensor reading. | AirObservation, PM2.5, Ozone, Weather Observation, WindField (obs role), Precipitation, Temperature | model presented as observation |
| `PUBLIC_AQI_REPORT` | An agency-issued index report, not a raw concentration. | PM2.5, Ozone (report role) | AQI presented as concentration |
| `REGULATORY_ARCHIVE` | An archived regulatory measurement of record. | PM2.5, Ozone (archive role) | archive vintage presented as live |
| `LOW_COST_SENSOR` | A low-cost sensor reading requiring caveats. | AirObservation, PM2.5 (low-cost role) | uncalibrated value presented as reference-grade |
| `ATMOSPHERIC_MODEL_FIELD` | A modeled field, never an observation. | Forecast Context, SmokeContext (forecast role), WindField (model role) | model presented as observation |
| `REMOTE_SENSING_MASK` | A satellite-derived mask/proxy, not a ground measurement. | AODRaster, SmokeContext (analysis role) | AOD presented as PM2.5 |
| `CLIMATE_ANOMALY_CONTEXT` | A baseline-relative climate statement. | Climate Normal, Climate Anomaly | anomaly presented as observation |
| `METEOROLOGICAL_CONTEXT` | Supporting weather context. | Weather Observation, Precipitation, Temperature (context role) | context presented as primary claim |
| `ALERT_AND_ADVISORY_CONTEXT` | Referral context, **not** a life-safety instruction. | Advisory Context | advisory presented as life-safety directive |
| `NETWORK_AND_SITE_CONTEXT` | Station/network metadata, including siting. | AirStation, Weather Station | site coordinates exposed without generalization |

[Back to top](#table-of-contents)

---

## 5. Identity and Temporal Discipline

**Identity rule (all objects).** PROPOSED deterministic basis per Atlas §11.E:

```text
identity = source_id + object_role + temporal_scope + normalized_digest
```

> [!NOTE]
> `object_role` carries the knowledge character into identity, so the same physical reading admitted under two roles (e.g., observation vs. report) yields two distinct identities — by design. This is **PROPOSED** until a schema fixes the digest algorithm (BLAKE3 vs SHA-256 is a repo-wide decision).

**Temporal discipline (all objects).** CONFIRMED per Atlas §11.E: the six times stay distinct where material and MUST NOT collapse:

| Time field | Meaning |
|---|---|
| `source_time` | When the source asserts the value pertains. |
| `observed_time` | When the phenomenon was measured. |
| `valid_time` | The interval over which the value is valid. |
| `retrieval_time` | When KFM fetched the value. |
| `release_time` | When KFM published the derivative. |
| `correction_time` | When a correction was issued, if any. |

A validator MUST reject any object that collapses two of these into one field where they are materially distinct (`test_temporal_fields_distinct`).

[Back to top](#table-of-contents)

---

## 6. Per-Object Detail

All identity rows are **PROPOSED**; all temporal rows are **CONFIRMED** (Atlas §11.E). Sensitivity hooks are PROPOSED bindings to `policy/domains/atmosphere/`.

### 6.1 Network and site context

| Object | Purpose | Sensitivity hook |
|---|---|---|
| **AirStation** | A monitoring station/network site that air observations attach to. | Exact siting is `NETWORK_AND_SITE_CONTEXT`; generalize coordinates before public release. |
| **Weather Station** | A meteorological station/network site. | Same siting caveat as AirStation. |

### 6.2 Air-quality observations

| Object | Purpose | Sensitivity hook |
|---|---|---|
| **AirObservation** | A general air-quality observation tied to an AirStation. | Low-cost-sensor caveats required if `LOW_COST_SENSOR` role. |
| **PM2.5 Observation** | A particulate concentration reading. | `aqi_is_not_concentration` denial; canonical units; AQI never aliased. |
| **Ozone Observation** | An ozone concentration reading. | Same AQI/units discipline as PM2.5. |

### 6.3 Remote-sensing and smoke

| Object | Purpose | Sensitivity hook |
|---|---|---|
| **AODRaster** | Aerosol optical depth raster (GOES/ABI). | `aod_is_not_pm25` denial; tag as `REMOTE_SENSING_MASK`. |
| **SmokeContext** | Atmospheric smoke reading — HMS analysis (`REMOTE_SENSING_MASK`) or HRRR-Smoke forecast (`ATMOSPHERIC_MODEL_FIELD`). | Source-role required; **see §8** — Hazards owns its own SmokeContext for event/impact. |

### 6.4 Weather observations

| Object | Purpose | Sensitivity hook |
|---|---|---|
| **Weather Observation** | A general meteorological observation. | Context vs primary-claim role must be tagged. |
| **WindField** | Wind speed/direction field — observed or modeled. | `model_is_not_observation` denial when model role. |
| **Precipitation Observation** | A precipitation reading. | Canonical units. |
| **Temperature Observation** | A temperature reading. | Canonical units. |

### 6.5 Climate context

| Object | Purpose | Sensitivity hook |
|---|---|---|
| **Climate Normal** | A reference-period baseline (e.g., 30-year normal). | Reference period required; baseline, not observation. |
| **Climate Anomaly** | A deviation from a Climate Normal. | MUST anchor to a Climate Normal; `CLIMATE_ANOMALY_CONTEXT`. |

### 6.6 Model and advisory context

| Object | Purpose | Sensitivity hook |
|---|---|---|
| **Forecast Context** | A modeled atmospheric field used as context. | `model_is_not_observation` denial; never an observation. |
| **Advisory Context** | A referral to an authoritative advisory. | `advisory_no_life_safety` denial — referral only; redirect to source. |

[Back to top](#table-of-contents)

---

## 7. Object Relationships (Diagram)

```mermaid
flowchart TB
  subgraph SITE["Network & site (NETWORK_AND_SITE_CONTEXT)"]
    AS["AirStation"]:::site
    WS["Weather Station"]:::site
  end

  subgraph AQ["Air quality"]
    AO["AirObservation"]:::obs
    PM["PM2.5 Observation"]:::obs
    OZ["Ozone Observation"]:::obs
  end

  subgraph WX["Weather"]
    WO["Weather Observation"]:::obs
    WF["WindField"]:::mixed
    PR["Precipitation Observation"]:::obs
    TM["Temperature Observation"]:::obs
  end

  subgraph RS["Remote-sensing & smoke"]
    AOD["AODRaster (mask)"]:::mask
    SC["SmokeContext (mask / model)"]:::mixed
  end

  subgraph CL["Climate"]
    CN["Climate Normal (baseline)"]:::clim
    CA["Climate Anomaly"]:::clim
  end

  subgraph MA["Model & advisory"]
    FC["Forecast Context (model)"]:::model
    AC["Advisory Context (referral)"]:::adv
  end

  AS --> AO --> PM
  AS --> OZ
  WS --> WO --> PR
  WS --> TM
  WS --> WF
  CN --> CA
  AO -. context .-> SC
  AOD -. proxy, NOT PM2.5 .-> PM

  classDef site fill:#e8f1ff,stroke:#1f6feb,color:#0b3a8a;
  classDef obs fill:#e8f8ec,stroke:#1f883d,color:#0b4a1f;
  classDef mask fill:#e7f6f8,stroke:#0e7490,color:#06424c;
  classDef model fill:#eee8ff,stroke:#5e35b1,color:#2a1a5e;
  classDef mixed fill:#fff8c4,stroke:#a07e00,color:#5a4500;
  classDef clim fill:#fff5e6,stroke:#b45f06,color:#7a3e00;
  classDef adv fill:#fde6e6,stroke:#b42318,color:#7a0e0e;
```

> [!NOTE]
> **Diagram status:** the grouping and knowledge-character coloring are INFERRED from Atlas §11.B/§11.C; the dashed "proxy, NOT PM2.5" edge encodes the §11.I anti-collapse rule. Relationship cardinalities are PROPOSED and NEEDS VERIFICATION against schemas.

[Back to top](#table-of-contents)

---

## 8. Cross-Lane Ownership Boundaries

Per Atlas §11.B, Atmosphere/Air **does not own** emergency/hazard event truth or life-safety context — that is the **Hazards** lane. Per Atlas §11.F, relations to other lanes must preserve ownership, source role, sensitivity, and EvidenceBundle support. **[CONFIRMED]**

| Object | Related lane | Boundary |
|---|---|---|
| **SmokeContext** | Hazards (also owns a `SmokeContext`) | Atmosphere/Air owns the **atmospheric reading** (mask/model); Hazards owns the **event/impact projection** of the same phenomenon. Same name in both lanes per Atlas §11.B and §12.B/§12.E. Deconfliction is an open ADR. |
| **Advisory Context** | Hazards (Warning/Advisory Context) | Atmosphere/Air `Advisory Context` is **referral-only**, never life-safety. Life-safety belongs to Hazards, which itself is "not an emergency alert system." |
| **Precipitation / Temperature / WindField** | Agriculture, Hydrology | Heat, precipitation, drought, flood-weather forcing context — relation, not re-ownership of canonical claims. |
| **SmokeContext / AODRaster / Forecast Context** | Biodiversity domains | Phenology, smoke, fire, drought stress context **without exposing sensitive locations**. |

> [!CAUTION]
> The `SmokeContext` name collision is a live ADR item (`ADR-XXXX-atmosphere-hazards-smokecontext-ownership`). Until resolved, neither lane's `SmokeContext` schema is canonical for the other; do not merge them.

[Back to top](#table-of-contents)

---

## 9. Contract and Schema Crosswalk

PROPOSED file homes per Directory Rules Domain Placement Law (`<root>/domains/atmosphere/...`). All **PROPOSED**; `schemas/contracts/v1/...` is the default schema home per ADR-0001 (NEEDS VERIFICATION of repo presence).

<details>
<summary><strong>Click to expand: object → contract → schema crosswalk (15 objects)</strong></summary>

| Object | Contract (`contracts/domains/atmosphere/`) | Schema (`schemas/contracts/v1/domains/atmosphere/`) |
|---|---|---|
| AirStation | `AirStation.md` | `air_station.schema.json` |
| AirObservation | `AirObservation.md` | `air_observation.schema.json` |
| PM2.5 Observation | `PM25Observation.md` | `pm25_observation.schema.json` |
| Ozone Observation | `OzoneObservation.md` | `ozone_observation.schema.json` |
| SmokeContext | `SmokeContext.md` | `smoke_context.schema.json` |
| AODRaster | `AODRaster.md` | `aod_raster.schema.json` |
| Weather Station | `WeatherStation.md` | `weather_station.schema.json` |
| Weather Observation | `WeatherObservation.md` | `weather_observation.schema.json` |
| WindField | `WindField.md` | `wind_field.schema.json` |
| Precipitation Observation | `PrecipitationObservation.md` | `precipitation_observation.schema.json` |
| Temperature Observation | `TemperatureObservation.md` | `temperature_observation.schema.json` |
| Climate Normal | `ClimateNormal.md` | `climate_normal.schema.json` |
| Climate Anomaly | `ClimateAnomaly.md` | `climate_anomaly.schema.json` |
| Forecast Context | `ForecastContext.md` | `forecast_context.schema.json` |
| Advisory Context | `AdvisoryContext.md` | `advisory_context.schema.json` |
| *(cross-cutting)* | — | `knowledge_character.schema.json`, `parameter_registry.schema.json` |

</details>

> [!NOTE]
> `contracts/` owns object **meaning**; `schemas/` owns machine **shape**. Both are required; neither replaces the other (Directory Rules §13.1, ADR-0001).

[Back to top](#table-of-contents)

---

## 10. Anti-Collapse Rules

Per Atlas §11.I, these are CONFIRMED doctrine and bind every object in this map:

- **AQI is not concentration** — `PUBLIC_AQI_REPORT` MUST NOT be presented as `OBSERVED_SENSOR` concentration.
- **AOD is not PM2.5** — `REMOTE_SENSING_MASK` (AODRaster) MUST NOT be presented as a PM2.5 measurement.
- **Model is not observation** — `ATMOSPHERIC_MODEL_FIELD` (Forecast Context, WindField model role, SmokeContext forecast role) MUST NOT be presented as `OBSERVED_SENSOR`.
- **Low-cost sensor public release** requires correction, caveats, confidence, and limitations.
- **Advisory is not life-safety** — `ALERT_AND_ADVISORY_CONTEXT` is referral-only; redirect to the authoritative source.
- **Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion** (Atlas §11.I, CONFIRMED).

[Back to top](#table-of-contents)

---

## Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-AIROBJ-01 | Atlas §11.E detail table and Appendix C spine truncate the object list before the §11.B owns-list does. Is the §11.B 15-object roster authoritative? | atmosphere-domain-steward | Confirm against Encyclopedia + ADR; this map assumes §11.B is canonical. |
| OQ-AIROBJ-02 | Freeze the one-to-one object → knowledge-character binding (several objects are role-dependent). | atmosphere-domain-steward | `ADR-XXXX-atmosphere-knowledge-character-vocabulary` |
| OQ-AIROBJ-03 | Resolve SmokeContext ownership split between Atmosphere/Air (reading) and Hazards (event/impact). | atmosphere + hazards stewards | `ADR-XXXX-atmosphere-hazards-smokecontext-ownership` |
| OQ-AIROBJ-04 | Fix the identity-digest algorithm (BLAKE3 vs SHA-256) and `normalized_digest` definition. | docs-steward + domain stewards | Repo-wide ADR + schema decision |
| OQ-AIROBJ-05 | Do any of these contract/schema files already exist in the mounted repo? Classify CONFIRMED or DRIFT. | docs-steward | Mounted-repo inspection |

## Open verification backlog

These items remain `NEEDS VERIFICATION` before promotion from `draft` to `published`:

1. Repository mounting and reclassification of every `contracts/` and `schemas/` path in §9.
2. ADR confirming the §11.B 15-object roster over the truncated §11.E / Appendix C surfaces.
3. ADR freezing the knowledge-character vocabulary and object binding.
4. ADR resolving the SmokeContext cross-lane name collision.
5. Confirmation of the identity-digest algorithm.
6. Verification that the anti-collapse denials (§10) are realized as `policy/domains/atmosphere/` rules with negative tests.

## Changelog

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial creation of the Atmosphere/Air Object Family Map | new | Required companion to README/UBIQUITOUS_LANGUAGE; referenced by MISSING_OR_PLANNED_FILES §6.1. |

> **Backward compatibility.** New file; no anchors to preserve.

## Definition of done

This document is done enough to enter the repository when:

- it is placed at `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` per Directory Rules;
- a docs steward and the atmosphere-domain steward review it;
- it is linked from `docs/domains/atmosphere/README.md` and crosswalked from `contracts/OBJECT_MAP.md`;
- it does not conflict with accepted ADRs (and OQ-AIROBJ-01/02/03 are at least filed);
- any conflict with current repo conventions is logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned in the PR (CONTRACT_VERSION `3.0.0`) is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

[Back to top](#table-of-contents)

---

## Related Docs

- `docs/domains/atmosphere/README.md` — domain landing page (TODO if not present).
- `docs/domains/atmosphere/UBIQUITOUS_LANGUAGE.md` — knowledge-character vocabulary (TODO).
- `docs/domains/atmosphere/SOURCE_FAMILIES.md` — source roster (TODO).
- `docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md` — knowledge-character registry (TODO).
- `docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md` — planned-files register.
- `contracts/OBJECT_MAP.md` — cross-domain object map.
- `docs/doctrine/directory-rules.md` — placement law.
- `ai-build-operating-contract.md` — canonical operating contract (CONTRACT_VERSION 3.0.0).

---

## Footer

---

**Related:** [README](./README.md) · [Ubiquitous Language](./UBIQUITOUS_LANGUAGE.md) · [Source Families](./SOURCE_FAMILIES.md) · [Knowledge Characters](./KNOWLEDGE_CHARACTERS.md) · [Planned Files](./MISSING_OR_PLANNED_FILES.md) · [Directory Rules](../../doctrine/directory-rules.md)

**Last updated:** 2026-05-29 · **Version:** v1 · **Status:** draft · **CONTRACT_VERSION = "3.0.0"**

[⤴ Back to top](#table-of-contents)
