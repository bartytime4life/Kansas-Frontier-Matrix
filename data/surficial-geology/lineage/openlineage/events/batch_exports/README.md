---
title: "🧾 Surficial Geology — OpenLineage Batch Exports"
path: "data/surficial-geology/lineage/openlineage/events/batch_exports/README.md"

version: "v0.1.0"
last_updated: "2025-12-14"
release_stage: "Draft / Governed"
status: "Active"

doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "data-lineage"
  applies_to:
    - "data/surficial-geology/lineage/openlineage/events/batch_exports/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by subsequent dataset lineage revisions"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain: []
provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

json_schema_ref: "../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"

story_node_refs: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:lineage:openlineage:events:batch-exports:readme:v0.1.0"
semantic_document_id: "kfm-surficial-geology-openlineage-batch-exports-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:lineage:openlineage:events:batch-exports:readme:v0.1.0"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "metadata-extraction"
    - "layout-normalization"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
---

<div align="center">

# 🧾 **Surficial Geology — OpenLineage Batch Exports**
`data/surficial-geology/lineage/openlineage/events/batch_exports/README.md`

**Purpose**  
Define how **OpenLineage event batches** are packaged and stored for the Surficial Geology pipeline,  
including naming, integrity, and governance constraints for safe downstream ingestion.

<img src="https://img.shields.io/badge/Lineage-OpenLineage-blue" />
<img src="https://img.shields.io/badge/Dataset-Surficial_Geology-6aa84f" />
<img src="https://img.shields.io/badge/Status-Draft-lightgrey" />

</div>

---

## 📘 Overview

This directory is intended for **batch export artifacts** of OpenLineage events (e.g., for bulk ingest into
a lineage service, archival, or offline review).

Design goals:

- **Deterministic & replayable:** batches should be reproducible from the same run inputs/config.
- **Auditable:** each batch should have a machine-readable manifest and integrity hashes.
- **Governance-safe:** do not export restricted/sensitive details that violate FAIR+CARE or sovereignty rules.

Batch exports are **derived artifacts**. Treat them as **rebuildable outputs**, not the authoritative source
of truth for the dataset itself.

## 🗂️ Directory Layout

~~~text
📁 batch_exports/                                          — Bundled OpenLineage event exports (derived)
├── 📄 README.md                                           — This file
├── 🧾 batch_<batch_id>.ndjson.gz                           — OpenLineage RunEvent stream (NDJSON, gz)
├── 🧾 batch_<batch_id>.manifest.json                       — Batch manifest (counts, hashes, metadata)
└── 🧾 batch_<batch_id>.sha256                              — SHA256 checksums for batch bundle + members
~~~

## 📦 Data & Metadata

### 1) Expected formats

- **Event stream:** NDJSON (one JSON object per line) containing OpenLineage `RunEvent` objects.
- **Compression:** gzip is recommended for portability and storage efficiency.
- **Manifest:** JSON file describing the batch and providing integrity metadata.

If other formats are required (e.g., `.json` array, `.tar.gz` bundle), document the deviation in the
corresponding manifest file.

### 2) Batch identifier convention

A `batch_id` SHOULD be unique and sortable. Recommended shape:

- `YYYYMMDDTHHMMSSZ__<run_id>__<job_or_pipeline_slug>`

Examples (illustrative):

- `20251214T031500Z__3f2c...__surficial-geology-etl`
- `20251214T031500Z__3f2c...__tiles-build`

### 3) Manifest minimum contract

A manifest SHOULD include at minimum:

~~~json
{
  "batch_id": "YYYYMMDDTHHMMSSZ__<run_id>__<slug>",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "openlineage": {
    "spec": "v1",
    "event_type_set": ["START", "COMPLETE", "FAIL"]
  },
  "run": {
    "run_id": "<openlineage-runId>",
    "job_namespace": "<namespace>",
    "job_name": "<name>"
  },
  "files": [
    {
      "path": "batch_<batch_id>.ndjson.gz",
      "content_type": "application/x-ndjson",
      "compressed": true,
      "bytes": 0,
      "sha256": "<sha256>"
    }
  ],
  "counts": {
    "events": 0
  },
  "governance": {
    "classification": "Public",
    "sensitivity_level": "None",
    "indigenous_rights_flag": true
  }
}
~~~

### 4) Integrity checksums

- `batch_<batch_id>.sha256` SHOULD contain SHA256 lines for each file in the batch.
- If hashes are duplicated in the manifest, the values MUST match.

### 5) Mutability and retention

- Batch exports SHOULD be treated as **append-only** once written.
- If a batch must be regenerated, write a **new** `batch_id` and note the replacement in the new manifest
  (do not silently overwrite).

## 🧪 Validation & CI/CD

Recommended validation for any new or updated batch export:

1. **Parseability**
   - NDJSON decompresses cleanly.
   - Every line is valid JSON.
2. **Schema sanity**
   - Events include the required OpenLineage fields for your collector (at minimum: `eventType`, `eventTime`,
     `run.runId`, `job.name`, `job.namespace`).
3. **Manifest integrity**
   - Manifest JSON parses and references existing files.
   - SHA256 values match file contents.
4. **Governance scans**
   - No secrets, tokens, or credentials.
   - No embedded PII.
   - No restricted precise locations if governance flags require masking/generalization.

## ⚖ FAIR+CARE & Governance

These exports are part of the lineage record and must remain governance-compliant:

- **No secrets / credentials** in event facets, environment fields, logs, or stack traces.
- **No PII** (usernames, emails, device IDs, or workstation paths) unless explicitly approved and classified.
- **Sovereignty-aware by default:** if any upstream inputs/outputs carry restrictions, exports must apply
  required masking/generalization before writing the batch.
- If the batch contains mixed-sensitivity events, the batch MUST be classified at the **highest** applicable
  sensitivity and handled accordingly.

## 🕰️ Version History

| Version | Date       | Change summary |
|--------:|------------|----------------|
| v0.1.0  | 2025-12-14 | Initial README for OpenLineage batch export conventions. |

---

<div align="center">

**🧾 Surficial Geology — OpenLineage Batch Exports**  
Deterministic Pipelines · Open Provenance · Governed Data

[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© Kansas Frontier Matrix — Documentation licensed CC-BY 4.0 (unless otherwise noted).

</div>

