---
title: "🧾 Kansas Frontier Matrix — Pull Request Template (MCP v6.3 · FAIR+CARE Certified)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../releases/v10.2.0/manifest.zip"
telemetry_ref: "../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-pullrequest-v2.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Pull Request Template**  
`.github/PULL_REQUEST_TEMPLATE.md`

**Purpose:**  
Ensure all contributions — code, data, models, and documentation — follow **Master Coder Protocol (MCP-DL v6.3)**, **FAIR+CARE** governance, and automated reproducibility validation.  
Every pull request is **telemetry-logged**, **governance-reviewed**, and **provenance-attested** through CI/CD pipelines.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-success)]()

</div>

---

## 🪶 Summary

> Provide a concise overview of the purpose of this pull request and its relevance to the Kansas Frontier Matrix system.

**Type of Change:**
- [ ] ✨ Feature / Enhancement  
- [ ] 🐛 Bug Fix  
- [ ] 🧠 AI / Model Update  
- [ ] 🗺️ Data Layer Addition  
- [ ] 📚 Documentation Update  
- [ ] 🔧 Refactor / Maintenance  
- [ ] ⚙️ CI/CD or Workflow Update  

**Description:**  
<!-- Write a concise (2–4 sentence) explanation of what this PR implements, including context and motivation. -->

---

## 🧩 Related Issues / Links
> Reference associated issues, datasets, or documentation changes.

- Closes #`<issue_number>`  
- Related Docs: `[docs/...path...]`  
- Dataset Manifest: `[data/sources/...json]`  
- STAC/DCAT Item: `[data/stac/...item.json]`  

---

## 📂 Changes Introduced
> Summarize the affected modules, new features, or files modified.

**Affected Modules:**
- [ ] `src/` — backend ETL, AI, or API updates  
- [ ] `web/` — frontend React / Timeline / MapLibre updates  
- [ ] `data/` — dataset, metadata, or schema additions  
- [ ] `docs/` — documentation or governance updates  
- [ ] `.github/` — CI/CD, workflow, or security modifications  

**Major Changes:**
```text
- Introduced predictive ETL for NOAA drought datasets.
- Integrated Focus Transformer v2.1 AI summaries.
- Upgraded telemetry schema for ISO 50001 energy metrics.
```

---

## 🧮 Validation Checklist

**Code & Data Validation:**
- [ ] 🧪 `make lint` — passes all formatting and schema checks  
- [ ] ✅ `make validate` — STAC/DCAT + FAIR+CARE audits successful  
- [ ] 🧾 `make test` — all unit/integration tests pass  
- [ ] 🧠 AI model updates include model card (`docs/templates/model_card.md`)  
- [ ] 🔐 No secrets, keys, or sensitive content included  
- [ ] 🧱 SBOM (`releases/v10.2.0/sbom.spdx.json`) updated if dependencies changed  

**Documentation Validation:**
- [ ] 📘 Updated or created `README.md` / `ARCHITECTURE.md` as required  
- [ ] 🗺️ Dataset manifests include license, checksum, and provenance fields  
- [ ] 🧩 Architecture or workflow references updated accordingly  

---

## ⚖️ FAIR+CARE Governance Confirmation

All contributors must certify ethical compliance:

- [ ] I confirm compliance with **FAIR** (Findable, Accessible, Interoperable, Reusable).  
- [ ] I confirm compliance with **CARE** (Collective Benefit, Authority to Control, Responsibility, Ethics).  
- [ ] I verify that no private, unethical, or sensitive material is included.  
- [ ] I have reviewed the **Master Coder Protocol v6.3** and **Governance Charter**.  

---

## 🧠 Testing & Results

> Provide results from local tests or CI/CD pipelines. Include key metrics, logs, or validation outputs.

| Test Type | Status | Notes |
|-----------|--------|-------|
| ETL / Pipeline | ✅ | Verified via `data/work/tmp/etl/logs/validation.json` |
| AI Model | ✅ | F1 = 0.94 (Focus Transformer v2.1 validation) |
| Frontend Build | ✅ | Verified via `npm run build` |
| FAIR+CARE Validation | ✅ | Ethical compliance confirmed |
| Docs Lint | ✅ | Passed Markdown and YAML schema validation |

Attach logs or screenshots if relevant.

---

## 🧾 Release / Deployment Notes

> Specify deployment considerations for this PR.

- [ ] Requires Docker rebuild  
- [ ] Requires Neo4j reindex  
- [ ] Requires STAC/DCAT revalidation  
- [ ] Introduces breaking changes  

**Breaking Changes:**
```text
List any schema, API, or pipeline modifications that require migration.
```

---

## 🧭 Reviewer Checklist (Maintainers Only)

| Check | Status | Notes |
|--------|--------|-------|
| CI/CD Workflows Passed | ☐ |  |
| FAIR+CARE Governance Review | ☐ |  |
| SBOM Verified / Updated | ☐ |  |
| Docs Follow Markdown Rules | ☐ |  |
| Ledger Entry Added | ☐ |  |

---

## 🕰️ Versioning & Provenance

**Version Increment:**
- [ ] Major (breaking)  
- [ ] Minor (feature)  
- [ ] Patch (fix/update)

**Target Release:**  
`releases/v10.2.0/manifest.zip`

**Checksum Verification:**
```bash
sha256sum <artifact>
```

**Telemetry Linkage:**  
Ensure workflow updates `releases/v10.2.0/focus-telemetry.json`.

---

<div align="center">

**Thank you for contributing to the Kansas Frontier Matrix!**  
Each PR reinforces open, ethical, and reproducible geospatial science.

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to GitHub Overview](README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>