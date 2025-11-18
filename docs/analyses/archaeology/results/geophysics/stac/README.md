---
title: "🗂️🧲 Kansas Frontier Matrix — Geophysics Results: STAC Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/geophysics/stac/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Geophysics WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-stac-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Registry"
intent: "archaeology-geophysics-stac-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Spatial Metadata"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Geophysics WG · FAIR+CARE Council"
risk_category: "Spatial Metadata & Sovereignty-Sensitive"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/geophysics/stac/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-geophysics-stac.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-geophysics-stac-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:geophysics:stac-registry-v11.0.0"
semantic_document_id: "kfm-arch-geophysics-stac-registry"
event_source_id: "ledger:docs/analyses/archaeology/results/geophysics/stac/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "feature-location-inference"
  - "reverse-subsurface-reconstruction"
  - "cultural-boundary-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-geophysics-stac-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next STAC schema update"
---

<div align="center">

# 🗂️🧲 **Geophysics Results — STAC Registry**  
`docs/analyses/archaeology/results/geophysics/stac/README.md`

**Purpose:**  
Define and standardize the **STAC (SpatioTemporal Asset Catalog)** metadata for all geophysical datasets—magnetometry, GPR, resistivity, electromagnetic induction (EMI), and multi-sensor composite layers—generated within the Kansas Frontier Matrix (KFM).  
Ensures **safe, H3-generalized geometry**, **FAIR+CARE alignment**, and **PROV-O integrated lineage**.

</div>

---

## 📘 Overview

All geophysical result datasets must be represented as:

- **STAC Items** (individual geophysical layers)  
- **STAC Collections** (method-level grouping)  

STAC metadata provides:

- machine-readable structure  
- sovereignty-safe generalized geometry  
- clean integration with DCAT and PROV-O  
- dataset discoverability across KFM platforms  
- safe, narrative-ready information for Focus Mode v3  

STAC entries **must never** include:

- precise coordinates  
- raw grids or point clouds  
- sensitive anomaly geometry  
- feature-level shapes  
- interpretable cultural or subsurface information  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/geophysics/stac/
├── README.md                                   # This file
├── items/                                      # STAC Items for each modality
│   ├── magnetometry/
│   ├── gpr/
│   ├── resistivity/
│   ├── electromagnetic/
│   └── composite/
├── collections/                                # STAC Collections (method groups)
│   ├── magnetometry-collection.json
│   ├── gpr-collection.json
│   ├── resistivity-collection.json
│   ├── electromagnetic-collection.json
│   └── composite-collection.json
├── templates/                                   # Authoritative templates
│   ├── stac-item-template.json
│   └── stac-collection-template.json
├── metadata/                                   # Crosswalks & extensions
│   ├── stac-kfm-extensions.schema.json
│   ├── stac-geophysics-extension.schema.json
│   └── dcat-crosswalk.json
└── validation/                                 # Validation outputs from CI
    ├── stac-validation-report.json
    ├── schema-validation.json
    └── integrity-checks.json
~~~

---

## 🧬 Required STAC Fields (Geophysics)

### **1️⃣ Core STAC fields**
Every Item must include:

- `"stac_version": "1.0.0"`  
- `"type": "Feature"`  
- unique `"id"`  
- `"geometry"` (H3 MULTIPOLYGON ONLY)  
- `"bbox"` derived from H3 geometry  
- `"datetime"` or OWL-Time interval  

### **2️⃣ KFM Geophysics Extensions**
All Items require:

- `kfm:method` (magnetometry, gpr, resistivity, emi, composite)  
- `kfm:uncertainty` (variance, sensor disagreement, drift)  
- `kfm:care_classification`  
- `kfm:environmental_drivers`  
- `kfm:lineage_ref` → PROV-O bundle  
- `kfm:generalization` (must be ≥ H3 r7)  
- `kfm:domain = "archaeology/geophysics"`  

### **3️⃣ Assets**
Permitted:

- highly generalized rasters (COG)  
- H3 geometries (GeoJSON)  
- uncertainty layers  
- environmental-driver surfaces  

Forbidden:

- raw anomaly grids  
- slice-level shape profiles  
- interpretable subsurface data  

---

## 🧭 Collections

Collections must:

- group Items by modality  
- define spatial + temporal extent (generalized)  
- list Items safely  
- include CARE/FAIR metadata  
- contain a provenance summary  

---

## 🧪 Validation

All STAC metadata must pass:

- JSON Schema validation  
- STAC 1.0.0 rules  
- KFM STAC extension validation  
- H3 geometry checks  
- PROV linkage integrity  
- CARE classification consistency  
- crosswalk validation (STAC ↔ DCAT ↔ PROV)  

Any failure → dataset blocked from ingestion.

---

## 🧠 Focus Mode Integration

Geophysics STAC metadata powers:

- safe map-layer registry  
- environmental reasoning chips  
- uncertainty overlays  
- multi-sensor context panels  
- Story Node v3 environmental blocks  

### Example Focus Summary

> **Focus Summary:**  
> STAC metadata describes this geophysical layer’s generalized geometry, environmental drivers, uncertainty, and lineage, ensuring safe integration with narrative and map systems under FAIR+CARE oversight.

---

## 🛡 CARE & Ethical Safeguards

All geophysical STAC records must:

- generalize spatial data to H3 r7+  
- avoid precise anomaly geometry  
- include uncertainty explanations  
- avoid cultural or subsurface inference  
- record masking and redaction steps  
- undergo FAIR+CARE Council review  

If metadata risks enabling sensitive inference →  
**It must be corrected, masked, or removed.**

---

## 🕰️ Version History

| Version | Date       | Author                                    | Summary |
|--------:|------------|-------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Geophysics WG · Archaeology WG · FAIR+CARE Council | Initial geophysics STAC registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Geophysics STAC Registry · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Geophysics Results](../README.md)

</div>
