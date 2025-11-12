---
title: "📝 CARE Access Request Form — Sensitive / Indigenous-Governed Data"
path: "docs/standards/data-generalization/governance/CARE_APPROVAL_FORMS/FORM_CARE_ACCESS_REQUEST.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-generalization-care-forms-v1.json"
governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
license: "CC BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📝 **CARE Access Request Form**  
`docs/standards/data-generalization/governance/CARE_APPROVAL_FORMS/FORM_CARE_ACCESS_REQUEST.md`

**Purpose:**  
Formal request form required when accessing **Indigenous-governed**, **archaeologically sensitive**, or **culturally restricted** datasets within the Kansas Frontier Matrix (KFM).  
Ensures compliance with **CARE Principles**, **Indigenous sovereignty**, and **MCP-DL v6.3** governance requirements.

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Indigenous_Governance-orange)](../../../faircare.md)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../LICENSE)

</div>

---

## 📘 Instructions

- Complete **all required fields**.  
- Submit this form to the **FAIR+CARE Council** *and* the **designated Tribal/Community Steward** listed in dataset metadata.  
- Access **will not** be granted without explicit community authorization.  
- All approvals and denials are recorded in the **Governance Ledger** (`reports/audit/governance-ledger.json`).  
- Sensitive datasets include:  
  - Indigenous cultural sites  
  - Sacred places  
  - Archaeological locations  
  - Restricted ecological habitats  
  - Tribal historical materials (oral histories, restricted archives, etc.)

---

## 🧾 Section 1 — Requestor Information

| Field | Value |
|-------|--------|
| **Name** |  |
| **Affiliation / Institution** |  |
| **Email** |  |
| **Phone (optional)** |  |
| **Role in KFM (if applicable)** | Researcher / Developer / Curator / External Partner / Other |

---

## 🗂️ Section 2 — Dataset(s) Requested

Provide STAC/DCAT identifiers or manifest paths.

| Dataset ID / Name | Path or Catalog Reference | Reason for Sensitivity |
|------------------|---------------------------|------------------------|
|  |  | High / Restricted / Tribal Sovereignty |

**Example:**  
`kfm-sensitive-site-0001` — `data/processed/archaeology/generalized_sites.geojson`

---

## 🎯 Section 3 — Purpose of Access

> Describe the intended use, research question, operational need, or analytical purpose.

```
[Enter purpose here]
```

Must include:
- Expected benefits  
- Whether results will be public-facing  
- Whether derived datasets will be generalized or masked  
- Whether findings may impact Indigenous communities  

---

## 🤝 Section 4 — Community Engagement & Benefit

Explain how this access request:
- Respects **Collective Benefit (CARE)**  
- Ensures **non-extractive use**  
- Provides value to the community of origin  
- Integrates **ethical consultation**

```
[Describe engagement strategy]
```

---

## 🔐 Section 5 — Data Handling & Security Plan

Describe how sensitive data will be:
- Stored  
- Accessed  
- Isolated  
- Protected  
- Destroyed (if applicable)  
- Prevented from public disclosure

Include:
- Storage environment (encrypted / offline / secure archive)  
- Access controls  
- Retention schedule  
- Personnel permissions  

```
[Describe security measures]
```

---

## ⚙️ Section 6 — Derived Data & Generalization Plan

If analysis will produce new geospatial layers, models, or summaries, describe:

- Generalization method (rounding, masking, grid aggregation)  
- Resolution after masking  
- CARE review required before publication  
- Whether any data will be filtered or suppressed  
- Expected public outputs  

```
[Describe generalization procedures]
```

---

## 🧠 Section 7 — Ethical & Cultural Risk Assessment

| Question | Response |
|----------|----------|
| Does this work involve culturally sensitive knowledge? | Yes / No |
| Could results expose protected locations? | Yes / No |
| Have Tribal representatives been consulted? | Yes / No |
| Are there risks of misinterpretation or harm? | Yes / No |
| Are additional protections required? | Yes / No |

```
[Explain risks]
```

---

## 🪙 Section 8 — Consent & Authorization Signatures

### **Requestor Certification**
I certify that all information provided is accurate and that I will comply with the CARE governance guidelines, data restrictions, and ethical requirements of the Kansas Frontier Matrix.

**Signature:** ______________________  
**Date:** ___________________________

---

### **Community / Tribal Steward Authorization**

| Field | Value |
|--------|--------|
| **Name** |  |
| **Nation / Organization** |  |
| **Role / Authority** |  |
| **Approval Decision** | Approved / Approved with Conditions / Denied |
| **Conditions (if any)** |  |
| **Date** |  |
| **Signature** |  |

---

### **FAIR+CARE Council Authorization**

| Field | Value |
|--------|--------|
| **Reviewer(s)** |  |
| **Decision** | Approved / Approved with Conditions / Denied |
| **Notes** |  |
| **Timestamp** |  |
| **Signature(s)** |  |

---

## 🧾 Governance Ledger Entry (Auto-Generated Upon Submission)

```json
{
  "event": "care_access_request",
  "requestor": "",
  "dataset_id": "",
  "decision": "",
  "reviewer": "",
  "timestamp": "",
  "conditions": "",
  "telemetry_ref": "releases/v10.2.0/focus-telemetry.json"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Initial CARE access request form aligned with sensitive data governance & Tribal sovereignty MOUs. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC BY-NC 4.0**  
Indigenous Data Sovereignty · FAIR+CARE Governance · Master Coder Protocol v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to CARE Forms Index](README.md) · [Governance Charter](../../../governance/ROOT-GOVERNANCE.md)

</div>

