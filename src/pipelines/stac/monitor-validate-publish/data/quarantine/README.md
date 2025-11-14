---
title: "🧯 Kansas Frontier Matrix — STAC Quarantine Zone (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/data/quarantine/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-stac-quarantine-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧯 **Kansas Frontier Matrix — STAC Quarantine Zone**  
`src/pipelines/stac/monitor-validate-publish/data/quarantine/README.md`

**Purpose:**  
Define the **governance-driven quarantine workflow** for STAC Items that **fail validation**, **violate FAIR+CARE rules**, **breach schema integrity**, or **raise sovereignty/cultural sensitivity issues**.  
This directory stores **blocked**, **unpublishable**, **unsafe**, or **ethically restricted** STAC batches for review by the FAIR+CARE Council and pipeline maintainers.

<img alt="Quarantine" src="https://img.shields.io/badge/State-Quarantined-critical"/>
<img alt="Governance" src="https://img.shields.io/badge/FAIR%2BCARE-Review_Required-orange"/>
<img alt="Validation" src="https://img.shields.io/badge/GE_Failed-red"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Blocked-success"/>

</div>

---

## 📘 Overview

`quarantine/` is the **high-security containment area** for any STAC Items that fail one or more checks in the **Monitor → Validate → Publish** pipeline:

- JSON schema mismatch  
- Great Expectations suite failure  
- KFM extension failure (checksum, provenance, ingest_version)  
- CARE label errors  
- Sovereignty violations (tribal territory conflicts, unmasked sensitive geometries)  
- Missing/invalid projection metadata  
- Broken STAC links or assets  
- Invalid MIME types  
- Metadata corruption  

Quarantined data **must NEVER** be published, indexed, graphed, or exposed to the UI.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/quarantine/
├── README.md
└── <timestamp>/
    ├── items.jsonl                 # Failed batch (unmodified)
    ├── last_failure_summary.md     # Human-readable diagnostics
    ├── datadocs/                   # Snapshot of GE Data Docs (HTML)
    └── metadata.json               # Governance + telemetry summary
~~~~~

Example:

~~~~~text
2025-11-14T06-00-00Z/
  items.jsonl
  last_failure_summary.md
  datadocs/
  metadata.json
~~~~~

---

## 🧩 Quarantine Workflow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Incoming STAC Batch"] --> B["GE Validation<br/>stac_item_suite"]
  B -->|FAIL| C["Move to Quarantine<br/>data/quarantine/<ts>"]
  C --> D["Write last_failure_summary.md"]
  C --> E["Store Data Docs Snapshot<br/>datadocs/"]
  C --> F["Generate metadata.json"]
  C --> G["Open GitHub Issue<br/>FAIR+CARE Council Notified"]
  G --> H["Governance Review<br/>CARE · Sovereignty · Schema"]
~~~~~

---

## ❌ Reasons for Quarantine

A batch enters quarantine upon **any** of the following:

### 🟥 Schema Failures
- Not valid STAC 1.0 Item structure  
- Missing required fields (id, geometry, properties, assets, links)  
- Invalid geometry or CRS mismatch

### 🟥 Great Expectations Failures
- Cloud cover outside [0,100]  
- Missing projection fields for rasters  
- Invalid MIME types  
- Missing ingest metadata (kfm:ingest_version)  
- Broken asset `href`s

### 🟧 FAIR+CARE Violations
- Missing or invalid `kfm:care_label`  
- Sensitive datasets lacking masking  
- Restricted datasets containing precise coordinates  
- Archaeological/tribal land intersections without sovereignty notes  
- CARE labeling conflicts

### 🟨 Provenance / Lineage Errors
- Invalid checksum  
- Missing lineage reference  
- Collision with previous published version

### 🟦 Structural Validation Errors
- Duplicate IDs  
- Link relations missing (`self`, `collection`, `root`)  
- Missing asset roles  

### 🟪 Provider Errors
- Malformed STAC provided by external API  
- Temporal ranges out of bounds  
- Missing EO/SAR metadata for applicable sensors  

---

## 📄 Required Files Per Quarantined Batch

### 1. `items.jsonl`
The **raw** Items exactly as polled from STAC API.

### 2. `last_failure_summary.md`
Human-readable failure summary containing:

- Schema mismatches  
- Expectation suite failures  
- CARE violations  
- Governance notes  
- Suggested remediation  
- Count of failures per rule  

### 3. `datadocs/`
Snapshot of Great Expectations Data Docs:

- HTML reports (WCAG-compliant)
- Links to failed expectations
- Schema mismatch visualizers

### 4. `metadata.json`
Governance + telemetry metadata, e.g.:

~~~~~json
{
  "timestamp": "2025-11-14T06:00:00Z",
  "items_total": 87,
  "items_failed": 87,
  "error_classes": ["schema", "care", "projection"],
  "care_violations": 42,
  "governance_status": "blocked",
  "quarantine_path": "data/quarantine/2025-11-14T06-00-00Z/",
  "telemetry_ref": "releases/v10.3.0/focus-telemetry.json"
}
~~~~~

---

## 🧭 Governance Integration

All quarantined batches MUST undergo governance review.

Triggers:

- GitHub Issue is automatically opened  
- FAIR+CARE Council is notified  
- Governance metadata appended to:

~~~~~text
../../../../../docs/reports/audit/versioning_ledger.json
~~~~~

Governance reviewers assess:

- Cultural/tribal sensitivity  
- CARE compliance  
- Ecological impact  
- Licensing / redistribution constraints  
- Provider quality issues  

---

## 📡 Telemetry Integration

For each quarantined batch, telemetry tracks:

- `items_quarantined`  
- `error_classes`  
- `care_errors`  
- `schema_errors`  
- `quarantine_latency_ms`  
- `energy_wh`, `co2_g`  
- `etag_used`

Telemetry stored to:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🕒 Retention Rules

| Directory | Retention | Reason |
|-----------|-----------|--------|
| `quarantine/` | **180 days** | Required for FAIR+CARE re-audit & traceability |
| `datadocs/` | 180 days | Evidence for governance review |
| `metadata.json` | Permanent | Immutable governance record |

Quarantine may hold multiple historical batches simultaneously.

---

## 🧪 Local Inspection Examples

Open summary:

~~~~~bash
cat src/pipelines/stac/monitor-validate-publish/data/quarantine/<ts>/last_failure_summary.md
~~~~~

Inspect Items:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/quarantine/<ts>/items.jsonl
~~~~~

View Data Docs:

~~~~~bash
open src/pipelines/stac/monitor-validate-publish/data/quarantine/<ts>/datadocs/index.html
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Created full quarantine documentation with FAIR+CARE, telemetry, governance rules, and retention policies. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Quarantine Zone**  
Safety · Ethics · Transparency · Immutable Governance  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to STAC Orchestrator Data Layer](../README.md)

</div>
