---
title: "💧 Kansas Frontier Matrix — Hydrology Domain Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/domains/hydrology/README.md"
version: "v11.2.5"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Hydrology Domain Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Domain Index"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.5/sbom.spdx.json"
manifest_ref: "releases/v11.2.5/manifest.zip"
telemetry_ref: "releases/v11.2.5/domains-hydrology-telemetry.json"
telemetry_schema: "schemas/telemetry/domains-hydrology-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-SOVEREIGNTY.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "hydrology"
  applies_to:
    - "etl"
    - "analyses"
    - "stac"
    - "graph"
    - "provenance"
    - "story-nodes"
    - "telemetry"

fair_category: "F1-A1-I1-R1"
care_label: "Hydrology · Public / Mixed Context"
classification: "Public / Restricted-Context"
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Environmental Monitoring / Water Resources"
indigenous_rights_flag: true
redaction_required: true

json_schema_ref: "schemas/json/domains-hydrology-index-v1.schema.json"
shape_schema_ref: "schemas/shacl/domains-hydrology-index-v1-shape.ttl"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "ProperInterval"
  prov_o: "prov:Collection"
  geosparql: "geo:FeatureCollection"

doc_uuid: "urn:kfm:doc:domains:hydrology:index:v11.2.5"
semantic_document_id: "kfm-domains-hydrology-index"
event_source_id: "ledger:docs/domains/hydrology/README.md"
immutability_status: "version-pinned"

machine_extractable: true
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative additions"
  - "fabricated hydrologic events"
  - "unverified regulatory claims"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next hydrology domain reorganization"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology Domain Index**  
`docs/domains/hydrology/README.md`

**Purpose**  
Serve as the **authoritative domain index** for all **hydrology-related data, pipelines, analyses, and Story Nodes** in the Kansas Frontier Matrix (KFM), spanning surface water, groundwater, water quality, drought–flood dynamics, and regulatory submissions (e.g., KDHE §303(d)).

</div>

---

## 📘 Overview

The **Hydrology Domain** covers how water moves through and interacts with Kansas landscapes, infrastructure, and communities. It brings together:

- **Datasets** — streamflow, stage, water quality, precipitation, soil moisture, groundwater.  
- **Pipelines** — deterministic ETL for hydrology (e.g., SDA soils, KDHE §303(d), USGS/NOAA ingest).  
- **Analyses** — drought–flood correlation, temporal modeling, watershed resilience.  
- **Story Nodes** — narrative overlays explaining hydrologic change, impairment, and adaptation.  
- **Regulatory & governance pathways** — KDHE submissions, FAIR+CARE reviews, sovereignty-aware masking.

This index connects domain docs under `docs/domains/hydrology/**` to:

- Hydrology analyses (`docs/analyses/hydrology/**`),  
- Hydrology pipelines (`src/pipelines/hydrology/**`),  
- Hydrology Story Nodes and Focus Mode narratives,  
- STAC/DCAT/PROV catalogs for hydrologic assets.

---

## 🗂️ Directory Layout

```text
📁 docs/
└── 📁 domains/
    └── 📁 hydrology/
        📄 README.md                            # ← This file (hydrology domain index)
        📁 kdhe/
        │   📄 303d-2026-submission.md          # KDHE 2026 §303(d) submission node pattern
        └── 📁 references/
            📄 sources-and-codes.md             # Parameter codes, method refs, KDHE crosswalks (planned)

📁 docs/
└── 📁 analyses/
    └── 📁 hydrology/
        📄 README.md                            # Hydrology analyses overview
        📁 methods/
        │   📄 temporal-analysis.md             # Temporal hydrology methods
        └── 📁 drought-flood-correlation/       # Drought–flood workflows & datasets

📁 docs/
└── 📁 story-nodes/
    └── 📁 domains/
        └── 📁 history/
            📄 README.md                        # History Story Node domain (historical hydrology context appears here)

📁 src/
└── 📁 pipelines/
    └── 📁 hydrology/
        📁 kdhe_2026/                           # KDHE §303(d) 2026 ETL
        │   📄 ingest.py
        │   📄 validate.py
        │   📄 standardize.py
        │   📄 export_kdhe.py
        └── 📁 common/
            📄 hydrology_schema.py              # Canonical hydro schemas (flows, WQ, gauges, etc.)

📁 data/
└── 📁 hydrology/
    📁 kdhe_2026/
        📁 raw/
        📁 validated/
        📁 standardized/
        📁 exports/
    📁 usgs/
        📁 raw/
        📁 processed/
    └── 📁 stac/
        📄 hydrology-collections.json           # STAC collections index for hydrology (illustrative)
```

