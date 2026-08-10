<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://apps/explorer-web/features/view-registry-inspector
title: View Registry Inspector
type: feature-readme
version: v0.1.0
status: proposed; fixture-backed; read-only
owner: OWNER_TBD - Explorer and registry stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; public-safe-projection; no-network
owning_root: apps/
responsibility: bounded read-only presentation of a closed View Registry inspection projection
truth_posture: PROPOSED fixture-backed UI; production wiring and hosted exact-head results need verification
related:
  - ../../adapters/ViewRegistryInspectorProjection.ts
  - ../../../../../contracts/ui/view_registry_profile.md
  - ../../../../../fixtures/ui/view_registry_inspector_projection/README.md
  - ../../../../../docs/intake/exploratory/pass-32-view-registry-inspector-source-map.md
[/KFM_META_BLOCK_V2] -->

# View Registry inspector

Status: **fixture-first Explorer component; not production-wired**.

This feature adapts Pass 32 card `KFM-P32-FEAT-0004` into a read-only
maintainer surface for one already-governed View Registry projection. It can
show proposed route paths, delivery-contract classes, layer-manifest
references, rendering hints, performance-budget references, policy labels,
Evidence Drawer profile references, ReleaseManifest references, and the fixed
`PROPOSED_INACTIVE` activation state.

## Projection boundary

The app-local profile
`kfm.explorer.view-registry-inspector.public-safe.v1` accepts only:

- one finite outcome, status, and reason binding;
- a registry identity whose suffix matches the first 24 hex characters of its
  declared SHA-256 spec hash;
- one to 32 unique entries sorted by `view_id`;
- unique route paths;
- canonical governed-reference strings without store locators, lifecycle
  paths, or embedded-query markers;
- one to 16 unique, sorted layer-manifest references per entry;
- finite MapLibre renderer and protocol hints;
- separate access-policy, sensitivity-policy, evidence, release, and
  performance-budget references; and
- a canonical whole-second UTC evaluation time.

Only `READY / AVAILABLE / REGISTRY_READY` may carry registry detail. `HELD`,
`DENIED`, and `UPSTREAM_ERROR` projections must use null identity fields and an
empty entry array. Unknown fields, identity drift, duplicate routes, unsorted
entries or layers, a non-ready entry, direct-store markers, embedded queries,
and invalid time fail closed to fixed `ERROR` copy without reflecting input
detail.

## Authority boundary

The inspector is a projection consumer. It does not read the canonical View
Registry fixture, resolve STAC/DCAT/PROV/catalog references, query a graph or
store, fetch a layer, bind a route, render a map, evaluate policy, activate a
layer, approve review, sign an artifact, release, deploy, publish, or authorize
public use.

The surface exposes no link, button, callback, transport client, or mutation
seam. `READY` means only that the upstream closed projection selected that
finite state. It is not proof that referenced objects exist or are released.

## Placement

- `apps/explorer-web/src/adapters/` owns strict app-local parsing.
- `apps/explorer-web/src/features/view_registry_inspector/` owns fixed display
  behavior.
- `fixtures/ui/view_registry_inspector_projection/` owns synthetic examples.
- `apps/explorer-web/tests/` owns unit and browser proof.

These are existing responsibility roots under accepted ADR-0029 and Directory
Rules v2. The feature creates no parallel route, registry, catalog, policy,
evidence, release, deployment, or publication authority.

## Existing contract relationship

`contracts/ui/view_registry_profile.md` and its schema, validator, fixtures, and
tests already own proposed registry meaning and deterministic local
validation. That contract explicitly leaves the inspector UI out of scope.
This feature does not import its fixture as production data or replace its
validator. A future governed producer must validate a registry and emit this
exact public-safe projection.

## Production hold

Production wiring remains **HOLD** until UI, catalog, policy, performance,
evidence, release, and security stewards accept a projection producer and an
authenticated maintainer-only delivery path.

## Validation

The existing `ui-build` workflow runs the Explorer build, unit suite, and
headless-browser suite. Focused commands are:

```text
pnpm --filter explorer-web exec vitest run tests/view-registry-inspector.test.ts
pnpm --filter explorer-web exec playwright test --config=playwright.config.ts tests/browser/view-registry-inspector.spec.ts
pnpm --filter explorer-web build
```

## Rollback

Revert the adapter, feature, fixtures, tests, source map, and authoring receipt
together. This additive surface creates no route, registry, source, lifecycle,
policy, review, release, deployment, publication, or public-use state to
restore.
