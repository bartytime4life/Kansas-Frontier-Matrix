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
notes: [owners and created date need direct repo confirmation; updated date preserved from supplied baseline; related paths and child-lane depth should be rechecked against mounted repo tree before merge]
[/KFM_META_BLOCK_V2] -->

# KFM Research — README

Research workspace for exploratory notes, source summaries, evaluations, and de-risking work that inform Kansas Frontier Matrix without becoming governed truth by default.

> **Status:** experimental  
> **Owners:** NEEDS VERIFICATION  
> **Source posture:** doctrine-grounded and baseline-preserving; exact repo-tree parity still needs verification  
> **Repo role:** root README for the `docs/research/` subtree  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Promotion rules](#promotion-rules) · [Definition of done](#definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

![Status: Experimental](https://img.shields.io/badge/status-experimental-7a3cff)
![Doc: Root README](https://img.shields.io/badge/doc-root%20README-0a7ea4)
![Scope: Non-normative](https://img.shields.io/badge/scope-non--normative-6c757d)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aware-ff8c00)
![Promotion Required](https://img.shields.io/badge/promotion-required-c0392b)

> [!IMPORTANT]
> Content in `docs/research/` is **exploratory and non-normative until promoted**. Research here can inform governed contracts, schemas, pipelines, Story Nodes, UI behavior, and Focus Mode, but it does **not** define them in this subtree.

## Scope

`docs/research/` is the working surface for exploratory, evidence-led documentation that helps KFM contributors reduce uncertainty before promoting work into governed artifacts.

Use this area for:

- literature notes
- trade studies
- prototype writeups
- benchmark and evaluation summaries
- structured source summaries
- design spikes that still need narrowing, review, or promotion
- risk registers and “what to verify next” notes that keep uncertainty visible

Do **not** treat this directory as the home for:

- authoritative governance policy
- API contracts
- schema definitions
- release notes
- production runbooks
- public-facing Story Node rules
- uncited Focus Mode behavior

## Repo fit

This file is the subtree contract for `docs/research/`. Its job is to route contributors into the right lane, make the non-normative boundary explicit, and prevent exploratory material from being mistaken for governed KFM doctrine.

| Item | Value |
|---|---|
| Path | `docs/research/README.md` |
| Role | Root README for the `docs/research/` subtree |
| Upstream | [`../`](../) · [`../governance/ROOT_GOVERNANCE.md`](../governance/ROOT_GOVERNANCE.md) · [`../governance/ETHICS.md`](../governance/ETHICS.md) · [`../governance/SOVEREIGNTY.md`](../governance/SOVEREIGNTY.md) |
| Downstream | [`./drafts/README.md`](./drafts/README.md) · [`./evaluations/README.md`](./evaluations/README.md) · [`./source_summaries/README.md`](./source_summaries/README.md) |
| Representative child lanes | [`./drafts/literature/README.md`](./drafts/literature/README.md) · [`./drafts/assets/README.md`](./drafts/assets/README.md) · [`./evaluations/assets/README.md`](./evaluations/assets/README.md) · [`./source_summaries/by_type/README.md`](./source_summaries/by_type/README.md) · [`./source_summaries/by_domain/README.md`](./source_summaries/by_domain/README.md) · [`./source_summaries/_attachments/README.md`](./source_summaries/_attachments/README.md) |
| Promotion destinations | Governed docs, templates, schemas, subsystem docs, Story Node pathways, and implementation work after review |
| Verification posture | Representative structure only; exact mounted path population and child-lane depth need verification |

> [!NOTE]
> **CONFIRMED:** research content here is non-normative until promoted.  
> **INFERRED:** the subtree centers on `drafts/`, `evaluations/`, and `source_summaries/`.  
> **NEEDS VERIFICATION:** owners, created date, exact mounted repo paths, and current child README parity.

## Accepted inputs

Accepted here:

- exploratory notes with a clear research question
- literature reviews and bibliographic summaries
- design spikes that compare options without declaring policy
- evaluation writeups with reproducible inputs, methods, and outcomes
- benchmark notes and measurement summaries
- structured summaries of external books, papers, datasets, maps, and web sources
- research backlogs, open questions, and scoped unknowns lists

## Exclusions

Do **not** put these here:

- final governance policies or standards
- API contracts or route guarantees
- canonical schema definitions
- release manifests or production receipts
- secrets, credentials, tokens, private keys, or private communications
- raw or derived datasets that belong under `data/`
- experimental runtime artifacts that belong under `mcp/`
- public narrative intended for Story Nodes or Focus Mode before promotion
- precise sensitive locations, culturally sensitive directions, or restricted site disclosure
- anything that depends on sensitive-location inference

## Directory tree

Representative subtree shape for this area:

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
> Treat this as a **representative** research layout, not a claim that every child path has been reverified in the mounted repo tree. Keep the structure shallow, legible, and lane-based.

## Quickstart

1. Put **early or uncertain work** in `./drafts/`.
2. Put **repeatable comparison or measurement work** in `./evaluations/`.
3. Put **one-source structured summaries** in `./source_summaries/`.
4. Keep sources, dates, and scope visible from the start.
5. Promote anything normative before it is treated as a contract, UI rule, Story Node, or Focus input.

## Usage

### Choose the right lane

| Lane | Use it for | Typical outputs | Do not use it for |
|---|---|---|---|
| `drafts/` | Early-stage thinking and open questions | trade studies, design notes, experiment plans, literature notes | authoritative policy, public narrative, final API behavior |
| `evaluations/` | Repeatable measurement and comparison work | benchmarks, QA summaries, result deltas, reproducible evaluation notes | raw datasets, production how-to docs, brainstorming |
| `source_summaries/` | Structured summaries of external sources | one-source markdown summaries, candidate entities, ingestion notes, attachments | ETL implementation, large copyrighted copies, uncited public claims |

### Write with KFM discipline

Research documents here should still behave like responsible KFM artifacts:

- state the question
- identify the sources
- use KFM truth labels when precision matters: **CONFIRMED**, **INFERRED**, **PROPOSED**, **UNKNOWN**, **NEEDS VERIFICATION**
- record evidence links, IDs, or provenance references where available
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

### Promotion should carry a named destination

When research work leaves this subtree, name the next governed home explicitly. “We should do this later” is not enough when the artifact is becoming behavior-significant.

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

### KFM truth labels

Use explicit labels when precision matters:

- **CONFIRMED**: directly supported by visible project evidence or cited source material
- **INFERRED**: a conservative interpretation supported by the evidence, but not a claim of mounted implementation
- **PROPOSED**: a recommended next step, design direction, or promotion path
- **UNKNOWN**: not supported strongly enough in the current evidence base
- **NEEDS VERIFICATION**: a specific point that should be rechecked before merge, promotion, or release

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

Research can inform the canonical KFM flow, but it does not bypass it.

`Research -> review -> promotion -> governed artifact -> implementation / surface use`

</details>

<details>
<summary><strong>Known verification gaps for this README</strong></summary>

This README is grounded in the supplied research baseline plus attached March 2026 KFM materials, but several details still need direct repo verification:

- exact owners or CODEOWNERS coverage for `docs/research/`
- exact creation date for this file
- exact mounted presence and depth of every linked child README
- whether additional research lanes now exist beyond the representative structure shown here
- whether linked governance files still exist at the exact relative paths used above

</details>

[Back to top](#kfm-research--readme)
