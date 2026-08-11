<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/fauna/tiles/readme
title: Fauna Tiles Test Lane README
type: test-lane-readme
version: v1.0.0
status: draft; one bounded executable field-name slice
owners: OWNER_TBD — Fauna steward · Map/UI steward · Release steward · Test steward
created: 2026-07-05
updated: 2026-08-11
policy_label: public
implementation_status: bounded fixture-only field-name allowlist executable; actual tile-byte and release validation held
verification_status: policy/schema/validator/fixtures/tests/workflow confirmed in-tree; local execution recorded in draft PR; hosted CI needs verification
owning_root: tests/
responsibility: Document Fauna tile conformance scope and the bounded inactive field-name executable while holding byte-level, geometry, value, manifest, release, and publication proof.
truth_posture: "CONFIRMED local field-name fixture proof; PROPOSED broader tile test lane; UNKNOWN production artifacts and consumers; NEEDS VERIFICATION human review and hosted CI"
related:
  - tests/README.md
  - tests/domains/fauna/README.md
  - tests/domains/fauna/layers/README.md
  - tests/domains/fauna/release/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - docs/domains/fauna/SENSITIVITY.md
  - data/published/layers/fauna/
  - fixtures/domains/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - data/receipts/
  - data/proofs/fauna/
tags:
  - kfm
  - tests
  - fauna
  - tiles
  - tile-artifact
  - tile-manifest
  - field-allowlist
  - map-ui
  - release
  - integrity
  - no-network
  - fail-closed
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Tiles Tests

