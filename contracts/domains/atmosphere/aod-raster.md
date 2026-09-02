<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://compat/contracts/domains/atmosphere/aod-raster
title: contracts/domains/atmosphere/aod-raster.md — AOD Raster Compatibility Pointer
type: compatibility-note
version: v0.1
status: draft
owners: OWNER_TBD — Atmosphere steward · Remote-sensing steward · Contract steward · Docs steward · Schema steward · Policy steward · Release steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; compatibility; aod-raster; no-parallel-authority; remote-sensing-mask
tags: [kfm, contracts, atmosphere, air, aod-raster, AODRaster, compatibility, casing, slug, no-parallel-authority, remote-sensing-mask, AOD-is-not-PM25, authoring-boundary, governance]
related:
  - ./AODRaster.md
  - ./SmokeContext.md
  - ./PM25Observation.md
  - ./AirObservation.md
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
  - ../../../schemas/contracts/v1/domains/atmosphere/AODRaster.schema.json
notes:
  - "This lowercase slug file existed as a planned scaffold sourced from FILE_SYSTEM_PLAN.md."
  - "The canonical expanded AOD-raster semantic contract is ./AODRaster.md."
  - "The paired schema contract_doc points to ./AODRaster.md, not this lowercase compatibility file."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance for this revision, not as content to paste into this compatibility pointer."
  - "The Focus Mode consent sentence belongs to Focus Mode / consent documentation and is referenced here only as an out-of-scope disposition."
  - "This file intentionally avoids duplicating AODRaster semantics so the repo does not grow two competing AOD-raster authorities."
  - "Schema, policy, fixtures, tests, evidence, consent enforcement, remote-sensing validation, and release decisions remain in their responsibility roots."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AOD Raster Compatibility Pointer

> Compatibility pointer for the lowercase planned path `contracts/domains/atmosphere/aod-raster.md`. This file exists to preserve older slug-style references while routing maintainers to the canonical `AODRaster` contract. It is **not** a second AOD-raster contract, not a consent pattern, and not a release authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Type: compatibility note" src="https://img.shields.io/badge/type-compatibility__note-blue">
  <img alt="Authority: pointer only" src="https://img.shields.io/badge/authority-pointer__only-lightgrey">
  <img alt="Canonical: AODRaster.md" src="https://img.shields.io/badge/canonical-AODRaster.md-purple">
  <img alt="No parallel authority" src="https://img.shields.io/badge/no__parallel__authority-required-critical">
  <img alt="AOD is not PM2.5" src="https://img.shields.io/badge/AOD_is_not-PM2.5-orange">
</p>

