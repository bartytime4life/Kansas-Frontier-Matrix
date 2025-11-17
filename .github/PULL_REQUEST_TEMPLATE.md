---
title: "🧾 Kansas Frontier Matrix — Pull Request Template (MCP v6.3 · FAIR+CARE Certified)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../releases/v10.4.0/manifest.zip"
telemetry_ref: "../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-pullrequest-v2.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Template"
intent: "pull-request-template"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - ".github/PULL_REQUEST_TEMPLATE.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../schemas/json/github-pullrequest.schema.json"
shape_schema_ref: "../schemas/shacl/github-pullrequest-shape.ttl"
doc_uuid: "urn:kfm:doc:github-pullrequest-template-v10.4.1"
semantic_document_id: "kfm-doc-github-pullrequest-template"
event_source_id: "ledger:.github/PULL_REQUEST_TEMPLATE.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "process-template"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next PR-process update"
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

## 📘 Overview

This file is the **canonical Pull Request template** for the Kansas Frontier Matrix (KFM) monorepo.

- It structures **every PR description** for MCP-DL v6.3 compliance.  
- It embeds **FAIR+CARE**, governance, and A11y confirmations directly into the review flow.  
- CI workflows parse sections of this template for **telemetry, governance checks, and release metadata**.  

Contributors should:

- Fill out all relevant sections honestly and completely.  
- Check all applicable boxes in the validation & governance sections.  
- Link to relevant docs, datasets, and manifests for provenance.  

Maintainers should:

- Use the **Reviewer Checklist** section when approving PRs.  
- Ensure governance, A11y, and telemetry implications are understood before merge.

---

## 🗂️ File Context

```text
.github/
│
├── PULL_REQUEST_TEMPLATE.md      # This file — PR process & governance template
└── README.md                     # GitHub infrastructure overview
````

---

## 📄 Pull Request Form

> **Note:** Everything below is what contributors will see and fill out when opening a PR.

### 🪶 Summary

> Provide a clear explanation of the purpose and context of this pull request.

**Type of Change:**

* [ ] ✨ Feature / Enhancement
* [ ] 🐛 Bug Fix
* [ ] 🧠 AI / Model Update
* [ ] 🗺️ Data Layer Addition
* [ ] 📚 Documentation Update
* [ ] 🔧 Refactor / Maintenance
* [ ] ⚙️ CI/CD or Workflow Update

**Description:**

<!-- (2–4 concise sentences explaining scope, motivation, and intent) -->

---

### 🧩 Related Issues / Links

* Closes #`<issue_number>`
* Related Docs: `[docs/...path...]`
* Dataset Manifest: `[data/sources/...json]`
* STAC/DCAT Item: `[data/stac/...item.json]`

---

### 📂 Changes Introduced

**Affected Modules:**

* [ ] `src/` — backend ETL, AI, API
* [ ] `web/` — React, Timeline, MapLibre, Cesium
* [ ] `data/` — datasets, manifests, schemas
* [ ] `docs/` — documentation, governance, architecture
* [ ] `.github/` — workflows, automation, security

**Major Changes:**

```text
- Introduced predictive ETL for NOAA drought datasets.
- Integrated Focus Transformer v2.4 narrative pipeline.
- Updated telemetry schema for ISO 50001 energy reporting.
```

---

### 🧮 Validation Checklist

#### Code & Data

* [ ] 🧪 `make lint` — formatting + schema checks
* [ ] 🏷️ `make validate` — STAC/DCAT + FAIR+CARE audits
* [ ] 🧾 `make test` — all tests pass
* [ ] 🧠 AI model updates include model card (`docs/models/...md`)
* [ ] 🔐 No secrets or sensitive content
* [ ] 🧱 SBOM updated (`releases/v10.4.0/sbom.spdx.json`)

#### Documentation

* [ ] 📘 Updated/created all required READMEs
* [ ] 🗺️ Dataset manifests include license, checksum, provenance
* [ ] 🧩 Architecture diagrams & workflow references updated

---

### ⚖️ FAIR+CARE Governance Confirmation

* [ ] I confirm compliance with **FAIR** principles.
* [ ] I confirm compliance with **CARE** principles.
* [ ] I verify no private, sensitive, or unethical content is included.
* [ ] I reviewed **MCP-DL v6.3** and the **Governance Charter**.

---

### 🧠 Testing & Results

| Test Type            | Status | Notes                                              |
| -------------------- | ------ | -------------------------------------------------- |
| ETL / Pipeline       | ✅/⚠️/❌ | e.g. See: `data/work/tmp/etl/logs/validation.json` |
| AI Model             | ✅/⚠️/❌ | e.g. F1 = 0.95 (Focus Transformer v2.4)            |
| Frontend Build       | ✅/⚠️/❌ | e.g. Verified via `npm run build`                  |
| FAIR+CARE Validation | ✅/⚠️/❌ | e.g. All restrictions + labels verified            |
| Docs Lint            | ✅/⚠️/❌ | e.g. Markdown + YAML valid                         |

> Attach logs or screenshots if helpful.

---

### 🧾 Release / Deployment Notes

* [ ] Requires Docker rebuild
* [ ] Requires Neo4j reindex
* [ ] Requires STAC/DCAT catalog rebuild
* [ ] Introduces breaking changes

**Breaking Changes:**

```text
List migrations or API/schema modifications here.
```

---

### 🧭 Reviewer Checklist (Maintainers Only)

| Check                       | Status | Notes |
| --------------------------- | ------ | ----- |
| CI/CD Workflows Passed      | ☐      |       |
| FAIR+CARE Governance Review | ☐      |       |
| SBOM Verified / Updated     | ☐      |       |
| Docs Follow Markdown Rules  | ☐      |       |
| Governance Ledger Updated   | ☐      |       |

---

### 🕰️ Versioning & Provenance

**Version Increment:**

* [ ] Major
* [ ] Minor
* [ ] Patch

**Target Release:**
`releases/v10.4.0/manifest.zip`

**Checksum Verification:**

```bash
sha256sum <artifact>
```

**Telemetry Linkage:**
All updates must appear in:

```text
releases/v10.4.0/focus-telemetry.json
```

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                    |
| ------: | ---------- | ---------------------------------------------------------------------------------------------------------- |
| v10.4.1 | 2025-11-16 | Upgraded to KFM-MDP v10.4.3; added extended YAML metadata, KFM-aligned sections, and v10.4.0 release refs. |
| v10.3.1 | 2025-11-13 | Initial governance-aligned PR template for MCP-DL v6.3 and FAIR+CARE certification.                        |

<div align="center">

**Thank you for contributing to the Kansas Frontier Matrix!**
Every PR strengthens open, ethical, and reproducible geospatial science.

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
[Back to GitHub Overview](README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
