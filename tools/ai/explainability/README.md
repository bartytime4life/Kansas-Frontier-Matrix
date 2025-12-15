---
title: "🔎 Kansas Frontier Matrix — AI Explainability Toolkit"
path: "tools/ai/explainability/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-explainability-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability"
event_source_id: "ledger:tools/ai/explainability/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "United States · Kansas"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

ai_training_allowed: false
ai_training_guidance: "Explainability evidence bundles, audit logs, and governance artifacts MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/README.md@v11.2.6"
---

<div align="center">

# 🔎 **KFM — AI Explainability Toolkit**
`tools/ai/explainability/README.md`

**Purpose**  
Define the **explainability (XAI) subsystem** for KFM AI governance:  
what “explainable” means in KFM, what artifacts must exist, how they are validated, and how evidence is bound to provenance and governance.

</div>

---

## 📘 Overview

### What explainability means in KFM (normative)

In KFM, **explainability** is not a vibe and not a screenshot. It is a governed, versioned, reproducible set of **evidence artifacts** that answer:

- **What inputs influenced the output?**
- **Why did the system choose this outcome (or narrative)?**
- **What data sources and transformations were involved?**
- **What constraints/redactions were applied (FAIR+CARE + sovereignty)?**
- **Is the explanation valid for the exact model + dataset version?**

Explainability in KFM is required whenever AI outputs:

- influence user-facing narratives (Focus Mode, Story Nodes),
- affect decisions about certification/promotion of derived artifacts,
- produce classifications/segmentations/forecasts used downstream.

### Explainability is task-aware

Different AI tasks require different evidence shapes:

- **Classification/regression (tabular/time-series):** feature attributions, residual explanations, counterfactual-style deltas (when safe)
- **Remote sensing / geospatial ML:** saliency or attribution overlays (policy-safe), region-based importance summaries
- **Retrieval / ranking:** *retrieval provenance* (which sources were used and why), exposure/coverage summaries
- **Narrative generation:** “evidence density” and grounding traces (citations/links), source contribution summaries, redaction trace

KFM does not mandate a single method everywhere; it mandates a **method registry + evidence bundle contract**.

### Core invariants (normative)

1. Explainability MUST be **config-driven** (thresholds and requirements are not hard-coded).
2. Explainability artifacts MUST be **version-correct**:
   - model identity (ID + version/hash),
   - dataset identity (ID + version),
   - config identity (profile ID + version + sha256).
3. Explainability artifacts MUST be **safe**:
   - no secrets,
   - no PII,
   - no protected-site coordinates,
   - no raw sensitive payloads embedded into reports.
4. Missing required explainability artifacts MUST trigger **fail closed** behavior for certification paths.

---

## 🗂️ Directory Layout

This directory sits under `tools/ai/`:

~~~text
📁 tools/
└── 🧠 ai/
    ├── 🧪 focus_audit.py                      # Explainability runner (often at tools/ai root)
    ├── 📁 configs/                            # Explainability threshold profiles (see configs README)
    └── 📁 explainability/
        └── 📄 README.md                       # This file
~~~

Canonical (intended) explainability subsystem layout:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 explainability/
        ├── 📄 README.md                            # This file
        │
        ├── 📁 methods/                             # Explainability method implementations (pluggable)
        │   ├── 🧾 feature_attribution.json          # Method definition / config (optional)
        │   ├── 🧾 saliency_overlay.json             # Method definition / config (optional)
        │   ├── 🧾 retrieval_provenance.json         # Method definition / config (optional)
        │   └── 🧾 narrative_grounding.json          # Method definition / config (optional)
        │
        ├── 📁 evidence_bundles/                     # Evidence bundle builders (report + artifacts)
        ├── 📁 validators/                           # Bundle validators (schema + completeness + safety)
        ├── 📁 scoring/                              # Coverage/quality scoring utilities
        ├── 📁 redaction/                            # Redaction and masking helpers (policy-aware)
        └── 📁 docs/                                 # Optional publishable notes (policy-safe only)
~~~

Directory rules (normative):

- Do not store run payloads here. Store explainability run artifacts under:
  - `mcp/experiments/<run-id>/...` (preferred),
  - or `mcp/runs/<run-id>/...` if the project uses that structure.
- Do not store large binaries or raw sensitive samples in-repo. Use references/hashes.

---

## 🧭 Context

### When explainability is required

Explainability is REQUIRED for any model/workload that is:

- **user-facing** (Focus Mode and Story Node generation/enrichment),
- **certification-impacting** (outputs promoted to `data/processed/` or release packaging),
- **high-variance over time** (long-running systems with changing distributions).

Explainability may be optional (policy-dependent) for strictly internal experiments, but if the output is promoted or published, explainability becomes required.

