---
title: "🧬 Kansas Frontier Matrix — Master Coder Protocol Workspace (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/README.md"

version: "v11.2.2"
last_updated: "2025-12-13"
review_cycle: "Annual · FAIR+CARE Council & Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-mcp-root"
doc_uuid: "urn:kfm:mcp:readme:v11.2.2"
event_source_id: "ledger:mcp/README.md"
immutability_status: "version-pinned"

sbom_ref: "../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../releases/v11.2.2/manifest.zip"
telemetry_ref: "../releases/v11.2.2/mcp-telemetry.json"
telemetry_schema: "../schemas/telemetry/mcp-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Workspace Overview"
intent: "mcp-workspace-overview"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public Document"
sensitivity: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Mixed"
jurisdiction: "Kansas / United States"

header_profile: "standard"
footer_profile: "standard"

ai_transform_permissions:
  allowed:
    - "summary"
    - "semantic-highlighting"
    - "metadata-extraction"
    - "layout-normalization"
    - "a11y-adaptations"
  prohibited:
    - "speculative-additions"
    - "fabricate-provenance"
    - "invent-governance-status"
    - "inject-secrets"
    - "inject-nonexistent-files"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Master Coder Protocol Workspace (v11)**
`mcp/README.md`

**Purpose**  
Define the **workspace, workflow, and governance rules** for all Master Coder Protocol (MCP)
artifacts in KFM v11 — experiments, SOPs, model cards, lineage bundles, and reproducibility assets.

Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence  
Designed for Longevity · Governed for Integrity

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧪 Experiments](./experiments/README.md) ·
[📝 SOPs](./sops/README.md) ·
[🧾 Model Cards](./model_cards/README.md) ·
[🏛️ Governance](../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE](../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Sovereignty](../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

---

## 📘 Overview

### 1. What “MCP” means in KFM v11
The **Master Coder Protocol (MCP-DL v6.3)** is KFM’s **documentation-first, experiment-first,
reproducibility-first** governance layer for scientific, analytical, and AI/ML work.

The MCP workspace (`mcp/`) exists to ensure every computational result is:
- **reproducible** (config-driven; deterministic/seeded where applicable)
- **auditable** (clear inputs/outputs; explicit validation gates)
- **governed** (FAIR+CARE + sovereignty constraints are explicit)
- **traceable** (PROV-O + OpenLineage references; release artifacts are versioned)

### 2. What lives in `mcp/`
The MCP workspace contains:
- 🧪 **Experiments** — deterministic scientific/ML runs and evaluations
- 📝 **SOPs** — governed Standard Operating Procedures for recurring workflows
- 🧾 **Model Cards** — transparency documentation for AI/ML models and their limits
- 🔗 **Provenance references** — PROV-O and OpenLineage linkouts to run bundles
- 📊 **Telemetry references** — energy/carbon/runtime metadata for governance and sustainability

### 3. Read-first entry points
- 🧪 `mcp/experiments/README.md`
- 📝 `mcp/sops/README.md`
- 🧾 `mcp/model_cards/README.md`

---

## 🗂 Directory Layout

### 1. MCP workspace structure (Emoji Style A)
~~~text
mcp/
├── 📄 README.md                           — 🧬 This document (workspace overview)
│
├── 🧪 experiments/                        — 🧪 Experiment logs (MCP-DL v6.3 governed)
│   ├── 📄 README.md                       — 🧪 Experiments index + rules
│   ├── 📄 2025-11-01_CLIMATE-EXP-001.md    — Example experiment (seeded, reproducible)
│   ├── 📄 2025-11-02_HYDRO-EXP-002.md      — Example experiment (fusion validation)
│   ├── 📄 2025-11-05_AI-EXP-003.md         — Example experiment (Story Node trial)
│   └── 📄 ...                              — Timestamped, domain-tagged experiments
│
├── 📝 sops/                               — 📝 Standard Operating Procedures
│   ├── 📄 README.md                       — 📝 SOP index + rules
│   ├── 📄 climate_downscaling.md           — Climate downscaling + bias correction
│   ├── 📄 hydrology_reconstruction.md      — Hydrology reconstruction + multi-source fusion
│   ├── 📄 storynode_generation.md          — Story Node v3 generation + narrative governance
│   └── 📄 ai_bias_check.md                 — AI bias/fairness/governance evaluation
│
├── 🧾 model_cards/                        — 🧾 AI/ML model documentation + boundaries
│   ├── 📄 README.md                       — 🧾 Model card index + rules
│   ├── 📄 climate_anomaly_net_v3.md        — Climate anomaly reconstruction model card
│   ├── 📄 hydrology_seq2seq_v11.md         — Hydrology reconstruction model card
│   ├── 📄 focus_mode_transformer_v3.md     — Governed narrative model card
│   ├── 📄 geo_alignment_net_v4.md          — Geospatial alignment model card
│   └── 📄 ...                              — Additional model cards
│
└── 📄 MCP-README.md                       — MCP-DL v6.3 protocol reference (“MCP bible”)
~~~

### 2. Directory layout rules (normative)
- directory trees MUST be fenced with `~~~text`
- use `📁` for directories and `📄` for files (emoji-enhanced layouts are allowed)
- keep comments aligned for scanability
- keep naming deterministic and index-friendly

---

## 🧭 Context

### 1. MCP in the KFM pipeline
MCP sits across the KFM pipeline as the governed documentation layer:

ETL → catalogs (STAC/DCAT/PROV) → graph → API → frontend → Story Nodes → Focus Mode

If MCP documents drift or become ambiguous, downstream outputs become unsafe or non-reproducible.

### 2. Non-negotiables (normative)
MCP artifacts MUST:
- declare inputs and outputs (paths, formats, identifiers)
- be deterministic and replayable (config-driven; seeded where applicable)
- include governance routing (FAIR+CARE + sovereignty)
- avoid secrets, credentials, and sensitive coordinates in Markdown
- use version-pinned references when pointing into releases (`releases/<version>/...`)

---

## 🧱 Architecture

### 1. Artifact types and contracts
- 🧪 **Experiment**: a reproducible run that generates new information or derived artifacts
- 📝 **SOP**: a deterministic procedure that can be executed and validated repeatedly
- 🧾 **Model Card**: documentation of model purpose, training/evaluation, risks, and boundaries

### 2. Expected interfaces (normative)
- SOPs define *how* to run.
- Experiments define *what was run* and *what changed*.
- Model Cards define *what a model is allowed to do* and *what it must not do*.

### 3. Where outputs go (normative defaults)
- derived artifacts: `data/processed/**`
- provenance bundles: `data/provenance/**`
- catalogs: `data/stac/**` and DCAT-compatible records (per KFM-DCAT profile)
- release packaging: `releases/<version>/**` (manifest, SBOM, telemetry snapshots)

---

## 📦 Data & Metadata

### 1. Required metadata (normative)
MCP documents MUST reference:
- KFM-PDC contract version (`KFM-PDC v11.0`)
- dataset identifiers (STAC/DCAT IDs or internal dataset IDs)
- model versions + model card references when AI/ML is used
- configuration pointers (paths) and reproducibility seeds (where applicable)

### 2. Telemetry (workspace-level)
MCP-level telemetry aggregates to:
~~~text
../releases/<version>/mcp-telemetry.json
~~~

Telemetry SHOULD include (when available):
- runtime duration
- hardware profile
- energy (Wh) and carbon estimate (gCO₂e)
- I/O volume
- provenance references (run IDs, bundle paths)

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. Catalog outputs
Where MCP activities generate datasets (especially spatial/temporal layers), outputs SHOULD be:
- registered as STAC Items/Collections where applicable
- mapped to DCAT-compatible dataset records for publishing/discovery

### 2. Provenance alignment (normative)
All MCP-controlled pipelines SHOULD emit:
- PROV-O fragments (Activity/Entity/Agent)
- OpenLineage references (job/run + input/output datasets)

MCP documents MUST include stable identifiers to connect:
- experiment → derived dataset → graph ingestion → narrative usage

---

## 🧪 Validation & CI/CD

### 1. CI enforcement (normative)
MCP content is expected to be CI-enforced for:
- KFM-MDP compliance (front-matter, heading registry, fence rules)
- schema validation (experiment/model card/SOP schemas where defined)
- provenance presence (no orphan artifacts)
- governance checks (FAIR+CARE and sovereignty flags where applicable)
- secret/PII scans

### 2. Workflow naming
CI workflow names and locations may vary by repo, but commonly live under:
~~~text
.github/workflows/
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Node v3
Story Nodes that reference scientific conclusions MUST:
- cite the relevant experiment (`mcp/experiments/**`)
- reference model cards when AI is involved
- preserve spatial/temporal grounding and provenance pointers
- respect masking/generalization requirements for sensitive geographies

### 2. Focus Mode v3
Focus Mode may use MCP artifacts to:
- provide grounded context (climate/hydrology/hazard)
- link to model cards for transparency
- surface provenance traces and validation outcomes

---

## 🗺 Diagrams

### 1. MCP artifact flow (workspace view)
~~~mermaid
flowchart TD
  A["Start work"] --> B["Follow an SOP"]
  B --> C["Run an experiment"]
  C --> D["Write outputs to data/processed"]
  D --> E["Write provenance to data/provenance"]
  E --> F["Register STAC/DCAT where applicable"]
  F --> G["Package release artifacts"]
  G --> H["Integrate into Story Nodes and Focus Mode"]
~~~

This diagram summarizes the expected lifecycle from governed procedure → reproducible run →
derived outputs → provenance → cataloging → release packaging → narrative integration.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR+CARE requirements (normative)
All MCP work MUST:
- declare FAIR+CARE posture and constraints
- avoid harmful narrative framing when outputs feed story/narrative layers
- ensure data rights and stewardship are respected

### 2. Sovereignty requirements (normative)
- do not publish sensitive locations or restricted knowledge in Markdown
- apply masking/generalization defaults for sensitive geographies
- escalate Tier A or sovereignty-flagged work to the appropriate review authority

---

## 🕰 Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.2 | 2025-12-13 | Aligned to KFM-MDP v11.2.6 (approved H2 registry, ordering, tilde fences, diagram safety, normalized identifiers). |
| v11.2.2 | 2025-11-27 | Stable / governed workspace overview; clarified CI enforcement & sustainability telemetry; emoji directory layout. |
| v11.0.0 | 2025-11-23 | Initial MCP workspace overview for KFM v11; defined experiments, SOPs, model cards, and lineage rules. |

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
🧬 Master Coder Protocol Workspace · MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

[⬅️ Back to Root](../README.md) ·
[📘 MCP Protocol](MCP-README.md) ·
[🏛️ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
