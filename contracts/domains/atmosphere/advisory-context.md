<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://compat/contracts/domains/atmosphere/advisory-context
title: contracts/domains/atmosphere/advisory-context.md — Advisory Context Compatibility Pointer
type: compatibility-note
version: v0.1
status: draft
owners: OWNER_TBD — Atmosphere steward · Contract steward · Docs steward · Schema steward · Policy steward · Release steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; compatibility; advisory-context; no-parallel-authority
tags: [kfm, contracts, atmosphere, air, advisory-context, compatibility, casing, slug, no-parallel-authority, governance]
related:
  - ./AdvisoryContext.md
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json
notes:
  - "This lowercase slug file existed as a planned scaffold sourced from FILE_SYSTEM_PLAN.md."
  - "The canonical expanded advisory-context semantic contract is ./AdvisoryContext.md."
  - "This file intentionally avoids duplicating advisory semantics so the repo does not grow two competing advisory-context authorities."
  - "Schema, policy, fixtures, tests, evidence, and release decisions remain in their responsibility roots."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Advisory Context Compatibility Pointer

> Compatibility pointer for the lowercase planned path `contracts/domains/atmosphere/advisory-context.md`.

## Canonical authority

Use the canonical contract:

[`./AdvisoryContext.md`](./AdvisoryContext.md)

That file is the authoritative Atmosphere/Air semantic contract for the `AdvisoryContext` object family. It defines advisory-context meaning as `ALERT_AND_ADVISORY_CONTEXT`: a governed referral to an authoritative advisory source, not KFM-generated emergency guidance, life-safety instruction, forecast substitution, source substitution, evidence proof, or release approval.

## Why this file exists

This lowercase slug path existed as a planned scaffold sourced from `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md`. Current repo evidence also contains the canonical CamelCase contract `contracts/domains/atmosphere/AdvisoryContext.md`, which is already expanded and paired with:

```text
schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json
```

Because KFM treats contracts as authority-bearing semantic objects, this file must not duplicate or fork the advisory contract. It exists only to catch older links, slug-based references, or planned-path references and route them to the canonical file.

## Rules for maintainers

- Do not add a second full advisory contract here.
- Do not point machine validators at this file as the advisory contract.
- Do not create a lowercase parallel schema solely for this compatibility path.
- Do not use this file as evidence proof, policy approval, release approval, or public-advisory authority.
- Keep object semantics in `./AdvisoryContext.md` unless an accepted ADR migrates the canonical contract path.
- If a future ADR changes the canonical advisory-context path, update this pointer and the paired schema `contract_doc` together.

## Boundary reminder

`AdvisoryContext` is referral context only. It is not:

- a life-safety directive;
- an emergency instruction;
- an official warning issued by KFM;
- a forecast/model field;
- an observation;
- a PM2.5, ozone, AQI, smoke, AOD, wind, precipitation, or temperature measurement;
- an EvidenceBundle;
- a PolicyDecision;
- a ReleaseManifest;
- public release approval.

## Validation posture

| Check | Status |
|---|---|
| Lowercase compatibility file exists | `CONFIRMED` |
| Canonical expanded file exists at `./AdvisoryContext.md` | `CONFIRMED` |
| Paired canonical schema exists at `../../../schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json` | `CONFIRMED from canonical contract evidence; schema enforcement still needs verification` |
| This file duplicates canonical advisory semantics | `NO — intentionally a pointer only` |
| This file is a public release approval | `NO` |
| This file is an EvidenceBundle or policy decision | `NO` |

## Rollback

Rollback this pointer if an accepted ADR makes lowercase `advisory-context.md` the canonical advisory-context contract path and migrates every paired schema, contract reference, fixture, test, policy bundle, release reference, and README index accordingly.

Rollback target: prior scaffold blob SHA `329d5f5889af81fbda2fac9aca1be5ed3ac93ad2`.

<p align="right"><a href="#top">Back to top</a></p>
