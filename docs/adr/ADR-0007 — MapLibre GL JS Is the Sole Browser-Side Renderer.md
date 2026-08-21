<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0007-maplibre-sole-browser-renderer
title: "ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer"
type: adr
adr_id: ADR-0007
version: v1.3
status: accepted
effective_decision_status: accepted
owners: ["@bartytime4life"]
reviewers_required:
  - Architecture steward
  - Map/runtime steward
  - Security and supply-chain reviewer
  - Explorer Web subsystem owner
  - Docs steward
created: 2026-05-10
updated: 2026-08-21
accepted_on: 2026-08-21
policy_label: public
truth_posture: "ACCEPTED renderer-family architecture / HOLD dependency and runtime / no publication effect"
owning_root: docs/
responsibility_root: docs/
current_path: "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
responsibility: "Record MapLibre GL JS as KFM's sole normal production browser map/scene renderer family, classify subordinate integrations and peer renderers, bind use to ADR-0006, and preserve separate dependency, runtime, release, deployment, and publication gates."
supersedes: []
superseded_by: []
decision_evidence:
  issue: 2957
  comment_id: 5361592217
  disposition: "ACCEPT ARCHITECTURE DIRECTION / PROHIBIT LEGACY CDN-GLOBAL ACQUISITION / ADR TEXT FOLLOW-UP REQUIRED / NO DEPENDENCY ADMISSION"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 60714d75d7f2b578131204768d1ca6c4bb04b730
  prior_source_blob: 6bfd66b1169728d7fad08f0bb2d7e2a56e3577b2
  prior_index_blob: 419ebd60db28404edb0d363125c85f6f15deaec0
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/maplibre.md
  - docs/architecture/map-shell.md
  - docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - packages/maplibre/README.md
  - packages/maplibre/package.json
  - scripts/maplibre-smoke-perf.mjs
  - tools/validators/maplibre/validate_v6_readiness.py
  - .github/workflows/maplibre-perf-governance.yml
tags: [kfm, adr, maplibre, browser-renderer, renderer-family, plugin, protocol, custom-layer, peer-renderer, no-parallel-authority]
notes:
  - "v1.3 is the reviewed documentation-only source transition authorized by the binding maintainer disposition in issue #2957; the synchronized index transition becomes effective on merge."
  - "MapLibre GL JS is accepted as the sole normal production browser map/scene renderer family, but no version, package, plugin, protocol, custom-layer integration, worker, or browser toolchain is admitted by this ADR."
  - "All future MapLibre runtime use is subordinate to ADR-0006's packages/maplibre/ MapRuntimePort/MapLibreAdapter seam and package-owned dependency rule."
  - "The legacy CDN/global smoke-performance path is prohibited by ADR-0006, carries no exception, and remains a conformance/runtime HOLD until a separate implementation PR migrates or retires it."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer

> **Accepted decision.** MapLibre GL JS is KFM's sole normal production browser map/scene renderer family. Plugins, protocols, overlays, and custom-layer integrations may operate only as subordinate capabilities behind the accepted [`MapRuntimePort` / `MapLibreAdapter`](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) seam. A peer browser renderer requires a separately accepted scoped exception or successor ADR.

