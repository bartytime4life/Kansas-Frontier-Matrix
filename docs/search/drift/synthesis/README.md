---
title: "🧠 KFM — DRIFT Synthesis (Evidence-Led Narrative · CARE Enforcement · Story Node v3 Output)"
path: "docs/search/drift/synthesis/README.md"

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

intent: "drift-synthesis"
audience:
  - "Search Engineering"
  - "Focus Mode Engineering"
  - "Graph + Provenance Engineering"
  - "Governance Reviewers"

classification: "Public (Governed)"
fair_category: "F1-A2-I2-R2"
care_label: "CARE-Aware Retrieval"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
redaction_required: true
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

sensitivity: "Synthesis touches heritage-context retrieval outputs; CARE screening mandatory and leakage-resistant."
risk_category: "Governed"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:search:drift:synthesis:v11.2.6"
semantic_document_id: "kfm-drift-search-synthesis"
event_source_id: "ledger:docs/search/drift/synthesis/README.md"
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
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"
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

# 🧠 **KFM — DRIFT Synthesis**
`docs/search/drift/synthesis/README.md`

**Purpose**  
Define the governed **synthesis layer** for DRIFT Search: how redacted evidence is transformed into an
**evidence-led narrative output** and a **Story Node v3-compatible payload**, while preserving determinism,
provenance, and CARE/sovereignty protections.

<img src="https://img.shields.io/badge/Search-DRIFT%20Synthesis-blue" />
<img src="https://img.shields.io/badge/Evidence-Required-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

DRIFT Synthesis consumes the **CARE-screened evidence bundle** produced by upstream retrieval steps and produces:

- a user-facing response (when allowed),
- a structured **Story Node v3** stub for narrative persistence,
- provenance and telemetry references linking the answer to:
  - the query,
  - the retrieval episode,
  - the evidence entities,
  - the redaction/policy events.

### Governance posture

Because `redaction_required: true` and `sensitivity_level: Medium`, synthesis MUST be **leakage-resistant**:

- it MUST NOT reconstruct sensitive coordinates or restricted site specifics,
- it MUST NOT “fill gaps” with invented details,
- it MUST prefer generalized spatial language (region-level) and clearly label uncertainty.

Synthesis is allowed only as **evidence-led output** under KFM governance.

---

## 🗂️ Directory layout

~~~text
📁 docs/search/drift/synthesis/                       — DRIFT synthesis reference + runbook
├── 📄 README.md                                      — This document
└── (optional) templates/                             — Prompt/policy templates (must be provenance-safe)
~~~

> This directory is documentation-first. If a code implementation exists elsewhere, this README defines the contract it MUST follow.

---

## 🧭 Inputs and outputs

### Inputs (required)

Synthesis expects a pre-screened, policy-safe evidence package.

Minimum inputs:

- `query_text` (normalized) and `query_hash`
- `retrieval_episode_id` (stable id)
- `evidence_redacted` (safe evidence set)
- `policy_events` (allow/deny/redact decisions)
- `constraints` (time range, bbox, user role, scope)
- provenance references:
  - `prov_bundle_ref` (PROV-O JSON-LD path or id)
  - `openlineage_run_id` (if emitted)
  - `stac_item_ref` (if used to represent the retrieval episode)

### Outputs (required)

Minimum synthesis outputs:

- `answer` (text, or empty if blocked)
- `evidence_refs[]` (machine-readable identifiers, not raw content)
- `storynode_stub` (structured payload; facts/interpretation/speculation separated)
- `safety_notes[]` (if any constraints were applied)
- telemetry summary references (latency, token counts, gate outcomes)

---

## 🧬 Synthesis pipeline (governed)

DRIFT Synthesis is a controlled transformation, not free-form generation.

### Stage A — Assemble and normalize evidence

- deduplicate evidence references (stable ordering),
- enforce type constraints (Document, Dataset, Place, Event, Person, Run/Activity),
- compute a deterministic “evidence pack” hash.

### Stage B — Plan a response from evidence only

- build a short outline from evidence summaries and metadata,
- select the minimal evidence required to answer,
- record “coverage” (how much of the answer is supported).

### Stage C — Compose with constraints and CARE posture

- generate the narrative with:
  - generalized location phrasing,
  - explicit temporal bounds,
  - uncertainty labels where evidence is thin,
  - no sensitive procedural content.

### Stage D — Verify and harden

- enforce that factual claims map to at least one `evidence_ref`,
- detect contradictions across evidence and either:
  - present both possibilities,
  - or block with a “needs review” outcome (policy-dependent),
- re-run leakage checks against the composed output.

### Stage E — Emit structured payloads and references

- create a Story Node v3 stub:
  - facts (evidence-backed),
  - interpretation (reasoned),
  - speculation (explicitly hypothetical, optional and often disabled),
- export provenance references:
  - `prov:wasDerivedFrom` pointers to evidence entities,
  - `prov:wasGeneratedBy` pointing to the synthesis activity.

---

## 🗺️ High-level flow

