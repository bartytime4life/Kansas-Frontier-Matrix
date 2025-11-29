---
title: "🧪 NASA SMAP — Sample Datasets & Example STAC Items (Training · Tutorials · Non-Sensitive Examples)"
path: "docs/data/satellites/smap/samples/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Non-Sensitive · Synthetic/Subset Samples"
status: "Active / Public"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Earth Systems WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"
doc_integrity_checksum: "<sha256>"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A (Public / Low-Risk)"
indigenous_rights_flag: false
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../schemas/json/smap-sample-datasets-v11.json"
shape_schema_ref: "../../../../schemas/shacl/smap-sample-datasets-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:samples-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-samples"
event_source_id: "ledger:docs/data/satellites/smap/samples/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "72 months"
sunset_policy: "Superseded upon SMAP sample refresh cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — Example / Sample Datasets Directory**  
`docs/data/satellites/smap/samples/`

**Purpose**  
Provide **public, low-risk, sovereignty-safe** example datasets, STAC Items, metadata,  
and miniature rasters used for:

- onboarding  
- documentation examples  
- tutorials  
- QA demonstrations  
- Focus Mode v3 behavior explanation  
- STAC/DCAT/PROV-O walk-throughs  
- CI smoke tests  

These samples DO NOT contain any real sovereign-relevant data and DO NOT represent  
full-quality SMAP science products.

</div>

---

## 📘 1. Overview

This directory holds *small*, *governance-safe*, *tutorial-ready* SMAP-like artifacts including:

- 🌍 tiny COG rasters (soil moisture, FT, VWC)  
- 📄 tiny JSON metadata examples (STAC Item + Collection fragments)  
- 📦 mini STAC catalogs for documentation & demos  
- 🧪 synthetic QA masks & uncertainty examples  
- 🌐 tiny GeoJSON footprints for STAC extents  

All samples are either:

- **synthetic**, **heavily degraded**, or **downsampled** versions, OR  
- **public-domain demonstration data** provided by NASA (if used, original license noted)

They are **NOT** used in production ETL but are used for **tutorials, CI smoke tests, docs**,  
and **story-driven demonstrations**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/samples/
├── 📄 README.md                             # This file
│
├── 🌍 rasters/                               # Tiny COGs (synthetic, safe)
│   ├── sm_sample.tif                         # Soil moisture (synthetic)
│   ├── ft_sample.tif                         # Freeze–Thaw sample
│   ├── vwc_sample.tif                        # Vegetation water content sample
│   └── uncertainty_sample.tif                # QA-derived uncertainty demo
│
├── 🗺️ footprints/                            # GeoJSON footprints for STAC examples
│   ├── sm_footprint.geojson
│   ├── ft_footprint.geojson
│   └── vwc_footprint.geojson
│
├── 📦 stac/                                  # Sample STAC Items / mini-Collections
│   ├── collection.json                       # Tutorial-friendly STAC Collection
│   ├── item_sm.json                          # Soil-moisture sample Item
│   ├── item_ft.json                          # FT sample Item
│   └── item_vwc.json                         # VWC sample Item
│
└── 🧪 qa/                                    # Synthetic QA/uncertainty samples
    ├── qa_mask_sample.json
    ├── qa_codes_sample.json
    └── uncertainty_mapping.json
~~~

---

## 🧩 3. Sample Dataset Responsibilities

### 🌍 **Sample Rasters (`rasters/`)**
Used for:

- STAC tutorials  
- MapLibre/Cesium demo layers  
- Focus Mode narrative examples  
- ETL demonstration (docs only)  
- QA layer walkthrough  

All values are **synthetic** and **safe**.

---

### 🗺️ **Footprints (`footprints/`)**
Provide minimal geographic contexts:

- tile bounding boxes  
- coverage extents  
- simple polygon edges  

Used to demonstrate STAC/geo concepts without exposing sensitive geography.

---

### 📦 **STAC Samples (`stac/`)**
Provide:

- Collection metadata structure  
- Item-level field formatting  
- Asset blocks (COG, JSON, QA, thumbnails)  
- Links & relations  
- License & provider examples  

CI ensures examples remain STAC 1.x valid.

---

### 🧪 **QA Samples (`qa/`)**
Provide demonstration-grade masks and example uncertainty mappings:

- Radiometer QA (tiny synthetic bitmaps)  
- RFI QA mini-masks  
- retrieval QA simplifications  
- uncertainty mapping rules  

Used in documentation and small-scale automated tutorial tests.

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

All content in this directory is:

- **explicitly safe for public use**  
- **synthetic, degraded, or public-domain**  
- **guaranteed NOT to include sovereign-sensitive data**  
- **pre-screened for CARE compliance**  
- **unlinked from real-world pixel precision**  

No sovereignty/H3 generalization needed, but metadata markers remain for demonstration.

---

## 🧪 5. Validation & CI Behavior

This folder supports **documentation CI smoke tests**:

- STAC schema validation  
- JSON-LD/PROV-O validation for examples  
- demo raster integrity checks  
- miniature uncertainty calculation examples  
- footprint geometry validation  
- accessibility metadata checks  

Failures here indicate broken **documentation examples**, not pipeline data.

---

## 🔁 6. Relationship to the SMAP ETL Pipeline

This directory is **outside** the real ETL flow and is used only for:

- Tutorials  
- Docs illustrations  
- Example notebooks  
- Sample Story Nodes  
- Focus Mode demonstration views  
- Developer onboarding  

Real ETL data exists under:

```
data/satellites/smap/stac/
data/satellites/smap/qa/
data/satellites/smap/transforms/
```

---

## 🔮 7. Applications Across KFM

- 🌐 Web UI demos  
- 🧭 Focus Mode training examples  
- 📘 Documentation figures & diagrams  
- 🛠 Developer onboarding  
- 🧪 Tiny CI smoke tests  
- 📚 Workshops & educational material  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial SMAP samples directory README; fully safe, FAIR+CARE compliant; STAC-complete; emoji-optimized.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🌐 SMAP STAC](../stac/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

