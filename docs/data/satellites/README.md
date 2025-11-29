---
title: "🛰️ Kansas Frontier Matrix — Satellite Data Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/satellites-v11.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

doc_kind: "Dataset Group Overview"
intent: "satellite-data-overview"
role: "data-layer"
category: "Satellite · Climate · Hydrology · Land Systems"

classification: "Public Dataset Overview"
fair_category: "F1-A1-I2-R2"
care_label: "CARE-A / CARE-B (depending on derived layers)"
sensitivity_level: "Low-to-Moderate (depending on variable)"
indigenous_rights_flag: true
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false
data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  prov_o: "prov:Collection"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/satellite-group-overview-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/satellite-group-overview-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:satellites:readme:v11.2.2"
semantic_document_id: "kfm-doc-data-satellites-overview"
event_source_id: "ledger:docs/data/satellites/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next v11.x satellite-catalog revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Satellite Observation Layers (v11.2.2)**  
`docs/data/satellites/README.md`

### Multi-Mission Water, Soil, Vegetation, Hazard, & Land-System Observations  
### ESA · NASA · NOAA · JAXA · EU Copernicus · Commercial Constellations

</div>

---

## 📌 Purpose

This directory provides the **complete satellite data domain** for the Kansas Frontier Matrix (KFM), covering:

- Water-cycle dynamics  
- Surface moisture  
- Freeze/thaw and snow  
- Inundation & wetlands  
- Vegetation & biomass  
- Thermal anomalies  
- Surface change & hazards  
- Land-use & ecological transitions  

All satellite datasets here are:

- Harmonized under **KFM-STAC v11**  
- Indexed as **DCAT v3** datasets  
- Tracked with **PROV-O** lineage  
- Inspected under **FAIR+CARE** & sovereignty governance  
- Mapped into **Story Node v3** and **Focus Mode v3** narrative layers  

This directory forms the **remote-sensing backbone** of the KFM knowledge system.

---

## 🌎 Major Satellite Missions Integrated Into KFM

### **🛰️ ESA & SSTL**
- **HydroGNSS (GNSS-R)**
  - Soil moisture, inundation, freeze/thaw, biomass  
  - All-weather, vegetation-penetrating water-cycle sensing  

- **Sentinel-1 (C-SAR)**  
  - Flood detection, soil moisture, surface deformation  

- **Sentinel-2 (MSI)**  
  - Vegetation, land cover, wetlands, archaeology features  

### **🛰️ NASA**
- **SMAP (L-band radiometer + SAR)**  
  - Soil moisture, freeze/thaw  

- **Landsat 5–9**  
  - Long-term land cover, thermal anomalies, wetland change  

- **GEDI (LiDAR)**  
  - Biomass & canopy structure (where available)  

### **🛰️ NOAA**
- **GOES-East/West**  
  - Cloud motion fields, thermal anomalies, drought monitoring  

- **VIIRS (Suomi-NPP/NOAA-20)**  
  - Nighttime lights, fire & thermal hotspots, NDVI  

### **🛰️ Copernicus / EU**
- **Sentinel-3 (OLCI/SLSTR)** — Ocean & land color, surface temp  
- **Sentinel-5P (TROPOMI)** — Atmospheric gases, pollution  

### **🛰️ Commercial & Open Constellations**
- PlanetScope (where licensed)  
- Harmonized Landsat/Sentinel (HLS)  
- ECOSTRESS (thermal stress)  

All missions undergo the same **governed ingestion + STAC harmonization workflow**.

---

## 🗂️ Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/
├── 📄 README.md                         # Satellite overview (this file)
│
├── 🛰️ hydrognss/                        # ESA HydroGNSS (GNSS-R water-cycle variables)
├── 🛰️ smap/                             # NASA SMAP soil moisture + freeze/thaw
├── 🛰️ sentinel-1/                       # SAR flood detection + surface deformation
├── 🛰️ sentinel-2/                       # MSI vegetation, NDVI/EVI, archaeology features
├── 🛰️ sentinel-3/                       # OLCI/SLSTR ocean + land color + temp
├── 🛰️ sentinel-5p/                      # Atmospheric gas verticals (NO₂, O₃, CH₄)
├── 🛰️ landsat/                          # Landsat 5–9 long-term land-change archive
├── 🛰️ viirs/                            # NOAA VIIRS thermal + nighttime lights + fires
├── 🛰️ goes/                             # GOES cloud motion / drought / thermal anomalies
├── 🛰️ hls/                              # Harmonized Landsat–Sentinel (HLS)
└── 🧷 common/                            # Shared utilities, metadata, QA rules, ingestion notes
~~~

