---
title: "💻 Kansas Frontier Matrix — Command Line Interface Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/cli/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_uuid: "urn:kfm:doc:tools-cli-readme-v11.0.0"
semantic_document_id: "kfm-tools-cli"
doc_kind: "Overview"
intent: "tools-cli"
role: "cli-governor"
category: "CLI · Governance · Validation · Automation"
immutability_status: "mutable-plan"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-cli-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
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
  - "tools/cli/README.md@v11.2.2"
  - "tools/cli/README.md@v11.0.0"
  - "tools/cli/README.md@v10.2.2"
  - "tools/cli/README.md@v10.0.0"
  - "tools/cli/README.md@v9.7.0"
  - "tools/cli/README.md@v9.5.0"

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
---

<div align="center">

# 💻 Kansas Frontier Matrix — Command Line Interface Tools

`tools/cli/README.md`  
v11.2.6 · MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω · Crown∞Ω

**Purpose**  
Define the governed, FAIR+CARE-aligned **CLI platform** that powers KFM validation, governance, provenance, sustainability, dataset, and AI audit operations.

<img alt="MCP-DL v6.3" src="https://img.shields.io/badge/MCP--DL-v6.3-blue">
<img alt="FAIR+CARE governed" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold">
<img alt="License MIT" src="https://img.shields.io/badge/License-MIT-green">
<img alt="ISO 19115 aligned" src="https://img.shields.io/badge/ISO-19115%20Aligned-teal">

</div>

## 📘 Overview

The KFM CLI platform (`kfm`) is a **critical governance surface**.

It provides a deterministic entrypoint for:

- Dataset validation (schema, checksums, FAIR+CARE, sovereignty, and related contracts)
- Governance ledger synchronization (append-only workflows)
- Release artifact alignment (manifest + SBOM references)
- AI audit operations that require explainability and bias review
- Sustainability telemetry export (energy + CO₂e estimates)
- Batch execution of repeatable workflows

Every CLI action should produce:

- Structured logs (machine-readable)
- Telemetry records
- Governance references (where applicable)
- Deterministic artifacts suitable for CI gating

## 🗂️ Directory Layout

~~~text
tools/cli/
├── 📄 README.md
│
├── 📄 kfm_cli.py
├── 📄 validator_runner.py
├── 📄 metadata_manager.py
├── 📄 provenance_tracker.py
├── 📄 workflow_launcher.py
└── 📄 metadata.json
~~~

Notes:

- Filenames above represent the governed CLI surface area described by this document.
- CLI modules should remain **composable** with other tools under `tools/`:
  - `tools/validation/`
  - `tools/governance/`
  - `tools/telemetry/`
  - `tools/ai/`

## 🧭 Context

The CLI layer lives under the repo’s `tools/` subsystem and is intended to be invoked by:

- Human operators (local runs)
- CI workflows
- Release automation pipelines

High-level system placement:

~~~text
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/MapLibre UI → Story Nodes / Focus Mode
~~~

Governance boundary rules:

- CLI should validate and produce artifacts that later feed catalogs/graph loaders.
- UI concerns remain behind APIs; CLI should not couple web UI builds to direct graph access.

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["User / CI Invocation"]
    --> B["kfm_cli.py<br/>Dispatcher & Subcommand Router"]
  B --> C["validator_runner.py<br/>Schema · FAIR+CARE · Checksums"]
  C --> D["metadata_manager.py<br/>STAC/DCAT metadata · Contracts"]
  D --> E["provenance_tracker.py<br/>PROV/SPDX/SLSA linkages"]
  E --> F["Telemetry Export<br/>Energy · Carbon · Runtime · Gate Outcomes"]
~~~

## 🧠 Story Node & Focus Mode Integration

The CLI is expected to support narrative governance workflows:

- Story Node inputs must remain validated and reproducible.
- Focus Mode bundles should be:
  - explainable (where AI-derived),
  - bias-audited (where AI-derived),
  - traceable via provenance identifiers.

Recommended pattern:

- Validate Story Node artifacts with the same schema/contract tooling used in CI.
- Emit a run record that can be referenced by governance review.

## 🧪 Validation & CI/CD

### Core command surface (normative)

These are the canonical subcommand responsibilities the CLI layer SHOULD expose:

- `kfm validate ...`
  - dataset schemas and contracts
  - checksums/integrity checks
  - FAIR+CARE and sovereignty policy checks
- `kfm checksum verify ...`
  - SHA-256 verification and provenance cross-check
- `kfm metadata update ...`
  - STAC/DCAT metadata update workflow (validated and reproducible)
- `kfm ledger sync ...`
  - governance ledger synchronization (append-only)
- `kfm ai audit ...`
  - explainability and bias audit workflows (where AI is used)
