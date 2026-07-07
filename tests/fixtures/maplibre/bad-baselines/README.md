<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-maplibre-bad-baselines-readme
title: MapLibre Bad Baselines Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; maplibre-bad-baselines-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Map steward
  - OWNER_TBD - UI steward
  - OWNER_TBD - MapLibre steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - Accessibility steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; maplibre; bad-baselines; negative-fixtures; visual-regression; synthetic-only; no-network; public-safe; renderer-not-truth; release-gated; policy-aware; accessibility-aware
tags: [kfm, tests, fixtures, maplibre, bad-baselines, visual-regression, screenshot-boundary, renderer-boundary, style-boundary, layer-manifest, MapReleaseManifest, LayerManifest, LayerDescriptor, trust-badges, no-network, DENY, ABSTAIN, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../../../domains/fauna/visual/README.md
  - ../../layers/README.md
  - ../../map/README.md
  - ../../ui/README.md
  - ../../runtime/README.md
  - ../../../../docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md
  - ../../../../docs/architecture/ui/LAYERING.md
  - ../../../../apps/explorer-web/src/features/layer_catalog/README.md
  - ../../../../packages/maplibre/
  - ../../../../packages/ui/
  - ../../../../contracts/release/map_release_manifest.md
  - ../../../../contracts/data/layer_manifest.md
  - ../../../../contracts/data/layer_descriptor.md
  - ../../../../schemas/contracts/v1/layers/
  - ../../../../schemas/contracts/v1/release/
  - ../../../../policy/layers/
  - ../../../../policy/sensitivity/
  - ../../../../release/
  - ../../../../artifacts/
notes:
  - "This README replaces placeholder content at tests/fixtures/maplibre/bad-baselines/README.md."
  - "This lane documents intentionally bad MapLibre visual/rendering baseline fixtures. It does not become a screenshot archive, renderer implementation, style authority, tile store, release artifact store, evidence store, policy home, or public map root."
  - "Bad baselines are negative test carriers: they should prove that visual tests fail or require review when trust, policy, release, evidence, accessibility, or deterministic-rendering expectations are violated."
  - "MapLibre, style JSON, screenshots, tiles, exports, popups, and scenes are downstream carriers, not sovereign truth."
  - "Executable tests, baseline payload inventory, runner wiring, screenshot retention, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre bad-baseline test fixtures

> Test-local documentation for intentionally bad MapLibre baseline fixtures under `tests/fixtures/maplibre/bad-baselines/`. This lane supports negative visual-regression, renderer-boundary, trust-state, policy, accessibility, and release-gating checks without turning screenshots, styles, tiles, rendered maps, or baseline images into truth authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: bad baselines" src="https://img.shields.io/badge/lane-bad__baselines-purple">
  <img alt="Renderer: MapLibre" src="https://img.shields.io/badge/renderer-MapLibre-0a7ea4">
  <img alt="Posture: negative fixtures" src="https://img.shields.io/badge/posture-negative__fixtures-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/maplibre/bad-baselines/README.md`  
**Status:** draft / placeholder replaced / MapLibre bad-baseline fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/maplibre/bad-baselines`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe negative fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED repo search did not surface a direct README for this exact lane before authoring; CONFIRMED `tests/README.md` allows `tests/fixtures/` only as unit-test-scoped fixtures and forbids direct pre-publication/internal reads, unlisted tile/style loads, and unsafe exact-detail exposure; CONFIRMED MapLibre doctrine says rendered artifacts are downstream carriers, not root truth; NEEDS VERIFICATION for executable tests, baseline payload inventory, visual runner wiring, screenshot retention, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/maplibre/bad-baselines/` is a unit-test-scoped negative fixture lane for MapLibre visual and rendering baselines.

Use this lane for intentionally wrong, unsafe, stale, incomplete, non-deterministic, or policy-invalid baseline examples that a visual or regression test must reject or route to review. A bad baseline fixture should make an expected failure obvious: missing trust badge, hidden denial state, missing release ref, missing layer manifest, missing artifact digest, unsafe display state, style-only masking, live-network dependency, unapproved tile/style/glyph/sprite load, stale release state, inaccessible color-only trust signal, or screenshot-as-truth misuse.

A bad baseline should not mean that the rendered map is true, a release is approved, a visual artifact is published, a screenshot is evidence, a style is policy, a tile is safe, or MapLibre has source authority. It should mean only that a bounded synthetic negative fixture exercises a bounded rejection or review expectation.

[Back to top](#top)

---

## Placement basis

`tests/fixtures/` is for unit-test-scoped fixtures local to a test's needs. This lane is appropriate only as a local negative fixture surface for MapLibre bad-baseline cases. It is not a fixture root for reusable shared MapLibre examples, and it is not a screenshot archive or artifact retention area.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Bad MapLibre baseline fixtures | `tests/fixtures/maplibre/bad-baselines/` | This directory. |
| Visual regression tests | `tests/` consumer lanes, such as domain visual tests or UI tests | Expected consumers; not fixture authority. |
| Renderer implementation | `packages/maplibre/` or accepted renderer wrapper roots | Not owned here. |
| Explorer Web UI implementation | `apps/explorer-web/` | Not owned here. |
| Shared UI components | `packages/ui/` | Not owned here. |
| Layer/release contracts | `contracts/data/`, `contracts/release/`, `contracts/map/` | Defines meaning; not owned here. |
| Layer/release schemas | `schemas/contracts/v1/layers/`, `schemas/contracts/v1/release/` | Defines machine shape; not owned here. |
| Policy authority | `policy/layers/`, `policy/sensitivity/`, `policy/release/` | Admissibility authority; not owned here. |
| Release authority | `release/` | Publication, correction, withdrawal, and rollback authority; not owned here. |
| Retained screenshots or CI artifacts | `artifacts/` or CI artifact storage when governed | This lane may reference them, not store production artifacts. |

> [!IMPORTANT]
> Do not use this directory as a baseline approval archive, visual evidence store, public screenshot store, style authority, tile authority, release store, policy home, proof home, or renderer implementation path. Bad baselines are rejection fixtures.

---

## Invariant under test

> **A bad baseline must fail or require review.** If a bad baseline passes silently, the visual/regression guard is not enforcing KFM's trust membrane.

Core checks:

| Check | Bad baseline condition | Expected outcome |
|---|---|---|
| Renderer-not-truth | Screenshot or rendered map is treated as evidence, proof, release, or source truth. | `DENY` / validation failure. |
| No-network default | Baseline depends on live tile, glyph, sprite, style, source, or API request. | `ERROR` / validation failure. |
| Release gate | Baseline uses unreleased, candidate, withdrawn, stale, or rollback-missing layer state as current public layer. | `DENY` / review required. |
| Manifest closure | Baseline lacks `LayerManifest`, `LayerDescriptor`, `MapReleaseManifest`, artifact digest, or release ref where material. | `ABSTAIN` / validation failure. |
| Evidence closure | Claim-bearing visual state lacks EvidenceRef / EvidenceBundle support. | `ABSTAIN`. |
| Policy closure | Rights, review, or public-display posture is absent or unresolved. | `DENY` / `ABSTAIN`. |
| Unsafe detail exposure | Restricted detail is made visible through style, labels, hover, popup, export, selection, or tile state. | `DENY`. |
| Style-only masking | Style filters hide a problem that must be handled by governed transform, restriction, delay, or denial before public artifacts. | `DENY`. |
| Trust-state visibility | Trust badges, stale/denied/withdrawn states, correction notices, or rollback state are missing or color-only. | validation failure. |
| Determinism | Viewport, time window, seed, font, device pixel ratio, or render options are unstable or unspecified. | `ERROR` / review required. |

---

## Expected bad-baseline families

| Family | What is intentionally wrong | Expected result |
|---|---|---|
| `missing_trust_badges` | Layer card or map overlay lacks rights/release/freshness labels. | validation failure. |
| `color_only_trust_state` | Denied/stale/restricted state is conveyed only by color. | validation failure. |
| `unreleased_layer_enabled` | Candidate or unpublished layer renders as public-enabled. | `DENY`. |
| `withdrawn_layer_current` | Withdrawn/superseded layer appears current. | `DENY` / review required. |
| `missing_manifest_ref` | Baseline cannot resolve required layer/release manifest refs. | `ABSTAIN` / validation failure. |
| `missing_artifact_digest` | Tile/style/sprite/glyph/COG/PMTiles ref lacks digest or integrity binding. | `ERROR`. |
| `live_tile_dependency` | Test fixture would fetch live network tile/style/glyph/sprite material. | `ERROR`. |
| `style_only_masking` | A style rule hides an issue that must be handled before publication. | `DENY`. |
| `unsafe_detail_visible` | Restricted detail appears in the rendered baseline. | `DENY`. |
| `screenshot_as_evidence` | Baseline metadata treats screenshot as EvidenceBundle/proof/release. | validation failure. |
| `unstable_viewport` | Viewport, clock, zoom, seed, or render flags are not deterministic. | `ERROR` / review required. |
| `missing_rollback_state` | Public release visual has no rollback target or correction lineage. | `DENY` / release block. |

---

## Accepted material

Only bounded, synthetic, reviewable negative material belongs in this lane:

- README files and small bad-baseline manifests
- synthetic metadata describing bad screenshot/baseline cases without storing real production screenshots
- toy viewport specs, toy layer refs, toy release refs, toy style refs, toy glyph/sprite refs, toy artifact refs, toy digests, toy timestamps, and toy policy refs
- synthetic expected outcomes and reason codes for visual/regression rejection
- small illustrative `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.md`, or minimal image placeholder references when review-safe and clearly synthetic
- canaries for missing trust badges, color-only state, unsafe display, missing digest, live-network dependency, style-only masking, stale release, withdrawn release, missing correction lineage, missing rollback target, and screenshot-as-truth misuse

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Production screenshots, real baseline image archives, public map screenshots, or retained CI artifacts | Use governed `artifacts/` or CI artifact storage with retention policy; this lane is not a screenshot archive. |
| Real PMTiles, COGs, MVT/MLT/vector tiles, tilejson, style JSON, sprites, glyphs, rasters, GeoParquet, or 3D Tiles | Artifacts belong in governed artifact/release/published homes, not tests. |
| Real `LayerManifest`, `MapReleaseManifest`, `ReleaseManifest`, `PolicyDecision`, `EvidenceBundle`, proof, receipt, signature, or attestation records | Governed trust and release records belong in their own roots. |
| Direct reads from pre-publication/internal stores, unpublished candidates, graph stores, vector indexes, public APIs, tile servers, style servers, or model runtime outputs | Bypasses the trust membrane and no-network posture. |
| Credentials, private endpoints, restricted telemetry, or access keys | Security and exposure risk. |
| Binding policy rules, schema definitions, contract prose, release procedures, pipeline implementation, connector implementation, map renderer implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/maplibre/bad-baselines/
|-- README.md
|-- missing_trust_badges.deny.json
|-- color_only_trust_state.invalid.json
|-- unreleased_layer_enabled.deny.json
|-- withdrawn_layer_current.deny.json
|-- missing_manifest_ref.abstain.json
|-- missing_artifact_digest.error.json
|-- live_tile_dependency.error.json
|-- style_only_masking.deny.json
|-- unsafe_detail_visible.deny.json
|-- screenshot_as_evidence.invalid.json
|-- unstable_viewport.error.json
|-- missing_rollback_state.deny.json
`-- expected_reason_codes.json
```

This layout is PROPOSED until executable files and consumers exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/ui tests/domains tests/fixtures/maplibre/bad-baselines
```

Required run posture: no network access, no live source calls, no direct tile/CDN/style/glyph/sprite fetches, no direct lifecycle-store reads, no direct model runtime calls, no production screenshots, no production trust artifacts, no public artifact writes, deterministic fixture inputs, deterministic viewport, and finite outcomes only.

---

## Minimal bad-baseline manifest

Synthetic manifests should describe the expected rejection without carrying real screenshots or artifacts.

```json
{
  "fixture_manifest_id": "maplibre-bad-baseline-missing-trust-badges",
  "fixture_family": "missing_trust_badges",
  "renderer": "maplibre",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "TRUST_BADGES_MISSING",
    "LAYER_STATE_NOT_REVIEWABLE"
  ],
  "viewport_ref": "viewport:synthetic:maplibre:fixed-800x600-z7",
  "layer_manifest_ref": "layer:synthetic:manifest:public-safe-example",
  "map_release_ref": "release:synthetic:map:public-safe-example",
  "network": "disabled",
  "uses_real_tiles": false,
  "uses_real_screenshots": false,
  "authorizes_publication": false
}
```

---

## Finite outcome expectations

| Outcome | Meaning in this lane | Example |
|---|---|---|
| `PASS` | Rare for this lane; used only when the negative fixture itself is well-formed and the consumer correctly rejects it. | Harness recognizes `style_only_masking` as denied. |
| `ABSTAIN` | Missing manifest, evidence, release, or citation support prevents visual approval. | Baseline lacks layer manifest ref. |
| `DENY` | Policy, release, trust-state, screenshot-boundary, or style-masking rule blocks the baseline. | Restricted display state appears in a rendered view. |
| `ERROR` | Fixture, loader, viewport, artifact digest, render configuration, or no-network guard is malformed. | Fixture attempts live tile fetch. |
| `REVIEW_REQUIRED` | Visual difference is not automatically safe or unsafe without steward review. | Deterministic but changed trust-state placement. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, public-safe, and no-network
- [ ] no production screenshots, real baselines, real tiles, styles, sprites, glyphs, rasters, PMTiles, COGs, or public payloads are present
- [ ] every fixture declares expected outcome, reason code where applicable, viewport/config posture, and no-network posture
- [ ] layer refs, release refs, evidence refs, policy refs, artifact digest placeholders, correction refs, rollback refs, and trust-state expectations are explicit where material
- [ ] bad baselines fail or require review; they do not pass silently
- [ ] unknown rights, unresolved evidence, missing policy, missing release state, missing rollback target, missing attestation, and unsafe display state fail closed
- [ ] style filters are never used as the redaction or restriction mechanism
- [ ] visual trust state has non-color labels and accessibility expectations where UI-facing
- [ ] screenshot artifacts remain review aids only and do not become evidence/proof/release material
- [ ] docs, tests, schemas, contracts, policies, governed API routes, UI consumers, renderer wrappers, visual runner configuration, and release gates are updated when baseline behavior changes

---

## Change discipline

Changes to this lane should be small, inspectable, and reversible.

| Change type | Required action |
|---|---|
| Add a bad-baseline manifest | Add fixture family, expected failure outcome, reason codes, viewport/config state, and no-network posture. |
| Add an unsafe-display canary | Use synthetic placeholders only; do not include restricted real-world values. |
| Add a screenshot reference | Keep it synthetic or CI-artifact-ref-only; never store production screenshots here. |
| Add a live-network canary | Model it as metadata; do not actually require live network in the default suite. |
| Add a style-masking canary | State that style-only masking is forbidden and expected to deny. |
| Add an accessibility baseline | Include non-color trust labels, keyboard, screen-reader, and reduced-motion expectations. |
| Discover real artifacts or restricted data | Move them out, quarantine through the governed lifecycle or registry process, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Exact lane evidence: repo search found no direct prior README evidence for `tests/fixtures/maplibre/bad-baselines/` beyond the placeholder during authoring; this lane is therefore documented as PROPOSED test-local negative fixture posture.
- Test-root alignment: verified against `tests/README.md` in related fixture updates for unit-test-scoped fixture posture, forbidden boundaries, sensitive-fixture safeguards, and deterministic no-network default.
- Visual-regression alignment: verified against `tests/domains/fauna/visual/README.md` for visual snapshot boundary, no-network default, screenshot-as-not-truth, trust-state visibility, policy-withheld detail, and reviewable visual changes.
- MapLibre architecture alignment: verified against `docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` for MapLibre as renderer, not truth store, and public map surfaces reading through governed interfaces.
- Contract/schema alignment: NEEDS VERIFICATION against layer, release, runtime, evidence, visual-runner, and policy schemas.
- Consumer alignment: NEEDS VERIFICATION against MapLibre visual tests, Layer Catalog tests, governed-API tests, map runtime tests, domain visual tests, Evidence Drawer checks, release-manifest checks, policy checks, rights checks, artifact-integrity checks, accessibility checks, rollback drills, renderer checks, screenshot retention policy, and CI coverage.
- Tests and validators: NOT RUN.
