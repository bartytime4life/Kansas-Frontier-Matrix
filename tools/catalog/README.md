<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION
title: tools/catalog/
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS_VERIFICATION
updated: 2026-04-13
policy_label: public
related: [../README.md, ../../data/README.md, ../../data/catalog/README.md, ../../scripts/README.md, ../../contracts/README.md, ../../schemas/README.md, ../../policy/README.md, ../../tests/README.md, ../../.github/README.md, ../../.github/CODEOWNERS, ../../tools/validators/promotion_gate/README.md, ../../tools/ci/README.md, ../../tools/attest/README.md, ../../tools/diff/README.md]
tags: [kfm, tools, catalog, dcat, stac, prov, crosslink, qa]
notes: [Merged from the older tools/catalog README and the later neighboring-lane thin-slice context. doc_id placeholder pending repo-internal registration; created/updated need live file-history verification; ownership grounded by visible CODEOWNERS fallback for /tools/.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/catalog/`

Catalog QA, cross-link, and reviewer-facing metadata helper surface for Kansas Frontier Matrix.

> Status: `experimental`
>
> Owners: `@bartytime4life`
>
> Repo fit: repo-root lane `tools/catalog/` · target file `tools/catalog/README.md` · parent [../README.md](../README.md) · metadata seam [../../data/catalog/README.md](../../data/catalog/README.md) · adjacent [../../scripts/README.md](../../scripts/README.md) · downstream [../../.github/README.md](../../.github/README.md)
>
> Evidence posture: repo-grounded for current public `main` plus KFM doctrine; any deeper helper inventory below is explicitly marked `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`
>
> Current public snapshot: `tools/catalog/` currently renders as `README.md` only on public `main`; the parent `tools/` lane already exists alongside sibling families such as `attest/`, `ci/`, `diff/`, `docs/`, `probes/`, and `validators/`, and the visible child lanes remain README-first in public view
>
> ![status: experimental](https://img.shields.io/badge/status-experimental-orange) ![doc: draft](https://img.shields.io/badge/doc-draft-blue) ![owners: @bartytime4life](https://img.shields.io/badge/owners-%40bartytime4life-6f42c1) ![lane: tools/catalog](https://img.shields.io/badge/lane-tools%2Fcatalog-0a7ea4) ![truth: evidence bounded](https://img.shields.io/badge/truth-evidence--bounded-555555)
>
> Quick jumps: [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Current evidence snapshot](#current-evidence-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> `tools/catalog/` is **not** `data/catalog/`.
> This directory is the reusable helper lane that inspects, validates, cross-checks, or summarizes catalog closure.
> The catalog records themselves belong in [../../data/catalog/README.md](../../data/catalog/README.md) and remain release-backed metadata, not helper-owned truth.

> [!TIP]
> **Current executable snapshot (thin-slice posture)**  
> `tools/catalog/` remains a catalog-helper lane with **bounded public executable evidence**.
> This README therefore documents:
>
> - the lane contract
> - the first-helper landing rules
> - the relationship between catalog closure and neighboring lanes
> - the expected helper families for QA, triplet cross-linking, and reviewer reporting
>
> Unlike the promotion lane and parts of `tools/ci/`, this lane does **not** yet claim a concrete current helper inventory beyond README-level public evidence unless verified on the active branch.

> [!NOTE]
> This README intentionally does two jobs at once:
>
> 1. describe the **confirmed** live public subtree honestly  
> 2. define the **proposed** executable helper shape that would make this lane useful without smuggling policy, schema authority, or publish logic into shell glue

---

## Scope

`tools/catalog/` is the KFM helper surface for **catalog closure quality**.

In practice, that means reusable tools that operate on the outward metadata seam anchored in **DCAT, STAC, and PROV**. These helpers should strengthen governed discovery, lineage inspection, triplet consistency, and promotion-readiness review without quietly becoming the source of truth for metadata law, policy law, or release state.

This lane exists because KFM treats catalog closure as operational infrastructure rather than optional metadata garnish. A good helper here should make catalog-backed trust easier to review, easier to automate, and easier to re-run locally.

### What this README is for

This file is meant to help maintainers do four things quickly:

1. understand what belongs in `tools/catalog/`
2. keep this lane separate from `data/catalog/`, `scripts/`, `contracts/`, `schemas/`, and `policy/`
3. extend the subtree without overclaiming mounted executable inventory
4. make the first real helper land with a clear boundary, caller, and proof burden

### Evidence markers used here

| Marker | Meaning in this README |
|---|---|
| `CONFIRMED` | Directly supported by the live public repo tree or documentary repo evidence |
| `INFERRED` | Strongly suggested by adjacent repo docs and KFM doctrine, but not proven as current subtree reality |
| `PROPOSED` | Doctrine-consistent target structure, helper family, or workflow pattern |
| `UNKNOWN` | Not established strongly enough from visible repo evidence |
| `NEEDS VERIFICATION` | A placeholder or repo/platform detail that should be checked before merge |

[Back to top](#top)

---

## Repo fit

`tools/catalog/` sits between the **catalog artifacts that already exist** and the **reviewable helper logic** that should keep those artifacts coherent.

### Path and adjacent surfaces

| Relation | Surface | Why it matters |
|---|---|---|
| Parent lane | [../README.md](../README.md) | Defines the broader `tools/` contract and helper-family expectations |
| Upstream metadata seam | [../../data/catalog/README.md](../../data/catalog/README.md) | Owns the governed `DCAT + STAC + PROV` closure surface that this lane should inspect, not replace |
| Parent lifecycle contract | [../../data/README.md](../../data/README.md) | Defines the `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED` truth path |
| Adjacent orchestration | [../../scripts/README.md](../../scripts/README.md) | Thin wrappers and CI entrypoints may call catalog helpers, but reusable logic should not be buried there |
| Shared object law | [../../contracts/README.md](../../contracts/README.md) and [../../schemas/README.md](../../schemas/README.md) | Helpers may validate declared authority, but must not silently define schema authority |
| Policy boundary | [../../policy/README.md](../../policy/README.md) | Rights, sensitivity, and deny-by-default rules belong there, even when helpers evaluate them |
| Verification surface | [../../tests/README.md](../../tests/README.md) | Fixtures and assertions should prove helper behavior instead of leaving README prose as the only evidence |
| Repo governance | [../../.github/README.md](../../.github/README.md) and [../../.github/CODEOWNERS](../../.github/CODEOWNERS) | Review boundaries, owner map, and merge posture live here |
| Neighbor helper lanes | [../../tools/ci/README.md](../../tools/ci/README.md), [../../tools/attest/README.md](../../tools/attest/README.md), [../../tools/diff/README.md](../../tools/diff/README.md), [../../tools/validators/README.md](../../tools/validators/README.md) | Catalog helpers should stay aligned with CI rendering, attestation, comparison, and validation lanes without absorbing their jobs |
| Promotion consumer | [../../tools/validators/promotion_gate/README.md](../../tools/validators/promotion_gate/README.md) | Promotion now makes catalog closure a first-class review surface; this lane is the natural helper boundary for closure QA and triplet checks |

### Operating rule

Use this lane when the work is:

- reusable
- catalog-specific
- callable by humans, scripts, or CI
- reviewable as a helper rather than as hidden business logic

Do **not** use this lane when the work is really:

- the catalog itself
- policy ownership
- schema ownership
- runtime API behavior
- one-off operator glue that should stay in `scripts/`

---

## Inputs

The following belong here when they remain helper inputs rather than truth stores:

- DCAT, STAC, and PROV records from `../../data/catalog/`
- related manifests, checksums, receipts, proofs, and release refs
- declared contract/schema surfaces used for validation
- read-only policy results or rule inputs needed to explain allow/deny/generalize outcomes
- bounded fixtures or non-sensitive sample records used to prove helper behavior
- reviewer/operator parameters for coverage, freshness, or cross-link summaries

### Accepted input profile

| Input family | Typical examples | Keep it here when |
|---|---|---|
| Catalog records | STAC collection/item JSON, DCAT JSON-LD, PROV bundles | the helper inspects or cross-checks them |
| Release linkage | manifests, checksums, receipts, proof refs | the helper verifies joinability or completeness |
| Contract surfaces | JSON Schemas, profile fragments, field expectations | the helper validates declared law without owning it |
| Review fixtures | valid/invalid samples, smoke inputs, snapshot outputs | the helper proves behavior in a repeatable way |
| CI/operator flags | `--root`, `--fail-on-warn`, explicit paths | the helper stays deterministic and easy to re-run |
| Promotion artifacts | decision refs, promotion records, bundle manifests | the helper checks whether outward catalog closure still aligns with governed promotion artifacts |
| Diff support | normalized prior/current catalog records | the helper checks closure or linkage, not policy meaning |

---

## Exclusions

The following do **not** belong here:

| Do not keep here | Better home | Why |
|---|---|---|
| Authoritative DCAT/STAC/PROV records | [../../data/catalog/README.md](../../data/catalog/README.md) | helper code must not become metadata truth |
| Raw or processed payloads | `../../data/raw/`, `../../data/work/`, `../../data/processed/` | payload storage and transformation live upstream |
| Policy bundles, reason codes, obligation registries | [../../policy/README.md](../../policy/README.md) | policy law must remain explicit and reviewable |
| Canonical contract/schema authority decisions | [../../contracts/README.md](../../contracts/README.md) and [../../schemas/README.md](../../schemas/README.md) | helpers may validate the chosen authority, not choose it silently |
| One-shot shell orchestration | [../../scripts/README.md](../../scripts/README.md) | wrappers may call helpers, but helper logic should stay reusable |
| Runtime API handlers or response envelopes | app/package surfaces | public behavior deserves stronger lifecycle ownership |
| Secret-bearing fixtures or unrestricted sensitive location dumps | governed secure lanes | public tooling must stay safe to clone and review |
| Signature generation or verification | [../../tools/attest/README.md](../../tools/attest/README.md) | catalog helpers may inspect signed state, but attestation belongs there |
| Reviewer rendering | [../../tools/ci/README.md](../../tools/ci/README.md) | catalog helpers should emit stable outputs that CI helpers can render |
| Promotion decisions | [../../tools/validators/README.md](../../tools/validators/README.md) | this lane can inform promotion, not decide it |

> [!CAUTION]
> If deleting a helper from `tools/catalog/` would erase the only understandable explanation of what is publishable, how policy was applied, or how catalog closure works, the helper is carrying too much meaning and should graduate to a stronger governed surface.

---

## Current evidence snapshot

| Evidence item | Status | How this README uses it |
|---|---|---|
| `tools/` exists on public `main` with sibling families `attest/`, `catalog/`, `ci/`, `diff/`, `docs/`, `probes/`, and `validators/` | `CONFIRMED` | grounds this file as one lane inside a broader helper family |
| `tools/catalog/` exists and currently shows `README.md` only on public `main` | `CONFIRMED` | prevents overclaiming executable helper inventory |
| `data/catalog/` exists with `dcat/`, `prov/`, and `stac/` child surfaces | `CONFIRMED` | grounds the adjacent metadata seam this lane should support |
| `tests/` exists as a top-level governed verification surface on public `main` | `CONFIRMED` | grounds the expectation that helpers should land with fixtures or assertions instead of prose alone |
| `/tools/` is owned by `@bartytime4life` in `/.github/CODEOWNERS` | `CONFIRMED` | grounds the owner line for this subtree |
| Promotion Gate documentation now treats catalog closure as part of review-significant promotion validation | `CONFIRMED via adjacent documentation` | strengthens the downstream value of reusable catalog QA and cross-link helpers |
| Mounted executable files under `tools/catalog/` beyond `README.md` | `UNKNOWN` | keeps deeper tool-family claims explicitly bounded |
| Exact file-history dates and repo-internal document ID for this README | `NEEDS VERIFICATION` | left as placeholders in the KFM meta block above |

[Back to top](#top)

---

## Directory tree

### Current live public neighborhood

```text
tools/
├── README.md
├── attest/
├── catalog/
│   └── README.md
├── ci/
├── diff/
├── docs/
├── probes/
└── validators/
```

### Adjacent live catalog seam

```text
data/catalog/
├── README.md
├── dcat/
├── prov/
└── stac/
```

### `PROPOSED` stable family shape to prefer

```text
tools/catalog/
├── README.md
├── qa/          # fast structural STAC / DCAT / PROV checks
├── crosslink/   # triplet + manifest / receipt consistency helpers
└── report/      # reviewer-facing completeness, freshness, and readiness summaries
```

That proposed shape is intentionally narrow.

- `qa/` keeps structural validation obvious
- `crosslink/` keeps triplet closure and evidence joins explicit
- `report/` keeps reviewer summaries separate from blocking validators

It avoids turning this lane into a hidden metadata factory.

### `PROPOSED` minimal single-helper landing shape

```text
tools/catalog/
├── README.md
└── catalog_crosslink.py
```

Use the smallest useful landing shape first if the subtree is still README-only in the working branch.

---

## Quickstart

Run these inventory-first commands before adding or moving anything under `tools/catalog/`.

### 1. Confirm what actually exists in your checkout

```bash
find tools/catalog -maxdepth 3 -print 2>/dev/null | sort
```

### 2. Re-read the parent helper contract and adjacent metadata / verification seams

```bash
sed -n '1,240p' tools/README.md 2>/dev/null
sed -n '1,260p' data/catalog/README.md 2>/dev/null
sed -n '1,260p' scripts/README.md 2>/dev/null
sed -n '1,260p' tests/README.md 2>/dev/null
sed -n '1,260p' tools/validators/promotion_gate/README.md 2>/dev/null
sed -n '1,260p' tools/ci/README.md 2>/dev/null
```

### 3. Search for current callers and references before inventing names

```bash
rg -n "catalog|stac|dcat|prov|crosslink|closure" tools scripts tests .github docs data policy contracts schemas pipelines -S 2>/dev/null
```

### 4. Inspect executable reality instead of assuming it exists

```bash
find tools scripts -maxdepth 4 -type f \( -name "*.py" -o -name "*.sh" -o -name "*.mjs" -o -name "*.ts" \) 2>/dev/null | sort
```

### 5. If the subtree is still scaffold-only locally, land the **first helper + caller + proof burden** in one change

```bash
echo "Plan one helper, one caller, one test/fixture set, one README delta."
```

> [!TIP]
> Inventory first, then name the helper.
> In KFM, a clear negative result is better than a confident fantasy inventory.

---

## Usage

### Add a reusable catalog helper

Use `tools/catalog/` when the helper has one clear job, for example:

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
5. point back to concrete artifacts, paths, digests, or release refs

### Keep helper logic separate from orchestration

A healthy split looks like this:

- `tools/catalog/` owns reusable helper behavior
- `scripts/` owns wrapper entrypoints and operator choreography
- `.github/workflows/` owns when the gate runs
- `tests/` owns fixtures and assertions
- `data/catalog/` owns the metadata being inspected
- `tools/ci/` owns reviewer-readable rendering of stable helper outputs

### Tool behavior contract

| Concern | Required posture |
|---|---|
| Determinism | Same inputs should yield the same output shape and exit code |
| Failure semantics | Blocking checks return non-zero and describe what failed |
| Output shape | Prefer JSON / JSONL or another stable format when CI or review surfaces consume it |
| Cross-link discipline | Reports should reference the concrete STAC/DCAT/PROV objects and any related manifest / receipt paths |
| Boundary discipline | No silent schema arbitration, no hidden policy law, no direct promotion shortcuts |
| Safety | No secret scraping, unrestricted sensitive fixtures, or logs that leak policy-restricted material |
| Reviewability | Humans, scripts, and CI should be able to call the same helper without semantic drift |
| Local/CI parity | A merge-blocking helper should be runnable locally with the same core behavior |

### When to graduate out of this lane

A helper should move out of `tools/catalog/` when it becomes:

- a reusable package or library
- the canonical place where schema or profile law is decided
- the only path that can generate valid metadata
- a service or runtime component rather than a helper CLI

[Back to top](#top)

---

## Diagram

```mermaid
flowchart LR
    P[data/processed + receipts + proofs + registry]
    CAT[data/catalog/\nDCAT + STAC + PROV]
    LAW[contracts/ + schemas/ + policy/]
    TC[tools/catalog/\nqa • crosslink • report]
    SC[scripts/\nwrappers / entrypoints]
    WF[.github/workflows/]
    TS[tests/fixtures]
    CI[tools/ci/\nreview renderers]
    RV[reviewers / governed APIs]

    P --> CAT
    LAW --> TC
    CAT --> TC
    TC -->|stable reports + exit codes| SC
    TC --> TS
    TC --> CI
    SC --> WF
    SC --> RV
    CI --> RV

    CAT -. remains metadata seam, not helper-owned truth .-> RV
    TC -. never bypass .-> LAW
```

---

## Tables

### Catalog helper boundary matrix

| Surface | Primary job | Must not quietly become |
|---|---|---|
| `data/catalog/` | release-backed DCAT/STAC/PROV metadata seam | helper-owned truth |
| `tools/catalog/` | reusable catalog QA, cross-link, and review support helpers | schema authority, policy authority, or release truth |
| `scripts/` | thin wrappers and operator/CI entrypoints | the only place helper behavior is documented |
| `contracts/` / `schemas/` | declared object grammar and validation law | implicit shell glue |
| `policy/` | rights, sensitivity, and deny-by-default rule ownership | undocumented helper side effects |
| `tools/ci/` | reviewer-facing rendering of stable outputs | hidden validator logic |

### Helper class matrix

| Helper class | Typical inputs | Typical outputs | Status in this README |
|---|---|---|---|
| Structural QA | STAC items / collections, DCAT JSON-LD, PROV bundles | pass/fail report, structured errors | `PROPOSED` executable family |
| Cross-link checks | STAC + DCAT + PROV + manifest / receipt refs | consistency report, missing-link diagnostics | `PROPOSED` executable family |
| Reviewer summaries | catalog directories, release refs, timestamps | completeness / freshness / readiness summary | `PROPOSED` executable family |
| Promotion closure helpers | promotion records, bundle refs, catalog triplet refs | closure alignment report | `PROPOSED` executable family |
| Scaffold-only current state | `README.md` | documentation only | `CONFIRMED` current subtree reality |

### Triplet questions this lane should answer well

| Question | Typical helper family |
|---|---|
| Does STAC link cleanly to the matching outward subject? | `qa/` or `crosslink/` |
| Does DCAT point to the same release-backed thing as STAC? | `crosslink/` |
| Does PROV name the same promoted subject and lineage context? | `crosslink/` |
| Do triplet members drift from receipts or release refs? | `crosslink/` |
| Is the closure fresh / complete / reviewable enough for promotion review? | `report/` |

---

## Task list

### Definition of done for the first real helper in this lane

- [ ] current local inventory rechecked before merge
- [ ] helper placed in the narrowest fitting family under `tools/catalog/`
- [ ] caller relationship documented in [../../scripts/README.md](../../scripts/README.md) or the relevant adjacent README
- [ ] at least one representative passing input and one failing input exist in `../../tests/` or another governed fixture surface
- [ ] helper output format and exit semantics are documented here
- [ ] boundary against `data/catalog/`, `contracts/`, `schemas/`, and `policy/` remains explicit
- [ ] merge-blocking behavior, if any, is runnable locally as well as in CI
- [ ] no secrets or policy-restricted sample payloads are committed here
- [ ] if promotion or bundle-aware closure checks are added, they report closure state without deciding release law

---

## FAQ

### Why is this not just part of `scripts/`?

Because KFM distinguishes **thin orchestration** from **reusable helper behavior**. Wrappers may live in `scripts/`; repeatable catalog checks belong in a reusable helper lane.

### Why not write catalog logic directly in workflow YAML?

Because reviewer-facing logic should stay inspectable outside CI configuration. Stable tool entrypoints are easier to run locally, easier to diff, and easier to test.

### Can `tools/catalog/` generate catalog files?

Only in a narrow support role and only when the authoritative metadata rules live somewhere stronger. This lane should support declared law, not become undeclared law.

### Where should fixtures live?

Prefer `../../tests/` or another governed fixture surface. Keep this lane focused on helpers, not fixture ownership.

### Is `tools/catalog/` allowed to decide which schema home is authoritative?

No. It may validate the declared authority. It must not silently choose one.

### Can this lane help promotion review?

Yes. Catalog closure is now visibly relevant to promotion review. But this lane should report and cross-check closure state, not decide whether release should proceed.

[Back to top](#top)

---

## Appendix

<details>
<summary>Illustrative adjacent wrapper pattern (`PROPOSED`, document-grounded, not current subtree proof)</summary>

The broader KFM documentation corpus already uses thin-wrapper examples like this:

```text
scripts/catalog/validate_stac.py
scripts/catalog/validate_jsonld.sh
scripts/evidence/crosslink_consistency.py
```

A healthy relationship would keep those as wrappers while reusable catalog-checking logic lives here.

</details>

<details>
<summary>Illustrative blocking output shape</summary>

```json
{
  "tool": "catalog-crosslink",
  "status": "fail",
  "blocking": true,
  "catalog_root": "data/catalog/",
  "checks": [
    {
      "id": "stac-self-link",
      "result": "pass"
    },
    {
      "id": "dcat-prov-linkage",
      "result": "fail",
      "message": "dataset record missing matching PROV bundle reference"
    }
  ]
}
```

Use a stable output shape when CI, review summaries, or release evidence need to parse the result.

</details>

<details>
<summary>Illustrative promotion-oriented closure output (`PROPOSED`)</summary>

```json
{
  "tool": "catalog-promotion-closure",
  "status": "warn",
  "blocking": false,
  "candidate_id": "overlay:floodplain-kansas",
  "spec_hash": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "checks": [
    {
      "id": "stac-dcat-subject-alignment",
      "result": "pass"
    },
    {
      "id": "prov-release-ref-alignment",
      "result": "warn",
      "message": "PROV bundle present but missing outward release_ref echo"
    }
  ]
}
```

That kind of helper belongs here only if it remains a closure checker and does not become a promotion authority surface.

</details>

[Back to top](#top)
