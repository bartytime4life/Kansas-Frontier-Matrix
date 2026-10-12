<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/county-environmental-recency-spine
title: CountyEnvironmentalRecencySpine Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Data steward · Source steward · Temporal steward · Domain stewards · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; data; county-scope; recency; cadence; no-public-authority
owning_root: contracts/
responsibility: fixture-only deterministic county-scoped weekly recency aggregation over declared existing source-health references without probing sources or granting interpretation, lifecycle, policy, release, publication, or public-use authority
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../source/source_health_assessment.md
  - ../source/source_availability_watchlist.md
  - ../evidence/temporal_support_assessment.md
  - ../../schemas/contracts/v1/data/county_environmental_recency_spine.schema.json
  - ../../fixtures/contracts/v1/data/county_environmental_recency_spine/cases.json
  - ../../tools/validators/data/validate_county_environmental_recency_spine.py
  - ../../tests/validators/test_validate_county_environmental_recency_spine.py
  - ../../docs/intake/exploratory/pass-32-county-environmental-recency-source-map.md
tags: [kfm, data, county, recency, cadence, source-health, fixture]
notes:
  - "Adapts Pass 32 cards KFM-P32-FEAT-0015 and KFM-P32-IDEA-0001 without probing a source or redefining source-health semantics."
  - "COMPLETE means the six synthetic weekly declarations are coherent; it is not an interpretation, promotion, release, or publication gate."
[/KFM_META_BLOCK_V2] -->

# CountyEnvironmentalRecencySpine Candidate Contract

`CountyEnvironmentalRecencySpineCandidate` is a deterministic, fixture-only projection of one weekly county-scoped source-health roster. It makes missing, stale, unavailable, degraded, and errored lanes visible before a separate interpretation gate is considered.

## Source-derived gap

Pass 32 proposes a county environmental cadence calendar (`KFM-P32-FEAT-0015`) and a county-first recency spine (`KFM-P32-IDEA-0001`) spanning vegetation, imagery, hydrology, air, soils, and biodiversity. The reviewed repository already owns source freshness in `SourceHealthAssessment` and aggregate source routing in `SourceAvailabilityWatchlist`. This profile therefore references those families instead of creating another probe, watcher, health vocabulary, or material-change authority.

## Bounded model

One candidate binds:

- one synthetic Kansas county composition scope;
- one exact seven-day UTC interval and post-interval assessment time;
- one `SourceAvailabilityWatchlist` reference;
- exactly one entry for each required lane: `AIR`, `BIODIVERSITY`, `HYDROLOGY`, `IMAGERY`, `SOILS`, and `VEGETATION`;
- one `SourceDescriptor` and `SourceHealthAssessment` reference per lane;
- the existing health vocabulary: `HEALTHY`, `DEGRADED`, `STALE`, `UNAVAILABLE`, or `UNKNOWN`;
- one local cadence declaration: `RECORDED`, `MISSED`, or `ERROR`; and
- a reproduced finite rollup: `COMPLETE`, `HOLD`, or `ERROR`.

The validator does not dereference any reference. A declared health outcome is process input, not proof of source condition.

## Deterministic rules

1. The interval timestamps use UTC, span exactly 168 hours, and `assessed_at` is not earlier than its end.
2. Entries are sorted by lane and cover the six-lane set exactly once.
3. `RECORDED` requires a check timestamp inside the interval and a non-`UNKNOWN` health outcome.
4. `MISSED` requires no check timestamp, `UNKNOWN`, and `CHECK_MISSING`.
5. `ERROR` requires an in-window check timestamp, `UNKNOWN`, and `CHECK_ERROR`.
6. Recorded health reason codes reproduce the existing health vocabulary.
7. Summary counts and the overall outcome are derived from the entries.
8. `COMPLETE` requires six recorded `HEALTHY` lanes. Any degraded, stale, unavailable, or missed lane yields `HOLD`; any errored lane yields `ERROR`.
9. `separate_interpretation_gate_required` is always true.
10. Every authority or effect flag is false.

`spec_hash` is RFC 8785 JCS plus SHA-256 over the object excluding only `spine_id` and `spec_hash`. `spine_id` uses the first 24 hexadecimal digest characters.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The six-lane weekly projection is internally coherent and reports `COMPLETE`. |
| `ABSTAIN` | The projection is coherent but reports `HOLD`. |
| `DENY` | Shape, time, lane, state, reason, summary, identity, or authority invariants failed. |
| `ERROR` | The projection coherently reports an errored lane or input could not be read safely. |

No outcome authorizes downstream interpretation.

## Directory Rules basis

The object is a cross-domain data/provenance projection, so semantic meaning belongs in `contracts/data/`; shape in `schemas/contracts/v1/data/`; synthetic cases in `fixtures/contracts/v1/data/`; repository validation in `tools/validators/data/`; conformance evidence in `tests/validators/`; orchestration in `.github/workflows/`; source adaptation in `docs/intake/exploratory/`; and authoring accountability in `data/receipts/generated/`.

The county is a composition scope, not a domain or root. No county data is copied and no new source, watcher, temporal-support, policy, release, or publication authority is created.

## Non-effects and rollback

A green fixture result does not probe a source, authenticate freshness, create a SourceHealthAssessment, clear a stale condition, interpret environmental conditions, write a lifecycle lane, approve policy or review, promote, release, deploy, publish, or authorize public use.

Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet. It has no runtime consumer or live state, so rollback requires no data migration, source action, cache invalidation, withdrawal, or public correction.
