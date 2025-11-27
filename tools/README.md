---
title: "🛠️ Kansas Frontier Matrix — Tools Directory Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/README.md"
version: "v11.2.2"
last_updated: "2025-11-27"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../releases/v11.2.2/manifest.zip"
data_contract_ref: "../docs/contracts/data-contract-v3.json"
telemetry_ref: "../releases/v11.2.2/tools-telemetry.json"
telemetry_schema: "../schemas/telemetry/tools-registry-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "tools-platform"
role: "architecture"
category: "Tools · Automation · Governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "tools/README.md@v10.3.1"
  - "tools/README.md@v10.3.2"
  - "tools/README.md@v10.4.0"
  - "tools/README.md@v11.0.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "N/A"

json_schema_ref: "../schemas/json/tools-readme.schema.json"
shape_schema_ref: "../schemas/shacl/tools-readme-shape.ttl"

event_source_id: "ledger:tools/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Review required every 6 months"
sunset_policy: "Superseded upon next major tools-platform release"
---

<div align="center">

# 🛠️ **Kansas Frontier Matrix — Tools Directory Architecture (v11)**  
`tools/README.md`

**Purpose**  
Define the **tools-platform architecture** governing all scripts, automations, validators, audits,
governance utilities, telemetry collectors, and CLI interfaces under `tools/**` in the Kansas Frontier Matrix (KFM).  
This document establishes **FAIR+CARE-aligned**, **reproducible**, **sovereignty-safe**, and **telemetry-instrumented**
operational workflows.

</div>

---

## 📘 1. Overview

The `tools/` directory is the **operational automation core** of KFM:

- AI & explainability audit tools  
- FAIR+CARE and sovereignty validation utilities  
- Governance-ledger synchronization commands  
- STAC/DCAT, checksum, and schema validators  
- Telemetry collectors and sustainability reporters  
- CI/CD helpers for docs, builds, security, and deployment  
- CLI interfaces for dataset management, provenance controls, and ETL orchestration  

Every tool:

- Has a defined **contract** (inputs/outputs, side-effects, telemetry)  
- Is referenced in **SBOM** and **manifest** releases  
- Emits **provenance**, **telemetry**, and **governance events**  
- Must comply with **MCP-DL v6.3**, **KFM-PDC v11**, and **FAIR+CARE** ethics constraints  

---

## 🗂️ 2. Directory Layout (Emoji Style A)

```text
tools/
├── 📄 README.md                      # Tools platform architecture (this file)
│
├── 🤖 ai/                            # AI oversight and explainability tools
│   ├── 🧪 focus_audit.py             # Story Node & Focus Mode narrative/grounding audit
│   ├── ⚖️ bias_check.py              # Bias & fairness metrics for models
│   └── 🌡️ drift_monitor.py           # Drift detection and alerting
│
├── ⚙️ ci/                            # CI helper workflows and scripts
│   ├── 📜 docs_validate.yml          # Docs lint + KFM-MDP v11 validation
│   ├── 📜 checksum_verify.yml        # Checksum and SBOM parity checks
│   └── 📜 site_deploy.yml            # Docs + web deployment helper
│
├── 💻 cli/                           # User-facing command-line tools
│   ├── 🧰 kfm_cli.py                 # Main KFM command-line interface
│   └── 🧾 metadata_manager.py        # STAC/DCAT/contract metadata management
│
├── 🏛 governance/                    # Governance and ledger tooling
│   ├── 🔄 governance_sync.py         # Syncs graph/data provenance into governance ledgers
│   ├── 📒 ledger_update.py           # Appends entries to data_provenance_ledger.json
│   └── ✅ certification_audit.py     # Runs certification checks for datasets/models
│
├── 📡 telemetry/                     # Telemetry collection & analysis
│   ├── 📥 telemetry_collector.py     # Aggregates metrics from pipelines and tools
│   ├── 📊 performance_analyzer.py    # SLO metrics and reliability analysis
│   └── 🌱 sustainability_reporter.py # Energy/CO₂ estimates and sustainability reporting
│
└── ✅ validation/                    # Cross-domain validation tools
    ├── ⚖️ faircare_validator.py      # CARE, sovereignty, license & ethics checks
    ├── 📐 schema_check.py           # JSON/YAML/STAC/DCAT/schema validation
    └── 🧠 ai_explainability_audit.py # Ensures explainability artifacts exist for AI models
```

