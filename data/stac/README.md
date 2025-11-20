---
title: "🗃️ Kansas Frontier Matrix — STAC Catalog (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/stac/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-stac-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11"
status: "Active / Enforced"
doc_kind: "Data Catalog"
intent: "stac-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 🗃️ **Kansas Frontier Matrix — STAC Catalog**  
`data/stac/README.md`

**Purpose:**  
Authoritative SpatioTemporal Asset Catalog (STAC) for all Kansas Frontier Matrix datasets.  
Implements FAIR+CARE governance, PROV-O lineage, checksum verification, DCAT 3.0 alignment, ISO 19115 metadata, and **Streaming STAC** for continuously-updating Items.

</div>

## 📘 Overview
The KFM STAC Catalog is the primary metadata index for all validated climatology, hydrology, hazards, landcover, spatial raster/vector, and tabular datasets.  
It ensures:

* FAIR+CARE certification  
* Governance-led provenance and checksum lineage  
* STAC 1.0 + DCAT 3.0 cross-compatibility  
* JSON-LD semantic linkage into the knowledge graph  
* Energy/carbon telemetry for sustainability accountability  
* Streaming STAC updates for real-time datasets

## 🗂️ Directory Layout
```plaintext
data/stac/
├── README.md
├── catalog.json
├── collection_climate.json
├── collection_hazards.json
├── collection_hydrology.json
├── collection_landcover.json
├── collection_spatial.json
├── collection_tabular.json
└── metadata.json
```

## 🌍 Domain Overview
The STAC catalog unifies all spatial and temporal datasets across the Kansas Frontier Matrix.  
Domain targets include:

* 🌡️ Climate normals and projections  
* 🌊 Hydrology, streamflow, watersheds  
* ⚠️ Hazards: tornado, drought, seismic, flood  
* 🗺️ Raster and vector spatial composites  
* 🗂️ Tabular datasets mapped to DCAT  
* 🧩 Mixed-media layers (LiDAR, scanning, surveys)

All datasets attach:  
STAC → DCAT → JSON-LD → PROV-O → Neo4j Graph → Story Node v3 → Focus Mode integration.

## 🔗 Entity Requirements (PROV-O)
All STAC entities must declare:

* `prov:Entity` (dataset or collection)  
* `prov:Location` (canonical KFM path)  
* `prov:wasGeneratedBy` (ETL pipeline reference)  
* `prov:wasAttributedTo` (agent)  
* `prov:wasDerivedFrom` (source dataset IDs)  
* `prov:qualifiedAttribution` (governance approval entry)

Checksum rules:

* SHA256 only  
* Stored within `metadata.json`  
* Matched to `manifest.zip`

## ⚙️ Activity Requirements
Each dataset must include:

* Extraction method  
* Transformation pipeline ID  
* Validation workflow ID  
* Publication timestamp (UTC, ISO 8601 ASCII only)  
* Telemetry bundle (energy_wh, carbon_gco2e)

Pipelines must be deterministic and reproducible.

## 🧑‍💼 Agent Requirements
Agents contributing to STAC entries include:

* `@kfm-architecture` (schema)  
* `@kfm-data` (pipelines)  
* `@kfm-governance` (approvals)  
* `@faircare-council` (ethics)  
* `@kfm-security` (checksum integrity)

Agents are PROV-O `prov:Agent`.

## 🧪 Validation Requirements
Every collection and item must pass:

* STAC 1.0 conformance  
* DCAT 3.0 crosswalk validation  
* ISO 19115 field check  
* FAIR+CARE compliance  
* Checksum integrity  
* Schema verification (JSON schema)  
* Governance approval step (append-only ledger)

Outputs stored under:

* `data/reports/audit/…`  
* `data/reports/fair/…`  
* `data/reports/validation/…`

## 📥 Retrieval Examples
### Python (pystac-client)
```python
from pystac_client import Client
catalog = Client.open("https://kfm.example.org/catalog.json")
hydro = catalog.get_collection("kfm_hydrology")
items = list(hydro.get_items())
```

### CURL
```bash
curl -s https://kfm.example.org/data/stac/catalog.json
```

### Neo4j Cypher
```cypher
MATCH (c:StacCollection {id: "kfm_hazards_v11_1"})
RETURN c.title, c.temporal_extent_start, c.temporal_extent_end;
```

## 🛣️ Roadmap
* v11.2 — Real-time streaming STAC WebSocket bridge  
* v11.3 — Automated provenance embedding within STAC items  
* v11.4 — H3-based spatial generalization for ethical masking  
* v11.5 — Multi-resolution tiling integration for Focus Mode v3  

## 🕰️ Version History
| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v11.1.0 | 2025-11-19 | `@kfm-architecture` | Full KFM-MDP v11 upgrade, governance strengthening, directory alignment. |
| v11.0.0 | 2025-11-15 | `@kfm-architecture` | Initial v11 metadata migration. |
| v10.2.2 | 2025-11-12 | `@kfm-architecture` | Streaming STAC and telemetry v2. |

## 🔗 Footer
[⬅️ Back to Data Index](../README.md) ·  
[📐 Data Architecture](../../docs/ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)
