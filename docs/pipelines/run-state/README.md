---
title: "🧩 KFM v11.2.2 — Run-State Pattern (Idempotent Nodes · Deterministic Retries · lakeFS-Safe) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
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

## 🌟 Pattern Summary

This pattern defines a **tiny run-state record** stored **per node per pipeline run**.  
It enables:

- ✔ **Idempotent retries** — same node + same run = same record  
- ✔ **Skip-if-unchanged** logic via `inputs_hash`  
- ✔ **Deterministic rollbacks** when paired with lakeFS branches  
- ✔ **Stable provenance** (PROV-O compatible)  
- ✔ **Ultra-low-overhead audit trail**  
- ✔ **Safe for long-running DAGs**

A run-state record is written **exactly once per node per run**, and **updated only on reattempt**.

---

## 🧬 Minimal Schema (Authoritative)

Each node writes one logical record with the following fields:

- `dataset_id` — canonical node identifier (e.g., `hrrr.wind.tiles`, `soil.joiner.v2`)  
- `run_id` — pipeline-wide UUID or lakeFS commit-root  
- `lakefs_branch` — execution branch (`main`, `release/v11.2`, etc.)  
- `inputs_hash` — hash of normalized input URIs + checksums + params  
- `validation_summary` — minimal QC results (e.g., `{"checks": 18, "passed": 18, "failed": 0}`)  
- `outcome` — enum: `success | failed | partial | skipped`  
- `recorded_at` — timestamp (UTC)

This schema maps cleanly into:

- PROV-O (`prov:Activity`, `prov:Entity`, `prov:wasGeneratedBy`)  
- STAC Item properties (`kfm:run_state`)  
- OpenLineage `run.facets`  

---

## 🗄️ Storage Patterns

### Option A — Delta/Parquet Table (Preferred for Analytics)

Primary key: `(dataset_id, run_id)`

- Fast queries  
- Easy historization  
- Version-controlled snapshots in lakeFS  

### Option B — lakeFS Object (Preferred for Simplicity)

    lakefs://{repo}/{branch}/_run_state/{dataset_id}/{run_id}.json

- Immutable by default  
- Naturally versioned by lakeFS  

### Option C — Relational Table

- PostgreSQL / SQLite with primary key `(dataset_id, run_id)`  
- Suitable when a central relational registry is already in place

---

## 🔁 Execution Contract (All Nodes)

1. Compute **`inputs_hash`** deterministically.  
2. Load existing state for `(dataset_id, run_id)` if present.  
3. If `outcome == "success"` **and** `inputs_hash` matches → **SKIP** work.  
4. Otherwise → execute node logic.  
5. Run validation and generate `validation_summary`.  
6. UPSERT run-state record.  
7. Emit lineage to OpenLineage + STAC sidecar if configured.

This guarantees:

- Safe retries  
- Zero duplication  
- Predictable behavior under partial failures  
- Deterministic resumption after crash/interrupt  

---

## 🧪 Validation Summary (Minimal JSON)

Minimal example:

    {"checks": 18, "passed": 18, "failed": 0}

Nodes may attach richer metrics (Great Expectations, custom QC), but must keep a **minimal pass/fail count** for dashboards and SLO reporting.

---

## 🧮 Computing `inputs_hash`

To maintain deterministic idempotency:

- Sort input URIs lexicographically  
- Append checksums (lakeFS commits, ETags, or equivalent)  
- Append parameters (serialized JSON with stable key ordering)  
- Compute SHA-256 over the concatenated bytes  
- Store as string `"sha256:<digest>"`  

External API calls MUST incorporate:

- Query parameters  
- Time windows  
- ETag or Last-Modified (if provided)  

This ensures run-state is sensitive to the **actual logical inputs** that matter.

---

## 📂 Directory Layout

    docs/pipelines/patterns/run-state/
    ├── 📄 README.md                         # This file
    ├── 📁 examples/                         # Example implementations
    │   ├── 📁 python/                       # Python usage examples
    │   ├── 📁 airflow/                      # Airflow DAG snippets
    │   └── 📁 lakefs/                       # Branch-based examples
    └── 📁 schemas/
        └── 📄 run-state.schema.json         # JSON Schema for pattern v11

---

## 🛰️ Story Node Integration (Focus Mode v3)

**Story Node ID:** `patterns/run-state`

Focus Mode v3 uses this pattern to:

- Annotate lineage steps (e.g., “node skipped due to unchanged inputs”)  
- Explain why a node **skipped** or **re-executed**  
- Surface reliability guarantees (idempotency, WAL safety)  
- Display retry and resumption events as narrative elements alongside data products  

This allows operators and reviewers to move from **story → run-state record → pipeline logs**.

---

## 🧭 Field Guide (Operator-Centric)

### When a retry happens

- Check prior run-state for `(dataset_id, run_id)`  
- If `inputs_hash` differs → treat as a **new logical attempt**  
- If `inputs_hash` matches but prior `outcome != "success"` → reattempt is allowed  
- All attempts must emit WAL entries and SLO budget updates  

### When a rollback happens

- Upstream lakeFS branch is reset or rebased  
- Downstream nodes detect mismatch via `inputs_hash`  
- Only affected nodes re-run  
- All unaffected nodes naturally **skip** via the run-state check  

---

## 🛠 Example: Python Upsert (Schematic)

**This is schematic — production code belongs under `examples/python/`.**

    write_run_state(
        dataset_id="hrrr.wind.tiles",
        run_id=os.environ["KFM_RUN_ID"],
        lakefs_branch=current_branch(),
        inputs_hash=inputs_hash,
        validation_summary={"checks": 18, "passed": 18, "failed": 0},
        outcome="success",
    )

The actual implementation MUST:

- Enforce a single upsert semantics on `(dataset_id, run_id)`  
- Respect WAL, error handling, and telemetry standards  

---

## 🕰️ Version History

| Version  | Date       | Notes                                             |
|----------|------------|---------------------------------------------------|
| v11.2.2  | 2025-11-28 | Upgraded to KFM-MDP v11.2.2; emoji layout; telemetry schemas |
| v11.0.0  | 2025-11-10 | Initial KFM v11 release; deterministic idempotency pattern |

---

<div align="center">

[📘 KFM Docs](../../../README.md) · [🧭 Governance](../../standards/governance/ROOT-GOVERNANCE.md) · [📡 Telemetry](../../telemetry/README.md)

</div>
