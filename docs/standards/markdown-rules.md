<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION
title: Markdown Rules (Authoring Brief)
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS_VERIFICATION
updated: 2026-04-14
policy_label: public
related: [
  ./KFM_MARKDOWN_WORK_PROTOCOL.md,
  ./README.md,
  ../README.md,
  ../../README.md,
  ../../.github/CODEOWNERS,
  ../../.github/PULL_REQUEST_TEMPLATE.md,
  ../../.github/workflows/README.md,
  ../../contracts/README.md,
  ../../schemas/README.md,
  ../../policy/README.md,
  ../../tests/README.md
]
tags: [kfm, markdown, authoring, standards, brief]
notes: [
  "This file is a task-facing Markdown authoring brief distinct from the normative KFM_MARKDOWN_WORK_PROTOCOL.md.",
  "doc_id, created date, and policy_label remain NEEDS VERIFICATION.",
  "Authority split between this file and the protocol is intentional and must remain explicit."
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `markdown-rules.md`

Concise, task-facing **Markdown authoring brief** for KFM contributors.

> [!NOTE]
> **Status:** experimental  
> **Document status:** draft  
> **Owners:** `@bartytime4life`  
> **Path:** `docs/standards/markdown-rules.md`  
> ![Status](https://img.shields.io/badge/status-experimental-orange) ![Doc](https://img.shields.io/badge/doc-draft-lightgrey) ![Surface](https://img.shields.io/badge/surface-authoring%20brief-0a7ea4) ![Truth](https://img.shields.io/badge/truth-aligned%20to%20protocol-6f42c1)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [When to use](#when-to-use-this-file) · [Rules](#core-markdown-rules) · [Formatting](#github-formatting-rules) · [Checklist](#quick-checklist) · [Boundaries](#authority-boundary) · [FAQ](#faq)

> [!IMPORTANT]
> This file is a **quick authoring brief**, not the normative standard.
>
> The authoritative rules live in:  
> 👉 [`KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md)

---

## Scope

This file provides a **fast, practical checklist** for writing or editing Markdown in KFM.

Use it when you need to:
- quickly align to repo style
- avoid common mistakes
- produce clean, reviewable Markdown without rereading the full protocol

Do **not** use this file to:
- define new standards
- override the protocol
- claim implementation or enforcement

[Back to top](#top)

---

## Repo fit

| Role | Description |
|---|---|
| This file | Task-facing authoring brief |
| Protocol | [`KFM_MARKDOWN_WORK_PROTOCOL.md`](./KFM_MARKDOWN_WORK_PROTOCOL.md) — normative authority |
| Index | [`README.md`](./README.md) — standards routing |
| Review surface | `.github/PULL_REQUEST_TEMPLATE.md` — truth-label and evidence expectations |

### Boundary rule

| Surface | Job |
|---|---|
| `markdown-rules.md` | quick how-to |
| `KFM_MARKDOWN_WORK_PROTOCOL.md` | what must be true |

[Back to top](#top)

---

## When to use this file

Use this brief when:

- writing or updating a README
- cleaning up formatting
- preparing a PR
- aligning to repo style quickly

Switch to the protocol when:

- defining standards
- making truth claims
- describing repo structure
- writing architecture or governance docs

---

## Core Markdown rules

### 1. One H1 only

```md
# Title
```

---

### 2. Start with purpose

```md
# File Name

Short one-line purpose.
```

---

### 3. Use sections intentionally

Prefer:

- Scope
- Repo fit
- Inputs
- Exclusions
- Usage
- Diagram
- Tables
- Task list

---

### 4. Keep paragraphs short

Avoid:

```
Huge blocks of text with no breaks
```

Prefer:

```
Short paragraphs.
Readable chunks.
```

---

### 5. Use tables when clarity improves

| Good | Bad |
|---|---|
| structured comparisons | dense prose dumps |

---

### 6. Label uncertainty

Use:

- **CONFIRMED**
- **INFERRED**
- **PROPOSED**
- **UNKNOWN**
- **NEEDS VERIFICATION**

---

### 7. Do not overclaim

Never say:

- “this is enforced” (unless proven)
- “CI guarantees this” (unless visible)
- “this exists” (without repo evidence)

---

### 8. Link instead of duplicating

Prefer:

```md
See [contracts/README.md](../../contracts/README.md)
```

Avoid rewriting authoritative content.

---

### 9. Keep boundaries explicit

Always show:

- what belongs here
- what belongs elsewhere

---

### 10. Docs must stay evidence-aligned

Docs are not marketing.  
Docs are not guesses.  
Docs are not aspirations.

Docs = **truth surfaces**.

---

## GitHub formatting rules

### Headings

- One `#`
- Clean hierarchy
- No decorative noise

---

### Lists

- bullets for concepts
- numbers for steps

---

### Code blocks

Always language-tagged:

```bash
command
```

```json
{ "example": true }
```

---

### Callouts

Use only:

- NOTE
- TIP
- IMPORTANT
- WARNING
- CAUTION

---

### Tables

Use when:

- comparing things
- listing rules
- clarifying structure

---

### Diagrams

Use Mermaid when structure matters:

```mermaid
flowchart LR
    A --> B
```

---

### Collapsible sections

```html
<details>
<summary>More</summary>

Hidden content.

</details>
```

---

### Navigation

Add quick jumps in long docs:

```md
**Quick jump:** [Scope](#scope) · [Usage](#usage)
```

---

## Quick checklist

Before committing:

- [ ] one H1 only
- [ ] purpose line present
- [ ] sections structured
- [ ] no large text walls
- [ ] truth labels used where needed
- [ ] links resolve
- [ ] no overclaiming
- [ ] diagram present (for README-like docs)
- [ ] boundaries explicit
- [ ] placeholders used for unknowns

---

## Authority boundary

| Do this | Not this |
|---|---|
| link to protocol | rewrite protocol |
| label unknowns | hide uncertainty |
| follow repo patterns | invent new ones |
| respect contracts/policy | override them in docs |
| use evidence | use assumptions |

---

## FAQ

### Is this the Markdown standard?

No.

👉 Use:
- this file = quick guide  
- protocol = real standard

---

### Can I change rules here?

Only if:

- it stays aligned with the protocol
- the protocol is updated **at the same time**

---

### What if rules conflict?

The protocol wins.

---

### Why keep both files?

Because:

- protocol = deep, authoritative
- this file = fast, usable

Removing one weakens the system.

---

## Appendix

<details>
<summary><strong>Short authoring pattern</strong></summary>

```text
1. Identify doc type
2. Inspect repo context
3. Write purpose
4. Add sections
5. Link to authority
6. Add diagram
7. Label uncertainty
8. Run checklist
```

</details>

[Back to top](#top)
