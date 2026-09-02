# PlanningScenarioManifest synthetic fixtures

This directory contains one generalized Kansas drought-planning scenario and bounded negative cases for the proposed `PlanningScenarioManifest` contract.

- `valid/valid_1.json` is synthetic. It contains no real person, project, alert, forecast, regulatory determination, exact geometry, or current-condition claim.
- `invalid/invalid_1.json` proves structural rejection.
- `cases.json` applies deterministic, schema-valid mutations to the valid fixture and records exact semantic findings.

Passing these fixtures proves local shape and bounded semantic behavior only. It does not resolve evidence, source freshness, participation completeness, rights, sensitivity, policy, review, release, UI rendering, or publication.
