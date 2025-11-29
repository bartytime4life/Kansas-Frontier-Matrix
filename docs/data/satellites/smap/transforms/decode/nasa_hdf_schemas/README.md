---
title: "📚 NASA SMAP — L2/L3 HDF Schema Definitions for Decode Stage (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/data/satellites/smap/transforms/decode/nasa_hdf_schemas/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

doc_kind: "ETL Schema Reference"
intent: "smap-hdf-schemas"
role: "decode-stage-schemas"
category: "Satellite · ETL · Schema"

classification: "Public ETL Documentation"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B (dependent on downstream use)"
indigenous_rights_flag: true
sensitivity_level: "Low (schema only)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../schemas/json/transform-smap-hdf-schemas-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/transform-smap-hdf-schemas-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transforms:decode:nasa-hdf-schemas-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-decode-hdf-schemas"
event_source_id: "ledger:docs/data/satellites/smap/transforms/decode/nasa_hdf_schemas/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next SMAP product-schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📚 **NASA SMAP — L2/L3 HDF Schema Definitions (Decode Stage)**  
`docs/data/satellites/smap/transforms/decode/nasa_hdf_schemas/README.md`

**Purpose**  
Provide **formal schema descriptions** for NASA SMAP L2/L3 HDF5/NetCDF products  
used by the **Decode Stage** of the KFM SMAP ETL pipeline.  
These schemas ensure *deterministic, reproducible, FAIR+CARE-safe parsing* of  
soil-moisture, freeze–thaw, VWC, and QA variables into the KFM transformation stack.

</div>

---

## 📘 1. Overview

The `nasa_hdf_schemas/` directory defines **how KFM understands NASA SMAP products** at the file level:

- Group/variable layout for **L2** (swath-level) and **L3** (gridded) products  
- Data-type, dimension, and attribute expectations  
- Mapping rules from **NASA variable names → KFM canonical fields**  
- QA/RFI representation at the file-schema level  
- Required metadata fields (orbit, time, grid, processing version)  

These schemas are consumed by:

- `decode_l2.py`  
- `decode_l3.py`  
- Downstream transform modules that rely on consistent field presence & semantics  

They are the **source of truth** for decode logic — changes here imply controlled decode-pipeline updates.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/decode/nasa_hdf_schemas/
├── 📄 README.md                      # This file
│
├── 📜 l2_schema.json                 # HDF schema for SMAP L2 radiometer/swath products
├── 📜 l3_sm_schema.json              # HDF schema for SMAP L3 Soil Moisture
├── 📜 l3_ft_schema.json              # HDF schema for SMAP L3 Freeze/Thaw (FT)
├── 📜 l3_vwc_schema.json             # HDF schema for SMAP L3 Vegetation Water Content (VWC)
└── 📚 common_fields.json             # Shared field definitions (time, orbit, QA, etc.)
~~~

Each file describes **expected groups/variables/attributes** and their mapping into the KFM decode pipeline.

---

## 🧩 3. Schema Files & Responsibilities

### 📜 `l2_schema.json` — SMAP L2 Swath Products

Describes:

- HDF5 group layout for L2 radiometer products  
- Lat/lon, incidence angle, brightness temperature fields  
- Swath-level QA/RFI fields  
- Orbit metadata (track, pass, local time)  
- Dimension definitions (scan, footprint, channel)  

Used by `decode_l2.py` to:

- Validate field presence & shapes  
- Map NASA field names → KFM canonical variable names  
- Extract orbit + geometry metadata for PROV-O & STAC  

---

### 📜 `l3_sm_schema.json` — SMAP L3 Soil Moisture

Includes:

- Grid-level soil moisture variables (`soil_moisture`, `soil_moisture_error`)  
- EASE-Grid dimensions (row, column)  
- QA flags for soil moisture  
- Processing version attributes  
- Global attributes for sensor/mode  

Used by `decode_l3.py` and soil-moisture transforms to ensure:

- Compatible dimensionality  
- Correct unit + scale/offset handling  
- Presence of required QA and uncertainty fields  

---

### 📜 `l3_ft_schema.json` — SMAP L3 Freeze/Thaw

Describes:

- FT classification variable (`freeze_thaw_state`)  
- Coding scheme (frozen, thawed, transition, etc.)  
- Associated QA flags  
- Temporal attributes (daily/3-day windows)  

Ensures freeze–thaw STAC Items:

- Are derived from valid NASA fields  
- Use the correct classification scheme  
- Carry necessary QA/uncertainty metadata  

---

### 📜 `l3_vwc_schema.json` — SMAP L3 Vegetation Water Content

Defines:

- Vegetation water content variable(s)  
- Units, scaling, and valid ranges  
- VWC-specific QA fields  
- Sensor-specific flags relevant to VWC retrievals  

Used by the VWC transform chain to:

- Validate input fields exist and are consistent  
- Normalize units for KFM usage  
- Tie QA and uncertainty to appropriate variables  

---

### 📚 `common_fields.json` — Shared Fields & Constraints

Centralizes definitions for:

- Time fields (start/end time, mid-scan time, etc.)  
- Orbit identifiers  
- Platform/instrument names  
- Global attributes required for provenance  
- Shared QA code domains  
- Shared uncertainty attributes  

Guarantees:

- Consistent decode behavior across SMAP product families  
- Single point of change for time/orbit/QA-level semantics  

---

## 🔐 4. Governance & FAIR+CARE Impact

While these schemas describe **technical structures**, they have governance effects:

- Identify which fields **must** propagate CARE + sovereignty metadata downstream  
- Declare where masking flags must be attached (e.g., `care_label`, H3 generalization states)  
- Prevent use of “optional” NASA fields that KFM intentionally excludes for ethics or provenance reasons  

Schema changes must be reviewed by:

- Earth Systems Working Group  
- FAIR+CARE Council  
- Sovereignty reviewers (as needed)  

---

## 🧪 5. Validation & CI Integration

These schema files are used by decode tests to ensure:

- NASA products match expected HDF structure  
- All required dimensions/variables exist and are typed correctly  
- Transform modules use up-to-date field definitions  
- No decode code path depends on fields not declared here  

Validation steps:

- JSON Schema / SHACL validation of these spec files  
- Sample-product comparison (HDF introspection)  
- Decode-stage tests in:

```text
docs/data/satellites/smap/transforms/decode/tests/

