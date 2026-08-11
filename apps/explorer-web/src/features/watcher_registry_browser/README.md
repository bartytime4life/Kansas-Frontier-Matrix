<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://apps/explorer-web/features/watcher-registry-browser
title: Watcher Registry Browser
type: feature-readme
version: v0.1.0
status: proposed; fixture-backed; read-only
owner: OWNER_TBD - Explorer, watcher, and source stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; public-safe-projection; no-network
owning_root: apps/
responsibility: bounded read-only presentation of a closed Watcher Registry browser projection
truth_posture: PROPOSED fixture-backed UI; production wiring and hosted exact-head results need verification
related:
  - ../../adapters/WatcherRegistryBrowserProjection.ts
  - ../../../../../contracts/source/watcher_registry.md
  - ../../../../../control_plane/watcher_registry.json
  - ../../../../../fixtures/ui/watcher_registry_browser_projection/README.md
  - ../../../../../docs/intake/exploratory/pass-31-watcher-registry-browser-source-map.md
[/KFM_META_BLOCK_V2] -->

# Watcher Registry browser

Status: **fixture-first Explorer component; not production-wired**.

This feature adapts Pass 31 card `KFM-P31-FEAT-0019` into a read-only
maintainer surface for an already-governed Watcher Registry projection. It can
show watcher identity, canonical identity, version, inactive state, opaque
spec/endpoint/policy/schema/signature references, poll mode, output types,
reason codes, and declared spec hashes.

## Projection boundary

The app-local profile
`kfm.explorer.watcher-registry-browser.public-safe.v1` accepts only:

- finite available, abstain, deny, and error outcomes with paired reasons;
- the existing v1 Watcher Registry identity and `PROPOSED_INACTIVE` status;
- a canonical whole-second UTC evaluation time and SHA-256 registry binding;
- one to 128 unique entries sorted by `watcher_id`;
- unique canonical watcher identities;
- finite non-active watcher states and poll modes;
- opaque `kfm://` references rather than URLs or repository-store paths;
- sorted, unique output and reason-code arrays; and
- seven fixed-false governance flags.

Only `AVAILABLE / REGISTRY_AVAILABLE` may carry registry detail. Other
outcomes require null metadata and an empty watcher array. Placeholder entries
must be manual-only and carry no endpoint, policy, output, schema, or signature
claim. Unknown fields, entry-order drift, duplicate identity, unsafe
governance, active-state claims, and placeholder contradictions fail closed to
fixed error copy without reflecting input detail.

## Authority boundary

The browser consumes only a closed display projection. It does not import or
read `control_plane/watcher_registry.json`, inspect watcher specification
bytes, resolve references, dereference endpoints, schedule or execute a
watcher, activate a source, admit RAW data, classify material change, write a
receipt, evaluate policy, approve review, promote, release, deploy, publish, or
authorize public use.

The surface exposes no button, link, callback, transport client, persistence
store, or mutation seam. Displayed metadata is not proof that a watcher,
endpoint, source, signature, policy, schema, output, scheduler, or consumer is
active or valid.

## Placement

- `apps/explorer-web/src/adapters/` owns strict app-local parsing.
- `apps/explorer-web/src/features/watcher_registry_browser/` owns fixed display
  behavior.
- `fixtures/ui/watcher_registry_browser_projection/` owns synthetic examples.
- `apps/explorer-web/tests/` owns unit and browser proof.

These are existing responsibility roots under accepted ADR-0029 and Directory
Rules v2. No parallel watcher registry, source registry, policy, lifecycle,
receipt, release, deployment, or publication authority is created.

## Existing contract relationship

`contracts/source/watcher_registry.md`, its schema, control-plane projection,
validator, fixtures, tests, and workflow already own proposed registry meaning
and deterministic validation. This component neither replaces those controls
nor treats the control-plane JSON as a public API. A future governed producer
must emit the exact public-safe projection accepted here.

## Production hold

Production wiring remains **HOLD** until watcher, source, policy, security, UI,
and release stewards accept a projection producer and an authenticated
maintainer-only delivery route.

## Validation

The existing `ui-build` workflow runs the Explorer build, unit suite, and
headless-browser suite. Focused commands are:

```text
pnpm --filter explorer-web exec vitest run tests/watcher-registry-browser.test.ts
pnpm --filter explorer-web exec playwright test --config=playwright.config.ts tests/browser/watcher-registry-browser.spec.ts
pnpm --filter explorer-web build
```

## Rollback

Revert the adapter, feature, fixtures, tests, source map, and authoring receipt
together. This additive, unmounted surface creates no watcher, source,
lifecycle, policy, review, release, deployment, publication, or public-use
state to restore.
