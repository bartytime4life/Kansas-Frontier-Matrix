---
title: "🧾 Kansas Frontier Matrix — Pull Request Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v11.2.3"
last_updated: "2025-12-09"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../releases/v11.2.2/manifest.zip"
telemetry_ref: "../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-pullrequest-v4.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Template"
intent: "pull-request-template"
role: "process-template"
category: "Governance · Process · CI/CD"

classification: "Public Document"
sensitivity: "General"
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
indigenous_rights_flag: false
redaction_required: false

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
data_steward: "KFM FAIR+CARE Council"

provenance_chain:
  - ".github/PULL_REQUEST_TEMPLATE.md@v10.3.1"
  - ".github/PULL_REQUEST_TEMPLATE.md@v10.4.1"
  - ".github/PULL_REQUEST_TEMPLATE.md@v11.0.0"
  - ".github/PULL_REQUEST_TEMPLATE.md@v11.0.1"
  - ".github/PULL_REQUEST_TEMPLATE.md@v11.2.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:Feature"

json_schema_ref: "../schemas/json/github-pullrequest-v11.schema.json"
shape_schema_ref: "../schemas/shacl/github-pullrequest-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-pullrequest-template:v11.2.3"
semantic_document_id: "kfm-doc-github-pullrequest-template"
event_source_id: "ledger:.github/PULL_REQUEST_TEMPLATE.md"
immutability_status: "mutable-plan"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical narratives"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next PR-process update"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Pull Request Template**  
`.github/PULL_REQUEST_TEMPLATE.md`

Ensure every contribution meets **KFM-MDP v11.2.2**, **MCP-DL v6.3**, **FAIR+CARE**,  
and **Diamond⁹ Ω / Crown∞Ω** governance requirements.

All PRs are:

- Fully validated  
- Governance-audited  
- SBOM-verified  
- Telemetry-logged  
- Schema-checked  
- Security-scanned  

