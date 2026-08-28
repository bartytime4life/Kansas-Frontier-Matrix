<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://compat/contracts/domains/atmosphere/air-observation
title: contracts/domains/atmosphere/air-observation.md — Air Observation Compatibility Pointer
type: compatibility-note
version: v0.1
status: draft
owners: OWNER_TBD — Atmosphere steward · Air-quality steward · Contract steward · Docs steward · Schema steward · Policy steward · Release steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; compatibility; air-observation; no-parallel-authority
tags: [kfm, contracts, atmosphere, air, air-observation, compatibility, casing, slug, no-parallel-authority, authoring-boundary, governance]
related:
  - ./AirObservation.md
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
  - ../../../schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json
notes:
  - "This lowercase slug file existed as a planned scaffold sourced from FILE_SYSTEM_PLAN.md."
  - "The canonical expanded air-observation semantic contract is ./AirObservation.md."
  - "The paired schema contract_doc points to ./AirObservation.md, not this lowercase compatibility file."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance for this revision, not as content to paste into this compatibility pointer."
  - "The Focus Mode consent sentence belongs to Focus Mode / consent documentation and is referenced here only as an out-of-scope disposition."
  - "This file intentionally avoids duplicating air-observation semantics so the repo does not grow two competing air-observation authorities."
  - "Schema, policy, fixtures, tests, evidence, consent enforcement, and release decisions remain in their responsibility roots."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Air Observation Compatibility Pointer

> Compatibility pointer for the lowercase planned path `contracts/domains/atmosphere/air-observation.md`. This file exists to preserve older slug-style references while routing maintainers to the canonical `AirObservation` contract. It is **not** a second air-observation contract, not a consent pattern, and not a release authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Type: compatibility note" src="https://img.shields.io/badge/type-compatibility__note-blue">
  <img alt="Authority: pointer only" src="https://img.shields.io/badge/authority-pointer__only-lightgrey">
  <img alt="Canonical: AirObservation.md" src="https://img.shields.io/badge/canonical-AirObservation.md-purple">
  <img alt="No parallel authority" src="https://img.shields.io/badge/no__parallel__authority-required-critical">
</p>

