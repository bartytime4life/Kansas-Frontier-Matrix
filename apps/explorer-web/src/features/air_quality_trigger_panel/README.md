# Air-quality trigger panel

Status: **fixture-first Explorer component; not production-wired**.

This feature adapts Pass 32 card `KFM-P32-FEAT-0007` over the existing
`PM25_TRIGGER_CANDIDATE_ASSESSMENT_V1` foundation. It distinguishes a proposed
categorical candidate, a categorical no-candidate result, held context, policy
denial, and upstream error without exposing a concentration, numeric threshold,
AQI value, coordinate, station identity, health category, detector setting, or
policy explanation.

## Projection boundary

The app-local profile `kfm.explorer.air-quality-trigger.fixture.v1` accepts
digest-bound assessment, observation, trailing-median, and evidence references;
one whole-second UTC observation time; the fixed `OBSERVED_SENSOR` knowledge
character; and finite threshold/median relations. A proposed candidate requires
both relations to be above their separately governed references and at least two
unique evidence references. A no-candidate result requires at least one
at-or-below relation.

Evidence is fixed to `REFERENCED_NOT_RESOLVED`. The UI therefore describes an
evidence-referenced analytical candidate, not an evidence-resolved or
evidence-backed claim.

## Authority boundary

The panel does not fetch a source, receive raw PM2.5 values, calculate a
threshold or trailing median, mutate detector configuration, declare an event,
decide regulatory compliance, issue health advice, evaluate policy, approve
review, write lifecycle state, promote, release, deploy, publish, or authorize
public use. Negative outcomes carry no candidate or reference detail.

## Placement

- `apps/explorer-web/src/adapters/` owns strict app-local parsing.
- `apps/explorer-web/src/features/air_quality_trigger_panel/` owns fixed display
  behavior.
- `fixtures/ui/air_quality_trigger_projection/` owns synthetic display packets.
- `apps/explorer-web/tests/` owns unit and browser proof.

Accepted ADR-0029 and Directory Rules v2 place these artifacts in existing
responsibility roots. The existing Atmosphere contract, schema, validator, and
fixtures retain candidate-assessment authority and are referenced rather than
copied.

## Production hold

Production wiring remains **HOLD** until a reviewed governed API emits this
exact public-safe projection from an accepted assessment and resolvable
EvidenceRefs. The browser must not ingest source responses, canonical
observations, internal policy output, or health/regulatory data directly.

## Validation

```text
pnpm --filter explorer-web exec vitest run tests/air-quality-trigger-panel.test.ts
pnpm --filter explorer-web exec playwright test --config=playwright.config.ts tests/browser/air-quality-trigger-panel.spec.ts
pnpm --filter explorer-web build
```

## Rollback

Revert the adapter, feature, fixtures, tests, source map, and authoring receipt
together. This additive component creates no source, detector, event, evidence,
policy, review, lifecycle, promotion, release, deployment, publication, or
public-use state.
