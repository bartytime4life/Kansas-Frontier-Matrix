<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-synthetic-kcds-readme
title: fixtures/synthetic/kcds/ — KCDS No-Network Synthetic Fixture Lane
type: readme; fixture-lane; discovery-only; no-network
version: v0.1.0
status: discovery-only draft; no source activation; no real crash data
owners: NEEDS VERIFICATION — Kansas source steward + Privacy reviewer + Synthetic fixture maintainer
created: 2026-07-28
updated: 2026-07-28
policy_label: >
  repository-facing; fixtures; synthetic; deterministic; no-network-default;
  discovery-only; no-crash-data; no-pii; fail-closed
owning_root: fixtures/synthetic/
responsibility: >
  Compact no-network synthetic fixtures for KCDS schema-shape and
  discovery-documentation validation. These fixtures do not contain
  real crash data, real road geometry, real person data, or real
  vehicle data. They exist solely to support schema-validation tooling
  and documentation tests without requiring network access to any
  KCDS surface.
truth_posture: >
  CONFIRMED synthetic fixture lane; no live data / PROPOSED fixture
  schema shapes; NEEDS VERIFICATION against official KCDS data
  dictionary when that becomes available
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  discovery_document: docs/sources/catalog/kansas/kcds.md
related:
  - ../README.md
  - ../../../../docs/sources/catalog/kansas/kcds.md
  - ../../../../docs/sources/catalog/kansas/kdot.md
tags: [kfm, fixtures, synthetic, kcds, kansas, kdot, road-reference, no-network, discovery-only, no-pii, no-crash-data]
notes:
  - "All fixture content is invented for schema-shape testing. Nothing here represents real KCDS data."
  - "No fixture implies that the corresponding KCDS surface is activated, accessible, or approved for ingestion."
  - "Road-reference fixture is road-geometry shape only; it does not simulate crash records."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `fixtures/synthetic/kcds/` — KCDS No-Network Synthetic Fixture Lane

> No-network synthetic fixture lane for Kansas Crash Data System (KCDS) discovery documentation and schema-shape validation. **No real crash data, person data, vehicle data, or real road geometry is present in this directory.** These are invented fixtures for tooling tests only.

[![Status: discovery-only](https://img.shields.io/badge/status-discovery--only-d4a72c?style=flat-square)](#status)
[![No crash data](https://img.shields.io/badge/crash%20data-none%20(synthetic%20only)-6e7781?style=flat-square)](#caution)
[![No PII](https://img.shields.io/badge/PII-none-1f883d?style=flat-square)](#caution)
[![Source activation: none](https://img.shields.io/badge/source%20activation-none-b42318?style=flat-square)](#authority-boundary)

> [!CAUTION]
> No fixture in this directory is real KCDS data. No fixture implies that the corresponding KCDS surface is activated, that access is authorized, or that any KCDS data has been ingested. Synthetic fixtures represent invented schema shapes only.

> [!IMPORTANT]
> The road-reference fixture represents a road-geometry response shape only. It does not simulate crash records, crash IDs, person data, vehicle data, or incident details. The KCDS road-reference FeatureServer returns road network geometry, not crash incidents.

## Status

| Field | Value |
|---|---|
| Directory lifecycle | `discovery-only draft` |
| Real crash data | None present |
| PII | None present |
| Real road geometry | None — synthetic only |
| Source activation | None |
| Network access performed | None |

## Authority boundary

These fixtures may be used to:
- validate schema-shape expectations against invented data;
- support no-network documentation tests;
- illustrate expected field names and types for future schema design.

These fixtures must NOT be used to:
- claim that any KCDS surface has been accessed;
- assert that any field classification has been verified against real data;
- derive production schema from without first verifying against official KCDS documentation.

## Fixture inventory

| File | Simulates | Purpose |
|---|---|---|
| `road_reference_feature_stub.json` | ArcGIS FeatureServer road-reference record shape | Schema-shape validation; no real geometry, no crash data |
| `source_surface_inventory.yaml` | Machine-readable surface inventory | Documentation tooling; mirrors the table in `kcds.md` §1 |

## No-network guarantee

These fixtures require no network access. They contain no live endpoint URLs as data values, no credentials, no authenticated tokens, and no real agency identifiers. Fixture values use clearly synthetic placeholder patterns (e.g., `SYNTHETIC-`, `TEST-`).

[Back to top](#top)
