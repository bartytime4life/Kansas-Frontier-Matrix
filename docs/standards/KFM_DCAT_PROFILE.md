<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-standards-kfm-dcat-profile
title: KFM DCAT Profile
type: standard
version: v1
status: draft
owners: NEEDS_VERIFICATION
created: 2026-04-28
updated: 2026-04-28
policy_label: NEEDS_VERIFICATION
related: [README.md, KFM_STAC_PROFILE.md, KFM_PROV_PROFILE.md, ../../schemas/catalog/dcat_dataset.schema.json, ../../contracts/v1/catalog/dcat/kfm_dcat_dataset.schema.json]
tags: [kfm, standards, dcat, metadata, profile]
notes: [Routing standard for DCAT obligations; machine checks must remain external.]
[/KFM_META_BLOCK_V2] -->

# KFM DCAT Profile

Defines KFM’s outward DCAT documentation posture for dataset/distribution discovery.

## Scope

This profile governs prose-level expectations for field meaning, public discovery semantics, and release-facing metadata consistency.

## Baseline expectations

1. DCAT records should remain traceable to governed release and provenance objects.
2. Rights/sensitivity labels must remain explicit.
3. Reviewers should be able to locate schema and test coverage for each normative claim.

## Non-goals

- Not a replacement for JSON Schema.
- Not proof of publication eligibility.

## Proof burden

Changes here should trigger companion review in schema, contract, policy, and test lanes.
