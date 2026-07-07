<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-maplibre-readme
title: MapLibre Tests README
type: test-readme
version: v0.1
status: draft; placeholder-replaced; maplibre-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Map steward
  - OWNER_TBD - MapLibre steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; maplibre; renderer-boundary; no-network; synthetic-only; release-gated; policy-aware; evidence-aware; public-safe
tags: [kfm, tests, maplibre, renderer-boundary, map-tests, visual-regression, MapReleaseManifest, LayerManifest, TileArtifactManifest, no-network, ABSTAIN, DENY, ERROR, rollback]
related:
  - ../README.md
  - ../fixtures/README.md
  - ../fixtures/maplibre/README.md
  - ../../packages/maplibre/README.md
  - ../../docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md
  - ../../docs/architecture/ui/README.md
  - ../../docs/architecture/ui/BOUNDARIES.md
  - ../../docs/architecture/map-shell.md
  - ../../contracts/release/map_release_manifest.md
  - ../../contracts/data/layer_manifest.md
  - ../../schemas/contracts/v1/layers/
  - ../../policy/layers/
  - ../../release/
notes:
  - "This README replaces placeholder content at tests/maplibre/README.md."
  - "The root tests/README.md does not currently list tests/maplibre/ in its proposed test tree; packages/maplibre/README.md names tests/packages/maplibre/ or repo-confirmed equivalents as expected test homes. This lane is therefore PROPOSED / NEEDS VERIFICATION until placement is accepted."
  - "This lane documents executable MapLibre-focused tests, not MapLibre fixtures. Fixture payloads belong under tests/fixtures/maplibre/ or root fixtures/ as appropriate."
  - "MapLibre tests must prove renderer-boundary behavior without turning MapLibre, screenshots, styles, tiles, or visual baselines into truth, evidence, policy, release, or publication authority."
  - "Executable test inventory, actual runner/framework, fixture consumption, schema bindings, policy/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre tests

> Test-lane README for MapLibre-focused renderer-boundary checks under `tests/maplibre/`. This lane is for executable or test-owned checks that prove MapLibre-facing descriptors, fixtures, baselines, and render-admission behavior stay downstream of governed evidence, policy, release, and artifact manifests.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: MapLibre tests" src="https://img.shields.io/badge/lane-maplibre__tests-purple">
  <img alt="Renderer: downstream" src="https://img.shields.io/badge/renderer-downstream__only-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/maplibre/README.md`  
