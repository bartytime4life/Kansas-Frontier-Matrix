---
title: "🛰️ NASA SMAP — STAC Collections & Items (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-stac-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A / CARE-B depending on variable"
classification: "Public Dataset Overview"
indigenous_rights_flag: true
risk_category: "Low"
redaction_required: false
sensitivity_level: "Low (raw) / Medium (derived)"
public_exposure_risk: "Low"

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/stac-smap-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/stac-smap-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:stac:readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-stac"
event_source_id: "ledger:docs/data/satellites/smap/stac/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next STAC schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **NASA SMAP — STAC Collections & Items (KFM v11.2.2)**  
`docs/data/satellites/smap/stac/README.md`

**Purpose**  
Document the **STAC Collections + Items** for NASA SMAP within the Kansas Frontier Matrix,  
aligned with **KFM-STAC v11**, FAIR+CARE governance, OpenLineage lineage,  
and multi-mission hydrology/climate interoperability.

</div>

---

## 📘 1. Overview

This directory contains the **entire SMAP STAC hierarchy**, including:

- 🌱 **Soil moisture (L2/L3)**  
- ❄️ **Freeze–thaw (L3_FT)**  
- 🌿 **Vegetation water content**  
- ⚠️ **Quality flags & uncertainty**  
- 📚 **Ancillary orbit & grid metadata**  

All Items and Collections are:

- 🌐 STAC 1.x compliant  
- 🧬 JSON-LD enriched (schema.org + GeoSPARQL + OWL-Time)  
- 🧾 DCAT v3 compatible  
- 🧱 PROV-O tracked (derivation chains)  
- 🛡 CARE-governed (H3 masking where needed)  
- 📦 Stored as Cloud-Optimized GeoTIFF (COG) or Zarr/NetCDF (when available)  

These STAC assets power:

- KFM hydrology ETL  
- Drought & freeze-line modeling  
- Story Node v3 temporal-spatial layers  
- Focus Mode v3 contextual “environmental background”  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/
├── 📄 README.md                          # This file
│
├── 🌱 soil-moisture/                     # SMAP L2/L3 soil moisture STAC Items
│   ├── collection.json                   # Soil moisture STAC Collection
│   ├── YYYY/                             # Year folders
│   │   └── YYYY-MM-DD-item.json          # Daily/3-day Items
│   └── assets/                           # COGs, QA masks, uncertainty layers
│
├── ❄️ freeze-thaw/                       # Freeze/Thaw STAC
│   ├── collection.json
│   ├── YYYY/
│   │   └── item.json                     # Daily FT state
│   └── assets/
│
├── 🌿 vegetation-water/                  # Vegetation water content
│   ├── collection.json
│   ├── YYYY/
│   │   └── item.json
│   └── assets/
│
├── ⚠️ qa-flags/                           # QA layers (radiometer quality, gain, RFI)
│   ├── collection.json
│   ├── flags-legend.json                 # QA codebook
│   └── assets/
│
└── 📚 ancillary/                         # Ancillary orbit, grid metadata, calibration notes
    ├── ease-grid-2.0.json
    ├── orbit-tracks.json
    └── radiometer-modes.json
~~~

---

## 🧩 3. KFM-STAC v11 Requirements

### ✔ Required Fields in Each Item

- `id` — unique ID (mission + grid + date)  
- `type: "Feature"`  
- `geometry` — polygon or global swath  
- `bbox` — required for all Items  
- `properties.datetime` or `properties.start_datetime` + `end_datetime`  
- `providers` — NASA, KFM  
- `kfm:governance` — CARE label + sovereignty flags  
- `kfm:uncertainty` — sensor + processing uncertainty  
- `kfm:lineage` — PROV-O compliant  

### ✔ Required Asset Roles

- `data` (COG or NetCDF/Zarr)  
- `qa` (Quality flags)  
- `uncertainty`  
- `metadata` (text/json)  

### ✔ CARE + Sovereignty

KFM enforces:

- **CARE-A/B labeling** for all STAC Items intersecting tribal lands  
- **H3 masking/generalization** for:
  - wetness anomalies  
  - vegetation water content  
  - freeze–thaw transitions  
- Items must include:
  - `kfm:care_label`
  - `kfm:sovereignty_note`
  - H3 resolution used for generalization

---

## 🧪 4. Validation & QA

All SMAP STAC data must pass:

- **JSON Schema validation**  
- **KFM-STAC v11 structural conformance**  
- **GeoJSON geometry checks** (multi-polygon validity)  
- **BBox match to geometry**  
- **Temporal validity** (OWL-Time)  
- **CARE + sovereignty rule enforcement**  
- **Cross-mission QA** against:
  - HydroGNSS  
  - Mesonet soil moisture  
  - NOAA NCEI drought indices  

QA reports are placed in:

`docs/data/satellites/smap/qa/`

Telemetry for validation is exported to:

`releases/<version>/data-telemetry.json`

---

## 🔁 5. Ingestion & Lineage

Each STAC Item is generated by the SMAP ingestion chain:

```
NASA SMAP L2/L3  
   → Decode & geolocation  
   → Grid harmonization (EASE-Grid ↔ KFM CRS)  
   → QA mask application  
   → STAC creation  
   → CARE/H3 governance checks  
   → Lineage export (PROV-O)  
   → Catalog registration  
```

All steps emit **OpenLineage v2.5** events for auditability.

---

## 🔮 6. Usage in KFM

### Hydrology
- Soil moisture model inputs  
- Floodplain wetness detection  
- Drought stress analysis  

### Climate
- Long-term anomaly analysis  
- Freeze-line migration trends  

### Archaeology
- Wetness patterns along historical settlement routes  
- Vegetation water content → site visibility assessment  
- Freeze–thaw cycles → erosion risk indicators  

### Story Node v3 & Focus Mode v3
- Contextual “environment backdrop” layers  
- Time-aligned moisture/freeze states  
- Spatial narratives correlated with archaeological or historical events  

---

## 🧭 7. Version History

| Version | Date       | Summary                                                                                       |
|--------:|------------|-----------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full v11.2.2 upgrade; added emoji layout, CARE/H3 metadata rules, STAC v11 validation model. |
| v10.3.2 | 2025-11-14 | Pre-v11 skeletal STAC listing.                                                                |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ Satellite Catalog](../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

