---
title: "📁 Kansas Frontier Matrix — Land Treaties Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/historical/land-treaties/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

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

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Module"
header_profile: "standard"
footer_profile: "standard"

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
    - "📦 Data & Metadata"
    - "🧱 Architecture"
    - "🧪 Validation & CI/CD"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

provenance_chain:
  - "docs/data/historical/land-treaties/README.md@v11.2.2"
  - "docs/data/historical/land-treaties/README.md@v11.2.1"
  - "docs/data/historical/land-treaties/README.md@v11.1.0"

json_schema_ref: "../../../schemas/json/story-node.schema.json"
shape_schema_ref: "../../../schemas/shacl/story-node-shape.ttl"
doc_uuid: "urn:kfm:module:land-treaties:v11.2.6"
semantic_document_id: "kfm-module-land-treaties-v11.2.6"
event_source_id: "ledger:kfm:module:land-treaties:v11.2.6"
---

<div align="center">

# 📁 **Kansas Frontier Matrix — Land Treaties Module**  
`docs/data/historical/land-treaties/`

**Purpose**  
Provide authoritative, structured, governed treaty datasets (≈1850–1890) for narrative, geospatial, and historical interpretation within the Kansas Frontier Matrix v11 architecture, tightly integrated with the canonical pipeline:

Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-purple)]()  
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

It sits under the **Historical Data Domain** (`data/historical/`) and specializes that domain’s rules for land-treaty material: jurisdictional change, treaty polygons, and treaty-driven narratives.

This module connects:

- Source archives (e.g., state archives, NARA, BLM GLO, tribal archives, partner-curated open data)  
- ETL workflows (OCR, NER, geocoding, polygon construction)  
- The KFM **knowledge graph** (Neo4j) and geospatial front-end layers  
- The KFM **map + timeline UI**  
- **Story Nodes** and **Focus Mode** narratives backed by treaty data  

All content here must be:

