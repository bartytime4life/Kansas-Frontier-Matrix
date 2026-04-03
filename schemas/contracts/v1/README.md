<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: schemas/contracts/v1
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: 2026-04-03
policy_label: NEEDS-VERIFICATION
related: [../README.md, ../vocab/README.md, ../../README.md, ../../tests/README.md, ../../tests/fixtures/contracts/v1/README.md, ../../workflows/README.md, ../../../contracts/README.md, ../../../docs/standards/README.md, ../../../policy/README.md, ../../../tests/README.md, ../../../tests/contracts/README.md, ../../../.github/workflows/README.md]
tags: [kfm, schemas, contracts, v1, readme]
notes: [doc_id, created date, and policy_label need verification; updated date reflects the current-session revision date; public-main tree confirms live v1 family lanes, sibling vocab registries, and nested schema-tests scaffolds, but canonical schema-home authority remains unresolved]
[/KFM_META_BLOCK_V2] -->

# `schemas/contracts/v1`

Versioned boundary guide and current-state index for the live public `schemas/contracts/v1/` contract-family lane.

Repo fit: path `schemas/contracts/v1/README.md` · parent [`../README.md`](../README.md) · sibling machine-file lane [`../vocab/README.md`](../vocab/README.md) · sibling schema fixture lane [`../../tests/README.md`](../../tests/README.md) · sibling schema workflow boundary [`../../workflows/README.md`](../../workflows/README.md) · stronger doctrinal contract lane [`../../../contracts/README.md`](../../../contracts/README.md)

> [!IMPORTANT]
> **Status:** experimental · **Owners:** `@bartytime4life` *(via public `.github/CODEOWNERS` global fallback; no narrower `/schemas/` rule was directly verified on public `main`)* · **Path:** `schemas/contracts/v1/README.md`  
> **Current role:** index the live `v1` subtree honestly, keep schema-home ambiguity visible, and stop placeholder scaffolds from being mistaken for enforcement-grade contract law.

