---
title: "📦 NASA SMAP — Freeze/Thaw Assets (2025) · Data / QA / Uncertainty / Metadata"
path: "docs/data/satellites/smap/stac/freeze-thaw/2025/assets/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-freeze-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Asset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B depending on geographic overlap"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived transition patterns)"
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

json_schema_ref: "../../../../../../../../schemas/json/stac-smap-freeze-v11.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/stac-smap-freeze-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:freeze-thaw:2025:assets-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-freeze-thaw-2025-assets"
event_source_id: "ledger:docs/data/satellites/smap/stac/freeze-thaw/2025/assets/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next FT-assets revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Freeze/Thaw Assets (2025)**  
`docs/data/satellites/smap/stac/freeze-thaw/2025/assets/README.md`

**Purpose**  
Document the **per-Item asset bundle** for all 2025 SMAP Freeze/Thaw daily STAC Items:  
FT raster, QA mask, uncertainty layer, and metadata, aligned to **KFM-STAC v11** and governed  
under **FAIR+CARE + sovereignty** review.

</div>

---

## 📘 1. Overview

Each Freeze/Thaw STAC Item in **2025** references this directory for its **asset files**, providing:

- ❄️ **Freeze/Thaw raster** (`frozen` / `thawed` / `transition`)  
- ⚠️ **QA/RFI mask** (radiometer integrity, gain anomalies, RFI detection)  
- 📈 **Uncertainty raster** (per-pixel reliability estimate)  
- 🧾 **Orbit/Grid metadata** (EASE-Grid mapping, sensor timing, provenance)  

These assets serve:

- Hydrology + climate ETL  
- Seasonal transition analyses  
- Archaeological hazard interpretation  
- Focus Mode v3 environmental background  
- Story Node v3 temporal-spatial layering  
- Cross-mission validation (HydroGNSS, Mesonet, ERA5)

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/freeze-thaw/2025/assets/
├── 📄 README.md                        # This file
│
├── ❄️ freeze-thaw.tif                  # Freeze/Thaw state raster
├── ⚠️ qa-flags.tif                     # QA/RFI mask (sensor & retrieval quality)
├── 📈 freeze-uncertainty.tif           # Uncertainty raster (standard deviation/error estimate)
└── 🧾 metadata.json                    # Orbit/grid/provenance metadata for FT retrieval
~~~

---

## 🧩 3. Asset Specifications (KFM-STAC v11)

### ❄️ **freeze-thaw.tif**

Primary raster indicating:

- `"frozen"` (1)  
- `"thawed"` (0)  
- `"transition"` (2)  

Required metadata:

- `kfm:state`  
- `raster:bands` (nodata, scale, offset)  
- `proj:*` EASE-Grid 2.0 parameters  
- Uncertainty linkage field

---

### ⚠️ **qa-flags.tif**

Encodes:

- Radiometric QC flags  
- RFI detection  
- Grid anomalies  
- Confidence drops near snow/wetness boundaries  

Metadata requirements:

- `kfm:qa_flag_schema`  
- `kfm:qa_interpretation`  
- `kfm:qa_values` (coded legend)

---

### 📈 **freeze-uncertainty.tif**

Represents per-pixel uncertainty for freeze/thaw classification.

Required metadata:

- `kfm:uncertainty_type: "classification"`  
- `kfm:stdev`  
- `kfm:error_model`  

Supports:

- Story Node v3 confidence displays  
- Focus Mode v3 environmental background qualifiers  

---

### 🧾 **metadata.json**

Contains:

- ESA/NASA L3_FT product identifiers  
- Orbit/attitude metadata  
- EASE-Grid info  
- Calibration notes  
- Processing chain (PROV-O)  
- CARE/H3 flags  

This file must be **lineage-complete**.

---

## 🔐 4. Governance & Sovereignty

Freeze/Thaw data can reveal:

- Seasonal accessibility  
- Wetland behavior  
- Ground stability risks  
- Ecological/cultural landscape transitions  

Thus KFM mandates:

- **CARE-A/B labels** for FT-derived layers in cultural/tribal contexts  
- **Dynamic H3 masking** for sensitive areas (e.g., thaw-related erosion near heritage sites)  
- `"kfm:mask_applied": true` where appropriate  
- Complete provenance reporting in derived layers  

Governance validation pipelines include:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

Assets are validated for:

- COG structural integrity  
- Raster alignment (freeze, qa, uncertainty)  
- BBox/geometry consistency across Items  
- Temporal continuity  
- Cross-sensor QA vs:
  - SMAP soil moisture  
  - HydroGNSS  
  - Mesonet freeze observations  
  - ERA5-Land freeze-line  

QA results live at:  
`docs/data/satellites/smap/qa/`

Telemetry exported to:  
`releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion → Lineage

```
NASA SMAP L3_FT Product
 → decode + grid-mapping
 → QA/RFI mask integration
 → uncertainty propagation
 → COG generation
 → CARE/H3 masking
 → STAC asset registration
 → PROV-O lineage export
 → OpenLineage + OTel telemetry
```

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Freeze–thaw boundary detection  
- Spring runoff estimation  
- Surface-process hazard modeling  

### Climate  
- Seasonal freeze-line anomalies  
- Early/late thaw trend analysis  

### Archaeology  
- Freeze-related site risk  
- Seasonal-landscape access  

### Story Node v3  
- Environmental change context  

### Focus Mode v3  
- Background freeze/thaw conditions for entities and events  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                |
|--------:|------------|--------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full asset-level README created; CARE/H3 rules; emoji layout; STAC v11-conformant; provenance aligned. |
| v10.3.2 | 2025-11-14 | Pre-v11 placeholder assets structure.                                                                  |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ Freeze/Thaw 2025](../README.md) · [🛡 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

