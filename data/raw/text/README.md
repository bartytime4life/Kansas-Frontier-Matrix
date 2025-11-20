---
title: "📜 Kansas Frontier Matrix — Raw Text & Document Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/text/README.md"
version: "v11.0.0"
last_updated: "2025-11-19"
review_cycle: "Continuous / Autonomous · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-text-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0 / Public Domain"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Data Layer"
intent: "text-raw"
fair_category: "F1-A1-I1-R1"
care_label: "Medium—Cultural Material (Ethical Handling Required)"
sensitivity_level: "Contextual"
provenance_chain:
  - "data/sources/khs_text.json"
  - "data/sources/loc_newspapers.json"
  - "data/sources/university_archives.json"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "CreativeWork"
  prov_o: "prov:Entity"
  geo: "GeoSPARQL (if geotagged)"
  stac: "STAC 1.0.0 (extended)"
story_node_refs: []
metadata_profiles:
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "PROV-O"
  - "FAIR+CARE"
doc_uuid: "urn:kfm:data:raw:text:readme:v11"
semantic_document_id: "kfm-data-raw-text"
event_source_id: "ledger:data_raw_text"
immutability_status: "mutable"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with filters"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "provenance-digest"
ai_transform_prohibited:
  - "content-alteration"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public / Cultural"
lifecycle_stage: "active"
ttl_policy: "Persistent Archival"
sunset_policy: "Review annually"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Raw Text & Document Data**  
`data/raw/text/README.md`

