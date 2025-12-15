---
title: "✅ Kansas Frontier Matrix — Validation & FAIR+CARE Compliance Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/validation/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_uuid: "urn:kfm:doc:tools:validation:readme:v11.2.6"
doc_kind: "Operational Specification"
intent: "tools-validation"
role: "validation-registry"
category: "Validation · Governance · FAIR+CARE · Sovereignty"
semantic_document_id: "kfm-doc-tools-validation"
immutability_status: "mutable-plan"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-validation-registry-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_benefit_level: "High"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "tools/validation/README.md@v10.0.0"
  - "tools/validation/README.md@v10.2.2"
  - "tools/validation/README.md@v10.3.0"
  - "tools/validation/README.md@v10.3.1"
  - "tools/validation/README.md@v11.0.0"
  - "tools/validation/README.md@v11.0.1"
  - "tools/validation/README.md@v11.2.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalDuration"
  prov_o: "prov:Activity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/tools-validation-readme-v11.json"
shape_schema_ref: "../../../schemas/shacl/tools-validation-readme-v11.shape.ttl"

event_source_id: "ledger:tools/validation/README.md"

ai_training_allowed: false
ai_training_guidance: "Do not use validation logs as training input."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: true

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_readable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
lifecycle_stage: "operational"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next validation-tools architecture update"
---

<div align="center">

# ✅ **Kansas Frontier Matrix — Validation & FAIR+CARE Compliance Tools**
`tools/validation/README.md`

**Purpose**  
The authoritative validation suite for **structural correctness, governance safety, ethics, sovereignty,
explainability, and sustainability telemetry** across the Kansas Frontier Matrix.

<img src="https://img.shields.io/badge/FAIR%2BCARE-Validation%20Certified-gold" />
<img src="https://img.shields.io/badge/License-MIT-green" />
<img src="https://img.shields.io/badge/DCAT--3.0-Integrated-green" />
<img src="https://img.shields.io/badge/STAC-Profiled-blue" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />

</div>

---

## 📘 Overview

The **Validation & FAIR+CARE Compliance Suite** defines and enforces the **governed correctness** of:

- **Data lifecycle** artifacts (`data/raw → data/work → data/processed → publish`)
- **Catalogs and metadata** (STAC, DCAT, JSON-LD, contracts, telemetry)
- **Pipeline outputs** (ETL, enrichment, inference, exports)
- **Integrity and provenance** (hash chains, manifest alignment, release attestation)
- **AI accountability** (explainability coverage, bias/fairness auditing, drift gates)
- **Sovereignty and ethics** (CARE labels, Indigenous protection policy compliance)
- **Sustainability** (energy/carbon telemetry requirements and thresholds)

This suite is the **single operational source of truth** for validation behavior across:

- `tools/**` (tooling and governance automation)
- `.github/workflows/**` (CI/CD enforcement and release gates)
- `src/pipelines/**` (ETL + AI pipeline orchestration)
- `schemas/**` (JSON Schema / SHACL / telemetry schemas)
- Focus Mode safety + explainability screens (consumer of validation artifacts)

### What this suite does not do

- It does **not** relax policy for performance.
- It does **not** mint new facts or “fix” data silently.
- It does **not** publish sensitive content to logs or reports (fail-closed on policy violations).

---

## 🗂️ Directory Layout

The directory tree below is **KFM-MDP box-safe** and uses the required `~~~text` fence.

~~~text
📁 tools/                                         — Tooling and utilities for development, validation, governance
└── 📁 validation/                                — ✅ Validation + FAIR+CARE compliance suite (this directory)
    ├── 📄 README.md                              — This file (registry + runbook + contracts)
    │
    ├── 📄 faircare_validator.py                  — (entrypoint) CARE, sovereignty, licensing, A11y, ethics
    ├── 📄 schema_check.py                        — (entrypoint) STAC/DCAT/JSON-LD/contracts/telemetry validation
    ├── 📄 ai_explainability_audit.py             — (entrypoint) explainability + bias/fairness checks
    ├── 📄 checksum_audit.py                      — (entrypoint) SHA-256 integrity + manifest alignment
    │
    ├── 🧾 validator_manifest.json                — Roll-up results + hashes + telemetry linkage (output artifact)
    └── 🧾 metadata.json                          — Validation profile configuration (JSON-LD or JSON)
~~~

Notes:

- The file list above reflects the **contracted entrypoints and artifacts referenced by this README**.
- If your branch restructures these entrypoints (e.g., moves code into `validators/`), update this tree and
  preserve the same external interfaces (inputs/outputs) described below.

---

## 🧭 Context

### Where validation sits in KFM v11+

Validation is the core **governance gate** that sits between “generated” and “ship-ready.”

~~~text
CI / Operator
   ↓
💻 tools/cli (optional wrapper)
   ↓
✅ tools/validation   — you are here
   ↓
🏛 tools/governance   — ledger syncing, policy attestations
   ↓
📡 tools/telemetry    — energy/carbon/system metrics aggregation
   ↓
🤖 tools/ai/drift     — drift evaluation (baseline vs candidate), consumed by validation gates
   ↓
