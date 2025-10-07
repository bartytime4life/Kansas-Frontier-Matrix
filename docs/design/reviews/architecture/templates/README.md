<div align="center">


🧭 Kansas Frontier Matrix — Architecture Review Templates

docs/design/reviews/architecture/templates/

Mission-grade · Reproducible · MCP-Aligned Design Governance

</div>



⸻

🪶 Overview

This directory provides standardized templates and checklists for conducting architecture reviews across
the Kansas Frontier Matrix (KFM) stack — ensuring every change to ETL → STAC → Knowledge Graph → API → Web UI
is reproducible, traceable, and semantically consistent.
All templates follow Master Coder Protocol (MCP) standards and integrate with CI validation
(STAC Validate · CodeQL · Trivy).

⸻

📁 Contents

File / Template	Purpose
architecture_review_template.md	Full architecture-review outline with per-layer findings, Mermaid flow, and provenance.
ADR_template.md	Architecture Decision Record template (ADR-0000-slug.md).
risk_register.md	Risk + Assumptions Register with likelihood / impact / mitigation.
traceability_matrix.md	Links requirements ⇄ datasets ⇄ graph ⇄ API ⇄ UI ⇄ tests.
validation_checklists.md	STAC / CIDOC CRM / OWL-Time / a11y / security checklist.


⸻

⚙️ Usage

# Create a new dated review
mkdir docs/design/reviews/architecture/2025-10-07_system-upgrade
cp docs/design/reviews/architecture/templates/architecture_review_template.md \
   docs/design/reviews/architecture/2025-10-07_system-upgrade/README.md

Each review must address all major layers and document:
	•	Data provenance (inputs / outputs / commit / checksums)
	•	Validation results (STAC schema · CIDOC CRM alignment · CI status)
	•	Risks, decisions, and follow-ups

Reviews are committed via PR and validated automatically by GitHub Actions.

⸻

🧩 Architecture Flow (Reference)

flowchart TD
  A["ETL\nMakefile · Python · checksums"] --> B["Processed Layers\nCOGs · GeoJSON"]
  B --> C["STAC Catalog\ncollections · items · assets"]
  B --> I["AI / ML Enrichment\nNER · geocoding · linking"]
  C --> H["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
  H --> J["API Layer\nFastAPI · GraphQL"]
  C --> J
  J --> F["Frontend (Web UI)\nReact + MapLibre · Timeline · Search"]
<!-- END OF MERMAID -->

Reference: Architecture Overview

⸻

🧱 Review Template (Excerpt)

---
title: "Architecture Review — {{ topic }}"
review_id: "AR-{{ YYYYMMDD }}-{{ slug }}"
owners: ["@handle1"]
status: "draft"
scope: [etl, stac, graph, api, web]
provenance:
  commit: "{{ GIT_COMMIT }}"
  inputs: ["data/sources/*.json","src/**"]
  outputs: ["data/stac/**","web/**"]
---

# Architecture Review — {{ topic }}

## Summary
Intent, context, and related ADRs.

## Findings (by Layer)
- **ETL** — data flows, idempotence, checksum tests  
- **STAC** — item coverage · schema validation  
- **Knowledge Graph** — CIDOC CRM · OWL-Time alignment  
- **API** — performance · security · query efficiency  
- **Web UI** — MapLibre sources · Canvas timeline · accessibility  
- **CI / Security** — STAC Validate · CodeQL · Trivy · tests  

## Risks / Mitigations · Follow-ups  
## Provenance · Checksums · Commit


⸻

🧾 Validation Checklist (Summary)

Category	Pass Criteria
STAC Catalog	Valid schema · bbox · temporal interval · asset links
Graph Semantics	Entities → CIDOC CRM · Intervals → OWL-Time · PeriodO tags
API / UI	REST/GraphQL responds ≤ 300 ms · no N+1 · a11y passed
Reproducibility	Checksums verified · container scan clean · CI green


⸻

🧰 Badges & Provenance Block Snippet

[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/badge/CodeQL-secure-blueviolet)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../.github/workflows/trivy.yml)

> **Provenance**
> • Commit              : {{ GIT_COMMIT }}  
> • Inputs              : data/sources/, src/  
> • Outputs            : data/stac/, web/  
> • Checksums          : checksums.sha256  


⸻

📚 References & Cross-Links
	•	📖 System Architecture
	•	🗺 Web UI Architecture
	•	🧱 Monorepo Design
	•	📜 Markdown Standard Kit

⸻

License: CC-BY 4.0 | Maintained under Master Coder Protocol (MCP v1.0)
All templates are automatically validated in CI (STAC Validate · Markdown Lint · Link Check).

⸻
