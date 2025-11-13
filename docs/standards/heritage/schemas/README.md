---
title: "📐 Kansas Frontier Matrix — Heritage Standards Schemas Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/heritage/schemas/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/standards-heritage-schemas-v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Heritage Standards Schemas Index**  
`docs/standards/heritage/schemas/README.md`

**Purpose:**  
Serve as the **authoritative index** for all JSON Schemas governing heritage, archaeological, cultural, and sensitive-location standards within the Kansas Frontier Matrix (KFM).  
These schemas define the structural, ethical, privacy, and lineage rules required to meet FAIR+CARE, NHPA §304, and KFM Diamond⁹ Ω protection standards.

<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Heritage Standards" src="https://img.shields.io/badge/Heritage_Standards-Schemas-blue" />
<img alt="Protected Data" src="https://img.shields.io/badge/Protection_Level-III-red" />

</div>


---

## 📚 Overview

This directory contains all **schema definitions** regulating how heritage-related data is:

- ingested  
- transformed  
- generalized  
- validated  
- published (STAC/DCAT)  
- visualized (MapLibre / Cesium 3D)  
- protected under FAIR+CARE and NHPA confidentiality  

Schemas here enforce:

- Required metadata fields  
- Cultural sensitivity governance  
- Spatial confidentiality (H3 generalization)  
- Provenance and lineage requirements  
- KFM-specific extensions for protected contexts  
- Accessibility, ethical, and semantic compliance  

All downstream pipelines, Story Nodes, STAC Items, and public datasets depend on these schemas for correctness and legal compliance.

---

### 🗂️ Directory Layout

    schemas/
    |-- README.md                                    # This index document
    |-- h3-generalization-standard.json              # Schema for spatial generalization rules
    |-- heritage-sensitive-location.schema.json      # Schema for sensitive site metadata
    |-- heritage-dataset.schema.json                 # Schema for STAC/DCAT-integrated heritage datasets
    |-- heritage-protection-flags.schema.json        # Schema defining CARE/confidentiality fields
    |-- lineage-provenance.schema.json               # Schema for required lineage metadata
    |
    └── examples/                                    # Example JSON files validating against schemas

---

## 🧱 Schema Descriptions

### 🪧 `h3-generalization-standard.json`

Defines:

- Allowed H3 resolutions  
- Required confidentiality fields  
- Dropping of raw coordinates  
- Minimum aggregation thresholds  
- Legally required NHPA §304 compliance flags  

### 🏺 `heritage-sensitive-location.schema.json`

Defines metadata rules for:

- Cultural-site classification  
- Indigenous/tribal sovereignty fields  
- CARE labels (public / restricted / sacred)  
- Sensitivity scoring  
- Prohibited coordinate exports (lat/lon forbidden)

### 📦 `heritage-dataset.schema.json`

Controls:

- STAC Item / Collection compatibility  
- Required dataset-level metadata  
- FAIR+CARE provenance  
- H3 generalization requirements  
- Dataset identity + temporal validity  

### 🔐 `heritage-protection-flags.schema.json`

Defines:

- Tiered protection levels (I–III)  
- Sensitivity flags  
- Restrictions for display, export, indexing  
- Symbol-level protection metadata  

### 🧬 `lineage-provenance.schema.json`

Governs:

- Required lineage fields  
- Who/when/what change logs  
- Diff manifests  
- Reproducibility constraints  
- Crosswalk definitions for versioned resources  

---

## 🧪 Validation Rules

All heritage data must:

- Validate against these schemas before entering PGV or Neo4j  
- Pass FAIR+CARE ethical checks  
- Include `mcp_protected=true` where required  
- Strip raw coordinates when schema flags mandate  
- Attach H3 generalization metadata for all sensitive features  
- Include dataset lineage fields for reproducibility  

Local validator:

    make validate-heritage-schemas

---

## 🕒 Version History

| Version  | Date       | Author        | Notes                                                                       |
|----------|------------|---------------|-----------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial heritage schemas index — fully memory-rule compliant.               |
