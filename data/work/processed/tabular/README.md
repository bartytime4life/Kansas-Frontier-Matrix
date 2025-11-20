---
title: "📊 Kansas Frontier Matrix — Processed Tabular Data (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/processed/tabular/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-work-processed-tabular-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0 · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11"
status: "Active / Enforced"
doc_kind: "Processed Dataset Layer"
intent: "processed-tabular"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Processed Tabular Data**  
`data/work/processed/tabular/README.md`

**Purpose:**  
Define the authoritative **processed tabular dataset layer** for the Kansas Frontier Matrix.  
This directory contains **FAIR+CARE-certified**, **checksum-verified**, **schema-aligned**, and **provenance-documented** structured tables used across **AI analytics**, **Focus Mode v3**, **graph ingest**, **DCAT catalogs**, and **public open-data releases**.

</div>

## 📘 Overview
The Processed Tabular Data Layer holds all final structured datasets generated after:

* Deterministic ETL pipelines  
* FAIR+CARE certification  
* Schema normalization & DCAT 3.0 alignment  
* Telemetry v11 sustainability tracking  
* PROV-O lineage encoding  
* Checksum & SBOM-backed verification  
* Governance approval  

All datasets here are ready for open publication, long-term archival, and integration into KFM’s knowledge graph.

## 🗂️ Directory Layout
```plaintext
data/work/processed/tabular/
├── README.md
├── environmental_indicators_v11.1.0.csv
├── treaties_aggregated_v11.1.0.csv
├── socioeconomic_summary_v11.1.0.parquet
└── metadata/
```

## 🌍 Domain Overview
Tabular datasets capture:

* 🌿 Environmental indicators (climate, hydrology, hazards)  
* 📜 Treaty and historical metadata crosswalks  
* 📈 Socioeconomic aggregates  
* 🧭 Mixed-domain composite indicators  
* 🧪 Derived metrics for Focus Mode and analytics  

All files are schema-validated and machine-readable (CSV or Parquet).

## 🔗 Entity Requirements (PROV-O)
Every processed tabular dataset must include:

* Unique `prov:Entity` identifier  
* Stable dataset UUID  
* SHA256 checksum  
* Schema version  
* FAIR+CARE certification metadata  
* Telemetry block (energy_wh, carbon_gco2e)  
* DCAT metadata fields (theme, keywords, temporal, spatial)  
* Provenance chain (`prov:wasDerivedFrom`)  
* Governance ledger reference  
* ASCII-only timestamp (ISO 8601)  

Entities are immutable after publication.

## ⚙️ Activity Requirements
Generation of processed tabular datasets must capture:

* ETL pipeline name & version  
* Parameter digest (ASCII hash)  
* Validation coverage  
* FAIR+CARE certification ID  
* Execution timestamp  
* DCAT/STAC synchronization event  
* SBOM & checksum registry reference  
* Associated human+AI agents  

Activities are encoded as PROV-O `prov:Activity`.

## 🧑‍💼 Agent Requirements
Agents overseeing tabular workflows:

* `@kfm-tabular-lab` — structured data stewards  
* `@kfm-architecture` — schema + DCAT alignment  
* `@kfm-security` — checksum/integrity validation  
* `@faircare-council` — ethics governance  
* `@kfm-data` — lifecycle + metadata coordination  

Agents are stored as `prov:Agent`.

## 🧪 Validation Requirements
Before tabular datasets enter this layer, they must pass:

* DCAT 3.0 schema alignment  
* JSON schema structural validation  
* FAIR+CARE certification  
* Telemetry completion  
* Provenance chain validation  
* Checksum/manifest verification  
* Licensing verification (CC-BY 4.0)  
* CARE checks for culturally sensitive indicators  

Validation outputs stored in:

* `data/reports/validation/`  
* `data/reports/audit/`  
* `data/reports/fair/`

## 📥 Retrieval Examples

### Python
```python
import pandas as pd
df = pd.read_csv("data/work/processed/tabular/environmental_indicators_v11.1.0.csv")
print(df.head())
```

### Bash
```bash
ls data/work/processed/tabular/
```

### Cypher (graph linkage)
```cypher
MATCH (t:ProcessedTable)
RETURN t.id, t.schema_version, t.checksum_sha256;
```

## 🛣️ Roadmap
* v11.2 — Composite environmental scoring engine  
* v11.3 — Multi-domain tabular linking for Focus Mode v3  
* v11.4 — Column-level provenance (fine-grained lineage)  
* v11.5 — Real-time Streaming STAC support for rapidly updated tables  

## 🧩 Example Processed Tabular Metadata Record
```json
{
  "id": "processed_tabular_environmental_indicators_v11.1.0",
  "domain": "tabular",
  "source_stage": "data/work/staging/tabular/",
  "records_total": 58914,
  "schema_version": "v3.3.0",
  "checksum_sha256": "sha256:0402e449e975f3e189a625db4cbdd0b0a67f7e64790dc4f01cc32c84d6f40435",
  "fairstatus": "certified",
  "license": "CC-BY 4.0",
  "validator": "@kfm-tabular-lab",
  "telemetry": {
    "energy_wh": 7.1,
    "co2_g": 9.8,
    "validation_coverage_pct": 100
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json",
  "created": "2025-11-19T19:52:00Z"
}
```

## 🕰️ Version History
| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v11.1.0 | 2025-11-19 | `@kfm-tabular` | Full KFM-MDP v11 upgrade; schema harmonization; PROV-O alignment; telemetry v11 integration. |
| v11.0.0 | 2025-11-15 | `@kfm-tabular` | Initial v11 migration of tabular layer. |
| v10.0.0 | 2025-11-09 | `@kfm-tabular` | Original processed tabular dataset definition. |

## 🔗 Footer
[⬅️ Back to Processed Layer](../README.md) ·  
[📐 Data Architecture](../../../../docs/ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