**Path:** `contracts/domains/atmosphere/aod-raster.md`  
**Canonical contract:** [`./AODRaster.md`](./AODRaster.md)  
**Status:** `draft` / compatibility note  
**Truth posture:** `CONFIRMED` lowercase file path, canonical CamelCase contract, schema pointer to canonical contract, and planned-path lineage; `NEEDS VERIFICATION` validator, fixture, policy, release, raster pipeline, and runtime behavior.

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Rules for maintainers](#rules-for-maintainers) · [Boundary reminder](#boundary-reminder) · [Validation posture](#validation-posture) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

Use the canonical contract:

[`./AODRaster.md`](./AODRaster.md)

That file is the authoritative Atmosphere/Air semantic contract for the `AODRaster` object family. It defines AOD-raster meaning as an aerosol optical depth raster or comparable remotely sensed aerosol-opacity field admitted as `REMOTE_SENSING_MASK`, not PM2.5 concentration, AQI, ground observation, forecast, health/safety guidance, evidence proof, or release approval by itself.

The paired schema also points to the canonical CamelCase contract path:

```text
schemas/contracts/v1/domains/atmosphere/AODRaster.schema.json
x-kfm.contract_doc = contracts/domains/atmosphere/AODRaster.md
```

---

## Why this file exists

This lowercase slug path existed as a planned scaffold sourced from `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md`. The live repo also contains the canonical CamelCase contract `contracts/domains/atmosphere/AODRaster.md`, which is already expanded and paired with:

```text
schemas/contracts/v1/domains/atmosphere/AODRaster.schema.json
```

Because KFM treats contracts as authority-bearing semantic objects, this file must not duplicate, fork, or drift the AOD-raster contract. It exists only to catch older links, slug-based references, or planned-path references and route them to the canonical file.

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
| Responsibility-root warning | `KEEP + STRENGTHEN` | Schema, policy, fixtures, release, evidence, tests, and remote-sensing validation stay in their own homes. |
| Canonical `AODRaster.md` link | `ADD / CONFIRM` | Prevents duplicate AOD-raster authority. |
| Schema pointer | `ADD / CONFIRM` | The paired schema already points to the canonical CamelCase contract. |
| AOD/PM2.5 caution | `KEEP + SURFACE` | The canonical contract and policy posture both require AOD not to be presented as PM2.5. |
| Full authoring prompt text | `DO NOT PASTE` | It is operating guidance, not AODRaster object content. |
| Focus Mode consent sentence | `ROUTE ELSEWHERE` | It belongs to Focus Mode / consent documentation, not an Atmosphere AOD-raster compatibility pointer. |

---

## Consent-pattern disposition

The user-provided sentence — “Here’s a compact, privacy-first consent pattern you can drop into KFM Focus Mode without bending doctrine...” — is **not** AODRaster object semantics.

It belongs in Focus Mode / consent documentation because it concerns consent-bound Focus Mode rendering, not Atmosphere AOD remote-sensing mask meaning. The repository has a dedicated Focus Mode consent pattern note at:

```text
docs/focus-mode/CONSENT_PATTERN.md
```

This file may reference that pattern as related governance context, but it must not absorb it. AODRaster remains a remote-sensing mask/proxy contract; consent gates remain in consent / Focus Mode / policy responsibility roots.

---

## Rules for maintainers

- Do not add a second full AOD-raster contract here.
- Do not point machine validators at this file as the AOD-raster contract.
- Do not create a lowercase parallel schema solely for this compatibility path.
- Do not paste generic authoring prompts, Focus Mode consent patterns, or policy standards into this file as AODRaster semantics.
- Do not use this file as evidence proof, PM2.5 proof, AQI proof, policy approval, release approval, or AOD-raster authority.
- Keep object semantics in `./AODRaster.md` unless an accepted ADR migrates the canonical contract path.
- If a future ADR changes the canonical AOD-raster path, update this pointer, the paired schema `contract_doc`, README indexes, fixtures, validators, policy references, and any release references together.

---

## Boundary reminder

`AODRaster` is a governed remote-sensing mask/proxy object. It is not:

- a PM2.5 measurement;
- an AQI report;
- a ground sensor observation;
- a regulatory archive measurement by default;
- a forecast field by default;
- an advisory or health/safety instruction;
- proof of smoke exposure, health effect, visibility impact, or ground-level concentration;
- a public tile, map layer, or published raster by default;
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
| Canonical expanded file exists at `./AODRaster.md` | `CONFIRMED` |
| Paired canonical schema exists at `../../../schemas/contracts/v1/domains/atmosphere/AODRaster.schema.json` | `CONFIRMED` |
| Schema `x-kfm.contract_doc` points to `contracts/domains/atmosphere/AODRaster.md` | `CONFIRMED` |
| This file duplicates canonical AOD-raster semantics | `NO — intentionally a pointer only` |
| This file is a consent pattern | `NO — consent pattern routed to Focus Mode / consent docs` |
| This file is PM2.5 proof or AQI proof | `NO` |
| This file is a public raster release approval | `NO` |
| This file is an EvidenceBundle or policy decision | `NO` |
| Validator behavior for AODRaster | `NEEDS VERIFICATION` |
| Fixture coverage for slug/CamelCase compatibility | `NEEDS VERIFICATION` |
| ADR resolving lowercase vs CamelCase contract naming | `NEEDS VERIFICATION` |

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/atmosphere/aod-raster.md` prior scaffold | `CONFIRMED repo evidence` | Lowercase path existed as a proposed scaffold sourced from `FILE_SYSTEM_PLAN.md`. | Did not define authoritative semantics. |
| `contracts/domains/atmosphere/AODRaster.md` | `CONFIRMED repo evidence` | Canonical AOD-raster object contract exists and defines `AODRaster` as remote-sensing mask/proxy, not PM2.5, AQI, ground observation, evidence proof, or release approval. | Schema/validator/policy enforcement remains `NEEDS VERIFICATION`. |
| `schemas/contracts/v1/domains/atmosphere/AODRaster.schema.json` | `CONFIRMED scaffold schema` | Schema exists and `x-kfm.contract_doc` points to the canonical CamelCase contract. | Properties are still empty and `additionalProperties` is true. |
| `docs/focus-mode/CONSENT_PATTERN.md` | `CONFIRMED repo evidence` | Provides the Focus Mode consent pattern home for the pasted consent idea. | It is a draft documentation pattern; policy/runtime enforcement remains `NEEDS VERIFICATION`. |
| User-provided authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest, visually polished Markdown with no-loss preservation, validation, and rollback posture. | Prompt guidance, not repo implementation proof. |
| User-provided Focus Mode consent sentence | `CONFIRMED user-supplied source material` | Indicates desired consent-pattern content for Focus Mode. | Not AODRaster semantics; routed to Focus Mode / consent documentation. |

---

## Rollback

Rollback this pointer if an accepted ADR makes lowercase `aod-raster.md` the canonical AOD-raster contract path and migrates every paired schema, contract reference, fixture, test, policy bundle, release reference, and README index accordingly.

Rollback this revision if it is misused to claim that this compatibility file is the canonical AOD-raster contract, a consent standard, PM2.5 proof, AQI proof, a policy decision, an EvidenceBundle, a ReleaseManifest, public raster approval, or proof of runtime implementation.

Rollback target: prior scaffold blob SHA `0134b7d72544771dc24f1b095ea5f96fff44d12e`.

<p align="right"><a href="#top">Back to top</a></p>
