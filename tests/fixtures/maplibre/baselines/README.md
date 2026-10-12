<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-maplibre-baselines-readme
title: MapLibre Baselines Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Map steward
  - OWNER_TBD - UI steward
  - OWNER_TBD - Fixture steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; maplibre; baselines; synthetic-only; no-network; renderer-not-truth; release-gated
tags: [kfm, tests, fixtures, maplibre, baselines, visual-regression, renderer-boundary, release-gated, no-network]
related:
  - ../../README.md
  - ../../../README.md
  - ../bad-baselines/README.md
  - ../../../domains/fauna/visual/README.md
  - ../../../../docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md
  - ../../../../packages/maplibre/
  - ../../../../release/
notes:
  - "This README replaces empty placeholder content at tests/fixtures/maplibre/baselines/README.md."
  - "This lane documents expected MapLibre visual baseline fixtures. It is not a renderer implementation, screenshot archive, release store, evidence store, policy home, or public map root."
  - "Rejected examples belong under ../bad-baselines/."
  - "Executable tests, payload inventory, runner wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# MapLibre baseline test fixtures

`tests/fixtures/maplibre/baselines/`

Status: draft / empty placeholder replaced / PROPOSED until executable tests and fixture payloads are verified.

This directory is the test-local home for expected MapLibre visual baseline fixtures. Baselines here are review fixtures for deterministic rendering checks. They are not source truth, evidence, release approval, renderer authority, publication authority, or public map artifacts.

## Boundary

Use this lane for small synthetic baseline manifests and expected-state notes that a test can compare against. Keep rejected, intentionally broken, or unsafe examples in `../bad-baselines/`.

This lane must not become:

- a screenshot archive;
- a renderer implementation home;
- a style or tile authority;
- a release store;
- an evidence or proof store;
- a policy or schema home;
- a public map artifact root.

## Placement basis

`tests/fixtures/` is for unit-test-scoped fixtures. MapLibre implementation belongs in renderer and app roots. Release decisions belong in `release/`. Architecture and doctrine live in `docs/`. This README only documents the test fixture lane.

## Expected fixture families

| Family | Purpose | Expected posture |
|---|---|---|
| `public_layer_card` | Expected public-safe layer card state. | deterministic fixture |
| `released_layer_enabled` | Expected enabled released-layer state. | release-aware fixture |
| `stale_layer_labelled` | Expected stale/degraded label state. | visible trust state |
| `withdrawn_layer_disabled` | Expected unavailable withdrawn state. | fail-closed fixture |
| `corrected_layer_notice` | Expected correction notice state. | correction-aware fixture |
| `rollback_visible` | Expected rollback-aware state. | rollback-aware fixture |
| `legend_accessible` | Expected labelled legend state. | accessibility-aware fixture |
| `trust_badges_accessible` | Expected labelled trust badges. | accessibility-aware fixture |

## Accepted material

Accepted material is limited to compact synthetic `*.json`, `*.yaml`, `*.yml`, or `*.md` fixture notes and manifests that describe expected baseline state. Use toy refs, toy ids, toy timestamps, and deterministic viewport notes.

## Exclusions

Do not place production screenshots, real map artifacts, release records, evidence records, implementation code, policy rules, schema files, retained CI outputs, secrets, or public payloads in this lane.

## Suggested layout

```text
tests/fixtures/maplibre/baselines/
|-- README.md
|-- public_layer_card.valid.json
|-- released_layer_enabled.valid.json
|-- stale_layer_labelled.valid.json
|-- withdrawn_layer_disabled.valid.json
|-- corrected_layer_notice.valid.json
|-- rollback_visible.valid.json
|-- legend_accessible.valid.json
`-- trust_badges_accessible.valid.json
```

The layout is PROPOSED until files and consumers exist.

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/ui tests/domains tests/fixtures/maplibre/baselines
```

Default runs should be deterministic, local, and no-network.

## Verification status

- Target README: replaced empty placeholder content.
- Companion lane: `../bad-baselines/README.md` verified during authoring.
- Fixture payload inventory: NEEDS VERIFICATION.
- Runner and CI wiring: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
