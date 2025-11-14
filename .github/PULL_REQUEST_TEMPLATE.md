---
title: "🧾 Kansas Frontier Matrix — Pull Request Template (MCP v6.3 · FAIR+CARE Certified)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.3.1/sbom.spdx.json"
manifest_ref: "../releases/v10.3.1/manifest.zip"
telemetry_ref: "../releases/v10.3.1/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-pullrequest-v2.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Pull Request Template**  
`.github/PULL_REQUEST_TEMPLATE.md`

**Purpose:**  
Ensure every contribution — code, data, models, Story Nodes, pipelines, workflows, or documentation — adheres to **Master Coder Protocol (MCP-DL v6.3)**, **FAIR+CARE** ethics, and **Diamond⁹ Ω / Crown∞Ω** governance.  
All PRs are automatically **validated**, **telemetry-logged**, **governance-audited**, and **provenance-attested**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)  
[![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-success)]()

</div>

---

## 🪶 Summary

> Provide a clear explanation of the purpose and context of this pull request.

**Type of Change:**
- [ ] ✨ Feature / Enhancement  
- [ ] 🐛 Bug Fix  
- [ ] 🧠 AI / Model Update  
- [ ] 🗺️ Data Layer Addition  
- [ ] 📚 Documentation Update  
- [ ] 🔧 Refactor / Maintenance  
- [ ] ⚙️ CI/CD or Workflow Update  

**Description:**  
<!-- (2–4 concise sentences explaining scope, motivation, and intent) -->

---

## 🧩 Related Issues / Links

- Closes #`<issue_number>`  
- Related Docs: `[docs/...path...]`  
- Dataset Manifest: `[data/sources/...json]`  
- STAC/DCAT Item: `[data/stac/...item.json]`  

---

## 📂 Changes Introduced

**Affected Modules:**
- [ ] `src/` — backend ETL, AI, API  
- [ ] `web/` — React, Timeline, MapLibre, Cesium  
- [ ] `data/` — datasets, manifests, schemas  
- [ ] `docs/` — documentation, governance, architecture  
- [ ] `.github/` — workflows, automation, security

**Major Changes:**
```text
- Introduced predictive ETL for NOAA drought datasets.
- Integrated Focus Transformer v2.4 narrative pipeline.
- Updated telemetry schema for ISO 50001 energy reporting.
```

---

## 🧮 Validation Checklist

### Code & Data
- [ ] 🧪 `make lint` — formatting + schema checks  
- [ ] 🏷️ `make validate` — STAC/DCAT + FAIR+CARE audits  
- [ ] 🧾 `make test` — all tests pass  
- [ ] 🧠 AI model updates include model card (`docs/models/...md`)  
- [ ] 🔐 No secrets or sensitive content  
- [ ] 🧱 SBOM updated (`releases/v10.3.1/sbom.spdx.json`)  

### Documentation
- [ ] 📘 Updated/created all required READMEs  
- [ ] 🗺️ Dataset manifests include license, checksum, provenance  
- [ ] 🧩 Architecture diagrams & workflow references updated  

---

## ⚖️ FAIR+CARE Governance Confirmation

- [ ] I confirm compliance with **FAIR** principles.  
- [ ] I confirm compliance with **CARE** principles.  
- [ ] I verify no private, sensitive, or unethical content is included.  
- [ ] I reviewed **MCP-DL v6.3** and the **Governance Charter**.  

---

## 🧠 Testing & Results

| Test Type | Status | Notes |
|-----------|--------|-------|
| ETL / Pipeline | ✅ | See: `data/work/tmp/etl/logs/validation.json` |
| AI Model | ✅ | F1 = 0.95 (Focus Transformer v2.4) |
| Frontend Build | ✅ | Verified via `npm run build` |
| FAIR+CARE Validation | ✅ | All restrictions + labels verified |
| Docs Lint | ✅ | Markdown + YAML valid |

> Attach logs or screenshots if helpful.

---

## 🧾 Release / Deployment Notes

- [ ] Requires Docker rebuild  
- [ ] Requires Neo4j reindex  
- [ ] Requires STAC/DCAT catalog rebuild  
- [ ] Introduces breaking changes  

**Breaking Changes:**
```text
List migrations or API/schema modifications here.
```

---

## 🧭 Reviewer Checklist (Maintainers Only)

| Check | Status | Notes |
|--------|--------|-------|
| CI/CD Workflows Passed | ☐ |  |
| FAIR+CARE Governance Review | ☐ |  |
| SBOM Verified / Updated | ☐ |  |
| Docs Follow Markdown Rules | ☐ |  |
| Governance Ledger Updated | ☐ |  |

---

## 🕰️ Versioning & Provenance

**Version Increment:**
- [ ] Major  
- [ ] Minor  
- [ ] Patch  

**Target Release:**  
`releases/v10.3.1/manifest.zip`

**Checksum Verification:**
```bash
sha256sum <artifact>
```

**Telemetry Linkage:**  
All updates must appear in:  
`releases/v10.3.1/focus-telemetry.json`

---

<div align="center">

**Thank you for contributing to the Kansas Frontier Matrix!**  
Every PR strengthens open, ethical, and reproducible geospatial science.

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to GitHub Overview](README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
