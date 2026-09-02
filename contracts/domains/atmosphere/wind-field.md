<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/wind-field-lowercase-compat
title: contracts/domains/atmosphere/wind-field.md — WindField Lowercase Compatibility Pointer
type: contract-compatibility-pointer
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Weather steward · Wind steward · Forecast/model steward · Contract steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; wind-field; compatibility; alias; no-parallel-authority; observed-sensor; atmospheric-model-field
tags: [kfm, contracts, atmosphere, air, wind, wind-field, WindField, observed-sensor, atmospheric-model-field, source-role, model-run, uncertainty, compatibility, alias, camelcase-canonical, governance]
related:
  - ./WindField.md
  - ./WeatherStation.md
  - ./WeatherObservation.md
  - ./TemperatureObservation.md
  - ./PrecipitationObservation.md
  - ./ForecastContext.md
  - ./SmokeContext.md
  - ./ClimateNormal.md
  - ./ClimateAnomaly.md
  - ./AdvisoryContext.md
  - ./AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/WindField.schema.json
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
notes:
  - "This lowercase slug existed as a planned-path scaffold from the Atmosphere file-system plan."
  - "Canonical expanded semantic contract is ./WindField.md."
  - "The paired schema x-kfm.contract_doc points to contracts/domains/atmosphere/WindField.md, not this lowercase compatibility file."
  - "This file intentionally avoids defining a second WindField authority."
  - "WindField is role-dependent: OBSERVED_SENSOR for observed wind and ATMOSPHERIC_MODEL_FIELD for modeled/reanalysis/forecast wind."
  - "Model-as-observation collapse is denied by Atmosphere policy doctrine."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance, not pasted contract content."
  - "The Focus Mode consent sentence is out of scope here and remains routed to Focus Mode / consent documentation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# WindField Lowercase Compatibility Pointer

> Compatibility surface for the lowercase slug `wind-field.md`. The canonical Atmosphere/Air object contract is [`WindField.md`](./WindField.md).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonical: WindField.md" src="https://img.shields.io/badge/canonical-WindField.md-blue">
  <img alt="Schema: CamelCase contract_doc" src="https://img.shields.io/badge/schema-contract__doc__CamelCase-orange">
  <img alt="Character: OBSERVED_SENSOR or ATMOSPHERIC_MODEL_FIELD" src="https://img.shields.io/badge/character-OBSERVED__SENSOR%20%7C%20ATMOSPHERIC__MODEL__FIELD-purple">
  <img alt="Model role: never observation" src="https://img.shields.io/badge/model__role-never__observation-orange">
  <img alt="Parallel authority: denied" src="https://img.shields.io/badge/parallel__authority-denied-critical">
</p>

