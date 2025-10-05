<div align="center">

# 📚 Kansas Frontier Matrix — Documentation System  
`docs/README.md`

**Mission:** Serve as the **comprehensive documentation hub** for the  
Kansas Frontier Matrix (KFM) — connecting technical, architectural,  
and procedural docs under a unified, reproducible framework.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

## 📖 Overview

The `docs/` directory is the **source of truth** for the **Kansas Frontier Matrix** and a **published knowledge hub** (GitHub Pages).  
It follows **MCP (Master Coder Protocol)** principles:

- 🧠 **Documentation-first** — define intent, scope, and interfaces *before* code.
- 🔁 **Reproducibility** — every reader can re-run builds and validations as documented.
- 🌐 **Open standards** — Markdown, JSON Schema, STAC 1.0, Mermaid.
- 🧩 **Provenance** — each artifact declares authorship, version, and context.
- 🧾 **Auditability** — CI/CD validates docs, links, and schemas.

---

## 🗂️ Directory Layout

```bash
docs/
├── README.md                        # Documentation index (this file)
├── architecture/                    # System, data, API, CI/CD, web design
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
├── standards/                       # Style guides & validation specs
│   ├── metadata-standards.md
│   ├── naming-conventions.md
│   └── validation-protocols.md
├── templates/                       # MCP templates
│   ├── sop.md
│   ├── experiment.md
│   └── model_card.md
└── glossary.md                      # Cross-disciplinary terms
````

> **Note:** Each subdirectory includes its own `README.md` or header block describing scope, ownership, and version.

---

## 🧭 Quick Navigation

| Category               | Description                                  | Primary Docs                                                                                                                |
| ---------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 🧱 **Architecture**    | System & process blueprints                  | [`architecture/architecture.md`](architecture/architecture.md), [`data-architecture.md`](architecture/data-architecture.md) |
| ⚙️ **Pipelines**       | ETL + AI/ML design and automation            | [`architecture/pipelines.md`](architecture/pipelines.md)                                                                    |
| 🌐 **Web & API**       | Frontend visualization & programmatic access | [`web-ui-architecture.md`](architecture/web-ui-architecture.md), [`api-architecture.md`](architecture/api-architecture.md)  |
| 🧠 **Knowledge Graph** | Ontologies, schema, reasoning                | [`knowledge-graph.md`](architecture/knowledge-graph.md)                                                                     |
| 🔄 **CI/CD**           | Validation, security, and deploy workflows   | [`ci-cd.md`](architecture/ci-cd.md)                                                                                         |
| 📏 **Standards**       | Metadata, naming, validation policies        | [`standards/metadata-standards.md`](standards/metadata-standards.md)                                                        |
| 🧪 **Templates**       | MCP SOPs, experiments, model cards           | [`templates/`](templates/)                                                                                                  |
| 📚 **Glossary**        | Canonical terminology                        | [`glossary.md`](glossary.md)                                                                                                |

---

## 🧩 Render & Deploy

Documentation is built and published by **GitHub Actions** (`site.yml`) as a static site.

| Task                | Command                               | Output                  |
| ------------------- | ------------------------------------- | ----------------------- |
| **Build docs**      | `make site`                           | `_site/` (static site)  |
| **Preview locally** | `python -m http.server -d _site 8000` | `http://localhost:8000` |
| **Deploy (CI/CD)**  | Triggered by `site.yml` on `main`     | GitHub Pages            |

---

## 🧮 Diagrams & Visuals

All diagrams are authored in **Mermaid** and reproducibly exported.

```bash
make diagrams
```

Artifacts live in `docs/architecture/diagrams/exported/` and are referenced with relative paths, e.g.:

```md
![System Overview](architecture/diagrams/exported/system_overview.svg)
```

---

## 🧠 Governance & MCP Compliance

| MCP Principle           | Enforcement                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------- |
| **Documentation-first** | Each module has a README + design doc before code merges.                          |
| **Reproducibility**     | `make docs`, `make site`, and validation targets must pass.                        |
| **Open Standards**      | Docs rely on Markdown, JSON Schema, STAC, Mermaid.                                 |
| **Provenance**          | Headers include author(s), version, date; PRs require semantic commits.            |
| **Auditability**        | CI (`site.yml`, `stac-validate.yml`, pre-commit) checks links, schemas, and style. |

---

## 🧾 Writing & Formatting Guide

Use **GitHub-Flavored Markdown (GFM)** and keep content lint-clean.

**Headings**

```md
## Section
### Subsection
#### Detail
```

**Code Blocks**

<pre markdown="1">

```bash
make site
```
```python
print("hello, KFM")
```
</pre>

**Tables**

| Field     | Description               |
| :-------- | :------------------------ |
| `id`      | Unique identifier         |
| `license` | Data/document usage terms |

**Links & Images**

* Prefer **relative** links: `[Pipelines](architecture/pipelines.md)`
* Place assets under `docs/architecture/diagrams/exported/`

**Front-Matter Metadata (optional)**

```md
<!--
Author: Your Name
Version: v1.1
Last-Updated: 2025-10-05
Scope: Docs Hub Index
-->
```

---

## 🔍 CI/CD Validation of Docs

| Workflow                   | Function                              | When               |
| -------------------------- | ------------------------------------- | ------------------ |
| `site.yml`                 | Build & publish static docs site      | On merge to `main` |
| `stac-validate.yml`        | Validate STAC JSON & links            | On PR / commit     |
| `pre-commit.yml`           | Lint Markdown & check structure       | Every PR           |
| `codeql.yml` / `trivy.yml` | Security scanning (code & containers) | Scheduled / PR     |

---

## 🧩 Contributor Workflow

1. **Create / Update** a doc in `docs/` (and add diagrams if needed).
2. **Validate locally**:

   ```bash
   make docs-validate
   ```
3. **Commit (semantic)**:

   ```bash
   git commit -m "docs(architecture): clarify ETL lineage and add diagram"
   ```
4. **Open a PR** and ensure all docs checks pass.
5. **Merge** — CI publishes the site.

> For new subsystems, include: scope, interfaces, dependencies, failure modes, and testing strategy.

---

## 🧭 Recommended Reading Order

1. `architecture/architecture.md` — **System Overview**
2. `architecture/data-architecture.md` — **Data Flow & Provenance**
3. `architecture/pipelines.md` — **ETL & AI/ML**
4. `architecture/ci-cd.md` — **Automation & Governance**
5. `architecture/web-ui-architecture.md` — **Visualization Pipeline**
6. `architecture/knowledge-graph.md` — **Semantic Layer**
7. `standards/metadata-standards.md` — **Schemas & Compliance**
8. `glossary.md` — **Terminology**

---

## 🧷 Appendix — Doc Status Badges

Use these shields at the top of new documents to indicate maturity and scope:

* ![Status: Draft](https://img.shields.io/badge/Status-Draft-yellow)
* ![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)
* ![Scope: Architecture](https://img.shields.io/badge/Scope-Architecture-blue)
* ![Scope: Pipelines](https://img.shields.io/badge/Scope-Pipelines-purple)

---

## 📅 Version History

| Version  | Date       | Summary                                                                                                   |
| -------- | ---------- | --------------------------------------------------------------------------------------------------------- |
| **v1.1** | 2025-10-05 | Added governance, rendering commands, improved tables/format, doc-status badges, and local preview steps. |
| **v1.0** | 2025-10-04 | Initial documentation hub and MCP-compliant structure for `docs/`.                                        |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Document is a Blueprint. Every Blueprint is Reproducible.”*
📍 [`docs/`](.) · Central documentation and architecture index for the Kansas Frontier Matrix.

</div>
