---
title: "🔧 NASA SMAP — Transformation & Harmonization Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/transforms/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
provenance_profile: "KFM-PROV-O v11.2"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Pipeline Documentation"
fair_category: "F1-A1-I2-R3"
care_label: "CARE-A / CARE-B (depending on variable)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  prov_o: "prov:Activity"
  schema_org: "DataTransform"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/transform-smap-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/transform-smap-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transforms-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transforms"
event_source_id: "ledger:docs/data/satellites/smap/transforms/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next SMAP ETL revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔧 **NASA SMAP — Transform & Harmonization Pipelines (KFM v11.2.2)**  
`docs/data/satellites/smap/transforms/README.md`

**Purpose**  
Describe all **transformation pipelines** for NASA SMAP datasets inside KFM —  
from raw NASA L2/L3 → harmonized KFM rasters → STAC Items → DCAT datasets →  
PROV-O lineage → governance/CARE masking → Story Node v3 + Focus Mode v3 context.

</div>

---

## 📘 1. Overview

This directory contains the **entire SMAP transformation layer**, including:

- 🛰️ **Decoding NASA L2/L3 radiometer products**  
- 🗺️ **EASE-Grid 2.0 → KFM CRS reprojection**  
- 🧼 **Temporal + spatial harmonization**  
- ⚠️ **QA/RFI mask integration**  
- 🎚️ **Calibration & radiometer drift correction**  
- 📉 **Uncertainty propagation**  
- 🔐 **CARE/H3 governance generalization**  
- 🧾 **PROV-O lineage construction**  
- 🧬 **STAC & DCAT metadata emission**  
- 📦 **COG generation for data / QA / uncertainty**  

These pipelines support:

- Soil Moisture  
- Freeze/Thaw  
- Vegetation Water (VWC)  
- QA/RFI Flags  
- Ancillary metadata production  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/
├── 📄 README.md                           # This file
│
├── 🛠️ decode/                             # NASA L2/L3 decoding & raw ingest
│   ├── decode_l2.py
│   └── decode_l3.py
│
├── 🗺️ reprojection/                       # EASE-Grid → KFM CRS projection modules
│   ├── ease_to_kfm_grid.py
│   └── geolocation_utils.py
│
├── 🎚️ calibration/                        # Radiometer calibration + drift correction
│   ├── apply_calibration.py
│   └── calibration_tables/
│
├── ⚠️ qa_integration/                     # QA/RFI flags + radiometric QC
│   ├── integrate_qa.py
│   ├── decode_rfi.py
│   └── qa_flag_schema.json
│
├── 📉 uncertainty/                        # Uncertainty derivation models
│   ├── propagate_uncertainty.py
│   └── uncertainty_models/
│
├── 🔐 governance/                         # CARE/H3 sovereignty masking
│   ├── apply_masking.py
│   └── h3_policy.json
│
├── 📦 stac_writer/                        # KFM-STAC v11 item/collection builders
│   ├── build_item.py
│   ├── build_collection.py
│   └── stac_extensions/
│
├── 🧾 provenance/                         # PROV-O lineage builders
│   ├── build_prov.py
│   └── prov_context.jsonld
│
└── 📚 utils/                              # Shared helpers
    ├── dates.py
    ├── grid.py
    ├── raster_io.py
    └── logging.py
~~~

---

## 🧩 3. Pipeline Breakdown (KFM v11)

### 3.1 🛠️ Decode Stage (NASA L2/L3)
- Parse HDF5/NetCDF radiometer products  
- Extract brightness temperature / soil moisture / freeze–thaw / VWC fields  
- Normalize metadata structures  
- Validate mission identifiers, DOIs, versioning  

---

### 3.2 🗺️ Reprojection Stage (EASE-Grid → KFM CRS)
- Use shared KFM grid definitions  
- Check anti-meridian handling  
- Maintain geolocation precision  
- Harmonize pixel-area / cell-shape assumptions  

---

### 3.3 🎚️ Calibration Stage
- Radiometer drift correction  
- Mode-dependent adjustments  
- Warm/cold calibration offsets  
- Calibration QA integrated into metadata  

---

### 3.4 ⚠️ QA/RFI Integration
- Decode RFI flags  
- Integrate radiometer-level QA  
- Apply surface-condition corrections  
- Place QA masks in both “qa” and “uncertainty” asset roles  

---

### 3.5 📉 Uncertainty Propagation
- Compute or propagate uncertainty for:
  - Soil moisture
  - Freeze/thaw
  - VWC  
- Support uncertainty overlays in KFM UI  
- Write uncertainty surfaces as COGs  

---

### 3.6 🔐 CARE/H3 Sovereignty Masking
- Apply H3 resolution-based generalization  
- Remove overly sharp spatial detail near sensitive areas  
- Add:
  - `kfm:care_label`  
  - `kfm:sovereignty_note`  
  - `"kfm:mask_applied": true`  
- Update lineage with governance decisions  

---

### 3.7 📦 STAC Writer Stage
- Build STAC Collections  
- Build STAC Items  
- Apply:
  - projection extension  
  - raster extension  
  - sat extension  
  - KFM provenance + governance extensions  
- Validate output via schema + STAC validator  

---

### 3.8 🧾 PROV-O Lineage
- Each STAC Item has:
  - `prov:wasDerivedFrom` (NASA L2/L3)  
  - `prov:wasGeneratedBy` (KFM transform pipeline)  
  - `prov:used` (QA masks, calibration tables, ancillary metadata)  
- Exported into JSON-LD + graph backend  

---

## 🔐 4. Governance & Sovereignty Controls

All transforms must:

- Retain CARE classification  
- Honor sovereignty constraints  
- Record masking & generalization choices  
- Never sharpen sensitive geospatial detail  
- Propagate metadata via STAC/DCAT/JSON-LD  

Non-compliant pipelines = **CI hard failure**.

---

## 🧪 5. QA & Validation

Validation includes:

- Raster alignment checks  
- CRS integrity  
- STAC schema compliance  
- JSON-LD ontology conformance  
- PROV-O chain completeness  
- Cross-sensor validation (HydroGNSS, Mesonet, ERA5)  
- Performance telemetry (energy, carbon)

Results in:

`docs/data/satellites/smap/qa/`

Telemetry → `releases/<version>/data-telemetry.json`

---

## 🔁 6. End-to-End Lineage Workflow

```
NASA SMAP L2/L3
 → decode
 → geolocation + reprojection
 → calibration + QA/RFI integration
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC Item/Collection assembly
 → PROV-O lineage/JSON-LD export
 → DCAT dataset registration
 → OpenLineage telemetry emission
```

All steps **WAL-protected, deterministic, reproducible**.

---

## 🔮 7. Applications Inside KFM

### Hydrology
- Soil moisture/hydrologic trend analyses  
- Freeze-line behavior  

### Climate
- Vegetation stress  
- Drought/wetness cycles  

### Archaeology
- Environmental context for cultural landscapes  

### Story Node v3
- Environmental backdrops  
- Data-provenance explanation overlays  

### Focus Mode v3
- Confidence + calibration context  
- Relevant dataset linking  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                          |
|--------:|------------|--------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full pipeline documentation; emoji-rich; governance/H3; STAC v11; PROV-O alignment; CI-safe.    |
| v10.3.2 | 2025-11-14 | Pre-v11 transform outline.                                                                        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ SMAP Data Home](../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

