<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/admin-boundary-change
title: AdminBoundaryChange Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD - Geography steward; Contract steward; Evidence steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; common; geography; administrative-boundary; no-network
owning_root: contracts/
responsibility: Declare one source-supported administrative geography lineage event without carrying geometry, inferring identity, executing a crosswalk, transferring observations, or changing release state.
truth_posture: CONFIRMED source idea and adjacent geography contracts / PROPOSED inactive profile / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ../../schemas/contracts/v1/common/admin_boundary_change.schema.json
  - ../../fixtures/contracts/v1/common/admin_boundary_change/cases.json
  - ../../tools/validators/validate_admin_boundary_change.py
  - ../../tests/validators/test_validate_admin_boundary_change.py
  - ../../docs/intake/exploratory/admin-boundary-change-source-map.md
  - ./geography_version.md
  - ../crosswalks/geography_crosswalk.md
tags: [kfm, common, geography, administrative-boundary, lineage, crosswalk, fixture-only]
notes:
  - "Implements the AdminBoundaryChange object named by the Full Atlas Frontier Matrix lane and the version/crosswalk discipline described by the KFM Implementation Reference."
  - "A validated declaration is not legal or boundary truth, geometry, identity equivalence, an executed crosswalk, transferred observations, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# AdminBoundaryChange Candidate

> A deterministic declaration of one administrative geography lineage event between pinned `GeographyVersion` records.

## Purpose

Historical county-year analysis needs to explain when an administrative geography was created, dissolved, split, merged, annexed, detached, transferred, renamed, recoded, or revised. `GeographyVersion` already makes feature identity version-local, and `GeographyCrosswalk` already requires a separate, reviewed mapping. This profile fills only the event seam between them.

An `AdminBoundaryChange` records:

- event type, administrative level, jurisdiction, effective date, publication time, and retrieval time;
- digest-bound source and target `GeographyVersion` references;
- digest-bound predecessor and successor feature references;
- an optional separately governed `GeographyCrosswalk` reference;
- digest-bound source descriptor, dataset, legal-instrument, and evidence references;
- explicit source, rights, and sensitivity posture;
- mandatory interpretation limits and inactive governance flags; and
- deterministic RFC 8785 JCS plus SHA-256 identity.

It carries no coordinates, geometry, names, population values, observation values, crosswalk rows, weights, source payloads, or released artifacts.

## Event cardinality

| Change type | Source versions/features | Target versions/features |
|---|---:|---:|
| `CREATION` | exactly 0 | at least 1 |
| `DISSOLUTION` | at least 1 | exactly 0 |
| `SPLIT` | at least 1 | at least 2 |
| `MERGER` | at least 2 | at least 1 |
| `ANNEXATION`, `DETACHMENT`, `TRANSFER`, `RENAME`, `CODE_CHANGE`, `BOUNDARY_REVISION` | at least 1 | at least 1 |

The same geography-version or feature ref may not appear on both sides. This prevents accidental identity equivalence. Arrays are lexical and unique.

## Crosswalk posture

| Version sides | Allowed posture |
|---|---|
| A creation or dissolution has an empty side | `NOT_APPLICABLE`; `crosswalk_ref` is `null` |
| Both sides exist and no crosswalk is selected | `UNRESOLVED`; `crosswalk_ref` is `null` |
| Both sides exist and a crosswalk is cited | `REFERENCED_NOT_RESOLVED`; a digest-bound ref is required |

The validator never resolves or runs a crosswalk. `identity_scope` is fixed to `VERSION_LOCAL`, `identity_assertion` to `NONE`, and `different_version_join_policy` to `CROSSWALK_REQUIRED`.

## Time and source rules

- `retrieved_at` may not precede `source_published_at`.
- Publication may precede or follow the effective date; the two concepts are intentionally not collapsed.
- Source role is preserved as `OFFICIAL_ADMINISTRATIVE_NOTICE`, `STATISTICAL_HISTORY`, or `SYNTHETIC_FIXTURE`.
- References remain opaque and unresolved; a digest proves only the declared reference token, not the referenced content.

## Evidence and authority boundary

A passing fixture proves only closed shape, event cardinality, time coherence, explicit crosswalk posture, required limits, inactive governance flags, and deterministic identity. It does not prove:

- that a legal change occurred or that the effective date is correct;
- that any boundary, feature, source, instrument, evidence, or crosswalk exists or is authoritative;
- that predecessor and successor features are identical or comparable;
- that a population, observation, area, or statistic can be transferred;
- that policy, review, promotion, release, public use, publication, or deployment is authorized.

## Deterministic identity

The validator removes only `change_id` and `spec_hash`, canonicalizes the remaining object with RFC 8785 JCS, and computes SHA-256.

```text
spec_hash = SHA-256(JCS(identity subject))
change_id = kfm:admin-boundary-change:<first 24 digest hex>
```

## Directory Rules basis

The event is a cross-domain geography value object, so semantic meaning belongs in the accepted `contracts/common/` responsibility root beside `GeographyVersion`. Machine shape belongs in `schemas/contracts/v1/common/`; synthetic replay in `fixtures/contracts/v1/common/`; reusable validation in `tools/validators/`; executable conformance in `tests/validators/`; read-only orchestration in `.github/workflows/`; source reconciliation in `docs/intake/exploratory/`; and authoring provenance in `data/receipts/generated/`.

No new root, geography store, crosswalk registry record, policy home, runtime, public API, release lane, or publication path is created.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_admin_boundary_change
python tools/validators/validate_admin_boundary_change.py --fixtures
```

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert this additive packet. Because the profile is inactive and fixture-only, no source, geography, evidence, crosswalk, lifecycle, policy, deployment, release, or public state requires restoration.
