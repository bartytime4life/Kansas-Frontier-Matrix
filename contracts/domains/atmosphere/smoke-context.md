<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/smoke-context-lowercase-compat
title: contracts/domains/atmosphere/smoke-context.md — SmokeContext Lowercase Compatibility Pointer
type: contract-compatibility-pointer
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Smoke/remote-sensing steward · Forecast/model steward · Hazards liaison · Contract steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; smoke-context; compatibility; alias; no-parallel-authority; sensitive-cross-lane
tags: [kfm, contracts, atmosphere, air, smoke, smoke-context, remote-sensing-mask, atmospheric-model-field, compatibility, alias, camelcase-canonical, anti-collapse, sensitive-joins, governance]
related:
  - ./SmokeContext.md
  - ./AODRaster.md
  - ./PM25Observation.md
  - ./AirObservation.md
  - ./WindField.md
  - ./ForecastContext.md
  - ./AdvisoryContext.md
  - ./AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/SmokeContext.schema.json
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
notes:
  - "This lowercase slug existed as a planned-path scaffold from the Atmosphere file-system plan."
  - "Canonical expanded semantic contract is ./SmokeContext.md."
  - "The paired schema x-kfm.contract_doc points to contracts/domains/atmosphere/SmokeContext.md, not this lowercase compatibility file."
  - "This file intentionally avoids defining a second SmokeContext authority."
  - "Smoke/fire/AOD/PM2.5 joins can become policy-significant and must fail closed unless evidence, sensitivity, review, and release gates support disclosure."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance, not pasted contract content."
  - "The Focus Mode consent sentence is out of scope here and remains routed to Focus Mode / consent documentation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SmokeContext Lowercase Compatibility Pointer

> Compatibility surface for the lowercase slug `smoke-context.md`. The canonical Atmosphere/Air object contract is [`SmokeContext.md`](./SmokeContext.md).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonical: SmokeContext.md" src="https://img.shields.io/badge/canonical-SmokeContext.md-blue">
  <img alt="Schema: CamelCase contract_doc" src="https://img.shields.io/badge/schema-contract__doc__CamelCase-orange">
  <img alt="Sensitive joins: fail closed" src="https://img.shields.io/badge/sensitive__joins-fail__closed-orange">
  <img alt="Parallel authority: denied" src="https://img.shields.io/badge/parallel__authority-denied-critical">
</p>