📦 releases/          — SBOM, manifests, attestations, telemetry snapshots
~~~

### Non-optional enforcement

- No dataset, model, or catalog record is promoted unless validation passes.
- Validation outputs are treated as **governed artifacts**:
  - machine-readable for CI gates
  - human-readable for review
  - provenance-linked for audits

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Dataset / Model / Metadata"] --> B["Schema Check\n(STAC · DCAT · JSON-LD · Contracts · Telemetry)"]
  B --> C["FAIR+CARE Validator\n(Sovereignty · A11y · Ethics · License)"]
  C --> D["Checksum Audit\n(SHA-256 Integrity Chains · Manifest)"]
  D --> E["AI Explainability & Bias Audit\n(SHAP/LIME coverage · Fairness metrics)"]
  E --> F["Drift Gate\n(Baseline vs Candidate)\n↳ tools/ai/drift artifacts"]
  F --> G["validator_manifest.json\nDecision · Telemetry linkage · Signing hash"]
~~~

Interpretation:

- **Schema → Governance → Integrity** must pass before AI audits can be trusted.
- Drift is evaluated as a **gate** (not as a narrative generator): it blocks unsafe or unstable changes.

---

## 🧠 Story Node & Focus Mode Integration

Validation outputs are **evidence-grade** and may be linked from Story Nodes and Focus Mode panels.

### Story Nodes

A Story Node that references validation must:

- treat validation results as **facts** (metric values, pass/fail, timestamp),
- link to the corresponding manifest/report as evidence,
- avoid converting validation warnings into historical claims.

### Focus Mode

Focus Mode may surface validation status as a quality overlay, for example:

- “This layer is certified for current release”
- “This model output is blocked pending bias audit”
- “Drift exceeded threshold for county-slice X; safer mode enabled”

Focus Mode MUST NOT use validation artifacts to:

- invent provenance,
- “justify” speculative narrative,
- override sovereignty masking.

---

## 🧪 Validation & CI/CD

### CI enforcement profiles (minimum)

This suite is expected to be invoked by CI workflows and/or release pipelines with at least:

- schema validation (STAC/DCAT/JSON-LD/contracts/telemetry)
- FAIR+CARE + sovereignty checks
- checksum + manifest alignment
- AI explainability + bias audit checks
- drift gate evaluation (consuming `tools/ai/drift` artifacts or equivalent output)

### Recommended local workflow

Use deterministic inputs and a config snapshot whenever possible.

~~~bash
# Example: run schema + governance + integrity checks (entrypoints shown for clarity)
python tools/validation/schema_check.py --target data/processed --out data/reports/validation/schema.json
python tools/validation/faircare_validator.py --target data/ --out data/reports/validation/faircare.json
python tools/validation/checksum_audit.py --manifest data/checksums/manifest.json --out data/reports/validation/checksums.json

# AI audits (run only when applicable; may be skipped in lightweight CI)
python tools/validation/ai_explainability_audit.py --model mcp/model_cards/<model_id> --out data/reports/validation/ai.json

# Drift gate (baseline vs candidate) is computed in tools/ai/drift and referenced here
# python tools/ai/drift/run_drift_eval.py --baseline <ref> --candidate <ref> --out mcp/runs/drift/<run_id>/
~~~

### What should fail CI

Validation SHOULD fail closed (block merge/release) on:

- schema errors on governed outputs (STAC/DCAT/JSON-LD/contracts)
- missing or invalid license/provenance fields required by policy
- checksum mismatch vs manifest (tamper or accidental regression)
- AI output lacking required explainability artifacts (where required)
- bias/fairness audit violations or missing audits for required models
- drift exceeding configured thresholds on protected slices or critical tasks
- any restricted-coordinate leakage into artifacts/logs

---

## 📦 Data & Metadata

### Core artifacts

At minimum, a governed validation run should produce:

- **Structured outputs** (machine readable)
  - `validator_manifest.json` (roll-up + decision + signing hash)
  - stage outputs (schema/faircare/checksum/ai/drift summaries)
- **Traceability hooks**
  - release/build identifiers (commit hash, manifest hash)
  - references to telemetry snapshots
  - provenance pointers (PROV sidecar or ledger event id)

### Example validation session record

~~~json
{
  "id": "validation_session_v11.2.6_example",
  "schema_passed": true,
  "checksum_verified": true,
  "faircare_compliant": true,
  "ai_explainability_score": 0.998,
  "bias_index": 0.017,
  "drift_status": "pass",
  "energy_wh": 2.4,
  "carbon_gco2e": 2.8,
  "validated_entities": [
    "data/processed/hydrology/streamflow.parquet"
  ],
  "signing_hash": "sha256:5a8b883f9...",
  "governance_registered": true,
  "timestamp": "2025-12-15T00:00:00Z",
  "validator": "@kfm-validation-core"
}
~~~

### Retention and review

| Artifact | Retention | Notes |
|---|---:|---|
| Schema validation outputs | ≥ 180 days | Rotated and archived via CI cleanup |
| FAIR+CARE logs | ≥ 365 days | Used for audits & re-certifications |
| Checksum manifests | Permanent | Required for traceability |
| Signed manifests / attestations | Permanent | Release integrity artifacts |
| Telemetry snapshots (raw) | ≥ 90 days | Summaries persisted in governance reports |

