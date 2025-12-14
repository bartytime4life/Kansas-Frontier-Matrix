---
title: "🧩 Kansas Frontier Matrix — Model Cards (Attestable, SBOM/Tel linked)"
path: "mcp/model_cards/README.md"
version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · MCP Board · FAIR+CARE Council · Reliability Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard + Index + How‑To"
header_profile: "standard"
footer_profile: "standard"
intent: "mcp-model-card-index"
semantic_document_id: "kfm-mcp-modelcards-index"
doc_uuid: "urn:kfm:mcp:modelcards:index:v11.2.6"
event_source_id: "urn:kfm:mcp:modelcards:index:v11.2.6"

machine_extractable: true
classification: "Governed AI Document"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R2"
care_label: "Collective Benefit · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"

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

telemetry_ref: "../../releases/v11.2.6/mcp-modelcards-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-modelcards-v11.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summarize"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "fabricate-model-claims"
  - "fabricate-provenance"
  - "invent-dataset-ids"
  - "invent-license-rights"
  - "override-governance"
  - "expose-sensitive-coordinates"
  - "deanonymize"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Model Cards (v11 LTS)**
`mcp/model_cards/README.md`

**Purpose**  
Provide the **governed, reproducible, FAIR+CARE + sovereignty-aligned index** and **enforceable authoring rules**
for all AI/ML **Model Cards** used inside the Kansas Frontier Matrix (KFM).

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧪 MCP Experiments Index](../experiments/README.md) ·
[📈 Model Cards Telemetry](../../releases/v11.2.6/mcp-modelcards-telemetry.json) ·
[🧾 Telemetry Schema](../../schemas/telemetry/mcp-modelcards-v11.json) ·
[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

---

## 📘 Overview

### ✅ What a Model Card is in KFM
A Model Card is the authoritative, governed contract for a model’s:

- 🎯 Intended use and prohibited use
- 🧪 Training and evaluation inputs (STAC/DCAT identifiers where applicable)
- 📊 Evaluation results and validation methodology
- ⚠️ Limitations, failure modes, and required human oversight
- 🛡️ Governance boundaries (FAIR+CARE + sovereignty constraints)
- 🧾 Provenance evidence (PROV-O + OpenLineage references + checksums)
- ♻️ Sustainability telemetry (energy + carbon) when tracked

### ✅ When a Model Card is required
A Model Card is required for any model that:

- 🧠 Produces predictions, reconstructions, or alignments
- ⚙️ Runs inference inside ETL/pipeline steps
- 🧭 Supports Focus Mode or Story Node workflows
- 🗺️ Performs interpolation, imputation, harmonization, or geospatial alignment
- 🤖 Participates in deterministic orchestrators (e.g., governed agent executors)

### ✅ Naming convention
Model Card filenames MUST follow:

~~~text
<model_slug>_v<version>.md
~~~

Downstream pipelines MUST reference:
- the model card path under `mcp/model_cards/`
- the model card `version:` (doc version)
- the model artifact version (if different)
- the experiment(s) and provenance bundle(s) supporting the model

### 🧩 Attestable, SBOM/Telemetry-linked model cards
Each **model_card** MUST carry deterministic references to:

- **SBOM** (`sbom_ref`), **manifest** (`manifest_ref`), and **provenance/attestation** (`attestation_ref`)
- **Telemetry bundles** (energy/carbon/reliability): `telemetry_ref` + `telemetry_schema`
- **Lineage**: `openlineage_ref` (PROV‑O / JSON‑LD aligned, where used)

KFM then:
- hashes the **rendered model card**
- records `doc_integrity_checksum`
- signs it and emits/links a release-grade attestation

This yields one canonical digest for audits and reproducibility.

### 📚 Model Card Index
Populate this table with the model cards present in this directory. Sample rows are illustrative and MUST be updated to match the repo contents.

| 🧠 Model | 📄 Model Card | 🔢 Model Version | 🧭 Domain | 🛡️ Sensitivity | ✅ Status |
|---|---|---:|---|---|---|
| 🌡️ Climate Anomaly Net | `./climate_anomaly_net_v3.md` | v3 | Climate anomaly reconstruction | Low | Active / Enforced |
| 💧 Hydrology Seq2Seq | `./hydrology_seq2seq_v11.md` | v11 | Hydrologic reconstruction (gap-fill) | Mixed | Active / Enforced |
| 🧠 Focus Mode Transformer | `./focus_mode_transformer_v3.md` | v3 | Governed narrative reasoning | Mixed | Active / Enforced |
| 🗺️ Geo Alignment Net | `./geo_alignment_net_v4.md` | v4 | Geospatial alignment & harmonization | Mixed | Active / Enforced |

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/                                   — Monorepo root
├── 📁 mcp/                                                — Master Coder Protocol (governed R&D)
│   ├── 📁 experiments/                                    — Experiment logs (MCP-DL)
│   │   └── 📄 README.md                                   — Experiments index + rules
│   └── 📁 model_cards/                                    — Model Cards (this directory)
│       ├── 📄 README.md                                   — This file (index + rules)
│       ├── 📁 templates/                                  — Authoring templates
│       │   └── 📄 model-card.md                           — Canonical model card template
│       ├── 📄 <model_slug>_v<version>.md                  — One model card per model+version
│       └── 📄 ...                                         — Additional cards
├── 📁 schemas/                                            — Repo-wide schemas
│   └── 📄 model_card_v11.json                             — Model card schema (front-matter + body rules)
└── 📁 scripts/                                            — Repo-wide scripts
    └── 📁 model_cards/                                    — Build/sign/verify utilities
        ├── 🧱 build_and_sign.sh                            — Validate, hash, sign, attest
        └── 🧪 verify.sh                                    — Verify digests/signatures (if present)
~~~

---

## 🧭 Context

### 🔗 Relationship to MCP experiments
Every model card MUST link to at least one `mcp/experiments/*.md` record documenting:
- training or fine-tuning
- evaluation/validation
- deployment validation gates (when applicable)
- reproducibility controls (seed, environment, dependencies, provenance outputs)

### 🧾 Minimum required declarations inside every model card
- ✅ Intended use vs ❌ restricted use
- 🧪 Training and evaluation datasets (STAC/DCAT IDs where applicable)
- 🎛️ Reproducibility (seed, framework, hardware/container, SBOM reference)
- 📊 Metrics and validation methodology
- ⚠️ Limitations and failure modes
- 🛡️ Governance boundaries + human oversight requirements
- 🧾 PROV-O + OpenLineage locations + checksums (where used)
- ♻️ Telemetry reference (energy/carbon) when tracked

---

## 📦 Data & Metadata

### 🔑 Required front-matter keys (model cards)
Each `mcp/model_cards/<model_slug>_v<version>.md` MUST declare (at minimum):

- `sbom_ref`, `manifest_ref`, `weights_ref`
- `telemetry_ref`, `telemetry_schema`
- `openlineage_ref` (or an explicit statement of “not applicable” if permitted by policy)
- `signature_ref`, `attestation_ref`
- `doc_integrity_checksum`, `previous_version_hash`

### 🪶 Sovereignty and sensitivity defaults
- Never publish or refine sensitive locations in model outputs.
- Require masking/generalization whenever a model may touch cultural or sovereignty-restricted content.
- Require human review gates for narrative-capable models and for any output used in high-stakes contexts.

### 🧩 Contract alignment expectations
Model cards MUST declare:
- pipeline contract version (KFM-PDC v11)
- any data contracts they rely on (if applicable)
- required masking/generalization policy for inputs and outputs

---

## 🌐 STAC, DCAT & PROV Alignment

Model cards MUST:
- reference STAC/DCAT identifiers for training/evaluation datasets (where applicable)
- specify where STAC/DCAT records are emitted (if the model produces publishable assets)
- provide a PROV-O JSON-LD block in the model card (or a stable path to it)
- identify OpenLineage event storage location(s) for key runs (where used)

---

## 🧱 Architecture

Model cards bind together:
- 🧰 pipeline configuration (what calls the model)
- 🗂️ catalog identifiers (STAC/DCAT)
- 🧠 graph entities and relationships (Neo4j, via API boundaries)
- 🖥️ UI consumption boundaries (Focus Mode + Story Nodes)
- 🧾 provenance traces (PROV-O + OpenLineage)
- ♻️ telemetry bundles (energy/carbon/reliability)
- 🔐 attestations and signatures (release-grade verification)

Minimum interface contract each card must state:
- what the model consumes (inputs + required metadata)
- what it produces (outputs + expected schemas)
- where provenance and telemetry are written

---

## 🧠 Story Node & Focus Mode Integration

### 🧠 Narrative-capable models (must be explicit)
If a model can generate or shape narrative output, its model card MUST state:
- ✅ allowed claim types (evidence-led only)
- ❌ prohibited claim types (no speculation, no invented causes, no genealogy)
- 🪶 masking rules and sovereignty gates
- 👤 required human review steps before publish/release

### 🗺️ Non-narrative geospatial models
Geospatial alignment/interpolation models must define:
- output precision constraints and confidence propagation
- masking/generalization defaults for restricted areas
- downstream boundaries for narrative systems

---

## 🧪 Validation & CI/CD

### Minimal authoring flow (attestable)
1) Author a model card from the template in `mcp/model_cards/templates/model-card.md`.  
2) Run `scripts/model_cards/build_and_sign.sh` to:
   - validate YAML front‑matter against `schemas/model_card_v11.json`
   - embed content hashes for all external refs (SBOM, telemetry, weights)
   - compute a final **document SHA‑256**
   - sign and emit/attach an attestation (policy-controlled)
3) CI enforces: schema‑lint, link‑audit, digest consistency, signature verify.

### Merge blockers (common)
- missing provenance artifacts or references
- missing dataset identifiers for training/eval (when required)
- missing or ambiguous restricted-use boundaries
- more than one H1
- unapproved H2 headings
- fence violations (use `~~~` fences; do not use triple-backtick fences)

---

## ⚖ FAIR+CARE & Governance

All model cards must:
- declare FAIR category and CARE label
- declare sovereignty implications and required masking/approvals
- list prohibited outputs and required human oversight
- ensure traceability from claim → dataset/document → provenance → run identity

---

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.6 | 2025-12-13 | Unified index + enforceable “attestable” model card workflow (SBOM/telemetry/attestation-linked) and CI gates. |
| v11.0.0 | 2025-11-23 | Initial MCP model cards index for KFM v11. |

---

<div align="center">

[🧪 MCP Experiments Index](../experiments/README.md) ·
[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · KFM-OP v11 · KFM-PDC v11

</div>
