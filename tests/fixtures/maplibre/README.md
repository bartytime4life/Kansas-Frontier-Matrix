<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-maplibre-readme
title: MapLibre Test Fixtures README
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
policy_label: public-doc; tests; fixtures; maplibre; synthetic-only; no-network; renderer-not-truth; release-gated
tags: [kfm, tests, fixtures, maplibre, baselines, bad-baselines, invalid, tiny, visual-regression, renderer-boundary, no-network, PASS, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../../README.md
  - ./baselines/README.md
  - ./bad-baselines/README.md
  - ./invalid/README.md
  - ./tiny/README.md
  - ../../domains/fauna/visual/README.md
  - ../../../docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md
  - ../../../apps/explorer-web/src/features/layer_catalog/README.md
  - ../../../packages/maplibre/
  - ../../../packages/ui/
  - ../../../release/
notes:
  - "This README replaces placeholder content at tests/fixtures/maplibre/README.md."
  - "This parent lane indexes MapLibre fixture sublanes. It is not a renderer implementation, screenshot archive, release store, evidence store, policy home, schema home, or public map root."
  - "MapLibre fixtures are synthetic test carriers only; they do not make screenshots, styles, tiles, rendered maps, or baselines into truth authority."
  - "Executable tests, payload inventory, runner wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre test fixtures

> Parent README for unit-test-scoped MapLibre fixtures under `tests/fixtures/maplibre/`. This lane indexes tiny smoke fixtures, expected baselines, invalid cases, and intentionally bad baseline canaries while preserving the boundary that MapLibre renders governed outputs but does not create truth, evidence, policy, release, or public-map authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: maplibre fixtures" src="https://img.shields.io/badge/lane-maplibre__fixtures-purple">
  <img alt="Renderer: MapLibre" src="https://img.shields.io/badge/renderer-MapLibre-0a7ea4">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/maplibre/README.md`  
**Status:** draft / placeholder replaced / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/maplibre`  
**Child lanes:** `baselines/`, `bad-baselines/`, `invalid/`, `tiny/`  
**Default posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED child README coverage exists for `baselines/`, `bad-baselines/`, `invalid/`, and `tiny/`; CONFIRMED `tests/fixtures/` is unit-test-scoped by repo doctrine; NEEDS VERIFICATION for executable tests, fixture payload inventory, runner wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/fixtures/maplibre/` as the parent lane for MapLibre test fixtures.

This directory should help maintainers route fixture material to the right child lane:

- `tiny/` for the smallest synthetic smoke fixtures;
- `baselines/` for expected visual/rendering baseline fixtures;
- `invalid/` for malformed, incomplete, rejected, or fail-closed fixture cases;
- `bad-baselines/` for intentionally bad baseline canaries that must fail or require review.

This parent README is an index and boundary document. It is not a renderer implementation, UI implementation, screenshot archive, style or tile authority, release store, evidence store, policy home, schema home, or public map artifact root.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| MapLibre fixture parent | `tests/fixtures/maplibre/` | This lane. |
| Tiny smoke fixtures | `tests/fixtures/maplibre/tiny/` | Child lane for minimal examples. |
| Expected visual baselines | `tests/fixtures/maplibre/baselines/` | Child lane for expected states. |
| Invalid fixtures | `tests/fixtures/maplibre/invalid/` | Child lane for malformed/fail-closed examples. |
| Bad baseline canaries | `tests/fixtures/maplibre/bad-baselines/` | Child lane for rejected baseline examples. |
| Visual and UI tests | `tests/` consumer lanes | Consumers, not fixture authority. |
| Renderer implementation | `packages/maplibre/` | Not owned here. |
| UI implementation | `apps/explorer-web/`, `packages/ui/` | Not owned here. |
| Release decisions | `release/` | Not owned here. |
| Architecture references | `docs/` | Human-facing doctrine and design context. |

---

## Child-lane index

| Lane | Use for | Do not use for |
|---|---|---|
| [`tiny/`](./tiny/README.md) | Minimal smoke fixtures, toy refs, tiny viewport notes, loader checks. | Full visual baselines or large scenario matrices. |
| [`baselines/`](./baselines/README.md) | Expected visual/rendering baseline manifests and expected-state notes. | Invalid cases or rejected baseline canaries. |
| [`invalid/`](./invalid/README.md) | Malformed, incomplete, rejected, or fail-closed fixture cases. | Approved expected baselines. |
| [`bad-baselines/`](./bad-baselines/README.md) | Intentionally bad visual baseline canaries that must fail or require review. | Normal expected baselines. |

---

## Fixture rule

> [!IMPORTANT]
> MapLibre fixtures are downstream test carriers. They do not make screenshots, rendered maps, style JSON, tiles, exports, popups, or scenes into source truth, evidence, policy, release approval, or public artifacts.

Core expectations:

| Expectation | Required posture |
|---|---|
| Synthetic data | Use toy IDs, toy refs, toy timestamps, and review-safe examples. |
| No-network default | No live source, tile, style, glyph, sprite, API, or model calls in default fixtures. |
| Renderer boundary | Fixtures do not imply MapLibre is truth, policy, release, or evidence authority. |
| Release awareness | Public-facing examples reference release posture where material. |
| Clear routing | Tiny, baseline, invalid, and bad-baseline examples stay in the appropriate child lane. |
| Finite outcomes | Expected outcomes should be explicit where useful: `PASS`, `ABSTAIN`, `DENY`, `ERROR`, or validation failure. |

---

## Accepted inputs

Accepted material is limited to compact synthetic examples, such as:

- small `*.json`, `*.yaml`, `*.yml`, or `*.md` fixture notes;
- toy viewport definitions;
- toy layer refs, release refs, style refs, and artifact refs;
- toy expected outcomes and reason-code notes;
- tiny loader examples that do not require live services;
- links to consumer tests after those tests are verified.

---

## Exclusions

Do not place these materials in this parent lane:

| Excluded material | Correct destination |
|---|---|
| detailed expected baselines | `./baselines/` |
| malformed or fail-closed examples | `./invalid/` |
| intentionally bad visual-baseline canaries | `./bad-baselines/` |
| tiny smoke fixtures | `./tiny/` |
| renderer implementation | `packages/maplibre/` or accepted renderer root |
| UI implementation | `apps/explorer-web/` or `packages/ui/` |
| release records | `release/` |
| screenshots, retained CI outputs, or map artifacts | governed artifact or release roots |
| policy rules or schemas | `policy/` and `schemas/` |
| production data, secrets, or public payloads | not allowed in this fixture lane |

---

## Suggested layout

```text
tests/fixtures/maplibre/
|-- README.md
|-- baselines/
|   `-- README.md
|-- bad-baselines/
|   `-- README.md
|-- invalid/
|   `-- README.md
`-- tiny/
    `-- README.md
```

The layout reflects README coverage verified during authoring. Fixture payload inventory remains NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/ui tests/domains tests/fixtures/maplibre
```

Default runs should be deterministic, local, no-network, and finite-outcome only.

---

## Maintenance checklist

- [ ] Keep parent material navigational and boundary-focused.
- [ ] Keep tiny smoke examples in `tiny/`.
- [ ] Keep expected baselines in `baselines/`.
- [ ] Keep invalid cases in `invalid/`.
- [ ] Keep intentionally bad visual-baseline canaries in `bad-baselines/`.
- [ ] Do not store screenshots, real map artifacts, release records, policy rules, schemas, implementation code, secrets, or public payloads here.
- [ ] Link to consumer tests only after verification.
- [ ] Update this README when child lanes, fixture payloads, tests, or runner wiring are verified.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| Child `baselines/` README | CONFIRMED during authoring. |
| Child `bad-baselines/` README | CONFIRMED during authoring. |
| Child `invalid/` README | CONFIRMED during authoring. |
| Child `tiny/` README | CONFIRMED during authoring. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Consumer tests | NEEDS VERIFICATION. |
| Runner and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
