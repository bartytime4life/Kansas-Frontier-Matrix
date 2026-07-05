# `schemas/people-dna-land/` — People / DNA / Land Schema Compatibility Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-people-dna-land-readme
title: schemas/people-dna-land/ README
type: readme; compatibility-index; schema-boundary
version: v0.1
status: draft; root-level-people-dna-land-compatibility-path; restricted-review; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: restricted-review
tags: [kfm, schemas, people-dna-land, people, dna, land, compatibility, restricted-review]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/people-dna-land/` is a root-level compatibility guardrail for People / DNA / Land schema placement.

The inspected versioned People / DNA / Land domain schema lane lives at `schemas/contracts/v1/domains/people-dna-land/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct files found under this root-level path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Default posture | restricted-review |

## Boundary

This folder is under `schemas/`, so it may contain machine-checkable shape material only if accepted here.

It is not the active v1 People / DNA / Land schema family, policy root, consent root, identity store, data root, fixture root, validator root, runtime root, public API root, map root, or release root.

Schema validation here does not prove identity, consent, genealogy, DNA-derived relation, land ownership, title status, policy compliance, release readiness, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/people-dna-land/README.md` | present | Empty file expanded by this README. |
| `schemas/people-dna-land/*` | not found in current search | No direct schema files were found under this root-level path. |
| `schemas/contracts/v1/domains/people-dna-land/README.md` | present | Inspected v1 People / DNA / Land domain schema index. |
| `schemas/contracts/v1/domains/people-dna-land/people/README.md` | present | Transitional child warning index according to the parent domain README. |
| `schemas/contracts/v1/domains/people-dna-land/genealogy/README.md` | present | Transitional child warning index according to the parent domain README. |
| `schemas/contracts/v1/domains/people-dna-land/land-ownership/README.md` | present | Transitional child warning index according to the parent domain README. |

## What belongs here

- This README.
- Compatibility notes for this root-level path.
- Migration notes if People / DNA / Land schema placement changes.
- Temporary mirror notes while placement is unresolved.

## What does not belong here

- New canonical v1 People / DNA / Land schemas while `schemas/contracts/v1/domains/people-dna-land/` remains the active lane.
- Person stores, identity-truth stores, DNA-derived relation records, consent records, land-title opinions, legal determinations, public map outputs, or generated-answer artifacts.
- Policy rules, data records, proof outputs, fixtures, validator code, runtime code, release records, or public API/UI behavior.
- Claims that identity, consent, genealogy, DNA relation, land ownership, title status, policy compliance, or public readiness occurred merely because an object validates against a schema.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep v1 lane visible | Prefer `schemas/contracts/v1/domains/people-dna-land/` for v1 People / DNA / Land schema work. |
| Do not create parallel authority | This root-level path must not evolve into a second domain schema home without migration review. |
| Restricted-review default | Identity, consent, DNA-derived, genealogy, land-link, and title-like surfaces require restricted review before promotion. |
| Shape is not truth | Schema validation constrains object shape; it does not prove identity, relationship, consent, ownership, title, or publication readiness. |
| Placement before promotion | Move, retire, or retain this root-level path only after path and ownership review. |

## Validation

```bash
find schemas/people-dna-land -maxdepth 4 -type f | sort
find schemas/contracts/v1/domains/people-dna-land -maxdepth 4 -type f | sort
find schemas/people-dna-land -name '*.json' -print0 | xargs -0 -r -I{} python -m json.tool {} >/dev/null
```

## Open questions

| Question | Status |
|---|---|
| Should `schemas/people-dna-land/` remain as a compatibility index or be retired after migration? | NEEDS VERIFICATION |
| Should all accepted schema files live only under `schemas/contracts/v1/domains/people-dna-land/`? | NEEDS VERIFICATION |
| Which synthetic examples and tests support future People / DNA / Land schemas? | NEEDS VERIFICATION |
| Which consent, policy, release, correction, and rollback references are required before any public-facing output? | NEEDS VERIFICATION |
