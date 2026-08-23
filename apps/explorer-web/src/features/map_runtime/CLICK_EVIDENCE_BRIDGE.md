# Renderer-neutral click-to-Evidence-Drawer bridge

**Status:** `CONFIRMED bounded implementation / fixture-only / no renderer dependency / no publication effect`

This slice connects a synthetic rendered-feature selection to the existing Evidence Drawer through an injected governed resolver. It proves the strict browser-side selection contract and finite evidence behavior without admitting MapLibre, activating a source, reading an internal lifecycle store, or creating release/publication authority.

## Implemented boundary

```text
synthetic feature selection
  -> strict kfm.explorer.map-feature-selection.v1 parser
  -> injected governed resolver
  -> Evidence Drawer strict projection parser
  -> ANSWER / ABSTAIN / DENY / ERROR
```

The selection contract contains only:

- `selection_id`
- `layer_id`
- `feature_id`
- `evidence_refs`

Unknown fields are rejected. IDs use a bounded portable grammar. Evidence references are unique and capped at 16. An empty evidence set returns `ABSTAIN / MISSING_EVIDENCE` without calling the resolver.

## Shared `MapRuntimePort` profile

The stable selection profile and internal `MapFeatureSelection` type now come from the dependency-free `@kfm/maplibre` package. Explorer Web imports that KFM-owned facade and re-exports the same symbols for compatibility; parsing, evidence-subset enforcement, and Evidence Drawer behavior remain app-owned.

The package also exposes a minimal renderer-neutral `MapRuntimePort` plus a deterministic `NullMapRuntime` for consumer migration and tests. The null runtime performs no DOM, WebGL, worker, protocol, plugin, tile, network, source, evidence, policy, release, model, deployment, or publication work. It is not a renderer and does not satisfy the authenticated browser probes in issue #2906.

Raw renderer acquisition remains prohibited outside `packages/maplibre/`. Importing the KFM-owned `@kfm/maplibre` facade is consumer use of the accepted port boundary, not dependency admission.

## Evidence-subset invariant

A returned drawer projection may cite only evidence references already declared by the clicked selection. If the resolver returns any additional reference, the bridge fails closed with:

```text
ERROR / DRAWER_EVIDENCE_OUTSIDE_SELECTION
```

Rendered properties are therefore request scope, never evidence, and the resolver cannot silently widen the clicked feature's evidence set.

## Finite failure behavior

| Condition | Outcome |
|---|---|
| Invalid or over-broad selection | `ERROR / SELECTION_INVALID` |
| No governed evidence reference | `ABSTAIN / MISSING_EVIDENCE` |
| Resolver throws | `ERROR / GOVERNED_RESOLVER_ERROR` |
| Resolver widens evidence scope | `ERROR / DRAWER_EVIDENCE_OUTSIDE_SELECTION` |
| Strict drawer returns a governed negative state | Existing `ABSTAIN`, `DENY`, or `ERROR` projection |
| Strict drawer returns supported evidence | `ANSWER / SUPPORTED` |

The bridge preserves the Evidence Drawer's current no-leak rules: denial and operational errors expose no evidence detail, unresolved citations cannot answer, and held/superseded/withdrawn/revoked evidence remains history rather than active claim support.

## Browser fixture

`mountMapFeatureEvidenceFixture(...)` renders ordinary buttons that behave as synthetic map clicks. The fixture provides:

- keyboard-native controls;
- deterministic focus behavior;
- an `aria-live` status region;
- stale-request suppression;
- clean listener and drawer teardown;
- no network or renderer import.

This is browser behavior evidence for the governed handoff, not proof of a real map renderer.

## Files and tests

- `apps/explorer-web/src/features/map_runtime/index.tsx`
- `packages/maplibre/src/map-runtime-port.ts`
- `packages/maplibre/src/null-map-runtime.ts`
- `apps/explorer-web/tests/map-runtime-port.test.ts`
- `apps/explorer-web/tests/map-evidence-bridge.test.ts`
- `apps/explorer-web/tests/browser/map-evidence-drawer.spec.ts`
- `apps/explorer-web/tests/browser/fixtures/map-evidence-bridge.html`
- `apps/explorer-web/tests/fixtures/map-evidence/*.json`
- `.github/workflows/map-evidence-bridge.yml`
- `.github/workflows/ui-build.yml`
- `tools/validators/maplibre/assess_acquisition_inventory.py`
- `tests/maplibre/test_assess_acquisition_inventory.py`

The test matrix covers supported evidence, missing evidence, policy denial, upstream error, evidence-scope widening, stale request suppression, keyboard use, accessibility status, and teardown. The shared-port tests additionally cover deterministic initialization, KFM-owned selection events, invalid camera/selection rejection, and idempotent disposal.

## Explicit non-effects

This implementation does **not**:

- import or admit `maplibre-gl`;
- select or authenticate a MapLibre version;
- satisfy issue #2906 browser or long-session readiness;
- activate live sources or retrieve live payloads;
- read RAW, WORK, QUARANTINE, or PROCESSED stores;
- resolve evidence directly in browser code;
- turn feature properties into evidence;
- alter policy, review, lifecycle, release, deployment, publication, or repository settings.

## Follow-up boundary

A later renderer implementation may translate a real click event into the same strict selection shape only after the package-owned concrete `MapLibreAdapter` and exact dependency-admission packet are separately reviewed. The next bridge must preserve:

1. released-layer input only;
2. stable feature identity;
3. governed evidence references;
4. evidence-subset enforcement;
5. keyboard and pointer parity;
6. explicit stale/withdrawn/correction behavior;
7. teardown and state restoration;
8. rollback to the dependency-free `NullMapRuntime` consumer seam.

Until then, the current slice remains a bounded fixture-first trust proof, not a renderer integration or publication path.
