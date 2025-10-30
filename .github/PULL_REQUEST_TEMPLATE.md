---
title: "🧩 Kansas Frontier Matrix — Pull Request Template (MCP-DL v6.4.3 · FAIR+CARE Diamond⁹ Ω Verified)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v9.5.0"
last_updated: "2025-10-30"
review_cycle: "Continuous Integration"
commit_sha: "<latest-commit-hash>"
---

<div align="center">

# 🧩 Kansas Frontier Matrix — **Pull Request Template**

**Purpose:** Standardized pull request structure ensuring **MCP-DL v6.4.3 Diamond⁹ Ω** compliance with FAIR+CARE, provenance, and reproducibility mandates.  
All contributors must complete this form to uphold KFM’s open governance, data integrity, and ethical AI principles.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../docs/architecture/repo-focus.md)
[![FAIR+CARE · Diamond⁹ Ω](https://img.shields.io/badge/FAIR%2BCARE-Diamond%E2%81%B9%E2%84%AA-gold)](../docs/standards/faircare-validation.md)
[![CI · site.yml](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)

</div>

---

## 🧾 Pull Request Overview

**PR Title:**  
> _Short, descriptive summary (e.g., “Integrate DCAT Export Workflow & Focus Mode Telemetry”)._

**Related Issue(s):**  
> _Link related issues using “Fixes #___” or “Refs #___”._

**Category:**  
- [ ] 🧱 Feature / Enhancement  
- [ ] 🐛 Bug Fix  
- [ ] 🧪 Research / Experimentation  
- [ ] 🧭 Documentation / Governance  
- [ ] 🔐 Security / Compliance  
- [ ] 🧬 AI / ML Model Update  

---

## 📦 Description

**Summary of Changes:**  
> _Describe what this PR introduces or modifies. Include rationale and affected components._

**Modified Paths:**  
> _List primary directories or files changed (e.g., `/data/work/`, `/src/pipelines/`, `/docs/standards/`)._

**Dependencies Added/Updated:**  
> _State any library, dataset, or tool updates._  
> _Example: “Upgraded PySTAC 1.9.0 for STAC–DCAT translation.”_

---

## 🧩 Validation & Governance Checklist

### ✅ Technical Validation
- [ ] All tests pass (`pytest`, `npm test`, etc.)
- [ ] No merge conflicts with target branch.
- [ ] ETL pipelines or AI workflows validated with sample data.
- [ ] Pre-commit hooks and linting passed.

### 🧠 FAIR+CARE Validation
- [ ] FAIR metadata updated (`data/stac/`, `data/meta/`, manifests).  
- [ ] CARE ethical checks completed (sensitive data, consent, visibility).  
- [ ] Provenance ledger entry created (`reports/audit/ai_hazards_ledger.json`).  
- [ ] Documentation updated for reproducibility (`README.md`, SOP, or docs).  
- [ ] Schema validation and STAC/DCAT compliance confirmed.  

---

## 🧭 Governance & Provenance

| Parameter | Reference / Path |
|------------|------------------|
| **Governance Ref** | `docs/standards/governance/ROOT-GOVERNANCE.md` |
| **Manifest Ref** | `releases/v9.5.0/manifest.zip` |
| **Telemetry Ref** | `releases/v9.5.0/focus-telemetry.json` |
| **Ontology Alignment** | `ontologies/CIDOC_CRM-KFM.owl` |
| **Data Contract** | `docs/contracts/data-contract-v3.json` |
| **SBOM Ref** | `releases/v9.5.0/sbom.spdx.json` |

> **Note:** Verify these paths are correct and referenced when introducing or modifying data, models, or workflows.

---

## 🧠 AI / ML Change Log (if applicable)

If this PR includes AI, ML, or NLP model updates:

- [ ] Model card(s) updated (`docs/ai/model_cards/`)  
- [ ] Training data audited for bias and consent  
- [ ] Explainability + drift reports generated (`data/work/tmp/hazards/logs/ai/`)  
- [ ] Focus Mode reasoning revalidated (`make focus-ai`)  
- [ ] Metrics logged to `focus-telemetry.json`  

**AI/ML Change Summary:**  
> _E.g., “Updated `focus-reasoner-v9` using 2025 NOAA drought dataset; improved F1 from 0.91 → 0.94.”_

---

## 🧮 Results Summary (Optional)

| Metric | Previous | New | Δ Change | Validation |
|---------|-----------|-----|-----------|-------------|
| Accuracy | 0.91 | 0.94 | +0.03 | ✅ |
| Model Drift Index | 0.05 | 0.02 | ↓ | ✅ |
| FAIR Coverage (%) | 95 | 100 | +5 | ✅ |
| Schema Errors | 2 | 0 | Fixed | ✅ |

---

## 📋 Reviewer Notes

> _Provide reviewer context or test steps. Example:_  
> ```
> make etl-all
> make validate-all
> make focus-ai
> ```  
> _Reviewers validate output at: `/data/work/tmp/hazards/logs/validation/`._

---

## 🔍 Reviewers

**Suggested Reviewers:**  
> _Tag reviewers or CODEOWNERS (e.g., `@kfm-etl-ops`, `@bartytime4life`)._

**Required Reviewers:**  
- [ ] @kfm-architecture (Governance & FAIR)  
- [ ] @kfm-etl-ops (ETL / Data Engineering)  
- [ ] @kfm-ai-lab (AI Systems)  
- [ ] @bartytime4life (Maintainer)

---

## 🧾 Submission Confirmation

Please confirm:
- [ ] I have followed **Master Coder Protocol (MCP-DL v6.4.3)** standards.  
- [ ] I have validated changes locally and through CI.  
- [ ] I have included FAIR+CARE metadata and governance references.  
- [ ] I agree this contribution complies with KFM’s open license (MIT / CC-BY 4.0).  
- [ ] I have updated relevant documentation and changelogs.  

---

<div align="center">

**Kansas Frontier Matrix** · *FAIR+CARE AI × Geospatial Reproducibility × Ethical Science*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [📖 Docs Portal](../docs/) • [⚖️ Governance Ledger](../docs/standards/governance/)

</div>
