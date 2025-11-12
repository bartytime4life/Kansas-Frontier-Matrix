---
title: "📊 Kansas Frontier Matrix — Reports & Validation Artifacts Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/README.md"
version: "v10.2.3"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-reports-v3.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Reports & Validation Artifacts Index**
`docs/reports/README.md`

**Purpose:**  
Central map for **all generated reports, validation outputs, security artifacts, governance audits, and telemetry logs** within the Kansas Frontier Matrix (KFM) monorepo.  
All artifacts indexed here are **automatically produced**, **cryptographically signed**, and **FAIR+CARE certified** under **MCP v6.3**.

![Badge Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![SLSA](https://img.shields.io/badge/Supply%20Chain-SLSA%201.0-7b1fa2)
![Status](https://img.shields.io/badge/Status-Automated-brightgreen)

</div>

---

## 📘 Overview

The `docs/reports/` subtree contains **machine-generated, versioned evidence** of system compliance, data validation, and governance performance.  
All outputs feed the **FAIR+CARE Council**, **Governance Ledger**, and **Focus Mode Telemetry Dashboard**.

- Produced via **GitHub Actions** CI pipelines.  
- Signed with **SHA-256 hashes** and **SLSA attestations**.  
- Fully reproducible and auditable per release tag.

---

## 🗂️ Directory Layout

```bash
docs/reports/
├── README.md                          # This index (you are here)
│
├── faircare_summary.json              # FAIR+CARE validation rollup
├── stac_validation.json               # STAC/DCAT compliance summary
│
├── telemetry/                         # Derived telemetry metrics
│   ├── build_metrics.json             # Build/runtime metrics
│   ├── governance_scorecard.json      # FAIR+CARE governance KPI
│   └── focus_telemetry_snapshot.json  # Merged dashboard snapshot
│
├── audit/                             # Governance & workflow ledgers
│   ├── github-workflows-ledger.json
│   ├── governance-ledger.json
│   ├── experiments-ledger.json
│   ├── ai_models.json
│   └── release-manifest-log.json
│
├── security/                          # Security & supply chain artifacts
│   ├── slsa_attestations.json
│   ├── sbom_summary.json
│   ├── prompt_defense_audit.json
│   └── secrets_rotation_report.json
│
└── self-validation/                   # Workflow-level outputs
    ├── stac/                          # STAC validation logs
    ├── fair/                          # FAIR+CARE validations
    ├── docs/                          # Docs & accessibility lint logs
    ├── security/                      # Dependency scans
    ├── experiments/                   # Experiment reproducibility
    └── sop/                           # SOP validation summaries
```

> Release-level mirrors exist under `releases/v10.2.0/`.

---

## 🧾 Report Categories

| Category | Description | Workflow |
|-----------|--------------|-----------|
| FAIR+CARE Validation | Dataset compliance audits | `faircare-validate.yml` |
| STAC/DCAT Validation | Metadata schema validation | `stac-validate.yml` |
| Telemetry & Metrics | System performance summaries | `telemetry-export.yml` |
| Governance Ledgers | Immutable council reviews | `governance-form.yml` |
| AI Model Reports | Model audit & bias summaries | `ai-train.yml` |
| Security Artifacts | SBOMs, SLSA attestations | `sbom-build.yml`, `site.yml` |
| CI/CD Ledgers | Workflow history & provenance | `audit.yml` |

---

## ⚙️ Workflow Integration Map

| Workflow | Artifact | Output Path |
|-----------|-----------|--------------|
| `stac-validate.yml` | STAC report | `reports/self-validation/stac/` |
| `faircare-validate.yml` | FAIR+CARE report | `reports/fair/` |
| `docs-lint.yml` | Accessibility & doc QA | `reports/self-validation/docs/` |
| `telemetry-export.yml` | Telemetry bundle | `releases/v10.2.0/focus-telemetry.json` |
| `ai-train.yml` | Model metrics & governance | `reports/audit/ai_models.json` |
| `site.yml` | Provenance attestations | `reports/security/slsa_attestations.json` |
| `sbom-build.yml` | SPDX/CycloneDX rollups | `reports/security/sbom_summary.json` |
| `prompt-attack-test.yml` | Prompt audit | `reports/security/prompt_defense_audit.json` |
| `secrets-validate.yml` | Secrets rotation report | `reports/security/secrets_rotation_report.json` |

---

## ⚖️ FAIR+CARE Alignment

| Principle | Implementation |
|------------|----------------|
| Findable | Versioned, indexed JSON with UUID & timestamps |
| Accessible | CC-BY 4.0 licensed, open metadata endpoints |
| Interoperable | STAC 1.0, DCAT 3.0, and JSON-LD compatibility |
| Reusable | Cryptographically signed, SLSA-verified |
| CARE | Council review and consent-based governance |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.2.3 | 2025-11-09 | KFM Docs Team | Aligned to v10.2 release; added security evidence and updated telemetry schema v3. |
| v9.7.0 | 2025-11-05 | A. Barta | Initial FAIR+CARE and telemetry integration with governance tables. |
| v9.5.0 | 2025-10-20 | A. Barta | Added scorecard KPIs and expanded audit ledgers. |
| v9.3.0 | 2025-08-12 | KFM Core Team | Introduced CI/CD ledger and telemetry ref. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established reports and validation framework. |

---

<div align="center">

© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3  
**FAIR+CARE Certified · SLSA Provenance · Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

[Back to Documentation Index](../README.md) · [Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
