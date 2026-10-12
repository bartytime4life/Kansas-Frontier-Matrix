<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/stac-search-behavior-fixture-profile
title: STAC Search Behavior Fixture Profile Candidate
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Data steward · STAC steward · Schema steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; data; stac; search; fixture; no-network; non-release
source_card: KFM-P31-PROG-0005
source_spec_hash: sha256:df00897c204c95a693a4e86012d0ac6e2c57a2866478bfd0f55dce3d4b172db3
related:
  - ../../schemas/contracts/v1/data/stac_search_behavior_fixture_profile.schema.json
  - ../../fixtures/contracts/v1/data/stac_search_behavior_fixture_profile/cases.json
  - ../../tools/validators/stac/validate_stac_search_behavior_fixture_profile.py
  - ../../tests/validators/stac/test_stac_search_behavior_fixture_profile.py
tags: [kfm, data, stac, search, paging, fields, filter, query, fixture]
[/KFM_META_BLOCK_V2] -->

# STAC Search Behavior Fixture Profile Candidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This profile proves bounded synthetic search-request and response declarations. It performs no HTTP request, discovers no live catalog, verifies no server conformance, mutates no catalog, evaluates no policy, and grants no promotion, release, or publication authority.

## Source-derived gap

Pass 31 card `KFM-P31-PROG-0005` calls for smoke fixtures covering spatial and temporal search, field inclusion and exclusion, stable sorted paging, and filter/query constraints. Existing STAC contracts describe metadata and asset shape, but they do not encode this cross-page behavioral fixture. This candidate owns that narrow gap.

## Directory Rules basis

Semantic meaning belongs under `contracts/data/`; machine shape under `schemas/contracts/v1/data/`; synthetic cases under `fixtures/contracts/v1/data/`; reusable enforcement under `tools/validators/stac/`; and proof under `tests/validators/stac/`. The packet creates no alternate catalog, API client, policy, evidence, receipt, or publication home.

## Required meaning

| Surface | Meaning | Fail-closed boundary |
|---|---|---|
| `request.bbox` and `request.datetime` | Declared synthetic spatial and temporal constraints. | Bounding boxes and intervals must be ordered and finite. |
| `request.fields` | Sorted, disjoint include/exclude paths. | Every included path must be declared returned and every excluded path absent. |
| `request.sortby` | Ordered sort keys with final `id` tie-breaker. | Item sort tuples must form one strict global order across all pages. |
| `request.constraint_mode` | Exactly one synthetic `filter` or `query` form. | The inactive alternative must be null. |
| `pages` | Synthetic request/next-token chain and returned item summaries. | First request and final next token are null; intermediate tokens must connect exactly; item IDs are unique. |
| `controls` | Fixed no-network and non-authority posture. | Live HTTP, catalog discovery/mutation, policy, review, promotion, release, and publication effects remain false. |

## Identity

`spec_hash` is RFC 8785/JCS SHA-256 over the complete record after removing `profile_id` and `spec_hash`. `profile_id` is `kfm:stac-search-behavior:` followed by the first 24 hexadecimal digest characters.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/stac \
  --pattern 'test_stac_search_behavior_fixture_profile.py' \
  --verbose

python tools/validators/stac/validate_stac_search_behavior_fixture_profile.py --fixtures
```

A pass proves only schema closure, declared request/response consistency, stable fixture ordering, token continuity, non-authority controls, and deterministic identity.

## Rollback

Revert this additive packet. No live catalog, endpoint, policy result, promotion state, release, or publication is created.
