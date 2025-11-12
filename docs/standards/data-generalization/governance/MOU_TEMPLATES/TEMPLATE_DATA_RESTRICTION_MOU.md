---
title: "📄 Kansas Frontier Matrix — Data Restriction MOU Template (FAIR+CARE / Sensitive Data Governance)"
path: "docs/standards/data-generalization/governance/MOU_TEMPLATES/TEMPLATE_DATA_RESTRICTION_MOU.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-generalization-mou-v1.json"
governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
license: "CC BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📄 **Kansas Frontier Matrix — Data Restriction Memorandum of Understanding (MOU) Template**  
`docs/standards/data-generalization/governance/MOU_TEMPLATES/TEMPLATE_DATA_RESTRICTION_MOU.md`

**Purpose:**  
Provide a **formal agreement template** for datasets requiring *conditional access*, *limited redistribution*, *embargo periods*, or *controlled generalization* due to cultural, archaeological, ecological, legal, or sovereignty considerations.  
This template ensures all restricted datasets remain compliant with **FAIR+CARE**, **MCP-DL v6.3**, **CIDOC CRM**, and **DCAT 3.0** governance.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../faircare.md)  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../LICENSE)  
[![Status: Governed](https://img.shields.io/badge/Status-Diamond⁹_Ω_Certified-brightgreen)]()
</div>

---

## 📘 Overview

This **Data Restriction MOU** governs datasets that:

- Contain information requiring *partial disclosure*  
- Require *generalization* (spatial/temporal masking) before publication  
- Are subject to *embargo periods* (e.g., ongoing excavations, endangered species)  
- Must be *reviewed periodically* by communities, tribal nations, or data stewards  
- Require *controlled redistribution* or *limited external access*  

Once completed, this MOU becomes part of the **Governance Ledger** and informs all FAIR+CARE validations and data contract checks.

---

## 🧱 MOU Metadata Block (Required)

```yaml
mou_id: "mou-template-data-restriction-v1"
version: "v1.0.0"
dataset_id: "<dataset-id>"
authority_to_control: "<community/tribal/stewardship entity>"
restriction_level: "Moderate | High | Very High"
review_cycle: "Annual / FAIR+CARE Council"
legal_contact: "<email or phone>"
sensitivity_class: "<Low|Moderate|High|Critical>"
governance_register_ref: "../../governance_register.json"
```

---

## 🧩 1. Parties to the Agreement

**1.1 Data Steward(s)**  
Kansas Frontier Matrix (KFM) — represented by:  
- Name: ___________________________  
- Title: ___________________________  
- Contact: _________________________  

**1.2 Authority to Control / Community Partner**  
(Tribal nation, museum, agency, land steward, cultural authority)

- Entity: __________________________  
- Authorized Representative: __________________  
- Role/Title: _______________________  
- Contact: _________________________  

**1.3 Additional Stakeholders (Optional)**  
- Partner Institution(s): ___________________  
- Fieldwork/Research PI(s): __________________  

---

## 🧩 2. Dataset Identification

| Field | Description |
|---|---|
| **Dataset Name** | __________________________________ |
| **Dataset ID (STAC/DCAT)** | __________________________________ |
| **Domain** | Archaeology / Ecology / Indigenous Knowledge / Historical / Other |
| **Data Type** | Spatial / Tabular / Text / Raster / Mixed |
| **Original Precision** | __________________________________ |
| **Associated Documentation** | _________________________________ |
| **Data Contract Reference** | `docs/contracts/data-contract-v3.json` |

---

## 🧩 3. Restriction Rationale

Provide the reason(s) this dataset requires restricted handling:

- Cultural sensitivity  
- Archaeological site protection  
- Ecological endangerment  
- Legal compliance  
- Confidential research  
- Community sovereignty  
- Ethical concerns  

**Statement of Rationale:**  
```
____________________________________________________________________________
____________________________________________________________________________
```

---

## 🧩 4. Allowed & Prohibited Uses

### 4.1 Allowed Uses (Check all that apply)
- [ ] Academic research  
- [ ] Teaching / educational use  
- [ ] Public summary-level reporting  
- [ ] Generalized map visualization  
- [ ] AI training (with CARE controls)  
- [ ] Archival storage (high-precision retention)

### 4.2 Prohibited Uses
- [ ] Commercial resale  
- [ ] Redistribution outside KFM  
- [ ] Publication of unmasked coordinates  
- [ ] Use in sensitive contexts (specify):  
```
_____________________________________________________________
```

---

## ⚙️ 5. Required Generalization Methods

Describe **exact masking procedures** required before public release:

| Method | Requirement |
|---|---|
| Spatial Rounding | e.g., round coordinates to 2 decimals |
| Random Offset | e.g., ± 1 km randomized displacement |
| Grid Aggregation | e.g., 5 × 5 km centroid masking |
| Temporal Masking | e.g., replace exact years with decade ranges |
| Attribute Suppression | e.g., remove excavation descriptions |
| Site Removal | Omit sacred or highly sensitive sites entirely |

**Generalization Specification:**  
```
_____________________________________________________________
_____________________________________________________________
```

---

## 🧩 6. Access Levels

| Access Tier | Description | Approved? |
|---|---|---|
| **Tier 0 — Internal Only** | High-precision data retained in secure vault; full restrictions | ☐ |
| **Tier 1 — Restricted Access** | Masked dataset accessible to trusted KFM staff | ☐ |
| **Tier 2 — Controlled Release** | Public dataset with generalization applied | ☐ |
| **Tier 3 — Fully Open** | Only after Council approval and MOU expiration | ☐ |

---

## 📜 7. Embargo or Expiry Conditions

If applicable:

- Embargo Start Date: __________________  
- Embargo End Date: ____________________  
- Conditions for lifting embargo:  
```
_____________________________________________________________
_____________________________________________________________
```

---

## 🧩 8. CARE Governance Requirements

### Mandatory CARE Statements
```text
This dataset requires oversight by the community or entity identified  
as Authority to Control. All publication or redistribution of the  
dataset—generalized or otherwise—must receive explicit approval  
from that authority, in partnership with the FAIR+CARE Council.
```

### CARE Metadata to Embed
```json
{
  "care": {
    "status": "restricted",
    "statement": "Limited release under conditional generalization.",
    "reviewer": "<community-or-council>",
    "date_reviewed": "<YYYY-MM-DD>",
    "notes": "Embargo until agreement expiration."
  }
}
```

---

## 🧩 9. Storage, Retention & Revocation

- **High-precision raw data must remain encrypted** in KFM secure archive.  
- Revocation requests must be honored within **72 hours**.  
- All access events logged in Governance Ledger.  
- Data retained for:  
  - [ ] 1 year  
  - [ ] 5 years  
  - [ ] 10 years  
  - [ ] Indefinite (with renewal)  

---

## 🧾 10. Signatures

### Community / Authority to Control  
Name: ___________________________  
Signature: ________________________  
Date: ____________________________

### Kansas Frontier Matrix (KFM)  
Name: ___________________________  
Signature: ________________________  
Date: ____________________________

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Added embargo section, masking table, and expanded CARE fields. |
| v10.0.0 | 2025-11-09 | FAIR+CARE Council | Initial template release for restricted-use sensitive datasets. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC BY-NC 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified ·  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to MOU Templates](README.md) · [Generalization Governance](../README.md)

</div>

