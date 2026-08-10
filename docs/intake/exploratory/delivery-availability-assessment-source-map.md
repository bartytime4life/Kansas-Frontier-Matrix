<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/delivery-availability-assessment-source-map
title: Delivery Availability Assessment - Source Map and Implementation Boundary
type: exploratory-intake-source-map
version: v0.1.0
status: promoted-to-fixture-candidate; non-authoritative; repository-grounded
owners: OWNER_TBD — Intake steward · Source steward · Temporal steward · affected domain stewards
created: 2026-08-09
updated: 2026-08-09
policy_label: public; intake; source; cadence; delivery; cite-or-abstain
owning_root: docs/
responsibility: Preserve traceability from the supplied Full Atlas product-delivery cards and the New Ideas 4-30 source map to one bounded repository candidate without adopting product timings or promoting source prose into policy, review, release, or publication authority.
truth_posture: CONFIRMED source-card traceability and inspected-tree collision review / PROPOSED bounded adaptation / NEEDS VERIFICATION steward review, product-specific timings, and later-main collisions
related:
  - ../../kfm_full_atlas_seed_cards.md
  - ./new-ideas-4-30-source-map.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/source/delivery_availability_assessment.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/source/source_health_assessment.md
  - ../../../contracts/source/source_availability_watchlist.md
  - ../../../contracts/source/source_polling_checkpoint.md
tags: [kfm, intake, full-atlas, delivery-latency, product-cadence, availability, freshness]
notes:
  - "Packet latency figures and all new fixture durations are synthetic or dated design lineage, not adopted source expectations."
  - "Repository collision review was refreshed against main@d0c8fffac1ea152066910725ef63e050958e8252 after the independent measurement-support packet merged."
[/KFM_META_BLOCK_V2] -->

# Delivery availability assessment - source map

> **Outcome:** `KFM-TRIAD-049` and programming card `KFM-CAND-0147` are adapted into one synthetic, no-network contract packet. It distinguishes expected lag from lateness and stale or missing products while fixing every expectation update and authority effect to false.

## Source lineage

| Source | Relevant proposal | Posture used here |
|---|---|---|
| Supplied/Drive `KFM_Full_Atlas_seed_cards.md` | `KFM-TRIAD-049`, `KFM-CAND-0145` through `KFM-CAND-0147`, and Slice K | Design lineage for separate delivery clocks and finite states. |
| `docs/intake/exploratory/new-ideas-4-30-source-map.md` | Gap table, unsafe-direct-transfer table, and source timing discussion | Repository-grounded prior triage; source-specific timings remain unverified. |
| Existing source contracts | Descriptor cadence, source health, availability/materiality watchlist, and conditional polling checkpoint | Adjacent semantic boundaries retained without modification. |
| `docs/doctrine/directory-rules.md` plus accepted ADR-0029 | Responsibility-root placement and no-parallel-authority rules | Placement authority. |

## Current-main collision review

At `main@d0c8fffac1ea152066910725ef63e050958e8252`, bounded searches found extensive cadence and freshness prose plus four adjacent executable or semantic families:

| Existing family | Responsibility retained |
|---|---|
| `SourceDescriptor` | Source identity, role, rights, sensitivity, declared cadence, and activation posture. |
| `SourceHealthAssessment` | Probe result, last retrieval, freshness deadline, and finite health. |
| `SourceAvailabilityWatchlist` | Aggregate availability plus material-change review routing. |
| `SourcePollingCheckpoint` | ETag, Last-Modified, digest, and conditional-fetch candidate state. |

No common executable contract was found that jointly binds observation cadence, product cadence, expected delivery latency, actual availability, retrieval, freshness, staleness, source revision, and evidenced outage while preventing learned timings from updating policy. This is **CONFIRMED for the inspected tree**, not a timeless repository claim.

## Bounded adaptation

The candidate keeps:

- separately versioned descriptor and delivery expectation references;
- observation and product cadence as different fields;
- minimum and maximum delivery-latency bounds;
- separate observed, generated, expected-available, actually available, retrieved, validated, and optional released times;
- separate freshness and stale thresholds;
- finite `ON_TIME`, `EXPECTED_LAG`, `LATE`, `STALE`, `MISSING`, `SUPERSEDED`, `SOURCE_OUTAGE`, and `ERROR` states;
- explicit revision supersession and outage-evidence binding;
- review-only learned latency; and
- deterministic identity, exact fixture polarity, and fixed false authority flags.

It deliberately excludes:

- live endpoint access, polling, provider jobs, credentials, conditional requests, and stored products;
- adopted source schedules, service-level objectives, latency percentiles, holidays, or outage rules;
- automatic tuning, statistical learning, descriptor mutation, or scheduler mutation;
- source activation, RAW writes, evidence resolution, policy decisions, review approval, promotion, release, deployment, publication, or public use.

## Why direct timing transfer is rejected

The source map explicitly warns that packet latency prose can age and differ from observation cadence. Therefore, every fixture duration is synthetic and every expectation is versioned. A later product-specific proposal must cite current official documentation, receive source-steward review, and update a separately governed profile; accumulated observations may inform that review but cannot update policy themselves.

## Directory Rules placement

| Artifact responsibility | Path |
|---|---|
| Source semantic meaning | `contracts/source/delivery_availability_assessment.md` |
| Canonical machine shape | `schemas/contracts/v1/source/delivery_availability_assessment.schema.json` |
| Reusable synthetic cases | `fixtures/contracts/v1/source/delivery_availability_assessment/cases.json` |
| Repository validator | `tools/validators/source/validate_delivery_availability_assessment.py` |
| Executable evidence | `tests/validators/test_validate_delivery_availability_assessment.py` |
| Hosted orchestration | `.github/workflows/delivery-availability-assessment.yml` |
| Human source adaptation | This file under `docs/intake/exploratory/` |
| AI-authoring process memory | `data/receipts/generated/` |

No new root or parallel source, schema, policy, evidence, lifecycle, receipt, proof, release, or publication home is created.

## Validation and rollback

Validation covers Draft 2020-12 schema validity, all eight finite states, exact `PASS/ABSTAIN/DENY/ERROR` fixture polarity, derived windows and learned latency, temporal and retrieval-state coherence, deterministic identity, parser bounds, no-network behavior, adjacent source-health regression tests, workflow parsing, documentation metadata, and generated-receipt hashes.

Rollback is an ordinary revert of the additive packet. Because no live source, descriptor, scheduler, stored product, policy, release, runtime, cache, or publication state is created, no operational data migration is required.
