---
title: "🗂️🌍 Kansas Frontier Matrix — Paleoenviron. Results: STAC Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/paleoenvironment/stac/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Paleoenvironment WG · Metadata WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-paleoenv-stac-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Registry"
intent: "archaeology-paleoenvironment-stac-results"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Spatial Metadata"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Paleoenvironment WG · Metadata WG · FAIR+CARE Council"
risk_category: "Spatial Metadata & Lineage"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/paleoenvironment/stac/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../../../schemas/json/archaeology-paleoenv-stac.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-paleoenv-stac-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoenvironment:stac-registry-v11.0.0"
semantic_document_id: "kfm-arch-paleoenv-stac-registry"
event_source_id: "ledger:docs/analyses/archaeology/results/paleoenvironment/stac/README.md"
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
  - "precise-environmental-feature inference"
  - "historical or cultural linkage"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal / CARE-Governed"
jurisdiction: "Kansas / United States"
role: "archaeology-paleoenv-stac-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded upon next STAC-governance update"
---

<div align="center">

# 🗂️🌍 **Paleoenvironmental Results — STAC Registry**  
`docs/analyses/archaeology/results/paleoenvironment/stac/README.md`

**Purpose:**  
Provide the authoritative STAC (SpatioTemporal Asset Catalog) registry for all **paleoenvironmental result layers** in the Kansas Frontier Matrix (KFM), including paleoclimate, seasonality, paleo-hydrology, vegetation, soils, drought cycles, and predictive reconstructions.

All STAC Items and Collections must follow **KFM-MDP v11**, **FAIR+CARE**, **H3 r7+ masking**, and **sovereignty-safe lineage**.

</div>

---

## 📘 Overview

This registry defines:

- STAC **Items** representing individual paleoenvironment raster/JSON layers  
- STAC **Collections** for grouping datasets by domain  
- KFM **geospatial generalization** standards  
- dataset-level metadata linking to DCAT + PROV  
- environmental-only, culturally neutral interpretation rules  

Paleoenvironmental STAC entries:

- **MUST** generalize spatial geometry to H3 r7+  
- **MUST NOT** expose raw proxy coordinates  
- **MUST** include uncertainty + driver metadata  
- **MUST NOT** suggest cultural or historical events  
- **MUST** include FAIR+CARE labels  
- **MUST** link to PROV-O lineage bundles  

These metadata structures feed:

- the Web STAC Explorer  
- Focus Mode v3 dataset panels  
- Story Node environmental context  
- model provenance validation pipelines  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/paleoenvironment/stac/
├── README.md                             # This file
├── items/                                # Item-level STAC metadata
│   ├── climate/
│   ├── hydrology/
│   ├── vegetation/
│   ├── soils/
│   ├── seasonality/
│   ├── drought-cycles/
│   └── predictive/
├── collections/                          # STAC Collections (domain-based groupings)
│   ├── climate-collection.json
│   ├── hydrology-collection.json
│   ├── vegetation-collection.json
│   ├── soils-collection.json
│   ├── seasonality-collection.json
│   └── drought-cycles-collection.json
├── templates/                             # STAC Item / Collection templates
│   ├── stac-item-template.json
│   └── stac-collection-template.json
├── metadata/                              # STAC extension schemas + DCAT crosswalks
│   ├── stac-kfm-extensions.schema.json
│   ├── stac-paleoenv-extension.schema.json
│   └── dcat-crosswalk.json
├── qa/                                    # Validation notebooks + schema outputs
│   ├── stac-validation-report.json
│   ├── schema-checks.json
│   └── integrity-validation.json
└── exports/                               # Rendered STAC JSON outputs
~~~

---

## 🧩 Required STAC Components

### **1️⃣ Mandatory Core Fields**
Every paleoenvironmental STAC Item must include:

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- unique `"id"`  
- `"geometry"` → **H3 MultiPolygon ONLY**  
- `"bbox"` derived from generalized geometry  
- `"properties.datetime"` or OWL-Time interval  
- `"assets"` with generalized raster/vector references  

---

### **2️⃣ Required KFM Extensions**
Must include:

- `kfm:domain = "paleoenvironment"`  
- `kfm:environmental_driver`  
- `kfm:uncertainty`  
- `kfm:generalization` (≥ H3 r7)  
- `kfm:care_classification`  
- `kfm:lineage_ref` → PROV-O bundle  
- `kfm:proxy_sources` (PD-only, generalized)  

---

### **3️⃣ Assets Allowed**
Approved asset roles:

- `"data"` → environmental generalized raster (COG)  
- `"geometry"` → MultiPolygon (H3-derived)  
- `"uncertainty"` → uncertainty raster or JSON  
- `"drivers"` → environmental driver rasters (generalized)  

Forbidden:

- raw proxy point clouds  
- raw sediment core coordinates  
- sub-H3 geometry  
- any sensitive spatial information  

---

## 🧪 Validation Rules

STAC metadata must pass:

- JSON Schema  
- KFM STAC extension validation  
- SHACL metadata rules  
- H3 geometry validator  
- socio-cultural sensitivity screens (FAIR+CARE)  
- provenance linkage checks  

Any failure → dataset is **blocked** from results.

---

## 🧠 Focus Mode Integration

Paleoenvironmental STAC metadata powers:

- dataset cards  
- environmental temporal panels  
- uncertainty chips  
- narrative-safe context blocks  
- ecological change timelines  

**Example Focus Summary**  
> STAC metadata provides generalized spatial, temporal, and uncertainty descriptions of paleoenvironmental datasets, ensuring sovereignty-safe integration into Focus Mode.

---

## 🛡 CARE & Ethical Requirements

All STAC records must:

- mask sensitive locations  
- avoid cultural interpretation  
- disclose uncertainty  
- log masking + generalization decisions  
- follow sovereignty & tribal governance guidelines  

If metadata risks harm → **generalize or remove**.

---

## 🕰️ Version History

| Version | Date       | Author                                     | Summary |
|--------:|------------|--------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Paleoenvironment WG · FAIR+CARE Council    | Initial STAC registry for paleoenvironment results. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Paleoenvironmental STAC Registry · FAIR+CARE Certified · Sovereignty-Safe  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified  

[Back to Paleoenvironment Results](../README.md)

</div>
