<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-standards-kfm-stac-profile
title: KFM STAC Profile
type: standard
version: v1
status: draft
owners: NEEDS_VERIFICATION
created: 2026-04-28
updated: 2026-04-28
policy_label: NEEDS_VERIFICATION
related: [README.md, KFM_DCAT_PROFILE.md, KFM_PROV_PROFILE.md, ../../schemas/catalog/stac_item.schema.json, ../../contracts/v1/catalog/stac/kfm_stac_item.schema.json]
tags: [kfm, standards, stac, catalog, profile]
notes: [Profile-level guidance only; executable validation remains in schema, policy, and tests.]
[/KFM_META_BLOCK_V2] -->

# KFM STAC Profile

This document defines the human-readable STAC posture for KFM publication metadata.

## Scope

Use this profile for STAC-facing requirements that KFM maintainers can review in prose before enforcing them in schemas, validators, fixtures, and policies.

## Baseline expectations

1. Every outward STAC Item should resolve to an evidence-bearing lineage path.
2. Any restricted or sensitive content must fail closed through policy labels and review outcomes.
3. STAC assets should be explainable via associated contract/schema surfaces.

## Non-goals

- This file does not replace schema validation.
- This file does not claim workflow or platform enforcement.

## Proof burden

When changing this profile, update or verify companion surfaces in:

- `schemas/**`
- `contracts/**`
- `policy/**`
- `tests/**`
