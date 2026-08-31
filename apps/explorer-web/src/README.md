<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/explorer-web/src/readme
title: Explorer Web Source Tree README
type: app-readme
version: v0.4
status: draft
owners: OWNER_TBD — Apps steward · UI steward · Map steward · Governed API steward · Policy steward · Docs steward
created: 2026-06-16
updated: 2026-08-31
policy_label: public
related:
  - ../README.md
  - ../../README.md
  - ../../governed-api/README.md
  - ../../review-console/README.md
  - ../../../docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - ../../../docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - ../../../docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - ../../../packages/ui/README.md
  - ../../../packages/maplibre/README.md
  - ../../../packages/cesium/README.md
  - ../../../policy/access/README.md
  - ../../../policy/decision/README.md
  - ../../../release/README.md
  - ../../../data/README.md
tags: [kfm, apps, explorer-web, src, map-first, public-ui, governed-api, evidence-drawer, focus-mode, renderer-boundary]
notes:
  - "v0.4 records the exact-one same-origin governed map/evidence transport, package-owned inline MapLibre runtime, identity-preserving selection, and Null fallback while preserving broader readiness and production holds."
  - "Repository evidence confirms bounded local and fixture-first implementation slices plus one same-origin governed map/evidence integration; it does not establish a production route tree, broader source admission, deployment, release, or publication."
  - "The package-owned MapLibre adapter renders the exact-one synthetic slice with Null fallback; broader MapLibre readiness remains HOLD."
  - "src/ is the app implementation source-layout boundary only; it must not become a public API, lifecycle data store, policy root, release authority, schema/contract home, model-runtime surface, or shared package root."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# Explorer Web Source Tree

`apps/explorer-web/src/`

**Source-layout boundary for the map-first Explorer Web app: route, shell, map, Evidence Drawer, Focus Mode, story, compare/export, settings, diagnostics, and governed-client implementation may live here while truth and authority stay elsewhere.**

