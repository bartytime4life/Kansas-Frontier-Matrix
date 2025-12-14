---
title: "🧭 Kansas Frontier Matrix — DRIFT Search Integration (Neo4j × LlamaIndex) · Hybrid Global→Local Retrieval"
path: "docs/search/drift/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Search Architecture"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

intent: "drift-search"
category: "Search · Knowledge Graph · AI Retrieval"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/search-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/drift-search-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../security/supply-chain/README.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A2-I2-R2"
care_label: "CARE-Aware Retrieval"
classification: "Public (Governed)"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
sensitivity: "Contains contextual references to cultural/archaeological datasets; CARE screening mandatory"
risk_category: "Governed"
redaction_required: true

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

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
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "content-alteration"
  - "narrative-fabrication"
  - "governance-override"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

doc_uuid: "urn:kfm:doc:search:drift-integration:v11.2.6"
semantic_document_id: "kfm-drift-search"
event_source_id: "ledger:docs/search/drift/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

jurisdiction: "Kansas / United States"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded by drift-search-v12"
---

<div align="center">

# 🧭 **KFM — DRIFT Search Integration**
`docs/search/drift/README.md`

**Purpose**  
Define the DRIFT (Dynamic Retrieval Inference Flow Technique) architecture integrating **global → local hybrid retrieval**
across **Neo4j**, **LlamaIndex**, and **STAC/DCAT**, with **CARE-governed heritage constraints** including redaction,
aggregation, and provenance-first synthesis.

<img src="https://img.shields.io/badge/Search-DRIFT%20v11-blue" />
<img src="https://img.shields.io/badge/Graph-Neo4j%20v5-success" />
<img src="https://img.shields.io/badge/LlamaIndex-HyDE%20Enabled-9c27b0" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

DRIFT Search implements a **hybrid retrieval engine** combining:

- 🌐 Global semantic initialization (HyDE-style expansion)
- 🧠 Embedding-based community retrieval (LlamaIndex / ANN index)
- 🕸️ Graph-local precision retrieval (Neo4j traversals)
- 🗂️ STAC/DCAT context ingestion for dataset discovery and provenance
- 🛡️ CARE-aware redaction and generalization for sensitive heritage contexts

This pattern supports:

- Focus Mode v3 (retrieval + evidence bundling)
- Story Node v3 entity/context resolution
- Heritage-safe narrative synthesis
- Spatial-temporal knowledge traversal with policy enforcement

---

## 🗂️ Directory Layout

~~~text
📁 docs/search/drift/                               — DRIFT search architecture root
├── 📁 workflows/                                   — DAG configs for global→local DRIFT execution
├── 📁 hyde/                                        — HyDE templates and query reformulation logic
├── 📁 embeddings/                                  — Embedding artifacts for communities/entities (governed)
├── 📁 graph-queries/                               — Cypher templates for precision retrieval
├── 📁 synthesis/                                   — Synthesis policies and safety rules (CARE enforcement)
├── 📁 provenance/                                  — PROV-O lineage and retrieval traces
├── 📁 examples/                                    — Demonstrations of DRIFT runs (redacted when required)
├── 📁 stac/                                        — STAC Items representing retrieval episodes
└── 📄 README.md                                    — This document
~~~

---

## 🧬 DRIFT Search Architecture

DRIFT executes in four coordinated phases.

### 🔷 Phase 1 — Global semantic initialization

- HyDE expands the user’s question into a structured pseudo-answer (hypothesis).
- LlamaIndex computes embeddings for the query and hypothesis.
- Embeddings are matched against Neo4j-stored “community summaries” (or an external vector store).
- Output: a set of **context anchors** to guide local retrieval.

### 🟦 Phase 2 — Follow-up question generation

- The system generates targeted sub-queries per anchor.
- Each sub-query forms a **local retrieval action**.

### 🟧 Phase 3 — Local Neo4j precision traversal

Cypher traversals fetch:

- entities (e.g., `Person`, `Place`, `Event`, `Document` as KFM graph labels),
- spatial geometries + H3 footprints (policy-gated generalization),
- temporal extents (OWL-Time instants / intervals),
- heritage-safe relations (site → context → culture → region; redacted when required),
- STAC-linked datasets and DCAT distributions.

### 🟩 Phase 4 — Synthesis and CARE enforcement

- Results are merged into an evidence set.
- CARE rules apply redaction, aggregation, or generalization as required.
- Output includes:
  - answer summary (if permitted),
  - evidence bundle references,
  - Story Node v3-compatible metadata (when enabled).

---

## 🗺️ High-level flow

~~~mermaid
flowchart TD
  A["User query"] --> B["HyDE expansion - global hypothesis"]
  B --> C["Vector retrieval - anchors"]
  C --> D["Generate follow-up subqueries"]
  D --> E["Neo4j local retrieval - Cypher traversals"]
  E --> F["Aggregate evidence + CARE screening"]
  F --> G["Final response + Story Node hooks"]
~~~

---

## 🛡️ FAIR+CARE enforcement

DRIFT Search MUST enforce:

- H3 generalization of sensitive site coordinates (no raw coordinates exposed)
- minimum cluster size thresholds before summarization
- region-level masking for sovereignty/tribal heritage content where required
- provenance bundling (PROV-O trace for every retrieval episode)
- redaction rules for Indigenous sovereignty data
- AI ethics gating before narrative generation

### Redaction posture

Because `redaction_required: true` and `sensitivity_level: Medium`, this doc and associated examples MUST:

- avoid disclosing precise locations of sensitive cultural/archaeological sites,
- avoid presenting “how to find” or “where exactly” instructions,
- prefer region-level or generalized spatial descriptions.

---

## 📦 Outputs stored in this directory

DRIFT Search produces governed outputs (exact files depend on deployment):

- `provenance/*.jsonld` — PROV-O / OpenLineage retrieval traces (policy-gated)
- `examples/*` — human-readable run samples (redacted when required)
- `stac/*.json` — STAC Items for retrieval episodes
- `workflows/*.yaml` — orchestration configs (if used)
- `embeddings/*` — embedding artifacts (format may vary)

---

## 🔧 Integration notes

- Designed for Focus Mode v3 retrieval and evidence bundling.
- Compatible with DAG orchestration (e.g., LangGraph-style execution graphs).
- SHOULD log:
  - embedding model id and dimensionality,
  - similarity and fusion statistics,
  - graph expansion depth and node/edge counts,
  - redaction/generalization decisions (as policy events),
  - energy/carbon telemetry references (when enabled).

---

## 🧩 Related standards and documents

- `docs/standards/faircare/FAIRCARE-GUIDE.md`
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`
- `docs/architecture/SEARCH-ARCHITECTURE.md` (if present)
- KFM STAC/DCAT profiles (v11) and any search extensions (where governed)

---

## 🕰️ Version history

| Version  | Date       | Summary |
|---------:|------------|---------|
| v11.2.6  | 2025-12-13 | Updated to KFM-MDP v11.2.6 header/footer profiles; clarified redaction posture and governance constraints; normalized directory layout and diagram fences. |
| v11.2.0  | 2025-11-27 | Earlier governed DRIFT integration doc (v11.2.0 baseline). |
| v11.1.0  | 2025-11-26 | Initial DRIFT documentation; Focus Transformer v3 + community embeddings + provenance rules. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />

[⬅ Back to Search Index](../README.md) ·
[🛡️ Governance](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🛰 Telemetry Schema](../../../schemas/telemetry/drift-search-v11.json)

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
