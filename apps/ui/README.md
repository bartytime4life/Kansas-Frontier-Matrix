<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_UUID>
title: KFM UI Path Boundary
type: standard
version: v1
status: review
owners: @bartytime4life
created: <NEEDS_VERIFICATION_DATE>
updated: 2026-04-18
policy_label: public
related: [../README.md, ../explorer-web/README.md, ../review-console/README.md, ../governed-api/README.md, ../api/README.md, ../api/src/README.md, ../api/src/api/README.md, ../api/tests/README.md, ../../README.md, ../../web/README.md, ../../ui/README.md, ../../contracts/README.md, ../../policy/README.md, ../../tests/README.md, ../../.github/CODEOWNERS, ../../.github/PULL_REQUEST_TEMPLATE.md]
tags: [kfm, apps, ui]
notes: [Current public main lists `apps/ui/` in `apps/README.md` and exposes `apps/ui/` as README-only; `web/README.md` and root `ui/README.md` are now substantive UI guidance surfaces; runtime ownership between `apps/ui/`, `apps/explorer-web/`, `web/`, and root `ui/` still needs branch-level reconciliation before this path is treated as a settled runtime root. Created date and UUID still need verification.]
[/KFM_META_BLOCK_V2] -->

# KFM UI Path Boundary

Docs-first boundary README for `apps/ui/` while runtime ownership between the placeholder app UI path, the explorer shell, `web/`, and the root `ui/` guidance lane is reconciled.

