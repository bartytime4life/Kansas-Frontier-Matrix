<div align="center">

# 📝 Kansas Frontier Matrix — Documentation Standards  
`docs/standards/documentation.md`

**Purpose:** Define the official documentation, writing, and formatting standards for the  
**Kansas Frontier Matrix (KFM)** repository — ensuring that every file is written,  
structured, and maintained with **clarity**, **consistency**, and **MCP reproducibility**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The **KFM Documentation Standards** ensure that every document, README, SOP, and architecture file is:
- 🧠 **Documentation-first** — written before or alongside implementation  
- 🧩 **Consistent** — structured uniformly for human and machine readability  
- 🔁 **Reproducible** — describes procedures that can be repeated exactly  
- 🔗 **Provenance-tracked** — includes version, authorship, and relationships  
- 🧾 **Auditable** — validated through CI/CD and peer review  

All documentation is **Markdown-based**, uses **open standards (MD + JSON Schema + STAC)**,  
and is automatically validated during builds via `make site` and `.github/workflows/site.yml`.

---

## 🧩 Documentation Structure

Each document follows a standardized structure for clarity and auditability.

### 🧱 Recommended Markdown Layout

| Section | Description |
|:-----------|:-------------|
| **Title Block** | Includes document title, repository path, purpose, and badges. |
| **Overview** | High-level summary and scope of the document. |
| **Core Content** | Main topic sections (procedures, methods, diagrams, etc.). |
| **MCP Compliance Summary** | Table showing adherence to MCP principles. |
| **Related Documentation** | Links to connected files or references. |
| **Version History** | Tracks updates, authors, and summary of changes. |
| **Footer** | Tagline and file location for reproducibility. |

---

### Example File Header

```markdown
<div align="center">

# 🧱 Kansas Frontier Matrix — Example Document Title  
`path/to/file.md`

**Purpose:** Short one-sentence summary of document’s purpose.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>
````

---

## 🧱 Writing Standards

| Area            | Standard                                                     | Example                                            |
| :-------------- | :----------------------------------------------------------- | :------------------------------------------------- |
| **Language**    | Clear, concise, professional English.                        | “This workflow validates all STAC metadata.”       |
| **Tone**        | Objective, instructional, and consistent.                    | Avoid jargon and subjective phrasing.              |
| **Perspective** | Second-person (you/your) for guides; third-person for specs. | “You can run this with `make site`.”               |
| **Verb Tense**  | Present tense for procedures; past tense for results.        | “This process generates a checksum.”               |
| **Voice**       | Active preferred over passive.                               | ✅ “Run validation.” ❌ “Validation should be run.”  |
| **Clarity**     | Avoid redundancy or ambiguity.                               | “Use the `stac-validator` tool to check metadata.” |

---

## 🧾 Formatting Conventions

| Element         | Format                                           | Notes                                             |
| :-------------- | :----------------------------------------------- | :------------------------------------------------ |
| **Headings**    | Use `#`, `##`, `###` hierarchically.             | Start with one `#` per file.                      |
| **Tables**      | GitHub-flavored Markdown tables.                 | Align columns with `:` for readability.           |
| **Code Blocks** | Triple backticks with language tag.              | `bash` for commands, `json` for metadata.         |
| **Lists**       | Use `-` for unordered, `1.` for ordered lists.   | Nested lists indented 2 spaces.                   |
| **Emphasis**    | `**bold**` for key terms, *italic* for emphasis. | Avoid overuse.                                    |
| **Links**       | Relative paths within repo.                      | `[architecture.md](architecture/architecture.md)` |
| **Badges**      | Include MCP and license badges in header.        | See example header above.                         |

---

## 🧩 Versioning & Provenance Metadata

Each document must include version control and authorship metadata.

| Field       | Description                     | Example                                    |
| :---------- | :------------------------------ | :----------------------------------------- |
| **Version** | Semantic version (vX.Y).        | `v1.0`                                     |
| **Date**    | Last modification date.         | `2025-10-04`                               |
| **Author**  | Document creator or maintainer. | `KFM Documentation Team`                   |
| **Summary** | One-line change summary.        | “Initial data architecture documentation.” |

