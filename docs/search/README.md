---
title: "🔍 Kansas Frontier Matrix — Search System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/search/README.md"
version: "v11.2.2"
last_updated: "2025-11-27"
review_cycle: "Quarterly · FAIR+CARE Council"
release_stage: "Stable / Governed"
lifecycle: "LTS"
commit_sha: "<latest-commit-hash>"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/search-system-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "SearchGuide"
intent: "search-system-overview"
category: "Documentation · Search"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Documentation"
redaction_required: false

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "TechArticle"
  owl_time: "ProperInterval"
  prov_o: "prov:Collection"

json_schema_ref: "../../schemas/json/search-docs-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/search-docs-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:search:index:v11"
semantic_document_id: "kfm-docs-search-index"
event_source_id: "ledger:docs/search/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

machine_extractable: true
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "fabricated claims"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "12 months"
sunset_policy: "Superseded upon next search-architecture revision"
---

<div align="center">

# 🔍 **Kansas Frontier Matrix — Search System Overview**  
`docs/search/README.md`

**Purpose**  
Provide a consolidated reference for the **Search & Discovery System** powering the Kansas Frontier Matrix (KFM).  
Defines search pipelines, index structures, semantic enrichment, FAIR+CARE considerations, and integration with Focus Mode v3.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)]()  
[![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.2-purple)]()

</div>

---

## 📘 Overview

KFM’s Search System provides **unified, semantic, ethical, and geospatially-aware discovery** across:

- Historical documents  
- Datasets & metadata  
- Story Nodes  
- Focus Mode entities  
- STAC Catalog assets  
- Knowledge graph relationships  
- Spatial layers & temporal events  

It combines:

- **Vector search** (embeddings)  
- **Graph search** (Neo4j Cypher / GQL)  
- **STAC/DCAT index lookups**  
- **Metadata filters** (FAIR+CARE, dataset type, temporal range)  
- **Full-text indexing** (Elastic/Lucene-based)  

Built for high performance, transparency, and machine interpretability.

---

## 🗂️ Directory Layout

~~~text
docs/search/
├── 📄 README.md
├── 🧠 semantic-search.md
├── 🔎 query-language.md
├── 📚 index-architecture.md
└── 🛡️ faircare-search-rules.md
~~~

---

## 🧩 Search Components

### 1️⃣ Full-Text Search (FTS)
- Uses Lucene/Elastic indexing  
- Tokenization, stemming, stopwords, N-grams  
- Multi-field relevance scoring  
- Highlight fragments for Focus Mode summaries  

### 2️⃣ Semantic Vector Search (Embeddings)
- Transformer-based embedding models  
- Sentence-level and entity-level encodings  
- Approximate nearest neighbor (ANN) recall  
- Embedding masking for sensitive fields (CARE compliance)  

### 3️⃣ Knowledge Graph Search
- Cypher pattern matching  
- Multi-hop entity traversal  
- Spatial + temporal constraints supported  
- Used heavily in Focus Mode v3  

### 4️⃣ Metadata Search (STAC/DCAT)
- Search by dataset type, bbox, time range  
- Works across processed & raw metadata  
- Ensures reproducibility and dataset lineage discovery  

### 5️⃣ Hybrid Search Pipeline
All search types can be combined:

```
User Query → Classification → Query Routing  
  → (FTS + Vector + Graph + Metadata)
  → Fusion Ranking → Ethical Filter (CARE)
  → Focus Summary (optional)
```

---

## 🧭 Query Routing

The router inspects:

- Query type (keyword, natural language, structured)  
- Entities referenced  
- Temporal expressions (e.g., “in 1880s”)  
- Spatial hints (“near Fort Larned”, “in SW Kansas”)  
- Ethical context (restricted terms → masked)  

Then sends requests to:

- FTS → quick lexical grounding  
- Vector search → semantic similarity  
- Graph search → entity relations  
- Metadata search → datasets & files  

Rank fusion returns a unified result list.

---

## 🛡️ Ethical Search (FAIR+CARE Filters)

Search results pass through:

| Filter | Function |
|--------|----------|
| **Consent Filter** | Excludes datasets lacking community consent |
| **Sovereignty Filter** | Enforces Indigenous data governance rules |
| **Sensitivity Filter** | Masks culturally sensitive content |
| **Provenance Filter** | Ensures only verified, lineage-tracked data is shown |
| **Role-based Permissions** | Restricts access to certain collections |

CARE rules are **mandatory** and integrated at the engine level — not optional.

---

## 🧠 Focus Mode Integration

Search results can be passed directly into Focus Mode:

- Entities are grouped into clusters (People · Places · Events · Documents)  
- Graph neighborhood used to expand summaries  
- Narrative generated with citations and provenance markers  
- No hallucinations: all statements are traceable  

---

## 📚 Index Architecture

The indexing system includes:

- **text-index/** (FTS tokens)  
- **vector-index/** (embeddings for all entities)  
- **graph-index/** (entity metadata → KG)  
- **stac-index/** (dataset metadata hierarchy)  

Indexes are deterministic and re-creatable via ETL workflows.

---

## 🧮 Search Metrics

| Metric | Definition | Target |
|--------|------------|---------|
| **Precision@10** | Relevance of top 10 | ≥ 0.88 |
| **Recall@50** | Coverage of relevant docs | ≥ 0.92 |
| **Latency** | 95th percentile response | < 450ms |
| **Ethical Compliance** | CARE filter correctness | 100% |
| **Index Freshness** | From commit to index update | < 10 minutes |

---

## 🛠 Maintenance & Reindexing

Reindex triggers:

- Dataset updates  
- Story Node updates  
- Graph migrations  
- Model upgrades  
- Release promotions (staging → prod)  

Full reindex schedule: **Monthly**  
Partial reindex schedule: **Continuous (event-driven)**

---

## 🕰 Version History

| Version | Date | Summary |
|--------|--------|----------|
| v11.2.2 | 2025-11-27 | Initial v11.2.2 release of Search System Overview. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧠 Semantic Search](semantic-search.md) · [🛡️ Governance](../standards/governance/ROOT-GOVERNANCE.md)

</div>

