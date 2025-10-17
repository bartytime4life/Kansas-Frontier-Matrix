<div align="center">

# 🗂️ **Kansas Frontier Matrix — Documentation Templates**  
`docs/templates/`

**Mission:** Provide reusable, standardized **templates and boilerplates** for experiments,  
standard operating procedures (SOPs), model cards, dataset records, provenance logs, and architecture decisions —  
ensuring **reproducibility, clarity, and MCP compliance** across the Kansas Frontier Matrix (KFM) ecosystem.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue?logo=markdown)](../README.md)
[![Templates](https://img.shields.io/badge/Templates-Standardized-green)](README.md)
[![Version Control](https://img.shields.io/badge/Tracked-Git%20%26%20Provenance-orange)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Documentation Templates"
version: "v1.2.0"
last_updated: "2025-10-17"
owners: ["@kfm-docs","@kfm-architecture"]
tags: ["templates","mcp","standards","reproducibility","provenance","fair","stac"]
status: "Stable"
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - DCAT 2.0
  - JSON Schema
ci_required_checks:
  - docs-validate
  - pre-commit
  - markdownlint
---
````

---

## 🎯 Purpose

The `docs/templates/` directory provides **ready-to-use Markdown templates** for contributors,
ensuring consistent structure, documentation quality, and reproducibility across all domains —
including **scientific research**, **data engineering**, **software design**, and **AI/ML experiments**.

By following these templates, every document, dataset, or workflow in KFM becomes:

* **📜 Auditable** → versioned, traceable, and linked to provenance.
* **♻️ Reproducible** → fully repeatable via structured documentation.
* **🔗 Interoperable** → aligned with MCP, STAC, DCAT, and ontology metadata.
* **🧾 Readable** → clear, standardized, and GitHub-renderable.

---

## 🗂️ Directory Overview

```bash
docs/templates/
├── README.md            # Template index (this file)
├── experiment.md        # MCP-style research & experiment log
├── sop.md               # Standard Operating Procedure template
├── model_card.md        # AI/ML model card (purpose, metrics, ethics)
├── adr.md               # Architecture Decision Record template
├── dataset.md           # Dataset descriptor (schema, license, extent)
├── provenance.md        # Provenance & checksum logging template
└── checklist.md         # Contributor / peer-review checklist
```

Each template aligns with **Master Coder Protocol (MCP)** documentation-first principles and the
**FAIR** framework (Findable, Accessible, Interoperable, Reusable).

---

## 🧩 Template Index

| Template            | Purpose                                                                                | Format   |
| :------------------ | :------------------------------------------------------------------------------------- | :------- |
| **`experiment.md`** | MCP-compliant experiment log (`Problem → Hypothesis → Method → Results → Conclusion`). | Markdown |
| **`sop.md`**        | Step-by-step reproducible process for tasks (ETL, STAC validation, ingestion).         | Markdown |
| **`model_card.md`** | AI/ML model documentation — purpose, data, metrics, deployment, risks & fairness.      | Markdown |
| **`adr.md`**        | Architecture Decision Record — context, decision, alternatives, implications.          | Markdown |
| **`dataset.md`**    | Dataset descriptor — spatial/temporal extent, schema, license, access, DCAT/STAC.      | Markdown |
| **`provenance.md`** | Provenance tracking — checksums, version IDs, lineage, SBOM/SLSA capture.              | Markdown |
| **`checklist.md`**  | Contributor/reviewer checklist for MCP, CI/CD, and metadata compliance.                | Markdown |

---

## 🧭 Usage Guide

1. **Select Template** — choose the relevant template for your task (`experiment`, `sop`, `adr`, etc.).
2. **Copy Locally** — duplicate the template into your working directory:

   ```bash
   cp docs/templates/experiment.md docs/experiments/exp_2025_ks_hydrography.md
   ```
3. **Complete Metadata Fields** — fill in author(s), dates, version, IDs, provenance.
4. **Link Related Artifacts** — reference code, data, STAC items, and ADRs.
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
| **Open Standards**      | Markdown, STAC 1.0.0, JSON Schema; optional DCAT/JSON-LD.             |
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

## 🔗 Cross-References

| Documentation                        | Description                          |
| :----------------------------------- | :----------------------------------- |
| `../architecture/pipelines.md`       | Workflow and ETL pipeline reference  |
| `../architecture/architecture.md`    | System-level architecture overview   |
| `../standards/metadata-standards.md` | Metadata and schema compliance       |
| `../glossary.md`                     | Definitions and term consistency     |
| `../audit/repository_compliance.md`  | Repository-wide compliance dashboard |

---

## 🔐 Governance & Contribution Workflow

| Step | Description                                                                    |
| :--- | :----------------------------------------------------------------------------- |
| 1️⃣  | Add/update a template — ensure YAML header & MCP-DL alignment.                 |
| 2️⃣  | Validate via pre-commit (`markdownlint`, `yamllint`) and `make docs-validate`. |
| 3️⃣  | Submit PR labeled `docs(templates)` for peer review (CODEOWNERS required).     |
| 4️⃣  | CI/CD (`site.yml`) rebuilds docs and publishes updates to Pages.               |

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                          |
| :------ | :--------- | :----------------------------------------------------------------------------------------------- |
| v1.2.0  | 2025-10-17 | Added YAML metadata, governance workflow, CI checks, and links to the compliance dashboard.      |
| v1.1.0  | 2025-10-05 | Added new templates (`dataset.md`, `provenance.md`, `checklist.md`); enhanced usage & MCP matrix |
| v1.0.0  | 2025-10-03 | Initial set of MCP-aligned documentation templates.                                              |

---

<div align="center">

🗂️ **Templates are the scaffolding of MCP reproducibility.**
Every experiment, SOP, dataset, model, and decision in Kansas Frontier Matrix starts here.

📍 `docs/templates/` — *“Define before you build. Document before you deploy.”*

</div>
