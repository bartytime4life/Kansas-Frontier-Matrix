---
title: "🧾 Kansas Frontier Matrix — Pull Request Template (MCP v6.3 · FAIR+CARE Certified)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../releases/v9.7.0/manifest.zip"
telemetry_ref: "../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-pullrequest-v1.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Pull Request Template**
`.github/PULL_REQUEST_TEMPLATE.md`

**Purpose:** Provide a structured, reproducible pull request (PR) format to ensure that all code, data, and documentation changes follow **Master Coder Protocol (MCP v6.3)** and **FAIR+CARE** validation.  
Every submission is CI-verified, governance-reviewed, and telemetry-logged.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-success)]()

</div>

---

## 🪶 Summary

> Briefly describe the change (what, why, and how it improves the system).

**Type of Change:**
- [ ] ✨ Feature / Enhancement  
- [ ] 🐛 Bug Fix  
- [ ] 🧠 AI / Model Update  
- [ ] 🗺 Data Layer Addition  
- [ ] 📚 Documentation Update  
- [ ] 🔧 Refactor / Maintenance  
- [ ] ⚙️ CI/CD or Workflow Update  

**Description:**  
<!-- Write a concise summary (2–4 sentences) of what this PR does. -->

---

## 🧩 Related Issues / Links

> Reference connected issues, datasets, or docs.

- Closes #`<issue_number>`  
- Documentation: `[docs/...path...]`  
- Dataset Manifests: `[data/sources/...json]`  

---

## 📂 Changes Introduced

> Summarize what was added, modified, or removed.

**Affected Modules:**
- [ ] `src/` (ETL, AI, API)  
- [ ] `web/` (UI, React, Timeline)  
- [ ] `data/` (new/updated datasets)  
- [ ] `docs/` (documentation updates)  
- [ ] `.github/` (workflow, governance, or config)

**Major Changes:**
```text
- Added NOAA drought dataset and STAC manifest.
- Implemented AI Focus Transformer v2.0 summarization.
- Updated FAIR+CARE validation reports and telemetry schema.
```

---

## 🧮 Validation Checklist

> Confirm that the contribution passes all validations.

**Code & Data Validation:**
- [ ] 🧪 `make lint` — passes locally.  
- [ ] ✅ `make validate` — STAC/DCAT + FAIR+CARE checks pass.  
- [ ] 🧾 `make test` — unit/integration suites succeed.  
- [ ] 🧠 AI models documented via `docs/templates/model_card.md`.  
- [ ] 🔐 No secrets, credentials, or proprietary data included.  
- [ ] 🧱 SBOM updated (`releases/v9.7.0/sbom.spdx.json`) if dependencies added.  

**Documentation Validation:**
- [ ] 📘 Updated or created relevant `README.md`.  
- [ ] 🗺 Updated dataset manifests (`data/sources/`) with license & checksum.  
- [ ] 🧩 Linked updates to architecture or workflow READMEs.

---

## ⚖️ FAIR+CARE Governance Confirmation

Contributors must certify FAIR+CARE compliance.

- [ ] I confirm all contributions follow **FAIR** (Findable, Accessible, Interoperable, Reusable) and **CARE** (Collective Benefit, Authority, Responsibility, Ethics).  
- [ ] I confirm no private, proprietary, or unethical content is included.  
- [ ] I have reviewed and agree to the **Master Coder Protocol v6.3** and **KFM Governance Charter**.  

---

## 🧠 Testing & Results

> Summarize any local or pipeline testing performed.

| Test Type | Status | Notes |
|------------|--------|-------|
| ETL / Pipeline | ✅ | Logs: `data/work/tmp/etl/logs/validation.json` |
| AI Model | ✅ | F1=0.91 (focus_transformer_v1) |
| Frontend Build | ✅ | Verified via `npm run build` |
| FAIR+CARE Validation | ✅ | Ethics annotations verified |
| Docs Lint | ✅ | `docs-lint.yml` passed |

Attach relevant logs or screenshots below, if applicable.

---

## 🧾 Release / Deployment Notes

> Indicate any deployment implications or follow-up tasks.

- [ ] Requires Docker rebuild.  
- [ ] Requires Neo4j reindexing.  
- [ ] Requires STAC/DCAT revalidation.  
- [ ] Contains breaking changes (documented below).

**Breaking Changes (if applicable):**
```text
Describe backward-incompatible updates or data migrations.
```

---

## 🧭 Reviewer Checklist (Maintainers Only)

| Check | Status | Comments |
|--------|--------|-----------|
| All CI/CD Workflows Passed | ☐ |  |
| FAIR+CARE Review Completed | ☐ |  |
| SBOM Updated / Verified | ☐ |  |
| Docs Conform to Markdown Rules | ☐ |  |
| Governance Ledger Entry Added | ☐ |  |

---

## 🕰️ Versioning & Provenance

**Semantic Version Increment:**  
- [ ] Major (breaking)  
- [ ] Minor (new feature)  
- [ ] Patch (fix or update)  

**Affected Release:**  
`releases/v9.7.0/manifest.zip`  

**Checksum Verification:**  
Validate file integrity before merge:
```bash
sha256sum <file>
```

---

<div align="center">

**Thank you for contributing to the Kansas Frontier Matrix!**  
Every pull request advances open, ethical, and reproducible science.

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to GitHub Overview](README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
