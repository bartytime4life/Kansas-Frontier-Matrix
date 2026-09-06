# Earth-inspired Layer Library — dormant integration handoff

**2026-09-05 — M1 PARTIAL; branch authoring only.**
This is implementation guidance for the existing application, not a second
Explorer, a source-admission record, an approved workspace contract or a Site
publication. The parent [application README](../README.md) and
[shared UI source README](../../../packages/ui/src/README.md) retain their roles.

## Exact authoring scope

Delivery base: `cbd6d82bad962a58ab62cfb776ee31696b575107`.
Authoring started at `3d6b8a6e81ed65a726156feae67fa73875b5b069`; the four-commit
advance changed five non-overlapping paths in Explorer Web and an existing
generated receipt. This application, UI package, and governing inputs are unchanged.
This is a source-export check, not a complete-checkout integration test.
The source candidate is carried forward from
`KFM_Earth_Layer_Library_Candidate_2026-09-05.zip`, with its supplied SHA-256
manifest checked before editing. No prior test claim substitutes for a rerun.

The source files are:

- `packages/ui/src/layer-library-model.ts`, `layer-library-view.ts`, and `layer-library.css`;
- `app/site-layer-library-metadata.ts` and `app/site-layer-library.tsx` in this application;
- `tests/earth-layer-library.test.mjs` and `tests/earth-layer-library.browser.py`.

This branch does **not** change `app/page.tsx`, `app/layout.tsx`, dependencies,
lockfiles, build-script policy, MapRuntimePort, temporal kernel, KanPlan,
workflows, hosting configuration, source/data activation or existing snapshots.
The production entrypoint therefore does not expose the new Library yet.
The browser test is not a deployed app and must never be published as one.

The current source declares the existing Site project
`appgprj_6a870a079c1c8191abb7401ef092a181` and slug
`kansas-frontier-matrix-explorer`. Saved/deployed versions and live source equality
were not verified through a Sites tool. No Site version was saved or deployed.

## Behavior and important limits

Metadata comes from an already-disclosable projection. Catalog membership does
not authorize delivery. The generic model has independent disclosure, access,
rights, sensitivity, release, fixture, generalization and runtime axes.
Unknown authorization is not operational eligibility. Fixture previews require
an explicit mode choice. Metadata may remain discoverable for an unavailable
item only when the host explicitly permits disclosure.

The app projection accepts only eight previously inspected built-in fixtures:
`kansas-extent`, `water-context`, `watershed-context`, `prairie-context`,
`geology-context`, `elevation-concept`, `agriculture-context`, and
`atmosphere-observations`. It reads no geometry, per-feature attributes, renderer
descriptors or counts. Dataset/artifact versions stay unknown. All renderers
stay held; synthetic elevation is not terrain. Do not add production source IDs
to this fixture set as a shortcut to admission.

The existing year predicate supplies time matching. This is not the newer
shared temporal kernel, a second clock or irregular-time support. Bbox overlap
is a discovery hint, not a scientifically complete AOI query. The existing app
still bundles fixture geometry, so this does not close whole-app metadata/payload
separation. Fit, legends, styles, actual rendering order, new recipes, reports,
workspace migrations, live evidence resolution and Qwen remain outside this slice.

## Requested-state write protocol

`LibraryPort.write(next, expected)` is a synchronous compare-and-set for requested
layer state. The component checks the current state first, sends at most one
write, requires literal `true`, and reads back exact IDs, order, visibility and
opacity. Inputs are immutable detached snapshots. The finite outcomes are
`APPLIED`, `CONFLICT`, `UNCONFIRMED`, and `ERROR`; these are UI transaction results,
not policy or release decisions.

An acknowledgment without matching readback is not success. A host may mutate
and then throw: preserve the observed state, suppress raw error text, clear the
unconfirmed undo receipt and do not retry or compensate automatically. Read
failure disables mutation without treating unknown state as an empty workspace.
Disclosure revocation is still hidden even when the host refuses cleanup.

The React wrapper's new callback is:

```ts
onChange(next: SiteLibraryChange, expected: SiteLibraryChange): boolean
```

The wrapper updates its requested-state snapshot only after explicit host
acknowledgment. It updates its props reference in a layout effect, not during a
potentially abandoned render. These source changes do not prove React scheduling,
commit, paint or whole-application atomicity. Its hidden membership is session-local;
existing snapshots are not migrated or silently extended.

