---
title: "🧪 KFM — DRIFT HyDE (Hypothesis-Driven Expansion · Deterministic Templates · CARE Gates)"
path: "docs/search/drift/hyde/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Reference + Runbook"
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

intent: "drift-hyde"
audience:
  - "Search Engineering"
  - "Graph + Provenance Engineering"
  - "Focus Mode Engineering"
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

sensitivity: "HyDE expands user queries; outputs can amplify sensitive context. CARE screening mandatory; no restricted locations in artifacts."
risk_category: "Governed"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:search:drift:hyde:v11.2.6"
semantic_document_id: "kfm-drift-search-hyde"
event_source_id: "ledger:docs/search/drift/hyde/README.md"
immutability_status: "version-pinned"
machine_extractable: true

telemetry_schema: "../../../../schemas/telemetry/drift-search-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

json_schema_ref: "../../../../schemas/json/drift-hyde-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/drift-hyde-v11-shape.ttl"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
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

# 🧪 **KFM — DRIFT HyDE**
`docs/search/drift/hyde/README.md`

**Purpose**  
Define the governed **HyDE (hypothesis-driven expansion)** layer used by DRIFT Search to improve recall in global retrieval,
while maintaining **determinism**, **provenance completeness**, and **CARE/sovereignty protections**.

<img src="https://img.shields.io/badge/Search-DRIFT%20HyDE-blue" />
<img src="https://img.shields.io/badge/Determinism-Required-brightgreen" />
<img src="https://img.shields.io/badge/Provenance-PROV--O%20%2B%20OpenLineage-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

HyDE in DRIFT is a **controlled query-expansion step** that generates a short “hypothesis” representation of the user query
to improve global retrieval (vector/community recall) before graph-local precision retrieval begins.

### Normative posture

HyDE output is:

- **not a factual claim set**, and MUST NOT be presented as evidence,
- an internal retrieval aid that MUST be:
  - deterministic (policy-defined),
  - provenance-logged,
  - CARE-screened (redaction/generalization as required).

Because `redaction_required: true`, HyDE MUST avoid amplifying sensitive details and MUST default to **hash-based query representation** in artifacts.

---

## 🗂️ Directory Layout

~~~text
📁 docs/search/drift/hyde/                             — HyDE reference + governance contract
├── 📄 README.md                                       — This document
├── 📁 templates/                                      — Prompt templates (no secrets; provenance-safe)
│   ├── 🧾 hyde.prompt.template.md                     — Hypothesis prompt template (stable)
│   ├── 🧾 hyde.guardrails.template.md                 — Safety + refusal + redaction phrasing rules
│   └── 🧾 hyde.output.schema.json                     — Output schema for the HyDE envelope
├── 📁 policies/                                       — CARE/sovereignty gates applied to HyDE outputs
│   └── 🧾 hyde_policy.yml                             — Allowed fields, thresholds, and masking rules
└── 📁 examples/                                       — Redacted examples (no sensitive locations)
    ├── 🧾 hyde_request.example.json
    └── 🧾 hyde_response.example.json
~~~

> Template and example files are recommended for consistency. If they do not exist yet, add them under governance review.

---

## 🧭 What HyDE does in DRIFT

HyDE produces a structured “hypothesis envelope” that can be embedded and used to retrieve:

- community summaries,
- candidate entities,
- candidate datasets (STAC/DCAT),
- candidate documents.

HyDE MUST also produce “routing hints” that do not leak restricted detail, such as:

- likely entity types (Person/Place/Event/Dataset/Document),
- generalized time window hints (if present in the query),
- generalized spatial scope (region-level only if allowed),
- optional follow-up questions for local retrieval.

---

## 🧱 Determinism contract (required)

HyDE is governed as a deterministic transform.

### Required controls

HyDE execution MUST record and/or enforce:

- pinned model identifier and runtime version
- stable template version (`hyde.prompt.template.md` + hash)
- `temperature: 0` (or policy-defined deterministic setting)
- fixed max tokens and stop sequences
- fixed locale and timezone
- seed (when supported) recorded in provenance
- canonical input normalization and hashing:
  - whitespace normalization
  - unicode normalization (policy-defined)
  - deterministic query hash

### Deterministic output rule

Given the same:

- normalized query hash,
- constraints,
- template hash,
- model id/version,
- policy bundle hash,

HyDE MUST produce the same envelope fields (or fail closed under policy, returning a deny/redact outcome).

---

## 🛡️ CARE and sovereignty gates

HyDE MUST run under the same governance regime as the rest of DRIFT:

- apply sovereignty filters to any “suggested sources” or “suggested locations”
- generalize any spatial hints (region/H3 coarse) if allowed; otherwise omit
- do not include:
  - precise coordinates,
  - site access directions,
  - restricted dataset endpoints,
  - sensitive identifiers that enable re-identification

