---
title: "🧭 Kansas Frontier Matrix — DRIFT Search Integration (Neo4j × LlamaIndex) · Hybrid Global→Local Retrieval"
path: "docs/search/drift/README.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../releases/v11.2.0/search-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/drift-search-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active · Enforced"
doc_kind: "Search Architecture"
intent: "drift-search"
category: "Search · Knowledge Graph · AI Retrieval"

fair_category: "F1-A2-I2-R2"
care_label: "CARE-Aware Retrieval"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

sensitivity: "Contains contextual references to cultural/archaeological datasets; CARE screening mandatory"
risk_category: "Governed"
redaction_required: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/search/drift/README.md@v11.1.0"
  - "KFM DRIFT Search Prototype v10.4"
  - "LlamaIndex HyDE Research Notes"
  - "Neo4j Graph Retrieval Experiments"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../../schemas/json/drift-search-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/drift-search-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "3d-context-render"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "content-alteration"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - summary
    - semantic-highlighting
    - diagram-extraction
    - metadata-extraction
    - timeline-generation
  prohibited:
    - narrative-fabrication
    - unverified-architectural-claims

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

doc_uuid: "urn:kfm:doc:search:drift-integration:v11.2.0"
semantic_document_id: "kfm-drift-search"
event_source_id: "ledger:docs/search/drift/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded by drift-search-v12"
---

<div align="center">

# 🧭 **DRIFT Search Integration**  
### *Hybrid Global → Local Retrieval for Narrative, Spatial, and Heritage-Constrained Queries*  
`docs/search/drift/README.md`

