<div align="center">

# 📚 Kansas Frontier Matrix — Documentation System  
`docs/README.md`

**Mission:** Serve as the **comprehensive documentation hub** for the  
Kansas Frontier Matrix (KFM) — connecting all technical, architectural,  
and procedural documents under a unified, reproducible framework.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

## 📖 Overview

The `docs/` directory contains all documentation for the **Kansas Frontier Matrix**,  
organized according to **MCP (Master Coder Protocol)** principles of:

- 🧠 **Documentation-first** — every process and system is explained before implementation  
- 🔁 **Reproducibility** — workflows can be replicated exactly via provided instructions  
- 🌍 **Open Standards** — Markdown, JSON Schema, STAC, and Mermaid diagrams  
- 🧩 **Provenance** — every document includes authorship, version, and context metadata  
- 🧾 **Auditability** — CI/CD pipelines validate documentation consistency  

This directory is both the **source of truth** for repository operations and a **published knowledge hub** when deployed to GitHub Pages.

---

## 🗂️ Directory Layout

```bash
docs/
├── README.md                        # This file (documentation index)
├── architecture/                    # System, data, API, CI/CD, and web design docs
│   ├── architecture.md
│   ├── data-architecture.md
│   ├── file-architecture.md
│   ├── web-ui-architecture.md
│   ├── api-architecture.md
│   ├── knowledge-graph.md
│   ├── pipelines.md
│   ├── ci-cd.md
│   └── diagrams/
│       ├── README.md
│       ├── exported/
│       └── templates/
├── standards/                       # Style guides, metadata standards, and data schema docs
│   ├── metadata-standards.md
│   ├── naming-conventions.md
│   └── validation-protocols.md
├── templates/                       # MCP templates for experiments, SOPs, and model cards
│   ├── sop.md
│   ├── experiment.md
│   └── model_card.md
└── glossary.md                      # Definitions of KFM-specific and cross-disciplinary terms
````

> **Note:** Each directory includes its own `README.md`, providing localized documentation and compliance context.

---

## 🧭 Navigation Guide

| Category               | Description                                                        | Key Documents                                          |
| :--------------------- | :----------------------------------------------------------------- | :----------------------------------------------------- |
| 🧱 **Architecture**    | System, data, and process blueprints.                              | `architecture/architecture.md`, `data-architecture.md` |
| ⚙️ **Pipelines**       | ETL process documentation and automation patterns.                 | `architecture/pipelines.md`                            |
| 🌐 **Web & API**       | Frontend visualization and programmatic access architecture.       | `web-ui-architecture.md`, `api-architecture.md`        |
| 🧩 **Knowledge Graph** | Semantic and RDF data integration system.                          | `knowledge-graph.md`                                   |
| 🔄 **CI/CD**           | Automated validation, testing, and deployment system.              | `ci-cd.md`                                             |
| 🗃️ **Standards**      | Metadata formats, schema validation, and naming policies.          | `standards/metadata-standards.md`                      |
| 🧪 **Templates**       | MCP-compliant research and procedural templates.                   | `templates/experiment.md`, `templates/sop.md`          |
| 📚 **Glossary**        | Unified definitions for technical and domain-specific terminology. | `glossary.md`                                          |

---

## 🧩 Rendering & Site Deployment

Documentation is automatically compiled and published as a static site via
the **`site.yml`** GitHub Actions workflow.

| Task                | Command                        | Output                                    |
| :------------------ | :----------------------------- | :---------------------------------------- |
| **Build Docs**      | `make site`                    | Generates `_site/` directory              |
| **Preview Locally** | `python -m http.server _site/` | Local preview at `http://localhost:8000`  |
| **Deploy (CI/CD)**  | Triggered by `site.yml`        | Published to GitHub Pages (`main` branch) |

---

## 🧮 Diagram & Visualization Standards

All diagrams and charts are built using **Mermaid** syntax and exported to
SVG/PNG formats through reproducible CLI commands.

**Example Build:**

```bash
make diagrams
```

Outputs are stored in:

```
docs/architecture/diagrams/exported/
```

Diagrams appear across:

* `architecture.md` → system overview
* `data-architecture.md` → data lineage
* `ci-cd.md` → automation flow
* `web-ui-architecture.md` → visualization pipeline

---

## 🧠 Documentation Governance (MCP Compliance)

