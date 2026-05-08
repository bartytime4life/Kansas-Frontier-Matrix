# USDA PLANTS Live Source Readiness Layer

## Purpose
Prepare no-network, operator-supplied intake and staging for USDA PLANTS snapshots.

## Lifecycle placement
RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED.

## Why this layer is not live ingestion
No CI downloads, no publication, no promotion, no county geometries, no live production ingestion.

## Source discovery contract
Local HTML parsing only; unknown links are retained.

## Operator-supplied snapshot intake
Operator files are raw evidence candidates until validation and policy gates pass.

## Raw snapshot manifest
Checksums, sizes, required role tracking, and quarantine links.

## Column contract
Canonical staged column contract for checklist/state/county tables.

## Drift detection
Missing required columns fail closed; unknown tables are quarantined.

## Quarantine behavior
Quarantined snapshots cannot feed release candidates.

## Staged input generation
Stage in WORK only, canonical normalize/sort, then handoff to existing fixture loader.

## How staged inputs feed the existing fixture loader
Existing fixture loader remains the only path to processed USDA PLANTS dataset objects.

## Policy gates
Source-intake Rego rules block non-USDA URI, CI network enablement, missing hashes/checksums, open quarantine, and published writes.

## CI expectations
All tests run with local fixtures only and no network.

## Manual future live-download path
Reserved for explicit operator manual mode, never CI default.

## What is intentionally not implemented yet
No direct live downloader, no publish/promotion pipeline modifications.

## Future work
Alias mapping expansion, richer source-shape fingerprints, and operator audit UX.
