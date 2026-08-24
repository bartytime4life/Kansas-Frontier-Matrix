# Renderer-neutral click-to-Evidence-Drawer bridge

**Status:** `CONFIRMED bounded implementation / fixture-only / no renderer dependency / no publication effect`

This slice connects a synthetic rendered-feature selection to the existing Evidence Drawer through an injected governed resolver. It proves the strict browser-side selection contract and finite evidence behavior without admitting MapLibre, activating a source, reading an internal lifecycle store, or creating release/publication authority.

## Implemented boundary

```text
synthetic feature selection
  -> strict kfm.explorer.map-feature-selection.v1 parser
  -> closed LayerManifest admission projection for the same layer_id
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

The stable selection profile and internal `MapFeatureSelection` type come from the dependency-free `@kfm/maplibre` package. Explorer Web imports that KFM-owned facade and re-exports the same symbols for compatibility; parsing, evidence-subset enforcement, and Evidence Drawer behavior remain app-owned.

The package also exposes a minimal renderer-neutral `MapRuntimePort` plus a deterministic `NullMapRuntime` for consumer migration and tests. The null runtime performs no DOM, WebGL, worker, protocol, plugin, tile, network, source, evidence, policy, release, model, deployment, or publication work. It is not a renderer and does not satisfy the authenticated browser probes in issue #2906.

Raw renderer acquisition remains prohibited outside `packages/maplibre/`. Importing the KFM-owned `@kfm/maplibre` facade is consumer use of the accepted port boundary, not dependency admission.

## Runtime selection binding

`runtime-evidence-binding.ts` closes the dependency-free event handoff between `MapRuntimePort` and the existing app-owned evidence bridge:

```text
MapRuntimePort selection event
  -> validate and freeze KFM-owned MapFeatureSelection
  -> translate to the strict external selection profile
  -> resolveMapFeatureEvidence(...)
  -> evidence-subset guard
  -> finite Evidence Drawer resolution
  -> consumer callback
```

The binding:

- accepts only a validated KFM-owned runtime selection;
- requires the supplied closed LayerManifest projection to return `PASS` for the selected `layer_id` before invoking the governed resolver;
- exposes the exact finite layer-admission result beside the Evidence Drawer result and maps non-`PASS` admission to a visible, no-leak `ABSTAIN`, `DENY`, or `ERROR` drawer state;
- still routes the selection through the existing strict parser rather than bypassing it;
- uses an injected governed resolver and performs no transport itself;
- suppresses a slower stale result when a newer selection arrives;
- observes KFM-owned runtime snapshots and invalidates unresolved evidence when
  the runtime leaves `READY`;
- prevents a late `ANSWER` from crossing a stale, denied, abstained, conflicted,
  degraded, withdrawn, rolled-back, or error transition;
- provides idempotent teardown that unsubscribes the runtime and invalidates pending results; and
- is proven with `NullMapRuntime`, not with a concrete renderer.

`NullMapRuntime.emitTrustState(...)` is a deterministic test/control-plane hook.
It clears the selected feature and publishes a frozen snapshot with a finite
KFM-owned reason code. It consumes an upstream state for continuity testing; it
does not decide evidence, policy, review, correction, release, or rollback.

This is a bounded consumer-integration proof. The current browser lab may continue to use deterministic controls until a separately reviewed concrete adapter translates real renderer events into the same port contract.

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
| Layer admission is held | `ABSTAIN / MISSING_EVIDENCE`; governed resolver not called |
| Layer admission is policy/security denied | `DENY / POLICY_DENIED`; governed resolver not called |
| Admitted projection names another layer or has an integrity mismatch | `ERROR / UPSTREAM_ERROR`; governed resolver not called |
| Layer admission input is invalid | `ERROR / UPSTREAM_ERROR`; governed resolver not called |
| No governed evidence reference | `ABSTAIN / MISSING_EVIDENCE` |
| Resolver throws | `ERROR / GOVERNED_RESOLVER_ERROR` |
| Resolver widens evidence scope | `ERROR / DRAWER_EVIDENCE_OUTSIDE_SELECTION` |
| Runtime leaves `READY` while resolution is pending | Pending result invalidated; no late drawer delivery |
| Runtime snapshot changes | A separate text-first status presenter exposes the exact KFM-owned state and reason without inferring evidence, policy, sensitivity, review, release, correction, rollback authority, or publication state |
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

`mountMapRuntimeTrustStatus(...)` subscribes to the same renderer-neutral port and keeps every finite runtime state visible through a stable `status` or `alert` region. Only `READY` is marked eligible to emit a candidate selection. Critical `DENIED`, `WITHDRAWN`, and `ERROR` states are assertive; other bounded states remain polite. The presenter uses fixed copy and exact reason codes, never raw renderer errors or upstream payloads.

## Files and tests

- `apps/explorer-web/src/features/map_runtime/index.tsx`
- `apps/explorer-web/src/features/map_runtime/runtime-evidence-binding.ts`
- `apps/explorer-web/src/features/map_runtime/runtime-trust-status.ts`
- `packages/maplibre/src/map-runtime-port.ts`
- `packages/maplibre/src/null-map-runtime.ts`
- `apps/explorer-web/tests/map-runtime-port.test.ts`
- `apps/explorer-web/tests/map-runtime-evidence-binding.test.ts`
- `apps/explorer-web/tests/map-runtime-trust-status.test.ts`
- `apps/explorer-web/tests/map-evidence-drawer.test.ts`
- `apps/explorer-web/tests/browser/map-evidence-drawer.spec.ts`
- `apps/explorer-web/tests/browser/map-evidence-drawer.fixture.ts`
- `apps/explorer-web/tests/browser/map-runtime-trust-status.spec.ts`
- `apps/explorer-web/tests/browser/map-runtime-trust-status.fixture.ts`
- `.github/workflows/ui-build.yml`
- `tools/validators/maplibre/assess_acquisition_inventory.py`
- `tests/maplibre/test_assess_acquisition_inventory.py`

The test matrix covers matching layer admission, held/denied/invalid admission, cross-layer manifest reuse denial, supported evidence, missing evidence, policy denial, upstream error, evidence-scope widening, stale request suppression, runtime trust-state invalidation, visible text-first runtime status, critical alert semantics, keyboard use, accessibility status, and teardown. Shared-port coverage additionally proves deterministic initialization, KFM-owned selection and snapshot events, strict runtime-to-evidence translation, invalid camera/selection/state rejection, selection clearing on negative state, stale-result suppression, and idempotent disposal.

## Explicit non-effects

This implementation does **not**:

- import or admit `maplibre-gl`;
- select or authenticate a MapLibre version;
- satisfy issue #2906 browser or long-session readiness;
- activate live sources or retrieve live payloads;
- assert that the fixture-only admission projection is a live registry lookup, release decision, or source registration;
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
