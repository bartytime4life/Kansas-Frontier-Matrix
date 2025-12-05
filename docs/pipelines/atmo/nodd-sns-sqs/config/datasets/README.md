---
title: "📘 KFM v11.2.3 — NODD Dataset Ingestion Contracts Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index for NOAA NODD dataset ingestion contracts used by the SNS → SQS event-driven atmospheric pipeline in KFM."
path: "docs/pipelines/atmo/nodd-sns-sqs/config/datasets/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Dataset Contracts Index"
intent: "nodd-sns-sqs-dataset-contracts-index"
category: "Pipelines · Atmospheric · Config"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD dataset contract standard"

header_profile: "standard"
footer_profile: "standard"
---

# 📘 NODD Dataset Ingestion Contracts Index  

`docs/pipelines/atmo/nodd-sns-sqs/config/datasets/README.md`

This directory defines **per-dataset ingestion contracts** for the NOAA NODD SNS → SQS atmospheric pipeline.

Each contract describes, for a single dataset family (GOES, NEXRAD, HRRR, GFS, surface obs, NDBC, etc.):

- SNS topic → SQS queue bindings  
- Expected message envelope and schema  
- Object-location templates (S3/OCI/HTTPS paths)  
- Spatial/temporal domain and tiling  
- STAC collection mapping and extensions  
- Governance, sensitivity, and FAIR+CARE annotations  

All NODD producers and operators MUST treat these contracts as the **single source of truth** for dataset behavior.

⸻

## 🗂 1. Directory Layout (Dataset Contracts)

~~~text
docs/pipelines/atmo/nodd-sns-sqs/config/datasets/
│
├── 📄 README.md                          # This file — dataset contracts index
│
├── 📄 goes-abi.yaml                      # GOES-East/West ABI L1b/L2 contract
├── 📄 nexrad-level2.yaml                 # NEXRAD Level II ingestion contract
├── 📄 nexrad-level3.yaml                 # NEXRAD Level III ingestion contract
├── 📄 hrrr.yaml                          # HRRR model output contract
├── 📄 gfs.yaml                           # GFS model output contract
├── 📄 surface-obs.yaml                   # Surface observation feeds (METAR/SYNOP/etc.)
├── 📄 ndbc-buoys.yaml                    # NDBC ocean buoy products
│
└── 📄 _template.dataset-contract.yaml    # Canonical template for new dataset contracts
~~~

Notes:

- File set above is illustrative; actual presence is governed by CI.  
- `_template.dataset-contract.yaml` MUST be used when onboarding new NODD datasets into the pipeline.

⸻

## 🧭 2. Purpose & Scope

This directory exists to:

- Provide **explicit, versioned contracts** for each NOAA NODD dataset flowing through SNS → SQS → KFM.  
- Ensure that:
  - Message envelopes are stable and validated.  
  - STAC mappings are deterministic.  
  - Governance and sensitivity labels are applied consistently.  
- Support:
  - **Automated validation gates** in the pipeline.  
  - **Replay selection** and WAL debugging.  
  - **Story Node** and Focus Mode awareness of atmospheric datasets.

Out of scope:

- Runtime credentials or secrets.  
- Implementation details of operators (`message-parse`, `metadata-extract`, `stac-register`).  
- Non-NODD atmospheric data sources.

⸻

## 🧱 3. Dataset Contract Structure (Conceptual)

Each `*.yaml` in this directory MUST follow the canonical dataset contract schema (summarized here conceptually):

- `apiVersion` — e.g., `kfm.nodd.dataset/v1alpha1`  
- `kind` — `NoddDatasetContract`  
- `metadata`  
  - `id` — canonical dataset identifier (e.g., `goes-abi`, `nexrad-l2`)  
  - `title`  
  - `description`  
  - `provider` (NOAA / NODD program)  
  - `labels` (e.g., `priority`, `product_class`)  
- `sns`  
  - `topic_arn`  
  - `message_schema_ref` (JSON Schema for SNS payload)  
- `sqs`  
  - `queue_name` / `queue_arn`  
  - `dlq_arn`  
  - `fifo` / `standard` and dedupe semantics (if applicable)  
- `storage`  
  - `uri_templates` (S3/HTTPS patterns)  
  - `compression` / `encoding`  
  - `granule_time_fields` (e.g., start/end time keys)  
- `stac`  
  - `collection_id`  
  - `item_id_pattern`  
  - `extensions` (e.g., `proj:*`, `raster:*`, `eo:*`, `sat:*`)  
  - `asset_mappings` (e.g., which bands or files map to STAC assets)  
- `governance`  
  - `fair_category`  
  - `care_label`  
  - `sensitivity` / `sensitivity_level`  
  - `indigenous_data_flag` (typically false for NODD, but explicit)  
