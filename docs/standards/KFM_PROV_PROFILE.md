<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-standards-kfm-prov-profile
title: KFM PROV Profile
type: standard
version: v1
status: draft
owners: NEEDS_VERIFICATION
created: 2026-04-28
updated: 2026-04-28
policy_label: NEEDS_VERIFICATION
related: [README.md, KFM_STAC_PROFILE.md, KFM_DCAT_PROFILE.md, ../../schemas/catalog/prov_document.schema.json, ../../contracts/v1/provenance/kfm_prov_sidecar.schema.json]
tags: [kfm, standards, provenance, prov, lineage]
notes: [Describes lineage expectations; enforcement requires validated artifacts and gates.]
[/KFM_META_BLOCK_V2] -->

# KFM PROV Profile

Human-readable lineage and provenance expectations for KFM release and catalog surfaces.

## Scope

Use this document for cross-cutting provenance conventions that need clear reviewer interpretation.

## Baseline expectations

1. Provenance should expose entities/activities/agents needed for traceability.
2. Claims about derivation must map to evidence-bearing artifacts.
3. Sensitive source details must respect policy and sovereignty constraints.

## Non-goals

- This file is not a PROV serializer.
- This file does not guarantee complete provenance coverage in every lane.
