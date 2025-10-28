---
title: "🧩 Kansas Frontier Matrix — Pull Request Template (MCP-DL v6.3 · FAIR+CARE Verified)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Continuous Integration"
commit_sha: "<latest-commit-hash>"
---

<div align="center">

# 🧩 Kansas Frontier Matrix — **Pull Request Template**

**Purpose:** Standardized pull request format enforcing Master Coder Protocol (MCP-DL v6.3) and FAIR+CARE compliance across all contributions.  
All contributors must complete the required sections to ensure reproducibility, provenance, and ethical governance in the Kansas Frontier Matrix (KFM) repository.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../docs/architecture/repo-focus.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Verified-gold)](../docs/standards/faircare-validation.md)
[![CI Status](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)

</div>

---

## 🧾 Pull Request Overview

**PR Title:**  
> _Concise summary of your change (e.g., “Add NOAA Hydrology ETL Integration to Hazards Workspace”)._

**Related Issue(s):**  
> _Link any related issue(s) using “Fixes #___” or “Refs #___”._

**Category:**  
- [ ] 🧱 Feature / Enhancement  
- [ ] 🐛 Bug Fix  
- [ ] 🧪 Experiment / Research  
- [ ] 🧭 Documentation / Governance  
- [ ] 🔐 Security / Compliance  

---

## 📦 Description

**Summary of Changes:**  
> _Describe what this PR introduces or modifies. Be explicit about directories, modules, or datasets affected._

**Modified Paths:**  
> _List key directories or files changed (e.g., `/data/work/tmp/hazards/etl/`, `/src/pipelines/ai/`, `/docs/standards/`)._

**Dependencies Added or Updated:**  
> _Include any new libraries, tools, or datasets integrated._  
> _Example: “Added spaCy 3.8.0 for NER enhancements.”_

---

## 🧩 Validation & Governance Checklist

### ✅ Technical Validation
- [ ] Code runs locally without errors.
- [ ] All tests pass (`pytest` or equivalent).
- [ ] No merge conflicts with the target branch.
- [ ] ETL pipelines or AI workflows validated with sample data.

### 🧠 FAIR+CARE Validation
- [ ] FAIR metadata updated (`data/stac/`, `manifest.json`, etc.).
- [ ] CARE principles reviewed (data sensitivity, ethical provenance).
- [ ] Governance ledger entry created or updated (`reports/audit/`).
- [ ] Documentation updated for reproducibility (`README.md` or SOP).  

---

## 🧭 Governance & Provenance

| Parameter | Reference / Path |
|------------|------------------|
| **Governance Ref** | `docs/standards/governance/ROOT-GOVERNANCE.md` |
| **Manifest Ref** | `releases/v9.3.2/manifest.zip` |
| **Telemetry Ref** | `releases/v9.3.2/focus-telemetry.json` |
| **Ontology Alignment** | `ontologies/CIDOC_CRM-KFM.owl` |
| **Data Contract** | `docs/contracts/data-contract-v3.json` |

> **Note:** Ensure the above references are correctly linked or updated if new datasets or schemas are introduced.

---

## 🧠 AI/ML Change Log (if applicable)

If this PR includes updates to AI or NLP pipelines:
- [ ] Model cards updated (`docs/ai/model_cards/`).
- [ ] Training datasets validated for ethics and bias.
- [ ] Explainability and drift logs generated (`data/work/tmp/hazards/logs/ai/`).
- [ ] Focus Mode behavior tested and logged.

**Describe AI/ML Change:**  
> _E.g., “Updated `hazard-flood-v14` model with 2024–2025 FEMA flood data; improved AUC from 0.88 → 0.92.”_

---

## 🧮 Results Summary (Optional)

| Metric | Previous | New | Δ Change | Validation |
|---------|-----------|-----|-----------|-------------|
| F1 Score | 0.89 | 0.92 | +0.03 | ✅ |
| Model Drift Index | 0.07 | 0.03 | ↓ | ✅ |
| FAIR Coverage (%) | 92 | 100 | +8 | ✅ |
| Schema Errors | 3 | 0 | Fixed | ✅ |

---

## 📋 Reviewer Notes

> _Provide any notes for reviewers, including steps for local replication or testing. Example:_
> ```
> make hazards-etl
> make validate-hazards
> make focus-mode
> ```
> _Reviewer should confirm outputs at: `/data/work/tmp/hazards/logs/validation/`_

---

## 🔍 Reviewers

**Requesting Review From:**  
> _Tag specific reviewers or CODEOWNERS (e.g., `@kfm-etl-ops`, `@bartytime4life`)._

**Required Reviewers:**  
- [ ] @kfm-architecture (Governance)
- [ ] @kfm-etl-ops (Data Engineering)
- [ ] @kfm-ai-lab (AI Systems)
- [ ] @bartytime4life (Repository Maintainer)

---

## 🧾 Submission Confirmation

Please confirm:
- [ ] I have followed the **Master Coder Protocol (MCP-DL v6.3)**.
- [ ] I have validated my changes locally.
- [ ] I have included FAIR metadata and governance references.
- [ ] I agree that this contribution complies with the project’s open-source license.

---

<div align="center">

**Kansas Frontier Matrix** · *FAIR+CARE AI × Geospatial Reproducibility × Ethical Science*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../docs/) • [⚖️ Governance Ledger](../docs/standards/governance/)

</div>