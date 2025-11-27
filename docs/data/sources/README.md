---
title: "🌎 Kansas Frontier Matrix — Data Sources & Registries (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/sources/README.md"
version: "v11.2.2"
last_updated: "2025-11-27"
review_cycle: "Continuous · FAIR+CARE Council"
release_stage: "Stable / Governed"
lifecycle: "LTS"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-sources-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
status: "Active / Enforced"
doc_kind: "Registry"
header_profile: "standard"
footer_profile: "standard"
category: "Data · Registry · Metadata"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
ttl_policy: "12 months"
provenance_chain:
  - "docs/data/sources/README.md@v10.0.0"
  - "docs/data/sources/README.md@v11.0.0"
  - "docs/data/sources/README.md@v11.1.0"
  - "docs/data/sources/README.md@v11.2.1"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🌎 **Kansas Frontier Matrix — Data Sources & Registries**  
`docs/data/sources/README.md`

**Purpose**  
Authoritative registry for **all datasets, archives, and APIs** integrated into the Kansas Frontier Matrix (KFM).  
Defines provenance, lineage, schema compliance, FAIR+CARE classification, and STAC/DCAT mappings.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare/FAIRCARE-GUIDE.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)](../../../releases/v11.2.2/manifest.zip)

</div>

---

## 📘 Overview

All KFM data sources must meet:

- STAC 1.0 Collection/Item requirements  
- DCAT 3.0 dataset catalog requirements  
- FAIR+CARE ethical constraints  
- PROV-O lineage requirements  
- Ontology alignment (CIDOC-CRM · OWL-Time · GeoSPARQL)  

This registry ensures **consistent ingestion**, **deterministic ETL**, and **traceable provenance**.

---

## 🗂️ Directory Layout

~~~text
docs/data/sources/
├── 📄 README.md
├── 🗺️ usgs_historic_topo.json
├── 🌦️ noaa_stations.json
├── 🏔️ ks_dem.json
├── 🚨 fema_disasters.json
├── 📜 blm_land_patents.json
├── 🧭 kgs_geology.json
├── 🪶 tribal_boundaries.json
└── 🏛️ khs_archives.json
~~~

---

## 🌐 Primary Data Sources (STAC + DCAT)

| ID | Org | Description | Formats | License | FAIR+CARE | Status |
|----|-----|-------------|----------|----------|------------|---------|
| `usgs_historic_topo` | USGS | Historic topo maps | GeoTIFF/COG | Public Domain | F1-A1 | ✅ Approved |
| `noaa_stations` | NOAA | Climate stations | CSV/API | Public Domain | F1-A1 | ✅ Approved |
| `ks_dem` | DASC | Elevation DEM + LiDAR | GeoTIFF/COG | CC-BY 4.0 | F1-R1 | ✅ Approved |
| `fema_disasters` | FEMA | Disaster declarations | JSON/API | Public Domain | F1-A1 | ✅ Approved |
| `blm_land_patents` | BLM | Land patents 1850–1900 | CSV/Shapefile | Public Domain | CARE-Flag | ⚙ Review |
| `kgs_geology` | KGS | Geology + aquifers | GeoJSON/NetCDF | CC-BY 4.0 | F1-R1 | ✅ Approved |
| `tribal_boundaries` | BIA/Tribal | Historic territories | Shapefile | Restricted | CARE-High | ⚠ Restricted |
| `khs_archives` | KHS | Historical documents/maps | PDF/Text | Mixed | CARE-High | ⚙ Review |

---

## 🧩 Metadata Schema (DCAT + STAC + JSON-LD)

Each catalog entry MUST include:

- `@context` (schema.org + STAC)
- DCAT dataset fields (`dct:title`, `dct:license`, `dct:spatial`)
- STAC Collection (`type: Collection`)
- `extent.spatial.bbox`
- `extent.temporal.interval`
- `prov:wasDerivedFrom`
- `care:authority_to_control`  
- `license` (SPDX)
- CRS declared (`EPSG:4326` unless justified)

---

## 🧮 Example Entry (v11-compliant)

~~~json
{
  "@context": ["https://schema.org", "https://stacspec.org/stac/context.json"],
  "id": "noaa_stations",
  "type": "Collection",
  "stac_version": "1.0.0",
  "title": "NOAA Kansas Climate Stations",
  "description": "Daily precipitation and temperature observations (1880–present).",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": { "bbox": [[-102.05, 37.0, -94.6, 40.0]] },
    "temporal": { "interval": [["1880-01-01T00:00:00Z", null]] }
  },
  "care": {
    "authority_to_control": "Open",
    "ethics": "No sensitive content"
  },
  "prov:wasDerivedFrom": "https://www.ncei.noaa.gov/"
}
~~~

---

## 🧠 Provenance & Lineage (PROV-O)

Every dataset is logged with:

- ETL activity record (`prov:Activity`)  
- STAC asset creation logs  
- Graph-edge provenance (`prov:wasGeneratedBy`)  
- Sovereignty filters for cultural/tribal data  

---

## 🕰️ Version History

| Version | Date | Summary |
|---------|---------|----------|
| v11.2.2 | 2025-11-27 | Full v11.2.2 compliance, emoji directory layout restored, footer upgraded. |
| v11.2.1 | 2025-09-01 | CARE enforcement layer added. |
| v11.1.0 | 2025-05-10 | STAC/DCAT harmonization. |
| v11.0.0 | 2025-01-12 | Initial v11 registry. |
| v10.0.0 | 2025-11-10 | First unified registry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [➡️ Next](../contracts/README.md) · [🛡️ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
