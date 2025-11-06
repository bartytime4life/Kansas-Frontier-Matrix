---
title: "🧾 Kansas Frontier Matrix — Pull Request Template"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Pull Request Template**
`.github/PULL_REQUEST_TEMPLATE.md`

**Purpose:** Standardize contributions to ensure that every pull request includes documentation, FAIR+CARE metadata, validation results, and adherence to the Master Coder Protocol (MCP v6.3).

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-success)]()

</div>

---

## 🪶 Summary

> Provide a concise description of the change. Include what, why, and how it improves the project.

**Type of Change:**
- [ ] ✨ Feature / Enhancement  
- [ ] 🐛 Bug Fix  
- [ ] 🧠 AI / Model Update  
- [ ] 🗺 Data Layer Addition  
- [ ] 📚 Documentation Update  
- [ ] 🔧 Refactor / Maintenance  
- [ ] ⚙️ CI/CD or Workflow Update  

**Short Description:**  
<!-- Write 2–4 sentences summarizing your pull request -->

---

## 🧩 Related Issues / Links

> Reference related issues or documents that this PR addresses.

- Related Issue(s): Closes #`<issue_number>`  
- Associated Docs: `[docs/...path...]`  
- Dataset Manifest(s): `[data/sources/...json]`  

---

## 📂 Changes Introduced

> List key modifications made in this PR.

**Code or Data Added:**
- [ ] `src/` (ETL, AI, or API code changes)  
- [ ] `web/` (UI, React, or timeline updates)  
- [ ] `data/` (new or updated datasets)  
- [ ] `docs/` (documentation updates)  
- [ ] `.github/` (workflow or governance changes)  

**Description of Major Changes:**
```text
- Added NOAA drought dataset and STAC manifest
- Implemented AI focus transformer v2.0 summarization
- Updated FAIR+CARE validation reports
```

---

## 🧮 Validation Checklist

> Confirm that your changes meet the required quality, compliance, and reproducibility standards.

**Code & Data Validation:**
- [ ] 🧪 `make lint` passes locally  
- [ ] ✅ `make validate` passes (STAC/DCAT, FAIR+CARE)  
- [ ] 🧾 Unit tests (`make test`) all pass  
- [ ] 🧠 AI models documented via `docs/templates/model_card.md`  
- [ ] 🔐 No secrets or credentials included  
- [ ] 🧱 Updated SBOM (`releases/v9.7.0/sbom.spdx.json`) if new dependencies added  

**Documentation:**
- [ ] 📘 Added or updated `README.md` in modified directories  
- [ ] 🗺 Updated dataset manifests (`data/sources/`) with license and checksum  
- [ ] 🧩 Added references in `docs/architecture.md` or relevant module READMEs  

---

## ⚖️ FAIR+CARE & Governance Acknowledgment

All contributors must acknowledge and comply with KFM’s ethical and governance principles.

- [ ] I confirm that all contributed data complies with **FAIR+CARE** (Findable, Accessible, Interoperable, Reusable + Collective Benefit, Authority to Control, Responsibility, Ethics).  
- [ ] I confirm that my contribution does not contain proprietary, private, or unethical data.  
- [ ] I have reviewed and agree to the **Master Coder Protocol (MCP v6.3)** and **KFM Governance Charter**.  

---

## 🧠 Testing and Results

> Provide a summary of any local or pipeline tests performed.

| Test Type | Status | Notes |
|------------|---------|-------|
| ETL / Pipeline Run | ✅ Pass | `data/work/tmp/etl/logs/validation.json` updated |
| AI Model Training | ✅ Pass | F1=0.91 (focus_transformer_v1) |
| Frontend Build | ✅ Pass | Verified via `npm run build` |
| FAIR+CARE Validation | ✅ Pass | Ethics tag added to dataset manifest |
| Docs Validation | ✅ Pass | `docs-lint.yml` successful |

Attach relevant logs or screenshots if applicable.

---

## 🧾 Release / Deployment Notes

> Describe any implications for deployment or releases.

- [ ] Requires rebuild of Docker image  
- [ ] Requires reindexing of Neo4j graph database  
- [ ] Requires revalidation of STAC or FAIR+CARE datasets  
- [ ] Includes breaking changes (documented below)

**Breaking Changes (if any):**
```text
Describe any backward-incompatible changes or migrations.
```

---

## 🧭 Reviewer Checklist (for Maintainers Only)

| Check | Status | Comments |
|--------|---------|-----------|
| CI/CD All Workflows Passed | ☐ |  |
| FAIR+CARE Report Reviewed | ☐ |  |
| SBOM Updated | ☐ |  |
| Docs Alignment Verified | ☐ |  |
| Governance Ledger Entry Added | ☐ |  |

---

## 🕰️ Versioning & Provenance

**Semantic Version Update:**  
- [ ] Major (breaking)  
- [ ] Minor (new feature)  
- [ ] Patch (fix or update)  

**Affected Release:**  
`releases/v9.7.0/manifest.zip`  

**Checksum Validation:**  
All added files verified with SHA-256:
```bash
sha256sum <file>
```

---

<div align="center">

**Thank you for contributing to the Kansas Frontier Matrix!**  
Every pull request moves us closer to a fully FAIR+CARE-certified, reproducible open-science platform.

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

</div>