Concrete subdocs and collections may expand, but the **domain-level layout** must remain consistent for discoverability, graph ingestion, and CI validation.

---

## 🧭 Domain Scope & Subdomains

The hydrology domain focuses on interconnected subdomains:

1. **Water Quality & Impairments**  
   - KDHE §303(d) submissions (e.g., **KDHE 2026 node**),  
   - Nutrients, bacteria, physical–chemical parameters, cyanotoxins, algal metrics,  
   - Station metadata and monitoring program crosswalks.

2. **Surface Water (Streams, Rivers, Lakes)**  
   - USGS NWIS streamflow, stage, derived indices,  
   - Reservoir and lake-level records,  
   - Flood/drought event characterization and frequency analysis.

3. **Groundwater & Aquifers**  
   - Well-level time series,  
   - Aquifer system characterization and trends,  
   - Links to soil and geology domains.

4. **Hydroclimate & Coupled Analyses**  
   - Precipitation, ET, snow (where relevant),  
   - Drought indices (SPI/SPEI) and hydrologic response,  
   - Interactions with land use, energy, and ecology.

5. **Regulatory & Governance Interfaces**  
   - KDHE data submissions,  
   - Federal/state guidance and scenario work,  
   - FAIR+CARE governance and sovereignty-aware decision support.

Each subdomain should anchor to specific:

- STAC Collections,  
- DCAT Datasets,  
- Graph node labels (e.g., `:Waterbody`, `:Measurement`, `:Gauge`, `:Program`),  
- Story Node bundles where narratives are developed.

---

## 🧱 Data & Pipelines (Hydrology Stack Overview)

Hydrology pipelines are expected to implement KFM’s core patterns:

- **Idempotent ETL Node Pattern**  
  - Node-level guarantees:
    - WAL-safe operations,  
    - Deterministic transforms,  
    - Content hashing and idempotent upserts.

- **Event-Driven Deterministic Ingestion Pattern**  
  - Trigger → ingest → normalize → validate → transform → publish → graph → Story Nodes.  
  - Used for event-driven flows (USGS updates, KDHE refresh windows, etc.).

- **Unified Idempotency, Safety & Governance Pattern**  
  - Governance envelope enforcing:
    - Masking and sovereignty rules,  
    - Telemetry (energy, CO₂e, cost),  
    - DLQ/replay and SLSA/SBOM checks.

For each hydrology pipeline, the domain index expects:

- A statement of **which patterns** it implements,  
- Clear **input manifests** under `data/sources/**`,  
- Tiered outputs (`raw → validated → standardized → exports` or equivalent),  
- STAC/PROV wiring documented in the pipeline’s own README.

---

## 🌐 Catalog & Graph Alignment

### STAC / DCAT

Hydrology catalogs must:

- Use **STAC Collections** like (illustrative):

  - `kfm-hydro-surface-water`,  
  - `kfm-hydro-water-quality`,  
  - `kfm-hydro-groundwater`.

- Use **STAC Items** for:
  - Time-bounded exports (e.g., annual/seasonal water-quality snapshots),  
  - KDHE submission bundles (with assets for measurements, metadata, station indices, PROV).

