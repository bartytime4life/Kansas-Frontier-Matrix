---
title: "🪶 KFM v11 — Indigenous Data Governance & Consent Protocol (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/governance/indigenous-data-protocol.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Governance Protocol (LTS)"
review_cycle: "Biannual · Indigenous Data Governance Board (IDGB)"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "Aligned with v10.x → v11.x governance rules"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/indigenous-data-protocol-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/indigenous-data-protocol-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Governance Protocol"
intent: "indigenous-data-governance-and-consent"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Sovereignty-Respectful"

classification: "Public (Governed)"
sensitivity: "High (Indigenous & cultural data governance)"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
ttl_policy: "Biannual review"
sunset_policy: "Superseded by next Indigenous governance protocol revision"
---

<div align="center">

# 🪶 **KFM v11 — Indigenous Data Governance & Consent Protocol**  
`docs/data/governance/indigenous-data-protocol.md`

**Purpose**  
Define the **Indigenous Data Governance & Consent Protocol** of the **Kansas Frontier Matrix (KFM)** —  
ensuring **cultural sovereignty, ethical collaboration, and stewardship of Indigenous knowledge and heritage data**  
under the **FAIR+CARE** and **OCAP™ (Ownership, Control, Access, Possession)** frameworks and aligned with **UNDRIP**.

This protocol is binding for **all Indigenous-related data** in KFM.

</div>

---

## 📘 1. Overview

The **Indigenous Data Governance Protocol** ensures that all Indigenous-related datasets within KFM are managed in accordance with:

- **Tribal sovereignty & self-determination**  
- **Cultural respect & relational accountability**  
- **Free, prior, and informed consent (FPIC)**  
- **CARE principles** (Collective Benefit, Authority to Control, Responsibility, Ethics)  
- **OCAP™** principles (Ownership, Control, Access, Possession)  

It formalizes how Indigenous communities:

- Guide data use, access, and visibility  
- Retain rights of **ownership, control, and benefit** over any data derived from their heritage, lands, or knowledge  
- Participate in governance and approval of any public representation or reuse  

This protocol is jointly maintained by:

- **Indigenous Data Governance Board (IDGB)**  
- **FAIR+CARE Council**  
- **KFM Governance Secretariat**

---

## 🧭 2. Guiding Frameworks

| Framework | Description |
|----------|-------------|
| **OCAP™** | Affirms that Indigenous communities have the right to **Own, Control, Access, and Possess** their data. |
| **CARE Principles** | Embeds Collective Benefit, Authority to Control, Responsibility, and Ethics into all Indigenous datasets. |
| **FAIR Principles** | Supports findability, accessibility, and reuse **only within the bounds of cultural sensitivity and consent**. |
| **UNDRIP (Articles 18–31)** | Upholds Indigenous rights to maintain, protect, and develop manifestations of their cultures and intellectual property. |

---

## ⚙️ 3. Data Classification Levels

| Level | Description | Example | Access Policy |
|------|-------------|---------|--------------|
| **Level 1 — Open Cultural Data** | Data cleared for public educational use with explicit community approval. | Cultural geography layers, high-level TEK summaries (where communities approve sharing). | **Open Access** (with attribution + CARE flags) |
| **Level 2 — Controlled Access Data** | Requires explicit tribal or IDGB approval per request. | Heritage site polygons (generalized), oral history transcripts, community narratives. | **Ethical Access** (Request + Review + Agreement) |
| **Level 3 — Sensitive / Restricted Data** | Culturally sacred, ceremonial, or high-risk data. | Ceremonial objects, burial locations, spiritual practices, highly specific site coordinates. | **Restricted** — Not publicly shared; limited steward access |

All Indigenous datasets MUST include **machine-readable consent metadata**, e.g.:

~~~json
{
  "careConsent": {
    "authority": "Kaw Nation",
    "status": "approved",
    "access_level": "controlled",
    "last_reviewed": "2025-09-01"
  }
}
~~~

---

## ⚖️ 4. Indigenous Governance Workflow

~~~mermaid
flowchart TD
  A["Dataset Proposal or Update"] --> B["Indigenous Data Review (IDGB)"]
  B --> C{"Consent Granted?"}
  C -- Yes --> D["FAIR+CARE Certification\n+ Access Tier Assignment"]
  C -- No --> E["Dataset Restricted or Redacted"]
  D --> F["STAC/DCAT Publication\n(With Ethical/CARE Tags)"]
  E --> G["Governance Ledger Update\n(Restricted Entry)"]
~~~

- **Consent Review:** IDGB evaluates provenance, purpose, representation, and potential harms/benefits.  
- **Approval:** Only datasets with formal documented consent progress to public or controlled publication.  
- **Restriction/Redaction:** Sensitive datasets remain in secure repositories, may be generalized or redacted.  
- **Transparency:** Every decision is logged in the **Governance Ledger** and tracked via telemetry.

---

## 🧩 5. Consent & Attribution Requirements

All datasets referencing Indigenous communities MUST include:

