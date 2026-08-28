<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/pm25-observation-lowercase-compat
title: contracts/domains/atmosphere/pm25-observation.md — PM25Observation Lowercase Compatibility Pointer
type: contract-compatibility-pointer
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Air-quality steward · PM2.5 steward · Contract steward · Schema steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; pm25-observation; compatibility; alias; no-parallel-authority
tags: [kfm, contracts, atmosphere, air, pm25, pm2.5, particulate-matter, pm25-observation, compatibility, alias, camelcase-canonical, anti-collapse, governance]
related:
  - ./PM25Observation.md
  - ./AirObservation.md
  - ./AirStation.md
  - ./OzoneObservation.md
  - ./AODRaster.md
  - ./SmokeContext.md
  - ./ForecastContext.md
  - ./AdvisoryContext.md
  - ./AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
notes:
  - "This lowercase slug existed as a planned-path scaffold from the Atmosphere file-system plan."
  - "Canonical expanded semantic contract is ./PM25Observation.md."
  - "The paired schema x-kfm.contract_doc points to contracts/domains/atmosphere/PM25Observation.md, not this lowercase compatibility file."
  - "This file intentionally avoids defining a second PM25Observation authority."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance, not pasted contract content."
  - "The Focus Mode consent sentence is out of scope here and remains routed to Focus Mode / consent documentation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PM25Observation Lowercase Compatibility Pointer

> Compatibility surface for the lowercase slug `pm25-observation.md`. The canonical Atmosphere/Air object contract is [`PM25Observation.md`](./PM25Observation.md).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonical: PM25Observation.md" src="https://img.shields.io/badge/canonical-PM25Observation.md-blue">
  <img alt="Schema: CamelCase contract_doc" src="https://img.shields.io/badge/schema-contract__doc__CamelCase-orange">
  <img alt="Parallel authority: denied" src="https://img.shields.io/badge/parallel__authority-denied-critical">
</p>

`contracts/domains/atmosphere/pm25-observation.md`

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Boundary rules](#boundary-rules) · [No-loss disposition](#no-loss-disposition) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

> [!IMPORTANT]
> **Use [`./PM25Observation.md`](./PM25Observation.md) for authoritative object meaning.**  
> This lowercase file is a compatibility pointer for a planned-path slug. It does not replace the canonical CamelCase contract, schema reference, policy roots, fixtures, validators, or release objects.

Canonical current relationship:

| Concern | Governing location |
|---|---|
| PM25Observation semantic contract | [`./PM25Observation.md`](./PM25Observation.md) |
| Machine shape scaffold | `../../../schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json` |
| Object-family mapping | `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` |
| Atmosphere policy posture | `../../../docs/domains/atmosphere/POLICY.md` and `../../../policy/domains/atmosphere/` after verification |
| Release, correction, rollback authority | release/correction object families; not this file |

---

## Why this file exists

This file existed as a planned-path scaffold for:

```text
contracts/domains/atmosphere/pm25-observation.md
```

The expanded CamelCase object contract already exists at:

```text
contracts/domains/atmosphere/PM25Observation.md
```

The paired schema currently points to the CamelCase contract path:

```text
contracts/domains/atmosphere/PM25Observation.md
```

Keeping this lowercase file as a pointer preserves inbound links and scaffold lineage without creating a second source of object meaning.

---

## Boundary rules

This compatibility file must not be used to:

- redefine `PM25Observation` separately from [`./PM25Observation.md`](./PM25Observation.md);
- bypass schema, policy, fixtures, validators, evidence, release, correction, or rollback roots;
- claim PM2.5 AQI is PM2.5 concentration;
- claim AOD, smoke mask, or satellite proxy data is ground PM2.5;
- claim low-cost PM2.5 sensor records are reference-grade without caveats, correction, confidence, limitations, policy state, and review;
- claim model output is an observed PM2.5 value;
- claim a PM2.5 observation is a health, medical, emergency, or life-safety instruction;
- claim public release without source rights, evidence, policy, review state, release state, correction path, and rollback target;
- treat generated language, map tiles, dashboards, or UI badges as sovereign truth.

---

## No-loss disposition

| Existing scaffold element | Disposition | Reason |
|---|---|---|
| H1 `Pm25 Observation` | `REPLACED` | The file role is now compatibility pointer, not canonical object contract. |
| `Status: PROPOSED scaffold` | `PRESERVED AS LINEAGE` | The scaffold came from the file-system plan and remains part of why this path exists. |
| Source reference to `FILE_SYSTEM_PLAN.md` | `KEEP + CLARIFY` | The file-system plan is plan-class evidence, not implementation proof. |
| Reminder to keep schemas/policy/fixtures/release separate | `KEEP + EXPAND` | Authority separation is the reason this file must not become a parallel contract. |
| Need for domain-reviewed content | `REDIRECT TO CANONICAL` | Domain-reviewed object content belongs in `PM25Observation.md`. |

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

The pasted Focus Mode consent sentence is out of scope for a PM2.5-observation compatibility pointer.

Consent may become relevant when PM2.5 evidence is rendered through Focus Mode, but consent remains a separate governance concern. It should be handled by Focus Mode / consent documentation and by policy/runtime checks, not by this slug alias.

---

## Validation

Before treating this compatibility pointer as stable, verify:

- all inbound links that point to lowercase `pm25-observation.md` intentionally use the compatibility alias;
- all authoritative contract references point to [`./PM25Observation.md`](./PM25Observation.md);
- schema `x-kfm.contract_doc` continues to point to the canonical CamelCase file unless an ADR changes naming;
- registry/index docs do not treat this file as a second object contract;
- future rename/migration plans preserve redirects or update references;
- a drift/register entry exists if the project chooses to retire the lowercase slug.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/domains/atmosphere/pm25-observation.md` scaffold | `CONFIRMED repo evidence` | Lowercase target existed as a planned-path scaffold. | It did not contain authoritative object semantics. |
| `contracts/domains/atmosphere/PM25Observation.md` | `CONFIRMED repo evidence` | Expanded canonical semantic contract exists and defines PM25Observation meaning and boundaries. | Does not by itself prove validator/runtime enforcement. |
| `schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json` | `CONFIRMED schema evidence` | Schema exists and points to the CamelCase contract path. | Schema properties remain empty and permissive. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | `CONFIRMED docs evidence` | Maps PM2.5 Observation as an air-quality object with role-dependent `OBSERVED_SENSOR` / `PUBLIC_AQI_REPORT` character. | Binding remains role-dependent/inferred where documented. |
| `docs/domains/atmosphere/POLICY.md` | `CONFIRMED docs evidence` | Supports fail-closed policy and AQI/AOD/model/low-cost-sensor anti-collapse posture. | Policy bundle runtime enforcement remains unverified here. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | `CONFIRMED plan evidence` | Explains that concrete Atmosphere paths in the plan are proposed until verified and preserves placement logic. | Plan-class source, not implementation proof. |

---

## Rollback

Rollback if this file is used as a second canonical `PM25Observation` contract, weakens the CamelCase contract, or hides slug/authority drift.

Rollback target: prior scaffold blob SHA `cfe12e64269feb31286912631b54e6bde568cdbb`.

<p align="right"><a href="#top">Back to top</a></p>
