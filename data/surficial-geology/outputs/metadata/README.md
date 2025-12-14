---
title: "🧾 Surficial Geology — Output Metadata"
path: "data/surficial-geology/outputs/metadata/README.md"

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
    - "data/surficial-geology/outputs/metadata/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:outputs-metadata-readme:v0.1.0"
semantic_document_id: "surficial-geology-outputs-metadata-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:outputs-metadata-readme:v0.1.0"

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

# 🧾 **Surficial Geology — Output Metadata**
`data/surficial-geology/outputs/metadata/README.md`

**Purpose**  
Define what belongs in `outputs/metadata/`, how sidecar metadata is structured and validated, and how it supports STAC/DCAT/PROV linkage for Surficial Geology outputs.

</div>

---

## 📘 Overview

This directory holds **machine-readable sidecar metadata** for artifacts under `data/surficial-geology/outputs/`.

Treat everything under `outputs/metadata/` as:

- **Derived** (generated alongside outputs; not the authoritative source of truth)
- **Deterministic** (re-creatable from tracked inputs + config)
- **Contract-like** (stable names, stable structure, safe for validators and ingestion tooling)

### What belongs here

- Schemas describing output fields and constraints (e.g., attribute dictionaries).
- Manifests describing what was exported, how, and with which parameters.
- Provenance summaries that point back to the producing run and the inputs.

### What does not belong here

- Hand-maintained “documentation” that should live in `docs/`.
- Secrets, API keys, access tokens, personal emails, or any restricted locations.
- One-off metadata patches (fix the pipeline inputs/config and re-generate).

---

## 🗂️ Directory Layout

~~~text
📁 metadata/                                   — Machine-readable sidecars for `outputs/`
├── 📄 README.md                               — This file (conventions + validation rules)
├── 🧾 attributes.schema.json                  — Field dictionary + types + constraints (JSON Schema)
├── 🧾 export.manifest.json                    — Output inventory + checksums + build parameters
└── 🧾 prov.run.json                           — PROV summary for the run that generated the outputs
~~~

Notes:

- Sidecars listed above are **recommended defaults**; pipelines may add more files when governed and schema-stable.
- All files here must be included in the parent `../checksums.sha256` when committed.

---

## 🧭 Context

In the KFM pipeline, `outputs/metadata/` exists to make Surficial Geology exports **discoverable, verifiable, and reproducible**:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

Practically:

- **STAC/DCAT** use these sidecars to describe distributions and schemas.
- **PROV** uses these sidecars to capture lineage and build activity context.
- **Validation tooling** uses these sidecars to confirm schema and inventory integrity.

---

## 📦 Data & Metadata

### `attributes.schema.json`

A schema-style description of the exported dataset’s fields.

Minimum expectations (when present):

- Field names are canonical and match the export exactly.
- Each field includes a type and (when applicable) constraints (enums, ranges, required/optional).
- Any domain-controlled vocabularies are referenced consistently.

### `export.manifest.json`

An inventory of what was produced for a given output version.

Typical contents:

- Output version identifier (the same version token used in filenames).
- List of files (relative paths), sizes, and checksums.
- Build parameters and tool versions that affect determinism.
- References to source manifests/checksums for traceability.

### `prov.run.json`

A compact provenance summary for the run that generated the outputs.

Typical contents:

- Run identifier and pointer to the run record under `mcp/runs/`.
- Inputs used (raw/processed entities) and their checksums/ids where available.
- Output entities generated (the files in `outputs/`) and their linkage to the activity.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Sidecars here are commonly published as STAC assets with roles like `metadata` and `schema`.
- When possible, include checksums for sidecars in both:
  - `../checksums.sha256`
  - STAC asset fields (e.g., `checksum:sha256`)

### DCAT

- Sidecars may be represented as supporting distributions (e.g., schema distributions) when publishing to external catalogs.
- License/rights MUST be inherited from the authoritative source manifest or catalog record (do not guess).

### PROV

- Each sidecar file is a `prov:Entity`.
- The build that generated the outputs is a `prov:Activity`.
- Each entity should link back to its generating activity and (where tracked) the upstream inputs it was derived from.

---

## 🧪 Validation & CI/CD

Minimum expectations for committed metadata:

- **JSON validity**: sidecars parse as valid JSON.
- **Schema lint**: `attributes.schema.json` conforms to the repo’s schema expectations (where provided).
- **Inventory integrity**: `export.manifest.json` matches the actual files in `../` for that version.
- **Checksums**: entries for sidecars exist in `../checksums.sha256` and match file contents.
- **Governance scans**: no secrets, no PII, and no disallowed sensitive precision.

---

## ⚖ FAIR+CARE & Governance

Metadata can become sensitive when it enables inference.

When producing sidecars:

- Avoid including restricted coordinates, sensitive site annotations, or contributor-identifying details.
- Prefer generalized extents and governed identifiers.
- If sovereignty or sensitivity flags apply, record the decision in catalogs (STAC/DCAT) and in provenance (PROV).

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `outputs/metadata/` README defining expected sidecar files, validation rules, and STAC/DCAT/PROV linkage guidance. |

---

<div align="center">

🧾 **Surficial Geology — Output Metadata**  
KFM Data Layer · Deterministic Sidecars · Provenance-First

[📘 Docs Root](../../../../docs/README.md) ·
[📂 Standards Index](../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

