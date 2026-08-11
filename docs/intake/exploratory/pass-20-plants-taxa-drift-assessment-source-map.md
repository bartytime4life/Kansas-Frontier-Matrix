<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-20-plants-taxa-drift-assessment
title: Pass 20 PLANTS Taxa-Drift Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Flora source steward · Taxonomy steward · Sensitivity steward · Contract steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; flora; plants; taxa-drift; sensitivity; non-publisher
responsibility: Preserve source and repository lineage for a bounded fixture-only PLANTS taxa-drift assessment without activating a source, selecting a conflicted watcher home, exposing locations, changing lifecycle state, or granting taxonomy, policy, review, or publication authority.
truth_posture: "CONFIRMED supplied Pass 20 Markdown, connected Drive source, inspected repository boundaries, and accepted Directory Rules; PROPOSED bounded assessment; UNKNOWN watcher placement, live source activation, current PLANTS interface, taxonomy/conservation authorities, and reviewer ownership; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/source/plants_taxa_drift_assessment.md
  - ../../../contracts/source/source_intake_record.md
  - ../../../contracts/source/watcher_registry.md
  - ../../../contracts/crosswalks/taxonomy/taxonomic_concept_lineage.md
  - ../../domains/flora/SOURCE_REGISTRY.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 20 PLANTS Taxa-Drift Assessment Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`, SHA-256 `57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780` | `KFM-IDX-ANA-004` requires taxa additions/removals under a stable taxonomy version, conservation-list intersection, avoidance of public exact-occurrence exposure, and sensitive/non-sensitive fixtures. `KFM-IDX-SRC-006` separates material source change from publication. `EXP-001` asks for mutated, unchanged, and missing-attestation fixture proofs with `WORK_CANDIDATE` posture. | `CONFIRMED` source statement |
| Connected Drive `New Ideas 5-19-26` (`1Gx4pU71Pqk1cG1oKb8l69B8K4yOJK7zy5KNH-Xvl4HQ`) | The document identifies USDA PLANTS as a standardized taxonomic/distribution scaffold and highlights natural-heritage sensitivity controls before map or score publication. Its broader code proposals are not treated as repository instructions. | `CONFIRMED` thematic corroboration |
| `docs/domains/flora/SOURCE_REGISTRY.md`, SHA-256 `f282fe8538bd94a2101b4955114cae5f87996639b37bc42bf7cfe76d61ba74be` | The repository already defines PLANTS taxa drift as a proposed implementation: stable taxonomy version, taxa set difference, conservation intersection, SourceIntakeRecord candidate, counts-only/withheld posture, and steward review for sensitive joins. | `CONFIRMED` existing domain meaning |
| `tools/ingest/plants_watch/README.md`, SHA-256 `ac9145a23458428cb12864cf9588e4c3c6c2e5abff65531c6722f7661e5fd932`, and `tools/watchers/plants_watch/README.md`, SHA-256 `6ddb44511a16f872644f6d334cc330d24424c582dae14b636bc7d1a5044a78aa` | Both paths are documentation-only. The latter explicitly records unresolved executable/specification placement, missing live activation, and absent representative fixtures/tests. | `CONFIRMED` placement conflict and inactive state |
| `contracts/crosswalks/taxonomy/taxonomic_concept_lineage.md`, SHA-256 `825f63bcd9a144ce75e4b2abaacb69914c3b6798e0d9aaeecc022d792d0311d0` | An existing candidate separates source-native name usage from taxon concepts through time. The new assessment binds it by opaque ref instead of inventing taxonomy identity or rename authority. | `CONFIRMED` adjacent responsibility |
| `contracts/source/source_intake_record.md`, SHA-256 `eedf1d84bf7f6fba9f40b7e27ea62966ebd4118f5197aa71a9351794f4e4bbd2`, and `contracts/source/watcher_registry.md`, SHA-256 `190a542215bdf06b3a07c6912aeeaea6504407097c1729471929725e4d7643e9` | The repository already owns intake-candidate meaning and watcher registration. The assessment carries only opaque refs and does not duplicate, emit, register, or resolve either object. | `CONFIRMED` adjacent responsibility |
| Starting `main@bd59127604f3ab7578fe43f30caaeef089c0fffc` plus repository, code, branch, and pull-request searches | CDL has a fixture-first executable, but no PLANTS taxa-drift assessment contract, schema, fixture matrix, validator, workflow, matching branch, or open matching pull request was found. | `CONFIRMED` inspected snapshot |

The source packet and connected Drive file are evidence inputs, not authority to
activate endpoints, copy proposed code, select a disputed path, or publish data.

## Collision and placement decision

| Candidate action | Existing repository state | Decision |
|---|---|---|
| Implement a live PLANTS watcher under one proposed tool/pipeline home. | Executable and specification homes remain explicitly conflicted; source activation and interface are unknown. | `ABSTAIN`; do not pre-empt an ADR or activation decision. |
| Create PLANTS domain doctrine or a second source registry entry. | Flora registry, source-family, source-intake, and watcher-boundary docs already carry the meaning. | `REUSE`; do not duplicate. |
| Create a new taxonomy object or rename resolver. | `TaxonomicConceptLineagePacket` already owns source-native concept history. | `REUSE` by opaque ref; no resolution. |
| Emit a real SourceIntakeRecord or watcher registry entry. | Those accepted/proposed families have separate ownership and lifecycle meaning. | `DENY` for this fixture packet. |
| Supply the missing sensitive/non-sensitive, changed/unchanged, and attestation-negative proof. | No bounded PLANTS assessment fixture family was found. | `PLACE` under established source contract/schema/fixture/validator roots. |

## Selected increment

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Compare successive taxa inventories. | Synthetic prior/current refs and digests plus canonical added/removed sets and rename/recode candidates. | No live package, taxon name, PLANTS symbol, county, occurrence, or endpoint. |
| Separate taxonomy drift from package drift. | Same-version comparison passes; version mismatch abstains and binds an existing lineage profile by ref. | No accepted-name, synonym, merge, split, or taxonomy decision. |
| Exercise changed and unchanged fixtures. | A coherent delta emits a synthetic `WORK_CANDIDATE`; identical taxa state emits `NO_WORK_RECORD`. | Neither result is a SourceIntakeRecord or lifecycle transition. |
| Exercise sensitive and non-sensitive fixtures. | Non-sensitive output is counts-only; a present conservation intersection is withheld and requires synthetic policy/review refs; unknown intersection abstains while withheld. | No conservation member, location, join product, geoprivacy transform, or public detail. |
| Deny missing attestation and unsafe joins. | Two snapshot attestations and one taxonomy-version attestation are required; occurrence joins and exact locations are denied. | Refs are not resolved and no attestation truth is inferred. |

## Directory Rules basis

| Artifact | Owning root and scope | Outcome |
|---|---|---|
| Source-drift assessment meaning | `contracts/source/` owns the inactive semantic contract. | `PLACE` |
| Machine shape | `schemas/contracts/v1/source/` owns the closed Draft 2020-12 shape. | `PLACE` |
| Synthetic replay | `fixtures/contracts/v1/source/` owns public-safe invented cases. | `PLACE` |
| Validator and tests | `tools/validators/source/` and `tests/validators/` own executable conformance. | `PLACE` |
| Source lineage and read-only automation | `docs/intake/exploratory/` and `.github/workflows/` retain their existing non-authoritative roles. | `PLACE` |

No watcher executable home, duplicate specification, connector, source registry
entry, data path, policy rule, release lane, application, map, API, UI, AI, or
public path is selected or created.

## Deferred questions

- Which watcher and specification paths become canonical requires a separate path decision or ADR.
- Live USDA PLANTS interface, rights, cadence, source activation, and SourceDescriptor truth require current verification.
- Taxonomy-version and conservation-list authorities, update cadence, and intersection policy require steward decisions.
- Whether a real candidate becomes a SourceIntakeRecord, and which review queue receives it, remain outside this profile.
- Any future occurrence join requires a separate sensitivity gate, transform receipt, review, release, and public-use decision.

## Rollback

Rollback is a focused revert of the additive packet. No source activation,
watcher runtime, taxonomy, conservation, occurrence, sensitivity, lifecycle,
review, release, deployment, publication, or public state requires restoration.