| Field              | Description                                       | Example |
|--------------------|---------------------------------------------------|---------|
| `community_name`   | Full tribal or nation name                        | `"Osage Nation"` |
| `consent_status`   | Approval / restriction flag                       | `"approved"`, `"restricted"` |
| `consent_document` | Link or hash of signed consent agreement/template | `"docs/data/governance/consent_forms/Osage_2025.pdf"` |
| `review_date`      | Last review timestamp                             | `"2025-10-15"` |
| `review_authority` | Governing body granting consent                   | `"Indigenous Data Governance Board"` |
| `ethical_scope`    | Scope of approved use                             | `"Educational and non-commercial use only."` |

Consent metadata MUST be:

- **Machine-readable** (JSON/JSON-LD)  
- Validated against the Indigenous governance schema  
- Linked into STAC/DCAT and PROV-O lineage where Indigenous data is used  

---

## 🧠 6. Indigenous Representation in Metadata

To prevent erasure or misrepresentation, all datasets linked to Indigenous peoples MUST:

1. **Acknowledge communities explicitly** via `community_name` and related fields.  
2. **Avoid generic labels** (“Native American”, “Tribal group”) in place of precise tribal identifiers.  
3. **Use tribally approved place names** when supplied by the community.  
4. **Include community-sourced narratives** when describing culturally relevant events or places (where consented).  
5. **Support Indigenous language fields** in metadata when provided (e.g., place names, descriptors).  

---

## 📜 7. Data Sharing Agreements (DSAs)

All collaborative projects involving Indigenous data MUST use a formal **Data Sharing Agreement (DSA)** template under:

~~~text
docs/data/governance/agreements/
~~~

Each DSA includes:

- Project scope and intended data use  
- Rights of attribution, review, and withdrawal  
- Cultural sensitivity and review requirements  
- FAIR+CARE audit checkpoints  
- Termination clauses for breach or non-compliance  

A JSON-LD summary of each DSA is appended to the **Governance Ledger** for transparency.

---

## 🧾 8. Cultural Sensitivity Checklist

Before publication, each dataset undergoes an Indigenous Data Review using this checklist:

| Criterion                    | Requirement                                                           | Status |
|-----------------------------|-----------------------------------------------------------------------|--------|
| **Cultural Consent Verified** | Formal consent recorded from appropriate authority.                  |        |
| **Community Attribution**    | Community name, language, and review board listed.                   |        |
| **Sensitive Content Screening** | Sacred/ceremonial elements removed or masked as requested.      |        |
| **Ethical Use Statement**    | Dataset description contains CARE-compliant intent and use scope.    |        |
| **Indigenous Language Support** | Metadata includes Indigenous labels where provided.             |        |

All checklist results are stored as governance artifacts and can be inspected in audits.

---

## 🌍 9. Integration with FAIR+CARE & Governance Systems

| Integration                  | Description                                                  | Artifact / Workflow |
|-----------------------------|--------------------------------------------------------------|---------------------|
| **FAIR+CARE Council Review** | Independent review of CARE flags & consent docs            | `faircare-audit.yml` |
| **Governance Ledger Update** | Immutable record of consent approvals/restrictions         | `docs/data/governance/ledger/` |
| **STAC/DCAT Publication Filter** | Ensures restricted datasets are excluded from public catalogs | STAC API / `manifest.zip` |
| **Telemetry Tracking**        | Consent & access flags tracked in governance telemetry      | `docs/data/telemetry/governance-summaries.json` |

---

## ⚙️ 10. Enforcement & Accountability

Violations of this protocol—such as unauthorized use, redistribution, or misattribution—trigger:

1. Immediate **revocation of dataset access** for the offending party or process.  
2. **Council-led investigation** (IDGB + FAIR+CARE Council) and remediation planning.  
3. Required public statement and notation in `review-council-minutes.md`.  
4. Permanent entry in the Governance Ledger describing the incident and resolution.  

Repeated non-compliance may result in **suspension of contributor privileges** under MCP governance.

---

## 🕊️ 11. Collaborative Principles

The Indigenous Data Governance Board (IDGB) commits to:

- Continuous dialogue with tribal representatives and cultural stewards.  
- Shared authorship and credit on datasets involving Indigenous knowledge.  
- Education and outreach promoting ethical data science practices.  
- Prioritization of **community benefit over institutional gain**.  
- Co-design of data products and governance workflows wherever possible.

---

## 🕰️ 12. Version History

| Version | Date       | Author                                          | Summary |
|--------:|------------|-------------------------------------------------|---------|
| v11.2.3 | 2025-11-29 | Indigenous Data Governance Board & FAIR+CARE Council | Upgraded to v11.2.3; added sustainability telemetry v2, explicit STAC/DCAT/PROV-O hooks, H3/sensitivity guidance, and integration with governance ledger and dashboards. |
| v10.0.0 | 2025-11-10 | Indigenous Data Governance Board & FAIR+CARE Council | Established Indigenous Data Governance Protocol, ensuring cultural sovereignty, CARE compliance, and machine-readable consent metadata for all Indigenous datasets. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Governed under **Master Coder Protocol v6.3** · Verified by **Indigenous Data Governance Board** & **FAIR+CARE Council**  

[⬅ Governance Index](README.md) · [🏛 Council Charter](council-charter.md) · [🔓 Data Access Policy](data-access-policy.md)

</div>