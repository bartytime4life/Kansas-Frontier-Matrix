<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-layers-readme
title: Layer Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; layer-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Layer steward
  - OWNER_TBD - Map/UI steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - Accessibility steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; layers; map-release; synthetic-only; no-network; public-safe; evidence-bound; rights-aware; sensitivity-aware; release-gated; rollback-aware; accessibility-aware
tags: [kfm, tests, fixtures, layers, LayerManifest, LayerDescriptor, LayerCatalogItem, MapReleaseManifest, KFMGeoManifest, RuntimeResponseEnvelope, ANSWER, ABSTAIN, DENY, ERROR, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, RollbackCard, trust-badges, maplibre, no-network]
related:
  - ../README.md
  - ../../README.md
  - ../../api/README.md
  - ../../ui/README.md
  - ../../runtime_proof/README.md
  - ../../../apps/explorer-web/src/features/layer_catalog/README.md
  - ../../../docs/architecture/ui/LAYERING.md
  - ../../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../../docs/architecture/publication/GEO_MANIFEST.md
  - ../../../contracts/release/map_release_manifest.md
  - ../../../contracts/release/release_manifest.md
  - ../../../contracts/release/layer_manifest.md
  - ../../../contracts/release/tile_artifact_manifest.md
  - ../../../contracts/data/layer_manifest.md
  - ../../../contracts/data/layer_descriptor.md
  - ../../../contracts/data/layer_catalog_item.md
  - ../../../contracts/map/map_release_manifest/README.md
  - ../../../schemas/contracts/v1/layers/
  - ../../../schemas/contracts/v1/release/
  - ../../../schemas/contracts/v1/runtime/
  - ../../../schemas/contracts/v1/evidence/
  - ../../../policy/layers/
  - ../../../policy/release/
  - ../../../policy/sensitivity/
  - ../../../data/registry/layers/
  - ../../../data/catalog/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/candidates/
  - ../../../release/manifests/
notes:
  - "This README replaces placeholder content at tests/fixtures/layers/README.md."
  - "This lane documents unit-test-scoped layer fixtures. It does not become a canonical layer, catalog, policy, release, tile, artifact, style, evidence, or public-map root."
  - "Layer fixtures must prove governed layer behavior with manifest refs, evidence refs, policy refs, release refs, rights/sensitivity state, accessibility state, and finite outcomes."
  - "Public clients must not load tiles, styles, sprites, glyphs, or layer state unless the material is governed, release-backed, and allowed by policy."
  - "Executable tests, fixture payload inventory, schema bindings, UI/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Layer test fixtures

> Test-local fixture documentation for layer, layer-catalog, layer-manifest, and map-release examples under `tests/fixtures/layers/`. This lane supports deterministic, no-network checks for governed layer behavior without turning examples into layer truth, source truth, evidence closure, policy approval, release approval, tile authority, style authority, or public map artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: layer fixtures" src="https://img.shields.io/badge/lane-layer__fixtures-purple">
  <img alt="Surface: layer catalog" src="https://img.shields.io/badge/surface-layer__catalog-0a7ea4">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release__gated-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/layers/README.md`  
**Status:** draft / placeholder replaced / layer test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/layers`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/README.md` allows `tests/fixtures/` only as unit-test-scoped fixtures and requires five fixture classes for `LayerManifest`, `LayerDescriptor`, and related governed objects; CONFIRMED Layer Catalog and MapReleaseManifest docs require governed API, manifest, evidence, rights, sensitivity, policy, release, correction, and rollback posture before public layer use; NEEDS VERIFICATION for executable tests, payload inventory, schema bindings, UI/runtime wiring, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/layers/` is the unit-test-scoped fixture lane for layer and layer-catalog examples.

Use this lane for synthetic fixtures that exercise governed layer behavior:

