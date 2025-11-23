---
title: "📦 KFM v11 — Climate Refresh Resources Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/climate-refresh/resources/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/telemetry/autonomous-climate-refresh.json"
telemetry_schema: "../../../../../schemas/telemetry/autonomous-climate-refresh-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Resource Module"
semantic_document_id: "kfm-autonomous-climate-refresh-resources-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:climate-refresh:resources:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📦 **Climate Refresh Resources Module (v11)**  
`src/pipelines/autonomous/climate-refresh/resources/README.md`

**Purpose:**  
Document all **static, declarative resources** required by the **Autonomous Climate Refresh Pipeline**, including  
provider registries, climate schemas, checksum manifests, spatial/temporal metadata, and STAC default settings.  
This module provides the configuration backbone enabling deterministic, zero-touch climate ingestion under KFM v11.

</div>

---

# 📘 Overview

This module contains resource objects that:

- Declare **climate data providers** (NOAA, PRISM, Daymet, Mesonet, NCEI, CPC indices, etc.)  
- Define **climate variable schemas** (`climate_v1.schema.json`)  
- Store **checksum manifests** for STAC assets (`manifest.json`)  
- Provide **STAC template metadata blocks**  
- Establish canonical **spatial**, **temporal**, and **units** metadata for climate variables  
- Encode **FAIR+CARE**, **CRS v11**, **Vertical Axis v11**, and **Tiling v11** requirements  

All files here MUST be treated as **read-only configuration** during runtime unless governance policies  
permit controlled updates (such as checksum rotation).

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/climate-refresh/resources/
│
├── README.md                            # This file (v11 MDP)
│
├── providers.yaml                        # All climate providers + STAC defaults
│
├── schema/
│   └── climate_v1.schema.json            # JSON Schema for normalized climate variables + metadata
│
└── checksums/
    └── manifest.json                     # SHA-256 manifest for station/gridded climate STAC assets
```

---

# 🌍 providers.yaml — Climate Providers Registry

This file defines **all upstream climate sources** ingested by the autonomous pipeline.

### Required fields per provider:

- `id`: canonical provider key  
- `kind`: `csv_http | json_http | netcdf_http | raster_http | custom`  
- `url`: remote resource location  
- `etag_header` / `time_header`: for stale-detection  
- `stac`:  
  - `collection`: STAC Collection ID  
  - `license`: SPDX identifier  
  - `providers`: list of data producers/licensors  
  - default metadata (citation, attribution)  

### Example (KFM v11-compliant):

```yaml
providers:
  - id: "noaa.ncei.daily"
    kind: "csv_http"
    url: "https://example.noaa.gov/ncei/ks/daily.csv"
    etag_header: "ETag"
    time_header: "Last-Modified"
    stac:
      collection: "kfm-climate-statewide"
      license: "CC0-1.0"
      providers:
        - name: "NOAA NCEI"
          roles: ["producer"]
```

---

# 📑 climate_v1.schema.json — Climate Variable Schema

This schema governs **station** and **gridded climate variables**, ensuring:

- Canonical variable names (`tmax`, `tmin`, `prcp`, `vpd`, `srad`, `ws`, etc.)  
- Units aligned with **Data Contract v3**  
  - temperature → °C  
  - precipitation → mm  
  - solar radiation → W/m²  
  - vapor pressure deficit → kPa  
- Spatial fields conform to **EPSG:4326**  
- Gridded rasters conform to **CRS v11** → EPSG:26914 for processing, EPSG:4326 for STAC geometry  
- Temporal indexing using **ISO 8601** and **OWL-Time** intervals  

MUST validate all outputs of:

- `normalize_station.py`  
- `normalize_gridded.py`

---

# 🔐 checksums/manifest.json — Climate Asset Integrity Ledger

This manifest holds **SHA-256 digests** for:

- Station normalized files  
- Gridded COG climate rasters  
- Derived climate composites  
- Any additional STAC assets referenced by the pipeline

CI blocks PRs when:

- A referenced climate asset has no matching hash  
- A hash mismatch is detected  
- Manifest JSON is malformed or non-deterministic  
- Unauthorized checksum updates occur  

Checksum verification is performed in:

- `validate_checksums.py`  
- `detect_stale.py` (staleness logic)  
- `post_hooks.py` (telemetry emission)

---

# 🧬 Integration Across Climate Pipeline

This resources module is consumed by the following nodes:

- `detect_stale.py` — provider timestamps, etags  
- `fetch_sources.py` — remote URLs + headers  
- `normalize_station.py` — schema enforcement  
- `normalize_gridded.py` — CRS + raster metadata constraints  
- `build_stac_items.py` — STAC templates + defaults  
- `validate_checksums.py` — manifest usage  
- `stac_validate.py` — schema + STAC compliance  

Any changes MUST be reflected consistently across:

- STAC Collections  
- KFM vertical axis & CRS metadata  
- Neo4j sync node  
- Tiling logic for climate COGs  
- Climate Story Node v3 extraction  

---

# 🔍 CI/CD Enforcement

CI MUST enforce:

- Schema lint (`climate_v1.schema.json`)  
- Provider registry sanity (valid URLs, headers, STAC fields)  
- Checksum manifest integrity  
- No missing required metadata fields  
- JSON/YAML integrity via validators  
- Backwards-compatibility rules when new schema versions are introduced  

PRs failing any rule are automatically rejected.

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial Climate Refresh resources module (KFM v11).

---

<div align="center">

**Kansas Frontier Matrix — Climate Refresh Resources (v11)**  
*Declarative · Deterministic · Scientifically Traceable*

</div>

---

### 🔗 Footer  
[⬅ Back to Climate Pipeline](../README.md) · [🧩 Nodes](../nodes/README.md) · [📑 Schema Module](./schema/README.md) · [🔐 Checksums](./checksums/README.md) · [🏛 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

