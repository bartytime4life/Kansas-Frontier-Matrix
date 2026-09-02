# KFM Explorer Source Ledger, Gap Register, and Traceability

Audit date: 2026-08-24
Target: existing Site `kansas-frontier-matrix-explorer`
Truth rule: the current mounted Site proves current behavior; Drive documents support doctrine or proposals but do not prove implementation.

## Source ledger

Private Drive URLs are intentionally excluded from this Site artifact. The source codes below are audit-local IDs.

| Source ID | Title | Version / date | Drive modified | Status and authority | Site capabilities supported | Limits / supersession |
|---|---|---|---|---|---|---|
| `SRC-MAP-OPS` | KFM MapLibre Operating Architecture, Governed UI, and AI Interaction Manual — Revised Working Edition | Generated 2026-04-26 | 2026-04-26 | `CONFIRMED` doctrine; `PROPOSED` implementation; `UNKNOWN` repo depth | Persistent map shell, stable feature translation, Evidence Drawer, temporal state, bounded Focus Mode, validation | Supersedes its named baseline as a working revision; cannot prove current Site behavior; version facts require recheck |
| `SRC-MAP-MASTER` | Master MapLibre Components-Functions-Features | v2.0, 2026-05-16 | 2026-05-16 | Cumulative reference atlas; retained doctrine plus proposals | Registry-driven layers, runtime proof, PMTiles governance, public-safe fixtures, accessibility, performance | 2,950-record idea atlas; repetition is not adoption; retains v1.9 as lineage |
| `SRC-DOCTRINE` | KFM Unified Doctrine Synthesis | v1.0; last reviewed 2026-05-19 | 2026-07-12 | Doctrine-rank synthesis, not implementation evidence | Inspectable claims, finite outcomes, MapLibre/Evidence Drawer/Focus boundary, negative states | Proposed paths and runtime claims remain unverified |
| `SRC-CONNECTED` | Kansas Frontier Matrix — Connected-Dots Architecture Brief | v2.1; supersedes v1.0 PDF dated 2026-05-20 | 2026-07-12 | `CONFIRMED` doctrine synthesis; `PROPOSED` implementation | Map-first operating surface, exports with evidence/release metadata, finite Focus outcomes | No live-repo scan in source-authoring session |
| `SRC-PIPE` | Kansas Frontier Matrix Pipeline Living Implementation Manual | v0.3, 2026-04-30 | 2026-05-07 | Planning and loop-control doctrine | Lifecycle boundary, no-autopublish, no-generated-truth, negative fixtures | Supersedes v0.2 for planning; v0.2 retained as lineage; code paths proposed |
| `SRC-AI` | Kansas Frontier Matrix — AI Build Operating Contract | v3.0; generated/reviewed 2026-05-19 | 2026-07-12 | Operating law confirmed at doctrine rank; operational realization proposed | Evidence-subordinate AI, finite outcomes, cite/abstain, no direct model path | Proposed repo placement; not proof of a governed backend |
| `SRC-DIR` | Directory Rules | preparation date not stated in file | 2026-05-03 | Placement doctrine / responsibility-root guidance | Keeps audit material under `docs/`; prevents browser exposure of internal source paths | Connected-Dots cites Directory Rules v1.2, while this copy lacks an explicit version header; unresolved version identity |
| `SRC-FOCUS-NEMAHA` | Nemaha County Focus Mode Build Plan | v0.1-proposed, 2026-06-09 | 2026-06-09 | `PROPOSED`; release `NEEDS_VERIFICATION` | Bounded county context, sensitive-domain denials, four finite outcomes | Explicitly claims no implementation, admission, validation, review, release, or publication |
| `SRC-WHOLE-PROP` | KFM Authoritative Whole-System Reference | proposed-for-adoption edition, 2026-08-15 | 2026-08-16 | `PROPOSED`; synthesis/reference only | Public-safe hydrology proof slice, shell surfaces, negative states, LayerManifest/StyleManifest concepts | Does not supersede accepted ADRs, contracts, code, tests, manifests, or runtime evidence |
| `SRC-UNIFIED-WORKSPACE` | KFM Unified Workspace — Complete User Interface Architecture | v0.1.0 draft, 2026-08-23 | repository current-main source | `PROPOSED`; repository-grounded architecture synthesis | Four public workspaces, one context spine, role-bounded capability, progressive disclosure | Proposed routes and privileged surfaces are not runtime, authorization, release, deployment, or publication evidence |
| `SRC-DELTA` | KFM Circled Sources — Distinctive Delta Synthesis | consolidation record, 2026-08-23 | 2026-08-23 | `WORKING REFERENCE`; exclusion and residual-idea record | Separate authority/maturity axes, optional contributor rhythm, briefing lenses | Creates no state machine, policy result, workflow gate, roadmap commitment, or authority claim |
| `SRC-ATLAS-SEED` | KFM Full Atlas Seed Cards | Drive document inspected 2026-08-24 | 2026-07-12 | `PROPOSED`; normalized idea and feature cards | Claim-level trust fields, separate temporal axes, evidence-preserving export, health states, receipts | Placeholder IDs and normalized proposals are not stable runtime contracts or implementation proof |

