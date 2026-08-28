<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-maplibre-tiny-readme
title: MapLibre Tiny Test Fixtures README
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
policy_label: public-doc; tests; fixtures; maplibre; tiny; synthetic-only; no-network; renderer-not-truth; release-gated
tags: [kfm, tests, fixtures, maplibre, tiny, smoke-fixtures, renderer-boundary, no-network, PASS, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../baselines/README.md
  - ../bad-baselines/README.md
  - ../invalid/README.md
  - ../../../domains/fauna/visual/README.md
  - ../../../../docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md
  - ../../../../packages/maplibre/
  - ../../../../packages/ui/
  - ../../../../release/
notes:
  - "This README replaces placeholder content at tests/fixtures/maplibre/tiny/README.md."
  - "This lane documents tiny MapLibre smoke fixtures. It is not a renderer implementation, screenshot archive, release store, evidence store, policy home, or public map root."
  - "Tiny fixtures are minimal synthetic test carriers for fast local checks; complete expected visual baselines belong under ../baselines/, invalid cases under ../invalid/, and intentionally bad baseline canaries under ../bad-baselines/."
  - "Executable tests, payload inventory, runner wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre tiny test fixtures

> Unit-test-scoped lane for the smallest synthetic MapLibre smoke fixtures. Tiny fixtures should prove basic renderer-boundary and fixture-loader behavior without becoming visual baselines, screenshots, releases, evidence, policy, or public map artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: tiny" src="https://img.shields.io/badge/lane-tiny-purple">
  <img alt="Renderer: MapLibre" src="https://img.shields.io/badge/renderer-MapLibre-0a7ea4">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/maplibre/tiny/README.md`  
**Status:** draft / placeholder replaced / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/maplibre/tiny`  
**Sibling lanes:** `../baselines/`, `../bad-baselines/`, `../invalid/`  
**Default posture:** tiny, deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED sibling MapLibre fixture lanes exist; CONFIRMED `tests/fixtures/` is unit-test-scoped by repo doctrine; NEEDS VERIFICATION for executable tests, payload inventory, runner wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/fixtures/maplibre/tiny/` for the smallest possible MapLibre fixture examples needed by smoke tests, loader tests, schema stubs, or documentation examples.

Tiny fixtures should be deliberately boring: toy IDs, toy refs, tiny viewport notes, tiny layer snippets, deterministic values, and no live services. They should help tests fail fast before larger baseline or visual-regression fixtures are loaded.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Tiny MapLibre smoke fixtures | `tests/fixtures/maplibre/tiny/` | This lane. |
| Expected visual baselines | `tests/fixtures/maplibre/baselines/` | Larger expected-state lane. |
| Invalid fixtures | `tests/fixtures/maplibre/invalid/` | Malformed or fail-closed lane. |
| Bad baseline canaries | `tests/fixtures/maplibre/bad-baselines/` | Negative visual-baseline lane. |
| Renderer implementation | `packages/maplibre/` | Not owned here. |
| UI implementation | `apps/explorer-web/`, `packages/ui/` | Not owned here. |
| Release decisions | `release/` | Not owned here. |
| Architecture references | `docs/` | Human-facing doctrine and design context. |

---

## Tiny fixture rule

> [!IMPORTANT]
> Tiny fixtures should be small enough to inspect at a glance. If a fixture needs full visual baseline semantics, release-state matrix coverage, or negative visual-regression explanation, move it to a sibling lane.

Core expectations:

| Expectation | Required posture |
|---|---|
| Minimal shape | Fixture includes only the fields needed for the consumer test. |
| Synthetic data | Use toy IDs, toy refs, toy timestamps, and toy viewport notes. |
| No-network default | No live source, tile, style, glyph, sprite, API, or model calls. |
| Renderer boundary | Fixture does not imply MapLibre is truth, policy, release, or evidence authority. |
| Fast failure | Missing required fields should be easy for a test to diagnose. |
| Clear routing | Large, invalid, or bad-baseline cases move to the correct sibling lane. |

---

## Accepted inputs

Accepted material is limited to compact synthetic examples, such as:

- tiny `*.json`, `*.yaml`, `*.yml`, or `*.md` fixture notes;
- toy viewport definitions;
- toy layer refs and release refs;
- toy expected outcomes such as `PASS`, `ABSTAIN`, `DENY`, or `ERROR`;
- tiny loader examples that do not require live services;
- links to consumer tests once those tests are verified.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| expected visual baselines | `../baselines/` |
| malformed or fail-closed examples | `../invalid/` |
| intentionally bad visual-baseline canaries | `../bad-baselines/` |
| renderer implementation | `packages/maplibre/` or accepted renderer root |
| UI implementation | `apps/explorer-web/` or `packages/ui/` |
| release records | `release/` |
| screenshots, retained CI outputs, or map artifacts | governed artifact or release roots |
| policy rules or schemas | `policy/` and `schemas/` |
| production data, secrets, or public payloads | not allowed in this fixture lane |

---

## Suggested layout

```text
tests/fixtures/maplibre/tiny/
|-- README.md
|-- viewport.tiny.json
|-- layer_ref.tiny.json
|-- release_ref.tiny.json
|-- empty_style_ref.tiny.json
|-- trust_label_stub.tiny.json
`-- expected_outcomes.tiny.json
```

The layout is PROPOSED until files and consumers exist.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/ui tests/fixtures/maplibre/tiny
```

Default runs should be deterministic, local, no-network, and finite-outcome only.

---

## Maintenance checklist

- [ ] Keep examples tiny, synthetic, and reviewable.
- [ ] Keep expected baselines in `../baselines/`.
- [ ] Keep invalid cases in `../invalid/`.
- [ ] Keep bad visual-baseline canaries in `../bad-baselines/`.
- [ ] Do not store screenshots, real map artifacts, release records, policy rules, schemas, implementation code, secrets, or public payloads here.
- [ ] Link to consumer tests only after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| Sibling `baselines/` README | CONFIRMED during authoring. |
| Sibling `bad-baselines/` README | CONFIRMED during authoring. |
| Sibling `invalid/` README | CONFIRMED during authoring. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Consumer tests | NEEDS VERIFICATION. |
| Runner and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