| MCP Principle           | Enforcement Mechanism                                                              |
| :---------------------- | :--------------------------------------------------------------------------------- |
| **Documentation-first** | Required README + architecture files for every module.                             |
| **Reproducibility**     | `make docs` + `make site` regenerate identical output.                             |
| **Open Standards**      | Markdown + JSON Schema + STAC for all documentation.                               |
| **Provenance**          | Version headers, author metadata, and commit IDs in all docs.                      |
| **Auditability**        | CI/CD (`site.yml`, `stac-validate.yml`) verifies consistency and schema integrity. |

---

## 🧾 Writing & Formatting Standards

| Type            | Standard                            | Example                                                          |       |             |   |
| :-------------- | :---------------------------------- | :--------------------------------------------------------------- | ----- | ----------- | - |
| **Headings**    | Use hierarchical `##` for clarity   | `## Section → ### Subsection`                                    |       |             |   |
| **Code Blocks** | Use triple backticks + language tag | ```bash                                                          |       |             |   |
| **Tables**      | GitHub Markdown syntax              | `                                                                | Field | Description | ` |
| **Links**       | Relative paths within repo          | `[architecture.md](architecture/architecture.md)`                |       |             |   |
| **Images**      | Relative to `docs/` directory       | `![Diagram](architecture/diagrams/exported/system_overview.png)` |       |             |   |
| **Metadata**    | Top-of-file comments or YAML blocks | Author, version, date                                            |       |             |   |

---

## 🔍 CI/CD Validation of Docs

| Workflow                       | Function                                                       | Frequency          |
| :----------------------------- | :------------------------------------------------------------- | :----------------- |
| **`site.yml`**                 | Builds and publishes all Markdown docs as a static site.       | On merge to `main` |
| **`stac-validate.yml`**        | Checks for valid JSON links and broken references.             | On PR / commit     |
| **`pre-commit.yml`**           | Ensures style, linting, and structure of Markdown docs.        | Every PR           |
| **`codeql.yml` / `trivy.yml`** | Scans for security vulnerabilities in code referenced by docs. | Weekly             |

---

## 🧩 Documentation Contribution Workflow

1. **Create or Edit a Doc**
   Add/update a `.md` file in the appropriate `docs/` subdirectory.

2. **Validate Locally**

   ```bash
   make docs-validate
   ```

3. **Commit with Semantic Message**

   ```bash
   git commit -m "docs(architecture): update ci-cd section"
   ```

4. **Open Pull Request**
   Ensure all CI/CD documentation checks pass (`site.yml`, `pre-commit.yml`).

5. **Merge + Deploy**
   Once approved, GitHub Actions automatically rebuilds and publishes documentation.

---

## 🧩 Recommended Reading Order

1. [`architecture/architecture.md`](architecture/architecture.md) — **System Overview**
2. [`architecture/data-architecture.md`](architecture/data-architecture.md) — **Data Flow + Provenance**
3. [`architecture/pipelines.md`](architecture/pipelines.md) — **ETL and Processing Design**
4. [`architecture/ci-cd.md`](architecture/ci-cd.md) — **Automation and Governance**
5. [`architecture/web-ui-architecture.md`](architecture/web-ui-architecture.md) — **Visualization + User Experience**
6. [`architecture/knowledge-graph.md`](architecture/knowledge-graph.md) — **Semantic Data Layer**
7. [`standards/metadata-standards.md`](standards/metadata-standards.md) — **Metadata + Schema Compliance**
8. [`glossary.md`](glossary.md) — **Reference + Definitions**

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                    |
| :---------------------- | :---------------------------------------------------------------- |
| **Documentation-first** | All systems and processes are documented prior to deployment.     |
| **Reproducibility**     | Documentation site can be regenerated and verified automatically. |
| **Open Standards**      | Uses Markdown, Mermaid, JSON Schema, and STAC 1.0.0 formats.      |
| **Provenance**          | File headers include author, version, and date.                   |
| **Auditability**        | Docs validated via CI/CD workflows and manual peer review.        |

---

## 📎 Related Documentation

| Path                 | Description                                             |
| :------------------- | :------------------------------------------------------ |
| `data/README.md`     | Data management overview and organization.              |
| `.github/README.md`  | Automation and governance documentation.                |
| `web/README.md`      | Web viewer, visualization layers, and UI documentation. |
| `docs/architecture/` | All system and process design documents.                |

---

## 📅 Version History

| Version | Date       | Summary                                                                          |
| :------ | :--------- | :------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial documentation hub and MCP-compliant structure for the `docs/` directory. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Document is a Blueprint. Every Blueprint is Reproducible.”*
📍 [`docs/`](.) · Central documentation and architecture index for the Kansas Frontier Matrix.

</div>
