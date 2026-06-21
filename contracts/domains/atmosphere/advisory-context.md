<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://compat/contracts/domains/atmosphere/advisory-context
title: contracts/domains/atmosphere/advisory-context.md — Advisory Context Compatibility Pointer
type: compatibility-note
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Contract steward · Docs steward · Schema steward · Policy steward · Release steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; compatibility; advisory-context; no-parallel-authority
tags: [kfm, contracts, atmosphere, air, advisory-context, compatibility, casing, slug, no-parallel-authority, authoring-boundary, governance]
related:
  - ./AdvisoryContext.md
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/focus-mode/CONSENT_PATTERN.md
  - ../../../schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json
notes:
  - "This lowercase slug file existed as a planned scaffold sourced from FILE_SYSTEM_PLAN.md."
  - "The canonical expanded advisory-context semantic contract is ./AdvisoryContext.md."
  - "The paired schema contract_doc points to ./AdvisoryContext.md, not this lowercase compatibility file."
  - "The user-provided Markdown Authoring Agent v2 prompt is treated as authoring guidance for this revision, not as content to paste into this compatibility pointer."
  - "The Focus Mode consent sentence belongs to Focus Mode / consent documentation and is referenced here only as an out-of-scope disposition."
  - "This file intentionally avoids duplicating advisory semantics so the repo does not grow two competing advisory-context authorities."
  - "Schema, policy, fixtures, tests, evidence, consent enforcement, and release decisions remain in their responsibility roots."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Advisory Context Compatibility Pointer

> Compatibility pointer for the lowercase planned path `contracts/domains/atmosphere/advisory-context.md`. This file exists to preserve older slug-style references while routing maintainers to the canonical `AdvisoryContext` contract. It is **not** a second advisory contract, not a consent pattern, and not a release authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Type: compatibility note" src="https://img.shields.io/badge/type-compatibility__note-blue">
  <img alt="Authority: pointer only" src="https://img.shields.io/badge/authority-pointer__only-lightgrey">
  <img alt="Canonical: AdvisoryContext.md" src="https://img.shields.io/badge/canonical-AdvisoryContext.md-purple">
  <img alt="No parallel authority" src="https://img.shields.io/badge/no__parallel__authority-required-critical">
</p>

