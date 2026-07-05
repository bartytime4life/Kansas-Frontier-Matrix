# `schemas/governance/` — Governance Schema Compatibility Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-governance-readme
title: schemas/governance/ README
type: readme; compatibility-index; schema-boundary
version: v0.1
status: draft; root-level-governance-compatibility-path; scaffold-files-present; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, governance, compatibility, consent-receipt, overlay-pointer]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/governance/` is a root-level compatibility guardrail for governance-related schema scaffolds.

The inspected v1 governance schema family lives at `schemas/contracts/v1/governance/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct schema files found | `overlay_pointer.schema.json`, `consent_receipt.schema.json` |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |

## Boundary

This folder is under `schemas/`, so it may contain machine-checkable shape material only if accepted here.

It is not the active v1 governance schema family, a policy root, data root, consent authority, fixture root, validator root, runtime root, or release root.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/governance/README.md` | present | Empty file expanded by this README. |
| `schemas/governance/overlay_pointer.schema.json` | PROPOSED scaffold | Empty `properties`; `additionalProperties: true`; source doc points to People-DNA-Land DNA sublane docs. |
| `schemas/governance/consent_receipt.schema.json` | PROPOSED scaffold | Empty `properties`; `additionalProperties: true`; source docs point to People-DNA-Land API and DNA sublane docs. |
| `schemas/contracts/v1/governance/README.md` | present | Inspected v1 governance schema family index. |

## What belongs here

- This README.
- Compatibility notes for this root-level path.
- Migration notes for governance schema scaffolds if placement changes.
- Temporary mirror notes if these files are moved under a versioned schema lane.

## What does not belong here

- New canonical v1 governance schemas while `schemas/contracts/v1/governance/` remains the active lane.
- Policy rules, data records, consent records, emitted review records, proof outputs, fixtures, validator code, runtime code, or release records.
- Claims that governance review, consent, approval, policy compliance, or release readiness occurred merely because an object validates against a schema.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep v1 lane visible | Prefer `schemas/contracts/v1/governance/` for v1 governance schema work. |
| Do not create parallel authority | Root-level scaffolds must not evolve into a second governance schema home without migration review. |
| Shape is not governance proof | Schema validation constrains object shape; it does not prove review, consent, or approval. |
| Placement before promotion | Move, retire, or retain these scaffolds only after path and ownership review. |

## Validation

```bash
find schemas/governance -maxdepth 4 -type f | sort
find schemas/contracts/v1/governance -maxdepth 4 -type f | sort
find schemas/governance -name '*.json' -print0 | xargs -0 -r -I{} python -m json.tool {} >/dev/null
```

## Open questions

| Question | Status |
|---|---|
| Should `overlay_pointer.schema.json` move under `schemas/contracts/v1/governance/`, `schemas/contracts/v1/ui/`, or another accepted lane? | NEEDS VERIFICATION |
| Should `consent_receipt.schema.json` move under governance, receipts, policy, People-DNA-Land, or another accepted lane? | NEEDS VERIFICATION |
| Should `schemas/governance/` remain as a compatibility index or be retired after migration? | NEEDS VERIFICATION |
| Which examples and tests support these scaffolds? | NEEDS VERIFICATION |