`contracts/domains/atmosphere/wind-field.md`

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Wind boundary rules](#wind-boundary-rules) · [No-loss disposition](#no-loss-disposition) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

> [!IMPORTANT]
> **Use [`./WindField.md`](./WindField.md) for authoritative object meaning.**  
> This lowercase file is a compatibility pointer for a planned-path slug. It does not replace the canonical CamelCase contract, schema reference, policy roots, fixtures, validators, evidence objects, model-run receipts, uncertainty records, or release objects.

Canonical current relationship:

| Concern | Governing location |
|---|---|
| WindField semantic contract | [`./WindField.md`](./WindField.md) |
| Machine shape scaffold | `../../../schemas/contracts/v1/domains/atmosphere/WindField.schema.json` |
| Object-family mapping | `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` |
| Model-as-observation and source-role policy posture | `../../../docs/domains/atmosphere/POLICY.md` and `../../../policy/domains/atmosphere/` after verification |
| Release, correction, rollback authority | release/correction object families; not this file |

---

## Why this file exists

This file existed as a planned-path scaffold for:

```text
contracts/domains/atmosphere/wind-field.md
```

The expanded CamelCase object contract already exists at:

```text
contracts/domains/atmosphere/WindField.md
```

The paired schema currently points to the CamelCase contract path:

```text
contracts/domains/atmosphere/WindField.md
```

Keeping this lowercase file as a pointer preserves inbound links and scaffold lineage without creating a second source of wind-field meaning.

---

## Wind boundary rules

This compatibility file must not be used to:

- redefine `WindField` separately from [`./WindField.md`](./WindField.md);
- bypass schema, policy, fixtures, validators, evidence, release, correction, or rollback roots;
- collapse modeled, reanalysis, forecast, or gridded wind into an observed station/sensor reading;
- present an `ATMOSPHERIC_MODEL_FIELD` as `OBSERVED_SENSOR`;
- omit source-role, knowledge-character, observed/run/valid time, units, QA, uncertainty, freshness, or model-run receipt where required;
- treat wind speed, wind direction, gust, vector component, or gridded wind context as a generic `WeatherObservation` when wind-specific semantics matter;
- turn wind context into `WeatherStation`, `TemperatureObservation`, `PrecipitationObservation`, `ForecastContext`, `SmokeContext`, `ClimateNormal`, `ClimateAnomaly`, or `AdvisoryContext` authority;
- treat wind as proof of smoke transport, fire behavior, hazard event, infrastructure impact, crop loss, health exposure, property damage, or other impact by itself;
- publish stale, rights-unclear, source-role-unclear, unit-unclear, model-run-missing, uncertainty-missing, station-location-sensitive, or unsupported action/impact claims;
- use wind context as emergency, medical, legal, title, insurance, or life-safety guidance;
- treat generated language, map tiles, dashboards, or UI badges as sovereign truth.

---

## No-loss disposition

| Existing scaffold element | Disposition | Reason |
|---|---|---|
| H1 `Wind Field` | `REPLACED` | The file role is now compatibility pointer, not canonical object contract. |
| `Status: PROPOSED scaffold` | `PRESERVED AS LINEAGE` | The scaffold came from the file-system plan and remains part of why this path exists. |
| Source reference to `FILE_SYSTEM_PLAN.md` | `KEEP + CLARIFY` | The file-system plan is plan-class evidence, not implementation proof. |
| Reminder to keep schemas/policy/fixtures/release separate | `KEEP + EXPAND` | Authority separation is the reason this file must not become a parallel contract. |
| Need for domain-reviewed content | `REDIRECT TO CANONICAL` | Domain-reviewed object content belongs in `WindField.md`. |

---

## Authoring-prompt treatment

The user-provided **KFM Repository Markdown Authoring Agent — Full Operating Prompt v2** was applied as authoring guidance for this update. It was not pasted into this file as object content.

The prompt’s useful effects here were:

- preserve existing scaffold lineage;
- avoid parallel contract authority;
- state implementation uncertainty;
- keep schema, policy, fixtures, validators, release, evidence, and docs roots separate;
- keep observed-sensor versus atmospheric-model-field boundaries visible;
- preserve source-role, unit, QA, uncertainty, model-run receipt, freshness, policy, review, release, correction, and rollback requirements;
- make the file visually inspectable on GitHub;
- include validation and rollback notes.

---

## Consent-pattern disposition

The pasted Focus Mode consent sentence is out of scope for a WindField compatibility pointer.

Consent may become relevant when wind context is rendered through Focus Mode and touches consent-bound, privacy-scoped, living-person-sensitive, private-land, infrastructure-sensitive, habitat-sensitive, station-location-sensitive, hazard-sensitive, or other restricted evidence. Consent remains a separate governance concern handled by Focus Mode / consent documentation and by policy/runtime checks, not by this slug alias.

---

## Validation

Before treating this compatibility pointer as stable, verify:

- all inbound links that point to lowercase `wind-field.md` intentionally use the compatibility alias;
- all authoritative contract references point to [`./WindField.md`](./WindField.md);
- schema `x-kfm.contract_doc` continues to point to the canonical CamelCase file unless an ADR changes naming;
- registry/index docs do not treat this file as a second object contract;
- observed wind and modeled wind remain separated by source role and knowledge character;
- model-run receipt and uncertainty requirements remain visible for modeled/reanalysis/forecast wind;
- units, vector semantics, QA, freshness, rights, sensitivity, source role, review state, release state, correction path, and rollback target remain visible in downstream docs and policy checks;
- future rename/migration plans preserve redirects or update references;
- a drift/register entry exists if the project chooses to retire the lowercase slug.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/domains/atmosphere/wind-field.md` scaffold | `CONFIRMED repo evidence` | Lowercase target existed as a planned-path scaffold. | It did not contain authoritative object semantics. |
| `contracts/domains/atmosphere/WindField.md` | `CONFIRMED repo evidence` | Expanded canonical semantic contract exists and defines role-dependent WindField meaning and boundaries. | Does not by itself prove validator/runtime enforcement. |
| `schemas/contracts/v1/domains/atmosphere/WindField.schema.json` | `CONFIRMED schema evidence` | Schema exists and points to the CamelCase contract path. | Schema properties remain empty and permissive. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | `CONFIRMED docs evidence` | Maps WindField as `OBSERVED_SENSOR` / `ATMOSPHERIC_MODEL_FIELD` depending on role. | Binding remains constrained by source role and review posture where documented. |
| `docs/domains/atmosphere/POLICY.md` | `CONFIRMED docs evidence` | Supports model-is-not-observation denial, source-role requirements, freshness and rights gates, and fail-closed outcomes. | Policy bundle runtime enforcement remains unverified here. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | `CONFIRMED plan evidence` | Explains that concrete Atmosphere paths in the plan are proposed until verified and preserves placement logic. | Plan-class source, not implementation proof. |

---

## Rollback

Rollback if this file is used as a second canonical `WindField` contract, weakens the CamelCase contract, hides slug/authority drift, or enables model-as-observation collapse, unit/QA/uncertainty omission, source-role omission, stale/rights-unclear public display, smoke/hazard/impact overclaiming, advisory/life-safety guidance, or release bypass.

Rollback target: prior scaffold blob SHA `d2c9df7a5f728d4880913568eef546acb3635611`.

<p align="right"><a href="#top">Back to top</a></p>