![status](https://img.shields.io/badge/status-draft-blue)
![owner](https://img.shields.io/badge/owner-OWNER__TBD-lightgrey)
![layout](https://img.shields.io/badge/layout-src%2F-0a7ea4)
![app](https://img.shields.io/badge/app-explorer--web-2ea44f)
![truth](https://img.shields.io/badge/truth-bounded__implementation-0969da)

[Purpose](#1-purpose) · [Repo fit](#2-repo-fit) · [Boundary](#3-authority-boundary) · [Inputs](#5-inputs) · [Exclusions](#6-exclusions) · [Module map](#7-current-source-map) · [Definition of done](#14-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / bounded implementation
> **Owners:** `OWNER_TBD` — Apps steward · UI steward · Map steward · Governed API steward · Policy steward · Docs steward  
> **Path:** `apps/explorer-web/src/README.md`  
> **Responsibility root:** `apps/` — deployable application surfaces  
> **Truth posture:** CONFIRMED repository-grounded local composition, app-local adapters and feature slices, exact-one governed map/evidence transport, package-owned renderer and Null fallback, deterministic fixtures, and positive/negative tests / HOLD broader renderer readiness and general trust-bearing transport / UNKNOWN deployment and public operation

> [!CAUTION]
> Code under `apps/explorer-web/src/` must not directly read lifecycle data roots, canonical/internal stores, direct model runtime outputs, or local source files as user-facing truth. Claim-bearing UI should render only governed API envelopes, released or bounded-safe layer artifacts, EvidenceBundle-derived payloads, and finite states.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Repo fit](#2-repo-fit)
- [3. Authority boundary](#3-authority-boundary)
- [4. Default posture](#4-default-posture)
- [5. Inputs](#5-inputs)
- [6. Exclusions](#6-exclusions)
- [7. Current source map](#7-current-source-map)
- [8. Diagram](#8-diagram)
- [9. Source-tree obligations](#9-source-tree-obligations)
- [10. Route and component expectations](#10-route-and-component-expectations)
- [11. Inspection path](#11-inspection-path)
- [12. Validation expectations](#12-validation-expectations)
- [13. Safe change pattern](#13-safe-change-pattern)
- [14. Definition of done](#14-definition-of-done)
- [15. Open verification items](#15-open-verification-items)

---

## 1. Purpose

`apps/explorer-web/src/` is the implementation source tree for the Explorer Web app.

It currently holds the default local entrypoint, repository-grounded site composition, boundary adapters, fixture-first feature modules, and bounded viewer templates for the map-first shell.

This README defines the source-tree boundary. The current implementation proves bounded local and synthetic interaction slices, including one same-origin `/layers` and `/evidence` integration through the package-owned inline MapLibre adapter with Null fallback. It does not prove a production route tree, general Governed API transport, arbitrary renderer/source admission, deployment wiring, release, publication, or public operation.

[Back to top](#top)

---

## 2. Repo fit

| Concern | Owning root | Expected relationship |
|---|---|---|
| Explorer Web source tree | `apps/explorer-web/src/` | Implementation source for the map-first shell |
| Parent Explorer app | `apps/explorer-web/` | Deployable public/semi-public UI boundary |
| Apps root | `apps/README.md` | Deployable app root and trust-membrane doctrine |
| Public trust membrane | `apps/governed-api/` | Normal data path for claim-bearing UI |
| Shared UI primitives | `packages/ui/` | Reusable components extracted from app source when shared |
| 2D renderer wrapper | `packages/maplibre/` | Renderer wrapper; app source should use adapter boundaries |
| Optional 3D wrapper | `packages/cesium/` | Conditional and gated 3D support |
| Policy gates | `policy/` | Access, sensitivity, rights, and decision policy |
| Release authority | `release/` | Publication, correction, rollback control |
| Lifecycle artifacts | `data/` | Receipts, proofs, registry, catalog, triplets, published artifacts |

## 3. Authority boundary

This source tree may implement UI behavior. It does not own source truth, policy, evidence, release, lifecycle, renderer, schema, or contract authority.

```text
apps/explorer-web/src/ = Explorer Web implementation source
apps/explorer-web/     = map-first public/semi-public app boundary
apps/governed-api/     = trust membrane and normal data path
packages/ui/           = shared UI primitives
packages/maplibre/     = 2D renderer wrapper
packages/cesium/       = optional gated 3D renderer wrapper
policy/                = finite policy decisions
schemas/               = machine-readable shape
contracts/             = object meaning
data/                  = lifecycle artifacts, receipts, proofs, registries
release/               = publication, correction, rollback authority
```

## 4. Default posture

Explorer Web source should fail safe and render finite bounded states rather than guessing.

A route, component, adapter, export flow, or map interaction should not render claim-bearing output when any of these are unresolved:

- governed API response shape;
- finite outcome envelope;
- EvidenceRef or EvidenceBundle support;
- citation validation;
- release or layer-manifest state;
- sensitivity, rights, and redaction obligations;
- source-role or provenance summary;
- valid-time semantics;
- rollback or correction status where relevant.

## 5. Inputs

| Input family | Examples | Required posture |
|---|---|---|
| API refs | governed endpoint, response envelope, validator, decision result | Runtime-validated before render |
| Route refs | Explore, Focus, Story, Compare, Export, Settings, Diagnostics | Explicit route contract |
| Layer refs | layer manifest, tile source, legend, trust badges, valid time | Released or bounded safe source only |
| Evidence refs | EvidenceRef, EvidenceBundle-derived payload, citation state | Required for claim-bearing views |
| Policy refs | sensitivity, rights, audience, redaction/generalization obligations | Preserved in route and export state |
| Renderer refs | map adapter, viewport, selected feature, tile status | Not treated as truth by itself |
| Export refs | selected layer, bounds, citations, redaction profile, output mode | Governed export only |

## 6. Exclusions

| Does not belong here | Correct home |
|---|---|
| Public API implementation | `apps/governed-api/` |
| Shared reusable UI components | `packages/ui/` |
| Renderer wrapper authority | `packages/maplibre/`, `packages/cesium/` |
| Policy bundles | `policy/` |
| Schemas and contracts | `schemas/contracts/v1/`, `contracts/` |
| Lifecycle artifacts, receipts, proofs, catalog, triplets | `data/` |
| Release manifests, rollback cards, correction notices | `release/` |
| Admin-only operations | `apps/admin/` |
| Steward review authority | `apps/review-console/` and review governance lanes |
| Source connectors | `connectors/` |
| Direct model runtime behavior | `runtime/` behind governed API only |
| Secrets, credentials, tokens, private keys | Secret manager / deployment environment, not app source |

## 7. Current source map

| Current area | Verified repository responsibility | Maturity limit |
|---|---|---|
| `main.ts` | Mounts the Explorer site, bounded same-origin governed map transport, package-owned Vite adapter, public workspace navigation, shared trust surface, and synthetic Focus workspace. | Bounded local composition; not a production router, arbitrary source loader, deployment, release, or publication path. |
| `site/` | Implements Map, Knowledge, Features, and Trust regions, anchor navigation, conservative catalogs, URL context, trust-state primitives, and synthetic workspace composition. | Synthetic/local inputs do not establish live data, authentication, evidence authority, or public operation. |
| `adapters/` | Contains defensive projections and the byte-bounded, abortable same-origin `/layers` and `/evidence` transport for the exact-one synthetic slice. | This narrow transport is not a general production API client, policy engine, or source loader. |
| `features/` | Contains bounded modules for shell, evidence, Focus, map runtime, story, compare, export, settings, diagnostics, read-only review, trust, time, and additional fixture-first projections. | A module and its tests prove only that slice; most modules are not composed as production routes or backed by live services. |
| `viewer_templates/` | Contains deterministic JSON style templates for default, compare, review, and story views. | Templates are not released layer manifests, admitted renderer configuration, or publication authority. |

No production router or arbitrary renderer/source adapter tree is present. The bounded synthetic transport and package-owned inline renderer are intentionally narrower; broader work remains subject to accepted contracts, admission, tests, and the app boundary.

## 8. Diagram

```mermaid
flowchart TD
    src["apps/explorer-web/src/"] --> app["app shell + routes"]
    app --> client["governed client + validators"]
    client --> api["apps/governed-api"]
    app --> map["map adapter boundary"]
    map --> ml["packages/maplibre"]
    map -. gated .-> cz["packages/cesium"]
    app --> ui["packages/ui"]
    api --> envelope{"ANSWER / ABSTAIN / DENY / ERROR"}
    envelope --> evidence["Evidence Drawer / finite state"]
    src -. DENY .-> data["direct lifecycle data reads"]
```

## 9. Source-tree obligations

| Obligation | Example effect |
|---|---|
| `governed_api_only` | Claim-bearing UI data comes through governed API envelopes |
| `runtime_validation_required` | API responses validate before render |
| `evidence_required` | Feature details and claims link to EvidenceBundle-derived payloads |
| `redaction_preserved` | UI never re-expands redacted/generalized details |
| `renderer_boundary_preserved` | Renderer APIs stay behind adapter/wrapper modules |
| `finite_states_required` | Routes render answer, abstain, deny, error, hold, and restricted states safely |
| `safe_export_required` | Export preserves citations, redaction, rights, and release constraints |
| `accessibility_required` | Keyboard, focus, contrast, skip-link, and status-announcement behavior stays testable |

## 10. Route and component expectations

Every long-lived route, panel, adapter, or component group should document or encode:

- route or component purpose;
- governed API endpoint or envelope family used;
- expected finite outcomes;
- evidence/citation display behavior;
- sensitivity, rights, and release-state display behavior;
- redaction/generalization behavior;
- loading, empty, deny, abstain, error, hold, and restricted states;
- export behavior, if any;
- tests or fixtures proving trust-membrane behavior.

## 11. Inspection path

The repository inventory and bounded synthetic integration are directly inspectable; broader production integration and deployment remain `NEEDS VERIFICATION`.

```bash
find apps/explorer-web/src -maxdepth 6 -type f | sort
find apps/explorer-web/tests tests/policy fixtures -maxdepth 6 -type f 2>/dev/null | grep -Ei 'explorer|map|layer|evidence|focus|story|compare|export|diagnostic|governed|maplibre' | sort
pnpm --filter explorer-web build
pnpm --filter explorer-web test
python -m pytest -q tests/policy/test_explorer_web_adapter_boundary.py
```

## 12. Validation expectations

Useful validation for this source tree should cover:

- no imports or fetches from lifecycle data roots;
- all claim-bearing requests use the governed API client;
- response validators reject unknown or malformed envelopes;
- finite outcomes render safe UI states;
- map feature clicks call governed claim/evidence resolution;
- Evidence Drawer cannot invent unsupported claims;
- redaction/generalization cannot be reversed client-side;
- export flows require citation, redaction, rights, and release support;
- renderer imports stay inside accepted adapter/wrapper boundaries.

## 13. Safe change pattern

For source changes under `apps/explorer-web/src/`:

1. Update route inventory and expected finite outcomes.
2. Add tests for answer, abstain, deny, error, hold, restricted, loading, and empty states.
3. Check governed API and renderer import boundaries.
4. Move reusable UI primitives to `packages/ui/` when shared.
5. Update this README and parent `apps/explorer-web/README.md` when public behavior changes.

## 14. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [x] The bounded `src/` entrypoint and package build/test scripts are confirmed.
- [x] The no-input `ABSTAIN` and supplied-input `ERROR` paths are tested without reflecting supplied input.
- [x] The current `site/`, `adapters/`, `features/`, and `viewer_templates/` inventory and maturity limits are documented.
- [x] Bounded Evidence Drawer, Focus, layer catalog, export, diagnostics, trust, time, story, and map-runtime slices have app-local tests.
- [x] A policy test constrains renderer imports and direct internal-store path literals.
- [x] Keyboard and browser checks cover bounded implemented surfaces.
- [ ] A production route inventory and router are implemented and tested.
- [x] Bounded same-origin `/layers` and `/evidence` transport and strict runtime response validation are implemented and tested.
- [x] The package-owned renderer dependency and functional inline Point/circle adapter slice are admitted and tested.
- [ ] Broader production transport and general renderer/source/layer/style admission are verified.
- [ ] Deployment, authentication, CSP, operations, release, and public availability are verified from current evidence.

## 15. Open verification items

| Item | Why it matters |
|---|---|
| Commission a production route inventory and router | Required before describing the local composition as a production application |
| Extend beyond the bounded Governed API transport | Required before claiming general authenticated or production trust-bearing integration |
| Verify broader renderer readiness and admission | The inline Point/circle slice is functional; arbitrary sources, layers, styles, protocols, and operational readiness remain held |
| Graduate bounded export behavior | App-local behavior is not proof of a public download or released artifact path |
| Verify deployment, authentication, CSP, and operations | Required before any public-availability claim |
| Confirm legacy shell roots | Required to prevent parallel shell drift |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The target file began as an empty placeholder. Earlier README versions correctly established the `src/` boundary but later became stale as `site/`, `adapters/`, `features/`, `viewer_templates/`, and their tests were added.

This version records those bounded repository facts without promoting the exact-one transport and renderer slice into claims about a production router, general transport, arbitrary renderer/source admission, deployment, release, publication, or public operation.

</details>

## Status summary

`apps/explorer-web/src/` holds a buildable, repository-grounded local composition and multiple fail-closed, fixture-first feature slices, including one exact-one governed MapLibre/evidence path. It must not be described as a production map application until the broader route, transport, renderer-admission, deployment, release, and public-operation gates are verified.

It must stay downstream of governed APIs, policy decisions, EvidenceBundle closure, release state, correction/rollback controls, and renderer adapter boundaries without becoming source truth, release authority, policy authority, lifecycle store, schema/contract home, model-output surface, or parallel shell authority.

<p align="right"><a href="#top">Back to top</a></p>
