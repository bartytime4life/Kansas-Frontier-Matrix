<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-32-county-environmental-recency-source-map
title: Pass 32 County Environmental Recency Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · Data steward · Source steward · Temporal steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded mapping from Pass 32 county recency proposals to bounded repository artifacts without treating proposal cards as implementation evidence or authority
truth_posture: CONFIRMED source-card transcription and repository comparison / PROPOSED bounded adaptation pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/data/county_environmental_recency_spine.md
  - ../../atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md
  - ../../../contracts/source/source_health_assessment.md
  - ../../../contracts/source/source_availability_watchlist.md
tags: [kfm, pass-32, county, recency, cadence, source-map]
[/KFM_META_BLOCK_V2] -->

# Pass 32 County Environmental Recency Source Map

## Source cards

| Card | Source statement retained | Repository adaptation |
|---|---|---|
| `KFM-P32-FEAT-0015` | A weekly county cadence calendar should surface freshness for CDL/vegetation, imagery, hydrology, AQS/air, soils, and biodiversity inputs. | Define one fixture-only six-lane weekly aggregate; do not create UI, probes, dashboards, or source state. |
| `KFM-P32-IDEA-0001` | County-first checks should form a governed recency spine before downstream interpretation. | Require a separate interpretation gate and reuse existing source-health/watchlist references. |

The source atlas labels both cards `PROPOSED` and marks repository implementation status unknown. This implementation claim is based on the current repository comparison, not the source document alone.

## Current repository reconciliation

`SourceHealthAssessment` already owns finite source freshness and retrieval-health semantics. `SourceAvailabilityWatchlist` already separates availability from material change and review routing. `TemporalSupportAssessment` owns claim-specific time support. The new profile composes references to those authorities; it does not duplicate their decisions or dereference their records.

Repository search at base `76da0a048590710bd927891d43075d989568bf7d` found no county environmental recency/cadence contract, schema, validator, fixture family, or workflow outside proposal atlases.

## Path decision

```yaml
path_decision:
  artifact: CountyEnvironmentalRecencySpineCandidate
  proposed_path: contracts/data/county_environmental_recency_spine.md
  artifact_kind: semantic contract
  authority_owner: cross-domain data/provenance projection
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: geography
  scope_id: synthetic-county-composition
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-PLACE-001
    - DIR-AUTHROOT-001
    - DIR-SCOPELANE-001
    - DIR-SCOPELANE-004
  outcome: PLACE
```

## Non-effects

This source map and the proposed packet do not activate a source, authenticate freshness, create a watcher, write a county data copy, interpret environmental conditions, evaluate policy, approve review, promote, release, deploy, publish, or authorize public use.
