<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0006
title: "ADR-0006 — MapLibre Boundary: Only MapLibreAdapter Imports MapLibre"
type: adr
adr_id: ADR-0006
version: v1.5
status: accepted
effective_decision_status: accepted
owners: ["@bartytime4life"]
reviewers_required:
  - Architecture steward
  - Map/runtime steward
  - Explorer Web subsystem owner
  - Package/tooling owner
  - Docs steward
created: 2026-05-10
updated: 2026-09-12
accepted_on: 2026-08-21
policy_label: public
truth_posture: "ACCEPTED architecture / scoped implementation observed / bounded evidence / no operational authority"
owning_root: docs/
responsibility_root: docs/
current_path: docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
responsibility: "Record the accepted package-owned MapRuntimePort and MapLibre adapter seam, reconcile its current implementation evidence precisely, and retain independent gates for source admission, release, deployment, and publication."
supersedes: []
superseded_by: []
decision_evidence:
  issue: 2957
  comment_id: 5361592217
  disposition: "ACCEPT ARCHITECTURE DIRECTION / PROHIBIT LEGACY CDN-GLOBAL ACQUISITION / ADR TEXT FOLLOW-UP REQUIRED / NO DEPENDENCY ADMISSION"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 6f8bf49e04ac9f5d65dc6737a677d332c1676eca
  document_before_update_blob: 4bf4292dc05a85fd4cd829c491808b13894bc223
  package_manifest_blob: 03a24dc1669151863192db30778f30faac0ec5b4
  port_blob: 5a033319649d5fa55fabbab4d077e29d5235980c
  adapter_blob: e201a7717a0a10efc72440e1c71fd4e07fd919cc
  vite_adapter_blob: 57e0f7da9b13006cde2da2592869fc2ba06a4512
  explorer_composition_blob: 65e5e575f0c116fe60d70d83cf9d631eefe745ca
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - packages/maplibre/README.md
  - packages/maplibre/package.json
  - packages/maplibre/src/map-runtime-port.ts
  - packages/maplibre/src/maplibre-adapter.ts
  - packages/maplibre/src/maplibre-vite-adapter.ts
  - apps/explorer-web/src/site/mount-living-atlas.ts
  - apps/explorer-web/src/features/living_atlas/map-style.ts
  - apps/explorer-web/tests/browser/maplibre-webgl-probe.spec.ts
  - tests/policy/test_explorer_web_adapter_boundary.py
  - tools/validators/maplibre/validate_v6_readiness.py
  - scripts/maplibre-smoke-perf.mjs
  - .github/workflows/maplibre-webgl-probe.yml
  - .github/workflows/maplibre-perf-governance.yml
tags: [kfm, adr, maplibre, map-runtime-port, maplibre-adapter, dependency-owner, acquisition-boundary, trust-membrane, currentness-correction]
notes:
  - "v1.5 is a documentation-only current-source reconciliation. It preserves the accepted architecture decision and does not re-admit a dependency, source, release, deployment, promotion, or publication."
  - "At the pinned source, @kfm/maplibre declares maplibre-gl 6.7.0 and contains a concrete adapter plus a package-owned Vite worker helper."
  - "The title's MapLibreAdapter denotes the one package-owned adapter implementation boundary. It is not a claim that exactly one source file imports maplibre-gl: the package-owned Vite worker helper also imports it."
  - "The current Explorer composition is bounded to an inline style and local Vite assets. That source fact and its fixture proof do not activate an external data source or operational environment."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0006 — MapLibre Boundary: Only `MapLibreAdapter` Imports MapLibre

> **Accepted architecture; reconciled current source.** KFM retains one browser-renderer dependency seam: `packages/maplibre/` owns the MapLibre implementation, `MapRuntimePort` remains the KFM-owned runtime contract, and consumers must not acquire `maplibre-gl` directly. At the evidence snapshot, the package contains a concrete `maplibre-gl@6.7.0` implementation and Explorer composes it through the package-owned Vite adapter.

