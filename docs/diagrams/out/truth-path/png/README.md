<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/62de27f6-0430-41bf-bccb-776779928f1b
title: Truth Path PNG Diagrams
type: standard
version: v1
status: draft
owners: TBD
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/diagrams/out/truth-path/png/
  - docs/diagrams/
tags: [kfm, diagrams, truth-path, png]
notes:
  - This directory contains rendered PNG exports of the KFM “truth path” lifecycle diagram(s).
  - Source diagram(s) and render scripts may live elsewhere; this README documents the *output* directory contract.
[/KFM_META_BLOCK_V2] -->

# Truth Path PNG Diagrams

**Purpose:** Rendered PNG exports of the Kansas Frontier Matrix (KFM) **Truth Path** lifecycle diagrams for use in docs, wikis, PR discussions, and slide decks.

![status](https://img.shields.io/badge/status-draft-lightgrey)
![policy](https://img.shields.io/badge/policy-public-blue)
![format](https://img.shields.io/badge/format-PNG-informational)

> **NOTE**
> This is an **output** directory. Prefer changing the **source diagram** and re-rendering outputs rather than editing PNGs by hand.

---

## Quick navigation

- [What is the Truth Path](#what-is-the-truth-path)
- [What belongs here](#what-belongs-here)
- [Naming and export conventions](#naming-and-export-conventions)
- [How to regenerate](#how-to-regenerate)
- [Quality gates](#quality-gates)
- [Changelog](#changelog)

---

## What is the Truth Path

The **Truth Path** is KFM’s governed lifecycle from upstream acquisition through publication.

```mermaid
flowchart LR
  U[Upstream sources] -->|Acquire (immutable)| R[RAW zone]
  R -->|Validate & quarantine| W[WORK / QUARANTINE]
  W -->|Transform & QA| P[PROCESSED]
  P -->|Describe & link| C[CATALOG<br/>DCAT + STAC + PROV]
  C -->|Serve via policy| Pub[PUBLISHED<br/>Governed APIs/UI]

  %% Governance/controls
  R -.->|Run receipt & audit| A[Audit ledger]
  W -.->|Evidence refs| E[Evidence bundles]
  Pub -.->|Trust membrane| T[Policy enforcement point]
```

### Invariants the diagram is expected to communicate

- **No promotion without gates**: each step produces artifacts and a run receipt/audit trail.
- **Immutable-by-default** in upstream/RAW; downstream stages are reproducible from receipts + inputs.
- **Trust membrane**: clients/UI access data through governed APIs (policy boundary), not direct storage.

---

## What belongs here

✅ **Acceptable inputs**

- PNG files that are **rendered exports** of the Truth Path diagram(s).
- Variants for different contexts (e.g., `light` vs `dark`, `screen` vs `print`) *if clearly named*.
- Optional accompanying sidecar checksums (e.g., `.sha256`) **if your build system emits them**.

🚫 **Exclusions**

- Do **not** commit editable source formats here (e.g., `.drawio`, `.svg`, `.pptx`, `.excalidraw`, `.figma` exports).
- Do **not** commit screenshots that *look like* the diagram but aren’t reproducible from the source.
- Do **not** store unrelated diagrams in this folder (create a sibling folder instead).

---

## Naming and export conventions

Keep filenames **stable, explicit, and diff-friendly**.

### Recommended filename pattern

```text
truth-path__v<MAJOR>.<MINOR>__<variant>__<WxH>@<scale>x.png
```

Examples:

- `truth-path__v1.0__light__1920x1080@1x.png`
- `truth-path__v1.0__dark__1920x1080@2x.png`
- `truth-path__v1.0__print__2550x3300@1x.png` (US Letter @ 300dpi)

### Export rules

| Rule | Why |
|---|---|
| Prefer 1x **and** 2x exports for screen | avoids blurry embedding in slides |
| Keep consistent aspect ratios per variant | makes swapping versions painless |
| Prefer transparent background unless readability suffers | supports different doc backgrounds |
| Don’t bake sensitive dataset names/IDs into the diagram | keeps the diagram reusable + policy-safe |

---

## How to regenerate

**Unknown in this repo snapshot:** the canonical source file(s) and the exact render command(s).

Minimum steps to resolve:

1. Search for a “truth-path” diagram source in `docs/diagrams/src/`, `docs/diagrams/`, or `tools/` (repo-specific).
2. Search for a diagram build pipeline in `scripts/`, `Makefile`, or `package.json` (repo-specific).
3. Confirm the output of the render step is written to this folder (or symlinked/copied here).

If you have a diagram build script, add a short “one-liner” here. Suggested format:

```bash
# Example (replace with the real command in this repo)
# ./scripts/diagrams/render.sh truth-path --format png --out docs/diagrams/out/truth-path/png
```

---

## Quality gates

Before committing updated PNGs:

- [ ] Diagram still matches the **current** Truth Path definition (zones + ordering).
- [ ] Any policy-related labels are **generic** (no dataset-specific secrets or private locations).
- [ ] Exported PNGs are readable at 100% zoom and in common embed contexts (GitHub, slides).
- [ ] If a new variant is introduced, the README and naming table are updated.

---

## Changelog

- **2026-03-01** — Created directory README; documented output contract and naming conventions.
