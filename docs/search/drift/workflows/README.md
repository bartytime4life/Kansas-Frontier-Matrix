---
title: "🧭 KFM — DRIFT Workflows (Global→Local Retrieval DAGs · Provenance · CARE Gates)"
path: "docs/search/drift/workflows/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Runbook + Reference"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "drift-workflow-definitions"
audience:
  - "Search Engineering"
  - "Graph + Provenance Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public (Governed)"
fair_category: "F1-A2-I2-R2"
care_label: "CARE-Aware Retrieval"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
redaction_required: true
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:search:drift:workflows:v11.2.6"
semantic_document_id: "kfm-drift-search-workflows"
event_source_id: "ledger:docs/search/drift/workflows/README.md"
immutability_status: "version-pinned"

telemetry_schema: "../../../../schemas/telemetry/drift-search-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

machine_extractable: true
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "diagram-extraction"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "content-alteration"
  - "narrative-fabrication"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded by drift-search-v12"
---

<div align="center">

# 🧭 **KFM — DRIFT Workflows**
`docs/search/drift/workflows/README.md`

**Purpose**  
Define the **workflow/DAG layer** for DRIFT global→local hybrid retrieval, including **determinism controls**,
**provenance emission**, **telemetry hooks**, and **CARE-governed redaction gates**.

<img src="https://img.shields.io/badge/Search-DRIFT%20Workflows-blue" />
<img src="https://img.shields.io/badge/Provenance-PROV--O%20%2B%20OpenLineage-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

This directory holds **workflow definitions** for DRIFT Search.

A “workflow” is a deterministic, replayable orchestration that:

- initializes global context (HyDE-style hypothesis),
- retrieves anchors (vector/community stage),
- performs local precision retrieval (Neo4j traversals),
- aggregates evidence,
- applies CARE screening (mask/aggregate/generalize),
- emits provenance and telemetry artifacts suitable for governance review and Focus Mode use.

### Governance posture

Because `redaction_required: true`, workflows MUST:

- avoid emitting precise sensitive locations in logs, examples, or artifacts,
- generalize spatial outputs (H3/region level) where required,
- record redaction decisions as first-class policy events in provenance.

---

## 🗂️ Directory layout

~~~text
📁 docs/search/drift/workflows/                       — Workflow definitions for DRIFT Search
├── 📄 README.md                                      — This document
├── 🧾 00_global_init.yml                              — Global initialization (HyDE + query normalization)
├── 🧾 10_vector_anchors.yml                           — Anchor retrieval (vector/community recall)
├── 🧾 20_graph_local.yml                              — Neo4j local retrieval (precision traversal)
├── 🧾 30_care_gate.yml                                — CARE screening + redaction/generalization
├── 🧾 40_synthesis.yml                                — Evidence synthesis (policy-gated narrative assembly)
└── 🧾 99_emit_evidence.yml                            — Emit STAC/DCAT refs + PROV/O-L + telemetry bundles
~~~

> File names above are a governed naming convention for readability. Implementations MAY consolidate steps, but MUST preserve:
> determinism, provenance, and CARE gates.

---

## 🧱 Workflow contract

Each workflow YAML MUST be:

- deterministic (seeded, stable ordering),
- reproducible (config snapshot + commit hash recorded),
- provenance-complete (OpenLineage + PROV-O emitted),
- policy-gated (CARE screen before final output).

### Minimal workflow schema

~~~yaml
workflow_id: "drift:hybrid-global-local"
workflow_version: "v11.2.6"
description: "Hybrid retrieval with CARE gate and provenance emission"

determinism:
  seed: 1337
  locale: "C"
  timezone: "UTC"
  stable_sort: true

inputs:
  query_text: "${QUERY_TEXT}"
  user_context_ref: "${USER_CONTEXT_REF}"          # optional (policy-gated)
  constraints:
    time_range: "${TIME_RANGE}"                    # optional
    bbox: "${BBOX}"                                # optional

steps:
  - id: "global_init"
    uses: "drift/global_init@v11"
    outputs: ["query_norm", "hyde_hypothesis", "query_hash"]

  - id: "vector_anchors"
    uses: "drift/vector_anchors@v11"
    inputs: ["query_norm", "hyde_hypothesis"]
    outputs: ["anchors", "anchor_stats"]

  - id: "graph_local"
    uses: "drift/neo4j_local@v11"
    inputs: ["anchors", "constraints"]
    outputs: ["evidence_nodes", "evidence_edges", "graph_stats"]

  - id: "care_gate"
    uses: "drift/care_gate@v11"
    inputs: ["evidence_nodes", "evidence_edges"]
    outputs: ["evidence_redacted", "policy_events", "redaction_summary"]

  - id: "synthesis"
    uses: "drift/synthesis@v11"
    inputs: ["evidence_redacted", "constraints"]
    outputs: ["answer", "citations", "storynode_stub"]

  - id: "emit_evidence"
    uses: "drift/emit@v11"
    inputs: ["policy_events", "redaction_summary", "anchor_stats", "graph_stats"]
    outputs: ["prov_bundle_ref", "openlineage_refs", "stac_item_ref", "telemetry_ref"]

