<div align="center">

# 📚 **Kansas Frontier Matrix — Documentation System (v2.0.0 · Tier-Ω+∞ Certified)**  
`docs/README.md`

**Mission:** Be the **single source of truth** for the **Kansas Frontier Matrix (KFM)** — connecting technical, architectural, design, data, and governance docs under a **reproducible, auditable, FAIR/CARE-aligned** framework.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue?logo=markdown)](../docs/)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&logo=json)](../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy&logo=github)](../.github/workflows/site.yml)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../.github/workflows/docs-validate.yml)
[![Security](https://img.shields.io/badge/security-CodeQL%20%7C%20Trivy-red?logo=github)](../.github/workflows/)
[![SBOM & SLSA](https://img.shields.io/badge/Supply--Chain-SBOM%20%7C%20SLSA-green)](../.github/workflows/sbom.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Documentation System"
document_type: "Documentation Hub"
version: "v2.0.0"
last_updated: "2025-11-15"
owners: ["@kfm-docs","@kfm-architecture","@kfm-accessibility"]
maturity: "Production"
status: "Stable"
license: "CC-BY 4.0"
tags: ["documentation","mcp","standards","architecture","ci","cd","governance","ai","ethics","fair","care"]
alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - DCAT 2.0
  - CIDOC CRM
  - OWL-Time
  - GeoSPARQL
  - WCAG 2.1 AA / 3.0 readiness
  - FAIR / CARE
validation:
  docs_ci_required: true
  frontmatter_required: ["title","version","last_updated","owners","license"]
  mermaid_end_marker: "<!-- END OF MERMAID -->"
observability:
  endpoint: "https://metrics.kfm.ai/docs"
  metrics: ["docs_build_status","link_errors","frontmatter_coverage","diagram_parse_rate"]
preservation_policy:
  retention: "build logs 90d · artifacts 30d · releases permanent"
  checksum_algorithm: "SHA-256"
---
```

---

## 📖 Overview

`docs/` is the **canonical knowledge base** for KFM. Every change to code, data, models, or UI **must** be reflected here and verified by CI (**docs-validate.yml**). We treat docs as **executable specifications**: diagrams, schemas, SOPs, and ADRs drive implementation and governance.

### MCP Principles Applied

- 🧠 **Documentation-first** — author the spec before writing code.  
- ♻️ **Reproducibility** — `make site` produces the same output locally and in CI.  
- 🌐 **Open Standards** — Markdown/MDX, JSON Schema, STAC/DCAT, Mermaid, FAIR.  
- 🧩 **Provenance** — each page declares authorship, version, and metadata.  
- 🧾 **Auditability** — CI enforces headers, links, diagrams, and schema conformance.

---

## 🗂️ Directory Layout

```bash
docs/
├── README.md                        # Documentation hub (this file)
├── architecture/                    # System, data, API, CI/CD, web architecture
│   ├── system-architecture-overview.md
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
├── design/                          # Design system, a11y, mockups, reviews
│   ├── mockups/README.md
│   ├── reviews/
│   └── standards/
├── standards/                       # Style guides & validation protocols
│   ├── markdown_rules.md
│   ├── markdown_guide.md
│   ├── metadata-standards.md
│   ├── naming-conventions.md
│   └── validation-protocols.md
├── templates/                       # MCP templates (SOPs, experiments, model cards)
│   ├── sop.md
│   ├── experiment.md
│   └── model_card.md
├── audit/                           # Compliance audits and governance reports
│   ├── repository_compliance.md
│   └── governance_matrix.md
├── adr/                             # Architecture Decision Records
│   └── ADR-####-kebab-slug.md
└── glossary.md                      # Cross-disciplinary term index
```

> Each subdirectory starts with a **front-matter block** stating **scope**, **owners**, and **compliance metadata**.

---

## 🧭 Quick Navigation

| Category                  | Description                                | Primary Docs                                                                                                 |
|:--------------------------|:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| 🧱 **Architecture**       | System & data blueprints                   | `architecture/system-architecture-overview.md`                                                               |
| ⚙️ **Pipelines**          | ETL & AI/ML automation                     | `architecture/pipelines.md`                                                                                  |
| 🌐 **Web & API**          | Frontend and programmatic access           | `architecture/web-ui-architecture.md`, `architecture/api-architecture.md`                                    |
| 🧠 **Knowledge Graph**    | Ontologies, schema, reasoning              | `architecture/knowledge-graph.md`                                                                            |
| 🔄 **CI/CD**              | Validation, security, supply chain         | `architecture/ci-cd.md`                                                                                      |
| 📏 **Standards**          | Metadata, naming, validation guides        | `standards/metadata-standards.md`                                                                            |
| 🧪 **Templates**          | SOPs, experiments, model cards             | `templates/`                                                                                                 |
| 🧩 **Gov & Audits**       | Compliance tracking and MCP validation     | `audit/repository_compliance.md`                                                                             |
| 📚 **Glossary**           | Canonical terminology                      | `glossary.md`                                                                                                |
| 🎨 **Design Archive**     | Mockups & wireframes (trace to code)       | `design/mockups/README.md`                                                                                   |

---

## 🧭 Recommended Reading Order

1) **System Overview** → `architecture/system-architecture-overview.md`  
2) **Data Flow & Provenance** → `architecture/data-architecture.md`  
3) **ETL & AI** → `architecture/pipelines.md`  
4) **CI/CD Governance** → `architecture/ci-cd.md`  
5) **Knowledge Graph** → `architecture/knowledge-graph.md`  
6) **Standards** → `standards/metadata-standards.md`  
7) **Audits & ADRs** → `audit/repository_compliance.md`, `adr/`  
8) **Glossary** → `glossary.md`

---

## 🧮 Diagrams & Visuals

All diagrams are authored in **Mermaid** and version-controlled.  
Generate or export:

```bash
make diagrams      # renders diagrams to docs/architecture/diagrams/exported/
```

Embed exports with relative paths:

```md
![System Overview](architecture/diagrams/exported/system_overview.svg)
```

> **Rule:** Mermaid blocks **must** end with `<!-- END OF MERMAID -->` (CI-enforced).

---

## 🧪 Render & Deploy

Docs are built/deployed via **site.yml** (GitHub Actions) using the same reproducible infrastructure as data pipelines.

| Task                | Command                               | Output                  |
|:--------------------|:-------------------------------------- |:------------------------|
| **Build docs**      | `make site`                           | `_site/` (static site)  |
| **Preview locally** | `python -m http.server -d _site 8000` | `http://localhost:8000` |
| **Deploy (CI/CD)**  | Merge to `main`                       | GitHub Pages            |

**CI gates:** `docs-validate.yml` (front-matter + link check + diagram parse), `policy-check.yml` (required fields), `stac-validate.yml` (when docs reference datasets).

---

## 🧠 Writing & Formatting Guide

- Use **GFM**; keep lines ≤ 120 chars. Prefer active voice and concise sentences.  
- Headings:

```md
## Section
### Subsection
#### Detail
```

- Code blocks:

```bash
make site
```

```python
print("Kansas Frontier Matrix")
```

- **Tables** use header alignment and concise labels.  
- **Front-matter Template** (required):

```yaml
---
title: "Doc Title"
version: "vX.Y.Z"
last_updated: "YYYY-MM-DD"
owners: ["@kfm-docs"]
license: "CC-BY 4.0"
---
```

---

## 🔐 Security, Supply Chain & Provenance (Docs)

- **SBOM & SLSA:** Documentation build artifacts attach SBOM + provenance in releases.  
- **Policy-as-Code:** `policy-check.yml` blocks docs missing `title|version|last_updated|owners|license`.  
- **Retention:** Build logs ≥ 90d; provenance JSON under `artifacts/`.  
- **Action Pinning:** Any docs workflows use pinned versions or SHAs.

---

## 📈 Observability & Quality Metrics (DQI)

```yaml
docs_quality_index:
  frontmatter_coverage_pct: 100
  link_error_count: 0
  diagram_parse_rate_pct: 100
  a11y_alt_text_coverage_pct: 100
  thresholds:
    min_frontmatter_coverage: 100
    max_link_errors: 0
```

A live dashboard at **https://metrics.kfm.ai/docs** shows build status and drift detection.

---

## 🤖 AI-Assisted Documentation Checks

```yaml
ai_validation:
  model: "kfm-gpt-docs-lint-v2"
  scope: ["missing sections","broken anchors","inconsistent terminology"]
  confidence_threshold: 0.9
  outputs:
    - "docs_ai_report.json"
```

- AI suggestions are **recommendations**, not auto-edits.  
- All AI-suggested diffs require `@kfm-docs` review.

---

## 🌍 Localization & Accessibility (Docs)

- Use neutral English and **plain language** (≤ Grade 9).  
- Provide **alt text** for all images/figures.  
- RTL & pseudo-locale (`en-XA`) examples should be noted when doc content includes UI text.  
- **WCAG** docs style: adequate contrast in figure callouts, no color-only meaning in diagrams.

---

## 🧭 ADR Index (Decisions)

`docs/adr/` holds **Architecture Decision Records**:

```text
docs/adr/
├── ADR-0001-adopt-stac.md
├── ADR-0012-graph-schema-cidoc.md
└── ADR-0048-ai-metadata-embedding.md
```

Every ADR uses the template with **status**, **decision_date**, **reviewed_by**, **commit**, and links to related PRs.

---

## 🔍 CI/CD Validation of Documentation

| Workflow                   | Function                                          | Trigger            |
|:---------------------------|:--------------------------------------------------|:-------------------|
| `site.yml`                 | Build and publish documentation site              | Merge → `main`     |
| `docs-validate.yml`        | Check front-matter, links, diagrams               | PR                 |
| `stac-validate.yml`        | Validate STAC schemas and links                   | PR / commit        |
| `policy-check.yml`         | Verify required metadata fields                   | PR                 |
| `pre-commit.yml`           | Lint Markdown and structure                       | PR                 |

---

## 🧾 Contributor Workflow

1. Create or update docs under `docs/`.  
2. Validate locally:

```bash
make docs-validate
```

3. Commit using semantic conventions:

```bash
git commit -m "docs(architecture): clarify ETL lineage & update system diagram"
```

4. Open a PR and ensure CI is green.  
5. Merge → CI deploys to GitHub Pages.

> Describe **scope**, **inputs**, **outputs**, **dependencies**, **failure modes**, and **test strategy** for new systems.

---

## 🔄 Versioning & Release Governance

```yaml
versioning:
  policy: "Semantic Versioning (MAJOR.MINOR.PATCH)"
  docs_tag_pattern: "docs-v*"
  release_notes: true
  doi_on_major: true
  changelog_dir: "docs/changelog/"
  auto_changelog_from_commits: true
```

**When to bump:**
- **Major:** Information architecture or standards overhaul  
- **Minor:** New sections/templates/diagrams  
- **Patch:** Typos, small clarifications, link fixes

### 📘 Version History (Docs)

| Version | Date | Summary |
|:--|:--|:--|
| **v2.0.0** | 2025-11-15 | Tier-Ω+∞ upgrade: added ADR index, AI docs lint, DQI metrics, localization guidance, governance/versioning section. |
| v1.3.0 | 2025-10-18 | Added docs-validate, policy-as-code, supply-chain badges, FAIR/GeoSPARQL alignment. |
| v1.2.0 | 2025-10-17 | Added diagrams workflow, audit links, MCP front-matter validation. |
| v1.1.0 | 2025-10-05 | Added governance & local preview steps. |
| v1.0.0 | 2025-10-04 | Initial documentation hub. |

---

## 🔗 Related Documents & Indices

- `architecture/system-architecture-overview.md`  
- `architecture/ci-cd.md`  
- `design/mockups/README.md`  
- `standards/metadata-standards.md`  
- `audit/repository_compliance.md`  
- `adr/` (decision registry)  
- `glossary.md`

---

## 🧱 Documentation Provenance Metadata (auto-injected)

```yaml
provenance:
  generated_by: "docs-validate.yml"
  reviewers: ["@kfm-docs","@kfm-architecture"]
  last_audit: "2025-11-15"
  artifacts:
    - "artifacts/docs/provenance.json"
  checksums:
    - "artifacts/docs/readme.sha256"
  dashboards:
    - "https://metrics.kfm.ai/docs"
```

---

## 🧷 Appendix — Doc Status Badges

| Badge                                                                        | Meaning                        |
|:-----------------------------------------------------------------------------|:-------------------------------|
| ![Status: Draft](https://img.shields.io/badge/Status-Draft-yellow)           | Early-stage or pending review  |
| ![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)    | Published and CI-validated     |
| ![Scope: Architecture](https://img.shields.io/badge/Scope-Architecture-blue) | Applies to system architecture |
| ![Scope: Pipelines](https://img.shields.io/badge/Scope-Pipelines-purple)     | Applies to ETL / ML pipelines  |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*“Every Document is a Blueprint — and every Blueprint is Reproducible.”*  
📍 [`docs/`](.) — Central documentation hub for the Kansas Frontier Matrix.

</div>