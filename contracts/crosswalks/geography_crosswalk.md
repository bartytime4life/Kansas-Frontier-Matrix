<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/crosswalks/geography-crosswalk
title: GeographyCrosswalk Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD - Geography steward; Crosswalk steward; Contract steward; Evidence steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; crosswalk; geography; no-network
owning_root: contracts/
responsibility: Define a version-pinned, direction-specific geography mapping declaration without resolving geography, executing joins, upgrading source roles, or changing release state.
truth_posture: CONFIRMED source and repository gap / PROPOSED inactive profile / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ../../schemas/contracts/v1/crosswalks/geography_crosswalk.schema.json
  - ../../fixtures/contracts/v1/crosswalks/geography_crosswalk/cases.json
  - ../../tools/validators/validate_geography_crosswalk.py
  - ../../tests/validators/test_validate_geography_crosswalk.py
  - ../../docs/intake/exploratory/pass-20-geography-crosswalk-source-map.md
  - ../common/geography_version.md
tags: [kfm, crosswalk, geography, version, deterministic, fixture-only]
notes:
  - "Implements the separately reviewed crosswalk dependency required by GeographyVersion and Pass 20 KFM-IDX-APP-008."
  - "A validated declaration is not a boundary comparison, identity equivalence, executed join, evidence resolution, review approval, release record, or publication authority."
[/KFM_META_BLOCK_V2] -->

# GeographyCrosswalk Candidate

> A deterministic declaration of how feature identities from one pinned `GeographyVersion` may map to another.

## Purpose

`GeographyVersion` correctly refuses to infer identity across versions. A downstream county-year comparison therefore needs a separate object that can declare a reviewed mapping without placing crosswalk rows, schemas, policy, validation, and registry state in one authority surface.

This fixture-only profile records:

- distinct digest-bound source and target `GeographyVersion` references;
- one forward-only, version-pinned method reference;
- digest-only source and target feature identifiers;
- exact, split, merge, partial-overlap, and unmapped relations;
- integer-millionth weights to avoid floating-point identity drift;
- unresolved evidence, rights, sensitivity, policy, and review posture; and
- deterministic RFC 8785 JCS plus SHA-256 identity.

It contains no coordinates, boundary features, names, source payloads, observations, county values, or released artifacts.

## Mapping rules

| Relation | Required declaration |
|---|---|
| `EXACT` | One target with weight `1000000`; identity equivalence is not inferred outside this direction and version pair. |
| `SPLIT` | Two or more ordered targets whose weights total `1000000`. |
| `MERGE` | One target with weight `1000000`; at least two source rows must declare the same merge target. |
| `PARTIAL_OVERLAP` | One or more ordered targets with a positive total below `1000000`. |
| `UNMAPPED` | No targets and reason `NO_SUPPORTED_TARGET`. |

Rows are ordered by source digest. Targets and evidence references are unique and lexically ordered. A target reused by multiple source rows is coherent only when all such rows declare `MERGE`.

## Evidence and authority boundary

Evidence references remain opaque and unresolved. A passing fixture proves only declaration coherence and deterministic identity. It does not prove that either geography, boundary artifact, feature identity, method, mapping row, weight, evidence record, rights decision, sensitivity decision, policy decision, review, release, or public product exists or is correct.

The validator performs no source fetch, geometry comparison, overlay, join, reverse mapping, identity resolution, policy evaluation, promotion, release, publication, or deployment.

## Deterministic identity

The validator removes only `crosswalk_id` and `spec_hash`, canonicalizes the remaining object with RFC 8785 JCS, and computes SHA-256.

```text
spec_hash   = SHA-256(JCS(identity subject))
crosswalk_id = kfm:geography-crosswalk:<first 24 digest hex>
```

## Directory Rules basis

The primary responsibility is governed mapping meaning, so the semantic contract belongs in the existing `contracts/crosswalks/` family. Machine shape belongs in `schemas/contracts/v1/crosswalks/`; synthetic replay in `fixtures/contracts/v1/crosswalks/`; reusable validation in `tools/validators/`; executable conformance in `tests/validators/`; read-only orchestration in `.github/workflows/`; source reconciliation in `docs/intake/exploratory/`; and authoring provenance in `data/receipts/generated/`.

These are existing responsibility roots under ADR-0029. The packet creates no root, geography store, crosswalk registry record, evidence store, policy home, runtime, public API, release lane, or publication path.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_geography_crosswalk
python tools/validators/validate_geography_crosswalk.py --fixtures
```

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the additive packet. No source, geography, evidence, crosswalk registry, lifecycle, policy, deployment, release, or public state requires restoration.
