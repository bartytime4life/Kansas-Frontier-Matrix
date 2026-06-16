<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/explorer-web/src/adapters/readme
title: Explorer Web Adapters README
type: app-readme
version: v0.1
status: draft
owners: OWNER_TBD — Apps steward · UI steward · Map steward · Governed API steward · Policy steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../governed-api/README.md
  - ../../../../docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - ../../../../docs/adr/ADR-0006-maplibre-boundary-only-maplibreadapter-imports-maplibre.md
  - ../../../../docs/adr/ADR-0007-cesium-3d-is-conditional-and-gated.md
  - ../../../../docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - ../../../../packages/ui/README.md
  - ../../../../packages/maplibre/README.md
  - ../../../../packages/cesium/README.md
  - ../../../../policy/access/README.md
  - ../../../../policy/decision/README.md
  - ../../../../release/README.md
  - ../../../../data/README.md
tags: [kfm, apps, explorer-web, adapters, map-adapter, governed-client, renderer-boundary, maplibre, cesium, trust-membrane]
notes:
  - "Initial README for Explorer Web adapter source boundary."
  - "Repository evidence confirms this README path; adapter implementation files, imports, tests, fixtures, and runtime wiring remain NEEDS VERIFICATION."
  - "Adapters may translate between Explorer Web UI code and governed API or renderer ports, but they must not become source truth, policy authority, release authority, lifecycle storage, direct model surface, or renderer authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# Explorer Web Adapters

`apps/explorer-web/src/adapters/`

**Adapter boundary for Explorer Web integrations: governed API client adapters, map-runtime adapters, renderer bridges, evidence payload adapters, and safe export/diagnostic adapters.**

