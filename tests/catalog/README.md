<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION_UUID
title: tests/catalog
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS_VERIFICATION_DATE
updated: 2026-04-14
policy_label: public
related: [
  ../README.md,
  ../../README.md,
  ../../tools/catalog/README.md,
  ../../data/catalog/README.md,
  ../../data/catalog/stac/README.md,
  ../../data/catalog/dcat/README.md,
  ../../data/catalog/prov/README.md,
  ../../contracts/README.md,
  ../../schemas/README.md,
  ../../policy/README.md,
  ../../.github/workflows/README.md,
  ../../.github/CODEOWNERS,
  ../../tools/ci/README.md
]
tags: [kfm, tests, catalog, stac, dcat, prov, crosslink, fixtures]
notes: [
  "Updated to reflect the thin-slice `catalog_crosslink.py` helper, the passing `test_catalog_crosslink.py` test, and the proposed mismatch fixtures.",
  "Current public-main evidence confirms `tests/` as a governed verification surface and `tools/catalog/` as the adjacent helper lane.",
  "Exact checked-in public-tree parity for `tests/catalog/` still requires verification against the target branch."
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/catalog/`

Governed verification lane for **catalog closure**, **triplet cross-link consistency**, and **catalog-helper proof** in Kansas Frontier Matrix.

> [!NOTE]
> **Status:** experimental  
> **Document state:** draft  
> **Owners:** `@bartytime4life`  
> **Path:** `tests/catalog/README.md`  
> ![Status](https://img.shields.io/badge/status-experimental-orange) ![Doc](https://img.shields.io/badge/doc-directory__README-blue) ![Owners](https://img.shields.io/badge/owners-%40bartytime4life-6f42c1) ![Lane](https://img.shields.io/badge/lane-tests%2Fcatalog-0a7ea4) ![Scope](https://img.shields.io/badge/scope-catalog%20closure%20proof-1f6feb) ![Truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED-2ea043)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current evidence snapshot](#current-evidence-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Reference tables](#reference-tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> `tests/catalog/` is **not** the home of STAC, DCAT, or PROV truth.
>
> This lane proves catalog-closure behavior over declared artifacts. The authoritative records stay in `data/catalog/`; policy law stays in `policy/`; machine-contract authority stays in `contracts/` and `schemas/`.

> [!TIP]
> Keep the KFM trust split visible here:
>
> **fixtures + assertions ≠ helper behavior ≠ metadata truth**
>
> `tests/catalog/` should prove behavior.  
> `tools/catalog/` should implement reusable checks.  
> `data/catalog/` should remain the authoritative outward metadata seam.

> [!WARNING]
> This README is intentionally evidence-bounded.
>
> Current public documentation clearly supports `tests/` as a governed verification surface and `tools/catalog/` as an adjacent helper lane, but it does **not** fully prove the exact checked-in `tests/catalog/` subtree on public `main`. Treat current thin-slice files as target-branch evidence unless rechecked directly.

---

## Scope

`tests/catalog/` is the verification lane for **small, reviewable proofs** that catalog-oriented helper logic behaves correctly over declared inputs.

In practice, that means proving behavior around:

- STAC / DCAT / PROV cross-link consistency
- promotion-adjacent catalog closure checks
- stable JSON report shapes intended for CI or reviewer rendering
- negative-path handling for missing refs, subject drift, version drift, release drift, and malformed inputs

This lane matters because it keeps catalog-proof behavior explicit without collapsing metadata law, policy law, and workflow orchestration into one hidden place.

### Evidence markers used in this README

| Marker | Meaning here |
|---|---|
| **CONFIRMED** | Directly supported by visible repo docs, ownership files, or public-tree inspection |
| **INFERRED** | Conservative interpretation of adjacent repo evidence or repeated doctrine |
| **PROPOSED** | Recommended landing shape or lane behavior consistent with current doctrine |
| **UNKNOWN** | Not established strongly enough from currently visible evidence |
| **NEEDS VERIFICATION** | Placeholder or branch-specific detail that should be checked before merge |

[Back to top](#top)

---

## Repo fit

`tests/catalog/` sits between the **helper lane that inspects catalog closure** and the **release-bearing metadata surfaces that must remain authoritative**.

| Relation | Surface | Why it matters |
|---|---|---|
| Parent verification lane | [`../README.md`](../README.md) | Defines `tests/` as a governed verification surface rather than a generic QA bucket |
| Root posture | [`../../README.md`](../../README.md) | Keeps evidence-first, trust-visible repo posture in scope |
| Helper under test | [`../../tools/catalog/README.md`](../../tools/catalog/README.md) | Defines the helper lane for catalog QA, cross-link, and reviewer-facing metadata support |
| Metadata seam | [`../../data/catalog/README.md`](../../data/catalog/README.md) | Catalog records live there; this lane proves behavior over them rather than owning them |
| Catalog child lanes | [`../../data/catalog/stac/README.md`](../../data/catalog/stac/README.md), [`../../data/catalog/dcat/README.md`](../../data/catalog/dcat/README.md), [`../../data/catalog/prov/README.md`](../../data/catalog/prov/README.md) | The triplet surfaces the helper reads and this lane pressure-tests |
| Contract authority | [`../../contracts/README.md`](../../contracts/README.md) | Canonical contract semantics should stay upstream from test assertions |
| Schema authority | [`../../schemas/README.md`](../../schemas/README.md) | Test fixtures should pressure declared shapes, not silently replace them |
| Policy authority | [`../../policy/README.md`](../../policy/README.md) | Tests may exercise policy consequences, but policy remains the authority |
| Workflow boundary | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | Merge-blocking invocation belongs at the workflow boundary, not hidden inside tests |
| Ownership | [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | Current owner coverage for `/tests/` resolves here |
| Reviewer rendering handoff | [`../../tools/ci/README.md`](../../tools/ci/README.md) | Stable machine-readable outputs from this lane can later feed reviewer-facing summaries |

### Repo-fit summary

| Question | Answer |
|---|---|
| What belongs here? | Small, deterministic proofs for catalog closure helpers and catalog-adjacent validation behavior |
| What does not belong here? | Authoritative catalog records, policy bundles, schema-home decisions, or workflow orchestration |
| Why keep it separate from `tools/catalog/`? | `tools/catalog/` owns reusable helper behavior; `tests/catalog/` owns fixtures, assertions, and fail-path proof |
| Why keep it separate from `data/catalog/`? | Catalog artifacts are release-bearing metadata, not disposable test fixtures |

[Back to top](#top)

---

## Accepted inputs

Only explicit, reviewable, public-safe artifacts belong here.

| Input class | Examples | Why it belongs here |
|---|---|---|
| Thin-slice helper inputs | `decision.json`, `promotion-record.json`, crosslink report JSON | Lets the lane prove concrete helper behavior over declared artifacts |
| Catalog reference fixtures | STAC / DCAT / PROV refs with aligned or misaligned subject/version shapes | Makes cross-link behavior legible and deterministic |
| Minimal negative-path cases | missing refs, wrong subject, version drift, release drift, malformed JSON | KFM negative states are first-class and should be proved directly |
| Stable helper outputs | compact JSON reports and exit codes | CI and reviewer helpers can consume these without scraping logs |
| Small synthetic metadata | public-safe catalog fragments and placeholder IDs | Keeps the lane clone-safe and understandable |

### Input rules

1. Prefer explicit files over implicit environment state.
2. Prefer tiny synthetic fixtures over copied production artifacts.
3. Keep identifiers and references legible enough for review.
4. Preserve upstream artifact shape when a helper depends on it.
5. Treat malformed-input cases as equally important proof surfaces.

[Back to top](#top)

---

## Exclusions

| Does **not** belong here | Better home | Why |
|---|---|---|
| Authoritative STAC / DCAT / PROV records | [`../../data/catalog/README.md`](../../data/catalog/README.md) | Tests should not become the metadata truth surface |
| Helper implementation code | [`../../tools/catalog/README.md`](../../tools/catalog/README.md) | This lane proves behavior; it does not become the helper lane |
| Promotion decision logic | [`../../tools/validators/README.md`](../../tools/validators/README.md) | Validation and release decisions deserve their own stronger surface |
| Reviewer-facing Markdown rendering | [`../../tools/ci/README.md`](../../tools/ci/README.md) | Catalog tests should emit stable output that CI helpers can render |
| Workflow sequencing or permissions | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | Orchestration belongs at the workflow boundary |
| Policy vocabularies, obligations, or reason-code law | [`../../policy/README.md`](../../policy/README.md) | Tests may assert consequences, but policy remains the authority |
| Schema-home arbitration | [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md) | Test code must not quietly settle canonical object law |
| Secret-bearing or rights-unclear fixtures | governed secure lanes | Public test surfaces must stay safe to clone and review |

> [!CAUTION]
> If deleting a test from `tests/catalog/` would erase the only understandable explanation of how catalog closure works, too much meaning has leaked into the test lane.

[Back to top](#top)

---

## Current evidence snapshot

| Evidence item | Status | How this README uses it |
|---|---|---|
| `tests/` is a governed verification surface with public README-first routing | **CONFIRMED** | Grounds this file as a child test lane rather than a generic folder |
| `/tests/` is owned by `@bartytime4life` in current visible `CODEOWNERS` | **CONFIRMED** | Grounds the owners line |
| The current public `tests/README.md` names several downstream families but does **not** list `catalog/` among its confirmed downstream surfaces | **CONFIRMED** | Prevents overclaiming current public subtree maturity |
| The current public `tests/` tree visibly includes `accessibility/`, `ci/`, `contracts/`, `e2e/`, `fixtures/`, `integration/`, `policy/`, `reproducibility/`, `runtime_verification/`, `unit/`, `validators/`, and `README.md` | **CONFIRMED** | Grounds the parent-lane snapshot and makes the absence of visible `catalog/` meaningful |
| `tools/catalog/README.md` exists and clearly frames `tools/catalog/` as the helper lane for catalog QA, cross-link, and reviewer-facing metadata support | **CONFIRMED** | Grounds the adjacent lane contract this README should complement |
| A thin-slice direction centered on `tools/catalog/catalog_crosslink.py` with `tests/catalog/test_catalog_crosslink.py` as its proof surface is documented in adjacent lane materials | **DOCUMENTED / NEEDS VERIFICATION ON TARGET BRANCH** | Supports the lane shape below without upgrading branch reality into public-tree fact |
| Exact checked-in presence of `tests/catalog/`, `tests/catalog/test_catalog_crosslink.py`, and `tests/catalog/fixtures/` on current public `main` | **NEEDS VERIFICATION** | Kept explicitly bounded until the target branch is inspected directly |

[Back to top](#top)

---

## Directory tree

### Current public parent snapshot

```text
tests/
├── README.md
├── accessibility/
├── ci/
├── contracts/
├── e2e/
├── fixtures/
├── integration/
├── policy/
├── reproducibility/
├── runtime_verification/
├── unit/
└── validators/
```

### Target landing shape for this lane

```text
tests/catalog/
├── README.md
├── test_catalog_crosslink.py
└── fixtures/
    ├── promotion-record-mismatch.json
    └── prov-mismatch.json
```

### Optional fixture shape to prefer as the lane matures

```text
tests/catalog/
├── README.md
├── test_catalog_crosslink.py
└── fixtures/
    ├── aligned/
    ├── misaligned/
    └── malformed/
```

> [!NOTE]
> The first tree above is **current public-tree fact**.
>
> The latter shapes are the safest repo-native landing forms for this README, the thin-slice proof, and the first mismatch fixtures. Keep them marked as branch-conditional until the target checkout confirms them.

[Back to top](#top)

---

## Quickstart

Use an inspection-first sequence so this lane stays truthful as the branch evolves.

### 1) Confirm what actually exists in your checkout

```bash
find tests -maxdepth 3 -print 2>/dev/null | sort
find tools/catalog -maxdepth 3 -print 2>/dev/null | sort
```

### 2) Re-read the parent and adjacent lane contracts

```bash
sed -n '1,260p' tests/README.md 2>/dev/null
sed -n '1,260p' tools/catalog/README.md 2>/dev/null
sed -n '1,260p' data/catalog/README.md 2>/dev/null
sed -n '1,260p' .github/workflows/README.md 2>/dev/null
```

### 3) Search for current callers before inventing names

```bash
rg -n "catalog|crosslink|stac|dcat|prov" tests tools scripts .github data contracts schemas policy -S 2>/dev/null
```

### 4) Thin-slice local run

```bash
python tools/catalog/catalog_crosslink.py \
  --decision data/proofs/releases/floodplain-kansas-v1/decision.json \
  --record data/proofs/releases/floodplain-kansas-v1/promotion-record.json \
  --output catalog-crosslink-report.json
```

### 5) Thin-slice test run

```bash
pytest -q tests/catalog/test_catalog_crosslink.py
```

> [!TIP]
> Inventory first, then assert lane maturity.
>
> In KFM, a clear “not present yet” result is stronger than a confident fantasy subtree.

[Back to top](#top)

---

## Usage

### Add a focused catalog proof

Use `tests/catalog/` when the main job is to prove **catalog-oriented helper behavior** over declared inputs.

Typical fits:

- proving STAC / DCAT / PROV ref presence checks
- proving subject alignment across a catalog triplet
- proving version alignment across a catalog triplet
- proving release-ref alignment against the same promoted subject
- proving blocking vs non-blocking output shape for CI or reviewer handoff

### Keep this split clean

A healthy split looks like this:

- `data/catalog/` owns the outward metadata
- `tools/catalog/` owns reusable helper behavior
- `tests/catalog/` owns fixtures and assertions
- `.github/workflows/` decides when blocking checks run
- `tools/ci/` renders stable helper outputs for reviewers

### Thin-slice behavior this lane should prove

The smallest credible first proof is a pass/fail pair around cross-link closure:

1. **aligned triplet**  
   same subject, same version, release ref aligned  
   → helper returns pass and non-blocking output

2. **misaligned triplet**  
   mismatched subject or mismatched version / release  
   → helper returns fail and blocking output

### Tool behavior contract

| Concern | Required posture |
|---|---|
| Determinism | Same inputs should yield the same JSON shape and exit code |
| Failure semantics | Blocking checks fail non-zero and explain what broke |
| Output shape | Prefer stable JSON when CI or reviewer helpers consume the result |
| Boundary discipline | No hidden policy law, no silent schema arbitration, no publish shortcuts |
| Local / CI parity | A merge-blocking check should be runnable locally |
| Safety | No secret scraping, no rights-unclear fixtures, no unrestricted sensitive metadata |

[Back to top](#top)

---

## Diagram

```mermaid
flowchart LR
    A[data/catalog/\nSTAC + DCAT + PROV] --> B[tools/catalog/\nhelper surface]
    C[decision.json\npromotion-record.json] --> B
    B --> D[catalog_crosslink.py\nread-only evaluation]
    D --> E[JSON report\npass/fail + blocking]
    E --> F[tests/catalog/\nfixture + assertion lane]
    E --> G[.github/workflows/\nmerge gate]
    E --> H[tools/ci/\nreviewer rendering]

    style A fill:#eef7ff,stroke:#1f6feb
    style B fill:#f6f8fa,stroke:#6f42c1
    style D fill:#fff8e1,stroke:#d97706
    style F fill:#eefaf1,stroke:#238636
    style G fill:#fff1f2,stroke:#dc2626
```

[Back to top](#top)

---

## Reference tables

### Proof matrix

| Proof case | Inputs | Expected result | Why it matters |
|---|---|---|---|
| Aligned triplet | STAC / DCAT / PROV refs for one subject and one version | `pass`, non-blocking | proves the happy path without ambiguity |
| PROV subject drift | mismatched PROV subject ref | `fail`, blocking | catches lineage misbinding |
| Version drift | STAC / DCAT / PROV versions diverge | `fail`, blocking | catches closure drift across outward records |
| Release-ref drift | release ref version not aligned to catalog triplet | `fail`, blocking | catches review-significant promotion mismatch |
| Malformed input | missing file or invalid JSON | `error`, non-success exit | proves fail-closed hygiene |

### Boundary matrix

| Surface | Owns truth? | Owns proof? | Owns orchestration? |
|---|---:|---:|---:|
| `data/catalog/` | ✅ | ❌ | ❌ |
| `tools/catalog/` | ❌ | helper behavior only | ❌ |
| `tests/catalog/` | ❌ | ✅ | ❌ |
| `.github/workflows/` | ❌ | ❌ | ✅ |
| `tools/ci/` | ❌ | rendered summaries only | ❌ |

### Current thin-slice fixture intent

| Fixture | Intent | Expected failure |
|---|---|---|
| `fixtures/promotion-record-mismatch.json` | points to an intentionally wrong PROV bundle | version / release mismatch |
| `fixtures/prov-mismatch.json` | carries mismatched `subject_id` and `release_ref` | triplet closure failure |

[Back to top](#top)

---

## Task list

- [ ] Verify whether `tests/catalog/` already exists on the target branch
- [ ] Land or confirm `test_catalog_crosslink.py`
- [ ] Land or confirm the first mismatch fixtures
- [ ] Prove local and CI invocation parity with one documented command pair
- [ ] Extend cross-link checks from ref-shape alignment toward mounted-record subject/property checks
- [ ] Add an optional reviewer-facing handoff path into `tools/ci/` once the JSON report shape is stable
- [ ] Reconcile this lane with the parent `tests/README.md` family map after subtree reality is confirmed

### Definition of done

This lane is ready to move from draft toward review when all of the following are true:

- the target branch clearly contains the subtree
- one thin-slice test is executable
- one aligned and one misaligned case are both present
- the helper under test has a documented local run path
- negative-path behavior is explicit
- parent and adjacent lane docs no longer disagree about whether the subtree exists

[Back to top](#top)

---

## FAQ

### Why put this under `tests/` instead of `tools/catalog/`?

Because `tools/catalog/` should own reusable helper behavior. `tests/catalog/` should own fixtures, assertions, and negative-path proof.

### Why does this README keep saying `NEEDS VERIFICATION`?

Because the visible public repo evidence does not cleanly prove the subtree already exists, even though adjacent lane materials clearly point toward it. This file keeps that tension visible instead of smoothing it away.

### Why not store real catalog records here as fixtures?

Because catalog records are release-bearing metadata. Small synthetic examples are fine; authoritative records should stay in the metadata lane and be referenced deliberately.

### Should this lane become a full end-to-end promotion suite?

No. Once the proof burden becomes broader than catalog-helper behavior, it should graduate to `tests/e2e/`, `tests/validators/`, or another stronger lifecycle surface.

[Back to top](#top)

---

## Appendix

<details>
<summary><strong>Illustrative thin-slice fixture pair</strong></summary>

These examples are illustrative only. Keep checked-in fixtures tiny and synthetic.

### `decision.json`

```json
{
  "candidate_id": "floodplain-kansas",
  "dataset_version_id": "floodplain-kansas__v1",
  "release_id": "floodplain-kansas-v1"
}
```

### `promotion-record.json`

```json
{
  "promotion_id": "promotion:floodplain-kansas-v1",
  "candidate_id": "floodplain-kansas",
  "dataset_version_id": "floodplain-kansas__v1",
  "release_id": "floodplain-kansas-v1",
  "catalog_refs": {
    "stac_ref": "data/catalog/stac/items/floodplain-kansas__v1.json",
    "dcat_ref": "data/catalog/dcat/datasets/floodplain-kansas__v1.jsonld",
    "prov_ref": "data/catalog/prov/floodplain-kansas__v1.prov.json"
  }
}
```

### Review prompt

Before treating the lane as live, check:

1. Does the active branch actually contain `tests/catalog/`?
2. Does the helper under test emit a stable JSON report?
3. Are aligned and misaligned cases both present?
4. Does the workflow lane call the same helper humans can run locally?

</details>

[Back to top](#top)
