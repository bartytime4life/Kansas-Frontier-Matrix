<div align="center">

# 📝 Kansas Frontier Matrix — Documentation & Writing Standards

`docs/standards/documentation.md`

**Purpose:** Define the official **documentation, formatting, and governance standards** for
the **Kansas Frontier Matrix (KFM)** — ensuring every document is **clear**, **consistent**,
and **reproducible** under the **Master Coder Protocol (MCP)**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The KFM documentation system is the **living backbone** of the project.
All text artifacts — from architecture notes to dataset metadata — must be:

| Principle                  | Description                                              |
| :------------------------- | :------------------------------------------------------- |
| 🧠 **Documentation-first** | Drafted before or alongside code and data changes.       |
| 🧩 **Consistent**          | Structured and formatted identically across directories. |
| 🔁 **Reproducible**        | Fully re-buildable and verifiable by any contributor.    |
| 🔗 **Provenance-tracked**  | Authorship, version, and file lineage embedded within.   |
| 🧾 **Auditable**           | Validated automatically in CI/CD and peer-review logs.   |

All content uses **GitHub-Flavored Markdown (GFM)** and, where relevant,
**open interchange standards** — **JSON Schema**, **STAC 1.0.0**, and **DCAT**.
Validation runs via `make docs-validate` and the CI workflow `.github/workflows/site.yml`.

---

## 🧩 Document Anatomy

Each Markdown file follows this standard composition for clarity and MCP traceability.

| Section                  | Description                                                  |
| :----------------------- | :----------------------------------------------------------- |
| **Title Block**          | File path, title, purpose, and badges in a centered `<div>`. |
| **Overview**             | A concise statement of scope and context.                    |
| **Core Sections**        | Procedures, diagrams, methods, or standards content.         |
| **MCP Compliance Table** | Declares how MCP principles are implemented.                 |
| **Related Docs**         | Cross-links to other standards or architecture files.        |
| **Version History**      | Semantic version, date, author, and summary of edits.        |
| **Footer Tagline**       | Official MCP provenance quote and file path.                 |

---

### 🧱 Example Header

```markdown
<div align="center">

# 🧱 Kansas Frontier Matrix — Example Title  
`path/to/file.md`

**Purpose:** Short one-sentence summary of intent.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>
```

---

## ✍️ Writing & Style Guide

| Category        | Requirement                              | Example                                            |
| :-------------- | :--------------------------------------- | :------------------------------------------------- |
| **Language**    | Clear, precise technical English.        | “This workflow validates all STAC items.”          |
| **Tone**        | Objective / instructional.               | Avoid hype or ambiguity.                           |
| **Perspective** | Guides = 2nd person; Specs = 3rd person. | “You can run this with `make site`.”               |
| **Tense**       | Present for process; past for results.   | “This script generates checksums.”                 |
| **Voice**       | Prefer active.                           | ✅ “Run validation.”  ❌ “Validation should be run.” |
| **Clarity**     | One idea per sentence; avoid redundancy. | “Use `stac-validator` to check metadata.”          |

All new files must pass Markdown linting and human editorial review before merge.

---

## 🧾 Formatting Conventions

| Element         | Standard                                    | Notes                                   |
| :-------------- | :------------------------------------------ | :-------------------------------------- |
| **Headings**    | `#`, `##`, `###` hierarchy.                 | Only one top-level `#` per file.        |
| **Tables**      | GFM tables with colons for alignment.       | Keep ≤ 4 columns per table if possible. |
| **Code Blocks** | Triple backticks + language tag.            | `bash`, `json`, `python`, `mermaid`.    |
| **Lists**       | `-` unordered, `1.` ordered.                | Indent 2 spaces for nested.             |
| **Emphasis**    | `**bold**` key terms; *italic* for context. | Avoid decorative emphasis.              |
| **Links**       | Relative paths within repo.                 | `[architecture.md](../architecture/)`   |
| **Badges**      | MCP + License required.                     | Add workflow badges as relevant.        |

> ℹ️ Use the examples from `docs/standards/coding.md` for code-block colorization and emoji support (see 🧾 GitHub Formatting Guide).

---

## 🧩 Version & Provenance Metadata

Every document must include explicit metadata at the end **and** in the Git commit.

