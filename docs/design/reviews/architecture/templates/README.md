<div align="center">


🧭 Architecture Reviews — Templates

Kansas Frontier Matrix (KFM) · Documentation-first · MCP-aligned

</div>


KFM uses a GitHub-first, documentation-first process for design governance. This folder provides copy-paste templates and checklists to review system architecture across the full stack — ETL → STAC → Knowledge Graph → API → Web UI — with provenance, semantics, and reproducibility baked in.

⸻

What’s here
	•	Review Doc template (comprehensive, project-wide)
	•	ADR (Architecture Decision Record) template
	•	Risk & Assumptions Register (with mitigation)
	•	Traceability Matrix (requirements ⇄ tests ⇄ data layers ⇄ graphs ⇄ UI)
	•	STAC & Semantics validation checklist (data + ontology)
	•	Mermaid & Markdown rules (GitHub-safe)
	•	Provenance blocks (checksums, inputs/outputs, commit IDs) per MCP.

Use these to keep reviews consistent with the KFM architecture and monorepo conventions.

⸻

How to use (quick start)
	1.	Create a review:

docs/design/reviews/architecture/YYYY-MM-DD_<short-topic>/README.md

Include the Review Doc template below, then add ADRs as ADR-XXXX-<slug>.md.

	2.	Scope your review to at least: ETL, STAC, Graph, API, Web UI, and CI/Observability. Tie each finding to artifacts (data/sources, data/stac, src/, web/).
	3.	Validate: run STAC + lint + tests + container scans in CI (or locally via make data && make test && make validate).
	4.	Publish via PR with provenance and checklists checked.

⸻

1) Architecture Review — Doc Template

Copy from here into a new review README.md.

---
title: "Architecture Review — {{ topic }}"
review_id: "AR-{{ YYYYMMDD }}-{{ slug }}"
owners: ["@handle1","@handle2"]
semver: "0.1.0"
created: "{{ ISO8601_DATE }}"
status: "draft" # draft | in_review | approved | followup
scope:
  - etl
  - stac
  - graph
  - api
  - web
provenance:
  commit: "{{ GIT_COMMIT }}"
  inputs:
    - "data/sources/*.json"
    - "src/**"
    - "web/**"
  outputs:
    - "docs/design/reviews/architecture/{{YYYY-MM-DD}}_{{slug}}/"
---

# Architecture Review — {{ topic }}

## Summary
- **Decision intent**: One paragraph on *why now*.
- **Context**: Link to related ADRs / tickets.

## System Overview (KFM reference)
This review maps to KFM’s stack (**ETL → STAC → Knowledge Graph → API → Web UI**). Provide a one-screen figure.
  
```mermaid
flowchart TD
  A["ETL\nMakefile · Python · checksums"] --> B["Processed Layers\nCOGs · GeoJSON"]
  B --> C["STAC Catalog\ncollections · items · assets"]
  B --> D["AI/ML Enrichment\nNER · geocoding · linking"]
  C --> E["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
  E --> F["API\nFastAPI · GraphQL"]
  C --> F
  F --> G["Web UI\nReact + MapLibreGL · Timeline"]
<!-- END OF MERMAID -->

Findings (by layer)

ETL
	•	Inputs, transforms, idempotence, checksums, failure modes.

STAC Catalog
	•	Items/Collections correctness; temporal/spatial extents; asset types (COG/GeoJSON). Validation results.

Knowledge Graph
	•	Entity/edge model; CIDOC CRM & OWL-Time alignment; uncertainty and provenance.

API
	•	Query shapes (REST/GraphQL); perf; pagination; auth; caching.

Web UI
	•	MapLibre sources/layers; Canvas timeline behavior; accessibility (ARIA/keyboard); responsiveness.

Observability & CI
	•	STAC validate; unit/integration tests; CodeQL; Trivy; logs/metrics.

Risks & Mitigations
	•	R1: …
	•	R2: …

Actions / Follow-ups
	•	A1: …
	•	A2: …

Provenance
	•	Checksums: attach checksums.sha256 or link to artifacts.
	•	Commit: {{ GIT_COMMIT }}

> Notes: The figure and layer breakdown align with the canonical KFM architecture and web UI design.  

---

## 2) ADR — Architecture Decision Record (template)

```markdown
# ADR-{{ number }}: {{ concise-title }}
Date: {{ ISO8601_DATE }}
Status: proposed # proposed | accepted | superseded | deprecated
Context
- Background & constraints.

Decision
- The choice and boundaries.

Consequences
- Positive, negative, and neutral outcomes.

Links
- Review: AR-{{ review_id }}
- Supersedes: ADR-…


⸻

3) Risk & Assumptions Register (template)

| ID | Risk / Assumption | Likelihood | Impact | Mitigation / Trigger | Owner |
|----|-------------------|------------|--------|----------------------|-------|
| R1 |                   | M          | H      |                      |       |
| R2 |                   | L          | M      |                      |       |


⸻

4) Traceability Matrix (template)

| Requirement | Dataset / STAC Item | Graph Entities/Edges | API Endpoint | UI Component | Test/CI |
|-------------|----------------------|----------------------|--------------|--------------|---------|
| FR-01       | data/stac/items/...  | Place, Event → OCCURRED_AT | /events | TimelineView | tests/... |


⸻

5) Validation Checklists

STAC & Data
	•	STAC Item/Collection has bbox, datetime/interval, assets (COG/GeoJSON) with MIME types.
	•	Temporal coverage matches layer vintage; CRS and extents correct.
	•	STAC validation passes in CI; failures triaged.

Semantics (Graph)
	•	Entities mapped to CIDOC CRM classes; OWL-Time for instants/intervals.
	•	Provenance & confidence recorded on edges; uncertainties visualized.

API & Web UI
	•	Endpoints return minimal JSON/GeoJSON; server-side aggregation; no N+1.
	•	MapLibre sources and styles load; Canvas timeline performs at target FPS; a11y checks.

Reproducibility & Security
	•	Checksums (.sha256) committed; CodeQL and Trivy green in CI.

⸻

6) GitHub-safe Mermaid & Markdown rules
	•	Quote labels with punctuation, use \n for line breaks, and always end with <!-- END OF MERMAID -->.
	•	Keep figures small and scannable; prefer flowchart TD/LR.

⸻

7) Badges & Provenance blocks (snippets)

[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/badge/CodeQL-secure-blueviolet)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../.github/workflows/trivy.yml)

> **Provenance**
> - Commit: `{{ GIT_COMMIT }}`
> - Inputs: `data/sources/*.json`, `src/**`
> - Outputs: `data/stac/**`, `web/**`
> - Checksums: `checksums.sha256`


⸻

8) References
	•	KFM Architecture: end-to-end layers, ETL → STAC → Graph → API → Web.
	•	Root architecture diagram & governance (flow + semantics + STAC).
	•	Web UI design (React + MapLibre + Canvas timeline integration).
	•	Monorepo & CI standards (badges, workflows, security gates).
	•	Markdown Standard Kit (front-matter, JSON-LD, Mermaid rules).

⸻

Template license: CC-BY-4.0.
Placeholders: replace {{ … }} tokens during authoring or via your review Make targets.