---
title: "🧠 Kansas Frontier Matrix — AI · ETL Integration Architecture Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai-etl-integration.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
backward_compatibility: "Full v11.x-compatible (Pipeline Contract v11.0)"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/pipelines-ai-etl-integration-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "High Governance · AI-Constrained · Full Provenance · Auto-Masked Sensitive Data"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "ai-etl-integration"
category: "Pipelines · AI/ML · ETL · Lineage"
sensitivity: "General (auto-masking for protected datasets)"
classification: "Public Document"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM AI Lineage Extensions"
openlineage_profile: "OpenLineage v2.5 + KFM AI Extensions"

ontology_ref:
  - "../graph/ontology/core-entities.md"
  - "../graph/ontology/cidoc-crm-mapping.md"
  - "../graph/ontology/spatial-temporal-patterns.md"

metadata_profiles:
  - "../../schemas/stac/kfm-stac-v11.json"
  - "../../schemas/dcat/kfm-dcat-v11.json"
  - "../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"
  - "lineage-audit-v11"
  - "governance-audit-v11"
  - "etl-validation-v11"
  - "ai-governance-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

runtime:
  compute: "KFM Multi-Cloud Mesh (AWS + GCP + On-Prem)"
  graph_engine: "Neo4j Enterprise v5.x Cluster"
  api_stack: "FastAPI · GraphQL Gateway (GovHooks v4)"
  frontend_stack: "React · MapLibre · Cesium · Vite"
  lineage_bus: "OpenLineage v2.5"
  reliability_engine: "Reliable Pipelines v11 — WAL · Retry · Rollback · Hotfix · Lineage"
  agents: "LangGraph Autonomous Updater v11"

fair_category: "F1-A1-I1-R1"
sensitivity_level: "Low"
public_exposure_risk: "Low to Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/pipelines-ai-etl-integration-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/pipelines-ai-etl-integration-v11-shape.ttl"

doc_uuid: "urn:kfm:docs:pipelines:ai-etl-integration:v11.0.0"
semantic_document_id: "kfm-pipelines-ai-etl-integration"
event_source_id: "ledger:docs/pipelines/ai-etl-integration.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "schema-hints"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified data fabrication"
  - "modifying normative requirements"
  - "overwriting authoritative source values"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major AI/ETL contract revision (v12)"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — AI · ETL Integration Architecture Guide (v11.0.0)**  
`docs/pipelines/ai-etl-integration.md`

**Purpose:**  
Define the **canonical v11 architecture and guardrails** for integrating AI/ML components into KFM’s ETL pipelines.  
Ensures AI remains *assistive, constrained, explainable, provenance-complete*, and fully aligned with FAIR+CARE, sovereignty, STAC/DCAT v11, and the Neo4j ontology stack.

</div>

---

# 📘 Executive Summary

AI in KFM v11 is **not** an opaque black-box bolted onto ETL — it is a **tightly-governed, lineage-rich co-pilot** that:

- Performs OCR, NER, geocoding, summarization, pattern detection, and predictive modeling  
- Emits **derived** or **annotative** fields only (never overwriting sources-of-truth)  
- Publishes all outputs as **provenance-attached, schema-validated entities**  
- Powers **Focus Mode v3** and **Story Nodes v3** with explainable narratives  
- Operates under explicit CARE, sovereignty, and ethics constraints  

This guide describes **how AI components must attach to ETL pipelines**, which responsibilities belong to AI vs. deterministic code, and what validation + observability requirements apply before AI outputs are promoted into the KFM knowledge graph.

---

# 🧩 1. AI Roles in the ETL Stack

AI components are allowed to perform the following categories of tasks:

- **Perception**  
  - OCR on scanned maps and documents  
  - Image-to-text extraction for historical imagery  

- **Understanding**  
  - NER (people, places, events, organizations)  
  - Geoparsing & geocoding using GNIS / OSM / tribal gazetteers  
  - Topic tagging & document classification (treaty vs. newspaper vs. deed)  

- **Summarization & Narrative Preparation**  
  - Document-level summaries (for UI cards, Focus mode, Story Node candidates)  
  - Multi-document condensed overviews (with explicit provenance aggregation)  

- **Pattern & Predictive Modeling**  
  - Climate/hazards projections (where models exist and are documented)  
  - Outlier detection & anomaly surfacing (e.g., suspicious flood records, corrupted time series)  

- **Schema Assistance**  
  - Suggesting CIDOC-CRM class mappings (never auto-committing)  
  - Suggesting relationships for human review in curation workflows  

Every AI output must be treated as **data with its own provenance**, not as an unquestionable truth.

---

# 🗺️ 2. Integration Architecture

```mermaid
flowchart LR
    A["Raw Inputs
    (docs, maps, rasters, tables, sensors)"]
        --> B["Deterministic ETL
        (parse, normalize, reproject)"]

    B --> C["AI Enrichment Layer
    OCR · NER · Geocoding · Summaries · Predictions"]

    C --> D["Validation & Governance
    Schema · CARE · Sovereignty · Lineage"]

    D --> E["Knowledge Graph
    Neo4j · CIDOC-CRM · GeoSPARQL · OWL-Time · PROV-O"]

    D --> F["STAC/DCAT Registries
    data/stac · catalogs"]

    E --> G["Focus Mode v3 · Story Nodes v3"]
```

**Key principles:**

- AI is **logically downstream** of deterministic ETL.  
- No ingest path is *only* AI — all flows pass through deterministic checks.  
- Promotion into the graph/UI requires validation & governance approval.

---

# 🧱 3. Responsibilities & Boundaries