**Purpose:**  
Define the **unmodified, provenance-verified textual corpus** powering KFM v11’s NLP, knowledge-graph ingestion, historical modeling, and **Focus Mode v3** narrative generation.  
All assets follow **FAIR+CARE**, **ISO-19115**, **PROV-O**, and **STAC/DCAT** metadata frameworks.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11](https://img.shields.io/badge/KFM–MDP-v11.0.0-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()  
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0_Aligned-0052cc)]()  
[![CIDOC CRM](https://img.shields.io/badge/CIDOC–CRM-E31_Document-brown)]()

</div>

---

# 🧭 Overview

The **Raw Text Layer** contains **primary-source Kansas materials**:

- Scanned manuscripts  
- Treaties, legal records, field notes  
- OCR’d historical newspapers  
- Oral history transcripts  
- Geological and agricultural reports  
- Cultural heritage materials (ethically reviewed)

Nothing in this directory is altered.  
All transformations occur in:

```

data/work/staging/text/
data/processed/text/

```

v11 introduces:

- **Story Node v3 hooks** (text→narrative linkage)  
- **Focus Mode v3 context embeddings**  
- **Extended provenance chains (PROV-O: activity/agent/entity)**  
- **Semantic risk tagging** for culturally sensitive content  
- **Text integrity hashing (SHA-256 + size + mime)**  

---

# 🗂️ Directory Layout

```

data/raw/text/
├── README.md
├── kansas_treaties_1800s.pdf
├── newspapers_1854_1950.zip
├── oral_histories.json
├── geological_reports.txt
├── agricultural_bulletins.csv
├── metadata.json                # Provenance, checksums, OCR/encoding metadata
└── source_licenses.json         # License and attribution registry

````

---

# 📚 Data Acquisition & Provenance Summary

| Dataset | Source | Format | License | CARE Notes | Integrity |
|--------|--------|--------|----------|-------------|-----------|
| Kansas Treaties | KHS / NARA | PDF | CC-BY 4.0 | Requires contextual handling | ✔ |
| Historic Newspapers | LOC Chronicling America | ZIP/TXT | Public Domain | Minimal sensitivity | ✔ |
| Oral Histories | KU Oral History Project | JSON | CC-BY 4.0 | Potential cultural sensitivity | ✔ |
| Geological Surveys | Kansas Geological Survey | TXT | Public Domain | None | ✔ |
| Agriculture Bulletins | USDA / K-State Extension | CSV | Public Domain | None | ✔ |

---

# 🧩 Example v11 Metadata Record (DCAT + STAC + PROV-O Hybrid)

```json
{
  "id": "kfm_raw_text_treaties_1800s",
  "type": "Document",
  "conformsTo": ["DCAT-3.0", "STAC-1.0.0", "PROV-O"],
  "providers": [
    {
      "name": "Kansas Historical Society",
      "roles": ["producer", "licensor"],
      "url": "https://www.kshs.org/"
    }
  ],
  "assets": {
    "source": {
      "href": "https://kshs.org/research/collections/treaties",
      "type": "application/pdf",
      "checksum:sha256": "a17f92e37bd8f2d54...",
      "size": 18499224
    }
  },
  "temporal": { "start": "1800-01-01", "end": "1899-12-31" },
  "provenance": {
    "prov:wasGeneratedBy": "digitization_batch_khs_2025",
    "prov:wasAttributedTo": "Kansas Historical Society",
    "prov:generatedAtTime": "2025-11-12T20:35:00Z"
  },
  "text_quality": {
    "ocr_engine": "Tesseract 5.3",
    "character_accuracy": 0.984
  },
  "care_flags": ["contextual_cultural_material"],
  "governance_ref": "docs/standards/governance/ROOT-GOVERNANCE.md"
}
````

---

# ⚖️ FAIR+CARE Compliance Matrix

| Axis                 | Implementation                             | Oversight            |
| -------------------- | ------------------------------------------ | -------------------- |
| Findable             | STAC/DCAT indexes + persistent identifiers | `@kfm-data`          |
| Accessible           | Open formats + accessibility metadata      | `@kfm-accessibility` |
| Interoperable        | Schema.org, CIDOC, DCAT, ALTO/METS         | `@kfm-architecture`  |
| Reusable             | Complete provenance + licensing            | `@kfm-governance`    |
| Collective Benefit   | Community-beneficial openness              | FAIR+CARE Council    |
| Authority to Control | Tribal/Community protocols applied         | Ethics Board         |
| Responsibility       | Proper handling of cultural materials      | Data Stewards        |
| Ethics               | Sensitivity tagging + access review        | FAIR+CARE Council    |

---

# 🧠 Integrity & Audit Pipelines

| Step              | Description                    | Output                      |
| ----------------- | ------------------------------ | --------------------------- |
| Checksum Verify   | SHA-256, size, mime validation | `metadata.json`             |
| License Audit     | Verified reuse permissions     | `source_licenses.json`      |
| OCR Audit         | CER/WER, engine version logged | ETL audit logs              |
| Story Node Hooks  | Text→narrative candidates      | `storynode_candidates.json` |
| STAC Registration | Dataset-level Item creation    | `stac/collections/text/`    |

---

# 🕰️ Retention & Sustainability

| Category       | Retention | Policy                      |
| -------------- | --------- | --------------------------- |
| Raw Text       | Permanent | Immutable archival layer    |
| Metadata       | Permanent | Required for provenance     |
| OCR Stats      | 10 years  | AI transparency requirement |
| Ethics Reviews | 10 years  | Required by CARE protocol   |

---

# 🧾 Internal Citation (v11)

```
Kansas Frontier Matrix (2025). Raw Text & Document Data (v11.0.0).  
Unaltered Kansas archival documents spanning treaties, newspapers, oral histories, and technical bulletins.  
Checksum-verified, FAIR+CARE aligned, and governed under MCP-DL v6.3 and KFM-MDP v11.
```

---

# 🔄 Version History

| Version | Date       | Author          | Summary                                                                                        |
| ------- | ---------- | --------------- | ---------------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-19 | Lead Programmer | Full KFM-MDP v11 upgrade, STAC/DCAT/PROV-O alignment, Focus Mode v3 hooks, ethics-risk tagging |
| v10.2.2 | 2025-11-12 | `@kfm-text`     | Streaming STAC + telemetry v2                                                                  |
| v10.0.0 | 2025-11-09 | `@kfm-text`     | OCR audit + governance linking                                                                 |

---

<div align="center">

**Kansas Frontier Matrix — Raw Text Data Layer**
📜 *Authenticity preserved. Provenance guaranteed. Ethics enforced.*

[⬅️ Back to Raw Data Index](../README.md) •
[📐 Data Architecture](../../../docs/architecture/system_overview.md) •
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
