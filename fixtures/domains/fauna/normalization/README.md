<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures/domains/fauna/normalization/readme
title: Fauna Normalization Fixtures
type: readme
version: v0.1
status: draft
owners: ["@bartytime4life - repository review route"]
created: 2026-10-29
updated: 2026-10-29
policy_label: public
owning_root: fixtures/
responsibility: Synthetic taxonomy snapshot input for offline Fauna tests
truth_posture: CONFIRMED synthetic fixture; no real species or occurrence evidence
tags: [fauna, fixtures, synthetic, taxonomy]
[/KFM_META_BLOCK_V2] -->

# Fauna normalization fixtures

`taxonomy_snapshot.json` contains invented taxa and fixture-only identifiers.
One explicit synonym resolves; one synonym deliberately matches two concepts
and must abstain. The fixture is not an authority snapshot or admitted source.

The [closed draft schema](../../../../schemas/contracts/v1/domains/fauna/taxonomy_snapshot.schema.json)
owns its machine shape. Existing source-shaped test records remain under
[`occurrence_evidence/`](../occurrence_evidence/README.md); tests derive bounded
negative cases in memory. No real locations or private source payloads belong
here. See the [implementation guide](../../../../docs/domains/fauna/normalization.md).
