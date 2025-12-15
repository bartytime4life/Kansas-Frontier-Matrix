---
title: "📡 Kansas Frontier Matrix — AI Telemetry & Sustainability Metrics"
path: "tools/ai/telemetry/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-telemetry-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-telemetry"
event_source_id: "ledger:tools/ai/telemetry/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../schemas/json/tools-ai-telemetry-record-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/tools-ai-telemetry-record-v11.shape.ttl"

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
ai_training_guidance: "AI telemetry, audit logs, and governance metrics MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/README.md@v11.2.6"
---

<div align="center">

# 📡 **KFM — AI Telemetry & Sustainability Metrics**
`tools/ai/telemetry/README.md`

**Purpose**  
Define the **telemetry subsystem** for KFM AI governance:  
how AI/ML workloads emit **runtime, quality, drift/fairness/explainability summary scores, and sustainability metrics (energy + carbon)** in a reproducible, policy-safe, schema-valid way.

</div>

---

## 📘 Overview

### What “AI telemetry” means in KFM (normative)

In KFM, **AI telemetry** is a governed, machine-readable record of:

- **What ran** (tool / workflow / pipeline step),
- **What it operated on** (model + dataset identifiers and versions),
- **What happened** (PASS/WARN/FAIL, summary scores),
- **How much it cost** (runtime + compute usage),
- **How sustainable it was** (estimated energy and carbon),
- **Where to find evidence** (references to audit artifacts and provenance bundles).

Telemetry is not “logging.” Telemetry is an **auditable measurement interface** used by:

- CI gating (block/publish decisions),
- governance review (FAIR+CARE),
- sustainability reporting (energy/carbon awareness),
- release packaging (system telemetry snapshots),
- longitudinal monitoring (trend analysis).

### Why telemetry is required

KFM runs long-lived workflows across changing conditions and datasets. Telemetry provides:

- accountability (what changed, when, and why),
- reproducibility (same inputs → same outputs, recorded under stable IDs),
- operational safety (fail-closed if required measurements are missing),
- sustainability tracking (energy/carbon observability, trend-aware choices).

### Core invariants (normative)

1. Telemetry MUST be **schema-valid** (per referenced telemetry schemas).
2. Telemetry MUST be **version-aware**:
   - model ID + version/hash (when applicable),
   - dataset ID + version (or STAC/DCAT references),
   - config profile ID + version + sha256.
3. Telemetry MUST be **policy-safe**:
   - no secrets,
   - no PII,
   - no protected-site coordinates,
   - no raw input samples embedded in telemetry.
4. Telemetry MUST support **linkage**:
   - references to reports/evidence bundles/provenance bundles,
   - references to release packets when applicable.
5. Missing required telemetry fields MUST trigger **fail closed** behavior for certification paths.

---

## 🗂️ Directory Layout

This directory sits under `tools/ai/`:

~~~text
📁 tools/
└── 🧠 ai/
    ├── 📁 configs/                         # Telemetry policies (see tools/ai/configs/README.md)
    └── 📁 telemetry/
        └── 📄 README.md                    # This file
~~~

Canonical (intended) telemetry subsystem layout:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 telemetry/
        ├── 📄 README.md                            # This file
        │
        ├── 📁 collectors/                          # Capture runtime + resource signals (safe-by-default)
        ├── 📁 estimators/                          # Energy/carbon estimation adapters (policy-safe)
        ├── 📁 exporters/                           # Serialize/emit telemetry (JSON/JSON-LD as needed)
        ├── 📁 aggregators/                         # Roll up per-run telemetry to per-release bundles
        ├── 📁 validators/                          # Schema validation + safety checks (no PII/secrets)
        ├── 📁 policies/                            # Telemetry policy helpers (required fields by run type)
        └── 📁 docs/                                # Optional publishable notes (policy-safe only)
~~~

Storage rules (normative):

- Do not store run telemetry payloads in this directory.
- Store per-run telemetry alongside run artifacts:
  - `mcp/experiments/<run-id>/telemetry.json` (preferred),
  - or `mcp/runs/<run-id>/telemetry.json` if used by the repo.
- Release-level telemetry snapshots belong in:
  - `releases/<version>/focus-telemetry.json` (or equivalent per release packet).

---

## 🧭 Context

### Telemetry consumers (who uses it)

Telemetry is used by:

- **CI/CD**: enforce required measurements and fail closed when absent
- **Governance**: verify that audits were run and are current; review energy/carbon impact
- **Release packaging**: capture a “telemetry snapshot” for release packets
- **Maintainers**: monitor regressions in runtime/cost/quality and plan mitigation
- **Focus Mode / Story Node governance**: ensure narrative systems are evidence-led and controlled

