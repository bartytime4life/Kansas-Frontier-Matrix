<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-30-pm-sensor-trust-profile-source-map
title: Pass 30 PM Sensor Trust Profile Source Adaptation
type: source-adaptation-map
version: v1.0.0
status: proposed; exploratory; review-pending
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; intake; atmosphere; source-map
[/KFM_META_BLOCK_V2] -->

# Pass 30 PM Sensor Trust Profile Source Adaptation

## Source card

- Stable ID: `KFM-P30-PROG-0001`
- Title: `PM sensor trust schema`
- Status in consolidated atlas: active, unchanged
- Source ID: `SRC-P30-001`
- Spec hash: `sha256:6fed794c95d89545865ee4faa472ee9dc5906a073d2af0e22145fe16610b7b4f`
- Drive carrier: `gdrive://1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa#KFM-P30-PROG-0001`
- Supplied carrier: `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`

The source proposes a schema with accuracy, stability, responsiveness, consensus alignment, calibration version, and reference-anchor fields. It explicitly marks repository implementation status unknown.

## Repository assay

At assayed base `6947a2cbae6e02ce0bacedc74353f8dc3b430774`:

- `AirStation` separates station identity from calibration and quality proof.
- `PM25Observation` preserves low-cost-sensor caveats and calibration references.
- synthetic low-cost-sensor calibration fixtures preserve correction lineage, meteorology inputs, reference collocation, evidence, caveats, and anti-overclaim rules.
- no indexed repository file, branch, or pull request implements this source-card ID or the complete six-field trust profile.

## Adaptation decision

The smallest dependency-closed slice is a fixture-only declaration profile. It records independent dimensions and evidence closure but produces no composite trust score, scientific threshold, source admission, reference-grade equivalence, policy decision, promotion, release, publication, or health guidance.

## Placement

Directory Rules assigns Atmosphere semantic meaning to `contracts/domains/atmosphere/`, machine shape to `schemas/`, synthetic proof to `fixtures/`, enforcement to `tools/validators/` and `tests/`, and emitted authoring accountability to `data/receipts/generated/`.

## Truth posture

- **CONFIRMED:** source-card identity, statement, status, spec hash, and existing repository boundaries were inspected.
- **PROPOSED:** the new contract and profile semantics remain pending human steward review.
- **NEEDS VERIFICATION:** scientific metric methods, thresholds, live-source binding, schema registry admission, policy integration, and runtime use.
