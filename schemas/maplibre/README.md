# `schemas/maplibre/` — MapLibre Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-maplibre-readme
title: schemas/maplibre/ README
type: readme; compatibility-index; schema-boundary
version: v0.1
status: draft; root-level-maplibre-schema-path; scaffold-files-present; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, maplibre, map, layers, rendering, performance]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/maplibre/` is a root-level compatibility index for MapLibre-related schema scaffolds.

The inspected versioned map and layer schema families live at `schemas/contracts/v1/map/` and `schemas/contracts/v1/layers/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct schema files found | 8 files |
| Current role | compatibility index |
| Placement | NEEDS VERIFICATION |
| Schema maturity | PROPOSED scaffold / permissive |

## Boundary

This folder is under `schemas/`, so it may contain machine-checkable shape material only if accepted here.

It is not MapLibre runtime code, UI code, tile storage, fixture storage, validator code, data storage, or release authority.

Schema validation here does not render a map, publish tiles, approve public display, prove evidence closure, or replace release records.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/maplibre/README.md` | present | Empty file expanded by this README. |
| `schemas/maplibre/perf-envelope.schema.json` | PROPOSED scaffold | Opened file is a draft 2020-12 object with `additionalProperties: true`. |
| `schemas/maplibre/perf-receipt.schema.json` | PROPOSED scaffold | Opened file is a draft 2020-12 object with `additionalProperties: true`. |
| `schemas/maplibre/render-diff-report.schema.json` | PROPOSED scaffold | Opened file is a draft 2020-12 object with `additionalProperties: true`. |
| `schemas/maplibre/perf-proof-pack.schema.json` | PROPOSED scaffold | Found by search; not opened in this pass. |
| `schemas/maplibre/perf-rollback-plan.schema.json` | PROPOSED scaffold | Found by search; not opened in this pass. |
| `schemas/maplibre/perf-failure-bundle.schema.json` | PROPOSED scaffold | Found by search; not opened in this pass. |
| `schemas/maplibre/perf-release-manifest.schema.json` | PROPOSED scaffold | Found by search; not opened in this pass. |
| `schemas/maplibre/perf-correction-notice.schema.json` | PROPOSED scaffold | Found by search; not opened in this pass. |
| `schemas/contracts/v1/map/README.md` | present | Inspected versioned map schema family index. |
| `schemas/contracts/v1/layers/README.md` | present | Inspected versioned layer schema family index. |

## What belongs here

- This README.
- Compatibility notes for the root-level MapLibre schema path.
- Migration notes if these files move under a versioned schema lane.
- Temporary mirror notes while placement is unresolved.

## What does not belong here

- MapLibre application code, UI components, API handlers, style files, map tiles, screenshots, dashboards, or generated render outputs.
- Data records, fixtures, validator code, runtime records, release records, correction notices, or rollback records as emitted records.
- Claims that a map surface is rendered, performant, approved, or public-ready merely because a payload validates against a schema.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep versioned lanes visible | Check `schemas/contracts/v1/map/` and `schemas/contracts/v1/layers/` before promoting a schema here. |
| Shape is not rendering | Schema validation constrains object shape; it does not render MapLibre. |
| Shape is not release | Release and rollback records remain outside this folder. |
| Avoid parallel authority | Equivalent map, layer, performance, release, and correction shapes must not drift across roots without migration notes. |

## Validation

```bash
find schemas/maplibre -maxdepth 4 -type f | sort
find schemas/contracts/v1/map schemas/contracts/v1/layers -maxdepth 4 -type f 2>/dev/null | sort
find schemas/maplibre -name '*.json' -print0 | xargs -0 -r -I{} python -m json.tool {} >/dev/null
```

## Open questions

| Question | Status |
|---|---|
| Should these MapLibre schemas remain under `schemas/maplibre/` or move under a versioned contract schema lane? | NEEDS VERIFICATION |
| Should performance receipts belong under map, layers, runtime, receipts, or release instead? | NEEDS VERIFICATION |
| Which examples and tests support these schemas? | NEEDS VERIFICATION |
