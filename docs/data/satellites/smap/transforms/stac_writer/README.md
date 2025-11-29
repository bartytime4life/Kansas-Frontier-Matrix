---
title: "📦 NASA SMAP — STAC Writer Stage (STAC v1.0 · DCAT v3 · PROV-O) · ETL Finalization Layer"
path: "docs/data/satellites/smap/transforms/stac_writer/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · STAC/DCAT Review Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public ETL Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R5"
care_label: "CARE-A / CARE-B (Final governed stage)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "STAC/DCAT Review Board · FAIR+CARE Council · Earth Systems Working Group"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../schemas/json/transform-smap-stac-writer-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/transform-smap-stac-writer-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transform:stac-writer-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transform-stac-writer"
event_source_id: "ledger:docs/data/satellites/smap/transforms/stac_writer/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next STAC/DCAT schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — STAC Writer Stage (Final ETL Layer)**  
`docs/data/satellites/smap/transforms/stac_writer/README.md`

**Purpose**  
Define the **final ETL stage** for NASA SMAP inside KFM — the generation of  
**STAC v1.0 Items + Collections**, **DCAT v3 Records**, **JSON-LD metadata**, and  
**full PROV-O lineage**, with all **CARE/H3 sovereignty restrictions** applied.

This stage produces the **authoritative public-facing data objects** for SMAP inside KFM.

</div>

---

## 📘 1. Overview

The STAC Writer stage:

- 📦 Builds STAC **Collections** for SMAP domains:
  - Soil Moisture  
  - Freeze–Thaw  
  - Vegetation Water Content  
  - QA/RFI  
  - Uncertainty  
  - Ancillary Metadata  

- 🗂 Produces STAC **Items** per time slice / tile  
- 🌐 Writes **DCAT v3 Dataset & Distribution** metadata  
- 🔗 Adds **PROV-O lineage graphs**  
- 🔐 Applies **final governance metadata**  
- ⚠️ Ensures *no prohibited precision* or *forbidden metadata* leaks  
- 📤 Exports final data assets (COGs, JSON-LD, QA flags, uncertainty rasters, mask rasters)

This is the **final gate** before KFM publishes SMAP-derived data.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/stac_writer/
├── 📄 README.md                           # This file
│
├── 🧩 build_collection.py                  # Builds STAC Collections (v1.0)
├── 🧩 build_items.py                       # Builds STAC Items from ETL outputs
├── 📚 stac_templates/                      # STAC JSON templates
│   ├── collection_template.json
│   ├── item_template.json
│   ├── asset_template.json
│   └── provenance_template.json
│
├── 🔐 governance_extension.json            # KFM governance STAC extension (CARE/H3)
├── 🧭 dcat_writer.py                       # DCAT v3 metadata generation
├── 🧾 prov_writer.py                       # PROV-O JSON-LD lineage generator
│
└── 🧪 tests/                                # STAC Writer test suite
    ├── test_collection_build.py
    ├── test_item_build.py
    ├── test_governance_metadata.py
    ├── test_stac_schema_compliance.py
    └── fixtures/
        ├── sample_processed_raster.tif
        ├── sample_qa_mask.tif
        ├── sample_uncertainty.tif
        ├── sample_governance_metadata.json
        └── expected_stac_item.json
~~~

---

## 🧩 3. Responsibilities of the STAC Writer

### 📦 STAC Collections
- Write fully validated **STAC v1.0 Collections**  
- Include fields:
  - `extent.spatial`
  - `extent.temporal`
  - `summaries`
  - `stac_extensions`
  - Projection & raster metadata  
  - Governance extension fields  

### 🗂 STAC Items
- Create Items with:
  - geometry + bbox  
  - datetime / start_datetime / end_datetime  
  - assets (COG rasters, masks, uncertainty)  
  - QA metadata  
  - CARE/H3 metadata  
  - PROV-O lineage  
  - Links to parent Collection  

### 🔐 Governance Extension
Adds mandatory governance metadata:
- `kfm:care_label`  
- `kfm:h3_sensitive`  
- `kfm:mask_required`  
- `kfm:sovereignty_uncertainty_floor`  
- `kfm:governance_notes`  

### 🧬 Uncertainty Metadata
- Uncertainty type  
- Floor rules  
- Model version  
- Link to uncertainty assets  

### 📡 QA Integration
- Add QA interpretation fields  
- Include QA masks as assets  
- Populate `kfm:qa_values` + `kfm:qa_confidence_score`  

### 🧾 PROV-O Lineage
- `prov:wasGeneratedBy`
- `prov:used`
- `prov:wasDerivedFrom`
- `prov:atLocation`

### 📘 DCAT Metadata
Generates:
- Dataset → Distribution metadata  
- JSON-LD structured data  
- License, rights, data stewardship  

### 🛡 Final Safety Checks
- Sovereignty masking must be applied  
- No unmasked values remain  
- CARE labels must match previous ETL stage  
- Temporal + spatial fields must be validated  
- All STAC Schema validations must pass  

---

## 🔐 4. Governance & FAIR+CARE Integration

STAC Writer stage must ensure:

- No sensitive geolocation leaks  
- All masking is respected  
- Uncertainty floors correctly represented  
- CARE labels preserved  
- Sovereignty flags included  
- All governance changes logged in PROV  
- All exports ethically safe  

Governance validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. QA & Validation

The STAC Writer is tested for:

- STAC v1.0 schema validity  
- DCAT v3 conformance  
- Projection and raster extension correctness  
- Governance extension correctness  
- Lineage accuracy  
- Deterministic asset ordering  
- Stability across runs  

Telemetry logs record all validation data.

---

## 🔁 6. Position in the Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC Writer (FINAL STAGE)
 → STAC/DCAT publishing
 → PROV-O + OpenLineage archival
~~~

This stage produces the **publishable, governed, lineage-complete dataset**.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Official, governed soil-moisture STAC archives.

### Climate  
Reliable FT + VWC anomaly STAC surfaces.

### Archaeology  
Governed environmental layers for Story Nodes.

### Story Node v3  
Direct links to temporal OK-event contexts & environmental layers.

### Focus Mode v3  
Governance-safe environmental layers used in reasoning.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First complete STAC Writer README; fully governed; STAC/DCAT/PROV aligned; emoji layout; CI-safe. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 STAC Writer Tests](../README.md) · [🛡 Governance Standards](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

