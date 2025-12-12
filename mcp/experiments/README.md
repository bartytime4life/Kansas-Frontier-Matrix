---
title: "🧪 Kansas Frontier Matrix — MCP Experiments Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/experiments/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & MCP Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"
intent: "mcp-experiment-index"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../releases/v11.2.6/mcp-experiments-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-experiments-v11.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

semantic_document_id: "kfm-mcp-experiments-index"
event_source_id: "ledger:kfm:mcp:experiments:index:v11.2.6"
doc_uuid: "urn:kfm:mcp:experiments:index:v11.2.6"

machine_extractable: true
classification: "Public"
sensitivity: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Mixed"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"

ai_transform_permissions:
  - "summarization"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"
  - "provenance-fabrication"

provenance_chain:
  - "urn:kfm:mcp:experiments:index:v11.0.0"
  - "urn:kfm:mcp:experiments:index:v11.2.6"
---

<div align="center">

# 🧪 **MCP Experiments — Official Index (v11 LTS)**  
`mcp/experiments/README.md`

**Purpose**  
Provide the **canonical index and ruleset** for all experiments executed under the Kansas Frontier Matrix Master Coder Protocol (MCP‑DL v6.3).  
This directory forms the **scientific and computational backbone** of KFM v11: every climate run, hydrology reconstruction, geospatial inference, narrative validation, and AI/ML model is documented here with **full provenance, reproducibility, and governance metadata.**

</div>

---

## 📘 Overview

### What counts as an experiment?

Any activity that produces **new information**, **processed data**, **trained models**, **derived spatial/temporal layers**, or **AI-generated narrative components** must be logged as an MCP experiment.

This includes (non-exhaustive):

- Climate anomaly calculations
- Hydrology reconstruction (1900 → 2100)
- ETL harmonization experiments
- Geospatial alignment / vertical datum conversions
- H3 generalization tuning (heritage masking trials)
- Story Node generation tests
- Explainability studies (SHAP/LIME overlays)
- NLP over newspapers / archives
- Any model training or re-training
- CrewAI or LangGraph agent-driven transformations

If a dataset or narrative **changes because of your code**, it must be reproducible and therefore must be logged.

### Index of experiments

This table is intended to be **auto-generated friendly** (or maintained manually when needed).

| Experiment ID | Title | Domain | Date | Status |
|--------------:|-------|--------|------|--------|
| _None yet_ | — | — | — | — |

---

## 🗂️ Directory Layout

~~~text
📁 mcp/
└── 📁 experiments/                              — MCP experiment logs (timestamped)
    ├── 📄 README.md                             — Canonical index + rules (this file)
    ├── 📄 2025-11-01_CLIMATE-EXP-001.md          — Climate anomaly reconstruction experiment
    ├── 📄 2025-11-02_HYDRO-EXP-002.md            — Hydrology temporal smoothing experiment
    ├── 📄 2025-11-05_AI-EXP-003.md               — Story Node v3 generation trial
    ├── 📄 2025-11-12_AI-EXP-004.md               — CrewAI harmonization test
    └── 📄 YYYY-MM-DD_<DOMAIN>-EXP-###.md         — Additional experiments (required format)
~~~

### Filename convention

All experiment filenames MUST follow:

~~~text
YYYY-MM-DD_<DOMAIN>-EXP-###.md
~~~

### Domain codes

Domains may include:

- CLIMATE
- HYDRO
- GEO
- AI
- NLP
- ARCH
- HAZARD
- STORY
- PIPELINE

---

## 🧭 Context

### Where experiment artifacts live

- Source intake manifests and checksums: `data/sources/`
- Derived artifacts: `data/processed/` (or a clearly named subfolder)
- Run logs / config snapshots / seeds: `mcp/runs/`
- Lineage outputs: `data/provenance/experiments/`

### Determinism requirement

Experiments MUST be config-driven, replayable, and deterministic where possible. If randomness is used, record **seed values** and all non-default parameters in the experiment log.

---

## 🧠 Story Node & Focus Mode Integration

Experiments that generate or modify Story Nodes must:

- Separate **facts**, **interpretation**, and **speculation**
- Preserve **evidence links** back to source datasets/documents
- Respect sovereignty rules (mask/generalize sensitive locations by default)

---

## 🧪 Validation & CI/CD

Markdown and experiment compliance is CI-enforced.

Minimum expectations for this directory:

- Filename pattern enforcement (`YYYY-MM-DD_<DOMAIN>-EXP-###.md`)
- KFM-MDP v11.2.6 Markdown rules (single H1; approved H2s; tilde-fenced blocks)
- Required experiment metadata presence (IDs, versions, seeds, environment)
- Provenance completeness (PROV-O + OpenLineage + checksums)
- No prohibited coordinate exposure / PII / secrets

---

## 📦 Data & Metadata

### Required structure for each experiment log (MCP-DL v6.3)

Each experiment MUST contain:

- Metadata header (Experiment ID; date; authors/agents; dataset versions; model versions; seed values; hardware/environment; contract version; CARE classification)
- Objective / hypothesis
- Background (prior work, citations, linked documents; STAC/DCAT references)
- Methods (full reproducibility: steps; parameters; code refs; config files; seeds; inputs/transformations)
- Execution log (actual run logs; errors/retries; pipeline steps; OpenLineage event IDs)
- Results (tables; graphs; maps; derived datasets; metrics)
- Analysis (interpretation; uncertainty; ethical/CARE considerations)
- Limitations
- Next steps
- Provenance block (PROV-O JSON-LD + OpenLineage v2.5 metadata + output checksums)

### Telemetry & sustainability

Each experiment is measured for:

- Execution duration
- Energy (Wh)
- Carbon (gCO₂e)
- IO and memory usage

Telemetry is written to:

~~~text
releases/<version>/mcp-experiments-telemetry.json
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Experiments that produce artifacts MUST:

- Emit **STAC Items** for spatial datasets (or `geometry: null` for non-spatial artifacts)
- Emit **DCAT** dataset records for publishable outputs
- Emit **PROV-O** lineage linking raw → processed → derived outputs and the activity/run that generated them

Lineage is stored in:

~~~text
data/provenance/experiments/
~~~

Experiments lacking lineage **do not pass CI**.

---

## ⚖ FAIR+CARE & Governance

All experiments must:

- Annotate CARE status appropriately
- Avoid sensitive heritage coordinates
- Use H3 masking/generalization for archaeological/cultural locations
- Document any potentially sensitive outputs
- Request FAIR+CARE Council review where required (Tier A datasets; cultural sensitivity; hazard projections)

Ethics notes are required for:

- AI narrative generation
- Cultural datasets
- Sensitive historical records
- Climate/hazard projections

---

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| **v11.2.6** | 2025-12-12 | Updated to KFM‑MDP v11.2.6 compliance (approved H2s + ordering; `~~~` fences; required front‑matter keys; governance links in footer). |
| v11.0.0 | 2025-11-23 | Initial MCP experiments index for KFM v11. |

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

</div>
