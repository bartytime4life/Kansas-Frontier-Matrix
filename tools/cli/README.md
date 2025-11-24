---
title: "💻 Kansas Frontier Matrix — Command Line Interface Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/cli/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_guid: "urn:kfm:doc:tools-cli-readme-v11.0.0"
semantic_document_id: "kfm-tools-cli"
doc_kind: "Overview"
intent: "tools-cli"
role: "cli-governor"
category: "CLI · Governance · Validation · Automation"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-cli-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "tools/cli/README.md@v9.5.0"
  - "tools/cli/README.md@v9.7.0"
  - "tools/cli/README.md@v10.0.0"
  - "tools/cli/README.md@v10.2.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalDuration"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/tools-cli-readme-v11.json"
shape_schema_ref: "../../../schemas/shacl/tools-cli-readme-v11.shape.ttl"

ai_training_allowed: false
ai_training_guidance: "CLI logs and governance data MUST NOT be used for training."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: true

machine_readable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
lifecycle_stage: "operational"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next CLI-layer architecture update"
immutability_status: "mutable-plan"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Command Line Interface Tools (v11)**  
`tools/cli/README.md`

**Purpose:**  
Define the governed, FAIR+CARE-certified **Command Line Interface Platform** that powers KFM’s  
validation, governance, provenance, sustainability, dataset, and AI audit operations.

This suite is a **critical governance surface** — all dataset promotions, ledger updates,  
AI explainability audits, checksum verifications, sustainability exports, and Story Node  
validations MUST flow through a safe, deterministic CLI entrypoint.

