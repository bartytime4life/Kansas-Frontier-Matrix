---
title: "🧾 Kansas Frontier Matrix — Pull Request Template (MCP v6.3 · FAIR+CARE Certified)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../releases/v10.0.0/manifest.zip"
telemetry_ref: "../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-pullrequest-v1.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Pull Request Template**
`.github/PULL_REQUEST_TEMPLATE.md`

**Purpose:**  
Ensure every contribution to KFM — code, data, models, or documentation — follows **Master Coder Protocol (MCP-DL v6.3)**, **FAIR+CARE** governance, and automated validation.  
All pull requests are **telemetry-logged**, **governance-reviewed**, and **provenance-attested**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-success)]()

</div>

---

## 🪶 Summary

> Provide a concise overview of what this PR changes and why it matters.

**Type of Change:**
- [ ] ✨ Feature / Enhancement  
- [ ] 🐛 Bug Fix  
- [ ] 🧠 AI / Model Update  
- [ ] 🗺 Data Layer Addition  
- [ ] 📚 Documentation Update  
- [ ] 🔧 Refactor / Maintenance  
- [ ] ⚙️ CI/CD or Workflow Update  

**Description:**  
<!-- Write a concise summary (2–4 sentences) of what this PR implements and how it improves the system. -->

---

## 🧩 Related Issues / Links
> Reference relevant issues, datasets, or documentation.

- Closes #`<issue_number>`  
- Documentation: `[docs/...path...]`  
- Dataset Manifests: `[data/sources/...json]`  
- STAC/DCAT Item: `[data/stac/...item.json]`  

---

## 📂 Changes Introduced
> Summarize what files or components were modified, added, or removed.

**Affected Modules:**
- [ ] `src/` — backend ETL, AI, or API changes  
- [ ] `web/` — frontend (React, Timeline, MapLibre) updates  
- [ ] `data/` — dataset or metadata additions  
- [ ] `docs/` — documentation or standards edits  
- [ ] `.github/` — automation or workflow updates  

**Major Changes:**
```text
- Added NOAA drought dataset with updated FAIR+CARE metadata.
- Integrated Focus Transformer v2.1 into AI pipeline.
- Enhanced telemetry schema for ISO 50001 energy tracking.
```

---

## 🧮 Validation Checklist
> Verify all tests and validations pass before requesting review.

**Code & Data Validation:**
- [ ] 🧪 `make lint` — code formatting and schema validation pass.  
- [ ] ✅ `make validate` — STAC/DCAT & FAIR+CARE audits pass.  
- [ ] 🧾 `make test` — all unit/integration tests succeed.  
- [ ] 🧠 AI model updated with model card (`docs/templates/model_card.md`).  
- [ ] 🔐 No secrets, credentials, or sensitive data included.  
- [ ] 🧱 SBOM (`releases/v10.0.0/sbom.spdx.json`) updated if dependencies changed.  

**Documentation Validation:**
- [ ] 📘 Updated/created relevant `README.md` or `ARCHITECTURE.md`.  
- [ ] 🗺 Added/updated dataset manifests with license, checksum, and provenance.  
- [ ] 🧩 Linked changes to architecture or workflow READMEs.  

---

## ⚖️ FAIR+CARE Governance Confirmation
All contributors must confirm ethical and reproducible standards:

- [ ] I confirm adherence to **FAIR** (Findable, Accessible, Interoperable, Reusable).  
- [ ] I confirm adherence to **CARE** (Collective Benefit, Authority, Responsibility, Ethics).  
- [ ] I confirm no private, unethical, or sensitive content is included.  
- [ ] I have reviewed the **Master Coder Protocol v6.3** and the **KFM Governance Charter**.  

---

## 🧠 Testing & Results
> Provide results from local or CI testing (include logs if possible).

| Test Type | Status | Notes |
|------------|--------|-------|
| ETL / Pipeline | ✅ | Verified via `data/work/tmp/etl/logs/validation.json` |
| AI Model | ✅ | F1 = 0.93 (Focus Transformer v2.1) |
| Frontend Build | ✅ | Verified via `npm run build` |
| FAIR+CARE Validation | ✅ | Ethical annotations and provenance verified |
| Docs Lint | ✅ | Passed all Markdown compliance rules |

Attach relevant screenshots or JSON log snippets below if helpful.

---

## 🧾 Release / Deployment Notes
> Note if this PR affects production or deployment environments.

- [ ] Requires Docker rebuild  
- [ ] Requires Neo4j reindexing  
- [ ] Requires STAC/DCAT revalidation  
- [ ] Introduces breaking changes  

**Breaking Changes (if applicable):**
```text
List any backward-incompatible schema, API, or pipeline updates.
```

---

## 🧭 Reviewer Checklist (Maintainers Only)

| Check | Status | Notes |
|--------|--------|-------|
| All CI/CD Workflows Passed | ☐ |  |
| FAIR+CARE Governance Review | ☐ |  |
| SBOM Updated & Verified | ☐ |  |
| Docs Conform to Markdown Rules | ☐ |  |
| Ledger Entry Added (Governance / Release) | ☐ |  |

---

## 🕰️ Versioning & Provenance

**Semantic Version Increment:**  
- [ ] Major (breaking)  
- [ ] Minor (feature)  
- [ ] Patch (fix/update)  

**Affected Release:**  
`releases/v10.0.0/manifest.zip`

**Checksum Verification:**  
Validate artifact integrity before merge:
```bash
sha256sum <file>
```

**Telemetry Binding:**  
Ensure the workflow updates `releases/v10.0.0/focus-telemetry.json` automatically.

---

<div align="center">

**Thank you for contributing to the Kansas Frontier Matrix!**  
Each pull request strengthens open, ethical, and reproducible science.

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to GitHub Overview](README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>