`contracts/domains/atmosphere/smoke-context.md`

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Boundary rules](#boundary-rules) · [No-loss disposition](#no-loss-disposition) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

> [!IMPORTANT]
> **Use [`./SmokeContext.md`](./SmokeContext.md) for authoritative object meaning.**  
> This lowercase file is a compatibility pointer for a planned-path slug. It does not replace the canonical CamelCase contract, schema reference, policy roots, fixtures, validators, or release objects.

Canonical current relationship:

| Concern | Governing location |
|---|---|
| SmokeContext semantic contract | [`./SmokeContext.md`](./SmokeContext.md) |
| Machine shape scaffold | `../../../schemas/contracts/v1/domains/atmosphere/SmokeContext.schema.json` |
| Object-family mapping | `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` |
| Atmosphere policy posture | `../../../docs/domains/atmosphere/POLICY.md` and `../../../policy/domains/atmosphere/` after verification |
| Release, correction, rollback authority | release/correction object families; not this file |

---

## Why this file exists

This file existed as a planned-path scaffold for:

```text
contracts/domains/atmosphere/smoke-context.md
```

The expanded CamelCase object contract already exists at:

```text
contracts/domains/atmosphere/SmokeContext.md
```

The paired schema currently points to the CamelCase contract path:

```text
contracts/domains/atmosphere/SmokeContext.md
```

Keeping this lowercase file as a pointer preserves inbound links and scaffold lineage without creating a second source of object meaning.

---

## Boundary rules

This compatibility file must not be used to:

- redefine `SmokeContext` separately from [`./SmokeContext.md`](./SmokeContext.md);
- bypass schema, policy, fixtures, validators, evidence, release, correction, or rollback roots;
- claim smoke context is PM2.5 concentration, AQI, or an observed sensor reading by default;
- claim AOD, remote-sensing smoke masks, plume context, or satellite proxy data is ground-level PM2.5;
- claim forecast/model smoke is observed smoke without explicit source role and method support;
- claim smoke context proves fire-event truth, exposure, health impact, damage, crop loss, infrastructure impact, habitat impact, or evacuation posture by itself;
- publish smoke/fire/AOD/PM2.5 joins near sensitive habitat, infrastructure, living-person, or rights-uncertain contexts without policy review and release support;
- turn smoke context into emergency, medical, or life-safety guidance;
- claim public release without source rights, evidence, policy, review state, release state, correction path, and rollback target;
- treat generated language, map tiles, dashboards, or UI badges as sovereign truth.

---

## No-loss disposition

| Existing scaffold element | Disposition | Reason |
|---|---|---|
| H1 `Smoke Context` | `REPLACED` | The file role is now compatibility pointer, not canonical object contract. |
| `Status: PROPOSED scaffold` | `PRESERVED AS LINEAGE` | The scaffold came from the file-system plan and remains part of why this path exists. |
| Source reference to `FILE_SYSTEM_PLAN.md` | `KEEP + CLARIFY` | The file-system plan is plan-class evidence, not implementation proof. |
| Reminder to keep schemas/policy/fixtures/release separate | `KEEP + EXPAND` | Authority separation is the reason this file must not become a parallel contract. |
| Need for domain-reviewed content | `REDIRECT TO CANONICAL` | Domain-reviewed object content belongs in `SmokeContext.md`. |

---

## Authoring-prompt treatment

The user-provided **KFM Repository Markdown Authoring Agent — Full Operating Prompt v2** was applied as authoring guidance for this update. It was not pasted into this file as object content.

The prompt’s useful effects here were:

- preserve existing scaffold lineage;
- avoid parallel contract authority;
- state implementation uncertainty;
- keep schema, policy, fixtures, validators, release, evidence, and docs roots separate;
- keep sensitive smoke/fire/AOD/PM2.5 joins fail-closed;
- make the file visually inspectable on GitHub;
- include validation and rollback notes.

---

## Consent-pattern disposition

The pasted Focus Mode consent sentence is out of scope for a smoke-context compatibility pointer.

Consent may become relevant when smoke context is rendered through Focus Mode and touches consent-bound, privacy-scoped, living-person-sensitive, habitat-sensitive, infrastructure-sensitive, or other restricted evidence. Consent remains a separate governance concern handled by Focus Mode / consent documentation and by policy/runtime checks, not by this slug alias.

---

## Validation

Before treating this compatibility pointer as stable, verify:

- all inbound links that point to lowercase `smoke-context.md` intentionally use the compatibility alias;
- all authoritative contract references point to [`./SmokeContext.md`](./SmokeContext.md);
- schema `x-kfm.contract_doc` continues to point to the canonical CamelCase file unless an ADR changes naming;
- registry/index docs do not treat this file as a second object contract;
- smoke/fire/AOD/PM2.5 cross-lane disclosure rules remain fail-closed in policy and release checks;
- future rename/migration plans preserve redirects or update references;
- a drift/register entry exists if the project chooses to retire the lowercase slug.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/domains/atmosphere/smoke-context.md` scaffold | `CONFIRMED repo evidence` | Lowercase target existed as a planned-path scaffold. | It did not contain authoritative object semantics. |
| `contracts/domains/atmosphere/SmokeContext.md` | `CONFIRMED repo evidence` | Expanded canonical semantic contract exists and defines SmokeContext meaning and boundaries. | Does not by itself prove validator/runtime enforcement. |
| `schemas/contracts/v1/domains/atmosphere/SmokeContext.schema.json` | `CONFIRMED schema evidence` | Schema exists and points to the CamelCase contract path. | Schema properties remain empty and permissive. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | `CONFIRMED docs evidence` | Maps SmokeContext as source-dependent `REMOTE_SENSING_MASK` / `ATMOSPHERIC_MODEL_FIELD`. | Binding remains source-dependent/inferred where documented. |
| `docs/domains/atmosphere/POLICY.md` | `CONFIRMED docs evidence` | Supports fail-closed policy, AOD/PM2.5 denial, model/observation denial, source-role discipline, and sensitivity posture. | Policy bundle runtime enforcement remains unverified here. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | `CONFIRMED plan evidence` | Explains that concrete Atmosphere paths in the plan are proposed until verified and preserves placement logic. | Plan-class source, not implementation proof. |

---

## Rollback

Rollback if this file is used as a second canonical `SmokeContext` contract, weakens the CamelCase contract, hides slug/authority drift, or enables unsafe smoke/fire/AOD/PM2.5 joins.

Rollback target: prior scaffold blob SHA `1b09d7835a2b3ee54bcd0670b0cff9fbd8161733`.

<p align="right"><a href="#top">Back to top</a></p>
