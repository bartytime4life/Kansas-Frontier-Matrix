<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION
title: Review Console
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS_VERIFICATION
updated: 2026-04-18
policy_label: NEEDS_VERIFICATION
related: [../../README.md, ../README.md, ../../.github/README.md, ../../.github/CODEOWNERS, ../../contracts/README.md, ../../schemas/README.md, ../../policy/README.md, ../../tests/README.md]
tags: [kfm, apps, review-console, stewardship, review]
notes: [Owner grounded in current public CODEOWNERS broad /apps ownership; public app-family inventory reconciled with ../README.md, including apps/.codex as a support/audit path rather than runtime surface; doc_id, created date, and policy_label still need direct registry or repo-history verification.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Review Console

Governed reviewer and steward surface for promotion approval, policy assignment, QA inspection, and correction workflow.

![status](https://img.shields.io/badge/status-experimental-lightgrey)
![owners](https://img.shields.io/badge/owners-bartytime4life-0969da)
![surface](https://img.shields.io/badge/surface-review--console-8250df)
![trust](https://img.shields.io/badge/trust-shell%20variation-0a7d5a)
![evidence](https://img.shields.io/badge/evidence-drill--through%20required-1f6feb)
![policy](https://img.shields.io/badge/policy-review--bearing-f59e0b)
![tree](https://img.shields.io/badge/tree-public--main%20reconciled-2da44e)

> [!IMPORTANT]
> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> **Path:** `apps/review-console/README.md`  
> **Repo fit:** directory README for the review-bearing app boundary inside [`../README.md`](../README.md)  
> **Evidence posture:** doctrine-grounded · current-public-`main` path evidence · branch-local implementation depth still bounded  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Reference tables](#reference-tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

| Field | Value |
|---|---|
| Primary role | Keep approval, denial, hold, QA, and correction work inside the same trust-visible shell family as the rest of KFM |
| Upstream | [apps-root][] · [repo-root][] · [github-gatehouse][] · [codeowners][] |
| Authority neighbors | [contracts-root][] · [schemas-root][] · [policy-root][] · [tests-root][] |
| Downstream | Checked-in public-main baseline remains docs-first; exact branch-local routes, panels, fixtures, and tests stay `UNKNOWN` until re-verified |
| Working posture | **CONFIRMED doctrine** · **CONFIRMED current public-main path evidence** · **PROPOSED future local realization** · **UNKNOWN active-branch implementation depth** |

> [!NOTE]
> In KFM doctrine, review is a **shell variation**, not a second product and not a hidden authority layer. Approval, denial, hold, rollback, and correction work remain downstream of governed APIs, review artifacts, release state, and evidence drill-through.

> [!CAUTION]
> This README is **public-main-grounded for checked-in path claims** and **branch-grounded for merge-time truth**. If the working branch adds code beneath this directory, update the tree, downstream links, and test references in the same PR.

---

## Scope

`apps/review-console/` is the home for KFM’s **review-bearing operator surface**: the place where reviewers and stewards inspect evidence, assess QA state, assign or confirm policy, approve or deny promotion, and drive visible correction or rollback flows.

It is not here to become a separate admin island with looser truth rules. The review console should inherit the same core KFM commitments that govern the public shell:

- map-first, time-aware operation
- evidence drill-through at point of use
- explicit release context
- policy-visible decisions
- role-visible review authority
- negative outcomes as first-class states
- correction lineage that remains inspectable after publication

In practice, this directory is a **boundary README first** and an implementation surface second.

### Evidence boundary used here

| Evidence layer | What this README treats as settled |
|---|---|
| **CONFIRMED doctrine** | Review belongs inside the same governed shell family as map, timeline, Evidence Drawer, Focus, compare, export, and correction-visible surfaces |
| **CONFIRMED repo path evidence** | `apps/review-console/README.md` is present on current public `main`; current local subtree is README-only in public evidence |
| **INFERRED local fit** | Review mode should use shared shell grammar and shell continuity state rather than inventing a separate product model |
| **PROPOSED realization** | Future route, panel, fixture, and test names in this README are examples until active-branch files prove them |
| **UNKNOWN / NEEDS VERIFICATION** | Active branch implementation depth, exact routes, exact contract filenames, test inventory, workflow enforcement, and emitted review artifacts |

[Back to top](#top)

---

## Repo fit

`apps/review-console/README.md` sits below the app-level boundary README and should stay aligned with repo-wide governance posture in the root and `.github` docs.

### What belongs here

This directory is the right home for review-bearing UI concerns such as:

- promotion approval and denial flows
- hold, escalate, and re-review flows
- policy assignment and review-state presentation
- QA inspection against candidate or promoted artifacts
- evidence drill-through during review
- correction, supersession, withdrawal, and rollback visibility
- steward-safe comparison of release context, support state, and obligations

### Why this is an app surface

KFM doctrine separates **truth-bearing backend artifacts** from **shell-owned interaction state**. This directory should own the second category, not the first.

Truth-bearing artifacts stay elsewhere:

- contracts
- policy bundles
- release manifests
- review records
- evidence bundles
- catalog closures
- correction notices

Shell-owned state belongs here:

- selected subject
- compare state
- drawer openness
- active panel
- actor mode
- time scope
- operator navigation context

### Current public sibling and support context

| Surface | Current public state | Why it matters here |
|---|---|---|
| `../api/` | present in current public-main `apps/` family | current API lane exists beside `governed-api`; do not guess final naming authority |
| `../cli/` | present | confirms `apps/` is not only browser UI; operator-adjacent surfaces exist beside review |
| `../explorer-web/` | present | public exploration stays distinct from review-bearing stewardship work |
| `../governed-api/` | present | review must remain downstream of governed interfaces rather than embedding hidden authority |
| `./` | checked-in public-main baseline is docs-first | this path does not yet prove a shipped route tree |
| `../ui/` | present as a thin placeholder child doc in current public evidence | review still belongs to the same governed shell family, but durable UI boundary ownership needs verification |
| `../workers/` | present | execution and async work stay adjacent to, not collapsed into, review UI concerns |
| `../.codex/` | visible as an app-local support/audit path | useful for markdown/path integrity context, not runtime proof and not a review-console child app |

### Nearby docs that should stay in sync

- [apps-root][] — app boundary and runtime grouping
- [repo-root][] — repo posture, trust model, and current evidence boundary
- [github-gatehouse][] — contributor and review workflow posture
- [codeowners][] — current broad ownership fallback
- [contracts-root][] / [schemas-root][] / [policy-root][] — authority surfaces this app consumes but must not replace

[Back to top](#top)

---

## Accepted inputs

The review console should accept **review-shaped inputs**, not raw canonical mutation power.

| Input family | What it looks like here | Status |
|---|---|---|
| Review queue items | candidate releases, held items, approval-needed work, correction-needed work | **PROPOSED local realization** |
| Policy decisions | approve / deny / hold / generalize / restrict outcomes with reasons and obligations | **CONFIRMED doctrinal need** |
| QA and validation signals | structural, temporal, spatial, CRS, rights, accessibility, or catalog findings | **CONFIRMED doctrinal need** |
| Evidence drill-through payloads | Evidence Drawer targets, `EvidenceBundle` refs, lineage pointers, proof-pack references | **CONFIRMED doctrinal need** |
| Release context | release ID, dataset version, review state, promotion readiness, correction status | **CONFIRMED doctrinal need** |
| Shell state | selected subject, compare mode, active panel, actor role, time scope | **INFERRED local fit** |
| Restricted review actions | action payloads that emit review and decision artifacts rather than hidden mutations | **CONFIRMED doctrinal need** |

### Good examples of content for this directory

- review panels and routes
- shell-state adapters for review mode
- review-specific tests and fixtures
- accessibility checks for approval and correction flows
- visual states for hold, deny, partial, stale, superseded, withdrawn, and generalized conditions
- local docs explaining how review behavior stays governed

[Back to top](#top)

---

## Exclusions

This directory should **not** become the quiet place where canonical law hides.

| Does **not** belong here | Why | Put it in / keep it with |
|---|---|---|
| Canonical schemas and vocabularies | review screens consume them; they do not define them | [contracts-root][] and [schemas-root][] |
| Policy source of truth | the review console presents and applies policy outcomes; it should not become the policy registry | [policy-root][] |
| RAW, WORK, QUARANTINE, or unpublished source storage | this surface must not become a direct path to canonical or unpublished stores | governed data and lifecycle zones |
| Evidence resolution law | UI should call it, not re-implement it | governed API or package boundary for evidence resolution |
| Promotion manifests / release proof generation logic | review can inspect or trigger, but it must not silently own artifact law | release, build, promotion, proof, or worker surfaces |
| Detached chatbot behavior | review-focused synthesis must remain bounded, cited, and subordinate to evidence | governed Focus/runtime surfaces |
| Public discovery UI | this surface is steward/reviewer-facing, not the default public exploration mode | explorer/public shell surfaces |
| Hidden write paths to truth stores | breaks the trust membrane | governed API only |
| Markdown/path audit reports treated as runtime proof | support artifacts can assist review, but they do not prove route or test depth | docs/tooling or `.codex` support surfaces |

> [!WARNING]
> If this directory starts owning domain rules, policy grammar, or release proof composition directly, it has crossed from **review surface** into **hidden authority layer**.

[Back to top](#top)

---

## Directory tree

The tree below reflects the **current public-main path snapshot** that this README is reconciling against. It is a path inventory, not a runtime maturity claim.

### Current public-main `apps/` snapshot

```text
apps/
├── README.md
├── .codex/
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

### Current checked-in `review-console/` subtree baseline

```text
apps/
└── review-console/
    └── README.md
```

The broader app-family snapshot above is reconciled with [`../README.md`](../README.md). The local subtree baseline stays intentionally narrow. Re-check the active branch before presenting either view as merge-time truth.

### Why the tree is still kept minimal here

This README should not pretend that routes, panels, tests, or fixtures already exist unless the active branch confirms them.

<details>
<summary><strong>PROPOSED</strong> future subtree once the active branch grows beyond the scaffold</summary>

```text
apps/
└── review-console/
    ├── README.md
    ├── routes/
    │   ├── approvals/
    │   ├── policy/
    │   ├── qa/
    │   ├── corrections/
    │   └── audits/
    ├── panels/
    │   ├── evidence-drawer/
    │   ├── release-summary/
    │   ├── diff-inspection/
    │   ├── obligations/
    │   └── correction-lineage/
    ├── state/
    │   ├── shell/
    │   └── review-session/
    ├── lib/
    │   ├── contracts/
    │   └── api-clients/
    ├── tests/
    │   ├── accessibility/
    │   ├── review-flows/
    │   ├── evidence-drillthrough/
    │   └── corrections/
    └── fixtures/
        ├── approval/
        ├── denial/
        ├── hold/
        └── correction/
```

All items above are **PROPOSED**, not confirmed current contents.
</details>

[Back to top](#top)

---

## Quickstart

This section is intentionally **read-only and verification-first**. Do not treat it as proof that a runnable review console already exists.

### 1) Confirm current branch, current tree, and local drift

```bash
git rev-parse --show-toplevel
git rev-parse --short HEAD

find apps/review-console -maxdepth 5 -print | sort
git diff -- apps/review-console
```

### 2) Confirm the boundary docs still line up

```bash
sed -n '1,260p' README.md
sed -n '1,320p' apps/README.md
sed -n '1,260p' apps/review-console/README.md
sed -n '1,260p' .github/README.md
sed -n '1,220p' .github/CODEOWNERS
```

### 3) Inspect the app family and support paths

```bash
find apps -maxdepth 4 -type f | sort
find apps/.codex -maxdepth 2 -type f 2>/dev/null | sort
```

### 4) Confirm which KFM review terms already appear in code and docs

```bash
grep -RInE 'ReviewRecord|DecisionEnvelope|ReleaseManifest|ReleaseProofPack|CorrectionNotice|EvidenceBundle|review-action|release-action|approve|deny|hold|rollback|supersed|withdraw' \
  apps packages contracts policy docs tests 2>/dev/null
```

### 5) Confirm whether this directory has real routes, tests, or fixtures yet

```bash
find apps/review-console -maxdepth 5 \
  \( -name 'app' -o -name 'pages' -o -name '*.tsx' -o -name '*.ts' -o -name '*.test.*' -o -name '*.spec.*' -o -name 'fixtures' \) \
  -print | sort
```

### 6) Confirm whether review behavior is wired only through governed surfaces

```bash
grep -RInE 'EvidenceRef|EvidenceBundle|audit_ref|policy_label|ReviewRecord|DecisionEnvelope|RuntimeResponseEnvelope' \
  apps packages contracts docs tests 2>/dev/null
```

### 7) Update this README only after the inspection

Use the results above to replace placeholders such as:

- `NEEDS_VERIFICATION`
- `UNKNOWN active-branch implementation depth`
- `PROPOSED local realization`
- candidate subtree examples
- missing downstream references
- provisional route and test assumptions

> [!TIP]
> Prefer one small follow-up commit that updates owner notes, child tree, exact route names, and test paths after inspection over a broad speculative rewrite.

[Back to top](#top)

---

## Usage

### Operating law

The review console should be used as a **governed inspection-and-decision surface**.

A healthy review pass looks like this:

1. Open the candidate subject, release, or correction case.
2. Keep geography, time scope, release context, actor role, and review state visible.
3. Open supporting evidence without leaving the shell family.
4. Inspect QA and policy-bearing facts before acting.
5. Approve, deny, hold, generalize, restrict, or escalate with explicit rationale.
6. Preserve review state, correction lineage, and audit linkage after the action.

### What good use looks like

- a reviewer can move from map or dossier context into review work without losing trust cues
- every consequential claim has a route back to evidence
- approval is never just a button; it is an action with visible support, obligations, and lineage
- denial is not hidden or collapsed into a generic error state
- correction and supersession remain legible after publication
- route changes do not erase active release, time, policy, or evidence context

### What bad use looks like

- approving from an isolated table with no evidence access
- policy assignment without visible rights or sensitivity context
- correction screens that silently overwrite what happened before
- review-only UI that fetches directly from canonical stores
- an operator surface that drifts away from the shell grammar used elsewhere
- UI-only policy decisions that are not backed by governed decision artifacts

[Back to top](#top)

---

## Diagram

```mermaid
flowchart LR
    R[Reviewer / steward] --> S[Review Console<br/>shell variation]

    S --> API[Internal governed API]
    API --> EV[EvidenceRef → EvidenceBundle]
    API --> PO[Policy runtime]
    API --> QA[Validation / QA state]
    API --> RL[Catalog / release context]
    API --> CL[Correction lineage]

    EV --> S
    PO --> S
    QA --> S
    RL --> S
    CL --> S

    S --> D1[Approve / promote]
    S --> D2[Hold / deny / escalate]
    S --> D3[Correct / supersede / withdraw]

    D1 --> O1[DecisionEnvelope<br/>ReviewRecord<br/>ReleaseManifest]
    D2 --> O2[DecisionEnvelope<br/>ReviewRecord]
    D3 --> O3[CorrectionNotice<br/>rebuild refs<br/>visible lineage]

    C[contracts + schemas] -. define payload shapes .-> API
    P[policy] -. evaluates obligations .-> API
    T[tests] -. prove boundary behavior .-> S
```

### Reading rule for the diagram

The review console is **not** the place where truth originates. It is the place where already-governed evidence, policy, validation, and release context become inspectable enough for human review actions.

[Back to top](#top)

---

## Reference tables

### Shared shell regions that review should inherit

| Region | Shared responsibility in review mode | Status |
|---|---|---|
| Top command bar | global search, mode switching, scope badges, saved views, role context, alerts | **CONFIRMED shell doctrine** |
| Left rail | layers, domains, filters, compare controls, story chapter lists, review queue visibility for authorized roles | **CONFIRMED shell doctrine** |
| Map canvas | primary geography surface, selection anchor, story playback surface, direct evidence launch point | **CONFIRMED shell doctrine** |
| Bottom timeline rail | valid-time framing, playback, compare anchors, as-of inspection, visible chronology | **CONFIRMED shell doctrine** |
| Right inspection stack | dossier panels, Evidence Drawer, review controls, correction lineage, obligations | **CONFIRMED shell doctrine / INFERRED review fit** |

### Decision lanes and minimum visible outputs

| Review lane | Minimum visible outputs | Why it matters |
|---|---|---|
| Approve / promote | `DecisionEnvelope`, `ReviewRecord`, `ReleaseManifest` / `ReleaseProofPack` | a public-safe release should not leave review as a hidden click |
| Hold / deny / escalate | `DecisionEnvelope`, `ReviewRecord`, reason and obligation codes | negative outcomes are first-class review behavior, not embarrassing edge cases |
| Correct / supersede / withdraw | `CorrectionNotice`, rebuild references, visible lineage | correction must remain inspectable after publication |

### Review-bearing artifact families

| Artifact family | Why this surface cares | Status |
|---|---|---|
| `DecisionEnvelope` | machine-readable policy result for action, lane, result, reason codes, obligation codes, and audit linkage | **CONFIRMED doctrinal dependency** |
| `ReviewRecord` | captures approval, denial, escalation, or note with reviewer role, time, and refs | **CONFIRMED doctrinal dependency** |
| `ReleaseManifest` / `ReleaseProofPack` | packages the public-safe release and its proof posture for approval-ready work | **CONFIRMED doctrinal dependency** |
| `EvidenceBundle` | provides drill-through support for a claim, feature, export preview, or review decision | **CONFIRMED doctrinal dependency** |
| `CorrectionNotice` | preserves visible lineage under supersession, withdrawal, replacement, or narrowing | **CONFIRMED doctrinal dependency** |

### Trust cues that must not disappear in review mode

| Trust cue | Must remain visible in review mode? | Notes |
|---|---|---|
| Active release context | Yes | no detached “review truth” |
| Time basis / freshness | Yes | compare and correction depend on it |
| Evidence Drawer access | Yes | mandatory drill-through path |
| Policy label / visibility class | Yes | approval without policy context is weak review |
| Correction / supersession state | Yes | review must not hide history |
| Actor role / permission posture | Yes | review authority must be explicit |
| Negative outcome states | Yes | deny / hold / restricted must not flatten into generic success/failure |

### Status ledger for this README

| Topic | Status |
|---|---|
| Review / stewardship is a necessary KFM surface concept | **CONFIRMED doctrine** |
| Review remains a shell variation, not an alternate truth system | **CONFIRMED doctrine** |
| Review is an internal governed route family, not a public route family | **CONFIRMED doctrine** |
| Review actions must emit review and decision artifacts | **CONFIRMED doctrine** |
| This exact directory path is checked in on current public `main` | **CONFIRMED current repo evidence** |
| Current public-main `apps/` inventory includes `.codex/`, `api/`, `cli/`, `explorer-web/`, `governed-api/`, `review-console/`, `ui/`, and `workers/` | **CONFIRMED current repo evidence** |
| Current checked-in `review-console/` subtree baseline is still docs-first | **CONFIRMED current repo evidence** |
| Exact child files, routes, panels, tests, fixtures, and branch-local depth | **UNKNOWN / NEEDS VERIFICATION** |
| Proposed future subtree and local file names in this README | **PROPOSED** |

[Back to top](#top)

---

## Task list

### Merge-time review gates for this README

- [ ] Re-inspect the active branch and reconcile it against the current public-main snapshot above.
- [ ] Replace proposed child paths with confirmed local files, or delete them.
- [ ] Link exact review routes or entrypoints if they now exist.
- [ ] Confirm whether review uses shared shell state or a separate local store.
- [ ] Confirm whether approval, denial, hold, and correction payloads are documented elsewhere.
- [ ] Add exact test paths once accessibility, evidence-drill-through, and correction tests exist.
- [ ] Reconfirm owner mapping if `/.github/CODEOWNERS` changes.
- [ ] Reconfirm this file if the public `apps/` family changes again.
- [ ] Confirm whether `apps/.codex/` should remain linked from app READMEs as support evidence.
- [ ] Remove any statement that has become stale after implementation lands.

### Definition of done for the surface itself

- [ ] Every consequential review screen can open evidence without leaving the governed shell family.
- [ ] Approval, denial, hold, and correction each produce visible, inspectable outcomes.
- [ ] Review actions do not bypass governed APIs.
- [ ] Release context, time basis, actor role, and trust cues survive route changes.
- [ ] Accessibility checks cover keyboard navigation, reduced motion, role-state cues, and drawer reachability.
- [ ] Correction and rollback states are visibly distinguishable from normal approval flows.
- [ ] Negative outcomes are visible and reviewable, not collapsed into generic errors.
- [ ] Review artifacts can be inspected without granting direct canonical-store access.

[Back to top](#top)

---

## FAQ

### Is this a separate admin application?

No. It should behave as a **shell variation** with stricter permissions and additional review actions, not as a second product with different truth rules.

### Can review screens talk directly to canonical stores?

No. This surface should read and act **through governed APIs only**.

### Does this README prove the review console already has routes and tests?

No. The checked-in public-main baseline is still docs-first. Exact active-branch implementation depth still needs inspection before merge.

### Should this surface own policy definitions?

No. It may present, confirm, and apply policy-shaped decisions, but policy grammar and policy source of truth belong elsewhere.

### Why mention `apps/.codex/`?

Because the current app-family README records it as a visible support/audit path under `apps/`. This README treats it as documentation integrity context only, not as runtime proof and not as part of the review console.

### What is the most important trust object on this surface?

The **Evidence Drawer** or equivalent drill-through path. Review without inspectable support is not strong KFM review.

[Back to top](#top)

---

## Appendix

<details>
<summary><strong>Current evidence boundary and maintenance notes</strong></summary>

### What is safe to claim here

- `apps/review-console/README.md` is a checked-in path on current public `main`
- the broader current public-main `apps/` inventory includes `.codex/`, `api/`, `cli/`, `explorer-web/`, `governed-api/`, `review-console/`, `ui/`, and `workers/`
- `apps/.codex/` is a support/audit path, not a review-console runtime surface
- the checked-in `review-console/` baseline is still docs-first
- KFM doctrine treats review / stewardship as part of the same governed shell family
- review is an internal governed route family, not a public route family
- active-branch implementation depth remains branch-dependent and must be re-verified

### What should be checked before the next rewrite

- confirmed active-branch subtree
- exact route families in use
- whether review state is persisted, URL-shaped, or session-local
- exact contract names for review payloads
- exact test inventory
- exact accessibility evidence
- exact correction and rollback drill evidence
- exact relationship between any `.codex` support artifacts and merge-time documentation checks

### Maintenance rule

When this directory gains real code, update this README in the same change set that adds:

1. child tree changes
2. route names
3. test paths
4. confirmed owner shifts
5. any new downstream doc links
6. any new review artifact or proof-pack linkage

That keeps the README from getting ahead of mounted proof.
</details>

[Back to top](#top)

---

[apps-root]: ../README.md
[repo-root]: ../../README.md
[github-gatehouse]: ../../.github/README.md
[codeowners]: ../../.github/CODEOWNERS
[contracts-root]: ../../contracts/README.md
[schemas-root]: ../../schemas/README.md
[policy-root]: ../../policy/README.md
[tests-root]: ../../tests/README.md
[data-root]: ../../data/README.md