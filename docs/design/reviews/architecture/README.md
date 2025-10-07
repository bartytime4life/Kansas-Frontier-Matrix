<div align="center">

# 🧱 Kansas Frontier Matrix — Architecture Reviews  
`docs/design/reviews/architecture/`

**Purpose:** Maintain documentation-first, reproducible **architecture design reviews** across all system layers — ETL, AI/ML, Knowledge Graph, API, and Web UI — following Master Coder Protocol (MCP) best practices.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../LICENSE)

</div>

---

## 🎯 Objective

Architecture reviews ensure the **Kansas Frontier Matrix** system remains:
- **Modular** — ETL → STAC → Knowledge Graph → API → Web UI flow.
- **Reproducible** — all layers documented and validated by CI.
- **Interoperable** — open standards (STAC 1.0, CIDOC CRM, OWL-Time, GeoJSON, COG).
- **Observable** — logging, tracing, provenance across pipelines.
- **Accessible** — diagrams and docs readable on GitHub and exportable for reports.

---

## 🧭 Directory Layout

```text
docs/design/reviews/architecture/
├── README.md                       # This index
├── system_overview_review.md        # End-to-end architecture analysis
├── web_ui_architecture_review.md    # React + FastAPI integration review
├── pipeline_overview_review.md      # ETL + AI/ML + STAC pipeline audit
├── provenance_chain_review.md       # Provenance & reproducibility validation
└── templates/                       # Architecture review templates
    ├── architecture_review_template.md
    ├── diagram_validation_checklist.md
    └── mmd_render_audit.md


⸻

🧩 Review Types

Review Type	Scope	Deliverables	Frequency
System Overview	Verify overall stack, component boundaries, and data flow.	Annotated Mermaid diagrams + audit notes.	Quarterly
ETL & Pipeline	Check reproducibility, schema alignment, STAC validation.	STAC validation log + Makefile review.	Per release
Knowledge Graph	Confirm ontology mappings (CIDOC CRM, OWL-Time).	Graph schema doc + sample queries.	Semi-annual
API Layer	Review endpoint design, GraphQL/REST consistency.	OpenAPI spec validation report.	Per release
Web UI Architecture	Audit integration between React, MapLibre, and FastAPI.	Updated web_ui_architecture.mmd.	Per release
Provenance Chain	Confirm checksum + evidence traceability.	Provenance chain diagram + audit log.	Continuous


⸻

🧠 Review Process (MCP-Aligned)
	1.	Create — copy templates/architecture_review_template.md.
	2.	Link — reference relevant .mmd diagram(s) and commit ID(s).
	3.	Evaluate — ensure clarity, scalability, and compliance with open-data standards.
	4.	Document — add inline comments or Markdown tables for issues.
	5.	Validate — run CI checks (make validate, STAC + CodeQL).
	6.	Approve — tag reviewers, bump version (semver: minor).
	7.	Archive — move old reviews to /archive/ folder for provenance.

⸻

🧩 Example Architecture Flow

flowchart TD
  A["Sources\n(scans · rasters · vectors · documents)"] --> B["ETL Pipeline\nMakefile · Python · checksums"]
  B --> C["STAC Catalog\ncollections · items · assets"]
  C --> D["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
  D --> E["API Layer\nFastAPI · GraphQL"]
  E --> F["Web UI\nReact · MapLibre · Timeline"]
  F --> G["Design Review\n(this folder)"]
  G --> H["Continuous Integration\nGitHub Actions · STAC validate · CodeQL"]
<!-- END OF MERMAID -->


⸻

🧰 Templates & Tools

File	Description
architecture_review_template.md	Base form for documenting architecture evaluations.
diagram_validation_checklist.md	Step-by-step validation for GitHub Mermaid rendering.
mmd_render_audit.md	Tracks .mmd diagram parsing and GitHub compliance results.

Tools used in reviews:
	•	Mermaid CLI / Live Editor → validate syntax and layout.
	•	STAC Validator → confirm JSON metadata compliance.
	•	GraphQL Inspector → compare schema diffs.
	•	MkDocs / GitHub Pages → verify docs build correctly.

⸻

🧾 Provenance Metadata Example

review_id: "architecture_review_{{component}}_{{version}}"
reviewed_by: ["@architecture-team"]
date: "{{ ISO8601_DATE }}"
commit: "{{ GIT_COMMIT }}"
scope: "system | pipeline | ui | provenance"
status: "approved"
confidence: "high"


⸻

🪪 License

All architecture review files are released under Creative Commons CC-BY 4.0.
© 2025 Kansas Frontier Matrix Design Collective

⸻