Searches also found duplicate retained artifacts, including two identical Pass 17 master PDFs and duplicate Implementation Reference PDFs. They were treated as duplicate lineage, not independent support.

## Current Site capability inventory

`CONFIRMED` from the mounted Site checkout:

- MapLibre GL JS `6.4.1` is the installed browser renderer.
- The MapLibre instance stays mounted while the Layer Catalog, Evidence Drawer, timeline, tools, and responsive sheets change state.
- Eleven registry-driven, site-local GeoJSON layers cover public-safe demonstration categories: boundaries/places, hydrology, ecology, geology, agriculture, atmosphere, communities, transport, historical geography, generalized planning, and diagnostics.
- Stable source, layer, renderer, and feature IDs are used; GeoJSON sources use `promoteId: "fid"`.
- Style switching restores custom sources, layers, selection, measurement state, and draw order.
- Layer search, visibility, opacity, legends, metadata, attribution, zoom, draw order, valid-time notes, freshness, release labels, sensitivity notes, and unavailable-time explanations are working.
- Hover, click selection, clusters, popups, zoom-to-feature/layer, clear selection, distance/area measurement, and keyboard-accessible catalog inspection are implemented.
- The Evidence Drawer exposes source role, citation/reference, spatial/temporal scope, freshness, review/release state, rights, generalization, uncertainty, correction, and lineage; the Map Workbench adds explicit preflight before public-safe export.
- Timeline steps, playback, exact observation time, cumulative historical vintage, availability indicators, and no-data messaging are implemented with site-local fixtures.
- Search covers layers, datasets, feature names, and stable IDs.
- URL state preserves camera, visible layers, opacity, time, basemap, projection, layer order, workspace, map-workbench view, selection, Drawer/Focus state, and a restored privacy-redaction marker.
- Responsive panels become focus-trapped modal sheets on compact layouts; map status has a screen-reader live region; reduced-motion and forced-colors handling exist.
- Focus Mode is a deterministic site-local adapter with no direct browser-to-model endpoint.
- Globe projection is available as context; terrain and swipe comparison were described as unavailable because no audited data dependency exists.
- Source errors are isolated to the affected registry layer when MapLibre supplies a source ID; unrecoverable runtime errors fail visibly.

## Gap register

### `GAP-P0-001` — Focus Mode outcome could be manually forced

