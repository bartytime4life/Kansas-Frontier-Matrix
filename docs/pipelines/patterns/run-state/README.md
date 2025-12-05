---
title: "🧩 KFM v11.2.2 — Run-State Pattern (Idempotent Nodes · Deterministic Retries · lakeFS-Safe)"
path: "docs/pipelines/patterns/run-state/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/patterns-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pattern-run-state-v11.2.2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Operational"
sensitivity_level: "None"
public_exposure_risk: "Low"

scope:
  domain: "pipelines/patterns"
  applies_to:
    - "run-state"
    - "idempotent-nodes"
    - "deterministic-retries"
    - "lakefs-safe"

semantic_intent:
  - "reliability-pattern"
  - "idempotent-execution"
  - "run-state-tracking"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:pipelines:patterns:run-state:v11.2.2"
semantic_document_id: "kfm-pipelines-patterns-run-state-v11.2.2"
event_source_id: "ledger:pipelines-patterns-run-state-v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🧩 **KFM v11.2.2 — Run-State Pattern**  
### Idempotent Nodes · Deterministic Retries · lakeFS-Safe State Tracking  
`docs/pipelines/patterns/run-state/README.md`

**Purpose:**  
Provide a **lightweight, deterministic, idempotent state-tracking model** so every KFM pipeline node can reliably skip, retry, resume, and audit without duplicating work — all in **FAIR+CARE-safe**, STAC-aware form.

</div>

---

## 📘 Overview

The **Run-State Pattern** defines a tiny, stable record of execution **per node per pipeline run**.  
It underpins Reliable Pipelines v11 by enabling:

- ✔ **Idempotent retries** — same node + same run + same inputs → safe no-op  
- ✔ **Skip-if-unchanged** behavior via `inputs_hash`  
- ✔ **Deterministic rollbacks** when paired with lakeFS branches  
- ✔ **Stable provenance** (PROV-O and OpenLineage compatible)  
- ✔ **Ultra-low-overhead audit trails** for long-running DAGs  

Centrally, a node:

1. Computes a deterministic `inputs_hash`.  
2. Looks up any existing run-state.  
3. Decides **skip vs. execute**.  
4. Updates run-state and emits lineage + telemetry.

This pattern is **mandatory** for new reliability-critical pipelines and strongly recommended for all others.

---

## 🧱 Architecture

### 1. Run-State Record Schema (Authoritative)

Each node writes one logical record with the following fields:

- `dataset_id` — canonical node identifier (e.g., `hrrr.wind.tiles`, `soil.joiner.v2`).  
- `run_id` — pipeline-wide UUID or lakeFS commit-root.  
- `lakefs_branch` — execution branch (`main`, `release/v11.2`, `hotfix/atmo-123`, …).  
- `inputs_hash` — hash of normalized input URIs + checksums + parameters.  
- `validation_summary` — minimal QC summary (e.g., `{"checks": 18, "passed": 18, "failed": 0}`).  
- `outcome` — enum: `success | failed | partial | skipped`.  
- `recorded_at` — UTC timestamp.

**Mapping:**

- **PROV-O** — `run_id` → `prov:Activity`; `dataset_id` → `prov:Entity`; `outcome` and `validation_summary` → activity/entity attributes.  
- **STAC** — exposed via `properties.kfm:run_state` on Items/Collections where relevant.  
- **OpenLineage** — `run.facets["kfmRunState"]` for each node.

### 2. Execution Contract (All Nodes)

Each node using this pattern MUST:

1. Compute **`inputs_hash`** deterministically.  
2. Load existing record for `(dataset_id, run_id)` if present.  
3. If `outcome == "success"` **and** `inputs_hash` matches → **SKIP execution** and emit a “skipped” span.  
4. Otherwise:
   - Execute node logic.  
   - Run validations and fill `validation_summary`.  
   - UPSERT run-state record with final `outcome`.  
   - Emit OpenLineage + telemetry events.

This guarantees:

- Safe retries under worker restarts.  
- Zero duplicate side-effects on stable input.  
- Predictable resumption after crashes.  
- Natural re-execution of only **affected** nodes after a lakeFS rollback.

### 3. Storage Patterns

You may implement run-state storage via any of the following, provided the **contract** holds.

#### 3.1 Delta/Parquet Table (Analytics-Optimized, Preferred)

Primary key: `(dataset_id, run_id)`

- Fast analytics across runs and datasets.  
- Easy historization and time-travel in lakeFS.  
- Well-suited for SLO compliance dashboards and drift monitoring.

#### 3.2 lakeFS Object (Simplicity-Optimized)

Path convention:

```text
lakefs://{repo}/{branch}/_run_state/{dataset_id}/{run_id}.json
```

- Naturally versioned with the branch.  
- Immutable by default; safe to inspect via commits and tags.  
- Ideal for smaller environments or low-volume pipelines.

#### 3.3 Relational Table

- Central registry in PostgreSQL/SQLite.  
- Primary key `(dataset_id, run_id)`.  
- Useful when a shared metadata DB already exists.

> **Rule:** Choose **one canonical store** per environment; do not spread the same run-state across multiple independent backends.

