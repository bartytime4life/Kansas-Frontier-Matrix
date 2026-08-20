<a id="top"></a>

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/maplibre
title: MapLibre in KFM — Architecture Lane Entry Point
type: architecture
subtype: lane-entry-point
version: v2.0-draft
status: draft; repository-grounded; runtime-HOLD; decision-pending; non-release; non-publication
owners:
  - "@bartytime4life — current CODEOWNERS route for docs/architecture/**"
  - "NEEDS VERIFICATION — independent architecture, map-runtime, release, and policy stewards"
created: 2026-05-25
updated: 2026-08-20
policy_label: public; architecture; maplibre; renderer-downstream; cite-or-abstain; no-release-authority
current_path: docs/architecture/maplibre.md
owning_root: docs/
responsibility: "Provide the repository-grounded entry point for MapLibre architecture, implementation evidence, unresolved renderer decisions, validation gates, and direct task navigation without creating runtime, contract, schema, policy, release, or publication authority."
authority_posture: "Explanatory architecture entry point subordinate to accepted ADRs, adopted Directory Rules, semantic contracts, machine schemas, policy, current code/configuration, tests/workflows, receipts/proofs/manifests, release records, and runtime evidence."
truth_posture: "CONFIRMED current repository paths and bounded implementation surfaces at the evidence snapshot / PROPOSED architecture decisions and future runtime integration / UNKNOWN production behavior, deployment, public reliance, and independent stewardship / NEEDS VERIFICATION hosted exact-head checks and any later dependency admission"
evidence_snapshot: "repository=bartytime4life/Kansas-Frontier-Matrix; base_ref=main; base_commit=5451e5bc1ae7ffd8d721197b930cadd827fbbd7f; target_prior_blob=ff4b4754e5dc7beae22620ee669d3fdc240c44d7; directory_rules_blob=fd49a0b83e55cef52c1124281f093e263526898d; directory_rules_decision=ADR-0029 accepted"
related:
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/architecture/map-master/README.md
  - docs/architecture/maplibre-master.md
  - docs/architecture/map-shell.md
  - docs/architecture/planetary-3d.md
  - docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - docs/architecture/map-master/RENDERER_BOUNDARY.md
  - docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
tags: [kfm, architecture, maplibre, map-master, explorer-web, renderer-boundary, evidence-drawer, pmtiles, validation]
notes:
  - "This revision preserves the document identity and stable legacy anchors while replacing proposal-era repository assumptions with current pinned evidence."
  - "The accepted Directory Rules bytes are the v2.0.0-draft.1 text adopted by ADR-0029; the word draft in that source version does not make the accepted decision provisional."
  - "ADR-0006 and ADR-0007 remain proposed. This file does not accept them, retire another renderer, admit maplibre-gl, or authorize release or publication."
  - "The verified current package is packages/maplibre/. The proposal-era paths docs/architecture/maplibre-3d.md and packages/maplibre-runtime/ were not present at the evidence snapshot and are not cited as current authorities."
[/KFM_META_BLOCK_V2] -->

# MapLibre in KFM — Architecture Lane Entry Point

> **Purpose.** Start here for KFM's MapLibre architecture lane: what is implemented, what remains proposed, which trust boundaries apply, where current files live, and what evidence is required before a concrete browser renderer can graduate from `HOLD`.

| Field | Current status |
|---|---|
| **Document state** | `draft · repository-grounded · explanatory` |
| **Placement** | `CONFIRMED PLACE` — same-path architecture documentation under the adopted `docs/` responsibility root |
| **Current package state** | `CONFIRMED scaffold` — `@kfm/maplibre` exists without a `maplibre-gl` dependency |
| **Concrete browser runtime** | `HOLD` — no admitted MapLibre GL JS runtime is proven in Explorer Web |
| **Renderer decision** | `PROPOSED` — ADR-0006 and ADR-0007 are not accepted decisions |
| **Publication state** | `NONE` — this document, branch, commit, or pull request is not a release or publication event |
| **Review route** | `CONFIRMED` CODEOWNERS route to `@bartytime4life`; independent steward roles remain `NEEDS VERIFICATION` |
| **Evidence read** | Repository `main` at `5451e5bc1ae7ffd8d721197b930cadd827fbbd7f` |

> [!IMPORTANT]
> **The renderer is downstream of trust.** MapLibre may render and interact with public-safe released artifacts, but it cannot become the source registry, canonical evidence store, policy engine, citation authority, review authority, promotion authority, release authority, or AI authority.