1. layer catalog state arrives through governed API projections;
2. `LayerCatalogItem`, `LayerDescriptor`, `LayerManifest`, `KFMGeoManifest`, and `MapReleaseManifest` refs are validated where material;
3. evidence, source role, rights, sensitivity, review, freshness, correction, release, and rollback posture remain visible;
4. sensitive layer exposure is transformed, generalized, delayed, restricted, denied, or withheld before public tile generation;
5. layer cards, map toggles, legends, Evidence Drawer launches, Compare/Export handoffs, and Focus scopes use governed refs only;
6. tile, style, sprite, glyph, raster, vector, or PMTiles/COG refs are digest-bound and release-backed before use;
7. every fixture has a finite expected state such as `PASS`, `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

A layer fixture should not mean that a layer is published, a map release exists, a source is authoritative, evidence is closed, a policy gate passed, a tile is safe, a style is safe, or public clients may load anything. It should mean only that a bounded synthetic input is expected to produce a bounded layer-test outcome.

[Back to top](#top)

---

## Placement basis

`tests/README.md` disambiguates fixture homes: `tests/fixtures/` is for unit-test-scoped fixtures local to a test's needs, while root `fixtures/` is for cross-cutting golden, valid, invalid, and synthetic fixtures shared across test areas and pipelines. This path is therefore a test-local fixture lane for layer checks, not a layer registry, release store, tile store, map artifact store, schema home, policy home, or public-map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Unit-test-scoped layer fixtures | `tests/fixtures/layers/` | This directory. |
| Layer catalog feature tests | `tests/ui/`, `tests/api/`, or feature-specific consumer tests | Expected consumers; not fixture authority. |
| Layer Catalog UI feature | `apps/explorer-web/src/features/layer_catalog/` | Downstream UI surface; not fixture authority. |
| Governed API layer responses | `apps/governed-api/` | Trust membrane and normal layer path; not owned here. |
| Layer contracts | `contracts/data/`, `contracts/release/`, `contracts/map/` | Defines meaning; not owned here. |
| Layer schemas | `schemas/contracts/v1/layers/`, `schemas/contracts/v1/release/`, runtime/evidence schema roots | Defines machine shape; not owned here. |
| Layer policy | `policy/layers/`, `policy/release/`, `policy/sensitivity/` | Admissibility authority; not owned here. |
| Layer registry/catalog | `data/registry/layers/`, `data/catalog/` | Discovery and catalog state; not owned here. |
| Proofs and receipts | `data/proofs/`, `data/receipts/` | Auditable trust artifacts; referenced only by synthetic refs. |
| Release decisions | `release/` roots | Publication, correction, withdrawal, and rollback authority; not owned here. |
| Published artifacts | `data/published/`, release/artifact roots, or accepted artifact stores | Public/restricted artifacts; not stored here. |

> [!IMPORTANT]
> Do not use this directory as a second layer registry, tile store, style store, release manifest store, evidence store, policy bundle, or public map artifact root. Fixtures here are test carriers only.

---

## Invariant under test

> **Layers are derived governed surfaces, not sovereign truth.** A layer fixture must preserve source, evidence, policy, rights, sensitivity, release, correction, rollback, artifact-integrity, and accessibility state instead of hiding them inside renderer styling.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | `tests/fixtures/layers/` remains unit-test-scoped and does not become layer authority. | drift entry / validation failure. |
| No-network boundary | Default fixtures do not call live source APIs, tile servers, style servers, CDN URLs, public APIs, model runtimes, or release services. | `ERROR`. |
| Governed API boundary | Layer catalog and layer state come through governed API projections or synthetic envelopes, not direct internal reads. | `DENY` / validation failure. |
| Manifest boundary | `LayerManifest`, `LayerDescriptor`, `LayerCatalogItem`, `KFMGeoManifest`, and `MapReleaseManifest` refs remain explicit where material. | `ABSTAIN` / validation failure. |
| Evidence boundary | Claim-bearing layer fixtures require synthetic EvidenceRef / EvidenceBundle support or abstain. | `ABSTAIN`. |
| Rights boundary | Unknown license, redistribution, attribution, embargo, or export posture fails closed. | `DENY` / `ABSTAIN`. |
| Sensitivity boundary | Exact sensitive geometry, restricted attributes, and style-only hiding fail closed. | `DENY`. |
| Release boundary | Public-selectable layers require release state, rollback target, correction lineage, and policy refs. | `DENY` / release block. |
| Artifact-integrity boundary | Tile/style/sprite/glyph/COG/PMTiles refs are digest-bound in fixtures when material. | validation failure. |
| Accessibility boundary | Trust badges, denial states, legends, and layer controls are testable without color-only semantics. | validation failure. |

---

## Expected fixture families

| Family | Purpose | Expected outcome |
|---|---|---|
| `layer_catalog_item_valid` | Public-safe layer catalog item with release/evidence/policy refs. | `PASS` / `ANSWER`. |
| `layer_catalog_item_denied` | Layer card is visible only as denied/unavailable or absent due to policy. | `DENY`. |
| `layer_manifest_valid` | Layer manifest refs resolve and carry valid release/evidence/rights/sensitivity state. | `PASS`. |
| `layer_manifest_missing_evidence` | Claim-bearing layer lacks resolvable evidence. | `ABSTAIN`. |
| `layer_manifest_unknown_rights` | Rights/license/redistribution state is unknown. | `DENY` / `ABSTAIN`. |
| `layer_manifest_sensitive_exact_geometry` | Exact sensitive geometry would leak or style-only hiding is attempted. | `DENY`. |
| `map_release_manifest_valid` | Map release refs artifacts, layer manifests, rights, sensitivity, policy, attestations, correction, rollback. | `PASS`. |
| `map_release_manifest_missing_rollback` | Map release lacks rollback target or invalidation plan. | `DENY` / release block. |
| `tile_artifact_digest_missing` | PMTiles/COG/tile/style refs lack digest/integrity binding. | `ERROR` / validation failure. |
| `layer_catalog_a11y_state` | Trust badges, legend, and disabled states expose non-color labels. | `PASS` / validation failure. |

---

## Accepted material

Only bounded, synthetic, reviewable material belongs in this lane:

- small layer catalog, layer manifest, layer descriptor, geo manifest, tile artifact, style, legend, trust badge, and map-release fixture examples
- synthetic `LayerCatalogItem`, `LayerDescriptor`, `LayerManifest`, `KFMGeoManifest`, `TileArtifactManifest`, `MapReleaseManifest`, `ReleaseManifest`, `RuntimeResponseEnvelope`, `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- expected-output examples for layer states such as released, denied, abstain, error, stale, degraded, withdrawn, corrected, generalized, restricted, delayed, disabled, and rollback-visible
- negative canaries for direct raw reads, unreleased layer loading, unknown rights, missing evidence, missing rollback, missing attestation, missing digest, sensitive exact geometry, style-only hiding, browser-to-internal-store access, and color-only trust badge failures
- toy artifact refs, toy layer refs, toy source refs, toy release refs, toy digests, toy URLs, toy timestamps, toy zoom ranges, toy CRS values, toy legend classes, and toy policy refs

