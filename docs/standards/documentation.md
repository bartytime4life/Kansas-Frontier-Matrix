<div align="center">

# 📝 Kansas Frontier Matrix — **Documentation & Writing Standards**  
`docs/standards/documentation.md`

**Master Coder Protocol (MCP-DL v6.3+) · Documentation-First · Reproducibility · Provenance · Validation**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/)
[![Docs Validated](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/docs-validate.yml?label=Docs%20Validated&color=blue)](../../.github/workflows/docs-validate.yml)
[![Site Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Site%20Build&logo=github)](../../.github/workflows/site.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Documentation & Writing Standards"
version: "v1.3.0"
last_updated: "2025-10-18"
owners: ["@kfm-docs","@kfm-architecture","@kfm-data","@kfm-security"]
tags: ["standards","documentation","markdown","mcp","governance","validation","provenance"]
status: "Stable"
scope: "Monorepo-Wide"
license: "CC-BY 4.0"
semver_policy: "MAJOR.MINOR.PATCH"
audit_framework: "MCP-DL v6.3"
ci_required_checks:
  - docs-validate
  - site-build
  - pre-commit
semantic_alignment:
  - STAC 1.0
  - DCAT 2.0
  - JSON Schema
  - ISO 8601
  - CIDOC CRM
  - OWL-Time
---
````

---

## 📚 Overview

KFM treats documentation as a **first-class artifact**: every feature, dataset, and workflow is specified, reviewed, and versioned alongside code to guarantee clarity, reproducibility, and collaborative research at scale. 
All content uses **GitHub-Flavored Markdown (GFM)** and interoperates with **open standards** (JSON Schema, STAC, DCAT) to enable machine-checkable provenance and CI validation. 

**Core principles**

| Principle                  | Description                                                                        |
| :------------------------- | :--------------------------------------------------------------------------------- |
| 🧠 **Documentation-first** | Draft before or with code/data; docs are the blueprint and source of truth.        |
| 🧩 **Consistent**          | Unified structure, headings, and style across all directories.                     |
| 🔁 **Reproducible**        | Build/run steps, parameters, and environments are explicit; outputs re-buildable.  |
| 🔗 **Provenance-tracked**  | Authorship, version, and lineage embedded; STAC/DCAT metadata cross-links.         |
| 🧾 **Auditable**           | CI enforces linting, link checks, schemas, and site build; reviews are logged.     |

---

## 🧩 Document Anatomy

Each Markdown file follows this composition for MCP traceability. 

| Section                  | Description                                              |
| :----------------------- | :------------------------------------------------------- |
| **Title Block**          | Centered `<div>` with title, file path, purpose, badges. |
| **Overview**             | Concise scope and context; link related standards.       |
| **Core Sections**        | Procedures, standards, diagrams, examples.               |
| **MCP Compliance Table** | States how the doc fulfills MCP principles.              |
| **Related Docs**         | Cross-links to standards and architecture.               |
| **Version History**      | Semantic version, date, author, concise changes.         |
| **Footer Tagline**       | KFM provenance tagline + file path.                      |

---

## 🧱 Example Header

```markdown
<div align="center">

# 🧱 Kansas Frontier Matrix — Example Title  
`path/to/file.md`

**Purpose:** Short one-sentence summary of intent.

[![Docs · MCP-DL v6.3](...)](../../docs/)  
[![License: CC-BY 4.0](...)](../../LICENSE)

</div>
```

> **Tip:** Add CI badges (docs/site, schema checks) when a doc is validated by workflows. 

---

## ✍️ Writing & Style Guide

| Category        | Requirement                              | Example                                           |
| :-------------- | :--------------------------------------- | :------------------------------------------------ |
| **Language**    | Clear, precise technical English.        | “This workflow validates all STAC items.”         |
| **Tone**        | Objective/instructional.                 | Avoid hype; favor evidence.                       |
| **Perspective** | Guides = 2nd person; Specs = 3rd person. | “You can run `make site`.”                        |
| **Tense**       | Present for process; past for results.   | “This script generates checksums.”                |
| **Voice**       | Prefer active voice.                     | ✅ “Run validation.” ❌ “Validation should be run.” |
| **Clarity**     | One idea per sentence.                   | “Use `stac-validator` to check metadata.”         |

**Accessibility & i18n (UI-facing docs)**
Follow inclusive design and ARIA practices; pair documentation for UI with clear widget and layout descriptions (e.g., timeline Canvas vs. retained-mode widget trees, a11y labels). 

---

## 🧾 Formatting Conventions

| Element         | Standard                                                               | Notes                              |
| :-------------- | :--------------------------------------------------------------------- | :--------------------------------- |
| **Headings**    | `#`, `##`, `###` hierarchy; single H1 per file.                        | Consistency enables anchors.       |
| **Tables**      | GFM tables, colon alignment; ≤ 4 columns when possible.                | Split wide tables.                 |
| **Code Blocks** | Triple backticks + language tag (`bash`, `json`, `python`, `mermaid`). | Use realistic snippets.            |
| **Lists**       | `-` unordered, `1.` ordered; 2-space indent for nesting.               |                                    |
| **Emphasis**    | `**bold**` for key terms; *italic* for context.                        | Avoid decorative emphasis.         |
| **Links**       | Prefer relative repo paths.                                            | `[architecture](../architecture/)` |
| **Badges**      | Include Docs + License; add CI badges if relevant.                     |                                    |

**Mermaid diagrams** must render on GitHub and use stable, documented patterns. Include comments, version, and minimal labels for clarity. 

---

## 🧠 Content Types & Templates

**SOPs / Experiments / ADRs / Model Cards**

* Use standardized templates for **experiments** (hypothesis → methods → data → results → analysis → conclusion) to ensure reproducibility and clarity. 
* Model cards document AI models: purpose, training data, metrics, risks, version, and license. 
* ADRs record decisions and alternatives; link to affected modules and issues.

> **Why documentation-first?** It operationalizes the scientific method, making results testable and verifiable across disciplines. 

---

## 🧮 Evidence, Citations & Provenance

* Cite primary sources, datasets, and methods in-line or footnotes; include links to STAC Items/Collections where applicable. 
* For disciplinary context (history, cartography, geology), summarize and cite foundational theory when needed to interpret data. 
* Use **versioned** dataset descriptors and checksums; embed `checksum:multihash` in STAC assets and include sidecar `.sha256` files. 

**Example inline evidence**

* Documentation-first and modular knowledge accumulation underpin MCP. 
* Interdisciplinary integrations (history/cartography/geology) guide narrative clarity and accuracy. 
* Design audit emphasizes incorporating oral histories, fire regimes, paleoclimate proxies. 

---

## 🧪 Diagrams & Media Standards

* **Mermaid**: `flowchart TD/LR`, `erDiagram`, and simple sequence diagrams with short labels; ensure legibility in GitHub renderer. 
* **Canvas/HTML5 graphics**: prefer vector/SVG for diagrams; Canvas examples acceptable for UI/visualization docs; include alt text and captions.  
* **Screenshots**: Use neutral themes; add captions and version notes.

---

## 🔧 Data, Code & Results Embedding

* Prefer short, **runnable** snippets; link to full examples or notebooks under `tools/` or `notebooks/`. 
* For **spatial examples**, provide concise STAC or CSVW metadata excerpts; show EPSG and time fields. 
* For **R workflows** and exploratory maps/analysis, show reproducible minimal examples and exported figures. 

---

## 🔍 Automated Validation

| Check           | Tool / Workflow                 | Purpose                    |
| :-------------- | :------------------------------ | :------------------------- |
| Markdown Lint   | `markdownlint-cli`              | Syntax & structure         |
| Link Validation | `remark-lint`                   | Cross-link integrity       |
| Schema & STAC   | `jsonschema` · `stac-validator` | Metadata conformance       |
| Site Build      | `.github/workflows/site.yml`    | Render & publish docs site |
| Spellcheck      | `codespell` (optional)          | Typos/wordlist             |

```bash
make docs-validate
```

> **Note:** Docs are validated alongside code in CI for consistent governance and a reproducible monorepo workflow. 

---

## 🗂 Directory Organization

| Path                 | Contents                                                           |
| :------------------- | :----------------------------------------------------------------- |
| `docs/architecture/` | System & data architecture, UI design, diagrams.                   |
| `docs/standards/`    | Governance: documentation, coding, formats, security, provenance.  |
| `docs/templates/`    | Experiment, SOP, model card templates.                             |
| `docs/glossary.md`   | Canonical domain terms & cross-disciplinary definitions.           |
| `docs/audit/`        | Repository audit, RMI/DCI dashboards, action plans.                |

Each directory **must** contain a local `README.md` with scope, structure, and version history. 

---

## 🧩 Governance & Review Workflow

| Review     | Reviewer        | Responsibility                        |
| :--------- | :-------------- | :------------------------------------ |
| Technical  | Domain Expert   | Methods, accuracy, data alignment.    |
| Editorial  | Docs Lead       | Clarity, tone, accessibility.         |
| Compliance | Governance Team | MCP alignment, provenance, CI status. |

All reviews are logged under `data/work/logs/docs/review_<filename>.log`. 

---

## 🧮 MCP Compliance Matrix

| MCP Principle           | Implementation                                                      |
| :---------------------- | :------------------------------------------------------------------ |
| **Documentation-first** | Specs/ADR drafted pre-implementation; templates enforced in PR.     |
| **Reproducibility**     | Build steps, environment, and schemas embedded; CI checks.          |
| **Open Standards**      | Markdown + JSON Schema + STAC + DCAT across docs/data.              |
| **Provenance**          | Version tables, commit metadata, STAC lineage, checksum manifests.  |
| **Auditability**        | Validation logs retained; audits published quarterly.               |

---

## 🧭 Cross-Disciplinary Writing Aids

* **History/Cartography/Geology** sections should cite disciplinary methods and limits; clarify context, uncertainty, and multiple perspectives. 
* **Modeling/Simulation** docs specify model class (ABM, DES, SD, PDE/FEA) and credibility (V&V) with assumptions and boundary conditions. 
* **UI/UX** docs describe interaction models (event-driven, retained vs. immediate vs. declarative) and accessibility considerations. 
* **Archaeology** docs address context, stratigraphy, dating methods, and field SOPs; preserve provenance and uncertainty explicitly. 

---

## 🔗 Related References

| File                                     | Purpose                                         |
| :--------------------------------------- | :---------------------------------------------- |
| `docs/standards/markdown_rules.md`       | Layout & badge rules (GFM best practices).      |
| `docs/standards/markdown_guide.md`       | Styling patterns, emojis, header anatomy.       |
| `docs/standards/coding.md`               | Code & comment style, testing & security gates. |
| `docs/standards/data-formats.md`         | Approved file/metadata formats & CI checks.     |
| `docs/architecture/data-architecture.md` | File and data architecture & STAC layout.       |
| `docs/audit/repository_compliance.md`    | Compliance dashboards & action plans.           |
| `docs/architecture/web-ui.md`            | Web UI patterns, timeline & map composition.    |

---

## 📘 Version History

| Version | Date       | Author    | Summary                                                                                                          |
| :------ | :--------- | :-------- | :--------------------------------------------------------------------------------------------------------------- |
| v1.3.0  | 2025-10-18 | @kfm-docs | Added YAML front matter, a11y/i18n, evidence & citation policy, cross-disciplinary aids, and CI matrix alignment |
| v1.2.0  | 2025-10-05 | @kfm-docs | Expanded formatting rules + CI matrix; link validation guidance                                                  |
| v1.0.0  | 2025-10-04 | @kfm-docs | Initial MCP-compliant documentation standard                                                                     |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Word Accounted For. Every Page Proven.”*
📍 `docs/standards/documentation.md` — Maintained under MCP governance and CI validation.

</div>