## 3.1 Deterministic ETL Responsibilities

Deterministic code is responsible for:

- Basic parsing & format conversions (CSV → normalized table, TIFF → COG)  
- CRS normalization and geometry fixing  
- Unit conversions & numeric sanity checks  
- Cross-field consistency checks (date ranges, ID formats, referential integrity)  
- Guaranteeing that AI receives **clean, predictable** input  

## 3.2 AI Responsibilities

AI components are responsible for:

- Generating candidate annotations, labels, summaries, and derived metrics  
- Providing **confidence scores, uncertainty indicators, and explanations**  
- Attaching PROV-O lineage (`prov:wasGeneratedBy` AI activity)  
- Respecting domain constraints (e.g., not inventing treaty dates)  

## 3.3 Hard Boundaries

- AI may **not**:
  - Overwrite original fields from authoritative sources  
  - Bypass schema validation or sovereignty checks  
  - Persist new graph entities without passing through pipeline validation  
  - Generate speculative numeric values that look like measurements  

- All AI writes are:
  - Clearly namespaced (e.g., `ai_summary`, `ai_tags`, `ai_confidence`)  
  - Linked to model IDs and versioned configurations  
  - Upgradeable/fixable by re-running the same pipeline  

---

# 🧪 4. Data Contracts for AI Outputs

AI outputs are governed by **KFM Pipeline Data Contracts (KFM-PDC v11.0)**:

- Each AI field (e.g., `ai_summary`, `ai_place_candidates`, `ai_event_link_hints`) is defined in a **JSON Schema**  
- Contracts specify:
  - Type, allowed ranges, required metadata  
  - Required provenance fields (model ID, version, timestamp)  
  - Expected confidence structure (e.g., `p_high`, `p_medium`, `p_low`)  

AI/ETL pipelines MUST:

- Validate their AI outputs against the schemas referenced by `json_schema_ref`  
- Reject or quarantine outputs that fail schema or governance criteria  
- Record failures as OpenLineage events for debugging and audit

---

# 🛰️ 5. Provenance & Observability for AI Steps

Every AI step must emit:

- A PROV-O `prov:Activity` node (AI inference)  
- `prov:used` references to:
  - Input entities  
  - Model artifact (e.g., Story Summary Model v3.2)  
  - Configuration (prompt or hyperparameters)  
- `prov:generated` references to the resulting entities/fields  

These lineage events are published to:

- The **OpenLineage bus**  
- The **Neo4j lineage graph**  
- STAC `processing` and `lineage` properties where applicable  

This enables:

- Re-running a given AI step with identical inputs for reproducibility  
- Tracing all fields displayed in Focus Mode back to an exact inference call  
- Debugging model performance, drift, and bias over time  

---

# 🧭 6. Focus Mode v3 Integration

AI outputs are key inputs to Focus Mode v3, but must satisfy:

- **Validation**: Only AI summaries whose underlying entities pass ETL/graph validation are used  
- **Explainability**: Focus panels must be able to show:
  - Source documents  
  - Supporting data points  
  - Model version & configuration  
- **Ethics & CARE**:
  - No sensitive tribal information surfaced without proper flags  
  - No speculative or uncorroborated historical claims in narrative form  

Focus Mode uses AI primarily to:

- Rank and highlight relevant entities for the user’s focal selection  
- Generate concise, citation-rich summaries from validated data  
- Suggest candidate Story Nodes for human curation  

---

# 📖 7. Story Nodes v3 Integration

AI/ETL integration for Story Nodes:

1. Deterministic ETL:
   - Ensures all referenced entities (events, places, people) exist and are valid  
   - Provides the base spatiotemporal envelope  

2. AI:
   - Proposes narrative candidates (`ai_story_candidates`)  
   - Provides descriptive text and multi-document summarization  

3. Validation & Governance:
   - Enforces `story-node.schema.json`  
   - Applies CARE & sovereignty rules  
   - Approves or rejects Story Node promotion  

4. Graph Load:
   - Approved Story Nodes become first-class entities in the graph  
   - Focus Mode can reuse them as narrative anchors  

---

# 🛡️ 8. AI Governance & Risk Controls

The following controls are mandatory:

- **Model Registry**: Every model used in ETL has:
  - Unique ID  
  - Version  
  - Training data summary  
  - Intended-use statement  
  - Limitations & known failure modes  

- **Approval Gate**: New or updated models require:
  - FAIR+CARE review  
  - Sovereignty implications review (for cultural/historical data)  
  - Acceptance by the KFM FAIR+CARE Council  

- **Runtime Policies (GovHooks v4)**:
  - Prevent model use outside its approved scope  
  - Enforce max-confidence thresholds for unsupervised promotion  
  - Require human review for high-risk narratives or inferences  

---

# 🧾 9. Validation & CI Requirements

AI/ETL integration is covered by:

- `etl-validation-v11` — ensures ETL contracts are respected  
- `ai-governance-v11` — checks AI usage, model registry references, and provenance  
- `schema-lint-v11` — validates JSON/JSON-LD for AI fields  
- `lineage-audit-v11` — verifies PROV-O chain completeness  
- `governance-audit-v11` — confirms CARE & sovereignty adherence  

No pipeline using AI may be promoted unless all checks pass in CI.

---

# 🕰 Version History

| Version | Date       | Notes                                                                      |
|--------:|-----------:|----------------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial AI · ETL integration architecture for KFM v11 LTS.                 |

---

# 🔗 Footer

**Back to Root:** `../../README.md`  
**Back to Architecture:** `../architecture/system_overview.md`  
**Back to Standards:** `../standards/README.md`

