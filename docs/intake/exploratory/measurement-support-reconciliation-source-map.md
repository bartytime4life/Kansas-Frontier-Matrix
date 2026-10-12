<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/measurement-support-reconciliation-source-map
title: Measurement Support Reconciliation - Source Map and Implementation Boundary
type: exploratory-intake-source-map
version: v0.1.0
status: promoted-to-fixture-candidate; non-authoritative; repository-grounded
owners: OWNER_TBD — Intake steward · Measurement steward · affected domain stewards
created: 2026-08-09
updated: 2026-08-09
policy_label: public; intake; measurement; comparison; cite-or-abstain
owning_root: docs/
responsibility: Preserve traceability from the supplied Full Atlas measurement-support cards and the New Ideas 4-30 source map to one bounded repository candidate without promoting source prose into scientific, policy, review, release, or publication authority.
truth_posture: CONFIRMED source-card traceability and inspected-tree collision review / PROPOSED bounded adaptation / NEEDS VERIFICATION steward review and later-main collisions
related:
  - ../../kfm_full_atlas_seed_cards.md
  - ./new-ideas-4-30-source-map.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/common/measurement_support_reconciliation.md
  - ../../../contracts/common/condition_relation.md
tags: [kfm, intake, full-atlas, measurement-support, unit-transform, scale-reconciliation]
notes:
  - "The source cards are design lineage, not evidence that a scientific method, threshold, source, or comparison is accepted."
  - "Repository collision review was performed against main@1ab34018d7fb13ad41cfe8a79aed5d4763e58bf8."
[/KFM_META_BLOCK_V2] -->

# Measurement support reconciliation - source map

> **Outcome:** `KFM-TRIAD-048` and programming card `KFM-CAND-0144` are adapted into one synthetic, no-network contract packet. The packet preserves support differences and can only return `PASS/REVIEW_REQUIRED`, `ABSTAIN/HOLD`, `DENY`, or `ERROR`. It activates no source and authorizes no comparison for production or public use.

## Source lineage

| Source | Relevant proposal | Posture used here |
|---|---|---|
| Supplied `KFM_Full_Atlas_seed_cards.md` | `KFM-TRIAD-048`, `KFM-CAND-0142` through `KFM-CAND-0144`, and Slice K | Design lineage for a common support/reconciliation seam. |
| `docs/intake/exploratory/new-ideas-4-30-source-map.md` | Packet pages 21-29 and 197; explicit repository gap for `MeasurementSupport` and `ScaleReconciliationReport` | Repository-grounded prior triage; external facts and packet thresholds remain unverified. |
| `contracts/common/condition_relation.md` | Cross-domain source-role, support-type, time, scale, and weighting boundary | Existing adjacent semantic authority; this packet does not replace it. |
| `docs/doctrine/directory-rules.md` plus accepted ADR-0029 | Responsibility-root placement and no-parallel-authority rules | Placement authority. |

## Current-main collision review

At `main@1ab34018d7fb13ad41cfe8a79aed5d4763e58bf8`, bounded searches found many domain-specific unit, depth, resolution, quality, co-location, and source-role fields, plus the shared `ConditionRelation` contract. No shared executable packet named `MeasurementSupport`, `UnitTransformReceipt`, `ScaleReconciliationReport`, `ComparisonFitnessDecision`, or semantic equivalent that jointly closes all of those axes was found.

This finding is **CONFIRMED for the inspected tree**, not a timeless claim. The implementation therefore adds one common candidate rather than altering domain observation contracts or creating a new domain lane.

## Bounded adaptation

The candidate keeps:

- exactly two synthetic support declarations;
- explicit measured, modeled, or derived character;
- reviewed unit-transform and resampling declarations;
- separate parameter, unit, vertical, temporal, spatial, knowledge-character, uncertainty, quality, and no-data axes;
- deterministic identity and exact fixture polarity; and
- fixed false authority flags.

It deliberately excludes:

- live station, satellite, forecast, or model data;
- source activation, network access, real geometry, and credentials;
- adopted conversions beyond the synthetic test pairs;
- scientific thresholds, calibration, fusion, interpolation, or causal inference;
- evidence resolution, policy decisions, review approval, promotion, release, deployment, publication, and public use.

## Directory Rules placement

| Artifact responsibility | Path |
|---|---|
| Shared semantic meaning | `contracts/common/measurement_support_reconciliation.md` |
| Canonical machine shape | `schemas/contracts/v1/common/measurement_support_reconciliation.schema.json` |
| Reusable synthetic cases | `fixtures/contracts/v1/common/measurement_support_reconciliation/cases.json` |
| Repository validator | `tools/validators/validate_measurement_support_reconciliation.py` |
| Executable evidence | `tests/validators/test_validate_measurement_support_reconciliation.py` |
| Hosted orchestration | `.github/workflows/measurement-support-reconciliation.yml` |
| Human source adaptation | This file under `docs/intake/exploratory/` |
| AI-authoring process memory | `data/receipts/generated/` |

No root, domain, source, policy, evidence, lifecycle, proof, release, or publication home is created.

## Validation and rollback

Validation covers Draft 2020-12 schema validity, exact `PASS/ABSTAIN/DENY` fixture polarity, unit arithmetic, support-window checks, derived summaries, deterministic identity, parser bounds, no-network behavior, adjacent `ConditionRelation` regression tests, workflow parsing, documentation metadata, and generated-receipt hashes.

Rollback is an ordinary revert of the additive packet. Because no live source, stored value, scientific transform, policy, release, runtime, cache, or publication state is created, no operational data migration is required.
