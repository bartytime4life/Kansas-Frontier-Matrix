---
title: "🛰️ KFM v11.2 — ESA HydroGNSS Water-Cycle Observation Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/hydrognss/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sat-hydrognss-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A / Indigenous Data Sensitivity Reviewed"
doc_kind: "Dataset Overview"
intent: "hydrognss-overview"
role: "data-layer"
category: "Satellites · Climate · Hydrology"

classification: "Public Dataset Overview"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/dataset-hydrognss-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/dataset-hydrognss-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:hydrognss:readme:v11.2.2"
semantic_document_id: "kfm-doc-data-hydrognss-overview"
event_source_id: "ledger:docs/data/satellites/hydrognss/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded by next HydroGNSS integration revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **ESA HydroGNSS — Water-Cycle Observations for KFM**  
`docs/data/satellites/hydrognss/README.md`

### Soil Moisture • Inundation • Freeze/Thaw • Biomass  
### GNSS-R → Reflected GNSS Signals → Climate & Hydrology Insights

</div>

---

## 📌 Purpose

This directory documents the **HydroGNSS satellite data integration layer** for the Kansas Frontier Matrix (KFM).

HydroGNSS supplies globally consistent measurements of crucial **water-cycle variables** derived from **GNSS reflectometry (GNSS-R)**, enabling all-weather, day/night, vegetation-penetrating observations of:

- 🌱 Soil moisture  
- 🌊 Inundation / wetlands / ephemeral pooling  
- ❄️ Freeze–thaw state  
- 🌿 Above-ground biomass  
- 🌬️ Supplemental: ocean wind speed, sea-ice state (context only)

These are harmonized into **FAIR+CARE-aligned STAC Items** and DCAT datasets, enabling integration with:

- KFM climate + hydrology ETL  
- Flood/drought models  
- Archaeological landscape analyses  
- Story Node v3 + Focus Mode v3 narrative layers  

---

## 🛰️ Mission Summary (KFM Knowledge Capsule · v11.2)

**Launch Date:** 28 Nov 2025  
**Agency:** ESA (Scout Mission #1)  
**Operator:** SSTL (UK)  
**Orbit:** Sun-synchronous · ~550 km  
**Constellation:** 2 spacecraft (180° phased)

### Why HydroGNSS matters to KFM

- ✔ All-weather soil-moisture monitoring  
- ✔ Freeze–thaw detection for ecohydrology + infrastructure risk  
- ✔ Biomass & inundation: critical for archaeology, land-use history, and ecology  
- ✔ Robust cross-validation with SMAP, ERA5, Landsat/Sentinel, NOAA datasets  
- ✔ GNSS-R offers **continuity** as older missions degrade  

HydroGNSS is one of the **core water-cycle satellite layers** in the KFM v11 data architecture.

---

## 🗂️ Directory Layout

~~~text
docs/data/satellites/hydrognss/
├── 📄 README.md                               # HydroGNSS dataset overview (this file)
├── 🗂️ stac/                                    # STAC Collections / Items for HydroGNSS products
│   ├── 🌱 soil-moisture/                      # Soil moisture STAC Items (GNSS-R derived)
│   ├── 🌊 inundation/                          # Wetlands / pooling extents & inundation flags
│   ├── ❄️ freeze-thaw/                         # Freeze/thaw ground state (seasonal & daily)
│   ├── 🌿 biomass/                             # Above-ground biomass indicators
│   └── 📚 ancillary/                           # Orbit metadata, calibration notes, mission docs
├── 🧾 metadata/                                # DCAT, JSON-LD, PROV-O lineage metadata
├── 🛠️ transforms/                              # Harmonization logic, band extraction, QA masks
├── 🧪 qa/                                      # Cross-mission comparisons, data-quality analytics
└── 🧷 samples/                                  # Example rasters + sample STAC items for onboarding
~~~

---

## 🧩 Data Standards & Integration Model

HydroGNSS products flow through the **KFM v11 ingestion pipeline**, conforming to:

### 📦 **STAC-Level Harmonization**

- Uses **KFM-STAC v11** profile  
- STAC Items include:
  - Geometry footprints  
  - Orbit metadata  
  - Variable bands + uncertainty layers  
  - QA flags  
  - CARE + sovereignty metadata  
- Assets: COG (primary), Zarr/NetCDF (optional)

### 🧾 **Metadata Stack**

- **FAIR** → discoverability, versioning, provenance, schema compliance  
- **CARE** → sensitivity & sovereignty review on inundation/biomass  
- **PROV-O** → explicit derivations from ESA L1/L2 → KFM products  
- **JSON-LD** → graph alignment with CIDOC, OWL-Time, GeoSPARQL  

### 🔗 **Hydrologic/Climate Interoperability**

- Soil moisture → drought ETL  
- Inundation → flood models, wetland dynamics  
- Freeze–thaw → ecohydrology, hazards  
- Biomass → archaeology, land-use change, fire-regime analyses  

---

## 🛠️ KFM Ingestion Pipeline (Conceptual)

*(Plain text to maintain single-code-block compliance; diagrams live in-repo.)*

1. Detect ESA HydroGNSS L1/L2 product release  
2. Retrieve → stage → preprocess  
3. Apply orbit filtering + geolocation  
4. Extract water-cycle variables  
5. Generate STAC Items & Collections  
6. Apply QA masks & uncertainty thresholds  
7. Cross-compare with SMAP, SMOS, NOAA NCEI, Mesonet, Landsat/Sentinel  
8. Produce:
   - STAC/DCAT metadata  
   - PROV-O lineage  
   - Energy + carbon telemetry  
   - CARE/sovereignty flags  
9. Register datasets in global KFM catalogs  
10. Publish release bundle (SBOM, manifest, telemetry)

---

## 🔮 Applications Inside KFM

### 🌡️ Climate  
- Drought risk & long-term soil-moisture trend detection  
- Freeze-line mapping for seasons + anomalies  

### 🏺 Archaeology  
- Wetland reactivation linked to trade routes & settlement corridors  
- Biomass change affecting site detectability  
- Freeze–thaw erosion risk near cultural landscapes  

### 💧 Hydrology  
- Soil infiltration modeling  
- Floodplain expansion + wetland connectivity  
- Recharge inference (indirect)  

### 🔬 Multi-Sensor Fusion  
- Pair with:
  - SMAP/SMOS  
  - NOAA drought indices  
  - Landsat/Sentinel NDVI/EVI  
  - ERA5/CMIP climate products  

---

## 🔐 Governance & Sensitivity Notes

HydroGNSS is broadly open, but KFM enforces:

- **CARE-A** labeling when intersecting tribal jurisdictions  
- **Dynamic H3 generalization** for sensitive inundation/biomass indicators  
- No display of raw high-precision anomalies in sensitive areas  
- Full provenance, lineage, WAL protection  
- Required data-use notices in Focus Mode v3 + Story Node v3  

Derived layers that could imply vulnerability **must undergo sovereignty review**  
before publication.

---

## 🧭 Version History

| Version | Date       | Summary                                                                                      |
|--------:|------------|----------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Added emoji-rich directory, improved CARE/H3 sections, updated metadata to MDP v11.2.2.      |
| v11.2.0 | 2025-11-29 | Initial HydroGNSS documentation, directory standardization, STAC scaffolding.                |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../../README.md) · [🗂️ Data Catalog](../../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