Safe outputs may include fixture ID, layer ID, domain label, source role, trust badge labels, manifest refs, evidence refs, policy refs, release refs, correction refs, rollback refs, artifact digests, expected outcome, expected reason code, and no-network posture.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, public payloads, or public layer payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Real PMTiles, COGs, MVT/MLT/vector tiles, tilejson, style JSON, sprites, glyphs, rasters, GeoParquet, or 3D Tiles | Artifacts belong in governed artifact/release/published homes, not tests. |
| Real `LayerManifest`, `MapReleaseManifest`, `ReleaseManifest`, `PolicyDecision`, `EvidenceBundle`, proof, receipt, signature, or attestation records | Governed trust and release records belong in their own roots. |
| Exact sensitive geometry, living-person data, DNA/genomic material, rare-species coordinates, archaeological site geometry, critical-infrastructure detail, or private property/person joins | Sensitive material must fail closed and be represented only by synthetic denial canaries. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, graph stores, vector indexes, public APIs, tile servers, or model runtime outputs | Bypasses the trust membrane and no-network posture. |
| Secrets, credentials, private endpoints, telemetry with restricted content, or access tokens | Security and exposure risk. |
| Binding policy rules, schema definitions, contract prose, release procedures, pipeline implementation, connector implementation, map renderer implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/layers/
|-- README.md
|-- layer_catalog_item.valid.json
|-- layer_catalog_item.denied.json
|-- layer_manifest.valid.json
|-- layer_manifest.missing_evidence.abstain.json
|-- layer_manifest.unknown_rights.deny.json
|-- layer_manifest.sensitive_exact_geometry.deny.json
|-- map_release_manifest.valid.json
|-- map_release_manifest.missing_rollback.deny.json
|-- tile_artifact_digest_missing.error.json
|-- layer_catalog_a11y_state.valid.json
`-- expected_reason_codes.json
```

This layout is PROPOSED until executable files and consumers exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/api tests/ui tests/runtime_proof tests/fixtures/layers
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no direct tile/CDN/style/glyph/sprite fetches, no direct model runtime calls, no real secrets, no production logs, no production trust artifacts, no exact sensitive geometry, no public artifact writes, deterministic fixture inputs, and finite outcomes only.

---

## Minimal layer fixture manifest

Synthetic manifests should describe fixture expectations without carrying real layer data or artifacts.

```json
{
  "fixture_manifest_id": "layers-fixture-layer-catalog-item-valid",
  "fixture_family": "layer_catalog_item_valid",
  "expected_outcome": "PASS",
  "layer_catalog_item_ref": "layer:synthetic:catalog-item:public-safe-example",
  "layer_manifest_ref": "layer:synthetic:manifest:public-safe-example",
  "evidence_refs": [
    "evidence:synthetic:layer:public-safe-example"
  ],
  "policy_decision_ref": "policy:synthetic:layers:allow-public-safe-example",
  "release_ref": "release:synthetic:map:public-safe-example",
  "rollback_ref": "rollback:synthetic:map:public-safe-example",
  "network": "disabled",
  "uses_real_source_data": false,
  "uses_real_artifacts": false,
  "authorizes_publication": false
}
```