**Status:** draft / placeholder replaced / MapLibre test lane / PROPOSED until placement and executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `maplibre`  
**Fixture companion:** `tests/fixtures/maplibre/`  
**Default posture:** deterministic, synthetic, no-network, public-safe tests only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/` is the canonical enforceability root; CONFIRMED `tests/fixtures/maplibre/` exists as a unit-test-scoped fixture lane; NEEDS VERIFICATION for whether `tests/maplibre/` is the accepted executable test home versus `tests/packages/maplibre/`, plus test inventory, runner, schema bindings, CI coverage, and pass rates.

---

## Scope

Use `tests/maplibre/` for executable MapLibre-focused tests when the repository accepts this path as the test home or compatibility lane.

In scope:

- descriptor validation checks for source, layer, style, tile, sprite, glyph, and map-release refs;
- no-network renderer-admission checks;
- MapReleaseManifest, LayerManifest, StyleManifest, TileArtifactManifest, rollback, and correction-ref checks;
- tests that prove unmanifested tile/style/sprite/glyph loads fail;
- tests that prove screenshots, rendered maps, visual baselines, and style JSON are downstream review aids only;
- tests for invalid, denied, stale, withdrawn, unreleased, unsigned, rollback-missing, and policy-blocked renderer states;
- tests that consume synthetic fixtures from `tests/fixtures/maplibre/`.

Out of scope:

- MapLibre helper implementation;
- UI component implementation;
- fixture payload collections;
- style or tile authority;
- release decisions;
- schema, contract, or policy definitions;
- real map artifacts, screenshots, tiles, PMTiles, COGs, source exports, secrets, or public payloads.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| MapLibre executable tests | `tests/maplibre/` | This PROPOSED lane; placement NEEDS VERIFICATION. |
| Alternate package-specific test home | `tests/packages/maplibre/` if adopted | Mentioned by package README as an expected home or equivalent. |
| MapLibre unit-test fixtures | `tests/fixtures/maplibre/` | Fixture inputs; not executable tests. |
| Shared MapLibre helper code | `packages/maplibre/` | Implementation; not owned here. |
| UI implementation | `apps/explorer-web/`, `packages/ui/`, or accepted UI roots | Consumers; not owned here. |
| Semantic contracts | `contracts/` | Meaning authority; tests verify, not define. |
| Machine schemas | `schemas/` | Shape authority; tests verify, not define. |
| Policy gates | `policy/` | Admissibility authority; tests assert behavior. |
| Release decisions | `release/` | Publication authority; tests can block promotion but do not approve release. |
| Map artifacts | governed artifact/data/release homes | Not stored here. |

> [!IMPORTANT]
> `tests/maplibre/` must not become a renderer implementation home, fixture payload archive, screenshot archive, tile/style store, schema home, policy home, release store, evidence store, or public map artifact root.

---

## Placement note

`tests/README.md` lists core test lanes such as `tests/ui/`, `tests/e2e/`, `tests/runtime_proof/`, and `tests/domains/`, but does not list `tests/maplibre/` in the proposed tree. `packages/maplibre/README.md` names `tests/packages/maplibre/`, `fixtures/packages/maplibre/`, or repo-confirmed equivalents as expected proof homes. Because the requested path exists as a placeholder, this README treats `tests/maplibre/` as a repo-confirmed placeholder and PROPOSED executable test lane pending placement review.

If maintainers later choose `tests/packages/maplibre/` as canonical, this README should either redirect there or be reduced to a compatibility pointer.

---

## Test rule

MapLibre tests prove renderer-boundary discipline. They do not prove map truth, source authority, evidence closure, policy approval, release approval, or publication.

Core expectations:

| Expectation | Required posture |
|---|---|
| No-network default | No live source, API, tile, style, glyph, sprite, CDN, model, or public-service calls. |
| Manifest-gated assets | Tile, style, sprite, glyph, and layer refs must be listed in governed manifests where material. |
| Renderer downstream | MapLibre consumes governed descriptors; it does not create truth, policy, evidence, or release. |
| Fixture separation | Payload examples belong under `tests/fixtures/maplibre/` or root `fixtures/` when shared. |
| Finite outcomes | Expected outcomes remain explicit: `PASS`, `ABSTAIN`, `DENY`, `ERROR`, validation failure, or review-required. |
| Sensitive fail-closed | Exact sensitive detail and unsafe public geometry deny before tile build or public release. |
| Rollback visible | Public-facing renderer state preserves correction and rollback posture where material. |

---

## Expected test families

| Family | What it proves | Expected outcome |
|---|---|---|
| `descriptor_valid` | Valid synthetic source/layer/style descriptor can be accepted as a renderer candidate. | `PASS`. |
| `descriptor_invalid` | Malformed or incomplete descriptor is rejected. | validation failure / `ERROR`. |
| `unmanifested_asset` | Tile/style/sprite/glyph ref missing from release manifest is blocked. | `DENY` / validation failure. |
| `unreleased_layer` | Candidate or unreleased layer cannot render as public-current. | `DENY`. |
| `stale_or_withdrawn_layer` | Stale, withdrawn, or superseded state remains visible and non-current. | `PASS` / review-required. |
| `sensitive_geometry_deny` | Unsafe exact detail is denied before tile or public release. | `DENY`. |
| `baseline_matches` | Expected baseline remains deterministic. | `PASS`. |
| `bad_baseline_fails` | Bad baseline canary fails or requires review. | validation failure / review-required. |
| `screenshot_not_truth` | Screenshot/rendered output is not treated as evidence, proof, or release. | validation failure if promoted. |
| `rollback_missing` | Public renderer candidate lacking rollback posture is rejected. | `ERROR` / validation failure. |

---

## Accepted inputs

Accepted material is limited to executable tests, test notes, and tiny inline synthetic values when they are too small to justify a separate fixture file.

Preferred inputs should be referenced from:

- `tests/fixtures/maplibre/tiny/` for smoke inputs;
- `tests/fixtures/maplibre/baselines/` for expected renderer baselines;
- `tests/fixtures/maplibre/invalid/` for malformed/fail-closed cases;
- `tests/fixtures/maplibre/bad-baselines/` for bad baseline canaries;
- root `fixtures/` only when a cross-cutting reusable fixture is intentionally shared.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| MapLibre helper code | `packages/maplibre/` |
| fixture payload collections | `tests/fixtures/maplibre/` or root `fixtures/` |
| UI component code | `apps/`, `packages/ui/`, or accepted UI roots |
| contracts | `contracts/` |
| schemas | `schemas/` |
| policy rules | `policy/` |
| release manifests, correction notices, rollback cards | `release/` roots |
| tiles, PMTiles, COGs, screenshots, sprites, glyphs, style archives, public exports | governed artifact/data/release roots only |
| source data, lifecycle data, secrets, production logs, exact sensitive detail, direct model output | not allowed in repository tests |

---

## Suggested layout

```text
tests/maplibre/
|-- README.md
|-- descriptor_valid.test.PROPOSED
|-- descriptor_invalid.test.PROPOSED
|-- unmanifested_asset.test.PROPOSED
|-- unreleased_layer.test.PROPOSED
|-- stale_or_withdrawn_layer.test.PROPOSED
|-- sensitive_geometry_deny.test.PROPOSED
|-- baseline_matches.test.PROPOSED
|-- bad_baseline_fails.test.PROPOSED
|-- screenshot_not_truth.test.PROPOSED
`-- rollback_missing.test.PROPOSED
```

