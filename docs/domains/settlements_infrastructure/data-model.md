# Settlements & Infrastructure Data Model

This document defines the minimum bounded contexts for the settlements-infrastructure lane.

## Bounded contexts

| Context | Purpose | Canonical identity |
|---|---|---|
| Settlements | Human place entities, names, legal status, civic roles, and temporal boundaries | settlement ID + time validity |
| Infrastructure | Assets, networks, nodes, segments, facilities, operators, and dependencies | infrastructure ID + network/asset type |
| Observations | Population, condition, service, and status observations | subject ID + observed timestamp + source |
| Governance | Evidence, review, policy, release, and correction lineage | evidence/release/decision IDs |

## Core object families

- `Settlement`
- `SettlementName`
- `SettlementBoundaryVersion`
- `SettlementStatusEvent`
- `PopulationObservation`
- `InfrastructureAsset`
- `InfrastructureNetwork`
- `InfrastructureNode`
- `InfrastructureSegment`
- `InfrastructureFacility`
- `InfrastructureConditionObservation`
- `EvidenceBundle`
- `DecisionEnvelope`
- `ReleaseManifest`

## Modeling rules

1. Preserve temporal validity explicitly; avoid flattening legal/status history into one row.
2. Separate legal place identity from rendered geometry snapshots.
3. Keep source role and rights posture attached at record level for consequential claims.
4. Represent network topology as relations, not inferred map adjacency.
5. Public DTOs must carry claim scope and uncertainty affordances.
