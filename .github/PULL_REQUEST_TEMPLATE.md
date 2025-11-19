---
title: "🧾 Kansas Frontier Matrix — Pull Request Template (MCP v6.3 · FAIR+CARE Certified)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v11.0.0"
last_updated: "2025-11-18"

review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"

sbom_ref: "../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../releases/v11.0.0/manifest.zip"
telemetry_ref: "../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-pullrequest-v3.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"

status: "Active / Enforced"
doc_kind: "Template"
intent: "pull-request-template"
role: "process-template"

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
  - ".github/PULL_REQUEST_TEMPLATE.md@v10.4.1"

previous_version_hash: "<previous-sha256>"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/github-pullrequest-v11.schema.json"
shape_schema_ref: "../schemas/shacl/github-pullrequest-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-pullrequest-template-v11.0.0"
semantic_document_id: "kfm-doc-github-pullrequest-template"
event_source_id: "ledger:.github/PULL_REQUEST_TEMPLATE.md"
immutability_status: "mutable-plan"
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
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next PR-process update"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Pull Request Template**  
`.github/PULL_REQUEST_TEMPLATE.md`

**Purpose**  
Ensure every contribution — code, data, models, Story Nodes, pipelines, workflows, or documentation — adheres to **Master Coder Protocol (MCP-DL v6.3)**, **KFM-MDP v11.0.0**, **FAIR+CARE** ethics, and **Diamond⁹ Ω / Crown∞Ω** governance.  
All PRs are automatically **validated**, **telemetry-logged**, **governance-audited**, and **provenance-attested**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)  
[![Markdown · KFM-MDP v11](https://img.shields.io/badge/Markdown-KFM--MDP_v11.0.0-informational)](../docs/standards/kfm_markdown_protocol_v11.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)  
[![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-success)]()

</div>

--- ✦ ---

## 📘 Overview

This file is the **canonical Pull Request template** for the Kansas Frontier Matrix (KFM) monorepo.

- It structures every PR for **MCP-DL v6.3** and **KFM-MDP v11** compliance.  
- It embeds **FAIR+CARE**, governance, and accessibility confirmations into the review flow.  
- CI workflows parse sections of this template for **telemetry, governance checks, and release metadata**.  

Contributors should:

- Fill out all relevant sections honestly and completely.  
- Check all applicable boxes in the validation & governance sections.  
- Link to relevant docs, datasets, and manifests for provenance.  

Maintainers should:

- Use the **Reviewer Checklist** when approving PRs.  
- Ensure governance, A11y, and telemetry implications are understood before merge.

--- ✦ ---

## 🗂️ File Context

```text
.github/
│
├── PULL_REQUEST_TEMPLATE.md      # This file — PR process & governance template
└── README.md                     # GitHub infrastructure overview
```

Everything below this line is what contributors see when opening a PR.

---

## 🪶 Summary

> Provide a clear explanation of the purpose and context of this pull request.

**Type of Change (select all that apply):**

- [ ] ✨ Feature / Enhancement  
- [ ] 🐛 Bug Fix  
- [ ] 🧠 AI / Model Update  
- [ ] 🗺️ Data Layer Addition / Change  
- [ ] 📚 Documentation Update  
- [ ] 🔧 Refactor / Maintenance  
- [ ] ⚙️ CI/CD or Workflow Update  
- [ ] 🏛 Governance / Standards / Policy  

**Short Description**

> 2–4 concise sentences explaining scope, motivation, and intent.

---

## 🧩 Related Issues / References

- Closes: #`<issue_number>`  
- Related issues: #`<issue_number>`, ...  
- Related docs: `docs/...`  
- Dataset manifest(s): `data/sources/...json`  
- STAC/DCAT item(s): `data/stac/...item.json` / `docs/data/dcat/...jsonld`  
- Design or ADR docs: `docs/architecture/...`, `docs/guides/...`  

---

## 📂 Changes Introduced

**Affected Areas (check all that apply):**

- [ ] `src/` — backend ETL, AI, API  
- [ ] `web/` — React, Timeline, MapLibre, Cesium  
- [ ] `data/` — datasets, manifests, schemas  
- [ ] `docs/` — documentation, governance, architecture  
- [ ] `schemas/` — JSON Schema, SHACL, ontology  
- [ ] `.github/` — workflows, automation, security  
- [ ] `tests/` — unit, integration, E2E, schema, a11y  

**High-Level Change List (bullets):**

```text
- ...
- ...
- ...
```

---

## 🧮 Local Validation & Testing Checklist

**Code & Data**

- [ ] `npm run lint` (or equivalent)  
- [ ] `npm test` / `pytest` / `make test` (as applicable)  
- [ ] Schemas validate (JSON Schema / SHACL)  
- [ ] STAC/DCAT validation passes for changed datasets  
- [ ] No secrets or sensitive data added to code or configs  
- [ ] SBOM impact considered (new deps or major updates)  

**Documentation**

- [ ] New/updated docs follow **KFM-MDP v11** (front-matter, fences, headings)  
- [ ] Directory layouts updated where structure changed  
- [ ] Links and references validated  
- [ ] Diagrams (Mermaid, etc.) render correctly  

> Add any additional project-specific commands you ran here (e.g., `make validate`, `pre-commit run`).

---

## ♿ Accessibility (A11y) Impact

**If this PR changes UI or content, please address:**

- [ ] Keyboard navigation verified for new/changed components  
- [ ] Focus states and landmarks correct  
- [ ] Color contrast meets WCAG 2.1 AA  
- [ ] Alt text and accessible names added/updated  
- [ ] Respects reduced-motion preferences (if applicable)  

**A11y Notes**

> Briefly describe any specific A11y testing performed or known limitations.

---

## ⚖️ FAIR+CARE Governance Confirmation

**FAIR (Data Principles)**

- [ ] Data affected by this PR remains **Findable** (indexed, documented)  
- [ ] Data remains **Accessible** (licensed, documented endpoints)  
- [ ] Data remains **Interoperable** (STAC/DCAT, standard schemas)  
- [ ] Data remains **Reusable** (clear license, provenance, usage notes)  

**CARE (Indigenous Data Governance)**

- [ ] This PR does **not** introduce or expose new sensitive Indigenous or cultural data  
- [ ] Any dataset with cultural/heritage content has CARE labels and notes updated  
- [ ] Necessary community reviews (if any) have occurred or are requested via governance forms  

**Confirmations**

- [ ] I have reviewed **FAIR+CARE** guidelines (`docs/standards/faircare.md`).  
- [ ] I have reviewed the **Governance Charter** (`docs/standards/governance/ROOT-GOVERNANCE.md`).  

If this PR includes sensitive or Indigenous data, link to the corresponding governance issue:

> Governance issue: `#<issue_id>` or URL

---

## 🧠 AI / Model Updates (if applicable)

If this PR touches AI models, prompts, Focus Mode, or Story Nodes:

- [ ] Model card added/updated in `docs/models/...`  
- [ ] Training/eval datasets documented and licensed  
- [ ] Known limitations and risks documented  
- [ ] Hallucination/grounding checks implemented or unchanged  
- [ ] Focus Mode references remain grounded in the graph and sources  

**Model Details**

- Model name / version:  
- Change type: (new, fine-tune, configuration, prompt, etc.)  
- Evaluation summary (metrics, datasets):  

---

## 🗺️ Data & Metadata Changes (if applicable)

- [ ] STAC Items/Collections updated and validated  
- [ ] DCAT dataset JSON-LD updated and validated  
- [ ] Spatial extents (bbox) and CRS documented  
- [ ] Temporal extents documented and OWL-Time-consistent  
- [ ] Licenses, rights, and provenance updated  

**Data Notes**

> Describe any new or updated datasets, including sources, transformations, and intended use.

---

## 🧪 Testing & Results (Table)

| Test Type            | Status (✅/⚠️/❌) | Notes / Command                                                     |
|----------------------|-------------------|---------------------------------------------------------------------|
| Unit Tests           |                   | e.g., `npm test`, `pytest`                                         |
| Integration Tests    |                   | e.g., `pytest tests/integration`                                   |
| E2E Tests            |                   | e.g., `npm run test:e2e`                                           |
| Schema Validation    |                   | e.g., `python tools/validate_schemas.py`                           |
| STAC/DCAT Validation |                   | e.g., `make validate-stac`, `make validate-dcat`                   |
| FAIR+CARE Validation |                   | e.g., `faircare-validate.yml` output checked                       |
| A11y Tests           |                   | e.g., `npm run test:a11y`                                          |
| Performance Checks   |                   | e.g., any major performance-impacting test suite or benchmark logs |

Attach logs or screenshots if helpful, particularly for failing or borderline cases.

---

## 🧾 Release / Deployment Notes

- [ ] Requires Docker rebuild  
- [ ] Requires Neo4j reindex or migration  
- [ ] Requires STAC/DCAT catalog rebuild  
- [ ] Requires data backfill / re-run of specific ETL pipelines  
- [ ] Introduces breaking changes (see below)  

**Breaking Changes**

```text
Describe any API, schema, or behavior changes that may break existing usage.
```

**Target Release / Tag (if known)**

```text
e.g., v11.0.1 or "next minor"
```

---

## 🧭 Versioning & Provenance

**Suggested Version Increment**

- [ ] Major (breaking change)  
- [ ] Minor (new functionality, backwards compatible)  
- [ ] Patch (bug fix / small change)  

**Relevant Artifacts (SBOM & Manifest)**

- SBOM (to be updated/verified): `releases/v11.0.0/sbom.spdx.json`  
- Manifest: `releases/v11.0.0/manifest.zip`  

**Telemetry Linkage**

Changes introduced in this PR should be reflected in:

```text
releases/v11.0.0/focus-telemetry.json
```

If you are changing telemetry schemas, describe how:

```text
Short description of new or modified telemetry fields and rationale.
```

---

## ✅ Reviewer Checklist (Maintainers Only)

| Check                                 | Status (☐/✅) | Notes |
|---------------------------------------|---------------|-------|
| CI/CD Workflows Passed                |               |       |
| FAIR+CARE Governance Requirements Met |               |       |
| SBOM Impact Reviewed / Updated        |               |       |
| Docs Follow KFM-MDP v11               |               |       |
| Sensitive Data Review (if applicable) |               |       |
| Telemetry & Observability Considered  |               |       |
| Governance Ledger Updated (if needed) |               |       |

Maintainers should document any **exceptions** or **conditional approvals** in the PR discussion.

--- ✦ ---

## 🕰️ Template Version History

| Version  | Date         | Summary                                                                                                                    |
|---------:|-------------:|----------------------------------------------------------------------------------------------------------------------------|
| v11.0.0  | 2025-11-18   | Upgraded to KFM-MDP v11; updated release references to v11.0.0; added explicit FAIR+CARE, A11y, AI, and telemetry blocks. |
| v10.4.1  | 2025-11-16   | KFM-MDP v10.4.3; added extended YAML metadata, KFM-aligned sections, and v10.4.0 release refs.                            |
| v10.3.1  | 2025-11-13   | Initial governance-aligned PR template for MCP-DL v6.3 and FAIR+CARE certification.                                       |

---

<div align="center">

**Thank you for contributing to the Kansas Frontier Matrix!**  
Every PR strengthens open, ethical, and reproducible geospatial science.

© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0  
Maintained under **Master Coder Protocol v6.3** and **KFM-MDP v11.0.0** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to GitHub Overview](README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>