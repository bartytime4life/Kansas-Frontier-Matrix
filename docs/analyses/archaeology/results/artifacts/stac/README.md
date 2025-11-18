---
title: "🗂️🏺 Kansas Frontier Matrix — Artifact Results: STAC Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/artifacts/stac/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly · Archaeology WG · FAIR+CARE Council · Metadata Governance Unit"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-stac-results-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Registry"
intent: "archaeology-artifacts-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Spatial Metadata"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology WG · FAIR+CARE Council"
risk_category: "Spatial Metadata / Artifact Governance"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/artifacts/stac/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../schemas/json/archaeology-artifact-stac.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/archaeology-artifact-stac-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:artifacts:stac-registry-v11.0.0"
semantic_document_id: "kfm-arch-artifacts-stac"
event_source_id: "ledger:docs/analyses/archaeology/results/artifacts/stac/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "precision-location-inference"
  - "reverse-provenience"
  - "cultural-identity-attribution"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-artifacts-stac-root"
lifecycle_stage: "stable"
ttl_policy: "Review every 6 months"
sunset_policy: "Superseded on next STAC governance update"
---

<div align="center">

# 🗂️🏺 **Artifact Results — STAC Registry**  
`docs/analyses/archaeology/results/artifacts/stac/README.md`

**Purpose:**  
Define the complete **STAC (SpatioTemporal Asset Catalog)** metadata framework for artifact-result datasets—ceramics, lithics, faunal, metals, clustering, environmental correlation layers, and spatial distribution models—within the Kansas Frontier Matrix (KFM).  
Ensures all artifact outputs follow **FAIR+CARE**, **H3 r7+ spatial masking**, **PROV-O lineage**, and **KFM-MDP v11** documentation standards.

</div>

---

## 📘 Overview

Every artifact result dataset produced in KFM must be represented by a **STAC Item**, and grouped appropriately in **STAC Collections**.  
These STAC entries are used across:

- Story Node v3 environmental/material context  
- Focus Mode v3 narrative engines  
- map + timeline integration  
- dataset search / filtering  
- cross-domain modeling pipelines  

STAC metadata enforces:

- **complete machine-readability**  
- **H3 generalized spatial geometry**  
- **ethical + CARE protections**  
- **provenance cross-linking**  
- **uncertainty + environmental metadata inclusion**  

No STAC entry may include site coordinates, inferred provenience, culturally sensitive distributions, or restricted materials.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/results/artifacts/stac/
├── README.md                                       # This file
├── items/                                          # STAC Items for artifact result datasets
│   ├── ceramics/                                   # Ceramic result STAC Items
│   ├── lithics/                                    # Lithic result STAC Items
│   ├── faunal/                                     # Faunal result STAC Items
│   ├── metals/                                     # Metal artifact STAC Items
│   ├── clustering/                                 # Artifact cluster STAC Items
│   └── distributions/                              # Spatial distribution STAC Items
├── collections/                                    # STAC Collections
│   ├── ceramics-collection.json
│   ├── lithics-collection.json
│   ├── faunal-collection.json
│   ├── metals-collection.json
│   ├── clustering-collection.json
│   └── distributions-collection.json
├── templates/                                      # Authoritative templates for new datasets
│   ├── stac-item-template.json
│   └── stac-collection-template.json
├── metadata/                                       # Crosswalk + extensions
│   ├── stac-kfm-extensions.schema.json
│   ├── stac-artifact-extension.schema.json
│   └── dcat-crosswalk.json
└── validation/                                     # Validation outputs
    ├── stac-validation-report.json
    ├── schema-validation.json
    └── integrity-checks.json
~~~

---

## 🧬 Required STAC Fields for Artifact Results

### **1️⃣ Core STAC Requirements**
All STAC Items MUST include:

- `"stac_version": "1.0.0"`  
- `"type": "Feature"`  
- unique `"id"`  
- generalized `"geometry"` (H3 multipolygon only)  
- `"bbox"` derived from H3 geometry  
- temporal coverage using:
  - `"datetime"` **OR**  
  - OWL-Time interval extension  
- `"links"` to provenance, metadata, and related assets  

---

### **2️⃣ KFM Artifact Result Extensions**

Each artifact STAC Item must include:

- `kfm:artifact_type` (ceramic, lithic, faunal, metal, clustering, distribution)  
- `kfm:care_classification`  
- `kfm:uncertainty` (variance, disagreement, etc.)  
- `kfm:environmental_drivers` (if applicable)  
- `kfm:lineage_ref` (PROV-O bundle path)  
- `kfm:domain = "archaeology"`  
- `kfm:generalization` (H3 r7+)  
- `kfm:pd_verification` (public-domain confirmation)  

If clustering or predictive modeling is involved, include:

- `kfm:explainability` (SHAP/LIME metadata paths)  

---

### **3️⃣ Assets**

Artifact STAC Items may contain:

- distribution rasters (COG/GeoTIFF)  
- H3 vector layers (GeoJSON)  
- PCA/cluster reduction artifacts  
- environmental-correlation surfaces  
- uncertainty rasters  
- public-domain typology/petrographic data summaries  
- JSON-LD narrative-ready metadata  

No assets may include raw, sensitive, or provenience-linked artifact data.

---

## 🧭 STAC Collections

Collections group Items by:

- artifact category  
- environmental domain  
- modeling approach  
- temporal extent  
- uncertainty class  
- CARE sensitivity level  

Each collection must include:

- spatial extent  
- temporal extent  
- child item references  
- dataset purpose  
- CARE/FAIR metadata  
- provenance summary  

---

## 🧪 Validation

The CI/CD pipeline validates:

- JSON Schema correctness  
- STAC 1.0.0 compliance  
- KFM extension compliance  
- H3 geometry safety  
- CARE-label alignment  
- PROV-O integration integrity  
- crosswalk alignment (STAC ↔ DCAT ↔ PROV)  

STAC metadata failing any check is rejected until corrected.

---

## 🧠 Focus Mode Integration

STAC metadata drives:

- artifact layer loading  
- uncertainty visualization  
- environmental + material reasoning contexts  
- Story Node v3 material-culture scaffolding  
- narrative-safe dataset descriptions  

Example Focus Summary:

> **Focus Summary:**  
> STAC metadata documents the artifact dataset’s generalized geometry, uncertainty, environmental context, and sovereign governance protections. All metadata complies with FAIR+CARE and cultural safety rules.

---

## 🛡 CARE & Ethical Rules

All artifact STAC metadata must:

- use H3 r7+ spatial generalization  
- avoid providing site-level or cultural-identifying detail  
- include uncertainty & masking statements  
- avoid inferring cultural identity, territory, or restricted knowledge  
- undergo FAIR+CARE Council review  

If STAC metadata introduces cultural risks → dataset must be revised or removed.

---

## 🕰️ Version History

| Version | Date       | Author                               | Summary |
|--------:|------------|--------------------------------------|---------|
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council   | Initial artifact STAC registry under KFM-MDP v11.0.0. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Artifact STAC Registry · CARE-Governed · FAIR+CARE Certified  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Artifact Results](../README.md)

</div>
