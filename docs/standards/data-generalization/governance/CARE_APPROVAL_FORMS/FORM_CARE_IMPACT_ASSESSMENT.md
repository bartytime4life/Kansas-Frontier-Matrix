---
title: "🧭 CARE Community Impact Assessment Form — Sensitive / Indigenous-Governed Data"
path: "docs/standards/data-generalization/governance/CARE_APPROVAL_FORMS/FORM_CARE_IMPACT_ASSESSMENT.md"
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

# 🧭 **CARE Community Impact Assessment Form**  
`docs/standards/data-generalization/governance/CARE_APPROVAL_FORMS/FORM_CARE_IMPACT_ASSESSMENT.md`

**Purpose:**  
Assess and document the **cultural, ethical, environmental, community, and sovereignty impacts** of any dataset, analysis, visualization, or AI process using **sensitive or Indigenous-governed data** in the Kansas Frontier Matrix.  
Ensures alignment with **CARE Principles**, **Indigenous Data Sovereignty**, **FAIR+CARE Governance**, and **MCP-DL v6.3**.

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Indigenous_Governance-orange)](../../../faircare.md)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../LICENSE)

</div>

---

## 📘 When This Form is Required

A **CARE Impact Assessment** must be completed when:

- A dataset or derivative may have **non-technical impacts** on Indigenous communities.  
- Results may influence **policy**, **land use**, **heritage protection**, or **public perception**.  
- Cultural or archaeological information may become **exposed** or **misinterpreted**.  
- AI/ML models will make **inferences**, **predictions**, or **classifications** involving sensitive historical or cultural data.  
- A Tribal government, researcher, or steward specifically requests an impact review.

This form precedes or accompanies the **CARE Data Use Approval** process.

---

## 🧾 Section 1 — Dataset or Project Information

| Field | Value |
|------|--------|
| **Dataset or Project ID** |  |
| **Title / Description** |  |
| **Sensitivity Class** | High / Restricted / Tribal Sovereignty |
| **Dataset Steward / Authority** |  |
| **Requesting Person / Organization** |  |
| **Contact Email** |  |

---

## 🌱 Section 2 — Community & Cultural Context

Describe the cultural, ecological, political, or sovereignty-relevant context associated with the dataset.

```
[Describe community and cultural context]
```

Suggested prompts:
- Is the dataset tied to **ancestral lands**, **sacred sites**, **burial grounds**, or **cultural landscapes**?  
- Does it relate to **treaty boundaries**, **migration routes**, **historical trauma**, or **tribal governance areas**?  
- What relationships or MOUs govern this data?

---

## 🧠 Section 3 — Potential Impacts (Required)

### 3.1 Cultural & Ethical Impacts  
```
[Describe cultural risks or benefits]
```

### 3.2 Community Well-Being Impacts  
```
[Describe how project may affect community welfare, safety, or representation]
```

### 3.3 Environmental or Land Impacts  
```
[Describe potential effects on land, water, resources, or conservation areas]
```

### 3.4 Sovereignty & Governance Impacts  
```
[Describe how work intersects with tribal law, governance authority, or jurisdiction]
```

---

## ⚠️ Section 4 — Risk Identification & Mitigation

| Risk Category | Description | Mitigation Strategy |
|---------------|-------------|----------------------|
| **Cultural Risk** |  |  |
| **Misinterpretation Risk** |  |  |
| **Re-identification Risk** |  |  |
| **Environmental / Land Risk** |  |  |
| **Sovereignty Risk** |  |  |

```
[Describe mitigation details]
```

---

## 🔐 Section 5 — Data Protection & Generalization Requirements

Detail the masking, coarsening, or generalization steps required for ethical publication.

| Protection Level | Required? | Description |
|------------------|-----------|-------------|
| Coordinate Rounding | Yes / No |  |
| Grid Aggregation (1km / 10km) | Yes / No |  |
| Temporal Aggregation | Yes / No |  |
| Location Suppression | Yes / No |  |
| Restricted Access Controls | Yes / No |  |

```
[List relevant restrictions or requirements]
```

---

## 🤝 Section 6 — Community Consultation Summary

Describe consultation meetings, discussions, or approvals with Tribal or community representatives.

```
[Summarize consultation details]
```

Include:
- Participants  
- Dates  
- Outcomes  
- Requests or conditions  

---

## 🪙 Section 7 — Final Recommendation (by Data Steward)

| Field | Value |
|-------|--------|
| **Recommended Decision** | Approve / Approve with Conditions / Deny |
| **Conditions** |  |
| **Ethics Notes** |  |
| **Data Steward Name** |  |
| **Date** |  |
| **Signature** |  |

---

## ⚖️ Section 8 — FAIR+CARE Council Decision

| Field | Value |
|-------|--------|
| **Council Decision** | Approved / Approved with Conditions / Denied |
| **Required Safeguards** |  |
| **Reviewer(s)** |  |
| **Timestamp** |  |
| **Signatures** |  |

---

## 🧾 Governance Ledger Entry (Auto-Generated)

```json
{
  "event": "care_impact_assessment",
  "dataset_or_project_id": "",
  "decision": "",
  "reviewer": "",
  "conditions": "",
  "timestamp": "",
  "telemetry_ref": "releases/v10.2.0/focus-telemetry.json"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Initial CARE Impact Assessment form for high-sensitivity datasets. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC BY-NC 4.0**  
Indigenous Data Sovereignty · FAIR+CARE Governance · Master Coder Protocol v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to CARE Forms Index](README.md) · [Root Governance Charter](../../../governance/ROOT-GOVERNANCE.md)

</div>

