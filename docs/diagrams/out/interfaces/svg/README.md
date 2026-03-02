<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/a5d8fe66-a354-4c0d-a2ef-8227b3d5da07
title: Interface Diagrams (SVG)
type: standard
version: v1
status: draft
owners: TODO: set CODEOWNERS team (e.g., kfm-platform, kfm-architecture)
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/diagrams/src/interfaces/
  - docs/diagrams/out/interfaces/
tags: [kfm, diagrams, interfaces, svg]
notes:
  - This directory is intended to contain rendered SVG artifacts for interface/contract diagrams.
  - Do not edit SVGs by hand; edit the source diagram and re-render.
[/KFM_META_BLOCK_V2] -->

# Interface diagrams (SVG)

Rendered, versioned **interface/contract** diagrams in **SVG** format for use across KFM docs, architecture notes, and UI embeds.

![status](https://img.shields.io/badge/status-draft-lightgrey) ![format](https://img.shields.io/badge/format-SVG-blue) ![generated](https://img.shields.io/badge/artifact-generated-important) ![scope](https://img.shields.io/badge/scope-interfaces-informational)

> **TODO (repo wiring):** Replace/augment badges with real CI/status badges once the diagram build + link-check workflows are known.

## Quick navigation

- [What belongs here](#what-belongs-here)
- [What must NOT go here](#what-must-not-go-here)
- [Where this fits in the repo](#where-this-fits-in-the-repo)
- [Naming conventions](#naming-conventions)
- [How to add or update a diagram](#how-to-add-or-update-a-diagram)
- [Quality and governance checks](#quality-and-governance-checks)
- [Embedding SVGs in docs](#embedding-svgs-in-docs)
- [Appendix: SVG hygiene checklist](#appendix-svg-hygiene-checklist)

---

## What belongs here

**Acceptable inputs (expected):**
- **`*.svg`** files that are **rendered outputs** of interface/contract diagrams.
  - “Interface” here means: API boundaries, request/response flows, policy boundaries, service-to-service contracts, and cross-layer interactions.
- This `README.md` (directory contract + usage rules).

**Recommended characteristics for SVG outputs:**
- Pure vector (no embedded bitmap screenshots unless there’s a compelling reason).
- No external network references (fonts, images, CSS) — keep diagrams portable.
- No scripts.
- Includes a `viewBox` so it scales correctly.

---

## What must NOT go here

**Do not commit source-of-truth diagram files** here. Keep “editables” elsewhere.

Examples of files that **do not belong** in this folder:
- Diagram sources: `*.mmd`, `*.puml`, `*.drawio`, `*.excalidraw`, `*.fig`, Figma exports, etc.
- Other output formats: `*.png`, `*.pdf` (unless your repo explicitly mirrors formats in sibling folders).
- One-off screenshots, ad-hoc visuals, or WIP experiments that are not referenced anywhere.
- Any diagram containing sensitive implementation details that should not be published (secrets, internal hostnames, exact coordinates for vulnerable sites, etc.).

> **Rule of thumb:** This folder is for **stable rendered artifacts** that downstream docs can link to reliably.

---

## Where this fits in the repo

This directory is intended to be the **rendered-output** endpoint for interface diagrams.

**Intended layout (illustrative; adjust to match repo reality):**
```text
docs/diagrams/
  src/
    interfaces/              # source-of-truth diagrams (edit here)
  out/
    interfaces/
      svg/                   # rendered SVGs (this folder)
```

If your repository uses a different layout, update the `related:` entries in the MetaBlock and adjust the guidance above accordingly.

---

## Naming conventions

Because SVGs are referenced from docs, treat filenames as part of the public interface.

**Recommended filename pattern (PROPOSED):**
```text
<domain-or-surface>__<topic>__v<major>.<minor>.svg
```

Examples:
- `api__stac-items-read__v1.0.svg`
- `api__datasets-search__v1.2.svg`
- `policy__trust-membrane-pep__v1.0.svg`
- `ingest__promotion-contract-flow__v1.0.svg`

**Rules:**
- Use lowercase with `-` or `__` separators; avoid spaces.
- Include a version in the filename when the diagram is referenced by long-lived docs.
- If a diagram is purely internal / iterative, keep versioning in the source file until it stabilizes.

> **NOTE:** If the repo already has a naming standard, prefer the existing standard and revise this section to match.

---

## How to add or update a diagram

1. **Edit the source diagram** (do not hand-edit SVG outputs).
   - Source location is expected to be something like `docs/diagrams/src/interfaces/…` (update if different).
2. **Render to SVG** using repo tooling.
   - **TODO:** Document the exact command once confirmed (examples below are placeholders).
3. **Run checks** (lint/link-check/validation if present).
4. **Commit the updated SVG** in this folder.
5. **Reference it from docs** using a stable relative link.

### Tooling placeholders (replace with the real commands)

```sh
# Example placeholders — replace with the repo’s actual diagram build commands
# pnpm -w diagrams:build
# make diagrams
# python tools/diagrams/render.py --in docs/diagrams/src/interfaces --out docs/diagrams/out/interfaces/svg
```

---

## Quality and governance checks

Even though these are “just diagrams,” they can leak sensitive details or misrepresent contracts.

### Minimum quality bar

- Text is readable at typical doc widths.
- Diagram includes a title and (ideally) a small footer with:
  - diagram id / name
  - version
  - “source-of-truth” pointer (where the editable file lives)

### Governance / safety bar

- Do not include secrets, tokens, internal-only endpoints, private hostnames, or credentials.
- For vulnerable/private/culturally restricted locations: **do not include exact coordinates**; use coarse geography and ensure policy review.
- Ensure the diagram reflects the **governed boundary** posture:
  - clients should interact via **governed APIs** (policy boundary), not direct storage access.

> **WARNING:** Treat diagrams as publishable artifacts. If you wouldn’t paste it into an issue tracker visible to the same audience as your docs, don’t commit it here.

---

## Embedding SVGs in docs

### Markdown

```md
![STAC items read flow](./api__stac-items-read__v1.0.svg)
```

### HTML (when you need sizing control)

```html
<img
  src="./api__stac-items-read__v1.0.svg"
  alt="STAC items read flow"
  width="900"
/>
```

**Accessibility guidance:**
- Always provide meaningful alt text.
- If the diagram is complex, add a short textual summary near the embed.

---

## Appendix: SVG hygiene checklist

<details>
<summary><strong>Checklist</strong> (expand)</summary>

- [ ] SVG renders correctly in GitHub and the docs site (if applicable)
- [ ] No embedded scripts
- [ ] No external references (remote fonts/images)
- [ ] Has `viewBox`
- [ ] No sensitive data (secrets, internal-only identifiers, vulnerable coordinates)
- [ ] Filename is stable and follows the repo convention
- [ ] Linked from at least one doc page, or intentionally staged for upcoming work
- [ ] Source-of-truth diagram path is documented (in the source folder or in-diagram footer)

</details>

---

<p align="right"><a href="#interface-diagrams-svg">Back to top</a></p>
