<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/soil-support-role-assessment-source-map
title: Soil support-role assessment source map
type: exploratory-source-map
version: 1.0.0
status: proposed
owning_root: docs/
truth_posture: source-derived proposal; current repository behavior verified separately
related:
  - ../../../contracts/domains/soil/soil_support_role_assessment.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Soil support-role assessment source map

## Goal

Translate the strongest anti-collapse requirement in the supplied soil architecture into one deterministic, no-network, fixture-only repository slice.

## Source-derived requirement

The soil report explicitly separates authoritative static soil survey, gridded derivative soil, station soil moisture, and satellite soil-moisture grids. It warns that these support types must not masquerade as one authoritative surface. It also recommends preserving source references, evidence references, content identity, freshness, support type, and quality or confidence disclosures for consequential soil claims.

The report's larger first-slice proposal includes SSURGO/SDA, Kansas Mesonet, validators, receipts, catalog closure, and map artifacts. This implementation deliberately narrows that proposal to the shared semantic boundary that must exist before a live connector, catalog product, or public layer can be trusted.

## Repository gap and bounded choice

Current repository evidence contains mature soil workflow and runtime-proof surfaces, but the campaign scan did not identify a dedicated, fixture-backed object that validates the anti-collapse relationship among static survey, gridded derivative, station observation, and satellite grid support. This packet adds only that held assessment profile.

## Non-effects

The packet does not activate SSURGO, SDA, gSSURGO, gNATSGO, Kansas Mesonet, SCAN, USCRN, or SMAP; fetch or retain source bytes; establish source rights; resolve an EvidenceBundle; evaluate real freshness; build GeoParquet, catalog, triplet, PMTiles, or API artifacts; approve review; promote; release; deploy; publish; or authorize public use.

## Directory Rules basis

Accepted ADR-0029 makes the adopted Directory Governance Standard the placement authority. The packet uses existing domain-contract, schema, fixture, validator, test, workflow, exploratory-doc, and generated-receipt roots. No new root or parallel authority home is created.