The layout is schematic. Actual test filenames, extensions, package manager, runner, and framework remain NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/maplibre
```

Default runs should be deterministic, local, no-network, public-safe, and finite-outcome only. Replace the command once the repo's actual test runner and naming convention are verified.

---

## Maintenance checklist

- [ ] Confirm whether `tests/maplibre/` or `tests/packages/maplibre/` is the accepted executable test home.
- [ ] Keep fixture payloads in `tests/fixtures/maplibre/` unless an inline value is minimal and synthetic.
- [ ] Assert manifest-gated tile/style/sprite/glyph loading where material.
- [ ] Assert MapLibre remains downstream of governed evidence, policy, release, review, correction, and rollback posture.
- [ ] Assert screenshots and rendered outputs never become evidence, proof, release, policy, or truth authority.
- [ ] Do not store real source data, public artifacts, release records, schemas, contracts, policy rules, app code, renderer code, secrets, production logs, or direct model output here.
- [ ] Link each test to its fixture and manifest/policy/contract/schema source after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| Root `tests/` authority | CONFIRMED as canonical enforceability root. |
| Placement of `tests/maplibre/` | NEEDS VERIFICATION; not listed in the proposed `tests/README.md` tree. |
| `tests/fixtures/maplibre/` companion lane | CONFIRMED during authoring. |
| `packages/maplibre/` boundary | CONFIRMED as helper package, not truth/release/policy authority. |
| Executable test inventory | NEEDS VERIFICATION. |
| Actual runner/framework | NEEDS VERIFICATION. |
| Fixture consumption | NEEDS VERIFICATION. |
| Schema bindings | NEEDS VERIFICATION. |
| Policy/runtime wiring | NEEDS VERIFICATION. |
| CI wiring and pass rates | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
