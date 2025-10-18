<div align="center">

# 🗂️ **Kansas Frontier Matrix — Documentation Templates**  
`docs/templates/`

**Mission:** Provide reusable, standardized **templates and boilerplates** for experiments,  
standard operating procedures (SOPs), model cards, dataset records, provenance logs, and architecture decisions —  
ensuring **reproducibility, clarity, security, and MCP compliance** across the Kansas Frontier Matrix (KFM) ecosystem.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue?logo=markdown)](../README.md)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../.github/workflows/docs-validate.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&logo=json)](../../.github/workflows/stac-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../.github/workflows/policy-check.yml)
[![Security](https://img.shields.io/badge/security-CodeQL%20%7C%20Trivy-red)](../../.github/workflows/)
[![SBOM & SLSA](https://img.shields.io/badge/Supply--Chain-SBOM%20%7C%20SLSA-green)](../../.github/workflows/sbom.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Documentation Templates"
version: "v1.3.0"
last_updated: "2025-10-18"
owners: ["@kfm-docs","@kfm-architecture"]
tags: ["templates","mcp","standards","reproducibility","provenance","fair","stac","security","ai","ethics"]
status: "Stable"
license: "CC-BY 4.0"
ci_required_checks:
  - docs-validate
  - pre-commit
  - markdownlint
  - policy-check
semantic_alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - DCAT 2.0
  - JSON Schema
  - FAIR Principles
  - CIDOC CRM
  - OWL-Time
  - GeoSPARQL
---
```

---

## 🎯 Purpose

The `docs/templates/` directory provides **ready-to-use Markdown templates** for contributors,
ensuring consistent structure, documentation quality, and reproducibility across all domains —
including **scientific research**, **data engineering**, **software design**, and **AI/ML experiments**.

By following these templates, every document, dataset, or workflow in KFM becomes:

* **📜 Auditable** → versioned, traceable, and linked to provenance & checksums.  
* **♻️ Reproducible** → fully repeatable via structured metadata and SOPs.  
* **🔗 Interoperable** → aligned with MCP, STAC, DCAT, OWL-Time, and ontology metadata.  
* **🧾 Readable** → clear, standardized, and GitHub-renderable with Docs-as-Code validation.  

---

## 🗂️ Directory Overview

```bash
docs/templates/
├── README.md            # Template index (this file)
├── experiment.md        # MCP-style research & experiment log
├── sop.md               # Standard Operating Procedure template
├── model_card.md        # AI/ML model card (purpose, metrics, ethics)
├── adr.md               # Architecture Decision Record template
├── dataset.md           # Dataset descriptor (schema, license, extent, STAC/DCAT)
├── provenance.md        # Provenance & checksum logging template (PROV-O, SBOM/SLSA refs)
└── checklist.md         # Contributor / peer-review checklist
```

Each template aligns with **Master Coder Protocol (MCP)** documentation-first principles and the
**FAIR** framework (Findable, Accessible, Interoperable, Reusable).

> Every template includes a **frontmatter block** (`title`, `version`, `last_updated`, `owners`) and sections for **scope, inputs, outputs, dependencies, failure modes, and test strategy**.

---

## 🧩 Template Index

| Template            | Purpose                                                                                  | Format   |
| :------------------ | :---------------------------------------------------------------------------------------- | :------- |
| **`experiment.md`** | MCP-compliant experiment log (`Problem → Hypothesis → Method → Results → Conclusion`).   | Markdown |
| **`sop.md`**        | Step-by-step reproducible process for tasks (ETL, STAC validation, ingestion).           | Markdown |
| **`model_card.md`** | AI/ML model documentation — purpose, data, metrics, bias/quality gates, deployment.      | Markdown |
| **`adr.md`**        | Architecture Decision Record — context, decision, alternatives, implications, rollbacks. | Markdown |
| **`dataset.md`**    | Dataset descriptor — extent, schema, license, access, DCAT/STAC mapping, ethics.         | Markdown |
| **`provenance.md`** | Provenance tracking — checksums, version IDs, lineage, SBOM/SLSA capture.                | Markdown |
| **`checklist.md`**  | Contributor/reviewer checklist for MCP, CI/CD, and metadata compliance.                  | Markdown |

---

## 🧭 Usage Guide

1. **Select Template** — choose the relevant template (`experiment`, `sop`, `adr`, etc.).  
2. **Copy Locally** — duplicate into your working directory:

   ```bash
   cp docs/templates/experiment.md docs/experiments/exp_2025_ks_hydrography.md
   ```

3. **Complete Metadata** — fill in authors, dates, version, IDs, **provenance** and **ethics** fields.  
4. **Link Artifacts** — reference code, data, STAC items, ADRs, and CI runs.  
5. **Validate Format** — run linting and CI checks:

   ```bash
   make docs-validate
   ```

6. **Commit with Traceable Metadata**

   ```bash
   git commit -m "docs(experiment): add hydrology ETL validation log"
   ```

7. **Publish** — after peer review, link from `docs/architecture/` and dataset STAC.

---

## 🧮 MCP Alignment Matrix

| MCP Principle           | Template Support                                                      |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | All artifacts begin with a standardized, versioned template.          |
| **Reproducibility**     | Enforced metadata completeness and procedural repeatability.          |
| **Open Standards**      | Markdown, STAC 1.0, JSON Schema; optional DCAT/JSON-LD.              |
| **Provenance**          | Author, checksum, dataset version, ADR/PR links in each template.     |
| **Auditability**        | Integrates with CI/CD (`docs-validate`, `stac-validate`, pre-commit). |

---

## 📋 Example Workflows

### 🧪 Example — Experiment Log (`experiment.md`)

```markdown
## Problem
Assess whether terrain-derived slope influences stream density in Ellsworth County.

## Hypothesis
Steeper slopes increase stream segmentation in the NHD dataset.

## Method
- DEM: USGS 1m LiDAR (EPSG:4326)
- Hydrography: NHD Flowlines 2020
- Script: src/pipelines/terrain/derive_slope.py

## Results
r² = 0.81 (p < 0.01)

## Conclusion
Slope gradient materially affects flowline density; add slope to hydrology STAC metadata.
```

### ⚙️ Example — SOP (`sop.md`)

```markdown
## Purpose
Validate STAC collections prior to publication.

## Steps
1. `make stac-validate`
2. Inspect `_reports/stac_validation.json`
3. Confirm checksum & license
4. `make checksums` and commit manifest
```

---

## 🔐 Governance & Contribution Workflow

| Step | Description                                                                    |
| :--- | :----------------------------------------------------------------------------- |
| 1️⃣  | Add/update a template — ensure YAML header & MCP-DL alignment.                 |
| 2️⃣  | Validate via pre-commit (`markdownlint`, `yamllint`) and `make docs-validate`. |
| 3️⃣  | Submit PR labeled `docs(templates)` for peer review (CODEOWNERS required).     |
| 4️⃣  | CI/CD (`site.yml`) rebuilds docs and publishes updates to Pages.               |

---

## 🔍 CI/CD Validation of Templates

| Workflow             | Function                                    | Trigger |
| :------------------- | :------------------------------------------- | :------ |
| `docs-validate.yml`  | Lint Markdown, check links & frontmatter     | PR      |
| `policy-check.yml`   | Block missing fields (title/version/owners)  | PR      |
| `stac-validate.yml`  | Validate any embedded STAC & links           | PR      |
| `pre-commit.yml`     | Local fast checks (lint, style, actionlint)  | PR      |

> **Mermaid diagrams** must end with `%% END OF MERMAID`. Add thumbnails/exports under `docs/architecture/diagrams/exported/` when used.

---

## 🔗 Cross-References

| Documentation                        | Description                          |
| :----------------------------------- | :----------------------------------- |
| `../architecture/pipelines.md`       | Workflow and ETL pipeline reference  |
| `../architecture/architecture.md`    | System-level architecture overview   |
| `../standards/markdown_rules.md`     | House Markdown rules & patterns      |
| `../standards/markdown_guide.md`     | Styling cheatsheet & examples        |
| `../standards/metadata-standards.md` | Metadata and schema compliance       |
| `../glossary.md`                     | Definitions and term consistency     |
| `../audit/repository_compliance.md`  | Repository-wide compliance dashboard |

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                             |
| :------ | :--------- | :-------------------------------------------------------------------------------------------------- |
| **v1.3.0** | 2025-10-18 | Added policy-as-code gate, supply-chain badges, docs-validate integration call-outs, and FAIR links. |
| **v1.2.0** | 2025-10-17 | Added YAML metadata, governance workflow, CI checks, and links to the compliance dashboard.         |
| **v1.1.0** | 2025-10-05 | Added new templates (`dataset.md`, `provenance.md`, `checklist.md`); enhanced usage & MCP matrix    |
| **v1.0.0** | 2025-10-03 | Initial set of MCP-aligned documentation templates.                                               |

---

<div align="center">

🗂️ **Templates are the scaffolding of MCP reproducibility.**  
Every experiment, SOP, dataset, model, and decision in Kansas Frontier Matrix starts here.

📍 `docs/templates/` — *“Define before you build. Document before you deploy.”*

</div>