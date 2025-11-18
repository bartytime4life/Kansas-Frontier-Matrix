---
title: "📑📍 Kansas Frontier Matrix — Site Distribution Results: Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Metadata WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-site-distributions-metadata-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata Registry"
intent: "archaeology-site-distributions-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Sensitive Spatial Heritage Metadata"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Spatial Heritage Metadata"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-site-distributions-metadata.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-site-distributions-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:site-distributions:metadata-v11.0.0"
semantic_document_id: "kfm-arch-site-distributions-metadata"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Metadata-Safe"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "coordinate-reconstruction"
  - "inference of precise site geometry"
  - "cultural-boundary deduction"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-site-distributions-metadata-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Updated upon next metadata-governance revision"
---

<div align="center">

# 📑📍 **Site Distribution Results — Metadata Registry**  
`docs/analyses/archaeology/results/site-distributions/metadata/README.md`

**Purpose:**  
Provide the authoritative **metadata registry** for all **generalized site-distribution layers** in the Kansas Frontier Matrix (KFM).  
This registry governs STAC/DCAT metadata, FAIR+CARE compliance, sensitivity flags, spatial generalization levels, and dataset-level documentation rules for all site-distribution products.

</div>

---

## 📘 Overview

Metadata for site-distribution layers ensures:

- **sovereignty-safe masking** (H3 r7+ required)  
- zero precise coordinate disclosure  
- full **FAIR+CARE** cultural-safety alignment  
- complete STAC + DCAT metadata  
- linkages to PROV-O lineage bundles  
- uncertainty & smoothing metadata  
- environmental-only contextualization  
- no culturally sensitive inferences  

Metadata describes **generalized spatial summaries**, *never* archaeological site locations.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/site-distributions/metadata/
├── README.md                          # This file
├── stac/                              # STAC JSON metadata for distributions
├── dcat/                              # DCAT JSON-LD dataset descriptions
├── prov/                              # PROV-O metadata enrichment records
├── harmonization/                     # Crosswalks: STAC ↔ DCAT ↔ PROV
├── sensitivity/                       # CARE sensitivity classifications
├── uncertainty/                       # Uncertainty metadata blocks
├── qa/                                # Metadata validation outputs
└── exports/                           # Published metadata bundles
~~~

---

## 🧩 Metadata Categories

### **1️⃣ STAC Metadata (`stac/`)**
Includes:

- STAC Items for KDE envelopes, H3 grids, clustering outputs  
- generalized geometries (H3 MultiPolygon)  
- uncertainty & smoothing descriptors  
- asset metadata (COGs, JSON)  
- lineage reference fields  

---

### **2️⃣ DCAT Metadata (`dcat/`)**
Describes:

- dataset title & description  
- access rights  
- license & provenance  
- temporal extent (OWL-Time)  
- spatial generalization class  
- distribution formats  

---

### **3️⃣ PROV-O Metadata (`prov/`)**
Adds:

- provenance extensions  
- agent/activity/entity relationships  
- transformation logs  
- masking & redaction reasoning  

---

### **4️⃣ Metadata Harmonization (`harmonization/`)**
Provides:

- STAC ↔ DCAT crosswalk  
- STAC ↔ PROV-O alignment  
- unified field dictionaries  
- metadata normalization rules  

---

### **5️⃣ Sensitivity Metadata (`sensitivity/`)**
Documents:

- CARE category  
- sovereign protection level  
- redaction requirements  
- spatial generalization justification  

---

### **6️⃣ Uncertainty Metadata (`uncertainty/`)**
Includes:

- KDE bandwidth variance  
- smoothing & envelope uncertainty  
- driver disagreement  
- temporal-spread uncertainty  
- Focus Mode “Distribution Confidence Chips” metadata  

---

### **7️⃣ Metadata QA (`qa/`)**
Tracks:

- schema validation (JSON Schema, SHACL)  
- STAC extension compliance  
- DCAT crosswalk integrity  
- sensitive-field scrubbing  
- sovereignty validation  

---

## 🧬 Metadata Export Conventions

All metadata exports must include:

- **STAC JSON**  
- **DCAT JSON-LD**  
- **prov:Bundle** lineage identifiers  
- **generalization metadata**  
- **uncertainty documentation**  
- **CARE labels**  
- **sensitivity flags**  
- **safe environmental context**  

Outputs populate:

- `metadata/stac/`  
- `metadata/dcat/`  
- `metadata/prov/`  
- `metadata/exports/`

---

## 🧠 Focus Mode Integration

Metadata powers:

- dataset cards  
- sovereignty badges  
- uncertainty chips  
- environmental-only context blocks  
- safe Story Node engagement  

**Example Focus Summary:**  
> Site-distribution metadata documents generalized geometry, uncertainty, and CARE controls, ensuring sovereign-safe presentation of archaeological patterns in Focus Mode.

---

## 🛡 CARE & Ethical Requirements

All metadata must:

- prevent any recovery of sensitive site coordinates  
- maintain generalized geometry ≥ H3 r7  
- avoid cultural or interpretive claims  
- fully document uncertainty  
- include CARE labels  
- describe all redaction steps  
- pass FAIR+CARE council review  

If metadata risks exposure → **block release**.

---

## 🕰️ Version History

| Version | Date       | Author                                  | Summary |
|--------:|------------|-----------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council      | Initial metadata registry for site-distribution results. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Site Distribution Metadata Registry · Sovereignty-Protected · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Site Distribution Results](../README.md)

</div>
