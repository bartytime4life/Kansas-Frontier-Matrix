---
title: "🗂️📍 Kansas Frontier Matrix — Site Distribution Results: STAC Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/stac/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · Metadata WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-site-distributions-stac-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Registry"
intent: "archaeology-site-distributions-stac-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Spatial Metadata"
sensitivity_level: "High"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Sensitive Spatial Metadata"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/stac/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../schemas/json/archaeology-site-distributions-stac.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-site-distributions-stac-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:site-distributions:stac-registry-v11.0.0"
semantic_document_id: "kfm-arch-site-distributions-stac-registry"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/stac/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Metadata-Only"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "coordinate-reconstruction"
  - "locational inference"
  - "cultural-boundary inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / Highly Sensitive / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-site-distributions-stac-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next STAC governance update"
---

<div align="center">

# 🗂️📍 **Site Distribution Results — STAC Registry**  
`docs/analyses/archaeology/results/site-distributions/stac/README.md`

**Purpose:**  
Define the sovereign-safe **STAC (SpatioTemporal Asset Catalog)** records for all **generalized site-distribution datasets** in the Kansas Frontier Matrix (KFM).  
This registry ensures that spatially sensitive heritage data is **never exposed**, always **H3-generalized**, and fully **FAIR+CARE compliant**.

</div>

---

## 📘 Overview

Site-distribution STAC records:

- provide machine-readable metadata for **generalized spatial layers**  
- document **H3 r7+ masking** used to protect cultural heritage  
- include **temporal extent** using OWL-Time  
- store **dataset lineage links** (PROV-O bundles)  
- include **uncertainty indicators** (variance, KDE spread, smoothing confidence)  
- support dataset rendering in the **KFM Web STAC Explorer**  
- enable safe use in **Focus Mode v3** and **Story Node** narratives  

They **never** include:

- site coordinates  
- feature polygons  
- unmasked point data  
- cultural identities  
- restricted spatial knowledge  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/site-distributions/stac/
├── README.md                           # This file
├── items/                              # STAC Items by site-distribution subtype
│   ├── clusters/
│   ├── h3-envelopes/
│   ├── kde-smoothed/
│   ├── environmental-links/
│   └── temporal/
├── collections/                        # STAC Collections
│   ├── site-distributions-collection.json
│   └── clusters-collection.json
├── templates/                          # Authoritative STAC templates (Item + Collection)
│   ├── stac-item-template.json
│   └── stac-collection-template.json
├── metadata/                           # STAC extensions + crosswalks
│   ├── stac-kfm-extensions.schema.json
│   ├── stac-site-distributions-extension.schema.json
│   └── dcat-crosswalk.json
├── qa/                                 # STAC validation outputs
│   ├── stac-validation-report.json
│   ├── schema-validation.json
│   └── masking-integrity.json
└── exports/                            # Rendered STAC Items & Collections
~~~

---

## 🧩 Required STAC Components

### **1️⃣ Core STAC Fields**
All STAC Items must include:

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `"geometry"` = **H3 MultiPolygon (generalized)**  
- `"bbox"` = H3-derived  
- `"properties.datetime"` or OWL-Time interval  
- `"assets.data"` (generalized raster/vector)  

---

### **2️⃣ KFM STAC Extensions**
Required fields:

- `kfm:domain = "archaeology/site-distributions"`  
- `kfm:generalization` (H3 r7+ required)  
- `kfm:care_classification`  
- `kfm:uncertainty`  
- `kfm:environmental_drivers`  
- `kfm:lineage_ref` → PROV-O  
- `kfm:masking_justification`  

---

### **3️⃣ Assets Allowed**
Permitted:

- H3 multi-polygons  
- KDE envelope rasters  
- environmental generalized grids  
- uncertainty layers  
- metadata JSON-LD  

Prohibited:

- point coordinates  
- site polygons  
- sensitive-derived shapes  

---

## 🧪 Validation Rules

STAC metadata must:

- pass JSON Schema  
- satisfy KFM STAC extension schema  
- be CARE-compliant  
- use ≥ H3 r7  
- link correctly to provenance  
- validate all asset references  

Failure → dataset **cannot** be published.

---

## 🧠 Focus Mode Integration

STAC records feed:

- dataset info cards  
- uncertainty chips  
- sovereignty badges  
- environmental-only narrative blocks  
- safe integration into time sliders & maps  

**Example Focus Summary:**  
> Site-distribution STAC metadata describes generalized geometry, uncertainty, and lineage while guaranteeing that no sensitive coordinates or cultural inferences are exposed.

---

## 🛡 CARE & Ethical Safeguards

All site-distribution STAC records must:

- apply sovereignty-based masking  
- avoid cultural inference  
- document uncertainty  
- disclose generalization method  
- pass FAIR+CARE review  
- include justification if masking is increased  

If any STAC entry risks cultural exposure → **remove or generalize further**.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council       | Initial site-distribution STAC registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Site Distribution STAC Registry · FAIR+CARE Certified · Sovereignty-Protected  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Site Distribution Results](../README.md)

</div>
