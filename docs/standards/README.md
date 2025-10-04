<div align="center">

# 📐 Kansas Frontier Matrix — Standards (`/docs/standards/`)

**Mission:** Define and maintain **project-wide standards** for code,  
data formats, metadata, and documentation to ensure **clarity,  
reproducibility, and interoperability** across the Kansas Frontier Matrix (KFM).  

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)  

</div>

---

## 🎯 Purpose

The `/docs/standards/` directory consolidates **technical and scientific standards**  
followed by KFM. These ensure that every dataset, pipeline, and UI component  
is **auditable, reproducible, and interoperable** across disciplines.  

This directory covers:  
- 📜 **Coding standards** (Python, JavaScript, CSS).  
- 🌍 **Data & file formats** (GeoJSON, Cloud-Optimized GeoTIFF, CSV/JSON).  
- 🗂️ **Metadata & ontologies** (STAC, DCAT, CIDOC CRM, OWL-Time, PeriodO).  
- 🔒 **Security & governance** (Trivy, CodeQL, provenance logs).  
- 🧭 **Documentation conventions** (MCP templates, README rules).  

---

## 📚 Contents

```text
docs/standards/
├── README.md               # Index (this file)
├── coding.md               # Python, JS, CSS coding standards
├── data-formats.md         # File format standards (GeoJSON, COG, CSV, JSON)
├── metadata.md             # Metadata models (STAC, DCAT, schema.org)
├── ontologies.md           # CIDOC CRM, OWL-Time, PeriodO, semantic web links
├── testing.md              # Testing & validation standards
├── security.md             # Security, scanning, licensing compliance
└── documentation.md        # MCP templates, README/ADR style, Git standards


⸻

🗂️ Key Standards
	•	Coding:
	•	Python (PEP8 + Black + Ruff)
	•	JavaScript (ES6+, Prettier, ESLint)
	•	CSS (BEM naming, design tokens)
	•	Data Formats:
	•	Vectors → GeoJSON
	•	Rasters → Cloud-Optimized GeoTIFF (COG)
	•	Tables → CSV (RFC 4180) with sidecar .json schema
	•	Checksums → SHA-256 sidecars
	•	Metadata:
	•	Catalogs → STAC 1.0.0 ￼
	•	Dataset descriptors → JSON with DCAT alignment
	•	Documentation → MCP experiment, SOP, model card templates
	•	Ontologies & Semantics:
	•	Cultural heritage → CIDOC CRM ￼
	•	Temporal alignment → OWL-Time ￼ ￼
	•	Historical periods → PeriodO ￼
	•	Testing & CI/CD:
	•	All new data validated against JSON Schema + STAC.
	•	All code passes unit + integration tests (/tests/).
	•	GitHub Actions enforce CodeQL + Trivy scans.
	•	Documentation:
	•	Every directory has a README.md (purpose, usage, dependencies).
	•	All experiments logged in docs/templates/experiment.md.
	•	ADR-style notes for major design decisions.

⸻

🧭 Usage
	1.	Before coding — review coding.md for language-specific rules.
	2.	Before ingesting data — check data-formats.md + metadata.md.
	3.	Before publishing — run STAC validation & schema checks.
	4.	For new contributors — follow documentation.md to match style.

⸻

🔗 Related Docs
	•	Architecture
	•	Integration
	•	Design
	•	Glossary

⸻


<div align="center">


📐 Standards are the backbone of reproducibility.
Every commit must uphold them, every dataset must document them.

</div>