# Explorer composition shell

This directory contains the repository-grounded composition layer for the KFM Explorer site.

## Scope

The composition:

- replaces the minimal default page with a map-first, trust-visible landing shell;
- inventories the current Explorer feature families and their conservative maturity state;
- exposes the thirteen domain families already represented under `src/features/domains/`;
- presents KFM's evidence, finite-outcome, time, correction, accessibility, and trust-membrane principles;
- mounts the existing renderer-neutral `map_runtime` selection-to-Evidence-Drawer bridge with deterministic synthetic cases;
- mounts the existing finite `MapRuntimePort` trust-status presenter in the normal map workspace through the dependency-free `NullMapRuntime`;
- mounts the package-owned MapLibre adapter with an inline-only site-local style and no external resources;
- presents 18 typed default-view records, 24 typed layer/evidence records, explicit data holds, a Source Observatory with 15 repository candidates, deep-time preview/commit, and draft-only report/story capture;
- projects its existing public anchors through a code-owned workspace registry;
- builds the fixed illustrative SVG stage with namespace-aware DOM nodes and text content rather than parsing an HTML string; and
- composes existing finite-state features into one text-first public trust surface.

## DOM safety boundary

The retained illustrative map is a fixed browser composition, not an HTML template. It creates SVG nodes in the SVG namespace, sets attributes individually, and assigns visible labels through text content. Keep dynamic trust-bearing material out of this helper; evidence and state continue through typed, text-first projections. This legacy laboratory does not establish a governed data path.

## Unified Workspace UI-01 bounded slice

The first Unified Workspace implementation slice is intentionally public, no-network, and composition-owned:

- `workspace-registry.ts` defines the four existing public workspace destinations and binds them to the current `#map`, `#knowledge`, `#features`, and `#trust` anchors.
- `workspace-navigation.ts` mounts those descriptors into the existing shell without creating routes or privileged actions.
- `workspace-context.ts` defines a strict UI-owned public context projection for workspace, domain, place, released-layer IDs, renderer-neutral camera and selection, material time, compare references, and story position.
- The context parser reuses `@kfm/maplibre` camera and selection validators, rejects extra fields, requires `publicSafe: true`, and keeps URL context synchronized with the compatible workspace hash.
- Evidence references remain available for bounded in-memory context transfer, but URL serialization and parsing reject any selection that carries them because this browser-owned projection cannot prove release or access eligibility. Shareable links retain the public selection identifier; a governed interface must resolve admissible evidence after navigation.
- Unit and browser tests cover registry integrity, feature references, deterministic URL round-trip, evidence-reference exclusion, malformed/oversized/duplicated context, public-safety exclusions, hash mismatch, and rendered anchor navigation.

UI-01 is a bounded browser-composition contract. It is not a canonical semantic contract, source registry, policy rule, evidence object, review decision, release record, deployment record, or publication artifact.

Implementation baseline for UI-01: `main@f732cbd1003898dc765a7afe4b635d710e295d17`.

## Public workspace temporal validation repair

The repair reviewed from `main@47de77deb845bbba948c66566d9b88696cb14f8b`
keeps the existing context profile, fields, and URL parameter. It tightens
calendar validation rather than adding a new clock or changing source authority.

`validAt`, `observedAt`, and `asOf` must preserve a real written calendar date
and clock. Invalid dates such as February 30, non-leap February 29, and `24:00`
fail closed before context parsing, URL serialization, query parsing, URL
construction, or the temporal adapter can accept them. The adapter returns
`ERROR / PUBLIC_CONTEXT_INVALID` with no state for such a context. Validation
checks the written local fields before applying an offset; otherwise a valid
cross-midnight offset could be confused with an invalid calendar rollover.