- Derive **DCAT Datasets** and Distributions automatically from STAC via the KFM STAC→DCAT standards.

### Neo4j Graph

Recommended graph mapping:

- Nodes:
  - `:Waterbody` (rivers, lakes, segments),  
  - `:Measurement` (parameter + time + location),  
  - `:Gauge` / `:Station`,  
  - `:HydroDatasetVersion`,  
  - `:Program` (monitoring programs),  
  - Optional `:ImpairmentTag` for regulatory tags.

- Relationships:
  - `(:Waterbody)-[:HAS_MEASUREMENT]->(:Measurement)`  
  - `(:Gauge)-[:LOCATED_ON]->(:Waterbody)`  
  - `(:Measurement)-[:RECORDED_BY]->(:Gauge)`  
  - `(:HydroDatasetVersion)-[:DERIVES_FROM]->(:HydroDatasetVersion)`  
  - `(:HydroDatasetVersion)-[:RECORDED_IN]->(:Program)`  
  - `(:Waterbody)-[:HAS_IMPAIRMENT_CANDIDATE]->(:ImpairmentTag)` (for KDHE-type work).

Catalog and graph designs must be fully detailed in pattern- and pipeline-level docs, with this domain index serving as the coordination hub.

---

## 🧠 Story Nodes & Focus Mode

Hydrology narratives will often appear in:

- **History Story Nodes**  
  - e.g., Dust Bowl hydrology, notable flood events, long-term watershed changes.

- **Hydrology-specific Story Nodes** (planned & in development):  
  - Water-quality and impairment stories,  
  - Drought–flood “whiplash” episodes,  
  - Watershed resilience and adaptation narratives.

Domain obligations for Story Nodes:

- Story Nodes referencing hydrologic data must:
  - Link to specific datasets (`:HydroDatasetVersion` nodes, STAC Items),  
  - Use correct time and space extents,  
  - Respect sovereignty (e.g., when waters intersect Tribal lands or sacred sites).

- Focus Mode should be able to:
  - Display time-series overlays for flow, water quality, and drought indices,  
  - Indicate source datasets and their FAIR+CARE status,  
  - Expose relevant governance notes (e.g., KDHE submission context, masking rules).

This domain index should be updated to reference any **hydrology Story Node domain docs** once they are formalized.

---

## 🧪 Validation, FAIR+CARE & Governance

Hydrology assets are subject to:

- **Validation & QA**:
  - Schema validation (unit consistency, parameter codes),  
  - Domain checks (e.g., no physically impossible values, consistent censoring logic),  
  - Coverage and completeness metrics.

- **FAIR+CARE**:
  - Clear licensing and data source attribution,  
  - Consent and ethical usage constraints recorded in STAC/DCAT/PROV,  
  - Spatial generalization or masking where sensitive locations overlap waterbodies (e.g., cultural sites, Tribal waters).

- **Governance**:
  - Hydrology domain changes (pipelines, schemas, KDHE submissions) must be reviewed by:
    - Hydrology Domain Board,  
    - FAIR+CARE Council,  
    - IDGB where sovereign waters are implicated.

Telemetry (per `telemetry_schema`) should record:

- Energy, CO₂e, cost for major hydrology ETL pipelines,  
- Data volumes and coverage,  
- Validation pass/fail rates.

---

## 🕰️ Version History

| Version  | Date       | Summary                                                                                         |
|----------|------------|-------------------------------------------------------------------------------------------------|
| v11.2.5  | 2025-12-08 | Initial governed hydrology domain index; aligned with KDHE 2026 submission node and v11.2.4 pipeline/pattern standards. |

---

<div align="center">

💧 **Kansas Frontier Matrix — Hydrology Domain**  

[🌐 Domains Index](../README.md) ·  
[📊 Hydrology Analyses](../../analyses/hydrology/README.md) ·  
[💧 KDHE 2026 §303(d) Node](kdhe/303d-2026-submission.md) ·  
[⚖️ Root Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>