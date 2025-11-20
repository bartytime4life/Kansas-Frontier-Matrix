---
title: "🧾 Kansas Frontier Matrix — Processed Climate Metadata (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/processed/climate/metadata/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-work-processed-climate-metadata-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0 · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11"
status: "Active / Enforced"
doc_kind: "Metadata Layer"
intent: "processed-climate-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Processed Climate Metadata**  
`data/work/processed/climate/metadata/README.md`

**Purpose:**  
Define the **canonical metadata manifests** for all processed climate datasets in KFM.  
This directory stores **provenance manifests**, **checksum registries**, **FAIR+CARE certification summaries**, **telemetry bundles**, and **schema alignment metadata**, ensuring full traceability across KFM’s climate workflows.

</div>

## 📘 Overview
The Processed Climate Metadata Layer provides:

* Provenance lineage for all climate datasets  
* Immutable checksum manifests (SHA256 only)  
* FAIR+CARE certification artifacts  
* Telemetry sustainability metrics  
* DCAT/STAC metadata synchronization blocks  
* PROV-O encoded entity → activity → agent mappings  
* AI validation and explainability audit references  

This folder is the **source of truth** for all climate metadata entering catalogs, the graph, and Focus Mode.

## 🗂️ Directory Layout
```plaintext
data/work/processed/climate/metadata/
├── README.md
├── climate_manifest_v11.1.0.json
├── provenance_chain_v11.1.0.json
├── checksums_v11.1.0.json
├── certification_faircare_v11.1.0.json
├── telemetry_v11.1.0.json
└── schema_alignment_v11.1.0.json
```

## 🌍 Domain Overview
Metadata in this directory covers:

* 🌡️ Climate dataset identity  
* ⏱️ Temporal and spatial extents  
* 🧭 Coordinate systems (EPSG definitions)  
* 📐 Schema structure and field-level mappings  
* 🔗 Provenance relationships (derived-from, validated-by)  
* 📊 Certification and ethics records  
* 🔒 Integrity & governance checkpoints  

Every file is ASCII-safe and validated against JSON schemas.

## 🔗 Entity Requirements (PROV-O)
Each metadata manifest must encode:

* `prov:Entity` identifiers  
* Dataset UUID  
* SHA256 checksum  
* Derived-from lineage (staging → processed)  
* Temporal boundaries  
* Spatial bbox  
* FAIR+CARE tags  
* Telemetry summary  

All metadata files must be immutable after publication.

## ⚙️ Activity Requirements
Activities contributing to metadata generation:

* ETL transformations  
* Climate harmonization workflows  
* CF convention compliance checks  
* FAIR+CARE certification operations  
* Provenance ledger updates  
* STAC/DCAT synchronization pipelines  

Each activity must declare:

* Pipeline name & version  
* Parameter digest (ASCII hash)  
* Validation coverage percent  
* Execution timestamp  
* Associated agent  

## 🧑‍💼 Agent Requirements
Agents responsible for metadata:

* `@kfm-climate-lab` — primary climate processing  
* `@kfm-architecture` — schema & metadata structure  
* `@kfm-security` — checksum & manifest verification  
* `@faircare-council` — ethics oversight  
* `@kfm-data` — governance lifecycle management  

Each agent is a PROV-O `prov:Agent`.

## 🧪 Validation Requirements
Before climate metadata is published, it must pass:

* JSON schema validation  
* Checksum reconciliation  
* FAIR+CARE certification checks  
* PROV-O structural validation  
* ISO 19115 metadata alignment  
* STAC/DCAT metadata mapping  
* Telemetry completeness  

Validation output is stored in:

* `data/reports/validation/`  
* `data/reports/audit/`  
* `data/reports/fair/`

## 📥 Retrieval Examples

### Python
```python
import json
with open("data/work/processed/climate/metadata/checksums_v11.1.0.json") as f:
    data = json.load(f)
print(data["datasets"][0]["checksum_sha256"])
```

### Bash
```bash
cat data/work/processed/climate/metadata/climate_manifest_v11.1.0.json
```

### Cypher (graph import)
```cypher
MATCH (m:ClimateMetadata)
RETURN m.id, m.sha256, m.fair_status;
```

## 🛣️ Roadmap
* v11.2 — AI-generated metadata anomaly detection  
* v11.3 — Climate metadata tiling alignment for Focus Mode  
* v11.4 — Automated CF/ISO metadata merging engine  
* v11.5 — Streaming STAC metadata ingestion for real-time climate updates  

## 🧩 Example Metadata Manifest
```json
{
  "id": "climate_manifest_v11.1.0",
  "domain": "climate",
  "version": "v11.1.0",
  "datasets": [
    {
      "dataset_id": "processed_climate_summary_v11.1.0",
      "checksum_sha256": "sha256:073a1f9c2f194b397dd412edb8c8756f68baaf0e5ab379ed91323d9722aa98cc",
      "temporal_start": "1900-01-01",
      "temporal_end": "2025-11-19",
      "fairstatus": "certified",
      "telemetry": {
        "energy_wh": 14.7,
        "co2_g": 19.2
      }
    }
  ],
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

## 🕰️ Version History
| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v11.1.0 | 2025-11-19 | `@kfm-climate` | Initial metadata module aligned to KFM-MDP v11; manifests consolidated; PROV-O mappings added. |

## 🔗 Footer
[⬅️ Back to Processed Climate](../README.md) ·  
[📐 Data Architecture](../../../../../docs/ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