### Telemetry producers (what emits it)

Telemetry is produced by:

- AI governance runners:
  - bias/fairness audits (`bias_check`)
  - explainability audits (`focus_audit`)
  - drift monitoring (`drift_monitor`)
- evaluation workflows (model evaluation runs)
- (optional) training workflows (if recorded; be careful with sensitive data)

### Where telemetry belongs in the KFM pipeline

Telemetry sits at the end of governed AI activities:

- activity runs
- results computed
- decision produced (PASS/WARN/FAIL)
- telemetry emitted
- provenance bound
- (optional) registry updated / release packaged

Telemetry is therefore an **output contract** of the governance system.

---

## 🗺️ Diagrams

### Telemetry flow (conceptual)

~~~mermaid
flowchart TD
  A["AI activity executes<br/>(audit / eval / training)"] --> B["Collector captures runtime + environment<br/>(safe subset)"]
  B --> C["Estimator computes energy/carbon<br/>(policy-safe method)"]
  C --> D["Exporter writes telemetry.json<br/>(schema-valid)"]
  D --> E["Validator checks schema + safety<br/>(no PII/secrets)"]
  E -->|PASS| F["Store with run artifacts<br/>(mcp/experiments/<run-id>/...)"]
  E -->|FAIL| G["Fail closed<br/>(block certification/promotion)"]
  F --> H["Aggregator rolls up<br/>release telemetry snapshot"]
  H --> I["Release packet contains telemetry<br/>(releases/<version>/...)"]
~~~

Accessibility note: flow from run → collect → estimate → export → validate → store → aggregate → release.

---

## 🧠 Story Node & Focus Mode Integration

### Why telemetry matters for narrative systems

Focus Mode and Story Node generation are governance-sensitive and should be observable. Telemetry supports:

- audit freshness tracking (when were bias/explainability/drift audits run?),
- performance tracking (latency and runtime budget),
- sustainability tracking (cost of narrative generation workflows),
- operational gating (block narrative generation when required audits/telemetry missing).

### Recommended telemetry fields for narrative systems

For Focus Mode / Story Nodes, telemetry SHOULD include:

- `run_type: "narrative_audit" | "narrative_generation" | "retrieval_only"`
- `evidence_density_score` or equivalent safe aggregate
- counts:
  - number of sources retrieved
  - number of evidence references emitted
- redaction indicators:
  - whether masking/generalization occurred (boolean + safe summary)

Telemetry MUST NOT include:

- raw narrative text,
- raw documents,
- sensitive coordinates,
- PII.

---

## 🧪 Validation & CI/CD

### Determinism rules (normative)

Telemetry emitters MUST:

- be config-driven (telemetry policies in `tools/ai/configs/`)
- record config identity:
  - `profile_id`, `profile_version`, `config_sha256`
- record model/dataset identity when relevant
- be reproducible (no hidden network requirement for telemetry emission itself)
- emit stable JSON keys and types (schema-valid)

### Fail-closed rules (normative)

Telemetry validation MUST FAIL (and block certification/promotion) if:

- required identity fields are missing (run_id, tool, model/dataset where applicable),
- energy/carbon fields are required by policy but missing,
- schema validation fails,
- safety checks detect PII/secrets/protected-site coordinates.

### Recommended CI checks

- JSON schema validation against:
  - `telemetry_schema`
  - `energy_schema`
  - `carbon_schema`
- safety scans (no secrets; no PII)
- invariant checks:
  - `run_id` exists and is stable
  - references to report/evidence bundle exist for audits
  - config sha256 recorded

---

## 📦 Data & Metadata

### Telemetry record contract (recommended minimum)

A telemetry record SHOULD include:

- **Identity**
  - `run_id`
  - `tool` (e.g., `bias_check`, `focus_audit`, `drift_monitor`)
  - `tool_version` (or commit SHA reference)
  - `run_type` (audit/eval/training/generation)

- **Context**
  - `model_id`, `model_version` or hash (when applicable)
  - `dataset_id`, `dataset_version` (or STAC/DCAT refs)
  - `config_profile_id`, `config_profile_version`, `config_sha256`

- **Timing**
  - `started_at`, `ended_at` (ISO times)
  - `runtime_ms`

- **Outcome**
  - `status` (`PASS` | `WARN` | `FAIL`), when applicable
  - summary scores:
    - `bias_score` (if fairness audit)
    - `explainability_score` (if explainability audit)
    - `drift_score` (if drift monitor)
  - counts (safe aggregates only)