![Status](https://img.shields.io/badge/status-experimental-orange?style=flat-square)
![Contracts v1](https://img.shields.io/badge/contracts-v1-2563eb?style=flat-square)
![Tree](https://img.shields.io/badge/public_tree-live%20family%20lane-brightgreen?style=flat-square)
![Schema body](https://img.shields.io/badge/schema_bodies-placeholder_%7B%7D-b91c1c?style=flat-square)
![Authority](https://img.shields.io/badge/schema_home-unresolved-6b7280?style=flat-square)

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Current public snapshot](#current-public-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Family registry](#family-registry) · [Task list / definition of done](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

---

## Scope

`schemas/contracts/v1/` is now a **real, public, versioned subtree** under `schemas/contracts/`.

That changes how this README has to behave. It is no longer safe to describe this path as hypothetical, and it is still not safe to treat file presence alone as proof that canonical contract authority has moved here.

This README should now do five jobs well:

1. record the current public `v1/` tree and its family files;
2. keep the still-stronger `contracts/`-side authority signal visible;
3. route contributors toward the sibling lanes that now matter operationally;
4. keep placeholder bodies, fixture scaffolds, policy, and workflow execution in distinct surfaces; and
5. make a future authority decision easy to merge without another full rewrite.

### Truth posture used here

| Label | Meaning in this file |
|---|---|
| **CONFIRMED** | Directly visible on current public `main` or directly stated in adjacent public repo docs reopened for this revision. |
| **INFERRED** | Conservative interpretation that fits the visible tree and repeated KFM doctrine, but is not itself a checked-in authority decision. |
| **PROPOSED** | Safe next-step guidance that fits KFM doctrine and current repo reality, but is not presented as settled implementation. |
| **UNKNOWN** | Not verified strongly enough to present as current checked-in or platform reality. |
| **NEEDS VERIFICATION** | A review placeholder important enough to block stronger claims until directly checked. |

[Back to top](#schemascontractsv1)

## Repo fit

| Field | Value |
|---|---|
| **Path** | `schemas/contracts/v1/README.md` |
| **Audience** | Maintainers working on machine-readable contract families, schema-home reconciliation, fixtures, policy adjacency, and workflow-proof follow-through. |
| **Parent lane** | [`../README.md`](../README.md) |
| **Sibling machine-file lane** | [`../vocab/README.md`](../vocab/README.md) |
| **Sibling schema-lane boundaries** | [`../../README.md`](../../README.md), [`../../tests/README.md`](../../tests/README.md), [`../../workflows/README.md`](../../workflows/README.md) |
| **Stronger doctrinal contract signal** | [`../../../contracts/README.md`](../../../contracts/README.md) |
| **Adjacent standards / proof / gate surfaces** | [`../../../docs/standards/README.md`](../../../docs/standards/README.md), [`../../../policy/README.md`](../../../policy/README.md), [`../../../tests/README.md`](../../../tests/README.md), [`../../../tests/contracts/README.md`](../../../tests/contracts/README.md), [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md) |
| **Current public path signal** | `schemas/contracts/v1/` is materially present on public `main` with eight family subdirectories and checked-in `*.schema.json` files. |
| **Current public body signal** | All eight `v1` schema files directly reopened for this revision are currently `{}`. |
| **Current role** | Boundary-first, inventory-first, reconciliation-first README for a live subtree that is still placeholder-heavy. |
| **Authority posture** | **UNKNOWN / NEEDS VERIFICATION** |

### Upstream and downstream links

**Upstream and sibling context**

- [`../../README.md`](../../README.md)
- [`../README.md`](../README.md)
- [`../vocab/README.md`](../vocab/README.md)
- [`../../tests/README.md`](../../tests/README.md)
- [`../../workflows/README.md`](../../workflows/README.md)

**Cross-root doctrinal and enforcement context**

- [`../../../contracts/README.md`](../../../contracts/README.md)
- [`../../../docs/standards/README.md`](../../../docs/standards/README.md)
- [`../../../policy/README.md`](../../../policy/README.md)
- [`../../../tests/README.md`](../../../tests/README.md)
- [`../../../tests/contracts/README.md`](../../../tests/contracts/README.md)
- [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md)

**Downstream family lanes**

- [`./common/`](./common/)
- [`./correction/`](./correction/)
- [`./data/`](./data/)
- [`./evidence/`](./evidence/)
- [`./policy/`](./policy/)
- [`./release/`](./release/)
- [`./runtime/`](./runtime/)
- [`./source/`](./source/)

> [!WARNING]
> Read this path as **live inventory plus unresolved law**.
>
> The subtree is real. The canonical-home decision is not yet publicly settled.

[Back to top](#schemascontractsv1)

## Inputs

### Accepted inputs

This lane should accept only material that clearly belongs to the versioned `v1` contract-family subtree.

| Accepted here | Why |
|---|---|
| Version-lane README improvements | Keeps the subtree navigable and reviewable. |
| Inventory updates tied to visible public-main changes | Prevents the index from drifting behind the tree. |
| Links to family-specific schema files already present in this subtree | Keeps navigation local and predictable. |
| Cross-links to sibling vocab, fixtures, and workflow-boundary docs | Those surfaces now materially affect how this lane is read. |
| Authority notes, ADR references, and migration guidance | Schema-home authority is still unresolved. |
| Family-level documentation that explains role, maturity, and next proof burden | Helpful without inventing enforcement depth. |
| Generated or mirrored outputs **only if** the repo later formalizes that pattern | Safe only after authority and lifecycle are explicit. |

### Strengthening prerequisites

If this subtree is going to become more than scaffold:

1. the repo needs one explicit authoritative schema-home decision;
2. the family `*.schema.json` files need substantive JSON Schema bodies instead of `{}`;
3. valid and invalid fixture packs need a confirmed home and direct file-level proof;
4. validator entrypoints need to be checked in and linkable; and
5. workflow automation needs to prove these files actually gate trust-bearing changes.

[Back to top](#schemascontractsv1)

## Exclusions

This lane should **not** become a second trust platform hidden inside a neat directory tree.

| Excluded from this path | Put it here instead |
|---|---|
| Competing canonical copies of the same family under both `schemas/` and `contracts/` | Resolve authority first, then keep one authoritative home plus any explicitly declared mirror/pointer strategy. |
| Shared reason / obligation / reviewer registries | [`../vocab/README.md`](../vocab/README.md) |
| Executable policy bundles, rule logic, or review engines | [`../../../policy/README.md`](../../../policy/README.md) |
| Fixture inventories, valid/invalid example packs, drill payloads, or contract harnesses | [`../../tests/README.md`](../../tests/README.md), [`../../../tests/README.md`](../../../tests/README.md), [`../../../tests/contracts/README.md`](../../../tests/contracts/README.md) |
| GitHub Actions YAML, dispatch wiring, permissions, required checks, or environment approvals | [`../../workflows/README.md`](../../workflows/README.md) for boundary notes, and [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md) for executable workflow inventory |
| Release proof packs, rollback artifacts, or emitted runtime envelopes as primary records | release / data / proof-pack / runtime emit surfaces |
| UI payload examples that are really app-surface contracts | the owning app, package, or eventual authoritative contract home |
| Domain-specific ETL semantics or publication policy | domain docs, pipeline docs, or policy docs |

> [!CAUTION]
> A tidy folder that quietly mixes schemas, fixtures, policy, and workflow execution is worse than an incomplete folder that states its limits plainly.

[Back to top](#schemascontractsv1)

## Current public snapshot

The local `schemas/` picture is more synchronized than earlier drafts assumed. The remaining tension is now mostly **cross-root**:

- `schemas/README.md` and `schemas/contracts/README.md` both acknowledge the live subtree;
- `schemas/contracts/vocab/` and `schemas/tests/` now matter to how `v1/` should be read; but
- root `contracts/README.md` and `docs/standards/README.md` still route machine contracts more strongly toward root `contracts/`, and some of their inventory language still lags the live `schemas/` tree.

### Summary signal matrix

| Signal | Current public read |
|---|---|
| **Tree reality** | `schemas/contracts/v1/` exists with eight family lanes: `common`, `correction`, `data`, `evidence`, `policy`, `release`, `runtime`, and `source`. |
| **File reality** | Each lane has a local `README.md` plus one `*.schema.json`; all eight raw schema bodies directly reopened for this revision are `{}`. |
| **Sibling machine-file reality** | `schemas/contracts/vocab/` is also materialized, with `README.md`, `reason_codes.json`, `obligation_codes.json`, and `reviewer_roles.json`. |
| **Fixture reality** | `schemas/tests/fixtures/contracts/v1/README.md` is present, and `schemas/tests/README.md` documents a visible `valid/` + `invalid/` scaffold beneath it. |
| **Verification reality** | `tests/contracts/` exists as the stronger contract-facing verification family, but current public inventory there is still `README.md` only. |
| **Workflow reality** | `.github/workflows/` remains `README.md` only on public `main`; deleted workflow names remain historical signal, not current checked-in YAML proof. |
| **Authority reality** | `schemas/` materialization is real, but canonical schema-home authority is still unresolved and standards/doctrinal routing still leans toward root `contracts/`. |

### Adjacent doc matrix

| Surface | Current public signal | Why it matters here |
|---|---|---|
| [`../../README.md`](../../README.md) | Now acknowledges the live `schemas/` subtree and explicitly calls out `./contracts/v1/*/*.schema.json`, `./contracts/vocab/*.json`, and `schemas/tests/` scaffold context | The parent lane is no longer pretending this subtree is absent |
| [`../README.md`](../README.md) | Now acknowledges both `v1/` and `vocab/` as live `schemas/contracts/` children | The immediate parent lane is materially synchronized with the local tree |
| [`../vocab/README.md`](../vocab/README.md) | Confirms the current branch-visible vocabulary registries and keeps long-term authority unresolved | Shared registries already have a local machine-file lane outside `v1/` |
| [`../../tests/README.md`](../../tests/README.md) | Confirms `schemas/tests/` as a real nested lane and documents a visible `fixtures/contracts/v1/{valid,invalid}` scaffold | There is now a nearby fixture-boundary surface inside the `schemas/` subtree |
| [`../../workflows/README.md`](../../workflows/README.md) | Keeps workflow-adjacent schema discussion boundary-only and explicitly separates it from executable `.github/workflows/` automation | This helps keep execution and schema topic organization distinct |
| [`../../../contracts/README.md`](../../../contracts/README.md) | Still presents root `contracts/` as the stronger contract-publication lane and still describes current visible `schemas/` inventory as README-only | The authority signal remains strong, but part of the inventory prose is now stale relative to the live tree |
| [`../../../docs/standards/README.md`](../../../docs/standards/README.md) | Still routes machine contracts toward root `contracts/` and still describes `../../schemas/README.md` as a README-only lane | Standards posture continues to reinforce contracts-side authority while lagging live `schemas/` inventory reality |
| [`../../../tests/contracts/README.md`](../../../tests/contracts/README.md) | Contract-facing verification family exists, but current public inventory is README-only | Contract verification has a named home, but runner depth remains unproven |
| [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md) | Confirms the workflow lane is README-only and records deleted workflow names as historical signal only | CI enforcement burden remains documentary from public-main evidence alone |
| [`../../../.github/CODEOWNERS`](../../../.github/CODEOWNERS) | Uses a global fallback plus explicit root-lane rules; no narrower `/schemas/` rule is directly visible | Ownership for this file is grounded through fallback, not through a schema-specific rule |

> [!IMPORTANT]
> The local synchronization story has improved.
>
> The unresolved split now lives mostly between **live `schemas/` materialization** and **cross-root authority routing toward `contracts/`**.

[Back to top](#schemascontractsv1)

## Directory tree

### Context tree

```text
schemas/
├── README.md
├── contracts/
│   ├── README.md
│   ├── v1/
│   │   ├── README.md
│   │   ├── common/
│   │   │   ├── README.md
│   │   │   └── header_profile.schema.json
│   │   ├── correction/
│   │   │   ├── README.md
│   │   │   └── correction_notice.schema.json
│   │   ├── data/
│   │   │   ├── README.md
│   │   │   └── dataset_version.schema.json
│   │   ├── evidence/
│   │   │   ├── README.md
│   │   │   └── evidence_bundle.schema.json
│   │   ├── policy/
│   │   │   ├── README.md
│   │   │   └── decision_envelope.schema.json
│   │   ├── release/
│   │   │   ├── README.md
│   │   │   └── release_manifest.schema.json
│   │   ├── runtime/
│   │   │   ├── README.md
│   │   │   └── runtime_response_envelope.schema.json
│   │   └── source/
│   │       ├── README.md
│   │       └── source_descriptor.schema.json
│   └── vocab/
│       ├── README.md
│       ├── obligation_codes.json
│       ├── reason_codes.json
│       └── reviewer_roles.json
├── tests/
│   ├── README.md
│   └── fixtures/
│       └── contracts/
│           └── v1/
│               ├── README.md
│               ├── invalid/
│               └── valid/
└── workflows/
    └── README.md
```

### Reading rule for the tree

- Tree presence is **CONFIRMED**.
- Machine-file presence is **not** the same thing as settled canonical authority.
- The `invalid/` and `valid/` leaves are confirmed by the sibling `../../tests/README.md` surface; re-open them directly before making file-level claims about their contents.
- All eight raw `v1` schema files directly reopened for this revision are currently `{}`.
- That makes this lane **materialized, documented, and still placeholder-heavy**.

[Back to top](#schemascontractsv1)

## Quickstart

Use this path first as an inspection lane, not as a place to assume contract maturity.

```bash
# 1) Inventory the live v1 lane
find schemas/contracts/v1 -maxdepth 2 \( -type f -o -type d \) | sort

# 2) Re-open every checked-in v1 schema body
find schemas/contracts/v1 -name '*.schema.json' -type f | sort \
  | while read -r f; do
      printf '\n== %s ==\n' "$f"
      cat "$f"
    done

# 3) Inspect sibling machine-file and scaffold context
find schemas/contracts/vocab -maxdepth 1 -type f | sort
find schemas/tests/fixtures/contracts/v1 -maxdepth 2 \( -type f -o -type d \) | sort
find tests/contracts -maxdepth 2 \( -type f -o -type d \) | sort
find .github/workflows -maxdepth 2 -type f | sort

# 4) Re-open the boundary docs that govern how this lane should be read
sed -n '1,260p' schemas/README.md
sed -n '1,260p' schemas/contracts/README.md
sed -n '1,220p' schemas/contracts/vocab/README.md
sed -n '1,220p' schemas/tests/README.md
sed -n '1,220p' schemas/workflows/README.md
sed -n '1,260p' contracts/README.md
sed -n '1,220p' docs/standards/README.md
sed -n '1,220p' tests/contracts/README.md
sed -n '1,220p' .github/workflows/README.md

# 5) Re-open at least one local family guide before editing a family
sed -n '1,240p' schemas/contracts/v1/common/README.md
sed -n '1,240p' schemas/contracts/v1/source/README.md
```

### Safe review sequence

1. Re-read `schemas/README.md`, `schemas/contracts/README.md`, and `schemas/contracts/vocab/README.md`.
2. Re-check `schemas/tests/README.md`, `tests/contracts/README.md`, and `.github/workflows/README.md` before claiming fixtures or automation depth.
3. Inspect the exact family README and `*.schema.json` body you want to touch.
4. Confirm whether an ADR or equivalent repo decision now resolves schema-home authority.
5. Only then decide whether the change belongs here, in root `contracts/`, in a sibling `schemas/*` boundary lane, or in `tests/`, `policy/`, or workflow control surfaces.

> [!TIP]
> If you cannot say which directory is authoritative **before** you edit a trust-bearing family, pause and resolve that question first. Silent duplication is harder to unwind than a deliberate delay.

[Back to top](#schemascontractsv1)

## Usage

### Recommended use right now

Use this README as:

- the versioned index for the current public `schemas/contracts/v1/` tree;
- a warning surface against schema-home drift;
- a routing surface to `../vocab/`, `../../tests/`, and root proof / workflow boundaries;
- a contributor checkpoint before adding or expanding any trust-bearing family; and
- a reconciliation aid between live subtree reality and still-unsettled authority language.

### Recommended use after authority is resolved

| If `schemas/` becomes authoritative | If `contracts/` becomes authoritative |
|---|---|
| Expand this README into the normative `v1` contract index and keep root `contracts/` as pointer/generated output only if explicitly declared. | Convert this README into a pointer or mirror guide and move normative contract maintenance to the `contracts/`-side versioned lanes. |

### Update rules

- Keep relative links stable.
- Prefer **small, reviewable updates** over a second full rewrite.
- Do not remove explicit uncertainty labels until public evidence supports the stronger claim.
- When a schema body stops being `{}`, update the family registry and note the first linked fixture/test surface.
- When nested `schemas/tests` fixtures gain real file content, link them here only after direct re-open.
- When workflow enforcement lands, add the exact workflow file and validation command.
- When cross-root docs still lag the tree, reconcile them in the same reviewed change stream so readers do not inherit conflicting stories.

[Back to top](#schemascontractsv1)

## Diagram

```mermaid
flowchart TD
    A[schemas/README.md<br/>live subtree acknowledged] --> V[v1 lane]
    B[schemas/contracts/README.md<br/>v1 + vocab acknowledged] --> V
    C[schemas/contracts/vocab/README.md<br/>shared registries] --> V
    D[schemas/tests/README.md<br/>fixture scaffold visible] --> F[Fixture context]
    E[schemas/workflows/README.md<br/>boundary-only] --> W[Workflow boundary]

    G[contracts/README.md<br/>stronger doctrinal contract lane<br/>root tree README-only] -. authority signal .-> V
    H[docs/standards/README.md<br/>routes machine contracts to contracts/] -. standards signal .-> V

    I[tests/contracts/README.md<br/>contract verification family<br/>README-only] --> F
    J[.github/workflows/README.md<br/>workflow lane README-only] --> W
    K[.github/CODEOWNERS<br/>global fallback only for schemas] --> V

    V --> L[common]
    V --> M[correction]
    V --> N[data]
    V --> O[evidence]
    V --> P[policy]
    V --> Q[release]
    V --> R[runtime]
    V --> S[source]

    L --> T[placeholder schema bodies {}]
    M --> T
    N --> T
    O --> T
    P --> T
    Q --> T
    R --> T
    S --> T

    F --> U[visible scaffold, not proved runnable]
    W --> X[historical workflow signal,<br/>not checked-in YAML proof]
```

### Interpretation

The diagram is intentionally conservative:

- `schemas/contracts/v1/` is shown as a **live public subtree**;
- sibling machine-file and fixture-boundary lanes are shown because they now materially affect how `v1/` should be read;
- root `contracts/` and `docs/standards/` still provide the stronger documentary authority signal;
- root `tests/contracts/` and `.github/workflows/` remain important proof/gate surfaces, but public-main inventory there is still docs-only; and
- the current `v1` schema bodies remain **placeholder state**, not enforcement-grade contract law.

[Back to top](#schemascontractsv1)

## Family registry

| Family | Local guide | Schema file | Current body state | Current read |
|---|---|---|---|---|
| Common | [`./common/README.md`](./common/README.md) | [`./common/header_profile.schema.json`](./common/header_profile.schema.json) | `{}` | Shared header/profile lane is materialized, but its schema body is still scaffold-state. |
| Correction | [`./correction/README.md`](./correction/README.md) | [`./correction/correction_notice.schema.json`](./correction/correction_notice.schema.json) | `{}` | Correction family is present, but not yet field-level contract law. |
| Data | [`./data/README.md`](./data/README.md) | [`./data/dataset_version.schema.json`](./data/dataset_version.schema.json) | `{}` | Dataset-version family is visible, but still placeholder-only. |
| Evidence | [`./evidence/README.md`](./evidence/README.md) | [`./evidence/evidence_bundle.schema.json`](./evidence/evidence_bundle.schema.json) | `{}` | Evidence-bundle family is present, but current machine body is still empty. |
| Policy | [`./policy/README.md`](./policy/README.md) | [`./policy/decision_envelope.schema.json`](./policy/decision_envelope.schema.json) | `{}` | Decision-envelope lane is visible, but executable meaning still depends on future schema + policy proof. |
| Release | [`./release/README.md`](./release/README.md) | [`./release/release_manifest.schema.json`](./release/release_manifest.schema.json) | `{}` | Release-manifest lane exists, but release-proof semantics are not yet encoded here. |
| Runtime | [`./runtime/README.md`](./runtime/README.md) | [`./runtime/runtime_response_envelope.schema.json`](./runtime/runtime_response_envelope.schema.json) | `{}` | Runtime envelope lane is present, but public-main body is still placeholder-only. |
| Source | [`./source/README.md`](./source/README.md) | [`./source/source_descriptor.schema.json`](./source/source_descriptor.schema.json) | `{}` | SourceDescriptor lane is live and documented, but still boundary-first rather than enforcement-grade. |

### Why this registry matters

Folder names can make a lane look mature long before the schema bodies are. This table is here to stop that mistake.

[Back to top](#schemascontractsv1)

## Task list / definition of done

A revision to this README is in good shape when the following are true:

- [ ] the KFM Meta Block v2 is present and unresolved values remain visibly reviewable;
- [ ] title, purpose line, and repo-fit line match the file’s actual role;
- [ ] current public `v1/` tree contents are described honestly;
- [ ] sibling machine-file and fixture-boundary context are included where they materially change how `v1/` should be read;
- [ ] schema-home ambiguity is visible, not hidden;
- [ ] relative links resolve to the right nearby repo surfaces;
- [ ] the directory tree matches the current public snapshot being described;
- [ ] the family registry distinguishes **present** from **placeholder** cleanly;
- [ ] no section implies runnable validators, merge-blocking workflow YAML, or settled canonical authority without evidence;
- [ ] the Mermaid diagram still reflects the actual local-versus-cross-root boundary condition; and
- [ ] a future authority decision can be merged into this file without another rewrite.

### Review gates for maintainers

| Gate | Pass condition |
|---|---|
| **Truth gate** | No unsupported authority or enforcement claim slips in. |
| **Boundary gate** | The file does not blur `schemas/`, `contracts/`, `tests/`, `policy/`, and workflow responsibilities. |
| **Navigation gate** | A new maintainer can find each family, sibling context lane, and cross-root proof surface quickly. |
| **Drift gate** | The file makes silent duplication harder, not easier. |
| **Reconciliation gate** | Cross-root docs that still lag the live tree are called out explicitly instead of being silently harmonized away. |

[Back to top](#schemascontractsv1)

## FAQ

### Is `schemas/contracts/v1/` real on current public `main`?

Yes. Treat the subtree itself as **CONFIRMED public inventory**.

### Is it the canonical machine-contract home?

**UNKNOWN / NEEDS VERIFICATION.**  
The subtree is real, but the stronger documentary authority signal still leans toward root `contracts/`, and no public ADR or equivalent repo decision was directly verified here.

### Why not rewrite this as a normative contract index right now?

Because that would silently convert live tree presence into authority. Current public evidence does not justify that move.

### Do the nested `schemas/tests` fixtures mean this lane already has runnable examples?

No. They prove nearby scaffold presence, not mounted executable contract validation. Re-open the exact fixture files and validator entrypoints before making stronger claims.

### Why keep root `contracts/` in view if the machine files are here?

Because KFM’s doctrine still cares more about singular authority than about whichever path materialized first. A validator cannot safely govern two competing homes for the same trust-bearing family.

### What should happen when the authority decision lands?

Update this README immediately:

- if this lane becomes authoritative, turn it into the normative `v1` contract index;
- if root `contracts/` becomes authoritative, turn this lane into an explicit pointer or mirror guide; and
- in either case, remove ambiguity **only after** the decision is public and linkable.

[Back to top](#schemascontractsv1)

## Appendix

<details>
<summary><strong>Observed public files in and around this lane</strong></summary>

### Directly reopened in this revision

- `./README.md`
- `./common/README.md`
- `./common/header_profile.schema.json`
- `./correction/README.md`
- `./correction/correction_notice.schema.json`
- `./data/README.md`
- `./data/dataset_version.schema.json`
- `./evidence/README.md`
- `./evidence/evidence_bundle.schema.json`
- `./policy/README.md`
- `./policy/decision_envelope.schema.json`
- `./release/README.md`
- `./release/release_manifest.schema.json`
- `./runtime/README.md`
- `./runtime/runtime_response_envelope.schema.json`
- `./source/README.md`
- `./source/source_descriptor.schema.json`

### Nearby public context reopened in this revision

- `../README.md`
- `../vocab/README.md`
- `../../README.md`
- `../../tests/README.md`
- `../../tests/fixtures/contracts/v1/README.md`
- `../../workflows/README.md`
- `../../../contracts/README.md`
- `../../../docs/standards/README.md`
- `../../../policy/README.md`
- `../../../tests/README.md`
- `../../../tests/contracts/README.md`
- `../../../.github/workflows/README.md`
- `../../../.github/CODEOWNERS`

</details>

<details>
<summary><strong>Contributor checklist before editing a trust-bearing family</strong></summary>

1. Re-open the exact family README and the exact `*.schema.json` body.
2. Re-check `schemas/contracts/vocab/README.md`, `schemas/tests/README.md`, and root `tests/contracts/README.md`.
3. Re-read root `contracts/README.md` and `docs/standards/README.md` before making any authority claim.
4. Confirm whether the change is a schema change, a vocab change, a fixture change, a policy change, or a workflow change.
5. Update this README if the public inventory, sibling context, or authority posture changes.
6. Reconcile any stale cross-root inventory wording in the same reviewed change stream.

</details>

---

This README should remain intentionally honest: **useful now, stronger later, and never more certain than the repo evidence allows.**
