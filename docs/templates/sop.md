---
title: "🧾 Kansas Frontier Matrix — Standard Operating Procedure (SOP) Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/sop.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../releases/v10.2.0/focus-telemetry.json"
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
Every SOP created from this template ensures consistent, ethical, and reproducible task execution — fulfilling the MCP directive: *“Document first, execute second.”*

Use this format for:

- ETL pipelines and data governance workflows  
- AI model retraining, explainability, and deployment  
- FAIR+CARE audits, ledger updates, and schema validation  
- Sustainability, telemetry, or provenance reporting routines  

All SOPs are validated via CI (`docs-lint.yml`, `faircare-validate.yml`, `telemetry-export.yml`) and version-logged in the governance ledger.

---

## 🧱 Metadata (YAML Front-Matter — Required)

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
telemetry_schema: "schemas/telemetry/docs-sop-template-v2.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---
```

> CI will **fail** if required keys are missing or malformed.

---

## 🎯 Purpose

Define **why** this SOP exists and the impact it aims to have.

**Example**  
> Document the steps for validating, packaging, and deploying FAIR+CARE-certified STAC/DCAT metadata for each quarterly archive.

---

## 🧩 Scope

Specify **inclusions** and **exclusions** to clarify context and boundaries.

| Included | Excluded |
|---|---|
| STAC/DCAT validation workflows | Manual editing of STAC JSON |
| FAIR+CARE audit automation | Final Council decision text |

---

## ⚙️ Prerequisites

List technical, procedural, or governance dependencies required before execution.

| Requirement | Description |
|---|---|
| **Environment** | Python 3.11+, Docker 24+, Git CLI |
| **Dependencies** | `pystac`, `jsonschema`, `requests`, `pytest`, `kfm-stac-tools` |
| **Credentials** | GitHub token (read), STAC asset access keys (if private) |
| **Validation Scripts** | Located under `tools/validation/` or `src/pipelines/validation/` |

---

## 🪜 Procedure

Provide a numbered, reproducible set of instructions. Each step **must** be deterministic and testable.

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
   git commit -m "chore: FAIR+CARE + schema validation for vX.Y.Z"
   git push origin main
   ```

5. **Trigger CI governance sync**  
   - Confirm `governance_sync.yml` passes.  
   - Ensure `focus-telemetry.json` updated for current release.

---

## 🧪 Validation & Quality Assurance

Detail the validation checks required for SOP compliance.

| Validation Type | Expected Output | Workflow |
|---|---|---|
| Markdown / YAML Lint | No critical errors | `.github/workflows/docs-lint.yml` |
| FAIR+CARE Audit | Updated `faircare_summary.json` | `.github/workflows/faircare-validate.yml` |
| Telemetry Log | Appended entry in `focus-telemetry.json` | `.github/workflows/telemetry-export.yml` |

---

## ⚖️ FAIR+CARE Governance Mapping

Explain how this SOP meets FAIR+CARE principles.

| Principle | Implementation |
|---|---|
| **Findable** | SOP stored in `docs/sop/` with stable path and versioned metadata. |
| **Accessible** | CC-BY 4.0 public Markdown, rendered in repository. |
| **Interoperable** | References STAC/DCAT and ISO 19115-compliant metadata and contracts. |
| **Reusable** | Immutable ledger entries and checksum manifests. |
| **CARE** | Reviewed for inclusivity, cultural considerations, and data sensitivity. |

Governance records appended to:
```
reports/audit/github-workflows-ledger.json
```

---

## 🔄 Change Management

Describe how this SOP is updated, reviewed, and approved.

| Stage | Description | Responsible |
|---|---|---|
| Draft | Propose changes; open PR | Contributor |
| Review | FAIR+CARE + technical validation | Governance Council & Maintainers |
| Approval | Merge to `main` | Repository Maintainer |
| Publish | CI runs; telemetry updated | CI/CD Pipelines |

---

## 🧮 CI & Validation Integration

| Workflow | Description |
|---|---|
| `docs-lint.yml` | Validates SOP front-matter and structure. |
| `faircare-validate.yml` | Audits SOP for ethics and governance consistency. |
| `telemetry-export.yml` | Logs SOP updates for sustainability reporting. |

Logs for SOP validation are archived under:

```
reports/self-validation/sop/
```

---

## 🌱 Sustainability Metrics

| Metric | Value | Verified By |
|---|---:|---|
| SOP Validation Energy | 1.3 Wh | `@kfm-sustainability` |
| Carbon Output | 1.5 gCO₂e | `@kfm-security` |
| Renewable Energy | 100% (RE100) | `@kfm-infrastructure` |
| FAIR+CARE Compliance | 100% | `@faircare-council` |

Telemetry reference:  
`../../releases/v10.2.0/focus-telemetry.json`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.2.2 | 2025-11-12 | A. Barta | Aligned telemetry refs to v10.2.0; clarified governance, CI, and sustainability linkages. |
| v10.0.0 | 2025-11-10 | A. Barta | Upgraded to v10; enhanced telemetry schema; FAIR+CARE integration and ISO 19115 compliance. |
| v9.7.0 | 2025-11-05 | A. Barta | Created SOP template with governance integration and CI mapping. |
| v9.5.0 | 2025-10-20 | A. Barta | Added telemetry reporting and automation references. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial SOP template creation. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · **Diamond⁹ Ω / Crown∞Ω** Ultimate Certified  
[Back to Template Index](README.md) · [Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>