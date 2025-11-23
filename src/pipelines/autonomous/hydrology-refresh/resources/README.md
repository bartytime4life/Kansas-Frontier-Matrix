---
title: "📦 KFM v11 — Hydrology Refresh Resources Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/hydrology-refresh/resources/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/telemetry/autonomous-hydrology-refresh.json"
telemetry_schema: "../../../../../schemas/telemetry/autonomous-hydrology-refresh-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Resource Module"
semantic_document_id: "kfm-autonomous-hydro-resources-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:hydrology-refresh:resources:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📦 **Hydrology Refresh Resources Module (v11)**  
`src/pipelines/autonomous/hydrology-refresh/resources/README.md`

**Purpose:**  
Document all static configuration required by the **Autonomous Hydrology Refresh Pipeline**, including  
provider definitions, hydrology schema, checksum manifests, and STAC default metadata. These  
resources form the deterministic backbone for automated ingestion, validation, and graph promotion  
of hydrologic datasets under KFM v11.

</div>

---

# 📘 Overview

This module contains all **resource files** needed by the hydrology-refresh pipeline:

- ☑ **providers.yaml** — registry of USGS, NOAA, KDHE, and other hydrology data sources  
- ☑ **hydro_v1.schema.json** — normalization schema for hydrology tabular outputs  
- ☑ **manifest.json** — hashlib SHA-256 ledger for STAC asset integrity  
- ☑ **STAC default metadata blocks** for hydrology Items  
- ☑ **Temporal/spatial requirements** for streamflow, WSEL, bathymetry, WID, sediment, and precip  
- ☑ **Governance & Data Contract v3 compliance fields**

All resources must remain **declarative**, **version-controlled**, and **machine-extractable**.  
They participate in stale detection, schema checks, lineage tracking, checksum enforcement,  
and STAC generation.

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/hydrology-refresh/resources/
│
├── README.md                                # This file (v11 standard)
│
├── providers.yaml                            # Hydrology provider registry (USGS, NOAA, KDHE…)
│
├── schema/
│   └── hydro_v1.schema.json                  # Canonical hydrology normalization schema
│
└── checksums/
    └── manifest.json                         # SHA-256 integrity ledger for hydrology STAC assets
```

---

# 🌐 providers.yaml — Hydrology Provider Registry

Defines all upstream hydrology sources:

- Streamflow (USGS NWIS)  
- Water-surface elevation  
- Precipitation (NOAA/NWS)  
- Water-quality (KDHE)  
- Any CSV/JSON/GeoJSON/NetCDF hydrologic source  

### Required fields:

- `id`: unique provider key  
- `kind`: `csv_http | json_http | geojson_http | netcdf_http`  
- `url`: remote location  
- `etag_header`, `time_header`: stale-detection fields  
- `stac:`  
  - STAC collection ID  
  - provider roles  
  - license  
  - attribution metadata  

### Example (v11):

```yaml
providers:
  - id: "usgs.streamflow.ks_mainstem"
    kind: "csv_http"
    url: "https://example.gov/usgs/ks/mainstem/daily.csv"
    etag_header: "ETag"
    time_header: "Last-Modified"
    stac:
      collection: "kfm-hydrology-statewide"
      license: "CC-BY-4.0"
      providers:
        - name: "USGS"
          roles: ["producer","licensor"]
```

---

# 📑 hydro_v1.schema.json — Hydrology Schema Overview

This schema governs **all normalized hydrology outputs**, enabling:

- Canonical naming and units  
- Consistent temporal structure (ISO 8601)  
- CRS v11 alignment (EPSG:4326 for tabular)  
- Hydrology variable typing  
- Direct mapping to STAC Items + Neo4j entities  

## Minimum required fields:

- `SITE_ID` (string)  
- `DATETIME` (ISO 8601 UTC)  
- `FLOW_CFS` (m³/s or cfs → converted to Data Contract v3 units)  
- `STAGE_M` (meters, NAVD88)  
- `PRCP_MM` (precipitation in mm)  
- `LAT`, `LON` (EPSG:4326)  

Optional fields:

- `WSEL_M` (water-surface elevation; NAVD88)  
- `WQ_PARAM` values (KDHE)  
- `PROVIDER` metadata  
- `QUALITY_CODE`

Schema MUST be JSON Schema 2020-12 compliant and validated by CI.

---

# 🔐 checksums/manifest.json — Integrity Ledger (SHA-256)

The checksum manifest:

- Ensures **STAC asset immutability**  
- Detects upstream provider drift  
- Prevents invalid/missing datasets from entering the knowledge graph  
- Supports multi-hash (future KFM-STAC extension)  

### Manifest fields:

- `version` — schema version of manifest  
- `last_updated` — timestamp  
- `entries` — per-asset SHA-256  
- Optional `mh:sha256-hex`

### CI must:

- Block PRs on missing hash entries  
- Check alphabetical ordering of keys  
- Validate JSON structure  
- Reject mismatched SHA-256 values  
- Verify deterministic regeneration through pipeline

---

# 🧬 How These Resources Are Used in the DAG

These files power the nodes:

| DAG Node | Resource Used |
|---------|----------------|
| `detect_stale.py` | providers.yaml + checksum manifest |
| `fetch_sources.py` | providers.yaml |
| `normalize_tabular.py` | hydro_v1.schema.json |
| `build_stac_items.py` | providers.yaml + schema |
| `validate_checksums.py` | checksum manifest |
| `stac_validate.py` | schema + STAC validation |
| `neo4j_sync.py` | STAC metadata from Items |
| `post_hooks.py` | telemetry & lineage bundles |

All resources MUST remain stable, version-controlled, and documented.

---

# 🔍 CI/CD Enforcement

CI MUST validate:

- Schema correctness (`hydro_v1.schema.json`)  
- URL/header sanity in `providers.yaml`  
- `manifest.json` existence + structural correctness  
- No missing hashes for hydrology assets  
- STAC Items derived from these resources contain:  
  - `hydro:type`  
  - CRS/vertical metadata  
  - STAC 1.0 compliance  
  - PROV-O lineage  
  - DCAT 3 mapping fields  

Failure → PR blocked.

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial Hydrology Refresh Resources module (KFM v11).

---

<div align="center">

**Kansas Frontier Matrix — Hydrology Refresh Resources (v11)**  
*Declarative · Deterministic · Hydrologically Accurate*

</div>

---

### 🔗 Footer  
[⬅ Back to Hydrology Pipeline](../README.md) · [🧩 Nodes](../nodes/README.md) · [📑 Schema Module](./schema/README.md) · [🔐 Checksums](./checksums/README.md) · [🏛 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

