<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/cover-class-crosswalk-profile-source-map
title: Habitat Cover-Class Crosswalk Profile Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Habitat steward · Land-cover steward · Crosswalk steward · Contract steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded adaptation of ontology-version and class-crosswalk drift safeguards into a bounded Habitat fixture candidate
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/domains/habitat/land_cover/cover_class_crosswalk_profile.md
  - ../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../domains/habitat/sublanes/land_cover.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, habitat, land-cover, crosswalk, ontology, versioning, drift, source-map]
[/KFM_META_BLOCK_V2] -->

# Habitat Cover-Class Crosswalk Profile Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| Attached `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`, SHA-256 `57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780` | `KFM-IDX-MOD-004` states that categorical products—including landcover—need ontology/version references and drift checks; missing remaps should fail closed so numerical continuity cannot mask semantic discontinuity. | Confirmed idea-index requirement, not proof of a current registry, crosswalk, mapping, or pipeline. |
| Attached `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`, SHA-256 `020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639`, PDF page 853 | Stable card `KFM-P4-PROG-0006` carries the same ontology/version rule, calls for `classmap_version`, remapping tables, source version, and schema validation, and leaves crosswalk ownership open. | Atlas card is source doctrine; repository implementation status is explicitly unknown in the source. |
| Google Drive `KFM_Full_Atlas_seed_cards`, document `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho` | The `Connector and Watcher as Anti-Corruption Layer Capability` proposal calls for `classmap_version`, crosswalk version, and translator identity so external semantics cannot become shadow authority. | Connector-wide proposal; this packet does not change connectors, watchers, SourceDescriptors, or activation. |
| Repository `main` at `7335ed9ea0f81342ae0b1c7828a21ac74711c78b` | The Habitat land-cover contract already defines `CoverClassCrosswalk` as a directional, reviewed, citable mapping; it requires complete class inventory, visible lossiness, source-role preservation, correction, and rollback. Its paired schema is an intentionally permissive scaffold. | The additive profile must not silently tighten the scaffold, claim review, or activate a real source pair. |

## Repository reconciliation

GitHub was inspected on 2026-08-09 with no open pull requests before this work.
Recent merged changes covered renderer capabilities, object-family/domain
references, catalog behavior, and several domain-specific profiles. Live
`main` did not contain `CoverClassCrosswalkProfileCandidate`, its closed
profile schema, fixture cases, executable validator, tests, workflow, source
map, or receipt.

The repository already had the broad Habitat crosswalk contract, a permissive
scaffold schema, fixture/test lane documentation, and a Habitat validator
lane. The packet therefore adds a discriminator-bound profile instead of
replacing the scaffold or selecting a production scheme pair.

## Bounded adaptation

| Source pressure | Retained behavior | Held boundary |
|---|---|---|
| Pin categorical semantics | Source and target schemes carry explicit versions and version-bound ontology URNs. | Synthetic URNs do not activate or authenticate a real ontology. |
| Fail closed on missing remaps | Every declared source code must appear exactly once; explicit `UNMAPPED` and `DENIED` rows still deny the candidate. | The validator does not invent mappings or recode bytes. |
| Expose lossiness | Many-to-one aggregation and one-to-many split states require loss and caveat flags. | A declared caveat is not evidence that a real mapping is acceptable. |
| Preserve direction | The profile is forward-only; bidirectional review requests deny. | Human/steward review cannot be represented by fixture success. |
| Prevent shadow authority | Source roles remain distinct and all evidence, policy, renderer, release, and publication authority flags are false. | No connector, source, renderer, observation, summary, layer, or release is created. |

## Path decision

~~~yaml
path_decision:
  artifact: CoverClassCrosswalkProfileCandidate
  proposed_path: contracts/domains/habitat/land_cover/cover_class_crosswalk_profile.md
  artifact_kind: semantic contract profile
  authority_owner: fixture-only version-bound crosswalk meaning
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: domain
  scope_id: habitat/land_cover/crosswalk
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - contracts/domains/habitat/land_cover/crosswalk.md
    - docs/domains/habitat/sublanes/land_cover.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

The established Habitat land-cover contract lane owns candidate meaning.
Schema, fixtures, validator, tests, workflow, source map, and receipt remain in
their separate responsibility roots. A real crosswalk instance, source pair,
registry record, mapping table, pipeline, policy, or release would require a
separate reviewed change.

## Non-effects

This packet does not download, activate, classify, map, recode, transform,
render, compare, aggregate, release, or publish real land-cover data; create a
scheme or ontology registry; resolve evidence; decide policy; approve review;
upgrade source role; authorize reverse use; alter a public layer; or authorize
public use.
