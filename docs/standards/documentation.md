<div align="center">

# 📝 Kansas Frontier Matrix — **Documentation & Writing Standards**  
`docs/standards/documentation.md`

**Master Coder Protocol (MCP-DL v6.3+) · Documentation-First · Reproducibility · Provenance · Validation · Security**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/)
[![Docs Validated](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/docs-validate.yml?label=Docs%20Validated&color=blue)](../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../.github/workflows/policy-check.yml)
[![Site Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Site%20Build&logo=github)](../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&color=green)](../../.github/workflows/stac-validate.yml)
[![Security](https://img.shields.io/badge/security-CodeQL%20%7C%20Trivy%20%7C%20Gitleaks-red)](../../.github/workflows/)
[![SBOM](https://img.shields.io/badge/SBOM-Syft%20%7C%20SPDX-green)](../../.github/workflows/sbom.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Documentation & Writing Standards"
version: "v1.4.0"
last_updated: "2025-10-18"
owners: ["@kfm-docs","@kfm-architecture","@kfm-data","@kfm-security","@kfm-ai"]
tags: ["standards","documentation","markdown","mcp","governance","validation","provenance","policy","a11y","i18n"]
status: "Stable"
scope: "Monorepo-Wide"
license: "CC-BY 4.0"
semver_policy: "MAJOR.MINOR.PATCH"
audit_framework: "MCP-DL v6.3"
ci_required_checks:
  - docs-validate
  - policy-check
  - site-build
  - pre-commit
semantic_alignment:
  - STAC 1.0
  - DCAT 2.0
  - JSON Schema
  - ISO 8601
  - CIDOC CRM
  - OWL-Time
  - GeoSPARQL
  - FAIR Principles
---
```

---

## 📚 Overview

KFM treats documentation as a **first-class artifact**: every feature, dataset, and workflow is specified, reviewed, and versioned alongside code to guarantee clarity, reproducibility, and collaborative research at scale.  
All content uses **GitHub-Flavored Markdown (GFM)** and interoperates with **open standards** (JSON Schema, STAC, DCAT, FAIR) to enable machine-checkable provenance and CI validation.

**Core principles**

| Principle                  | Description                                                                        |
| :------------------------- | :--------------------------------------------------------------------------------- |
| 🧠 **Documentation-first** | Draft before or with code/data; docs are the blueprint and source of truth.        |
| 🧩 **Consistent**          | Unified structure, headings, and style across all directories.                     |
| 🔁 **Reproducible**        | Build/run steps, parameters, and environments are explicit; outputs re-buildable.  |
| 🔗 **Provenance-tracked**  | Authorship, version, and lineage embedded; STAC/DCAT metadata cross-links.         |
| 🧾 **Auditable**           | CI enforces linting, link checks, schemas, policy gates, and site build.            |
| 🔐 **Secure**              | No secrets in docs; supply-chain metadata (SBOM links) where relevant.             |

---

## 🧩 Document Anatomy

Each Markdown file follows this composition for MCP traceability.

| Section                  | Description                                                 |
| :----------------------- | :---------------------------------------------------------- |
| **Title Block**          | Centered `<div>` with title, file path, purpose, badges.    |
| **Overview**             | Concise scope and context; link related standards.          |
| **Core Sections**        | Procedures, standards, diagrams, examples.                  |
| **MCP Compliance Table** | States how the doc fulfills MCP principles.                 |
| **Related Docs**         | Cross-links to standards and architecture.                  |
| **Version History**      | Semantic version, date, author, concise changes.            |
| **Footer Tagline**       | KFM provenance tagline + file path.                         |

---

## 🧱 Example Header

```markdown
<div align="center">

# 🧱 Kansas Frontier Matrix — Example Title  
`path/to/file.md`

**Purpose:** Short one-sentence summary of intent.

[![Docs · MCP-DL v6.3](...)](../../docs/)
[![Docs Validated](...)](../../.github/workflows/docs-validate.yml)
[![License: CC-BY 4.0](...)](../../LICENSE)

</div>
```

> **Tip:** Add CI badges (docs/site/policy) when a doc is validated by workflows.

---

## ✍️ Writing & Style Guide

| Category        | Requirement                              | Example                                           |
| :-------------- | :--------------------------------------- | :------------------------------------------------ |
| **Language**    | Clear, precise technical English.        | “This workflow validates all STAC items.”         |
| **Tone**        | Objective/instructional.                 | Avoid hype; favor evidence.                       |
| **Perspective** | Guides = 2nd person; Specs = 3rd person. | “You can run `make site`.”                        |
| **Tense**       | Present for process; past for results.   | “This script generates checksums.”                |
| **Voice**       | Prefer active voice.                     | ✅ “Run validation.” · ❌ “Validation should be run.” |
| **Clarity**     | One idea per sentence.                   | “Use `stac-validator` to check metadata.”         |

**Accessibility & i18n (UI facing)**  
Follow inclusive/WCAG 2.1 AA practices; document ARIA roles/labels and keyboard flows; describe motion preferences and localization constraints when relevant.

---

## 🧾 Formatting Conventions

| Element         | Standard                                                               | Notes                              |
| :-------------- | :--------------------------------------------------------------------- | :--------------------------------- |
| **Headings**    | `#`, `##`, `###` hierarchy; single H1 per file.                        | Consistency enables anchors.       |
| **Tables**      | GFM tables, colon alignment; ≤ 4 columns where possible.               | Split wide tables.                 |
| **Code Blocks** | Triple backticks + language tag (`bash`, `json`, `python`, `mermaid`). | Use realistic snippets.            |
| **Lists**       | `-` unordered, `1.` ordered; 2-space indent for nesting.               |                                    |
| **Emphasis**    | `**bold**` for key terms; *italic* for context.                        | Avoid decorative emphasis.         |
| **Links**       | Prefer relative repo paths.                                            | `[architecture](../architecture/)` |
| **Badges**      | Include Docs + License; add CI badges if relevant.                     | CI must actually cover the doc.    |

**Mermaid diagrams** must render on GitHub, include `%% END OF MERMAID`, and use legible labels.

---

## 🧠 Content Types & Templates

Use standardized templates:

- **Experiments** — hypothesis → methods → data → results → analysis → conclusion.  
- **Model Cards** — purpose, data, metrics, risks, ethics, deployment, version.  
- **ADRs** — context, decision, alternatives, implications, validation evidence.  
- **SOPs** — step-by-step process with acceptance gates and runbooks.

> **Why documentation-first?** It operationalizes the scientific method and ensures verifiable results.

---

## 🧮 Evidence, Citations & Provenance

- Cite primary sources, datasets, and methods; link **STAC Items/Collections** where appropriate.  
- Use **versioned** dataset descriptors and checksums; embed `checksum:multihash` in STAC assets and include sidecar `.sha256` files.  
- Include container digests/SBOM links for build artifacts when documenting pipelines.

**Inline evidence examples**

- Design audits emphasize integrating oral histories, fire regimes, paleoclimate proxies where relevant to Kansas history.  
- ETL design references STAC lineage and checksums for deterministic regeneration.

---

## 🧪 Diagrams & Media Standards

- **Mermaid:** `flowchart TD/LR`, `sequenceDiagram`, `erDiagram` with concise text; end with `%% END OF MERMAID`.  
- **Graphics:** prefer vector/SVG; Canvas examples acceptable for UI docs; include alt text and captions.  
- **Screenshots:** Neutral theme; captions and version notes.

---

## 🔧 Data, Code & Results Embedding

- Prefer short, **runnable** snippets; link to full examples or notebooks under `tools/` or `notebooks/`.  
- **Spatial examples:** provide STAC or CSVW metadata excerpts; show EPSG and time fields.  
- **R/Python workflows:** include minimal reproducible examples and exported figures.

---

## 🔍 Automated Validation

| Check              | Tool / Workflow                 | Purpose                    |
| :----------------- | :------------------------------ | :------------------------- |
| Markdown Lint      | `markdownlint-cli`              | Syntax & structure         |
| Link Validation    | `remark-lint`                   | Cross-link integrity       |
| Policy Gate        | **OPA/Conftest** (`policy-check.yml`) | Required front-matter/fields |
| Schema & STAC      | `jsonschema` · `stac-validator` | Metadata conformance       |
| Site Build         | `.github/workflows/site.yml`    | Render & publish docs site |
| Spellcheck (opt)   | `codespell`                     | Typos/wordlist             |

```bash
make docs-validate
```

> Docs are validated alongside code in CI for consistent governance and a reproducible monorepo workflow.

---

## 🗂 Directory Organization

| Path                 | Contents                                                           |
| :------------------- | :----------------------------------------------------------------- |
| `docs/architecture/` | System & data architecture, UI design, diagrams.                   |
| `docs/standards/`    | Governance: documentation, coding, formats, security, provenance.  |
| `docs/templates/`    | Experiment, SOP, model card, dataset, ADR, provenance templates.   |
| `docs/glossary.md`   | Canonical domain terms & cross-disciplinary definitions.           |
| `docs/audit/`        | Repository audit, RMI/DCI dashboards, action plans.                |

Each directory **must** include a local `README.md` with scope, ownership, and version history.

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

- **History/Cartography/Geology:** cite disciplinary methods; clarify context, uncertainty, and multiple perspectives.  
- **Modeling/Simulation:** specify model class (ABM, DES, SD, PDE/FEA) and credibility (V&V); list assumptions/boundary conditions.  
- **UI/UX:** describe interaction models (event-driven, retained vs. immediate vs. declarative) and a11y requirements.  
- **Archaeology:** address context, stratigraphy, dating methods; preserve provenance and uncertainty explicitly.

---

## 🔗 Related References

| File                                     | Purpose                                         |
| :--------------------------------------- | :---------------------------------------------- |
| `docs/standards/markdown_rules.md`       | Layout & badge rules (GFM best practices)       |
| `docs/standards/markdown_guide.md`       | Styling patterns, emojis, header anatomy        |
| `docs/standards/coding.md`               | Code & comment style, testing & security gates  |
| `docs/standards/data-formats.md`         | Approved file/metadata formats & CI checks      |
| `docs/architecture/data-architecture.md` | File and data architecture & STAC layout        |
| `docs/audit/repository_compliance.md`    | Compliance dashboards & action plans            |

---

## 📘 Version History

| Version | Date       | Author      | Summary                                                                                                                       |
| :------ | :--------- | :---------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **v1.4.0** | 2025-10-18 | @kfm-docs   | Added policy gate, security badges (Gitleaks/SBOM), a11y/i18n guidance, expanded evidence policy, and stronger MCP alignment. |
| **v1.3.0** | 2025-10-18 | @kfm-docs   | YAML front matter, evidence & citation policy, cross-disciplinary aids, CI matrix alignment                                   |
| **v1.2.0** | 2025-10-05 | @kfm-docs   | Expanded formatting rules + CI matrix; link validation guidance                                                               |
| **v1.0.0** | 2025-10-04 | @kfm-docs   | Initial MCP-compliant documentation standard                                                                                 |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Word Accounted For. Every Page Proven.”*  
📍 `docs/standards/documentation.md` — Maintained under MCP governance and CI validation.

</div>