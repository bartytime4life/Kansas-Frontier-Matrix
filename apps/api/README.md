<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: apps/api
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related: [../README.md, ../governed-api/README.md, ./src/README.md, ./src/api/README.md, ./src/api/routes/README.md, ./src/api/middleware/README.md, ./tests/README.md, ../../contracts/README.md, ../../policy/README.md, ../../data/catalog/stac/README.md, ../../data/registry/README.md]
tags: [kfm, apps, api, runtime, governed-api]
notes: [Populate doc_id and dates after mounted-branch verification; current public-main apps/api subtree is documentation-heavy rather than placeholder-only; final naming authority between apps/api and apps/governed-api still needs verification.]
[/KFM_META_BLOCK_V2] -->

# apps/api

_App-root README for the KFM API subtree: boundary, current tree, and maintenance routing for the `apps/api/` lane._

> **Status:** experimental  
> **Doc state:** draft  
> **Owners:** `@bartytime4life`  
> **Path:** `apps/api/README.md`  
> ![status](https://img.shields.io/badge/status-experimental-orange?style=flat-square) ![doc](https://img.shields.io/badge/doc-draft-blue?style=flat-square) ![surface](https://img.shields.io/badge/surface-apps%2Fapi-1f6feb?style=flat-square) ![public main](https://img.shields.io/badge/public__main-docs--first-lightgrey?style=flat-square) ![trust](https://img.shields.io/badge/trust-governed%20API%20required-0a7d5a?style=flat-square) ![posture](https://img.shields.io/badge/posture-verification__first-57606a?style=flat-square)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current public evidence snapshot](#current-public-evidence-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** `apps/api/README.md` → parent [`../README.md`](../README.md) · parallel boundary [`../governed-api/README.md`](../governed-api/README.md) · source subtree [`./src/README.md`](./src/README.md) · deeper API lane [`./src/api/README.md`](./src/api/README.md) · route families [`./src/api/routes/README.md`](./src/api/routes/README.md) · middleware seam [`./src/api/middleware/README.md`](./src/api/middleware/README.md) · tests [`./tests/README.md`](./tests/README.md)

> [!IMPORTANT]
> Keep this README **app-root and boundary-aware**.
>
> It should explain what `apps/api/` is, what the subtree currently contains, what this lane is expected to own, and where deeper detail belongs. It should **not** silently absorb the sibling trust-boundary role of [`../governed-api/README.md`](../governed-api/README.md), and it should **not** duplicate source-file, route-handler, middleware, or test-suite detail that belongs in downstream app-local docs.

> [!WARNING]
> Current public `main` no longer shows `apps/api/` as a placeholder-only subtree.
>
> What public `main` now proves is a **README-defined API lane** with app-root, source-boundary, deeper API, route-family, middleware, and app-local test docs.
>
> What it still does **not** prove from this subtree alone is concrete handler code, package-manager truth, ports, endpoint inventory, executable test depth, or workflow guarantees. Treat those as **NEEDS VERIFICATION** until the target branch proves them.

## Scope

`apps/api/` is the app-root documentation surface for the API-facing lane currently living under `apps/`.

As currently exposed on public `main`, this lane is **documentation-deepened but still implementation-light**. In repo terms, this README should own four things:

1. the subtree’s identity and routing
2. the current verified file inventory
3. app-root maintenance rules
4. the handoff into deeper API, contract, policy, and test surfaces

It should **not** try to become the entire authority for whole-system trust-membrane doctrine, route-by-route implementation detail, or the final live runtime story.

### Truth labels used here

| Label | Meaning in this README |
| --- | --- |
| **CONFIRMED** | Directly supported by the current public repo tree or stable KFM doctrine carried by the attached corpus |
| **INFERRED** | Small structural completion that fits adjacent repo docs and KFM doctrine, but is not freshly proven as current branch reality |
| **PROPOSED** | Recommended next shape or maintenance rule that fits KFM and improves reviewability |
| **NEEDS VERIFICATION** | A path, owner split, command, or implementation claim that should be checked on the target branch before merge |
| **UNKNOWN** | Not supported strongly enough in the current session to present as current repo fact |

### Stable doctrine carried into this subtree

| Rule | Practical consequence for `apps/api/` |
| --- | --- |
| Trust membrane | Client-facing surfaces should cross governed API boundaries rather than reaching into canonical stores or unpublished artifacts directly. |
| Truth path | Runtime-facing docs should assume release-linked, promoted scope rather than ad hoc source access. |
| Evidence resolution | Consequential API paths should remain one hop from `EvidenceRef → EvidenceBundle` resolution. |
| Fail-closed posture | Rights, policy, or verification uncertainty should not be documented as successful outward behavior. |
| Bounded assistance | Any AI-facing runtime surface belongs downstream of evidence, policy, and release state, not beside or above them. |

[Back to top](#appsapi)

## Repo fit

`apps/api/README.md` sits inside the runtime-facing `apps/` family and should stay explicit about both its upstream doctrine and its downstream local surfaces.

| Path | Role | Relationship |
| --- | --- | --- |
| [`../README.md`](../README.md) | app-family boundary README | parent runtime surface hub |
| [`../governed-api/README.md`](../governed-api/README.md) | trust-boundary / membrane README | parallel sibling; final naming authority still needs verification |
| [`./src/README.md`](./src/README.md) | source subtree README | downstream local source lane; public `main` now shows a substantive boundary doc |
| [`./src/api/README.md`](./src/api/README.md) | deeper API lane | downstream HTTP / controller / adapter doc surface; public `main` now shows route and middleware child seams beneath it |
| [`./src/api/routes/README.md`](./src/api/routes/README.md) | route-family README | downstream handler-family navigation and request/response rule surface |
| [`./src/api/middleware/README.md`](./src/api/middleware/README.md) | middleware README | downstream cross-cutting request/response seam |
| [`./tests/README.md`](./tests/README.md) | app-local test lane | downstream verification surface; boundary-setting rather than suite-proving |
| [`../../contracts/README.md`](../../contracts/README.md) | shared contract authority | upstream machine-contract neighbor |
| [`../../policy/README.md`](../../policy/README.md) | policy authority | upstream rights / sensitivity / obligation authority |
| [`../../data/catalog/stac/README.md`](../../data/catalog/stac/README.md) | discovery-facing catalog lane | downstream discovery consumer of API-shaped release scope |
| [`../../data/registry/README.md`](../../data/registry/README.md) | onboarding / identity seam | adjacent upstream source-governance lane |
| [`../../tests/README.md`](../../tests/README.md) | repo-wide verification lane | upstream shared test surface |

### Boundary rule for this file

This README should stay focused on **app-root ownership**:

- what `apps/api/` is for
- how it relates to `apps/governed-api/`
- how to navigate the local subtree
- what can be stated today without overclaiming

It should not become a hidden second home for:

- full route catalogs
- DTO or handler inventories
- full policy semantics
- endpoint-by-endpoint implementation notes
- middleware implementation notes better owned by `./src/api/middleware/README.md`
- branch-local runtime claims that have not been directly checked

[Back to top](#appsapi)

## Accepted inputs

Place the following here when they are primarily **app-root concerns** for `apps/api/`:

- current verified subtree inventory and path changes
- app-root ownership notes and local conventions
- verified local bootstrap, smoke-test, and inspection commands
- links to deeper API, route, middleware, contract, policy, and test surfaces
- reconciliation notes for the `apps/api` ↔ `apps/governed-api` split
- short maintenance rules that help reviewers know where deeper material belongs
- updates when the subtree stops being README-first and gains branch-proven implementation files

## Exclusions

Do **not** place the following here:

- route-by-route endpoint details or handler notes → [`./src/api/routes/README.md`](./src/api/routes/README.md)
- middleware-specific cross-cutting behavior inventories → [`./src/api/middleware/README.md`](./src/api/middleware/README.md)
- source-tree implementation walkthroughs → [`./src/README.md`](./src/README.md)
- app-local test matrix details → [`./tests/README.md`](./tests/README.md)
- whole-of-system trust-membrane doctrine or public/steward shell law → [`../governed-api/README.md`](../governed-api/README.md) and [`../README.md`](../README.md)
- source onboarding or dataset identity rules → [`../../data/registry/README.md`](../../data/registry/README.md)
- STAC / DCAT / PROV field law → catalog and standards surfaces under `../../data/` and `../../docs/`
- speculative claims about package manager, ports, local run commands, workflow gates, or enforcement depth that are not directly verified on the target branch
- copied contract prose that should stay authoritative in `../../contracts/` or `../../policy/`

## Current public evidence snapshot

This section intentionally describes what the current public tree proves **today**, without inflating it into live runtime certainty.

| Signal | Status | Current reading |
| --- | --- | --- |
| `apps/api/README.md` | **CONFIRMED** | Substantive app-root README exists on current public `main` |
| `apps/api/` tree | **CONFIRMED** | Contains `src/`, `tests/`, and `README.md` |
| `apps/api/src/README.md` | **CONFIRMED** | Substantive source-boundary README exists on current public `main` |
| `apps/api/src/api/README.md` | **CONFIRMED** | Substantive deeper API README exists on current public `main` |
| `apps/api/src/api/routes/README.md` | **CONFIRMED** | Route-family README exists on current public `main` |
| `apps/api/src/api/middleware/README.md` | **CONFIRMED** | Middleware README exists on current public `main` |
| `apps/api/tests/README.md` | **CONFIRMED** | Substantive app-local test README exists on current public `main` |
| currently visible file inventory under `apps/api/` | **CONFIRMED** | Public-main inspection currently shows a README-first subtree rather than branch-proven handler or test files |
| `apps/README.md` | **CONFIRMED** | App-family boundary README keeps `api/`, `cli/`, `explorer-web/`, `governed-api/`, `review-console/`, `ui/`, and `workers/` visible |
| `apps/governed-api/README.md` | **CONFIRMED** | Parallel boundary README exists and still keeps canonical ownership between `apps/api` and `apps/governed-api` explicit |
| owner routing | **CONFIRMED** | Broad public `.github/CODEOWNERS` fallback routes `/apps/` to `@bartytime4life` |
| final naming authority between `apps/api` and `apps/governed-api` | **NEEDS VERIFICATION** | Keep both surfaces visible until the target branch resolves canonical ownership |
| local bootstrap commands, package manager, ports, endpoint inventory, app-local runner wiring, and API implementation depth | **UNKNOWN** | Not proven from the current public subtree inspection used here |

> [!NOTE]
> The biggest change from older snapshot language is simple: public `main` now proves **more documentation depth**, not **more runtime depth**.
>
> This README should preserve that distinction instead of collapsing it into confident API maturity prose.

## Directory tree

Current public-main snapshot verified in this session:

```text
apps/api/
├── README.md
├── src/
│   ├── README.md
│   └── api/
│       ├── README.md
│       ├── middleware/
│       │   └── README.md
│       └── routes/
│           └── README.md
└── tests/
    └── README.md
```

What this tree means right now:

- the subtree is no longer just `README.md + empty children`
- the subtree is still **README-defined** on current public `main`
- deeper implementation files under `routes/`, `middleware/`, or `tests/` are still **NEEDS VERIFICATION** until the target branch proves them

Suggested reading order inside the subtree:

1. this file — app-root ownership and routing
2. `../governed-api/README.md` — trust-boundary doctrine and surface classes
3. `./src/README.md` — source subtree boundary
4. `./src/api/README.md` — deeper API lane detail
5. `./src/api/routes/README.md` — route-family rules and route-family taxonomy
6. `./src/api/middleware/README.md` — middleware seam and cross-cutting request/response rules
7. `./tests/README.md` — app-local verification surface

[Back to top](#appsapi)

## Quickstart

### 1) Inspect what is actually present

```bash
find apps/api -maxdepth 5 -type f | sort
```

### 2) Separate doc proof from implementation proof

```bash
find apps/api -maxdepth 5 -type f ! -name 'README.md' | sort
```

If this second command returns nothing on the branch you are documenting, treat the lane as **docs-first**, not implementation-proven.

### 3) Read adjacent authority docs before editing this lane

```bash
sed -n '1,260p' apps/README.md
sed -n '1,260p' apps/governed-api/README.md
sed -n '1,260p' apps/api/README.md
sed -n '1,260p' apps/api/src/README.md
sed -n '1,260p' apps/api/src/api/README.md
sed -n '1,260p' apps/api/src/api/routes/README.md
sed -n '1,220p' apps/api/src/api/middleware/README.md
sed -n '1,220p' apps/api/tests/README.md
```

### 4) Add verified run/test commands only after they work on the target branch

```bash
# TODO: replace with branch-verified commands only.
# Examples to add only after proof:
# - package manager bootstrap
# - local API start command
# - smoke-test or health-check command
# - app-local test command
# - required env file or secrets reference
```

> [!IMPORTANT]
> Do not guess the package manager, server command, port, or env shape here.
> This app-root README should become the place a maintainer starts for local use, but only after the commands have been checked against the actual branch.

## Usage

### Update this README when

- the `apps/api/` subtree inventory changes
- the ownership split between `apps/api` and `apps/governed-api` is clarified
- non-README files appear or disappear under `apps/api/`
- local bootstrap or smoke-test commands are verified
- downstream README targets are renamed, added, or removed
- app-root conventions change and reviewers need a stable routing surface

### Keep the doc split clean

| Change type | Update here? | Also update |
| --- | --- | --- |
| subtree inventory changed | Yes | [`../README.md`](../README.md) if the app-family inventory changes too |
| authoritative naming between `apps/api` and `apps/governed-api` changed | Yes | [`../governed-api/README.md`](../governed-api/README.md) and [`../README.md`](../README.md) |
| source subtree organization changed | Summary only | [`./src/README.md`](./src/README.md) |
| deeper API boundary changed | Summary only | [`./src/api/README.md`](./src/api/README.md) |
| route-family documentation changed | Summary only | [`./src/api/routes/README.md`](./src/api/routes/README.md) |
| middleware seam changed | Summary only | [`./src/api/middleware/README.md`](./src/api/middleware/README.md) |
| app-local tests changed | Summary only | [`./tests/README.md`](./tests/README.md) |
| contract or policy authority moved | Yes | [`../../contracts/README.md`](../../contracts/README.md), [`../../policy/README.md`](../../policy/README.md) |

### Use this README as the handoff point

A good maintainer experience for this lane should look like this:

- start here to learn what the subtree is supposed to own
- confirm what the public tree actually contains
- branch outward into boundary, source, API, route, middleware, or test docs as needed
- avoid mistaking documentation depth for runnable API maturity

## Diagram

```mermaid
flowchart TD
    A[apps/README.md<br/>runtime surface hub] --> B[apps/api/README.md<br/>app-root API lane]
    A --> C[apps/governed-api/README.md<br/>boundary-first trust doc]

    B -. naming / boundary authority<br/>needs verification .-> C

    B --> D[apps/api/src/README.md<br/>source subtree]
    D --> E[apps/api/src/api/README.md<br/>deeper API lane]
    E --> F[apps/api/src/api/routes/README.md<br/>route families]
    E --> G[apps/api/src/api/middleware/README.md<br/>middleware seam]
    B --> H[apps/api/tests/README.md<br/>app-local tests]

    C --> I[contracts/ + policy/ + schemas/]
    B --> J[data/catalog/* + evidence-facing consumers]
```

## Tables

### Responsibility split

| Surface | What it should own | What it should not quietly own |
| --- | --- | --- |
| `apps/api/README.md` | app-root identity, subtree routing, verified inventory, bootstrap handoff | final route catalog, handler detail, whole-system doctrine |
| `apps/governed-api/README.md` | trust-boundary law, governed request classes, membrane rules, edge-facing API posture | app-root inventory churn, source-tree walkthroughs, route-handler duplication |
| `apps/api/src/README.md` | source subtree structure and local implementation entrypoints | whole-boundary doctrine or sibling app-family ownership |
| `apps/api/src/api/README.md` | deeper API-lane navigation, route-family framing, middleware seams, response-shaping expectations | app-root tree inventory or whole-app ownership |
| `apps/api/src/api/routes/README.md` | route families, request parsing/validation, policy invocation, response-return rules | business logic, direct storage access, policy authoring |
| `apps/api/src/api/middleware/README.md` | cross-cutting request/response seams, correlation, shared response cues | hidden business logic, route-local hacks, or silent trust bypasses |
| `apps/api/tests/README.md` | app-local verification organization and test surfaces | repo-wide testing doctrine or shared policy law |

### Doctrine-backed route families

These are the route families KFM doctrine expects an API boundary to handle. The table below is included to keep this app-root README aligned with project law **without** claiming that the current subtree already proves every endpoint.

| Route family | Why `apps/api/` should care | Current implementation claim |
| --- | --- | --- |
| Catalog / discovery | dataset, version, and outward metadata reads shape what the app-root API lane eventually exposes | **Doctrine-backed / implementation UNKNOWN** |
| Feature / subject read | authoritative released reads are part of the public/steward runtime boundary | **Doctrine-backed / implementation UNKNOWN** |
| Map / tile / portrayal | map-facing delivery belongs downstream of release scope and policy | **Doctrine-backed / implementation UNKNOWN** |
| Evidence resolution | `EvidenceRef → EvidenceBundle` is load-bearing for Evidence Drawer and related trust surfaces | **Doctrine-backed / implementation UNKNOWN** |
| Story / dossier / compare | API-facing narrative and comparison surfaces stay anchored to the same geography/time shell | **Doctrine-backed / implementation UNKNOWN** |
| Export / report | public-safe outward artifacts inherit release, policy, and correction state | **Doctrine-backed / implementation UNKNOWN** |
| Focus / governed assistance | bounded runtime assistance should remain cite-or-abstain and evidence-shaped | **Doctrine-backed / implementation UNKNOWN** |
| Review / stewardship | internal-only moderation, rollback, rights, and denial flows are part of the same API world, but not public by default | **Doctrine-backed / implementation UNKNOWN** |
| Ops / status | health and audit-facing status may exist, but must not become a second truth surface | **Doctrine-backed / implementation UNKNOWN** |

[Back to top](#appsapi)

## Task list -- definition of done

A strong, review-ready `apps/api/README.md` is done when all of the following are true:

- [ ] top-level placeholders in the meta block are replaced with real values after mounted-branch verification
- [ ] the current `apps/api/` tree snapshot is accurate, including `routes/` and `middleware/` doc seams
- [ ] the docs-first vs. code-depth distinction is explicit and truthful
- [ ] the relationship between `apps/api` and `apps/governed-api` is explicitly settled or clearly flagged
- [ ] local bootstrap and smoke-test commands have been verified and added
- [ ] route- and middleware-level detail is routed to `./src/api/README.md` and its child docs rather than duplicated here
- [ ] test-surface detail is routed to `./tests/README.md` rather than duplicated here
- [ ] any endpoint or runtime claims are anchored to visible code, contracts, or tests
- [ ] relative links still resolve after every subtree change

## FAQ

### Why keep both `apps/api` and `apps/governed-api` visible?

Because current public `main` still exposes **both** surfaces. Until the target branch resolves which path owns which layer of API documentation, this README should keep the split visible instead of flattening it into confident prose.

### Does this README prove a runnable API today?

No. Current public `main` proves a documentation-deepened subtree, not the final runtime command set, route inventory, enforcement depth, handler code, or test matrix.

### Where should endpoint detail live?

In the deeper API lane under [`./src/api/README.md`](./src/api/README.md), with route-family and middleware specifics flowing into [`./src/api/routes/README.md`](./src/api/routes/README.md) and [`./src/api/middleware/README.md`](./src/api/middleware/README.md), plus authoritative contract surfaces under `../../contracts/` and related schema/policy lanes once those are verified for the target branch.

### Why is this file doctrine-aware even though the subtree is still docs-first?

Because KFM treats runtime boundaries as part of the trust model. Even when implementation depth is not yet proven, boundary docs should still preserve the trust membrane, truth-path discipline, and evidence-first posture that later code must satisfy.

## Appendix

<details>
<summary><strong>Open verification backlog</strong></summary>

### Still needs direct branch proof

- final naming authority between `apps/api` and `apps/governed-api`
- actual non-README implementation files under `apps/api/src/api/`
- actual executable tests under `apps/api/tests/`
- package manager and bootstrap workflow
- local port, auth, and health-check behavior
- concrete OpenAPI / schema / policy entrypoints used by this subtree
- workflow YAML and merge-blocking checks that apply specifically to this lane

### Safe rule while those remain open

Keep path facts explicit, keep doctrine visible, and downgrade anything else to **NEEDS VERIFICATION** or **UNKNOWN** instead of smoothing the gap away.

</details>

<details>
<summary><strong>Current public-main tree snapshot to refresh when the subtree changes</strong></summary>

```text
apps/api/
├── README.md
├── src/
│   ├── README.md
│   └── api/
│       ├── README.md
│       ├── middleware/
│       │   └── README.md
│       └── routes/
│           └── README.md
└── tests/
    └── README.md
```

Refresh this snapshot whenever files are added, renamed, or moved under `apps/api/`.

</details>

<details>
<summary><strong>Current public-main interpretation rule</strong></summary>

Public `main` now proves more README depth than older placeholder snapshots did. That is real progress in documentation shape, but it is still not proof of handler files, middleware modules, executable tests, or runtime boot paths under this subtree.

Treat that distinction as load-bearing whenever this README is edited.

</details>

[Back to top](#appsapi)