~~~mermaid
flowchart TD
  A["evidence_redacted + policy_events"] --> B["Assemble evidence pack - stable ordering"]
  B --> C["Plan response from evidence only"]
  C --> D["Compose narrative under constraints"]
  D --> E["Verify - evidence coverage + leakage checks"]
  E --> F["Emit answer + Story Node stub"]
  F --> G["Attach provenance and telemetry refs"]
~~~

---

## 🛡️ CARE and sovereignty enforcement

Synthesis MUST enforce the following, even if upstream gates were applied.

### Leakage-resistant rules

- Do not output:
  - precise coordinates,
  - exact site access instructions,
  - “how to locate” restricted places,
  - identifiers that re-enable doxxing of sensitive resources.
- If user query requests restricted specifics:
  - return a generalized response,
  - explain that precision is restricted by policy,
  - include safe alternatives (public datasets or region-level info).

### Required policy signals

Synthesis SHOULD include safe, machine-readable policy results:

- `care_gate_status`: `allow` | `redact` | `deny`
- `redaction_summary`: counts and categories (no sensitive details)
- `sovereignty_gate`: `clear` | `restricted` | `conflict` | `unknown`

---

## 📦 Output contracts

### 1) Answer envelope (recommended)

~~~json
{
  "retrieval_episode_id": "urn:kfm:search:episode:<id>",
  "query_hash": "sha256:<...>",
  "care_gate_status": "redact",
  "answer": "…",
  "evidence_refs": [
    { "kind": "stac", "id": "urn:kfm:stac:item:<...>" },
    { "kind": "prov", "id": "urn:kfm:prov:bundle:<...>" },
    { "kind": "graph", "id": "urn:kfm:entity:<...>" }
  ],
  "safety_notes": [
    "Spatial specificity generalized due to governance policy."
  ],
  "telemetry": {
    "latency_ms": 0,
    "tokens_in": 0,
    "tokens_out": 0,
    "redaction_events": 0
  }
}
~~~

### 2) Story Node v3 stub (recommended shape)

This stub MUST separate facts, interpretation, and speculation.

~~~json
{
  "id": "urn:kfm:storynode:draft:<id>",
  "title": "…",
  "facts": [
    {
      "claim": "…",
      "evidence_refs": ["urn:kfm:stac:item:<...>"],
      "confidence": "high"
    }
  ],
  "interpretation": [
    {
      "note": "…",
      "based_on": ["urn:kfm:entity:<...>"],
      "confidence": "medium"
    }
  ],
  "speculation": [],
  "spatial_extent": {
    "type": "generalized",
    "h3_resolution": 6,
    "region": "Kansas (generalized)"
  },
  "temporal_extent": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "provenance_refs": {
    "prov_bundle_ref": "artifacts/prov/<run>.jsonld",
    "openlineage_run_id": "urn:uuid:<...>"
  }
}
~~~

---

## 🎛️ Determinism requirements

Synthesis must be reproducible and stable.

### Deterministic ordering

- sort evidence by:
  1) entity kind priority (policy-defined),
  2) stable identifier,
  3) timestamp (when available).

### Stable configuration

- pin model identifiers (if used),
- pin templates/policies by version id,
- enforce fixed locale and timezone,
- record all seeds and config hashes into provenance.

### Deterministic serialization

- canonical JSON key ordering for emitted envelopes and stubs,
- stable newline and whitespace rules for stored artifacts.

---

## 🧪 Validation expectations

Synthesis outputs SHOULD be validated by CI checks (policy-dependent), including:

- schema validation of envelope and Story Node stub
- “no raw coordinates” scanner for medium+ sensitivity documents
- evidence coverage check (each fact has at least one `evidence_ref`)
- provenance completeness:
  - `prov:Activity` for synthesis exists,
  - output entities reference `prov:wasDerivedFrom` evidence entities,
  - policy events are represented in the provenance bundle

---

## 🔧 Integration notes

### Focus Mode integration

Synthesis outputs are compatible with Focus Mode when they provide:

- stable `retrieval_episode_id`,
- evidence references that can be resolved through APIs/catalog/graph,
- explicit policy and redaction notes.

### Neo4j and catalog alignment

Synthesis SHOULD reference evidence by identifiers:

- graph entities: `urn:kfm:entity:*`
- STAC items: `urn:kfm:stac:item:*`
- DCAT datasets: `urn:kfm:dcat:dataset:*`
- provenance: `urn:kfm:prov:*`

The response text should avoid embedding long raw metadata blobs; the structured payload carries references.

---

## 🧰 Authoring checklist

Before updating synthesis behavior or this doc:

- confirm CARE gate rules are explicit and non-bypassable,
- confirm output contracts include evidence refs and provenance refs,
- confirm deterministic ordering rules are stated and implementable,
- confirm no examples include sensitive locations or restricted identifiers,
- update version history and keep footer governance links intact.

---

## 🕰️ Version history

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Initial governed DRIFT synthesis reference; codified evidence-led narrative rules, leakage-resistant CARE posture, and Story Node v3 output contracts. |

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