### Sustainability telemetry targets (v11)

| Metric | Target |
|---|---:|
| Energy/run | ≤ 2.5 Wh |
| Carbon/run | ≤ 3.0 gCO₂e |
| FAIR+CARE pass rate | 100% |

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT 3.0

- Validation outputs may be represented as a `dcat:Dataset` (“KFM Validation Runs”).
- `validator_manifest.json` and stage reports are `dcat:Distribution`s.
- `semantic_document_id` maps to `dct:identifier`.

### STAC

- Validation outputs can be represented as non-spatial STAC Items:
  - `geometry: null`
  - `properties.datetime = run timestamp`
  - assets: `validator_manifest.json`, stage reports, telemetry pointers

### PROV-O

- Inputs (datasets/models/baselines) are `prov:Entity`s.
- The validation run is a `prov:Activity`.
- Artifacts are generated `prov:Entity`s linked via `prov:wasGeneratedBy`.
- CI bots/councils/maintainers are `prov:Agent`s.

---

## 🧱 Architecture

### Stage responsibilities (contract)

#### 1) Schema validation (`schema_check.py`)

Validates:

- STAC (with KFM profiles/extensions)
- DCAT 3.0 dataset/distribution descriptors
- Story Node schema and governed JSON-LD metadata
- Telemetry schemas (tools + pipelines)
- Data Contracts (`data_contract_ref`)

Outputs include:

- `schema_passed` boolean
- error/warning lists
- list of validated entities/paths

#### 2) FAIR+CARE validation (`faircare_validator.py`)

Enforces:

- CARE label presence and propagation
- Sovereignty conflicts & Indigenous data protection constraints
- Licensing and reuse conditions
- Accessibility metadata expectations (A11y hints, alt text coverage for docs/UX artifacts)

#### 3) Integrity validation (`checksum_audit.py`)

Responsibilities:

- compute SHA-256 for governed artifacts
- compare vs checksum manifests and release manifests
- classify manifest status (`up_to_date`, `missing`, `mismatch`)
- emit tamper-detection signals

#### 4) AI accountability validation (`ai_explainability_audit.py`)

Responsibilities:

- verify explainability artifact coverage when required
- verify bias/fairness audit presence and thresholds
- verify AI usage constraints are not violated (policy-aligned behavior)

#### 5) Drift gate (consumes `tools/ai/drift` outputs)

Responsibilities:

- compare baseline vs candidate on defined slices
- block or warn on significant drift thresholds (especially on policy-sensitive slices)
- record drift evidence links in `validator_manifest.json` (do not re-derive drift implicitly)

### Extension points

New validators must:

- be deterministic (config-driven)
- produce machine-readable artifacts
- integrate into `validator_manifest.json`
- respect sovereignty and redaction requirements
- ship with tests validating schema + policy enforcement

---

## ⚖ FAIR+CARE & Governance

### Governance matrix (enforcement mapping)

| Principle | Enforced by | Typical checks | Oversight |
|---|---|---|---|
| **F1 — Findable** | schema_check | stable IDs, catalog references, identifiers | `@kfm-data` |
| **A1 — Accessible** | faircare_validator | access labels, format expectations | `@kfm-accessibility` |
| **I1 — Interoperable** | schema_check | STAC/DCAT/JSON-LD + contract validation | `@kfm-architecture` |
| **R1 — Reusable** | faircare_validator + checksum_audit | license + provenance + integrity | `@kfm-governance` |
| **Collective Benefit** | faircare_validator | harm-aware gating, impact flags | `@faircare-council` |
| **Authority to Control** | faircare_validator | sovereignty blocking on violations | `@kfm-governance` |
| **Responsibility** | telemetry integration | energy/carbon reporting required | `@kfm-security` |
| **Ethics** | ai_explainability_audit + drift gate | bias + drift + explainability | `@kfm-ethics` |

### Fail-closed sovereignty rule

If a validation artifact would expose restricted locations or protected knowledge:

- redact or generalize outputs, **or**
- block publication and require manual review

The correct default is **fail closed**, not “log more.”

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| v11.2.6 | 2025-12-15 | Updated to KFM-MDP v11.2.6 (approved H2s, tilde fences), added explicit AI transform limits, clarified drift gate integration via `tools/ai/drift`. |
| v11.2.2 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; emoji directory layout; clarified FAIR+CARE, AI audit, sustainability integration. |
| v11.0.1 | 2025-11-24 | Cross-toolchain upgrade; v11 telemetry; sovereignty gates; box-safe fences and diagrams. |
| v11.0.0 | 2025-11-19 | First v11 rewrite of validation suite; integrated contracts, STAC/DCAT, governance-led pipelines. |
| v10.x | 2023–2025 | Earlier validation pipeline generations; pre-v11 governance and telemetry semantics. |

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
✅ Validation & FAIR+CARE Tools · MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

[⬅️ Back to Tools Index](../README.md) ·
[🧱 Tools Architecture](../ARCHITECTURE.md) ·
[🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>