> [!CAUTION]
> The repository contains a real Explorer Web shell, renderer-neutral map-runtime helpers, fixture-driven admission and cache planning, a MapLibre readiness validator, focused tests, and a placeholder package seam. It does **not** currently prove a concrete MapLibre GL JS runtime, a completed v6 probe record, release-backed map sources, production operation, deployment, or public reliance.

## Quick jump

- [1. What MapLibre is in KFM](#1-what-maplibre-is-in-kfm)
- [2. The architecture lane — where to look for what](#2-the-architecture-lane--where-to-look-for-what)
- [3. The five non-negotiables](#3-the-five-non-negotiables)
- [4. Capability surface, in one screen](#4-capability-surface-in-one-screen)
- [5. Renderer disposition](#5-renderer-disposition)
- [6. Repo placement at a glance](#6-repo-placement-at-a-glance)
- [7. Quick start by task](#7-quick-start-by-task)
- [8. Required objects — short reminder](#8-required-objects--short-reminder)
- [9. Open questions](#9-open-questions)
- [10. Related docs](#10-related-docs)
- [11. Validation and graduation gate](#11-validation-and-graduation-gate)
- [12. Change boundary and rollback](#12-change-boundary-and-rollback)
- [13. Modernization ledger](#13-modernization-ledger)

---

<a id="1-what-maplibre-is-in-kfm"></a>

## 1. What MapLibre is in KFM

KFM's architectural direction treats MapLibre as a **browser-side rendering and interaction runtime inside a governed shell**. The current repository proves only part of that direction.

| Architectural responsibility | Current evidence | Status |
|---|---|---|
| Render released vector, raster, terrain, or other public-safe artifacts | Architecture documents and bounded helper surfaces describe this responsibility; no admitted concrete runtime is present | `PROPOSED implementation` |
| Maintain camera, viewport, layer interaction, and clicked-feature candidate state | Explorer Web contains a renderer-neutral map stage and fixture-driven selection flow | `CONFIRMED bounded implementation` |
| Route a selected candidate toward governed evidence resolution | The map-runtime flow accepts an injected resolver and preserves finite negative outcomes | `CONFIRMED bounded implementation` |
| Import and own MapLibre GL JS through one adapter seam | `MapLibreAdapter.ts` and `packages/maplibre/` exist as placeholders; ADR-0006 proposes the seam | `PROPOSED decision · scaffold present` |
| Decide whether a claim, source, layer, or geometry may be exposed | No renderer surface is authorized to make that decision | `DENY` |
| Promote, release, publish, or correct canonical truth | No renderer surface is authorized to perform those transitions | `DENY` |

### MapLibre may carry evidence; it does not create authority

| MapLibre may do | MapLibre must not do |
|---|---|
| Render an already governed and public-safe representation | Read RAW, WORK, QUARANTINE, or canonical internal stores as the normal public path |
| Emit camera, time, selection, and representation context | Treat a click, pixel, popup, screenshot, tile, or style as proof |
| Surface `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states supplied through governed interfaces | Convert missing evidence, policy failure, or runtime error into a permissive fallback |
| Display evidence, freshness, review, release, correction, and rollback cues | Hide sensitivity through style-only filtering or client-only opacity changes |
| Support deterministic, testable adapter behavior after dependency admission | Infer architecture acceptance from a package name, absent competitor, green badge, or prose claim |

### Current repository boundary

`CONFIRMED` from the pinned repository snapshot:

- [`packages/maplibre/package.json`](../../packages/maplibre/package.json) defines the private `@kfm/maplibre` package at version `0.0.0` but does not declare `maplibre-gl`.
- [`packages/maplibre/src/index.ts`](../../packages/maplibre/src/index.ts) is a placeholder export, not a renderer implementation.
- [`apps/explorer-web/package.json`](../../apps/explorer-web/package.json) defines the current Explorer Web application but does not declare `maplibre-gl`.
- [`MapLibreAdapter.ts`](../../apps/explorer-web/src/adapters/MapLibreAdapter.ts) contains only a placeholder comment.
- [`map_runtime/index.tsx`](../../apps/explorer-web/src/features/map_runtime/index.tsx) provides a renderer-neutral, fixture-driven selection profile with an injected resolver.
- [`layer_manifest_admission.ts`](../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts) evaluates bounded admission inputs but does not mutate a registry or call `addSource`.
- [`pmtiles_release_cache.ts`](../../apps/explorer-web/src/features/map_runtime/pmtiles_release_cache.ts) plans release-scoped cache behavior but performs no fetch or cache operation.

That is meaningful implementation surface, but it is not a concrete MapLibre runtime and it is not publication evidence.

[Back to top](#top)

---

<a id="2-the-architecture-lane--where-to-look-for-what"></a>

## 2. The architecture lane — where to look for what

```mermaid
flowchart TD
    Entry["maplibre.md\nthis entry point"]
    Rules["Directory Rules\nadopted by ADR-0029"]
    Master["map-master/README.md\ncurrent lane index"]
    Register["maplibre-master.md\ncomponent/function/feature register"]
    Shell["map-shell.md\nExplorer shell and evidence flow"]
    Planetary["planetary-3d.md\nconditional 3D boundary"]
    Boundary["map-master/RENDERER_BOUNDARY.md\nrenderer trust boundary"]
    ADR6["ADR-0006\nproposed import seam"]
    ADR7["ADR-0007\nproposed sole-renderer decision"]
    Code["packages/maplibre + Explorer Web\ncurrent bounded implementation"]
    Ready["validate_v6_readiness.py\nreadiness gate"]

    Rules --> Entry
    Entry --> Master
    Entry --> Register
    Entry --> Shell
    Entry --> Planetary
    Master --> Boundary
    Boundary --> ADR6
    Boundary --> ADR7
    Entry --> Code
    Code --> Ready
```

| Surface | Current role | Authority or maturity |
|---|---|---|
| [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) | Writable human placement authority | `CONFIRMED adopted` through [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| [`map-master/README.md`](./map-master/README.md) | Current Map Master lane index and direct-child navigation | `CONFIRMED repository-grounded draft` |
| [`maplibre-master.md`](./maplibre-master.md) | Repository-grounded MapLibre component/function/feature register | `CONFIRMED file · draft authority` |
| [`map-shell.md`](./map-shell.md) | Current Explorer shell, map-selection, Evidence Drawer, and finite-state boundary | `CONFIRMED bounded implementation evidence` |
| [`planetary-3d.md`](./planetary-3d.md) | Conditional 3D, terrain, globe, scene, and reality-boundary guidance | `CONFIRMED current doc · mixed maturity` |
| [`map-master/RENDERER_BOUNDARY.md`](./map-master/RENDERER_BOUNDARY.md) | Renderer trust membrane and implementation boundary | `CONFIRMED current doc` |
| [ADR-0006](../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) | Proposed single-import seam | `PROPOSED decision` |
| [ADR-0007](../adr/ADR-0007%20%E2%80%94%20MapLibre%20GL%20JS%20Is%20the%20Sole%20Browser-Side%20Renderer.md) | Proposed sole browser-renderer disposition | `PROPOSED decision` |
| [`map-master.md`](./map-master.md) | Proposal-era lineage and abstract architecture material | `RETAINED lineage`; use `map-master/README.md` for the current lane index |

> [!NOTE]
> The proposal-era paths `docs/architecture/maplibre-3d.md` and `packages/maplibre-runtime/` were not present at the evidence snapshot. Do not use them as current implementation or navigation authorities. Current 3D guidance is in [`planetary-3d.md`](./planetary-3d.md), and the verified package seam is [`packages/maplibre/`](../../packages/maplibre/).

### Map Master direct-child navigation

The current lane index routes detailed responsibilities to:

- [2D / 3D parity](./map-master/2D_3D_PARITY.md)
- [Evidence Drawer](./map-master/EVIDENCE_DRAWER.md)
- [Layer lifecycle](./map-master/LAYER_LIFECYCLE.md)
- [Performance budgets](./map-master/PERFORMANCE_BUDGETS.md)
- [Renderer boundary](./map-master/RENDERER_BOUNDARY.md)
- [Tile artifacts](./map-master/TILE_ARTIFACTS.md)
- [Viewer verification](./map-master/VIEWER_VERIFICATION.md)

[Back to top](#top)

---

<a id="3-the-five-non-negotiables"></a>

## 3. The five non-negotiables

These rules apply whether the runtime remains synthetic, adopts MapLibre later, or changes implementation detail through an accepted ADR.

| # | Rule | Required consequence |
|---|---|---|
| **N-1** | **The renderer is downstream of trust.** | Renderer code may consume governed decisions and released artifacts; it cannot become truth, policy, evidence, review, release, or AI authority. |
| **N-2** | **Public rendering requires governed inputs.** | A layer, style, tile archive, terrain source, scene, or plugin reference needs the appropriate identity, provenance, policy, review, release, correction, and rollback support before public exposure. Fixture eligibility is not release. |
| **N-3** | **Selection narrows scope; it does not prove a claim.** | A click or spatial query produces a candidate context. Consequential answers require `EvidenceRef` resolution to an admissible `EvidenceBundle`, or a finite `ABSTAIN`, `DENY`, or `ERROR` outcome. |
| **N-4** | **Styling is not policy.** | Sensitive geometry must be omitted, generalized, aggregated, delayed, or denied upstream with an auditable transform. Client styling cannot be the only protection. |
| **N-5** | **Decision state must stay visible.** | Proposed ADRs remain proposed; a readiness `READY` result means only eligibility for a later governed decision; a branch, PR, test, package scaffold, absent competitor, or documentation statement does not admit, release, deploy, publish, or retire architecture. |

> [!IMPORTANT]
> A concrete MapLibre integration that cannot preserve all five rules must remain `HOLD` or be narrowed. The correct response to unresolved evidence, rights, sensitivity, review, release, or runtime state is never a persuasive renderer fallback.

[Back to top](#top)

---

<a id="4-capability-surface-in-one-screen"></a>

## 4. Capability surface, in one screen

This table reports **current repository maturity**, not the broader capabilities of the upstream MapLibre ecosystem.

| Capability or surface | Verified current evidence | Current posture |
|---|---|---|
| MapLibre package seam | `packages/maplibre/package.json` and one placeholder export | `SCAFFOLD` |
| Explorer Web application | Vite/TypeScript/Vitest/Playwright application exists; no `maplibre-gl` dependency | `IMPLEMENTED SHELL · RENDERER-NEUTRAL` |
| MapLibre adapter | Placeholder file exists | `SCAFFOLD` |
| Map selection and evidence-resolution bridge | Fixture-driven profile with injected resolver and finite outcomes | `IMPLEMENTED BOUNDED SLICE` |
| Layer-manifest admission evaluation | Deterministic fixture-only evaluator; no registry mutation or source creation | `IMPLEMENTED BOUNDED SLICE` |
| PMTiles release-cache planning | Deterministic fixture-only planner; no fetch or cache side effects | `IMPLEMENTED BOUNDED SLICE` |
| Readiness validator | Exact candidate `6.4.0`, import-boundary checks, TypeScript/module checks, and twelve named runtime probes | `IMPLEMENTED VALIDATOR` |
| Readiness tests | Synthetic positive and exact-negative unit coverage | `IMPLEMENTED TESTS` |
| Committed v6 probe result | `configs/maplibre/v6-probe-results.json` not present at the evidence snapshot | `HOLD` |
| Admitted MapLibre GL JS dependency | No current inspected manifest declares it | `HOLD` |
| Standalone performance harness | `scripts/maplibre-smoke-perf.mjs` exists and independently acquires MapLibre `5.5.0` from a public CDN | `DRIFT / NON-HERMETIC · NOT ADMISSION` |
| MapLibre configuration lane | README plus a performance-envelope payload; not a live viewer config or source registry | `BOUNDED CONFIG SUPPORT` |
| Production 2D / terrain / globe / 3D runtime | No current code, runtime trace, release manifest, deployment record, or hosted result inspected proves it | `UNKNOWN / NOT PROVEN` |

### Why the readiness posture is `HOLD`

Static repository evidence is enough to show that the validator exists and what it requires. It is also enough to show that the current inspected manifests do not pin `maplibre-gl` and that the required v6 probe result is absent. The validator's own contract therefore prevents a false `READY` claim.

A later `READY` result would still mean only that the pinned candidate satisfies the repository-owned readiness profile. It would **not** accept ADR-0006 or ADR-0007, authorize dependency admission, change public behavior, approve a release, or publish a viewer.

[Back to top](#top)

---

<a id="5-renderer-disposition"></a>

## 5. Renderer disposition

The repository currently contains a **MapLibre-oriented architecture direction** and a **proposed sole-renderer decision**, not an accepted renderer admission.

| Question | Current answer | Evidence needed to change it |
|---|---|---|
| Is MapLibre the intended browser-renderer direction? | `CONFIRMED architecture direction` | Existing architecture lane and package naming |
| Is the one-import adapter boundary accepted? | `PROPOSED` | Acceptance or supersession of ADR-0006 plus enforceable implementation |
| Is MapLibre GL JS the accepted sole browser-side renderer? | `PROPOSED` | Acceptance or supersession of ADR-0007 |
| Is Cesium formally retired by an accepted decision? | `NO` | Accepted supersession or retirement decision; absence from manifests is not enough |
| Is `maplibre-gl` admitted and pinned? | `NO` at the evidence snapshot | Exact dependency selection, synchronized lockfile, complete probes, review, and bounded implementation |
| Is there a concrete production renderer? | `NOT PROVEN` | Current code, tests, hosted checks, release state, deployment evidence, and runtime traces |
| Are 3D plugins admitted? | `NO GENERAL ADMISSION` | Per-plugin rights, security, performance, compatibility, evidence-parity, and rollback review |

### Bounded decision posture

Until the renderer ADRs are accepted or superseded:

1. preserve the existing `packages/maplibre/` and `MapLibreAdapter.ts` seams as scaffolds, not proof;
2. keep application code renderer-neutral where the current boundary requires it;
3. do not add a peer renderer or declare one retired by documentation alone;
4. do not allow standalone benchmark tooling to become the production dependency path by accident;
5. treat each terrain, globe, 3D, point-cloud, custom-layer, or protocol integration as a separately governed capability rather than automatic inheritance from the renderer choice.

[Back to top](#top)

---

<a id="6-repo-placement-at-a-glance"></a>

## 6. Repo placement at a glance

### Directory Rules basis

This update stays at `docs/architecture/maplibre.md`. Under the accepted Directory Rules, `docs/` owns human-readable architecture explanation, while executable code, machine schemas, policy, tests, configuration, data, and release records remain in their own responsibility roots. No new path, root, authority surface, or migration is created by this document.

| Verified current path | Owning responsibility | What its presence proves | What it does not prove |
|---|---|---|---|
| [`docs/architecture/maplibre.md`](./maplibre.md) | Human-readable lane entry point | Architecture documentation exists | Accepted renderer decision or runtime |
| [`docs/architecture/map-master/`](./map-master/README.md) | Map Master architecture sublane | Current navigation and bounded doctrine exist | Production viewer or release |
| [`packages/maplibre/`](../../packages/maplibre/) | Reusable package seam | Package scaffold exists | `maplibre-gl` admission or working adapter |
| [`apps/explorer-web/`](../../apps/explorer-web/) | Explorer Web application | Current browser application and bounded shell code exist | Concrete MapLibre runtime or published site |
| [`configs/maplibre/`](../../configs/maplibre/) | Commit-safe configuration support | README and bounded performance input exist | Live style/layer/source registry |
| [`tools/validators/maplibre/`](../../tools/validators/maplibre/) | Repository validation tooling | Readiness logic exists | A passing current repository result unless executed against current bytes |
| [`tests/maplibre/`](../../tests/maplibre/) | Focused test ownership | Synthetic validator tests exist | Browser/runtime parity or hosted success |
| [`scripts/maplibre-smoke-perf.mjs`](../../scripts/maplibre-smoke-perf.mjs) | Standalone script | A performance harness exists | Accepted package seam, hermetic operation, or release eligibility |

### Placement rules for future work

Any later concrete integration must:

- keep semantic meaning, machine shape, admissibility, reusable fixtures, executable tests, and runtime implementation in their respective responsibility roots;
- use the verified current package and application roots unless an accepted ADR and migration say otherwise;
- update direct documentation, tests, configuration, lockfiles, and generated outputs required by the actual change;
- avoid recreating absent proposal-era paths as parallel authorities;
- preserve correction, rollback, and compatibility boundaries for any public or persisted behavior.

The exact future file set is `NEEDS VERIFICATION` until a scoped implementation task inspects current main, accepted ADRs, consumers, and repository-owned validation.

[Back to top](#top)

---

<a id="7-quick-start-by-task"></a>

## 7. Quick start by task

| Task | Start here | Then inspect |
|---|---|---|
| Understand the whole Map Master lane | [Map Master README](./map-master/README.md) | [MapLibre register](./maplibre-master.md) |
| Change or review the renderer trust boundary | [Renderer Boundary](./map-master/RENDERER_BOUNDARY.md) | [UI Map Runtime Boundary](./ui/MAP_RUNTIME_BOUNDARY.md) and [ADR-0006](../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) |
| Review the sole-renderer proposal | [ADR-0007](../adr/ADR-0007%20%E2%80%94%20MapLibre%20GL%20JS%20Is%20the%20Sole%20Browser-Side%20Renderer.md) | [Renderer disposition](#5-renderer-disposition) |
| Work on Explorer shell behavior | [Map Shell](./map-shell.md) | [`map_runtime/index.tsx`](../../apps/explorer-web/src/features/map_runtime/index.tsx) |
| Work on selection and Evidence Drawer behavior | [Evidence Drawer](./map-master/EVIDENCE_DRAWER.md) | [`map_runtime/index.tsx`](../../apps/explorer-web/src/features/map_runtime/index.tsx) |
| Work on layer admission or lifecycle | [Layer Lifecycle](./map-master/LAYER_LIFECYCLE.md) | [`layer_manifest_admission.ts`](../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts) |
| Work on PMTiles or tile release behavior | [Tile Artifacts](./map-master/TILE_ARTIFACTS.md) | [`pmtiles_release_cache.ts`](../../apps/explorer-web/src/features/map_runtime/pmtiles_release_cache.ts) |
| Work on performance | [Performance Budgets](./map-master/PERFORMANCE_BUDGETS.md) | [MapLibre config boundary](../../configs/maplibre/README.md) and the [performance harness](../../scripts/maplibre-smoke-perf.mjs) |
| Work on 2D / 3D evidence parity | [2D / 3D Parity](./map-master/2D_3D_PARITY.md) | [Planetary / 3D](./planetary-3d.md) |
| Verify viewer behavior and negative states | [Viewer Verification](./map-master/VIEWER_VERIFICATION.md) | Current Explorer tests and exact-head hosted checks |
| Evaluate the v6 candidate | [Readiness validator](../../tools/validators/maplibre/validate_v6_readiness.py) | [Focused tests](../../tests/maplibre/test_validate_v6_readiness.py) |
| Change object meaning, shape, or admissibility | [Contract / Schema / Policy / Test Split](./contract-schema-policy-split.md) | Current contracts, schemas, policy, fixtures, validators, and tests for the exact object family |
| Change identity or digest handling | [Identity and `spec_hash`](./identity-and-spec-hash.md) | Current object-family contracts, schemas, validators, and migration evidence |

[Back to top](#top)

---

<a id="8-required-objects--short-reminder"></a>

## 8. Required objects — short reminder

This entry point does not establish canonical object names or machine shapes. It records the minimum **responsibilities** that a concrete renderer flow must be able to carry or resolve.

| Responsibility | Minimum information needed before consequential public use | Failure posture |
|---|---|---|
| Layer or representation identity | Stable identity, version, spatial/temporal scope, source role, and content digest where applicable | `ABSTAIN` or `ERROR` when identity cannot be resolved |
| Evidence support | Resolvable `EvidenceRef` to an admissible `EvidenceBundle` for claims that depend on evidence | `ABSTAIN` when support is absent, stale, conflicted, or out of scope |
| Policy and sensitivity | Applicable access, rights, sensitivity, precision, and transform decision | `DENY` when exposure is unsafe or unresolved |
| Review and release | Review state, release identity, release decision, and public-safe artifact binding | `DENY` or `HOLD` when not released for the requested surface |
| Selection context | Geometry or candidate identity, camera/viewport, time state, layer identity, and requested operation | Narrow the request; never infer proof from a click |
| Representation metadata | Style/layer/source version, renderer capability, degradation state, and any transformation or reality-boundary note | Make uncertainty and synthetic/derived status visible |
| Correction and rollback | Supersession/correction lineage, rollback target, and cache or client invalidation instructions where public reliance exists | `ERROR` rather than silently serving stale or withdrawn state |
| Finite runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` plus stable reason information suitable for the caller | Never convert a negative state into implicit allow |

Before creating or changing a concrete object family, verify its semantic contract, canonical schema, policy, fixture, validator, tests, identity grammar, consumers, and release/correction obligations. The architecture docs do not substitute for those authorities.

[Back to top](#top)

---

<a id="9-open-questions"></a>

## 9. Open questions

| ID | Question | Current status | Evidence or decision needed |
|---|---|---|---|
| `ML-OPEN-01` | Will ADR-0006's one-import seam be accepted, amended, or superseded? | `NEEDS VERIFICATION` | Architecture decision plus enforceable import-boundary tests |
| `ML-OPEN-02` | Will ADR-0007's sole-renderer proposal be accepted, amended, or superseded? | `NEEDS VERIFICATION` | Accepted ADR with explicit consequences and migration/rollback |
| `ML-OPEN-03` | Is `6.4.0` still the candidate when dependency admission is actually attempted? | `NEEDS VERIFICATION` | Current authoritative upstream review plus exact repository compatibility evidence |
| `ML-OPEN-04` | Who owns the package seam, Explorer adapter, performance profile, and release decision independently? | `UNKNOWN` | Accepted stewardship and review routing beyond the current CODEOWNERS fallback |
| `ML-OPEN-05` | How will the standalone `5.5.0` CDN performance harness be reconciled with the package seam and no-network test posture? | `CONFLICTED` | Small dependency-closed design decision, hermetic fixture strategy, and focused validation |
| `ML-OPEN-06` | Which current contracts and schemas canonically carry layer, tile, selection, representation, and release metadata? | `NEEDS VERIFICATION` | Current object-family inventory and accepted contract/schema authority |
| `ML-OPEN-07` | What exact probe artifact and browser matrix are required for candidate readiness? | `PARTIALLY CONFIRMED` | Twelve-probe profile exists; concrete execution environment and committed result remain absent |
| `ML-OPEN-08` | Which terrain, globe, custom-layer, point-cloud, or 3D plugins are admissible? | `UNKNOWN` | Per-capability security, rights, compatibility, performance, accessibility, evidence-parity, and rollback review |
| `ML-OPEN-09` | Which hosted workflows are required for a concrete runtime PR? | `NEEDS VERIFICATION` | Current workflow inventory and exact-head repository policy at implementation time |
| `ML-OPEN-10` | What proves public-safe operation after dependency admission? | `UNKNOWN` | Released fixtures/artifacts, policy outcomes, browser tests, accessibility/performance evidence, correction/rollback rehearsal, and runtime traces |

These questions do not block this documentation correction. They do block any claim that the renderer is admitted, production-ready, released, deployed, or published.

[Back to top](#top)

---

<a id="10-related-docs"></a>

## 10. Related docs

### Governing placement and responsibility boundaries

- [Directory Rules](../doctrine/directory-rules.md)
- [ADR-0029 — adopt Directory Governance Standard v2](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Contract / Schema / Policy / Test Split](./contract-schema-policy-split.md)
- [Identity and `spec_hash`](./identity-and-spec-hash.md)

### Map and UI architecture

- [Map Master lane index](./map-master/README.md)
- [MapLibre component/function/feature register](./maplibre-master.md)
- [Map Shell](./map-shell.md)
- [Planetary / 3D](./planetary-3d.md)
- [UI Map Runtime Boundary](./ui/MAP_RUNTIME_BOUNDARY.md)
- [Renderer Boundary](./map-master/RENDERER_BOUNDARY.md)
- [Layer Lifecycle](./map-master/LAYER_LIFECYCLE.md)
- [Tile Artifacts](./map-master/TILE_ARTIFACTS.md)
- [Evidence Drawer](./map-master/EVIDENCE_DRAWER.md)
- [2D / 3D Parity](./map-master/2D_3D_PARITY.md)
- [Performance Budgets](./map-master/PERFORMANCE_BUDGETS.md)
- [Viewer Verification](./map-master/VIEWER_VERIFICATION.md)

### Decisions and current implementation evidence

- [ADR-0006 — proposed MapLibre import boundary](../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md)
- [ADR-0007 — proposed sole browser-side renderer](../adr/ADR-0007%20%E2%80%94%20MapLibre%20GL%20JS%20Is%20the%20Sole%20Browser-Side%20Renderer.md)
- [`@kfm/maplibre` package manifest](../../packages/maplibre/package.json)
- [Explorer Web manifest](../../apps/explorer-web/package.json)
- [MapLibre adapter placeholder](../../apps/explorer-web/src/adapters/MapLibreAdapter.ts)
- [Renderer-neutral map runtime](../../apps/explorer-web/src/features/map_runtime/index.tsx)
- [Layer-manifest admission evaluator](../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts)
- [PMTiles release-cache planner](../../apps/explorer-web/src/features/map_runtime/pmtiles_release_cache.ts)
- [MapLibre configuration boundary](../../configs/maplibre/README.md)
- [v6 readiness validator](../../tools/validators/maplibre/validate_v6_readiness.py)
- [v6 readiness tests](../../tests/maplibre/test_validate_v6_readiness.py)
- [Standalone performance harness](../../scripts/maplibre-smoke-perf.mjs)

[Back to top](#top)

---

<a id="11-validation-and-graduation-gate"></a>

## 11. Validation and graduation gate

### Documentation changes to this file

A same-path documentation update should prove at least:

1. GFM source is structurally valid enough for repository rendering;
2. explicit legacy anchors remain unique;
3. local Markdown links resolve to current repository paths;
4. no absent proposal-era path is presented as current;
5. current behavior claims are pinned to repository evidence;
6. proposed decisions remain visibly proposed;
7. no runtime, dependency, schema, contract, policy, release, deployment, or publication state changes are implied.

### Concrete runtime changes

The focused repository-owned validator supports three explicit modes:

```bash
python tools/validators/maplibre/validate_v6_readiness.py --scan-root .
python tools/validators/maplibre/validate_v6_readiness.py --manifest configs/maplibre/v6-probe-results.json
python tools/validators/maplibre/validate_v6_readiness.py --fixtures
```

Focused unit coverage lives at:

```bash
python -m unittest tests.maplibre.test_validate_v6_readiness
```

The validator returns:

- exit `0` for `READY`;
- exit `3` for `HOLD`;
- exit `1` for `ERROR`.

> [!IMPORTANT]
> `READY` is an **eligibility result**, not dependency admission, ADR acceptance, release, deployment, or publication. A concrete runtime PR must also close the adapter, application, lockfile, browser-probe, negative-state, accessibility, performance, evidence, policy, release, correction, and rollback dependencies introduced by that change.

### Minimum graduation sequence

```text
scaffold
  -> exact dependency candidate
  -> one enforced import seam
  -> deterministic fixtures and negative cases
  -> complete browser probes
  -> governed layer/evidence/release binding
  -> accessibility and performance evidence
  -> review and accepted decision state
  -> release-eligible artifact set
  -> separate governed release/deployment/publication transitions
```

Skipping a step requires an explicit accepted decision and a documented tradeoff; documentation alone cannot waive the gate.

[Back to top](#top)

---

<a id="12-change-boundary-and-rollback"></a>

## 12. Change boundary and rollback

This document revision:

- updates one existing Markdown file at the same path;
- changes no application or package code;
- adds or updates no dependency or lockfile;
- changes no contract, schema, policy, fixture, validator, test, workflow, configuration, generated output, receipt, proof, manifest, source registry, release record, or runtime state;
- activates no source, network integration, renderer, plugin, release, deployment, promotion, or publication;
- creates no new authority surface.

**Before merge**, rollback is to close or abandon the draft pull request and leave `main` unchanged. **After merge**, rollback is a normal Git revert of the documentation commit. Because this change creates no public runtime behavior or published artifact, no data correction, cache invalidation, or public withdrawal workflow is required for the documentation rollback itself.

A later concrete runtime change needs its own compatibility, correction, rollback, and public-reliance analysis.

[Back to top](#top)

---

<a id="13-modernization-ledger"></a>

## 13. Modernization ledger

The prior edition contained useful architecture intent but mixed it with unverified repository paths, stale governance labels, external capability claims, and proposed decisions presented too strongly. This revision preserves the useful intent while making current evidence and uncertainty inspectable.

| Prior material | Disposition in this edition |
|---|---|
| Renderer-downstream principle | `RETAINED` and strengthened as N-1 |
| Released/public-safe input rule | `RETAINED` and bounded to current implementation evidence |
| Evidence Drawer and Focus Mode routing | `RETAINED` through current Map Master and Map Shell links |
| Sensitive geometry must be transformed upstream | `RETAINED` as N-4 without inventing current policy paths |
| Capability overview | `REPLACED` with a repository-maturity table; upstream ecosystem details remain in deeper docs and require current verification |
| Repository placement table | `CORRECTED` to verified current paths and accepted Directory Rules |
| Quick-start task routing | `EXPANDED` to current Map Master child documents and implementation files |
| Required object reminder | `RETAINED` as responsibility requirements without claiming unverified canonical names or schema homes |
| Open-question register | `EXPANDED` around current decisions, package admission, probes, ownership, and public-safety proof |
| Directory Rules v1.3 claim | `CORRECTED` to the exact Directory Rules bytes accepted through ADR-0029 |
| `docs/architecture/maplibre-3d.md` navigation | `REMOVED AS CURRENT PATH`; current 3D guidance is `planetary-3d.md` |
| `packages/maplibre-runtime/` placement | `REMOVED AS CURRENT PATH`; verified package seam is `packages/maplibre/` |
| “Cesium retired” badge and settled-disposition language | `CORRECTED` to a proposed decision pending ADR acceptance |
| “No mounted repo inspected” limitation | `SUPERSEDED` by current commit-pinned repository evidence |
| “Implementation UNKNOWN” as a blanket claim | `NARROWED` into confirmed scaffolds, bounded implemented slices, `HOLD` gates, and remaining unknowns |
| CI TODO badge | `REMOVED`; hosted status belongs to actual PR/workflow evidence, not a decorative placeholder |

No prior proposal is silently upgraded to current fact, and no current repository scaffold is represented as a released runtime.

[Back to top](#top)
