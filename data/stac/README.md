---
title: "🗃️ Kansas Frontier Matrix — STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/stac/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/stac-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-stac-v11.2.2.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Data Catalog"
intent: "kfm-stac-root"
semantic_document_id: "kfm-data-stac-root"
doc_uuid: "urn:kfm:data:stac:root:v11.2.2"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified (EO-Spatial Non-Sensitive)"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🗃️ **Kansas Frontier Matrix — STAC Catalog**  
`data/stac/README.md`

**Purpose**  
Serve as the **authoritative STAC v11.2 catalog root** for all spatial, temporal, geoscientific, hydrologic, hazard, landcover, tabular, and EO-derived datasets across the Kansas Frontier Matrix.  
Implements:

- **FAIR+CARE governance**
- **STAC 1.1.0 + KFM-STAC v11.2 extensions**
- **DCAT 3.0 crosswalks**
- **PROV-O lineage + OpenLineage v2.5**
- **ISO 19115 metadata**
- **Energy + Carbon telemetry (ISO 50001 / ISO 14064)**
- **Streaming STAC** for real-time datasets

</div>

---

## 📘 Overview

The KFM STAC root catalog provides:

- A unified entrypoint for **all KFM geospatial/temporal datasets**
- Canonical metadata for:
  - Hydrology
  - Climate / weather
  - Hazards
  - Landcover / land use
  - Raster + Vector spatial layers
  - Tabular statistical and environmental datasets
- A single machine-readable interface via STAC → DCAT → JSON-LD → Neo4j Graph
- Versioned, reproducible, governance-enforced dataset lineage

All datasets passing through KFM ingestion pipelines **must register here**.

---

## 🗂️ Directory Layout

This layout follows the **global canonical structure** shared across all KFM v11.2.2 standards:

```text
📁 data/
└── 📁 stac/                                 — Root STAC catalog
    ├── 📄 README.md                         — ← This file
    ├── 📄 catalog.json                      — Root STAC catalog
    ├── 📄 collection_climate.json           — Climate datasets
    ├── 📄 collection_hazards.json           — Hazard datasets
    ├── 📄 collection_hydrology.json         — River, reservoir, groundwater datasets
    ├── 📄 collection_landcover.json         — NLCD, crop, land use layers
    ├── 📄 collection_spatial.json           — Raster, vector composites & DEMs
    ├── 📄 collection_tabular.json           — DCAT-mapped tabular datasets
    ├── 📄 metadata.json                     — STAC-level metadata manifest
    │
    └── 📁 missions/                         — EO mission namespaces (Sentinel, Landsat, NAIP, SWOT)
        ├── 📁 sentinel-1d/
        ├── 📁 sentinel-1c/
        ├── 📁 sentinel-2/
        ├── 📁 landsat-9/
        ├── 📁 naip/
        └── 📁 swot/
```

This directory is **authoritative** for all STAC-facing references in KFM.

---

## 🌍 Domain Overview

The STAC catalog covers:

### 🌡️ Climate  
- PRISM  
- HRRR  
- Daymet  
- NDFD  
- NOAA Climate Normals  

### 🌊 Hydrology  
- Streamflow + stage  
- WID (Water Information Dashboard)  
- Reservoir levels  
- Flood depth grids  
- Watershed boundaries  

### ⚠️ Hazards  
- Severe weather (tornado paths, hail swaths, storm tracks)  
- Wildfire risk  
- Drought indices  
- Heat advisories  
- InSAR-derived deformation once Sentinel-1D becomes operational  

### 🗺️ Spatial  
- Elevation (DEM, nDSM, DTM)  
- Land use  
- Parcels  
- Road networks  
- Soil datasets (SSURGO / gNATSGO)  

### 📊 Tabular  
- Water quality  
- Meteorological station archives  
- Air quality from AQS/AirNow  
- Census & socioeconomic layers  

Every dataset stored here must satisfy **KFM-STAC v11.2** fields, including:

