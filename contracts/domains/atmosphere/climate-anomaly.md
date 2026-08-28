<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://compat/contracts/domains/atmosphere/climate-anomaly
title: contracts/domains/atmosphere/climate-anomaly.md — Climate Anomaly Compatibility Pointer
type: compatibility-note
version: v0.1
status: draft
owners: OWNER_TBD — Atmosphere steward · Climate steward · Contract steward · Docs steward · Schema steward · Policy steward · Release steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; compatibility; climate-anomaly; no-parallel-authority; baseline-relative
tags: [kfm, contracts, atmosphere, air, climate-anomaly, ClimateAnomaly, compatibility, casing, slug, no-parallel-authority, climate-anomaly-context, climate-normal, baseline-anchor, authoring-boundary, governance]
related:
  - ./ClimateAnomaly.md
  - ./ClimateNormal.md
  - ./TemperatureObservation.md
  - ./PrecipitationObservation.md
  - ./WeatherObservation.md
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
  - ../../../schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json
notes:
  - "This lowercase slug file existed as a planned scaffold sourced from FILE_SYSTEM_PLAN.md."
  - "The canonical expanded climate-anomaly semantic contract is ./ClimateAnomaly.md."
  - "The paired schema contract_doc points to ./ClimateAnomaly.md, not this lowercase compatibility file."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance for this revision, not as content to paste into this compatibility pointer."
  - "The Focus Mode consent sentence belongs to Focus Mode / consent documentation and is referenced here only as an out-of-scope disposition."
  - "This file intentionally avoids duplicating ClimateAnomaly semantics so the repo does not grow two competing climate-anomaly authorities."
  - "Schema, policy, fixtures, tests, evidence, consent enforcement, aggregation receipts, baseline review, and release decisions remain in their responsibility roots."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Climate Anomaly Compatibility Pointer

> Compatibility pointer for the lowercase planned path `contracts/domains/atmosphere/climate-anomaly.md`. This file exists to preserve older slug-style references while routing maintainers to the canonical `ClimateAnomaly` contract. It is **not** a second climate-anomaly contract, not a consent pattern, and not a release authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Type: compatibility note" src="https://img.shields.io/badge/type-compatibility__note-blue">
  <img alt="Authority: pointer only" src="https://img.shields.io/badge/authority-pointer__only-lightgrey">
  <img alt="Canonical: ClimateAnomaly.md" src="https://img.shields.io/badge/canonical-ClimateAnomaly.md-purple">
  <img alt="No parallel authority" src="https://img.shields.io/badge/no__parallel__authority-required-critical">
  <img alt="Baseline anchor required" src="https://img.shields.io/badge/baseline__anchor-required-orange">
</p>