outputs:
  answer: "${steps.synthesis.answer}"
  storynode_stub: "${steps.synthesis.storynode_stub}"
  prov_bundle_ref: "${steps.emit_evidence.prov_bundle_ref}"
~~~

---

## 🧬 Phase mapping

DRIFT phases map to workflow steps as follows:

- Phase 1: Global semantic initialization → `global_init`
- Phase 2: Follow-up question generation / anchor shaping → `global_init` + `vector_anchors` (and optional subquery generation inside)
- Phase 3: Local Neo4j precision traversal → `graph_local`
- Phase 4: Synthesis + CARE enforcement → `care_gate` + `synthesis`

~~~mermaid
flowchart TD
  A["Input query"] --> B["global_init - normalize and HyDE hypothesis"]
  B --> C["vector_anchors - recall anchors"]
  C --> D["graph_local - Neo4j traversals"]
  D --> E["care_gate - redact and generalize"]
  E --> F["synthesis - narrative and evidence set"]
  F --> G["emit_evidence - PROV O-L STAC telemetry"]
~~~

---

## 🎛️ Determinism controls

Workflows MUST record and/or enforce:

- fixed seeds (when stochastic components exist),
- pinned model identifiers for embeddings and HyDE generation,
- stable ordering before ranking/fusion (canonical sort keys),
- explicit locale/timezone,
- config hashes and commit SHA recorded into provenance,
- deterministic serialization (canonical JSON ordering for emitted artifacts).

### Noise control recommendations

- canonicalize query text before hashing (trim, normalize whitespace),
- canonicalize evidence payloads before diffing or caching,
- avoid non-deterministic iteration over maps/sets in code paths.

---

## 🛡️ CARE gate requirements

The CARE gate MUST occur **before**:

- any user-facing synthesis,
- any Story Node emission,
- any export of spatial geometry beyond governed precision.

Minimum policy functions:

- generalize sensitive coordinates to H3/region bounds,
- enforce minimum cluster size before summarization,
- block or mask restricted collections per sovereignty policy,
- emit policy events for every redaction/allow/deny decision.

### Required policy outputs

The `care_gate` step MUST emit:

- `policy_events` (machine-readable),
- `redaction_summary` (counts, reasons, scopes),
- `evidence_redacted` (safe-to-use evidence set).

---

## 📦 Required artifacts

Each workflow execution SHOULD produce the following evidence artifacts (as refs/paths):

- provenance:
  - PROV-O JSON-LD bundle reference
  - OpenLineage event references (by step/run id)
- catalog evidence (when used):
  - STAC Item reference for retrieval episode
  - DCAT distribution refs when datasets are surfaced
- telemetry (when enabled):
  - latency and stage timings
  - energy and CO2e references
  - policy gate counters (allow/deny/redact rates)

All artifacts MUST be linkable to the run via stable identifiers in the provenance bundle.

---

## 🧪 Validation and CI expectations

Workflow YAML changes SHOULD trigger validation:

- YAML lint and schema validation (workflow contract keys present)
- Mermaid parse validation (if diagrams updated)
- policy lint (OPA/Rego or equivalent) for CARE gate rules
- provenance validation (PROV-O bundle schema; OpenLineage event shape)
- redaction tests (no sensitive coordinates emitted in examples/log fixtures)

---

## 🧰 Authoring checklist

Before adding or changing a workflow:

- ensure determinism section is present and complete,
- ensure a CARE gate step exists before synthesis/output,
- ensure provenance emission is included (even for dry-runs),
- ensure examples contain no restricted/sensitive locations,
- update version history and keep the footer governance links intact.

---

## 🕰️ Version history

| Version  | Date       | Summary |
|---------:|------------|---------|
| v11.2.6  | 2025-12-13 | Initial governed workflow reference for DRIFT Search; codified determinism controls, CARE gates, and required evidence artifacts. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />

[⬅ Back to DRIFT Search](../README.md) ·
[🔍 Search Index](../../README.md) ·
[🏛️ Governance](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🛰 Telemetry Schema](../../../../schemas/telemetry/drift-search-v11.json)

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