All mission subdirectories contain:

- **STAC collections**  
- **DCAT metadata**  
- **PROV-O lineage**  
- **QA reports**  
- **Integration rules**  
- **Sample assets**  

---

## 🧩 KFM Satellite Integration Standards

### ✔ **KFM-STAC v11 Compliance**
All satellite missions conform to the KFM STAC schema:

- Geometry footprints  
- Time intervals (OWL-Time compliant)  
- Asset roles (primary, QA, uncertainty, auxiliary)  
- License + FAIR/CARE metadata  
- Sovereignty/H3 masking where required  

### ✔ **DCAT v3 Dataset Registry**
Each mission is listed in the **KFM Data Catalog**, enabling:

- Discoverability  
- Automated ETL linkages  
- Metadata-based filtering (domain, spatial, temporal)  

### ✔ **PROV-O Lineage**
Every satellite dataset includes:

- `prov:used` (raw product ID, mission, orbit)  
- `prov:wasGeneratedBy` (KFM transformation pipeline)  
- Cross-sensor linkages (e.g., HydroGNSS ↔ SMAP ↔ Mesonet)  

### ✔ **FAIR+CARE Enforcement**
Satellite layers touching sensitive context (wetlands, biomass, land-use change) use:

- **CARE labels**  
- Dynamic **H3 masking**  
- Clear **governance flags** in STAC/DCAT  
- Lineage + consent flags for Indigenous territories  

---

## 🛠️ Shared Ingestion Framework

All missions follow a unified ETL pattern:

1. Detect new upstream release  
2. Stage → validate → geolocate  
3. Extract variables (GNSS-R, SAR, radiometry, optical, thermal, etc.)  
4. Generate **STAC Items + Collections**  
5. Apply QA flags, uncertainty metrics  
6. Produce PROV-O lineage  
7. Perform cross-sensor comparisons  
8. Export telemetry (energy/carbon/compute cost)  
9. Register dataset in:
   - `data/stac/catalog.json`
   - `docs/data/metadata/**` (DCAT)

All steps are **OpenLineage-instrumented** and reproducible.

---

## 🔮 Uses Inside KFM

### 🏞️ Environment & Hydrology  
- Soil moisture + drought analyses  
- Flood detection & wetland change  
- Freeze–thaw hazard modeling  
- Surface water persistence  

### 🏺 Archaeology & Cultural Landscape  
- Biomass + vegetation transitions  
- Hidden feature detection (Sentinel-2, Landsat, GNSS-R wetness anomalies)  
- Terrain visibility & access  
- Wetland reactivation over heritage corridors  

### 🌾 Ecology & Land Systems  
- NDVI trends  
- Fire scars (VIIRS/Landsat)  
- Grassland/plains dynamics  
- Invasive species monitoring  

### 🌪 Hazards  
- Thermal hotspots  
- Soil moisture preconditioning (flood/hail/severe weather drivers)  
- Land surface anomalies tied to severe storm damage  

---

## 🔐 Governance & Sovereignty

Satellite data itself is usually open, but **derived layers may not be**.

KFM enforces:

- **CARE-A & CARE-B labels** where applicable  
- **H3-based masking/generalization** for:
  - wetlands  
  - biomass  
  - inundation  
  - land-use transitions  
- Full lineage tracking: no orphaned spatial derivatives  
- Strict handling of imagery near culturally sensitive landscapes  

All derived layers used in **Focus Mode v3** must carry:

- Source mission  
- Processing chain  
- Uncertainty  
- Sovereignty notes  

---

## 🧭 Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete rewrite; emoji directory added; governance/H3 upgrades; fully aligned with KFM-MDP v11.2.2. |
| v10.4.0 | 2025-11-15 | Earlier satellite overview; pre-v11 metadata structure.                                           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../../README.md) · [🗂️ Data Catalog](../../README.md) · [🛡 Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>