![status](https://img.shields.io/badge/status-draft-blue)
![owner](https://img.shields.io/badge/owner-OWNER__TBD-lightgrey)
![app](https://img.shields.io/badge/app-explorer--web-2ea44f)
![boundary](https://img.shields.io/badge/boundary-adapters-0a7ea4)
![truth](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)

[Purpose](#1-purpose) · [Repo fit](#2-repo-fit) · [Boundary](#3-authority-boundary) · [Inputs](#5-inputs) · [Exclusions](#6-exclusions) · [Adapter families](#7-adapter-family-map) · [Definition of done](#14-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owners:** `OWNER_TBD` — Apps steward · UI steward · Map steward · Governed API steward · Policy steward · Docs steward  
> **Path:** `apps/explorer-web/src/adapters/README.md`  
> **Responsibility root:** `apps/` — deployable application surfaces  
> **Truth posture:** CONFIRMED README path / PROPOSED adapter-boundary contract / UNKNOWN adapter files, imports, tests, fixtures, and runtime wiring

> [!CAUTION]
> Adapter code must not bypass the trust membrane. It may translate governed API envelopes, renderer ports, evidence payloads, layer manifests, and export requests into UI-friendly shapes, but it must not directly read lifecycle data roots, canonical/internal stores, raw renderer internals as truth, direct model output, or local source files as user-facing claims.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Repo fit](#2-repo-fit)
- [3. Authority boundary](#3-authority-boundary)
- [4. Default posture](#4-default-posture)
- [5. Inputs](#5-inputs)
- [6. Exclusions](#6-exclusions)
- [7. Adapter family map](#7-adapter-family-map)
- [8. Diagram](#8-diagram)
- [9. Adapter obligations](#9-adapter-obligations)
- [10. Adapter contract](#10-adapter-contract)
- [11. Inspection path](#11-inspection-path)
- [12. Validation expectations](#12-validation-expectations)
- [13. Safe change pattern](#13-safe-change-pattern)
- [14. Definition of done](#14-definition-of-done)
- [15. Open verification items](#15-open-verification-items)

---

## 1. Purpose

`apps/explorer-web/src/adapters/` is the proposed source boundary for Explorer Web adapter code.

Adapters should isolate integration details so route and component code can remain governed, testable, and renderer-agnostic. This directory may eventually contain adapter modules that translate:

- governed API response envelopes into route/view models;
- EvidenceBundle-derived payloads into Evidence Drawer state;
- layer manifests into map-layer configuration;
- map runtime events into governed feature-selection requests;
- MapLibre and optional Cesium ports into app-facing interfaces;
- export requests into governed export payloads;
- diagnostics and telemetry into safe, non-secret UI diagnostics.

This README does not prove those adapters are implemented.

[Back to top](#top)

---

## 2. Repo fit

| Concern | Owning root | Expected relationship |
|---|---|---|
| Explorer Web adapter source | `apps/explorer-web/src/adapters/` | App-local adapter modules, if implemented and tested |
| Explorer Web source tree | `apps/explorer-web/src/` | Parent source-layout boundary |
| Explorer Web app | `apps/explorer-web/` | Deployable map-first public/semi-public shell |
| Governed API | `apps/governed-api/` | Trust membrane and normal data path |
| Shared UI components | `packages/ui/` | Reusable UI primitives, not adapter authority |
| MapLibre wrapper | `packages/maplibre/` | Renderer wrapper boundary for MapLibre-specific behavior |
| Cesium wrapper | `packages/cesium/` | Conditional and gated 3D renderer wrapper |
| Policy gates | `policy/` | Access, sensitivity, rights, and decision policy |
| Release authority | `release/` | Publication, correction, rollback control |
| Lifecycle artifacts | `data/` | Receipts, proofs, registry, catalog, triplets, published artifacts |

## 3. Authority boundary

Adapters translate between boundaries. They do not own the truth, policy, evidence, release, lifecycle, schema, contract, or renderer authority that they consume.

```text
apps/explorer-web/src/adapters/ = app-local integration adapters
apps/explorer-web/src/          = Explorer Web implementation source
apps/governed-api/              = governed trust membrane
packages/maplibre/              = MapLibre renderer wrapper
packages/cesium/                = optional gated 3D renderer wrapper
packages/ui/                    = shared UI components
policy/                         = finite policy decisions
schemas/                        = machine-readable shape
contracts/                      = object meaning
data/                           = lifecycle artifacts, receipts, proofs, registries
release/                        = publication, correction, rollback authority
```

## 4. Default posture

Adapters should fail safe and return finite bounded states when integration support is unresolved.

An adapter should not emit claim-bearing UI state when any of these are missing or malformed:

- governed API envelope;
- response validator result;
- finite outcome;
- EvidenceRef or EvidenceBundle-derived payload;
- citation validation;
- sensitivity, rights, release, or redaction state;
- layer manifest or tile proof metadata;
- renderer adapter readiness;
- export citation and redaction support;
- safe diagnostic target.

## 5. Inputs

| Input family | Examples | Required posture |
|---|---|---|
| API envelope | answer, abstain, deny, error, decision envelope, evidence payload | Runtime-validated before adapting |
| Evidence payload | EvidenceRef, EvidenceBundle summary, citation state, proof visibility | Required for claim-bearing UI detail |
| Layer manifest | layer id, source role, release state, tile URL, legend, valid time, rights/sensitivity badges | Released or bounded safe source only |
| Renderer port | map runtime, feature id, viewport, interaction event, tile state | Never treated as truth by itself |
| Export request | bounds, selected layers, citation bundle, redaction state | Governed export only |
| Diagnostics payload | version, envelope status, route status, layer status, adapter health | Safe, non-secret, non-sensitive |

## 6. Exclusions

| Does not belong here | Correct home |
|---|---|
| Public API implementation | `apps/governed-api/` |
| Shared reusable UI primitives | `packages/ui/` |
| Renderer wrapper authority | `packages/maplibre/`, `packages/cesium/` |
| Policy bundles or policy decisions | `policy/` |
| Schemas and contracts | `schemas/contracts/v1/`, `contracts/` |
| Lifecycle artifacts, receipts, proofs, catalog, triplets | `data/` |
| Release manifests, rollback cards, correction notices | `release/` |
| Direct source acquisition | `connectors/` |
| Direct model runtime behavior | `runtime/` behind governed API only |
| Secrets, credentials, tokens, private keys | Secret manager / deployment environment |

## 7. Adapter family map

Exact adapter modules remain `NEEDS VERIFICATION`. Candidate families should be introduced only with tests and import-boundary checks.

| Candidate adapter | Responsibility | Status |
|---|---|---|
| `governedClientAdapter` | Normalize governed API calls and response validators | PROPOSED |
| `evidenceDrawerAdapter` | Convert evidence payloads into drawer view state | PROPOSED |
| `layerManifestAdapter` | Convert layer manifests into layer catalog/map state | PROPOSED |
| `mapRuntimeAdapter` | Convert UI map interactions into governed map/runtime events | PROPOSED |
| `maplibreAdapter` | Keep MapLibre-specific calls behind app-facing port | PROPOSED |
| `cesiumAdapter` | Conditional gated 3D bridge | PROPOSED |
| `exportAdapter` | Build governed export requests and safe export state | PROPOSED |
| `diagnosticsAdapter` | Convert safe diagnostics into UI diagnostic panels | PROPOSED |

> [!WARNING]
> Candidate names are not implementation proof. Do not document an adapter as runnable until files, imports, fixtures, and tests confirm it.

## 8. Diagram

```mermaid
flowchart TD
    routes["Explorer routes/components"] --> adapters["src/adapters"]
    adapters --> client["governed API adapter"]
    client --> api["apps/governed-api"]
    adapters --> evidence["evidence drawer adapter"]
    adapters --> layers["layer manifest adapter"]
    adapters --> map["map runtime adapter"]
    map --> ml["packages/maplibre"]
    map -. gated .-> cz["packages/cesium"]
    api --> envelope{"finite governed envelope"}
    envelope --> routes
    adapters -. DENY .-> data["direct lifecycle/canonical reads"]
```

## 9. Adapter obligations

| Obligation | Example effect |
|---|---|
| `governed_api_only` | Claim-bearing data is adapted only from governed API envelopes |
| `runtime_validation_required` | Unknown or malformed envelopes fail closed |
| `evidence_preserved` | Evidence and citation handles survive adaptation |
| `redaction_preserved` | Redacted/generalized details are never re-expanded |
| `renderer_boundary_preserved` | Renderer imports remain in approved adapter/wrapper locations |
| `finite_state_required` | Adapter output distinguishes answer, abstain, deny, error, hold, and restricted states |
| `safe_export_required` | Export adapters preserve citations, redaction, rights, and release constraints |
| `safe_diagnostics_required` | Diagnostics adapters never expose secrets or restricted internals |

## 10. Adapter contract

Every long-lived adapter should document or encode:

- source boundary it consumes;
- app-facing shape it returns;
- validator or schema/contract dependency;
- finite outcome handling;
- evidence/citation preservation;
- sensitivity, rights, and release-state behavior;
- redaction/generalization behavior;
- safe error behavior;
- tests or fixtures proving boundary behavior.

## 11. Inspection path

Adapter implementation files, import boundaries, tests, fixtures, client validators, renderer wrappers, and package scripts remain `NEEDS VERIFICATION`.

```bash
find apps/explorer-web/src/adapters -maxdepth 5 -type f | sort
find apps/explorer-web/src packages/maplibre packages/cesium packages/ui apps/governed-api tests fixtures -maxdepth 6 -type f 2>/dev/null | grep -Ei 'adapter|governed|maplibre|cesium|evidence|layer|export|diagnostic|validator' | sort
find data/raw data/work data/quarantine data/processed data/catalog data/triplets data/published -maxdepth 2 -type f 2>/dev/null | sort
```

## 12. Validation expectations

Useful validation for this adapter boundary should cover:

- no adapter imports or reads lifecycle data roots directly;
- claim-bearing adapters consume governed API envelopes only;
- malformed envelopes return safe error or abstain states;
- evidence drawer adapter preserves EvidenceRef/EvidenceBundle handles;
- layer adapter preserves release, source-role, sensitivity, rights, and valid-time state;
- map feature selection triggers governed claim/evidence resolution;
- renderer imports stay in approved adapter/wrapper modules;
- export adapter preserves citation, redaction, rights, and release constraints;
- diagnostics adapter redacts secrets and restricted internals.

## 13. Safe change pattern

For adapter changes:

1. Add or update fixtures for the boundary shape being adapted.
2. Add tests for answer, abstain, deny, error, hold, restricted, malformed, and empty states.
3. Check renderer and data-root import boundaries.
4. Preserve evidence, citation, policy, and release fields in adapted output.
5. Update this README and parent `src/`/app READMEs when adapter behavior changes.

## 14. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Adapter file inventory is documented.
- [ ] Governed API adapter and validators are implemented and tested.
- [ ] Renderer imports are confined to accepted adapter/wrapper modules.
- [ ] Evidence, citation, release, rights, sensitivity, and redaction fields survive adaptation.
- [ ] Direct lifecycle-data import/read checks are covered.
- [ ] Export and diagnostics adapters are tested for safe output.
- [ ] Malformed and unresolved inputs produce finite safe states.

## 15. Open verification items

| Item | Why it matters |
|---|---|
| Confirm adapter implementation files beyond README | Prevents overclaiming adapter maturity |
| Confirm governed API client adapter shape | Required for trust membrane enforcement |
| Confirm renderer adapter modules and imports | Required for MapLibre/Cesium boundary discipline |
| Confirm fixtures and tests | Required before implementation claims |
| Confirm export adapter behavior | Required before public download claims |
| Confirm diagnostics redaction | Prevents secret or restricted-internal leakage |
| Confirm package scripts beyond TODO | Required before build/test claims |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The target file was an empty placeholder. This README adds a bounded adapter-directory contract without claiming governed API adapters, renderer adapters, evidence adapters, layer adapters, export adapters, diagnostics adapters, tests, fixtures, imports, package scripts, or runtime wiring are implemented.

</details>

## Status summary

`apps/explorer-web/src/adapters/` should contain app-local adapters only after adapter files, import boundaries, fixtures, and tests are verified.

It must preserve the trust membrane and renderer boundary: adapters translate governed API envelopes, evidence payloads, layer manifests, renderer ports, and export/diagnostic requests without becoming source truth, release authority, policy authority, lifecycle store, schema/contract home, model-output surface, or renderer authority.

<p align="right"><a href="#top">Back to top</a></p>
