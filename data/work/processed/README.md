---
title: "🧾 Kansas Frontier Matrix — Processed Data Layer (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/processed/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-work-processed-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0 · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11"
status: "Active / Enforced"
doc_kind: "Data Layer"
intent: "processed-data"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Processed Data Layer**  
`data/work/processed/README.md`

**Purpose:**  
Define the **final, certified, canonical datasets** produced by the Kansas Frontier Matrix ETL, AI validation, schema alignment, and FAIR+CARE governance workflows.  
The Processed Data Layer is the authoritative source for **publication-ready, checksum-verified, provenance-certified** datasets used across STAC, DCAT, Focus Mode, and the KFM knowledge graph.

</div>

## 📘 Overview
The Processed Data Layer is where datasets become **immutable scientific assets**.  
All records here must pass:

* Full schema validation  
* FAIR+CARE certification  
* Provenance chain completion  
* Telemetry accounting (energy_wh, carbon_gco2e)  
* Checksum/manifest reconciliation  
* Governance ledger registration  
* STAC/DCAT synchronization  

This layer serves as the **release buffer** for official public datasets.

## 🗂️ Directory Layout
```plaintext
data/work/processed/
├── README.md
├── climate/
├── hazards/
├── hydrology/
├── landcover/
├── spatial/
├── tabular/
└── metadata/
```

## 🌍 Domain Overview
Domains supported by the Processed Data Layer:

* 🌡️ Climate — standardized climatic indicators and summaries  
* ⚠️ Hazards — tornado, drought, seismic, flood, severe weather outputs  
* 🌊 Hydrology — streamflow, aquifers, watershed processed layers  
* 🗺️ Spatial — harmonized raster/vector datasets, tiling outputs  
* 🗂️ Tabular — aggregated and normalized reference datasets  
* 🧮 Metadata — certification manifests, provenance chains, validation bundles  

All outputs are UUID-tagged and PROV-O aligned.

## 🔗 Entity Requirements (PROV-O)
Each processed dataset must include:

* `prov:Entity` classification  
* Source reference path(s)  
* Checksum_sha256 mapped to manifest entry  
* Telemetry block (energy_wh, carbon_gco2e)  
* FAIR+CARE tags  
* Licensing compliance (CC-BY 4.0)  
* Governance reference ID  
* Creation timestamp in ASCII ISO 8601 format  

Records stored in `metadata/` act as canonical certification manifests.

## ⚙️ Activity Requirements
Processed outputs must record:

* Pipeline name + version  
* Configuration digest  
* Validation summary reference  
* Certification reference (FAIR+CARE)  
* Dependency chain (prov:wasDerivedFrom)  
* Promotion timestamp  

All activities are PROV-O `prov:Activity`.

## 🧑‍💼 Agent Requirements
Agents involved:

* `@kfm-processed` — publishing authority  
* `@kfm-architecture` — schema alignment  
* `@kfm-security` — checksum integrity  
* `@faircare-council` — ethical/CARE oversight  
* `@kfm-data` — staging-to-processed promotion  

Agents stored as PROV-O `prov:Agent`.

## 🧪 Validation Requirements
Validation steps required prior to entry into `processed/`:

* Schema validation (tabular + spatial)  
* Geospatial topology checks (for spatial datasets)  
* Field type enforcement  
* FAIR+CARE certification  
* Telemetry accounting  
* Checksum verification  
* Provenance ledger append-only reference update  
* Metadata alignment with DCAT/STAC  

Validation outputs stored in:

* `data/reports/validation/`  
* `data/reports/audit/`  
* `data/reports/fair/`

## 📥 Retrieval Examples

### Python
```python
import json
with open("data/work/processed/metadata/hazards_manifest.json") as f:
    meta = json.load(f)
print(meta["checksum_sha256"])
```

### Bash
```bash
ls data/work/processed/climate/
```

### Cypher
```cypher
MATCH (p:ProcessedDataset)
RETURN p.id, p.domain, p.checksum_sha256;
```

## 🛣️ Roadmap
* v11.2 — AI-assisted post-validation anomaly detection  
* v11.3 — Spatial-temporal consistency scoring  
* v11.4 — Autonomous release cadence to STAC/DCAT   
* v11.5 — Long-term retention vault with sustainability tiering  

## 🧩 Example Processed Metadata Record
```json
{
  "id": "processed_hazards_summary_v11.1.0",
  "domain": "hazards",
  "source_stage": "data/work/staging/hazards/",
  "records_total": 55129,
  "fairstatus": "certified",
  "checksum_sha256": "sha256:9845d1e7bfe321ceac6499f71ef2b1db2ba112cedf91ceded18a9048cf38a11a",
  "license": "CC-BY 4.0",
  "validator": "@kfm-hazard-lab",
  "telemetry": {
    "energy_wh": 14.2,
    "co2_g": 18.3,
    "validation_coverage_pct": 100
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json",
  "created": "2025-11-19T18:30:00Z"
}
```

## 🕰️ Version History
| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v11.1.0 | 2025-11-19 | `@kfm-processed` | Full v11 upgrade, PROV-O hardening, checksum alignment, directory updates. |
| v11.0.0 | 2025-11-15 | `@kfm-processed` | Migrated to v11 metadata model. |
| v10.0.0 | 2025-11-09 | `@kfm-processed` | Initial v10 processed layer definition. |

## 🔗 Footer
[⬅️ Back to Work Layer](../README.md) ·  
[📐 Data Architecture](../../../docs/ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)