- Category: Evidence / governed AI.
- Sources: `SRC-MAP-OPS` §12 and §14; `SRC-DOCTRINE` §§18–21; `SRC-CONNECTED` §§8–9; `SRC-AI` §§20–23.
- Source authority/status: confirmed doctrine; implementation must be proven by current Site behavior.
- Current Site evidence: a four-button scenario switch let any selected feature display `ANSWER`, including missing, stale, restricted, denied, or error fixtures.
- Current state: misleading deterministic demonstration control.
- Desired state: selected evidence state alone determines `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
- Truth label: `CONFIRMED`.
- User value: prevents a public user from generating an apparently supported result from unsupported context.
- KFM trust value: restores cite-or-abstain and fail-closed finite outcomes.
- Dependencies: existing `EvidenceState`; no service or new data dependency.
- UI dependency: Focus Mode panel.
- Rights/sensitivity: improves withholding; exposes no additional detail.
- Accessibility: replaces color-only scenario buttons with a text evidence-state-to-outcome mapping.
- Performance: negligible.
- Effort / risk / priority: small / low / P0.
- Acceptance: `ANSWER` only for `ANSWER` or `CORRECTED`; restricted/denied map to `DENY`; error maps to `ERROR`; all other states map to `ABSTAIN`; no manual override exists.
- Rollback: revert the Focus result resolver and panel block.
- Disposition: `IMPLEMENT_NOW`.

### `GAP-P1-002` — Shared state omitted projection and draw order

- Category: Sharing / navigation.
- Sources: `SRC-MAP-OPS` §§8–10 and §14; `SRC-MAP-MASTER` components/functions matrix; `SRC-CONNECTED` §8.
- Source authority/status: doctrine plus proposed implementation guidance.
- Current Site evidence: camera, visibility, opacity, year, basemap, feature, and Drawer tab were serialized; globe/2D projection and registry draw order were not.
- Current / desired state: partial deep link → complete working demonstration state for supported controls.
- Truth label: `CONFIRMED`.
- User / trust value: a shared view reproduces the visual context used for evidence inspection.
- Dependencies: URL state only; no service/data dependency.
- UI / rights / accessibility: no new exposure; copy action retains an announced result.
- Performance: negligible.
- Effort / risk / priority: small / low / P1.
- Acceptance: `proj` and validated complete `order` restore; exports include layer order; malformed order is ignored.
- Rollback: remove the two URL keys and restore branches.
- Disposition: `IMPLEMENT_NOW`.

### `GAP-P1-003` — Browser history did not restore Explorer state

- Category: Navigation / reliability.
- Sources: `SRC-MAP-OPS` governed interaction and state model; `SRC-MAP-MASTER` deep-link guidance.
- Current Site evidence: startup restoration existed, but no `popstate` listener reapplied state.
- Desired state: history navigation reapplies the same bounded URL state without remounting MapLibre.
- Truth label: `CONFIRMED`.
- User / trust value: avoids mismatches between the address bar and visible map/evidence context.
- Dependencies: existing URL state parser and MapLibre camera.
- Rights / sensitivity: unchanged.
- Accessibility: reduces context loss for keyboard/browser navigation.
- Performance: bounded local state update.
- Effort / risk / priority: small / low / P1.
- Acceptance: a `popstate` event reapplies camera, layers, opacity, time, basemap, projection, order, selection, and Drawer view.
- Rollback: remove the listener and keep startup-only restoration.
- Disposition: `IMPLEMENT_NOW`.

### `GAP-P1-004` — Desktop Escape behavior was incomplete

- Category: Accessibility.
- Sources: `SRC-MAP-OPS` §8 and §14; `SRC-MAP-MASTER` accessibility records.
- Current Site evidence: compact modal sheets trapped focus and handled Escape; desktop help/tools/Evidence Drawer did not share an Escape path.
- Desired state: Escape closes the active desktop overlay or Drawer in priority order.
- Truth label: `CONFIRMED`.
- User / trust value: predictable keyboard recovery from map overlays.
- Dependencies: existing panel state and focus-return behavior.
- Rights / performance: unchanged / negligible.
- Effort / risk / priority: small / low / P1.
- Acceptance: Escape closes help, then tools, then the Evidence Drawer; compact sheet behavior remains unchanged.
- Rollback: remove the desktop key handler.
- Disposition: `IMPLEMENT_NOW`.

### `GAP-P1-005` — Persistent map shell, registry catalog, Evidence Drawer, timeline, and public-safe export

- Category: Core Explorer.
- Sources: `SRC-MAP-OPS`, `SRC-MAP-MASTER`, `SRC-DOCTRINE`, `SRC-CONNECTED`.
- Current Site evidence: mounted MapLibre shell and working controls listed in the inventory above.
- Current / desired state: adequately implemented for a site-local demonstration.
- Truth label: `CONFIRMED`.
- Dependencies / impact: existing local fixtures only; no rights expansion.
- Acceptance: existing build and rendered-shell tests remain green.
- Rollback: not applicable to this audit.
- Disposition: `ALREADY_PRESENT`.

### `GAP-P3-006` — Terrain and hillshade

- Category: Advanced rendering.
- Sources: `SRC-MAP-OPS` §§10–11 marks terrain conditional; `SRC-MAP-MASTER` treats advanced rendering as gated.
- Current Site evidence: no audited raster-DEM source or release-linked terrain manifest.
- Desired state: only after evidence-parity 2D fallback, rights, attribution, performance, and release linkage exist.
- Truth label: `NEEDS VERIFICATION`.
- Data/service/UI dependencies: audited DEM/raster tiles, source manifest, fallback, device gate, attribution.
- Rights/sensitivity / accessibility / performance: review required / 2D equivalent required / material GPU and network impact.
- Effort / risk / priority: large / medium-high / P3.
- Acceptance: not defined until source admission and performance budgets exist.
- Rollback: feature flag and removal of DEM source/layers.
- Disposition: `DEFER_DATA`.

### `GAP-P2-007` — Swipe/raster comparison

- Category: Comparison.
- Sources: `SRC-MAP-MASTER` comparison records; `SRC-MAP-OPS` interaction model.
- Current Site evidence: no compatible released or demonstration raster pair with aligned time/rights metadata.
- Desired state: comparison only when two compatible sources and attribution/export rules are available.
- Truth label: `UNKNOWN`.
- Dependencies: paired sources, temporal alignment, comparison control, keyboard/text alternative.
- Rights/sensitivity / accessibility / performance: unresolved / alternative required / potentially material.
- Effort / risk / priority: medium / medium / P2.
- Acceptance: deferred with dependencies.
- Rollback: remove comparison control and secondary source.
- Disposition: `DEFER_DATA`.

### `GAP-P1-008` — Released PMTiles/MVT/COG or governed API adapters

- Category: Delivery / backend.
- Sources: `SRC-MAP-OPS` §§10–14; `SRC-MAP-MASTER` PMTiles governance; `SRC-PIPE` §§18–21.
- Current Site evidence: all ten layers are bounded site-local GeoJSON fixtures; no released remote adapter is claimed.
- Desired state: manifest-bound, release-linked adapters with range/header, rights, stale, correction, and error proof.
- Truth label: `UNKNOWN`.
- Dependencies: governed backend or admitted public artifact, manifest, rights review, cache/correction rules.
- UI dependency: existing registry can host a future adapter boundary.
- Accessibility: existing text metadata and negative states should remain.
- Performance: must be measured before activation.
- Effort / risk / priority: large / high / P1 dependency.
- Acceptance: exact-negative source failures, release/correction propagation, and attribution survive export.
- Rollback: adapter removal returns to site-local fixtures.
- Disposition: `DEFER_DEPENDENCY`.

### `GAP-P2-009` — County Focus Mode package

- Category: Domain / Focus Mode.
- Sources: `SRC-FOCUS-NEMAHA` only, supported by general doctrine.
- Current Site evidence: no county-specific admitted data or release package.
- Desired state: bounded county package after source admission, policy, rights, security, review, and release evidence.
- Truth label: `PROPOSED`.
- Dependencies: county source descriptors, generalized geometry, review owners, EvidenceBundles, release record.
- Rights/sensitivity: material; ownership/access, infrastructure, operational, and culturally sensitive inferences must remain denied.
- Accessibility/performance: county summary alternative and bounded layer budgets required.
- Effort / risk / priority: large / high / P2.
- Acceptance: cannot be set before the plan's explicit `NEEDS_VERIFICATION` items are resolved.
- Rollback: remove county package and preserve statewide demonstration.
- Disposition: `DEFER_POLICY`.

### `GAP-P1-010` — Demonstration, stale, generalized, restricted, corrected, superseded, loading, empty, denied, and error states

- Category: Trust visibility.
- Sources: all doctrine sources above.
- Current Site evidence: feature and layer fixtures plus runtime overlays already expose these states in text and non-color UI.
- Truth label: `CONFIRMED`.
- Dependencies: existing fixtures and MapLibre error events.
- Acceptance: negative fixtures never produce unsupported answers or unredacted geometry in export.
- Rollback: not applicable to this audit.
- Disposition: `ALREADY_PRESENT`.

## Implemented source-to-feature traceability

| Implementation item | Supporting sources | Gap resolved | Data / status | Trust states | Changed components | Validation | Known limitations | Rollback |
|---|---|---|---|---|---|---|---|---|
| Fail-closed Focus resolver | `SRC-MAP-OPS`, `SRC-DOCTRINE`, `SRC-CONNECTED`, `SRC-AI` | `GAP-P0-001` | Existing site-local fixtures; `DEMONSTRATION` | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | `app/page.tsx`, `app/globals.css` | Build, source guard, browser interaction check | Not a governed backend; no live model | Revert resolver/panel block |
| Projection and draw-order deep links | `SRC-MAP-OPS`, `SRC-MAP-MASTER` | `GAP-P1-002` | Browser URL state; demonstration | Preserves selected evidence context | `app/page.tsx` | Build, malformed-order guard, browser restore check | Does not create a short-link service | Remove `proj`/`order` keys |
| History restoration | `SRC-MAP-OPS`, `SRC-MAP-MASTER` | `GAP-P1-003` | Browser-local state | Prevents URL/UI trust mismatch | `app/page.tsx` | Source guard and browser back/forward check | History entries are created only when the user shares | Remove `popstate` handler |
| Desktop Escape path | `SRC-MAP-OPS`, `SRC-MAP-MASTER` | `GAP-P1-004` | UI state only | No trust-state change | `app/page.tsx` | Keyboard browser check | Does not turn desktop side panels into modal dialogs | Remove key handler |
| Unsupported-browser fail-visible path | `SRC-MAP-OPS`, `SRC-MAP-MASTER` | Reliability acceptance criterion | Capability probe only | `ERROR`; catalog and trust text remain available | `app/page.tsx` | Browser environment without WebGL2 | Interactive map requires WebGL2 | Remove the preflight capability check |
| Visible advanced-capability gates | `SRC-MAP-OPS`, `SRC-MAP-MASTER` | `GAP-P3-006`, `GAP-P2-007` | No data added | `UNKNOWN` / unavailable remains visible | `app/page.tsx`, `app/globals.css` | Render/build check | Terrain and swipe remain intentionally unavailable | Remove explanatory gate block |

## Remaining boundary

- `NEEDS VERIFICATION`: current external MapLibre/tool version facts quoted in older Drive manuals; source-led error simulation with a real remote adapter.
- `NEEDS DATA`: audited DEM, comparison raster pair, released or explicitly admitted tile/data artifacts.
- `NEEDS POLICY`: county Focus Mode review owners and lane-specific public-safe rules.
- `NEEDS RIGHTS REVIEW`: any external county, ecology, infrastructure, parcel, archive, or imagery source.
- `NEEDS ARCHITECTURE DECISION`: real adapter and manifest contract; short-link service; production comparison architecture.
- `NEEDS GOVERNED BACKEND`: released EvidenceBundle resolution, governed API, model adapter, citation validation, AIReceipt/audit linkage.
- `EXPERIMENTAL`: terrain, advanced 3D, point clouds, offline mode, field capture.
- `NOT RECOMMENDED`: direct browser-to-model access, client database access, precise protected locations, invented live status, or treating Drive proposals as releases.
