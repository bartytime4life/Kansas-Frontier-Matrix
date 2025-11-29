---
title: "🌿 NASA SMAP — Vegetation Water Content (VWC) STAC Items for 2025 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/vegetation-water/2025/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-vwc-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B (depending on intersection with tribal lands)"
indigenous_rights_flag: true
sensitivity_level: "Low (raw VWC) / Medium (derived biomass indicators)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false
data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../schemas/json/stac-smap-vwc-v11.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/stac-smap-vwc-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:vwc:2025:readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-vwc-2025"
event_source_id: "ledger:docs/data/satellites/smap/stac/vegetation-water/2025/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next VWC 2025 revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌿 **NASA SMAP — Vegetation Water Content (VWC) STAC Items (Year 2025)**  
`docs/data/satellites/smap/stac/vegetation-water/2025/README.md`

**Purpose**  
Provide the governed overview of all **2025 SMAP Vegetation Water Content (VWC)**  
STAC Items: vegetation moisture, biomass indicators, uncertainty layers, QA masks,  
and orbit/grid metadata.  
Aligned with **KFM-STAC v11**, FAIR+CARE + sovereignty rules, hydrology/climate ETL,  
and Story Node v3 / Focus Mode v3 environmental context.

</div>

---

## 📘 1. Overview

The **2025 VWC dataset** provides:

- 🌿 **Vegetation water content** (radiometer-derived)  
- 🌱 Soil–vegetation coupling metadata  
- ⚠️ Radiometer **QA/RFI flags**  
- 📉 Uncertainty layers  
- 🧭 EASE-Grid 2.0 footprints & BBoxes  
- 🔐 CARE/H3 sovereignty masking where needed  
- 🧾 Complete PROV-O lineage  
- 🧬 JSON-LD (schema.org + GeoSPARQL + OWL-Time) metadata  

These files power:

- Hydrology & ecohydrology ETL  
- Biomass change analysis  
- Archaeological landscape state inference  
- Fire risk preconditioning analytics  
- Seasonal vegetation state narratives in Story Node v3  
- Focus Mode v3 “background vegetation moisture” context  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A · v11.2.2)

~~~text
docs/data/satellites/smap/stac/vegetation-water/2025/
├── 📄 README.md                           # This file
│
├── 📅 2025-01-01-item.json                # Daily / 3-day VWC STAC Items
├── 📅 2025-01-02-item.json
├── 📅 2025-01-03-item.json
├── 📅 ...                                  # All days of 2025
│
└── 🗃️ assets/                              # Common asset bundle for 2025
    ├── 🌿 vegetation-water.tif             # Primary VWC raster
    ├── 📈 vegetation-uncertainty.tif       # Uncertainty layer
    ├── ⚠️ qa-flags.tif                     # QA / RFI mask
    └── 🧾 metadata.json                    # Orbit / grid / calibration / provenance metadata
~~~

All item filenames use the required pattern:  
**`YYYY-MM-DD-item.json`**

All COG filenames follow **KFM-STAC v11** conventions.  

---

## 🧩 3. STAC Item Requirements (KFM-STAC v11)

### Core Fields

Every 2025 SMAP VWC STAC Item MUST include:

- `"type": "Feature"`  
- `"id": "smap-vwc-2025-<date>"`  
- `"collection": "smap-vegetation-water"`  
- Valid `geometry` + `bbox`  
- `properties.datetime` or interval fields  
- `kfm:unit` (VWC retrieved units vary; typically `"kg/m2"` or `"dimensionless"` depending on version)  
- `kfm:uncertainty` (numeric or band-derived)  
- `kfm:qa_flags`  
- `kfm:care_label`  
- `kfm:sovereignty_note`  
- `kfm:mask_applied` (true/false)  
- `kfm:lineage` (PROV-O derivation chain)

### Required Assets

- **`data`** → VWC raster COG  
- **`uncertainty`** → VWC uncertainty COG  
- **`qa`** → Radiometer QA/RFI flag raster  
- **`metadata`** → Orbit/grid metadata JSON  

### Required Extensions

- `raster`  
- `proj`  
- `sat`  
- `kfm-gov`  
- `kfm-qa`  
- `kfm-provenance`  

---

## 🔐 4. Governance & Sovereignty

Vegetation & biomass moisture can reveal:

- land management patterns  
- culturally sensitive land transitions  
- ecological vulnerability  
- heritage-landscape visibility  

Thus KFM mandates:

- **CARE-A/B** labels where needed  
- **Dynamic H3 generalization** in sovereign Indigenous areas  
- `"kfm:mask_applied": true`  
- Full provenance & uncertainty in downstream visualizations  

Governance checks via:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

Each Item undergoes:

- JSON Schema validation  
- Geometry/BBox checks  
- Raster alignment (VWC, QA, uncertainty)  
- Temporal validity checks  
- QA/RFI classification checks  
- Cross-sensor QA vs:
  - SMAP soil moisture  
  - HydroGNSS biomass/wetness  
  - Landsat/Sentinel NDVI/EVI  
  - VIIRS fire & thermal indicators  
  - ERA5 vegetation metrics  

QA results:  
`docs/data/satellites/smap/qa/`  
Telemetry:  
`releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion → Lineage Pipeline (2025)

```
NASA SMAP L3 Vegetation Water Product
 → decode + map to EASE-Grid 2.0
 → integrate QA / RFI masks
 → extract VWC + biomass-related indices
 → propagate uncertainty
 → assemble STAC Item
 → CARE/H3 review
 → register collection + item (STAC/DCAT)
 → export lineage (PROV-O)
 → emit OpenLineage + OTel telemetry
```

All steps are WAL-protected & deterministic.

---

## 🔮 7. Applications Inside KFM (2025)

### Climate  
- Vegetation water stress  
- Biomass anomaly tracking  

### Ecology  
- Grassland dynamics  
- Fire-risk indicators  

### Archaeology  
- Visibility of cultural features  
- Vegetation masking cycles  
- Wetness/biomass transitions near heritage corridors  

### Story Node v3  
- Environmental backdrop for narrative sequences  

### Focus Mode v3  
- Vegetation-moisture context for entity/event explanations  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                             |
|--------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First full v11.2.2 SMAP VWC year-layer README; emoji layout; STAC v11; governance/H3 alignment.     |
| v10.3.2 | 2025-11-14 | Pre-v11 skeletal STAC directory.                                                                    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ VWC STAC Home](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

