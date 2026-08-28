# AdvisoryEventEnvelope source adaptation

Status: `PROPOSED` / fixture-first / no-network

## Source idea

The *KFM Briefing-to-System Integration Architecture* proposes a shared
`AdvisoryEventEnvelope` after the existing `BriefingSignal` and
`TemporalAuthorityEnvelope` foundations. It describes reusable volatile-event
mechanics for heat, harmful-algal-bloom, drinking-water, road-closure, and smoke
advisories while requiring each domain to retain its own payload and state
meaning.

The source’s central fail-closed rules are:

- retrieval failure is `STATUS_CHECK_FAILED`, never a clear;
- stale or incomplete status remains unconfirmed;
- authoritative rescission/expiry semantics are required before clearing;
- identity and geometry conflicts block guessed public geometry;
- zone scope must not be promoted to a larger area;
- forecast, observation, model, regulatory advisory, and synthetic support must
  not collapse into one source role; and
- the first implementation should be synthetic, no-network, release-neutral,
  and non-public.

## Repository assay

Current repository evidence already contains:

- `BriefingSignal`, deterministic clustering/materiality/routing, and a
  read-only issue projection;
- `TemporalAuthorityEnvelope`, schema, fixtures, validator, tests, and CI;
- a fixture-first `KdheHabAdvisorySnapshot` domain profile with active, lifted,
  stale, source-unavailable, identity-conflict, and zoned cases; and
- an existing `briefing-integration` workflow.

No `AdvisoryEventEnvelope` object family was found by exact repository search.

## Bounded adaptation

This slice adds one shared envelope and one domain profile:

```text
AdvisoryEventEnvelope
  -> TemporalAuthorityEnvelope
  -> local KdheHabAdvisorySnapshot fixture
  -> canonical payload digest + source-content digest
  -> exact finite status/scope mapping
  -> deterministic validation findings
  -> no alert/release/public authority
```

The wrapper references existing hazards fixtures rather than copying their
native fields into `contracts/common/`. That preserves the common shared-kernel
boundary and keeps KDHE HAB meaning in the hazards lane.

## Deliberately deferred

- live KDHE retrieval or source activation;
- NWS heat products;
- drinking-water advisories;
- road closures and WZDx;
- smoke forecasts and observed PM2.5;
- public alert, API, map, search, Focus Mode, or notification surfaces;
- policy/review/release integration; and
- any claim that the fixtures represent current real-world status.

Each future profile requires its own source-role, rights, identity, geometry,
correction, fixture, validator, and rollback review.