> Test-lane contract for proving Fauna tile artifacts are public-safe, release-bound, manifest-backed, integrity-checkable, field-limited, and downstream of governed release and policy controls.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Ffauna%2Ftiles-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Ffauna%2Ftiles-informational)
![authority: tests--only](https://img.shields.io/badge/authority-tests--only-lightgrey)
![posture: fail--closed](https://img.shields.io/badge/posture-fail--closed-blue)
![implementation: bounded field names](https://img.shields.io/badge/implementation-bounded--field--names-orange)

**Status:** `draft`  
**Authority:** tile test-lane README; not a tile store, tile artifact, layer manifest, release manifest, schema, policy bundle, fixture inventory, receipt, proof, or public artifact  
**Owning root:** `tests/`  
**Domain segment:** `domains/fauna/`  
**Lane:** `tiles/`  
**Default posture:** public-safe fixtures; no-network by default; finite outcomes; fail closed when tile safety or release context is unresolved  
**Last reviewed:** 2026-08-11

---

## 1. Purpose

This directory is the Fauna domain test lane for **tile behavior**.

It exists to prove that Fauna map tiles are downstream public carriers, not evidence, policy, release, or truth authority. A tile may support a public map only when the tile artifact is produced from public-safe inputs, governed by release state, backed by a manifest, field-limited, integrity-checkable, and unable to leak policy-withheld material through encoded properties, geometry, metadata, cache state, screenshots, or exports.

A mature lane should prove:

1. Public Fauna tiles load only through governed release/layer/tile manifests.
2. Tile properties obey an explicit public field allowlist.
3. Tile artifacts do not contain fields or geometry classes that policy says must not reach public clients.
4. Tile digests, artifact identifiers, release links, and rollback targets are present where required.
5. Renderer styling is not treated as tile protection.
6. Stale, withdrawn, superseded, denied, or unreleased tile artifacts cannot be served as current public truth.
7. Tests use deterministic public-safe fixtures and no live tile services by default.

---

## 2. Directory fit and authority

Directory Rules place domain-specific tests under the `tests/` responsibility root with the domain as a segment:

```text
tests/domains/fauna/tiles/
```

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove Fauna tile behavior. |
| Owning root | `tests/` |
| Domain segment | `domains/fauna/` |
| Test lane | `tiles/` |
| Published artifact home | `data/published/layers/fauna/` when present. |
| Fixture home | `fixtures/domains/fauna/` unless tiny test-local examples are documented. |
| Policy homes | `policy/domains/fauna/` and `policy/sensitivity/fauna/`. |
| Receipt/proof homes | `data/receipts/` and `data/proofs/`. |
| Release home | `release/`. |
| Documentation reference | `docs/domains/fauna/MAP_UI_CONTRACTS.md`. |

> [!WARNING]
> This directory must not become a second tile store, published-artifact home, layer registry, release home, fixture home, policy home, receipt home, proof home, or source-data home.

[↑ Back to top](#top)

---

## 3. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| `tests/README.md` allows release-manifest, lifecycle, policy, governed API, UI trust-state, and domain-specific tests | CONFIRMED from current repo docs. |
| `tests/README.md` excludes sensitive exact data and live network calls from default tests | CONFIRMED from current repo docs. |
| Fauna Map UI contract says renderer and tiles are downstream carriers, not truth or release authority | CONFIRMED from current repo docs. |
| Fauna Map UI contract says public clients must not read internal lifecycle stores | CONFIRMED from current repo docs. |
| Fauna Map UI contract names tile field allowlist testing for Fauna tiles | CONFIRMED from current repo docs. |
| Inactive field-name allowlist executable | CONFIRMED: policy, schema, validator, synthetic cases, focused unit tests, and workflow definition are present. |
| Actual PMTiles/MVT/MLT byte inspection | NOT IMPLEMENTED / HOLD. |
| Actual TileArtifactManifest, release, digest, rollback, geometry, value, size, and cache validation | NEEDS VERIFICATION / HOLD. |
| Focused CI job | CONFIRMED definition: `fauna-tile-field-allowlist`; hosted run NEEDS VERIFICATION until the PR check completes. |

This README defines the broader test-lane contract and records one implemented subset. The executable compares synthetic property names with a candidate `LayerManifest` allowlist and an inactive domain policy. It does not inspect tile bytes or prove that a tile artifact, manifest, release, or public consumer exists.

---

## 4. Tile rule

**Rule:** A Fauna tile may be served to a public client only when its manifest, release state, policy state, field allowlist, integrity hook, and rollback target are valid for the tested scope.

Tests should fail or require a finite negative outcome when:

- a tile lacks a governed artifact manifest or release link;
- a tile lacks an integrity hook, digest, artifact ID, or rollback reference where required;
- a public tile contains non-public fields or unapproved geometry detail;
- renderer style is the only thing preventing exposure;
- a candidate, work, quarantine, processed, catalog, internal, withdrawn, or superseded tile is served as current public state;
- a public tile bypasses governed API or release/layer manifests;
- tile metadata treats renderer output as evidence;
- stale tile support is served without trust-visible state; or
- tests store production tiles, source data, or trust-bearing release records under `tests/`.

Tests may allow a tile only when the fixture is public-safe, policy permits it, required governance references are present, and the test remains inside its validation scope.

---

## 5. Proof matrix

| Test concern | Required proof | Expected behavior |
|---|---|---|
| Tile manifest required | Tile fixture links to governed tile/layer/release metadata. | Schema/validator assertion. |
| Public field allowlist | Tile properties contain only allowed public fields. | Allowlist assertion. |
| Policy-restricted fields absent | Non-public fields do not appear in encoded tile data. | Validation failure if present. |
| Geometry safety | Public tile geometry is already public-safe before rendering. | Policy/tile assertion. |
| Style is not protection | Style filter alone cannot make unsafe tile public. | Test failure. |
| Integrity hook | Digest or comparable artifact integrity field is present where required. | Manifest assertion. |
| Release state | Candidate, withdrawn, superseded, or unreleased tile cannot serve as current public truth. | `DENY`, `ABSTAIN`, `ERROR`, or validation failure. |
| Rollback target | Public tile release has rollback target where required. | Release assertion. |
| API/UI boundary | Public client does not load internal lifecycle files directly. | Boundary assertion. |
| No-network default | Tests use deterministic local public-safe fixtures only. | Harness guard. |

---

## 6. What belongs here

This directory may contain:

- README and lane contract material for Fauna tile tests.
- Tests that call canonical tile, layer, release, policy, and validator code from owning roots.
- Negative tests for missing manifests, missing integrity hooks, missing rollback targets, non-public fields, unsafe geometry, stale tiles, and unreleased tiles.
- Positive tests for public-safe tile fixtures with required governance references.
- Public-safe test-local examples when they are tiny, deterministic, and not reusable fixture inventory.

## 7. What does not belong here

This directory must not contain production tiles, PMTiles, GeoJSON/GeoParquet public artifacts, source records, reusable fixture inventories, receipts, proofs, release decisions, policy definitions, schemas, credentials, or default tests that require live network access.

---

## 8. Fixture posture

Reusable fixtures should normally live under:

```text
fixtures/domains/fauna/
```

Fixture records should be deterministic, public-safe, no-network, and clearly test-only. They should model tile-governance states rather than include production tiles or live source material.

Expected fixture families include valid public tile metadata, missing manifest, missing digest, missing rollback target, forbidden field, unsafe geometry class, style-only protection, stale tile, withdrawn tile, superseded tile, and public-safe allowed tile.

---

## 9. Local commands for the bounded slice

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_tile_field_allowlist.py' \
  --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/fauna/tiles/validate_tile_field_allowlist.py \
  --fixtures
```

---

## 10. Open questions

| Question | Status | Notes |
|---|---|---|
| What is the canonical TileArtifactManifest schema/path? | NEEDS VERIFICATION | Must inspect map/release schema roots. |
| Which validator command owns the inactive field-name slice? | RESOLVED FOR FIXTURES | `tools/validators/domains/fauna/tiles/validate_tile_field_allowlist.py --fixtures`; production build-gate ownership remains open. |
| Which field-name fixture family exists? | RESOLVED FOR THIS SLICE | `fixtures/domains/fauna/layers/tile_field_allowlist_cases.json`. |
| Which published tile artifact paths exist on `main`? | NEEDS VERIFICATION | Must inspect `data/published/layers/fauna/`. |
| Which CI job runs the bounded slice? | RESOLVED IN DEFINITION / HOSTED RUN PENDING | `.github/workflows/fauna-tile-field-allowlist.yml`. |
| Should shared tile-manifest tests live here or under a cross-domain map/tile test root? | OPEN | This lane should own Fauna-specific expectations only. |

---

## 11. Definition of done

This lane is mature when:

- [x] A deterministic no-network field-name allowlist test runs locally.
- [x] Synthetic cases cover a valid candidate, forbidden coordinates, observer identity, style-only protection, missing click-to-evidence field, manifest mismatch, manifest policy overreach, and authority elevation.
- [x] Tests call the canonical inactive profile and repository validator rather than redefining allowlist behavior locally.
- [ ] Actual tile properties are enumerated from bounded PMTiles/MVT/MLT artifacts.
- [ ] Missing manifest, missing digest, missing rollback target, forbidden field, unsafe geometry, stale tile, withdrawn tile, and superseded tile cases are tested.
- [ ] Positive public-safe fixtures prove allowed tile behavior without becoming publication approval.
- [ ] Tests call canonical tile/layer/release/policy validators rather than redefining behavior locally.
- [ ] Public-safe fixtures are used and verified no-network.
- [ ] CI exposes the Fauna tile proof clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 12. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-08-11 | v1.0.0 | Recorded the bounded inactive field-name allowlist policy/schema/validator/fixture/test/workflow slice and kept actual tile/release validation held. |
| 2026-07-05 | v0.1 | Initial governed README for the Fauna tiles test lane. |

---

## 13. Last reviewed

**2026-08-11** — Confirmed one inactive, synthetic, field-name-only executable slice. Actual tile bytes, values, geometry, artifact manifests, release bindings, published artifact paths, cache behavior, and hosted CI outcome remain **NEEDS VERIFICATION** or `HOLD`.

[↑ Back to top](#top)
