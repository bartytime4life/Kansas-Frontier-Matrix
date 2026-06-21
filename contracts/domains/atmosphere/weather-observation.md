<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/weather-observation-lowercase-compat
title: contracts/domains/atmosphere/weather-observation.md — WeatherObservation Lowercase Compatibility Pointer
type: contract-compatibility-pointer
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Weather steward · Contract steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; weather-observation; compatibility; alias; no-parallel-authority
tags: [kfm, contracts, atmosphere, air, weather, weather-observation, observed-sensor, meteorological-context, source-role, compatibility, alias, camelcase-canonical, governance]
related:
  - ./WeatherObservation.md
  - ./WeatherStation.md
  - ./TemperatureObservation.md
  - ./PrecipitationObservation.md
  - ./WindField.md
  - ./ForecastContext.md
  - ./ClimateNormal.md
  - ./ClimateAnomaly.md
  - ./AdvisoryContext.md
  - ./AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
notes:
  - "This lowercase slug existed as a planned-path scaffold from the Atmosphere file-system plan."
  - "Canonical expanded semantic contract is ./WeatherObservation.md."
  - "The paired schema x-kfm.contract_doc points to contracts/domains/atmosphere/WeatherObservation.md, not this lowercase compatibility file."
  - "This file intentionally avoids defining a second WeatherObservation authority."
  - "General weather observations require source-role and context-vs-primary-claim discipline before public use."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance, not pasted contract content."
  - "The Focus Mode consent sentence is out of scope here and remains routed to Focus Mode / consent documentation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# WeatherObservation Lowercase Compatibility Pointer

> Compatibility surface for the lowercase slug `weather-observation.md`. The canonical Atmosphere/Air object contract is [`WeatherObservation.md`](./WeatherObservation.md).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonical: WeatherObservation.md" src="https://img.shields.io/badge/canonical-WeatherObservation.md-blue">
  <img alt="Schema: CamelCase contract_doc" src="https://img.shields.io/badge/schema-contract__doc__CamelCase-orange">
  <img alt="Role tagging: required" src="https://img.shields.io/badge/role__tagging-required-orange">
  <img alt="Parallel authority: denied" src="https://img.shields.io/badge/parallel__authority-denied-critical">
</p>