- **Schema-valid** (STAC, DCAT, PROV-O, GeoSPARQL, CIDOC-CRM, OWL-Time)  
- **Provenance-complete**, with traceable ETL runs and agents  
- **Governance-compliant**, masking or generalizing locations or details that are sensitive under FAIR+CARE and Indigenous sovereignty policies [oai_citation:0‡kfm_markdown_protocol_v11.2.6.md.pdf](file-service://file-S1j2ngbeczrSfsWfRkKX9B)  

This README is the module-level governance and architecture contract; dataset-level READMEs and pipeline configs must reference and comply with it.

---

## 🗂️ Directory Layout

Emoji-enriched, CI-safe layout for this module, following KFM-MDP’s `immediate-one-branch-with-descriptions-and-emojis` layout profile (📁 = directory, 📄 = markdown/text, 🧾 = config/JSON/TTL, 🧪 = tests/fixtures). [oai_citation:1‡kfm_markdown_protocol_v11.2.6.md.pdf](file-service://file-S1j2ngbeczrSfsWfRkKX9B)  

~~~text
docs/data/historical/land-treaties/
│
├── 📄 README.md                      # This file: module overview & governance contract
│
├── 📁 stac/                          # STAC metadata for treaty assets
│   ├── 📁 collections/               # STAC Collection JSONs (e.g., treaties-kansas-v1)
│   └── 📁 items/                     # STAC Items per asset (polygons, scans, docs)
│
├── 📁 schemas/                       # JSON Schema / SHACL / ontology fragments
│   ├── 🧾 json/                      # JSON Schemas for treaty data records
│   └── 🧾 ttl/                       # SHACL shapes & ontology fragments (CIDOC, OWL-Time)
│
├── 📁 workflows/                     # ETL and orchestration configs
│   ├── 📁 etl/                       # Deterministic ETL job definitions (YAML/Python)
│   └── 📁 jobs/                      # Orchestration specs (cron, Airflow/Dagster, etc.)
│
├── 📁 qa/                            # Fixtures and validation reports
│   ├── 🧪 fixtures/                  # Minimal test data (polygons, sample docs)
│   └── 🧾 reports/                   # Schema/STAC/lineage validation reports
│
├── 📁 samples/                       # Samples and tutorials
│   ├── 📁 data/                      # Example treaty boundaries, CSV excerpts, micro-STAC
│   └── 📁 notebooks/                 # Walkthroughs (e.g., “load a treaty polygon”)
│
└── 📁 assets/                        # Static source material and configs (governed)
    ├── 🧾 config/                    # Module-level configuration (YAML/TOML/JSON5)
    └── 📁 docs/                      # Scanned treaties, reference PDFs, supporting maps
~~~

Requirements:

- Any change to this layout must be reflected here.  
- New subdirectories **must** document purpose, governance, and relationship to ETL and catalogs.  
- No ad-hoc or personal scratch directories under this path; use project-wide scratch locations instead.

---

## 📦 Data & Metadata

This module’s primary objects are **treaty events**, **treaty polygons**, and **treaty documents**, modeled consistently across:

- STAC Collections/Items (spatiotemporal assets) [oai_citation:2‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  
- DCAT datasets (catalog-level metadata) [oai_citation:3‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  
- PROV-O bundles (lineage of scans, ETL, and derivatives) [oai_citation:4‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- GeoSPARQL / OWL-Time / CIDOC-CRM entities in the Neo4j graph [oai_citation:5‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

### STAC

Treaty-related assets (polygons, georeferenced maps, scans, transcriptions) are described as:

- **Collections** (e.g., `treaties-kansas-v1`) capturing:
  - Spatial extent (often multi-county or multi-state)  
  - Temporal extent (negotiation/ratification windows)  
  - License and providers (archives, tribal partners, institutions)  
  - Keywords (e.g., `"treaty"`, `"reservation"`, `"cession"`)  
- **Items** for each distinct spatiotemporal slice:
  - `geometry` / `bbox` in EPSG:4326  
  - `properties.datetime` (primary event date) plus interval extensions if multi-day  
  - `assets` such as:
    - `polygon` (GeoJSON/COG)  
    - `scan` (PDF/TIFF)  
    - `transcription` (text/markdown)  
    - Optional `summary` / `notes`  

All STAC artifacts must validate against the KFM STAC profile and pinned validator versions in CI. [oai_citation:6‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  

### DCAT

Each treaty series exposed outside internal scratch is modeled as a `dcat:Dataset` within a DCAT 3–compliant catalog: [oai_citation:7‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  

- Titles and descriptions oriented to public discovery, not internal jargon  
- Spatial coverage referencing treaty polygons or named places  
- Temporal coverage reflecting negotiation/ratification/implementation periods  
- Distribution entries that typically point at:
  - STAC Collections/Items  
  - Downloadable derivative products (e.g., generalized public polygons)  

DCAT records must be exportable as static RDF/JSON-LD for external harvesting and triple-store loading.

### GeoSPARQL, CIDOC-CRM, OWL-Time

In the knowledge graph:

- Geometry is modeled via **GeoSPARQL 1.1**:
  - `geo:Feature` nodes for treaty-related places  
  - `geo:Geometry` nodes linked with `geo:hasGeometry`  
  - WKT literals (`geo:wktLiteral`) and optional GeoJSON serializations [oai_citation:8‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
- Heritage semantics follow **CIDOC-CRM**:
  - `E5 Event` — treaty negotiations/ratifications  
  - `E53 Place` — negotiation sites and affected lands  
  - `E39 Actor` — tribal nations, U.S. government, signatories  
  - `E31 Document` — treaty texts and scans  
- Temporal coverage uses **OWL-Time**:
  - `time:Interval` with `time:hasBeginning` / `time:hasEnd`  
  - Precision (year / month / day) stored explicitly when granular dates are unknown  

The combination of GeoSPARQL, OWL-Time, and CIDOC-CRM is required so treaty queries can mix **where**, **when**, and **who** consistently (e.g., “treaties affecting this county between 1860 and 1875”). [oai_citation:9‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

### PROV-O

All key datasets and derivatives (e.g., generalized public polygons) must be linked to **PROV-O**:

- `prov:Entity` — scans, transcriptions, vector layers, STAC Items  
- `prov:Activity` — ETL runs, manual curation, QA/approval steps  
- `prov:Agent` — teams, institutions, automated systems [oai_citation:10‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

At minimum:

- `prov:wasGeneratedBy` (entity → ETL run)  
- `prov:used` (ETL run → source entities)  
- `prov:wasAssociatedWith` (ETL run → responsible agent/team)  

PROV bundles live alongside DCAT records and are referenced from STAC Items where appropriate.

---

## 🧱 Architecture

The Land Treaties Module is a **specialized slice** of the standard KFM pipeline, tuned for high-sensitivity historical and Indigenous content and governed by KFM-MDP v11.2.6 and MCP-DL v6.3.  

### Deterministic, Config-Driven ETL

Workflows in `workflows/etl/`:

- Are **deterministic** and **idempotent**:
  - No unseeded randomness  
  - Pinned NLP models and geoprocessing libraries  
  - Stable reprojection and simplification parameters  
- Are **config-driven**:
  - ETL configs live in `assets/config/` and, for cross-module reuse, under `configs/historical/` in the repo root (referenced here, not duplicated)  
  - All tunable parameters (OCR thresholds, NER models, snapping tolerances) are encoded in configuration rather than code constants  

Running the same ETL job with the same inputs must produce identical outputs and checksums.

### State Management, WAL, and Rollback

Before any write to STAC, DCAT, or Neo4j:

- A **write-ahead log (WAL)** is generated describing intended changes (by ID)  
- Snapshots or diffs of previous states are captured for reversible operations  

Rollback tools in `workflows/jobs/` must support:

- Reverting by `run_id` (OpenLineage run identifier)  
- Restoring prior catalog/graph state from WAL and snapshot manifests  

This is especially important for treaty content because governance decisions may require rapid rollback or reclassification if newly discovered sensitivities arise.

### Telemetry, Energy, and Carbon

Every ETL or enrichment job must emit telemetry conforming to the module schemas:

- `telemetry_schema` — base job metrics and SLO alignment  
- `energy_schema` — estimated energy consumption (Wh)  
- `carbon_schema` — estimated carbon footprint (e.g., µg CO₂eq)  

Telemetry aggregates into `telemetry_ref` and feeds both reliability dashboards and sustainability accounting consistent with KFM’s broader data-management practices.  

### OpenLineage Integration

Each run emits an **OpenLineage** event capturing:

- `run_id`, optional `parent_run_id`  
- `job_name` (e.g., `treaties_ingest_v2`)  
- `inputs[]` and `outputs[]` keyed by STAC/DCAT/graph identifiers  
- `facets` describing:
  - Code version (commit hash)  
  - Config version  
  - Environment hash (container image, dependencies)  

This enables graph-wide tracing: from a Focus Mode narrative back through graph nodes, STAC Items, ETL runs, and ultimately raw archive scans.

---

## 🧪 Validation & CI/CD

Treaty data is **never** considered production-ready until it passes module-level and cross-module CI gates.

### Schema and Catalog Validation

CI workflows must:

- Validate all STAC Collections/Items in `stac/` against the pinned KFM STAC profile and official JSON Schemas  
- Validate DCAT datasets for structural correctness and key constraints (identifiers, rights, spatial/temporal coverage) [oai_citation:11‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  
- Validate PROV bundles for well-formed entities, activities, and agents [oai_citation:12‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- Run SHACL validation for graph-facing shapes in `schemas/ttl/`, including GeoSPARQL and OWL-Time constraints [oai_citation:13‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

Validation reports should be written to `qa/reports/` and referenced from PRs that modify treaty data or schemas.

### Data Integrity and Spatial Quality

Additional automated checks include:

- Geometry validity (no self-intersections; tolerances recorded where simplification is applied)  
- CRS consistency (inputs reprojected to EPSG:4326 before publication)  
- Topological sanity for treaty polygons (e.g., no impossible overlaps between mutually exclusive cessions)  
- Referential integrity between:
  - STAC/graph IDs  
  - Dataset-level READMEs  
  - Story Node references  

### Reproducibility and Experiment Logs

Where AI/ML is used (e.g., OCR, NER, boundary inference), the module follows MCP’s reproducibility rules:

- Configured runs with recorded seeds and hyperparameters  
- Experiment identifiers linked to outputs in PROV and optional experiment logs under `mcp/experiments/historical/`  

---

## 🧠 Story Node & Focus Mode Integration

Treaties are central to many KFM Story Nodes and Focus Mode experiences. The module is therefore **Story-Node-ready** per KFM-MDP v11.2.6.  

### Story Nodes

Story Nodes binding to the Land Treaties Module must:

- Validate against `json_schema_ref` and `shape_schema_ref`  
- Use **real graph identifiers** (e.g., `neo4j://Event/...`, `neo4j://Place/...`)  
- Provide, at minimum:
  - `id` (stable, human-readable)  
  - `title`  
  - `summary`  
  - `narrative.body` (Markdown)  
  - `spacetime.geometry` and `spacetime.when`  

Illustrative (non-normative) example:

~~~yaml
story_node:
  id: "treaty-medicine-lodge-1867"
  title: "Medicine Lodge Treaties (1867)"
  summary: "Three treaties negotiated between the U.S. and Plains tribes along Medicine Lodge Creek in October 1867."
  narrative:
    body: |
      The Medicine Lodge treaties of 1867 were negotiated between the United States
      and several Plains tribes, including the Kiowa, Comanche, Apache, Arapaho, and
      Cheyenne. These agreements redefined reservation boundaries and attempted to
      confine tribal nations to specific territories in Indian Territory.
    format: "text/markdown"
  spacetime:
    geometry: { /* GeoJSON polygon representing a generalized treaty area */ }
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

Narrative text must be **data-backed** and clearly distinguish:

- Facts directly supported by data and graph  
- Interpretation (reasoned, sourced narrative)  
- Explicitly labeled speculation (where allowed), or omission where speculative content would be harmful  

### Focus Mode

Focus Mode treats a treaty **Event** or treaty-related Story Node as a focus anchor and:

1. Queries the Neo4j graph for the local neighborhood:
   - Negotiation sites (Places)  
   - Participating tribes & agents (Actors)  
   - Linked documents (E31)  
   - Subsequent events (implementation, conflicts, migrations)  
2. Materializes relevant STAC and spatial assets (polygons, scans, atlases)  
3. Uses pinned AI summarization models to generate short, data-backed narratives with explicit provenance  
4. Returns a bundle containing:
   - Focus summary  
   - Map layers and timeline context  
   - Links to Story Nodes and source documents  

All Focus Mode outputs must:

- Respect **CARE** and sovereignty masking rules  
- Expose “see sources” links back to STAC/DCAT/graph entities  
- Avoid speculative or sensational interpretations, especially for contested or traumatic histories [oai_citation:14‡KFM’s AI Project Reference Data.pdf](file-service://file-3GvMUA8YBFYyqQnq9ArHAm)  

---

## ⚖ FAIR+CARE & Governance

Land-treaty data intersects with:

- Indigenous sovereignty and governance  
- Histories of displacement, conflict, and trauma  
- Locations of reservations, homelands, and other culturally significant spaces  

Accordingly:

- **FAIR**:
  - Datasets must be findable and interoperable via STAC/DCAT/PROV, with stable identifiers and open formats.  
  - Provenance must make it clear how each public geometry or narrative was derived. [oai_citation:15‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- **CARE and Indigenous data sovereignty**:
  - Mask or generalize sensitive locations (e.g., to county or region scale).  
  - Where Indigenous partners request non-publication, provide **metadata-only** entries or omit entirely from public catalogs.  
  - Honor tribal governance decisions on representation, terminology, and narrative framing. [oai_citation:16‡kfm_markdown_protocol_v11.2.6.md.pdf](file-service://file-S1j2ngbeczrSfsWfRkKX9B)  

Concrete requirements:

- Every dataset in this module must declare:
  - Sensitivity level and access policy (aligned with `classification` and `sensitivity` fields)  
  - Whether it includes Indigenous content and how authority/control are handled (e.g., MOUs, tribal review processes)  
- CI/governance checks must detect:
  - Accidental exposure of disallowed precise coordinates  
  - Missing rights or sovereignty metadata in DCAT and PROV  
- When in doubt, the default posture is **conservative**:
  - Treat the dataset as sensitive  
  - Seek guidance from the FAIR+CARE Council and relevant Indigenous partners before publication  

---

## 🕰️ Version History

| Version  | Date       | Author        | Notes                                                                 |
|----------|------------|---------------|-----------------------------------------------------------------------|
| v11.2.6  | 2025-12-11 | `<your-name>` | Aligned with KFM-MDP v11.2.6: emoji layout, H2 registry, footer, CI. |
| v11.2.2  | 2025-11-30 | `<your-name>` | Initial v11-compliant Land Treaties Module README.                    |

Update this table whenever structural, governance, or pipeline-significant changes are made, and keep `provenance_chain` synchronized.

---

<div align="center">

📁 **Kansas Frontier Matrix — Land Treaties Module**  
Scientific Insight · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Docs Root](../../../README.md) · [📂 Standards Index](../../../standards/INDEX.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · STAC/DCAT · CIDOC-CRM · OWL-Time · GeoSPARQL · PROV-O · SLSA Level 3 · SPDX 2.3 · OpenLineage  

**♻️ Sustainability:**  
Energy & Carbon Telemetry Enabled (ISO 50001 / ISO 14064)

</div>