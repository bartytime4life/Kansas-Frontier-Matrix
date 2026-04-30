---
kfm_meta:
  version: 2
  status: draft
  domain: flora
  layer: usda_plants_controlled_publication
  rights: public
  promotion_state: promoted_package_required
  publication_state: controlled_publication
  network: disabled
  sensitivity: public
  source_id: usda_plants
  source_uri: https://plants.sc.egov.usda.gov/downloads
---

# USDA PLANTS Controlled Publication Layer

## Purpose
Publishes only from sealed promoted packages into public-safe outputs.

## Lifecycle placement
PROMOTED_PACKAGE → PUBLICATION_REQUEST → PUBLICATION_APPROVAL → PUBLISHED.

## Promotion vs publication
Promotion is internal sealing; publication emits sanitized public artifacts only.

## Publication request model
Human-only request and blocked outputs include coordinates/geometry/tiles.

## Publication approval model
Human-only approval required before execution.

## Publication execution plan model
Writes only to `published/flora/usda_plants/<snapshot_date>/`.

## Published release manifest
Contains source attribution, rights, and safety flags.

## Published dataset index
Contains taxon summaries and references only.

## Published Evidence Drawer index
Indexes sanitized evidence payloads.

## Published county-presence data product
Publishes FIPS-keyed presence only.

## Published MapLibre descriptor
Descriptor only; requires external county geometry in future layer.

## Publication receipt
Execution result with published item hashes.

## Publication rollback plan
Human-approved supersession planning only.

## Publication audit ledger
Deterministic hash ledger across publication artifacts.

## Policy gates
Denies missing approval, unsealed package, leaks, tiles, auto-merge claims.

## Optional protected-environment workflow
Manual workflow_dispatch path with protected environment.

## CI and no-network posture
No USDA fetch and no network dependency.

## What is intentionally not implemented
No precise coordinates, no county geometry, no vector tiles, no auto-merge.

## Future geometry/tile layer
Future layer may add geometry and tile generation with separate controls.
