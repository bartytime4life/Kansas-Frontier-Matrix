<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-map-scale-generalization-disclosure
title: Pass 18 Map-Scale Generalization Disclosure Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Data contract steward · Cartography steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; cartography; scale; generalization
responsibility: Preserve source and repository lineage for a bounded map-scale generalization disclosure adaptation without promoting proposal material into evidence, policy, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription, visual review, Drive discovery, and inspected-repository comparison; PROPOSED bounded adaptation; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/data/map_scale_generalization_disclosure.md
  - ../../../contracts/data/layer_manifest.md
  - ../../../contracts/data/cartographic_omission_disclosure.md
  - ../../../schemas/contracts/v1/data/map_scale_generalization_disclosure.schema.json
  - ../../../fixtures/contracts/v1/data/map_scale_generalization_disclosure/cases.json
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Map-Scale Generalization Disclosure Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 53 / printed page 50 | Card `KFM-P18-INV-476` proposes disclosing the map scale or zoom context in which generalization choices are valid so simplified geometry is not treated as equally precise at every context. The page was rendered and visually checked. | `CONFIRMED` |
| Connected Drive `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) | Drive metadata confirms the named Pass 18 dossier is present. Byte identity with the supplied attachment was not asserted. | `CONFIRMED` metadata only |
| Connected Drive `Kansas Frontier Matrix — Connected-Dots Architecture Brief` (`1sdiLNDLFr2cVD3Q8h3ZvHO4D96WLJ6V7vf5neNzEyTM`) | The brief assigns show/hide/generalize declarations to `LayerManifest` while keeping map layers downstream of evidence, policy, review, and release. | `CONFIRMED` thematic corroboration |
| `main@90deefee3c30dd5878e704cdfc621f89f1edf1f0` | Exact repository, PR, branch, and GitHub code searches found adjacent LayerManifest, omission, legend, representation-fitness, and predictive-generalization profiles but no map-scale generalization disclosure contract, schema, fixture family, validator, workflow, branch, or PR. The intervening main change from the original inspection was limited to an unrelated generated receipt. | `CONFIRMED` for the inspected snapshot |

The source artifacts are proposal evidence, not repository instruction authority. Repository placement and scope follow accepted Directory Rules and current responsibility-root evidence.

## Reconciliation and selected increment

The current repository already owns `LayerManifest` meaning, map omission disclosure, legend disclosure, representation fitness, transform receipts, and evidence references. Modifying those consumers or the existing manifest schema would enlarge compatibility and migration risk.

The selected increment is one additive disclosure candidate that composes those families by pinned reference. It records validity context and representation caveats but does not modify a manifest, create a zoom-to-scale crosswalk, inspect geometry, or bind a UI/runtime consumer.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Disclose scale or zoom validity. | Closed `ZOOM_RANGE`, `SCALE_DENOMINATOR_RANGE`, `BOTH`, and unresolved basis vocabulary. | No renderer/device equivalence or scale inference. |
| Identify generalization choices. | Closed method vocabulary plus transform-receipt reference and omitted-detail classes. | No geometry transformation or receipt authentication. |
| Prevent survey-grade over-interpretation. | Bounded `SOURCE_LIMITED`, `DISPLAY_ONLY`, and `UNKNOWN` precision postures with a public caveat. | No positional-accuracy or source-truth claim. |
| Keep trust state visible. | Evidence, purpose, review, and authority declarations remain explicit and separate. | No evidence resolution, policy/review decision, release, or publication. |

## Directory Rules basis

Semantic meaning is placed beside the canonical data-layer manifest contract. Shape, fixtures, validator, tests, workflow, source map, and generated receipt stay in their established responsibility roots. No new root or parallel map, schema, evidence, policy, release, or publication authority is introduced.

## Deferred questions

- Which layer families require zoom ranges, scale denominators, or both?
- Which component may establish device- or renderer-specific scale equivalence?
- Which generalization methods require domain-specific review obligations?
- Whether a later compatible `LayerManifest` version embeds this disclosure or references it remains undecided.

## Validation and rollback

Focused validation covers closed shape, deterministic identity, UTC timestamps, canonical arrays, range/basis coherence, transform-receipt binding, omitted-detail coherence, visible caveats, review references, unresolved abstention, malformed Unicode, and unknown-field rejection.

Rollback is a focused revert of the additive packet. No reprocessing, release withdrawal, correction notice, cache invalidation, UI cleanup, or public-map cleanup is required because the profile has no consumer and changes no layer.
