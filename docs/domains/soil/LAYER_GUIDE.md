<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/soil/layer-guide
title: Soil Layer Guide
type: standard
version: v1
status: draft
owners: TODO-VERIFY
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO-VERIFY
related: [kfm://doc/TODO-VERIFY-uuid]
tags: [kfm, soil, maplibre, evidence-drawer, layers]
notes: [UI-oriented guidance companion for the soil domain README.]
[/KFM_META_BLOCK_V2] -->

# Soil Layer Guide

Guidance for presenting soil layers in map-first experiences while preserving evidence-first trust.

## Layer design principles

1. Each layer has one primary `support_type`.
2. Legends and tooltips must not hide derivation status.
3. Click actions must resolve to an `EvidenceBundle` (or finite refusal).
4. Non-authoritative overlays must carry visible caveats.

## Recommended layer families

| Layer ID | Theme | support_type | Minimum click payload |
|---|---|---|---|
| `soil-mapunits` | Survey map units | `authoritative_static_soil` | `mukey`, source/version, spec hash, validation timestamp |
| `soil-components` | Component composition | `authoritative_static_soil` | `mukey`, `cokey`, component percentage, lineage refs |
| `soil-horizons` | Horizon details | `authoritative_static_soil` or `profile_soil_evidence` | `chkey`, depth interval, method/source |
| `soil-property-summary` | Derived properties and ratings | `soil_interpretation` | value, units, method, weighting/aggregation basis |
| `soil-moisture-stations` | Station points | `station_soil_moisture` | station ID, depth list, freshness/QC summary |
| `soil-moisture-series` | Time-series chart hooks | `station_soil_moisture` | timestamp, depth, value, QC flags |
| `soil-gridded-derivative` | Raster/grid derivatives | `gridded_derivative_soil` | resolution, derivation lineage, limitations |
| `smap-soil-moisture-context` | Satellite moisture context | `satellite_soil_moisture_grid` | product/version, grid/time window, QA status |

## Drawer behavior expectations

The Evidence Drawer should include, at minimum:

- source family + version/release indicator,
- support type and interpretation/derivation caveats,
- identity keys (e.g., `mukey`, station ID, depth/time for readings),
- policy/rights visibility marker,
- links/references to catalog and receipt/proof artifacts where available.

## Copy constraints

- Avoid declarative language that overstates certainty (e.g., “proves”).
- Prefer bounded phrasing (e.g., “indicates”, “derived from”, “as observed at”).
- Clearly separate station observations from gridded/satellite context.