[![Decision: accepted](https://img.shields.io/badge/decision-accepted-1a7f37?style=flat-square)](#1)
[![Implementation: hold](https://img.shields.io/badge/implementation-HOLD-d4a72c?style=flat-square)](#8)
[![Dependency: not admitted](https://img.shields.io/badge/renderer_dependency-not_admitted-6e7781?style=flat-square)](#81-current-conformance-posture)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#123-exact-non-effects)

> [!IMPORTANT]
> **Renderer-family acceptance is not version, package, plugin, runtime, or operational admission.** This source/index transition chooses the architecture family only. The repository remains dependency-free at the MapLibre package seam; issue #2906 remains on `HOLD`; and release, deployment, public serving, and publication require later governed decisions.

**Quick navigation:** [Status](#1) · [Context](#2) · [Decision](#3) · [Evidence](#4) · [Directory Rules](#5) · [Consequences](#6) · [Alternatives](#7) · [Validation](#8) · [Rollback](#9) · [Open work](#10) · [Migration](#11) · [Truth summary](#12)

---

<a id="1"></a>

## 1. Status

### 1.1 Decision and implementation state

| Concern | State after merge | Meaning |
|---|---|---|
| ADR source and canonical index | **ACCEPTED** | MapLibre GL JS is the selected browser map/scene renderer family. |
| Import/acquisition seam | **ACCEPTED architecture** | All runtime acquisition is governed by ADR-0006 and physically owned by `packages/maplibre/`. |
| Exact MapLibre version | **NOT ADMITTED** | No version, tarball, integrity, license, provenance, dependency closure, or lockfile entry is accepted here. |
| Plugins, protocols, workers, and custom layers | **NONE ADMITTED** | Classification as subordinate does not grant dependency or capability admission. |
| Package and app implementation | **HOLD / NOT ESTABLISHED** | The package remains a dependency-free scaffold and the app-side adapter path remains placeholder-level. |
| Peer renderer | **PROHIBITED BY DEFAULT** | A peer browser renderer requires a separately accepted scoped exception or successor ADR. |
| Legacy CDN/global harness | **NONCONFORMING / NO EXCEPTION** | It remains unchanged and held pending migration or retirement under ADR-0006. |
| Browser readiness | **HOLD** | Issue #2906 remains the authenticated runtime evidence gate after dependency admission and implementation. |
| Release, deployment, publication | **UNCHANGED / NOT AUTHORIZED** | The accepted renderer family does not release, deploy, promote, serve, or publish anything. |

### 1.2 Acceptance evidence

Issue #2957 contains a binding maintainer disposition that:

1. accepts MapLibre GL JS as the sole normal production browser map/scene renderer family;
2. makes plugins, protocols, overlays, and custom-layer integrations subordinate to that family and the ADR-0006 seam;
3. requires a separately accepted scoped exception or successor ADR for a peer renderer;
4. prohibits the legacy CDN/global path rather than preserving it as an exception;
5. keeps exact dependency/version admission, implementation, browser proof, release, deployment, and publication separate.

The previously proposed gates that required a functioning runtime before accepting the family choice are therefore removed. Conformance remains downstream and fail-closed.

[Back to top](#top)

---

<a id="2"></a>

## 2. Context

KFM needs one stable browser-map rendering family so package ownership, public types, plugin review, browser support, security correction, testing, and rollback remain finite. Allowing each feature, app, example, or performance harness to choose its own renderer would create parallel runtime authorities and make the browser trust boundary dependent on incidental imports.

The repository's existing architecture is strongly MapLibre-oriented but remains scaffold/HOLD at runtime. That posture is sufficient to decide the family without claiming that any current file, workflow, package version, screenshot, benchmark, or planning document proves implementation readiness.

### 2.1 Scope of “browser-side renderer”

This ADR governs the engine that owns the primary interactive browser map or geospatial scene lifecycle, including camera/view state, source/layer composition, hit testing, feature selection, frame rendering, and renderer-bound resource loading.

It does not govern ordinary webpage rendering, DOM layout, forms, tables, text, generic charts, non-map Canvas/SVG components, native mobile map engines, server-side geoprocessing, tile generation, or offline catalog production unless such a surface becomes a browser peer renderer under the definition below.

### 2.2 Why family choice and dependency admission are separate

A family decision answers which architecture KFM intends to implement. Dependency admission answers whether exact third-party bytes, versions, transitive packages, workers, browser support, license, integrity, and supply-chain posture are acceptable. Runtime readiness answers whether the admitted implementation behaves correctly in the required browsers and long-session conditions. None of those transitions substitutes for another.

[Back to top](#top)

---

<a id="3"></a>

## 3. Decision

### 3.1 Sole normal production renderer family

MapLibre GL JS is the sole normal production browser map/scene renderer family for KFM. All product browser-map capabilities must be expressible through the KFM-owned `MapRuntimePort` and realized through the package-owned `MapLibreAdapter` defined by ADR-0006.

KFM does not support an ambient “default renderer plus optional peers” model. A second independent browser renderer is prohibited unless a separately reviewed and accepted decision establishes a bounded exception or superseding architecture.

### 3.2 Accepted vocabulary

| Term | Accepted meaning | Governance effect |
|---|---|---|
| **Renderer** | The browser engine that owns the primary map/scene lifecycle, camera/view state, source/layer composition, frame rendering, hit testing, and feature selection | MapLibre GL JS is the sole accepted family |
| **Plugin** | A renderer-bound extension that executes within the accepted renderer family and does not own an independent map/scene lifecycle | Subordinate; requires separate dependency/capability admission |
| **Protocol** | A renderer resource-loading hook registered and managed inside the accepted adapter boundary | Subordinate; no independent endpoint, policy, or publication authority |
| **Overlay** | A visual/interaction surface synchronized to the accepted renderer while the accepted renderer remains the map/scene lifecycle owner | Subordinate; may not become a hidden peer renderer |
| **Custom-layer integration** | An integration using the accepted renderer's extension APIs while MapLibre remains responsible for scene lifecycle and KFM selection translation | Subordinate; requires explicit admission and teardown/correction proof |
| **Peer renderer** | An independent browser rendering engine capable of owning map/scene lifecycle, camera, hit testing, feature selection, or a separately initialized geospatial scene | Prohibited without an accepted scoped exception or successor ADR |

A library's marketing label does not determine its classification. Its actual lifecycle, dependency, rendering, selection, worker, endpoint, and teardown behavior does.

### 3.3 Subordinate integration rule

A plugin, protocol, overlay, or custom-layer integration is subordinate only when all of the following are true:

1. MapLibre remains the primary map/scene lifecycle owner.
2. The integration is acquired and initialized only inside the ADR-0006 package seam.
3. Consumers see only KFM-owned types and finite states.
4. The integration cannot bypass governed descriptors, evidence, policy, rights, sensitivity, review, or release state.
5. Dependency/version/license/integrity/supply-chain admission is explicit and reversible.
6. Teardown, correction, withdrawal, failure, and rollback behavior are reviewable.
7. It does not create a second renderer dependency owner, global, CDN loader, worker authority, or direct app import.

An integration that fails any of these tests is a peer-renderer candidate or nonconforming acquisition path, not an automatically admitted plugin.

### 3.4 Peer-renderer exception rule

A peer renderer requires a separately accepted scoped exception or successor ADR that identifies at least:

- exact use case and why the accepted MapLibre family cannot satisfy it;
- physical package and dependency ownership;
- public KFM port and raw-type isolation;
- affected consumers and coexistence/migration model;
- package/version/integrity/license/supply-chain posture;
- worker, CSP, endpoint, browser, performance, accessibility, and security evidence;
- evidence/policy/sensitivity/release boundaries;
- deterministic enforcement and negative proof;
- correction, removal, rollback, and sunset conditions;
- whether ADR-0006 or this ADR is amended, excepted, or superseded.

A test, example, feature flag, benchmark, custom layer, or temporary experiment does not create an exception by implication.

### 3.5 Dependency and version non-admission

This ADR does not select or admit any `maplibre-gl` version. It does not admit a plugin, protocol helper, custom-layer library, worker package, style-runtime package, 3D engine, overlay framework, or peer renderer.

All future renderer-bound dependencies are owned by `packages/maplibre/package.json` under ADR-0006 and require a separate exact dependency-admission record before implementation or runtime use.

### 3.6 Legacy acquisition path

The root CDN/global smoke-performance harness is not a renderer-family exception. It is a nonconforming acquisition path under ADR-0006 and must be migrated behind the admitted package seam or retired in a separate implementation change. It may not be used to prove version admission, browser readiness, production support, or release eligibility.

### 3.7 No authority by implication

MapLibre and subordinate integrations render governed inputs. They do not decide claim truth, source authority, rights, sensitivity, evidence closure, policy, review, lifecycle promotion, correction authority, release, deployment, or publication. A render, feature query, screenshot, pixel comparison, benchmark, or successful probe is downstream runtime evidence only.

[Back to top](#top)

---

<a id="4"></a>

## 4. Evidence and Current Repository Boundary

### 4.1 Confirmed acceptance baseline

| Surface | Confirmed state | Effect on this ADR |
|---|---|---|
| `packages/maplibre/` | Private dependency-free scaffold | Accepted physical home under ADR-0006; not an implemented renderer |
| `packages/maplibre/src/index.ts` | Placeholder-level entry | No functioning adapter or public API is established |
| Explorer app adapter path | Comment-only placeholder | May not become a second importer or dependency owner |
| Readiness validator and fixtures | Bounded structural/classifier evidence | Useful downstream seed; not complete renderer-family enforcement or browser proof |
| Legacy smoke/performance harness | CDN/global runtime acquisition outside the package seam | Known nonconformance; no exception |
| Issue #2906 | Separate browser and long-session evidence gate | Remains `HOLD` and is not satisfied by this ADR |

### 4.2 Evidence that is not acceptance proof

The following do not admit a renderer or subordinate integration:

- an upstream release or version string;
- repository package/file presence;
- a placeholder interface or adapter;
- synthetic classifier fixtures;
- a successful static workflow;
- a screenshot, benchmark, or pixel result;
- planning manuals or supplied design lineage;
- a branch, commit, pull request, merge, issue state, badge, or index row without matching source status;
- a release, deployment, or publication claim made by browser code.

[Back to top](#top)

---

<a id="5"></a>

## 5. Directory Rules and ADR-0006 Relationship

Accepted ADR-0029 and Directory Rules place reusable implementation in `packages/`, deployable product surfaces in `apps/`, repository-wide validators in `tools/validators/`, and architecture decisions in `docs/adr/`.

This ADR does not create a new root. ADR-0006 resolves the exact reusable child package and dependency seam:

```text
apps/explorer-web and shared consumers
        -> KFM-owned MapRuntimePort
        -> packages/maplibre/ MapLibreAdapter
        -> later-admitted MapLibre GL JS and subordinate integrations
```

The two accepted decisions are complementary:

| ADR | Binding question |
|---|---|
| ADR-0006 | Where may browser-renderer dependencies be declared, acquired, initialized, and exposed? |
| ADR-0007 | Which browser map/scene renderer family is accepted, and what requires a peer-renderer exception? |

Neither ADR admits exact third-party bytes, proves implementation, or authorizes operations.

[Back to top](#top)

---

<a id="6"></a>

## 6. Consequences

### 6.1 Positive consequences

- KFM has one browser map/scene renderer family and one reusable dependency seam.
- Plugin and custom-layer review remains subordinate rather than becoming silent multi-renderer architecture.
- Consumer contracts can remain KFM-owned and renderer-neutral.
- Browser-support, supply-chain correction, and rollback evidence converge on one package.
- Peer renderer proposals become explicit, reviewable architecture choices.
- The legacy CDN/global path remains visible as nonconformance instead of being normalized through historical use.
- Architecture acceptance can precede implementation without misrepresenting readiness.

### 6.2 Costs and constraints

- MapLibre-specific constraints must be handled deliberately rather than escaped through a second renderer.
- Advanced integrations need classification and per-dependency admission.
- The package seam and structural validator must detect disguised peer renderers and indirect acquisition.
- A legitimate future use case for another renderer requires an ADR rather than an incidental package addition.
- Runtime failure after admission may force dependency rollback while the family decision remains accepted.

### 6.3 Compatibility and public behavior

This architecture transition changes no public data contract, evidence identity, layer manifest, browser behavior, package dependency, runtime output, release, deployment, or published artifact. Later implementation may preserve product behavior through `MapRuntimePort` while changing renderer internals behind the adapter.

[Back to top](#top)

---

<a id="7"></a>

## 7. Alternatives Considered

### 7.1 MapLibre as default with ungoverned peer renderers — rejected

A default-only rule permits independent lifecycle, dependency, selection, and correction paths to spread across the repository. It defeats the finite package and trust boundary.

### 7.2 One renderer per feature or deployable — rejected

Per-feature or per-app choice multiplies dependency owners, browser behavior, testing, security correction, and rollback obligations.

### 7.3 Treat every 3D/overlay library as a harmless plugin — rejected

Some integrations can own independent cameras, hit testing, workers, scenes, or render loops. Classification depends on actual behavior; a hidden peer renderer requires explicit architecture review.

### 7.4 Permanent or temporary exception for the CDN/global harness — rejected

The binding maintainer direction prohibits the path. Test intent does not remove dependency, network, integrity, correction, or rollback obligations.

### 7.5 Keep the renderer family undecided until browser proof — rejected

Browser proof requires an architecture and admitted implementation to test. Deferring the family decision until runtime proof recreates the circular gate resolved in issue #2957.

### 7.6 Native or server-side rendering under this ADR — not selected

Native mobile, server-side preview, tile generation, and offline production are distinct execution boundaries. They require their own concrete use case and architecture review if introduced; this ADR neither accepts nor forbids them by implication.

[Back to top](#top)

---

<a id="8"></a>

## 8. Validation and Admission Gates

### 8.1 Current conformance posture

The architecture is accepted; implementation remains held. Current package, validator, app, workflow, and harness surfaces do not yet prove conformity. In particular, a bounded import scan cannot establish complete peer-renderer absence or package-only acquisition, and the legacy CDN/global path remains known divergence.

### 8.2 Downstream transition order

1. Merge this architecture-only source/index transition with ADR-0006.
2. Separately admit exact renderer dependency bytes, version, integrity, license, provenance, transitive closure, browser support, worker/CSP posture, and lockfile resolution in `packages/maplibre/package.json`.
3. Implement `MapRuntimePort`/`MapLibreAdapter`, migrate consumers, enforce renderer-family/acquisition rules, and migrate or retire the legacy harness.
4. Execute issue #2906's authenticated browser, headless, interaction, resource, and long-session probes.
5. Make release, deployment, public serving, and publication decisions separately.

### 8.3 Required future enforcement

A later structural gate must:

- identify renderer, plugin, protocol, overlay, custom-layer, and peer-renderer acquisitions by actual behavior and dependency;
- inspect manifests, imports, re-exports, dynamic/CommonJS paths, workers, CDN/global loading, generated/runtime surfaces, examples, tests, and harnesses;
- require the ADR-0006 package owner and KFM public seam;
- reject direct app/root/shared-package renderer dependencies;
- include positive and negative fixtures with stable reason codes;
- keep version-readiness policy separate from structural ownership;
- fail closed on unclassified or unadmitted renderer technologies.

### 8.4 Documentation-transition validation

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

A green result proves source/index coherence only. It does not prove dependency admission, renderer-family conformance, runtime correctness, performance, accessibility, security, release, deployment, or publication.

[Back to top](#top)

---

<a id="9"></a>

## 9. Rollback

### 9.1 Repository rollback

Before merge, close the draft PR or reset its branch. After merge, revert the three documentation changes through normal review if the accepted transition was erroneous. Because the packet adds no dependency or runtime, repository rollback requires no package, lockfile, consumer, release, deployment, or publication migration.

### 9.2 Dependency/runtime rollback

A later dependency or runtime failure must remove or revert the admitted implementation through its own recorded rollback while preserving this ADR as accepted architecture history. Returning `packages/maplibre/` to its dependency-free fake/null-port posture does not require pretending the family decision was never made.

### 9.3 Architectural supersession

Replacing MapLibre as the sole family, admitting an enduring peer renderer, changing the exception model, or making another package the renderer authority requires a successor or explicit amendment ADR and synchronized index treatment. Do not rewrite this accepted record through code or manifest changes.

[Back to top](#top)

---

<a id="10"></a>

## 10. Open Work

The architecture choice is closed. These downstream questions remain held:

| Question | State | Required later evidence |
|---|---|---|
| Exact MapLibre version and immutable package bytes | `NOT ADMITTED` | Dependency/integrity/license/supply-chain packet |
| Exact browser, worker, CSP, bundler, and support matrix | `HOLD` | Dependency and implementation review |
| Initial plugin/protocol/custom-layer inventory | `NONE ADMITTED` | Per-integration classification and admission |
| Complete peer-renderer/acquisition validator | `HOLD` | Deterministic structural implementation and fixtures |
| Consumer migration and raw-type isolation | `HOLD` | Compile-time and runtime-neutral tests |
| Legacy harness migration versus retirement | `HOLD`; no exception | Separate implementation PR |
| Browser/headless/long-session readiness | `HOLD` | Issue #2906 |
| Native, server-side, or offline renderer use cases | `UNDECIDED / OUT OF SCOPE` | Concrete separately reviewed requirement |
| Release, deployment, public serving, publication | `NOT AUTHORIZED` | Separate governed operational decisions |

[Back to top](#top)

---

<a id="11"></a>

## 11. Migration

### 11.1 Architecture-only transition

This packet changes only ADR-0006, ADR-0007, and `docs/adr/INDEX.md`. It does not modify the package, app, manifest, lockfile, validators, tests, workflows, harness, or runtime.

### 11.2 Later implementation sequence

1. Bind exact dependency ownership and admitted bytes to `packages/maplibre/`.
2. Define KFM-owned port/event/selection/error types.
3. Implement the package-owned MapLibre adapter and fake/null counterpart.
4. Inventory and enforce every renderer/acquisition path.
5. Migrate Explorer and shared consumers without raw renderer types.
6. Migrate or retire the CDN/global harness.
7. Execute #2906 at the exact admitted head/toolchain.
8. Seek any release, deployment, and publication authority separately.

No step may silently introduce a peer renderer, direct app dependency, global loader, or plugin outside the accepted seam.

[Back to top](#top)

---

<a id="12"></a>

## 12. Truth Summary and References

### 12.1 Truth summary

| Claim | Status |
|---|---|
| MapLibre GL JS is KFM's sole normal production browser map/scene renderer family | **ACCEPTED** |
| Plugins, protocols, overlays, and custom-layer integrations are subordinate behind ADR-0006 | **ACCEPTED architecture; none admitted** |
| A peer renderer requires a separately accepted scoped exception or successor ADR | **ACCEPTED** |
| `packages/maplibre/` and `MapLibreAdapter` own runtime acquisition | **ACCEPTED architecture under ADR-0006** |
| An exact MapLibre version or dependency closure is admitted | **FALSE / NOT ADMITTED** |
| The current package implements a functioning renderer | **NOT ESTABLISHED** |
| The legacy CDN/global path is allowed | **FALSE / PROHIBITED / NO EXCEPTION** |
| #2906 browser readiness is satisfied | **FALSE / HOLD** |
| Release, deployment, or publication changed | **FALSE** |

### 12.2 References

- [Issue #2957 — MapLibre architecture governance](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957)
- [ADR-0006 — MapLibre package and adapter boundary](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md)
- [Canonical ADR index](./INDEX.md)
- [ADR-0029 — Directory Governance Standard v2](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [MapLibre architecture](../architecture/maplibre.md)
- [Map Runtime Boundary](../architecture/ui/MAP_RUNTIME_BOUNDARY.md)
- [MapLibre package README](../../packages/maplibre/README.md)
- [Legacy smoke/performance harness](../../scripts/maplibre-smoke-perf.mjs)
- [Issue #2906 — browser/runtime readiness](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2906)

### 12.3 Exact non-effects

This transition does not add or change `maplibre-gl`, any plugin, protocol, worker, manifest, lockfile, source module, app, test, fixture, validator, workflow, harness, browser result, source admission, policy, contract, schema, evidence, receipt, proof, lifecycle state, release, deployment, publication, access, or repository setting.

### 12.4 Change history

| Edition | Date | Disposition |
|---|---|---|
| `v1.2` | 2026-08-13 | Repository-grounded proposed decision and pre-acceptance evidence snapshot; preserved in Git history |
| `v1.3` | 2026-08-21 | Accepted renderer-family source transition authorized by issue #2957; no dependency, runtime, release, deployment, or publication effect |

---

_Last updated 2026-08-21 · Document version: v1.3 · Source metadata: `accepted` · Effective decision status: `accepted` · Implementation: dependency-free scaffold / `HOLD` · Publication effect: none · [Back to top](#top)_
