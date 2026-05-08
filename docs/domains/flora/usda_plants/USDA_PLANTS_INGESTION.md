# USDA PLANTS Ingestion

> [!IMPORTANT]
> This is a **no-network governance slice**. It validates deterministic USDA PLANTS-shaped fixtures for the Flora lane. It is **not** a live USDA connector, publication workflow, promotion workflow, or EvidenceBundle release path.

## At a glance

| Field | Value |
|---|---|
| Domain | `flora` |
| Layer | `ingestion` |
| Source family | USDA PLANTS |
| Current slice posture | Fixture-backed CI validation |
| Network posture | Disabled / no live downloads |
| Lifecycle coverage | PROCESSED contract validation only |
| Publication posture | No public release from this slice alone |
| Promotion posture | Future governed promotion required |
| External source terms | NEEDS_VERIFICATION before live connector activation |

## Purpose

Define a deterministic, fixture-backed USDA PLANTS ingestion slice for the KFM Flora lane so CI can validate source posture and core data integrity without relying on live downloads, changing source endpoints, or external network access.

This slice is intentionally small. Its job is to prove that USDA PLANTS-shaped records can pass or fail a stable contract under controlled conditions.

## Lifecycle placement

```mermaid
flowchart LR
  RAW[RAW intake] -. out of scope .-> WORK[WORK / QUARANTINE]
  FIXTURES[No-network fixtures] --> VALIDATOR[USDA PLANTS dataset validator]
  VALIDATOR --> PROCESSED[PROCESSED contract verdict]
  PROCESSED -. future governed promotion .-> CATALOG[CATALOG / TRIPLET]
  CATALOG -. future release gate .-> PUBLISHED[PUBLISHED]
