---
title: "🌱 KFM v11 — Soil Systems Pipeline Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/soil/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Soil Systems Working Group · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/soil-pipeline-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/soil/soil-pipeline-suite-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Pipeline Group"
intent: "soil-systems-root"
fair_category: "F1-A2-I1-R1"
care_label: "CARE · Land, Ecology & Indigenous Sensitivity"
classification: "Public (Governed)"
sensitivity: "Low/Moderate (Spatially Masked Where Required)"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
---

<div align="center">

# 🌱 **KFM v11 — Soil Systems Pipeline Suite**  
`docs/pipelines/soil/README.md`

**Purpose**  
Provide the governed **v11 soil-pipeline root**, defining ingest, transformation, drift-aware refresh,  
generalization, masking, storage, lineage, and STAC/DCAT metadata standards for all soil datasets  
(SDA, SSURGO, gNATSGO, hydric soils, derived terrain units, DEM-linked soil attributes).

Soil systems directly support **archaeology**, **hydrology**, **ecology**, **agriculture**, **climate**,  
and **land-change modeling**, requiring **temporal correctness**, **spatial generalization**,  
**ethical sensitivity**, and **FAIR+CARE governance**.

</div>

---

## 📘 1. Overview

KFM v11 unifies all soil pipelines under a consistent **governance + ETL + metadata** framework:

- **Ingest pipelines** for SDA, SSURGO, gNATSGO, hydric soils, statewide derived terrain units  
- **Dynamic change-aware refresh** powered by drift metrics (schema, spatial, statistical, upstream)  
- **H3-based spatial partitioning** for scalable recomputation & masking  
- **Terrain/DEM-linked soil attributes** standardized across resolutions  
- **STAC 1.0 / DCAT 3** metadata for all derived soil layers  
- **OpenLineage** provenance for reproducibility  
- **Energy/Carbon telemetry** for sustainability & governance  
- **CARE-aligned spatial generalization** for sensitive archaeological contexts  

This directory serves as the **root index** for all soil pipelines.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/soil/
├── 📄 README.md                            # This file (soil pipelines root)
│
├── 🧩 change-aware-refresh/                # Drift-aware soil/terrain refresh pipeline (v11)
│   ├── 📄 README.md
│   ├── 📊 signals.yml
│   ├── 🧾 decision-schema.json
│   ├── 🧠 dag/
│   ├── 🌐 stac/
│   └── 🧪 tests/
│
├── 🌱 gNATSGO/                              # gNATSGO ingest, conversions, derived layers
│   ├── 📄 README.md
│   ├── 🔁 transformers/
│   ├── 🧪 validators/
│   ├── 🌐 stac/
│   └── 🧪 tests/
│
├── 🌾 SSURGO/                               # SSURGO ingest + attribute harmonization
│   ├── 📄 README.md
│   ├── 🧩 schema/
│   ├── 🔁 transformers/
│   ├── 🌐 stac/
│   └── 🧪 tests/
│
├── 💧 hydric/                               # Hydric soil layers + wetness indices
│   ├── 📄 README.md
│   ├── 🔁 transforms/
│   └── 🌐 stac/
│
├── 🏔️ terrain/                              # DEM-derived soil-relevant layers (slope, aspect, TPI, wetness)
│   ├── 📄 README.md
│   ├── 📐 geomorphometry.py
│   ├── 🌐 stac/
│   └── 🧪 tests/
│
└── 🔒 generalization/                       # H3 generalization + masking for sensitive sites
    ├── 📄 README.md
    ├── 🧭 h3-rules.yml
    └── 🗝️ masks/
~~~

---

## 🧬 3. Unified Soil Ingest Model (v11)

KFM’s soil pipelines produce **structurally consistent, analysis-ready layers**, each with:

### 📌 Required Schema Components
- Canonical CRS (`EPSG:4326`) + optional DEM-CRS alignment  
- Attribute harmonization (names/types/units)  
- Data dictionary w/ provenance  
- H3 partition IDs for scalable partial refresh  
- Temporal tags for upstream data versions  

### 🌐 Required Metadata (v11)
Every soil dataset publishes:

- **STAC Item**  
- **STAC Collection**  
- **DCAT dataset** (JSON-LD)  
- Full **PROV-O lineage bundle**  
- `kfm:generalization` + CARE flags where masking applied  

### 💾 Required Formats
- **GeoParquet** (primary)  
- Cloud-optimized optional formats:
  - **Zarr**
  - **COG** (when rasterized DEM-derived)  

---

## 🔁 4. Change-Aware Refresh (v11 Core Feature)

The drift-aware refresh system (see module) enables:

- Reduced compute when soil sources are unchanged  
- Automatic partial rebuilds when **localized drift** found  
- Full rebuilds only for **schema/spatial red-drift** events  
- Governance-logged decisions for audit & reproducibility  
- Story Node integration for narrative insight into soil updates  

KFM governs refresh with:

- **Schema drift metrics**  
- **Spatial drift H3 ratios**  
- **Statistical PSI/KL/KS drift measures**  
- **Upstream version jumps**  
- **Signed STAC evidence**  

This significantly reduces energy/carbon cost, keeps soil layers fresh,  
and stabilizes models depending on soil-derived parameters.

---

## 🔐 5. Ethical & Indigenous Data Protections

Soil layers can indirectly expose culturally sensitive landscapes.

KFM applies:

- **H3 generalization**
- **Coordinate fuzzing for sensitive grid cells**
- **Removal/aggregation of high-risk attributes**
- **CARE governance labeling**

All masking & generalization actions are recorded in lineage metadata.

---

## 📦 6. Provenance & Telemetry

### 🔗 Provenance
Every soil pipeline run emits:

- OpenLineage job/run  
- Upstream dataset references  
- lakeFS commit IDs  
- Derived model metadata  
- Drift-decision STAC Items (where applicable)

### 🌱 Telemetry
All soil jobs must log:

- `energy_wh`  
- `carbon_gco2e`  
- `records_processed`  
- `anomaly_counts`  
- Drift-signal metrics (if relevant)

Telemetry is included in sustainability dashboards and governance audits.

---

## 🧭 7. Version History

| Version | Date       | Summary                                                              |
|--------:|------------|----------------------------------------------------------------------|
| v11.2.3 | 2025-11-29 | Updated root index; aligned with v11 drift-aware pipelines; added H3/CARE rules. |
| v11.2.2 | 2025-11-28 | Initial v11 soil pipeline consolidation; added emoji-prefix layout.   |

---

<div align="center">

🌱 **Kansas Frontier Matrix — Soil Systems v11**  
Sustainable Intelligence · FAIR+CARE · Drift-Aware Geospatial Pipelines  

[📘 Docs Root](../../..) · [🧪 Pipelines](../README.md) · [🛡 Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>