**All version histories must appear in a table at the end of the document.**

---

## 🧠 Diagrams & Visual Standards

Visual assets must be stored under:

```
docs/architecture/diagrams/exported/
```

| Type                       | Format                             | Standard                                          |
| :------------------------- | :--------------------------------- | :------------------------------------------------ |
| **Architecture Diagrams**  | Mermaid (`.mmd` → `.svg` / `.png`) | Must render correctly in GitHub preview.          |
| **Data Flow / Provenance** | Mermaid Flowcharts                 | Include directional arrows and clear node labels. |
| **ER Diagrams**            | Mermaid `erDiagram`                | Follow STAC and MCP terminology.                  |
| **Metadata Visuals**       | STAC or JSON Schema examples       | Embed as fenced code blocks.                      |

> All diagrams must include title comments, version, author, and commit hash in their Mermaid source files.

---

## 🧮 Document Validation

Documentation is validated automatically through the CI/CD pipeline.

| Validation Type           | Tool / Workflow              | Description                                    |
| :------------------------ | :--------------------------- | :--------------------------------------------- |
| **Markdown Linting**      | `markdownlint-cli`           | Checks syntax, headers, links, and tables.     |
| **Broken Link Check**     | `remark-lint`                | Validates internal cross-references.           |
| **Style Compliance**      | `pre-commit` hooks           | Ensures adherence to repo writing conventions. |
| **CI Build Test**         | `.github/workflows/site.yml` | Builds static site to confirm render success.  |
| **Spellcheck (Optional)** | `codespell`                  | Detects common spelling errors.                |

Example command:

```bash
make docs-validate
```

---

## 🧾 Documentation Storage & Organization

| Directory            | Purpose                                                |
| :------------------- | :----------------------------------------------------- |
| `docs/architecture/` | System, data, and CI/CD architecture documentation.    |
| `docs/standards/`    | Governance standards and validation rules.             |
| `docs/templates/`    | Reusable MCP templates for reproducible documentation. |
| `docs/glossary.md`   | Canonical term definitions.                            |
| `docs/README.md`     | Documentation system index.                            |

All directories must include:

* A `README.md` describing contents and dependencies.
* Internal cross-links for navigation.
* Version history at the bottom.

---

## 🧩 Documentation Governance & Review

Documentation updates must pass peer review and CI validation before merge.

| Review Type           | Reviewer Role      | Validation                                      |
| :-------------------- | :----------------- | :---------------------------------------------- |
| **Technical Review**  | Domain Expert      | Ensures factual correctness.                    |
| **Editorial Review**  | Documentation Lead | Ensures clarity and consistency.                |
| **Compliance Review** | Governance Team    | Confirms MCP adherence and provenance accuracy. |

Reviews are recorded under:

```
data/work/logs/docs/review_<filename>.log
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                        |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | All procedures and standards documented before implementation.        |
| **Reproducibility**     | Docs, diagrams, and metadata validated by CI/CD workflows.            |
| **Open Standards**      | Markdown, JSON Schema, STAC 1.0.0 used throughout.                    |
| **Provenance**          | Version history, authorship, and commit linkage embedded in each doc. |
| **Auditability**        | Validation logs archived in `data/work/logs/docs/`.                   |

---

## 📎 Related Documentation

| File                                | Description                                                         |
| :---------------------------------- | :------------------------------------------------------------------ |
| `docs/README.md`                    | Overview of the entire documentation system.                        |
| `docs/standards/coding.md`          | Coding and formatting conventions supporting documentation quality. |
| `docs/standards/data-formats.md`    | Defines approved file formats for referenced content.               |
| `docs/architecture/architecture.md` | Core architectural overview linked by documentation system.         |
| `.github/workflows/site.yml`        | CI/CD workflow that builds and validates documentation.             |

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                         |
| :------ | :--------- | :--------------------- | :-------------------------------------------------------------- |
| v1.0    | 2025-10-04 | KFM Documentation Team | Initial documentation and writing standards for MCP compliance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Word Accounted For. Every Page Proven.”*
📍 [`docs/standards/documentation.md`](.) · Official documentation and writing standards under MCP governance for Kansas Frontier Matrix.

</div>
