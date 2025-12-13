---
title: "🧬 Kansas Frontier Matrix — MCP Model Cards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/README.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · MCP Board · FAIR+CARE Council · AI Governance Team"
commit_sha: "<latest-commit-hash>"
signature_ref: "../../releases/v11.0.0/signature.sig"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/mcp-modelcards-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-modelcards-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active / Enforced"
doc_kind: "Index"
intent: "mcp-model-card-index"
semantic_document_id: "kfm-mcp-modelcards-index"
doc_uuid: "urn:kfm:mcp:modelcards:index:v11.0.0"
event_source_id: "ledger:kfm:mcp:modelcards:index:v11.0.0"
machine_extractable: true
classification: "Governed AI Document"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R2"
care_label: "Collective Benefit · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "alter-normative-requirements"
  - "invent-governance-status"
  - "fabricate-provenance"
  - "introduce-novel-facts"
provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"
  - "docs/standards/kfm_markdown_protocol_v11.md@v11.0.1"
  - "docs/standards/markdown_rules.md@v10.4.3"
---

<div align="center">

# 🧬 **Master Coder Protocol — Model Cards Index (v11 LTS)**
`mcp/model_cards/README.md`

**Purpose**  
Provide the canonical, governed index for all AI/ML **Model Cards** used in the Kansas Frontier Matrix (KFM).
Model Cards are mandatory documentation artifacts defining intended use, training data, evaluation, limitations,
governance boundaries, provenance, and sustainability telemetry for every model used in pipelines, Focus Mode,
and Story Node workflows.

</div>

---

## 📘 Overview

### What a Model Card is in KFM
A Model Card is the **authoritative contract** for a model’s:
- intended use and prohibited use
- training data inputs (STAC/DCAT identifiers)
- evaluation and validation results
- known limitations and failure modes
- governance boundaries (FAIR+CARE + sovereignty constraints)
- provenance evidence (PROV‑O + OpenLineage references)
- sustainability telemetry (energy + carbon)

### When a Model Card is required
A Model Card is required for any model that:
- produces predictions or reconstructions
- runs inference inside ETL/pipeline steps
- supports Focus Mode or Story Node generation
- performs alignment, interpolation, imputation, or harmonization
- participates in CrewAI/LangGraph deterministic executors

### Naming rules
Model card filenames must follow:
- `<model_slug>_v<version>.md`

Downstream pipelines MUST reference:
- the **model card path** and **card version**
- not just the model artifact version

### Current Model Card Index

| Model Card | Version | Domain | CARE Label | Status |
|---|---|---|---|---|
| `climate_anomaly_net_v3.md` | v3 | Climate anomaly reconstruction | Responsible · Ethics · Stewardship | Active / Enforced |
| `hydrology_seq2seq_v11.md` | v11 | Hydrology reconstruction (seq2seq) | Collective Benefit · Responsibility · Ethics | Active / Enforced |
| `focus_mode_transformer_v3.md` | v3 | Governed narrative reasoning | Collective Benefit · Authority to Control · Responsibility · Ethics | Active / Enforced |
| `geo_alignment_net_v4.md` | v4 | Geospatial alignment & harmonization | Collective Benefit · Ethics · Responsibility | Active / Enforced |

---

## 🗂️ Directory Layout

~~~text
mcp/model_cards/
│
├── README.md                           # 🧬 Canonical index + governance rules for model cards
├── climate_anomaly_net_v3.md           # 🌡️ Climate anomaly reconstruction (CAN‑v3)
├── hydrology_seq2seq_v11.md            # 💧 Hydrology reconstruction (HS2S‑v11)
├── focus_mode_transformer_v3.md        # 🧠 Governed narrative reasoning engine (FMT‑v3)
├── geo_alignment_net_v4.md             # 🗺️ Geospatial alignment & harmonization (GAN‑v4)
└── (add new model cards here)          # ➕ One file per model + version
~~~

---

## 🧭 Context

