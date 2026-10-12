<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-aggregate-boundary-assessment
title: Pass 18 Aggregate Boundary Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Governance steward · Domain steward · Contract steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; governance; aggregate-boundary; domain-driven-design
responsibility: Preserve source and repository lineage for a bounded aggregate-boundary assessment without creating objects, executing persistence or transactions, changing schemas or registers, or granting evidence or lifecycle authority.
truth_posture: "CONFIRMED attached-card transcription, attached DDD reference, visual review, Drive corroboration, and inspected-repository comparison; PROPOSED bounded KFM adaptation; UNKNOWN family adoption and reviewer ownership; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/governance/aggregate_boundary_assessment.md
  - ../../../contracts/governance/object_identity_kind_assessment.md
  - ../../../control_plane/object_family_register.yaml
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Aggregate Boundary Assessment Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF pages 287-288 / printed pages 284-285 | Card `KFM-P18-INV-465` proposes aggregate roots carrying invariants, validation scope, and external-reference rules; names bounded context, root, repository/query surface, and fixtures as dependencies; and leaves cross-domain EvidenceBundle treatment open. Both pages were rendered and visually inspected. | `CONFIRMED` |
| Supplied `Domain-Driven Design Reference.pdf`, SHA-256 `4406daa99ff0e3d58757d62d40358c9fd745f95137e99f14602659d0c3f54e55`, physical PDF pages 23-25 / printed pages 16-18 | The reference describes one root per aggregate, root-only external references, synchronous consistency inside a boundary, asynchronous updates across boundaries, root-oriented repositories, and whole-aggregate factories that enforce invariants. All three pages were rendered and visually inspected. | `CONFIRMED` source corroboration |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The proposal corpus treats bounded contexts, object-family semantics, EvidenceBundles, and lifecycle gates as separable concerns; its placeholder ordinals are not implementation IDs. | `CONFIRMED` thematic corroboration |
| `contracts/governance/object_identity_kind_assessment.md` | The existing inactive candidate can declare an object family as an entity, value object, derived artifact, or unresolved. This packet composes that decision by opaque ref and requires an entity root; it does not repeat identity classification. | `CONFIRMED` adjacent responsibility |
| `control_plane/object_family_register.yaml` and `contracts/governance/object_family_domain_reference_profile.md` | The machine register is a partial navigational projection; the domain-reference profile covers ownership/citation/sensitivity declarations. Neither declares aggregate membership, roots, invariants, reference edges, repository/factory scope, or consistency boundaries. | `CONFIRMED` adjacent, non-duplicate responsibility |
| Starting `main@c4cb046829f72afd07e39d167c781fb7435a9ac4` plus repository, code, branch, and PR searches | No exact card ID, aggregate-boundary assessment contract, schema, fixture family, validator, workflow, matching branch, or matching PR was found before implementation. | `CONFIRMED` inspected snapshot |

The attached sources provide design evidence, not repository instruction
authority. In particular, the DDD reference is not treated as a universal KFM
migration mandate.

## Selected increment

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Make a root responsible for one aggregate's invariants. | Exactly one entity root, explicit members, and canonical invariant refs with declared coverage. | No object construction, invariant execution, family adoption, or migration. |
| Keep external references at the root. | External edges may target the root only; single-operation internal edges stay inside the member set. | No reference resolution, graph traversal, query execution, or relationship mutation. |
| Use boundaries for consistency. | Declare aggregate transaction scope, synchronous internal rules, and asynchronous or explicit cross-boundary process. | No transaction manager, persistence behavior, distribution claim, or runtime enforcement. |
| Encapsulate aggregate access and creation. | Optional repository and factory profiles are checked for whole-aggregate scope; `NOT_REQUIRED` is valid and `UNRESOLVED` abstains. | No repository/factory implementation or database access. |
| Preserve KFM evidence boundaries. | EvidenceBundle refs remain reference-only and outside aggregate consistency ownership. | This is a `PROPOSED` KFM choice; no evidence is resolved or admitted. |

## Directory Rules basis

| Artifact | Owning root and scope | Outcome |
|---|---|---|
| Semantic boundary meaning | `contracts/governance/` owns cross-family governance contracts. | `PLACE` |
| Machine shape | `schemas/contracts/v1/governance/` owns the closed Draft 2020-12 shape. | `PLACE` |
| Synthetic replay | `fixtures/contracts/v1/governance/` owns public-safe cases. | `PLACE` |
| Validator and tests | `tools/validators/governance/` and `tests/validators/governance/` own executable conformance. | `PLACE` |
| Source lineage and read-only automation | `docs/intake/exploratory/` and `.github/workflows/` retain their existing non-authoritative roles. | `PLACE` |

No new root, bounded-context register, aggregate register, object-family entry,
policy source, persistence layer, transaction service, evidence store, release
lane, or public path is created.

## Deferred questions

- Which high-risk KFM family, if any, should receive the first reviewed aggregate boundary?
- Which steward roles may adopt boundary, root, and invariant declarations?
- How should a later runtime prove that repository, factory, and transaction behavior matches an adopted declaration?
- Whether cross-domain EvidenceBundle refs always remain outside aggregate consistency ownership remains a review question beyond this candidate.

## Rollback

Rollback is a focused revert of the additive packet. No object, schema, register,
repository, factory, persistence, transaction, evidence, review, release,
deployment, publication, or public artifact requires restoration.
