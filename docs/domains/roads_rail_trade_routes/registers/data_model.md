# Data Model

Canonical object-family summary for transport evidence.

## Families
- `RoadSegment`, `RailSegment`, `CorridorRoute`, `RouteMembership`.
- `NetworkNode`, `Crossing`, `TransportFacility`.
- `RestrictionEvent`, `StatusEvent`, `OperatorAssignment`.
- `AlignmentVersion`, `HistoricRouteClaim`, `TradeRouteCorridor`.

## Invariants
- Identity and membership are time-scoped.
- Legal authority claims require governing/authoritative source role.
- Sensitive corridors default to generalized or denied public geometry.

## Validation hooks
- Schema, CRS/geometry, temporal consistency, and source-role checks.
