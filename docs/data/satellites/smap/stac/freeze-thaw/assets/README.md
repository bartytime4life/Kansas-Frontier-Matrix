---
title: "📦 NASA SMAP — Freeze/Thaw Asset Definitions (Global) · Data / QA / Uncertainty / Metadata"
path: "docs/data/satellites/smap/stac/freeze-thaw/assets/README.md"
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

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-smap-freeze-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Asset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B (dependent on geographic overlap)"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived transitions)"
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

json_schema_ref: "../../../../../../schemas/json/stac-smap-freeze-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/stac-smap-freeze-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:freeze-thaw:assets:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-freeze-assets"
event_source_id: "ledger:docs/data/satellites/smap/stac/freeze-thaw/assets/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded on next FT asset-schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Freeze/Thaw Asset Definitions (Global)**  
`docs/data/satellites/smap/stac/freeze-thaw/assets/README.md`

**Purpose**  
Define the global **Freeze/Thaw STAC asset templates** used across *all* years of SMAP FT STAC Items  
(e.g., `/2023/`, `/2024/`, `/2025/`, etc.).  
These represent the **actual raster and metadata payloads** referenced by each STAC Item:  
FT classification, QA/RFI masks, uncertainty surfaces, and orbit/grid metadata.

</div>

---

## 📘 1. Overview

Freeze/thaw data from NASA SMAP provides:

- ❄️ **Frozen** surface state  
- 🌿 **Thawed** ground state  
- 🔄 **Transition** state regions  
- ⚠️ **RFI + radiometric QA**  
- 📉 **Uncertainty estimates**  
- 🧾 Sensor + orbit + grid metadata  

These global asset definitions ensure:

- STAC consistency across years  
- FAIR+CARE governance enforcement  
- H3-based sovereignty masking where required  
- Reuse of common metadata  
- No divergence between year-level STAC folders  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/freeze-thaw/assets/
├── 📄 README.md                     # This file
│
├── ❄️ freeze-thaw.tif               # Global FT raster template (per-day files in year dirs)
├── ⚠️ qa-flags.tif                  # QA / RFI mask (radiometer condition flags)
├── 📈 freeze-uncertainty.tif        # Uncertainty surface (retrieval reliability metric)
└── 🧾 metadata.json                 # Orbit/grid/sensor provenance; processing + calibration metadata
~~~

📝 **Note:**  
These global files define the **schema & metadata rules** applicable to all year-specific assets.  
Actual per-day rasters live in directories like:  
`docs/data/satellites/smap/stac/freeze-thaw/2025/assets/`.

---

## 🧩 3. Asset Specifications (KFM-STAC v11)

### ❄️ freeze-thaw.tif — FT State Raster

Values:

- `0` → thawed  
- `1` → frozen  
- `2` → transition  

Metadata required:

- `raster:bands` specs (nodata, scale, offset, data_type)  
- `proj:epsg` / `proj:transform`  
- `kfm:state_info` (classification definition)  
- `kfm:uncertainty_link` (ties to uncertainty raster)

---

### ⚠️ qa-flags.tif — QA / RFI Mask

Includes:

- RFI detection  
- Radiometer performance flags  
- Gain stability flags  
- Retrieval quality codes  

Metadata required:

- `kfm:qa_flag_schema`  
- `kfm:qa_values` (coded legend)  
- `kfm:qa_interpretation`

---

### 📈 freeze-uncertainty.tif — Uncertainty Raster

Represents per-pixel classification uncertainty.

Metadata required:

- `kfm:uncertainty_type: "classification"`  
- `kfm:error_model`  
- `kfm:stdev`  
- `proj:*` & `raster:*`  

---

### 🧾 metadata.json — Orbit / Provenance

Contains:

- EASE-Grid 2.0 grid info  
- Orbit parameters (local time of overpass, swath ID, direction)  
- Calibration notes  
- Processing chain description  
- PROV-O lineage  
- CARE/H3 flags & sovereignty conditions  

This file must be **comprehensive and non-speculative**.

---

## 🔐 4. Governance & Sovereignty Requirements

Freeze/Thaw patterns may reveal:

- access to landscapes  
- seasonal vulnerability  
- wetland or habitat dynamics  
- possible cultural-landscape transitions  

Thus KFM enforces:

- **CARE-A/B labeling** where applicable  
- Mandatory **H3 generalization** in sensitive Indigenous areas  
- `"kfm:mask_applied": true` when H3 upscaling is applied  
- Clear uncertainty + provenance disclosure in derived visualizations  

All assets must pass:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml` governance hooks  

---

## 🧪 5. QA & Validation Requirements

Validate:

- COG integrity  
- GeoSpatial alignment (freeze, QA, uncertainty)  
- Temporal consistency  
- Agreement with NASA SMAP L3_FT  
- Cross-sensor agreement with:
  - SMAP soil moisture  
  - HydroGNSS freeze signals  
  - Mesonet freeze data  
  - ERA5-Land freeze-line  

QA logs stored in:  
`docs/data/satellites/smap/qa/`

Telemetry exported to:  
`releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion → Lineage Workflow

```
NASA SMAP L3_FT Product
 → decode + grid harmonization
 → QA/RFI integration
 → uncertainty derivation
 → COG generation
 → CARE/H3 governance enforcement
 → STAC asset registration
 → lineage export (PROV-O)
 → OpenLineage + OTel telemetry
```

All steps use WAL-safe, reproducible pipelines.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Freeze-line mapping  
- Spring thaw → runoff forecasting  

### Climate  
- Seasonal freeze/thaw anomalies  
- Climate regime change indicators  

### Archaeology  
- Winter/spring access to cultural landscapes  
- Freeze-related site risk  

### Story Node v3 / Focus Mode v3  
- Seasonal transition context  
- Environmental “background state” layers  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                |
|--------:|------------|--------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Created global freeze/thaw asset definitions; CARE/H3 rules; emoji layout; STAC v11 alignment; CI-safe. |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal placeholder.                                                                           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ Freeze/Thaw STAC](../README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

