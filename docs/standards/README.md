<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/REVIEW_REQUIRED_UUID
title: docs/standards
type: standard
version: v1
status: draft
owners: @bartytime4life
created: REVIEW_REQUIRED_DATE
updated: 2026-04-18
policy_label: public
related: [../README.md, ../../README.md, ./KFM_STAC_PROFILE.md, ./KFM_DCAT_PROFILE.md, ./KFM_PROV_PROFILE.md, ./KFM_MARKDOWN_WORK_PROTOCOL.md, ./markdown-rules.md, ./governance/README.md, ./governance/ROOT_GOVERNANCE.md, ./faircare/README.md, ./faircare/FAIRCARE-GUIDE.md, ./sovereignty/README.md, ./sovereignty/INDIGENOUS-DATA-PROTECTION.md, ./stac/README.md, ./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md, ../runbooks/README.md, ../../contracts/README.md, ../../contracts/vocab/README.md, ../../schemas/README.md, ../../schemas/contracts/README.md, ../../schemas/contracts/v1/README.md, ../../policy/README.md, ../../tests/README.md, ../../tests/contracts/README.md, ../../tests/e2e/runtime_proof/, ../../.github/workflows/README.md]
tags: [kfm, docs, standards, metadata, provenance, governance, markdown, routing, runtime-proof]
notes: [UUID and commit-level dates still need direct verification., This revision preserves the public-main standards surface while making contract/schema routing ambiguity explicit., docs/standards is a prose authority lane and must not silently choose the canonical machine-contract home., Runtime-proof is now treated as a downstream consumer that must not redefine contract or schema authority.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/standards/`

Governed **standards index** for KFM metadata, provenance, publication, documentation, review, and cross-lane routing rules.

<div align="left">

![Status](https://img.shields.io/badge/status-experimental-orange)
![Doc](https://img.shields.io/badge/doc-draft-orange)
![Owner](https://img.shields.io/badge/owner-%40bartytime4life-blue)
![Routing](https://img.shields.io/badge/routing-authority__split__explicit-5319e7)
![Branch](https://img.shields.io/badge/branch-main-blue)
![KFM](https://img.shields.io/badge/KFM-standards-purple)
![Evidence](https://img.shields.io/badge/evidence-public%20main%20%2B%20April%202026%20corpus-lightgrey)

</div>

| Field | Value |
|---|---|
| **Path** | `docs/standards/README.md` |
| **Status** | experimental |
| **Owners** | `@bartytime4life` *(current visible `/docs/` owner signal; no narrower `/docs/standards/` rule directly confirmed here)* |
| **Primary job** | root standards index and routing surface for shared norm text |
| **Not this lane** | machine-contract registry, executable policy home, fixture store, workflow gatehouse, or silent authority winner |
| **Current emphasis** | truthful public-tree index, routing clarity, authority-split visibility, runtime-proof consumption boundaries |

**Quick jumps:** [Scope](#scope) · [Evidence posture](#evidence-posture) · [Repo fit](#repo-fit) · [Current public standards surface](#current-public-standards-surface) · [Lane-local directories](#lane-local-directories) · [Routing guardrails](#routing-guardrails) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Standards map](#standards-map) · [Put-it-here test](#put-it-here-test) · [Definition of done](#definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This index is grounded in two evidence layers:
>
> - the current KFM doctrine corpus
> - direct public-`main` inspection of `docs/standards/`, its lane-local subdirectories, `docs/README.md`, `.github/CODEOWNERS`, `contracts/README.md`, `contracts/vocab/README.md`, `schemas/README.md`, `schemas/contracts/README.md`, `schemas/contracts/v1/README.md`, `policy/README.md`, `tests/README.md`, `tests/contracts/README.md`, `docs/runbooks/README.md`, and `.github/workflows/README.md`

> [!WARNING]
> `docs/standards/` must not resolve the current **machine-contract home split** by tone, implication, or convenience.
>
> Current repo signals still point at both:
>
> - `../../contracts/`
> - `../../schemas/contracts/`
>
> Until the repo explicitly resolves that split, this standards lane should route contributors carefully and **block silent duplication**.

> [!TIP]
> Treat `tests/e2e/runtime_proof/` as a **downstream consumer** of standards, contracts, schemas, and policy.
>
> It may prove request-time behavior, but it must **not** choose contract authority, invent private vocabularies, or fork schema shape by test convenience.

> [!NOTE]
> [`markdown-rules.md`](./markdown-rules.md) is a visible repo surface on current public `main`, but it is **not** the same thing as [`KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md).
>
> Treat the latter as the **normative Markdown standards file** unless the branch under review explicitly changes that authority split.

---

## Scope

`docs/standards/` is the governed home for **cross-cutting standards and profiles** used across KFM domains, catalog closure, governed APIs, UI surfaces, Story Nodes, Focus Mode, and review/release flows.

Inside `docs/`, this lane is the answer to the question:

> **What must be true?**

It should keep shared rules legible without quietly replacing contracts, policy bundles, tests, workflow gates, or truth-path artifacts with prose.

This README is an **index and routing surface**, not a second copy of every standard. Its job is to keep the standards lane readable, correctly classified, and synchronized with the real branch.

### Parent-lane rule

Use this directory for:

- reusable standards
- shared profiles
- cross-domain governance text
- lane-local standards routing READMEs
- normative documentation protocol
- temporary routing law while machine-contract authority remains unresolved

Do **not** use this lane to quietly become:

- the machine-contract registry
- the executable policy home
- the test fixture store
- the workflow gatehouse
- the runbook lane
- a duplicate authority source for rules already owned elsewhere

### Temporary routing rule

Until canonical machine-contract authority is written down explicitly:

1. **Do not create new contract families by default**
2. **Do not let standards prose imply that both homes are equally valid for new files**
3. **Do not let runtime-proof, validators, or schemas point at different “authoritative” paths**
4. **Require an explicit placement decision before landing new trust-bearing contract families**

[Back to top](#top)

---

## Evidence posture

| Claim | Status | Why it matters |
|---|---|---|
| `docs/standards/` is a real governed standards lane | **CONFIRMED** | this file is a live routing surface, not a placeholder |
| root-level standards and lane-local standards files are visible on public `main` | **CONFIRMED** | this index must route to existing files honestly |
| `contracts/` and `schemas/contracts/` are both meaningful adjacent signals | **CONFIRMED** | standards routing must not hide the split |
| `contracts/vocab/` and `schemas/contracts/vocab/` both matter to routing | **CONFIRMED** | vocabulary ownership is part of standards routing now |
| runtime-proof is now a downstream standards consumer | **INFERRED** | current KFM doctrine repeatedly pressures request-time proof surfaces |
| canonical machine-contract home is resolved | **NEEDS VERIFICATION** | current evidence still shows split authority |
| this lane may choose the winning machine-contract path implicitly | **DENIED by doctrine** | prose routing must not settle machine authority by accident |

[Back to top](#top)

---

## Repo fit

| Item | Value |
|---|---|
| Path | [`docs/standards/README.md`](./README.md) |
| Path status | **CONFIRMED** on public `main`; mounted-checkout parity still **NEEDS VERIFICATION** |
| Role | directory index and routing surface for cross-cutting standards, profiles, lane-local README boundaries, and adjacent authoring guidance |
| Within `docs/` | the lane for “what must be true?” |
| Upstream | [`../README.md`](../README.md) · [`../../README.md`](../../README.md) |
| Root standard files | [`./KFM_STAC_PROFILE.md`](./KFM_STAC_PROFILE.md) · [`./KFM_DCAT_PROFILE.md`](./KFM_DCAT_PROFILE.md) · [`./KFM_PROV_PROFILE.md`](./KFM_PROV_PROFILE.md) · [`./KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md) · [`./markdown-rules.md`](./markdown-rules.md) |
| Lane-local directories | [`./governance/README.md`](./governance/README.md) · [`./faircare/README.md`](./faircare/README.md) · [`./sovereignty/README.md`](./sovereignty/README.md) · [`./stac/README.md`](./stac/README.md) |
| Primary downstream standards and notes | [`./governance/ROOT_GOVERNANCE.md`](./governance/ROOT_GOVERNANCE.md) · [`./faircare/FAIRCARE-GUIDE.md`](./faircare/FAIRCARE-GUIDE.md) · [`./sovereignty/INDIGENOUS-DATA-PROTECTION.md`](./sovereignty/INDIGENOUS-DATA-PROTECTION.md) · [`./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md`](./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md) |
| Adjacent governed areas | [`../runbooks/README.md`](../runbooks/README.md) · [`../../contracts/README.md`](../../contracts/README.md) · [`../../contracts/vocab/README.md`](../../contracts/vocab/README.md) · [`../../schemas/README.md`](../../schemas/README.md) · [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md) · [`../../schemas/contracts/v1/README.md`](../../schemas/contracts/v1/README.md) · [`../../policy/README.md`](../../policy/README.md) · [`../../tests/README.md`](../../tests/README.md) · [`../../tests/contracts/README.md`](../../tests/contracts/README.md) · [`../../tests/e2e/runtime_proof/`](../../tests/e2e/runtime_proof/) · [`../../.github/workflows/README.md`](../../.github/workflows/README.md) |
| Ownership signal | `/docs/` currently routes to `@bartytime4life` in `.github/CODEOWNERS`; no narrower `/docs/standards/` rule is directly visible on public `main` |

### Boundary rule

Use `docs/standards/` to state **shared norm text** and **routing law**.

Do **not** use it to own:

- machine schemas
- executable policies
- CI logic
- domain ETL instructions
- runtime behavior contracts
- release proof objects
- ad hoc planning notes disguised as standards

### Routing rule for adjacent machine surfaces

When standards text refers to machine-facing companions:

- it may point to `contracts/`
- it may point to `schemas/contracts/`
- it may point to both **only to describe the current unresolved state**
- it must **not** tell contributors to add new trust-bearing families to both
- it must **not** imply that ambiguity is harmless

[Back to top](#top)

---

## Current public standards surface

The standards lane is no longer just this index plus a few profile files. Public `main` now shows a mixed surface: root-level standards, a visible task-facing Markdown brief, and lane-local README boundaries beneath multiple subdirectories.

### Root-level standards and protocol files

| Surface | Current public `main` state | Why it matters |
|---|---|---|
| [`README.md`](./README.md) | present, substantive directory index | this file should be revised in place, not replaced by a parallel index |
| [`KFM_STAC_PROFILE.md`](./KFM_STAC_PROFILE.md) | present, substantive draft standard | STAC rules already have a dedicated home; this index should route to it rather than re-explaining it |
| [`KFM_DCAT_PROFILE.md`](./KFM_DCAT_PROFILE.md) | present, substantive draft standard | DCAT dataset/distribution rules already have their own surface |
| [`KFM_PROV_PROFILE.md`](./KFM_PROV_PROFILE.md) | present, substantive draft standard | outward lineage/profile work is already materially started here |
| [`KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md) | present, substantive draft protocol | repo-native Markdown authoring and review rules already have a normative home |
| [`markdown-rules.md`](./markdown-rules.md) | present, visible task-facing authoring brief / repo-local instruction surface | contributors should not confuse this file with the normative Markdown protocol or let the two drift silently apart |

[Back to top](#top)

---

## Lane-local directories

| Lane | Current public `main` state | Routing consequence |
|---|---|---|
| [`governance/`](./governance/README.md) | `README.md` + [`ROOT_GOVERNANCE.md`](./governance/ROOT_GOVERNANCE.md) are both visible | route directory-boundary and lane-index edits to `governance/README.md`; route cross-domain governance law to `ROOT_GOVERNANCE.md` |
| [`faircare/`](./faircare/README.md) | `README.md` + [`FAIRCARE-GUIDE.md`](./faircare/FAIRCARE-GUIDE.md) are both visible | do **not** keep calling this lane scaffold-only; the guide is now a substantive public-main standards surface |
| [`sovereignty/`](./sovereignty/README.md) | `README.md` + [`INDIGENOUS-DATA-PROTECTION.md`](./sovereignty/INDIGENOUS-DATA-PROTECTION.md) are both visible | route lane-boundary edits to the README and substantive sovereignty rules to the downstream standard |
| [`stac/`](./stac/README.md) | `README.md` + [`OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md`](./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md) are both visible | treat this as the STAC-specific support lane beneath the repo-wide STAC profile, not as a duplicate authority root |

### Adjacent repo signals

| Surface | Current public `main` state | Why it matters here |
|---|---|---|
| [`../README.md`](../README.md) | present, substantive | the repo root frames KFM as governed, evidence-first, map-first, and time-aware |
| [`../runbooks/README.md`](../runbooks/README.md) | present, substantive | procedures, rollback, correction, and operator behavior now have a visible sibling surface and should not be absorbed into standards prose |
| [`../../contracts/README.md`](../../contracts/README.md) | present, substantive | root human-readable machine-contract guidance still lives here |
| [`../../contracts/vocab/README.md`](../../contracts/vocab/README.md) | present, substantive | vocabulary routing now has an explicit root-side surface |
| [`../../schemas/README.md`](../../schemas/README.md) | present, substantive | `schemas/` now has a live nested subtree, but schema-home authority remains explicitly unresolved |
| [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md) | present, substantive | current public `main` shows a real machine-file-bearing subtree under `schemas/contracts/` |
| [`../../schemas/contracts/v1/README.md`](../../schemas/contracts/v1/README.md) | present, substantive | the versioned contract lane is already visible and should be routed honestly when standards talk about machine-facing companions |
| [`../../policy/README.md`](../../policy/README.md) | present, substantive | keeps deny-by-default, reasons/obligations, and publication-as-governance visible |
| [`../../tests/README.md`](../../tests/README.md) | present, substantive | frames verification as governed proof, not generic QA |
| [`../../tests/contracts/README.md`](../../tests/contracts/README.md) | present, substantive | contract-facing verification should eventually point to one authoritative machine path |
| [`../../tests/e2e/runtime_proof/`](../../tests/e2e/runtime_proof/) | doctrinally relevant downstream proof family; exact branch contents may vary | request-time proof must consume one authoritative contract/schema path rather than redefining it |
| [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | present, README-only lane | public `main` still documents workflow intent more strongly than checked-in workflow YAML inventory |

[Back to top](#top)

---

## Routing guardrails

This section is intentionally explicit because the repo now has enough live surfaces to drift by “reasonable” interpretation.

### Guardrail 1 — no silent authority choice

If a standard needs to reference machine contracts:

- cite the current state honestly
- name unresolved authority when it exists
- avoid language that implies “put it in either place”

### Guardrail 2 — no new family by inertia

Until the repo resolves canonical machine-contract authority:

- do **not** create new trust-bearing contract families by default
- do **not** add a matching file under both `contracts/` and `schemas/contracts/`
- do **not** let standards prose normalize duplication as routine

### Guardrail 3 — runtime-proof is consumption, not authorship

`tests/e2e/runtime_proof/` may:

- consume contract and schema authority
- prove governed runtime behavior
- validate outward outcome grammar

It must **not**:

- invent new envelope shapes
- fork vocabulary families
- choose the canonical home by fixture convenience
- silently repair upstream ambiguity with local copies

### Guardrail 4 — vocabulary must stay singular

When standards text references shared vocabularies:

- contract-shared vocab points to `contracts/vocab/` or the explicitly chosen canonical machine-readable home
- policy-owned code lists point to `policy/`
- if `schemas/contracts/vocab/` remains in play, its relationship to `contracts/vocab/` must be described explicitly as canonical, mirror, pointer, or unresolved

### Guardrail 5 — one rule family, one owning surface

A standards file may route to many downstream surfaces, but each rule family still needs one owning home.

If you cannot name the owner cleanly, the standards change is not ready.

[Back to top](#top)

---

## Accepted inputs

Place a document in `docs/standards/` when it defines a reusable rule that multiple KFM subsystems must share.

| Accepted input | Why it belongs here |
|---|---|
| metadata profiles | shared outward rules for STAC, DCAT, PROV, and related release-safe discovery surfaces |
| governance and review-trigger standards | cross-domain rules for trust-state transitions, review burden, publication, correction, and runtime boundaries |
| FAIR+CARE / sovereignty / rights / sensitivity standards | cross-cutting protection rules that multiple domains and outward surfaces must inherit |
| documentation protocols | rules for governed Markdown authoring, structure, truth posture, and review |
| lane-local directory READMEs | routing, scope, exclusions, and local ownership boundaries for a standards sub-lane |
| interoperability and deployment notes | standards-aligned guidance that sharpens how KFM implements shared profiles |
| routing constraints for unresolved authority seams | temporary but necessary guardrails while adjacent machine homes are being reconciled |

### Minimum bar for anything added here

- it is genuinely **normative** across more than one lane or domain
- it has a clear owning surface
- it does not duplicate a stronger neighboring authority
- it stays prose-focused rather than pretending to be executable policy or schema authority
- it makes unresolved enforcement depth visible instead of smoothing it away

[Back to top](#top)

---

## Exclusions

This directory should not become a catch-all, and this README should not duplicate rules already owned elsewhere.

| Does **not** belong in this index | Put it here instead |
|---|---|
| field-by-field STAC rules | [`./KFM_STAC_PROFILE.md`](./KFM_STAC_PROFILE.md) |
| DCAT dataset/distribution detail | [`./KFM_DCAT_PROFILE.md`](./KFM_DCAT_PROFILE.md) |
| PROV entity/activity/agent detail | [`./KFM_PROV_PROFILE.md`](./KFM_PROV_PROFILE.md) |
| normative Markdown authoring and review rules | [`./KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md) |
| one-off or branch-local writing prompts that are **not** an intentionally maintained repo surface | task / planning / review surface, not `docs/standards/` |
| lane-local routing/index prose | the relevant subdirectory `README.md` |
| core governance law and review outcomes | [`./governance/ROOT_GOVERNANCE.md`](./governance/ROOT_GOVERNANCE.md) |
| FAIR+CARE-specific norm text | [`./faircare/FAIRCARE-GUIDE.md`](./faircare/FAIRCARE-GUIDE.md) |
| sovereignty-sensitive publication rules | [`./sovereignty/INDIGENOUS-DATA-PROTECTION.md`](./sovereignty/INDIGENOUS-DATA-PROTECTION.md) |
| STAC-specific deployment comparison guidance | [`./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md`](./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md) |
| operational procedures, rollback playbooks, or correction runbooks | [`../runbooks/README.md`](../runbooks/README.md) and the owning runbook |
| API endpoint schemas and machine contracts | [`../../contracts/`](../../contracts/) and [`../../schemas/contracts/`](../../schemas/contracts/) |
| executable policy bundles or Rego decision logic | [`../../policy/`](../../policy/) |
| fixtures, drills, negative-path cases, or proof packs | [`../../tests/`](../../tests/) |
| domain ETL instructions or source-specific runbooks | domain / runbook / owning code surface |
| exploratory notes, research digests, or idea packets | research / idea / planning surface |

> [!NOTE]
> A good rule of thumb: if the file is primarily **normative across multiple domains**, it likely belongs here. If it is primarily **machine-facing**, **operational**, **domain-specific**, or already owned by a dedicated downstream file, it probably does not belong in this index.

[Back to top](#top)

---

## Directory tree

The tree below reflects the files directly verified on current public `main` for this revision.

```text
docs/standards/
├── README.md
├── KFM_DCAT_PROFILE.md
├── KFM_MARKDOWN_WORK_PROTOCOL.md
├── KFM_PROV_PROFILE.md
├── KFM_STAC_PROFILE.md
├── markdown-rules.md
├── faircare/
│   ├── FAIRCARE-GUIDE.md
│   └── README.md
├── governance/
│   ├── README.md
│   └── ROOT_GOVERNANCE.md
├── sovereignty/
│   ├── INDIGENOUS-DATA-PROTECTION.md
│   └── README.md
└── stac/
    ├── OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md
    └── README.md
```

> [!CAUTION]
> The tree above is a **public-main snapshot**, not a guarantee about the branch under review. Re-open the working checkout before merge and update this index if the lane changed again.

[Back to top](#top)

---

## Quickstart

### 1) Find the owning surface first

Use this index as a router, then move to the owning file:

1. For outward item/asset discovery rules, go to [`KFM_STAC_PROFILE.md`](./KFM_STAC_PROFILE.md).
2. For outward dataset/distribution discovery rules, go to [`KFM_DCAT_PROFILE.md`](./KFM_DCAT_PROFILE.md).
3. For publication lineage rules, go to [`KFM_PROV_PROFILE.md`](./KFM_PROV_PROFILE.md).
4. For normative Markdown authoring and review rules, go to [`KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md).
5. For a visible repo-local Markdown task brief that may affect how AI-assisted editing is framed, check [`markdown-rules.md`](./markdown-rules.md) — but do not let it silently outrank the normative protocol.
6. For governance lane routing, start with [`governance/README.md`](./governance/README.md); for cross-domain governance law, go to [`governance/ROOT_GOVERNANCE.md`](./governance/ROOT_GOVERNANCE.md).
7. For FAIR+CARE lane routing, start with [`faircare/README.md`](./faircare/README.md); for substantive FAIR+CARE guidance, go to [`faircare/FAIRCARE-GUIDE.md`](./faircare/FAIRCARE-GUIDE.md).
8. For sovereignty lane routing, start with [`sovereignty/README.md`](./sovereignty/README.md); for substantive sovereignty rules, go to [`sovereignty/INDIGENOUS-DATA-PROTECTION.md`](./sovereignty/INDIGENOUS-DATA-PROTECTION.md).
9. For STAC-specific support notes beneath the main profile, start with [`stac/README.md`](./stac/README.md) and then use [`stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md`](./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md).

### 2) If the change touches contracts or schemas

Before editing standards text that references machine-facing surfaces:

1. reopen [`../../contracts/README.md`](../../contracts/README.md)
2. reopen [`../../contracts/vocab/README.md`](../../contracts/vocab/README.md)
3. reopen [`../../schemas/README.md`](../../schemas/README.md)
4. reopen [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md)
5. reopen [`../../tests/contracts/README.md`](../../tests/contracts/README.md)
6. reopen [`../../tests/e2e/runtime_proof/`](../../tests/e2e/runtime_proof/) or its nearest README / proof family surface
7. confirm whether the branch has **explicitly** resolved canonical machine-contract home

If not, route conservatively and avoid adding new trust-bearing family guidance.

### 3) Add or revise a standard

1. Confirm the document is **normative**, not exploratory.
2. Check whether an existing root file, lane README, or downstream standard already owns the rule.
3. If the right file already exists, **revise it in place** instead of creating a second file with overlapping authority.
4. If a lane-local README and a downstream standard both exist, decide explicitly which one owns:
   - routing and exclusions, or
   - substantive rule text.
5. Re-check neighboring machine-facing and operational surfaces:
   - [`../../contracts/README.md`](../../contracts/README.md)
   - [`../../contracts/vocab/README.md`](../../contracts/vocab/README.md)
   - [`../../schemas/README.md`](../../schemas/README.md)
   - [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md)
   - [`../../schemas/contracts/v1/README.md`](../../schemas/contracts/v1/README.md)
   - [`../../policy/README.md`](../../policy/README.md)
   - [`../../tests/README.md`](../../tests/README.md)
   - [`../../tests/contracts/README.md`](../../tests/contracts/README.md)
   - [`../../tests/e2e/runtime_proof/`](../../tests/e2e/runtime_proof/)
   - [`../../.github/workflows/README.md`](../../.github/workflows/README.md)
   - [`../runbooks/README.md`](../runbooks/README.md)
6. Update this index whenever the standards surface, routing split, or maturity snapshot changes.

### 4) Minimal authoring skeleton

```md
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/REVIEW_REQUIRED_UUID
title: <Standard title>
type: standard
version: v1
status: draft
owners: REVIEW_REQUIRED_OWNER
created: REVIEW_REQUIRED_DATE
updated: REVIEW_REQUIRED_DATE
policy_label: REVIEW_REQUIRED_POLICY_LABEL
related: [<relative paths or kfm:// ids>]
tags: [kfm, standards]
notes: [<reviewable notes>]
[/KFM_META_BLOCK_V2] -->

# <Standard title>

_One-line purpose._

> [!IMPORTANT]
> State the truth boundary up front. Do not silently upgrade unknown repo state into implementation fact.

## Scope

## Repo fit

## Requirements

## Validation

## Related standards

## Open verification
```

### 5) Merge-time review prompts

- Does this change define a cross-cutting rule, or is it really a lane-local note?
- Does an existing root file, lane README, or downstream standard already own the rule?
- Did the change keep `markdown-rules.md` and `KFM_MARKDOWN_WORK_PROTOCOL.md` aligned where both still apply?
- Did the change point to the contracts, schema, policy, tests, runtime-proof, workflows, or runbooks it expects?
- Did it preserve KFM’s evidence-first, fail-closed, and correction-visible posture?
- Did it avoid choosing machine-contract authority by implication?

[Back to top](#top)

---

## Usage

### For maintainers

Use this directory to keep shared rules centralized and reviewable. The strongest current public-main shape is now **three-layered**:

1. the root standards index (`README.md`)
2. root-level standard/protocol files
3. lane-local directory READMEs plus their downstream standards or notes

Keep those layers synchronized without letting any one of them become a second silent authority source.

### For domain stewards

Reference standards from your domain docs. Do not copy them into domain READMEs unless the local adaptation itself must be governed, reviewed, and versioned as a distinct rule.

When a local question is really about procedure rather than norm text, route it to [`../runbooks/README.md`](../runbooks/README.md) instead of stretching standards prose to cover operational steps.

### For contributors

Start here when you need to answer questions like these:

- Which metadata profile applies to this published artifact?
- Where do publication lineage rules live?
- Is this change a lane-local README edit or a downstream standard edit?
- Which Markdown protocol should a governed README or standard follow?
- Is `markdown-rules.md` the brief I should read for this task, or do I need the normative protocol file?
- Which current files are real standards, which are lane-local routing surfaces, and which are still README-only support lanes?
- Has the repo actually resolved contract-home authority, or do I need to route conservatively?

### For reviewers

Reject changes that do any of the following:

- imply that new machine-contract families can safely land in both `contracts/` and `schemas/contracts/`
- let standards text silently upgrade an unresolved path into canonical authority
- let runtime-proof tests or examples invent private outcome grammar, envelope shapes, or vocabulary families
- duplicate lane-owned or downstream rule text without an explicit reason
- downgrade a substantive standards file back to “scaffold” language without evidence

[Back to top](#top)

---

## Diagram

```mermaid
flowchart LR
    IDX[docs/standards/README.md]

    IDX --> STACP[KFM_STAC_PROFILE.md]
    IDX --> DCATP[KFM_DCAT_PROFILE.md]
    IDX --> PROVP[KFM_PROV_PROFILE.md]
    IDX --> MDP[KFM_MARKDOWN_WORK_PROTOCOL.md]
    IDX --> MR[markdown-rules.md]

    IDX --> GOVR[governance/README.md]
    GOVR --> GOVSTD[governance/ROOT_GOVERNANCE.md]

    IDX --> FAIRR[faircare/README.md]
    FAIRR --> FAIRG[faircare/FAIRCARE-GUIDE.md]

    IDX --> SOVR[sovereignty/README.md]
    SOVR --> SOVSTD[sovereignty/INDIGENOUS-DATA-PROTECTION.md]

    IDX --> STACR[stac/README.md]
    STACR --> STACNOTE[stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md]

    STACP --> CLOSURE[CatalogClosure / published discovery]
    DCATP --> CLOSURE
    PROVP --> CLOSURE

    GOVSTD -.review / release / correction law.-> CLOSURE
    FAIRG -.rights / care / redaction.-> CLOSURE
    SOVSTD -.sovereignty / precision controls.-> CLOSURE

    MDP -.normative authoring law.-> DOCS[repo-authored Markdown]
    MR -.task-facing brief when present.-> DOCS

    CONTRACTS[../../contracts/README.md] -.human-readable machine-contract guidance.-> CLOSURE
    CVOCAB[../../contracts/vocab/README.md] -.shared vocab guidance.-> CLOSURE
    SCHEMAS[../../schemas/README.md] -.boundary / authority split.-> CONTRACTS
    SCON[../../schemas/contracts/README.md] -.machine-file subtree.-> CONTRACTS
    POLICY[../../policy/README.md] -.deny-by-default rules.-> CLOSURE
    TESTS[../../tests/README.md] -.proof burdens.-> CLOSURE
    TCON[../../tests/contracts/README.md] -.contract verification.-> CLOSURE
    RTP[../../tests/e2e/runtime_proof/] -.consumes authoritative shapes only.-> CLOSURE
    WF[../../.github/workflows/README.md] -.automation gates when implemented.-> CLOSURE
    RUNBOOKS[../runbooks/README.md] -.operational procedures.-> CLOSURE
```

[Back to top](#top)

---

## Standards map

This section separates **root-level standard files** from **lane-local routing surfaces** so the index stays truthful as the tree matures.

### Root-level standards and protocol files

| Surface | Primary role | Current public `main` state | Routing consequence |
|---|---|---|---|
| [`README.md`](./README.md) | root standards index and routing surface | present; substantive directory index | revise in place when the visible standards tree changes |
| [`KFM_STAC_PROFILE.md`](./KFM_STAC_PROFILE.md) | outward STAC profile for items, collections, assets, and catalog discovery | present; substantive draft standard | route STAC profile work here |
| [`KFM_DCAT_PROFILE.md`](./KFM_DCAT_PROFILE.md) | outward dataset/distribution discovery profile | present; substantive draft standard | route DCAT mapping and discovery obligations here |
| [`KFM_PROV_PROFILE.md`](./KFM_PROV_PROFILE.md) | outward provenance / lineage profile | present; substantive draft standard | route lineage and release-traceability work here |
| [`KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md) | governed Markdown authoring / revision / review protocol | present; substantive draft protocol | route normative Markdown rules here |
| [`markdown-rules.md`](./markdown-rules.md) | repo-local task-facing authoring brief / instruction mirror | present; visible current-tree file | keep it aligned to the protocol or consolidate explicitly; do not let it silently become second authority |

### Lane-local directory surfaces

| Lane | Primary role | Current public `main` state | Routing consequence |
|---|---|---|---|
| [`governance/README.md`](./governance/README.md) | governance lane index and scope boundary | present | use for lane routing, exclusions, and index-level edits |
| [`governance/ROOT_GOVERNANCE.md`](./governance/ROOT_GOVERNANCE.md) | standards-layer governance baseline | present; substantive draft standard | use for cross-domain governance rules |
| [`faircare/README.md`](./faircare/README.md) | FAIR+CARE lane index and scope boundary | present | use for lane routing and README-level scope control |
| [`faircare/FAIRCARE-GUIDE.md`](./faircare/FAIRCARE-GUIDE.md) | FAIR+CARE norm text | present; substantive guide | use for publication, redaction, stewardship, and reuse rules |
| [`sovereignty/README.md`](./sovereignty/README.md) | sovereignty lane index and scope boundary | present | use for lane routing and exclusions |
| [`sovereignty/INDIGENOUS-DATA-PROTECTION.md`](./sovereignty/INDIGENOUS-DATA-PROTECTION.md) | sovereignty / protected-knowledge standard | present; substantive draft standard | use for Indigenous/community-sensitive handling rules |
| [`stac/README.md`](./stac/README.md) | STAC-specific support lane index | present | use for STAC support-lane routing |
| [`stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md`](./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md) | STAC deployment/alignment note | present; substantive guidance note | use for STAC-specific interoperability and deployment comparison work |

### Machine-surface routing map

| Change type | Best home now | Standards note |
|---|---|---|
| contract meaning and family semantics | `../../contracts/` | route there, but do not imply canonical machine-home authority is settled |
| machine schema / enum enforcement | `../../schemas/` / `../../schemas/contracts/` | route there honestly; do not duplicate in prose |
| shared vocabulary semantics | `../../contracts/vocab/` | route there unless a later explicit decision changes ownership |
| policy-owned codes and obligations | `../../policy/` | standards may reference them, not own them |
| contract verification | `../../tests/contracts/` | tests should consume one authoritative path |
| request-time proof | `../../tests/e2e/runtime_proof/` | consumes authority; does not create it |

[Back to top](#top)

---

## Put-it-here test

| Candidate change | Belongs in `docs/standards/`? | Best home |
|---|---|---|
| new STAC field rule for outward Items | yes | [`./KFM_STAC_PROFILE.md`](./KFM_STAC_PROFILE.md) |
| STAC deployment or interoperability comparison note | yes | [`./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md`](./stac/OGC_STAC_COMMUNITY_STANDARD_AND_CDSE_DEPLOYMENTS.md) |
| new DCAT distribution-linkage rule | yes | [`./KFM_DCAT_PROFILE.md`](./KFM_DCAT_PROFILE.md) |
| new PROV entity/activity constraint | yes | [`./KFM_PROV_PROFILE.md`](./KFM_PROV_PROFILE.md) |
| new README metadata or Markdown review rule | yes | [`./KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md) |
| repo-local task-facing markdown brief already intentionally maintained in-tree | maybe | [`./markdown-rules.md`](./markdown-rules.md) — but keep it aligned to the normative protocol |
| governance lane routing or exclusions update | yes | [`./governance/README.md`](./governance/README.md) |
| new cross-domain governance rule | yes | [`./governance/ROOT_GOVERNANCE.md`](./governance/ROOT_GOVERNANCE.md) |
| FAIR+CARE lane routing update | yes | [`./faircare/README.md`](./faircare/README.md) |
| FAIR+CARE standards build-out | yes | [`./faircare/FAIRCARE-GUIDE.md`](./faircare/FAIRCARE-GUIDE.md) |
| sovereignty lane routing update | yes | [`./sovereignty/README.md`](./sovereignty/README.md) |
| Indigenous/community-sensitive release rule | yes | [`./sovereignty/INDIGENOUS-DATA-PROTECTION.md`](./sovereignty/INDIGENOUS-DATA-PROTECTION.md) |
| shared machine vocabulary semantics | no | [`../../contracts/vocab/README.md`](../../contracts/vocab/README.md) |
| API request/response schema | no | [`../../contracts/`](../../contracts/) or [`../../schemas/contracts/`](../../schemas/contracts/) |
| Rego policy bundle or decision grammar | no | [`../../policy/`](../../policy/) |
| test fixtures, golden files, or failure drills | no | [`../../tests/`](../../tests/) |
| runtime-proof outcome fixture or request-time envelope example | no | [`../../tests/e2e/runtime_proof/`](../../tests/e2e/runtime_proof/) |
| publication / rollback / correction procedure | no | [`../runbooks/README.md`](../runbooks/README.md) and the owning runbook |
| domain ingest runbook | no | domain / runbook / owning code surface |
| exploratory note or literature digest | no | research / idea / planning surface |

[Back to top](#top)

---

## Definition of done

A standards doc is ready to merge when all of the following are true:

- [ ] path and title align with the document’s actual role
- [ ] scope is explicit and excludes material that belongs elsewhere
- [ ] relative links resolve to the governing or downstream files it names
- [ ] the change lands in the owning root file, lane README, or downstream standard if one already exists
- [ ] contracts, schemas, vocab, policy, tests, runtime-proof, workflow, and runbook touchpoints are referenced where relevant
- [ ] draft / experimental / unknown state is visible
- [ ] the file does not silently create second authority beside a stronger neighboring surface
- [ ] if the standard affects sensitive or public outputs, review triggers are explicit
- [ ] this index is updated if the standards surface, lane routing, or maturity snapshot changed

### Review checklist for this index

- [ ] the `Current public standards surface` section still matches the target branch
- [ ] `markdown-rules.md` is still present, or this file has been updated to reflect its removal or relocation
- [ ] lane-local README files under `governance/`, `faircare/`, `sovereignty/`, and `stac/` are still accurately represented
- [ ] [`faircare/FAIRCARE-GUIDE.md`](./faircare/FAIRCARE-GUIDE.md) is still described accurately and is **not** silently downgraded back to scaffold-only
- [ ] `.github/CODEOWNERS` still supports the owner line used here
- [ ] `.github/workflows/README.md` is still README-only on the target branch, or this file has been updated to reflect checked-in workflow YAML
- [ ] `contracts/README.md`, `contracts/vocab/README.md`, `schemas/README.md`, and `schemas/contracts/README.md` still reflect the current authority split, or this file has been updated to match
- [ ] runtime-proof references still consume rather than redefine upstream authority
- [ ] meta-block placeholders have been replaced or intentionally retained

[Back to top](#top)

---

## FAQ

### Is this directory only for metadata standards?

No. Metadata profiles are central here, but the directory also covers governance, Markdown protocol, FAIR+CARE, sovereignty handling, and other shared normative rules that multiple KFM lanes depend on.

### Do standards replace contracts, schemas, or policy?

No. Standards explain the rule set. Contracts and schemas are the machine-facing artifacts that implement or validate those rules, and policy is the executable decision layer that enforces them.

### Does this file decide whether `contracts/` or `schemas/contracts/` is canonical?

No. This README now makes that unresolved state explicit. It may route to both surfaces to describe current reality, but it must not quietly decide the winner.

### Is `FAIRCARE-GUIDE.md` still scaffold-only?

No. Not on the current public-main snapshot used for this revision. The FAIR+CARE lane now has both a lane-local `README.md` and a substantive [`FAIRCARE-GUIDE.md`](./faircare/FAIRCARE-GUIDE.md).

### What is `markdown-rules.md` relative to `KFM_MARKDOWN_WORK_PROTOCOL.md`?

`markdown-rules.md` is a visible repo-local authoring brief. [`KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md) remains the normative standards-layer Markdown protocol unless the active branch explicitly changes that relationship.

### Should runtime-proof tests define their own outcome grammar or envelope vocabulary?

No. Runtime-proof should prove governed behavior using authoritative upstream shapes and vocabularies. If it needs a new value or field, that change should be made in the owning upstream surface first.

### Should lane-local READMEs repeat their child standards?

No. Lane-local READMEs should define lane scope, routing, exclusions, and ownership boundaries. The downstream standard or note should carry the substantive rule text.

### What should happen if a proposed standard conflicts with a stronger KFM doctrine doc?

The stronger governing doctrine wins. Update the proposal, or document the conflict and route it for review instead of letting drift land quietly.

[Back to top](#top)

---

## Appendix

<details>
<summary><strong>Known verification items</strong></summary>

### Repo-state items still needing direct verification

- final UUID and commit-time `created` / `updated` dates for this document
- whether a narrower `/docs/standards/` CODEOWNERS rule should replace the current `/docs/` fallback owner
- whether `.github/workflows/` remains README-only on the target merge branch
- which tests or CI commands actually enforce standards-related validation, if any
- whether `markdown-rules.md` is a deliberate long-term repo surface or a transitional task brief that should be folded elsewhere
- whether any lane-local README should be collapsed into its downstream standard or kept as a distinct routing surface
- whether any standards doc here is using a documented exception to KFM Meta Block v2
- whether the branch under review has explicitly resolved canonical machine-contract authority
- what exact leaf inventory currently exists under `tests/e2e/runtime_proof/`

### Authoring notes for future maintainers

- keep this file as a **root index and routing surface**, not a second copy of downstream rule text
- when a root file, lane README, or downstream standard changes maturity or role, update this README in the same change stream
- do not call a substantive guide a scaffold, and do not call a task brief a normative standard without explicitly resolving the authority split
- sync this file with [`../README.md`](../README.md), [`../runbooks/README.md`](../runbooks/README.md), [`../../contracts/README.md`](../../contracts/README.md), [`../../contracts/vocab/README.md`](../../contracts/vocab/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../policy/README.md`](../../policy/README.md), [`../../tests/README.md`](../../tests/README.md), [`../../tests/contracts/README.md`](../../tests/contracts/README.md), [`../../tests/e2e/runtime_proof/`](../../tests/e2e/runtime_proof/), and [`../../.github/workflows/README.md`](../../.github/workflows/README.md) when boundaries move
- use reviewable placeholders when metadata is not confirmed; do not silently guess
- prefer one owning surface per rule family over overlapping duplicates
- do not let this file normalize unresolved duplication as stable architecture

</details>

<details>
<summary><strong>Temporary authority shorthand</strong></summary>

Until the repo resolves the machine-facing split explicitly, keep this shorthand in mind:

- **standards** explain shared norm text
- **contracts** explain object meaning
- **schemas** enforce machine shape
- **policy** decides allow / deny / obligations
- **tests/contracts** verify contract-facing behavior
- **runtime-proof** proves request-time behavior using authoritative upstream shapes
- **workflows** orchestrate checks and gates

If one change tries to do all of these at once, it needs to be split.

</details>

[Back to top](#top)