### Where explainability runs

Explainability audits may be invoked from:

- CI workflows (governance gates),
- scheduled pipelines (periodic re-audits),
- release packaging (release-to-release comparisons),
- operator runs (manual certification checks).

The explainability subsystem must support offline and deterministic execution.

### What explainability must never do (normative)

Explainability must never:

- expose protected or culturally sensitive site coordinates,
- embed record-level PII into evidence bundles,
- leak secrets via logs or traces,
- “invent” evidence when the underlying data does not support it.

If explanations cannot be produced safely, the correct outcome is **WARN/FAIL with governance action**, not fabrication.

---

## 🗺️ Diagrams

### Explainability audit flow (conceptual)

~~~mermaid
flowchart TD
  A["Select model + dataset slice<br/>(ID + version)"] --> B["Select explainability profile<br/>(configs)"]
  B --> C["Generate explanations<br/>(task-aware methods)"]
  C --> D["Build evidence bundle<br/>(report + artifacts + safety)"]
  D --> E["Validate bundle<br/>(completeness + version + policy)"]
  E --> F["Score explainability<br/>(coverage + quality)"]
  F --> G["Threshold decision<br/>(PASS/WARN/FAIL)"]
  G --> H["Emit telemetry + provenance refs<br/>(energy/carbon + run metadata)"]
  H --> I["Bind results to registry + governance ledgers"]
~~~

Accessibility note: flow from selection → profile → explanation → bundle → validation → scoring → decision → telemetry/provenance → registry.

---

## 🧠 Story Node & Focus Mode Integration

### Why explainability is critical for narrative systems

Focus Mode and Story Nodes must remain **evidence-led** and **governance-safe**.

Explainability for narrative systems should focus on:

- **Source contribution**: which documents/datasets contributed to the narrative and how
- **Grounding coverage**: what fraction of claims are linked to evidence references
- **Redaction trace**: what information was masked/generalized due to policy
- **Stability**: does the narrative remain consistent under small input perturbations (safe proxies only)

### Recommended “evidence density” (concept)

For narrative generation, an explainability bundle SHOULD include safe aggregate measures like:

- `citations_per_1k_tokens`
- `percent_claims_with_evidence_refs`
- `num_sources_used`
- `top_source_contribution` (as a percentage)

These measures must remain policy-safe and must not embed raw content.

### Fail-closed behavior for narrative generation (recommended)

If explainability status is:

- **PASS**: proceed normally.
- **WARN**: proceed with constraints (e.g., retrieval-only mode or limited claims) and trigger review.
- **FAIL**: block production narrative generation or degrade to retrieval-only, per governance policy.

---

## 🧪 Validation & CI/CD

### Determinism rules (normative)

Explainability tooling MUST:

- be config-driven (see `tools/ai/configs/README.md`)
- record the config path and config sha256
- record model + dataset IDs/versions
- pin seeds if sampling is used
- emit stable JSON artifacts

### Minimal outputs (contract)

Each explainability audit SHOULD produce:

- `report.json` (summary + status + scores)
- `evidence_bundle.json` (structured evidence references)
- optional artifacts directory:
  - `artifacts/` (plots/overlays/provenance traces) **only if policy-safe**
- `telemetry.json` (runtime_ms, energy_wh, carbon_gco2e, explainability_score)

### Fail-closed conditions (normative)

Explainability audit MUST return FAIL if:

- model identity is missing/ambiguous,
- dataset identity/version is missing,
- config profile is missing/invalid,
- required evidence bundle sections are missing,
- policy safety checks fail (PII, secrets, sensitive coordinates),
- schema validation fails (when a schema is defined and enforced).

### Recommended CI checks

- config validation (profile has required keys)
- evidence bundle validation (required keys + safe content)
- “no secrets / no PII” scan on outputs intended for repo storage
- deterministic shape checks (stable keys and types)

---

## 📦 Data & Metadata

### Evidence bundle (recommended contract)

An evidence bundle is the governed artifact that describes **what explains what**, without leaking restricted data.

Minimum recommended fields:

- `run_id`
- `status` (`PASS` | `WARN` | `FAIL`)
- model identity:
  - `model_id`, `model_version` (or `model_hash`)
- dataset identity:
  - `dataset_id`, `dataset_version` (or STAC/DCAT refs)
- config identity:
  - `profile_id`, `profile_version`, `config_sha256`
- explanation methods used:
  - method IDs + versions
- evidence references:
  - safe IDs/hashes referencing inputs, retrievals, or feature sets
- scoring:
  - coverage and quality metrics
- policy:
  - redaction flags + applied constraints summary

Example (illustrative):