For denial cases, make the denial explicit without carrying the restricted value:

```json
{
  "fixture_manifest_id": "layers-fixture-sensitive-exact-geometry-deny",
  "fixture_family": "layer_manifest_sensitive_exact_geometry",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "SENSITIVE_EXACT_GEOMETRY_BLOCKED",
    "STYLE_ONLY_HIDING_FORBIDDEN"
  ],
  "layer_manifest_ref": "layer:synthetic:manifest:sensitive-exact-denied",
  "policy_decision_ref": "policy:synthetic:layers:deny-sensitive-exact-geometry",
  "network": "disabled",
  "uses_real_source_data": false,
  "uses_real_artifacts": false,
  "authorizes_publication": false
}
```

---

## Finite outcome expectations

| Outcome | Meaning in this lane | Example |
|---|---|---|
| `PASS` | The synthetic fixture satisfies a bounded test expectation. | Valid layer manifest wrapper with refs and no artifacts. |
| `ANSWER` | Runtime-oriented fixture has released/evidence-backed, policy-allowed layer context. | Layer Catalog card may render enabled public-safe state. |
| `ABSTAIN` | Evidence, citation, rights, release, freshness, review, or manifest support is insufficient. | Layer claim lacks EvidenceRef. |
| `DENY` | Policy, rights, sensitivity, release, source-role, exact geometry, missing rollback, or style-only hiding blocks exposure. | Sensitive exact geometry layer request. |
| `ERROR` | Fixture, loader, schema, digest, manifest, or test setup is malformed or non-deterministic. | Tile artifact ref missing required digest. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, public-safe, and no-network
- [ ] no real tiles, styles, sprites, glyphs, rasters, PMTiles, COGs, or public payloads are present
- [ ] every fixture declares expected outcome, reason code where applicable, and no-network posture
- [ ] layer refs, evidence refs, policy refs, release refs, correction refs, rollback refs, and artifact digests are explicit where material
- [ ] unknown rights, unresolved evidence, missing policy, missing release state, missing rollback target, missing attestation, and sensitive exact geometry fail closed
- [ ] style filters are never used as the sensitive-geometry redaction mechanism
- [ ] Layer Catalog fixtures expose non-color trust state and accessibility labels where UI-facing
- [ ] release-shaped refs remain synthetic and do not authorize publication
- [ ] docs, tests, schemas, contracts, policies, governed API routes, UI consumers, and release gates are updated when layer behavior changes

---

## Change discipline

Changes to this lane should be small, inspectable, and reversible.

| Change type | Required action |
|---|---|
| Add a valid layer fixture | Include manifest refs, evidence refs, policy refs, release refs, rollback refs, and artifact digest posture. |
| Add an abstention fixture | State missing evidence, citation, rights, release, review, freshness, or manifest support. |
| Add a denial fixture | State the policy/sensitivity/release/source-role/accessibility reason without exposing restricted values. |
| Add an error fixture | Make the malformed schema, missing digest, invalid manifest, or loader failure explicit. |
| Add a UI-facing fixture | Include trust badge labels, keyboard/screen-reader state, and non-color state expectations. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real artifacts or sensitive data | Move them out, quarantine through the governed lifecycle or registry process, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Exact path search: no direct repo search hit for `tests/fixtures/layers/` beyond this placeholder during authoring; this lane is therefore documented as PROPOSED test-local fixture posture.
- Test-root alignment: verified against `tests/README.md` for tests as enforceability proof, optional `tests/fixtures/` split, five-fixture rule, forbidden boundaries, sensitive-fixture safeguards, and deterministic no-network default.
- MapReleaseManifest alignment: verified against `contracts/release/map_release_manifest.md` for map-publication envelope semantics, artifact refs/digests, evidence, rights, sensitivity, policy, attestations, correction lineage, rollback, lifecycle role, validation expectations, and exclusions.
- Layer Catalog alignment: verified against `apps/explorer-web/src/features/layer_catalog/README.md` for governed API-only catalog state, trust badges, finite layer states, sensitive-layer handling, exclusions, accessibility posture, and forbidden RAW/WORK/QUARANTINE/internal-store access.
- Contract/schema alignment: NEEDS VERIFICATION against layer, release, runtime, evidence, and policy schemas.
- Consumer alignment: NEEDS VERIFICATION against Layer Catalog tests, governed-API tests, map runtime tests, Evidence Drawer checks, Compare/Export handoff checks, release-manifest checks, policy checks, sensitivity checks, rights checks, source-role checks, artifact-integrity checks, accessibility checks, rollback drills, renderer checks, and CI coverage.
- Tests and validators: NOT RUN.
