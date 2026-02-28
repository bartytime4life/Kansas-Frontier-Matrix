<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/da0ec916-85a3-49ed-a87c-ef1d499a2293
title: docs/templates
type: standard
version: v1
status: draft
owners: KFM Docs Maintainers
created: 2026-02-28
updated: 2026-02-28
policy_label: public
related:
  - docs/MASTER_GUIDE_v13.md
  - docs/glossary.md
tags: [kfm, docs, templates]
notes:
  - Directory README for governed document templates (Universal Doc, Story Node v3, API contract extension).
[/KFM_META_BLOCK_V2] -->

# docs/templates

> Governed document templates for Kansas Frontier Matrix (KFM): use these to create **consistent, evidence-first, policy-aware** docs.

![kfm](https://img.shields.io/badge/kfm-docs-blue)
![templates](https://img.shields.io/badge/templates-governed-purple)
![status](https://img.shields.io/badge/status-draft-orange)
![policy](https://img.shields.io/badge/policy-default--deny-red)

---

## Navigation

- [Purpose](#purpose)
- [Where this fits](#where-this-fits)
- [What lives here](#what-lives-here)
- [Templates in this directory](#templates-in-this-directory)
- [Directory tree](#directory-tree)
- [How to use a template](#how-to-use-a-template)
- [MetaBlock v2](#metablock-v2)
- [Template selection matrix](#template-selection-matrix)
- [Contribution rules](#contribution-rules)
- [FAQ](#faq)

---

## Purpose

This folder contains **KFM-governed Markdown templates**. The templates standardize:

- **Metadata** (via *MetaBlock v2* embedded as an HTML comment)
- **Traceability** (clear places to put EvidenceRefs / citations / artifacts)
- **Review readiness** (sections and checklists that map to governance gates)

> NOTE: Templates are **starter kits**, not final documents. Copy them into the correct docs location and fill in real content.

---

## Where this fits

Within the repository documentation tree:

- `docs/` is the home for canonical governed documentation (guides, designs, runbooks, etc.)
- `docs/templates/` is the home for the **template sources** (universal docs, story nodes, and API contract extensions)

---

## What lives here

✅ **Acceptable inputs**

- Markdown templates prefixed `TEMPLATE__...`
- Snippets that are reused across templates (optional), **if** they are clearly marked as snippets
- This `README.md`

🚫 **Exclusions (do not put these here)**

- Live architecture docs (put in `docs/architecture/`)
- ADRs (put in `docs/architecture/adr/`)
- Story Node content (put under `docs/reports/story_nodes/...`)
- Dataset specs or run receipts (store with their owning subsystem / pipeline outputs)

---

## Templates in this directory

> The filenames below are the **expected** core templates in this folder.

| Template | Use for | Output target | Notes |
|---|---|---|---|
| `TEMPLATE__KFM_UNIVERSAL_DOC.md` | Guides, standards, runbooks, design notes | `docs/...` | General-purpose “universal doc” skeleton |
| `TEMPLATE__STORY_NODE_V3.md` | Story Nodes (narrative + map state) | `docs/reports/story_nodes/...` | Story Nodes typically have **markdown + sidecar JSON** |
| `TEMPLATE__API_CONTRACT_EXTENSION.md` | API change notes that complement OpenAPI | `docs/...` (often near `contracts/`) | Captures rationale, compatibility, policy impact |

---

## Directory tree

```text
docs/templates/
├── README.md                          # This directory guide
├── TEMPLATE__KFM_UNIVERSAL_DOC.md      # Universal governed doc template
├── TEMPLATE__STORY_NODE_V3.md          # Story Node v3 markdown skeleton
└── TEMPLATE__API_CONTRACT_EXTENSION.md # API contract extension notes
```

If your local tree differs, treat the table above as the **minimum expected set** and update this README when adding/removing templates.

---

## How to use a template

1. **Pick the right template** (see the [selection matrix](#template-selection-matrix)).
2. **Copy it** into the destination folder (do *not* edit the template in place for one-off docs).
3. **Fill in MetaBlock v2** (doc_id is stable; updated changes on meaningful edits).
4. Replace placeholder sections with real content.
5. Add evidence: cite primary sources, link artifacts, and include explicit assumptions.

Example:

```bash
# Example: start a new architecture note from the Universal Doc template
cp docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md docs/architecture/my_topic.md
```

---

## MetaBlock v2

MetaBlock v2 is structured metadata **without YAML frontmatter**. In Markdown, keep it as an **HTML comment** so it doesn’t render, but remains machine-readable.

```text
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: <Title>
type: <guide|standard|story|dataset_spec|adr|run_receipt>
version: v1
status: draft|review|published
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - kfm://dataset/<slug>@<version>
  - kfm://story/<id>@<version>
tags:
  - kfm
notes:
  - <short notes>
[/KFM_META_BLOCK_V2] -->
```

**Practical rules**

- `doc_id` must be **stable** (don’t regenerate it on edits).
- `updated` should change on meaningful edits.
- `policy_label` should reflect the intended visibility *if docs are served through governed APIs*.

---

## Template selection matrix

Use this to choose the right starting point.

| If you are writing… | Start here | Why |
|---|---|---|
| A general guide, standard, runbook, or design note | `TEMPLATE__KFM_UNIVERSAL_DOC.md` | Most flexible and broadly applicable |
| A narrative that binds claims to map state + citations | `TEMPLATE__STORY_NODE_V3.md` | Story Nodes are “machine-ingestible storytelling” |
| A non-trivial API change and its implications | `TEMPLATE__API_CONTRACT_EXTENSION.md` | Captures rationale + compatibility + policy impact |

---

## Lifecycle diagram

```mermaid
flowchart TD
  A[Need a new doc] --> B[Select template]
  B --> C[Copy into correct repo location]
  C --> D[Fill MetaBlock v2]
  D --> E[Write content and attach evidence]
  E --> F[Run local checks]
  F --> G[Open PR]
  G --> H[Governance review gates]
  H --> I[Merge]
  I --> J[Publish or reference from Master Guide]
```

---

## Contribution rules

> WARNING: Templates are governance-critical. A change here affects how evidence, policy labels, and review gates get applied across the repo.

**When you change a template, you must:**

- [ ] Keep the template **generic** (no project-specific one-off content)
- [ ] Preserve MetaBlock v2 and keep placeholders obvious
- [ ] Update this `README.md` if you add/remove templates or rename files
- [ ] Add an example snippet if you introduce a new required field/section
- [ ] Ensure any new sections have clear “what to put here” instructions

**Recommended “Definition of Done” for template changes**

- [ ] Template has a clear purpose statement
- [ ] Template has a minimal, scannable structure (toc, sections, checklists)
- [ ] Template includes at least one example of an EvidenceRef/citation pattern
- [ ] Links are relative and repo-stable (no ephemeral URLs)

---

## FAQ

**Can I store a finished doc in `docs/templates/`?**  
No. Store finished docs where they belong (e.g., `docs/architecture/`, `docs/governance/`, `docs/reports/story_nodes/...`). This folder is for *templates only*.

**Do we use YAML frontmatter?**  
No. Use MetaBlock v2 (embedded as an HTML comment) so templates remain consistent and machine-parseable.

**What if I don’t see a template for my doc type?**  
Start from `TEMPLATE__KFM_UNIVERSAL_DOC.md`, then propose a new template only if the pattern is reusable across multiple docs.

---

[Back to top](#docstemplates)