- `kfm telemetry report ...`
  - emit telemetry slice for this run

### Required behavior

- Support `--dry-run` on all commands that change artifacts.
- Emit typed exit codes suitable for CI gating:
  - `0` success
  - non-zero typed failures (validation, governance, security, IO, contract mismatch)
- Produce machine-readable logs (prefer NDJSON):
  - include `run_id`, timestamps, versions, and file references.

## 📦 Data & Metadata

### Output artifacts

Recommended default paths:

~~~text
mcp/runs/<run_id>/run.jsonl
mcp/runs/<run_id>/telemetry.json
data/reports/validation/tools-cli/*.json
data/reports/telemetry/tools-cli/*.json
data/reports/audit/*.json
~~~

Minimum fields in each run record:

- `run_id`
- `commit_sha`
- `cli_version` (or doc version reference)
- invoked command(s) + normalized arguments (redacted where needed)
- inputs + outputs (paths or URIs)
- gate outcomes (pass/fail) with typed failure reasons
- schema references (`telemetry_schema`, `energy_schema`, `carbon_schema`)

### Example governance record (illustrative)

~~~json
{
  "id": "cli_registry_v11.2.6_2025-12-15_001",
  "commit_sha": "<latest-commit-hash>",
  "commands_executed": [
    "kfm validate --dataset hydrology_streamflow",
    "kfm ai audit --model focus_model",
    "kfm ledger sync"
  ],
  "schema_passed": true,
  "checksum_verified": true,
  "faircare_compliant": true,
  "ai_audit_passed": true,
  "telemetry_logged": true,
  "timestamp": "2025-12-15T00:00:00Z",
  "validator": "@kfm-cli-core"
}
~~~

## 🌐 STAC, DCAT & PROV Alignment

The CLI layer should preserve contracts across catalog and lineage standards:

- **STAC**
  - Validate STAC items/collections during dataset promotion steps.
  - Ensure checksum fields (when present) match the governed on-disk assets.
- **DCAT**
  - Ensure dataset views remain consistent with release manifests and licensing.
- **PROV**
  - Attach run identifiers and artifact references so data lineage is reconstructable.

The CLI should not silently “fix” metadata; it should **report** and **block** contract violations unless an explicit, governed remediation step is invoked.

## 🧱 Architecture

Design constraints:

- **Determinism:** same inputs + config must reproduce the same outputs (or explain differences).
- **Config-driven:** batch workflows should be expressible in versioned YAML/JSON configs.
- **Composable:** CLI calls into reusable libraries under `tools/validation`, `tools/governance`, `tools/telemetry`, and `tools/ai`.
- **Audit-first:** every action produces a record that can be linked into release provenance and governance review.

## ⚖ FAIR+CARE & Governance

The CLI is a governance enforcement surface:

- Logs and governance data MUST NOT be used for training (`ai_training_allowed: false`).
- The CLI must fail closed on:
  - sovereignty violations,
  - missing attribution/licensing requirements,
  - schema/contract mismatches for governed artifacts,
  - disallowed attempts to bypass policy.

Security & privacy baselines:

- Never log secrets/tokens.
- Never print raw PII or sensitive coordinates; redact or generalize.
- Prefer explicit “safe defaults” (refuse destructive operations without explicit acknowledgement flags).

Retention guidance:

- Retention is governed by authoritative security/governance policies. CLI cleanup tasks should implement the official retention values (do not hard-code “policy” into the CLI without governance sign-off).

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| v11.2.6 | 2025-12-15 | Updated to KFM‑MDP v11.2.6 heading registry and fence rules; normalized artifact paths; clarified governance boundaries and standards alignment. |
| v11.2.2 | 2025-11-27 | Upgraded to KFM‑MDP v11.2.2; emoji directory layout; clarified tool roles, FAIR+CARE integration, and telemetry linkage. |
| v11.0.0 | 2025-11-24 | Full v11 rewrite; telemetry v4; KFM‑OP v11 alignment; sovereignty rules; governance metadata expansions. |
| v10.2.2 | 2025-11-12 | JSON-LD provenance; batch workflow launcher; sustainability logs implemented. |
| v10.0.0 | 2025-11-10 | Telemetry schema v2; expanded CLI governance features and contracts. |
| v9.7.0 | 2025-11-05 | Parallel workflow launcher; basic energy tracking; early governance integration. |
| v9.5.0 | 2025-11-01 | Initial governance-linked CLI framework. |

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
💻 KFM CLI Platform v11.2.6 · FAIR+CARE Governed · MCP‑DL v6.3 · Diamond⁹ Ω · Crown∞Ω

[⬅️ Back to Tools Index](../README.md) · [🧱 Tools Architecture](../ARCHITECTURE.md) · [🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>