[![Search](https://img.shields.io/badge/Search-DRIFT%20v11-blue)]()
[![Neo4j](https://img.shields.io/badge/Graph-Neo4j%20v5-success)]()
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-HyDE%20Enabled-9c27b0)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()
[![Telemetry](https://img.shields.io/badge/Telemetry-v11-lightseagreen)]()
[![MIT License](https://img.shields.io/badge/License-MIT-green)]()

**Purpose**  
Define the DRIFT (Dynamic Retrieval Inference Flow Technique) architecture integrating **global → local hybrid retrieval** across **Neo4j**, **LlamaIndex**, **STAC/DCAT**, and **CARE-governed heritage constraints**.

</div>

---

## 📘 1. Overview

DRIFT Search implements a **hybrid retrieval engine** combining:

- 🌐 **Global semantic retrieval** (HyDE-style query expansion)  
- 🧠 **Embedding-based community search** (LlamaIndex / VectorDB)  
- 🕸️ **Graph-local precision** (Neo4j Cypher traversals)  
- 🗂️ **STAC/DCAT context ingestion**  
- 🛡️ **CARE-aware spatial redaction**  

This pattern powers:

- **Focus Mode v3**  
- **Story Node v3 entity/context resolution**  
- **Heritage-safe narrative synthesis**  
- **Spatial-temporal knowledge traversal**  

---

## 🗂️ 2. Directory Layout (v11.2 · Emojis + Descriptions · Immediate+One Branch)

```text
📁 docs/search/drift/                        — DRIFT search architecture root
│   📂 workflows/                           — DAGs for global→local DRIFT execution
│   📂 hyde/                                — HyDE templates, LLM reformulation logic
│   📂 embeddings/                          — Embeddings for communities/entities
│   📂 graph-queries/                       — Cypher templates for precision retrieval
│   📂 synthesis/                           — LLM synthesis policies & safety rules
│   📂 provenance/                          — PROV-O lineage + retrieval traces
│   📂 examples/                            — Demonstrations of DRIFT runs
│   📂 stac/                                — STAC items representing retrieval events
│   📄 README.md                            — This document
```

---

## 🧬 3. DRIFT Search Architecture

DRIFT is implemented across **four coordinated phases**:

### 🔷 Phase 1 — Global Semantic Initialization
- HyDE expands the user’s question into a structured pseudo-answer.  
- LlamaIndex computes embeddings for query + hypothesis.  
- Embeddings matched against Neo4j-stored “community summaries.”  
- Produces **context anchors** for local reasoning.

### 🟦 Phase 2 — Follow-Up Question Generation  
- LLM generates targeted sub-queries per anchor.  
- Each sub-query forms a **local retrieval action**.

### 🟧 Phase 3 — Local Neo4j Precision Traversal  
Cypher traverses:

- Entities (E21 Person, E53 Place, E5 Event, etc.)  
- Spatial geometries + H3 footprints  
- Temporal extents (OWL-Time instants / intervals)  
- Heritage graphs (site → context → culture → region)  
- STAC-linked datasets  

Ensures deterministic, lineage-safe retrieval.

### 🟩 Phase 4 — LLM Synthesis & CARE Enforcement  
- Intermediate results merged.  
- CARE-driven redaction, aggregation, or generalization applied.  
- Story Node v3 metadata produced for Focus Mode narratives.

---

## 🔗 4. High-Level Flow (Narrative Diagram)

```text
User Query
   ↓
HyDE Context Expansion
   ↓
Vector Retrieval (Community Embeddings)
   ↓
LLM → Follow-up Questions
   ↓
Neo4j Local Retrievals (Parallel Cypher Traversals)
   ↓
Aggregation + CARE Screening
   ↓
Final Answer + Story Node v3 Output
```

---

## ⚖ 5. FAIR+CARE Enforcement (v11.2)

DRIFT Search **strictly enforces**:

- ✓ **H3 generalization** of sensitive archaeological coordinates  
- ✓ **Minimum cluster size** thresholds before summarization  
- ✓ **Region-level masking** for sovereign/tribal heritage content  
- ✓ **Lineage bundling** (PROV-O trace for every retrieval)  
- ✓ **Redaction rules** for Indigenous sovereignty data  
- ✓ **AI ethics gating** before narrative generation  

This prevents leakage, fabrication, or inappropriate specificity.

---

## 📦 6. Outputs Stored in This Directory

DRIFT Search produces governed outputs:

- `provenance/*.jsonld` — PROV-O / OpenLineage retrieval traces  
- `examples/*.md` — Human-readable run samples  
- `stac/*.json` — STAC Items for semantic retrieval episodes  
- `workflows/*.yaml` — Optional DAG orchestration configs  
- `embeddings/*.npy` — Embedding arrays for communities/entities  

---

## 🔧 7. Integration Notes

- Works with **Focus Transformer v3**  
- Compatible with **LangGraph DAG** orchestration  
- Auto-logs:
  - Embedding dimensionality  
  - Vector similarity stats  
  - Graph expansion depth  
  - H3 footprint generalization  
  - Energy/Carbon telemetry  

- Story Node v3 hooks enable:
  - Semantic linking to places/events  
  - Narrative time-scale binding  
  - Heritage-compliant spatial generalization  

---

## 🧩 8. Related Standards & Documents

- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `docs/standards/heritage/h3-generalization.md`  
- `docs/standards/telemetry_standards.md`  
- `docs/graph/write-patterns.md`  
- `docs/architecture/SEARCH-ARCHITECTURE.md`  
- STAC v11 Semantic Retrieval Extension

---

## 🕰️ 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| **v11.2.0** | 2025-11-27 | Upgraded to full KFM-MDP v11.2.2 formatting; added badge row, directory layout rules, CARE enforcement clarity, Focus Mode integration. |
| **v11.1.0** | 2025-11-26 | Initial DRIFT documentation; updated for Focus Transformer v3, Neo4j community embeddings, new provenance rules. |

---

<div align="center">

**Kansas Frontier Matrix — DRIFT Search Architecture**  
*FAIR+CARE Powered · Diamond⁹ Ω / Crown∞Ω Ultimate Certified*  

[⬅ Back to Search Index](../README.md) ·  
[📜 Governance](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Schema](../../../schemas/telemetry/drift-search-v11.json)

</div>