### 4. Computing `inputs_hash`

To maintain deterministic idempotency:

1. Collect all relevant inputs:
   - Input URIs or logical identifiers.  
   - lakeFS commit IDs / ETags / checksums.  
   - Critical configuration parameters (window, AOI, model version, etc.).  
2. Normalize:
   - Sort all keys and URIs lexicographically.  
   - Serialize parameters as JSON with **stable key ordering**.  
3. Concatenate into a single byte string.  
4. Compute **SHA-256** over the bytes.  
5. Represent as string: `"sha256:<digest>"`.

External API calls MUST incorporate:

- Query parameters.  
- Time windows.  
- ETag / Last-Modified (if available).  

If any of these change, the resulting `inputs_hash` changes, naturally forcing a re-run.

---

## 📦 Data & Metadata

### 1. Validation Summary (Minimal JSON)

A minimal `validation_summary` **MUST** include:

- `checks` — total checks run.  
- `passed` — number of checks passed.  
- `failed` — number of checks failed.

Example:

```json
{"checks": 18, "passed": 18, "failed": 0}
```

Pipelines MAY attach richer payloads (e.g., Great Expectations results), but dashboards and SLO monitors rely on this minimal structure for consistency.

### 2. Lineage & Catalog Integration

Run-state is designed to be:

- **PROV-O compatible:**  
  - `run_id` ties together all node activities in a single pipeline run.  
  - `inputs_hash` plus input references document **exactly which inputs** were consumed.

- **STAC/DCAT aligned:**  
  - STAC Items may embed `kfm:run_state` to indicate the specific run responsible for producing an asset.  
  - DCAT Datasets reference run-state via provenance notes and version/change logs.

- **OpenLineage-ready:**  
  - The run-state record feeds an OpenLineage facet, enabling unified visualization of node outcomes across runs.

---

## 🗂️ Directory Layout

```text
docs/pipelines/patterns/run-state/
├── 📄 README.md                     # This file (Run-State Pattern spec)
├── 📁 examples/                     # Example implementations
│   ├── 📁 python/                   # Python usage examples
│   ├── 📁 airflow/                  # Airflow DAG snippets
│   └── 📁 lakefs/                   # Branch-based examples
└── 📁 schemas/
    └── 📄 run-state.schema.json     # JSON Schema for pattern v11
```

Implementations under `examples/` MUST reference this README and `run-state.schema.json` as the normative contracts.

---

## 🧠 Story Node & Focus Mode Integration

**Story Node ID:** `patterns/run-state`

Focus Mode v3 consumes run-state to narrate **why** a pipeline behaved a certain way:

- Explains when a node **skipped execution** because inputs were unchanged.  
- Highlights **retries** and shows final `outcome` states.  
- Links from Story Node narratives → specific `run_id` and `dataset_id`.  
- Helps reviewers traverse from **“what user saw” → “which run-state backed it” → “which inputs were consumed”**.

Run-state must remain **read-only** in Story Nodes and Focus Mode; edits occur only via governed pipelines.

---

## 🧪 Validation & CI/CD

Pipelines adopting the Run-State Pattern MUST include:

- **Schema validation**  
  - `run-state.schema.json` enforced on write.  
- **Idempotency tests**  
  - Same inputs twice → second execution **skips**.  
- **Rollback tests**  
  - lakeFS rollback causes only affected nodes to re-run.  
- **Telemetry checks**  
  - Each node write increments pattern-level metrics in `patterns-telemetry.json`.  

CI workflows SHOULD include:

- `markdown-lint` and `schema-lint` for this pattern doc and schema.  
- Unit tests for `inputs_hash` computation and run-state upserts.  
- Integration tests verifying end-to-end skip/retry/rollback semantics.

---

## ⚖ FAIR+CARE & Governance

The Run-State Pattern itself stores **operational metadata** only:

- No direct personal data.  
- No raw coordinates or sensitive geometries.  
- No Indigenous knowledge or cultural content.

Nonetheless, it supports FAIR+CARE by:

- Making pipeline behavior **transparent and auditable**.  
- Enabling precise provenance for datasets that **do** carry sensitive content.  
- Supporting governance reviews where councils need to understand **how** a dataset was produced, retried, or rolled back.

Any pipeline handling Indigenous or heritage-sensitive data MUST:

- Ensure that run-state references (e.g., `dataset_id`) do not leak restricted internal identifiers in public catalogs.  
- Keep detailed, sensitive traces in governed internal environments only.

---

## 🕰️ Version History

| Version | Date       | Notes                                                                 |
|--------:|------------|-----------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Upgraded to KFM-MDP v11.2.2; emoji layout; telemetry schemas linked. |
| v11.0.0 | 2025-11-10 | Initial KFM v11 release; deterministic idempotency run-state pattern. |

---

<div align="center">

🧩 **KFM v11.2.2 — Run-State Pattern**  
Deterministic Execution · Idempotent Retries · lakeFS-Safe State Tracking  

[📘 Pipelines Patterns Index](../README.md) ·  
[🧭 Governance](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[📡 Telemetry](../../telemetry/README.md)

</div>