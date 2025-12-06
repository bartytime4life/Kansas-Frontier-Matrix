---
title: "📘 Kansas Frontier Matrix — Analyses Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/README.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"

doc_uuid: "urn:kfm:doc:analyses-overview:v11.2.4"
semantic_document_id: "kfm-doc-analyses-overview"
event_source_id: "ledger:kfm:doc:analyses-overview:v11.2.4"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/analyses-overview-v4.json"
signature_ref: "../../releases/v11.2.4/signature.sig"
attestation_ref: "../../releases/v11.2.4/slsa-attestation.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "analyses-index"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/analyses/README.md@v11.0.0"
  - "docs/analyses/README.md@v10.2.2"
  - "docs/analyses/README.md@v10.2.0"
  - "docs/analyses/README.md@v10.1.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../schemas/json/kfm-analyses-overview-v11.2.4.schema.json"
shape_schema_ref: "../../schemas/shacl/kfm-analyses-overview-v11.2.4-shape.ttl"
story_node_refs: []

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "analyses"
  applies_to:
    - "docs/analyses/**"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 📘 **Kansas Frontier Matrix — Analyses Overview (v11.2.4)**  
`docs/analyses/README.md`

**Purpose**  
Provide the **canonical entry point** for all analytical domains within the **Kansas Frontier Matrix (KFM)** — the environmental, historical, geospatial, ecological, and cross-domain research system built under **Diamond⁹ Ω / Crown∞Ω** governance.

All analytical workflows follow:

- **FAIR+CARE governance**  
- **ISO 19115 / ISO 50001 / ISO 14064 sustainability**  
- **MCP-DL v6.3 reproducibility standards**  
- **KFM-MDP v11.2.4 formatting & metadata**  
- **KFM-OP v11 ontology alignment**

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-gold" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen" />

</div>

---

## 📘 Overview

The **Analyses Layer** is where KFM transforms **data** into **insight**.

KFM analyses integrate:

- Hydrology & watershed analysis  
- Climatology & anomaly modeling  
- Geology & geophysics  
- Ecology & biodiversity intelligence  
- Historical–environmental correlation  
- Cross-domain synthesis and multimodal reasoning  

Every analysis is:

- **Versioned** (manifest + semantic IDs)  
- **Checksum-verified** (SBOM + manifest)  
- **Sustainability-audited** (energy, carbon, runtime)  
- **Linked to STAC/DCAT datasets** (inputs & outputs)  
- **Governed under FAIR+CARE** (ethics, sovereignty, community impact)

Telemetry from each workflow (energy, carbon, runtime, ethics status) is published into:  

`../../releases/v11.2.4/focus-telemetry.json`.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/                       # 📘 Root of all analytical domains
│
├── 📄 README.md                        # 📘 This overview file (Analyses index)
│
├── 📁 hydrology/                       # 🌊 Hydrology & streamflow analytics
│   ├── 📄 README.md                    # Domain overview (methods, scope, governance)
│   ├── 📁 datasets/                    # STAC/DCAT-indexed hydrology datasets
│   ├── 📁 methods/                     # Drought/flood models, ETL, harmonization
│   ├── 📁 results/                     # Derived metrics, plots, maps, tables
│   └── 📁 metadata/                    # Lineage + FAIR+CARE registry (JSON/CSV)
│
├── 📁 climatology/                     # 🌦 Climate trends & future projections
│   ├── 📄 README.md                    # Climate domain overview
│   ├── 📁 datasets/                    # Climate rasters (NetCDF/COG, gridded series)
│   ├── 📁 methods/                     # Anomaly models, heat index, teleconnections
│   ├── 📁 results/                     # Maps, trend plots, scenario tables
│   └── 📄 validation.md                # Schema + ethics validation notes
│
├── 📁 geology/                         # 🪨 Geology, soils, geomorphology
│   ├── 📄 README.md
│   ├── 📁 datasets/                    # Geology, soils, subsurface models
│   ├── 📁 methods/                     # Geostatistics, terrain models
│   ├── 📁 results/                     # Outputs, cross-sections, derived layers
│   └── 📁 metadata/                    # Provenance & contracts
│
├── 📁 ecology/                         # 🌱 Biodiversity & ecological modeling
│   ├── 📄 README.md
│   ├── 📁 datasets/                    # Species, habitat, vegetation layers
│   ├── 📁 methods/                     # SDMs, connectivity, resilience metrics
│   ├── 📁 results/                     # Model outputs, maps, dashboards
│   └── 📁 metadata/                    # FAIR+CARE flags, licenses
│
├── 📁 historical/                      # 🏛 Historical + archival environmental linkage
│   ├── 📄 README.md
│   ├── 📁 datasets/                    # GLO plats, aerials, archives, KHS collections
│   ├── 📁 methods/                     # OCR, NER, georeferencing, temporal alignment
│   ├── 📁 results/                     # Mapped features, narratives, timelines
│   └── 📄 governance.md                # Ethics, sovereignty & archival CARE notes
│
├── 📁 cross-domain/                    # 🔗 Integrated multi-domain analytics
│   ├── 📄 README.md                    # Cross-domain integration overview
│   ├── 📁 datasets/                    # Joined, harmonized, or composite datasets
│   ├── 📁 methods/                     # Fusion models, joint inference, MDM workflows
│   ├── 📁 results/                     # Synthesized indicators, risk scores
│   └── 📁 metadata/                    # Cross-domain provenance & contracts
│
└── 📁 metadata/                        # 🗄️ Global analyses-level metadata & audits
    ├── 📄 README.md                    # Analyses metadata overview
    └── 📁 audit-reports/               # FAIR+CARE + sustainability audit registry