**Path:** `contracts/domains/atmosphere/advisory-context.md`  
**Canonical contract:** [`./AdvisoryContext.md`](./AdvisoryContext.md)  
**Status:** `draft` / compatibility note  
**Truth posture:** `CONFIRMED` lowercase file path, canonical CamelCase contract, schema pointer to canonical contract, and planned-path lineage; `NEEDS VERIFICATION` validator, fixture, policy, release, and runtime behavior.

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Authoring-prompt treatment](#authoring-prompt-treatment) · [Consent-pattern disposition](#consent-pattern-disposition) · [Rules for maintainers](#rules-for-maintainers) · [Boundary reminder](#boundary-reminder) · [Validation posture](#validation-posture) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

Use the canonical contract:

[`./AdvisoryContext.md`](./AdvisoryContext.md)

That file is the authoritative Atmosphere/Air semantic contract for the `AdvisoryContext` object family. It defines advisory-context meaning as `ALERT_AND_ADVISORY_CONTEXT`: a governed referral to an authoritative advisory source, not KFM-generated emergency guidance, life-safety instruction, forecast substitution, source substitution, evidence proof, or release approval.

The paired schema also points to the canonical CamelCase contract path:

```text
schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json
x-kfm.contract_doc = contracts/domains/atmosphere/AdvisoryContext.md
```

---

## Why this file exists

This lowercase slug path existed as a planned scaffold sourced from `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md`. The live repo also contains the canonical CamelCase contract `contracts/domains/atmosphere/AdvisoryContext.md`, which is already expanded and paired with:

```text
schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json
```

Because KFM treats contracts as authority-bearing semantic objects, this file must not duplicate, fork, or drift the advisory contract. It exists only to catch older links, slug-based references, or planned-path references and route them to the canonical file.

> [!IMPORTANT]
> This compatibility file is deliberately smaller than a full contract. A larger duplicate would weaken KFM source integrity by creating two locations that appear to define the same object meaning.

---

## Authoring-prompt treatment

The user-provided **KFM Repository Markdown Authoring Agent — Full Operating Prompt v2** was applied as the revision standard for this file. That prompt requires evidence-grounded Markdown, preservation of strong existing material, explicit uncertainty, no parallel authority, GitHub readability, validation posture, and rollback visibility.

No-loss preservation outcome:

| Existing element | Disposition | Reason |
|---|---|---|
| Compatibility-pointer purpose | `KEEP + CLARIFY` | This is the safest role for the lowercase slug file. |
| Canonical `AdvisoryContext.md` link | `KEEP` | Prevents duplicate advisory authority. |
| No-parallel-schema warning | `KEEP + STRENGTHEN` | The paired schema already points to the canonical CamelCase contract. |
| Advisory boundary reminder | `KEEP + CLARIFY` | Preserves the life-safety / official-source anti-collapse rule. |
| Validation posture | `KEEP + EXPAND` | Makes implementation uncertainty visible. |
| Rollback target | `KEEP` | Preserves reversibility. |
| Full authoring prompt text | `DO NOT PASTE` | It is operating guidance, not AdvisoryContext object content. |
| Focus Mode consent sentence | `ROUTE ELSEWHERE` | It belongs to Focus Mode / consent documentation, not an Atmosphere advisory compatibility pointer. |

---

## Consent-pattern disposition

The user-provided sentence — “Here’s a compact, privacy-first consent pattern you can drop into KFM Focus Mode without bending doctrine...” — is **not** AdvisoryContext object semantics.

It belongs in Focus Mode / consent documentation because it concerns consent-bound Focus Mode rendering, not Atmosphere advisory referral meaning. The repository now has a dedicated Focus Mode consent pattern note at:

```text
docs/focus-mode/CONSENT_PATTERN.md
```

This file may reference that pattern as related governance context, but it must not absorb it. AdvisoryContext remains referral context for authoritative advisories; consent gates remain in consent / Focus Mode / policy responsibility roots.

---

## Rules for maintainers

- Do not add a second full advisory contract here.
- Do not point machine validators at this file as the advisory contract.
- Do not create a lowercase parallel schema solely for this compatibility path.
- Do not paste generic authoring prompts, Focus Mode consent patterns, or policy standards into this file as advisory semantics.
- Do not use this file as evidence proof, policy approval, release approval, or public-advisory authority.
- Keep object semantics in `./AdvisoryContext.md` unless an accepted ADR migrates the canonical contract path.
- If a future ADR changes the canonical advisory-context path, update this pointer, the paired schema `contract_doc`, README indexes, fixtures, validators, and any release references together.

---

## Boundary reminder

`AdvisoryContext` is referral context only. It is not:

- a life-safety directive;
- an emergency instruction;
- an official warning issued by KFM;
- a forecast/model field;
- an observation;
- a PM2.5, ozone, AQI, smoke, AOD, wind, precipitation, or temperature measurement;
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
| Canonical expanded file exists at `./AdvisoryContext.md` | `CONFIRMED` |
| Paired canonical schema exists at `../../../schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json` | `CONFIRMED` |
| Schema `x-kfm.contract_doc` points to `contracts/domains/atmosphere/AdvisoryContext.md` | `CONFIRMED` |
| This file duplicates canonical advisory semantics | `NO — intentionally a pointer only` |
| This file is a consent pattern | `NO — consent pattern routed to Focus Mode / consent docs` |
| This file is a public release approval | `NO` |
| This file is an EvidenceBundle or policy decision | `NO` |
| Validator behavior for advisory context | `NEEDS VERIFICATION` |
| Fixture coverage for slug/CamelCase compatibility | `NEEDS VERIFICATION` |
| ADR resolving lowercase vs CamelCase contract naming | `NEEDS VERIFICATION` |

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/atmosphere/advisory-context.md` prior version | `CONFIRMED repo evidence` | Lowercase compatibility file existed and already pointed to canonical `AdvisoryContext.md`. | Did not fully document prompt treatment or consent-pattern disposition. |
| `contracts/domains/atmosphere/AdvisoryContext.md` | `CONFIRMED repo evidence` | Canonical advisory object contract exists and defines `AdvisoryContext` as `ALERT_AND_ADVISORY_CONTEXT`, not life-safety instruction or release approval. | Schema/validator/policy enforcement remains `NEEDS VERIFICATION`. |
| `schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json` | `CONFIRMED scaffold schema` | Schema exists and `x-kfm.contract_doc` points to the canonical CamelCase contract. | Properties are still empty and `additionalProperties` is true. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | `CONFIRMED lineage / plan evidence` | Explains that planned file paths were proposed and required verification against repo evidence. | Plan status does not override current repo implementation evidence. |
| User-provided authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest, visually polished Markdown with no-loss preservation, validation, and rollback posture. | Prompt guidance, not repo implementation proof. |
| User-provided Focus Mode consent sentence | `CONFIRMED user-supplied source material` | Indicates desired consent-pattern content for Focus Mode. | Not advisory-context semantics; routed to Focus Mode / consent documentation. |

---

## Rollback

Rollback this pointer if an accepted ADR makes lowercase `advisory-context.md` the canonical advisory-context contract path and migrates every paired schema, contract reference, fixture, test, policy bundle, release reference, and README index accordingly.

Rollback this revision if it is misused to claim that this compatibility file is the canonical advisory contract, a consent standard, a policy decision, an EvidenceBundle, a ReleaseManifest, or proof of runtime implementation.

Rollback target: prior compatibility-pointer blob SHA `7b22cf2503867df291a1f546bce0aaed1e20792b`.

<p align="right"><a href="#top">Back to top</a></p>