### Required gate outputs (minimum)

- `care_gate_status`: `allow` | `redact` | `deny`
- `sovereignty_gate`: `clear` | `restricted` | `conflict` | `unknown`
- `redaction_summary`: counts + normalized reason codes (no sensitive details)

---

## 🧬 HyDE output envelope (contract)

HyDE outputs MUST be machine-validated against a governed schema (example shape below).

### Required fields

- `query_hash` (sha256; normalized)
- `hyde_hypothesis_text` (policy-safe; may be empty if denied)
- `routing_hints` (types/scopes; no sensitive precision)
- `followup_questions` (optional; policy-safe)
- `care_gate_status`, `sovereignty_gate`, `redaction_summary`
- provenance anchors:
  - `template_hash`
  - `policy_bundle_hash`
  - `model_id`
  - `code_commit_sha`

### Example (schematic; redaction-safe)

~~~json
{
  "query_hash": "sha256:…",
  "hyde_hypothesis_text": "A generalized summary of the inquiry, avoiding sensitive location specificity.",
  "routing_hints": {
    "entity_types": ["Place", "Event", "Document", "Dataset"],
    "temporal_hint": { "start": "1800-01-01", "end": "1900-12-31" },
    "spatial_hint": { "scope": "Kansas (generalized)", "h3_resolution": 6 }
  },
  "followup_questions": [
    "Which counties or regions (non-sensitive) are relevant to this query?",
    "Which time range constraints should be applied?"
  ],
  "care_gate_status": "redact",
  "sovereignty_gate": "unknown",
  "redaction_summary": {
    "events_total": 2,
    "reasons": ["spatial_precision_reduced", "restricted_terms_masked"]
  },
  "provenance": {
    "template_hash": "sha256:…",
    "policy_bundle_hash": "sha256:…",
    "model_id": "hyde-model:<pinned>",
    "code_commit_sha": "<latest-commit-hash>"
  }
}
~~~

---

## 🗺️ HyDE within the DRIFT workflow

~~~mermaid
flowchart TD
  A["User query (normalized)"] --> B["HyDE expansion (deterministic)"]
  B --> C["CARE / sovereignty gate"]
  C --> D["Vector anchor retrieval"]
  D --> E["Neo4j local retrieval"]
  E --> F["Synthesis (evidence-led)"]
  F --> G["Emit provenance + STAC episode item (optional)"]
~~~

---

## 📜 Provenance and telemetry mapping

HyDE MUST be represented as a first-class provenance activity.

### PROV-O (minimum mapping)

- `prov:Activity`: `drift_hyde_expand`
- `prov:Entity` (inputs):
  - query hash entity
  - constraints entity
  - template entity (by hash)
  - policy bundle entity (by hash)
- `prov:Entity` (outputs):
  - hyde envelope entity (by episode id)
  - routing hints entity (optional)
  - policy events entity
- `prov:Agent`:
  - software agent executing HyDE (runner)
  - model agent reference (as a software agent descriptor)

### OpenLineage (recommended mapping)

Emit step-level OpenLineage events:

- job: `drift/hyde_expand`
- run id: stable per episode
- inputs/outputs: query hash entity, hyde envelope entity, policy events entity

### Telemetry hooks (recommended)

- latency (ms) for HyDE generation + gating
- token counts (if applicable)
- redaction event counters

---

## 🧪 Validation and CI expectations

HyDE changes SHOULD be gated by:

- schema validation for the HyDE envelope (`hyde.output.schema.json`)
- determinism tests (golden-run snapshot tests with fixed inputs)
- leakage tests:
  - no coordinates-like patterns (policy threshold)
  - no restricted endpoint leakage
  - no secrets/tokens
- governance compliance:
  - required gate fields emitted
  - policy bundle hash recorded
  - provenance anchors present

---

## 🧠 Focus Mode integration rules

HyDE output MAY be used for retrieval routing but MUST NOT be treated as evidence.

Focus Mode MUST:

- cite evidence from governed sources (STAC/DCAT/graph/documents), not HyDE text
- preserve CARE gating notes in outputs when applicable
- avoid surfacing any redacted content that HyDE might have internally processed

---

## 🕰️ Version history

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Initial governed DRIFT HyDE reference; codified deterministic controls, CARE gates, envelope contract, and provenance mapping. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />

[⬅ Back to DRIFT Search](../README.md) ·
[🔍 Search Index](../../README.md) ·
[📜 DRIFT Provenance](../provenance/README.md) ·
[🏛️ Governance](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🛰 Telemetry Schema](../../../../schemas/telemetry/drift-search-v11.json)

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

