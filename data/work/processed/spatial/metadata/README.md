---
title: "🗺️ Kansas Frontier Matrix — Processed Spatial Metadata (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/processed/spatial/metadata/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-work-processed-spatial-metadata-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0 · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11"
status: "Active / Enforced"
doc_kind: "Metadata Layer"
intent: "processed-spatial-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Processed Spatial Metadata**  
`data/work/processed/spatial/metadata/README.md`

**Purpose:**  
Define the **official metadata manifest layer** for all processed spatial datasets in KFM.  
This directory houses **PROV-O provenance chains**, **checksum manifests**, **FAIR+CARE certifications**, **telemetry bundles**, and **schema-alignment definitions**, all required for transparent, reproducible, and ethics-compliant geospatial data governance.

</div>

## 📘 Overview
The Processed Spatial Metadata Layer documents:

* Spatial dataset identity and lineage  
* CRS/geometry schema details  
* FAIR+CARE ethics certifications  
* Provenance relationships (entity → activity → agent)  
* SHA256 integrity manifests  
* STAC/DCAT metadata synchronization  
* Telemetry (energy_wh, carbon_gco2e)  
* ISO 19115 spatial metadata alignment  

This layer forms the authoritative metadata source for catalogs, graph ingestion, and Focus Mode v3.

## 🗂️ Directory Layout
```plaintext
data/work/processed/spatial/metadata/
├── README.md
├── spatial_manifest_v11.1.0.json
├── provenance_chain_v11.1.0.json
├── checksums_v11.1.0.json
├── certification_faircare_v11.1.0.json
├── telemetry_v11.1.0.json
└── schema_alignment_v11.1.0.json
```

## 🌍 Domain Overview
Metadata here describes:

* 🗺️ Spatial boundaries (climate zones, hydrology regions, parcel features)  
* 🏔️ Elevation/DEM metadata and raster tiling rules  
* 🌿 Landcover classification schemas  
* 📐 Geometry/topology checks (validity, slivers, overlaps)  
* ⛯ CRS definition (EPSG:4326 required)  
* 📊 Spatial indexing and bbox definitions  
* 🔗 Crosswalking to STAC `extent` and DCAT `spatial` blocks  

Metadata fields follow strict JSON-schema validation and ASCII-only rules.

## 🔗 Entity Requirements (PROV-O)
Each metadata entity must include:

* Unique `prov:Entity` identifier  
* SHA256 checksum for associated dataset(s)  
* Dataset UUID reference(s)  
* CRS field (EPSG:4326)  
* Spatial bbox  
* Temporal metadata (ASCII ISO 8601)  
* Schema version  
* FAIR+CARE certification markers  
* Governance ledger pointer  
* Telemetry block (energy_wh, carbon_gco2e)  

Entities remain immutable upon publication.

## ⚙️ Activity Requirements
Activities generating spatial metadata must declare:

* ETL or spatial-processing pipeline version  
* Parameter digest (ASCII-safe hash)  
* Topology QA results  
* FAIR+CARE approval ID  
* Validation coverage percent  
* Timestamp of metadata generation  
* STAC/DCAT sync reference  
* Associated agents  

Activities are encoded as PROV-O `prov:Activity`.

## 🧑‍💼 Agent Requirements
Agents must be explicitly encoded as PROV-O `prov:Agent`:

* `@kfm-spatial-lab` — spatial domain custodians  
* `@kfm-architecture` — schema & CRS standards governance  
* `@kfm-security` — checksum/integrity verification  
* `@faircare-council` — ethics & CARE oversight  
* `@kfm-data` — metadata lifecycle and governance operations  

Agents provide auditability and accountability.

## 🧪 Validation Requirements
All metadata files must pass:

* JSON schema validation  
* CRS/spatial metadata checks  
* Provenance chain validation  
* FAIR+CARE certification review  
* CARE masking (if culturally sensitive boundaries exist)  
* ISO 19115 metadata alignment  
* STAC/DCAT metadata mapping  
* Telemetry completeness checks  

Validation output stored in:

* `data/reports/validation/`  
* `data/reports/audit/`  
* `data/reports/fair/`

## 📥 Retrieval Examples

### Python
```python
import json
with open("data/work/processed/spatial/metadata/checksums_v11.1.0.json") as f:
    ck = json.load(f)
print(ck["datasets"][0]["checksum_sha256"])
```

### Bash
```bash
cat data/work/processed/spatial/metadata/spatial_manifest_v11.1.0.json
```

### Cypher
```cypher
MATCH (m:SpatialMetadata)
RETURN m.id, m.crs, m.sha256;
```

## 🛣️ Roadmap
* v11.2 — Spatial metadata anomaly detection engine  
* v11.3 — Multi-resolution metadata tiling for 3D scenes  
* v11.4 — STAC metadata auto-expansion for derived layers  
* v11.5 — Real-time metadata ingestion for Streaming STAC spatial feeds  

## 🧩 Example Metadata Manifest
```json
{
  "id": "spatial_manifest_v11.1.0",
  "domain": "spatial",
  "version": "v11.1.0",
  "datasets": [
    {
      "dataset_id": "processed_spatial_landcover_v11.1.0",
      "checksum_sha256": "sha256:df8113a72ad119a848da12520d2c59d9ade2b077e65fbcb2d50118789e818e94",
      "crs": "EPSG:4326",
      "temporal_start": "2000-01-01",
      "temporal_end": "2025-11-19",
      "fairstatus": "certified",
      "telemetry": {
        "energy_wh": 9.1,
        "co2_g": 12.9
      }
    }
  ],
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

## 🕰️ Version History
| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v11.1.0 | 2025-11-19 | `@kfm-spatial` | Initial v11 spatial metadata module; PROV-O alignment; CRS and topology metadata enforced. |

## 🔗 Footer
[⬅️ Back to Processed Spatial](../README.md) ·  
[📐 Data Architecture](../../../../../docs/ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

