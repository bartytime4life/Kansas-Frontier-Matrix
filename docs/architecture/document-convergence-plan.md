<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-document-convergence-plan
title: KFM Architecture Documentation Convergence Plan
type: architecture-convergence-plan
version: v0.1
status: draft; repository-grounded; non-authoritative; no-moves
owners:
  - "@bartytime4life — CODEOWNERS review route"
  - "NEEDS VERIFICATION — architecture and documentation stewardship"
created: 2026-08-18
updated: 2026-08-18
policy_label: public
owning_root: docs/
current_path: docs/architecture/document-convergence-plan.md
responsibility: "Record the current docs/architecture topology, overlap clusters, provisional per-file placement outcomes, dependency-ordered convergence waves, validation requirements, and rollback controls without moving, deleting, accepting, publishing, or creating a competing architecture authority."
truth_posture: "CONFIRMED commit-pinned repository topology and accepted Directory Rules decision / PROPOSED file dispositions and target organization / HOLD where content, ownership, consumer, or authority closure is incomplete"
evidence_base: "bartytime4life/Kansas-Frontier-Matrix main@e5a5aa69de564601fe3dd5e8cce2fb7c109e6306; docs/architecture tree 40e936c47126c97e43688bd5c55619f23c0aef96"
related:
  - README.md
  - SYSTEM_MAP.md
  - SKELETON_MAP.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../adr/INDEX.md
  - ../registers/DOCUMENT_REGISTRY.md
  - ../../control_plane/document_registry.yaml
  - ../../tools/validators/docs/document-graph/README.md
  - ../../tools/validators/docs/link-check/README.md
  - ../../tools/validators/docs/meta-block/README.md
  - ../../tools/validators/directory_governance/README.md
tags: [kfm, architecture, documentation, convergence, information-architecture, directory-governance, migration, rollback]
notes:
  - "This first slice creates one planning document only. It moves, renames, deletes, redirects, or canonicalizes no existing architecture page."
  - "Every disposition is provisional until complete content comparison, inbound-link inventory, document-identity review, and applicable owner or ADR review close."
  - "The census covers all 102 Markdown documents under docs/architecture at the pinned evidence base."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Architecture Documentation Convergence Plan

> **Purpose.** Turn the current `docs/architecture/` collection into an inspectable, navigable, non-competing documentation system through small, reversible changes. This page records evidence and a migration sequence; it does not perform or authorize the migrations.

> [!IMPORTANT]
> **Current effect: documentation planning only.** This change creates one non-authoritative plan. No existing file is moved, renamed, deleted, redirected, superseded, accepted, released, deployed, or published.

