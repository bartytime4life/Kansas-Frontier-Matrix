<div align="center">

# 🗂️ Kansas Frontier Matrix — Documentation Templates  
`/docs/templates/`

**Mission:** Provide reusable, standardized **templates and boilerplates** for experiments,  
standard operating procedures (SOPs), model cards, dataset records, and architecture decisions —  
ensuring **reproducibility, clarity, and MCP compliance** across the entire Kansas Frontier Matrix (KFM) ecosystem.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../README.md)
[![Templates](https://img.shields.io/badge/Templates-Standardized-green)](README.md)
[![Version Control](https://img.shields.io/badge/Tracked-Git%20%26%20Provenance-orange)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)

</div>

---

## 🎯 Purpose

The `/docs/templates/` directory provides **ready-to-use Markdown templates** for contributors,  
ensuring consistent structure, documentation quality, and reproducibility across all domains —  
including **scientific research**, **data engineering**, **software design**, and **AI/ML experiments**.

By following these templates, every document, dataset, or workflow in KFM becomes:

- **📜 Auditable** → versioned, traceable, and linked to provenance.  
- **♻️ Reproducible** → fully repeatable via structured documentation.  
- **🔗 Interoperable** → aligned with MCP, STAC, and ontology metadata.  
- **🧾 Readable** → clear, standardized, and GitHub-renderable.  

---

## 🗂️ Directory Overview

```bash
docs/templates/
├── README.md              # Template index (this file)
├── experiment.md           # MCP-style research & experiment log
├── sop.md                  # Standard Operating Procedure template
├── model_card.md           # AI/ML model card (metadata + ethics + performance)
├── adr.md                  # Architecture Decision Record template
├── dataset.md              # Dataset metadata descriptor (schema, license, extent)
├── provenance.md           # Provenance & checksum logging template
└── checklist.md            # Contributor and peer-review checklist
````

Each template aligns with **Master Coder Protocol (MCP)** documentation-first principles and the
**FAIR Data** framework (Findable, Accessible, Interoperable, Reusable).

---

## 🧩 Template Index

| Template            | Purpose                                                                                | Format   |
| :------------------ | :------------------------------------------------------------------------------------- | :------- |
| **`experiment.md`** | MCP-compliant experiment log (`Problem → Hypothesis → Method → Results → Conclusion`). | Markdown |
| **`sop.md`**        | Step-by-step reproducible process for tasks (ETL, STAC validation, ingestion).         | Markdown |
| **`model_card.md`** | AI/ML model documentation — includes purpose, data, metrics, limitations, and biases.  | Markdown |
| **`adr.md`**        | Architecture Decision Record — captures context, decision, and implications.           | Markdown |
| **`dataset.md`**    | Dataset descriptor — spatial/temporal extent, schema, license, and access method.      | Markdown |
| **`provenance.md`** | Provenance tracking — record of checksums, version IDs, and data lineage.              | Markdown |
| **`checklist.md`**  | Contributor/reviewer checklist for MCP, CI/CD, and metadata compliance.                | Markdown |

---

## 🧭 Usage Guide

1. **Select Template:** Choose the relevant template for your task (`experiment`, `sop`, `adr`, etc.).
2. **Copy Locally:** Duplicate the template into your working directory.

   ```bash
   cp docs/templates/experiment.md docs/experiments/exp_2025_ks_hydrography.md
   ```
3. **Complete Metadata Fields:** Fill in:

   * Author, date, and version
   * Dataset IDs and provenance
   * Problem statement or hypothesis
   * Steps, results, or decisions
4. **Link to Related Artifacts:** Reference associated code, data, or architecture files.
5. **Validate Format:** Run markdown lint + pre-commit checks:

   ```bash
   make validate-docs
   ```
6. **Commit with Traceable Metadata:**

   ```bash
   git commit -m "docs(experiment): add hydrology ETL validation test log"
   ```
7. **Promote to Published Doc:** Once peer-reviewed, link your file from `/docs/architecture/` or `/data/sources/`.

---

## 🧮 MCP Alignment Matrix

| MCP Principle           | Template Support                                                      |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | Every experiment, SOP, and ADR begins with a standardized template.   |
| **Reproducibility**     | Templates enforce metadata completeness and procedural repeatability. |
| **Open Standards**      | Markdown, STAC 1.0.0, and JSON Schema alignment.                      |
| **Provenance**          | Embedded fields for author, checksum, and dataset version.            |
| **Auditability**        | Templates integrate with CI/CD validation and `stac-validate.yml`.    |

---

## 📋 Example Workflows

### 🧪 Example — Experiment Log

> File: `experiment.md`

```markdown
## Problem
Assess whether terrain-derived slope influences stream density in Ellsworth County.

## Hypothesis
Higher slopes correlate with increased stream segmentation in the NHD dataset.

## Method
- Source DEM: USGS 1m LiDAR (EPSG:4326)
- Source Hydrography: NHD Flowlines 2020
- Processing: `src/pipelines/terrain/derive_slope.py`

## Results
Correlation coefficient (r²) = 0.81

## Conclusion
Slope gradient significantly affects flowline density; add derived slope to hydrology STAC metadata.
```

---

### ⚙️ Example — Standard Operating Procedure (SOP)

> File: `sop.md`

```markdown
## Purpose
Procedure for validating STAC collections before publication.

## Steps
1. Run `make stac-validate`
2. Check schema compliance in `_reports/stac_validation.json`
3. Confirm checksum and license fields exist
4. Commit result with `make checksums`

## Expected Output
All STAC items validated ✅
```

---

## 🔗 Cross-References

| Related Documentation                                                        | Description                          |
| :--------------------------------------------------------------------------- | :----------------------------------- |
| [`docs/architecture/pipelines.md`](../architecture/pipelines.md)             | Workflow and ETL pipeline reference  |
| [`docs/architecture/architecture.md`](../architecture/architecture.md)       | System-level architecture overview   |
| [`docs/standards/metadata-standards.md`](../standards/metadata-standards.md) | Metadata and schema compliance guide |
| [`docs/glossary.md`](../glossary.md)                                         | Definitions and term consistency     |

---

## 🧾 Contribution Workflow

| Step | Description                                                             |
| :--- | :---------------------------------------------------------------------- |
| 1️⃣  | Add or update a template — ensure consistent headings and MCP metadata. |
| 2️⃣  | Validate via pre-commit hooks (`markdownlint`, `yamllint`).             |
| 3️⃣  | Submit PR labeled `docs(templates)` for peer review.                    |
| 4️⃣  | CI/CD runs `site.yml` to rebuild docs and publish updates.              |

---

## 🕰️ Version History

| Version  | Date       | Summary                                                                                            |
| :------- | :--------- | :------------------------------------------------------------------------------------------------- |
| **v1.1** | 2025-10-05 | Added new templates (`dataset.md`, `provenance.md`, `checklist.md`); enhanced usage & MCP mapping. |
| **v1.0** | 2025-10-03 | Initial set of MCP-aligned documentation templates.                                                |

---

<div align="center">

🗂️ **Templates are the scaffolding of MCP reproducibility.**
Every experiment, SOP, and decision in Kansas Frontier Matrix begins here.

📍 [`/docs/templates/`](.) — *“Define before you build. Document before you deploy.”*

</div>
