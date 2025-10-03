<div align="center">

# 🏗️ Kansas Frontier Matrix — Architecture Docs (`/docs/architecture/`)

**Mission:** Centralize all **architecture blueprints, flow diagrams, and system design docs**  
for the Kansas Frontier Matrix (KFM), ensuring **clarity, reproducibility, and MCP compliance**.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)  
[![Architecture](https://img.shields.io/badge/Architecture-Diagram-green)](architecture.md)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  

</div>

---

## 🎯 Purpose

The `/docs/architecture/` directory is the **canonical reference** for how the  
Kansas Frontier Matrix system is designed and connected.  

It includes:
- High-level **system architecture** overviews.  
- Detailed **data & file architecture** layouts.  
- **Web UI & API** architecture and flow diagrams.  
- Design decisions (ADR-style) for extensibility and reproducibility.  
- References to STAC, MCP, CIDOC CRM, OWL-Time, and other interoperability standards.  

Following **Master Coder Protocol (MCP)**, all artifacts are:
- Documented before code.  
- Version-controlled with provenance.  
- Renderable in GitHub (Markdown + Mermaid).  
- Linked to related components in `/data/`, `/src/`, `/tests/`, and `/web/`.  

---

## 📚 Contents

```text
docs/architecture/
├── README.md               # Index (this file)
├── architecture.md          # Root architecture overview
├── data-architecture.md     # Data & catalog design (sources, STAC, provenance)
├── file-architecture.md     # File & repository layout (monorepo + DVC/Git LFS)
├── web-ui-architecture.md   # React/MapLibre frontend design & flows
├── api-architecture.md      # FastAPI/GraphQL backend structure
├── knowledge-graph.md       # Neo4j + CIDOC CRM + OWL-Time ontology mapping
├── pipelines.md             # ETL & AI/ML enrichment pipeline design
├── ci-cd.md                 # GitHub Actions, tests, pre-commit, observability
└── diagrams/                # Static diagrams (Mermaid .md + exported .svg/.png)


⸻

🗂️ Key Docs
	•	architecture.md → Root architecture overview (ETL → Graph → API → UI).
	•	data-architecture.md → STAC-driven data catalog & provenance strategy.
	•	file-architecture.md → Monorepo + data/versioning practices.
	•	web-ui-architecture.md → Timeline + map React/MapLibre design.
	•	knowledge-graph.md → Graph schema, ontologies, entity linking.
	•	pipelines.md → Python ETL + AI enrichment flow.
	•	ci-cd.md → CI/CD, reproducibility, Trivy, CodeQL, pre-commit.

⸻

🧭 Usage
	1.	New contributors start here to understand the full system design.
	2.	Developers reference specific architecture docs when modifying pipelines, UI, or graph schema.
	3.	Researchers use diagrams and ontology mappings to link historical datasets.
	4.	CI/CD pipelines validate that all docs are present, current, and renderable in GitHub.

⸻

🔗 Related Docs
	•	Project Root Architecture
	•	Data Architecture
	•	Web UI Docs
	•	Knowledge Graph Design

⸻


<div align="center">


📐 Architecture is the backbone of MCP reproducibility.
Every dataset, pipeline, and UI element must trace back here.

</div>