**Path:** `contracts/domains/atmosphere/air-observation.md`  
**Canonical contract:** [`./AirObservation.md`](./AirObservation.md)  
**Status:** `draft` / compatibility note  
**Truth posture:** `CONFIRMED` lowercase file path, canonical CamelCase contract, schema pointer to canonical contract, and planned-path lineage; `NEEDS VERIFICATION` validator, fixture, policy, release, and runtime behavior.

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Rules for maintainers](#rules-for-maintainers) · [Boundary reminder](#boundary-reminder) · [Validation posture](#validation-posture) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

Use the canonical contract:

[`./AirObservation.md`](./AirObservation.md)

That file is the authoritative Atmosphere/Air semantic contract for the `AirObservation` object family. It defines air-observation meaning as a governed general air-quality observation tied to an `AirStation` or comparable station/network context, not PM2.5, ozone, AQI, model output, advisory guidance, evidence proof, or release approval by itself.

The paired schema also points to the canonical CamelCase contract path:

```text
schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json
x-kfm.contract_doc = contracts/domains/atmosphere/AirObservation.md
```

---

## Why this file exists

This lowercase slug path existed as a planned scaffold sourced from `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md`. The live repo also contains the canonical CamelCase contract `contracts/domains/atmosphere/AirObservation.md`, which is already expanded and paired with:

```text
schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json
```

Because KFM treats contracts as authority-bearing semantic objects, this file must not duplicate, fork, or drift the air-observation contract. It exists only to catch older links, slug-based references, or planned-path references and route them to the canonical file.

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
| Responsibility-root warning | `KEEP + STRENGTHEN` | Schema, policy, fixtures, release, evidence, and tests stay in their own homes. |
| Canonical `AirObservation.md` link | `ADD / CONFIRM` | Prevents duplicate air-observation authority. |
| Schema pointer | `ADD / CONFIRM` | The paired schema already points to the canonical CamelCase contract. |
| Full authoring prompt text | `DO NOT PASTE` | It is operating guidance, not AirObservation object content. |
| Focus Mode consent sentence | `ROUTE ELSEWHERE` | It belongs to Focus Mode / consent documentation, not an Atmosphere air-observation compatibility pointer. |

---

## Consent-pattern disposition

The user-provided sentence — “Here’s a compact, privacy-first consent pattern you can drop into KFM Focus Mode without bending doctrine...” — is **not** AirObservation object semantics.

It belongs in Focus Mode / consent documentation because it concerns consent-bound Focus Mode rendering, not Atmosphere air-quality observation meaning. The repository has a dedicated Focus Mode consent pattern note at:

```text
docs/focus-mode/CONSENT_PATTERN.md
```

This file may reference that pattern as related governance context, but it must not absorb it. AirObservation remains an air-quality observation contract; consent gates remain in consent / Focus Mode / policy responsibility roots.

---

## Rules for maintainers

- Do not add a second full air-observation contract here.
- Do not point machine validators at this file as the air-observation contract.
- Do not create a lowercase parallel schema solely for this compatibility path.
- Do not paste generic authoring prompts, Focus Mode consent patterns, or policy standards into this file as air-observation semantics.
- Do not use this file as evidence proof, policy approval, release approval, or air-quality observation authority.
- Keep object semantics in `./AirObservation.md` unless an accepted ADR migrates the canonical contract path.
- If a future ADR changes the canonical air-observation path, update this pointer, the paired schema `contract_doc`, README indexes, fixtures, validators, and any release references together.

---

## Boundary reminder

`AirObservation` is a governed air-quality observation object. It is not:

- a PM2.5 observation unless represented by the dedicated PM2.5 object or accepted pollutant-specific role;
- an ozone observation unless represented by the dedicated ozone object or accepted pollutant-specific role;
- an AQI report;
- a low-cost sensor record without caveats when that role applies;
- a model field;
- an AOD raster or smoke mask;
- an advisory or health/safety instruction;
- proof of exposure, health effect, regulatory exceedance, or impact by itself;
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
| Canonical expanded file exists at `./AirObservation.md` | `CONFIRMED` |
| Paired canonical schema exists at `../../../schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json` | `CONFIRMED` |
| Schema `x-kfm.contract_doc` points to `contracts/domains/atmosphere/AirObservation.md` | `CONFIRMED` |
| This file duplicates canonical air-observation semantics | `NO — intentionally a pointer only` |
| This file is a consent pattern | `NO — consent pattern routed to Focus Mode / consent docs` |
| This file is a public release approval | `NO` |
| This file is an EvidenceBundle or policy decision | `NO` |
| Validator behavior for air observation | `NEEDS VERIFICATION` |
| Fixture coverage for slug/CamelCase compatibility | `NEEDS VERIFICATION` |
| ADR resolving lowercase vs CamelCase contract naming | `NEEDS VERIFICATION` |

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/atmosphere/air-observation.md` prior scaffold | `CONFIRMED repo evidence` | Lowercase path existed as a proposed scaffold sourced from `FILE_SYSTEM_PLAN.md`. | Did not define authoritative semantics. |
| `contracts/domains/atmosphere/AirObservation.md` | `CONFIRMED repo evidence` | Canonical air-observation object contract exists and defines `AirObservation` as a general air-quality observation tied to station/network context. | Schema/validator/policy enforcement remains `NEEDS VERIFICATION`. |
| `schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json` | `CONFIRMED scaffold schema` | Schema exists and `x-kfm.contract_doc` points to the canonical CamelCase contract. | Properties are still empty and `additionalProperties` is true. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | `CONFIRMED lineage / plan evidence` | Explains that planned file paths were proposed and required verification against repo evidence. | Plan status does not override current repo implementation evidence. |
| `docs/focus-mode/CONSENT_PATTERN.md` | `CONFIRMED repo evidence` | Provides the Focus Mode consent pattern home for the pasted consent idea. | It is a draft documentation pattern; policy/runtime enforcement remains `NEEDS VERIFICATION`. |
| User-provided authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest, visually polished Markdown with no-loss preservation, validation, and rollback posture. | Prompt guidance, not repo implementation proof. |
| User-provided Focus Mode consent sentence | `CONFIRMED user-supplied source material` | Indicates desired consent-pattern content for Focus Mode. | Not air-observation semantics; routed to Focus Mode / consent documentation. |

---

## Rollback

Rollback this pointer if an accepted ADR makes lowercase `air-observation.md` the canonical air-observation contract path and migrates every paired schema, contract reference, fixture, test, policy bundle, release reference, and README index accordingly.

Rollback this revision if it is misused to claim that this compatibility file is the canonical air-observation contract, a consent standard, a policy decision, an EvidenceBundle, a ReleaseManifest, or proof of runtime implementation.

Rollback target: prior scaffold blob SHA `aee3a7f6673e6e65f3b387f1b681acffac4b5861`.

<p align="right"><a href="#top">Back to top</a></p>