`contracts/domains/atmosphere/weather-observation.md`

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Boundary rules](#boundary-rules) · [No-loss disposition](#no-loss-disposition) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

> [!IMPORTANT]
> **Use [`./WeatherObservation.md`](./WeatherObservation.md) for authoritative object meaning.**  
> This lowercase file is a compatibility pointer for a planned-path slug. It does not replace the canonical CamelCase contract, schema reference, policy roots, fixtures, validators, evidence objects, or release objects.

Canonical current relationship:

| Concern | Governing location |
|---|---|
| WeatherObservation semantic contract | [`./WeatherObservation.md`](./WeatherObservation.md) |
| Machine shape scaffold | `../../../schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json` |
| Object-family mapping | `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` |
| Atmosphere policy posture | `../../../docs/domains/atmosphere/POLICY.md` and `../../../policy/domains/atmosphere/` after verification |
| Release, correction, rollback authority | release/correction object families; not this file |

---

## Why this file exists

This file existed as a planned-path scaffold for:

```text
contracts/domains/atmosphere/weather-observation.md
```

The expanded CamelCase object contract already exists at:

```text
contracts/domains/atmosphere/WeatherObservation.md
```

The paired schema currently points to the CamelCase contract path:

```text
contracts/domains/atmosphere/WeatherObservation.md
```

Keeping this lowercase file as a pointer preserves inbound links and scaffold lineage without creating a second source of object meaning.

---

## Boundary rules

This compatibility file must not be used to:

- redefine `WeatherObservation` separately from [`./WeatherObservation.md`](./WeatherObservation.md);
- bypass schema, policy, fixtures, validators, evidence, release, correction, or rollback roots;
- flatten specialized variables that need their own semantics into generic weather context;
- replace `TemperatureObservation`, `PrecipitationObservation`, or `WindField` when temperature, precipitation, or wind-specific units, methods, QA, source roles, or model roles matter;
- collapse forecast/model weather context into observed weather;
- collapse a weather observation into `ClimateNormal` or `ClimateAnomaly` claims without aggregation method, baseline scope, evidence, and release review;
- treat a weather observation as proof of hazard event, exposure, health effect, crop loss, infrastructure impact, damage, regulatory threshold, or other impact by itself;
- publish station-specific or sensitive weather context without source rights, source role, units, QA, freshness, validation, policy, review, release state, correction path, and rollback target;
- turn weather context into emergency, medical, legal, title, insurance, or life-safety guidance;
- treat generated language, map tiles, dashboards, or UI badges as sovereign truth.

---

## No-loss disposition

| Existing scaffold element | Disposition | Reason |
|---|---|---|
| H1 `Weather Observation` | `REPLACED` | The file role is now compatibility pointer, not canonical object contract. |
| `Status: PROPOSED scaffold` | `PRESERVED AS LINEAGE` | The scaffold came from the file-system plan and remains part of why this path exists. |
| Source reference to `FILE_SYSTEM_PLAN.md` | `KEEP + CLARIFY` | The file-system plan is plan-class evidence, not implementation proof. |
| Reminder to keep schemas/policy/fixtures/release separate | `KEEP + EXPAND` | Authority separation is the reason this file must not become a parallel contract. |
| Need for domain-reviewed content | `REDIRECT TO CANONICAL` | Domain-reviewed object content belongs in `WeatherObservation.md`. |

---

## Authoring-prompt treatment

The user-provided **KFM Repository Markdown Authoring Agent — Full Operating Prompt v2** was applied as authoring guidance for this update. It was not pasted into this file as object content.

The prompt’s useful effects here were:

- preserve existing scaffold lineage;
- avoid parallel contract authority;
- state implementation uncertainty;
- keep schema, policy, fixtures, validators, release, evidence, and docs roots separate;
- keep source-role, context-vs-primary-claim, units, QA, freshness, and release requirements visible;
- make the file visually inspectable on GitHub;
- include validation and rollback notes.

---

## Consent-pattern disposition

The pasted Focus Mode consent sentence is out of scope for a weather-observation compatibility pointer.

Consent may become relevant when weather context is rendered through Focus Mode and touches consent-bound, privacy-scoped, living-person-sensitive, infrastructure-sensitive, habitat-sensitive, station-location-sensitive, or other restricted evidence. Consent remains a separate governance concern handled by Focus Mode / consent documentation and by policy/runtime checks, not by this slug alias.

---

## Validation

Before treating this compatibility pointer as stable, verify:

- all inbound links that point to lowercase `weather-observation.md` intentionally use the compatibility alias;
- all authoritative contract references point to [`./WeatherObservation.md`](./WeatherObservation.md);
- schema `x-kfm.contract_doc` continues to point to the canonical CamelCase file unless an ADR changes naming;
- registry/index docs do not treat this file as a second object contract;
- source-role, context-vs-primary-claim, units, QA, freshness, rights, sensitivity, and release controls remain visible in downstream docs and policy checks;
- future rename/migration plans preserve redirects or update references;
- a drift/register entry exists if the project chooses to retire the lowercase slug.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/domains/atmosphere/weather-observation.md` scaffold | `CONFIRMED repo evidence` | Lowercase target existed as a planned-path scaffold. | It did not contain authoritative object semantics. |
| `contracts/domains/atmosphere/WeatherObservation.md` | `CONFIRMED repo evidence` | Expanded canonical semantic contract exists and defines WeatherObservation meaning and boundaries. | Does not by itself prove validator/runtime enforcement. |
| `schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json` | `CONFIRMED schema evidence` | Schema exists and points to the CamelCase contract path. | Schema properties remain empty and permissive. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | `CONFIRMED docs evidence` | Maps Weather Observation as `OBSERVED_SENSOR` / `METEOROLOGICAL_CONTEXT`. | Binding remains constrained by source role and context-vs-primary-claim role where documented. |
| `docs/domains/atmosphere/POLICY.md` | `CONFIRMED docs evidence` | Supports fail-closed policy, source-role discipline, model/observation denial, freshness gates, and unresolved-rights holds. | Policy bundle runtime enforcement remains unverified here. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | `CONFIRMED plan evidence` | Explains that concrete Atmosphere paths in the plan are proposed until verified and preserves placement logic. | Plan-class source, not implementation proof. |

---

## Rollback

Rollback if this file is used as a second canonical `WeatherObservation` contract, weakens the CamelCase contract, hides slug/authority drift, or enables unsafe weather, specialized-variable, forecast, climate, hazard, or impact claims.

Rollback target: prior scaffold blob SHA `a74b53f29030e3ee77e1df6ec8bc1927cc654092`.

<p align="right"><a href="#top">Back to top</a></p>
