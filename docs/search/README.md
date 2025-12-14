---
title: "🔍 Kansas Frontier Matrix — Search System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/search/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
review_cycle: "Quarterly · FAIR+CARE Council"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "SearchGuide"
header_profile: "standard"
footer_profile: "standard"

intent: "search-system-overview"
category: "Documentation · Search"

commit_sha: "<latest-commit-hash>"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/search-system-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../security/supply-chain/README.md"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; policy-gated)"
sensitivity_level: "None"
public_exposure_risk: "Low"

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

doc_uuid: "urn:kfm:doc:search:index:v11.2.6"
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
Provide a consolidated, governed reference for the **Search & Discovery System** powering Kansas Frontier Matrix (KFM).  
Defines search pipelines, index structures, semantic enrichment, FAIR+CARE considerations, and integration with Focus Mode.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

KFM’s Search System provides **unified, semantic, ethical, and geospatially-aware discovery** across:

- Historical documents
- Datasets & metadata
- Story Nodes
- Focus Mode entities
- STAC catalog assets
- Knowledge graph relationships
- Spatial layers & temporal events

It combines (implementation may vary by deployment, but capabilities are governed):

- **Vector search** (embeddings / ANN)
- **Graph search** (Neo4j Cypher or equivalent)
- **STAC/DCAT index lookups**
- **Metadata filters** (FAIR+CARE, dataset type, temporal range)
- **Full-text indexing** (e.g., Lucene/Elastic-class engines)

Design priorities:

- performance and latency discipline,
- transparency and explainability,
- rights/sensitivity controls (FAIR+CARE + sovereignty policy),
- deterministic, replayable indexing workflows.

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

- Lexical indexing with tokenization, stemming, stopwords, n-grams
- Multi-field relevance scoring
- Highlight fragments for downstream summaries (when enabled and allowed)

### 2️⃣ Semantic Vector Search (Embeddings)

- Sentence-level and entity-level encodings
- Approximate nearest neighbor (ANN) retrieval (index-specific)
- Embedding masking/omissions for restricted or sensitive fields (CARE compliance)

### 3️⃣ Knowledge Graph Search

- Pattern matching and relationship traversal
- Multi-hop entity expansion
- Spatial + temporal constraints supported
- Used to enrich search results for Focus Mode and Story Nodes

### 4️⃣ Metadata Search (STAC/DCAT)

- Search by dataset type, bbox, time range, and catalog properties
- Supports reproducibility by exposing dataset/version provenance
- Bridges “files and metadata” with the graph and narrative layers

### 5️⃣ Hybrid Search Pipeline

All search types can be combined via routing + rank fusion:

~~~text
User Query → Classification → Query Routing
  → (FTS + Vector + Graph + Metadata)
  → Fusion Ranking → Ethical Filter (FAIR+CARE)
  → Focus Summary (optional; provenance-aware)
~~~

---

## 🧭 Query Routing

The router inspects:

- query type (keyword, natural language, structured)
- entities referenced (people/places/events)
- temporal expressions (e.g., “in the 1880s”)
- spatial hints (e.g., “near Fort Larned”, “in SW Kansas”)
- ethical context (restricted terms → masked or blocked)

Then sends requests to:

- FTS → quick lexical grounding
- vector search → semantic similarity
- graph search → entity relations
- metadata search → datasets and files

Rank fusion returns a unified result list with explainable components.

---

## 🛡️ Ethical Search (FAIR+CARE Filters)

All candidate results MUST pass policy gates before surfacing.

| Filter | Function |
|--------|----------|
| **Consent Filter** | Excludes datasets lacking appropriate consent signals |
| **Sovereignty Filter** | Enforces Indigenous data governance rules |
| **Sensitivity Filter** | Masks or blocks culturally sensitive content |
| **Provenance Filter** | Ensures only verified, lineage-tracked data is shown |
| **Role-based Permissions** | Restricts access to governed collections |

FAIR+CARE rules are **mandatory** and enforced as part of the search pipeline, not as an optional UI feature.

---

## 🧠 Focus Mode Integration

Search results can be passed into Focus Mode for provenance-aware synthesis:

- Entities grouped into clusters (People · Places · Events · Documents)
- Graph neighborhood used to expand context (when allowed)
- Narrative generation is **evidence-led**:
  - statements SHOULD be traceable to catalog/graph/document evidence,
  - restricted knowledge MUST be masked or withheld per policy.

---

## 📚 Index Architecture

The indexing system is organized into interoperable index families (logical roles; implementation may be service-backed):

- **FTS index**: lexical tokens and per-field analyzers
- **Vector index**: embeddings for entities and documents
- **Graph index**: queryable entity metadata and relationships
- **STAC/DCAT index**: catalog records and metadata lookups

Indexes are designed to be deterministic and re-creatable via governed ETL/indexing workflows.

---

## 🧮 Search Metrics

Targets below are service objectives (SLO-style) and may be tuned by the FAIR+CARE Council and search stewards.

| Metric | Definition | Target |
|--------|------------|--------|
| **Precision@10** | Relevance of top 10 | ≥ 0.88 |
| **Recall@50** | Coverage of relevant items | ≥ 0.92 |
| **Latency (p95)** | 95th percentile response | < 450 ms |
| **Ethical Compliance** | CARE filter correctness | 100% |
| **Index Freshness** | From commit to index update | < 10 minutes |

---

## 🛠 Maintenance & Reindexing

Reindex triggers:

- dataset updates
- Story Node updates
- graph migrations
- embedding/model upgrades (governed)
- release promotions (staging → prod)

Recommended schedules:

- full reindex: **monthly** (or upon breaking changes)
- partial reindex: **continuous** (event-driven)

All reindex operations SHOULD emit telemetry and provenance artifacts.

---

## 🕰 Version History

| Version | Date | Summary |
|--------|------|---------|
| v11.2.6 | 2025-12-13 | Updated to KFM-MDP v11.2.6 header/footer profile; clarified governed capabilities and policy-gated behaviors. |
| v11.2.2 | 2025-11-27 | Initial v11.2.2 release of Search System Overview. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Back to Docs Root](../README.md) ·
[🧠 Semantic Search](semantic-search.md) ·
[🔎 Query Language](query-language.md) ·
[📚 Index Architecture](index-architecture.md) ·
[🛡️ FAIR+CARE Search Rules](faircare-search-rules.md) ·
[🏛️ Governance](../standards/governance/ROOT-GOVERNANCE.md) ·
[🔐 Supply-Chain Security](../security/supply-chain/README.md)

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
