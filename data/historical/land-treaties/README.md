---
title: "📁 Kansas Frontier Matrix — Land Treaties Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/historical/land-treaties/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/telemetry.json"
telemetry_schema: "../../../schemas/telemetry/module-default-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Module"
semantic_intent:
  - "data-governance"
  - "heritage-records"
  - "treaty-boundaries"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Enforced"
sensitivity: "High (Indigenous data — masked/generalized)"
public_exposure_risk: "Medium"
classification: "Public With Safeguards"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Supersedes previous treaty modules"
immutability_status: "version-pinned"
ai_training_inclusion: false

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "📦 Metadata & Standards Compliance"
    - "🧱 Pipeline Behavior"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧬 Version History"
    - "⚖️ Footer"

provenance_chain:
  - "docs/data/historical/land-treaties/README.md@v11.2.1"
  - "docs/data/historical/land-treaties/README.md@v11.1.0"

json_schema_ref: "../../../schemas/json/story-node.schema.json"
shape_schema_ref: "../../../schemas/shacl/story-node-shape.ttl"
doc_uuid: "urn:kfm:module:land-treaties:v11.2.2"
semantic_document_id: "kfm-module-land-treaties-v11.2.2"
event_source_id: "ledger:kfm:module:land-treaties:v11.2.2"
---

<div align="center">

# 📁 **Kansas Frontier Matrix — Land Treaties Module**  
`docs/data/historical/land-treaties/`

