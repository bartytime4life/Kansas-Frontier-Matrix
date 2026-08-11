<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/geography-version
title: GeographyVersion Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD - Geography steward; Contract steward; Evidence steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; common; geography; versioning; no-network
owning_root: contracts/
responsibility: Define one immutable, version-bounded geography declaration without carrying geometry, resolving evidence, authorizing cross-version joins, or changing release state.
truth_posture: CONFIRMED source and repository gap / PROPOSED inactive profile / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ../../schemas/contracts/v1/common/geography_version.schema.json
  - ../../fixtures/contracts/v1/common/geography_version/cases.json
  - ../../tools/validators/validate_geography_version.py
  - ../../tests/validators/test_validate_geography_version.py
  - ../../docs/intake/exploratory/pass-20-geography-version-source-map.md
  - ../evidence/indicator_definition.md
tags: [kfm, common, geography, version, crosswalk, deterministic, fixture-only]
notes:
  - "Implements one bounded dependency named by Pass 20 KFM-IDX-APP-008 and already required by IndicatorDefinition support semantics."
  - "A validated declaration is not a boundary dataset, geography crosswalk, currentness proof, policy decision, release record, or publication authority."
[/KFM_META_BLOCK_V2] -->

# GeographyVersion Candidate

> A deterministic declaration of which geography vocabulary and boundary artifact one downstream analytic result intends to use.

## Purpose

County-year and other area-time analytics need to disclose the exact geography vintage used for joins. The current `IndicatorDefinition` profile already requires geography-version discipline, while the Pass 20 frontier-demography concept names `GeographyVersion` as a foundational object. This profile fills only that shared declaration seam.

A `GeographyVersion` records:

- a stable geography key, kind, unit level, jurisdiction, and source role;
- digest-bound source-descriptor, definition, boundary-artifact, CRS, and feature-identity references;
- source-valid, publication, and retrieval times without treating retrieval time as valid time;
- version-local identity semantics;
- predecessor and crosswalk posture without inferring a crosswalk;
- whether a referenced geometry is source-native, generalized, or synthetic;
- digest-bound evidence references and mandatory interpretation limits; and
- deterministic RFC 8785 JCS plus SHA-256 identity.

The object contains no coordinates, features, observations, population values, economic values, classifications, source payloads, or released artifacts.

## Version and join rules

| Concern | Required posture |
|---|---|
| Feature identity | `VERSION_LOCAL`; reuse across versions is never inferred |
| Different-version join | Requires a separately reviewed crosswalk |
| No predecessor | `crosswalk_state: NOT_APPLICABLE` and no crosswalk reference |
| Known predecessor, no crosswalk | `crosswalk_state: UNRESOLVED`; no cross-version join authority |
| Known predecessor and crosswalk | `REFERENCED_NOT_RESOLVED`; the reference is not resolved by this validator |
| Generalized geometry | Requires a digest-bound transform-receipt reference |

An open-ended `valid_to` is representable as `null`. When present, `valid_to` must be later than `valid_from`. Retrieval may not precede the declared publication instant.

## Evidence and authority boundary

Evidence references remain opaque and unresolved. A passing fixture proves only declaration coherence and deterministic identity. It does not prove:

- the referenced source or artifact exists, is current, or is admissible;
- the boundary geometry is authoritative, complete, accurate, or public-safe;
- feature IDs are stable outside the declared version;
- a predecessor, successor, or crosswalk is scientifically or administratively valid;
- any county-year observation or classification is correct; or
- policy, review, promotion, release, public use, publication, or deployment is authorized.

## Deterministic identity

The validator removes only `geography_version_id` and `spec_hash`, canonicalizes the remaining object with RFC 8785 JCS, and computes SHA-256.

```text
spec_hash           = SHA-256(JCS(identity subject))
geography_version_id = kfm:geography-version:<first 24 digest hex>
```

Evidence and disclosure arrays are unique and lexical. Order, duplicate, time, crosswalk, transform, stored-identity, or authority drift fails closed.

## Directory Rules basis

`GeographyVersion` is a cross-domain shared value object, so semantic meaning belongs in `contracts/common/`. Machine shape belongs in `schemas/contracts/v1/common/`; synthetic replay in `fixtures/contracts/v1/common/`; reusable validation in `tools/validators/`; executable conformance evidence in `tests/validators/`; read-only orchestration in `.github/workflows/`; source reconciliation in `docs/intake/exploratory/`; and authoring provenance in `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. The packet creates no root, geography data store, domain authority, crosswalk registry, evidence store, policy home, runtime, public API, release lane, or publication path.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_geography_version
python tools/validators/validate_geography_version.py --fixtures
```

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the additive packet. Because this profile is inactive and fixture-only, no source, geometry, evidence, lifecycle, policy, deployment, release, or public state requires restoration.
