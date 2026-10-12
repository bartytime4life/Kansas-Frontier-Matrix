<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/precipitation-observation-lowercase-compat
title: contracts/domains/atmosphere/precipitation-observation.md — PrecipitationObservation Lowercase Compatibility Pointer
type: contract-compatibility-pointer
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Weather steward · Precipitation steward · Contract steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; precipitation-observation; compatibility; alias; no-parallel-authority
tags: [kfm, contracts, atmosphere, air, precipitation, precipitation-observation, weather, compatibility, alias, camelcase-canonical, model-as-observation, governance]
related:
  - ./PrecipitationObservation.md
  - ./WeatherObservation.md
  - ./WeatherStation.md
  - ./TemperatureObservation.md
  - ./WindField.md
  - ./ForecastContext.md
  - ./ClimateNormal.md
  - ./ClimateAnomaly.md
  - ./AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/PrecipitationObservation.schema.json
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
notes:
  - "This lowercase slug existed as a planned-path scaffold from the Atmosphere file-system plan."
  - "Canonical expanded semantic contract is ./PrecipitationObservation.md."
  - "The paired schema x-kfm.contract_doc points to contracts/domains/atmosphere/PrecipitationObservation.md, not this lowercase compatibility file."
  - "This file intentionally avoids defining a second PrecipitationObservation authority."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance, not pasted contract content."
  - "The Focus Mode consent sentence is out of scope here and remains routed to Focus Mode / consent documentation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PrecipitationObservation Lowercase Compatibility Pointer

> Compatibility surface for the lowercase slug `precipitation-observation.md`. The canonical Atmosphere/Air object contract is [`PrecipitationObservation.md`](./PrecipitationObservation.md).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonical: PrecipitationObservation.md" src="https://img.shields.io/badge/canonical-PrecipitationObservation.md-blue">
  <img alt="Schema: CamelCase contract_doc" src="https://img.shields.io/badge/schema-contract__doc__CamelCase-orange">
  <img alt="Parallel authority: denied" src="https://img.shields.io/badge/parallel__authority-denied-critical">
</p>