> [!IMPORTANT]
> **This is not an operational authorization.** The source snapshot establishes a bounded implementation and limited test evidence. It does not itself establish dependency governance completion, data-source admission, policy or evidence authority, release, deployment, promotion, public serving, or publication.

**Quick navigation:** [Status](#1-status) · [Decision](#2-decision-preserved) · [Current implementation](#3-current-source-snapshot) · [Boundary contract](#4-boundary-contract) · [Evidence and limits](#5-evidence-and-its-limits) · [Consequences](#6-consequences) · [Open work](#7-open-work) · [References](#8-references)

---

## 1. Status

| Concern | State at `main@6f8bf49e` | Meaning |
|---|---|---|
| Architecture decision | **ACCEPTED** | `packages/maplibre/` is the one reusable browser MapLibre implementation home. No active `packages/maplibre-runtime/` peer is authorized. |
| Implementation | **PRESENT / BOUNDED** | `@kfm/maplibre` declares `maplibre-gl: 6.7.0` and provides `MapLibreAdapter`, a Vite worker helper, tests, and controlled package exports. |
| Direct-import boundary | **PARTIALLY STRUCTURALLY PROVED** | The relevant implementation source scope places direct runtime imports in package-owned adapter modules; Explorer Web has a policy test prohibiting direct raw renderer imports. |
| Consumer composition | **PRESENT / NARROW** | Explorer imports the KFM port and the package `vite-adapter` subpath, then initializes the adapter with a local inline style. |
| Browser fixture evidence | **BOUNDED PASS RECORDED** | A review-only WebGL2 fixture run passed at a separately pinned revision. It is neither rerun by this ADR edit nor a deployment receipt. |
| External source / live transport | **NOT ACTIVATED** | The adapter rejects external style/resource locators; the current Living Atlas style is inline GeoJSON and its browser test denies external requests. |
| Performance readiness | **HOLD** | The former live-CDN performance harness is retired with a finite hold; the performance-governance lane states that no runtime performance baseline or operational proof is produced. |
| Release / deployment / publication | **NOT AUTHORIZED** | This ADR and the current documentation update do not perform or authorize any of those transitions. |

### 1.1 What changed in v1.5

The accepted decision did not change. The superseded v1.4 implementation narrative was stale: it described a dependency-free scaffold with no port, adapter, or migrated consumer. The pinned current tree instead contains:

- private package `@kfm/maplibre` with `maplibre-gl` declared at the exact source value `6.7.0`;
- renderer-neutral `MapRuntimePort` values, finite states, camera operations, selection events, and disposal;
- `MapLibreAdapter` construction, WebGL2 availability checking, an initialization deadline, inline-style validation, camera synchronization, and teardown;
- a package-owned Vite worker configuration helper;
- Explorer’s `mount-living-atlas.ts` composition of the package adapter; and
- unit, browser, policy, export, and readiness surfaces that provide limited, scoped evidence.

The replacement facts are **source observations**, not a retroactive claim that every dependency-review, supply-chain, runtime, data, policy, or operational gate is complete.

### 1.2 Architecture decision versus implementation conformance

Acceptance on 2026-08-21 remains the architectural decision authorized by issue #2957. Current code can be evaluated against that decision without reopening it:

1. a later implementation may satisfy part of the boundary;
2. a later implementation may expose an unresolved mismatch; and
3. neither outcome by itself grants a release, deployment, publication, data-source, or policy authority.

This ADR therefore records both the accepted invariant and the present implementation posture. It does not turn source presence into a blanket compliance or readiness verdict.

[Back to top](#top)

---

## 2. Decision preserved

### 2.1 One physical implementation home

`packages/maplibre/` remains the sole reusable home for the browser MapLibre adapter implementation. `@kfm/maplibre` is an internal, private package identity; its source exports do not create a public distribution promise.

No app-local renderer package, root-owned renderer package, or active `packages/maplibre-runtime/` peer may evolve into a competing runtime owner without a successor or explicit amendment ADR.

### 2.2 What “only `MapLibreAdapter` imports MapLibre” means

The title is an architectural boundary statement, not a literal one-file count. At the pinned source, the relevant production implementation scope has two direct `maplibre-gl` acquisition modules:

| Package-owned module | Current role | Boundary interpretation |
|---|---|---|
| `packages/maplibre/src/maplibre-adapter.ts` | Imports MapLibre CSS and the map constructor; owns map creation, lifecycle, style validation, and teardown. | Core concrete `MapLibreAdapter` implementation. |
| `packages/maplibre/src/maplibre-vite-adapter.ts` | Imports the MapLibre worker asset and `setWorkerUrl`; configures the Vite worker once before creating the core adapter. | Subordinate, package-owned worker bootstrap for the same adapter implementation. It is not a second consumer authority. |

Accordingly, **only the package-owned adapter implementation boundary may import or bootstrap MapLibre**. Consumer code must not directly import `maplibre-gl`, create a renderer, load a CDN/global, or own the dependency. Package-owned tests may mock or exercise that boundary; they are not consumer acquisition paths.

### 2.3 KFM-owned port

`MapRuntimePort` is the renderer-neutral consumer contract. Its current source exposes only KFM-owned, serializable values for:

- initialization, snapshots, cameras, selection subscription, snapshot subscription, and disposal;
- finite lifecycle states including `IDLE`, `INITIALIZING`, `READY`, `STALE`, `DENIED`, `ERROR`, and `DISPOSED`; and
- KFM reason codes and selection/evidence-reference identifiers.

The port does not expose raw MapLibre maps, event objects, source objects, layers, worker objects, protocols, or renderer error classes. It also expressly has no evidence, source, policy, review, lifecycle, correction, release, deployment, or publication authority.

### 2.4 Dependency ownership

The package manifest is the current dependency owner:

~~~json
{
  "name": "@kfm/maplibre",
  "dependencies": {
    "maplibre-gl": "6.7.0"
  }
}
~~~

This records **where the dependency is declared and the exact source value at the snapshot**. It does not state that this ADR independently completed license, provenance, integrity, transitive-dependency, browser-support, CSP, supply-chain, or lockfile governance. Those decisions remain separately reviewable and must never be inferred only from a manifest line.

### 2.5 Consumer rule

Explorer Web may compose a `MapRuntimePort` supplied by `@kfm/maplibre`. It may also use the intentionally narrow package-owned `@kfm/maplibre/vite-adapter` entry point to configure the local build worker and construct the adapter. It must not:

- import `maplibre-gl` directly;
- declare `maplibre-gl` in its manifest;
- create a second adapter, renderer, worker bootstrap, CDN/global loader, plugin loader, or protocol authority;
- interpret a rendered feature, popup, screenshot, or runtime metric as evidence or publication truth; or
- bypass upstream policy, source, evidence, review, release, or correction decisions.

The existing policy test scans Explorer Web source for static, dynamic, and CommonJS raw renderer acquisition. That is useful structural evidence, but it is not a complete repository-wide authorization mechanism.

[Back to top](#top)

---

## 3. Current source snapshot

### 3.1 Runtime implementation

`MapLibreAdapter` implements `MapRuntimePort` and provides a finite browser lifecycle:

1. validates the calling container identifier;
2. copies a JSON-serializable inline style;
3. rejects style/resource fields containing external locators such as `http`, `data`, `blob`, `file`, and `pmtiles`;
4. checks for WebGL2 before renderer construction;
5. starts with a bounded initialization deadline (default 10 seconds, maximum 60 seconds);
6. synchronizes camera state and publishes KFM-owned snapshots; and
7. removes renderer effects and records a disposed state during teardown.

This is a **renderer-runtime capability**, not a data-access or authority capability. The implementation comment explicitly limits the slice to renderer construction, an inline-only style, camera synchronization, finite state, and teardown; source discovery, transport, external style/layer/protocol/plugin admission, and their proof remain outside it.

### 3.2 Worker ownership

The Vite-specific helper imports the package’s MapLibre worker asset via Vite’s `?worker&url` pipeline, calls `setWorkerUrl` once, then constructs the core adapter. Explorer does not repeat that raw worker configuration.

This keeps the worker setup inside the owned package boundary, but it also means the architecture must be evaluated at the **package implementation boundary**, not by treating a single class file as the only possible MapLibre-importing source.

### 3.3 Explorer composition

`apps/explorer-web/src/site/mount-living-atlas.ts` imports:

~~~ts
import type { MapRuntimePort } from "@kfm/maplibre";
import { createViteMapLibreAdapter } from "@kfm/maplibre/vite-adapter";
~~~

It initializes the package-owned adapter with a local `createLivingAtlasStyle(...)` value and an 8-second deadline. On a failure it reports `Renderer ERROR · no factual fallback`; it does not manufacture a data or evidence result.

The current Living Atlas style builds local GeoJSON fixtures. The UI text and tests make its status explicit: generalized/synthetic geometry is shown, external tiles and live observations are absent, and external browser requests are denied by the relevant fixture tests.

### 3.4 Narrow renderer-specific style input

The root `@kfm/maplibre` facade exports renderer-neutral port modules. The `vite-adapter` subpath additionally exports `MapLibreSafeStyle`, which is currently an alias of MapLibre’s `StyleSpecification`. Explorer imports that alias for its inline-style builder.

That is a deliberately bounded package-subpath dependency, not a raw `maplibre-gl` import in Explorer and not a raw map handle. It nevertheless means the current style-authoring path is **not purely renderer-neutral**. This ADR does not hide that distinction:

- the `MapRuntimePort` remains renderer-neutral;
- direct runtime acquisition remains package-owned; and
- the renderer-specific style type should remain narrow, inline-only, and explicitly reviewed, or be replaced by a KFM-owned serializable style contract in a later change.

### 3.5 Legacy CDN/global harness

`scripts/maplibre-smoke-perf.mjs` no longer acquires a live CDN/global renderer. It records that its former `MapLibre GL JS 5.5.0` and glyph CDN behavior is retired, exits with an explicit `WORKFLOW_HOLD` code, and directs bounded smoke evidence to the package-owned Vite fixture.

Retirement is not performance readiness. The script and the performance-governance workflow both retain a finite hold while deterministic fixtures, thresholds, artifact homes, and CI authority remain unresolved.

[Back to top](#top)

---

## 4. Boundary contract

### 4.1 Required behavior inside the package-owned boundary

The adapter implementation must:

- own MapLibre construction, CSS/runtime acquisition, and Vite worker configuration;
- keep raw MapLibre map instances private;
- convert browser lifecycle, camera, and selection behavior into KFM-owned runtime values;
- reject external style/resource locators before renderer acquisition;
- support finite errors, timeout, recovery, and disposal;
- make no claim about source truth, policy, evidence, review, lifecycle, correction, release, deployment, or publication; and
- keep renderer-specific tests, worker support, plugins, protocols, and future extensions subordinate to the same package owner.

### 4.2 Required behavior outside the boundary

Consumers, examples, fixtures, and unrelated packages must:

- depend on `MapRuntimePort` for runtime control;
- avoid a direct `maplibre-gl` dependency or import;
- use only an approved package-owned constructor path when a real renderer is required;
- treat renderer output as a candidate display/interaction result, not as proof of a claim; and
- remain able to use a fake or null runtime where a renderer is not required.

### 4.3 Explicitly out of scope

Nothing in the adapter owns or authorizes:

| Area | Current boundary |
|---|---|
| Canonical data, evidence, or citations | Supplied by governed upstream systems; a render never proves them. |
| Source discovery, remote tiles, live transport, or external styles | Not activated by the current inline-only implementation. |
| Rights, sensitivity, review, or policy | Must be decided upstream before any runtime presentation. |
| Release, deployment, promotion, public serving, or publication | Separate governed transitions; all remain outside this ADR. |
| Plugins, protocols, custom layers, terrain delivery, or alternative worker channels | Require separate, scoped review and evidence. |
| General performance, accessibility, security, long-session, or production browser readiness | No authority is conferred by the bounded tests or one historical probe run. |

[Back to top](#top)

---

## 5. Evidence and its limits

### 5.1 Source and test evidence at the snapshot

| Evidence surface | What it supports | What it does not support |
|---|---|---|
| `packages/maplibre/package.json` and package exports | The current dependency owner, exact declared source version, and owned `adapter`/`vite-adapter` entry points. | Supply-chain approval, release approval, or public package distribution. |
| Adapter unit tests | Container validation, inline-style rejection, lifecycle state, retries, camera sync, timeout, and disposal. | Browser/platform compatibility outside test doubles or any source authority. |
| Vite adapter test | One-time worker configuration before adapter construction. | A general CSP, hosting, or production-worker certification. |
| Explorer import-boundary policy test | No raw renderer acquisition in Explorer source. | All possible repository paths, generated output, future packages, or operational behavior. |
| Explorer browser tests | Local Vite assets, canvas presence, no external requests, finite WebGL error behavior, and teardown for fixture scope. | Remote data admission, a production network posture, performance readiness, or deployment. |
| WebGL probe workflow run `34701026392` | A review-only WebGL2/teardown probe passed at `691ad664442c18e70903847e7f93922cf61bd14d` on 2026-09-12. | A rerun at this documentation change, long-session assurance, release, deployment, publication, or any external-source authorization. |
| Readiness, acquisition-inventory, source-metadata, and performance lanes | Bounded structural/local validation and explicit holds. | Automatic promotion of a green local check into domain or operational authority. |

### 5.2 Evidence lineage and authority order

GitHub source at the evidence snapshot is authoritative for this reconciliation. The following were consulted as **supporting lineage only**:

- [Notion work item — reconcile MapLibre architecture boundary](https://app.notion.com/p/3c9a92021bf681319300c9b58c32e5d9), which identified the original stale scaffold contradiction;
- [Notion work item — close governed MapLibre runtime probe matrix](https://app.notion.com/p/3c9a92021bf68146ab6aca4e03139382), which records bounded probe context and remaining holds; and
- [Drive roadmap — KFM Explorer, Kansas-First Layers, Animation, Live Updates, 3D & Performance](https://docs.google.com/document/d/1L8zsQgam1bdP7uUbX2zxOkTA01enXXu_tlHLKZRPvzQ/edit), which is proposed design lineage and expressly preserves source-admission and operational holds.

The supplied **KFM MapLibre Operating Architecture** manual reinforces the governing distinction: MapLibre is a renderer and interaction runtime, not a truth, source, policy, citation, release, or publication authority. That doctrine guides interpretation; it does not override the repository source snapshot.

### 5.3 Documentation-only validation

This update should validate ADR/index coherence and documentation links at the branch revision. It must not be reported as a dependency upgrade, a browser re-certification, a source activation, a release, a deployment, or a publication event.

[Back to top](#top)

---

## 6. Consequences

### 6.1 Positive consequences

- Current documentation now matches the package, worker, and Explorer composition that actually exist.
- The accepted dependency seam remains local to `packages/maplibre/`.
- The legacy CDN/global path is accurately recorded as retired, not silently treated as a live exception.
- The source records no external-resource behavior in the default adapter/style slice.
- Bounded browser evidence can be cited without converting it into a release or deployment claim.
- The distinction between renderer-neutral port control and renderer-specific style authoring is explicit.

### 6.2 Constraints

- A direct import prohibition needs to be evaluated over the full package-owned adapter implementation boundary, including worker helpers, not only one class file.
- The `MapLibreSafeStyle` alias leaves a deliberately narrow renderer-specific type at the consumer composition edge; it needs continued review.
- Stronger static analysis is still required if the repository wants a proof over all import, dynamic import, generated, worker, plugin, protocol, and loader paths.
- The retired performance harness does not satisfy runtime performance governance.
- No data, authority, rights, evidence, or publication state follows from a visible canvas.

### 6.3 Rollback

This v1.5 change is documentation-only. Reverting it reverts the currentness reconciliation; it does not remove the existing package dependency or runtime implementation. Any code/dependency rollback must be performed by a separate reviewed change against its own version, lockfile, tests, and operational evidence.

[Back to top](#top)

---

## 7. Open work

| Work item | Current state | Required future action |
|---|---|---|
| Dependency governance closure | Not established by this ADR | Review exact package/lockfile state, license, provenance, integrity, transitive closure, browser support, CSP, and supply-chain posture. |
| Complete import/acquisition inventory | Partial | Cover static/type/dynamic/CommonJS/re-export/worker/CDN/global/plugin/protocol/generated paths with stable diagnostics. |
| Renderer-specific style type | Narrow, present | Keep `MapLibreSafeStyle` inline-only and scoped, or define a KFM-owned serializable style contract with a validated package translation. |
| External sources and live transport | Not activated | Require source, rights, policy, evidence, reproducibility, network, and browser admission before enabling any remote input. |
| Browser proof matrix | Bounded pass only | Run the accepted exact-version/browser/toolchain/CSP/teardown/long-session matrix under its owning issue and retain reviewable receipts. |
| Performance governance | Hold | Supply governed deterministic fixtures, thresholds, artifact ownership, and CI authority before calling performance readiness. |
| Operational transitions | Not authorized | Make release, deployment, promotion, public-serving, and publication decisions separately. |

[Back to top](#top)

---

## 8. References

### 8.1 Decision and repository source

- [Issue #2957 — MapLibre architecture governance](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957)
- [Canonical ADR index](./INDEX.md)
- [ADR-0007 — MapLibre GL JS is the sole browser-side renderer](<./ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>)
- [MapLibre package manifest](../../packages/maplibre/package.json)
- [Renderer-neutral runtime port](../../packages/maplibre/src/map-runtime-port.ts)
- [Core MapLibre adapter](../../packages/maplibre/src/maplibre-adapter.ts)
- [Package-owned Vite adapter](../../packages/maplibre/src/maplibre-vite-adapter.ts)
- [Explorer Living Atlas composition](../../apps/explorer-web/src/site/mount-living-atlas.ts)
- [Inline Living Atlas style](../../apps/explorer-web/src/features/living_atlas/map-style.ts)
- [Explorer raw-import boundary test](../../tests/policy/test_explorer_web_adapter_boundary.py)
- [WebGL probe fixture](../../apps/explorer-web/tests/browser/maplibre-webgl-probe.spec.ts)
- [MapLibre WebGL workflow](../../.github/workflows/maplibre-webgl-probe.yml)
- [Retired performance harness](../../scripts/maplibre-smoke-perf.mjs)
- [Performance-governance workflow](../../.github/workflows/maplibre-perf-governance.yml)
- [Bounded WebGL workflow run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/34701026392)

### 8.2 Change history

| Edition | Date | Disposition |
|---|---|---|
| `v1.3` | 2026-08-13 | Repository-grounded proposed decision and pre-acceptance snapshot; preserved in Git history. |
| `v1.4` | 2026-08-21 | Accepted architecture source transition authorized by issue #2957; original implementation narrative was intentionally scaffold-only. |
| `v1.5` | 2026-09-12 | Documentation-only current-source reconciliation at `main@6f8bf49e`. No code, dependency, source, release, deployment, or publication action. |

---

_Last updated 2026-09-12 · Document version: `v1.5` · Source metadata: `accepted` · Effective decision status: `accepted` · Implementation: package-owned bounded adapter observed · Operational authority: none · [Back to top](#top)_
