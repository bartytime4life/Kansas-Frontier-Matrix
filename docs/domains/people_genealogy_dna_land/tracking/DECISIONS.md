# Decisions — People / Genealogy-DNA / Land

This log records lane-level documentation decisions until formal ADRs are added.

## D-001: Assertion-first remains mandatory
- **Date:** 2026-04-27
- **Status:** Accepted
- **Decision:** Keep source-reported assertions and their provenance before any canonical person/relationship/ownership synthesis.
- **Why:** This preserves reversibility and correction lineage.

## D-002: DNA evidence is restricted by default
- **Date:** 2026-04-27
- **Status:** Accepted
- **Decision:** DNA kit identifiers, segment-level records, and triangulation groups are never public by default.
- **Why:** High sensitivity and consent obligations; prevents accidental public leakage.

## D-003: Assessor/tax data cannot be promoted to title truth alone
- **Date:** 2026-04-27
- **Status:** Accepted
- **Decision:** Assessor rows can support assessor facts only unless chain-of-title evidence is present.
- **Why:** Administrative records are not authoritative ownership proof in isolation.

## D-004: Geometry cannot prove legal boundary precision alone
- **Date:** 2026-04-27
- **Status:** Accepted
- **Decision:** Parcel polygons and derived geometry are context unless supported by legal-description/survey evidence.
- **Why:** Visualization geometry often differs from legal boundary authority.

## Pending decisions
- Schema-home finalization (`contracts/` vs `schemas/contracts/v1/`).
- API DTO naming and Evidence Drawer payload versioning.
- Policy module layout finalization under `policy/{people,genealogy,land_ownership,evidence}`.
