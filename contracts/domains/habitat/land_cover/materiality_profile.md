<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/habitat/land-cover/materiality-profile
title: Habitat Land-Cover Materiality Profile Contract
type: semantic-contract; domain-profile; material-change-adapter
version: v0.1.0
status: proposed; inactive; fixture-first; no-network
owners: OWNER_TBD — Habitat steward · Land-cover steward · Contract steward · Validation steward
created: 2026-08-04
updated: 2026-08-04
policy_label: public; habitat; land-cover; materiality; non-publisher
related:
  - ./change_summary.md
  - ../../../../data/material_change_assessment.md
  - ../../../../../schemas/contracts/v1/domains/habitat/land_cover/materiality_profile.schema.json
  - ../../../../../pipeline_specs/habitat/land_cover/materiality_profile.v1.json
  - ../../../../../tools/validators/domains/habitat/validate_land_cover_materiality.py
tags: [kfm, habitat, land-cover, materiality, non-event, county, fixture-first]
[/KFM_META_BLOCK_V2] -->

# Habitat land-cover materiality profile

> This profile is the first domain adapter for the shared
> `MaterialChangeAssessment` object. It converts a declared county land-cover
> comparison into `NON_EVENT`, `PROMOTION_CANDIDATE`, or `HOLD` process memory.
> It does not activate a source, decide policy, authorize promotion, release a
> layer, or publish land-cover truth.

## Scope

The first profile is deliberately narrow:

| Dimension | Bound value |
|---|---|
| Domain | `habitat` |
| Sublane | `land_cover` |
| Analysis unit | Kansas county or county-equivalent comparison supplied by a fixture |
| Source access | None; synthetic input only |
| Combination rule | `ANY` declared trigger may classify the semantic change as material |
| Canonicalization | `kfm-canonical-json-v1`; SHA-256 |
| Status | `PROPOSED_INACTIVE` |

The profile does not assert that the thresholds are scientifically, legally, or
operationally accepted. Threshold adoption and live-source use remain separate steward,
policy, source-admission, and release decisions.

## Declared triggers

The profile carries forward the explicit thresholds already documented in the land-cover
change-summary contract:

1. `reclassification_fraction > 0.02`; or
2. `max_net_class_delta_ha > max(250 ha, analysis_unit_area_ha * 0.0015)`.

The adapter represents this `ANY` rule as one required composite criterion,
`county-materiality-any`, plus two optional diagnostic criteria. This preserves the
shared `MaterialChangeAssessment` invariant that every required criterion must pass for
a `MATERIAL` classification while keeping the domain trigger semantics inspectable.

## Outcome mapping

| Input state | Shared classification | Outcome |
|---|---|---|
| Identical digests | `UNCHANGED` | `NON_EVENT` |
| Byte difference, no semantic difference | `BYTE_ONLY` | `NON_EVENT` |
| Semantic difference, both triggers fail | `SEMANTIC_NON_MATERIAL` | `NON_EVENT` |
| Semantic difference, either trigger passes | `MATERIAL` | `PROMOTION_CANDIDATE` |
| Unsupported analysis unit or unavailable semantic state | `UNDETERMINED` | `HOLD` |
| Invalid fixture/profile input | Adapter finding; no authoritative assessment emitted | fail closed |

`PROMOTION_CANDIDATE` means only that later evidence, rights, sensitivity, policy,
review, proof, release, correction, and rollback gates may inspect the candidate.

## Identity and replay

`materiality_profile.v1.json` contains `spec_hash`, calculated as SHA-256 over canonical
JSON after removing the `spec_hash` field. The validator recomputes it. Assessment
records bind the same hash in both `profile.spec_hash` and `governance.spec_hash`.

The profile is deterministic for the same profile bytes and candidate fixture. A profile
change requires a new version/hash and replay rather than silent mutation.

## Authority boundary

This adapter:

- reads no live network source;
- does not interpret NLCD, CDL, LANDFIRE, NWI, or another source as admitted;
- does not decide source role, rights, or sensitivity;
- does not infer habitat or species occurrence;
- does not evaluate policy or review;
- does not authorize promotion, release, rollback, or publication;
- does not write lifecycle data.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/habitat \
  --pattern 'test_land_cover_materiality.py' \
  --verbose

python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures
```

The focused tests require every emitted object to pass the shared
`MaterialChangeAssessment` validator.

## Rollback

Before merge, close the draft pull request. After merge, revert the contract, schema,
inactive profile, adapter, fixtures, tests, workflow, and generated receipt together. No
source, lifecycle object, release, or public artifact is created, so rollback requires no
data deletion or public cache mutation.
