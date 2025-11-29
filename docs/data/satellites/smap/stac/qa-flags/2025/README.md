---
title: "⚠️ NASA SMAP — QA / RFI Flags STAC Items for 2025 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/qa-flags/2025/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-qa-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B (depending on location & context)"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (interpretive QA effects)"
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

json_schema_ref: "../../../../../../../schemas/json/stac-smap-qa-v11.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/stac-smap-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:qa-flags:2025:readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-qa-2025"
event_source_id: "ledger:docs/data/satellites/smap/stac/qa-flags/2025/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next QA-layer revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ⚠️ **NASA SMAP — QA / RFI Flags STAC Items (Year 2025)**  
`docs/data/satellites/smap/stac/qa-flags/2025/README.md`

**Purpose**  
Document the **2025 SMAP QA/RFI Flags** STAC Items, which represent  
per-day radiometer quality, confidence codes, surface-condition flags, and  
RFI interference indicators, used across all SMAP-derived products in KFM  
(soil moisture, freeze–thaw, VWC).  
Fully aligned with **KFM-STAC v11**, FAIR+CARE, sovereignty governance, and  
OpenLineage/telemetry instrumentation.

</div>

---

## 📘 1. Overview

The **QA / RFI STAC Items for 2025** contain:

- ⚠️ **Radiometer performance flags**  
- 📡 **RFI contamination indicators**  
- ❄️ **Freeze-line interference codes**  
- 🌱 **Soil-state interaction flags (soil moisture consistency)**  
- 🌿 **Vegetation-water confidence flags**  
- 📉 **Uncertainty multipliers**  
- 🧾 **Orbit/grid/calibration metadata**  

These Items are critical for:

- Interpreting soil moisture quality  
- Identifying suspect freeze/thaw transitions  
- Detecting canopy interference  
- Downstream application of masks in hydrology & archaeology ETL  
- Filtering anomalies from Story Node v3 + Focus Mode v3 narratives  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/qa-flags/2025/
├── 📄 README.md                         # This file
│
├── 📅 2025-01-01-item.json              # Daily QA/RFI STAC Items
├── 📅 2025-01-02-item.json
├── 📅 2025-01-03-item.json
├── 📅 ...                                # All days for 2025
│
└── 🗃️ assets/                            # Shared asset directory (all 2025 Items pull from here)
    ├── ⚠️ qa-flags.tif                   # QA/RFI mask raster
    ├── 📈 qa-uncertainty.tif             # QA uncertainty / reliability indicators
    └── 🧾 metadata.json                  # Orbit/grid/provenance metadata
~~~

All Item filenames follow the required pattern:  
**`YYYY-MM-DD-item.json`**

---

## 🧩 3. STAC Item Requirements (KFM-STAC v11)

Every 2025 QA/RFI STAC Item MUST include:

### Core Fields
- `"type": "Feature"`  
- `"id": "smap-qa-2025-<date>"`  
- `"collection": "smap-qa-flags"`  
- Valid `geometry` + `bbox`  
- `properties.datetime` (ISO 8601)  
- `kfm:qa_values` (coded legend reference)  
- `kfm:qa_flag_schema`  
- `kfm:care_label`  
- `kfm:sovereignty_note`  
- `kfm:mask_applied` (if H3 generalization applies)  
- `kfm:uncertainty` (if present from SMAP retrieval pipeline)  
- `kfm:lineage` (PROV-O derivation chain)

### Required Assets
- **`qa`** → QA/RFI mask raster  
- **`uncertainty`** → QA-related uncertainty layer  
- **`metadata`** → orbit/grid/provenance JSON  

### Required Extensions
- `proj`  
- `raster`  
- `sat`  
- `kfm-gov`  
- `kfm-qa`  
- `kfm-provenance`  

---

## 🔐 4. Governance & Sovereignty Considerations

QA/RFI masks can reveal:

- soil/vegetation stress under certain conditions  
- anomaly clusters near culturally protected regions  
- sensor behavior that correlates with land-state transitions  

KFM requires:

- **CARE-A/B classification**  
- **H3 masking** in sensitive Indigenous territories  
- `"kfm:mask_applied": true` where active  
- Full provenance + uncertainty disclosure  
- Governing validation via:
  - `faircare_validate.yml`
  - `stac_validate.yml`
  - `jsonld_validate.yml`
  - `data_pipeline.yml`

---

## 🧪 5. QA & Validation

Each STAC Item undergoes:

- JSON Schema validation  
- Raster/COG structural validation  
- Geometry + BBox checks  
- Temporal consistency  
- QA consistency with:
  - SMAP soil moisture  
  - SMAP freeze/thaw  
  - SMAP VWC  
  - Mesonet & ERA5 freeze/soil/vegetation indicators  

QA results live in:

`docs/data/satellites/smap/qa/`

Telemetry exported to:

`releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion → Lineage Pipeline (2025)

```
NASA SMAP L3 QA/RFI Product
 → decode + map to EASE-Grid
 → integrate radiometer QA + RFI classifications
 → propagate QA uncertainty
 → assemble STAC Item
 → CARE/H3 governance enforcement
 → register (STAC / DCAT)
 → export PROV-O lineage
 → emit OpenLineage + OTel telemetry
```

---

## 🔮 7. Applications Inside KFM

### Hydrology
- Soil moisture reliability filters  
- Floodplain anomaly suppression  

### Climate
- Freeze/thaw boundary QA checks  
- Vegetation-water stress analysis  

### Archaeology
- Noise-aware wetness/vegetation trends  
- Reduced risk of misinterpreting environmental conditions  

### Story Node v3
- Context-aware uncertainty descriptors  
- Ethical filtering of low-confidence environmental claims  

### Focus Mode v3
- Reliability-aware environmental context blocks  
- Suppression of misleading anomalies near sensitive regions  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full year-level QA/RFI STAC README; emoji layout; CARE/H3 rules; STAC v11 compliance; CI-safe.      |
| v10.3.2 | 2025-11-14 | Early pre-v11 structure.                                                                             |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ QA Flags STAC](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

