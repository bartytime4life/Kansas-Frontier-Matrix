<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION
title: tools/catalog/
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS_VERIFICATION
updated: 2026-04-14
policy_label: public
related: [../README.md, ../../README.md, ../../data/README.md, ../../data/catalog/README.md, ../../data/catalog/dcat/README.md, ../../data/catalog/stac/README.md, ../../data/catalog/prov/README.md, ../../scripts/README.md, ../../contracts/README.md, ../../schemas/README.md, ../../policy/README.md, ../../tests/README.md, ../../tests/catalog/README.md, ../../.github/README.md, ../../.github/CODEOWNERS, ../../.github/workflows/README.md, ../validators/README.md, ../validators/promotion_gate/README.md, ../ci/README.md, ../attest/README.md, ../diff/README.md, ../docs/README.md, ../probes/README.md]
tags: [kfm, tools, catalog, dcat, stac, prov, crosslink, qa, review]
notes: [Updated to reflect the catalog_crosslink.py thin slice and tests/catalog/test_catalog_crosslink.py. doc_id placeholder pending repo-internal registration; created date needs live file-history verification; active-branch caller/workflow parity remains NEEDS VERIFICATION.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/catalog/`

Catalog QA, cross-link, and reviewer-facing metadata helper surface for Kansas Frontier Matrix.

![status](https://img.shields.io/badge/status-experimental-orange)
![doc](https://img.shields.io/badge/doc-draft-blue)
![owners](https://img.shields.io/badge/owners-%40bartytime4life-6f42c1)
![lane](https://img.shields.io/badge/lane-tools%2Fcatalog-0a7ea4)
![truth](https://img.shields.io/badge/truth-evidence--bounded-555555)

| Field | Value |
|---|---|
| **Status** | `experimental` |
| **Document state** | `draft` |
| **Owners** | `@bartytime4life` *(visible `/tools/` CODEOWNERS fallback; narrower lane ownership still needs verification)* |
| **Path** | `tools/catalog/README.md` |
| **Role** | Reusable helper lane for catalog closure QA, cross-link checks, and reviewer-facing metadata summaries |
| **Repo fit** | Child lane of [`../README.md`](../README.md); adjacent to [`../../data/catalog/README.md`](../../data/catalog/README.md); downstream of [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../policy/README.md`](../../policy/README.md), and [`../../tests/README.md`](../../tests/README.md) |
| **Current public snapshot** | Documented thin slice is `tools/catalog/catalog_crosslink.py` with proof surface `tests/catalog/test_catalog_crosslink.py`; wider family shape remains bounded |
| **Quick jumps** | [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current evidence snapshot](#current-evidence-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Reference tables](#reference-tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix) |

> [!IMPORTANT]
> `tools/catalog/` is **not** `data/catalog/`.
>
> This directory is the reusable helper lane that inspects, validates, cross-checks, or summarizes catalog closure.
>
> The catalog records themselves belong in [`../../data/catalog/README.md`](../../data/catalog/README.md) and remain release-backed metadata, not helper-owned truth.

> [!TIP]
> **Current executable snapshot (thin slice)**
>
> The current documented thin slice for this lane is:
>
> - `tools/catalog/catalog_crosslink.py`
>
> It checks:
>
> - STAC ref presence
> - DCAT ref presence
> - PROV ref presence
> - subject alignment across the catalog triplet
> - version alignment across the catalog triplet
> - release ref alignment against the triplet
>
> Expected proof surface:
>
> - `tests/catalog/test_catalog_crosslink.py`
> - optional JSON output for CI and reviewer rendering
>
> The broader lane remains larger than this one executable helper. QA, reporting, and richer closure helpers are still **PROPOSED** unless directly verified in the active branch.

> [!NOTE]
> This README intentionally does two jobs at once:
>
> 1. describe the **current documented lane state** honestly
> 2. define the **preferred lane shape** that improves catalog closure tooling without smuggling policy, schema authority, or publish logic into helper code

---

## Scope

`tools/catalog/` is the KFM helper surface for **catalog closure quality**.

In practice, that means small, explicit tools that operate on the outward metadata seam anchored in **DCAT**, **STAC**, and **PROV**. These helpers should strengthen governed discovery, lineage inspection, triplet consistency, and promotion-readiness review without quietly becoming the source of truth for metadata law, policy law, release law, or publication state.

This lane is valuable because KFM treats catalog closure as part of the trust model. Reviewers need a narrow place to ask questions like:

- do the triplet refs exist?
- do the subject IDs line up?
- do the versions line up?
- does the release ref still point at the same governed object family?
- can CI and reviewer summaries consume a stable report instead of recomputing closure logic ad hoc?

What this README does:

1. states the current lane posture without overclaiming
2. defines what belongs in `tools/catalog/`
3. separates current lane fact from target-shape guidance
4. keeps KFM truth posture visible with explicit labels

### Evidence markers used here

| Marker | Meaning in this README |
|---|---|
| **CONFIRMED** | Supported by current repo-facing documentation or adjacent KFM doctrine |
| **INFERRED** | Strongly suggested by adjacent repo-facing docs, but not proven as wider executable inventory |
| **PROPOSED** | Target shape, placement rule, or starter-helper guidance consistent with KFM doctrine |
| **UNKNOWN** | Not established strongly enough to present as current repo fact |
| **NEEDS VERIFICATION** | Branch-specific, workflow-specific, ownership-specific, or file-history detail that should be checked before merge |

[Back to top](#top)

---

## Repo fit

`tools/catalog/` sits between the metadata seam, the verification seam, and reviewer-facing helper surfaces.

| Relation | Surface | Why it matters |
|---|---|---|
| Parent helper family | [`../README.md`](../README.md) | Defines `tools/` as a reusable helper family rather than a shadow authority surface |
| Root posture | [`../../README.md`](../../README.md) | Sets the repo-wide evidence-first, map-first, trust-visible identity |
| Metadata seam | [`../../data/catalog/README.md`](../../data/catalog/README.md) | The catalog objects themselves live there, not here |
| Catalog children | [`../../data/catalog/stac/README.md`](../../data/catalog/stac/README.md), [`../../data/catalog/dcat/README.md`](../../data/catalog/dcat/README.md), [`../../data/catalog/prov/README.md`](../../data/catalog/prov/README.md) | Closure checks should be explicit about which outward surface they inspect |
| Authority surfaces | [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../policy/README.md`](../../policy/README.md) | This lane consumes declared law; it does not own that law |
| Verification seam | [`../../tests/README.md`](../../tests/README.md), [`../../tests/catalog/README.md`](../../tests/catalog/README.md) | Helper behavior should be proved with fixtures and assertions |
| Thin orchestration | [`../../scripts/README.md`](../../scripts/README.md) | Wrapper entrypoints may call helpers, but helper logic should stay reviewable outside shell glue |
| Workflow boundary | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | Workflow YAML should call stable helpers rather than bury logic |
| Promotion boundary | [`../validators/promotion_gate/README.md`](../validators/promotion_gate/README.md) | Promotion validation may consume closure checks, but promotion still decides |
| Reviewer rendering | [`../ci/README.md`](../ci/README.md) | Stable JSON output may be rendered there for reviewers |
| Adjacent helper lanes | [`../diff/README.md`](../diff/README.md), [`../attest/README.md`](../attest/README.md), [`../docs/README.md`](../docs/README.md), [`../probes/README.md`](../probes/README.md), [`../validators/README.md`](../validators/README.md) | Neighboring lanes clarify what should stay out of `tools/catalog/` |

### Repo-fit summary

| Question | Answer |
|---|---|
| What is this lane for? | Helper logic that inspects or summarizes catalog closure quality |
| What is this lane not for? | Owning metadata truth, deciding policy, signing releases, or publishing scope |
| Why keep it separate from `data/catalog/`? | Catalog records are release-backed metadata; helper code should stay replaceable and reviewable |
| Why keep it separate from promotion logic? | Closure inspection is an input to promotion, not promotion authority itself |

[Back to top](#top)

---

## Accepted inputs

The following belong in or immediately around `tools/catalog/` when the lane is behaving correctly:

| Accepted input | Why it belongs here | Typical posture |
|---|---|---|
| STAC / DCAT / PROV refs | Core catalog-triplet inspection surface | **CONFIRMED fit** |
| Promotion decisions and promotion records used only for cross-link validation | Lets helpers verify closure against governed promotion artifacts | **CONFIRMED thin-slice fit** |
| Release refs and manifest refs used as read-only comparison inputs | Supports closure consistency checks | **CONFIRMED thin-slice fit** |
| Small helper-local examples | Useful for docs or smoke checks if they stay tiny and non-sensitive | **PROPOSED** |
| JSON report outputs | Gives CI and reviewers a stable, parseable result | **CONFIRMED thin-slice fit** |
| Review-oriented readiness summaries | Good next step once stable machine checks already exist | **PROPOSED** |
| Structural QA helpers for STAC / DCAT / PROV | Natural widening of the lane without changing its role | **PROPOSED** |

---

## Exclusions

The following do **not** belong here:

| Exclusion | Where it belongs instead | Why |
|---|---|---|
| Canonical catalog records | [`../../data/catalog/README.md`](../../data/catalog/README.md) | Helper code must not become metadata truth |
| Policy decisions | [`../../policy/README.md`](../../policy/README.md) | Policy decides; helpers inspect |
| Schema-home authority | [`../../schemas/README.md`](../../schemas/README.md) and [`../../contracts/README.md`](../../contracts/README.md) | This lane may inspect shapes, not arbitrate authority |
| Publish logic | [`../../data/published/README.md`](../../data/published/README.md) | Catalog QA should not mutate release state |
| Proof-pack signing or verification | [`../attest/README.md`](../attest/README.md) | Attestation belongs in its own helper lane |
| Long-running orchestration | [`../../scripts/README.md`](../../scripts/README.md) or workflow callers | Keep helper behavior explicit and reusable |
| Validator-law ownership | [`../validators/README.md`](../validators/README.md) | Blocking rule law should not be hidden inside catalog helper prose |
| Sensitive fixtures or private source payloads | `../../tests/` or governed data lanes | Public helper surfaces should remain safe to clone and review |

[Back to top](#top)

---

## Current evidence snapshot

| Evidence item | Status | How this README uses it |
|---|---|---|
| `tools/` exists with sibling families `attest/`, `catalog/`, `ci/`, `diff/`, `docs/`, `probes/`, and `validators/` | **CONFIRMED** | Grounds this file as one lane inside a broader helper family |
| `data/catalog/` exists with `dcat/`, `prov/`, and `stac/` child surfaces | **CONFIRMED** | Grounds the adjacent metadata seam this lane should support |
| `tests/` exists as a top-level governed verification surface | **CONFIRMED** | Grounds the expectation that helpers should land with fixtures or assertions |
| `/tools/` ownership is covered by visible `CODEOWNERS` fallback to `@bartytime4life` | **CONFIRMED** | Grounds the owner line for this subtree |
| Promotion Gate documentation treats catalog closure as part of review-significant promotion validation | **CONFIRMED via adjacent documentation** | Justifies explicit handoff to promotion validation without collapsing the lanes |
| `tools/catalog/catalog_crosslink.py` is the current documented thin-slice executable helper | **CONFIRMED** | This README documents one concrete helper rather than a purely README-only lane |
| `tests/catalog/test_catalog_crosslink.py` is the current documented thin-slice proof surface | **CONFIRMED** | The first helper now lands with explicit test coverage |
| Wider helper families such as `qa/`, `crosslink/`, and `report/` | **PROPOSED** | These remain target shapes rather than fully proven current inventory |
| Exact repo-internal `doc_id`, original created date, and active-branch caller/workflow parity | **NEEDS VERIFICATION** | Left explicitly bounded rather than promoted to fact |

[Back to top](#top)

---

## Directory tree

### Current live public neighborhood

```text
tools/
├── README.md
├── attest/
├── catalog/
│   ├── README.md
│   └── catalog_crosslink.py
├── ci/
├── diff/
├── docs/
├── probes/
└── validators/
```

### Thin-slice executable shape

```text
tools/catalog/
├── README.md
└── catalog_crosslink.py

tests/catalog/
└── test_catalog_crosslink.py
```

### Adjacent live catalog seam

```text
data/catalog/
├── README.md
├── dcat/
├── prov/
└── stac/
```

> [!WARNING]
> The landing shape below is **PROPOSED**, not a claim that the current subtree is already fully populated.

### PROPOSED stable family shape to prefer

```text
tools/catalog/
├── README.md
├── qa/          # fast structural STAC / DCAT / PROV checks
├── crosslink/   # triplet + manifest / receipt consistency helpers
└── report/      # reviewer-facing completeness, freshness, and readiness summaries
```

That proposed shape is intentionally narrow:

- `qa/` keeps structural validation obvious
- `crosslink/` keeps triplet closure and evidence joins explicit
- `report/` keeps reviewer summaries separate from blocking validators

It avoids turning this lane into a hidden metadata factory.

[Back to top](#top)

---

## Quickstart

Run these inventory-first commands before adding, renaming, or moving anything under `tools/catalog/`.

### 1. Confirm what actually exists in your checkout

```bash
find tools/catalog -maxdepth 3 -print 2>/dev/null | sort
find tests/catalog -maxdepth 3 -print 2>/dev/null | sort
```

### 2. Re-read the parent helper contract and adjacent metadata / verification seams

```bash
sed -n '1,240p' tools/README.md 2>/dev/null
sed -n '1,260p' data/catalog/README.md 2>/dev/null
sed -n '1,260p' data/catalog/dcat/README.md 2>/dev/null
sed -n '1,260p' data/catalog/stac/README.md 2>/dev/null
sed -n '1,260p' data/catalog/prov/README.md 2>/dev/null
sed -n '1,260p' tests/README.md 2>/dev/null
sed -n '1,260p' tests/catalog/README.md 2>/dev/null
sed -n '1,260p' tools/validators/promotion_gate/README.md 2>/dev/null
sed -n '1,260p' tools/ci/README.md 2>/dev/null
```

### 3. Search for current callers and references before inventing names

```bash
rg -n "catalog|stac|dcat|prov|crosslink|closure" \
  tools scripts tests .github docs data contracts schemas policy -S 2>/dev/null
```

### 4. Inspect executable reality instead of assuming it

```bash
find tools scripts -maxdepth 4 -type f \( -name "*.py" -o -name "*.sh" -o -name "*.mjs" -o -name "*.ts" \) 2>/dev/null | sort
```

### 5. Thin-slice local run

```bash
python tools/catalog/catalog_crosslink.py \
  --decision decision.json \
  --record promotion-record.json \
  --output catalog-crosslink-report.json
```

### 6. Thin-slice test run

```bash
pytest -q tests/catalog/test_catalog_crosslink.py
```

> [!TIP]
> Inventory first, then name the helper.
>
> In KFM, a clear “not present yet” result is stronger than a confident fantasy inventory.

[Back to top](#top)

---

## Usage

### Add a reusable catalog helper

Use `tools/catalog/` when the helper has **one clear catalog-centered job**, for example:

- structural STAC / DCAT / PROV QA
- triplet cross-link verification
- release-readiness summaries for catalog closure
- freshness, completeness, or drift reporting for review surfaces
- promotion-oriented closure checks that ensure outward catalog records still align with governed release artifacts

A good helper here should usually:

1. read explicit paths or flags
2. default to read-only inspection
3. emit stable machine-readable output when CI or review surfaces parse it
4. fail non-zero when it is meant to block
5. point back to concrete refs, paths, digests, or release objects

### Keep helper logic separate from orchestration

A healthy split looks like this:

- `tools/catalog/` owns reusable helper behavior
- `scripts/` owns wrapper entrypoints and operator choreography
- `.github/workflows/` owns when a gate runs
- `tests/catalog/` owns fixtures and assertions
- `data/catalog/` owns the metadata being inspected
- `tools/ci/` owns reviewer-readable rendering of stable helper outputs

### Tool behavior contract

| Concern | Working rule | Why |
|---|---|---|
| Mutation | Read-only by default | Preserves the trust membrane |
| Output | Emit stable, reviewable reports | Humans and CI should inspect the same result |
| Exit behavior | Use clear non-zero exits for blocking failures | Callers should not guess what happened |
| Surface area | Keep each helper narrow | Avoid helper-lane sprawl |
| Inputs | Require explicit paths or explicit resolution rules | Prevent accidental ambient authority |
| Tests | Add positive and negative-path fixtures | KFM verification includes failure paths |
| Docs | Update this README when lane behavior changes materially | Keeps documentary surfaces honest |
| Authority | Never become the owner of policy, schema-home law, publish state, or catalog truth | Prevents helper-code drift into sovereign truth |

[Back to top](#top)

---

## Diagram

```mermaid
flowchart LR
    A[data/catalog/stac|dcat|prov] --> B[tools/catalog/catalog_crosslink.py]
    R[promotion record / decision inputs] --> B
    B --> C[stable JSON report]
    C --> D[tests/catalog/ fixtures + assertions]
    C --> E[tools/ci/ reviewer renderers]
    C --> F[tools/validators/promotion_gate]
    G[scripts/ entrypoints] --> B
    H[.github/workflows/] --> B

    B -. no publish authority .-> P[data/published/]
    B -. no policy ownership .-> Q[policy/]
    B -. no schema-home authority .-> S[contracts/ + schemas/]
    B -. helper only .-> T[data/catalog/]
```

Above: `tools/catalog/` inspects outward catalog seams and emits stable outputs for tests, CI, and promotion review, while staying outside publication, policy, and schema-home authority.

[Back to top](#top)

---

## Reference tables

### Boundary map

| Surface | Primary job | Handoff rule |
|---|---|---|
| `tools/catalog/` | Catalog QA and cross-link inspection | Keep the question narrow and the output reviewable |
| `data/catalog/` | Release-backed STAC / DCAT / PROV records | Own metadata truth, not helper logic |
| `tools/validators/promotion_gate/` | Fail-closed promotion validation | Consume helper outputs, but keep decision law there |
| `tools/ci/` | Reviewer-facing rendering | Render stable outputs; do not redefine comparison or policy law |
| `tools/diff/` | Deterministic comparison helpers | Use when the main task is comparing governed states |
| `tests/catalog/` | Proof surface for catalog helper behavior | Assert positive and negative cases explicitly |
| `scripts/` | Thin orchestration | Call helpers, but do not hide logic there |
| `contracts/` + `schemas/` | Machine-readable authority surfaces | Define shapes and schema-home law outside this lane |
| `policy/` | Governance decisions | A helper supplies evidence; policy decides |

### Helper family matrix

| Helper family | Primary inputs | Expected outputs | Status |
|---|---|---|---|
| Structural QA | STAC items / collections, DCAT JSON-LD, PROV bundles | pass/fail report, structured errors | **PROPOSED** |
| Cross-link checks | STAC + DCAT + PROV + manifest / receipt refs | consistency report, missing-link diagnostics | **Thin-slice documented** |
| Reviewer summaries | catalog directories, release refs, timestamps | completeness / freshness / readiness summary | **PROPOSED** |
| Promotion closure helpers | promotion records, bundle refs, catalog triplet refs | closure alignment report | **Thin-slice documented** |

### What the current thin slice checks

| Check ID family | Meaning |
|---|---|
| ref presence | STAC, DCAT, and PROV refs exist |
| subject alignment | The triplet points at the same governed subject |
| version alignment | The triplet agrees on version |
| release-ref alignment | Release-facing refs line up with the triplet |

[Back to top](#top)

---

## Task list / definition of done

### Current task list

- [x] document `tools/catalog/` as a helper lane distinct from `data/catalog/`
- [x] document the current thin slice `catalog_crosslink.py`
- [x] document the thin-slice proof surface `tests/catalog/test_catalog_crosslink.py`
- [ ] extend triplet checking from ref-shape alignment to declared subject/property alignment inside mounted catalog records
- [ ] add freshness / report helper support for reviewer-facing closure summaries
- [ ] add optional rendering handoff to `tools/ci/`
- [ ] verify exact file-history dates, `doc_id`, and active-branch caller/workflow parity before publication

### Definition of done for a new helper in this lane

A new `tools/catalog/` helper is ready when:

1. its role is catalog-centered and narrow
2. it remains read-only by default
3. it emits stable machine-readable output
4. blocking behavior is explicit and testable
5. positive and negative-path tests exist
6. README guidance and quickstart commands stay synchronized
7. the helper does not take ownership of publish logic, policy meaning, or schema authority

[Back to top](#top)

---

## FAQ

### Why is this lane separate from `data/catalog/`?

Because KFM keeps metadata truth and helper logic separate. `data/catalog/` holds outward catalog objects. `tools/catalog/` holds reusable inspection and summary logic over those objects.

### Why is `catalog_crosslink.py` not enough to prove all catalog closure?

Because one helper can prove one narrow class of closure checks. Structural QA, richer subject/property inspection, freshness reporting, and broader release-facing review still need separate, explicitly bounded helpers.

### Should `tools/catalog/` ever decide promotion?

No. It may strengthen promotion inputs, but promotion authority belongs in the promotion-gate lane and adjacent governed review surfaces.

### Why keep this README so explicit about what is confirmed versus proposed?

Because KFM doctrine rejects turning helper-lane intention into implementation fact. This README is meant to stay useful during branch drift, subtree growth, and documentation review.

[Back to top](#top)

---

## Appendix

### Appendix A — Reading rule

Treat this README as a lane contract plus a current-state guide.

- “Current evidence snapshot” sections describe surfaced repo-facing reality.
- “PROPOSED” shapes describe safe next growth, not already-landed inventory.
- “NEEDS VERIFICATION” items should be checked against the exact working branch before merge.

### Appendix B — Minimal local comparison loop

When you change the current thin slice, review in this order:

1. helper behavior
2. test behavior
3. README quickstart
4. downstream handoff assumptions in `tools/ci/` and `tools/validators/promotion_gate/`

### Appendix C — Anti-patterns to reject

Do not let `tools/catalog/` become:

- the only explanation of publishability
- the place where schema authority is silently settled
- a hidden workflow-only implementation seam
- a substitute for catalog records
- a backdoor promotion engine

[Back to top](#top)
