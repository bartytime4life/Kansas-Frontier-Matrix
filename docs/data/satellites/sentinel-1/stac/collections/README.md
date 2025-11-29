---
title: "🗂️ ESA Sentinel-1 — STAC Collections (GRD · GRDH · RTC · Coherence · Deformation · Flood · Wetlands)"
path: "docs/data/satellites/sentinel-1/stac/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Earth Observation (CC-BY 4.0)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"

review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../schemas/json/sentinel1-stac-collections-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-stac-collections-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-collections-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-collections"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/collections/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded on next ESA major reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🗂️ **Sentinel-1 STAC Collections**  
`docs/data/satellites/sentinel-1/stac/collections/`

**Collections for all Sentinel-1 SAR product families**  
GRD · GRDH · RTC · Coherence · Deformation · Flood · Wetlands

</div>

---

## 📘 1. Overview

This directory defines **STAC Collections** representing the governed Sentinel-1 SAR  
product families integrated into KFM v11.  
Each Collection provides:

- Collection metadata (STAC 1.x + JSON-LD)  
- Spatial & temporal extents  
- SAR-specific fields (`sar:*`, `s1:*`)  
- Provenance anchors (PROV-O)  
- CARE/H3 sovereignty metadata  
- Links to scene-level STAC Items  
- CI validation guarantees  
- compatibility with DCAT 3.0  

Collections in this directory form the **root catalog** for all Sentinel-1 STAC Items.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/sentinel-1/stac/collections/
├── 📄 README.md                             # This file
│
├── 🗂️ collection_grd.json                   # Sentinel-1 GRD (VV/VH backscatter)
├── 🗂️ collection_grdh.json                  # GRDH high-res scenes
├── 🗂️ collection_rtc.json                   # Radiometrically Terrain Corrected RTC
├── 🗂️ collection_coherence.json             # Temporal coherence Collection
├── 🗂️ collection_deformation.json           # Sovereignty-generalized InSAR (LOS)
├── 🗂️ collection_flood.json                 # Flood mapping Collection
└── 🗂️ collection_wetlands.json              # Wetlands / inundation Collection
~~~

---

## 🧩 3. Collection Responsibilities

### 🛰️ `collection_grd.json`
Represents:

- GRD backscatter (VV/VH)  
- σ⁰ backscatter  
- Scenes for hydrology, land cover, and flood pre/post analysis  

### 🛰️ `collection_grdh.json`
High-resolution GRDH scenes:

- increased pixel detail  
- used for fine-scale surface dynamics  
- sovereignty-generalized where appropriate  

### 🛰️ `collection_rtc.json`
RTC sigma0/gamma0:

- DEM-corrected radiometry  
- stable for time-series analytics  
- aligned with hydrology and land-cover analyses  

### 🔗 `collection_coherence.json`
Coherence time-series:

- flood-related coherence loss  
- damage mapping  
- agricultural change detection  

### 🌍 `collection_deformation.json`
InSAR deformation:

- LOS displacement  
- subsidence, uplift  
- **sovereignty-generalized LOS displacement**  
- `"kfm:mask_required"` when intersecting tribal H3 cells  

### 🌊 `collection_flood.json`
Floodwater detection:

- VH/VV thresholding  
- Otsu & hybrid classification  
- hydrology Story Node integrations  

### 🌿 `collection_wetlands.json`
Wetland & inundation mapping:

- SAR-based wetland signatures  
- multi-temporal floodplain analysis  
- hydrology/ecology pipelines  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

The Sentinel-1 STAC Collections are **governed** according to:

- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` (especially for deformation & flood)  
- `"kfm:care_label"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- geometric generalization in sovereign areas  
- PROV-O lineage for all ingestion pipelines  

Governance validated through:

- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `faircare_validate.yml`

---

## 🧪 5. Validation & CI Guarantees

CI enforces:

- STAC schema correctness  
- valid bounding boxes & geometry  
- correct link structure (self/root/parent)  
- sovereign-safe geometry generalization  
- required `"kfm:*"` governance fields  
- DCAT metadata compatibility  
- PROV-O lineage integrity  

Blocking errors prevent release of the Collection.

---

## 🔁 6. Relation to STAC Items

Each Collection has a corresponding folder under:

```
docs/data/satellites/sentinel-1/stac/items/<product-family>/
```

Items inherit:

- collection-level metadata  
- STAC extensions  
- SAR-specific properties  
- governance metadata  
- provenance structure  

---

## 🔮 7. Applications Across KFM

- SAR ingestion & harmonization  
- hydrology (flood, wetlands, soil proxies)  
- ecology/landscape change  
- disaster monitoring  
- cultural-landscape context (sovereignty-generalized)  
- Story Node v3 & Focus Mode v3 environmental narratives  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 STAC Collections README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; emoji-rich.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📁 STAC Items](../items/README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