**Path:** `contracts/domains/atmosphere/climate-anomaly.md`  
**Canonical contract:** [`./ClimateAnomaly.md`](./ClimateAnomaly.md)  
**Status:** `draft` / compatibility note  
**Truth posture:** `CONFIRMED` lowercase file path, canonical CamelCase contract, schema pointer to canonical contract, and planned-path lineage; `NEEDS VERIFICATION` validator, fixture, policy, release, climate pipeline, aggregation receipt, and runtime behavior.

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Rules for maintainers](#rules-for-maintainers) · [Boundary reminder](#boundary-reminder) · [Validation posture](#validation-posture) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

Use the canonical contract:

[`./ClimateAnomaly.md`](./ClimateAnomaly.md)

That file is the authoritative Atmosphere/Air semantic contract for the `ClimateAnomaly` object family. It defines climate-anomaly meaning as a governed baseline-relative climate anomaly statement admitted as `CLIMATE_ANOMALY_CONTEXT`, not a raw observation, climate normal, forecast/model field, climate-attribution claim, hazard/impact proof, evidence proof, or release approval by itself.

The paired schema also points to the canonical CamelCase contract path:

```text
schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json
x-kfm.contract_doc = contracts/domains/atmosphere/ClimateAnomaly.md
```

---

## Why this file exists

This lowercase slug path existed as a planned scaffold sourced from `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md`. The live repo also contains the canonical CamelCase contract `contracts/domains/atmosphere/ClimateAnomaly.md`, which is already expanded and paired with:

```text
schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json
```

Because KFM treats contracts as authority-bearing semantic objects, this file must not duplicate, fork, or drift the climate-anomaly contract. It exists only to catch older links, slug-based references, or planned-path references and route them to the canonical file.

> [!IMPORTANT]
> This compatibility file is deliberately smaller than a full contract. A larger duplicate would weaken KFM source integrity by creating two locations that appear to define the same object meaning.

---

## Authoring-prompt treatment

The user-provided **KFM Repository Markdown Authoring Agent — Full Operating Prompt v2** was applied as the revision standard for this file. That prompt requires evidence-grounded Markdown, preservation of strong existing material, explicit uncertainty, no parallel authority, GitHub readability, validation posture, and rollback visibility.

No-loss preservation outcome:

| Existing element | Disposition | Reason |
|---|---|---|
| Lowercase planned scaffold | `REPLACE WITH POINTER` | The canonical expanded contract already exists. |
| Source reference to `FILE_SYSTEM_PLAN.md` | `KEEP + CLARIFY` | Preserves lineage while not treating planned paths as current authority. |
| Responsibility-root warning | `KEEP + STRENGTHEN` | Schema, policy, fixtures, release, evidence, tests, baseline review, and aggregation receipts stay in their own homes. |
| Canonical `ClimateAnomaly.md` link | `ADD / CONFIRM` | Prevents duplicate climate-anomaly authority. |
| Schema pointer | `ADD / CONFIRM` | The paired schema already points to the canonical CamelCase contract. |
| Baseline-anchor caution | `KEEP + SURFACE` | The canonical contract requires anomaly claims to anchor to ClimateNormal or equivalent baseline support. |
| Full authoring prompt text | `DO NOT PASTE` | It is operating guidance, not ClimateAnomaly object content. |
| Focus Mode consent sentence | `ROUTE ELSEWHERE` | It belongs to Focus Mode / consent documentation, not an Atmosphere climate-anomaly compatibility pointer. |

---

## Consent-pattern disposition

The user-provided sentence — “Here’s a compact, privacy-first consent pattern you can drop into KFM Focus Mode without bending doctrine...” — is **not** ClimateAnomaly object semantics.

It belongs in Focus Mode / consent documentation because it concerns consent-bound Focus Mode rendering, not Atmosphere baseline-relative climate anomaly meaning. The repository has a dedicated Focus Mode consent pattern note at:

```text
docs/focus-mode/CONSENT_PATTERN.md
```

This file may reference that pattern as related governance context, but it must not absorb it. ClimateAnomaly remains a baseline-relative climate-context contract; consent gates remain in consent / Focus Mode / policy responsibility roots.

---

## Rules for maintainers

- Do not add a second full climate-anomaly contract here.
- Do not point machine validators at this file as the climate-anomaly contract.
- Do not create a lowercase parallel schema solely for this compatibility path.
- Do not paste generic authoring prompts, Focus Mode consent patterns, or policy standards into this file as ClimateAnomaly semantics.
- Do not use this file as evidence proof, climate-attribution proof, trend-significance proof, policy approval, release approval, or climate-anomaly authority.
- Keep object semantics in `./ClimateAnomaly.md` unless an accepted ADR migrates the canonical contract path.
- If a future ADR changes the canonical climate-anomaly path, update this pointer, the paired schema `contract_doc`, README indexes, fixtures, validators, policy references, aggregation receipts, baseline references, and any release references together.

---

## Boundary reminder

`ClimateAnomaly` is a governed baseline-relative climate context object. It is not:

- a raw weather observation;
- a raw climate normal;
- a forecast or model field by default;
- a station record;
- a single event claim by itself;
- a climate attribution claim by itself;
- proof of cause, impact, hazard, damages, or trend significance by itself;
- an AQI report, AOD raster, smoke context, advisory, or air-quality measurement;
- a consent standard;
- a Focus Mode payload contract;
- an EvidenceBundle;
- a PolicyDecision;
- a ReleaseManifest;
- public release approval.

---

## Validation posture

| Check | Status |
|---|---|
| Lowercase compatibility file exists | `CONFIRMED` |
| Canonical expanded file exists at `./ClimateAnomaly.md` | `CONFIRMED` |
| Paired canonical schema exists at `../../../schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json` | `CONFIRMED` |
| Schema `x-kfm.contract_doc` points to `contracts/domains/atmosphere/ClimateAnomaly.md` | `CONFIRMED` |
| This file duplicates canonical climate-anomaly semantics | `NO — intentionally a pointer only` |
| This file is a consent pattern | `NO — consent pattern routed to Focus Mode / consent docs` |
| This file is climate attribution, trend significance, or impact proof | `NO` |
| This file is a public climate layer release approval | `NO` |
| This file is an EvidenceBundle or policy decision | `NO` |
| Validator behavior for ClimateAnomaly | `NEEDS VERIFICATION` |
| Fixture coverage for slug/CamelCase compatibility | `NEEDS VERIFICATION` |
| ADR resolving lowercase vs CamelCase contract naming | `NEEDS VERIFICATION` |

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/atmosphere/climate-anomaly.md` prior scaffold | `CONFIRMED repo evidence` | Lowercase path existed as a proposed scaffold sourced from `FILE_SYSTEM_PLAN.md`. | Did not define authoritative semantics. |
| `contracts/domains/atmosphere/ClimateAnomaly.md` | `CONFIRMED repo evidence` | Canonical climate-anomaly object contract exists and defines `ClimateAnomaly` as baseline-relative climate context, not raw observation, forecast, attribution proof, evidence proof, or release approval. | Schema/validator/policy enforcement remains `NEEDS VERIFICATION`. |
| `schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json` | `CONFIRMED scaffold schema` | Schema exists and `x-kfm.contract_doc` points to the canonical CamelCase contract. | Properties are still empty and `additionalProperties` is true. |
| `docs/focus-mode/CONSENT_PATTERN.md` | `CONFIRMED repo evidence` | Provides the Focus Mode consent pattern home for the pasted consent idea. | It is a draft documentation pattern; policy/runtime enforcement remains `NEEDS VERIFICATION`. |
| User-provided authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest, visually polished Markdown with no-loss preservation, validation, and rollback posture. | Prompt guidance, not repo implementation proof. |
| User-provided Focus Mode consent sentence | `CONFIRMED user-supplied source material` | Indicates desired consent-pattern content for Focus Mode. | Not ClimateAnomaly semantics; routed to Focus Mode / consent documentation. |

---

## Rollback

Rollback this pointer if an accepted ADR makes lowercase `climate-anomaly.md` the canonical climate-anomaly contract path and migrates every paired schema, contract reference, fixture, test, policy bundle, release reference, baseline reference, aggregation receipt, and README index accordingly.

Rollback this revision if it is misused to claim that this compatibility file is the canonical climate-anomaly contract, a consent standard, climate-attribution proof, trend-significance proof, impact proof, a policy decision, an EvidenceBundle, a ReleaseManifest, public climate-layer approval, or proof of runtime implementation.

Rollback target: prior scaffold blob SHA `8eebcc50c46ac5f5acd0f7e74ce18fd64651a59a`.

<p align="right"><a href="#top">Back to top</a></p>