~~~

Author rules:

- New analytical domains **must** mirror this layout (README, datasets, methods, results, metadata).  
- Each `README.md` must follow **KFM-MDP v11.2.4** (front-matter + approved H2 headings).  
- All `metadata/` and `audit-reports/` content must be catalog-ready (STAC/DCAT/PROV-aligned).

---

## 🧭 Context

The Analyses Layer sits **downstream** of:

- Source & ETL pipelines (`data/sources/`, `src/pipelines/**`).  
- STAC/DCAT catalogs (`data/stac/**`, `docs/data/**`).  

…and **upstream** of:

- Story Nodes & Focus Mode narratives.  
- KFM dashboards (web, Cesium, MapLibre visualizations).  
- Governance ledgers and sustainability reporting.

Analyses therefore:

- Consume **governed datasets** with data contracts.  
- Produce **derived datasets** and **interpretations** with full provenance.  
- Feed **AI/ML models** (training/evaluation) and narrative overlays.

---

## 🗺️ Diagrams

### Analytical Governance Workflow (v11)

~~~mermaid
flowchart TD
  A["Raw Multidomain Data<br/>(Hydrology · Climate · Ecology · History)"]
    --> B["ETL Harmonization<br/>STAC/DCAT Registration"]
  B --> C["Domain Analysis Pipelines<br/>(analyses/*/methods/)"]
  C --> D["Results & Visualizations<br/>(analyses/*/results/)"]
  D --> E["Validation & FAIR+CARE Audit<br/>ISO 19115 · ISO 50001"]
  E --> F["Telemetry Export<br/>(Runtime · Energy · CO₂e · Ethics)"]
  F --> G["Governance Ledger Update<br/>Diamond⁹ Ω / Crown∞Ω"]
~~~

This diagram represents the **canonical lifecycle** of an analysis run:

1. Multidomain data pulled from governed catalogs.  
2. Domain-specific methods applied.  
3. Results written to `results/` with metadata.  
4. Validation/audit workflows run (CI/CD).  
5. Telemetry appended to `focus-telemetry.json`.  
6. Governance ledger updated for the analyses family.

---

## 🧪 Validation & CI/CD

Analyses participate in KFM CI/CD via:

- `docs-lint.yml` — Ensures all `docs/analyses/**` Markdown follows KFM-MDP v11.2.4.  
- `faircare-validate.yml` — Validates FAIR+CARE labels, sovereignty flags, and ethics notes.  
- `stac-validate.yml` — Validates STAC/DCAT Items associated with analyses inputs/outputs.  
- `telemetry-export.yml` — Aggregates per-run metrics into `focus-telemetry.json`.  

### Sustainability & Telemetry Targets (ISO 50001 / 14064)

| Metric                | Target (v11) | Unit  | Source                     |
|-----------------------|-------------:|------:|----------------------------|
| Energy per workflow   | ≤ 12         | Wh    | `energy_schema`            |
| Carbon footprint      | ≤ 0.005      | gCO₂e | `carbon_schema`            |
| Telemetry completeness| ≥ 98         | %     | `telemetry_schema`         |
| FAIR+CARE audit pass  | 100          | %     | Governance & FAIR+CARE CI |

All telemetry exports to:  
`../../releases/v11.2.4/focus-telemetry.json`.

---

## 📦 Data & Metadata

### Primary Analytical Data Sources (v11 Standardized)