- **Sustainability**
  - `energy_wh`
  - `carbon_gco2e`
  - method metadata (how estimation was done; safe descriptor)

- **References**
  - `report_ref` (audit report)
  - `evidence_bundle_ref` (if applicable)
  - `provenance_bundle_ref` (if emitted)
  - `release_ref` (if this run is included in a release packet)

### Example telemetry record (illustrative)

~~~json
{
  "run_id": "2025-12-15_focus_bias_audit",
  "tool": "bias_check",
  "tool_version": "<commit-sha-or-version>",
  "run_type": "audit",
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
    "profile_id": "fairness_thresholds.default",
    "profile_version": "11.2.6",
    "config_sha256": "<sha256>"
  },
  "timing": {
    "started_at": "2025-12-15T00:00:00Z",
    "ended_at": "2025-12-15T00:02:08Z",
    "runtime_ms": 128000
  },
  "scores": {
    "bias_score": 0.97
  },
  "sustainability": {
    "energy_wh": 7.4,
    "carbon_gco2e": 8.2,
    "estimation_method": "policy_default_v1"
  },
  "refs": {
    "report_ref": "mcp/experiments/2025-12-15_focus_bias_audit/report.json",
    "provenance_bundle_ref": "mcp/experiments/2025-12-15_focus_bias_audit/provenance_bundle.jsonld"
  }
}
~~~

### Storage guidance (normative)

Per-run telemetry belongs with the run:

~~~text
mcp/experiments/<run-id>/
├── telemetry.json
├── report.json                  # if audit
└── provenance_bundle.jsonld      # if emitted
~~~

Release telemetry belongs in release packets:

~~~text
releases/<version>/
└── focus-telemetry.json
~~~

Do not store telemetry payloads under `tools/ai/telemetry/`.

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment (lineage)

Every telemetry record should be linkable to a provenance representation:

- telemetry record: `prov:Entity`
- generating activity (audit/eval/training): `prov:Activity`
- associated agent (CI runner / pipeline / operator role): `prov:Agent`

Telemetry should reference the provenance bundle, not duplicate it.

### DCAT alignment (dataset-level)

If telemetry snapshots are published as part of a release packet:

- the release packet may expose telemetry as a distribution artifact
- dataset-level metadata can reference telemetry distributions by path
- telemetry remains policy-scoped; publication must remain governance-approved

### STAC alignment (asset-level, optional)

If telemetry is tied to STAC assets (e.g., evaluation of a spatial output item):

- reference STAC Item IDs and asset keys (safe identifiers)
- do not embed spatial asset content in telemetry

---

## 🧱 Architecture

### Components (recommended)

1. **Collectors**
   - capture runtime, environment-safe metadata, and counts
   - minimal footprint; avoid high-risk fields

2. **Estimators**
   - compute energy/carbon (method must be documented and stable)
   - avoid collecting sensitive infrastructure details
   - record method name/version (safe)

3. **Exporters**
   - serialize telemetry to JSON (and optionally JSON-LD)
   - ensure deterministic key ordering where required by tooling

4. **Validators**
   - schema validation + safety checks
   - fail closed on missing required fields

5. **Aggregators**
   - build release-level rollups and dashboards (policy-safe)
   - aggregate only (avoid row-level event leaks)

### Energy and carbon estimation guidance (policy-safe)

Telemetry should record:

- a safe “method identifier” (e.g., `policy_default_v1`)
- high-level inputs (runtime, hardware class where allowed)
- computed outputs:
  - `energy_wh`
  - `carbon_gco2e`

Avoid recording overly specific machine identifiers, IP addresses, or any data that increases attack surface.

---

## ⚖ FAIR+CARE & Governance

### Policy constraints (normative)

Telemetry must comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

Practical constraints:

- No PII
- No secrets
- No protected-site coordinates
- Avoid high-resolution infrastructure fingerprints

### Publication rule

Only policy-safe telemetry summaries may be published to `docs/reports/`.  
Release packets may include telemetry snapshots when governed and approved.

### Training prohibition

Telemetry and governance metrics MUST NOT be used as AI training data (`ai_training_allowed: false`).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created telemetry subsystem README: defined telemetry invariants, record contract, storage destinations, CI fail-closed rules, sustainability (energy/carbon) guidance, and PROV alignment for KFM AI governance telemetry. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
📡 Telemetry & Sustainability · Governed for Integrity

[⬅️ Back to AI Tools](../README.md) · [⚙️ Config Profiles](../configs/README.md) · [🧾 Provenance](../provenance/README.md) · [🛡 Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>