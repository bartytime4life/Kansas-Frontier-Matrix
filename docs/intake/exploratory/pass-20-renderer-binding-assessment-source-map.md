<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-20-renderer-binding-assessment
title: Pass 20 Renderer Binding Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD - Intake steward · Map steward · UI steward · Evidence steward · Release steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; pass20; exp-015; renderer-binding; maplibre
responsibility: Preserve source and repository lineage for a bounded renderer-to-layer binding assessment without creating a live registry, resolving references, executing renderer registration, or granting evidence, policy, review, release, deployment, publication, or public-use authority.
truth_posture: "CONFIRMED supplied Pass 20 EXP-015 proposal lineage, visually inspected MapLibre operating-manual boundary, current repository contracts and architecture, accepted Directory Rules, and inspected-repository gap; PROPOSED bounded assessment; UNKNOWN accepted binding policy and production registration gate; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/map/renderer_binding_assessment.md
  - ./pass20-expansion-conformance-baseline.md
  - ../../architecture/map-master.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 20 renderer binding assessment source map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` (`sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`) | The MAP category places renderer surfaces behind the trust membrane. `EXP-015` proposes a MapLibre layer-registry validator and names accepted renderer-binding policy and a production registration gate among its remaining closure criteria. | `CONFIRMED` proposal lineage; not current authority |
| Supplied `KFM_MapLibre_Operating_Architecture_Governed_UI_AI_Interaction_Manual_REVISED.pdf` (`sha256:77f56ec1ab632b76c7728cfb250330271b7dc8948db95c8c0594c92ad9ca6b36`), physical pages 3 and 5-6 | The rendered pages state that MapLibre is downstream of trust, consumes governed/released inputs, supplies interaction context, and must not read RAW/WORK/QUARANTINE or become evidence, policy, review, release, or publication authority. | `CONFIRMED` visually inspected source pressure |
| `docs/intake/exploratory/pass20-expansion-conformance-baseline.md` | The current baseline marks `EXP-015` partial: strict LayerManifest and admission surfaces exist, while a live registry, reference resolution, artifact/signature verification, accepted renderer-binding policy, and production gate remain absent. | `CONFIRMED` point-in-time repository assay |
| `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/ui/renderer_capability_profile.md`, and `contracts/map/renderer_plugin_admission_assessment.md` | Descriptor, manifest, capability, and plugin-admission meanings already have owners. | `REUSE BY OPAQUE REF`; do not create replacement objects |
| `docs/architecture/map-master.md` | The current architecture describes a renderer that consumes released carriers or governed APIs and treats feature interaction as a route to governed evidence resolution. | `CONFIRMED` repository guidance; runtime behavior remains unproved |
| Proposed ADR-0007 | The record proposes MapLibre GL JS as the sole browser renderer, but its effective status remains proposed. | `HOLD`; this packet cannot accept or enforce the ADR |
| `docs/doctrine/directory-rules.md` and accepted ADR-0029 | Contract meaning, schema shape, fixtures, validation, tests, source mapping, and CI remain in their responsibility roots. | `CONFIRMED` accepted placement authority |
| Starting `main@01b3f70bb0514c0557e777294b36992317e992c8` plus repository, history, branch, and pull-request searches | No exact renderer-binding assessment contract, schema, fixture family, validator, workflow, branch, or open pull request was found. | `CONFIRMED` bounded implementation gap |

The supplied sources establish implementation pressure. Current repository
objects and accepted Directory Rules control adaptation.

## Collision decision

| Source pressure | Existing owner | Decision |
|---|---|---|
| Define layers, manifests, styles, artifacts, renderer capability, or plugin evidence. | Existing data, UI, release, and map contracts. | `REFERENCE`; never embed replacement authority objects. |
| Create a live layer registry or MapLibre registration gate. | Runtime/control-plane and accepted policy decisions remain unresolved. | `HOLD`; no registry, route, adapter, or registration call is created. |
| Resolve evidence, policy, review, release, artifact, signature, or rollback refs. | Their existing object families and future resolvers. | `HOLD`; refs remain opaque. |
| Prove one declared relationship keeps the renderer downstream of trust. | No exact bounded executable assessment was found. | `PLACE` one inactive contract/schema/fixture/validator packet. |

## Selected increment

| Concern | Bounded adaptation | Held boundary |
|---|---|---|
| Renderer declaration | Family, runtime surface, adapter, capability, and inactive state. | No renderer is selected, installed, admitted, or executed. |
| Layer composition | Opaque descriptor, manifest, style, and artifact refs. | No existing semantic owner is duplicated or resolved. |
| Delivery membrane | Only governed API or released-carrier input classes can be locally coherent. | No endpoint is contacted and no store is read. |
| Trust closure | Evidence, policy, review, promotion, release, rollback, rights, and sensitivity declarations remain distinct. | The validator cannot determine their truth or approval. |
| Interaction boundary | Feature interaction routes to governed evidence context. | Feature properties and client-side filtering never become authority. |
| Human review | A coherent declaration returns `REVIEW_REQUIRED`. | No binding, policy, release, or registration approval is granted. |

## Directory Rules path decision

| Artifact | Responsibility signature | Outcome |
|---|---|---|
| Assessment meaning | Map renderer relationship contract, no runtime instance, internal, versioned; `contracts/map/`. | `PLACE` |
| Machine shape | Closed Draft 2020-12 schema; `schemas/contracts/v1/map/`. | `PLACE` |
| Synthetic cases | Public-safe test inputs; `fixtures/contracts/v1/map/`. | `PLACE` |
| Validator and tests | Repository validator and executable conformance; `tools/validators/map/` and `tests/validators/map/`. | `PLACE` |
| Source lineage and orchestration | Human exploratory mapping and platform read-only CI; `docs/intake/exploratory/` and `.github/workflows/`. | `PLACE` |

No new root, layer registry, renderer registry, adapter package, policy bundle,
release lane, runtime route, published carrier, or public path is created.

## Deferred questions

- Which renderer-binding policy is accepted, and which steward owns it?
- Which component resolves and authenticates descriptor, manifest, evidence,
  policy, review, promotion, release, correction, and rollback refs?
- Which artifact and signature checks are mandatory before registration?
- Which accepted decision resolves the current MapLibre package-home and
  renderer-policy seams?
- What production gate may call renderer registration APIs, and how is its
  rollback and cache invalidation recorded?

## Rollback

Rollback is a focused revert of the additive packet. No renderer, registry,
layer, data, policy, release, deployment, publication, or public state requires
restoration.