This layout is **GitHub- and mobile-safe**, KFM-MDP-compliant, and will not break boxes.

---

## 🧩 3. Toolchain Architecture

Tools integrate into a **deterministic governance pipeline**:

```text
Trigger (CLI / CI)
   → Validation (schema · STAC/DCAT · FAIR+CARE · sovereignty)
      → Governance (provenance · ledger · certification)
         → Telemetry (OTel v11 · energy/carbon · SLO state)
            → Release (certified, governed workflows)
```

Each execution MUST:

- Be **idempotent** where reasonable (e.g., `--dry-run`, re-run safe)  
- Emit **structured JSON logs** (machine-readable)  
- Update appropriate **governance ledgers** (append-only)  
- Append to **telemetry bundles** in the release artifacts  

---

## ⚖️ 4. FAIR+CARE Governance Architecture

| Principle             | Enforcement Mechanism in `tools/`                                           |
|-----------------------|-----------------------------------------------------------------------------|
| **F1 – Findable**     | Tools registered in SBOM & manifest with unique IDs and metadata           |
| **A1 – Accessible**   | MIT-licensed, consistent CLI UX (`--help`, exit codes)                     |
| **I1 – Interoperable**| Outputs are JSON/YAML/STAC/SPDX/JSON-LD, never proprietary formats        |
| **R1 – Reusable**     | Deterministic behavior, documented contracts, version pinning              |
| **Collective Benefit**| Tools must not weaken protections for communities or data subjects        |
| **Authority to Control** | Governance tools honor CARE/A2C flags and sovereignty policies       |
| **Responsibility**    | Telemetry, error categories, and audit logs required for non-trivial tools |
| **Ethics**            | Bias checks, drift monitoring, explainability audits enforced by `ai/`     |

Governance and FAIR+CARE evidence is recorded in:

```text
data/reports/audit/data_provenance_ledger.json
data/reports/fair/data_care_assessment.json
```

---

## 🏛 5. Governance Integration

Governance tools in `tools/governance/` act as **append-only provenance agents**:

- `governance_sync.py`  
  - Synchronizes data/graph provenance into the global governance ledgers.  

- `ledger_update.py`  
  - Writes **PROV-O** activities (`prov:Activity`) and entities (`prov:Entity`), using:
    - `prov:used`  
    - `prov:generated`  
    - `prov:wasAssociatedWith`  

- `certification_audit.py`  
  - Runs certification checks for datasets/models (FAIR+CARE, schema, integrity).  

All governance writes MUST:

- Include SHA-256 checksums for affected artifacts  
- Record:
  - `tool_name`, `tool_version`, `run_id`, `executor` (user/bot)  
- Include CARE labels & sovereignty zones (e.g., H3 generalization cells) when relevant  
- Be traceable back to CI or CLI invocation  

---

## 🧪 6. Validation Tools

`tools/validation/` provides cross-cutting validators:

- **Schema Validation** — `schema_check.py`
  - Validates JSON/YAML/Parquet schema; STAC/DCAT/Story Node/telemetry shapes aligned with contracts.  

- **FAIR+CARE & Sovereignty** — `faircare_validator.py`
  - Checks license compliance, CARE labels, sovereignty policies, Indigenous data rules.  

- **AI Explainability** — `ai_explainability_audit.py`
  - Ensures that for each production model, appropriate:
    - SHAP/LIME/attention maps exist  
    - Model cards and evaluation reports are up to date  
    - Drift, bias, and usage constraints are documented  

CI/CD gating:

- Failures in `validation/**` stop merges to protected branches.  
- FAIR+CARE and sovereignty violations are treated as **governance-blocking** issues.  

---

## 📡 7. Telemetry Tools

`tools/telemetry/` helps track performance, reliability, and sustainability:

- `telemetry_collector.py`  
  - Aggregates metrics from ETL runs, CI workflows, and tools.  

