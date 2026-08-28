<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0006
title: "ADR-0006 — MapLibre Boundary: Only MapLibreAdapter Imports MapLibre"
type: adr
adr_id: ADR-0006
version: v1.4
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
updated: 2026-08-21
accepted_on: 2026-08-21
policy_label: public
truth_posture: "ACCEPTED architecture / HOLD dependency and implementation / no publication effect"
owning_root: docs/
responsibility_root: docs/
current_path: docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
responsibility: "Record the accepted package-owned MapRuntimePort and MapLibreAdapter seam, renderer dependency ownership, acquisition prohibition, downstream admission order, and rollback without admitting a renderer dependency or granting runtime, release, deployment, or publication authority."
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
  prior_source_blob: 3b789a623a07d27eb538ffaed10b0487ffc43d95
  prior_index_blob: 419ebd60db28404edb0d363125c85f6f15deaec0
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/map-shell.md
  - docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - packages/maplibre/README.md
  - packages/maplibre/package.json
  - packages/maplibre/src/index.ts
  - apps/explorer-web/src/adapters/MapLibreAdapter.ts
  - scripts/maplibre-smoke-perf.mjs
  - tools/validators/maplibre/validate_v6_readiness.py
  - tests/policy/test_explorer_web_adapter_boundary.py
  - .github/workflows/maplibre-perf-governance.yml
tags: [kfm, adr, maplibre, map-runtime-port, maplibre-adapter, dependency-owner, acquisition-boundary, trust-membrane, no-parallel-authority]
notes:
  - "v1.4 is the reviewed documentation-only source transition authorized by the binding maintainer disposition in issue #2957; the synchronized index transition becomes effective on merge."
  - "The accepted physical reusable home is packages/maplibre/; packages/maplibre-runtime/ is not an active or authorized peer package."
  - "Acceptance defines architecture only. It does not add maplibre-gl, select a version, change a manifest or lockfile, implement MapRuntimePort or MapLibreAdapter, migrate a consumer, run browser probes, or change release, deployment, publication, source, policy, or repository settings."
  - "The existing CDN/global smoke-performance path is a known nonconforming acquisition path with no exception; it remains unchanged and held pending a separate migration-or-retirement implementation packet."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0006 — MapLibre Boundary: Only `MapLibreAdapter` Imports MapLibre

> **Accepted decision.** KFM has one browser-renderer dependency seam. The reusable implementation home is [`packages/maplibre/`](../../packages/maplibre/README.md); consumers depend on a KFM-owned `MapRuntimePort`; one package-owned `MapLibreAdapter` owns MapLibre runtime acquisition; and no renderer dependency, raw renderer type, CDN/global loader, worker bootstrap, plugin, or protocol may create a parallel acquisition path.

