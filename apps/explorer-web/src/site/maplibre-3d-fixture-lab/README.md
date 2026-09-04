# Synthetic MapLibre 3D fixture lab

Status: **branch-only, disabled by default, synthetic-only, not released, not deployed**.

This directory owns the Explorer composition for a bounded MapLibre 3D implementation proof. It is activated only when the Explorer URL contains:

```text
?kfm-maplibre-3d-fixture=1
```

The default Explorer path does not import or mount the lab.

## What the lab proves

When the browser and WebGL2 support it, the lab exercises the package-owned `@kfm/maplibre/vite-adapter` seam with:

- an inline GeoJSON source containing three generalized synthetic polygons;
- a `fill-extrusion` layer;
- Mercator/globe projection switching;
- bounded pitch, bearing, and vertical-field-of-view controls;
- pointer selection through the rendered extrusion layer;
- an equivalent keyboard-accessible feature-selection path;
- feature-state highlighting;
- a synthetic `EvidenceRef` handoff;
- finite `READY`, `ERROR`, and `DISPOSED` behavior;
- same-page teardown on `pagehide`;
- no camera animation, with an additional reduced-motion CSS guard.

The visual extrusion heights are deliberately exaggerated display values. They are not measurements.

## What the lab does not prove

The lab does not admit or activate any source. It does not use external styles, tiles, glyphs, sprites, APIs, COG, PMTiles, MVT, DEM, raster-dem, LiDAR, 3D models, terrain, hillshade, service workers, telemetry, uploads, or live data.

It does not create an `EvidenceBundle`, catalog entry, proof, release manifest, promotion decision, public layer, deployment, or publication. Its `EvidenceRef` values are synthetic test handoffs only.

A successful render is browser implementation evidence for this fixture branch. It is not production-readiness evidence and does not supersede any MapLibre, release, source-admission, or publication gate.

## Responsibility roots

- `apps/explorer-web/src/site/` owns application composition and opt-in presentation.
- `packages/maplibre/` owns direct MapLibre acquisition, worker setup, renderer objects, inline style construction, and renderer teardown.

No application file imports `maplibre-gl` directly.

## Validation

Run with the repository-locked toolchain:

```bash
pnpm --filter @kfm/maplibre test
pnpm --filter explorer-web test:unit
pnpm --filter explorer-web build
pnpm --filter explorer-web test:browser
```

The browser test accepts the finite no-WebGL fallback but requires the lab to remain absent by default and prohibits cross-origin map/data requests.

## Rollback

Abandon or delete the feature branch. No migration, source cleanup, cache invalidation, release rollback, or deployment rollback is required because the lab is disabled by default and has no publication effect.
