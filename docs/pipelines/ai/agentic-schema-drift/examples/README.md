---
title: "🧪 KFM v11.2.2 — Agentic Schema Drift Steward Examples (Events · Patches · Evaluations · Lineage)"
path: "docs/pipelines/ai/agentic-schema-drift/examples/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Draft / Experimental"
lifecycle: "Prototype"
review_cycle: "Quarterly · Autonomous Systems · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Experimental"
doc_kind: "Examples Index"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/agentic-schema-drift-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/agentic-schema-drift-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "AI-Agent-Examples"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "schema-drift-examples"
  - "agentic-etl"
  - "patch-evaluation"
  - "prov-lineage"
  - "governance-examples"
  - "telemetry-examples"

scope:
  domain: "agentic-schema-drift-examples"
  applies_to:
    - "schema-drift-event-examples"
    - "transform-patch-examples"
    - "patch-evaluation-examples"
    - "lineage-examples"
    - "telemetry-examples"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🧪 **Agentic Schema Drift Steward — Example Artifacts**  
`docs/pipelines/ai/agentic-schema-drift/examples/README.md`

**Purpose:**  
Provide **realistic, governed examples** of schema drift events, patch proposals, benchmark evaluations, telemetry bundles, and PROV-O lineage documents used by the KFM v11.2.2 Agentic Schema Drift Steward.

These curated examples support:
- Testing & CI  
- Developer onboarding  
- Governance review  
- Focus Mode v3 narrative generation  
- Story Node v3 schema-evolution entries  

</div>

---

## 📘 Overview

This directory contains **sample JSON, JSON-LD, and Markdown artifacts** that demonstrate how the agent handles:

- Schema drift detection  
- Patch generation  
- Patch evaluation  
- Governance screening  
- Telemetry emission  
- Lineage propagation into Focus Mode & Story Nodes  

All examples are **synthetic**, **privacy-safe**, and **culturally de-identified**.

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/agentic-schema-drift/examples/
    ├── 📄 README.md                                 # This file
    │
    ├── 📄 schema_drift_event_sample.json            # Example SchemaDriftEvent
    ├── 📄 transform_patch_sample.json               # Example TransformPatch (AI proposed)
    ├── 📄 patch_evaluation_sample.json              # Example PatchEvaluation (benchmarker)
    │
    ├── 📄 lineage_sample.jsonld                     # Example PROV-O lineage chain
    ├── 📄 telemetry_sample.json                     # Example telemetry bundle
    │
    └── 📁 narrative/                                # Story Node + Focus Mode examples
        ├── 📄 schema-change-story-node.jsonld       # Story Node v3 narrative describing drift
        └── 📄 focus-mode-summary.json               # Focus Mode v3 contextual summary

---

## 🧬 Artifact Types

### 1. 🛰️ `schema_drift_event_sample.json`
A fully-typed `SchemaDriftEvent` example:

- `source_id`  
- `source_kind` (stac/tabular/netcdf/neo4j)  
- Old vs new schema diff  
- Field changes (added/removed/renamed/type-changed)  
- Severity classification  

Used to test drift detection and agent invocation.

---

### 2. 🤖 `transform_patch_sample.json`
A synthetic example of the agent’s proposed patch:

- ETL transform patch (`code_diff`)  
- STAC/DCAT field updates  
- Neo4j migration suggestion  
- FAIR+CARE notes  
- Breaking-change risk  

Useful for CI snapshot tests.

---

### 3. 🧪 `patch_evaluation_sample.json`
An example of the Transform Benchmarker output:

- Data quality score  
- Test pass rate  
- Runtime delta  
- ML impact notes  
- Overall recommendation (`accept | reject | manual_review`)  

Supports governance and reproducibility tests.

---

### 4. 📘 `lineage_sample.jsonld`
A `prov:Activity` trace showing:

- Agents (software + human)  
- Entities (old & new schemas)  
- Activities (drift detection, patch evaluation, patch application)  
- Relations (`prov:used`, `prov:wasGeneratedBy`, etc.)  

This is used in Focus Mode v3 and Story Node v3 integration.

---

### 5. 📡 `telemetry_sample.json`
Example telemetry bundle containing:

- Drift metrics  
- Patch IDs  
- Prefect run IDs  
- LangGraph run IDs  
- Energy/Carbon v2  
- CARE flags  
- Violations (if any)  

Used to validate telemetry schema and CI-driven governance.

---

### 6. 🧭 `narrative/` examples
These demonstrate how the agentic workflow produces downstream narratives.

#### • `schema-change-story-node.jsonld`
Story Node v3 narrative describing how schema changed and why.

#### • `focus-mode-summary.json`
Compressed Focus Mode v3 reasoning summary:

- What changed  
- Why  
- What downstream layers it affects  
- How evidence was validated  

Both files are safe for public demonstration.

---

## 📌 Usage Guidance

These examples are used in:

- **Unit tests** (snapshot stability)  
- **Integration tests** (drift → patch → evaluation)  
- **Governance audits**  
- **Focus Mode QA**  
- **Story Node generation tests**  
- **Semantic reasoning test harness**  

When adding new examples:

- Follow JSON-LD & Pydantic schemas  
- Use synthetic identifiers (never sensitive data)  
- Mask any spatial features using H3 generalization  
- Add metadata in the telemetry bundle  
- Update the CI example registry  

---

## 🧪 CI Rules for Examples

Examples must:

- Validate against their relevant JSON Schema  
- Match the Pydantic input/output models  
- Contain no personally sensitive information  
- Pass FAIR+CARE governance checks  
- Be reproducible and stable across versions  

---

## 🕰 Version History

| Version  | Date       | Notes                                                           |
|----------|------------|-----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Added narrative examples & updated telemetry for v2 schemas     |
| v11.0.0  | 2025-11-22 | Initial example directory scaffold                              |

---

<div align="center">

### 🔗 Footer  
[⬅ Agentic Schema Drift Flows](../flows/README.md) · [🤖 Source Modules](../src/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