~~~json
{
  "run_id": "2025-12-15_focus_xai_audit",
  "status": "PASS",
  "model": {
    "model_id": "focus_mode_v3_narrative",
    "model_version": "11.2.6"
  },
  "dataset": {
    "dataset_id": "dcat:kfm:dataset:docs-corpus:v11",
    "dataset_version": "v11"
  },
  "config": {
    "profile_id": "explainability_thresholds.default",
    "profile_version": "11.2.6",
    "config_sha256": "<sha256>"
  },
  "methods": [
    { "method_id": "retrieval_provenance.v1", "method_version": "1.0.0" },
    { "method_id": "narrative_grounding.v1", "method_version": "1.0.0" }
  ],
  "scores": {
    "coverage": 0.98,
    "quality": 0.93,
    "explainability_score": 0.955
  },
  "evidence": {
    "sources_used_count": 42,
    "citations_per_1k_tokens": 7.1,
    "percent_claims_with_evidence_refs": 0.96,
    "source_contributions": [
      { "source_id": "doc:<hash>", "contribution": 0.14 },
      { "source_id": "doc:<hash>", "contribution": 0.11 }
    ]
  },
  "policy": {
    "redactions_applied": true,
    "notes": "Sensitive location details generalized per sovereignty policy."
  },
  "telemetry_ref": "mcp/experiments/2025-12-15_focus_xai_audit/telemetry.json"
}
~~~

### Storage guidance (normative)

Evidence bundles and explainability reports should live under:

~~~text
mcp/experiments/<run-id>/
├── report.json
├── evidence_bundle.json
├── telemetry.json
└── artifacts/   (optional; policy-safe only)
~~~

Do not store evidence bundles in `tools/ai/explainability/` itself.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

If explainability artifacts include spatial overlays (e.g., saliency maps for remote sensing):

- store overlays as governed assets (prefer `data/work/` for intermediate; `data/processed/` if published)
- reference them via STAC Items/Assets (IDs/paths), not embedded binaries

### DCAT

If explainability artifacts are published as part of a dataset release:

- DCAT-aligned dataset metadata should reference:
  - the explainability report/evidence bundle,
  - the model registry entry,
  - licensing and governance labels.

### PROV-O

Each explainability audit should be representable as:

- `prov:Activity` (the audit run)
- consuming Entities:
  - model artifact (Entity),
  - dataset slice (Entity),
  - config profile (Entity)
- producing Entities:
  - report (Entity),
  - evidence bundle (Entity),
  - telemetry record (Entity)
- attributed to Agents:
  - CI runner, maintainer role, governance role (as appropriate)

Goal: explainability artifacts are **traceable lineage events**, not ad-hoc files.

---

## 🧱 Architecture

### Method selection (task-aware, policy-aware)

Explainability methods should be chosen based on model/task type:

- **Tabular/time-series**
  - feature attribution methods (local/global)
  - residual analysis summaries
  - safe counterfactual deltas (only if policy-safe)

- **Deep learning (vision / geospatial)**
  - attribution overlays (saliency/integrated-gradient-style)
  - region-level importance summaries
  - uncertainty proxies (if supported)

- **Retrieval/ranking**
  - retrieval provenance (which items, which ranking signals)
  - coverage metrics (distribution of sources)
  - stability across small perturbations (safe tests)

- **Narrative generation**
  - grounding traces (links to evidence)
  - evidence density metrics
  - redaction trace summaries

### Scoring (recommended)

Explainability scoring should separate:

- **Coverage**: percent of outputs with valid explanations
- **Quality**: stability/fidelity proxies and completeness checks
- **Policy safety**: redaction compliance, sensitive content absence

Config profiles define:

- minimum coverage requirements,
- minimum quality thresholds,
- mandatory bundle fields per task type.

### Default actions (recommended)

- PASS: record bundle + link to registry
- WARN: record bundle + require review (and increase monitoring cadence)
- FAIL: block certification / quarantine dependent promotions

---

## ⚖ FAIR+CARE & Governance

### Policy constraints (normative)

Explainability must comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

This implies:

- no protected-site coordinates,
- no PII,
- no secrets,
- no raw sensitive samples embedded in reports.

### Publication rule

Only policy-safe explainability summaries may be published in `docs/reports/`.  
Full evidence bundles belong in `mcp/experiments/` and should follow governed access practices.

### Training prohibition

Explainability artifacts are governance outputs and MUST NOT be used as AI training data (`ai_training_allowed: false`).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created explainability subsystem README: definitions, artifact contracts, validation rules, scoring guidance, and provenance/governance alignment for KFM AI explainability. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🔎 Explainability · Governed for Integrity

[⬅️ Back to AI Tools](../README.md) · [⚙️ Config Profiles](../configs/README.md) · [🛡 Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>