JavaScript parsing alone is not this application's validation contract:
[ECMAScript's date format](https://tc39.es/ecma262/2025/multipage/numbers-and-dates.html#sec-date-time-string-format)
permits `24:00` and expanded years. This KFM adapter's existing instant grammar
uses four-digit years and its calendar round-trip excludes `24:00`. If a valid
numeric offset would normalize outside that grammar, the adapter now returns
`UNSUPPORTED / NORMALIZED_YEAR_OUT_OF_RANGE` with no state rather than slicing
an expanded year into a malformed supported timestamp.

Valid raw date strings, offsets, and one-to-nine fractional digits remain
unchanged in public URLs. Date-only selections remain `date_only` with
`normalized: null`; the validation-only midnight probe is never emitted as an
observation. The existing `-00:00` raw-link preservation and adapter
`UNSUPPORTED / UNKNOWN_TIMEZONE` outcome remain unchanged. A date-only knowledge
cutoff still returns `AS_OF_REQUIRES_ZONED_INSTANT`. This repair does not add
expanded-year, geologic-time, leap-second, source-admission, or release support.

The [new regressions](../../tests/workspace-context-temporal.test.ts) cover all
three time fields at the context and URL boundaries, leap/century rules,
malformed offsets, precision retention, year-boundary normalization, and the
existing unsupported outcomes. Run them alongside the original workspace tests
from `apps/explorer-web/` using the repository's locked dependencies:

```bash
pnpm exec vitest run tests/workspace-context.test.ts tests/workspace-context-temporal.test.ts
```

Local authoring evidence is deliberately narrower: the exact source and new
assertions were exercised in an isolated Node 22.16.0 harness, using TypeScript
5.8.3 transpilation and explicit test doubles for unrelated imports. All 130
cases passed in UTC, America/Chicago, and Pacific/Auckland. The unchanged source
failed 42 cases; removing only the calendar guard failed 36, and removing only
the expanded-year guard failed six. These are not pinned Vitest, real MapLibre,
state-identity conformance, browser, hosted CI, build, or deployment results;
those checks and independent review remain required before integration.

Design traceability: the
[Living Atlas Drive design](https://docs.google.com/document/d/1aivNyfMjQ8urQO6vjt4YvkT1ltF1t7fxCahEcnGV4Dw/edit)
and [Notion real-data hub](https://app.notion.com/p/3d6a92021bf6816cae0ec1ccbd15e21e)
require truthful, synchronized time across map, evidence, workspace, and export.
They are design inputs, not proof of implementation or release. This change is
limited to the repository's `apps/explorer-web` composition; it does not update,
synchronize, deploy, or publish the separate saved ChatGPT Site source.

Rollback this repair by reverting the two validation guards, the new regression
file, and this section together. No data or dependency migration is involved.

## Unified Workspace UI-02 bounded slice

UI-02 adds the smallest app-local shared trust grammar without moving component ownership or creating a new authority root:

- `trust-state-primitives.ts` strictly validates and renders the same visible labels for outcome, evidence, freshness, coarse sensitivity, release, and correction.
- `trust-surface.ts` composes the existing Trust Header, Time Banner, Citation Pill, Evidence Drawer, and Denial Reason Explorer around deterministic supported, unresolved, restricted, stale, error, and loading cases.
- Extra or inconsistent trust-state metadata fails closed to fixed error copy. The primitive never reflects unknown fields.
- The `LOADING` case is explicitly a transient browser condition, not a governed finite outcome or evidence/release claim.
- Coarse sensitivity values are already-supplied presentation metadata. The browser does not infer sensitivity or evaluate policy.
- Negative cases suppress citation and time affordances, retain text labels rather than color-only signals, and expose no override, approval, promotion, or publication action.
- Multiple Evidence Drawer mounts allocate document-unique panel, label, and title IDs while preserving the original IDs for the first compatible instance.
- Evidence Drawer `ERROR` views suppress release and correction labels when a resolver failure prevents a reliable user-facing interpretation; policy and freshness cues remain visible.
- Unit and browser tests verify the shared six-label grammar, alignment with the existing strict governed projection, loading separation, malformed-input denial, no-network behavior, keyboard-operable case selection, unique accessible drawer relationships, error-detail suppression, and absence of privileged controls.

UI-02 remains under `apps/explorer-web/src/site/` because it has one verified consumer: the Explorer composition. `packages/ui/` remains the future extraction home if another application requires the primitive. This follows the existing app-source and shared-package responsibility boundaries rather than creating a parallel UI root.

Implementation baseline for UI-02: `main@4671f53533cbb1c0757c01d4f90ae60733d544e8`.

Reconciliation baseline for the current UI-02 branch: `main@265b99b81f9526a885caaf799e17c89b5424f9f2`. The reconciliation preserves the separately merged synthetic Focus Mode request surface and repairs shared Evidence Drawer identity and error-state presentation without granting new authority.

## Evidence snapshot

The website feature catalog is refreshed against:

- repository: `bartytime4life/Kansas-Frontier-Matrix`
- ref: `main`
- commit: `d25a4c046892aa826ca04da29215f8ae4aae8e51`
- recorded at: `2026-09-12T01:19:24Z`
- Explorer path: `apps/explorer-web/`
- MapLibre package home: `packages/maplibre/`
- exact MapLibre package version present: `6.7.0`
- package-owned `MapLibreAdapter`: present
- Explorer browser runtime activated: bounded site-local branch candidate
- authenticated browser evidence complete: no
- readiness state: `HOLD`

`catalog.ts` is the code-owned website projection for this snapshot. Repository source links generated by the Explorer resolve against that exact main commit; the pin is source identity, not a green-build claim.

The prior public catalog snapshot `main@67cf9bcd8d4044beb2f7ec4ec17e1bf162ca30aa` remains available through Git history as lineage only; it is no longer presented as the current website snapshot.

Refresh `catalog.ts` again when repository authority, feature inventory, or maturity changes. A repository snapshot describes website data at one exact state; it does not create runtime, source-admission, review, release, deployment, promotion, or publication authority.

## Repository catalog/preflight slice

The Living Atlas exposes 15 repository-backed candidates and 10 existing workbench links as non-loadable discovery metadata. Available connector, declarative `pipeline_specs/`, and contract paths retain distinct visible labels; missing stages stay absent rather than being fabricated. Candidate maturity is not runtime availability, representation, review, or release state; real source admission and `EvidenceBundle` transport remain separate held work.

The catalog search moves to the first rail panel containing a match, held map tools expose `HELD` in their button text, and inspecting a repository candidate clears any prior selected runtime layer and evidence references before report/story capture. A selected design/data-held view constrains subsequent layer inspection and Focus evaluation to `ABSTAIN / VIEW_DATA_HELD` with empty eligible evidence; protected-layer `DENY` remains higher precedence. A committed time change disables out-of-time layer controls, clears incompatible visible state, selection, and evidence, preserves compatible timeless or policy-denied context, and rebuilds the inline map. Persisted v2 report/story collections are parsed against the complete registry-aware draft boundary; a valid v1 collection is read only when its v2 key is absent, while a present malformed v2 value fails closed without resurrecting legacy state. Draft reports keep only the current bounded snapshot. These are browser-composition behaviors only; they do not activate a connector, pipeline, layer, tool, source, or publication path.

## Trust boundary

This composition does not:

- read `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, candidate, canonical, graph, vector, object, or private lifecycle stores;
- activate or ingest a live source;
- call a model provider or local model runtime;
- perform policy, review, release, correction, rollback, or publication transitions;
- infer evidence from rendered features, pixels, route state, generated text, or a presentation badge;
- infer sensitivity or expand protected detail from a coarse public label;
- serialize prompts, reviewer notes, restricted coordinates, evidence excerpts, credentials, or private payloads into public workspace URLs;
- import `maplibre-gl` or create a second renderer acquisition seam; or
- claim that fixture-first feature slices are live production routes.

The concrete package-owned adapter is active only for the bounded inline Living Atlas candidate. External source admission, broader browser-readiness evidence, deployment, and release remain separate governed changes.

## Renderer-neutral runtime status

The map workspace now exposes the existing finite runtime-state presenter at its normal point of use. The synthetic controls exercise `IDLE`, `READY`, `STALE`, `WITHDRAWN`, and `ERROR` through `NullMapRuntime`; every non-`READY` state blocks candidate-selection eligibility, and critical states remain text-first assertive alerts.

This retained laboratory is consumer-migration and accessibility proof for the KFM-owned port only. The sibling Living Atlas composition uses `MapLibreAdapter` with no external resources; the laboratory still uses `NullMapRuntime` so stale, withdrawn, error, and recovery behavior remain deterministic. External tiles/sources, governed delivery, issue #2906 broader browser readiness, release, deployment, and publication remain on HOLD.

Implementation baseline: `main@8c943018a0cd59b06b5a623e15b9a9068a3513f4`.

## Validation

Run from `apps/explorer-web/` with the repository's locked toolchain:

```bash
pnpm run build
pnpm run test:unit
pnpm run test:browser
```

The catalog and Living Atlas tests check identifier/path uniqueness, the thirteen-domain inventory, all 18 views, 24 layers, 15 repository connections, four map controls, and 10 workbench links; source/evidence binding; declarative pipeline-specification labels; held-view abstention; sensitive-detail denial precedence; network-free style construction; multiscale time; and finite Focus outcomes. Browser checks also cover visible holds, matching-panel search, workbench handoff, held-view inspection, and evidence exclusion before draft capture. Workspace tests cover registry/context/URL behavior. Renderer, trust-surface, and Evidence Drawer tests preserve the no-network boundary, finite negative states, unique DOM identity, accessible relationships, and error suppression.

## Rollback

For the repository catalog/preflight slice, revert the Living Atlas connection/type exports, controller and CSS changes, catalog pin, paired unit/browser tests, affected READMEs, and generated receipt together. No source, data-lifecycle, renderer-activation, API, policy, review, release, deployment, promotion, or publication transition is required.

For the held-view forward fix, revert the registry evaluator, Living Atlas mount calls, paired unit/browser assertions, these README notes, and the forward-fix generated receipt as one bounded change. Do not alter or repurpose the preserved branch-only correction head; no data migration or external-state rollback is involved.

For UI-02, restore `src/main.ts`, remove `trust-state-primitives.ts`, `trust-surface.ts`, `site-trust.css`, and their tests, restore this README, and revert the bounded Evidence Drawer identity/error-presentation repair. UI-01 navigation/context behavior and the independently merged Focus Mode request surface remain intact. No data migration, renderer transition, API transition, source transition, policy action, release action, deployment action, or publication action is required.

For the renderer-neutral runtime-status slice, restore `mount-explorer-site.ts` and `site-map.css`, remove its bounded browser test, and restore this README. The reusable port and presenter remain intact, and rollback requires no data, dependency, renderer, API, source, release, deployment, or publication transition.
