<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO-UUID>
title: Data Registry Schemas
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-02-14
updated: 2026-03-22
policy_label: <TODO: verify public|restricted|...>
related: [../README.md, ../../README.md, ../../../contracts/README.md, ../../../schemas/README.md, ../../../schemas/contracts/README.md, ../../../tests/README.md, ../../../policy/README.md, ../../../.github/workflows/README.md, ../../../.github/CODEOWNERS]
tags: [kfm, data, registry, schemas]
notes: [Created/updated dates preserved from the current public-history baseline draft; doc_id and policy_label remain unverified; refresh updated on merge if this revision lands]
[/KFM_META_BLOCK_V2] -->

# Data Registry Schemas

Registry-local schema surface for KFM dataset and source registration entries, kept intentionally narrow so shared contract authority does not drift.

> **Status:** `experimental`  
> **Owners:** `@bartytime4life`  
> **Repo fit:** `data/registry/schemas/README.md` · parent [`../README.md`](../README.md) · shared [`../../../contracts/README.md`](../../../contracts/README.md) · shared [`../../../schemas/README.md`](../../../schemas/README.md)  
> **Badges:** ![status](https://img.shields.io/badge/status-experimental-orange) ![doc](https://img.shields.io/badge/doc-draft-blue) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-informational) ![path](https://img.shields.io/badge/path-data%2Fregistry%2Fschemas-blueviolet) ![authority](https://img.shields.io/badge/schema_authority-needs--verification-red) ![shared-home](https://img.shields.io/badge/shared_home-unresolved-yellow)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Definition of done](#definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> Current public `main` shows `data/registry/schemas/` as a scaffolded directory containing `README.md` only. Treat any concrete schema filenames in this subtree as **NEEDS VERIFICATION** until the checked-out branch proves them.

> [!WARNING]
> Current public `main` no longer presents top-level `schemas/` as a flat README-only boundary. It now exposes a live shared-schema scaffold, while adjacent docs still keep shared machine-contract authority visibly unresolved. Read that as shared-context you must inspect before changing this subtree, not as permission to grow registry-local schemas by inertia.

---

## Scope

This directory is for machine-readable schemas that validate registry-local entries and closely related local fragments. It exists to make source and dataset registration reviewable, machine-checkable, and easy to keep adjacent to the registry surface they govern.

This directory is **not** the default home for the shared KFM trust lattice. Release, runtime, correction, and other cross-cutting trust objects should stay in the repo’s authoritative shared schema or contract home.

| Status label | Meaning here |
| --- | --- |
| **CONFIRMED** | The current public tree or adjacent repo docs clearly show it now |
| **INFERRED** | Strong continuity signal from adjacent docs, but not proven in this subtree on current public `main` |
| **PROPOSED** | Recommended local shape that fits current doctrine but is not yet proven in-tree |
| **NEEDS VERIFICATION** | Must be checked against the live branch before treating as implemented |

[Back to top](#data-registry-schemas)

## Repo fit

### Path and role

| Item | Value |
| --- | --- |
| Path | `data/registry/schemas/README.md` |
| Local role | Registry-local schema/index surface |
| Parent | [`../README.md`][registry-readme] |
| Wider data lifecycle | [`../../README.md`][data-readme] |
| Shared contract authority | [`../../../contracts/README.md`][contracts-readme] |
| Shared schema authority | [`../../../schemas/README.md`][schemas-readme] |

### Upstream and downstream links

| Direction | Link | Why it matters |
| --- | --- | --- |
| Upstream | [Registry README][registry-readme] | Owns registry entries that local schemas would validate |
| Upstream | [Data README][data-readme] | Defines the governed truth path and wider `data/` responsibilities |
| Upstream | [Contracts README][contracts-readme] | Still acts as a strong shared-contract routing surface in adjacent docs |
| Upstream | [Schemas README][schemas-readme] | Documents the current shared-schema subtree and warns against silent authority by inertia |
| Constraint | [Policy README][policy-readme] | Carries deny-by-default language, reasons, and obligation expectations |
| Downstream | [Tests README][tests-readme] | Fixtures and proof surfaces should follow schema work |
| Downstream | [Workflows README][workflows-readme] | Enforcement belongs here only when mounted validator and merge/block workflows are actually visible |
| Ownership | [CODEOWNERS][codeowners] | Review routing for `/data/` |

### Shared authority context

| Surface | Current public reading | Why this README cares |
| --- | --- | --- |
| `contracts/` | README-bearing root lane | Shared machine-contract routing still points here in adjacent docs |
| `schemas/` | Parent boundary plus live nested subtree | Confirms shared schema scaffolding is active, not flat README-only |
| `schemas/contracts/` | Shared scaffold lane | Relevant shared context, but not proof that registry-entry validation belongs there |
| `data/registry/schemas/` | README-only local subtree | Local registry-schema authority is still documentary on current public `main` |

### Path resolution rule

If the checked-out branch keeps registry-entry schemas local, this README acts as the narrow home for that family.

If the branch has consolidated those schemas into the shared repo-wide schema or contract surface, this README should remain as a small signpost and should not duplicate that authority.

[Back to top](#data-registry-schemas)

## Inputs

### Accepted inputs

- Registry-entry JSON Schema files that validate dataset, source, or closely related registry records
- Registry-local shared fragments used only by those entry families
- Small compatibility notes for field evolution that are specific to registry-entry validation
- Human guidance that explains how local schemas relate to shared contract authority

### Preferred naming

| Pattern | Use |
| --- | --- |
| `<entry_family>.schema.json` | Canonical local schema filename |
| `<entry_family>.example.<validity>.json` | Review fixtures when examples live beside the schema |
| `fragments/<name>.schema.json` | Registry-local fragments only when reuse is truly local |

### Continuity signals

- `dataset_entry.schema.json` is a strong **INFERRED** candidate name because adjacent KFM documentation and earlier repo-aligned materials reference it, but the current public `main` tree does not prove it exists in this directory now.
- Any additional local family should be added only after checking that it is not already owned by the shared schema or contract surface.
- This README should not be used to silently settle the separate shared-home question now visible between root `contracts/` and the top-level shared `schemas/` subtree.

## Exclusions

| Does not belong here | Where it goes instead | Why |
| --- | --- | --- |
| Shared KFM trust-object schemas such as `DecisionEnvelope`, `EvidenceBundle`, `RuntimeResponseEnvelope`, `CorrectionNotice`, or `ReleaseManifest` | Shared authority in [`../../../contracts/README.md`][contracts-readme] and/or [`../../../schemas/README.md`][schemas-readme] | Prevents a third competing trust-object home |
| Policy bundles, reason registries, obligation registries, or deny-by-default rule files | [`../../../policy/README.md`][policy-readme] | Policy should stay executable and separately reviewable |
| Emitted registry entries, catalogs, proof packs, receipts, or published artifacts | `data/registry/`, `data/catalog/`, `data/receipts/`, `data/proofs/`, or `data/published/` as appropriate | These are outputs or lifecycle artifacts, not local validation contracts |
| STAC, DCAT, or PROV outputs | `data/catalog/` and its child lanes | Discovery and provenance outputs belong in catalog closure |
| Outward API DTOs or OpenAPI source files | Shared API/schema home | External-surface contracts should not be hidden in a local registry-validation subtree |
| Duplicate copies of schemas already treated as authoritative elsewhere | The already-authoritative shared home | Local convenience copies are the fastest path to schema drift |

> [!NOTE]
> The easiest way to create schema drift is to let local convenience copies accumulate here after a shared contract home already exists elsewhere.

[Back to top](#data-registry-schemas)

## Directory tree

### Current public `main` snapshot

```text
data/
└── registry/
    ├── README.md
    └── schemas/
        └── README.md
```

### Narrow local shape if this subtree becomes active

```text
data/registry/schemas/
├── README.md
├── dataset_entry.schema.json          # INFERRED continuity signal; verify on branch
├── fragments/                         # PROPOSED; only for registry-local reuse
│   └── <name>.schema.json
├── examples/                          # PROPOSED; keep valid/invalid examples reviewable
│   ├── valid/
│   └── invalid/
└── migrations/                        # PROPOSED; only when field changes need explicit notes
```

### Reading rule

| Tree view | Status | How to read it |
| --- | --- | --- |
| `README.md` only | **CONFIRMED** | Present on current public `main` |
| `dataset_entry.schema.json` local file | **INFERRED / NEEDS VERIFICATION** | Strong continuity signal, not current public-tree proof |
| `fragments/`, `examples/`, `migrations/` | **PROPOSED** | Helpful local structure only if the branch actually activates this subtree |

## Quickstart

### 1) Inspect the live branch before assuming local schema authority

```bash
find data/registry -maxdepth 3 -print | sort

sed -n '1,220p' data/registry/README.md
sed -n '1,260p' data/registry/schemas/README.md

sed -n '1,260p' contracts/README.md
sed -n '1,260p' schemas/README.md
sed -n '1,260p' schemas/contracts/README.md

sed -n '1,220p' policy/README.md
sed -n '1,220p' tests/README.md
sed -n '1,220p' .github/workflows/README.md
sed -n '1,220p' .github/CODEOWNERS
```

### 2) Re-read the shared authority context before you add local files

```bash
find schemas/contracts -maxdepth 3 -type f | sort
find .github/workflows -maxdepth 1 -type f | sort

# You are checking two different things here:
# - whether a shared machine-contract scaffold is already live elsewhere
# - whether merge/block validator YAML is actually mounted on this branch
```

### 3) Check whether a local registry-entry schema already exists

```bash
find data/registry/schemas -maxdepth 2 -type f | sort

test -f data/registry/schemas/dataset_entry.schema.json \
  && sed -n '1,200p' data/registry/schemas/dataset_entry.schema.json \
  || echo "dataset_entry.schema.json is not proven on this branch"
```

### 4) Make the smallest safe change

```bash
# Good first pass:
# - decide whether local authority is still needed
# - if yes, add one local schema family plus examples
# - if no, keep this README as a narrow index and point to the shared schema home
# - do not let this subtree silently resolve the wider shared schema-home split
```

[Back to top](#data-registry-schemas)

## Usage

### Working rules

1. Decide local versus shared authority first.
2. Keep registry entries one level up in [Registry README][registry-readme]; keep only their validation contracts here.
3. Move schema, examples, tests, and documentation together.
4. Prefer additive evolution and explicit migration notes over silent field breakage.
5. If this directory remains scaffold-only, say so plainly rather than implying executable authority.
6. Do not use this local subtree to silently pick a winner in the separate shared `contracts/` vs `schemas/contracts/` authority question.

### What “good” looks like

- A reviewer can tell in under a minute whether this subtree is active or only an index.
- If active, one registry-entry family has a clearly named schema and review examples.
- If inactive, the README still prevents drift by pointing contributors to the authoritative shared home.
- No file here duplicates cross-cutting families already governed elsewhere.
- Adjacent docs, fixtures, and validator references do not quietly imply contradictory authority homes.

## Diagram

```mermaid
flowchart LR
    Entry["Registry entry<br/>dataset/source record"] --> Local["data/registry/schemas/<br/>registry-local validation"]
    Shared["../../../contracts/ + ../../../schemas/<br/>shared authority context"] -. constrains .-> Local
    Policy["../../../policy/<br/>deny-by-default reasons / obligations"] -. constrains .-> Local
    Tests["../../../tests/<br/>fixtures + contract/policy proof"] -. proves .-> Local
    Workflows["../../../.github/workflows/<br/>merge/block when mounted"] -. enforces .-> Local
    Local --> Review["Registry review / source admission"]
    Review --> Flow["RAW → WORK / QUARANTINE → PROCESSED → CATALOG → PUBLISHED"]
```

## Tables

### Current evidence snapshot

| Claim | Status | Notes |
| --- | --- | --- |
| `data/registry/schemas/` exists on current public `main` | **CONFIRMED** | Directory is visible in the repo tree |
| This subtree currently shows `README.md` only | **CONFIRMED** | No concrete schema files are visible in the current public tree |
| `data/registry/` currently shows `README.md` and `schemas/README.md` only | **CONFIRMED** | Parent registry lane is present, but current public tree still reads as scaffold-first |
| `data/registry/README.md` currently owns the local registry description | **CONFIRMED** | Parent surface exists and is now documented as the source-registration lane |
| Current public `CODEOWNERS` routes `/data/` to `@bartytime4life` | **CONFIRMED** | Public owner routing is visible and matches this README’s owner line |
| `.github/workflows/` currently shows `README.md` only | **CONFIRMED** | Current public listing does not show checked-in workflow YAML files |
| A local `dataset_entry.schema.json` family is still mounted here | **NEEDS VERIFICATION** | Referenced in continuity materials, not proven in the current public tree |

### Shared authority snapshot

| Surface | Status | Current public reading |
| --- | --- | --- |
| `contracts/` root lane | **CONFIRMED** | `README.md` only |
| `schemas/` parent lane | **CONFIRMED** | Parent README plus visible nested subtree |
| `schemas/contracts/` shared scaffold | **CONFIRMED** | Shared machine-file-bearing context lane is visible in the public tree |
| Canonical shared machine-contract home is fully settled | **NEEDS VERIFICATION** | Adjacent docs still keep the shared-home decision explicit and unresolved |
| `data/registry/schemas/` local lane is active beyond `README.md` | **NEEDS VERIFICATION** | Public `main` does not prove any local schema family |

### Placement matrix

| Schema kind | Best home | Why |
| --- | --- | --- |
| Registry-entry validation | `data/registry/schemas/` only when proven local | Keeps entry rules close to the registry surface |
| Shared trust-bearing object families | Shared authority in `contracts/` and/or top-level `schemas/` | Prevents parallel schema universes |
| Policy vocab / deny-by-default rules | `policy/` | Policy should stay executable and separately reviewable |
| API/public payload shapes | Shared API/schema home | Keeps external surface contracts centralized |
| Emitted metadata artifacts | `data/catalog/` or generated outputs | These are outputs, not local entry-validation schemas |
| Shared-home arbitration between `contracts/` and `schemas/contracts/` | Shared boundary docs, not this local subtree | This README should acknowledge the split, not settle it by accident |

### Candidate local wave if authority stays here

| Candidate | Status | Purpose | Notes |
| --- | --- | --- | --- |
| `dataset_entry.schema.json` | **INFERRED** | Validate registry-entry shape | Verify on branch before treating as active |
| `fragments/<name>.schema.json` | **PROPOSED** | Local enums or reusable local fragments | Only if reuse is truly local |
| `examples/valid/*` | **PROPOSED** | Positive review fixtures | Can live here or point to the testing surface |
| `examples/invalid/*` | **PROPOSED** | Negative review fixtures | Must fail deterministically and legibly |

[Back to top](#data-registry-schemas)

## Definition of done

- [ ] Verify whether this subtree is still an active schema home on the checked-out branch
- [ ] If active, add the first confirmed local schema family with at least one valid and one invalid example
- [ ] If inactive, keep this README narrow and link contributors to the shared authority surface
- [ ] Confirm `doc_id` and `policy_label` in the meta block before merge
- [ ] Ensure parent and sibling READMEs do not contradict this placement rule
- [ ] Ensure this README does not silently settle the wider shared `contracts/` vs `schemas/contracts/` authority split
- [ ] Do not claim merge-blocking validation until a real workflow YAML and validator path are visible
- [ ] Keep local names, examples, tests, and migration notes in sync in the same PR

[Back to top](#data-registry-schemas)

## FAQ

### Why not put every KFM schema under `data/registry/schemas/`?

Because the repo already has shared contract/schema guidance at higher levels. Putting every family here would blur local registry-entry validation with the repo-wide trust lattice.

### Does current public `main` prove `dataset_entry.schema.json` lives here?

No. It is a continuity signal, not current-tree proof.

### Does the live `schemas/contracts/` scaffold mean registry-entry schemas belong there instead?

Not by itself. That shared scaffold is relevant context, but adjacent public docs still treat the shared machine-contract home as unresolved. This local README should acknowledge that split and avoid hardening either side by accident.

### When should a schema live here instead of in the shared schema or contract home?

Only when it validates registry-local entry shapes and does not create duplicate authority for a shared KFM object family.

### Why are `doc_id` and `policy_label` still placeholders?

Because the current public repo evidence confirms the file, owner routing, and neighboring lanes, but it does not surface a verified document UUID or an explicit policy label for this README. Those values should be resolved on the working branch before merge.

### Where should fixtures live?

Prefer the repo’s testing/proof surfaces when they already exist. If a branch deliberately keeps tiny local examples beside a schema for reviewer clarity, make that choice explicit and non-authoritative.

## Appendix

<details>
<summary><strong>Verification backlog</strong></summary>

| Question | Why it matters | Current posture |
| --- | --- | --- |
| Is `data/registry/schemas/` meant to stay active on the working branch? | Determines whether this README is a local home or just an index | **NEEDS VERIFICATION** |
| Does `dataset_entry.schema.json` exist here on the working branch? | Confirms whether the older registry-entry pattern still holds | **NEEDS VERIFICATION** |
| Where do valid/invalid fixtures live now? | Needed to avoid splitting examples across competing homes | **NEEDS VERIFICATION** |
| Is there a mounted validator command for registry-entry schemas? | Needed before calling anything enforced | **NEEDS VERIFICATION** |
| Do actual workflow YAMLs exist for this surface on the working branch? | Needed before claiming CI gate behavior | **NEEDS VERIFICATION** |
| Has the working branch explicitly resolved the shared `contracts/` vs `schemas/contracts/` machine-contract home? | Prevents this local doc from reinforcing the wrong shared-home assumption | **NEEDS VERIFICATION** |

</details>

<details>
<summary><strong>Continuity note</strong></summary>

Older repo-aligned materials and KFM compendium passages referenced a registry-entry schema such as `dataset_entry.schema.json`. That is useful as a continuity hint, but this README intentionally does not promote it to **CONFIRMED** unless the checked-out branch proves the file is present and still authoritative.

</details>

<details>
<summary><strong>Shared-authority note</strong></summary>

Current public `main` now exposes more shared-schema structure than an earlier `README.md`-only reading suggested. That matters here only as context. It does **not** automatically relocate registry-local entry validation into the shared schema lane, and it does **not** authorize this subtree to grow by inertia. The safe move is still: inspect the working branch, decide one authority home per family, then update adjacent docs, fixtures, and validator references together.

</details>

---

[registry-readme]: ../README.md
[data-readme]: ../../README.md
[contracts-readme]: ../../../contracts/README.md
[schemas-readme]: ../../../schemas/README.md
[schemas-contracts-readme]: ../../../schemas/contracts/README.md
[policy-readme]: ../../../policy/README.md
[tests-readme]: ../../../tests/README.md
[workflows-readme]: ../../../.github/workflows/README.md
[codeowners]: ../../../.github/CODEOWNERS
