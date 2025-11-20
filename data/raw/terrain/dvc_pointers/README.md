---
title: "🧷 Kansas Frontier Matrix — Raw Terrain DVC Pointer Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/terrain/dvc_pointers/README.md"
version: "v11.0.0"
last_updated: "2025-11-19"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-raw-terrain-dvc-pointers-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC0 / Public Domain (pointer files only)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Data Pointer Registry"
intent: "terrain-raw-storage"
fair_category: "F1-A1-I1-R1"
care_label: "Low-Risk / Public Geospatial Data"
sensitivity_level: "None"
provenance_chain:
  - "data/raw/terrain/sources/usgs_3dep.json"
  - "data/raw/terrain/sources/kansas_lidar.json"
  - "data/raw/terrain/sources/historic_topos.json"
ontology_alignment:
  geo: "GeoSPARQL"
  time: "OWL-Time"
  prov: "PROV-O"
  stac: "STAC 1.0.0"
story_node_refs: []
metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"
doc_uuid: "urn:kfm:data:raw:terrain:dvc_pointers:readme:v11"
semantic_document_id: "kfm-data-raw-terrain-dvc-pointers"
event_source_id: "ledger:data_raw_terrain_dvc_pointers"
immutability_status: "mutable"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
ai_transform_prohibited:
  - "content-alteration"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public"
lifecycle_stage: "active"
ttl_policy: "Persistent"
sunset_policy: "Reviewed annually"
---

<div align="center">

# 🧷 **Kansas Frontier Matrix — Raw Terrain DVC Pointer Registry**  
`data/raw/terrain/dvc_pointers/README.md`

**Purpose:**  
Define the **Data Version Control (DVC) pointer structure** for all raw terrain elevation assets—DEM tiles, LiDAR LAZ files, historic elevation rasters—stored in remote object storage.  
These pointer files ensure **reproducible data acquisition**, **exact versioned references**, and **CI/CD-safe lightweight tracking** in the KFM monorepo.

</div>

---

## 🌎 Overview

The `dvc_pointers/` directory houses **DVC-managed pointer files** (*.dvc) for raw terrain datasets.

These pointers reference remote storage locations (S3, GCS, Azure, or on-prem object stores) that contain:

- USGS 3DEP DEM tiles  
- Kansas statewide LiDAR QL1/QL2 LAZ files  
- Historic topographic rasters (pre-georeference)  
- Any upstream terrain asset that must be reproducibly pulled for ETL  

The goal is to:

- Prevent large binary blobs from polluting Git  
- Maintain deterministic ETL input sets  
- Record complete provenance (checksum, size, URL, and version)  
- Ensure downstream processing can always regenerate terrain-derived products  

The pointer files serve as the **official handshake** between KFM’s `data/raw/terrain` structure and remote storage.

---

## 📁 Directory Structure

```

data/raw/terrain/dvc_pointers/
├── ks_dem_1m.dvc          # Pointer to statewide 1m DEM mosaic
├── ks_lidar_ql2.dvc       # Pointer to statewide LiDAR QL2 tiles
├── usgs_ned_10m.dvc       # Pointer to legacy 10m DEM fallback
├── historic_topos.dvc     # Pointer to raw historic topo scans (bulk)
└── README.md              # This file

```

You MAY add additional pointers for county-level LiDAR, DEM subsets, or hydrology-ready masked rasters.

---

## 🛠️ Pointer Specification (DVC)

Each `.dvc` file MUST contain:

- **`outs:`**  
  - `path` — file or directory path when materialized  
  - `md5` — checksum ensuring deterministic provenance  
  - `size` — raw file size (expected)  
  - `remote` — remote storage alias  
- **Optional:**  
  - `meta:` block for spatial/temporal footprint metadata  
  - `stac_ref:` link to STAC Item representing this raw asset  

Example minimal pointer:

```

outs:

* md5: 6a9b345eac9b8dcb…
  size: 12893499324
  path: ks_dem_1m/
  remote: terrain-raw

```

Extended pointer with metadata:

```

meta:
bbox: [-102.05, 37.0, -94.6, 40.0]
crs: "EPSG:4326"
acquired: "2022-03-14"
stac_ref: "../../stac/terrain/items/ks_dem_1m.json"

```

All pointers undergo CI validation:

- Checksum correctness  
- Remote availability  
- Path/schema conformance  
- Metadata presence (if extended mode enabled)

---

## 🔗 Integration Flow (Raw → Processed → STAC)

```

.dvc pointer
↓ dvc pull
raw terrain files (LAZ/GeoTIFF/TIFF)
↓ ETL preprocessing
COG conversion / reprojection / merging
↓
Processed terrain assets
↓
STAC Collection + Items

```

---

## 🚦 FAIR+CARE & Governance Notes

- DVC pointers inherit licensing from upstream terrain datasets; most are public domain.  
- Historical rasters must follow archival access rules; only the pointer is tracked here—not the file.  
- Provenance for every ETL transformation MUST refer back to the DVC pointer source.  

---

## 📜 Version History

| Version | Date       | Author          | Summary |
|---------|------------|-----------------|---------|
| v11.0.0 | 2025-11-19 | Lead Programmer | Initial creation of DVC pointer registry for raw terrain layer |

---

<div align="center">

🧷 **Raw Terrain DVC Registry**  
_Secure, reproducible, version-controlled access to Kansas terrain foundations._

[⬅️ Back to Raw Terrain README](../README.md) •  
[🗂 Source Registry](../sources/README.md) •  
[📐 Data Architecture](../../../../docs/architecture/system_overview.md)

</div>