> **Status:** `experimental`  
> **Document status:** `review`  
> **Owners:** `@bartytime4life`  
> **Path:** `apps/ui/README.md`  
> **Repo fit:** directory README for the current `apps/ui/` path inside `apps/`; today it is still a routing and truth-boundary document before it is a runtime inventory.
>
> ![status: experimental](https://img.shields.io/badge/status-experimental-orange?style=flat-square)
> ![doc: review](https://img.shields.io/badge/doc-review-blue?style=flat-square)
> ![owners: @bartytime4life](https://img.shields.io/badge/owners-%40bartytime4life-blue?style=flat-square)
> ![public main: README only](https://img.shields.io/badge/public--main-README--only-lightgrey?style=flat-square)
> ![path: apps/ui](https://img.shields.io/badge/path-apps%2Fui-6f42c1?style=flat-square)
> ![shell law: map-first](https://img.shields.io/badge/shell-map--first%20%2B%20time--aware-0a7d5a?style=flat-square)
>
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> Current public `main` proves `apps/ui/` exists and is still **`README.md`-only**. It also proves nearby UI-boundary pressure: `apps/README.md` lists `ui/` as a placeholder child path, `apps/explorer-web/README.md` is the stronger app-local shell-boundary sibling, `web/README.md` is a stronger UI-root guidance surface, and root `ui/README.md` is another UI guidance lane that now needs reconciliation if touched.

> [!CAUTION]
> This file should not become a second, conflicting shell manual. Where branch reality still routes concrete shell behavior through `apps/explorer-web/`, `web/`, or root `ui/`, this README should stay narrow, honest, and explicit about that boundary.

---

## Scope

`apps/ui/` is a repo-visible UI path with a currently minimal public-main footprint. This README therefore does two jobs:

1. record the **CONFIRMED** current boundary of the path as it exists today
2. state what belongs here **only if** a working branch turns `apps/ui/` into a real runtime surface

KFM’s broader UI law still applies here:

- the shell is map-first and time-aware
- the interface is part of the evidence chain, not decorative chrome
- browser-facing surfaces consume governed APIs rather than canonical/internal stores
- Focus behavior remains bounded and evidence-linked
- review is a shell variation, not a detached admin universe
- 2D is the default operating surface; 3D is conditional and must inherit the same trust objects

In practice, `apps/ui/` should own composition and rendering behavior only when that ownership is directly proven by the branch. It should never silently absorb truth authority, policy authority, release authority, or evidence-resolution authority.

[Back to top](#kfm-ui-path-boundary)

---

## Repo fit

### Current public snapshot

| Item | Current reading |
|---|---|
| `apps/ui/` path | **CONFIRMED** repo-visible path |
| Current inventory under `apps/ui/` | **CONFIRMED** `README.md` only |
| Parent `apps/` tree | **CONFIRMED** includes `ui/` as a directory |
| Parent support path | **CONFIRMED** `apps/.codex/` exists as support/audit material, not as an app runtime family |
| Parent app-family summary | **CONFIRMED** lists `ui/` as a placeholder child path in `apps/README.md` |
| Strongest nearby app-local shell-boundary README | **CONFIRMED** `../explorer-web/README.md` |
| Review-shell sibling | **CONFIRMED** `../review-console/README.md` |
| Governed API sibling | **CONFIRMED** `../governed-api/README.md` |
| Nearby app-local API lane roots | **CONFIRMED** `../api/README.md`, `../api/src/README.md`, `../api/src/api/README.md`, and `../api/tests/README.md` |
| Parallel `web/` lane | **CONFIRMED** repo-visible and doctrine-heavy, but not proof of singular runtime-root ownership |
| Parallel root `ui/` lane | **CONFIRMED** repo-visible UI guidance lane with child paths; relationship to `apps/ui/` remains **NEEDS VERIFICATION** |
| Local manifests, routes, runtime code, tests, fixtures under `apps/ui/` | **UNKNOWN** |

### Working interpretation

Until branch-local evidence proves otherwise, the safest repo-native reading is:

- `apps/ui/` is presently a **routing / reconciliation boundary** and a path-local placeholder
- `../explorer-web/README.md` is the stronger current sibling for concrete app-local shell-boundary guidance
- `../../web/README.md` is a stronger UI-root guidance surface, but not proof that `web/` is the sole runtime root
- `../../ui/README.md` is another UI guidance lane that should not be ignored if ownership is reconciled
- `../review-console/README.md` remains the reviewer/steward shell variant
- `../governed-api/README.md`, `../api/README.md`, and `../api/src/api/README.md` remain the right place for API and route-boundary claims

### Upstream and downstream links

| Relationship | Path | Why it matters |
|---|---|---|
| Parent app subtree | [`../README.md`](../README.md) | runtime-facing app boundary and sibling map |
| Root repo posture | [`../../README.md`](../../README.md) | repo-wide identity, truth posture, and lane structure |
| Closest app-local shell sibling | [`../explorer-web/README.md`](../explorer-web/README.md) | strongest current public shell-boundary README under `apps/` |
| Review-shell sibling | [`../review-console/README.md`](../review-console/README.md) | review, moderation, and steward-facing shell variation |
| Governed API boundary | [`../governed-api/README.md`](../governed-api/README.md) | client-facing API trust membrane |
| App-local API lane root | [`../api/README.md`](../api/README.md) | app-root routing for the `apps/api/` subtree |
| App-local source subtree | [`../api/src/README.md`](../api/src/README.md) | source-subtree boundary under `apps/api/` |
| Deeper API surface | [`../api/src/api/README.md`](../api/src/api/README.md) | route and surface-contract context |
| App-local API tests | [`../api/tests/README.md`](../api/tests/README.md) | nearby verification surface inside `apps/api/` |
| Shared contracts | [`../../contracts/README.md`](../../contracts/README.md) | contract families and schema-facing expectations |
| Shared policy lane | [`../../policy/README.md`](../../policy/README.md) | policy bundles, decision logic, and gates |
| Shared verification lane | [`../../tests/README.md`](../../tests/README.md) | verification surface and test organization |
| Parallel UI-root guidance lane | [`../../web/README.md`](../../web/README.md) | browser-boundary and UI-root guidance surface |
| Parallel root UI guidance lane | [`../../ui/README.md`](../../ui/README.md) | additional root-level UI guidance surface needing reconciliation if touched |
| Ownership marker | [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | current public ownership signal |
| Review expectations | [`../../.github/PULL_REQUEST_TEMPLATE.md`](../../.github/PULL_REQUEST_TEMPLATE.md) | evidence, docs, risk, and verification expectations |

[Back to top](#kfm-ui-path-boundary)

---

## Accepted inputs

This file accepts material specifically about the `apps/ui/` path and its verified relationship to the rest of the repo.

| Accept here | Notes |
|---|---|
| app-local UI boundary notes | what this path owns, and what it explicitly does not own |
| shell-composition notes tied to this path | only when the branch actually places that shell code here |
| trust-visible rendering rules | freshness, policy, evidence, review, negative-state, and correction cues |
| client service-layer notes | governed API mediation, request envelopes, response handling |
| path-local contract adapters | view-state payloads, Focus response handling, Evidence Drawer payload usage |
| verified directory inventory | actual subtree files, entrypoints, tests, fixtures, configs |
| branch-local quickstart commands | only after toolchain and runtime files are directly present |
| README reconciliation notes | when ownership between `apps/ui/`, `apps/explorer-web/`, `web/`, and root `ui/` changes |

## Exclusions

Keep the path narrow. The following do **not** belong here by default.

| Do not place here | Put it here instead |
|---|---|
| canonical truth mutation rules | [`../../README.md`](../../README.md) and doctrinal architecture docs |
| policy bundle authoring or OPA rule design | [`../../policy/README.md`](../../policy/README.md) |
| shared contract family definitions | [`../../contracts/README.md`](../../contracts/README.md) |
| route-by-route API claims | [`../api/src/api/README.md`](../api/src/api/README.md) |
| source onboarding, ingestion, promotion, receipts | ingest / catalog / runbook lanes, not this UI boundary |
| detached assistant UX that bypasses evidence | do not add; Focus remains governed and bounded |
| duplicate shell doctrine already owned by sibling surface docs | route to [`../explorer-web/README.md`](../explorer-web/README.md), [`../../web/README.md`](../../web/README.md), or [`../../ui/README.md`](../../ui/README.md) unless ownership moves |
| speculative framework or startup instructions | wait until the branch proves manifests and entrypoints |
| direct browser calls to canonical/internal stores or model runtimes | always route through governed API boundaries |
| stale carry-forward claims that `../../web/README.md` is still placeholder-only | remove them; public docs now treat it as a stronger UI-root guidance surface |
| treating root `ui/` and `apps/ui/` as the same owner without proof | reconcile explicitly before merging ownership-sensitive claims |

[Back to top](#kfm-ui-path-boundary)

---

## Directory tree

### Current public-main app snapshot

```text
apps/
├── README.md
├── .codex/                         # support/audit path, not an app runtime family
│   ├── markdown-path-audit.json
│   ├── markdown-path-audit.md
│   └── markdown-path-report.md
├── api/
│   ├── README.md
│   ├── src/
│   │   ├── README.md
│   │   └── api/
│   │       └── README.md
│   └── tests/
│       └── README.md
├── cli/
│   └── README.md
├── explorer-web/
│   └── README.md
├── governed-api/
│   └── README.md
├── review-console/
│   └── README.md
├── ui/
│   └── README.md
└── workers/
    └── README.md
```

### Proposed local subtree if this path becomes real

The shape below is **PROPOSED / NEEDS VERIFICATION**. It is a guardrail, not a claim about current repo state.

```text
apps/ui/
├── README.md
├── package.json                  # NEEDS VERIFICATION
├── src/                          # PROPOSED
│   ├── app/
│   ├── components/
│   ├── services/
│   ├── contracts/
│   └── __tests__/
├── public/                       # PROPOSED
└── fixtures/                     # PROPOSED
```

> [!NOTE]
> If a working branch adds runtime files here, update this README in the same PR so the tree, quickstart, and usage sections stay truthful.

[Back to top](#kfm-ui-path-boundary)

---

## Quickstart

### 1. Inspect the live path before editing claims

```bash
git rev-parse --short HEAD 2>/dev/null || true

find apps/ui -maxdepth 3 -print 2>/dev/null | sort
find apps -maxdepth 4 -type f -name "README.md" | sort
```

### 2. Compare nearby UI-boundary surfaces

```bash
find apps/explorer-web apps/review-console apps/governed-api apps/api web ui \
  -maxdepth 3 -type f 2>/dev/null | sort
```

### 3. Reconcile shell and API vocabulary

```bash
grep -RInE 'Evidence Drawer|Focus Mode|MapLibre|RuntimeResponseEnvelope|DecisionEnvelope|CorrectionNotice|audit_ref|ViewState|Citation|ABSTAIN|DENY|ERROR' \
  apps web ui docs contracts policy tests 2>/dev/null | sed -n '1,240p'
```

### 4. Upgrade this README only after branch-local proof appears

Use the following sequence:

1. confirm real files exist under `apps/ui/`
2. inspect manifests, runtime entrypoints, test roots, and routing files
3. replace placeholder tree with exact inventory
4. add only the commands that are directly runnable from that branch
5. reconcile sibling links in the same PR if path ownership changes

### 5. Keep review evidence close to the doc change

When changing this file, include:

- what became **CONFIRMED**
- what remains **UNKNOWN**
- which sibling doc or lane was affected
- whether any prior link now needs supersession or correction

[Back to top](#kfm-ui-path-boundary)

---

## Usage

### Boundary-first operating rule

Use `apps/ui/README.md` in one of three modes:

1. **Routing mode**  
   When `apps/ui/` is still README-only, keep this file as a narrow routing and reconciliation boundary.

2. **Runtime mode**  
   When a branch proves real UI code exists here, expand this file into a local runtime README with verified startup, structure, and test guidance.

3. **Handoff mode**  
   If this path is intentionally superseded by another surface, keep a short handoff note here and route readers to the winning path rather than leaving drift behind.

### Runtime rules if this path becomes active

If `apps/ui/` becomes a real runtime surface, preserve these constraints:

- browser traffic reads through governed APIs
- Evidence Drawer payloads stay inspectable
- Focus outcomes remain finite and visible: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`
- freshness, policy, review, sensitivity, generalization, and correction cues render in place
- 3D remains conditional and inherits the same trust objects as 2D
- no hidden direct write path to canonical or unpublished stores

### Do not let this path silently own more than it proves

The path may eventually own rendering, composition, interaction continuity, and client-side service orchestration. It should not quietly absorb:

- evidence resolution authority
- policy decision authority
- release or correction authority
- source onboarding or ingestion logic
- direct model-runtime control paths
- root UI ownership that belongs to `web/`, root `ui/`, or `apps/explorer-web/`

### Neighboring doc rule

Where browser-boundary rules are already stronger in [`../../web/README.md`](../../web/README.md), link there instead of cloning them here. Where shell choreography and runtime-surface framing are stronger in [`../explorer-web/README.md`](../explorer-web/README.md), link there instead of re-explaining them here. Where root [`../../ui/README.md`](../../ui/README.md) carries broader UI guidance, reconcile the relationship explicitly rather than treating `apps/ui/` as a synonym.

[Back to top](#kfm-ui-path-boundary)

---

## Diagram

```mermaid
flowchart LR
    U[User / reviewer] --> UI[apps/ui<br/>candidate local UI boundary]
    UI --> SHELL[Map + timeline + right-stack composition]
    UI --> SVC[Client service layer]
    SVC --> GAPI[Governed API]
    GAPI --> EV[Evidence / citation / policy mediation]
    GAPI --> OUT[Finite outcomes<br/>ANSWER · ABSTAIN · DENY · ERROR]
    EV --> ED[Evidence Drawer payloads]
    EV --> DS[Dossier / Story / Focus payloads]

    UI -. stronger app-local shell-boundary sibling .-> EX[apps/explorer-web]
    UI -. UI-root guidance sibling .-> WEB[web]
    UI -. root UI guidance lane .-> RUI[ui]
    UI -. review variation .-> RC[apps/review-console]
    GAPI -. route boundary .-> API[apps/api/src/api]

    classDef soft fill:#f7f7f7,stroke:#888,color:#222;
    class UI,SHELL,SVC,GAPI,EV,OUT,ED,DS,EX,WEB,RUI,RC,API,U soft;
```

### Reading the diagram

- `apps/ui/` is modeled as a **candidate boundary**, not a proven current runtime root.
- The service layer is explicit because client code should not bypass the governed API.
- Evidence Drawer, Dossier, Story, and Focus payloads sit on the same trust substrate.
- `web/README.md` reads as a stronger UI-root guidance surface, while `apps/explorer-web/README.md` remains the stronger app-local shell-boundary sibling.
- Root `ui/README.md` is a confirmed UI guidance lane and should be reconciled if ownership-sensitive work touches it.
- Review is a sibling shell variation, not a separate epistemic system.

[Back to top](#kfm-ui-path-boundary)

---

## Tables

### Ownership and routing matrix

| Concern | Owning path now | Reading rule |
|---|---|---|
| repo-wide identity and trust posture | [`../../README.md`](../../README.md) | start here for system-level meaning |
| app-subtree runtime map | [`../README.md`](../README.md) | use as parent boundary |
| strongest app-local shell-boundary doc | [`../explorer-web/README.md`](../explorer-web/README.md) | use for shell-boundary and choreography claims unless branch-local proof moves ownership |
| review / stewardship shell | [`../review-console/README.md`](../review-console/README.md) | review is shell variation |
| governed client API edge | [`../governed-api/README.md`](../governed-api/README.md) | browser-to-runtime trust membrane |
| deeper route/API boundary | [`../api/src/api/README.md`](../api/src/api/README.md) | route and contract context |
| UI-root browser guidance surface | [`../../web/README.md`](../../web/README.md) | use for browser-boundary rules, but do not treat as exclusive runtime authority until reconciliation |
| root UI guidance lane | [`../../ui/README.md`](../../ui/README.md) | reconcile if top-level UI ownership changes or if root shell material moves |
| this path itself | [`./README.md`](./README.md) | current local routing, placeholder, and reconciliation boundary |

### Trust-visible cue set for any future active UI under this path

| Cue family | Minimum expectation |
|---|---|
| time | visible time scope, chronology anchor, valid-time or as-of context |
| freshness | stale / partial / source-dependent cues render in place |
| evidence | consequential claims stay one hop from inspectable evidence |
| policy | rights, sensitivity, generalization, or review state remain visible |
| negative outcomes | deny / abstain / unavailable states are explicit, not silent |
| correction | visible correction, supersession, withdrawal, or replacement path when outward meaning changes |
| accessibility | trust cues are not color-only and remain testable |

### Truth posture used in this file

| Label | How it is used here |
|---|---|
| **CONFIRMED** | directly supported by the current visible repo or attached doctrine |
| **INFERRED** | small structural completion strongly implied by nearby evidence |
| **PROPOSED** | recommended local shape if this path becomes active |
| **UNKNOWN** | not verified strongly enough from current public evidence |
| **NEEDS VERIFICATION** | review flag before merge-time upgrade to settled fact |

[Back to top](#kfm-ui-path-boundary)

---

## Task list

- [ ] Confirm whether `apps/ui/` is intended to stay placeholder-only, become a runtime root, or remain a routing handoff to `apps/explorer-web/`, `web/`, or root `ui/`.
- [ ] Keep `apps/README.md`, `apps/ui/README.md`, `apps/explorer-web/README.md`, `web/README.md`, and root `ui/README.md` synchronized when ownership changes.
- [ ] Decide whether `web/README.md` is guidance-only, the winning UI-root, or a doc that should eventually hand off to `apps/explorer-web/` or root `ui/`.
- [ ] Decide whether root `ui/` remains a separate guidance lane, becomes the winning UI root, or delegates to another surface.
- [ ] If code exists on the working branch, replace the proposed subtree with the exact verified file inventory.
- [ ] Add verified quickstart commands only after manifests and entrypoints are directly visible.
- [ ] Keep client service-layer notes explicit if this path starts calling governed APIs.
- [ ] Add local verification surfaces when real code appears: accessibility checks, trust-cue rendering checks, negative-state checks, and Evidence Drawer drill-through.
- [ ] Update sibling READMEs in the same PR if path ownership changes.

### Definition of done

This README is in a good state when:

- it does not overclaim current repo reality
- a maintainer can tell exactly what `apps/ui/` does today
- a contributor knows where to route UI work if this path is still thin
- any future branch that makes this path real has a clear checklist for upgrading the README
- neighboring docs tell one consistent UI-boundary story
- unresolved runtime ownership is labeled rather than smoothed over

[Back to top](#kfm-ui-path-boundary)

---

## FAQ

### Is `apps/ui/` the active explorer shell?

**UNKNOWN** on current public main. The stronger current app-local shell-boundary README is [`../explorer-web/README.md`](../explorer-web/README.md), while `apps/ui/` is currently README-only.

### How should `../../web/README.md` be treated now?

As a stronger **UI-root guidance surface**, not as a placeholder. It carries substantial browser-boundary doctrine. What it still does **not** prove on its own is that `web/` is the singular runtime root for the active branch.

### How should root `../../ui/README.md` be treated?

As an additional **root-level UI guidance lane** that should be reconciled if UI ownership changes. It should not be silently merged with `apps/ui/` by name alone.

### Can this path talk directly to stores, indexes, or model runtimes?

No. If `apps/ui/` becomes active, it should still read through governed API boundaries and inherit the same evidence, policy, and review constraints as the rest of the shell.

### Should 3D behavior be documented here?

Only if this path actually owns the relevant runtime code. Even then, 3D remains conditional, inherits the same trust objects, and should not be documented as a separate truth system.

[Back to top](#kfm-ui-path-boundary)

---

## Appendix

<details>
<summary><strong>Current reconciliation backlog</strong></summary>

### Tension register

| Tension | Why it matters |
|---|---|
| `apps/ui/` exists as a README-only child while `apps/explorer-web/`, `web/`, and root `ui/` are stronger doctrinal docs | multiple UI-boundary docs can drift if ownership is not named explicitly |
| `apps/README.md` now lists `ui/` as a placeholder child path | one earlier ambiguity is closed, but synchronization pressure is higher |
| `web/README.md` is now substantial while active runtime-root authority still needs verification | stronger guidance no longer equals settled ownership |
| root `ui/README.md` exists with UI guidance and child paths | root-level UI ownership may overlap with app-local `apps/ui/` unless reconciled |
| `apps/explorer-web/README.md` is concrete while `apps/ui/` remains thin | suggests the stronger live shell story currently lives elsewhere |
| `apps/governed-api/` and API-lane naming remain partially tensioned in nearby docs | API-boundary links should follow the current path while branch-level naming settles |

### Safe next move

The smallest safe next move is not a speculative runtime rewrite. It is a reconciliation pass:

1. verify the working branch tree
2. name one authoritative UI-root / shell-boundary story
3. downgrade all others to routing docs or upgrade them with real inventory
4. keep sibling links synchronized in the same PR

</details>

<details>
<summary><strong>What to add first if this path becomes real</strong></summary>

1. exact file tree  
2. verified toolchain and startup commands  
3. service-layer and API-boundary notes  
4. local test / fixture inventory  
5. trust-visible rendering rules tied to actual components  
6. path-local contract adapter examples  
7. screenshots or diagrams only after structure is stable  

</details>

[Back to top](#kfm-ui-path-boundary)