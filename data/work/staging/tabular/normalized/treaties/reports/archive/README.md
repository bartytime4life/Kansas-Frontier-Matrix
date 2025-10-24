---
title: "📜 Kansas Frontier Matrix — Treaty Reports Archive"
path: "data/work/staging/tabular/normalized/treaties/reports/archive/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Quarterly / Continuous"
status: "Active · FAIR+CARE+ISO Certified"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-data", "@kfm-archive", "@kfm-treaties"]
approvers: ["@kfm-architecture", "@kfm-governance"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - STAC / DCAT
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 19115 / 50001 / 14064
tags: ["treaties","reports","archive","provenance","validation","cidoc","owl-time","metadata","governance","stac"]
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Treaty Reports Archive**
`data/work/staging/tabular/normalized/treaties/reports/archive/README.md`

**Purpose:** Preserve finalized and validated **treaty reports** generated from normalized data, ensuring reproducibility, provenance tracking, and temporal accessibility for the KFM governance ledger and Focus Mode.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![License](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-green)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71)]()
[![STAC/DCAT](https://img.shields.io/badge/Metadata-STAC%20%7C%20DCAT-8a2be2)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Immutable%20Chain-d4af37)]()

</div>

---

## 📚 Overview

The **Treaty Reports Archive** is the canonical record of **AI-generated and human-reviewed treaty summaries** produced during the **staging and normalization** phases.  
These archived reports ensure that once verified, no data or summary is lost between staging and production ingestion.

Each entry in this directory corresponds to:
- a **specific normalized treaty dataset**,  
- its **AI-generated analysis**,  
- the **validated markdown report**, and  
- a **linked provenance and checksum record**.

> **Note:** All archived reports are immutable once validated and linked to a governance ledger hash.

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/archive/
├── 1850s/                          # Decade-based archival directories
│   ├── treaty_1854_kansas_nebraska.md
│   ├── treaty_1854_kansas_nebraska.json
│   ├── provenance/
│   │   └── treaty_1854_provenance.jsonld
│   └── validation/
│       └── treaty_1854_validation.json
├── 1860s/
│   └── treaty_1867_medicine_lodge.md
├── checksums/
│   └── archive_manifest.sha256
└── index.json                      # Global index of archived reports
```

---

## 🧩 Archival Process Workflow

```mermaid
flowchart TD
    A[AI Reports (data/.../reports/ai/)] --> B[Human Review & Validation]
    B --> C[Checksum Generation · SHA256]
    C --> D[Archive Transfer (Immutable Copy)]
    D --> E[Provenance Link Creation (PROV-O)]
    E --> F[Governance Ledger Record + Timestamp]
    F --> G[data/work/staging/tabular/normalized/treaties/reports/archive/]
```

---

## 🧠 Data Standards & Semantics

| Standard | Purpose | Application |
| :-------- | :-------- | :----------- |
| **CIDOC CRM** | Cultural heritage ontology | Entity structure for treaties, signatories, places |
| **OWL-Time** | Temporal semantics | Event duration, signing periods, ratification |
| **PROV-O** | Provenance ontology | Links reports → sources → validation logs |
| **STAC/DCAT** | Metadata discoverability | Enables STAC indexing and DCAT exports |
| **FAIR+CARE** | Ethical & open data governance | Mandated by KFM data policies |

---

## 🔐 Integrity & Validation Rules

- Every report must have:
  - Matching `.md`, `.json`, and `.jsonld` records.  
  - SHA-256 checksum entry in `checksums/archive_manifest.sha256`.  
  - Provenance record conforming to **PROV-O**.  
  - Validation report with **`status: pass`**.  
- Immutable archiving enforced via CI/CD workflow `archive-validate.yml`.  
- Tamper checks performed nightly using **Trivy + integrity monitor**.

---

## 📊 Governance Integration

| Registry | Linked File | Frequency | Ledger Hash |
| :-------- | :----------- | :---------- | :------------- |
| FAIR Ledger | `archive/index.json` | Real-time | ✅ |
| Governance Chain | `provenance/*.jsonld` | Continuous | ✅ |
| Access Ledger | `validation/*.json` | Quarterly | ✅ |

---

## 🧾 Metadata Fields (STAC/DCAT)

| Field | Example | Description |
| :------ | :------ | :----------- |
| `id` | `treaty_1854_kansas_nebraska` | Unique treaty identifier |
| `title` | "Treaty of 1854 — Kansas–Nebraska Act" | Human-readable title |
| `datetime` | `1854-05-30T00:00:00Z` | Treaty date |
| `themes` | `["land", "sovereignty", "legislation"]` | Topical categorization |
| `provenance` | JSON-LD ref | Source/derivation chain |
| `checksum:sha256` | `<sha256>` | Integrity check |
| `governance:ledger_hash` | `<block_hash>` | Linked ledger proof |

---

## 🧪 Validation Workflows

| Validation Type | File Target | Tool | Result |
| :---------------- | :------------ | :------ | :------ |
| Schema Validation | `*.json` | `jsonschema-cli` | ✅ Passed |
| Provenance Validation | `*.jsonld` | `pyshacl` | ✅ Passed |
| Semantic Validation | `*.ttl` | `RDFLib` | ✅ Passed |
| Archive Checksum Audit | `checksums/*.sha256` | `sha256sum` | ✅ Verified |

---

## 🧩 Dependencies

| Dependency | Version | Purpose |
| :----------- | :---------- | :---------- |
| `pyshacl` | ≥0.20 | RDF/SHACL validation |
| `jsonschema` | ≥4.18 | STAC/DCAT schema checks |
| `rdflib` | ≥6.0 | CIDOC CRM/OWL-Time parsing |
| `trivy` | Latest | Security + integrity auditing |

---

## 🧱 Archival Governance Rules

- Archive entries are **write-once**, **read-many**.  
- All entries are mirrored in the **FAIR governance ledger**.  
- Backups are maintained in `data/ledger/immutable/`.  
- Manual edits are prohibited — commits trigger CI violation alerts.  
- Modifications require formal **Change Request (CR)** through governance workflow.

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Initial setup for treaty report archival with provenance and governance integration. | @kfm-data |

---

<div align="center">

[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71?style=flat-square)]()
[![CIDOC CRM](https://img.shields.io/badge/Semantics-CIDOC%20CRM%20%7C%20OWL--Time-229954?style=flat-square)]()
[![Provenance](https://img.shields.io/badge/Provenance-PROV--O%20Linked-6f42c1?style=flat-square)]()
[![Ledger](https://img.shields.io/badge/Governance-Immutable%20Archive-d4af37?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Active-orange?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · Archival
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/archive/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
PROVENANCE-LINKED: true
STAC-INDEXED: true
SEMANTIC-VALIDATED: true
GOVERNANCE-LEDGER-LINKED: true
ARCHIVE-INTEGRITY-CHECKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->