- Temporal extent  
- Spatial geometry (GeoJSON)  
- License and FAIR+CARE flags  
- Provenance chain  
- Telemetry bundle  
- Schema and units metadata  

---

## 🔗 PROV-O Entity Requirements

Every STAC entity is a **prov:Entity** and MUST include:

- `prov:Location` — Canonical KFM path  
- `prov:wasGeneratedBy` — ETL pipeline reference  
- `prov:wasDerivedFrom` — One or more upstream dataset IDs  
- `prov:qualifiedAttribution` — Approval by KFM councils  
- `prov:wasAttributedTo` — One or more agents (ETL, governance, architecture)

### Checksum Rules

- SHA256 required  
- Recorded in:
  - `metadata.json`
  - manifest.zip  
- Must match actual dataset content byte-for-byte

---

## ⚙️ Activity Requirements (PROV-O + OpenLineage v2.5)

Every dataset MUST record:

- Extraction method (URL/API/file)  
- Transformation steps — deterministic DAG ID  
- Validation workflow ID  
- Ingestion pipeline ID (LangGraph v11)  
- Telemetry bundle:
  - `energy_wh`  
  - `carbon_gco2e`  
  - `records_processed`  
- Promotion timestamp (`YYYY-MM-DDTHH:MM:SSZ`, ASCII only)

Pipelines MUST be **replayable** and **idempotent**.

---

## 🧑‍💼 Agent Requirements

Agents acting on STAC entries include:

| Agent | Role |
|-------|------|
| `@kfm-data` | ETL pipelines, transformations, ingestion |
| `@kfm-architecture` | Schema & system design |
| `@kfm-governance` | Governance approvals |
| `@faircare-council` | FAIR+CARE compliance |
| `@kfm-security` | Integrity + checksum verification |

Agents MUST appear in PROV-O and in the KFM Graph.

---

## 🧪 Validation Requirements

Each STAC Collection and Item MUST pass:

- STAC 1.1.0 schema validation  
- DCAT 3.0 crosswalk check  
- ISO 19115 semantic field verification  
- FAIR+CARE compliance checks  
- Telemetry presence check  
- JSON Schema validation  
- GeoJSON geometry validation  
- Governance checklist approval  

Validation outputs stored under:

```text
📁 data/
└── 📁 reports/
    ├── 📁 audit/
    ├── 📁 fair/
    └── 📁 validation/
```

---

## 📥 Retrieval Examples

### Python (pystac-client)
```python
from pystac_client import Client
cat = Client.open("https://kfm.example.org/data/stac/catalog.json")
haz = cat.get_collection("kfm_hazards")
items = list(haz.get_items())
```

### CURL
```bash
curl -s https://kfm.example.org/data/stac/catalog.json
```

### Neo4j Cypher
```cypher
MATCH (c:StacCollection {id:"kfm_hydrology"})
RETURN c.title, c.temporal_extent_start, c.temporal_extent_end;
```

---

## 🛣️ Roadmap

- **v11.2.2** — Full telemetry and governance alignment  
- **v11.3** — Autonomous provenance embedding in STAC Items  
- **v11.4** — H3-based spatial generalization for ethical masking  
- **v11.5** — Multi-resolution tiling for Focus Mode v3  

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-27 | Upgraded to full KFM-MDP v11.2.2; added canonical directory layout; telemetry, provenance, FAIR+CARE updates; mission linkage. |
| v11.1.0 | 2025-11-19 | First v11 STAC catalog; baseline governance, checksum lineage, and telemetry integration. |
| v11.0.0 | 2025-11-15 | Initial v11 STAC metadata migration. |

---

<div align="center">

🗃️ **Kansas Frontier Matrix — STAC Catalog v11.2.2**  
“Metadata is governance. STAC is the backbone of the KFM knowledge ecosystem.”

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Certified · Master Coder Protocol v6.3 · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Data Index](../README.md) ·  
[📐 Data Architecture](../../docs/ARCHITECTURE.md) ·  
[⚖ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
