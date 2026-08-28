<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-route-chunk-hydration-assessment
title: Pass 18 Route Chunk Hydration Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · UI steward · Contract steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; ui; route-chunk; view-registry
responsibility: Preserve source and repository lineage for a bounded route-chunk hydration preflight without loading code, binding a route, resolving references, or granting activation, release, deployment, or publication authority.
truth_posture: "CONFIRMED attached-card transcription, attached MapLibre atlas, visual review, Drive metadata, and inspected-repository comparison; PROPOSED bounded KFM adaptation; UNKNOWN runtime adoption and reviewer ownership; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/ui/route_chunk_hydration_assessment.md
  - ../../../contracts/ui/view_registry_profile.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Route Chunk Hydration Assessment Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF pages 458-459 / printed pages 455-456 | Card `KFM-P18-INV-329` proposes hydrating route-specific UI chunks only after view-registry, render-hint, evidence, and access state are validated. Both pages were rendered and visually inspected. | `CONFIRMED` |
| Supplied `Master MapLibre Components-Functions-Features.pdf`, SHA-256 `309cf67311059c549e144ae9961b2f49eddf1caab8739a51b47ae88c2f5c1c90`, physical PDF pages 11 and 24 | Rows `ML-064-020` and `ML-064-021` separate the no-direct-store view-registry boundary from lazy route-chunk hydration and call for view-registry and chunk-name validation in CI. The rows cite their own `SRC-064` page lineage. Both pages were rendered and visually inspected. | `CONFIRMED` source corroboration |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The seed corpus treats public UI surfaces as downstream governed carriers; its pass and ordinal placeholders are not implementation identifiers. | `CONFIRMED` thematic corroboration |
| `contracts/ui/view_registry_profile.md` and paired schema/validator | The existing inactive profile owns route-to-contract, catalog, render-hint, policy, Evidence Drawer, and release references. It does not declare or assess route-chunk hydration. | `CONFIRMED` adjacent responsibility |
| `apps/explorer-web/src/adapters/ViewRegistryInspectorProjection.ts` and `apps/explorer-web/src/features/view_registry_inspector/` | A bounded read-only inspector projection exists. It does not expose a route-chunk declaration or lazy-hydration preflight. | `CONFIRMED` adjacent implementation |
| Starting `main@c4cb046829f72afd07e39d167c781fb7435a9ac4` plus repository, code, branch, and PR searches | No exact card ID, route-chunk hydration contract, schema, fixture family, validator, workflow, indexed implementation, matching branch, or matching PR was found before implementation. | `CONFIRMED` inspected snapshot |

The source artifacts are design evidence, not repository instruction authority.
Placement and scope follow accepted Directory Rules and current responsibility
roots.

## Selected increment

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Keep lazy hydration downstream of governance state. | Closed prerequisite states derive `HYDRATE_READY`, `HOLD`, or `REJECT`. | No module loading, route binding, activation, or cache mutation. |
| Validate view registry and chunk names in CI. | Compose `ViewRegistryProfile` by opaque reference and bind chunk ID to chunk name. | No registry lookup, module import, bundle inspection, or runtime assertion. |
| Preserve render, evidence, access, and release roles. | Separate role-specific refs and deny role collapse or direct-store/query markers. | No evidence resolution, policy evaluation, review approval, or release verification. |
| Keep uncertain state visible. | Partial, missing, held, and unknown prerequisites abstain. | No optimistic fallback or early hydration exception. |

## Directory Rules basis

| Artifact | Owning root and scope | Outcome |
|---|---|---|
| Semantic preflight meaning | `contracts/ui/` owns UI contract meaning. | `PLACE` |
| Machine shape | `schemas/contracts/v1/ui/` owns the closed Draft 2020-12 shape. | `PLACE` |
| Synthetic replay | `fixtures/ui/` owns reusable public-safe cases. | `PLACE` |
| Validator and tests | `tools/validators/ui/` and `tests/validators/ui/` own repository tooling and conformance evidence. | `PLACE` |
| Source lineage and read-only automation | `docs/intake/exploratory/` and `.github/workflows/` retain their existing non-authoritative roles. | `PLACE` |

The change adds no canonical, compatibility, conditional, data, release, or
runtime root and creates no parallel view registry.

## Deferred questions

- Which route chunks, if any, may load before Evidence Drawer state exists?
- Which accepted runtime component may consume an adopted hydration preflight?
- Whether module-integrity verification belongs in a later build receipt or release manifest remains undecided.

## Rollback

Rollback is a focused revert of the additive packet. No route, module, registry,
cache, policy decision, release, deployment, publication, or public artifact
requires restoration.
