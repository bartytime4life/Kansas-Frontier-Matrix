---
title: "🧾 Kansas Frontier Matrix — Standard Operating Procedure (SOP) Template"
path: "docs/templates/sop.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-sop-template-v1.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Standard Operating Procedure (SOP) Template**
`docs/templates/sop.md`

**Purpose:** Define a structured, reproducible format for operational procedures within the Kansas Frontier Matrix (KFM).  
All SOPs are written to ensure **consistency**, **reproducibility**, and **FAIR+CARE** alignment under the **Master Coder Protocol (MCP v6.3)**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../standards/faircare.md)
[![Status: Template](https://img.shields.io/badge/Status-Template-lightgrey)]()

</div>

---

## 🧭 Overview

This **SOP Template** standardizes how KFM operational workflows, maintenance tasks, and governance procedures are documented.  
Each SOP ensures that every process in KFM is **transparent**, **verifiable**, and **repeatable** — fulfilling the MCP principle: *“Documentation before execution.”*

Use this template for:
- ETL pipeline operations  
- AI/ML model retraining and deployment  
- FAIR+CARE validation workflows  
- Repository or governance maintenance procedures  

All SOPs are validated in CI pipelines (`docs-lint.yml`, `faircare-validate.yml`) and logged in the governance ledger.

---

## 🧱 Metadata (YAML Front-Matter)

Each SOP must begin with a YAML metadata block:

```yaml
---
title: "🧾 [SOP Title]"
path: "docs/sop/[filename].md"
version: "vX.Y.Z"
last_updated: "YYYY-MM-DD"
review_cycle: "Annual / Autonomous"
commit_sha: "<commit-hash>"
sbom_ref: "releases/vX.Y.Z/sbom.spdx.json"
manifest_ref: "releases/vX.Y.Z/manifest.zip"
telemetry_ref: "releases/vX.Y.Z/focus-telemetry.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
---
```

---

## 🎯 Purpose

Explain **why** this SOP exists and what it is intended to accomplish.

**Example:**
> This SOP defines the procedure for validating and deploying updated FAIR+CARE-compliant STAC catalog metadata under `data/stac/`.

---

## 🧩 Scope

Define the boundaries of this procedure — where it applies and any known exclusions.

| Included | Excluded |
|-----------|-----------|
| STAC catalog validation | Non-STAC JSON schema validations |
| FAIR+CARE compliance audit | Manual ethics review processes |

---

## ⚙️ Prerequisites

List software, environment configurations, credentials, and datasets needed before executing this SOP.

| Requirement | Description |
|--------------|-------------|
| Python Environment | Python 3.11+ with `pystac`, `jsonschema`, `requests` |
| Repository Access | Contributor permissions with branch protection enabled |
| Environment Variables | `GITHUB_TOKEN`, `STAC_PATH` |
| Validation Scripts | `tools/validate_data.py`, `src/pipelines/validation/` |

---

## 🪜 Procedure

Provide a step-by-step guide to complete the task.  
Use clear, numbered instructions and include code snippets or shell commands.

**Example:**
1. **Pull latest changes**  
   ```bash
   git pull origin main
   ```

2. **Run FAIR+CARE validation**  
   ```bash
   make validate-faircare
   ```

3. **Run STAC validation**  
   ```bash
   make validate-stac
   ```

4. **Review reports**  
   Reports will appear under `reports/fair/` and `reports/self-validation/stac/`.

5. **Commit and push results**  
   ```bash
   git add reports/
   git commit -m "chore: validated FAIR+CARE compliance for release v9.7.0"
   git push origin main
   ```

---

## 🧪 Validation & Quality Control

Document validation steps and QA criteria to confirm successful execution.

| Validation Type | Expected Output | Reference |
|------------------|----------------|------------|
| Markdown Linting | No errors in CI logs | `.github/workflows/docs-lint.yml` |
| FAIR+CARE Validation | `faircare_summary.json` generated | `.github/workflows/faircare-validate.yml` |
| Telemetry Logging | Entry in `focus-telemetry.json` | `releases/v9.7.0/focus-telemetry.json` |

---

## ⚖️ FAIR+CARE Governance Compliance

| Principle | Application |
|------------|--------------|
| **Findable** | SOP stored in GitHub with searchable metadata. |
| **Accessible** | Document licensed under CC-BY 4.0. |
| **Interoperable** | References standard YAML front-matter schema. |
| **Reusable** | Version-controlled and referenced in governance ledger. |
| **CARE** | Reviewed and approved by governance team for cultural sensitivity. |

Attach governance record:
```
reports/audit/github-workflows-ledger.json
```

---

## 🧾 Change Management

Explain how updates to this SOP will be proposed, reviewed, and approved.

| Step | Description | Responsible Party |
|------|--------------|------------------|
| Draft Update | Contributor modifies SOP and opens PR | Author / Maintainer |
| Review | FAIR+CARE Council or Governance Team | Council Members |
| Approval | Merge PR upon review completion | Project Maintainer |
| Publication | Update appears in `main` branch and telemetry logs | CI/CD Pipeline |

---

## 🧮 Validation & CI Integration

This SOP is automatically verified in CI/CD workflows:

| Workflow | Purpose |
|-----------|----------|
| `docs-lint.yml` | Ensures YAML header and Markdown consistency. |
| `faircare-validate.yml` | Confirms ethical and reproducibility compliance. |
| `telemetry-export.yml` | Logs metadata for traceability. |

Logs stored under:
```
reports/self-validation/sop/
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Created SOP template with governance integration and validation mapping. |
| v9.5.0 | 2025-10-20 | A. Barta | Added CI/CD and telemetry tracking sections. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial SOP structure established. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Template Index](README.md) · [Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
