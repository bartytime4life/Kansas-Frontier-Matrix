<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/weather-station-lowercase-compat
title: contracts/domains/atmosphere/weather-station.md — WeatherStation Lowercase Compatibility Pointer
type: contract-compatibility-pointer
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Weather steward · Station/network steward · Contract steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; weather-station; compatibility; alias; no-parallel-authority; station-siting
tags: [kfm, contracts, atmosphere, air, weather, weather-station, station, network, site, network-and-site-context, siting, compatibility, alias, camelcase-canonical, governance]
related:
  - ./WeatherStation.md
  - ./WeatherObservation.md
  - ./TemperatureObservation.md
  - ./PrecipitationObservation.md
  - ./WindField.md
  - ./ForecastContext.md
  - ./ClimateNormal.md
  - ./ClimateAnomaly.md
  - ./AdvisoryContext.md
  - ./AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/WeatherStation.schema.json
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
notes:
  - "This lowercase slug existed as a planned-path scaffold from the Atmosphere file-system plan."
  - "Canonical expanded semantic contract is ./WeatherStation.md."
  - "The paired schema x-kfm.contract_doc points to contracts/domains/atmosphere/WeatherStation.md, not this lowercase compatibility file."
  - "This file intentionally avoids defining a second WeatherStation authority."
  - "Weather Station is mapped to NETWORK_AND_SITE_CONTEXT and carries exact-siting generalization requirements before public release."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance, not pasted contract content."
  - "The Focus Mode consent sentence is out of scope here and remains routed to Focus Mode / consent documentation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# WeatherStation Lowercase Compatibility Pointer

> Compatibility surface for the lowercase slug `weather-station.md`. The canonical Atmosphere/Air object contract is [`WeatherStation.md`](./WeatherStation.md).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonical: WeatherStation.md" src="https://img.shields.io/badge/canonical-WeatherStation.md-blue">
  <img alt="Schema: CamelCase contract_doc" src="https://img.shields.io/badge/schema-contract__doc__CamelCase-orange">
  <img alt="Character: NETWORK_AND_SITE_CONTEXT" src="https://img.shields.io/badge/character-NETWORK__AND__SITE__CONTEXT-purple">
  <img alt="Siting: generalize before public release" src="https://img.shields.io/badge/siting-generalize__before__public__release-orange">
  <img alt="Parallel authority: denied" src="https://img.shields.io/badge/parallel__authority-denied-critical">
</p>

