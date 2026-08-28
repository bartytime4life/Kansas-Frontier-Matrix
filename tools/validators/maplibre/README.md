<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-maplibre-readme
title: tools/validators/maplibre README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-maplibre-steward-plus-ui-steward-plus-publication-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; maplibre-validator-index; renderer-boundary; map-runtime-boundary; evidence-drawer-aware; pmtiles-aware; cog-aware; layer-descriptor-aware; release-gated; public-surface-deny-by-default; non-authoritative
owning_root: tools/
responsibility: broad MapLibre validator routing index for checking renderer trust-boundary posture, released map artifact eligibility, source/layer/style descriptor readiness, PMTiles/COG/GeoParquet/TileJSON integrity references, MapReleaseManifest or release-reference linkage, EvidenceRef/EvidenceBundle and citation-validation linkage, policy/review/freshness/correction/rollback posture, forbidden browser operations, negative state propagation, and public-surface denial while deferring renderer implementation, UI shell code, contracts, schemas, policy decisions, proof records, receipts, lifecycle data, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../catalog/README.md
  - ../evidence/README.md
  - ../geo_manifest/README.md
  - ../identity/README.md
  - ../lifecycle/README.md
  - ../joins/README.md
  - ../../../packages/maplibre/README.md
  - ../../../packages/maplibre/src/README.md
  - ../../../docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - ../../../docs/architecture/map-shell.md
  - ../../../docs/architecture/evidence-drawer.md
  - ../../../docs/architecture/ui/LAYERING.md
  - ../../../docs/architecture/publication/GEO_MANIFEST.md
  - ../../../docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md
  - ../../../docs/domains/hydrology/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/agriculture/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/atmosphere/MAP_UI_CONTRACTS.md
  - ../../../contracts/data/layer_descriptor.md
  - ../../../contracts/evidence/kfm_geo_manifest.md
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../data/catalog/
  - ../../../data/published/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file at tools/validators/maplibre/README.md. It does not confirm executable validator code."
  - "MapLibre is the disciplined renderer and interaction runtime inside the governed KFM shell; it is not the canonical truth store, source registry, policy engine, citation authority, review authority, publication authority, or AI authority."
  - "packages/maplibre/ is a helper-code package for MapLibre adapter utilities and descriptor preparation. This validator lane checks readiness and boundary posture; it does not implement the renderer."
  - "KFM Geo Manifest is a release-candidate integrity manifest for PMTiles, COG, and GeoParquet bytes, not a release decision, policy engine, or sovereign truth source."
  - "Validators enforce declared contracts, schemas, evidence posture, policy references, release readiness, correction paths, rollback targets, and public-surface limits. They do not define map truth, approve release, publish public outputs, or authorize AI/map claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/maplibre

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-maplibre--validator--index-informational)
![renderer](https://img.shields.io/badge/renderer-downstream--only-blueviolet)
![release](https://img.shields.io/badge/release-gated-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/maplibre/` is the validator routing index for MapLibre renderer-boundary checks, map artifact readiness, source/layer/style descriptor safety, Evidence Drawer linkage, release references, correction/rollback posture, and public-surface denial without becoming renderer implementation, map truth, policy authority, citation authority, release authority, or AI authority.

---

## Purpose

`tools/validators/maplibre/` exists to organize MapLibre-facing validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Is a MapLibre-bound candidate safe for a governed renderer surface because it references released/public-safe artifacts, declared source/layer/style descriptors, evidence support, policy/review state, freshness/stale-state posture, release references, correction lineage, rollback targets, and negative states, while denying direct access to RAW, WORK, QUARANTINE, unpublished candidates, canonical/internal stores, source systems, direct model output, or unsupported public map claims?

The answer should be a deterministic validation result or routing decision. This folder should not create map truth, source truth, layer truth, style truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, PMTiles/COG/GeoParquet artifacts, MapLibre adapter code, public map layers, UI components, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/maplibre/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| `packages/maplibre/README.md` | **CONFIRMED README / implementation NEEDS VERIFICATION** | Shared helper-code package for MapLibre adapter utilities and validated descriptor preparation; renderer remains downstream and non-authoritative. |
| `docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md` | **CONFIRMED architecture doc / implementation NEEDS VERIFICATION** | Defines the map runtime boundary and states MapLibre is downstream of trust, never upstream of it. |
| `docs/architecture/publication/GEO_MANIFEST.md` | **CONFIRMED architecture doc / implementation NEEDS VERIFICATION** | Defines KFM Geo Manifest as release-candidate integrity manifest for PMTiles, COG, and GeoParquet bytes, not a release decision or truth source. |
| MapLibre validator executable | **NEEDS VERIFICATION** | No script name, registry wiring, runtime route, report destination, receipt path, or CI check is claimed here. |
| Source/layer/style schemas, fixtures, policy bundles, release manifests, artifact digests, browser tests, and public runtime integration | **NEEDS VERIFICATION** | This README is routing documentation only. |

[Back to top](#top)

---

## Relationship to nearby roots and lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| MapLibre validator routing | `tools/validators/maplibre/` | This README and possible future validator adapters. |
| MapLibre helper implementation | `packages/maplibre/` | Adapter/helper code; not truth, policy, release, or public authority. |
| Map runtime boundary doctrine | `docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md` | Defines renderer trust membrane and forbidden operations. |
| Map shell and UI architecture | `docs/architecture/map-shell.md`, `docs/architecture/ui/` | Human-facing architecture; validators check conformance. |
| Evidence Drawer | `docs/architecture/evidence-drawer.md`, evidence contracts/schemas | Drawer payloads resolve evidence; MapLibre does not create citations. |
| Map asset integrity | `docs/architecture/publication/GEO_MANIFEST.md`, `contracts/evidence/kfm_geo_manifest.md`, accepted schemas | Integrity manifests are not release decisions. |
| Catalog and layer records | `data/catalog/`, `contracts/data/layer_descriptor.md`, accepted schemas | Catalog/layer descriptors are carriers, not sovereign truth. |
| Published artifacts | `data/published/` and release-approved artifact homes | Renderer consumes public-safe released derivatives only. |
| Evidence/proof support | `data/proofs/`, `tools/validators/evidence/` | Validators check references; proof support stays outside this folder. |
| Receipts | `data/receipts/` | Receipts remain separate from validator docs and renderer code. |
| Policy | `policy/` | Validator reports gaps; it does not decide policy. |
| Release decisions and rollback | `release/` | Release authority remains in release records, promotion decisions, correction notices, rollback targets, and withdrawal records. |
| Lifecycle checks | `tools/validators/lifecycle/` | Map surfaces must not bypass lifecycle gates. |
| Tests and fixtures | `tests/validators/maplibre/`, `tests/packages/maplibre/`, `fixtures/`, or accepted conventions | Deterministic tests and synthetic fixtures prove behavior. |

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schemas are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not become |
|---|---|---|
| Renderer boundary | Does MapLibre receive only governed descriptors and public-safe released artifacts? | Direct trust source or data access layer. |
| Source descriptor safety | Does a source descriptor carry source role, attribution, bounds, artifact hash, lifecycle/release posture, and policy references? | URL-as-truth or browser-side source activation. |
| Layer descriptor safety | Does a layer descriptor carry layer id, source id, style id, time scope, evidence refs, policy refs, release refs, negative states, and rollback refs? | Map layer as sovereign claim. |
| Style descriptor safety | Are style expressions, sprites, glyphs, filters, legends, and opacity/visibility rules bounded by policy and public-safe constraints? | Hidden policy bypass or visual overclaim. |
| Tile/artifact integrity | Are PMTiles, COG, GeoParquet, MVT/MLT, TileJSON, sprites, glyphs, and screenshots backed by deterministic digest/manifest support where required? | Mutable URL, tag, or filename as trust. |
| Evidence Drawer linkage | Does a click or selected feature route to governed claim/evidence resolution instead of exposing raw map attributes as truth? | Popup as citation authority. |
| Negative states | Are denied, restricted, abstained, stale, unreleased, invalid, unavailable, unsigned, rollback-mismatch, and correction-pending states first-class? | Silent map failure or visual omission. |
| Forbidden browser operations | Does the browser avoid reading RAW/WORK/QUARANTINE/internal stores, source credentials, private endpoints, or direct model outputs? | Public client as trust bypass. |
| Public surface | Are map, popup, tile, export, screenshot, graph, search, Focus Mode, embedding, and AI interactions public-safe and release-supported? | Renderer-driven publication. |

[Back to top](#top)

---

## Renderer-boundary checks

A MapLibre-bound candidate should fail closed, deny, abstain, or route to steward review when it:

- lacks LayerManifest, StyleManifest, TileArtifactManifest, KFMGeoManifest, MapReleaseManifest, PromotionDecision, ReleaseManifest, rollback target, correction reference, or withdrawal posture required for its use;
- lacks EvidenceRef, EvidenceBundle, citation-validation reference, source descriptor, source role, policy decision, rights/sensitivity posture, freshness/stale-state posture, or review state required for public exposure;
- tries to load RAW, WORK, QUARANTINE, unpublished candidate, canonical/internal store, connector, private source URL, secret-bearing endpoint, or direct model output into a browser renderer;
- treats map source properties, TileJSON metadata, vector tile attributes, style expressions, popups, screenshots, Story Nodes, Focus Mode text, or AI answers as sovereign truth;
- displays stale, superseded, revoked, withdrawn, rollback-mismatched, or correction-pending layers as current;
- weakens sensitivity, rights, geoprivacy, cultural, infrastructure, living-person, DNA/genomic, archaeology, rare-species, or private parcel restrictions;
- omits official-source redirection where life-safety, regulatory, legal, title, engineering, medical, financial, or operational action could be inferred;
- bypasses lifecycle, catalog, evidence, policy, review, release, correction, or rollback gates because a map file or tile exists.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| MapLibre validator routing index | `tools/validators/maplibre/` |
| Shared validator plumbing | `tools/validators/_common/` |
| MapLibre helper code | `packages/maplibre/` |
| Map runtime boundary doctrine | `docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md` |
| Map shell, layering, compare/export, story-player, and UI docs | `docs/architecture/ui/`, `docs/architecture/map-shell.md` |
| Domain-specific map/UI contracts | `docs/domains/*/MAP_UI_CONTRACTS.md` or accepted domain docs |
| Layer/source/style/tile/map contracts | `contracts/` and accepted domain/data contracts |
| Machine schemas | `schemas/contracts/v1/` |
| Source descriptors and registries | `data/registry/`, `data/registry/sources/` |
| Catalog/layer records | `data/catalog/` |
| Published public-safe artifacts | `data/published/` and release-approved artifact homes |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Policy rules and release gates | `policy/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Public API and UI runtime | `apps/`, `ui/`, `web/`, or repo-confirmed runtime homes |
| Tests and fixtures | `tests/validators/maplibre/`, `tests/packages/maplibre/`, `fixtures/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared MapLibre renderer-boundary, source/layer/style descriptor, artifact-integrity, evidence, policy, release, correction, rollback, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, source registry topology, fixture shape, policy bundles, report destinations, receipt emission, package bindings, browser-test behavior, release integration, and CI wiring.
- **DENY:** using this folder as renderer implementation, UI shell, source registry, source payload store, lifecycle data store, catalog store, tile store, screenshot/export store, proof store, receipt store, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/maplibre/` include checks that:

- verify source/layer/style descriptor candidates carry required schema ids, versions, digests, source roles, evidence refs, policy refs, release refs, correction refs, and rollback refs;
- verify PMTiles, COG, GeoParquet, MVT/MLT, TileJSON, sprite, glyph, screenshot, and export candidates are backed by required integrity manifests and release references;
- verify MapLibre receives released/public-safe artifacts only through governed APIs, released artifacts, catalog records, tile services, and evidence-aware envelopes;
- verify feature-click payloads route to governed claim/evidence resolution rather than treating rendered attributes as truth;
- verify stale, invalid, denied, restricted, unreleased, unsigned, rollback-mismatch, correction-pending, and unavailable states are first-class and user-visible where appropriate;
- verify public surfaces do not leak sensitive exact locations, private identities, private parcel joins, archaeological locations, rare species locations, infrastructure exposure, DNA/genomic details, source credentials, or reconstruction hints;
- emit deterministic validation findings for steward review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/maplibre/` | Correct home |
|---|---|
| MapLibre adapter/runtime implementation | `packages/maplibre/`, `apps/`, `ui/`, `web/`, or accepted runtime homes |
| UI components, app shell, panels, map controls, Evidence Drawer views | `apps/`, `ui/`, `web/`, or accepted UI roots |
| Source descriptors or registries | `data/registry/`, `data/registry/sources/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Tiles, PMTiles, COGs, GeoParquet, MVT/MLT bundles, sprites, glyphs, screenshots, exports | lifecycle/release artifact homes with manifests and receipts |
| Catalog records or layer indexes | `data/catalog/` |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| Schemas, DTOs, enums, or descriptor machine shape | `schemas/contracts/v1/...` |
| Semantic contracts | `contracts/` |
| Policy rules, release gates, steward decisions, sensitivity thresholds | `policy/`, `release/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, map shell, Focus Mode runtime, generated AI map claims | governed application/runtime roots with evidence, policy, and release gates |
| Secrets, source credentials, private source content, sensitive exact locations, or reconstruction hints | denied here; keep out of repository-facing validator documentation |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `MAPLIBRE_VALIDATOR_PASS` | Candidate passed configured MapLibre renderer-boundary checks. |
| `MAPLIBRE_VALIDATOR_FAIL` | One or more configured checks failed. |
| `MAPLIBRE_VALIDATOR_DENY` | Candidate is denied because evidence, rights, policy, release, correction, rollback, sensitivity, or public-surface support cannot be resolved. |
| `MAPLIBRE_VALIDATOR_ABSTAIN` | Candidate lacks enough evidence or policy support to render. |
| `RENDERER_BOUNDARY_BREACH` | Candidate makes MapLibre truth, policy, citation, release, or AI authority. |
| `DIRECT_SOURCE_ACCESS_DENIED` | Candidate attempts browser access to RAW, WORK, QUARANTINE, unpublished, canonical/internal, connector, private, or source-system data. |
| `LAYER_DESCRIPTOR_MISSING` | Required layer descriptor or layer manifest reference is absent. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor, source role, attribution, or registry reference is absent. |
| `STYLE_DESCRIPTOR_INVALID` | Style candidate lacks required schema, policy, or public-safe constraints. |
| `GEO_MANIFEST_MISSING` | Required KFM Geo Manifest or artifact digest/integrity reference is absent. |
| `RELEASE_REFERENCE_MISSING` | Required MapReleaseManifest, ReleaseManifest, PromotionDecision, correction path, rollback target, or withdrawal path is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or citation-validation reference is absent or unresolved. |
| `POLICY_OR_REVIEW_GAP` | Required PolicyDecision, review state, rights posture, sensitivity posture, or release policy support is absent. |
| `STALE_OR_SUPERSEDED_LAYER_DENIED` | Stale, superseded, withdrawn, revoked, or rollback-mismatched layer is presented as current. |
| `NEGATIVE_STATE_NOT_RENDERABLE` | Required denied/restricted/abstain/invalid/stale/unreleased/unavailable state cannot be surfaced safely. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Map, popup, tile, export, screenshot, graph, search, Focus Mode, embedding, or AI surface exposes unsupported or unsafe map context. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/maplibre/
├── README.md
├── validate_maplibre_candidate.py       # PROPOSED; not confirmed
├── validate_maplibre_descriptor.py      # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If validator code is added, it should act as an adapter or dispatcher that routes to accepted schema, evidence, catalog, geo-manifest, policy, lifecycle, release, receipt, identity, and domain validators. It should not import MapLibre unless a narrow test adapter requires it, and it must not render UI, fetch source data, write lifecycle data, create EvidenceBundles, write receipts, decide policy, approve release, publish public outputs, or generate AI truth.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/maplibre/README.md`.
- [x] It marks this path as MapLibre validator routing, not renderer implementation, UI shell, map truth, policy, citation, release, public runtime, or AI authority.
- [x] It links MapLibre helper implementation to `packages/maplibre/` and renderer-boundary doctrine to `docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md`.
- [x] It links map artifact integrity posture to the KFM Geo Manifest and release/publication roots.
- [x] It preserves downstream-renderer, Evidence Drawer, source/layer/style descriptor, artifact integrity, evidence, policy, release, correction, rollback, and public-surface denial posture.
- [x] It routes machine shape, policy, fixtures, evidence, receipts, release, lifecycle data, tests, and semantic meaning to their owning roots.
- [x] It marks executable behavior, registry wiring, schema bindings, policy bundles, fixture files, receipt emission, runtime behavior, package bindings, browser-test behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to `maplibre/` are searched and classified.
- [ ] Accepted source/layer/style/tile/map schema homes, policy homes, fixture homes, test paths, and report destinations are verified.
- [ ] Tests exercise valid and invalid descriptor, artifact-integrity, release-reference, evidence-reference, stale-state, forbidden-browser-operation, rollback-mismatch, and public-surface leakage cases.
- [ ] CI invokes the relevant MapLibre validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with MapLibre validator routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