**Purpose:**  
Provide authoritative, structured, governed treaty datasets (≈1850–1890) for narrative, geospatial, and historical interpretation within the Kansas Frontier Matrix v11 architecture.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA%2B-brightgreen)]()  
[![SLSA Level 3](https://img.shields.io/badge/SLSA-Level%203-orange)]()

</div>

---

## 📘 Overview

The **Land Treaties Module** is the canonical home for:

- Historical treaty **events** (negotiations, signings, ratifications)  
- Treaty **boundaries** (ceded lands, reservations, hunting grounds)  
- Treaty **documents** (scans, transcriptions, translations)  
- **Actors** involved (tribal nations, leaders, U.S. officials, intermediaries)  

This module connects:

- Source archives (KHS, NARA, BLM GLO, tribal archives)  
- ETL workflows (OCR, NER, geocoding, polygon construction)  
- The KFM **knowledge graph** (Neo4j)  
- The KFM **map + timeline UI**  
- **Story Nodes** and **Focus Mode v3** narratives  

All content here must be **schema-valid**, **provenance-complete**, and **mask / generalize** locations or details that are sensitive under CARE and Indigenous sovereignty policies.

---

## 🗂️ Directory Layout

Emoji-enriched, CI-safe layout for this module:

~~~text
docs/data/historical/land-treaties/
│
├── 📄 README.md                      # This file: module overview & governance contract
│
├── 🗂️ stac/                          # STAC metadata for treaty assets
│   ├── 🗃️ collections/                # STAC Collection JSONs (e.g., treaties-kansas-v1)
│   └── 📑 items/                      # STAC Items per asset (polygons, scans, docs)
│
├── 🧬 schemas/                       # JSON Schema / SHACL / ontology fragments
│   ├── 📁 json/                      # JSON Schemas for treaty data records
│   └── 🧩 ttl/                       # SHACL shapes & ontology fragments (CIDOC, OWL-Time)
│
├── 🔁 workflows/                     # ETL and LangGraph pipelines
│   ├── ⚙️ etl/                       # Deterministic ETL job definitions (YAML/Python)
│   └── 🧵 jobs/                      # Orchestration configs (cron, Airflow/Dagster specs)
│
├── 🧪 qa/                            # Fixtures and validation reports
│   ├── 🧱 fixtures/                  # Minimal test data (small polygons, sample docs)
│   └── 📊 reports/                   # Schema/STAC/lineage validation reports
│
├── 🎛️ samples/                       # Samples and tutorials
│   ├── 🧩 data/                      # Example treaty boundaries, CSV excerpts, micro-STAC
│   └── 📓 notebooks/                 # Jupyter/MD walkthroughs (e.g., “load a treaty polygon”)
│
└── 📦 assets/                        # Static source material and configs
    ├── 🧾 config/                    # Module-level configuration (YAML/TOML/json5)
    └── 🗃️ docs/                      # Scanned treaties, reference PDFs, supporting maps
~~~

Every subdirectory MUST be kept in sync with this layout and described here if modified.

---

## 📦 Metadata & Standards Compliance

This module **must** satisfy the following standards for all datasets and files:

### STAC v1.0.0

- **Collections** (e.g., `treaties-kansas-v1`) describe:
  - spatial extent (multi-county, multi-state when relevant)  
  - temporal extent (negotiation/ratification years)  
  - license (`CC-BY 4.0` or stricter per source)  
  - providers (archives, tribal partners)  
  - keywords (e.g., `"treaty"`, `"reservation"`, `"cession"`)  

- **Items** describe:
  - `geometry` (GeoJSON polygon/multipolygon)  
  - `bbox`  
  - `properties.datetime` (primary event date; multi-day events use `start/end` extension)  
  - `assets` for each file:
    - `polygon` (GeoJSON / COG)  
    - `scan` (PDF/TIFF)  
    - `transcription` (text/markdown)  
    - `summary` or `notes` if provided  

### DCAT 3.0

- Each treaty dataset is a `dcat:Dataset` with:
  - `dct:title`, `dct:description`, `dct:creator`, `dct:publisher`  
  - `dct:temporal`, `dct:spatial`  
  - `dct:license`, `dct:rights`  
  - `dcat:distribution` entries pointing at STAC Items or static downloads  

### GeoSPARQL 1.1

- All geometries are:
  - stored as GeoJSON  
  - optionally mirrored as WKT literals in the graph  
  - default CRS: **EPSG:4326 (WGS84)**  
  - typed as `geo:Feature` / `geo:Geometry` in the graph  

### CIDOC-CRM

Mapping (minimum):

- `E5 Event` — Treaty negotiation/ratification event  
- `E53 Place` — The negotiation site and treaty polygons  
- `E39 Actor` — Tribes, U.S. government, signatories  
- `E31 Document` — Treaty texts & scans  

Relationships such as:

- `E5.P7_took_place_at → E53 Place`  
- `E5.P11_had_participant → E39 Actor`  
- `E31.P70_documents → E5 Event`  

### OWL-Time

- Treaties represented as `time:Interval` with:
  - `time:hasBeginning` / `time:hasEnd`  
  - precision (`year`, `month`, `day`) recorded in metadata  
  - original phrasing in `original_label` (e.g., `"autumn 1865"`)  

### PROV-O

For each asset:

- `prov:Entity` — STAC Item/file  
- `prov:Activity` — ETL job or transformation  
- `prov:Agent` — System / maintainer / contributing institution  

At minimum:

- `prov:wasGeneratedBy` → ETL activity  
- `prov:used` → source entities (raw scans, prior datasets)  

### FAIR+CARE

- **FAIR**:
  - Findable → STAC/DCAT + searchable IDs  
  - Accessible → stable URLs, documented access control  
  - Interoperable → open formats, standard vocabularies  
  - Reusable → clear licenses, quality notes, provenance  

- **CARE**:
  - Collective Benefit → clear articulation of use cases, including benefits to Indigenous communities  
  - Authority to Control → respect tribal governance, mask sensitive locations as requested  
  - Responsibility → no speculative claims; handle contested histories with care  
  - Ethics → no de-anonymization; no exposure of sacred or restricted sites  

If any treaty or site is flagged as **restricted** by partners, coordinates MUST be generalized (e.g., to county-level) or fully withheld.

---

## 🧱 Pipeline Behavior

All workflows under `workflows/` must follow the **KFM Reliability Framework**.

### 4.1 Determinism & Idempotency

- Use only deterministic operations (fixed random seeds, fixed NLP models & versions).  
- Running the same ETL job with the same inputs MUST produce identical outputs (same hashes).

Example responsibilities:

- OCR pipelines: same engine + language model + page segmentation config.  
- NER/relationship extraction: pinned model versions; pinned configuration.  
- Polygon creation: consistent reprojection, snapping, simplification thresholds.

### 4.2 Write-Ahead Logging (WAL) & Rollback

- Before modifying graph or STAC indices, record:
  - ID of to-be-created/updated entities  
  - previous state snapshot where applicable  

- Provide rollback tools in `workflows/` to:
  - revert an ETL run by `run_id`  
  - restore prior STAC/graph state from WAL and snapshot manifests  

### 4.3 Telemetry & SLOs

Each job MUST emit telemetry:

- `latency_slo_ms` — target latency  
- `latency_ms` — actual runtime  
- `error_budget_remaining` — error budget counter  
- `energy_wh` — estimated energy consumption  
- `carbon_ug` — estimated CO₂eq micrograms  

Telemetry flows into the KFM observability stack and is summarized in the module’s telemetry JSON referenced in the header.

### 4.4 OpenLineage Integration

Each ETL run must produce an OpenLineage event:

- `run_id` / `parent_run_id`  
- `job_name` (e.g., `treaties_ingest_v2`)  
- `inputs[]` — raw scans, source datasets, prior states  
- `outputs[]` — new STAC Items, updated graph nodes  
- `facets` — STAC IDs, DCAT URIs, code version, environment hash  

This allows cross-module lineage tracing from raw archive scans all the way to Focus Mode narratives.

---

## 🧠 Story Node & Focus Mode Integration

Treaties are central to many KFM narratives. This module must therefore support **Story Nodes** and **Focus Mode v3** out-of-the-box.

### 5.1 Story Nodes

Story Nodes bind narrative text to spacetime and graph entities.

Each Story Node MUST:

- Validate against `story-node.schema.json`  
- Reference real graph IDs (`neo4j://...`)  
- Provide at least:
  - `id`  
  - `title`  
  - `summary`  
  - `narrative.body` (Markdown)  
  - `spacetime.geometry` + `spacetime.when`  

Minimal conceptual example:

~~~yaml
story_node:
  id: "treaty-medicine-lodge-1867"
  title: "Medicine Lodge Treaty (1867)"
  summary: "Three treaties negotiated between the U.S. and Plains tribes along Medicine Lodge Creek in October 1867."
  narrative:
    body: |
      The Medicine Lodge treaties of 1867 were negotiated between the United States
      and several Plains tribes, including the Kiowa, Comanche, Apache, Arapaho, and
      Cheyenne. These agreements redefined reservation boundaries and attempted to
      confine tribal nations to specific territories in Indian Territory.
    format: "text/markdown"
  spacetime:
    geometry: { /* GeoJSON polygon approximating the council site / area */ }
    when:
      start: "1867-10-21T00:00:00Z"
      end:   "1867-10-28T00:00:00Z"
      precision: "day"
  relations:
    - rel: "references-event"
      target: "neo4j://Event/treaty-medicine-lodge"
      role: "primary"
    - rel: "mentions-place"
      target: "neo4j://Place/medicine-lodge-creek"
      role: "council-site"
~~~

Narrative text must stay within documented facts and clearly cite contested interpretations in the underlying knowledge graph, not in the Story Node itself.

### 5.2 Focus Mode v3

Focus Mode is the AI-powered contextual lens. For treaties, the Focus engine must be able to:

- Take a treaty `Event` or `Story Node` as the focus entity  
- Pull related entities within two hops:
  - negotiation site (Place)  
  - participating tribes & agents (Actors)  
  - linked documents (E31)  
  - linked subsequent events (implementations, conflicts, migrations)  

For each Focus request, the backend will:

1. Query the Neo4j graph for the neighborhood around the treaty event.  
2. Materialize relevant STAC/geo assets (polygons, maps).  
3. Use the AI summarization pipeline (pinned model version) to generate **data-backed** narrative text.  
4. Attach provenance to each summary (which graph nodes & documents were used).  

The front-end will:

- Highlight treaty polygons on the map  
- Center the timeline around the treaty interval  
- Populate the side panel with:
  - a short Focus summary  
  - list of tribes and key actors  
  - links to Story Nodes and source documents  

All Focus outputs must:

- be **non-speculative**  
- honor CARE masking rules  
- include a way for users to drill down to the underlying data (`see sources` link)

---

## 🧬 Version History

| Version | Date       | Author        | Notes |
|---------|------------|--------------|-------|
| v11.2.2 | 2025-11-30 | `<your-name>` | Initial v11-compliant Land Treaties Module README |

Update this table whenever you make structural or governance-significant changes.

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../README.md) •  
[Standards Index](../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · STAC/DCAT · CIDOC-CRM · OWL-Time · GeoSPARQL · PROV-O · SLSA Level 3 · SPDX 2.3 · OpenLineage

**♻️ Sustainability:**  
Energy & Carbon Telemetry Enabled (ISO 50001 / ISO 14064)

**End of Document**

</div>