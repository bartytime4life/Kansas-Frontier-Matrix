---
title: "🛠️ NASA SMAP — Decode Stage (L2/L3 Raw Product Ingest) · ETL Stage 1 (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/data/satellites/smap/transforms/decode/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
provenance_profile: "KFM-PROV-O v11.2"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public ETL Documentation"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A (Indigenous review required when spatially intersecting)"
indigenous_rights_flag: true
public_exposure_risk: "Low"
sensitivity_level: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  prov_o: "prov:Activity"
  schema_org: "DataDownload"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../schemas/json/transform-smap-decode-v11.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/transform-smap-decode-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transforms:decode-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transform-decode"
event_source_id: "ledger:docs/data/satellites/smap/transforms/decode/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next decode-pipeline revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛠️ **NASA SMAP — Decode Stage (Raw L2/L3 Product Ingest)**  
`docs/data/satellites/smap/transforms/decode/README.md`

**Purpose**  
Document the **Decode Stage** of the SMAP ETL pipeline: ingestion of  
NASA L2/L3 radiometer products, extraction of scientific variables, metadata normalization,  
and preparation for reprojection, calibration, QA integration, and governance screening.

</div>

---

## 📘 1. Overview

The **Decode Stage** is **Stage 1** of the KFM SMAP transformation chain.

It performs:

- 🛰️ **Raw NASA L2/L3 product ingestion** (HDF5 / NetCDF)  
- 🧩 **Extraction of scientific fields**:
  - soil moisture  
  - freeze/thaw classification  
  - vegetation water content (VWC)  
  - brightness temperature  
  - QA flags  
- 🧾 **Metadata normalization**  
- 🎚 Calibration pre-checks  
- 🕓 Temporal standardization (ISO 8601, OWL-Time)  
- 🗺️ Orbit geometry extraction  
- 🔧 Pre-validation for KFM-STAC v11 compliance  
- 🔐 Initial governance tag assignment (mission-wide CARE/H3 pre-scan)

Output is a **decoded, structured data batch** used by later stages:

```
decode → reprojection → calibration → QA integration → uncertainty → governance → STAC/DCAT → lineage
```

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/decode/
├── 📄 README.md                      # This file
│
├── 🛠️ decode_l2.py                   # SMAP L2 radiometer decode script
├── 🛠️ decode_l3.py                   # SMAP L3 (soil moisture / freeze-thaw / VWC) decode logic
├── 📚 nasa_hdf_schemas/              # NASA product schema descriptions (HDF5/NetCDF groups)
│   ├── l2_schema.json
│   └── l3_schema.json
├── 🧭 extract_orbit.py               # Orbit metadata extraction (swath, pass, LTAN)
├── 🧭 extract_temporal.py            # Timestamp normalization (UTC→ISO→OWL-Time)
├── 🔍 extract_metadata.py            # Metadata flattening + normalization
└── 🧪 tests/                         # Decode-stage validation tests
    ├── test_decode_l2.py
    ├── test_decode_l3.py
    └── test_metadata_norm.py
~~~

---

## 🧩 3. Decode Stage Responsibilities

### 3.1 🛰️ Raw Product Loading

- Read SMAP L2/L3 HDF5/NetCDF:  
  - brightness temperature  
  - quality control/engineering variables  
  - soil moisture  
  - freeze/thaw classification  
  - vegetation indices  
- Extract **swath-level** geolocation:
  - latitude  
  - longitude  
  - incidence angle  
  - orbit direction  

### 3.2 🧾 Metadata Normalization

- Flatten nested product metadata  
- Convert NASA-specific field names → KFM-standard names  
- Extract:
  - `platform`  
  - `processing_level`  
  - `production_time`  
  - `orbit_metadata`  
  - `retrieval_flags`  
- Insert KFM metadata stubs:
  - `kfm:source_product`  
  - `kfm:uncertainty_stub`  
  - `kfm:governance_stub`  

### 3.3 🕓 Temporal Processing

- Convert NASA timestamps → ISO 8601  
- Create OWL-Time interval representations  
- Validate temporal coverage against mission timelines  

### 3.4 🎚 Pre-Calibration

- Extract calibration fields  
- Validate calibration version ↔ KFM calibration tables  
- Produce warnings/flags for drift detectors (downstream)

### 3.5 🔍 Structural Validation

- Validate decoded product matches NASA schema  
- Verify data fields exist for the selected SMAP mode  
- Cross-check array dimensions before grid mapping  

### 3.6 🔐 Governance Pre-Scan

Using **CARE/H3-sensitive geometry overlays**, detect:

- Tribal lands intersections (inform downstream masking)  
- Sensitive ecological zones  
- Potentially protected land-use areas  

The decode stage **does not apply masking**, but sets governance flags  
for later mandatory masking.

---

## 🔁 4. Outputs of Decode Stage

The decode step outputs:

```
decoded_product = {
  "geometry": { ... },            # Swath-based footprint
  "metadata": { ... },            # Normalized metadata
  "orbit": { ... },               # Track + pass info
  "temporal": { ... },            # datetime / interval
  "variables": {
      "soil_moisture": [...],
      "freeze_thaw": [...],
      "vegetation_water": [...],
      "brightness_temp": [...],
      "qa_flags": [...]
  },
  "governance": {
      "care_label": "A/B",
      "sovereignty_precheck": true/false
  }
}
```

This object is used by later transform stages.

---

## 🔐 5. Governance & Sovereignty Handling

Decode stage **assigns no mask**, but triggers:

- CARE label inference (mission-level guidance)  
- H3 spatial “flagging” for sensitive areas  
- Sovereignty warnings for:
  - tribal territories  
  - cultural landscapes  
  - wetlands with cultural significance  

These flags **must propagate downstream**.

Decode output is validated by:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 6. QA & Validation Tests

Decode-stage tests verify:

- NASA schema conformance  
- Correct variable extraction  
- Accurate timestamp processing  
- Geolocation & swath footprint integrity  
- Metadata flattening  
- CARE/H3 pre-scan logic  
- Structural correctness for STAC assembly  

Coverage located at:

```
docs/data/satellites/smap/transforms/decode/tests/
```

---

## 🔁 7. Integration in Full ETL Pipeline

```
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance (CARE/H3)
 → STAC item generation
 → DCAT metadata generation
 → PROV-O lineage export
 → OpenLineage telemetry
```

Decode stage is the foundation for **all** downstream logic.

---

## 🔮 8. Applications Inside KFM

### Hydrology  
- Soil moisture quality interpretation  
- Freeze/thaw classification stability  

### Climate  
- Seasonal vegetation water logic  
- Drought model initialization  

### Archaeology  
- Environmental visibility shifts  
- Soil-landscape state interpretation  

### Focus Mode v3  
- Provenance-first environmental reasoning  

### Story Node v3  
- Accurate environmental backdrops for narratives  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                       |
|--------:|------------|-----------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full decode-pipeline documentation; emoji directory; governance/H3; STAC v11; CI-safe.        |
| v10.3.2 | 2025-11-14 | Pre-v11 decode outline.                                                                        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ SMAP Transform Layer](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

