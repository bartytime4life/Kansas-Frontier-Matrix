<div align="center">


🧩 Kansas Frontier Matrix — Architecture Review Templates

docs/design/reviews/architecture/templates/

Purpose: Provide standardized, MCP-compliant templates for architecture reviews across all system layers — ETL, AI/ML, STAC, Knowledge Graph, API, and Web UI.

</div>



⸻

🎯 Objective

Architecture review templates ensure the Kansas Frontier Matrix stays:
	•	Modular — clear ETL → STAC → Knowledge Graph → API → Web UI boundaries.
	•	Reproducible — every review includes commits, checksums, and CI results.
	•	Interoperable — grounded in open standards (STAC 1.0, CIDOC CRM, OWL-Time, GeoJSON, COG).
	•	Observable — evidence chain and validation logs are part of the doc.
	•	Readable — GitHub-safe grids/tables and Mermaid that render cleanly.

⸻

🧭 Directory Layout

docs/design/reviews/architecture/templates/
├── README.md                         # This index
├── architecture_review_template.md   # End-to-end review form
├── adr_template.md                   # Architecture Decision Record (ADR-####-slug.md)
├── risk_register.md                  # Risk & assumptions matrix
├── traceability_matrix.md            # Requirements → data → graph → API → UI → tests
├── validation_checklist.md           # STAC / semantics / a11y / CI checks
└── mmd_render_audit.md              # Mermaid (.mmd) render audit & GitHub parsing notes

⸻

🧩 Template Scopes

Review Type	Scope	Deliverables	Owner
Architecture Review	Verify stack flow and contracts (ETL → Web).	Annotated Markdown + Mermaid + provenance.	System Leads
ADR	Record a decision with context & consequences.	ADR-####-slug.md	Architects
Risk Register	Identify risks, impact, and mitigations.	Table (likelihood/impact/owner).	All reviewers
Traceability Matrix	Map requirements to data, graph, API, UI, tests.	Linked table.	QA / CI
Validation Checklist	Confirm STAC, CIDOC CRM, OWL-Time, a11y, CI.	Checkbox list.	Reviewers / CI

⸻

🧠 Review Process (MCP-Aligned)
	1.	Create — copy architecture_review_template.md to a new dated folder:
docs/design/reviews/architecture/YYYY-MM-DD_<topic>/README.md
	2.	Link — reference diagram(s), commit(s), and data sources; attach checksums.
	3.	Evaluate — clarity, scalability, security, and standards compliance.
	4.	Document — findings + tables (issues, actions, owners, due dates).
	5.	Validate — run make validate (STAC), CodeQL, Trivy, tests; paste CI links.
	6.	Approve — tag reviewers, set status = approved, bump version (semver).
	7.	Archive — move superseded reviews to /archive/ for provenance.

⸻

🧩 Example Architecture Flow

flowchart TD
A[“Sources\n(scans · rasters · vectors · documents)”] –> B[“ETL Pipeline\nMakefile · Python · checksums”]
B –> C[“STAC Catalog\ncollections · items · assets”]
B –> D[“AI/ML Enrichment\nNER · geocoding · summarization”]
C –> E[“Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time”]
E –> F[“API Layer\nFastAPI · GraphQL”]
F –> G[“Web UI\nReact · MapLibre · Timeline”]
G –> H[“Architecture Reviews\n(this folder)”]
H –> I[“Continuous Integration\nGitHub Actions · STAC Validate · CodeQL”]

<!-- END OF MERMAID -->


⸻

🧰 Templates & Tools

File	Description
architecture_review_template.md	Base form for end-to-end architecture evaluations.
adr_template.md	Decision record format (ADR-####-slug.md).
risk_register.md	Structured risk table (likelihood · impact · mitigation · owner).
traceability_matrix.md	Coverage map: requirement ⇄ data ⇄ graph ⇄ API ⇄ UI ⇄ tests.
validation_checklist.md	STAC / semantics / a11y / CI pass criteria.
mmd_render_audit.md	Mermaid lint + GitHub rendering compliance status.

Tools used in reviews:
	•	Mermaid CLI / Live Editor — validate syntax & layout.
	•	STAC Validator — check Item/Collection schemas.
	•	GraphQL Inspector — diff schemas between commits.
	•	MkDocs / Pages — verify docs build & links.

⸻

🧾 Provenance Metadata Example

review_id: “architecture_review_{{component}}_{{version}}”
reviewed_by: [”@architecture-team”]
date: “{{ ISO8601_DATE }}”
commit: “{{ GIT_COMMIT }}”
scope: “system | pipeline | ui | provenance”
status: “approved”
confidence: “high”

⸻

🪪 License

All template files are released under Creative Commons CC-BY 4.0.
© 2025 Kansas Frontier Matrix Design Collective

⸻