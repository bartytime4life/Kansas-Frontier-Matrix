<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/maplibre-6-9-canary
title: MapLibre GL JS 6.9.0 Canary
type: runbook
version: v1
status: draft
owners: ["@bartytime4life"]
policy_label: public
related:
  - "docs/architecture/maplibre.md"
  - "configs/maplibre/perf-envelope.v1.json"
  - "packages/maplibre/package.json"
  - "apps/explorer-web/tests/browser/maplibre-vite-adapter.spec.ts"
notes:
  - "This document records a bounded dependency canary, not renderer readiness or release authority."
  - "Terrain, DEM, external sources, plugins, deployment, publication, and production Explorer activation remain out of scope."
[/KFM_META_BLOCK_V2] -->

# MapLibre GL JS 6.9.0 Canary

**Status:** CANDIDATE · draft · human review required

**Base:** `main@d25a4c046892aa826ca04da29215f8ae4aae8e51`

**Candidate branch:** `agent/maplibre-6-9-canary-20260912`

**Dependency change:** package-owned `maplibre-gl` `6.7.0 → 6.9.0`, with the corresponding pnpm lock closure.

**Upstream release:** [MapLibre GL JS v6.9.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.9.0)

## Purpose

This canary checks whether the package-owned Vite worker seam and isolated browser fixture remain compatible with MapLibre GL JS 6.9.0. The release is relevant to KFM because it changes terrain-drape scheduling, sprite loading, hidden-container sizing, style/terrain transitions, projection movement, GeoJSON update behavior, and `idle` timing.

This is compatibility evidence only. It does not admit a DEM, source, layer, protocol, plugin, public endpoint, or production renderer path.

## Implemented slice

- Exact dependency and lockfile update in `packages/maplibre`.
- Existing package unit-test surface retained.
- Existing local-only browser fixture retained.
- Added a browser scenario that creates the fixture in a hidden container, reveals it, and verifies a nonzero canvas size.
- Existing disposal, local-request, and WebGL2 fail-closed cases retained.

## Scenario disposition

| Scenario | Status | Boundary |
|---|---|---|
| Package adapter unit tests | NOT RUN in this session | Hosted/local runner must execute them |
| Vite worker boot and disposal | NOT RUN in this session | Existing isolated fixture |
| No external browser requests | NOT RUN in this session | Existing isolated fixture |
| WebGL2 unavailable | NOT RUN in this session | Existing fail-closed fixture |
| Hidden container reveal and resize | NOT RUN in this session | New canary browser case |
| Terrain-drape scheduling | NOT RUN | No admitted DEM or terrain source |
| `setStyle()` during DEM loading | NOT RUN | No admitted style-transition harness |
| Projection change during camera movement | NOT RUN | No terrain/projection canary harness |
| Queued GeoJSON property removal | NOT RUN | No admitted live GeoJSON update surface |
| Historical radar/smoke frame churn | NOT RUN | No source or animation activation |
| Frame-time/GPU-memory baseline | NOT RUN | Requires an approved benchmark methodology |

## Acceptance rule

The candidate may advance only if:

1. package, typecheck, unit, and browser checks pass at the exact branch head;
2. the browser fixture remains local-only and does not acquire external resources;
3. no existing fail-closed behavior regresses;
4. the remaining `NOT RUN` scenarios stay explicit;
5. a reviewer records promotion or hold separately from the implementation change.

A green fixture run does not prove terrain readiness, real-data readiness, release, deployment, or publication.

## Rollback

Revert the package manifest and lockfile to the prior `6.7.0` closure and remove the additive hidden-container browser case. No data, source registry, Site identity, deployment, or published artifact is changed by this canary.
