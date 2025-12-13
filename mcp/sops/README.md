---
title: "📝 Kansas Frontier Matrix — MCP SOP Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/README.md"

version: "v11.0.0"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & MCP Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"
intent: "mcp-sop-index"
semantic_document_id: "kfm-mcp-sops-index"
doc_uuid: "urn:kfm:mcp:sops:index:v11.0.0"
event_source_id: "ledger:kfm:mcp:sops:index:v11.0.0"
machine_extractable: true

classification: "Public Document"
sensitivity: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Mixed"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"

telemetry_ref: "../../releases/v11.0.0/mcp-sops-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-sops-v11.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "governance-override"
  - "fabricate-provenance"
  - "inject-secrets"
  - "inject-nonexistent-files"
---

<div align="center">

# 📝 **Master Coder Protocol — SOP Index (v11 LTS)**
`mcp/sops/README.md`

**Purpose**  
Provide the **canonical index and governance rules** for all Standard Operating Procedures (SOPs)
executed under MCP-DL v6.3 in the Kansas Frontier Matrix. SOPs encode **repeatable, deterministic,
governed processes** for pipelines, AI/ML, geospatial workflows, heritage protection, dataset handling,
and narrative generation.

Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence  
Designed for Longevity · Governed for Integrity

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/SOPs-Governed-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange" />
<img src="https://img.shields.io/badge/Sovereignty-Enforced-critical" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧪 MCP Experiments](../experiments/README.md) ·
[🧬 Model Cards](../model_cards/README.md) ·
[🏛️ Governance](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Sovereignty](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

---

## 📘 Overview

### 🧾 What an SOP is in KFM v11
An SOP is a **repeatable, deterministic, fully governed procedure** documented under MCP-DL v6.3.

SOPs are required for any process that:
- produces or modifies derived data products (`data/processed/**`)
- influences Focus Mode or Story Node outputs
- enforces masking/generalization rules
- runs AI inference, alignment, or reconstruction
- emits provenance (PROV-O) and/or OpenLineage references

### 🧷 Naming convention (required)
~~~text
<domain>_<process>.md
~~~

Recommended domains:
- `climate`, `hydrology`, `hazard`, `geo`, `nlp`, `ai`, `storynode`, `archive`, `heritage`, `pipeline`, `governance`

### 📚 SOP index (canonical)
| SOP | File | Sensitivity | Status |
|---|---|---|---|
| 🌦️ Climate Downscaling & Bias Correction | `./climate_downscaling.md` | Low | Active / Enforced |
| 💧 Hydrology Reconstruction & Multi-Source Fusion | `./hydrology_reconstruction.md` | Mixed | Active / Enforced |
| 📖 Story Node v3 Generation & Narrative Governance | `./storynode_generation.md` | Mixed | Active / Enforced |
| 🧠 AI Bias, Fairness & Governance Check | `./ai_bias_check.md` | Mixed | Active / Enforced |

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 mcp/
│   ├── 📁 sops/
│   │   ├── 📄 README.md                                 — 📝 This index (rules + canonical list)
│   │   ├── 📄 climate_downscaling.md                    — 🌦️ Downscaling + bias correction workflow
│   │   ├── 📄 hydrology_reconstruction.md               — 💧 Time-series reconstruction + fusion workflow
│   │   ├── 📄 storynode_generation.md                   — 📖 Story Node v3 generation + narrative governance
│   │   └── 📄 ai_bias_check.md                          — 🧠 Bias/fairness/governance evaluation SOP
│   ├── 📁 experiments/
│   │   └── 📄 README.md                                 — 🧪 Experiment index + rules
│   └── 📁 model_cards/
│       └── 📄 README.md                                 — 🧬 Model card index + rules
└── 📁 releases/
    └── 📁 v11.0.0/
        └── 🧾 mcp-sops-telemetry.json                   — 📊 SOP telemetry aggregation (energy/carbon/runtime)
~~~

---

## 🧭 Context

### ✅ Non-negotiables (governed execution)
Every SOP must:
- be deterministic and replayable (config-driven; seeded where applicable)
- explicitly define inputs/outputs and where artifacts are written
- specify validation gates and acceptance criteria
- define failure modes + safe recovery actions
- route governance and sovereignty issues to the correct review authority
- never include secrets, credentials, or sensitive coordinates in Markdown

### 🔗 Required cross-links
Every SOP must link (at minimum) to:
- the relevant **model card(s)** (`mcp/model_cards/**`) if AI is used
- at least one **experiment log** (`mcp/experiments/**`) if training/evaluation is referenced
- relevant **data contract** (KFM-PDC v11)
- provenance/telemetry output locations

---

## 📦 Data & Metadata

### 🧾 SOP content requirements (normative)
Each SOP MUST include:
- **Purpose** and operational scope
- required inputs (datasets with STAC/DCAT identifiers; models with model cards)
- deterministic step-by-step procedure
- validation checklist and CI expectations
- provenance requirements (PROV-O + OpenLineage references)
- telemetry expectations (energy/carbon/runtime where available)
- failure modes and recovery steps
- FAIR+CARE and sovereignty routing rules

### ♻️ Telemetry requirements (SOP-level)
SOP execution telemetry aggregates to:
~~~text
releases/<version>/mcp-sops-telemetry.json
~~~

Telemetry SHOULD capture (when available):
- runtime duration
- hardware profile
- energy (Wh) and carbon estimate (gCO₂e)
- I/O volume
- provenance pointers (run IDs, bundle paths)

---

## 🧱 Architecture

### 🧰 How SOPs connect to the KFM pipeline
SOPs describe *how work is done* in:
- deterministic ETL and derived dataset creation
- STAC/DCAT packaging and versioning
- Neo4j graph ingestion validation
- Focus Mode and Story Node workflows
- governance gates (CARE tiers + sovereignty review routes)
- CI enforcement (schema + provenance + doc rules)

Minimum interface contract SOPs must state:
- what the procedure consumes (inputs + required metadata)
- what it produces (outputs + expected schemas)
- where provenance and telemetry are written

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[🟢 Start SOP] --> B[📥 Acquire inputs + verify rights]
  B --> C[🧾 Validate contracts + metadata]
  C --> D[⚙️ Execute deterministic steps]
  D --> E[✅ Validate outputs]
  E --> F[🧬 Write provenance (PROV-O + OpenLineage refs)]
  F --> G[📊 Write telemetry]
  G --> H[🚦 CI gates + governance routing]
  H --> I[🏁 Done / publish allowed]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Any SOP that influences Story Nodes or Focus Mode MUST:
- enforce evidence-led outputs (no speculative claims)
- define masking/generalization defaults for sensitive geographies
- require human review for narrative-capable outputs
- prevent coordinate leakage and prohibited inferences (genealogy, sacred-site inference)

---

## 🧪 Validation & CI/CD

### ✅ Minimum CI expectations
SOPs must pass:
- Markdown structure rules (single H1; approved H2 registry; tilde fences)
- front-matter presence checks
- footer governance links presence
- diagram validity (Mermaid parse)
- provenance and telemetry reference checks
- secret/PII scans

### ✅ Minimum “done” definition for an SOP run
An SOP execution is “done” when:
- outputs exist at declared paths
- validation gates pass
- provenance bundle is written and referenced
- telemetry is written or referenced (when applicable)
- governance routing has been satisfied (where triggered)

---

## 🌐 STAC, DCAT & PROV Alignment

SOPs must explicitly state:
- whether outputs are packaged as STAC Items/Collections
- whether DCAT records are emitted or updated
- where PROV-O bundles are written
- what OpenLineage event names are referenced (no embedded tokens)

---

## ⚖ FAIR+CARE & Governance

SOPs must:
- declare CARE posture and sovereignty implications
- enforce masking/generalization requirements when applicable
- define escalation triggers for Tier A / sovereignty-tagged material
- forbid unsafe outputs (sensitive coordinates, harmful narrative framing, unreviewed high-stakes usage)

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-11-23 | Initial MCP SOP index for KFM v11. |
| v11.0.0 | 2025-12-13 | Updated to KFM-MDP v11.2.6 (approved H2 registry + ordering, emoji directory layout, tilde fences, governed header/footer, populated canonical SOP list). |

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