`contracts/domains/atmosphere/precipitation-observation.md`

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Boundary rules](#boundary-rules) · [No-loss disposition](#no-loss-disposition) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

> [!IMPORTANT]
> **Use [`./PrecipitationObservation.md`](./PrecipitationObservation.md) for authoritative object meaning.**  
> This lowercase file is a compatibility pointer for a planned-path slug. It does not replace the canonical CamelCase contract, schema reference, policy roots, fixtures, validators, or release objects.

Canonical current relationship:

| Concern | Governing location |
|---|---|
| PrecipitationObservation semantic contract | [`./PrecipitationObservation.md`](./PrecipitationObservation.md) |
| Machine shape scaffold | `../../../schemas/contracts/v1/domains/atmosphere/PrecipitationObservation.schema.json` |
| Object-family mapping | `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` |
| Atmosphere policy posture | `../../../docs/domains/atmosphere/POLICY.md` and `../../../policy/domains/atmosphere/` after verification |
| Release, correction, rollback authority | release/correction object families; not this file |

---

## Why this file exists

This file existed as a planned-path scaffold for:

```text
contracts/domains/atmosphere/precipitation-observation.md
```

The expanded CamelCase object contract already exists at:

```text
contracts/domains/atmosphere/PrecipitationObservation.md
```

The paired schema currently points to the CamelCase contract path:

```text
contracts/domains/atmosphere/PrecipitationObservation.md
```

Keeping this lowercase file as a pointer preserves inbound links and scaffold lineage without creating a second source of object meaning.

---

## Boundary rules

This compatibility file must not be used to:

- redefine `PrecipitationObservation` separately from [`./PrecipitationObservation.md`](./PrecipitationObservation.md);
- bypass schema, policy, fixtures, validators, evidence, release, correction, or rollback roots;
- claim forecast/model precipitation is observed precipitation;
- claim a precipitation reading is a climate normal or climate anomaly by itself;
- claim a precipitation reading proves flood, drought, storm, crop loss, infrastructure damage, or other hazard/impact truth by itself;
- claim canonical-unit enforcement unless schema/validator/policy evidence proves it;
- claim public release without source rights, evidence, policy, review state, release state, correction path, and rollback target;
- turn a precipitation observation into emergency, medical, or life-safety guidance;
- treat generated language, map tiles, dashboards, or UI badges as sovereign truth.

---

## No-loss disposition

| Existing scaffold element | Disposition | Reason |
|---|---|---|
| H1 `Precipitation Observation` | `REPLACED` | The file role is now compatibility pointer, not canonical object contract. |
| `Status: PROPOSED scaffold` | `PRESERVED AS LINEAGE` | The scaffold came from the file-system plan and remains part of why this path exists. |
| Source reference to `FILE_SYSTEM_PLAN.md` | `KEEP + CLARIFY` | The file-system plan is plan-class evidence, not implementation proof. |
| Reminder to keep schemas/policy/fixtures/release separate | `KEEP + EXPAND` | Authority separation is the reason this file must not become a parallel contract. |
| Need for domain-reviewed content | `REDIRECT TO CANONICAL` | Domain-reviewed object content belongs in `PrecipitationObservation.md`. |

---

## Authoring-prompt treatment

The user-provided **KFM Repository Markdown Authoring Agent — Full Operating Prompt v2** was applied as authoring guidance for this update. It was not pasted into this file as object content.

The prompt’s useful effects here were:

- preserve existing scaffold lineage;
- avoid parallel contract authority;
- state implementation uncertainty;
- keep schema, policy, fixtures, validators, release, evidence, and docs roots separate;
- make the file visually inspectable on GitHub;
- include validation and rollback notes.

---

## Consent-pattern disposition

The pasted Focus Mode consent sentence is out of scope for a precipitation-observation compatibility pointer.

Consent may become relevant when precipitation evidence is rendered through Focus Mode and touches consent-bound, privacy-scoped, or living-person-sensitive evidence, but consent remains a separate governance concern. It should be handled by Focus Mode / consent documentation and by policy/runtime checks, not by this slug alias.

---

## Validation

Before treating this compatibility pointer as stable, verify:

- all inbound links that point to lowercase `precipitation-observation.md` intentionally use the compatibility alias;
- all authoritative contract references point to [`./PrecipitationObservation.md`](./PrecipitationObservation.md);
- schema `x-kfm.contract_doc` continues to point to the canonical CamelCase file unless an ADR changes naming;
- registry/index docs do not treat this file as a second object contract;
- future rename/migration plans preserve redirects or update references;
- a drift/register entry exists if the project chooses to retire the lowercase slug.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/domains/atmosphere/precipitation-observation.md` scaffold | `CONFIRMED repo evidence` | Lowercase target existed as a planned-path scaffold. | It did not contain authoritative object semantics. |
| `contracts/domains/atmosphere/PrecipitationObservation.md` | `CONFIRMED repo evidence` | Expanded canonical semantic contract exists and defines PrecipitationObservation meaning and boundaries. | Does not by itself prove validator/runtime enforcement. |
| `schemas/contracts/v1/domains/atmosphere/PrecipitationObservation.schema.json` | `CONFIRMED schema evidence` | Schema exists and points to the CamelCase contract path. | Schema properties remain empty and permissive. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | `CONFIRMED docs evidence` | Maps Precipitation Observation as a weather object with `OBSERVED_SENSOR` / `METEOROLOGICAL_CONTEXT` character. | Binding remains role-dependent/inferred where documented. |
| `docs/domains/atmosphere/POLICY.md` | `CONFIRMED docs evidence` | Supports fail-closed policy, source-role discipline, model-is-not-observation discipline, freshness gates, and unresolved-rights holds. | Policy bundle runtime enforcement remains unverified here. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | `CONFIRMED plan evidence` | Explains that concrete Atmosphere paths in the plan are proposed until verified and preserves placement logic. | Plan-class source, not implementation proof. |

---

## Rollback

Rollback if this file is used as a second canonical `PrecipitationObservation` contract, weakens the CamelCase contract, or hides slug/authority drift.

Rollback target: prior scaffold blob SHA `b6dfacc01d7d122475b7509033141a02546127c4`.

<p align="right"><a href="#top">Back to top</a></p>