- `performance_analyzer.py`  
  - Computes SLOs (latency, throughput) and error budgets.  

- `sustainability_reporter.py`  
  - Estimates per-job Wh/gCO₂e using energy/carbon schemas.  

Telemetry outputs MUST:

- Conform to `telemetry_schema: "../schemas/telemetry/tools-registry-v11.json"`  
- Be aggregated into:

```text
../releases/v11.2.2/tools-telemetry.json
```

These telemetry artifacts support:

- Governance dashboards  
- Reliability & performance analysis  
- Sustainability audits (ISO 14064/50001 alignment)  

---

## 🤖 8. AI Oversight Tools

`tools/ai/` implements AI governance:

- `focus_audit.py`  
  - Audits Story Node v3 and Focus Mode v3 outputs for:
    - Data grounding  
    - Narrative safety (no unverified claims, no harmful patterns)  
    - CARE & sovereignty compliance  

- `bias_check.py`  
  - Evaluates group fairness metrics and bias indicators.  

- `drift_monitor.py`  
  - Tracks distributional and concept drift; exports results to audit ledgers.  

Any **critical AI governance failure** MUST:

- Mark the affected model or pipeline as **non-certified**  
- Append a ledger entry:
  - Documenting the issue  
  - Indicating status (`"status": "blocked"`)  
  - Linking to remediation tickets or mitigation plans  

---

## 🧰 9. CLI Tools

`tools/cli/` contains user-facing entrypoints:

- `kfm_cli.py`  
  - Main command-line interface for:
    - Triggering ETL  
    - Registration of datasets  
    - Running validations and governance syncs  

- `metadata_manager.py`  
  - Manages STAC/DCAT metadata and data-contract attachments.  

CLI design:

- **Idempotent** where possible (`--dry-run`, `--force` options)  
- **Exit-code semantics**: `0` success, non-zero value with error categories  
- **Machine-readable outputs** (JSON) by default, with `--human` formatting where needed  

---

## 📈 10. Security & Privacy Requirements

All tools MUST:

- Never log secrets or tokens.  
- Avoid printing full file contents, especially for sensitive sources.  
- Strip or redact detailed coordinates for sensitive/CARE-protected layers in logs.  
- Use environment variables or secret managers (never commit API keys).  

Security workflows (`security_audit.yml`) in `.github/workflows` MUST include the `tools/**` subtree.

---

## 🗃️ 11. Retention & Rotation

| Artifact Type       | Retention           | Rotation Mechanism                |
|---------------------|--------------------:|-----------------------------------|
| Governance Logs     | Permanent           | Append-only; never truncated      |
| Validation Reports  | ≥ 365 days          | Archived as `*.archive.json`      |
| Telemetry Data      | ≥ 90 days (raw)     | Summarized into long-term metrics |
| SBOM/Manifests      | Permanent           | Statement of record               |
| Tool Metadata       | Permanent           | Captured via SBOM & manifests     |

Rotation and compaction handled by scheduled jobs:

```text
tools_cleanup.yml
tools/telemetry/telemetry_compactor.py
```

---

## 🕰 12. Version History

| Version | Date       | Summary                                                                                                        |
|--------:|-----------:|----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; applied emoji directory styling; clarified AI, telemetry, FAIR+CARE, and governance integration. |
| v11.0.0 | 2025-11-24 | First v11 tools platform architecture; introduced sovereignty-aware & telemetry-instrumented tooling.         |
| v10.4.0 | 2025-11-15 | Strict KFM-MDP v10.4 formatting; initial governance + telemetry architecture.                                 |
| v10.3.2 | 2025-11-14 | Enhanced telemetry; clearer FAIR+CARE flow and governance utilities.                                          |
| v10.3.1 | 2025-11-13 | Initial tools architecture for v10.3.                                                                          |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
**KFM Tools Platform v11** · FAIR+CARE Aligned · MCP-DL v6.3 · Sovereignty-Safe · Telemetry-Governed  

[⬅️ Back to Root](../README.md) · [📐 Data Architecture](../ARCHITECTURE.md) · [🛡 Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>