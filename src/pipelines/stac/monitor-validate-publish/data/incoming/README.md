---
title: "📥 Kansas Frontier Matrix — Incoming STAC Batches (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/data/incoming/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-stac-incoming-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📥 **Kansas Frontier Matrix — Incoming STAC Batches**  
`src/pipelines/stac/monitor-validate-publish/data/incoming/README.md`

**Purpose:**  
Describe the storage, retention, governance rules, and lifecycle of **raw incoming STAC Item batches** pulled by the STAC Monitor → Validate → Publish orchestrator.  
These files are **untrusted**, **unvalidated**, and represent the very first stage of the ingestion pipeline.

<img alt="Incoming" src="https://img.shields.io/badge/STAC_Incoming-Raw-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Checked_at_Validation-orange"/>
<img alt="MCP" src="https://img.shields.io/badge/MCP-DL_v6.3-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Transient-success"/>

</div>

---

## 📘 Overview

`incoming/` contains **raw STAC Item Search results** retrieved from external provider STAC APIs.

Characteristics:

- Fully **untrusted** data  
- Written directly from `monitor.py`  
- Structured as **timestamped folders**  
- Validated immediately via Great Expectations  
- NEVER published or consumed directly  
- Automatically cleaned once validated or quarantined  

This directory is the “inbox” of the entire STAC ingestion pipeline.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/incoming/
├── README.md
└── <timestamp>/
    └── items.jsonl             # Raw STAC Items (per polling cycle)
~~~~~

Example:

~~~~~text
2025-11-14T05-00-02Z/items.jsonl
2025-11-14T06-00-00Z/items.jsonl
~~~~~

---

## 🧩 Data Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Poll STAC API<br/>ETag / If-None-Match"] --> B["incoming/<ts>/items.jsonl"]
  B --> C["Great Expectations Validation<br/>stac_item_suite"]
  C -->|PASS| D["data/stac/published/**"]
  C -->|FAIL| E["data/quarantine/<ts>/**"]
  D --> F["Neo4j Hydration + Catalog Updates"]
  E --> G["GitHub Issue + Telemetry + Governance Review"]
~~~~~

---

## 📥 Incoming Batch Requirements

Each polling cycle writes:

- 1 **timestamped folder**  
- 1 `items.jsonl` file containing:
  - One STAC Item per line  
  - Raw JSON identical to API response  
  - No local normalization  
  - No governance metadata  

The orchestrator ensures:

- Atomic write  
- ETag cache update  
- No race conditions in timestamp generation  

---

## ⚠️ Important: Raw Data Is Untrusted

Incoming data **must not**:

- Be used for graph hydration  
- Be displayed in UI  
- Be treated as authoritative metadata  
- Be added to published STAC catalogs  
- Be included in Focus Mode reasoning  

Only after **schema + GE + CARE validation** can data progress downstream.

---

## 🛑 Validation

Immediately after writing an incoming batch, the orchestrator runs:

- JSON Schema validation  
- Great Expectations suite:
  - Field presence  
  - Cloud cover / proj fields  
  - Asset role/MIME checks  
  - CARE label existence  
  - Governance constraints  
- CARE masking rules  
- Link integrity validation  
- Provenance placeholder checks  

Outcome determines whether the batch proceeds to:

- `data/stac/published/`  
- `data/stac/quarantine/`

---

## 🧯 Failure Handling

If validation fails:

1. Batch is **moved** to:

   ~~~~~text
   data/quarantine/<timestamp>/
   ~~~~~

2. GE summary saved as:

   ~~~~~text
   last_failure_summary.md
   ~~~~~

3. Data Docs snapshot included:

   ~~~~~text
   datadocs/
   ~~~~~

4. GitHub Issue auto-created  
5. Telemetry updated with failure details  

---

## 🕒 Retention Policy

| Directory | Retention | Reason |
|-----------|-----------|--------|
| `incoming/` | **7 days** | Minimize unvalidated risk |
| `quarantine/` | **180 days** | CARE/FAIR re-audit requirement |

Incoming data is automatically removed once:

- Validated  
- or moved to quarantine  
- or expired per retention cycle  

---

## 📡 Telemetry Binding

Each incoming batch generates telemetry including:

- `timestamp`  
- `incoming_count`  
- `etag_used`  
- `fetch_latency_ms`  
- `schema_errors`  
- `care_errors`  
- `items_polled`  
- `jsonl_size_kb`  
- Energy/CO₂ metrics  

Telemetry aggregated into:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Local Inspection

Inspect a raw polled batch:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/incoming/<timestamp>/items.jsonl
~~~~~

Count items:

~~~~~bash
wc -l src/pipelines/stac/monitor-validate-publish/data/incoming/<timestamp>/items.jsonl
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Added complete documentation for incoming STAC batch storage, retention, and validation flow. |

---

<div align="center">

**Kansas Frontier Matrix — Incoming STAC Batches**  
Untrusted Input × Strict Validation × FAIR+CARE Gatekeeping  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to STAC Orchestrator Data Layer](../README.md)

</div>
