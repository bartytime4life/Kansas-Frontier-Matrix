<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-responsibility-layer-impact-assessment
title: Pass 18 Responsibility-Layer Impact Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Architecture steward · Governance steward · Contract steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; governance; responsibility-layer; change-impact
responsibility: Preserve source and repository lineage for a bounded responsibility-layer impact assessment without adopting the layer model, changing placement or ownership, deciding policy or review, or granting lifecycle authority.
truth_posture: "CONFIRMED attached-card transcription and visual review, connected Drive corroboration, accepted Directory Rules, existing draft architecture, and inspected-repository comparison; PROPOSED bounded change-impact assessment; UNKNOWN layer-model adoption and steward ownership; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/governance/responsibility_layer_impact_assessment.md
  - ../../architecture/cross-domain/responsibility-layers.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Responsibility-Layer Impact Assessment Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF pages 29-30 / printed pages 26-27 | Card `KFM-P18-INV-396` proposes responsibility layers as large-scale structure, names evidence, policy, catalog, release, API, UI, AI, and operations, and recommends carrying a `responsibility_layer` in change-impact summaries tied to decisions and tests. Both pages were rendered and visually inspected. | `CONFIRMED` |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The private proposal corpus separates evidence, policy, catalog, release, API, UI, AI, and operational concerns while keeping promotion and public-use authority distinct. It is used as thematic corroboration, not repository instruction authority. | `CONFIRMED` thematic corroboration |
| `docs/architecture/cross-domain/responsibility-layers.md`, SHA-256 `cd4b53f18ce82fd8b2eb321303de34947e1d4f3ddbb93ec78fe9ec2fb575aa85` | The repository already names the same eight layers, marks the framing `PROPOSED`, says layers are not folders, and provides a domain-by-layer completeness lens. The naming portion of the source card is therefore already represented. | `CONFIRMED` existing responsibility |
| `docs/doctrine/directory-rules.md`, SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e` | Accepted Directory Rules define responsibility roots and forbid deriving semantic authority from paths. The candidate records owning roots but cannot place files or assign owners. | `CONFIRMED` accepted placement authority |
| Starting `main@bd59127604f3ab7578fe43f30caaeef089c0fffc` plus repository, code, branch, and pull-request searches | No responsibility-layer change-impact contract, schema, fixture family, validator, workflow, matching branch, or open matching pull request was found before implementation. | `CONFIRMED` inspected snapshot |

The attached and Drive sources are evidence inputs, not instructions to adopt a
new architecture or bypass accepted repository governance.

## Collision decision

| Source-card pressure | Existing repository coverage | Decision |
|---|---|---|
| Name the eight responsibility layers in architecture docs. | Already present in the draft cross-domain architecture document. | `REUSE`; do not duplicate or silently canonize. |
| Use the layers when analyzing change impact. | Prose change-impact guidance exists, but no bounded machine-checkable layer assessment was found. | `PLACE` an inactive candidate under established contract/schema/fixture/validator roots. |
| Keep layers tied to decisions and tests rather than bureaucracy. | Existing refs and validation surfaces are distributed by responsibility root. | Require opaque decision, validation, review, and rollback refs; never resolve them or create a new layer hierarchy. |

## Selected increment

| Concern | Bounded adaptation | Held boundary |
|---|---|---|
| Artifact-to-layer declaration | Canonical repository-relative paths declare one existing owning root, one primary layer, and optional related layers. | A declaration cannot place or move a file, create a root, or assign an owner. |
| Complete change-impact view | Impact rows cover every declared layer and distinguish direct from related impact. | No completeness claim beyond the supplied synthetic candidate. |
| Public-surface trust chain | API, UI, or AI impact requires evidence, policy, and release coverage. | No evidence, PolicyDecision, or ReleaseManifest is created or resolved. |
| Cross-layer seams | A connected declared graph exposes review seams; unresolved seams abstain. | Connectivity is structural only and does not prove contract compatibility. |
| Review and rollback | Complete review requires record refs; release requires a rollback ref. | Refs remain opaque; no review or rollback action is executed. |

## Directory Rules basis

| Artifact | Owning root and scope | Outcome |
|---|---|---|
| Cross-family assessment meaning | `contracts/governance/` owns the inactive semantic contract. | `PLACE` |
| Machine shape | `schemas/contracts/v1/governance/` owns the closed Draft 2020-12 shape. | `PLACE` |
| Synthetic replay | `fixtures/contracts/v1/governance/` owns public-safe cases. | `PLACE` |
| Validator and tests | `tools/validators/governance/` and `tests/validators/governance/` own executable conformance. | `PLACE` |
| Source lineage and read-only automation | `docs/intake/exploratory/` and `.github/workflows/` retain their existing non-authoritative roles. | `PLACE` |

No new top-level root, layer directory, ownership registry, policy source,
runtime service, release lane, or public path is created.

## Deferred questions

- Whether the eight-layer framing should become canonical remains the existing ADR question.
- Which steward roles may complete an assessment for a real change remains unknown.
- Which change classes require the profile, and whether it composes with an existing release assessment, require separate review.
- Referenced decision, validation, review, and rollback records need their own authority and existence checks outside this validator.

## Rollback

Rollback is a focused revert of the additive packet. No placement, ownership,
policy, review, data, runtime, release, deployment, publication, or public state
requires restoration.
