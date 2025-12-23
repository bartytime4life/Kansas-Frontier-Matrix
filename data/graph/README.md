---
title: "KFM — data/graph/ (Graph Import Artifacts)"
path: "data/graph/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data:graph:readme:v1.0.0"
semantic_document_id: "kfm-data-graph-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:graph:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM — `data/graph/` (Graph Import Artifacts)

## 📘 Overview

### Purpose
- Define what belongs in `data/graph/` and how it is used to load/update the KFM Neo4j knowledge graph within the canonical pipeline ordering (**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**).  [oai_citation:3‡MASTER_GUIDE_v12.md.pdf](file-service://file-UydXsUR4BtxXsbTDpzoUmG)
- Keep the “data outputs are not code” boundary clear: this directory is for **generated import artifacts**, not source code.

### Scope

| In Scope | Out of Scope |
|---|---|
| Neo4j bulk import/export artifacts (CSV) and optional post-import Cypher scripts.  [oai_citation:4‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k) | Ontology definitions, migrations, and graph build code (these live under the graph subsystem code/docs, not here).  [oai_citation:5‡MASTER_GUIDE_v12.md.pdf](file-service://file-UydXsUR4BtxXsbTDpzoUmG) |
| Run-/release-ready artifacts that are reproducible and diffable. | UI consumption logic (UI must not query Neo4j directly).  [oai_citation:6‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k) |

### Audience
- **Primary:** Graph/ETL developers producing Neo4j load artifacts.
- **Secondary:** Reviewers and maintainers validating provenance + governance boundaries for graph loads.

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used: Graph import, Neo4j bulk load, provenance, redaction.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering and subsystem boundaries.  [oai_citation:7‡MASTER_GUIDE_v12.md.pdf](file-service://file-UydXsUR4BtxXsbTDpzoUmG) |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical `data/graph/csv/` + `data/graph/cypher/` outputs.  [oai_citation:8‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k)  [oai_citation:9‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k) |

### Definition of done (for this document)
- [x] Front-matter complete + valid
- [ ] Directory structure matches the canonical layout
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document
- `path`: `data/graph/README.md` (must match front-matter)

### Expected tree
The v13 blueprint defines graph import outputs as `data/graph/csv/` and `data/graph/cypher/`.  [oai_citation:10‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k)  [oai_citation:11‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k)

~~~text
📁 data/
└── 📁 graph/
    ├── 📁 csv/        # Graph import CSV exports (Neo4j loader inputs)
    ├── 📁 cypher/     # Optional post-import scripts (constraints, indexes, touch-ups)
    └── 📄 README.md   # (this file)
~~~

### What lives here

#### `data/graph/csv/`
- CSV files produced by the Graph build stage for bulk loading into Neo4j (e.g., node/relationship tables).  [oai_citation:12‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k)

#### `data/graph/cypher/`
- Optional Cypher scripts applied after import (e.g., indexes/constraints, post-load normalization).  [oai_citation:13‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k)

### What must *not* live here
- Graph ontology, label/relationship contracts, and migrations belong to the graph subsystem (e.g., `src/graph/` + `docs/graph/` as governed by the Master Guide).  [oai_citation:14‡MASTER_GUIDE_v12.md.pdf](file-service://file-UydXsUR4BtxXsbTDpzoUmG)
- Any UI code or direct-to-graph access patterns (UI must access graph data via the API boundary).  [oai_citation:15‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k)

---

## 🔗 Contracts & Linkage Expectations

### Ontology alignment
- CSV headers and relationship types should reflect the governed ontology and naming conventions defined in the graph subsystem docs/code (see `docs/graph/` / `src/graph/`).  [oai_citation:16‡MASTER_GUIDE_v12.md.pdf](file-service://file-UydXsUR4BtxXsbTDpzoUmG)  
- **Recommended convention (not confirmed in repo):** ensure every node has a stable `id` property and that relationships carry provenance/evidence references when applicable.

### Provenance and catalogs
- Graph records should remain traceable back to catalog/provenance artifacts (STAC/DCAT/PROV), consistent with the canonical pipeline ordering.  [oai_citation:17‡MASTER_GUIDE_v12.md.pdf](file-service://file-UydXsUR4BtxXsbTDpzoUmG)  [oai_citation:18‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k)

---

## 🧪 Validation & QA (minimum)

### Validation steps
- [ ] CSV schema sanity: expected columns present; consistent delimiter/encoding; no blank IDs.
- [ ] Referential integrity: every relationship endpoint ID exists in node CSVs.
- [ ] Determinism: regenerating artifacts with unchanged inputs yields diff-stable outputs (ordering, IDs).
- [ ] Governance checks: no restricted/sensitive locations beyond allowed generalization rules; no prohibited inferences.

### Reproduction (placeholders)
~~~bash
# Placeholder only (not confirmed in repo):
# 1) run graph build/export to produce data/graph/csv/*
# 2) (optional) run post-import scripts from data/graph/cypher/*
# 3) run validation checks (csv lint + referential integrity)
~~~

---

## ⚖ FAIR+CARE & Governance

### Sensitivity and redaction
If any artifacts include restricted locations or culturally sensitive knowledge, they must be protected by:
- generalization of geometry where required,
- API-level redaction,
- Story Node asset review gates.  [oai_citation:19‡Kansas Frontier Matrix — v13 Redesign Blueprint.pdf](file-service://file-PbXDvM77r6DdgZWjfspb9k)

### AI usage constraints
- This README permits summarization/structure extraction/translation/keyword indexing.
- It prohibits generating policy or inferring sensitive locations (see front-matter).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial `data/graph/README.md` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
