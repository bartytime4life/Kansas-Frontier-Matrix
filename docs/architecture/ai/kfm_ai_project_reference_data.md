---
title: "🤖 KFM — AI Project Reference Data & Architecture Guide"
path: "docs/architecture/ai/kfm_ai_project_reference_data.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"
status: "Active / Canonical"

doc_kind: "Architecture Reference"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "architecture"
  applies_to:
    - "ai-pipeline"
    - "focus-mode"
    - "story-nodes"
    - "knowledge-graph"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Enforced · Historical and Indigenous content"
sensitivity: "Mixed (historical; potential Indigenous and sensitive sites)"
sensitivity_level: "Assess-per-dataset"
public_exposure_risk: "Medium"
classification: "Public With Safeguards"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/ai-reference-telemetry.json"
telemetry_schema: "../../schemas/telemetry/ai-reference-v1.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

provenance_chain:
  - "docs/architecture/repo-focus.md@v11.2.5"
  - "docs/architecture/ai/kfm_ai_project_reference_data.md@v11.2.6"

ai_training_inclusion: false

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "glossary-suggestions"

ai_transform_prohibited:
  - "speculative-historical-claims"
  - "indigenous-knowledge-inference"
  - "governance-override"
  - "hallucinated-data-sources"

---

<div align="center">

# 🤖 KFM — AI Project Reference Data & Architecture Guide  
`docs/architecture/ai/kfm_ai_project_reference_data.md`

**Purpose**  
Capture the canonical, long-lived architecture for KFM’s AI pipeline — from ETL to Focus Mode — and anchor it to open standards (STAC, DCAT, PROV-O, GeoSPARQL), Neo4j knowledge graph design, and FAIR+CARE governance. This file is the bridge between the narrative “AI Project Reference Data” document and the in-repo implementation that powers Story Nodes and Focus Mode.  [oai_citation:0‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)

</div>

---

## 📘 Overview

KFM is an open-source “living atlas” of Kansas that fuses historical, cultural, and ecological data into a time-aware geospatial platform.  [oai_citation:1‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)

This guide:

- Summarizes the **end-to-end AI architecture** described in the KFM AI Project Reference Data document and makes it KFM-MDP v11.2.6 compliant.  [oai_citation:2‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
- Aligns the AI stack with the core KFM pipeline:  

  > Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode  [oai_citation:3‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.6".pdf](file-service://file-THbHjFhwcakK4cmtqgRiP2)  

- Defines how **AI models**, **knowledge graph semantics**, and **Focus Mode UX** interact, including provenance, versioning, and ethical safeguards.  [oai_citation:4‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
- Acts as a **reference anchor** for future AI-oriented design notes, experiment logs, and Story Node / Focus Mode feature work.

Audience:

- KFM core developers (ETL, graph, API, UI).
- AI/ML specialists building models against KFM data.
- Governance and FAIR+CARE reviewers evaluating compliance.
- Story Node and Focus Mode authors who need to understand infrastructure constraints.

---

## 🗂️ Directory Layout

KFM’s AI architecture surfaces across multiple repo locations. This document governs and explains the following core areas:

~~~text
📁 docs/
  📁 architecture/
    📄 repo-focus.md                          # Overall repo & Focus Mode architecture
    📁 ai/
      📄 kfm_ai_project_reference_data.md     # This file – AI pipeline & reference data guide
      📄 experiments-overview.md              # (planned) AI experiment patterns & IDs
      📄 model-cards-guide.md                 # (planned) How to write model cards for KFM

📁 src/
  📁 pipelines/
    📁 etl/
      📄 historical_ingest.py                 # Text, maps, tables ETL for historical data
      📄 remote_sensing_ingest.py             # Climate / remote sensing ETL
    📁 ai/
      📄 nlp_extraction.py                    # Entity extraction (people, places, dates)
      📄 vision_map_features.py               # Map/image feature extraction
      📄 qa_validation.py                     # AI output QA & governance checks

  📁 graph/
    📄 neo4j_schema.cypher                    # Core KFM-OP graph schema
    📄 ingestion_jobs.cypher                  # STAC/DCAT/PROV → Neo4j jobs
    📄 ai_annotations.cypher                  # AI-enriched relationships & annotations

  📁 api/
    📁 rest/
      📄 ai_insights_routes.py                # Endpoints for AI-driven summaries & explanations
    📁 graphql/
      📄 focus_mode_schema.graphql            # Focus Mode / Story Node query facets

  📁 web/
    📁 focus-mode/
      📄 FocusModeShell.tsx                   # Focus Mode UI container
      📄 StoryNodePanel.tsx                   # Story Node + AI explanation panel
      📄 ProvenancePanel.tsx                  # Lineage & governance flags view

📁 data/
  📁 stac/
    📁 collections/
      📄 historical_maps.json                 # STAC Collections for historical imagery
      📄 climate_layers.json                  # Climate & environmental datasets
    📁 items/
      📄 *.json                               # STAC Items with geometry + datetime

  📁 prov/
    📄 etl_runs.ttl                           # PROV-O for ETL activities
    📄 ai_inference_runs.ttl                  # PROV-O for AI model inferences

📁 schemas/
  📁 telemetry/
    📄 ai-reference-v1.json                   # Telemetry schema for this document & AI pipeline
  📁 graph/
    📄 kfm-op.cypher                          # KFM-OP ontology mapping
    📄 stac-dcat-prov-mapping.ttl             # STAC/DCAT/PROV ↔ Neo4j/knowledge graph

📁 releases/
  📁 v11.2.6/
    📦 sbom.spdx.json                         # SBOM for AI-related code + dependencies
    📦 manifest.zip                           # Frozen data + code snapshot (ETL + AI)
~~~

Any new AI-related architecture file should either extend this structure or explicitly reference it under `docs/architecture/ai/`.

---

## 🧭 Pipeline Context

The AI architecture sits inside the canonical KFM pipeline:

1. **Data Extraction & ETL**  
   - Ingests heterogeneous sources: text (diaries, newspapers, treaties), maps, LiDAR, climate grids, structured tables, web resources.  [oai_citation:5‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
   - Uses parsers and OCR for text, geospatial libraries for shapefiles/GeoJSON/DEM, and standard CSV/TSV readers for tabular data.

2. **Standardization & Metadata (STAC/DCAT/PROV)**  
   - Wraps assets as STAC Items/Collections with geometry, datetime, and asset links.  [oai_citation:6‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
   - Uses DCAT 3.0 to describe dataset-level catalog entries for open data portals and internal registries.  [oai_citation:7‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
   - Captures provenance with PROV-O and STAC Versioning Extension (entity, activity, agent).  [oai_citation:8‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  

3. **Knowledge Graph (Neo4j) Integration**  
   - Loads structured outputs into Neo4j using KFM-OP ontology (CIDOC-CRM + GeoSPARQL + OWL-Time alignment).  [oai_citation:9‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
   - Merges duplicate entities, links cross-source references, and records version relationships (:PREDECESSOR, :SUCCESSOR).  [oai_citation:10‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  

4. **AI Analysis & QA**  
   - NLP models extract entities, events, and relationships from text; computer vision models annotate maps and imagery; geospatial models perform clustering, prediction, and anomaly detection.  [oai_citation:11‡Comprehensive Open Data Sources and Tools for the Kansas Frontier-Matrix Project.pdf](file-service://file-TaFEKzoaANSnQHWuupWH38)  
   - Governance and ethics checks (FAIR+CARE, indigenous data flags, PII scans) run in-line with AI inferences.  [oai_citation:12‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  

5. **API Layer**  
   - REST and GraphQL endpoints expose graph and catalog facets: time, space, entity, lineage, and AI annotations.  [oai_citation:13‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
   - Provenance-aware queries enable “explain my view” and reproducible snapshots for Story Nodes and Focus Mode.

6. **Focus Mode & Story Nodes UI**  
   - MapLibre/Cesium front-end with timeline slider, interactive layers, and topic-centric Focus Mode dashboards.  [oai_citation:14‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
   - AI generates candidate summaries and highlights, but UI always exposes underlying data, sources, and AI explanations.

---

## 🧱 Architecture

From an architecture perspective, this guide:

1. **Defines the AI contract** between ETL, graph, API, and UI.  
2. **Anchors KFM’s AI to open standards**: STAC, DCAT, PROV-O, GeoSPARQL, CIDOC-CRM.  [oai_citation:15‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
3. **Specifies Neo4j as the authoritative knowledge graph** for AI and Story Node integration, using KFM-OP schema and version relationships.  [oai_citation:16‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
4. **Incorporates Master Coder Protocol 2.0** for reproducible AI pipelines, model cards, and experiment logs.  [oai_citation:17‡Master Coder Protocol 2.0.pdf](file-service://file-XjPWZrWdLTrVng7soAnSHp) [oai_citation:18‡Master Coder Protocol 2.0.pdf](file-service://file-XjPWZrWdLTrVng7soAnSHp)  
5. **Enforces governance** via CI: schema-lint, provenance-check, secret-scan, pii-scan, and FAIR+CARE alignment per KFM-MDP.  [oai_citation:19‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.6".pdf](file-service://file-THbHjFhwcakK4cmtqgRiP2)  

Key architectural decisions:

- **Config-driven pipelines** (Hydra/DVC-style) for ETL and AI ensure no hidden magic; each run has a frozen config and Experiment ID.  [oai_citation:20‡Master Coder Protocol 2.0.pdf](file-service://file-XjPWZrWdLTrVng7soAnSHp)  
- **Near-real-time provenance**: ETL and AI jobs emit PROV-O events to a triple store and/or Neo4j, enabling lineage queries and audit trails.  [oai_citation:21‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- **AI as a first-class but constrained layer**: AI components never operate “off-ledger”; all AI outputs must map to the graph and have PROV attribution.

---

## 📦 Data & Metadata

### STAC, DCAT, and PROV in Practice

- **STAC Items**  
  - Represent individual assets (e.g., a scanned 1873 county map, a LiDAR tile, a daily precipitation grid).  
  - Include `geometry`, `bbox`, `datetime`, `assets`, and KFM-specific properties (e.g. `kfm:dataset_id`, `kfm:lineage_id`).  [oai_citation:22‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  

- **DCAT Datasets**  
  - Group STAC Items into coherent collections (e.g., “USGS Historical Topographic Maps for Kansas”).  [oai_citation:23‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
  - Record `dct:title`, `dct:description`, `dct:temporal`, `dct:spatial`, `dct:publisher`, `dct:license`.  [oai_citation:24‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

- **PROV-O Lineage**  
  - For each STAC Item or DCAT Dataset, capture `prov:wasDerivedFrom` (sources), `prov:wasGeneratedBy` (ETL / AI activities), and `prov:wasAttributedTo` (agents).  [oai_citation:25‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
  - Use STAC Versioning Extension + PROV links to represent dataset version graph, enabling “lock to version” functionality in the UI.  [oai_citation:26‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  

### Knowledge Graph Entities

In Neo4j, KFM-OP models:

- `:Place` (aligned with CIDOC E53 Place, GeoSPARQL `geo:Feature`).  
- `:Event` (CIDOC E5 Event), with temporal extents and links to related Places and Actors.  [oai_citation:27‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
- `:Actor` (people, institutions, tribes; CIDOC E39 Actor), including role and provenance metadata.  
- `:Dataset`, `:Document`, `:Map`, and `:ModelRun` as content entities with STAC/DCAT/PROV identifiers.  
- Version and lineage relationships: `:PREDECESSOR`, `:SUCCESSOR`, and provenance edges derived from PROV-O.  [oai_citation:28‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  

---

## 🧠 AI Modeling & Workflows

KFM’s AI stack is multi-modal and multi-stage. This section summarizes the reference patterns; domain teams may extend them, but **must not** violate governance constraints.

### Core Modalities

- **NLP**  
  - Entity extraction (people, places, dates), event detection, relation extraction from diaries, newspapers, treaties.  [oai_citation:29‡Comprehensive Open Data Sources and Tools for the Kansas Frontier-Matrix Project.pdf](file-service://file-TaFEKzoaANSnQHWuupWH38)  
  - Uses open-source libraries (spaCy, transformers) and custom prompts/models where required.

- **Computer Vision & Remote Sensing**  
  - Map feature detection (roads, rivers, symbols) and remote-sensing pattern recognition (erosion, land use change).  [oai_citation:30‡Comprehensive Open Data Sources and Tools for the Kansas Frontier-Matrix Project.pdf](file-service://file-TaFEKzoaANSnQHWuupWH38) [oai_citation:31‡Archaeology, Artificial Intelligence, and Open Technology in Kansas.pdf](file-service://file-9aFuomr639RKSVn3XkU8s5)  

- **Geoanalytics & Time-Series**  
  - Climate trend analysis, flood/drought indicators, vegetation indices, and event-aligned environmental signals, using Pangeo/xarray-style stacks.  [oai_citation:32‡Comprehensive Open Data Sources and Tools for the Kansas Frontier-Matrix Project.pdf](file-service://file-TaFEKzoaANSnQHWuupWH38)  

- **Graph Analytics & Embeddings**  
  - Node embeddings and community detection for Story Node suggestions, “similar sites” recommendations, and temporal change detection.  [oai_citation:33‡AI Foundations of Computational Agents 3rd Ed.pdf](file-service://file-ASg7okzBAR8vUGsVkT9JsC)  

### Workflow Patterns

1. **Ingest & Normalize**  
   - Dataset enters staging; STAC/DCAT/PROV metadata created/validated; sensitive content flagged.  [oai_citation:34‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  

2. **AI Enrichment Pass**  
   - NLP, vision, or geo-models run in batch or streaming mode to produce structured annotations (entities, events, extents, scores).  
   - Outputs land in temporary graph structures or side-car JSON, always with PROV attribution to model + config + data version.  [oai_citation:35‡Master Coder Protocol 2.0.pdf](file-service://file-XjPWZrWdLTrVng7soAnSHp)  

3. **Human-in-the-Loop Review (where applicable)**  
   - Certain outputs (especially involving Indigenous lands or sensitive events) require human review before promotion.  [oai_citation:36‡Archaeology, Artificial Intelligence, and Open Technology in Kansas.pdf](file-service://file-9aFuomr639RKSVn3XkU8s5)  

4. **Graph Integration**  
   - Validated AI outputs mapped into Neo4j using KFM-OP; deduplication and conflict resolution run via Cypher scripts.  

5. **Expose via APIs**  
   - AI-derived facets become queryable (e.g. “find all events related to X between 1870–1890” or “suggest story nodes for this treaty”).  

6. **Focus Mode & Story Nodes**  
   - AI suggests content and structure, but Story Node authors retain final editorial control; Focus Mode surfaces AI explanations and provenance.

---

## 🧠 Story Node & Focus Mode Integration

The AI architecture is tightly coupled to Story Nodes and Focus Mode.

- **Story Nodes**  
  - Each Story Node references a stable `doc_uuid`, graph entities (Places, Events, Actors), and data sources (STAC/DCAT items).  
  - AI can propose narratives, timelines, and spatial extents, but governance requires explicit review for contested or sensitive histories.

- **Focus Mode**  [oai_citation:37‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  
  - A “deep dive” UI state centered on a topic (e.g., “Cheyenne Bottoms flood of 1951”).  
  - When activated:
    - Map centers and locks to topic extent/time range.  
    - Panels show multi-modal evidence: climate series, maps, documents, graph context.  
    - AI explanations and provenance panels reveal how content was assembled and which models contributed.  
    - Governance panel shows any CARE-driven protections (e.g. blurred locations, access restrictions).  

- **AI Constraints in Focus Mode**  
  - MAY: summarize data, highlight patterns, propose alternative views.  
  - MUST NOT: invent historical facts, infer Indigenous knowledge, or override governance flags.  [oai_citation:38‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.6".pdf](file-service://file-THbHjFhwcakK4cmtqgRiP2)  

---

## ⚖ FAIR+CARE & Governance

KFM’s AI pipeline is explicitly governed by FAIR+CARE and KFM’s security policy:

- **FAIR**  
  - *Findable*: STAC/DCAT catalogs, DOIs/IDs, and Neo4j graph IDs.  [oai_citation:39‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
  - *Accessible*: Open formats (JSON, GeoJSON, NetCDF, Turtle/JSON-LD), documented APIs.  [oai_citation:40‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
  - *Interoperable*: STAC/DCAT/PROV-O, GeoSPARQL, CIDOC-CRM, schema.org alignments.  [oai_citation:41‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
  - *Reusable*: Versioning, provenance, and clear licensing per dataset.

- **CARE**  [oai_citation:42‡Master Coder Protocol 2.0.pdf](file-service://file-XjPWZrWdLTrVng7soAnSHp)  
  - *Collective Benefit*: AI features must not privilege exploitative uses; Story Nodes and Focus Mode are designed for education and understanding.  
  - *Authority to Control*: Indigenous partners and data stewards can veto or shape AI uses involving their lands or histories; `indigenous_rights_flag` enforces additional review.  
  - *Responsibility*: AI pipelines include PII scans, sensitive-site filters, and Indigenous content checks before public publication.  [oai_citation:43‡Scalable Data Management for Future Hardware.pdf](file-service://file-Ux6jzbNvAwxsoYck7ECWJx)  
  - *Ethics*: Ethical impact assessments and AI model cards are required for major AI models; misuse scenarios considered and mitigated.  [oai_citation:44‡Master Coder Protocol 2.0.pdf](file-service://file-XjPWZrWdLTrVng7soAnSHp)  

- **Security & Integrity**  [oai_citation:45‡Scalable Data Management for Future Hardware.pdf](file-service://file-Ux6jzbNvAwxsoYck7ECWJx)  
  - Checksums and cryptographic hashes recorded for datasets and AI artifacts.  
  - SBOM and SLSA attestations required for AI code and dependencies.  
  - Threat-model integration ensures AI features do not bypass KFM’s security controls (e.g. by exposing sensitive coordinates).

---

## 🧪 Validation & CI/CD

AI architecture changes participate fully in KFM’s CI/CD regime:

### Test Profiles

From the global `test_profiles` (see KFM-MDP):  [oai_citation:46‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.6".pdf](file-service://file-THbHjFhwcakK4cmtqgRiP2)  

- `markdown-lint`, `schema-lint`, `metadata-check`, `diagram-check`, `accessibility-check`  
- `provenance-check`, `footer-check`, `secret-scan`, `pii-scan`  

AI-specific additions:

- `ai-config-check` — ensure AI pipelines are config-driven (no hard-coded paths, seeds, or credentials).  
- `ai-provenance-check` — verify that inference runs emit PROV-O records with model, data, and config IDs.  
- `ai-governance-check` — fail if models or pipelines are enabled for datasets flagged as restricted by CARE policies.

### Release & Reproducibility

- Each AI model and experiment is associated with:
  - Experiment ID (e.g. `AI-EXP-001`), code commit, data version, config hash.  [oai_citation:47‡Master Coder Protocol 2.0.pdf](file-service://file-XjPWZrWdLTrVng7soAnSHp)  
  - Stored artifacts (model weights, evaluation plots) under structured directories keyed by Experiment ID.  
- Releases under `releases/v11.2.6/` capture:
  - Frozen ETL + AI configs.  
  - SBOM for AI dependencies.  
  - Manifest of datasets and model artifacts.

---

## 🕰️ Version History

| Version   | Date       | Author        | Summary                                                                 |
|----------:|-----------:|--------------|-------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-11 | `<your-name>` | Initial in-repo AI architecture guide aligned with KFM-MDP v11.2.6; mapped ETL→STAC/DCAT/PROV→Neo4j→API→Focus Mode; codified AI constraints, FAIR+CARE integration, and CI checks. |

---

<div align="center">

🤖 **Kansas Frontier Matrix — AI Project Reference Data & Architecture Guide**  
Architecture · AI · Knowledge Graph · Focus Mode  

[📘 Docs Root](..) · [🧱 Architecture Index](./) · [🛡 Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>