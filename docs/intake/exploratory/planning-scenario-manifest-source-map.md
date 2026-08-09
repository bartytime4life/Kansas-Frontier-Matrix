# Source adaptation — PlanningScenarioManifest

## Goal

Implement the smallest dependency-closed form of Pass 20 `EXP-014`: a scenario manifest schema plus one Kansas-relevant synthetic pilot with explicit assumptions, time horizon, equity dimensions, participation references, a public-safe summary candidate, and an Evidence Drawer payload.

## Source basis

- **KFM Pass 20 Part 2 Idea Index**, `KFM-IDX-PLN-001` and `EXP-014`: planning scenarios expose assumptions, boundaries, equity, participation, data vintages, uncertainty, and non-predictive posture.
- **Kansas Frontier Matrix Architecture Consolidation Pass — March 2026**: planning and public surfaces remain downstream of evidence, policy, review, release, and correction boundaries.
- **KFM MapLibre Operating Architecture**: the primary surface stays concise while the drawer carries the fuller trust and limitation payload.
- **KFM Unified Doctrine / Connected-Dots Architecture**: maps and summaries are carriers, not sovereign truth.

## Repository adaptation

The repository already has an established `water_planning` bounded context, synthetic fixtures, an Evidence Drawer contract family, deterministic RFC 8785 hashing support, and responsibility-root placement under ADR-0029. The pilot therefore belongs in the existing water-planning contract/schema lane and reuses those boundaries instead of creating a new top-level planning authority.

The scenario is statewide and generalized because the source leaves the Kansas domain/AOI choice open. Drought planning is used only as a synthetic hydrology-relevant frame; the fixture makes no current-condition, forecast, facility, household, emergency, or regulatory claim.

## Non-effects

No source is activated, no evidence is resolved, no policy or review is approved, no map or drawer is rendered, and no release or publication occurs. The summary and drawer are candidate payload shapes held behind explicit false authority flags.