| Source                        | Description                               | Format          | FAIR+CARE Status |
|-------------------------------|-------------------------------------------|-----------------|------------------|
| **NOAA / NCEI**              | Climate normals, precipitation, drought   | NetCDF          | Certified        |
| **Daymet / PRISM**           | Gridded daily climate                     | TIFF / NetCDF   | Certified        |
| **USGS NWIS**                | Streamflow & hydrology                    | CSV / JSON      | Certified        |
| **NASA EarthData**           | RS imagery & anomaly layers               | COG / NetCDF    | Certified        |
| **NRCS SSURGO**              | Soil & infiltration maps                  | GeoPackage      | Certified        |
| **GBIF / KU Biodiversity**   | Species occurrence                        | CSV / JSON-LD   | Certified        |
| **Kansas Historical Society**| Scanned archival material                 | TIFF / JSON-LD  | Certified        |

Each dataset is:

- Registered as **STAC Items** in `data/stac/**`.  
- Mirrored as **DCAT Datasets** in documentation catalogs.  
- Linked to analyses via dataset IDs, contracts, and provenance chains.

### Example v11 Governance Ledger Entry

~~~json
{
  "ledger_id": "kfm-analyses-ledger-v11.2.4",
  "domains": [
    "Hydrology",
    "Climatology",
    "Ecology",
    "Geology",
    "Historical",
    "Cross-Domain"
  ],
  "energy_wh": 58.4,
  "carbon_gco2e": 0.021,
  "faircare_compliance": "certified",
  "validation_status": "passed",
  "record_created": "2025-12-06T13:00:00Z",
  "governance_ref": "docs/reports/audit/analyses-governance-ledger.json"
}
~~~

This JSON is **KFM-MDP-safe** (no nested fences) and suitable for:

- Telemetry dashboards.  
- Governance audits.  
- PROV-O / DCAT exports.

---

## 🌐 STAC, DCAT & PROV Alignment

Analyses are modeled as:

- **STAC**  
  - Derived layers (rasters, vectors) registered as Items in thematic Collections (e.g., `kfm-hydrology-analyses`).  
  - `properties.kfm:analysis_id` links outputs back to their analysis run and methods.  

- **DCAT**  
  - Analyses datasets described as `dcat:Dataset` with distributions for raw results, summaries, and visual assets.  
  - `dct:source` references input datasets; `dct:provenance` points to analysis docs.  

- **PROV-O**  
  - Each analysis run = `prov:Activity`.  
  - Inputs (datasets) = `prov:Entity` with `prov:used` relationships.  
  - Outputs (derived data, reports) = `prov:Entity` with `prov:wasGeneratedBy`.  
  - This overview doc = `prov:Plan` guiding activities in `docs/analyses/**`.

---

## ⚖ FAIR+CARE & Governance

### FAIR+CARE Integration (v11)

| Pillar                 | Enforcement                                          | Source                       |
|------------------------|------------------------------------------------------|------------------------------|
| **F1 Findable**        | STAC/DCAT metadata; UUID-linked lineage             | `analyses/*/metadata/`       |
| **A1 Accessible**      | Public FAIR+CARE review; clear licensing            | Governance Ledger            |
| **I1 Interoperable**   | EPSG:4326, NetCDF/COG/GeoJSON standards             | Telemetry & schemas          |
| **R1 Reusable**        | Manifest versioning; SPDX licensing                 | `manifest_ref`               |
| **Collective Benefit** | Analyses designed to support community & research   | FAIR+CARE Council review     |
| **Authority to Control** | Sovereignty checks for cultural/historical data  | `sovereignty_policy`         |
| **Responsibility**     | Energy/carbon metrics logged per run                | `telemetry_ref`              |
| **Ethics**             | AI-assisted outputs undergo bias/context audits     | `ethics_ref` + audit reports |

Sensitive or Indigenous-related analyses:

- Must record explicit `care_tag` and sovereignty flags in `metadata/`.  
- May require restricted publication or generalized spatial extents.  

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                                                     |
|----------:|------------|-------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Upgraded to KFM-MDP v11.2.4; added full v11 metadata, STAC/DCAT/PROV alignment, sustainability targets, and emoji-rich directory layout for analyses. |
| v11.0.0  | 2025-11-24 | Initial v11 analyses overview; introduced telemetry schema v4 and expanded FAIR+CARE matrix.               |
| v10.2.2  | 2025-11-10 | Added cross-domain integration section and ISO metrics alignment.                                           |
| v10.2.0  | 2025-11-09 | Linked metadata registry to FAIR+CARE pipelines for analyses.                                              |
| v10.1.0  | 2025-11-08 | Established initial analyses index across hydrology, climatology, ecology, geology, and history.          |

---

<div align="center">

📘 **Kansas Frontier Matrix — Analyses Overview (v11.2.4)**  
Scientific Insight · FAIR+CARE Ethics · Sustainable Intelligence  

[⬅ Back to Documentation Index](../README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·  
[📡 Telemetry Overview](../telemetry/README.md)

</div>
