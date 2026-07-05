# `schemas/contracts/v1/spatial-foundation/` — Spatial Foundation Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-spatial-foundation-readme
title: schemas/contracts/v1/spatial-foundation/ README
type: readme; schema-family-index; compatibility-index
version: v0.1
status: draft; empty-schema-family; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, contracts-v1, spatial-foundation, spatial, geometry, map, layers, common]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/contracts/v1/spatial-foundation/` is a draft placeholder for possible shared spatial foundation schema shapes.

This README is a placement guardrail only. It does not make this path canonical.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct schema files | not found in current search |
| Current role | README-only guardrail |
| Placement | NEEDS VERIFICATION |

## Adjacent schema lanes

| Path | Role |
|---|---|
| `schemas/contracts/v1/common/` | Shared reusable schema families. |
| `schemas/contracts/v1/map/` | Map-facing object shapes. |
| `schemas/contracts/v1/layers/` | Layer object shapes. |
| `schemas/contracts/v1/domains/<domain>/` | Domain-specific object shapes and profiles. |

## Boundary

This folder is under `schemas/`, so it may only contain machine-checkable shape material if accepted later.

It is not a data root, code root, fixture root, map runtime root, or domain authority root.

## What belongs here

- This README.
- Future shared spatial schema files only after placement review.
- Notes that prevent duplicate spatial definitions across common, map, layers, and domain schema lanes.

## What does not belong here

- Domain-specific schema definitions owned by a domain lane.
- Map or layer schema definitions owned by map or layer lanes.
- Geometry payloads, feature data, fixtures, validator code, runtime code, or generated outputs.

## Candidate shapes

These are only candidates, not confirmed files:

| Candidate | Status |
|---|---|
| `geometry_ref.schema.json` | NEEDS VERIFICATION |
| `spatial_extent.schema.json` | NEEDS VERIFICATION |
| `crs_ref.schema.json` | NEEDS VERIFICATION |
| `spatial_identity_key.schema.json` | NEEDS VERIFICATION |
| `location_precision.schema.json` | NEEDS VERIFICATION |

## Validation

```bash
find schemas/contracts/v1/spatial-foundation -maxdepth 3 -type f | sort

find schemas/contracts/v1/spatial-foundation -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null
```

## Open questions

| Question | Status |
|---|---|
| Should this folder remain README-only? | NEEDS VERIFICATION |
| Should shared spatial primitives live here or under `common/`? | NEEDS VERIFICATION |
| Should map/layer-facing shapes remain under `map/` and `layers/`? | NEEDS VERIFICATION |
| Which contracts, fixtures, validators, and tests would support any future schema here? | NEEDS VERIFICATION |
