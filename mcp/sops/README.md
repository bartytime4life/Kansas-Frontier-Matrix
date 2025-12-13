---
title: "📝 Kansas Frontier Matrix — MCP SOP Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/README.md"

version: "v11.0.0"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & MCP Board"
status: "Active / Enforced"
content_stability: "stable"

doc_kind: "Index"
intent: "mcp-sop-index"
semantic_document_id: "kfm-mcp-sops-index"
doc_uuid: "urn:kfm:mcp:sops:index:v11.0.0"
event_source_id: "ledger:kfm:mcp:sops:index:v11.0.0"
machine_extractable: true
immutability_status: "version-pinned"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

classification: "Public Document"
sensitivity: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Mixed"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
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

provenance_chain:
  - "prov:Plan:urn:kfm:mcp:sops:index:v11.0.0"
---

<div align="center">

# 📝 **Master Coder Protocol — SOP Index (v11 LTS)**
`mcp/sops/README.md`

**Purpose**  
Provide the **canonical index and governance rules** for all Standard Operating Procedures (SOPs) executed under the Master Coder Protocol (MCP-DL v6.3) inside the Kansas Frontier Matrix.

SOPs encode **repeatable, governed processes** for pipelines, AI/ML, geospatial workflows, heritage protection, dataset handling, and narrative generation.

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

In KFM v11, SOPs:
- define how pipelines, tools, AI, and governance processes **must** be executed
- serve as the **blueprint for consistent, reproducible operation**
- are required for any process that touches:
  - 🌦️ climate / downscaling / bias correction
  - 💧 hydrology reconstruction / fusion
  - 📖 Story Node / Focus Mode generation
  - 🪶 heritage protection and H3 masking/generalization
  - 🧠 AI explainability, auditing, and governance checks
  - 🧾 dataset intake, rights, and FAIR+CARE screening
  - 🧬 provenance validation and release attestation

Every SOP is a **controlled artifact**: changes are version-pinned and must pass CI.

### 🧷 Non-negotiables
- deterministic execution instructions (no ambiguity)
- pinned references (datasets, models, contracts, tools)
- explicit governance routing (CARE + sovereignty)
- provenance + telemetry expectations
- validation criteria and failure recovery steps

---

## 🗂️ Directory Layout

~~~text
mcp/sops/
├── README.md                         # 📝 This file — index + rules
├── climate_downscaling.md            # 🌦️ Climate downscaling + bias correction
├── hydrology_reconstruction.md       # 💧 Hydrology time-series reconstruction + fusion
├── storynode_generation.md           # 📖 Story Node v3 generation + narrative governance
├── ai_bias_check.md                  # 🧠 AI bias/fairness/governance evaluation
└── ...                               # ➕ Additional SOPs
~~~

### 🧷 Naming rule
SOP filenames must follow:
~~~text
<domain>_<process>.md
~~~

Examples:
- `climate_downscaling.md`
- `hydrology_reconstruction.md`
- `storynode_generation.md`
- `ai_bias_check.md`

Recommended domains:
- `climate`
- `hydrology`
- `hazard`
- `geo`
- `nlp`
- `ai`
- `storynode`
- `archive`
- `heritage`
- `pipeline`
- `governance`

---

## 🧾 SOP Content Requirements

Each SOP MUST include:

### 🧬 A. Metadata header
At minimum:
- purpose and intent
- governance pointers (ROOT-GOVERNANCE, FAIR+CARE, sovereignty)
- FAIR+CARE labels
- contract version alignment (KFM-PDC v11)
- provenance/telemetry references

### 📥 B. Inputs
- datasets and their STAC/DCAT identifiers (version-pinned)
- model references (model cards, version-pinned) when applicable
- required config files (paths)
- execution environment (container/toolchain expectations)

### 🛠️ C. Procedure (deterministic, step-by-step)
Must be reproducible with:
- explicit steps
- parameterization guidance
- method choices and constraints (what is allowed vs prohibited)
- where intermediates and outputs are written

### ✅ D. Verification
- required validations (schema/SHACL/contract checks)
- acceptance thresholds (or pass/fail gates)
- CI workflows that must pass

### 🧯 E. Failure modes & recovery
- common failures
- safe rerun plan
- rollback/containment guidance
- escalation triggers (FAIR+CARE Council / Sovereignty review)

### 🧬 F. Lineage, telemetry, and observability
Every SOP execution must define where it writes:
- PROV-O JSON-LD bundle
- OpenLineage references (no secrets embedded)
- telemetry entry expectations (energy/carbon/runtime where available)

---

## 🛡️ Governance Requirements

All SOPs must:
- comply with **MCP-DL v6.3**
- comply with **KFM-MDP v11.2.6** document rules
- declare sovereignty constraints and CARE routing
- apply masking/generalization rules when sensitive geographies are involved
- be CI-gated (documentation + governance checks)

If an SOP violates governance requirements, it is **not executable** and must not be merged.

---

## 🔗 Integration With Pipelines & Agents

SOPs drive:
- 🧠 LangGraph v11 DAG pipelines
- 🤖 CrewAI worker behavior (deterministic mode)
- 🧬 Neo4j graph ingestion workflows
- 🧭 Focus Mode v3 context and safety gating
- 📖 Story Node v3 generation and publish routing
- 🌦️ climate/hydrology/hazard runners
- 🗺️ geospatial harmonization and validation tasks

SOPs directly influence:
- data quality and reproducibility
- model performance and safety
- narrative integrity
- sovereignty compliance
- long-term governance auditability

---

## 📊 Telemetry & Observability

SOP execution telemetry aggregates to:
~~~text
releases/<version>/mcp-sops-telemetry.json
~~~

Telemetry captures (when available):
- steps executed and outcomes
- failures and retries
- energy (Wh) and carbon (gCO₂e)
- runtime duration
- hardware profile
- provenance pointers (run IDs, bundle paths)

Used for:
- sustainability dashboards
- governance audits
- reliability scoring
- pipeline tuning and regression detection

---

## 📚 SOP Index

| SOP File | Domain | Purpose | Sensitivity | Status |
|---|---|---|---|---|
| `climate_downscaling.md` | Climate | Downscaling + bias correction workflow | Low | Active / Enforced |
| `hydrology_reconstruction.md` | Hydrology | Time-series reconstruction + multi-source fusion | Mixed | Active / Enforced |
| `storynode_generation.md` | StoryNode | Story Node v3 generation + narrative governance | Mixed | Active / Enforced |
| `ai_bias_check.md` | AI Governance | Bias/fairness/governance evaluation + decision routing | Mixed | Active / Enforced |

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-11-23 | Initial KFM-MCP SOP index for v11 system. |
| v11.0.0 | 2025-12-13 | Updated to KFM-MDP v11.2.6 (directory layout profile, tilde fences, governed header/footer, populated SOP table). |

---

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · KFM-OP v11.0 · KFM-PDC v11.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
