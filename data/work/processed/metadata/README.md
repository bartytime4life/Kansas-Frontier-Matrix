---
title: "🧾 Kansas Frontier Matrix — Processed Metadata Layer (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/processed/metadata/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-work-processed-metadata-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0 · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11"
status: "Active / Enforced"
doc_kind: "Metadata Layer"
intent: "processed-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Processed Metadata Layer**  
`data/work/processed/metadata/README.md`

**Purpose:**  
Define the **final, canonical, FAIR+CARE-certified metadata layer** for all processed KFM datasets.  
This directory stores **STAC/DCAT/PROV-O aligned metadata**, **checksum manifests**, **FAIR+CARE certifications**, **telemetry bundles**, and **governance-linked provenance chains**, ensuring complete transparency, reproducibility, and open scientific stewardship.

</div>

## 📘 Overview
The Processed Metadata Layer maintains authoritative metadata describing:

* Dataset lineage  
* Schema mappings  
* FAIR+CARE ethics certification  
* SBOM + checksum integrity  
* Telemetry impact (energy_wh, carbon_gco2e)  
* STAC 1.0 and DCAT 3.0 synchronization  
* PROV-O entity/activity/agent structure  
* Catalog-ready publication metadata  

All files within this layer are **immutable**, **ASCII-safe**, and validated under strict KFM metadata schemas.

## 🗂️ Directory Layout
```plaintext
data/work/processed/metadata/
├── README.md
├── stac_collection_v11.1.0.json
├── provenance_manifest_v11.1.0.json
├── governance_certification_v11.1.0.json
├── metadata_summary_v11.1.0.csv
└── metadata_v11.1.0.json
```

## 🌍 Domain Overview
Metadata in this directory covers:

* STAC Collection definitions for processed datasets  
* DCAT Dataset metadata for downstream catalogs  
* PROV-O lineage across all processed domains (climate, hazards, hydrology, spatial, tabular)  
* Immutability guarantees and retention policies  
* CARE-sensitive fields for cultural or environmentally sensitive datasets  
* Licensing and attribution metadata (CC-BY 4.0)  

This folder supports KFM’s full-stack metadata journey:

**processed data → provenance → catalogs → graph → UI → Story Nodes**

## 🔗 Entity Requirements (PROV-O)
Every metadata file must declare:

* Unique `prov:Entity` ID  
* SHA256 checksum  
* Dataset associations (entity → dataset)  
* Schema version  
* FAIR+CARE certification status  
* Telemetry data (energy_wh, carbon_gco2e)  
* Governance ledger reference  
* Temporal and spatial metadata when relevant  

Entities must remain immutable once published.

## ⚙️ Activity Requirements
Metadata generation activities must record:

* Pipeline version  
* Configuration digest (ASCII hash)  
* Validation coverage  
* FAIR+CARE certification ID  
* Execution timestamp  
* STAC/DCAT sync reference  
* Associated agents  

All activities are encoded as `prov:Activity`.

## 🧑‍💼 Agent Requirements
Agents responsible for metadata include:

* `@kfm-metadata` — metadata stewards  
* `@kfm-architecture` — schema and standards alignment  
* `@kfm-security` — checksum/integrity validation  
* `@faircare-council` — ethics verification  
* `@kfm-data` — lifecycle governance and catalog management  

Agents must be `prov:Agent`.

## 🧪 Validation Requirements
Before metadata enters this layer, it must pass:

* JSON schema validation  
* STAC/DCAT compliance  
* FAIR+CARE certification  
* CARE-review if sensitive domains present  
* Provenance chain validation  
* Checksum/manifest reconciliation  
* Telemetry completeness checks  
* Licensing verification (CC-BY 4.0)  

Validation outputs stored in:

* `data/reports/validation/`  
* `data/reports/audit/`  
* `data/reports/fair/`

## 📥 Retrieval Examples

### Python
```python
import json
with open("data/work/processed/metadata/stac_collection_v11.1.0.json") as f:
    coll = json.load(f)
print(coll["id"])
```

### Bash
```bash
cat data/work/processed/metadata/provenance_manifest_v11.1.0.json
```

### Neo4j Cypher
```cypher
MATCH (m:ProcessedMetadata)
RETURN m.id, m.checksum_sha256, m.fair_status;
```

## 🛣️ Roadmap
* v11.2 — Metadata anomaly detection engine  
* v11.3 — Cross-domain metadata alignment index  
* v11.4 — Automated metadata tiling for 3D/temporal UI layers  
* v11.5 — Streaming STAC metadata ingestion for dynamic domains  

## 🧩 Example Metadata Manifest
```json
{
  "id": "processed_metadata_manifest_v11.1.0",
  "domain": "metadata",
  "version": "v11.1.0",
  "datasets": [
    {
      "dataset_id": "processed_hazards_composite_v11.1.0",
      "checksum_sha256": "sha256:1fa094d61c1eb1a7a568fb2189e5fbcdf1f4947564f5cccb2de39bcf4cbab843",
      "fairstatus": "certified",
      "temporal_start": "1950-01-01",
      "temporal_end": "2025-11-19",
      "telemetry": {
        "energy_wh": 12.1,
        "co2_g": 16.4
      }
    }
  ],
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

## 🕰️ Version History
| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v11.1.0 | 2025-11-19 | `@kfm-metadata` | Full v11 upgrade; STAC/DCAT/PROV-O harmonization; telemetry v11 alignment; consolidated manifests. |
| v11.0.0 | 2025-11-15 | `@kfm-metadata` | Initial transition to v11 metadata model. |
| v10.0.0 | 2025-11-09 | `@kfm-metadata` | Original processed metadata layer definition. |

## 🔗 Footer
[⬅️ Back to Processed Layer](../README.md) ·  
[📐 Data Architecture](../../../../docs/ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
