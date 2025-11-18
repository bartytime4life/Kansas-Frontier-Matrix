---
title: "📓🗂️ Kansas Frontier Matrix — Analysis Notebooks: STAC Metadata Generation (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/notebooks/stac/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Metadata WG · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stac-notebooks-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Notebook Index"
intent: "archaeology-stac-metadata-analysis-notebooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Metadata"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Metadata WG · Archaeology WG · FAIR+CARE Council"
risk_category: "Metadata Governance"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/notebooks/stac/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-stac-notebooks.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-stac-notebooks-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:results:notebooks:stac-v11.0.0"
semantic_document_id: "kfm-arch-stac-notebooks"
event_source_id: "ledger:docs/analyses/archaeology/results/notebooks/stac/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Metadata-Safe"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "coordinate-reconstruction"
  - "sensitive-location-inference"
  - "cultural-boundary-mapping"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-stac-notebooks-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded with next STAC-governance upgrade"
---

<div align="center">

# 📓🗂️ **STAC Metadata Generation — Notebook Index**  
`docs/analyses/archaeology/results/notebooks/stac/README.md`

**Purpose:**  
Provide a centralized index of **STAC metadata generation notebooks** used to create safe, generalized, FAIR+CARE-compliant STAC Items and Collections for archaeological, geophysical, environmental, cultural landscape, and predictive datasets within the Kansas Frontier Matrix (KFM).

</div>

---

## 📘 Overview

STAC notebooks in KFM:

- generate **STAC Items** for all dataset categories  
- create **STAC Collections** for grouped datasets  
- enforce **H3 r7+ geometry generalization**  
- populate asset metadata (COGs, GeoJSON, JSON-LD)  
- validate metadata integrity using JSON Schema + SHACL  
- guarantee sovereignty, masking, and cultural-safety  
- harmonize metadata with DCAT and PROV-O  
- export STAC-ready JSON for ingestion into KFM’s Web/STAC Explorer  
- supply metadata for Story Nodes + Focus Mode  

STAC notebooks **never**:

- include exact coordinates  
- expose sensitive geometries  
- reveal cultural or archaeological features  
- embed unreviewed provenance  
- bypass sovereignty or CARE constraints

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/notebooks/stac/
├── README.md                             # This file
├── items/                                 # Item-level STAC generation notebooks
│   ├── artifacts/
│   ├── geophysics/
│   ├── environmental/
│   ├── cultural-landscapes/
│   ├── predictive/
│   └── templates/
├── collections/                           # Collection-level STAC notebooks
│   ├── artifacts-collections/
│   ├── geophysics-collections/
│   ├── environmental-collections/
│   ├── cultural-landscapes-collections/
│   └── predictive-collections/
├── harmonization/                         # STAC ↔ DCAT ↔ PROV alignment notebooks
├── qa/                                    # STAC validation, masking check, schema QA
└── exports/                               # Rendered JSON STAC Items/Collections
~~~

---

## 🧪 Notebook Categories

### **1️⃣ STAC Item Notebooks (`items/`)**
Produce:

- STAC Item JSON  
- asset definitions (raster, vector, metadata blocks)  
- generalized geometry assets (H3 MultiPolygon)  
- lineage pointers (`kfm:lineage_ref`)  
- uncertainty summaries  
- CARE classification fields  

They ensure consistency across every dataset type.

---

### **2️⃣ STAC Collection Notebooks (`collections/`)**
Generate:

- Collection JSON  
- spatial/temporal extent blocks  
- dataset grouping + catalog hints  
- licensing, keywords, and environmental domains  

Collections are thematic, domain-specific, and sovereignty-safe.

---

### **3️⃣ Harmonization Notebooks (`harmonization/`)**
Build and validate:

- STAC ↔ DCAT crosswalks  
- STAC ↔ PROV-O integration  
- metadata alignment tables  
- cross-schema shared identifiers  

Ensures uniform metadata quality across the KFM.

---

### **4️⃣ STAC QA Notebooks (`qa/`)**
Perform:

- STAC 1.0.0 compliance validation  
- custom KFM STAC extension checks  
- H3 masking tests  
- asset-path validation  
- governance/CARE rule testing  
- JSON Schema + SHACL validation  
- reproducibility checks  

If any STAC entry fails → it is blocked from results.

---

## 🧬 Metadata & Provenance Export

All STAC notebooks must output:

- STAC JSON  
- CARE metadata  
- uncertainty JSON  
- environmental-driver metadata  
- linkage to PROV bundles  
- lineage fields  
- dataset relationships  
- generalization logs  
- reproducibility/seed/config metadata  

Exports are stored under:

- `stac/items/`  
- `stac/collections/`  
- `stac/harmonization/`  
- `stac/qa/`  
- `stac/exports/`

---

## 🧠 Focus Mode Integration

Focus Mode uses STAC notebook exports to:

- load safe dataset metadata  
- create dataset cards  
- provide narrative anchors  
- render uncertainty/provenance chips  
- power temporal slicing and map-layer previews  

Example Focus Summary:

> **Focus Summary:**  
> STAC notebooks generate the generalized, sovereignty-safe metadata structures that enable dataset discovery, visualization, and ethical use in Focus Mode.

---

## 🛡 CARE & Ethical Requirements

STAC metadata notebooks must:

- avoid precise spatial geometries  
- never reveal cultural features  
- include generalization metadata (H3 r7+)  
- document redaction + sovereignty steps  
- embed CARE labels and governance metadata  
- pass FAIR+CARE review before release  

If unsafe metadata is detected → **the STAC record is blocked.**

---

## 🕰️ Version History

| Version | Date       | Author                                  | Summary |
|--------:|------------|-----------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Metadata WG · Archaeology WG · FAIR+CARE Council | Initial STAC notebook index for KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
STAC Metadata Notebooks · FAIR+CARE Certified · Sovereignty-Safe  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Notebooks Index](../README.md)

</div>