- `validation`  
  - `schema_refs` (JSON Schema, STAC, ancillary checks)  
  - `qa_rules` (null thresholds, physical ranges)  

The full JSON Schema for dataset contracts is stored under:

- `schemas/json/nodd-dataset-contract-v1.json` (referenced from this repo’s schemas index).

⸻

## 🌐 4. Example: GOES-ABI Contract (Conceptual Snapshot)

The actual contract lives in `goes-abi.yaml`. This is a **shape-only** illustration:

- `metadata.id`: `goes-abi`  
- `sns.topic_arn`: points to NODD GOES ABI topic  
- `storage.uri_templates`: include bucket/key patterns for East/West, channels, scan times  
- `stac.collection_id`: `kfm-nodd-goes-abi`  
- `stac.extensions`: `proj:*`, `eo:*`, `sat:*`, `raster:*`  
- `validation.qa_rules`:
  - Ensure:
    - Valid projection and footprint  
    - Reasonable brightness temperature or reflectance ranges  
    - Time consistency between filename, headers, and STAC `datetime`

All enrichment and QC logic in operators MUST use these contracts as configuration, not hard-coded assumptions.

⸻

## 🧬 5. Governance & FAIR+CARE Alignment

Each dataset contract MUST:

- Declare FAIR+CARE metadata:
  - `fair_category` (e.g., `F1-A1-I1-R1`)  
  - `care_label` (e.g., `Public · Low-Risk`)  
- Specify:
  - License and reuse terms (as provided by NOAA / NODD).  
  - Any downstream usage constraints.

Even though NODD datasets are generally **low-sensitivity**, contracts MUST still:

- Confirm `indigenous_data_flag` is set correctly.  
- Capture any **indirect sensitivity** (e.g., derived layers that intersect sensitive land categories in downstream pipelines).

LangGraph governance gates reference these fields to:

- Attach the correct governance profile to STAC Items.  
- Enforce usage policies in Focus Mode / Story Nodes.

⸻

## 🧪 6. CI & Validation

CI MUST enforce:

- **Schema validation**:
  - Every `*.yaml` in this directory validates against `nodd-dataset-contract-v1.json`.  

- **Coverage**:
  - For each NODD dataset listed in:
    - `config/sns-topics.json`  
    - `config/sqs-queues.json`  
  - There MUST be a corresponding dataset contract here.

- **Referential integrity**:
  - `sns.topic_arn` and `sqs.queue_name/arn` keys in contracts MUST match values defined in the parent `config` layer (or be a governed subset).

- **No orphan contracts**:
  - Dataset contracts that are no longer referenced MUST be either:
    - Marked deprecated (with clear sunset policy), or  
    - Removed in a governed change.

Any change to a dataset contract in `prod` MUST:

- Pass CI.  
- Be associated with a change ticket or incident.  
- Trigger review of associated telemetry thresholds and runbooks if behavior meaningfully changes.

⸻

## 🧩 7. Onboarding New NODD Datasets

To onboard a new NODD dataset into the SNS → SQS pipeline:

1. **Copy the template**

   - Duplicate `_template.dataset-contract.yaml` to a new file:
     - Example: `new-dataset-id.yaml`.

2. **Fill metadata and endpoints**

   - Set:
     - `metadata.id`, `title`, `description`  
     - `sns.topic_arn`, `sqs.queue_*`  
     - `storage.uri_templates`  

3. **Define STAC mapping**

   - Choose:
     - `collection_id`  
     - Item ID and asset mapping patterns  
     - Required STAC extensions  

4. **Set governance fields**

   - Assign FAIR, CARE, sensitivity, and sovereignty flags.  
   - Confirm with governance references if unclear.

5. **Add validation rules**

   - Link relevant JSON Schemas, QA rules, and geospatial validity checks.

6. **Wire into pipeline config**

   - Update:
     - `config/sns-topics.json`  
     - `config/sqs-queues.json`  
     - Any dataset routing tables used by `message-parse` and `metadata-extract`.

7. **Run CI and non-prod tests**

   - Deploy to `dev`/`stage` for:
     - Schema validation.  
     - Ingest smoke tests.  
     - STAC output inspection.

Only after these steps and governance approval may the dataset be enabled in `prod`.

⸻

## 📘 8. Version History

| Version  | Date       | Notes                                                                                               |
|---------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD dataset ingestion contracts index for SNS → SQS atmospheric pipeline configuration.    |

---

<div align="center">

📘 NODD Dataset Ingestion Contracts Index · KFM v11.2.3  

Deterministic · Contract-First · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Config](../README.md) ·  
[🌩️ NODD Pipeline Overview](../../README.md) ·  
[📊 NODD Telemetry](../../telemetry/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
