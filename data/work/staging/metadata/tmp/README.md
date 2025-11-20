---
title: "🧩 Kansas Frontier Matrix — Metadata TMP Workspace (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/staging/metadata/tmp/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-work-staging-metadata-tmp-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "Internal · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11"
status: "Active / Enforced"
doc_kind: "Metadata Layer"
intent: "staging-metadata-tmp"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Metadata TMP Workspace**  
`data/work/staging/metadata/tmp/README.md`

**Purpose:**  
Define the **transient metadata harmonization workspace** used to **crosswalk, merge, and transform metadata** between **STAC**, **DCAT**, **PROV-O**, and **ISO 19115** before FAIR+CARE validation and governance registration.  
This directory supports **cross-standard interoperability**, **schema unification**, and **pre-validation ethics checks** for all KFM metadata.

</div>

## 📘 Overview
The Metadata TMP Workspace is the **first stop** for metadata entering the staging environment.  
It is used to:

* Align metadata across STAC, DCAT, PROV-O, and ISO schemas  
* Generate unified preview records for FAIR+CARE audits  
* Perform early integrity and consistency checks  
* Attach telemetry data (energy_wh, carbon_gco2e) at merge time  
* Prepare metadata for the `validation/` stage and eventual promotion to `processed/metadata/`  

Data in this directory is **ephemeral** and may change freely until promoted.

## 🗂️ Directory Layout
```plaintext
data/work/staging/metadata/tmp/
├── README.md
├── stac_to_dcat_crosswalk.json
├── provenance_mapping.json
├── metadata_merge_preview.json
├── metadata_patch_queue.json
└── metadata.json
```

## 🌍 Domain Overview
This workspace covers metadata operations for all KFM domains:

* STAC collection and item descriptors  
* DCAT dataset and distribution metadata  
* PROV-O provenance chains and relationships  
* ISO 19115 spatial and temporal descriptors  

Typical use cases:

* Building and testing STAC ↔ DCAT field mappings  
* Merging heterogeneous metadata sources into coherent previews  
* Queuing patch operations prior to governance review  
* Capturing temporary provenance for intermediate transformations  

## 🔗 Entity Requirements (PROV-O)
Each TMP session must be representable as a `prov:Entity` with:

* Unique entity ID (ASCII UUID or ID string)  
* References to applied crosswalk artifacts (for example `stac_to_dcat_crosswalk.json`, `provenance_mapping.json`)  
* Number of merged fields or records  
* SHA256 checksum of the merged preview or session bundle  
* Telemetry block (energy_wh, carbon_gco2e, validation_coverage_pct)  
* Governance status (`pending`, `in_review`)  
* Governance reference path (for example `data/reports/audit/data_provenance_ledger.json`)  
* Creation timestamp in ASCII ISO 8601 format  

TMP entities are **not immutable**; only promoted metadata in `staging/validation` and `processed/metadata` becomes permanent.

## ⚙️ Activity Requirements
TMP-level activities are `prov:Activity` instances such as:

* Schema crosswalk execution (STAC ↔ DCAT)  
* Provenance mapping enrichment (PROV-O relationships)  
* Merge and preview generation  
* Initial ethics and completeness checks  
* Checksum computation for previews  
* Patch-queue construction for governance review  

Each activity must log:

* Pipeline or tool ID and version  
* Parameter digest (ASCII hash of configuration)  
* Execution timestamp  
* Count of records and fields impacted  
* Issues detected and severity classification  
* Associated agents (human and system)  

## 🧑‍💼 Agent Requirements
Agents participating in TMP operations include:

* `@kfm-metadata` — metadata engineers and maintainers  
* `@kfm-architecture` — schema alignment and standards governance  
* `@kfm-security` — checksum integrity and access controls  
* `@faircare-council` — FAIR+CARE and CARE supervision for sensitive fields  
* `@kfm-data` — lifecycle and governance coordination  

All agents are represented as PROV-O `prov:Agent`.

## 🧪 Validation Requirements
TMP workspace outputs must undergo **basic pre-validation** before moving into `validation/`:

* Crosswalk completeness checks (expected fields mapped)  
* JSON structure validation for all JSON artifacts  
* Preliminary FAIR+CARE checks (presence of critical ethics fields)  
* Basic integrity checks (non-empty essential fields, IDs, and timestamps)  
* Checksum computation and storage in `metadata.json`  
* Telemetry recording for each TMP session  

Full FAIR+CARE certification, deep schema validation, and governance registration occur in the **staging/validation** and **staging/logs** layers.

## 📥 Retrieval Examples

### Python
```python
import json

with open("data/work/staging/metadata/tmp/metadata_merge_preview.json") as f:
    preview = json.load(f)

print(preview.get("id"), preview.get("title"))
```

### Bash
```bash
ls data/work/staging/metadata/tmp/
```

### Cypher
```cypher
MATCH (m:MetadataTmp)
RETURN m.id, m.crosswalks_applied, m.governance_status;
```

## 🛣️ Roadmap
* v11.2 — Automated field-level anomaly detection for crosswalks  
* v11.3 — Interactive diff tooling for metadata patches (graph-integrated)  
* v11.4 — Auto-suggestion of PROV-O relationships from raw logs  
* v11.5 — Streaming metadata crosswalk support for high-frequency updates  

## 🧩 Example TMP Metadata Record
```json
{
  "id": "metadata_tmp_hazards_v11.1.0",
  "crosswalks_applied": [
    "stac_to_dcat_crosswalk.json",
    "provenance_mapping.json"
  ],
  "merged_fields": 42,
  "issues_detected": 0,
  "validator": "@kfm-metadata-lab",
  "created": "2025-11-19T20:18:00Z",
  "checksum_sha256": "sha256:7f01a4ab9b38a9908deaea381a25c55b49f2506fcf0e45ad3169e4e32e1be4d4",
  "telemetry": {
    "energy_wh": 0.4,
    "co2_g": 0.5,
    "validation_coverage_pct": 100
  },
  "governance_status": "pending",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

## 🕰️ Version History
| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v11.1.0 | 2025-11-19 | `@kfm-metadata` | KFM-MDP v11 upgrade; PROV-O integration; telemetry v11 alignment; retention and TMP semantics clarified. |
| v11.0.0 | 2025-11-15 | `@kfm-metadata` | Initial migration of TMP workspace into v11 model. |
| v10.0.0 | 2025-11-09 | `@kfm-metadata` | Original TMP workspace definition with telemetry v2 and JSON-LD pre-validation. |

## 🔗 Footer
[⬅️ Back to Metadata Staging](../README.md) ·  
[📐 Data Architecture](../../../../../docs/ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