### Why this index exists
This index is the stable entry point for:
- audit trails (governance + provenance)
- deterministic pipeline references (contracts and configs)
- model lifecycle reviews (quarterly governance cadence)
- sustainability reporting (energy/carbon tracking)

### Relationship to MCP experiments
Every model card MUST point to:
- at least one `mcp/experiments/*` record that documents training, evaluation, or deployment validation
- reproducibility controls (seeds, environment, SBOM, and provenance outputs)

---

## 🧱 Architecture

### Where model cards sit in the KFM pipeline
Model cards are documentation entities that bind together:
- ETL outputs (data/processed/*)
- catalogs (STAC/DCAT records)
- graph representations (Neo4j nodes/edges)
- API contract expectations
- UI/Story Node/Focus Mode consumption boundaries

### Interface contract (minimum)
All model cards MUST clearly declare:
- what the model consumes (inputs + required metadata)
- what the model produces (outputs + expected schemas)
- where provenance and telemetry are written

---

## 📦 Data & Metadata

### Front-matter requirements (normative)
Each governed model card MUST include:
- identity: `title`, `path`, `version`, `last_updated`
- governance: `governance_ref`, `ethics_ref`, `sovereignty_policy`
- compliance: `license`, `classification`, `sensitivity`, `fair_category`, `care_label`
- provenance: `commit_sha`, `signature_ref` (when release-pinned), `provenance_chain`
- IDs: `doc_uuid`, `semantic_document_id`, `event_source_id`
- AI transform limits: `ai_transform_permissions`, `ai_transform_prohibited`

### Required declarations inside the body
Each model card MUST clearly state:
- intended use vs restricted use
- limitations and failure modes
- governance boundaries and required human review points
- the experiment(s) and datasets underpinning the model
- sustainability telemetry reference(s)

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT mapping (documentation entity)
Model cards are documentation distributions suitable for DCAT cataloging:
- `semantic_document_id` maps to `dct:identifier`
- the markdown file is a `dcat:Distribution` (`mediaType: text/markdown`)

### STAC representation (optional but supported)
A model card may be represented as a non-spatial STAC Item:
- `geometry: null`
- `properties.datetime = last_updated`
- `assets.markdown.href` points to the repo path

### PROV‑O linkage (required via references)
Model cards MUST reference:
- training/evaluation activities (`prov:Activity`)
- input datasets/entities (`prov:Entity`)
- responsible agents (teams/services) (`prov:Agent`)
- OpenLineage event locations for traceability

---

## 🧪 Validation & CI/CD

### Minimum validation profiles
Model card Markdown is CI-enforced for:
- structure (H1/H2 rules)
- YAML schema compliance
- required metadata presence
- footer governance links and ordering
- accessibility checks
- provenance chain consistency
- secret and PII scanning

### Common failure causes
- missing or malformed front-matter
- more than one H1
- unapproved H2 headings (emoji/text mismatch)
- directory layouts not fenced with `~~~text`
- mixed fence styles inside files
- footer missing governance links

---

## 🧠 Story Node & Focus Mode Integration

### Narrative-facing models
Any model that influences Story Node or Focus Mode narrative output MUST state:
- what the model is allowed to claim
- what the model must never claim (no speculation, no invented provenance)
- masking rules (H3-based generalization when required)
- required human review gates before publication

### Non-narrative models
Models that only produce numeric/geospatial layers MUST still define:
- output constraints (precision, masking, aggregation)
- downstream usage boundaries for narrative systems

---

## ⚖ FAIR+CARE & Governance

### Required governance signals
Every model card must declare:
- FAIR category
- CARE label
- sovereignty implications (including required masking / approvals)
- whether the model may interact with restricted datasets (and under what conditions)

### Release posture
Version-pinned model cards are treated as governed artifacts:
- provenance and telemetry references must be stable
- updates require governance review per review_cycle

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-11-23 | Initial MCP model cards index for KFM v11. |

---

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MCP‑DL v6.3 · CC‑BY 4.0

</div>
