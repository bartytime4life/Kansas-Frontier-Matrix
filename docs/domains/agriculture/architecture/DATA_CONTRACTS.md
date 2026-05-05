# Agriculture Data Contracts

This document defines the minimum object families expected for agriculture lane contracts.

## Schema home

Canonical schema home is currently **NEEDS VERIFICATION**. Use one canonical location only:

- `schemas/contracts/v1/agriculture/` **or**
- `contracts/agriculture/`

## Core object families

| Object | Purpose | Required identity |
|---|---|---|
| `AgricultureObservation` | Station-like or measured agriculture variable record | source ID + station/grid key + timestamp + variable |
| `AgricultureAggregateStat` | County/state/region aggregate statistic | source ID + geography + period + statistic |
| `AgricultureGridProduct` | Remote-sensing/gridded product slice | source ID + product/version + grid/time window |
| `AgricultureDerivedIndicator` | Derived stress/index product built from validated sources | indicator ID + source refs + processing version |
| `EvidenceBundle` | Claim support payload for API/UI consumption | bundle ID + evidence refs + policy/review status |
| `DecisionEnvelope` | Promotion/publication result object | decision ID + outcome + reasons + obligations |
| `ReleaseManifest` | Published release linkage | release ID + artifact digests + rollback reference |

## Contract rules

- Aggregate records cannot carry field-level claim affordances.
- Remote-sensing and derived products must expose product/version lineage.
- Public DTOs must include claim scope and uncertainty affordances.
- Corrections must supersede; never mutate historical canonical rows in place.