The source test runner also rejects implicit ambient compiler discovery through
`NODE_PATH`. Its default requires an app manifest/lock version match and an
explicit app/root `node_modules/typescript` candidate. Diagnostic fallback needs
`KFM_ALLOW_GLOBAL_TSC=1` and prints the actual version/path. Even a matching
installed version does not prove installation-byte integrity.

## Next safe integration action

Re-pin main and this branch; inspect overlapping work and current #4024/#4228
controls before editing. Do not apply the original ZIP's void `onChange` snippet:
it does not implement the new acknowledged protocol.

The previously inspected preimages were:

| Existing target | Git blob |
|---|---|
| `app/page.tsx` | `ab4c8d1f018ae4a62e61f6057a5efcbbafca1a91` |
| `app/layout.tsx` | `54d54efd9d3ca8a43824bdb1e91f46e32705b3bd` |

In a complete isolated checkout, retain the current page, map instance, camera,
all legacy controls and routes. Compose `SiteLayerLibrary` beside the existing
command-bar actions, passing the existing layer records, visibility, opacity,
order, analysis bounds, year and inspector callback. Import the scoped CSS
through the existing layout. Implement the callback through the host's current
state owner: compare expected touched values against actual current state,
apply both visibility and opacity together, preserve unrelated keys, acknowledge
only after acceptance, and ensure other writers cannot race a pending React update.
A boolean returned after two unexamined setters is not proof of that protocol.

Test the real host for rejected updates, later external edits, fast consecutive
changes, workspace restore, deferred rendering, focus return and Escape, Back/
Forward, camera preservation, hidden membership, catalog revocation and cleanup.
Keep unknown render groups fixed until effective package-owned order is proven.
Do not enable a renderer, source, release or public Site as a side effect.

M1 remains partial until that existing-app composition and changed-area checks
are verified. M2 renderer/delivery, M3 real-data source-to-report, and M4 richer
time/terrain/Qwen work are not delivered by this branch.

## Validation and evidence classes

Fresh diagnostics in the continuation run:

| Check | Result | Boundary |
|---|---|---|
| Original candidate Node suite | 37 passed | Rerun, not a main-branch test |
| Revised candidate Node suite | 47 passed | Explicit ambient TypeScript diagnostic |
| Original browser suite | 21 passed | Injected modules / synthetic host |
| Revised browser suite | 27 passed | Chromium DOM, not React/Vinext/GPU |
| Model/view/metadata strict TypeScript | Passed | TypeScript 5.8.3, not declared 7.0.2 |
| React wrapper | Syntax check only | Full React typing/runtime NOT_RUN |
| Lock-native app install/build/lint/tests | BLOCKED / NOT_RUN | No successful full checkout or locked toolchain |
| Native topology/receipt and hosted checks | NOT_RUN | No inherited-failure attribution or gate weakening |

Use the source test at repository root:

```bash
node --test apps/kansas-frontier-matrix-explorer/tests/earth-layer-library.test.mjs
```

For explicitly labeled diagnostic use only, prepend `KFM_ALLOW_GLOBAL_TSC=1`.
For the browser runner, compile the model/view/metadata with the repository's
TypeScript to an outside-repository CommonJS output folder, then pass
`--compiled-root` and `--output` explicitly. It needs Playwright and Chromium;
the `--chromium` argument selects an already-installed executable. It neither
installs dependencies nor starts a server. Do not relax browser security policy.

The final browser run records zero additional network requests and zero owned
DOM nodes after each of 50 teardown cycles. Coarse heap counters do not prove
memory stability. Timings are environment-specific metadata diagnostics; no FPS,
map latency, performance improvement or production budget is claimed.

## Placement, review and rollback

Adopted Directory Rules section 10.1 / DIR-EXEC-001 and accepted ADR-0029 place
reusable UI under `packages/` and this application's composition/tests/guidance
under its existing `apps/` lane. Types are UI interfaces, not new canonical
contracts or schemas. Generated-work accountability stays in the existing
`data/receipts/generated/` collection. No new root or parallel authority is created.

#4024 closed metadata is not qualifying evidence that its PR-state control path
is safe. Stop at branch-only delivery absent an independent permitted creator.
#4228 Stage 1B and Stage 2 remain held/unauthorized; `catalog/`, the correction
register and baseline are unchanged. No independent human approval is claimed.

Rollback the complete task commit after inspecting subsequent edits, or leave
it unintegrated. Because the entrypoints are unchanged, no Site rollback or
workspace deletion is necessary. A later integration must restore prior UI
without resurrecting revoked references or bypassing current policy. Preserve
correction and withdrawal history. There is no automatic rollback operation.
