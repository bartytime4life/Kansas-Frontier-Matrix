---
title: "🪨 Surficial Geology — Raw Source Metadata"
path: "data/surficial-geology/raw/<source_id>/metadata/README.md"

version: "v0.1.0"
last_updated: "2025-12-14"
release_stage: "Draft / In-Progress"
content_stability: "draft"

status: "Active"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"

scope:
  domain: "surficial-geology"
  applies_to:
    - "data/surficial-geology/raw/<source_id>/metadata/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:raw:<source_id>:metadata-readme:v0.1.0"
semantic_document_id: "surficial-geology-raw-<source_id>-metadata-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:raw:<source_id>:metadata-readme:v0.1.0"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-relationship-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🪨 **Surficial Geology — Raw Source Metadata**
`data/surficial-geology/raw/<source_id>/metadata/README.md`

**Purpose**  
Define what belongs in `data/surficial-geology/raw/<source_id>/metadata/`, how upstream metadata is captured safely (no secrets/PII), and how these records support STAC/DCAT/PROV linkage in the KFM pipeline.

</div>

---

## 📘 Overview

This directory contains **source-provided metadata artifacts** for the raw intake identified by `<source_id>`.

Treat files here as:

- **Evidence** of what the provider published (as-received or safely sanitized)
- **Non-derivative** (do not generate “helpful” edits by hand)
- **Input-facing** (used to build catalogs, manifests, and provenance)

### What belongs here

- Provider metadata files (XML/JSON/PDF/HTML) that describe the dataset, schema, update cadence, coverage, and constraints.
- Minimal machine-readable snapshots that make metadata ingestion deterministic (e.g., extracted citation, rights, and field dictionary), as long as they do not introduce claims not present in the source.

### What does not belong here

- The raw data files themselves (store those under `data/surficial-geology/raw/<source_id>/`).
- Any derived transforms (put derived metadata distributions under `data/surficial-geology/outputs/metadata/` instead).
- PII, secrets, tokens, or credentials (CI scans will block them).

---

## 🗂️ Directory Layout

~~~text
📁 metadata/                                              — Source metadata (as-received or sanitized)
├── 📄 README.md                                           — This file (rules + expectations)
├── 🧾 metadata.source.json                                — Minimal machine-readable snapshot (recommended)
├── 🧾 metadata.fgdc.xml                                   — Provider FGDC metadata (if supplied)
├── 🧾 metadata.iso19115.xml                                — Provider ISO 19115/19139 metadata (if supplied)
├── 📄 metadata.provider.pdf                                — Provider metadata PDF (if supplied)
├── 🧾 metadata.citation.csl.json                           — Citation record (optional, derived from source text)
├── 🧾 metadata.rights.constraints.json                     — Rights/constraints summary (no contact PII)
└── 🧾 checksums.sha256                                     — SHA-256 checksums for files in this folder
~~~

Notes:

- File names above are **recommended conventions**; keep provider originals when practical, but prefer stable, predictable names for ingestion.
- If multiple upstream versions exist, include a date token (e.g., `metadata.provider_YYYY-MM-DD.pdf`) and ensure `checksums.sha256` covers all committed files.

---

## 🧭 Context

In the KFM pipeline, this directory supports the “raw intake → governed catalog” handoff:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

Related locations:

- `data/surficial-geology/raw/<source_id>/README.md` — source-level overview for this intake
- `data/surficial-geology/raw/<source_id>/license/` — license and rights evidence
- `data/surficial-geology/lineage/` — run notes, manifests, indexes, and provenance outputs

---

## 📦 Data & Metadata

### Minimum expectation (recommended)

At least one machine-readable metadata snapshot should exist to make cataloging repeatable:

- `metadata.source.json` SHOULD include:
  - source name / publisher
  - source URI(s)
  - retrieval date (UTC date)
  - declared license / rights statement (as text + reference)
  - declared spatial/temporal coverage (if stated)
  - declared update cadence (if stated)
  - checksum inventory for metadata artifacts (or rely on `checksums.sha256`)

### Safe handling rules

- **No PII**: Provider metadata often includes contact names/emails/phone numbers. These MUST NOT be committed.
  - If the upstream file contains contact PII, store a **sanitized** version here and record the redaction decision in lineage notes.
- **No secrets**: API keys, tokens, signed URLs, or credentials must never appear.
- **No invented claims**: If you extract or summarize, keep it strictly grounded in the source and treat it as convenience metadata, not authority.

### Checksums

- Maintain `checksums.sha256` for all committed files in this folder.
- If a metadata file changes, update checksums and ensure lineage/provenance reflects the change.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Source metadata files may be attached as STAC assets (e.g., `roles: ["metadata"]`).
- Prefer keeping STAC records under `data/stac/` and referencing these files by stable repo paths.

### DCAT

- The dataset/source is represented as a DCAT `dcat:Dataset`.
- These metadata files can be distributions (`dcat:Distribution`) of type `text/xml`, `application/json`, or `application/pdf` as appropriate.

### PROV

- Metadata artifacts are `prov:Entity` inputs to ETL/cataloging activities.
- Any sanitized version should be traceable (as `prov:wasDerivedFrom`) from the original, with the original stored only in an approved location if it cannot be committed.

---

## 🧪 Validation & CI/CD

Minimum expectations for this folder to pass CI gates:

- **No PII / no secrets**: passes `pii-scan` and `secret-scan`.
- **Front-matter compliance**: passes `schema-lint` and `metadata-check`.
- **Directory layout compliance**: tree uses `~~~text` and correct glyphs.
- **Checksum integrity**: `checksums.sha256` matches committed files (when present).

---

## ⚖ FAIR+CARE & Governance

Even geologic data can become sensitive when combined with other layers. Follow governance rules:

- If any sovereignty, cultural sensitivity, or restricted-location concerns apply, record the decision and mitigation in lineage notes and catalogs.
- Do not publish precision beyond what is ethically justified and policy-compliant.
- Use the governance and sovereignty references linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial metadata README for raw source intake `<source_id>`: safe capture rules, expected artifacts, and STAC/DCAT/PROV linkage guidance. |

---

<div align="center">

🪨 **Surficial Geology — Raw Source Metadata**  
KFM Data Layer · Raw Intake · Evidence-First Metadata

[📘 Docs Root](../../../../../docs/README.md) ·
[📂 Standards Index](../../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