> [!CAUTION]
> **A provisional disposition is not a canonicality decision.** `PLACE`, `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, and `DENY` below use the finite Directory Rules vocabulary. Any structural action still requires the evidence, review, reference closure, compatibility treatment, validation, and rollback named for that row.

## Status and bounded result

| Field | Result |
|---|---|
| Evidence snapshot | `main@e5a5aa69de564601fe3dd5e8cce2fb7c109e6306` |
| Architecture tree | `40e936c47126c97e43688bd5c55619f23c0aef96` |
| Direct Markdown files | **40** |
| Direct subdirectories | **8** |
| Markdown files inside subdirectories | **62** |
| Total Markdown documents | **102** |
| Accepted placement decision | `ADR-0029` adopts Directory Rules v2; the source file retains its pre-adoption internal status label because exact bytes were adopted |
| Other numbered ADRs | `PROPOSED` at this snapshot |
| Repository mutation in this slice | One new planning page only |
| Release/publication effect | None |

The census is **CONFIRMED** from the commit-pinned Git tree. The proposed organization and dispositions are **PROPOSED**. Runtime behavior, deployment, public operation, and the semantic correctness of every existing page remain outside this first slice.

## Contents

1. [Goal and non-goals](#1-goal-and-non-goals)
2. [Evidence and Directory Rules basis](#2-evidence-and-directory-rules-basis)
3. [Current topology](#3-current-topology)
4. [Decision method](#4-decision-method)
5. [High-priority overlap clusters](#5-high-priority-overlap-clusters)
6. [Complete 102-file disposition ledger](#6-complete-102-file-disposition-ledger)
7. [Proposed target information architecture](#7-proposed-target-information-architecture)
8. [Dependency-ordered implementation waves](#8-dependency-ordered-implementation-waves)
9. [Validation and acceptance](#9-validation-and-acceptance)
10. [Rollback and correction](#10-rollback-and-correction)
11. [Open decisions](#11-open-decisions)

---

## 1. Goal and non-goals

### Goal

Create a documentation system in which:

- the root README accurately represents the real tree;
- every substantial subsystem has one landing page;
- cross-system principles remain at the architecture root;
- subsystem detail stays under the owning subsystem folder;
- domain-specific material remains under `docs/domains/`;
- operational history and procedures do not compete with durable architecture;
- compatibility pages are one-way, read-only, and time-bounded;
- every consequential move preserves identity, links, history, reviewability, and rollback.

### Non-goals

This plan does not:

- accept or amend an ADR;
- select a canonical winner solely because a page is newer, larger, or more polished;
- normalize conflicting promotion-gate, sensitivity, renderer, identity, or source-role vocabularies;
- move domain, security, runbook, report, or archive material before the receiving lane is verified;
- delete lineage merely to make the tree appear clean;
- claim that documentation proves implementation, deployment, release, or publication.

[Back to top](#top)

---

## 2. Evidence and Directory Rules basis

Accepted `ADR-0029` is the controlling placement decision at this snapshot. Directory Rules v2 supplies the operating law:

> A path is an authority claim. Place an artifact by the one responsibility that owns it, then refine by lifecycle, execution role, scope, exposure, mutability, and retention.

For this convergence work:

| Question | Controlling evidence |
|---|---|
| What paths exist? | The pinned Git tree |
| What currently works? | Code, configuration, tests, workflows, emitted artifacts, and runtime evidence—not architecture prose alone |
| Where should a human architecture page live? | Accepted Directory Rules, applicable accepted ADRs, root/lane README contracts, then current repository evidence |
| What does an object mean? | `contracts/` |
| What machine shape is valid? | `schemas/` |
| What is allowed or denied? | `policy/`, review, rights, sensitivity, and release records |
| What is released? | Append-only release/correction/rollback authority, not a document move |
| What should happen when evidence is incomplete? | `HOLD` rather than invented canonicality |

Domain-Driven Design vocabulary is useful supporting language: subsystem folders can act as bounded explanatory contexts, and the architecture root can act as a context map. It does not override KFM placement authority.

### Evidence grades used in this plan

- **CONFIRMED topology** — path and blob are present at the pinned tree.
- **Repository-grounded role** — content or a local landing page was inspected sufficiently to characterize the page's stated role.
- **PROPOSED disposition** — a convergence direction, not yet an executed or accepted migration.
- **HOLD** — complete content, identity, consumer, authority, sensitivity, or destination evidence is not yet closed.

[Back to top](#top)

---

## 3. Current topology

```text
docs/architecture/
├── 40 direct Markdown files
├── cross-domain/                  9 Markdown files
├── governed-ai/                  10 Markdown files
├── governed-api/                  8 Markdown files
├── map-master/                    8 Markdown files
├── publication/                   9 Markdown files
├── settlements-infrastructure/    1 Markdown file
├── story/                         2 Markdown files
└── ui/                           15 Markdown files
```

### Structural observations

1. The root README still describes a much smaller proposal-era directory and labels repository-present folders and files as unverified.
2. Several flat files compete with folder `README.md` landing pages.
3. `TRUST_MEMBRANE.md` and `trust-membrane.md` are a case-insensitive checkout collision.
4. Durable architecture and dated implementation-history notes share the same level.
5. Cross-domain seam pages exist both flat and under `cross-domain/`.
6. The map, UI, Evidence Drawer, Focus Mode, publication, source-role, sensitivity, and identity clusters repeat substantial concepts across several pages.
7. Existing validators provide the machinery needed for link, metadata, document-graph, registry, and topology closure, but validator success cannot choose document authority.

[Back to top](#top)

---

## 4. Decision method

Each document receives exactly one **provisional** finite outcome:

| Outcome | Meaning in this plan |
|---|---|
| `PLACE` | The current path has one clear explanatory responsibility; future edits may still be required. |
| `SPLIT` | The page mixes independently owned responsibilities; future work should create linked artifacts under their owners. |
| `MIGRATE` | A likely active target already exists; movement/consolidation requires no-loss and consumer closure first. |
| `MIRROR` | The current page should be a one-way compatibility pointer to a verified canonical source. |
| `HOLD` | Evidence is insufficient to move, merge, split, or retire safely. |
| `DENY` | A proposed path or relationship would violate an invariant. No current row is assigned `DENY`; future reviews may produce it. |

### Required preconditions for any later structural change

1. Freeze the base commit and applicable authority inputs.
2. Read the complete source and proposed target.
3. Inventory inbound links, fragments, generators, workflows, docs indexes, and external compatibility needs.
4. Reconcile `doc_id`, title, status, supersession, and history.
5. Preserve every unique governance-significant statement or record why it is rejected.
6. Repair references in the same bounded change.
7. Run changed-area documentation and topology validation.
8. Record rollback and exit criteria.
9. Do not use a newly drafted governance change to authorize its own dependent migration.

[Back to top](#top)

---

## 5. High-priority overlap clusters

| Priority | Cluster | Current risk | Provisional direction |
|---:|---|---|---|
| P0 | `TRUST_MEMBRANE.md` vs `trust-membrane.md` | Case-insensitive checkout collision and competing explanations | Atomic no-loss convergence to one lowercase path; no parallel tombstone pair |
| P0 | Root README | Current map materially understates the repository-present tree | Modernize in place after this ledger is reviewed |
| P1 | `SYSTEM_MAP.md` vs `SKELETON_MAP.md` | Competing whole-system orientation and possible writer dependencies | Keep `SYSTEM_MAP.md` as primary candidate; decide whether Skeleton Map becomes generated summary or compatibility page |
| P1 | Flat/folder Governed AI | Two landing-page candidates | Converge on `governed-ai/README.md` after no-loss comparison |
| P1 | Flat/folder Governed API | Two landing-page candidates | Converge on `governed-api/README.md` after no-loss comparison |
| P1 | Map/MapLibre cluster | Five flat entry points plus `map-master/` and UI overlap | One map landing page; split renderer, artifacts, and shell responsibilities |
| P1 | Evidence Drawer | Root, UI, and map-master pages repeat doctrine and payload behavior | Root concept anchor; subordinate UI and map pages own only local behavior |
| P1 | Publication/release | Flat release model/discipline plus nine-file publication lane | Converge under `publication/`; keep gate-vocabulary conflicts explicit |
| P1 | Evidence identity/hash | New repository-grounded evidence page and older hash doctrine page | Keep `evidence-identity.md`; route normative hash material to its authority owner |
| P2 | Source role | Taxonomy, universal rule, and cross-domain duplicate | One universal rule; taxonomy/catalog moves to source documentation; seam page narrows |
| P2 | Sensitivity/classification/security | Multiple rubrics and authority layers are blended | Split by responsibility; do not choose a vocabulary through documentation cleanup |
| P2 | Dated briefing notes | Implementation history appears beside durable architecture | Preserve in a verified history/report/archive lane |

[Back to top](#top)

---

## 6. Complete 102-file disposition ledger

> [!WARNING]
> The ledger is a review queue, not an automatic migration manifest. `MIGRATE`, `SPLIT`, and `MIRROR` rows remain unexecuted. `HOLD` rows deliberately prevent premature cleanup.

### Top-level files

| Path | Working role | Provisional outcome | Proposed active owner or target | Required closure |
|---|---|---|---|---|
| `docs/architecture/README.md` | Architecture-lane contract and entry point | `PLACE` | same path | Replace proposal-only tree/status with current 102-document map; preserve stable anchors. |
| `docs/architecture/SKELETON_MAP.md` | Whole-system skeleton/orientation | `HOLD` | docs/architecture/SYSTEM_MAP.md or generated summary | Inventory inbound links and any writer workflow; preserve unique topology material before deciding. |
| `docs/architecture/SYSTEM_MAP.md` | Repository-grounded whole-system orientation | `PLACE` | same path | Keep as primary orientation candidate; reverify evidence snapshot before future edits. |
| `docs/architecture/TRUST_MEMBRANE.md` | Repository-grounded trust-membrane architecture | `MIGRATE` | docs/architecture/trust-membrane.md | Case-colliding paths cannot coexist safely; compare complete content and repair all references in one migration. |
| `docs/architecture/briefing-implementation-campaign-20260806.md` | Dated implementation campaign record | `HOLD` | existing reports/archive/history lane — HOLD | Verify the receiving lane contract and inbound links; retain as implementation history. |
| `docs/architecture/briefing-integration.md` | Durable briefing-to-system architecture | `PLACE` | same path | Keep durable architecture separate from dated campaign and repair notes. |
| `docs/architecture/briefing-live-issue-inventory-binding.md` | Dated/current-state implementation repair note | `HOLD` | existing reports/archive/history lane — HOLD | Verify receiving lane and whether later repository state supersedes the note. |
| `docs/architecture/contract-schema-policy-split.md` | Cross-root meaning/shape/admissibility/proof map | `PLACE` | same path | Keep explanatory; normative meaning remains in owning roots and proposed ADRs. |
| `docs/architecture/critical-asset-exposure.md` | Critical-asset exposure architecture and security posture | `SPLIT` | architecture explanation + docs/security owner — HOLD | Classify threat-analysis versus cross-system architecture sections before any move. |
| `docs/architecture/cross-domain-invasives.md` | Invasives cross-domain seam | `HOLD` | docs/architecture/cross-domain/ — exact filename HOLD | Check seam register, target naming, links, and duplicate ecology material. |
| `docs/architecture/cross-lane-join-policy.md` | Cross-lane join architecture/policy explanation | `HOLD` | docs/architecture/cross-domain/ plus policy owner as needed | Determine which prose is architecture and which content claims policy authority. |
| `docs/architecture/data-classification-framework.md` | Cross-root classification and enforcement map | `PLACE` | same path | Retain architecture composition; resolve overlap with docs/security/DATA_CLASSIFICATION.md separately. |
| `docs/architecture/deployment-topology.md` | Deployment/exposure architecture | `PLACE` | same path | Keep current-state and target-state claims separated. |
| `docs/architecture/directory-rules.md` | Legacy architecture copy/redirect for Directory Rules | `MIRROR` | docs/doctrine/directory-rules.md | Keep read-only until inbound links and consumers reach zero; no second writable authority. |
| `docs/architecture/domain-placement-law.md` | Derived domain-placement guidance | `PLACE` | same path | Remain subordinate to accepted ADR-0029 and adopted Directory Rules bytes. |
| `docs/architecture/ecology-cross-domain.md` | Ecology cross-domain seam overview | `HOLD` | docs/architecture/cross-domain/ — exact filename HOLD | Compare with invasives and vegetation-stress seams; preserve unique material. |
| `docs/architecture/evidence-drawer.md` | Cross-root Evidence Drawer concept and authority boundary | `PLACE` | same path | Use as universal concept anchor; narrow subordinate UI/map pages to local responsibilities. |
| `docs/architecture/evidence-identity.md` | Repository-grounded evidence/identity composition | `PLACE` | same path | Keep current resolver boundary and hash-grammar conflict visible. |
| `docs/architecture/governed-ai.md` | Flat governed-AI overview | `MIGRATE` | docs/architecture/governed-ai/README.md | No-loss compare; retain temporary compatibility pointer only after link closure. |
| `docs/architecture/governed-api.md` | Flat Governed API overview | `MIGRATE` | docs/architecture/governed-api/README.md | No-loss compare; retain temporary compatibility pointer only after link closure. |
| `docs/architecture/hazards-trust-membrane.md` | Hazards-specific trust-membrane integration | `HOLD` | domain or cross-domain lane — HOLD | Classify domain doctrine, seam architecture, and generic trust-membrane duplication. |
| `docs/architecture/identity-and-spec-hash.md` | Older identity/hash architecture | `SPLIT` | evidence-identity + standards/contracts/ADR owners | Move normative hash grammar only to its authority owner; preserve unique replay guidance. |
| `docs/architecture/map-master.md` | Flat map architecture anchor | `MIGRATE` | docs/architecture/map-master/README.md | No-loss compare and citation-tag review before a compatibility pointer replaces content. |
| `docs/architecture/map-shell.md` | Map shell and UI interaction architecture | `HOLD` | docs/architecture/ui/ and docs/architecture/map-master/ | Separate shell/state responsibilities from renderer/artifact responsibilities. |
| `docs/architecture/maplibre-master.md` | Flat per-component MapLibre register | `MIGRATE` | docs/architecture/map-master/ | Retain unique component register material; do not duplicate renderer doctrine. |
| `docs/architecture/maplibre.md` | Flat MapLibre lane entry point | `MIGRATE` | docs/architecture/map-master/README.md | One active landing page; preserve useful task routing during convergence. |
| `docs/architecture/people-place-joins.md` | People/place cross-domain seam | `HOLD` | docs/architecture/cross-domain/ — exact filename HOLD | Sensitivity and domain-owner review required before migration. |
| `docs/architecture/planetary-3d.md` | Cross-cutting 3D/representation architecture | `SPLIT` | map-master + applicable domain architecture | Separate renderer/representation concerns from domain-specific model and sensitivity concerns. |
| `docs/architecture/release-discipline.md` | Flat release process architecture | `MIGRATE` | docs/architecture/publication/ | No-loss compare; do not resolve promotion-gate vocabulary without accepted decision. |
| `docs/architecture/release-model.md` | Flat release object-graph architecture | `MIGRATE` | docs/architecture/publication/ | Preserve unique model/reference material and keep contracts/schemas authoritative. |
| `docs/architecture/sensitive-domain-fail-closed.md` | Sensitive-lane fail-closed architecture | `SPLIT` | classification architecture + doctrine/security/policy/domain owners | Do not silently choose among sensitivity vocabularies. |
| `docs/architecture/sensitivity-tiers.md` | T0–T4 tier architecture | `HOLD` | same path pending governance decision | Keep visibly proposed until vocabulary and crosswalk authority are accepted. |
| `docs/architecture/sensitivity.md` | Umbrella sensitivity architecture | `SPLIT` | doctrine + architecture + standards/policy owners | Resolve overlap with docs/doctrine/sensitivity.md before consolidation. |
| `docs/architecture/smoke-atmosphere-hazards.md` | Atmosphere/hazards smoke seam | `HOLD` | docs/architecture/cross-domain/ — exact filename HOLD | Preserve temporal/source-role distinctions and domain links. |
| `docs/architecture/source-role-anti-collapse.md` | Cross-system source-role preservation rule | `PLACE` | same path | Use as active architecture rule page; contracts/schemas/policy remain authoritative. |
| `docs/architecture/source-roles.md` | Taxonomy and per-domain source catalog | `MIGRATE` | docs/sources/ plus links to active anti-collapse page | Verify source-doc lane contract and separate taxonomy from enforcement. |
| `docs/architecture/sovereignty-care.md` | Sovereignty/CARE cross-system architecture | `SPLIT` | architecture + doctrine/policy/domain owners | Qualified stewardship review required; do not reduce restrictions through restructuring. |
| `docs/architecture/spatial-foundation.md` | Cross-system spatial foundation | `PLACE` | same path | Keep representation, geometry, CRS, and temporal-spatial boundaries explanatory. |
| `docs/architecture/system-context.md` | System context and external interfaces | `PLACE` | same path | Keep distinct from detailed SYSTEM_MAP; clarify reading order in root README. |
| `docs/architecture/trust-membrane.md` | Older/lowercase trust-membrane architecture | `HOLD` | same path after atomic merge | Absorb verified unique content from uppercase peer and repair case-sensitive references atomically. |

### cross-domain/

| Path | Working role | Provisional outcome | Proposed active owner or target | Required closure |
|---|---|---|---|---|
| `docs/architecture/cross-domain/README.md` | Cross-domain architecture lane landing | `PLACE` | same path | Update only after seam inventory and migration targets are reviewed. |
| `docs/architecture/cross-domain/compositional-units.md` | Cross-domain compositional-unit guidance | `PLACE` | same path | Keep subordinate to domain placement and shared-kernel boundaries. |
| `docs/architecture/cross-domain/cross-lane-relations.md` | Cross-lane relation architecture | `PLACE` | same path | Reconcile with flat cross-lane-join-policy.md without policy-authority inflation. |
| `docs/architecture/cross-domain/multi-domain-placement.md` | Multi-domain placement guidance | `MIGRATE` | domain-placement-law or focused subordinate page | Compare unique examples and avoid two placement authorities. |
| `docs/architecture/cross-domain/responsibility-layers.md` | Responsibility-layer guidance | `MIGRATE` | domain-placement-law or SYSTEM_MAP | Preserve useful DDD/context material while avoiding duplicated root law. |
| `docs/architecture/cross-domain/shared-kernel.md` | Shared-kernel/context-map architecture | `PLACE` | same path | Keep shared kernel narrow; contracts and schemas own actual shared objects. |
| `docs/architecture/cross-domain/source-role-anti-collapse.md` | Cross-domain duplicate of source-role rule | `MIGRATE` | docs/architecture/source-role-anti-collapse.md | Retain only seam-specific detail here after universal material moves upward. |
| `docs/architecture/cross-domain/trust-membrane.md` | Cross-domain duplicate of trust membrane | `MIGRATE` | docs/architecture/trust-membrane.md | Retain only cross-domain seam obligations if they are unique. |
| `docs/architecture/cross-domain/vegetation-stress.md` | Vegetation-stress seam architecture | `PLACE` | same path | Maintain as bounded seam with explicit source-role and temporal distinctions. |

### governed-ai/

| Path | Working role | Provisional outcome | Proposed active owner or target | Required closure |
|---|---|---|---|---|
| `docs/architecture/governed-ai/ADAPTER_CONTRACT.md` | AI adapter architecture explanation | `PLACE` | same path | Semantic contract authority remains contracts/; page explains composition only. |
| `docs/architecture/governed-ai/AI_RECEIPTS.md` | AI receipt architecture explanation | `PLACE` | same path | Receipt shape/instances remain with contracts, schemas, and receipt data lanes. |
| `docs/architecture/governed-ai/BOUNDARIES.md` | Governed-AI subsystem boundaries | `PLACE` | same path | Keep public/internal/model boundaries explicit. |
| `docs/architecture/governed-ai/CONTINUITY_NOTES.md` | Historical continuity and migration notes | `HOLD` | same path or existing history lane | Verify whether it remains active maintenance guidance or historical record. |
| `docs/architecture/governed-ai/FOCUS_FLOW.md` | Focus Mode governed flow | `PLACE` | same path | Reconcile overlap with ui/FOCUS_FLOW.md by subsystem responsibility. |
| `docs/architecture/governed-ai/MOCK_FIRST.md` | Mock-first implementation architecture | `PLACE` | same path | Keep bounded fixture-first claims visible. |
| `docs/architecture/governed-ai/OLLAMA_INTEGRATION.md` | Ollama adapter/integration architecture | `PLACE` | same path | Remain provider-subordinate and avoid version claims without verification. |
| `docs/architecture/governed-ai/PROMPT_INJECTION.md` | Prompt-injection threat architecture | `PLACE` | same path | Coordinate with security threat modeling without duplicating policy source. |
| `docs/architecture/governed-ai/README.md` | Governed-AI subsystem landing page | `PLACE` | same path | Absorb unique flat overview content after no-loss review. |
| `docs/architecture/governed-ai/ROUTE_MAP.md` | Governed-AI route and interaction map | `HOLD` | same path | Reverify route presence and avoid presenting proposed endpoints as current. |

### governed-api/

| Path | Working role | Provisional outcome | Proposed active owner or target | Required closure |
|---|---|---|---|---|
| `docs/architecture/governed-api/AUDIENCE_CLASSES.md` | Audience-class architecture | `PLACE` | same path | Classification/policy authority remains elsewhere. |
| `docs/architecture/governed-api/DEPLOYMENT_RULES.md` | API deployment-boundary architecture | `PLACE` | same path | Coordinate with deployment-topology and infra; no operational claims without evidence. |
| `docs/architecture/governed-api/ENVELOPES.md` | API envelope architecture | `PLACE` | same path | Contracts/schemas own meaning and shape. |
| `docs/architecture/governed-api/ERROR_CODES.md` | API finite error/reason-code explanation | `PLACE` | same path | Exact machine vocabulary must follow current contract/schema. |
| `docs/architecture/governed-api/LIFECYCLE_GATES.md` | API/lifecycle trust gates | `PLACE` | same path | Do not duplicate publication gate authority. |
| `docs/architecture/governed-api/README.md` | Governed API subsystem landing page | `PLACE` | same path | Absorb unique flat overview content after no-loss review. |
| `docs/architecture/governed-api/THREAT_MODEL.md` | Governed API threat model | `PLACE` | same path | Coordinate with docs/security and avoid exposing restricted details. |
| `docs/architecture/governed-api/archaeology.md` | Archaeology-specific API boundary | `HOLD` | domain architecture or bounded API seam — HOLD | Qualified sensitivity/domain review and consumer inventory required. |

### map-master/

| Path | Working role | Provisional outcome | Proposed active owner or target | Required closure |
|---|---|---|---|---|
| `docs/architecture/map-master/2D_3D_PARITY.md` | 2D/3D parity architecture | `HOLD` | same path | Resolve stale dual-renderer lineage and proposed ADR-0007 before convergence. |
| `docs/architecture/map-master/EVIDENCE_DRAWER.md` | Map-selection-to-drawer behavior | `PLACE` | same path | Remove universal Evidence Drawer doctrine duplication; retain map-specific handoff. |
| `docs/architecture/map-master/LAYER_LIFECYCLE.md` | Map-layer lifecycle architecture | `PLACE` | same path | Lifecycle and release decisions remain with owning roots. |
| `docs/architecture/map-master/PERFORMANCE_BUDGETS.md` | Map performance expectations | `PLACE` | same path | Budgets require current measured evidence before being stated as achieved. |
| `docs/architecture/map-master/README.md` | Map/rendering subsystem landing page | `PLACE` | same path | Absorb unique flat MapLibre/map-master material after no-loss review. |
| `docs/architecture/map-master/RENDERER_BOUNDARY.md` | Renderer negative-authority boundary | `PLACE` | same path | Renderer selection remains proposed until ADR status changes. |
| `docs/architecture/map-master/TILE_ARTIFACTS.md` | Tile-carrier architecture | `PLACE` | same path | Artifact contracts, schemas, release records, and bytes stay in owning roots. |
| `docs/architecture/map-master/VIEWER_VERIFICATION.md` | Viewer verification architecture | `PLACE` | same path | Distinguish static readiness checks from browser/runtime proof. |

### publication/

| Path | Working role | Provisional outcome | Proposed active owner or target | Required closure |
|---|---|---|---|---|
| `docs/architecture/publication/CORRECTION.md` | Deep correction architecture | `MIGRATE` | publication correction family | Compare with rollback-and-correction.md; preserve deep lineage and trust-visible behavior. |
| `docs/architecture/publication/GEO_MANIFEST.md` | Geospatial carrier integrity architecture | `PLACE` | same path | Exact machine shape and release instance stay outside docs. |
| `docs/architecture/publication/README.md` | Publication subsystem landing page | `PLACE` | same path | Own navigation/conflict register, not release authority. |
| `docs/architecture/publication/RELEASE_GATES.md` | Detailed release gate matrix | `MIGRATE` | publication gate family | ADR-0018 remains proposed; do not normalize conflicting vocabularies silently. |
| `docs/architecture/publication/ROLLBACK.md` | Deep rollback architecture | `MIGRATE` | publication rollback family | Compare with rollback-and-correction.md; preserve drill and role detail. |
| `docs/architecture/publication/promotion-gates.md` | Lifecycle-wide promotion gate narrative | `MIGRATE` | publication gate family | Resolve scope and vocabulary through governance before one canonical narrative. |
| `docs/architecture/publication/release-objects.md` | Release object-family architecture | `PLACE` | same path | Contracts/schemas/release records own semantics, shape, and instances. |
| `docs/architecture/publication/release-state-machine.md` | Release-state architecture | `PLACE` | same path | Keep explanatory and distinct from transition implementation. |
| `docs/architecture/publication/rollback-and-correction.md` | Concise rollback/correction overview | `MIGRATE` | publication correction/rollback family | Decide concise-versus-deep reading model after link and content inventory. |

### settlements-infrastructure/

| Path | Working role | Provisional outcome | Proposed active owner or target | Required closure |
|---|---|---|---|---|
| `docs/architecture/settlements-infrastructure/README.md` | Settlements/Infrastructure integration overview | `HOLD` | same path pending relationship decision | Detailed domain authority already exists under docs/domains; preserve until links and unique integration content are classified. |

### story/

| Path | Working role | Provisional outcome | Proposed active owner or target | Required closure |
|---|---|---|---|---|
| `docs/architecture/story/CONTINUITY.md` | Story continuity lineage | `HOLD` | same path or existing history lane | Reverify active maintenance value and inbound links. |
| `docs/architecture/story/README.md` | Story subsystem landing page | `PLACE` | same path | Keep bounded projection proof separate from future playback and release. |

### ui/

| Path | Working role | Provisional outcome | Proposed active owner or target | Required closure |
|---|---|---|---|---|
| `docs/architecture/ui/ACCESSIBILITY.md` | UI accessibility architecture | `PLACE` | same path | Current conformance requires measured evidence; keep targets distinct from achieved state. |
| `docs/architecture/ui/BOUNDARIES.md` | UI subsystem boundaries | `PLACE` | same path | Keep client negative-authority boundaries explicit. |
| `docs/architecture/ui/COMPARE_AND_EXPORT.md` | Compare/export architecture | `PLACE` | same path | Export contracts, policy, and release state remain in owning roots. |
| `docs/architecture/ui/CONTINUITY_NOTES.md` | UI continuity/migration notes | `HOLD` | same path or existing history lane | Classify active guidance versus historical record. |
| `docs/architecture/ui/EVIDENCE_DRAWER.md` | Evidence Drawer UI behavior | `PLACE` | same path | Universal concept stays at root evidence-drawer.md. |
| `docs/architecture/ui/FOCUS_FLOW.md` | Focus interaction UI flow | `SPLIT` | same path + governed-ai/FOCUS_FLOW.md | UI owns interaction; Governed AI owns evidence/model decision flow. |
| `docs/architecture/ui/GOVERNED_SHELL.md` | Governed shell architecture | `PLACE` | same path | Keep current implementation maturity bounded. |
| `docs/architecture/ui/LAYERING.md` | UI layering/state architecture | `PLACE` | same path | Avoid duplicating renderer or lifecycle authority. |
| `docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md` | UI-to-renderer runtime boundary | `PLACE` | same path | Coordinate with map-master/RENDERER_BOUNDARY.md. |
| `docs/architecture/ui/README.md` | UI subsystem landing page | `PLACE` | same path | Maintain one UI navigation authority. |
| `docs/architecture/ui/REVIEW_CONSOLE.md` | Review-console UI architecture | `PLACE` | same path | Review authority remains outside the browser surface. |
| `docs/architecture/ui/STORY_PLAYER.md` | Story Player UI architecture | `SPLIT` | same path + story/README.md | UI owns playback interaction; Story lane owns story projection architecture. |
| `docs/architecture/ui/TELEMETRY.md` | UI telemetry architecture | `PLACE` | same path | Policy/security/retention obligations remain in owning roots. |
| `docs/architecture/ui/TRUST_BADGES.md` | Trust-state presentation architecture | `PLACE` | same path | Badges project evidence; they do not create trust state. |
| `docs/architecture/ui/map-context-evidence-drawer-admission.md` | Bounded implementation/admission note | `HOLD` | existing report/history or UI continuity lane | Determine whether it is durable architecture or implementation-history evidence. |

### Ledger totals

| Outcome | Count |
|---|---:|
| `PLACE` | 55 |
| `SPLIT` | 8 |
| `MIGRATE` | 18 |
| `MIRROR` | 1 |
| `HOLD` | 20 |
| **Total** | **102** |

The totals describe provisional review dispositions only. They do not prove that 55 pages are current, that 18 moves are approved, or that any page may be retired without the required closure.

[Back to top](#top)

---

## 7. Proposed target information architecture

The target below is intentionally conservative. It does not invent new root folders and it preserves existing subsystem lanes.

```text
docs/architecture/
├── README.md
├── SYSTEM_MAP.md
├── system-context.md
├── deployment-topology.md
├── trust-membrane.md
├── contract-schema-policy-split.md
├── domain-placement-law.md
├── spatial-foundation.md
├── data-classification-framework.md
├── evidence-identity.md
├── evidence-drawer.md
├── source-role-anti-collapse.md
├── sensitivity-tiers.md
├── briefing-integration.md
├── document-convergence-plan.md
├── cross-domain/
├── governed-ai/
├── governed-api/
├── map-master/
├── publication/
├── story/
└── ui/
```

### Top-level admission rule

A top-level architecture page should remain only when it:

- explains a concern spanning several responsibility roots;
- is not a domain dossier, runbook, security report, dated implementation note, or component-local README;
- has one clearly bounded explanatory responsibility;
- points to, rather than copies, contracts, schemas, policy, tests, code, and release records;
- has an explicit current/target-state boundary.

### Subsystem landing rule

Each substantial subsystem folder should have one active `README.md` that owns:

- local scope and exclusions;
- current evidence and maturity;
- direct-child map;
- reading order;
- links to contracts, schemas, policy, code, fixtures, tests, workflows, release, correction, and rollback;
- open conflicts and migration state.

A flat compatibility page may temporarily point to that landing page only when a verified consumer requires it and an exit condition is recorded.

[Back to top](#top)

---

## 8. Dependency-ordered implementation waves

### Wave 0 — this change: evidence and review packet

- Add this 102-file census and provisional disposition ledger.
- Move, rename, delete, redirect, or canonicalize nothing.
- Open one draft pull request for review.
- Re-run overlap discovery before any later wave because `main` is active.

### Wave 1 — root navigation and immediate topology hazard

1. Modernize `docs/architecture/README.md` against the reviewed ledger.
2. Inventory every reference to the two trust-membrane case variants.
3. Compare their complete content and metadata.
4. Perform one atomic case-safe migration through a temporary filename.
5. Reconcile any writer or generated-output dependency touching `SKELETON_MAP.md`.
6. Record active, subordinate, compatibility, lineage, and held pages in the root README.

### Wave 2 — subsystem landing convergence

- Governed AI flat/folder convergence.
- Governed API flat/folder convergence.
- Map/MapLibre landing convergence.
- UI versus map responsibility split.
- Story versus UI Story Player split.
- Publication landing and child-document reading model.

Each cluster should be its own small draft PR unless the same links and acceptance boundary make a combined change demonstrably safer.

### Wave 3 — evidence, source role, and classification

- Evidence Drawer three-page responsibility split.
- Evidence identity versus hash/canonicalization split.
- Source-role taxonomy versus anti-collapse split.
- Classification, sensitivity, sovereignty, security, standards, and policy responsibility split.

No vocabulary conflict is resolved by moving files. Applicable accepted ADRs or steward decisions must precede normative convergence.

### Wave 4 — cross-domain and misplaced documents

- Move reviewed seam pages into `cross-domain/`.
- Route domain-specific architecture to `docs/domains/<domain>/`.
- Route operational procedures to `docs/runbooks/`.
- Route threat/security analysis to `docs/security/`.
- Route dated implementation history to an existing verified report/archive/history lane.
- Preserve compatibility only for verified consumers.

### Wave 5 — compatibility retirement

A compatibility path may be removed only after:

- zero writers target it;
- repository-local inbound links and fragments are repaired;
- external or generated consumers are inventoried and handled;
- document identity and supersession are recorded;
- the document graph and registry agree;
- topology debt shrinks rather than gaining a waiver;
- rollback remains a focused revert.

[Back to top](#top)

---

## 9. Validation and acceptance

### Planned repository-native checks

The exact commands must be executed from a checkout of the feature branch and recorded with their real outcomes.

```bash
git diff --check

