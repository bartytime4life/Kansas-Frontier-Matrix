<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/coverage-priority-scorecard
title: CoveragePriorityScorecard Contract
type: contract
version: v0.1.0
status: proposed; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — analytics steward; coverage steward; governance steward; validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; workflow-triage; exploration-bias; fail-closed
owning_root: contracts/
responsibility: Make work-priority scoring, missingness, source-role concentration, costs, and counterfactual rank changes inspectable without creating ecological or assignment authority.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/governance/coverage_priority_scorecard.schema.json
  - ../../tools/validators/governance/validate_coverage_priority_scorecard.py
  - ../../fixtures/contracts/v1/governance/coverage_priority_scorecard/cases.json
  - ../../tests/validators/governance/test_coverage_priority_scorecard.py
  - ../../docs/intake/exploratory/full-atlas-coverage-priority-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "A scorecard is an inspectable workflow-triage aid, never a biodiversity, conservation, funding, source-activation, work-assignment, or publication decision."
  - "The fixture compares density-led and coverage-gap-led weights over synthetic areas only."
[/KFM_META_BLOCK_V2] -->

# CoveragePriorityScorecard

> **Purpose.** Expose how record density, sampling history, coverage gaps, uncertainty, source concentration, sensitivity, capacity, public value, and review cost change a proposed work queue.

## Source basis

Full Atlas `KFM-TRIAD-047` and programming card `KFM-CAND-0141` call for `CoveragePriorityProfile` and `PriorityScorecard` with versioned weights, source-role caps, explicit missingness, costs, counterfactual rankings, stability checks, and non-authorizing receipts. This profile implements that bounded fixture seam. It does not choose real counties or adopt a policy threshold.

## Scoring profile

Every weight profile declares ten integer weights whose sum is exactly `1000`. Benefits are added; `sensitivity_burden` and `review_cost` are subtracted:

```text
score = Σ(weight × benefit metric)
      − weight × sensitivity_burden
      − weight × review_cost
      − missingness_penalty
```

Metrics are integer values from `0` through `100`. No floating-point rounding is used. Each profile independently declares `PENALIZE`, `NEUTRAL_ZERO`, or `ABSTAIN` missingness treatment and a maximum source-role share in basis points. An area exceeding the cap is not ranked under that profile.

## Required comparison

The fixture contains a density-led and a coverage-gap-led profile. Each ranking exposes all component contributions, missingness penalty, source-cap state, score, and rank. The scorecard records rank correlation and rank flips. A changed counterfactual ranking is expected evidence of sensitivity to declared choices, not a defect to conceal.

## Finite posture

A complete, internally coherent scorecard declares decision `HOLD`; unresolved missingness or source-role concentration declares `ABSTAIN`. The validator's positive result is also `HOLD`, meaning only that the proposed fixture is coherent. Schema, derivation, identity, or authority failures return `DENY`. There is no `ALLOW`, `ASSIGN`, `ACTIVATE`, `RELEASE`, or `PUBLISH` state.

Required obligations keep components visible, label the output as workflow triage, and prohibit ecological-importance inference. Human stewards remain responsible for any later work selection.

## Identity and directory basis

`spec_hash` is RFC 8785 JCS plus SHA-256 over the scorecard with `scorecard_id` and `spec_hash` omitted. `scorecard_id` is `kfm:coverage-priority-scorecard:<digest>`.

Cross-domain work-selection meaning belongs in `contracts/governance/`; shape in `schemas/contracts/v1/governance/`; validation in `tools/validators/governance/`; fixtures in `fixtures/contracts/v1/governance/`; tests in `tests/validators/governance/`; provenance in `data/receipts/generated/`. No new root or parallel authority is created.

## Non-effects and rollback

The profile uses synthetic non-geographic areas, performs no network access, activates no source, assigns no work or funding, and makes no ecological, policy, review, release, or publication decision. Revert the bounded commit to remove it.
