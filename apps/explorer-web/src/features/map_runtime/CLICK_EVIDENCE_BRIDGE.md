# Map Feature Click to Evidence Drawer Bridge

## Status

| Field | Value |
|---|---|
| Implementation profile | `kfm.explorer.map-feature-selection.v1` |
| Repository role | Fixture-first app-local Map Runtime bridge |
| Authority | Candidate/request scoping only; no evidence, policy, release, or publication authority |
| Network posture | No network access in the feature module or default tests |
| Renderer posture | Renderer-neutral; no MapLibre dependency is admitted by this slice |
| Public state | Not released or published by this change |

## Goal

Implement the smallest safe slice behind the existing Map Runtime README's
`feature-click-resolver` plan: a rendered feature selection is converted into a
strict, renderer-neutral request scope, passed to an injected governed resolver,
and then rendered through the existing Evidence Drawer finite-state component.

This implements the source backlog item **ML-Y-113**, which calls for a
feature-click-to-`EvidenceBundle` fixture with visible `ABSTAIN` when evidence is
missing and `DENY` when policy blocks disclosure. The source is planning input;
current behavior is established only by the repository files and tests in this
slice.

## Boundary

The bridge accepts only:

- a closed selection object containing selection, layer, and feature identity;
- zero or more governed `EvidenceRef` identifiers that scope the request;
- an injected resolver that returns the existing public-safe Evidence Drawer
  projection.

The bridge does **not**:

- treat feature properties, pixels, geometry, or renderer state as evidence;
- fetch from a network, lifecycle store, canonical store, graph/index, object
  store, or model runtime;
- resolve `EvidenceRef` to `EvidenceBundle` inside the browser;
- evaluate policy, rights, sensitivity, review, or release state;
- admit MapLibre or another renderer dependency;
- promote, release, publish, correct, or roll back any KFM artifact.

## Finite behavior

| Condition | Bridge result | Drawer result |
|---|---|---|
| Valid selection and supported governed payload | `SUPPORTED` | `ANSWER` |
| Valid selection with no governed evidence reference | `MISSING_EVIDENCE` | `ABSTAIN` |
| Governed policy denial | existing governed reason code | `DENY` with fixed no-leak copy |
| Resolver failure | `GOVERNED_RESOLVER_ERROR` | `ERROR` with fixed no-leak copy |
| Drawer evidence falls outside selection scope | `DRAWER_EVIDENCE_OUTSIDE_SELECTION` | fail-closed `ERROR` |
| Malformed selection | `SELECTION_INVALID` | fail-closed `ERROR` |

Only `ANSWER` and evidence-bearing `ABSTAIN` projections may carry EvidenceRefs,
and every returned EvidenceRef must be a subset of the clicked selection's
allowed refs. The bridge never expands evidence scope.

## Files and tests

- `index.tsx` implements strict selection parsing, injected resolution,
  evidence-scope binding, finite local failures, and an accessible synthetic
  click fixture.
- `tests/map-evidence-drawer.test.ts` covers valid, invalid, missing-evidence,
  denied, out-of-scope, resolver-error, no-network, no-renderer-import, and
  no-lifecycle-path behavior.
- `tests/browser/map-evidence-drawer.*` proves keyboard-triggered selection,
  automatic drawer opening, focus entry, citation rendering, visible abstention,
  fixed policy-denial copy, evidence-scope rejection, and no-leak errors.

## Directory Rules basis

The implementation remains in the existing `apps/explorer-web/` deployable-app
boundary; tests remain in the existing app test lane. No new root, contract,
schema, policy, registry, proof, release, or publication authority is created.
The generated-work receipt is stored in the existing
`data/receipts/generated/` process-memory lane.

## Validation

The intended focused commands are:

```bash
cd apps/explorer-web
pnpm run build
pnpm run test:unit -- map-evidence-drawer.test.ts
pnpm run test:browser -- map-evidence-drawer.spec.ts
```

Repository-hosted checks remain the authoritative execution evidence for this
branch. A passing test proves only the bounded fixture and browser behavior; it
does not prove a live MapLibre integration, governed API route, evidence truth,
policy approval, release, deployment, or publication.

## Rollback

Before merge, close the draft pull request and leave the branch unmerged. After
an authorized merge, revert the implementation commit and its generated receipt,
then rerun the Explorer build, unit tests, and browser tests. No lifecycle data,
release state, cache, deployment, or external service requires reversal.

## Follow-up boundary

A later renderer-integration slice may translate a real MapLibre click event into
this same selection profile only after the MapRuntimePort and adapter import
boundary are verified. That later slice must not weaken the evidence-subset,
finite-outcome, no-public-raw-path, or fixed no-leak rules established here.
