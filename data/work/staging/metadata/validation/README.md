---
title: "🧪 Kansas Frontier Matrix — Metadata Validation Workspace (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/staging/metadata/validation/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-work-staging-metadata-validation-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "Internal · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11"
status: "Active / Enforced"
doc_kind: "Validation Layer"
intent: "staging-metadata-validation"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Metadata Validation Workspace**  
`data/work/staging/metadata/validation/README.md`

**Purpose:**  
Define the **validation-phase metadata workspace** where all KFM metadata undergo rigorous **schema checks**, **FAIR+CARE ethics validation**, **checksum verification**, **STAC/DCAT conformance checks**, **PROV-O structural validation**, and **telemetry accounting** prior to promotion to the Processed Metadata Layer.

</div>

## 📘 Overview
This workspace performs the **formal validation cycle** for metadata produced in the TMP workspace.  
It provides:

* JSON-schema validation for all metadata artifacts  
* FAIR+CARE audit execution  
* PROV-O structural and relationship verification  
* STAC and DCAT crosswalk validation  
* Checksum and integrity verification  
* Governance review and certification readiness checks  
* Telemetry v11 energy/carbon accounting  
* Pre-promotion provenance chain stamping  

All validation results produced here are immutable once recorded.

## 🗂️ Directory Layout
```plaintext
data/work/staging/metadata/validation/
├── README.md
├── schema_validation_summary.json
├── faircare_metadata_audit.json
├── stac_link_check.log
└── metadata_qa_summary.md
```

## 🌍 Domain Overview
This validation workspace covers:

* STAC collection/item metadata  
* DCAT dataset/distribution metadata  
* PROV-O lineage metadata  
* Metadata derived from climate, hazards, hydrology, spatial, and tabular domains  
* CARE-sensitive metadata structures requiring ethical review  

Outputs here inform the **promotion decision** for entry into:

`data/work/processed/metadata/`

## 🔗 Entity Requirements (PROV-O)
All metadata validation artifacts must map to a `prov:Entity` with:

* Entity ID (ASCII UUID or ID string)  
* Associated TMP entity reference  
* SHA256 checksum of the validated file  
* Validation status (`passed`, `failed`, `in_review`)  
* FAIR+CARE certification state  
* Schema version  
* Governance reference pointer  
* Telemetry block (energy_wh, carbon_gco2e, validation_coverage_pct)  
* Timestamp (ASCII ISO 8601)  

Entities recorded here become **immutable**.

## ⚙️ Activity Requirements
Validation-phase activities include:

* Schema validation runs  
* Ethics + FAIR+CARE audit execution  
* STAC/DCAT link-check and field crosswalk evaluation  
* Checksum verification and manifest reconciliation  
* Provenance chain restructuring and validation  
* Governance pre-certification workflows  
* Telemetry assignment  

Each `prov:Activity` must record:

* Pipeline ID and version  
* Parameter digest (ASCII hash)  
* Execution timestamp range  
* Validation coverage percent  
* Issues detected (warnings, errors)  
* Resulting status (`passed`, `failed`, `in_review`)  
* Agents involved  

## 🧑‍💼 Agent Requirements
Agents participating in validation:

* `@kfm-metadata-lab` — validation execution and schema QA  
* `@kfm-architecture` — schema/standard alignment oversight  
* `@kfm-security` — checksum and integrity verification  
* `@faircare-council` — ethical and cultural validation  
* `@kfm-data` — governance pre-certification management  

Agents are recorded under PROV-O `prov:Agent`.

## 🧪 Validation Requirements
Required checks before metadata can be promoted:

* JSON schema conformance  
* FAIR+CARE ethics validation  
* DCAT field presence and cardinality validation  
* STAC link and SKU conformity  
* Checksum confirmation  
* Provenance graph structural correctness  
* Telemetry completeness  
* License review (e.g., CC-BY 4.0 readiness)  
* CARE-sensitive metadata screening  

Results stored under:

* `data/reports/validation/`  
* `data/reports/fair/`  
* `data/reports/audit/`

## 📥 Retrieval Examples

### Python
```python
import json
with open("data/work/staging/metadata/validation/schema_validation_summary.json") as f:
    summary = json.load(f)
print(summary.get("schema_status"))
```

### Bash
```bash
cat data/work/staging/metadata/validation/faircare_metadata_audit.json
```

### Cypher
```cypher
MATCH (m:MetadataValidation)
RETURN m.id, m.validation_status, m.fairstatus, m.checksum_sha256;
```

## 🛣️ Roadmap
* v11.2 — Automated ontology alignment validator  
* v11.3 — Fine-grained CARE-sensitive field validator  
* v11.4 — Multi-metadata STAC/DCAT consistency checker  
* v11.5 — Predictive metadata integrity scoring for autonomous promotion decisions  

## 🧩 Example Metadata Validation Record
```json
{
  "id": "metadata_validation_climate_v11.1.0",
  "source_tmp_ref": "data/work/staging/metadata/tmp/metadata_merge_preview.json",
  "validation_status": "passed",
  "checksum_sha256": "sha256:d7c045428aa53f06ae18c247c8253492122abf82cb0d12a50c41804d3cb32b77",
  "fairstatus": "certified",
  "schema_version": "v3.3.0",
  "telemetry": {
    "energy_wh": 0.5,
    "co2_g": 0.7,
    "validation_coverage_pct": 100
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json",
  "created": "2025-11-19T20:25:00Z"
}
```

## 🕰️ Version History
| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v11.1.0 | 2025-11-19 | `@kfm-metadata` | Full KFM-MDP v11 upgrade; schema validation expansion; PROV-O linking; telemetry v11 integration. |
| v11.0.0 | 2025-11-15 | `@kfm-metadata` | Initial v11 validation workspace module. |
| v10.0.0 | 2025-11-09 | `@kfm-metadata` | Original metadata validation workspace definition. |

## 🔗 Footer
[⬅️ Back to Metadata Staging](../README.md) ·  
[📐 Data Architecture](../../../../../docs/ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
