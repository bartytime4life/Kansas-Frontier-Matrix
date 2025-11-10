---
title: "🧾 Kansas Frontier Matrix — Standard Operating Procedure (SOP) Template"
path: "docs/templates/sop.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-sop-template-v2.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Standard Operating Procedure (SOP) Template**  
`docs/templates/sop.md`

**Purpose:**  
Provide a structured, machine-verifiable template for documenting operational workflows within the Kansas Frontier Matrix (KFM).  
This ensures all processes are **transparent**, **auditable**, and **FAIR+CARE**-aligned under **Master Coder Protocol v6.3** and **ISO 19115**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../standards/faircare.md)
[![Status: Template](https://img.shields.io/badge/Status-Template-lightgrey)]()

</div>

---

## 🧭 Overview

This **SOP Template** standardizes the documentation of operational, governance, or technical procedures across KFM.  
Every SOP ensures consistent, ethical, and reproducible task execution — fulfilling the MCP directive: *“Document first, execute second.”*

Use this format for:
- ETL pipelines and data governance workflows  
- AI model retraining, explainability, and deployment  
- FAIR+CARE audits, ledger updates, and schema validation  
- Sustainability or provenance reporting routines  

All SOPs are validated via CI (`docs-lint.yml`, `faircare-validate.yml`) and version-logged in the governance ledger.

---

## 🧱 Metadata (YAML Front-Matter)

Each SOP must begin with this metadata block:

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
telemetry_schema: "schemas/telemetry/docs-sop-[vN].json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---
```

---

## 🎯 Purpose

Define **why** this SOP exists and its intended impact.

**Example**  
> Document the process for validating, packaging, and deploying verified FAIR+CARE STAC/DCAT metadata for archival release.

---

## 🧩 Scope

Specify **inclusions** and **exclusions** to clarify context.

| Included | Excluded |
|---|---|
| STAC/DCAT validation workflows | Raw JSON editing |
| FAIR+CARE audit automation | Manual council review |

---

## ⚙️ Prerequisites

List technical, procedural, or governance dependencies.

| Requirement | Description |
|---|---|
| **Environment** | Python 3.11+, Docker 24+, Git CLI |
| **Dependencies** | `pystac`, `jsonschema`, `requests`, `pytest` |
| **Credentials** | GitHub token, STAC dataset access keys |
| **Validation Scripts** | Located under `tools/validation/` or `src/pipelines/validation/` |

---

## 🪜 Procedure

Provide a numbered, reproducible set of instructions.

**Example**
1. **Pull latest repository version**  
   ```bash
   git pull origin main
   ```

2. **Run FAIR+CARE validator**  
   ```bash
   make validate-faircare
   ```

3. **Validate schema & STAC/DCAT metadata**  
   ```bash
   make validate-schema
   ```

4. **Commit validation reports**  
   ```bash
   git add reports/fair/ reports/self-validation/
   git commit -m "chore: validate metadata FAIR+CARE for release v10.0.0"
   git push origin main
   ```

5. **Trigger CI governance sync**  
   - Verify `governance_sync.yml` passed successfully.  
   - Telemetry metrics should log in `releases/v10.0.0/focus-telemetry.json`.

---

## 🧪 Validation & Quality Assurance

Document validation checks required for compliance.

| Validation Type | Expected Output | Workflow |
|---|---|---|
| Markdown / YAML Lint | No errors or warnings | `.github/workflows/docs-lint.yml` |
| FAIR+CARE Audit | `faircare_summary.json` created | `.github/workflows/faircare-validate.yml` |
| Telemetry Log | Entry created in `focus-telemetry.json` | `.github/workflows/telemetry-export.yml` |

---

## ⚖️ FAIR+CARE Governance Mapping

| Principle | Implementation |
|---|---|
| **Findable** | SOP stored under version control with semantic pathing. |
| **Accessible** | CC-BY 4.0 license; publicly readable Markdown. |
| **Interoperable** | Uses STAC/DCAT-compatible front-matter schema. |
| **Reusable** | Immutable ledger entry with checksum. |
| **CARE** | Reviewed for inclusivity, cultural ethics, and provenance sensitivity. |

Governance records appended to:
```
reports/audit/github-workflows-ledger.json
```

---

## 🔄 Change Management

Describe update procedure, review gates, and roles.

| Stage | Description | Responsible |
|---|---|---|
| Draft | Update SOP and open PR | Contributor |
| Review | Conduct FAIR+CARE and technical validation | Governance Council |
| Approval | Merge to `main` | Maintainer |
| Publish | Telemetry auto-updated | CI/CD Pipeline |

---

## 🧮 CI & Validation Integration

| Workflow | Description |
|---|---|
| `docs-lint.yml` | Validates metadata and Markdown structure. |
| `faircare-validate.yml` | Ethics and reproducibility compliance audit. |
| `telemetry-export.yml` | Logs sustainability and process metrics. |

All logs archived under:
```
reports/self-validation/sop/
```

---

## 🌱 Sustainability Metrics

| Metric | Value | Verified By |
|---|---:|---|
| Power Use | 1.3 Wh | @kfm-sustainability |
| Carbon Output | 1.5 gCO₂e | @kfm-security |
| Renewable Energy | 100% (RE100) | @kfm-infrastructure |
| FAIR+CARE Compliance | 100% | @faircare-council |

Telemetry file reference:  
`../../releases/v10.0.0/focus-telemetry.json`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | A. Barta | Upgraded to v10; enhanced telemetry schema, FAIR+CARE integration, and ISO 19115 compliance. |
| v9.7.0 | 2025-11-05 | A. Barta | Created SOP template with governance integration and CI mapping. |
| v9.5.0 | 2025-10-20 | A. Barta | Added telemetry reporting and automation references. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial SOP template creation. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · **Diamond⁹ Ω / Crown∞Ω** Ultimate Certified  
[Back to Template Index](README.md) · [Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>