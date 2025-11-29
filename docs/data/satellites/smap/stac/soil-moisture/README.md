---
title: "🌱 NASA SMAP — Soil Moisture STAC Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/soil-moisture/README.md"
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

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-smap-soil-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Overview"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-A / Indigenous Sensitivity Reviewed"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../schemas/json/stac-smap-soil-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/stac-smap-soil-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:soil-moisture:stac-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-stac-soil"
event_source_id: "ledger:docs/data/satellites/smap/stac/soil-moisture/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next SMAP soil-moisture STAC revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌱 **NASA SMAP — Soil Moisture STAC Collection (KFM v11.2.2)**  
`docs/data/satellites/smap/stac/soil-moisture/README.md`

**Purpose**  
Document the **Soil Moisture STAC Collection + Items** for NASA SMAP within KFM.  
This is the **primary water-cycle surface wetness dataset** supporting KFM drought,  
hydrology, land-surface, archaeology, and Focus Mode v3 environmental context layers.

</div>

---

## 📘 1. Overview

This subdirectory contains the **daily / 3-day SMAP Soil Moisture** STAC assets used by KFM:

- 🌱 **Surface Soil Moisture (0–5 cm)**  
- 🌿 Vegetation water impact metadata  
- ❄️ Freeze/thaw interaction indicators (cross-linked only)  
- ⚠️ QA & RFI contamination flags  
- 📉 Uncertainty & error-budget layers  

All Items are:

- 🧩 STAC 1.x compliant  
- 🧬 JSON-LD enriched (CIDOC, OWL-Time, GeoSPARQL)  
- 🧱 PROV-O lineage mapped  
- 🛡 CARE-aligned with sovereignty/H3 masking  
- 🛰 Geolocated on **EASE-Grid 2.0** → projected to KFM CRS where needed  
- 📦 Stored as **Cloud-Optimized GeoTIFF (COG)**  

These Items feed hydrology ETL, KFM climate baselines, Story Node v3 layers,  
Focus Mode v3 drought narratives, and cross-mission fusion (HydroGNSS, Mesonet, NCEI, ERA5).

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/soil-moisture/
├── 📄 README.md                      # This file
│
├── 📦 collection.json                # SMAP Soil Moisture STAC Collection
│
├── 📅 2025/                          # Year folder (example)
│   ├── 2025-01-01-item.json          # Daily SMAP STAC Item
│   ├── 2025-01-02-item.json
│   └── ...                           # One Item per day or 3-day composite
│
└── 🗃️ assets/                        # COGs, QA masks, uncertainty layers
    ├── soil-moisture.tif             # Primary radiometer product
    ├── soil-moisture-uncertainty.tif # Uncertainty estimates
    ├── qa-flags.tif                  # RFI + sensor quality masks
    └── metadata.json                 # Sensor/orbit metadata, processing notes
~~~

All filenames are **schema-validated** and follow the KFM-STAC v11 naming rules.

---

## 🧩 3. STAC Collection Specification (KFM-STAC v11)

The `collection.json` for soil moisture MUST contain:

### Required Fields

- `"type": "Collection"`  
- `"id": "smap-soil-moisture"`  
- `"title": "NASA SMAP Soil Moisture (L2/L3)"`  
- Spatial extent: global  
- Temporal extent: mission lifetime (2015-01-01 → present)  
- `"kfm:governance"` block:  
  - CARE label(s)  
  - Sovereignty & H3 masking metadata  
- `"kfm:lineage"` block:  
  - NASA source product ID  
  - Processing chain references  
  - QA lineage  
- `"assets"` for:
  - product documentation  
  - calibration tables  
  - grid metadata (EASE-Grid 2.0)  

### Required Extensions

- `proj` — projection metadata  
- `raster` — COG metadata  
- `sat` — orbit/attitude metadata (where available)  
- `kfm-gov` — CARE/H3 lineage & governance  
- `kfm-qa` — QA flag extension  
- `kfm-provenance` — PROV-O alignment

---

## 🧩 4. STAC Item Specification (Daily / 3-Day Items)

Each Item in this directory MUST include:

### Core Fields

- `id`: `"smap-soil-YYYY-MM-DD"`  
- `type: "Feature"`  
- `geometry` + `bbox`  
- `properties.datetime` or interval (`start_datetime`, `end_datetime`)  
- `kfm:unit`: `"m3/m3"`  
- `kfm:uncertainty`: numeric ± bands  
- `kfm:qa_flags`: coded mask applied  
- `kfm:care_label` & `kfm:sovereignty_note`  

### Required Assets

- **`data`** → soil moisture COG  
- **`uncertainty`** → uncertainty COG  
- **`qa`** → quality flags  
- **`metadata`** → ancillary orbit/grid metadata  

### Masking Requirements

If the Item intersects sensitive tribal land:

- H3 generalization to approved resolution  
- No precise anomaly display in derived interactive layers  
- Explicit `"kfm:mask_applied": true`  

---

## 🧪 5. QA & Validation

All Items are tested using:

- JSON Schema validation  
- Geometry validity tests (anti-meridian, MultiPolygon sanity checks)  
- BBox consistency  
- Temporal extent validity  
- CARE/H3 governance tests  
- Raster/COG integrity tests  
- Cross-sensor QA vs:
  - HydroGNSS  
  - Mesonet  
  - NOAA/ERA5  

Results logged in:  
`docs/data/satellites/smap/qa/`

Telemetry exported to:  
`releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion Lineage

All Items export PROV-O describing:

```
NASA SMAP L2/L3 Product
  → decode + geolocation
  → grid harmonization (EASE-Grid 2.0 ↔ KFM CRS)
  → QA mask integration
  → STAC Item assembly
  → CARE/H3 governance check
  → Catalog registration
```

Each step emits OpenLineage events.

---

## 🔮 7. Usage in KFM

### Hydrology
- Floodplain wetness  
- Drought evolution  
- Soil infiltration models  

### Climate
- Seasonal anomalies  
- Freeze-line comparison (via cross links)  

### Archaeology
- Hydrological context for cultural landscapes  
- Biomass & land-use interpretation  

### Story Node v3 / Focus Mode v3
- Temporal-spatial context overlays  
- Environmental “background state”  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                          |
|--------:|------------|--------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First full STAC soil-moisture README; added emoji layout, governance, CARE/H3 rules, STAC v11.2. |
| v10.3.2 | 2025-11-14 | Early pre-v11 STAC structure (minimal).                                                          |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ SMAP STAC Home](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