| Field       | Example                                   |
| :---------- | :---------------------------------------- |
| **Version** | `v1.2`                                    |
| **Date**    | `2025-10-05`                              |
| **Author**  | `KFM Docs Team`                           |
| **Summary** | “Added CI validation table and examples.” |

Append a **Version History Table**:

| Version | Date       | Author    | Summary                         |
| :------ | :--------- | :-------- | :------------------------------ |
| v1.2    | 2025-10-05 | Docs Team | Expanded MCP compliance matrix. |
| v1.0    | 2025-10-04 | Docs Team | Initial release.                |

---

## 🧠 Diagram Standards

All diagrams live under `docs/architecture/diagrams/exported/`.

| Diagram Type                 | Format                  | Rule                                       |
| :--------------------------- | :---------------------- | :----------------------------------------- |
| **Architecture / Data Flow** | Mermaid (`.mmd → .svg`) | Must render correctly on GitHub.           |
| **Entity Relations (ER)**    | `erDiagram` syntax      | Use STAC + MCP nomenclature.               |
| **Process Flows**            | `flowchart TD` or `LR`  | Include labeled arrows & version comments. |
| **Metadata Examples**        | JSON code blocks        | Show realistic file snippets.              |

Each `.mmd` source includes a comment header with title, author, date, commit hash.

---

## 🔍 Automated Validation

| Check            | Tool / Workflow              | Purpose                                     |
| :--------------- | :--------------------------- | :------------------------------------------ |
| Markdown Lint    | `markdownlint-cli`           | Syntax & structure consistency.             |
| Link Validation  | `remark-lint`                | Ensures internal cross-links resolve.       |
| Style Compliance | `pre-commit` hooks           | Applies coding + docs format rules.         |
| CI Build         | `.github/workflows/site.yml` | Verifies render and static site generation. |
| Spellcheck       | `codespell` (optional)       | Catches common typos.                       |

Run manually:

```bash
make docs-validate
```

---

## 🗂 Directory Organization

| Path                 | Contents                                      |
| :------------------- | :-------------------------------------------- |
| `docs/architecture/` | System, data, and workflow architecture docs. |
| `docs/standards/`    | Governance rules (MCP, coding, format, data). |
| `docs/templates/`    | MCP templates (experiment, sop, model card).  |
| `docs/glossary.md`   | Canonical definitions across disciplines.     |
| `docs/README.md`     | Entry index with navigation tree.             |

Every directory includes its own `README.md`, cross-links, and version table.

---

## 🧩 Governance & Review Workflow

| Review Type | Reviewer        | Responsibility                     |
| :---------- | :-------------- | :--------------------------------- |
| Technical   | Domain Expert   | Accuracy of facts and processes.   |
| Editorial   | Docs Lead       | Grammar, tone, and clarity.        |
| Compliance  | Governance Team | MCP alignment and provenance logs. |

All reviews logged under:
`data/work/logs/docs/review_<filename>.log`

---

## 🧮 MCP Compliance Matrix

| MCP Principle           | Implementation                                      |
| :---------------------- | :-------------------------------------------------- |
| **Documentation-first** | All specs authored before execution.                |
| **Reproducibility**     | CI pipelines verify syntax & output.                |
| **Open Standards**      | Markdown + JSON Schema + STAC used project-wide.    |
| **Provenance**          | Version and commit metadata embedded per file.      |
| **Auditability**        | Validation logs retained in `data/work/logs/docs/`. |

---

## 🔗 Related References

| File                                | Purpose                             |
| :---------------------------------- | :---------------------------------- |
| `docs/README.md`                    | Index of documentation system.      |
| `docs/standards/coding.md`          | Coding & commenting style.          |
| `docs/standards/data-formats.md`    | Approved data and metadata formats. |
| `docs/architecture/architecture.md` | System overview and data flow.      |
| `.github/workflows/site.yml`        | CI build & validation workflow.     |

---

<div align="center">

### 📘 Version History

| Version | Date       | Author    | Summary                                       |
| :------ | :--------- | :-------- | :-------------------------------------------- |
| v1.2    | 2025-10-05 | Docs Team | Expanded formatting rules + CI matrix.        |
| v1.0    | 2025-10-04 | Docs Team | Initial MCP-compliant documentation standard. |

---

**Kansas Frontier Matrix** — *“Every Word Accounted For. Every Page Proven.”*
📍 [`docs/standards/documentation.md`](.) · Maintained under MCP governance.

</div>