[![Decision: accepted](https://img.shields.io/badge/decision-accepted-1a7f37?style=flat-square)](#1-status)
[![Implementation: hold](https://img.shields.io/badge/implementation-HOLD-d4a72c?style=flat-square)](#71-current-conformance-posture)
[![Dependency: not admitted](https://img.shields.io/badge/maplibre--gl-not_admitted-6e7781?style=flat-square)](#72-downstream-gates)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#62-what-the-adapter-must-not-do)

> [!IMPORTANT]
> **Architecture acceptance is not dependency or runtime admission.** This decision becomes effective through the reviewed source-and-index merge. The repository remains at its dependency-free scaffold posture until separate admission and implementation packets close. Issue #2906 remains the browser/runtime evidence gate, and release, deployment, and publication remain later governed decisions.

**Quick navigation:** [Header](#0-adr-header) · [Status](#1-status) · [Summary](#2-summary) · [Context](#3-context) · [Decision](#4-decision) · [Scope](#5-scope) · [Boundary contract](#6-boundary-contract) · [Enforcement](#7-enforcement) · [Consequences](#8-consequences) · [Alternatives](#9-alternatives-considered) · [Migration and rollback](#10-migration--rollback) · [Open work](#11-open-questions) · [References](#12-references)

---

## 0. ADR Header

| Field | Accepted value |
|---|---|
| **ID** | `ADR-0006` |
| **Status** | `accepted` — synchronized with the canonical [`INDEX.md`](./INDEX.md) in this reviewed transition |
| **Created** | 2026-05-10 |
| **Accepted** | 2026-08-21; authorized by the binding maintainer disposition in issue #2957 |
| **Physical reusable home** | [`packages/maplibre/`](../../packages/maplibre/README.md) |
| **KFM public boundary** | `MapRuntimePort` and KFM-owned descriptors, events, selections, states, and errors |
| **Concrete renderer adapter** | One package-owned `MapLibreAdapter` implementation behind `MapRuntimePort` |
| **Dependency owner** | [`packages/maplibre/package.json`](../../packages/maplibre/package.json), if and only if a later dependency-admission change is approved |
| **Related renderer-family decision** | [`ADR-0007`](<./ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) |
| **Current implementation state** | `HOLD` — dependency-free scaffold; no functioning port, adapter, admitted renderer dependency, or authenticated browser proof is established by this change |
| **Publication effect** | None |

The source/index status transition accepts only the architecture recorded here. It does not claim that the current package scaffold conforms to the accepted design.

[Back to top](#top)

---

## 1. Status

### 1.1 Decision state versus conformance state

| Concern | State after merge | Meaning |
|---|---|---|
| Architecture decision | **ACCEPTED** | The package home, KFM port, adapter seam, dependency owner, acquisition prohibition, and transition ordering are binding. |
| Package path | **ACCEPTED** | `packages/maplibre/` is the sole reusable browser-renderer adapter home. No active `packages/maplibre-runtime/` peer is authorized. |
| Package implementation | **HOLD / NOT ESTABLISHED** | The current package remains a scaffold. This ADR does not create source, exports, build metadata, tests, or a runtime. |
| Renderer dependency | **NOT ADMITTED** | No `maplibre-gl` version, plugin, protocol helper, worker package, integrity value, license review, or lockfile closure is accepted here. |
| Consumer migration | **NOT STARTED BY THIS CHANGE** | Explorer Web and shared consumers are not modified. |
| Acquisition conformance | **HOLD** | Existing validators are bounded; the known CDN/global harness is nonconforming and has no exception. |
| Runtime readiness | **HOLD** | Issue #2906 remains responsible for authenticated browser and long-session evidence after dependency admission and implementation. |
| Release / deployment / publication | **UNCHANGED / NOT AUTHORIZED** | An accepted architecture ADR is not a release, deployment, promotion, source admission, policy decision, or publication record. |

### 1.2 Acceptance evidence

The maintainer disposition in issue #2957 explicitly decided all architecture questions needed for this record:

1. retain `packages/maplibre/` as the single reusable home;
2. define a KFM-owned `MapRuntimePort` and one concrete package-owned `MapLibreAdapter` seam;
3. keep renderer dependency ownership in the package manifest;
4. prohibit the legacy CDN/global acquisition path rather than granting it an exception;
5. keep the transition documentation-only and preserve dependency, implementation, runtime, release, deployment, and publication holds.

Implementation proof is deliberately downstream. Requiring a functioning adapter, admitted dependency, consumer migration, or #2906 browser result before accepting this architecture would invert the governing order and recreate the circular gate resolved by issue #2957.

[Back to top](#top)

---

## 2. Summary

MapLibre is a downstream browser renderer and interaction runtime. It is not a truth store, source registry, policy engine, evidence resolver, citation authority, release authority, or publisher. The accepted seam keeps those responsibilities separate:

```text
Governed inputs and finite upstream states
        -> KFM-owned MapRuntimePort
        -> package-owned MapLibreAdapter
        -> later-admitted MapLibre runtime and subordinate integrations
```

The architecture creates one reusable dependency owner and one renderer-neutral consumer contract. It preserves deterministic fake/null implementations for tests and rollback, prevents renderer types from spreading into product code, and keeps dependency/version correction bounded to one package.

ADR-0006 answers **where and through what KFM boundary** a browser renderer may be acquired. ADR-0007 separately answers **which renderer family** is accepted. Both architecture decisions can be accepted while implementation remains held.

[Back to top](#top)

---

## 3. Context

### 3.1 Repository posture at acceptance

The repository already contains `packages/maplibre/` as private `@kfm/maplibre` version `0.0.0`, but its entry point remains scaffold-level and its manifest has no renderer dependency. The Explorer-side `MapLibreAdapter.ts` path is comment-only. Existing source checks are bounded and not fully equivalent, while the root smoke/performance script acquires a renderer through a live CDN/global path outside the package seam.

Those facts establish the transition baseline, not implementation authority. The architecture decision resolves the previously open ownership questions without treating current files, fixtures, workflows, or planning lineage as proof of conformance.

### 3.2 Resolved package-name lineage

| Path | Accepted classification |
|---|---|
| `packages/maplibre/` | Sole reusable browser-renderer adapter home |
| `packages/maplibre-runtime/` | Historical/proposal lineage only; not an authorized active peer package |
| `apps/explorer-web/src/adapters/MapLibreAdapter.ts` | Existing placeholder path; a later implementation may remove it, rename it, or reduce it to renderer-neutral composition/bootstrap, but it may not become a second runtime importer or adapter authority |

A future change to the accepted physical home requires a successor or explicit amendment ADR with migration and rollback. It may not be inferred from a package rename, convenience wrapper, or implementation PR.

### 3.3 Problem being prevented

Without this decision, KFM could accumulate direct app imports, package re-exports, worker loaders, CDN scripts, globals, plugin bootstraps, protocol registration, raw type leakage, and multiple independently evolving adapter packages. That would blur dependency ownership, make supply-chain correction and rollback non-local, and permit renderer behavior to bypass governed inputs and finite evidence states.

[Back to top](#top)

---

## 4. Decision

### 4.1 Sole physical implementation home

`packages/maplibre/` is the sole reusable home for KFM's browser MapLibre adapter implementation. No second writable `packages/maplibre-runtime/`, app-local renderer package, or root-owned renderer implementation may evolve in parallel.

The package identity `@kfm/maplibre` is retained as the current internal identity. This architecture decision does not create a public distribution promise or admit package exports.

### 4.2 KFM-owned `MapRuntimePort`

`MapRuntimePort` is the renderer-neutral boundary used by browser-map consumers. Its exact TypeScript shape is deferred to the implementation packet, but its accepted semantic responsibilities are:

- initialize and dispose a map runtime through bounded KFM inputs;
- bind or remove governed layer, style, source, and artifact descriptors;
- expose serializable camera and view operations;
- translate renderer interactions into KFM-owned selection and event values;
- expose finite loading, ready, stale, denied, abstained, conflict, degraded, withdrawn, rollback, and error states;
- support deterministic fake or null implementations without MapLibre, network, DOM, WebGL, workers, or renderer-specific types.

The port MUST NOT expose or require raw MapLibre maps, events, sources, layers, styles, workers, protocols, plugin objects, or renderer error classes.

### 4.3 Package-owned `MapLibreAdapter`

`MapLibreAdapter` is the one concrete MapLibre implementation of `MapRuntimePort`. It is owned by `packages/maplibre/` and forms the sole renderer-acquisition seam.

A later implementation packet must make the exact package-internal acquisition surface explicit and machine-checkable. Package-private helpers may support the adapter only as part of that declared implementation boundary; they must not create another public adapter, manifest owner, consumer-facing renderer type, or independently callable acquisition path.

### 4.4 Dependency ownership

Only `packages/maplibre/package.json` may later declare `maplibre-gl` and renderer-bound plugin, protocol, worker, style-runtime, or helper dependencies. Root, Explorer Web, shared UI, examples, and unrelated packages must not declare those dependencies directly.

This ownership rule does **not** admit a dependency. Exact version, package integrity, license, provenance, supply-chain posture, browser support, CSP/worker strategy, transitive closure, package-manager resolution, and lockfile bytes require a separate reviewed dependency-admission packet.

### 4.5 Acquisition prohibition

Outside the declared package-owned adapter implementation boundary, KFM prohibits renderer acquisition through:

- static, side-effect, or type-only imports;
- re-exports or barrel exports;
- dynamic `import()` or CommonJS `require()`;
- package-manifest declarations;
- worker constructors, worker URLs, or runtime bootstrap bundles;
- browser `<script>` or `<link>` acquisition;
- CDN URLs or globals such as `maplibregl`;
- direct renderer object construction;
- plugin or custom-layer imports that acquire a peer runtime;
- protocol registration that creates an independent loading authority;
- examples, tests, benchmarks, development servers, generated source, or performance harnesses.

Static documentation references and data-only style/schema validation do not by themselves acquire a browser runtime. Any future non-runtime tooling exception must be explicitly scoped and must not re-export runtime types or create a browser acquisition path.

### 4.6 Legacy CDN/global path

[`scripts/maplibre-smoke-perf.mjs`](../../scripts/maplibre-smoke-perf.mjs) is a known nonconforming acquisition path because it obtains a renderer through CDN/global loading outside the accepted package seam.

The maintainer disposition grants it **no permanent, temporary, test-only, or grandfathered exception**. It remains unchanged in this documentation-only packet and keeps conformance/runtime readiness on `HOLD`. A separate implementation PR must either:

1. migrate the harness to package-owned, admitted, reproducible test support behind the seam; or
2. retire the harness and its dependent workflow assumptions.

A successful syntax check, performance run, screenshot, or historical receipt cannot convert that path into accepted architecture.

### 4.7 Consumer and app boundary

Explorer Web, shared UI, examples, and consumer tests use KFM-owned port/types only. They may compose a port instance, but they may not acquire MapLibre, own renderer dependencies, cast KFM values to renderer types, or treat rendered feature properties as evidence.

The existing app-local `MapLibreAdapter.ts` placeholder may survive only as renderer-neutral composition/bootstrap during migration. It may not import MapLibre, declare a second adapter implementation, or expose renderer handles.

### 4.8 No authority by implication

The port and adapter consume upstream policy, evidence, review, and release decisions. They do not originate source authority, rights, sensitivity, evidence closure, review approval, lifecycle promotion, correction authority, release, deployment, or publication.

[Back to top](#top)

---

## 5. Scope

### 5.1 In scope

- browser-side MapLibre runtime acquisition and dependency ownership;
- the physical package home and no-parallel-package rule;
- `MapRuntimePort` and `MapLibreAdapter` semantic roles;
- renderer-neutral public types and raw-type prohibition;
- workers, globals, CDN loading, plugins, protocols, custom layers, examples, tests, and harnesses as acquisition surfaces;
- consumer migration constraints, conformance evidence, correction, and rollback ordering.

### 5.2 Out of scope for this transition

- editing `packages/maplibre/`, any manifest, or `pnpm-lock.yaml`;
- selecting or installing a `maplibre-gl` version or any renderer-bound integration;
- defining exact TypeScript signatures, exports, build tooling, or source-module layout;
- modifying Explorer Web, tests, validators, fixtures, workflows, or the legacy harness;
- running or satisfying issue #2906 browser/runtime probes;
- changing data, contracts, schemas, policy, source admission, lifecycle state, evidence, receipts, proofs, release, deployment, publication, or repository settings;
- accepting a public package API or distribution contract.

[Back to top](#top)

---

## 6. Boundary Contract

### 6.1 What `MapLibreAdapter` must do

1. Consume governed, released, public-safe or otherwise authorized inputs.
2. Keep raw renderer handles and types private.
3. Translate camera, click, load, source, lifecycle, and error events into KFM-owned values.
4. Treat hit-test results as candidates, not supported claims.
5. Preserve finite negative, stale, correction, withdrawal, and rollback states.
6. Initialize and dispose renderer effects, admitted workers, protocols, and subordinate integrations inside the package boundary.
7. Support deterministic fake/null-port substitution for tests and rollback.
8. Keep runtime health and performance evidence separate from domain evidence.

### 6.2 What the adapter must not do

| Must not | Reason |
|---|---|
| Read RAW, WORK, QUARANTINE, canonical stores, credentials, or model runtimes | Public/browser runtime uses governed interfaces and released artifacts |
| Decide source authority, rights, sensitivity, evidence closure, review, release, or publication | Those responsibilities remain upstream |
| Fetch arbitrary unregistered data, tile, plugin, or protocol endpoints as the normal path | Inputs and integrations require governed admission |
| Re-export MapLibre or plugin types | That would recreate a second dependency seam in consumers |
| Treat a render, screenshot, popup, feature property, or metric as truth | Renderer output is downstream derived behavior |
| Hide sensitive geometry only with style rules | Underlying bytes may still disclose restricted information |
| Persist authoritative decisions or claim publication | The adapter is not a policy, evidence, release, or publication store |

### 6.3 What callers must do

| Caller | Obligation |
|---|---|
| Explorer Web | Depend on the KFM port, pass governed inputs, and forward selection candidates to governed resolution |
| Shared UI | Render KFM-owned state/events without renderer casts or direct runtime dependencies |
| Other apps/packages | Use the same port or a separately accepted non-browser boundary; do not initialize a peer browser renderer |
| Tests/examples | Use fake/null ports unless they are package-owned integration tests under a later admitted runtime packet |
| Docs | Describe the boundary accurately; prose is not conformance proof |

[Back to top](#top)

---

## 7. Enforcement

### 7.1 Current conformance posture

Current checks provide useful bounded evidence but do not yet enforce the complete accepted boundary. The v6 readiness validator, app-local adapter-boundary test, package scaffold, smoke/performance harness, and workflow holds must be reconciled through later implementation work. Their current incompleteness does not reopen the architecture choice; it keeps conformance and runtime admission on `HOLD`.

### 7.2 Downstream gates

The governed transition order is:

1. **Architecture source transition** — merge ADR-0006, ADR-0007, and the matching index rows only.
2. **Dependency admission** — separately review exact version, artifact integrity, license, provenance, supply chain, package ownership, transitive closure, CSP/worker posture, package-manager resolution, and lockfile bytes.
3. **Implementation and consumer migration** — implement the port/adapter, inventory all acquisition modes, enforce the package boundary, migrate consumers, and migrate or retire the legacy CDN/global harness.
4. **Runtime readiness** — execute issue #2906's authenticated interactive/headless browser and long-session probes at the exact admitted dependency/toolchain state.
5. **Operational decisions** — treat release, deployment, promotion, public serving, and publication as separate governed transitions.

No later step may be inferred from an earlier one. A failed dependency, implementation, security, compatibility, or runtime gate blocks or reverses that downstream state without rewriting the accepted architecture history.

### 7.3 Required structural proof before runtime use

A later implementation packet must provide at least:

- one explicit package-internal adapter acquisition surface;
- manifest ownership only in `packages/maplibre/package.json`;
- repository-wide inventory of static/type/dynamic/CommonJS/re-export/worker/CDN/global/plugin/protocol acquisition;
- deterministic positive and negative fixtures with stable diagnostics;
- no raw renderer types in public declarations;
- fake/null-port consumer tests without MapLibre installed;
- explicit disposition of the app-local placeholder and the legacy harness;
- CI invocation over the real owning paths;
- rollback to the dependency-free scaffold.

### 7.4 Validation for this documentation-only transition

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

These checks prove only ADR/index coherence at the checked revision. They do not prove package conformance, dependency admission, runtime behavior, security, accessibility, release, deployment, or publication.

[Back to top](#top)

---

## 8. Consequences

### 8.1 Positive consequences

- One package owns renderer dependency and correction scope.
- Consumers remain testable and renderer-neutral.
- Raw runtime objects cannot silently become application contracts.
- Plugins, protocols, workers, and custom-layer integrations remain subordinate to one adapter seam.
- The known CDN/global divergence is explicit rather than normalized as an exception.
- Architecture can be accepted before implementation without implying that implementation exists.
- Dependency removal can restore the current scaffold without migrating public data or evidence contracts.

### 8.2 Costs and constraints

- The port must evolve deliberately as capabilities grow.
- Existing app-local checks and placeholders require migration.
- A complete acquisition validator is broader than a simple import grep.
- The legacy harness must be migrated or retired; it cannot remain a permanent parallel runtime.
- Renderer-specific optimizations must be expressed as reviewed KFM capabilities rather than raw-handle escape hatches.

### 8.3 Current operational effect

This revision changes only ADR-0006, ADR-0007, and their canonical index rows. It does not modify code, manifests, dependencies, lockfiles, tests, validators, fixtures, workflows, the legacy harness, runtime behavior, release state, deployment, publication, or repository settings.

[Back to top](#top)

---

## 9. Alternatives Considered

### 9.1 `packages/maplibre-runtime/` as a new active home — rejected

The repository already has `packages/maplibre/`, and no implementation benefit justifies a second writable package or a migration in this architecture-only packet.

### 9.2 App-owned or root-owned renderer dependency — rejected

App ownership would make Explorer the real acquisition authority; root ownership would make the repository coordination manifest a product dependency owner. Both contradict the accepted reusable package seam.

### 9.3 Direct app imports behind an `adapters/` folder — rejected

A directory name does not establish a single dependency seam. Direct imports would leak renderer types and create app-local acquisition authority.

### 9.4 Legacy CDN/global harness exception — rejected

The binding maintainer disposition explicitly chose prohibition. Test or performance intent does not exempt runtime acquisition from dependency ownership, integrity, network, correction, and rollback requirements.

### 9.5 Soft convention without structural proof — rejected

Review-only convention cannot reliably detect dynamic imports, re-exports, workers, globals, package drift, plugins, or protocol acquisition.

### 9.6 Network/RPC-isolated rendering — deferred

A future iframe, worker, service, or headless boundary may be useful for a distinct use case, but it does not remove the need for one KFM-owned port and one accepted dependency owner. A materially different browser-renderer authority requires a successor or scoped exception ADR.

[Back to top](#top)

---

## 10. Migration & Rollback

### 10.1 Architecture transition

This packet performs only the synchronized source/index status transition. It deliberately leaves the dependency-free package scaffold and every runtime surface unchanged.

### 10.2 Downstream migration obligations

Later packets must, in order, close dependency admission, implement the KFM port and package-owned adapter, migrate consumers, reconcile validators, migrate or retire the CDN/global harness, execute #2906, and then seek any operational authority separately.

### 10.3 Repository rollback

Before merge, close the draft PR or reset its branch. After merge, revert the three documentation changes through normal review if the status transition was erroneous. Reverting documentation does not uninstall a dependency or alter runtime because this packet adds none.

### 10.4 Architectural supersession

A later change to the package home, dependency owner, public seam, acquisition rule, or renderer-boundary model requires a successor or explicit amendment ADR with reciprocal index treatment. Accepted history must not be rewritten through an implementation PR.

### 10.5 Implementation rollback baseline

The current dependency-free `packages/maplibre/` scaffold is the rollback baseline until a later dependency/implementation packet records a more specific target. Consumers must remain compilable/testable against a fake or null `MapRuntimePort` without MapLibre installed.

[Back to top](#top)

---

## 11. Open Questions

The architecture questions are closed. The following are downstream design or evidence questions and do not weaken acceptance:

| Question | State | Owning later packet |
|---|---|---|
| Exact TypeScript signatures and versioning for `MapRuntimePort` | `HOLD / NEEDS DESIGN` | Implementation and consumer-migration PR |
| Exact package-internal source module set behind `MapLibreAdapter` | `HOLD / NEEDS DESIGN` | Implementation and structural-enforcement PR |
| Exact `maplibre-gl` version, integrity, license, provenance, and lock closure | `NOT ADMITTED` | Dependency-admission PR |
| Admitted plugin/protocol/custom-layer set | `NONE ADMITTED` | Per-integration admission after ADR-0007 |
| Worker/CSP/browser support strategy | `HOLD` | Dependency and implementation review |
| App-local placeholder disposition | `HOLD` | Consumer-migration PR |
| Legacy harness migration versus retirement | `HOLD`; no exception | Separate implementation PR |
| Complete acquisition validator and reason codes | `HOLD` | Structural-enforcement implementation |
| Authenticated browser and long-session result | `HOLD` | Issue #2906 |
| Release, deployment, and publication | `NOT AUTHORIZED` | Separate governed operational decisions |

[Back to top](#top)

---

## 12. References

### 12.1 Decision and placement

- [Issue #2957 — MapLibre architecture governance](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957)
- [Canonical ADR index](./INDEX.md)
- [ADR-0007 — sole browser renderer](<./ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>)
- [ADR-0029 — Directory Governance Standard v2](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../doctrine/directory-rules.md)

### 12.2 Current implementation and held evidence surfaces

- [MapLibre package README](../../packages/maplibre/README.md)
- [MapLibre package manifest](../../packages/maplibre/package.json)
- [MapLibre package entry](../../packages/maplibre/src/index.ts)
- [Explorer placeholder adapter](../../apps/explorer-web/src/adapters/MapLibreAdapter.ts)
- [Map Runtime Boundary](../architecture/ui/MAP_RUNTIME_BOUNDARY.md)
- [Legacy smoke/performance harness](../../scripts/maplibre-smoke-perf.mjs)
- [MapLibre readiness validator](../../tools/validators/maplibre/validate_v6_readiness.py)
- [MapLibre performance workflow](../../.github/workflows/maplibre-perf-governance.yml)
- [Issue #2906 — browser/runtime readiness](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2906)

### 12.3 Change history

| Edition | Date | Disposition |
|---|---|---|
| `v1.3` | 2026-08-13 | Repository-grounded proposed decision and pre-acceptance evidence snapshot; preserved in Git history |
| `v1.4` | 2026-08-21 | Accepted architecture source transition authorized by issue #2957; no dependency, implementation, runtime, release, deployment, or publication effect |

---

_Last updated 2026-08-21 · Document version: v1.4 · Source metadata: `accepted` · Effective decision status: `accepted` · Implementation: dependency-free scaffold / `HOLD` · Publication effect: none · [Back to top](#top)_