python tools/validators/docs/document-graph/check_document_graph.py \
  --repo-root . \
  --entrypoint README.md \
  --entrypoint docs/README.md \
  --registry control_plane/document_registry.yaml \
  --git-diff <BASE_SHA>...HEAD \
  --format markdown \
  README.md docs tools/validators/docs

python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --git-diff <BASE_SHA>...HEAD \
  --format json

python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --registry control_plane/document_registry.yaml \
  --git-diff <BASE_SHA>...HEAD \
  --format markdown \
  --output /tmp/docs-meta-block.md \
  --registry-delta-output /tmp/document-registry-delta.json \
  README.md docs tools/validators/docs

python tools/validators/directory_governance/validate_repository_topology.py \
  --format text
```

### Acceptance for this Wave 0 slice

- [x] The evidence base is pinned.
- [x] All 102 Markdown paths are represented exactly once.
- [x] Every row has one provisional finite outcome.
- [x] No existing path is moved, renamed, deleted, or declared released.
- [x] High-risk case collision and landing-page overlaps are explicit.
- [x] Later waves are dependency ordered.
- [x] Rollback is repository-local and focused.
- [ ] Reviewers confirm the census and provisional outcomes.
- [ ] Hosted exact-head checks are inspected and classified.
- [ ] The next wave begins only after refreshing `main` and overlap.

### Acceptance for a later migration wave

A migration is complete only when:

- every affected source has a no-loss disposition;
- unique governance-significant content is preserved or explicitly rejected with reason;
- exactly one active landing page remains for the cluster;
- subordinate pages have narrower, non-competing roles;
- there is no case-insensitive collision;
- local paths and fragments resolve with exact casing;
- changed documents have stable, non-conflicting identities;
- no changed document becomes orphaned or unreachable;
- no new topology waiver or parallel authority is introduced;
- root and subsystem READMEs describe the resulting tree accurately.

[Back to top](#top)

---

## 10. Rollback and correction

### Before merge

Close the draft pull request and delete the feature branch. No existing document or external state needs restoration because this slice only adds the plan.

### After an authorized merge

Revert the single commit that added this page. No source, lifecycle, policy, release, deployment, cache, or public artifact is created.

### During later waves

- Use history-preserving moves where practical.
- Keep reference repair in the same bounded change.
- For case-only renames, use a temporary intermediate path.
- Preserve predecessor `doc_id` and supersession lineage where the document identity changes.
- Do not leave two writable copies.
- If validation or consumer closure fails, revert the migration rather than weakening the gate.

[Back to top](#top)

---

## 11. Open decisions

| ID | Question | Current result |
|---|---|---|
| ARCH-CONV-01 | Which trust-membrane path survives the case collision? | Lowercase target is proposed; complete no-loss comparison and reference inventory remain required. |
| ARCH-CONV-02 | Is `SKELETON_MAP.md` a manual peer, generated summary, or compatibility surface? | `HOLD` pending writer/workflow and consumer closure. |
| ARCH-CONV-03 | May folder READMEs become the sole Governed AI, Governed API, and Map landing pages? | Proposed; requires content and inbound-link closure. |
| ARCH-CONV-04 | Which promotion-gate vocabulary controls publication architecture? | `HOLD`; ADR-0018 remains proposed. |
| ARCH-CONV-05 | Which sensitivity and audience vocabularies are accepted and how are they crosswalked? | `HOLD`; restructuring must preserve conflicts. |
| ARCH-CONV-06 | Where do dated architecture-adjacent implementation notes belong? | Existing receiving lane must be verified before movement. |
| ARCH-CONV-07 | Should the machine document registry become complete for architecture docs? | Proposed review work; current registry authority and completeness must not be inferred. |
| ARCH-CONV-08 | Which specialist steward roles are accountable for each cluster? | `NEEDS VERIFICATION`; CODEOWNERS routing alone is not independent authority. |

---

## Decision

**PROPOSED:** accept this page as the review packet for Wave 0.  
**HOLD:** all moves, splits, migrations, mirrors, and retirements until their row-level closure requirements are met.  
**CONFIRMED:** this plan has no release or publication effect.

[Back to top](#top)
