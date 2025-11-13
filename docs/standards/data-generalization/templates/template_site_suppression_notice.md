---
title: "🚫 Kansas Frontier Matrix — Site Suppression Notice Template"
path: "docs/standards/data-generalization/templates/template_site_suppression_notice.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-generalization-suppression-v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🚫 **Kansas Frontier Matrix — Sensitive Site Suppression Notice Template**
`docs/standards/data-generalization/templates/template_site_suppression_notice.md`

**Purpose:**  
Provide a formal, FAIR+CARE-compliant notice documenting **why precise spatial or temporal site information has been fully suppressed**, withheld, or replaced with non-spatial representations in the Kansas Frontier Matrix (KFM).  
This template ensures transparency, sovereignty protection, and ethical governance under **CARE**, **CIDOC CRM**, and **MCP-DL v6.3**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governed-orange)](../../faircare.md)  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../LICENSE)

</div>

---

## 📘 Overview

This notice is required whenever **exact coordinates, geometries, temporal information, or descriptive details are removed entirely** rather than generalized.  
Site suppression is used only when disclosure could:

- Endanger Indigenous cultural resources  
- Facilitate looting or desecration of sacred or archaeological locations  
- Violate tribal sovereignty or established MOUs  
- Compromise endangered ecological or ceremonial areas  
- Contravene CARE-governed restrictions on cultural knowledge sharing  

All completed notices are stored under:

```
data/processed/suppression_notices/<dataset-or-site-id>.md
```

---

## 🧱 1. Metadata

```yaml
site_id: "<unique-site-or-feature-id>"
dataset_id: "<dataset-containing-site>"
site_type: "<archaeological | cultural | ecological | tribal | historical>"
reason_for_suppression: "<short-summary>"
suppression_method: "full-suppression"
authority_to_control: "<tribal/community authority>"
care_status: "<restricted | approved-with-conditions | sovereign-only>"
report_author: "<name + role>"
report_date: "YYYY-MM-DD"
```

---

## 🎯 2. Justification for Suppression

Provide a clear, concise explanation:

- Cultural sovereignty requirements  
- Tribal governance decisions  
- Sensitive ceremonial or burial sites  
- Legal or MOU restrictions  
- Ecological protection  
- Risk of harm through disclosure  

> _Example:_  
> Coordinates withheld at the request of the Prairie Band Potawatomi Nation to protect sacred ceremonial grounds and prevent unauthorized disturbance.

---

## 🧭 3. Original Data Characteristics (Before Suppression)

| Attribute | Description |
|-----------|-------------|
| Spatial precision | e.g., sub-meter GNSS, digitized archival record |
| Temporal precision | e.g., exact date, estimated period, centuries |
| Feature type | point, polygon, polyline, raster classification |
| Source provenance | museum, archive, tribal authority, ecological survey |
| Sensitivity classification | Low / Medium / **High** |

---

## ⚙️ 4. Suppression Methodology

Because this template covers **full suppression**, describe previous alternatives and why they were rejected.

| Method Considered | Reason Not Used |
|--------------------|------------------|
| Coordinate rounding | Still too precise for protection |
| Grid aggregation | Cluster too small; threat remains |
| Random displacement | Risk of approximate reverse-engineering |
| Generalization buffer | Insufficient masking for cultural safety |
| Temporal aggregation | Did not mitigate location risk |

### Final Decision  
```
Full suppression required to fulfill tribal sovereignty requirements and CARE governance responsibilities.
```

---

## 🧩 5. CARE Governance Review Summary

### 5.1 CARE Approval

```yaml
care_review:
  status: "<restricted | approved-with-conditions>"
  reviewer: "<council or tribal authority>"
  review_date: "YYYY-MM-DD"
  notes: "<ethical review notes>"
```

### 5.2 MOU or Sovereignty Agreement Reference  
(List formal agreements governing suppression)

```
docs/standards/data-generalization/governance/MOU_TEMPLATES/
```

---

## 🔐 6. Publication & Access Restrictions

| Restriction | Value |
|-------------|--------|
| Public access | prohibited / masked stub only |
| Internal access | restricted to council / sovereign authority |
| License | CC BY-NC 4.0 or stricter |
| Notice required | Yes — “Sensitive cultural site, location withheld” |
| Reverse engineering prohibition | explicitly stated |

Suggested published placeholder:

```
"Location withheld per CARE governance and sovereign authority."
```

---

## 🧪 7. Validation Artifacts

Attach or reference:

- CARE approval form  
- MOU  
- `faircare_summary.json`  
- `provenance_trace.json`  
- Telemetry entry showing suppression event  
- Governance ledger entry from:  
  ```
  docs/standards/data-generalization/governance/REVIEW_LOGS/sovereign_notices/
  ```

---

## 🧠 8. Ethical Rationale

Describe how suppression supports:

- Indigenous sovereignty  
- Cultural safety  
- Collective benefit  
- Prevention of harm  
- Ecological stewardship  
- CARE Principle compliance  

> _Example:_  
> The precise coordinates correspond to a burial site under active preservation and spiritual significance. Full suppression protects its sanctity and aligns with CARE Principle C4 — Ethics.

---

## 📓 9. Published Representation (What Replaces the Real Data)

| Representation | Description |
|----------------|-------------|
| Placeholder geometry | `"Location withheld"` |
| Thematic mapping | generalized region polygon (optional) |
| Metadata note | “Details withheld per CARE governance” |
| Data availability | “Upon sovereign approval only” |

Optional non-spatial representation may be provided if approved.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|--------|
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Initial site-suppression notice template aligned to v10 generalization + sovereignty governance updates. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC BY-NC 4.0**  
FAIR+CARE Sovereignty Protection · Ethical Data Stewardship · MCP v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Template Index](README.md) · [Generalization Standard](../README.md)

</div>