[![MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 🪶 Summary

> Provide a brief explanation of **what** this PR changes and **why**.

### Type of Change (check all that apply)

- [ ] ✨ Feature  
- [ ] 🐛 Bug Fix  
- [ ] 🧠 AI / Model Update  
- [ ] 🗺️ Data Update (STAC/DCAT/metadata)  
- [ ] 📚 Documentation  
- [ ] 🔧 Refactor / Maintenance  
- [ ] ⚙️ CI/CD Workflow  
- [ ] 🏛 Governance / Standards Update  

### Governance Binding?

- [ ] 🔒 **Non-governance** (no change to contracts, schemas, or standards)  
- [ ] 🏛 **Governance-impacting** (update standards, schemas, or contracts; requires council review)  

### PR Summary (2–4 sentences)

> _Write your summary here._

---

## 🧩 Related Issues / References

- Closes: #`<issue>`  
- Related issues:  
- Related docs:  
  - `docs/...`  
  - `docs/standards/...`  
  - `docs/history/...`  
- Dataset manifests: `data/...`  
- STAC/DCAT items: `data/stac/...`  
- Architecture docs: `docs/architecture/...`  
- ADRs touched/added: `ADR/00xx-*.md`  

---

## 📂 Changes Introduced

### Files / Areas Affected

- [ ] `src/`  
- [ ] `web/`  
- [ ] `data/`  
- [ ] `schemas/`  
- [ ] `docs/`  
- [ ] `.github/`  
- [ ] `tests/`  
- [ ] `configs/`  
- [ ] `ADR/`  

### Pipeline Stages Touched (if applicable)

- [ ] `calibrate`  
- [ ] `preprocess`  
- [ ] `pretrain`  
- [ ] `train`  
- [ ] `predict`  
- [ ] `diagnose`  
- [ ] `submit`  
- [ ] Other: `__________________`

### High-Level Overview

~~~text
- …
- …
- …
~~~

---

## 🧮 Local Validation & Testing Checklist

### Code & Data Validation

- [ ] Linting (Python/TS/MD)  
- [ ] Unit + integration tests  
- [ ] Schema validation (JSON/YAML)  
- [ ] STAC/DCAT validation (if applicable)  
- [ ] SBOM impact reviewed (dependencies / licenses)  
- [ ] No secrets or sensitive coordinates added  

### Documentation Validation

- [ ] Follows KFM-MDP v11.2.2  
- [ ] Front-matter updated & valid  
- [ ] Links verified  
- [ ] Mermaid diagrams render (if applicable)  

### Commands Run (for reproducibility)

~~~bash
# Example (edit as needed)
# make ci-local
# spectramind selftest --deep
# spectramind train --config ...
~~~

> _List the exact commands you ran locally/CI to validate this PR._

---

## ♿ Accessibility (A11y) Impact

If UI changes:

- [ ] Keyboard navigation verified  
- [ ] Focus states correct  
- [ ] High-contrast mode compatible  
- [ ] Alt text included where needed  
- [ ] Respects `prefers-reduced-motion`  

**A11y Notes:**  
> _Write here._

---

## ⚖️ FAIR+CARE Governance Confirmation

### FAIR Principles

- [ ] **F1** Findable (IDs, metadata, indexing)  
- [ ] **A1** Accessible (open formats, documented access)  
- [ ] **I1** Interoperable (STAC/DCAT/JSON-LD aligned)  
- [ ] **R1** Reusable (clear licensing & provenance)  

### CARE Principles

- [ ] No unapproved Indigenous or cultural data added  
- [ ] CARE labels added/updated where appropriate  
- [ ] Sovereignty/masking rules respected (H3, generalization, redaction)  

Governance references:

- `../docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `../docs/standards/governance/ROOT-GOVERNANCE.md`  
- `../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

**FAIR+CARE Notes:**  
> _Write here._

---

## 🛡️ Security, SBOM & Compliance

- [ ] Security impact assessed (auth, authz, secrets, infra)  
- [ ] `.github/workflows/security_audit.yml` passing (static analysis, CVE scan)  
- [ ] Secrets scanning clean for new/changed files  
- [ ] SBOM regenerated/verified if dependencies changed (`sbom_ref`)  
- [ ] License and third‑party notices updated if needed  

**Security / Compliance Notes:**  
> _Write here._

---

## 🧠 AI / Model-Specific Changes (If Applicable)

- [ ] Model card updated (`mcp/model_cards/...`)  
- [ ] Training/eval datasets documented (`mcp/experiments/...`)  
- [ ] Hallucination/grounding guards validated  
- [ ] Focus Mode compatibility maintained  
- [ ] Relevant ADRs updated/added (architecture, loss, fusion, pretraining, etc.)  

**AI Notes:**  
> _Write here._

---

## 🗺️ Data & Metadata Changes (If Applicable)

- [ ] STAC Items/Collections updated (`data/stac/...`)  
- [ ] DCAT JSON-LD updated (`docs/data/...`)  
- [ ] Spatial extents updated (CRS + bbox; H3 masking checked)  
- [ ] Temporal extents updated (OWL-Time aligned)  
- [ ] Provenance/rights/licensing verified  

**Data Notes:**  
> _Write here._

---

## 🌍 Telemetry, Energy & Carbon (If Applicable)

- [ ] Telemetry events added/updated (conform to `github-pullrequest-v4` schema)  
- [ ] Energy metrics captured/updated (conform to `energy-v2` schema)  
- [ ] Carbon metrics captured/updated (conform to `carbon-v2` schema)  
- [ ] Telemetry IDs kept in sync with `focus-telemetry.json`  
- [ ] Manifest/SBOM references updated if telemetry or pipelines change  

**Telemetry / Sustainability Notes:**  
> _Write here._

---

## 🧪 Test Results

| Test Type            | Status | Notes |
|----------------------|--------|-------|
| Unit Tests           |        |       |
| Integration Tests    |        |       |
| End-to-End Tests     |        |       |
| Schema Validation    |        |       |
| STAC/DCAT Validation |        |       |
| FAIR+CARE Checks     |        |       |
| Accessibility Tests  |        |       |
| Security Scan        |        |       |

Paste relevant logs or summaries if needed.

---

## 📦 Release & Deployment Considerations

- [ ] Requires Docker rebuild  
- [ ] Requires Neo4j migration  
- [ ] Requires STAC/DCAT rebuild or reindex  
- [ ] Requires re-running ETL pipelines  
- [ ] Breaking change  

### Breaking Change Notes

~~~text
Describe the breaking change, affected consumers, and migration path.
~~~

---

## 🧭 Versioning & Provenance

Suggested SemVer bump:

- [ ] Major (breaking changes, contract updates)  
- [ ] Minor (new features, backwards compatible)  
- [ ] Patch (bugfix / internal change)  

Telemetry impact:

~~~text
Describe modifications to telemetry fields, workload patterns, or governance dashboards.
~~~

Provenance notes (optional):

~~~text
List major upstream sources, tools, or workflows involved in this change.
~~~

---

## ✅ Reviewer Checklist (Maintainers)

| Check                                   | Status | Notes |
|-----------------------------------------|--------|-------|
| CI/CD Passed                            |        |       |
| FAIR+CARE Compliance Verified           |        |       |
| Sovereignty/H3 Rules Verified           |        |       |
| SBOM Updated/Reviewed (if needed)       |        |       |
| Documentation Meets KFM-MDP v11.2.2     |        |       |
| Sensitive Data Review Complete          |        |       |
| Telemetry Impact Considered             |        |       |
| Security Audit & Scans Clean            |        |       |
| Governance Ledger Updated (if needed)   |        |       |

---

## 🕰 Template History

| Version | Date       | Notes                                                                                              |
|--------:|------------|----------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-09 | Aligned with telemetry/energy/carbon schemas, SBOM & security workflows, and pipeline stage flags. |
| v11.2.2 | 2025-11-27 | Updated with v11.2.2 metadata, FAIR+CARE + sovereignty blocks, and telemetry integration language. |
| v11.0.1 | 2025-11-19 | Full v11 rebuild: governance, telemetry, sustainability.                                           |
| v11.0.0 | 2025-11-18 | First v11 version aligned with KFM-MDP v11.                                                        |
| v10.4.1 | 2025-11-16 | Governance, metadata, and accessibility improvements.                                              |
| v10.3.1 | 2025-11-13 | Initial PR template.                                                                               |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [⚙️ GitHub Infrastructure](./README.md) · [🛡 Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
