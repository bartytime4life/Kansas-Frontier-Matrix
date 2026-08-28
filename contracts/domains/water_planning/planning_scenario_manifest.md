# PlanningScenarioManifest Contract — Water Planning

> **Status:** PROPOSED · synthetic pilot only · no release or publication authority

## Meaning

A `PlanningScenarioManifest` is a bounded description of an exploratory water-planning scenario. It keeps the scenario's assumptions, input variables, data vintages, time horizon, equity dimensions, participation references, public-safe summary candidate, and Evidence Drawer payload together without presenting the scenario as a prediction, emergency alert, regulatory determination, or binding decision.

The first profile is deliberately limited to a synthetic, generalized Kansas drought-planning fixture. It is a proof of contract and surface shape, not a statement about current or future Kansas conditions.

## Placement

- Semantic meaning: `contracts/domains/water_planning/planning_scenario_manifest.md`
- Machine shape: `schemas/contracts/v1/domains/water_planning/planning_scenario_manifest.schema.json`
- Synthetic examples: `fixtures/domains/water_planning/planning_scenario_manifest/`
- Deterministic validation: `tools/validators/domains/water_planning/validate_planning_scenario_manifest.py`
- Executable proof: `tests/validators/test_validate_planning_scenario_manifest.py`

This uses the existing water-planning bounded context under the responsibility roots adopted by ADR-0029. It creates no parallel schema, policy, data, or release authority.

## Required semantics

The manifest must:

- identify itself as synthetic and exploratory;
- use generalized geography and carry no exact geometry;
- distinguish the baseline date from the future scenario horizon;
- expose every input variable, data vintage, assumption, uncertainty, equity dimension, and participation reference;
- bind every displayed evidence reference to the manifest's declared evidence set;
- provide a short public-safe summary candidate and a fuller drawer payload with matching finite outcomes;
- display `NOT_A_PREDICTION`, `NOT_EMERGENCY_ALERTING`, and `NOT_REGULATORY_DETERMINATION` labels;
- keep evidence, policy, review, release, and publication authority flags false in the fixture-only profile; and
- carry correction and rollback references without claiming those actions occurred.

## Anti-collapse boundaries

| This object | Must not be treated as |
|---|---|
| Exploratory scenario | Prediction, forecast, alert, warning, or recommendation |
| Public-safe summary candidate | Published public content or release approval |
| Participation reference | Consent, consensus, endorsement, or representative completeness |
| Equity dimension | Finding of impact, eligibility, need, or legal status |
| Data vintage reference | Evidence resolution, source freshness, or rights clearance |
| Drawer payload | Proof that a UI rendered or exposed the payload |
| Passing validator result | Evidence, policy, review, release, or publication authority |

## Fail-closed invariants

- `horizon_start` must precede `horizon_end`, and the baseline date may not follow the horizon start.
- Reference lists and identity-bearing object arrays are unique and canonically ordered.
- Drawer assumption, equity, participation, and evidence references must match the manifest declarations.
- The summary and drawer outcomes must agree.
- Internal lifecycle references are denied on the public-safe summary and drawer surfaces.
- `READY_FOR_REVIEW` requires both policy-decision and review references; the synthetic pilot remains `HELD`.
- The executable `spec_hash` binds the RFC 8785 canonical body excluding the `spec_hash` member itself.

## Non-effects and rollback

This contract activates no source, model, alert, policy, review, release, public route, or publication. Removing the contract, schema, fixtures, validator, tests, workflow, and receipt reverts the slice without migrating governed data because no governed instance is created.
