---
title: "📊 Kansas Frontier Matrix — Processed Tabular Metadata (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/processed/tabular/metadata/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-work-processed-tabular-metadata-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0 · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11"
status: "Active / Enforced"
doc_kind: "Metadata Layer"
intent: "processed-tabular-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Processed Tabular Metadata**  
`data/work/processed/tabular/metadata/README.md`

**Purpose:**  
Define the **canonical metadata manifest layer** for all processed tabular datasets in the Kansas Frontier Matrix (KFM).  
This directory stores **PROV-O provenance chains**, **checksum manifests**, **FAIR+CARE ethics certifications**, **DCAT schema mappings**, **telemetry bundles**, and **schema-alignment definitions**, ensuring full reproducibility, auditability, and cross-catalog interoperability.

</div>

## 📘 Overview
The Processed Tabular Metadata Layer captures authoritative details on:

* Dataset lineage (entity → activity → agent)  
* Schema versioning & JSON Schema alignment  
* FAIR+CARE governance certification  
* DCAT 3.0 crosswalks and catalog registration  
* SHA256 integrity manifests  
* Telemetry metrics (energy_wh, carbon_gco2e)  
* Licensing & ethics metadata  
* Immutability guarantees for tabular datasets  

All metadata artifacts are **ASCII-safe**, **JSON-schema validated**, and **immutably versioned**.

## 🗂️ Directory Layout
```plaintext
data/work/processed/tabular/metadata/
├── README.md
├── tabular_manifest_v11.1.0.json
├── provenance_chain_v11.1.0.json
├── checksums_v11.1.0.json
├── certification_faircare_v11.1.0.json
├── telemetry_v11.1.0.json
└── schema_alignment_v11.1.0.json
```

## 🌍 Domain Overview
This metadata layer documents:

* 📊 Tabular dataset schemas (fields, datatypes, constraints)  
* 📁 Cross-domain tabular linking (environmental, treaty, socioeconomics)  
* 📜 Licensing metadata (CC-BY 4.0)  
* 🌐 DCAT Dataset definitions and JSON-LD mappings  
* 🧭 Temporal and spatial indexing when applicable  
* 🔗 Provenance relationships for derived indicators  
* ⚖️ CARE compliance for culturally sensitive tabular fields  

Designed to support multi-domain analytics, public transparency, and reproducibility.

## 🔗 Entity Requirements (PROV-O)
Each metadata entity must include:

* A unique `prov:Entity` identifier  
* SHA256 checksums for associated datasets  
* Dataset UUID reference(s)  
* Schema version reference  
* FAIR+CARE certification metadata  
* Temporal coverage (ASCII ISO)  
* Spatial descriptors (if relevant)  
* Governance ledger pointer  
* Telemetry block (energy_wh, carbon_gco2e)  

Entities must be immutable after publication.

## ⚙️ Activity Requirements
Metadata-generating activities must describe:

* ETL or tabular-processing pipeline version  
* Parameter digest (ASCII hash)  
* Validation coverage percent  
* FAIR+CARE certification ID  
* Execution timestamp  
* DCAT/STAC sync reference ID  
* Associated agents  
* Provenance chain expansion  

Activities are stored as `prov:Activity`.

## 🧑‍💼 Agent Requirements
Agents managing metadata include:

* `@kfm-tabular-lab` — structured data stewards  
* `@kfm-architecture` — schema + DCAT alignment  
* `@kfm-security` — integrity and checksum verification  
* `@faircare-council` — ethical CARE certification  
* `@kfm-data` — governance lifecycle management  

Agents are `prov:Agent`.

## 🧪 Validation Requirements
All metadata must pass:

* JSON schema validation  
* DCAT 3.0 alignment  
* FAIR+CARE certification  
* CARE-sensitive field checks  
* License verification (CC-BY 4.0)  
* Provenance chain structural validation  
* Telemetry completeness  
* Catalog registration checks (STAC/DCAT)  

Outputs stored in:

* `data/reports/validation/`  
* `data/reports/audit/`  
* `data/reports/fair/`

## 📥 Retrieval Examples

### Python
```python
import json
with open("data/work/processed/tabular/metadata/checksums_v11.1.0.json") as f:
    ck = json.load(f)
print(ck["datasets"][0]["checksum_sha256"])
```

### Bash
```bash
cat data/work/processed/tabular/metadata/tabular_manifest_v11.1.0.json
```

### Cypher
```cypher
MATCH (m:TabularMetadata)
RETURN m.id, m.schema_version, m.sha256;
```

## 🛣️ Roadmap
* v11.2 — Column-level provenance (fine-grained lineage)  
* v11.3 — Multi-domain semantic linking for Focus Mode v3  
* v11.4 — Automated metadata synthesis from tabular transformations  
* v11.5 — Real-time metadata ingestion from Streaming STAC tables  

## 🧩 Example Metadata Manifest
```json
{
  "id": "tabular_manifest_v11.1.0",
  "domain": "tabular",
  "version": "v11.1.0",
  "datasets": [
    {
      "dataset_id": "processed_tabular_environmental_indicators_v11.1.0",
      "checksum_sha256": "sha256:9b243cd94e1e72d8c1fbd94f6792203415ca8ab347316e90bdc359fa5e139f75",
      "schema_version": "v3.3.0",
      "temporal_start": "1900-01-01",
      "temporal_end": "2025-11-19",
      "fairstatus": "certified",
      "telemetry": {
        "energy_wh": 7.1,
        "co2_g": 9.8
      }
    }
  ],
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

## 🕰️ Version History
| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v11.1.0 | 2025-11-19 | `@kfm-tabular` | Initial v11 metadata module; DCAT alignment; PROV-O expansion; telemetry v11 adoption. |

## 🔗 Footer
[⬅️ Back to Processed Tabular](../README.md) ·  
[📐 Data Architecture](../../../../../docs/ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

