---
title: "⚙️ Kansas Frontier Matrix — STAC Orchestrator GitHub Integration (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/.github/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-stac-github-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — STAC Orchestrator GitHub Integration**  
`src/pipelines/stac/monitor-validate-publish/.github/README.md`

**Purpose:**  
Document the **GitHub Actions workflows**, CI/CD behaviors, secrets, permissions, artifact flows, FAIR+CARE governance checks, and telemetry integrations used by the *STAC Monitor → Validate → Publish* pipeline in the Kansas Frontier Matrix (KFM).

<img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-Orchestrator-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="CI/CD" src="https://img.shields.io/badge/CI%2FCD-Secure-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Automated-success"/>

</div>

---

## 📘 Overview

This directory documents all **GitHub-integrated automation** powering the STAC orchestrator:

- Scheduled STAC polling with ETag support  
- Great Expectations validation gates  
- Transformation + publication workflows  
- Graph hydration triggers  
- Quarantine + issue creation  
- Artifact packaging & upload  
- Telemetry + sustainability metrics export  
- FAIR+CARE governance synchronization  
- SBOM/manifest linkage and SLSA provenance  

Workflows are defined externally under:

```
.github/workflows/stac-orchestrator.yml
```

but this folder provides all *pipeline-level documentation* needed for maintainers.

---

## 🗂️ Directory Layout (Authoritative)

```
src/pipelines/stac/monitor-validate-publish/.github/
├── README.md                     # This file
└── (No workflow files here)      # Workflows live in repo root .github/workflows
```

This folder is documentation-only and mirrors KFM repo standards.

---

## 🧩 Orchestrator CI Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Cron · Manual Dispatch · Re-run"] --> B["Checkout + Python Setup"]
  B --> C["Poll STAC API<br/>ETag / If-None-Match"]
  C -->|304| Z["No Change · Emit Telemetry"]
  C -->|200| D["Write Incoming Batch<br/>data/incoming/<ts>"]
  D --> E["Great Expectations Validation<br/>stac_item_suite"]
  E -->|PASS| F["Transform → Publish<br/>Items/Collections"]
  E -->|FAIL| G["Quarantine Batch<br/>Open GitHub Issue"]
  F --> H["Neo4j Hydration<br/>Scene/Dataset Relationships"]
  F --> I["Upload Artifacts<br/>Incoming · Published · DataDocs"]
  G --> I
  H --> J["Telemetry Export<br/>focus-telemetry.json"]
  I --> J
~~~~~

---

## 🤖 GitHub Actions Workflow Summary

### `stac-orchestrator.yml`

| Stage | Purpose |
|-------|---------|
| **Checkout** | Pulls the repository state |
| **Python Setup** | Installs GE, ETL libs, STAC tools |
| **Polling** | Calls STAC API with ETag caching |
| **Validation** | Runs GE checkpoints + CARE validators |
| **Publish** | Writes normalized STAC Items/Collections |
| **Graph** | Hydrates Neo4j Scene→Dataset edges |
| **Telemetry** | Exports metrics, sustainability data |
| **Artifacts** | Uploads incoming + published + DataDocs |
| **Issue Creation** | Auto-created for failed batches |
| **Governance Sync** | Updates audit ledgers |

---

## 🔐 Permissions & Security

Workflows require:

| Permission | Scope |
|-----------|--------|
| `contents: write` | Commit updated ETAG cache, upload artifacts |
| `issues: write` | Open quarantine-related GitHub Issues |
| `id-token: write` | Optional OIDC for secure artifact signing |
| `actions: read` | Access GE/CI logs |

**Security Controls:**

- No secrets stored locally  
- All secrets from GitHub Encrypted Secrets  
- No STAC provider keys exposed in logs  
- ETag cache protected by `.gitignore` rules  

Secrets used:

```
STAC_API
NEO4J_URI
NEO4J_USER
NEO4J_PASS
```

---

## 🧪 Validation Enforcement

The orchestrator enforces:

- JSON Schema validation  
- Great Expectations suite  
- CARE governance checks  
- STAC extension compliance  
- Link correctness  
- Provenance metadata  
- Immutability rules

Failure triggers:

- Quarantine  
- GitHub Issue  
- Telemetry update  
- No publish allowed  

---

## 📦 Artifact Outputs (CI/CD)

Artifacts uploaded per run include:

```
stac-run-<run_id>/
├── incoming/                       # Raw API-returned STAC JSONL
├── published/                      # Validated STAC Items/Collections
└── datadocs/                       # WCAG-compliant GE HTML reports
```

Artifacts support:

- Debugging  
- Governance review  
- Auditor verification  
- Offline inspection

---

## 📡 Telemetry Outputs

Telemetry written to:

```
src/pipelines/stac/monitor-validate-publish/data/telemetry/<timestamp>.jsonl
../../../../../releases/v10.3.0/focus-telemetry.json
```

Metrics include:

- Polling counts  
- GE pass/fail  
- CARE errors  
- ETag usage  
- Publish latency  
- Energy consumption  
- CO₂e estimates  
- Governance outcomes  

Telemetry schema defined by:

```
../../../../../schemas/telemetry/pipelines-stac-github-v1.json
```

---

## 🧭 Governance Integration

All governance events created here must:

- Update versioning & quarantine ledgers  
- Trigger FAIR+CARE review workflows  
- Link telemetry → provenance → STAC lineage  
- Produce audit-ready artifacts  

Governance anchoring file:

```
../../../../../docs/standards/governance/ROOT-GOVERNANCE.md
```

---

## ✨ Local Workflow Simulation

To simulate orchestrator logic without CI:

```bash
python src/pipelines/stac/monitor-validate-publish/monitor.py
great_expectations checkpoint run stac_items \
  --config src/pipelines/stac/monitor-validate-publish/expectations/great_expectations.yml \
  --suite stac_item_suite
python src/pipelines/stac/monitor-validate-publish/publish.py
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Added full documentation for GitHub CI/CD integration, telemetry flow, governance hooks, and artifact lifecycle. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Orchestrator GitHub Integration**  
Continuous Validation × FAIR+CARE × Immutable Telemetry × Automated Governance  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Orchestrator Root](../README.md)

</div>