`contracts/domains/atmosphere/weather-station.md`

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Station boundary rules](#station-boundary-rules) · [No-loss disposition](#no-loss-disposition) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

> [!IMPORTANT]
> **Use [`./WeatherStation.md`](./WeatherStation.md) for authoritative object meaning.**  
> This lowercase file is a compatibility pointer for a planned-path slug. It does not replace the canonical CamelCase contract, schema reference, policy roots, fixtures, validators, evidence objects, station registry records, or release objects.

Canonical current relationship:

| Concern | Governing location |
|---|---|
| WeatherStation semantic contract | [`./WeatherStation.md`](./WeatherStation.md) |
| Machine shape scaffold | `../../../schemas/contracts/v1/domains/atmosphere/WeatherStation.schema.json` |
| Object-family mapping | `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` |
| Exact-station-siting policy posture | `../../../docs/domains/atmosphere/POLICY.md` and `../../../policy/domains/atmosphere/` after verification |
| Release, correction, rollback authority | release/correction object families; not this file |

---

## Why this file exists

This file existed as a planned-path scaffold for:

```text
contracts/domains/atmosphere/weather-station.md
```

The expanded CamelCase object contract already exists at:

```text
contracts/domains/atmosphere/WeatherStation.md
```

The paired schema currently points to the CamelCase contract path:

```text
contracts/domains/atmosphere/WeatherStation.md
```

Keeping this lowercase file as a pointer preserves inbound links and scaffold lineage without creating a second source of station/network-site meaning.

---

## Station boundary rules

This compatibility file must not be used to:

- redefine `WeatherStation` separately from [`./WeatherStation.md`](./WeatherStation.md);
- bypass schema, policy, fixtures, validators, evidence, release, correction, or rollback roots;
- turn station metadata into `WeatherObservation`, `TemperatureObservation`, `PrecipitationObservation`, or `WindField` values;
- treat station/network membership as proof that attached observations are true, complete, current, calibrated, or publishable;
- collapse station site context into forecast/model context, climate normal, climate anomaly, advisory, hazard, exposure, crop-loss, damage, infrastructure, or impact claims;
- publish exact station coordinates, private-land context, infrastructure-sensitive context, station ownership, or access details without policy review, generalization/restriction, release approval, correction path, and rollback target;
- treat schema validity as evidence proof;
- normalize direct public access to raw station feeds, raw network exports, workspaces, quarantine material, or internal canonical stores;
- use station context as emergency, medical, legal, title, insurance, or life-safety guidance;
- treat generated language, map tiles, dashboards, or UI badges as sovereign truth.

---

## No-loss disposition

| Existing scaffold element | Disposition | Reason |
|---|---|---|
| H1 `Weather Station` | `REPLACED` | The file role is now compatibility pointer, not canonical object contract. |
| `Status: PROPOSED scaffold` | `PRESERVED AS LINEAGE` | The scaffold came from the file-system plan and remains part of why this path exists. |
| Source reference to `FILE_SYSTEM_PLAN.md` | `KEEP + CLARIFY` | The file-system plan is plan-class evidence, not implementation proof. |
| Reminder to keep schemas/policy/fixtures/release separate | `KEEP + EXPAND` | Authority separation is the reason this file must not become a parallel contract. |
| Need for domain-reviewed content | `REDIRECT TO CANONICAL` | Domain-reviewed object content belongs in `WeatherStation.md`. |

---

## Authoring-prompt treatment

The user-provided **KFM Repository Markdown Authoring Agent — Full Operating Prompt v2** was applied as authoring guidance for this update. It was not pasted into this file as object content.

The prompt’s useful effects here were:

- preserve existing scaffold lineage;
- avoid parallel contract authority;
- state implementation uncertainty;
- keep schema, policy, fixtures, validators, release, evidence, and docs roots separate;
- keep station/network site context, exact-siting sensitivity, rights, generalization, review, release, correction, and rollback requirements visible;
- make the file visually inspectable on GitHub;
- include validation and rollback notes.

---

## Consent-pattern disposition

The pasted Focus Mode consent sentence is out of scope for a WeatherStation compatibility pointer.

Consent may become relevant when station context is rendered through Focus Mode and touches consent-bound, privacy-scoped, living-person-sensitive, private-land, infrastructure-sensitive, habitat-sensitive, station-location-sensitive, or other restricted evidence. Consent remains a separate governance concern handled by Focus Mode / consent documentation and by policy/runtime checks, not by this slug alias.

---

## Validation

Before treating this compatibility pointer as stable, verify:

- all inbound links that point to lowercase `weather-station.md` intentionally use the compatibility alias;
- all authoritative contract references point to [`./WeatherStation.md`](./WeatherStation.md);
- schema `x-kfm.contract_doc` continues to point to the canonical CamelCase file unless an ADR changes naming;
- registry/index docs do not treat this file as a second object contract;
- exact station siting remains generalized/restricted before public release;
- station ownership, access, private-land context, infrastructure-sensitive context, rights, sensitivity, source role, review state, release state, correction path, and rollback target remain visible in downstream docs and policy checks;
- future rename/migration plans preserve redirects or update references;
- a drift/register entry exists if the project chooses to retire the lowercase slug.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/domains/atmosphere/weather-station.md` scaffold | `CONFIRMED repo evidence` | Lowercase target existed as a planned-path scaffold. | It did not contain authoritative object semantics. |
| `contracts/domains/atmosphere/WeatherStation.md` | `CONFIRMED repo evidence` | Expanded canonical semantic contract exists and defines WeatherStation meaning and station boundaries. | Does not by itself prove validator/runtime enforcement. |
| `schemas/contracts/v1/domains/atmosphere/WeatherStation.schema.json` | `CONFIRMED schema evidence` | Schema exists and points to the CamelCase contract path. | Schema properties remain empty and permissive. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | `CONFIRMED docs evidence` | Maps Weather Station as `NETWORK_AND_SITE_CONTEXT`. | Binding remains constrained by source role and review posture where documented. |
| `docs/domains/atmosphere/POLICY.md` | `CONFIRMED docs evidence` | Supports exact-station-siting generalization before public release, source-role discipline, freshness and rights gates, and fail-closed outcomes. | Policy bundle runtime enforcement remains unverified here. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | `CONFIRMED plan evidence` | Explains that concrete Atmosphere paths in the plan are proposed until verified and preserves placement logic. | Plan-class source, not implementation proof. |

---

## Rollback

Rollback if this file is used as a second canonical `WeatherStation` contract, weakens the CamelCase contract, hides slug/authority drift, or enables unsafe station-coordinate, station-ownership, access, private-land, infrastructure-sensitive, observation-truth, forecast, climate, hazard, advisory, or release claims.

Rollback target: prior scaffold blob SHA `426d39e2a2e0f2ee624776b1f9b19783ccf55793`.

<p align="right"><a href="#top">Back to top</a></p>