[![MCP v6.3](https://img.shields.io/badge/MCP--DL-v6.3-blue)](#)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-CLI%20Certified-gold)](#)  
[![MIT](https://img.shields.io/badge/License-MIT-green)](#)  
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Aligned-teal)](#)

</div>

---

# 📘 1. Overview

The **KFM CLI Platform (kfm)** implements:

- Dataset validation (schema, FAIR+CARE, checksum, sovereignty)
- Governance ledger synchronization (signed & append-only)
- Release artifact metadata updates (manifest + SBOM alignment)
- AI fairness, drift, and explainability audits (Focus Mode v3)
- Sustainability / carbon / energy telemetry export (ISO 50001 + 14064)
- Batch pipeline runs and multi-step automation sequences

It is designed for:

- **Operators**  
- **Data engineers**  
- **FAIR+CARE governance reviewers**  
- **Autonomous pipelines (LangGraph v11)**  
- **CI/CD workflows**  

Every CLI action produces:

- Structured JSON logs  
- Telemetry records  
- Governance ledger entries  
- Deterministic metadata artifacts  

---

# 🗂️ 2. Directory Layout (KFM-MDP v11)

~~~~text
tools/cli/
├── README.md                     ← this file
│
├── kfm_cli.py                    ← main CLI dispatcher
├── metadata_manager.py           ← dataset + STAC/DCAT metadata governance
├── provenance_tracker.py         ← signed ledger update & SLSA/SPDX linkages
├── validator_runner.py           ← FAIR+CARE + schema + checksum validator
├── workflow_launcher.py          ← batch orchestrator (YAML workflows)
└── metadata.json                 ← JSON-LD lineage, config, CARE/sensitivity profiles
~~~~

All files must:

- Run offline deterministically  
- Emit SHA-256 lineage  
- Respect CARE masking rules  
- Align with pipeline contract v11  

---

# ⚙️ 3. CLI Architecture Flow

~~~~mermaid
flowchart TD
    A["User / CI Command"] --> B["kfm_cli.py\nDispatcher"]
    B --> C["validator_runner.py\nSchema · FAIR+CARE · Checksums"]
    C --> D["metadata_manager.py\nMetadata · Licensing · Contracts"]
    D --> E["provenance_tracker.py\nSigned Ledger Update"]
    E --> F["Telemetry Export\nEnergy · Carbon · Runtime · CARE"]
~~~~

**Notes for v11 upgrades:**

- All CLI subcommands MUST enforce CARE and sovereignty policies.  
- All outputs are part of the release telemetry bundle.  
- Every validation failure must trigger a CI BLOCK event.  

---

# 🧩 4. Core CLI Commands (v11)

| Command | Purpose | Output |
|--------|---------|--------|
| `kfm validate --dataset <id>` | Runs schema, checksum, FAIR+CARE, sovereignty, accessibility | Validation Report |
| `kfm ledger sync` | Sync governance manifests + append ledger entries | Ledger JSON-LD |
| `kfm ai audit --model <id>` | Explainability + drift + fairness tests | AI Audit Report |
| `kfm checksum verify <path>` | SHA-256 verification & lineage trace | Checksum Manifest |
| `kfm metadata update <dataset>` | Update STAC/DCAT metadata via contracts | Metadata JSON |
| `kfm workflow batch --file <yaml>` | Multi-step batch execution | Batch Report |
| `kfm telemetry report` | Export energy, carbon, FIT, A11y metrics | focus-telemetry.json slice |

All commands must:

- Respect `--dry-run`  
- Emit structured logs (`run.jsonl`)  
- Validate all licenses & consent fields  

---

# 📜 5. Example v11 Governance Record

~~~~json
{
  "id": "cli_registry_v11.0.0",
  "commands_executed": [
    "kfm validate --dataset hydrology_streamflow",
    "kfm ai audit --model focus_transformer_v3",
    "kfm ledger sync"
  ],
  "schema_passed": true,
  "checksum_verified": true,
  "faircare_compliant": true,
  "sovereignty_clearance": "non-sensitive",
  "ai_audit_passed": true,
  "telemetry_logged": true,
  "governance_registered": true,
  "energy_wh": 0.44,
  "carbon_gco2e": 0.51,
  "timestamp": "2025-11-24T15:20:00Z",
  "validator": "@kfm-cli-core",
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

---

# 🧠 6. FAIR+CARE Governance Matrix (v11)

| Principle | Enforcement | Overseen By |
|----------|-------------|-------------|
| Findable | CLI metadata added to STAC/DCAT + telemetry | @kfm-data |
| Accessible | Clear logs, open license, machine-readable outputs | @kfm-accessibility |
| Interoperable | JSON-LD, STAC v1.1, DCAT v3, SPDX | @kfm-architecture |
| Reusable | Deterministic workflows, reproducible configs | @kfm-design |
| Collective Benefit | CLI enables community safety & transparency | FAIR+CARE Council |
| Authority to Control | Consent, sovereignty checks mandatory | @kfm-governance |
| Responsibility | Audit trails, energy/carbon logs | @kfm-security |
| Ethics | AI fairness & safety enforced | @kfm-ethics |

---

# ♻️ 7. Sustainability & Telemetry Requirements

Telemetry must include:

- Energy (Wh)  
- Carbon (gCO₂e)  
- CPU/GPU runtime  
- Memory footprint  
- FAIR+CARE anomalies  
- CARE masking events  
- Batch efficiency scores  

All records flow to:

~~~~text
../../../releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/tools-cli/*.json
~~~~

---

# 🛡 8. Security & Privacy (v11)

CLI tools must:

- Never log PII  
- Sanitize all error messages  
- Use SHA-256 exclusively  
- Never bypass governance policies  
- Reject malformed metadata and unsafe STAC  
- Block merges on sovereignty violations  

---

# ⚖️ 9. Retention Policy

| Artifact | Retention |
|---------|-----------|
| CLI Logs | 90 days |
| Validation Reports | 180 days |
| Governance Records | Permanent |
| Metadata | Permanent |
| Telemetry | 90 days (summaries retained) |

Retention automated via:

`cli_cleanup.yml`

---

# 🕰️ 10. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-24 | Full v11 rewrite; telemetry v4; OP-v11 alignment; sovereignty rules; new governance metadata |
| v10.2.2 | 2025-11-12 | JSON-LD provenance; batch launcher; sustainability logs |
| v10.0.0 | 2025-11-10 | Telemetry schema v2; expanded CLI governance features |
| v9.7.0 | 2025-11-05 | Parallel workflow launcher; energy tracking |
| v9.6.0 | 2025-11-03 | Initial governance-linked CLI framework |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
**KFM-MDP v11 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω**  
[Back to Tools Index](../README.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>