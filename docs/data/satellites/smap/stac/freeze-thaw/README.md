---
title: "❄️ NASA SMAP — Freeze/Thaw STAC Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/freeze-thaw/README.md"
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

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-freeze-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Overview"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-A / CARE-B depending on intersection"
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

json_schema_ref: "../../../../../schemas/json/stac-smap-freeze-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/stac-smap-freeze-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:freeze-thaw:stac-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-freeze-thaw"
event_source_id: "ledger:docs/data/satellites/smap/stac/freeze-thaw/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next SMAP freeze/thaw revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ❄️ **NASA SMAP — Freeze/Thaw STAC Collection (KFM v11.2.2)**  
`docs/data/satellites/smap/stac/freeze-thaw/README.md`

**Purpose**  
Document the **Freeze/Thaw STAC Collection + Items** for NASA SMAP within the Kansas Frontier Matrix (KFM).  
This dataset provides **global freeze/thaw state detection** at L-band microwave frequencies,  
supporting ecohydrology, hazard modeling, soil dynamics, Story Node v3 layers,  
and Focus Mode v3 environmental context.

</div>

---

## 📘 1. Overview

This directory contains all **SMAP Freeze/Thaw (FT) STAC assets**, including:

- ❄️ **Ground freeze state**  
- 🌿 **Thaw onset & offset timing**  
- 🌱 Soil moisture transitions linked via cross-product QA  
- 🔧 Radiometric QA & RFI flags  
- 📉 Uncertainty and error-budget layers  
- 📚 Ancillary orbit, grid, & calibration metadata  

All Items are:

- STAC 1.x compliant  
- JSON-LD enriched (CIDOC, GeoSPARQL, OWL-Time)  
- PROV-O lineage tracked  
- Subject to CARE-A/B & H3 sovereignty masking  
- Geolocated on **EASE-Grid 2.0**  
- Stored as **COG (Cloud-Optimized GeoTIFF)**  

Freeze/thaw is a **core seasonal indicator** used by KFM for:

- Hydrologic modeling
- Surface process hazards  
- Archaeological landscape access  
- Vegetation/land-use interpretation  
- Story Node v3 “environmental transition” narratives  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/freeze-thaw/
├── 📄 README.md                         # This file
│
├── 📦 collection.json                   # SMAP Freeze/Thaw STAC Collection
│
├── 📅 2025/                              # Example year directory
│   ├── 2025-01-01-item.json             # Daily FT state
│   ├── 2025-01-02-item.json
│   └── ...                              # Daily Items for whole year
│
└── 🗃️ assets/                           # Common assets for FT Items
    ├── ❄️ freeze-thaw.tif               # Freeze/thaw raster
    ├── ⚠️ qa-flags.tif                  # RFI + quality mask
    ├── 📈 freeze-uncertainty.tif        # Uncertainty surface
    └── 🧾 metadata.json                 # Orbit/grid/provenance metadata
~~~

---

## 🧩 3. STAC Collection Specification (KFM-STAC v11)

The Freeze/Thaw **collection.json** MUST include:

- `"type": "Collection"`  
- `"id": "smap-freeze-thaw"`  
- `"title": "NASA SMAP Freeze/Thaw (FT)"`  
- Spatial extent: global  
- Temporal extent: 2015 → present  
- `kfm:governance`: CARE label + sovereignty metadata  
- `kfm:lineage`: ESA/NASA product IDs + processing chain  
- Assets:
  - documentation  
  - calibration tables  
  - grid metadata (EASE-Grid)  
- Extensions required:
  - `raster`  
  - `proj`  
  - `sat`  
  - `kfm-gov`  
  - `kfm-provenance`  
  - `kfm-qa`  

---

## 🧩 4. STAC Item Specification (Daily Items)

Each Freeze/Thaw Item MUST include:

### Required Fields

- `"type": "Feature"`  
- `"id": "smap-ft-YYYY-MM-DD"`  
- `geometry` + `bbox`  
- `properties.datetime`  
- `kfm:state`: `"frozen"` / `"thawed"` / `"transition"`  
- `kfm:uncertainty`: numeric or band-provided  
- `kfm:qa_flags`  
- `kfm:care_label`  
- `kfm:sovereignty_note`  
- `kfm:mask_applied` (if H3 generalization used)  

### Required Assets

- **`data`** → freeze/thaw raster  
- **`qa`** → QA/RFI mask raster  
- **`uncertainty`** → uncertainty raster  
- **`metadata`** → calibration/orbit metadata  

---

## 🔐 5. Governance & Sovereignty

SMAP FT layers intersect:

- Indigenous territories  
- Culturally significant lands  
- Ecologically sensitive landscapes  

Therefore:

- CARE-A/B rules apply  
- Dynamic H3 masking MUST be applied in sensitive areas  
- No precise freeze-line anomalies in sensitive regions  
- All derived freeze-thaw transitions must surface:
  - CARE label  
  - sovereignty status  
  - uncertainty context  

Governance validation is enforced via:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 6. QA & Validation

All Items undergo:

- JSON Schema validation  
- Raster/COG integrity checks  
- Geometry/BBox validation  
- Temporal plausibility checks  
- QA/RFI mask verification  
- Cross-sensor QA with:
  - SMAP soil moisture  
  - HydroGNSS freeze indicators  
  - Mesonet freeze data  
  - ERA5 land-surface models  

QA outputs stored at:

`docs/data/satellites/smap/qa/`

Telemetry exported to:

`releases/<version>/data-telemetry.json`

---

## 🔁 7. Ingestion → Lineage Workflow

```
NASA SMAP L3_FT Product
 → decode + EASE-Grid transform
 → QA + RFI mask integration
 → freeze/thaw state extraction
 → STAC Item assembly
 → CARE/H3 sovereignty review
 → lineage export (PROV-O)
 → catalog registration
 → OpenLineage telemetry emission
```

---

## 🔮 8. Applications Inside KFM

### Hydrology
- Freeze-line migration  
- Spring runoff modeling  
- Ecohydrology transitions  

### Climate
- Seasonal freeze–thaw anomaly detection  
- Long-term climate regime change indicators  

### Archaeology
- Freeze–thaw erosion risk  
- Accessibility & land-use seasonality  
- Landscape hazard interpretation  

### Story Node v3 + Focus Mode v3
- Environmental transition context  
- Seasonal backdrop for historical timelines  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full v11.2.2 upgrade; emoji layout; governance & H3 masking; STAC v11 alignment; telemetry hooks.   |
| v10.3.2 | 2025-11-14 | Pre-v11 skeleton.                                                                                    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ SMAP STAC Home](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

