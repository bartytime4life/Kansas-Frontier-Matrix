<div align="center">

# 📚 **Kansas Frontier Matrix — Documentation System**  
`docs/README.md`

**Mission:** Serve as the **comprehensive documentation hub** for the  
Kansas Frontier Matrix (KFM) — connecting technical, architectural,  
and procedural documentation under a unified, reproducible framework.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue?logo=markdown)](../docs/)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&logo=json)](../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy&logo=github)](../.github/workflows/site.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL&logo=github)](../.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security&logo=security)](../.github/workflows/trivy.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Documentation System"
version: "v1.2.0"
last_updated: "2025-10-17"
owners: ["@kfm-docs","@kfm-architecture"]
tags: ["documentation","mcp","standards","architecture","ci","cd","governance"]
status: "Stable"
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - DCAT 2.0
  - CIDOC CRM
  - OWL-Time
---
````

---

## 📖 Overview

The `docs/` directory is the **source of truth** for all knowledge within the **Kansas Frontier Matrix (KFM)**.
It serves as a **living, reproducible knowledge hub** built on the **Master Coder Protocol (MCP-DL v6.3)**.

### MCP Principles Applied

* 🧠 **Documentation-first** — define scope, inputs, outputs *before* implementation.
* 🔁 **Reproducibility** — every reader can re-run builds and validations exactly as documented.
* 🌐 **Open Standards** — Markdown, JSON Schema, STAC 1.0, Mermaid, FAIR-compliant data.
* 🧩 **Provenance** — every artifact declares authorship, version, and metadata.
* 🧾 **Auditability** — CI/CD verifies docs, schemas, diagrams, and external links automatically.

---

## 🗂️ Directory Layout

```bash
docs/
├── README.md                        # Documentation hub (this file)
├── architecture/                    # System, data, API, CI/CD, web architecture
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
├── standards/                       # Style guides & validation protocols
│   ├── metadata-standards.md
│   ├── naming-conventions.md
│   └── validation-protocols.md
├── templates/                       # MCP templates
│   ├── sop.md
│   ├── experiment.md
│   └── model_card.md
├── audit/                           # Compliance audits and governance reports
│   ├── repository_compliance.md
│   └── governance_matrix.md
└── glossary.md                      # Cross-disciplinary term index
```

> Each subdirectory contains a `README.md` or header block describing scope, ownership, and compliance metadata.

---

## 🧭 Quick Navigation

| Category                  | Description                                | Primary Docs                                                                                                               |
| :------------------------ | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| 🧱 **Architecture**       | System & data blueprints                   | [`architecture/architecture.md`](architecture/architecture.md)                                                             |
| ⚙️ **Pipelines**          | ETL & AI/ML automation                     | [`architecture/pipelines.md`](architecture/pipelines.md)                                                                   |
| 🌐 **Web & API**          | Frontend and programmatic access           | [`web-ui-architecture.md`](architecture/web-ui-architecture.md), [`api-architecture.md`](architecture/api-architecture.md) |
| 🧠 **Knowledge Graph**    | Ontologies, schema, and reasoning          | [`knowledge-graph.md`](architecture/knowledge-graph.md)                                                                    |
| 🔄 **CI/CD**              | Validation, security, and deploy workflows | [`ci-cd.md`](architecture/ci-cd.md)                                                                                        |
| 📏 **Standards**          | Metadata, naming, and validation guides    | [`standards/metadata-standards.md`](standards/metadata-standards.md)                                                       |
| 🧪 **Templates**          | SOPs, experiments, and model cards         | [`templates/`](templates/)                                                                                                 |
| 🧩 **Audit & Governance** | Compliance tracking and MCP validation     | [`audit/repository_compliance.md`](audit/repository_compliance.md)                                                         |
| 📚 **Glossary**           | Canonical terminology reference            | [`glossary.md`](glossary.md)                                                                                               |

---

## 🧩 Render & Deploy

Documentation is built and deployed via **GitHub Actions** (`site.yml`), using the same reproducible infrastructure as data pipelines.

| Task                | Command                               | Output                  |
| :------------------ | :------------------------------------ | :---------------------- |
| **Build docs**      | `make site`                           | `_site/` (static site)  |
| **Preview locally** | `python -m http.server -d _site 8000` | `http://localhost:8000` |
| **Deploy (CI/CD)**  | Triggered by `site.yml` on `main`     | GitHub Pages            |

---

## 🧮 Diagrams & Visuals

All diagrams are authored in **Mermaid** and version-controlled.
To regenerate or export all diagrams:

```bash
make diagrams
```

Artifacts live in `docs/architecture/diagrams/exported/` and are embedded using relative paths.

Example:

```md
![System Overview](architecture/diagrams/exported/system_overview.svg)
```

---

## 🧠 Governance & MCP Compliance

| MCP Principle           | Enforcement                                                           |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | Each module includes a README and design doc prior to implementation. |
| **Reproducibility**     | All validation tasks (`make docs`, `make site`) must succeed in CI.   |
| **Open Standards**      | Documents adhere to Markdown, JSON Schema, STAC, and Mermaid.         |
| **Provenance**          | Each doc declares metadata (`version`, `owners`, `last_updated`).     |
| **Auditability**        | CI verifies links, linting, metadata, and structure automatically.    |

---

## 🧾 Writing & Formatting Guide

**General Rules**

* Use **GitHub-Flavored Markdown (GFM)**.
* Keep lines ≤ 120 characters.
* Prefer active voice and short, declarative sentences.

**Headings**

```md
## Section
### Subsection
#### Detail
```

**Code Blocks**

```bash
make site
```

```python
print("Hello, Kansas Frontier Matrix")
```

**Tables**

| Field     | Description               |
| :-------- | :------------------------ |
| `id`      | Unique identifier         |
| `license` | Data/document usage terms |

**Frontmatter Example**

```yaml
---
author: "Your Name"
version: "v1.0.0"
scope: "docs"
last_updated: "2025-10-17"
---
```

---

## 🔍 CI/CD Validation of Documentation

| Workflow                   | Function                                          | Trigger            |
| :------------------------- | :------------------------------------------------ | :----------------- |
| `site.yml`                 | Build and publish documentation site              | On merge to `main` |
| `docs-validate.yml`        | Check MCP-DL headers, YAML metadata, and diagrams | On PR              |
| `stac-validate.yml`        | Validate STAC schemas and links                   | On PR / commit     |
| `pre-commit.yml`           | Lint Markdown and structure                       | Each PR            |
| `codeql.yml` / `trivy.yml` | Static and dependency security scans              | Scheduled / PR     |

---

## 🧩 Contributor Workflow

1. Create or update docs under `docs/` (add diagrams if relevant).
2. Validate locally:

```bash
make docs-validate
```

3. Commit using semantic conventions:

```bash
git commit -m "docs(architecture): clarify ETL lineage and update diagrams"
```

4. Open a PR and ensure CI checks pass.
5. Merge — the CI/CD pipeline deploys changes automatically to GitHub Pages.

> When documenting new systems, describe: **scope**, **inputs**, **outputs**, **dependencies**, **failure modes**, and **test strategy**.

---

## 🧭 Recommended Reading Order

1. `architecture/architecture.md` — **System Overview**
2. `architecture/data-architecture.md` — **Data Flow & Provenance**
3. `architecture/pipelines.md` — **ETL + AI/ML Pipelines**
4. `architecture/ci-cd.md` — **Automation & Governance**
5. `architecture/knowledge-graph.md` — **Semantic Knowledge Layer**
6. `standards/metadata-standards.md` — **Metadata, Schema, & Validation**
7. `audit/repository_compliance.md` — **Compliance & Audit Records**
8. `glossary.md` — **Canonical Terminology**

---

## 🧱 Documentation Provenance Metadata

```yaml
provenance:
  generated_by: "docs-validate.yml"
  reviewed_by: ["@kfm-docs", "@kfm-architecture"]
  last_audit: "2025-10-17"
  related_docs:
    - "docs/audit/repository_compliance.md"
    - "docs/standards/metadata-standards.md"
    - "docs/glossary.md"
```

---

## 🧷 Appendix — Doc Status Badges

| Badge                                                                        | Meaning                        |
| :--------------------------------------------------------------------------- | :----------------------------- |
| ![Status: Draft](https://img.shields.io/badge/Status-Draft-yellow)           | Early-stage or pending review  |
| ![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)    | Published and CI-validated     |
| ![Scope: Architecture](https://img.shields.io/badge/Scope-Architecture-blue) | Applies to system architecture |
| ![Scope: Pipelines](https://img.shields.io/badge/Scope-Pipelines-purple)     | Applies to ETL / ML pipelines  |

---

## 📅 Version History

| Version    | Date       | Summary                                                                                            |
| :--------- | :--------- | :------------------------------------------------------------------------------------------------- |
| **v1.2.0** | 2025-10-17 | Added compliance metadata, diagrams workflow, audit links, and updated navigation for MCP-DL v6.3. |
| **v1.1.0** | 2025-10-05 | Added governance, local preview steps, and formatting improvements.                                |
| **v1.0.0** | 2025-10-04 | Initial documentation hub; MCP-compliant base structure for `docs/`.                               |

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*"Every Document is a Blueprint. Every Blueprint is Reproducible."*
📍 [`docs/`](.) — Central documentation and architecture hub for the Kansas Frontier Matrix.

</div>
