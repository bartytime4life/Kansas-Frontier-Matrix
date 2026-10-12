<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-maplibre-invalid-readme
title: MapLibre Invalid Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Map steward
  - OWNER_TBD - UI steward
  - OWNER_TBD - MapLibre steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; maplibre; invalid; synthetic-only; no-network; renderer-not-truth; release-gated
tags: [kfm, tests, fixtures, maplibre, invalid, visual-regression, renderer-boundary, release-gated, no-network, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../baselines/README.md
  - ../bad-baselines/README.md
  - ../../../domains/fauna/visual/README.md
  - ../../../../docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md
  - ../../../../apps/explorer-web/src/features/layer_catalog/README.md
  - ../../../../packages/maplibre/
  - ../../../../release/
notes:
  - "This README replaces placeholder content at tests/fixtures/maplibre/invalid/README.md."
  - "This lane documents invalid MapLibre fixture cases. It is not a renderer implementation, screenshot archive, release store, evidence store, policy home, or public map root."
  - "Expected valid baselines belong under ../baselines/. Intentionally bad visual baselines belong under ../bad-baselines/."
  - "Executable tests, payload inventory, runner wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre invalid test fixtures

> Unit-test-scoped fixture lane for malformed, incomplete, rejected, or fail-closed MapLibre fixture cases. This README keeps invalid examples useful for tests without turning renderer outputs, screenshots, styles, tiles, or baselines into truth authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Renderer: MapLibre" src="https://img.shields.io/badge/renderer-MapLibre-0a7ea4">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/maplibre/invalid/README.md`  
**Status:** draft / placeholder replaced / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/maplibre/invalid`  
**Sibling lanes:** `../baselines/`, `../bad-baselines/`  
**Default posture:** deterministic, synthetic, no-network, public-safe invalid fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED sibling baseline lanes exist; CONFIRMED `tests/fixtures/` is unit-test-scoped; NEEDS VERIFICATION for executable tests, payload inventory, runner wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/fixtures/maplibre/invalid/` for MapLibre fixture examples that should fail validation, abstain, deny, or error before normal rendering or visual-baseline approval.

Invalid fixtures are useful when they prove that the test harness rejects unsafe or incomplete inputs. They are not expected baselines, release records, style authority, renderer implementation, or public artifacts.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Invalid MapLibre fixture cases | `tests/fixtures/maplibre/invalid/` | This lane. |
| Expected valid baselines | `tests/fixtures/maplibre/baselines/` | Sibling lane. |
| Intentionally bad visual baselines | `tests/fixtures/maplibre/bad-baselines/` | Sibling negative lane. |
| Visual and UI tests | `tests/` consumer lanes | Consumers, not fixture authority. |
| Renderer implementation | `packages/maplibre/` | Not owned here. |
| UI implementation | `apps/explorer-web/`, `packages/ui/` | Not owned here. |
| Release decisions | `release/` | Not owned here. |
| Architecture references | `docs/` | Human-facing doctrine and design context. |

---

## Invalid fixture rule

> [!IMPORTANT]
> Invalid fixtures should fail loudly and early. A fixture in this lane should never be silently promoted into an expected baseline or public rendering path.

Core invalid classes:

| Invalid class | Expected result |
|---|---|
| malformed manifest shape | `ERROR` |
| missing layer or release reference | `ABSTAIN` / validation failure |
| missing expected outcome | validation failure |
| non-deterministic viewport or clock | `ERROR` / review required |
| live network dependency in default run | `ERROR` |
| missing trust-state labels | validation failure |
| unsupported renderer option | `ERROR` |
| unresolved policy or release posture | `DENY` / `ABSTAIN` |
| screenshot treated as evidence or release proof | validation failure |
| public render path attempts direct internal read | `DENY` / validation failure |

---

## Accepted inputs

Accepted material is limited to compact synthetic invalid examples, such as:

- small `*.json`, `*.yaml`, `*.yml`, or `*.md` fixture notes;
- toy layer refs, toy release refs, toy viewport refs, toy digests, and toy timestamps;
- invalid manifest examples that are safe to review;
- reason-code examples for `ABSTAIN`, `DENY`, `ERROR`, or validation failure;
- links to consumer tests when those tests are verified.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| valid expected baselines | `../baselines/` |
| intentionally bad visual-baseline canaries | `../bad-baselines/` |
| renderer implementation | `packages/maplibre/` or accepted renderer root |
| UI implementation | `apps/explorer-web/` or `packages/ui/` |
| release records | `release/` |
| real map artifacts or retained review outputs | governed artifact or release roots |
| policy rules or schemas | `policy/` and `schemas/` |
| production data, secrets, or public payloads | not allowed in this fixture lane |

---

## Suggested layout

```text
tests/fixtures/maplibre/invalid/
|-- README.md
|-- malformed_manifest.invalid.json
|-- missing_layer_ref.invalid.json
|-- missing_release_ref.invalid.json
|-- missing_expected_outcome.invalid.json
|-- nondeterministic_viewport.invalid.json
|-- live_network_dependency.invalid.json
|-- missing_trust_labels.invalid.json
|-- unsupported_renderer_option.invalid.json
|-- unresolved_policy_state.invalid.json
`-- screenshot_as_authority.invalid.json
```

The layout is PROPOSED until files and consumers exist.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/ui tests/domains tests/fixtures/maplibre/invalid
```

Default runs should be deterministic, local, no-network, and finite-outcome only.

---

## Maintenance checklist

- [ ] Keep examples synthetic and compact.
- [ ] Keep invalid cases separate from `../baselines/`.
- [ ] Move visual rejection canaries to `../bad-baselines/` when they are specifically baseline-regression cases.
- [ ] Declare the expected failure outcome and reason where useful.
- [ ] Link to consumer tests only after verification.
- [ ] Do not store production screenshots, real artifacts, release records, policy rules, schemas, or implementation code here.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| Sibling `baselines/` README | CONFIRMED during authoring. |
| Sibling `bad-baselines/` README | CONFIRMED during authoring. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Consumer tests | NEEDS VERIFICATION. |
| Runner and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
