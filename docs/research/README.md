<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: KFM Research — README
type: standard
version: v1
status: draft
owners: NEEDS VERIFICATION
created: YYYY-MM-DD
updated: 2025-12-20
policy_label: public
related: [docs/research/drafts/README.md, docs/research/evaluations/README.md, docs/research/source_summaries/README.md, docs/governance/ROOT_GOVERNANCE.md]
tags: [kfm, research, governance, docs]
notes: [updated date confirmed from repo support inventory preserved in the mounted corpus; current branch-visible root research README verified; created date and owners still need direct repo confirmation; child-lane depth varies in the current branch]
[/KFM_META_BLOCK_V2] -->

# KFM Research — README

Research workspace for exploratory notes, source summaries, evaluations, and de-risking work that inform Kansas Frontier Matrix without becoming governed truth by default.

> **Status:** experimental  
> **Owners:** NEEDS VERIFICATION  
> **Source posture:** repo-grounded root research guide aligned to the current branch-visible research README and March 2026 KFM doctrine  
> **Repo role:** root README for the `docs/research/` subtree  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Promotion rules](#promotion-rules) · [Definition of done](#definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

![Status: Experimental](https://img.shields.io/badge/status-experimental-7a3cff)
![Doc: Research Guide](https://img.shields.io/badge/doc-research%20guide-0a7ea4)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aware-ff8c00)
![Scope: Non-normative](https://img.shields.io/badge/scope-non--normative-6c757d)

> [!IMPORTANT]
> Content in `docs/research/` is **non-normative until promoted**. Research may inform KFM contracts, schemas, pipelines, Story Nodes, UI behavior, and Focus Mode, but it does **not** define them here.

## Scope

`docs/research/` is the working surface for exploratory, evidence-led documentation that helps KFM contributors reduce uncertainty before promoting work into governed artifacts.

Use this area for:

- literature notes
- trade studies
- prototype writeups
- benchmark and evaluation summaries
- structured source summaries
- design spikes that still need review, narrowing, or promotion

Do **not** treat this directory as the home for:

- authoritative governance policy
- API contracts
- schema definitions
- release notes
- production runbooks
- public-facing Story Node rules
- uncited Focus Mode behavior

## Repo fit

This file is the root contract for the research subtree. Its job is to route contributors into the right lane, make the non-normative boundary explicit, and prevent exploratory material from being mistaken for governed KFM doctrine.

| Item | Value |
|---|---|
| Path | `docs/research/README.md` |
| Upstream | [`../`](../) · [`../governance/ROOT_GOVERNANCE.md`](../governance/ROOT_GOVERNANCE.md) · [`../governance/ETHICS.md`](../governance/ETHICS.md) · [`../governance/SOVEREIGNTY.md`](../governance/SOVEREIGNTY.md) |
| Downstream | [`./drafts/README.md`](./drafts/README.md) · [`./evaluations/README.md`](./evaluations/README.md) · [`./source_summaries/README.md`](./source_summaries/README.md) |
| Supporting lanes | [`./drafts/literature/README.md`](./drafts/literature/README.md) · [`./source_summaries/by_type/README.md`](./source_summaries/by_type/README.md) · [`./source_summaries/by_domain/README.md`](./source_summaries/by_domain/README.md) · [`./source_summaries/_attachments/README.md`](./source_summaries/_attachments/README.md) |
| Promotion destinations | Governed docs, templates, schemas, subsystem docs, Story Node pathways, and implementation work after review |
| Current branch signal | This root README is live in the current branch. Verify child-lane depth before assuming every linked README has reached the same maturity. |

> [!NOTE]
> **Current branch signal (CONFIRMED):** this root README is live in the current branch.  
> **Current subtree maturity (NEEDS VERIFICATION):** linked lanes are part of the documented research structure, but child READMEs do not all yet appear to have equal depth. Use this file as the subtree contract, then inspect the target lane before assuming parity.

## Accepted inputs

Accepted here:

- exploratory notes with a clear research question
- literature reviews and bibliographic summaries
- design spikes that compare options without declaring policy
- evaluation writeups with reproducible inputs, methods, and outcomes
- benchmark notes and measurement summaries
- structured summaries of external books, papers, datasets, maps, and web sources
- “what to verify next” notes that clearly separate fact, inference, and hypothesis

## Exclusions

Do **not** put these here:

- final governance policies or standards
- API contracts or route guarantees
- canonical schema definitions
- release manifests or production receipts
- secrets, credentials, private keys, or private communications
- raw or derived datasets that belong under `data/`
- public narrative intended for Story Nodes or Focus Mode before promotion
- precise sensitive locations, culturally sensitive directions, or restricted site disclosure
- implementation changes that should land first as governed subsystem docs or tests

## Directory tree

Representative README-bearing structure for this subtree:

~~~text
docs/research/
├── README.md
├── drafts/
│   ├── README.md
│   ├── assets/
│   │   └── README.md
│   └── literature/
│       └── README.md
├── evaluations/
│   ├── README.md
│   └── assets/
│       └── README.md
└── source_summaries/
    ├── README.md
    ├── _attachments/
    │   └── README.md
    ├── by_domain/
    │   └── README.md
    └── by_type/
        └── README.md
~~~

> [!NOTE]
> Research structure should stay easy to scan. Prefer a small number of clearly named lanes over a deep maze of ad hoc folders.

## Quickstart

1. Put **early or uncertain work** in `./drafts/`.
2. Put **repeatable measurement or comparison work** in `./evaluations/`.
3. Put **one-source structured summaries** in `./source_summaries/`.
4. Link evidence clearly, separate claims from interpretation, and note sensitivity early.
5. Promote anything normative before it is treated as a contract, UI rule, Story Node, or Focus Mode input.

## Usage

### Choose the right lane

| Lane | Use it for | Typical outputs | Do not use it for |
|---|---|---|---|
| `drafts/` | Early-stage thinking and open questions | trade studies, design notes, experiment plans, literature notes | authoritative policy, public narrative, final API behavior |
| `evaluations/` | Repeatable measurement and governed summaries | benchmarks, QA summaries, result deltas, reproducible evaluation notes | raw datasets, production how-to docs, brainstorming |
| `source_summaries/` | Structured summaries of external sources | one-source markdown summaries, candidate entities, ingestion notes, attachments | ETL implementation, large copyrighted copies, uncited public claims |

### Write with KFM discipline

Research documents here should still behave like responsible KFM artifacts:

- state the question
- identify sources
- separate **fact**, **inference**, and **hypothesis**
- record relevant IDs, datasets, or provenance references when available
- call out rights, sensitivity, and redaction needs early
- avoid turning exploratory language into system policy by accident

### Promote when the work stops being exploratory

Once a research artifact starts defining system behavior, it has crossed the boundary.

| If the work becomes… | It belongs in… |
|---|---|
| a rule or standard | governed docs under `docs/` / governance destinations |
| a schema or machine-checked contract | `schemas/` plus the appropriate governed doc |
| an API change | governed API contract docs and tests |
| a UI or product behavior | subsystem docs and implementation review |
| a provenance-linked public narrative | Story Node / approved narrative pathway |
| a pipeline or ingestion obligation | subsystem docs, pipeline specs, and implementation work |

## Diagram

~~~mermaid
flowchart TD
    A[Research question or source] --> B[Drafts]
    A --> C[Source summaries]
    A --> D[Evaluations]

    B --> E{Ready to promote?}
    C --> E
    D --> E

    E -- No --> F[Remain exploratory / non-normative]
    E -- Yes --> G[Governed docs / standards]
    E -- Yes --> H[Schemas / contracts]
    E -- Yes --> I[Subsystem docs / implementation]
    E -- Yes --> J[Story Node candidate]

    G --> K[Approved internal or public surfaces]
    H --> K
    I --> K
    J --> K

    K --> L[Map / dossier / story / Focus Mode only after governed promotion]
~~~

## Promotion rules

### Promotion is required before public or runtime use

Research notes do **not** surface directly in Focus Mode. Draft content does **not** become public narrative merely because it is well written. Exploratory findings do **not** become contracts merely because they are plausible.

Use this rule of thumb:

| Question | If the answer is “yes”… |
|---|---|
| Does this text define a behavior others must follow? | Promote it |
| Does this change what the UI, API, or pipeline must do? | Promote it |
| Does this introduce a new identifier, contract, or schema obligation? | Promote it |
| Would a reader mistake this for KFM policy or authoritative truth? | Promote it |
| Is this intended for Story Node or Focus Mode use? | Promote it before use |

## Definition of done

A research artifact in this subtree is in good shape when:

- [ ] the question or purpose is explicit
- [ ] sources are identifiable
- [ ] key claims are separated from interpretation
- [ ] evidence links, IDs, or next actions are recorded where possible
- [ ] sensitivity and redaction concerns are called out
- [ ] no secrets, credentials, or private communications are included
- [ ] public narrative has **not** been implied without promotion
- [ ] the intended promotion target is named when the work becomes normative

## FAQ

### Is `docs/research/` authoritative?

No. It is intentionally exploratory. Authoritative material belongs in governed destinations after promotion and review.

### Can research notes be cited in Focus Mode?

Not directly. They can inform later governed artifacts, but they should not be treated as runtime truth surfaces on their own.

### Where should structured external-source summaries go?

Use `./source_summaries/`, then route by subtype as needed through `by_type/`, `by_domain/`, and `_attachments/`.

### Where do benchmarks or QA writeups belong?

Use `./evaluations/` when the work is repeatable, provenance-linked, and meant to support go/no-go judgment.

### What if a research note proposes a schema, API, or Story change?

Keep the exploratory reasoning here, but promote the actual normative artifact into its governed destination.

## Appendix

<details>
<summary><strong>Research writing guardrails</strong></summary>

### Fact, inference, hypothesis

Use explicit distinctions when precision matters:

- **Fact**: directly supported by the cited source or by project evidence
- **Inference**: reasoned interpretation drawn from that evidence
- **Hypothesis**: something worth testing, not yet established

### Provenance posture

When research work produces a candidate artifact that may later become part of KFM, record enough context to support promotion:

- source identifiers
- relevant dataset or asset references
- intended STAC / DCAT / PROV implications
- next action, ticket, or promotion target
- sensitivity or rights notes

### Sensitivity and redaction

When in doubt:

- generalize coordinates
- avoid precise protected-site guidance
- avoid reproducing large copyrighted material
- flag cultural, tribal, or sovereignty-sensitive content early
- move cautiously rather than polishing uncertainty away

### Relationship to the canonical flow

Research can inform the canonical KFM pipeline, but it does not bypass it.

`Research -> review -> promotion -> governed artifact -> implementation / surface use`

</details>

<details>
<summary><strong>Known verification gaps for this README</strong></summary>

This README is grounded in current branch-visible repo evidence plus mounted KFM supporting materials, but several details still need direct verification:

- exact owners or CODEOWNERS coverage for `docs/research/`
- exact creation date for this file
- whether every linked child path is still populated beyond scaffold level in the active branch
- whether additional research lanes now exist beyond the representative structure shown here
- whether adjacent governance docs at linked paths have expanded beyond the minimal surfaces directly inspected for this revision

</details>

[Back to top](#kfm-research--readme)
