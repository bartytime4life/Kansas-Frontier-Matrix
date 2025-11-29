---
title: "📦 NASA SMAP — Vegetation Water Content (VWC) Assets (2025) · Data / QA / Uncertainty / Metadata"
path: "docs/data/satellites/smap/stac/vegetation-water/2025/assets/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-vwc-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Asset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B depending on Indigenous overlap"
indigenous_rights_flag: true
sensitivity_level: "Low (raw VWC) / Medium (derived biomass/wetness indicators)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "DataDownload"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../schemas/json/stac-smap-vwc-v11.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/stac-smap-vwc-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:vwc:2025:assets-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-vwc-2025-assets"
event_source_id: "ledger:docs/data/satellites/smap/stac/vegetation-water/2025/assets/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next VWC asset-schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Vegetation Water Content (VWC) Assets (2025)**  
`docs/data/satellites/smap/stac/vegetation-water/2025/assets/README.md`

**Purpose**  
Document the **asset bundle** referenced by all **2025 SMAP VWC STAC Items**:  
VWC raster, QA/RFI mask, uncertainty raster, and orbit/grid/provenance metadata.  
These assets conform to **KFM-STAC v11**, **FAIR+CARE + sovereignty rules**, and  
support KFM hydrology, climate, ecology, archaeology, Focus Mode v3, and Story Node v3.

</div>

---

## 📘 1. Overview

Each VWC STAC Item (daily or 3-day composite) in **2025** references this directory for:

- 🌿 **Vegetation Water Content raster**  
- 📈 **Uncertainty raster** (confidence / error propagation)  
- ⚠️ **QA/RFI mask** (radiometer quality codes)  
- 🧾 **Metadata JSON** (orbit, grid, calibration, provenance, sovereignty flags)  

These assets support:

- Biomass/wetness fusion  
- Drought & fire-risk ETL  
- Soil–vegetation coupling diagnostics  
- Archaeological vegetation visibility modeling  
- Environmental context layers in Story Node v3 and Focus Mode v3  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/vegetation-water/2025/assets/
├── 📄 README.md                           # This file
│
├── 🌿 vegetation-water.tif                # Primary VWC raster
├── 📈 vegetation-uncertainty.tif          # Uncertainty raster
├── ⚠️ qa-flags.tif                         # QA / RFI mask raster
└── 🧾 metadata.json                        # Orbit/grid/provenance metadata (EASE-Grid, sensor, calibration)
~~~

All assets **must** follow the KFM-STAC v11 naming & schema rules.

---

## 🧩 3. Asset Specifications (KFM-STAC v11)

### 🌿 vegetation-water.tif — VWC Raster

- Radiometer-derived vegetation water content  
- Units may be:
  - `"kg/m2"`  
  - `"dimensionless"` (sensor-specific)  
- Metadata:
  - `raster:bands[]` with nodata/scale/offset  
  - `proj:*` EASE-Grid 2.0  
  - `kfm:unit`  
  - `kfm:uncertainty_link`  

---

### 📈 vegetation-uncertainty.tif — Uncertainty Raster

Specifies retrieval confidence:

- `kfm:uncertainty_type: "radiometric"`  
- `kfm:error_model`  
- `kfm:stdev`  
- Aligned to the VWC raster grid  

Used to:

- Drive uncertainty overlays in KFM web  
- Annotate Story Node v3 environmental narratives  
- Condition Focus Mode v3 environmental logic  

---

### ⚠️ qa-flags.tif — QA / RFI Mask

Encodes:

- RFI detection  
- Radiometer gain issues  
- Retrieval anomalies  
- Low-confidence zones  

Metadata includes:

- `kfm:qa_flag_schema`  
- `kfm:qa_values` (legend)  
- `kfm:qa_interpretation`  

---

### 🧾 metadata.json — Orbit / Grid / Provenance Metadata

Must include:

- EASE-Grid definitions  
- Overpass time / orbit geometry  
- Calibration notes  
- NASA L3 source product IDs  
- Full **PROV-O lineage** (derivations)  
- `kfm:care_label`, `kfm:sovereignty_note`, `kfm:mask_applied`  

---

## 🔐 4. Governance & Sovereignty

Vegetation moisture & biomass may expose:

- land-management signals  
- ecological vulnerability  
- cultural-landscape transitions  
- visibility changes relevant to heritage sites  

KFM enforces:

- **CARE-A/B labeling**  
- **Dynamic H3 generalization** in Indigenous territories  
- `"kfm:mask_applied": true` when active  
- Mandatory uncertainty & provenance display in all derived UI layers  

Governance checks triggered via:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

Validation includes:

- COG structural verification  
- Raster alignment checks (VWC, QA, uncertainty)  
- BBox/geometry alignment with STAC Items  
- Temporal plausibility checks  
- QA/RFI decoding  
- Cross-sensor QA vs:
  - SMAP soil moisture  
  - HydroGNSS biomass/wetness  
  - Landsat/Sentinel NDVI/EVI  
  - VIIRS thermal/fire hotspots  
  - ERA5 vegetation metrics  

QA logs → `docs/data/satellites/smap/qa/`  
Telemetry → `releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion → Lineage

```
NASA SMAP L3 VWC Product
 → decode + EASE-Grid mapping
 → QA/RFI mask integration
 → vegetation-water extraction
 → uncertainty propagation
 → COG generation
 → CARE/H3 sovereignty enforcement
 → STAC asset registration
 → PROV-O lineage export
 → OpenLineage + OTel telemetry
```

---

## 🔮 7. Applications Inside KFM

### Climate  
- Vegetation water stress monitoring  
- Biomass anomalies  

### Ecology  
- Grassland/plains moisture states  
- Fire-risk modeling  

### Archaeology  
- Vegetation masking of cultural features  
- Biomass-driven visibility cycles  

### Story Node v3  
- Environmental backdrops (vegetation moisture state)  

### Focus Mode v3  
- Vegetation-wetness context for entities/events  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                |
|--------:|------------|--------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Created full VWC 2025 asset README; emoji layout; governance/H3 rules; STAC v11 alignment; CI-safe.   |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal asset skeleton.                                                                         |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ VWC 2025](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

