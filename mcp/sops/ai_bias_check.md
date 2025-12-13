---
title: "🧠 KFM SOP — AI Bias, Fairness & Governance Check (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/ai_bias_check.md"

version: "v11.0.0"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & AI Governance Board"
status: "Active / Enforced"
content_stability: "stable"

doc_kind: "SOP"
intent: "ai-bias-check"
semantic_document_id: "kfm-sop-ai-bias-check"
doc_uuid: "urn:kfm:mcp:sop:ai-bias-check:v11.0.0"
event_source_id: "ledger:kfm:mcp:sop:ai-bias-check:v11.0.0"
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

classification: "Governed AI Document"
sensitivity: "Mixed"
fair_category: "F1-A1-I3-R3"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
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

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "genealogical-inference"
  - "sacred-site-inference"
  - "sensitive-coordinate-exposure"
  - "governance-override"
  - "fabricate-provenance"

provenance_chain:
  - "prov:Plan:urn:kfm:mcp:sop:ai-bias-check:v11.0.0"
---

<div align="center">

# 🧠 **KFM SOP — AI Bias, Fairness & Governance Check (v11 LTS)**
`mcp/sops/ai_bias_check.md`

**Purpose**  
Define the **governed, reproducible, FAIR+CARE–aligned** procedure for evaluating model bias, fairness risk, sovereignty conflicts, and compliance with KFM AI governance policies for all AI models deployed in pipelines, Focus Mode, and Story Node v3 generation.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/AI%20Governance-Enforced-critical" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧪 MCP Experiments](../experiments/README.md) ·
[🧬 Model Cards](../model_cards/README.md) ·
[🏛️ Governance](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Sovereignty](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

---

## 📘 Overview

### 🎯 Scope
This SOP applies to:
- 🧠 all AI/ML models used in KFM pipelines (ETL, climate, hydrology, NLP/CV, geospatial alignment)
- 🧭 Focus Mode v3 narrative engines and governed summarizers
- 📖 Story Node v3 generators and narrative shapers
- 🤖 CrewAI / LangGraph workers that produce user-visible or downstream-impacting artifacts
- 🧩 any AI component that can alter derived datasets, metadata, or narrative context

This SOP is mandatory:
- ✅ before model deployment
- ✅ before model updates (weights/config/prompt/templates)
- ✅ whenever training data or evaluation data versions change
- ✅ when governance, sovereignty, or CARE policy changes are introduced

### 🧷 Non-negotiables
- **No untracked data:** training/eval datasets must be version-pinned and referenced by STAC/DCAT identifiers.
- **No untracked runs:** evaluations must emit provenance and reference telemetry.
- **Sovereignty-first:** protected data and sensitive geographies override optimization goals.
- **Narrative safety:** narrative-capable models must pass “no speculation / no sensitive disclosure” gates.
- **Deterministic evaluation:** same inputs + config + seeds → same evaluation outputs.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 mcp/
│   ├── 📁 sops/
│   │   └── 📄 ai_bias_check.md                              — 🧠 This SOP
│   ├── 📁 model_cards/
│   │   ├── 📄 README.md                                     — 🧬 Model cards index
│   │   └── 📄 <model_card>.md                               — 🧾 Model card under review
│   └── 📁 experiments/
│       ├── 📄 README.md                                     — 🧪 Experiment index + rules
│       └── 📄 YYYY-MM-DD_AI-EXP-###.md                      — 🧪 Bias/XAI evaluation experiment log
├── 📁 data/
│   └── 📁 provenance/
│       └── 📁 experiments/
│           └── 📁 ai_bias_check/
│               └── 📁 <timestamp>/                          — 🧬 PROV-O bundle + OpenLineage refs
│                   ├── 🧬 prov.jsonld
│                   ├── 🧾 eval_report.json
│                   ├── 📊 metrics.json
│                   ├── 🧠 xai_manifest.json
│                   └── 🔐 checksums.json
└── 📁 releases/
    └── 📁 v11.0.0/
        └── 📊 mcp-sops-telemetry.json                        — ♻️ Energy/carbon telemetry aggregation
~~~

---

## 🧭 Context

### ✅ Preconditions
Before running this SOP, ensure:
- 🧬 a model card exists for the model under evaluation:
  - `mcp/model_cards/<model_card>.md`
- 🧪 supporting training/evaluation experiments exist (or are created as part of this run):
  - `mcp/experiments/YYYY-MM-DD_AI-EXP-###.md`
- 🧾 datasets are version-pinned and referenced by STAC/DCAT identifiers
- 🛡️ governance classification exists for all datasets used (FAIR+CARE + sovereignty flags)
- 🔗 provenance and run identity mechanisms are available (PROV-O + OpenLineage references)
- 📊 telemetry capture is enabled (energy/carbon/runtime where available)

### 📥 Required inputs
| Input | Description |
|---|---|
| Model artifacts | weights, config, tokenizer (if applicable), prompt templates (if applicable) |
| Model card | current model card with intended use/restricted use + governance constraints |
| Training dataset IDs | STAC/DCAT identifiers + pinned versions |
| Evaluation datasets | balanced + stress sets (region/time/topic stratified as applicable) |
| Experiment references | training + eval experiment IDs and run identifiers |
| Governance metadata | CARE tier, sovereignty tags, masking requirements |
| Integrity hashes | config hash, dataset hash list, prompt/template hashes (for narrative models) |

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[🟢 Start: select model + model card] --> B[📥 Load artifacts + pinned datasets]
  B --> C[🧾 Verify lineage: STAC/DCAT + hashes + SBOM refs]
  C --> D[🧩 Build fairness risk matrix]
  D --> E[🧠 Run XAI: SHAP/LIME/attribution/drift]
  E --> F{Narrative-capable?}
  F -->|Yes| G[📖 Narrative safety + sovereignty checks]
  F -->|No| H[🧮 Statistical bias scoring]
  G --> H
  H --> I[🛡️ Policy validations + prohibited-output scans]
  I --> J[🧬 Write PROV-O + OpenLineage refs + checksums]
  J --> K[📊 Write telemetry + evaluation report]
  K --> L{Decision}
  L -->|Approved| M[✅ Deploy allowed]
  L -->|Approved w/ restrictions| N[⚠️ Deploy w/ gates + masking]
  L -->|Rejected| O[⛔ Block deployment + remediation]
  L -->|Escalated| P[🏛️ Council decision required]
~~~

---

## 🧱 Architecture

### 🧪 Procedure (deterministic steps)

#### Step 1 — Load model + validate metadata integrity
- load weights/config/tokenizer/templates
- compute and record:
  - config hash
  - model artifact checksum(s)
  - prompt/template hash(es) for narrative/LLM components
- confirm dataset IDs and versions match those declared in the model card

Hard stop conditions:
- mismatch between model card dataset list and actual loaded dataset versions
- missing provenance references for training or evaluation data
- missing or invalid sovereignty/CARE metadata where required

#### Step 2 — Define the fairness risk matrix (model-specific)
Create a model-specific risk matrix describing:
- risk domains (environmental, cultural, historical, sovereignty, temporal, semantic)
- the required tests per domain
- acceptance criteria (thresholds or “must-pass” checks)
- required review route(s)

Template:

| Domain | Risk Type | Required Test | Accept/Reject Gate |
|---|---|---|---|
| Environmental | spatial bias | error-by-region / regional calibration | threshold |
| Temporal | decadal skew | error-by-period | threshold |
| Cultural/Narrative | framing bias | neutrality + prohibited language scan | must-pass |
| Sovereignty | conflict risk | masking + restricted content bypass | must-pass |
| Semantic | drift | embedding drift + topic skew | threshold |

#### Step 3 — Run explainability (XAI) suite
Run the XAI suite appropriate to the model class:

- tabular/time-series:
  - SHAP (global + local)
  - feature importance stability
  - counterfactual sanity checks (bounded)
- neural (seq2seq/CNN/transformer):
  - saliency/attribution (where applicable)
  - attention trace artifacts (where permitted)
- embedding / NLP:
  - embedding drift tests
  - cluster attribution and representational parity checks

Write an XAI manifest (no heavy binaries committed into Markdown):
~~~text
data/provenance/experiments/ai_bias_check/<timestamp>/xai_manifest.json
~~~

#### Step 4 — Narrative & factual safety checks (when applicable)
If the model can generate or shape text (Focus Mode / Story Node / metadata autogen):
- block:
  - speculation
  - genealogical inference
  - sacred-site inference
  - unverified claims presented as fact
  - restricted coordinate disclosure
  - colonial/bias phrasing that violates narrative governance

Required outputs:
- violations list (with stable pointers to test cases)
- pass/fail gate result
- remediation recommendations (bounded)

#### Step 5 — Statistical bias scoring (model-class dependent)
Compute bias metrics appropriate to the model:

Common metrics (use what applies; document selection):
- mean absolute bias (MAB)
- RMSE / MAE
- error-by-region heatmaps (Kansas ecoregions / east-west partitions)
- temporal skew metrics (error by decade/period)
- uncertainty calibration (coverage vs predicted CI)
- spatial autocorrelation bias (e.g., Moran’s I on residuals) when spatial outputs exist

Write metrics:
~~~text
data/provenance/experiments/ai_bias_check/<timestamp>/metrics.json
~~~

#### Step 6 — Governance validations (hard constraints)
Enforce:
- sovereignty policies and masking requirements
- prohibited output patterns
- contract compliance (KFM-PDC v11 alignment where relevant)
- model card restricted-use constraints

Record:
- violations
- auto-remediations applied (if permitted)
- escalation triggers

#### Step 7 — Lineage + reproducibility package
Write a reproducibility bundle containing:
- PROV-O JSON-LD referencing:
  - input entities (datasets, model artifacts)
  - activities (evaluation steps)
  - agents (pipeline services, human reviewers)
- OpenLineage references (IDs or pointers; no embedded secrets)
- checksums for key outputs
- config snapshot (or config hash + path)

Write:
~~~text
data/provenance/experiments/ai_bias_check/<timestamp>/prov.jsonld
data/provenance/experiments/ai_bias_check/<timestamp>/checksums.json
data/provenance/experiments/ai_bias_check/<timestamp>/eval_report.json
~~~

#### Step 8 — Final compliance decision
Decision outcomes (normative):
- ✅ **Approved**
- ⚠️ **Approved with restrictions**
  - required masking
  - required narrative safety filter
  - restricted domains/basins/topics
  - mandatory human review gates
- ⛔ **Rejected**
  - must not deploy; remediation required
- 🏛️ **Escalated**
  - FAIR+CARE Council and/or AI Governance Board decision required

Decision MUST be reflected in:
- model card status fields and restrictions section
- experiment log entry
- governance ledger event reference

---

## 📦 Data & Metadata

### 🧾 Required artifacts produced by this SOP
Minimum outputs for each evaluation run:
- `eval_report.json` (decision, gates, required restrictions, reviewer route)
- `metrics.json` (bias metrics + thresholds)
- `xai_manifest.json` (references to XAI artifacts and summaries)
- `prov.jsonld` (lineage)
- `checksums.json` (integrity)

### 🧬 Model card update requirements (mandatory)
After a successful run, update the model card to include:
- evaluation date + run identifier
- summarized bias findings and key metrics
- declared restrictions (if “Approved with restrictions”)
- updated provenance pointers (PROV-O bundle reference)
- updated telemetry pointer (if model evaluation compute is non-trivial)

---

## 🌐 STAC, DCAT & PROV Alignment

- This SOP does not inherently create STAC assets, but it MUST reference dataset STAC/DCAT identifiers used for evaluation.
- If the model evaluation produces publishable datasets (e.g., benchmark sets, fairness slices), those must be cataloged via STAC/DCAT under the appropriate domain.
- PROV-O is mandatory and must link:
  - datasets → evaluation activity → decision artifact
- OpenLineage references are required when evaluation is executed via pipeline runners.

---

## 🧪 Validation & CI/CD

### ✅ Verification checklist (must pass)
- model card exists and references correct datasets
- dataset IDs are version-pinned and match loaded inputs
- governance metadata present (CARE + sovereignty)
- XAI artifacts present (as manifest references)
- bias metrics computed and stored
- narrative checks performed for narrative-capable models
- PROV-O bundle present
- telemetry reference recorded (where applicable)
- CI gates green (docs + provenance + policy scans)

### 🧰 Recommended runbook (implementation-specific)
This SOP is compatible with multiple executors; the runbook must:
- record config + seeds
- record dataset identifiers
- emit the required artifact set

Example command placeholders (adjust to actual in-repo tools):
~~~bash
python -m src.pipelines.ai_gov.evaluate_bias_v11 \
  --model_card mcp/model_cards/<model_card>.md \
  --config src/pipelines/ai_gov/config/bias_eval_v11.yaml \
  --out_dir data/provenance/experiments/ai_bias_check/<timestamp>/
~~~

---

## ⚖ FAIR+CARE & Governance

### 🪶 Sovereignty requirements (hard constraints)
- never output or store restricted coordinates in evaluation artifacts
- protected datasets may require:
  - bypass of narrative-capable models
  - masked/generalized evaluation slices
  - restricted access handling per sovereignty policy
- any sovereignty-tagged violations trigger escalation routing

### 🤝 CARE requirements
All models must:
- avoid reinforcing historical or cultural harm
- avoid misrepresentation of communities or histories
- document bias and limitations clearly
- enforce restrictions and human review for high-risk domains

No exceptions without formal governance approval.

---

## 🌱 Telemetry & Sustainability

Record (when compute is meaningful):
- runtime duration
- energy use (Wh)
- carbon estimate (gCO₂e)
- hardware profile
- IO + memory patterns (where available)

Telemetry aggregates to:
~~~text
releases/<version>/mcp-sops-telemetry.json
~~~

Used for:
- sustainability scoring
- governance audits
- model efficiency tracking and optimization

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-11-23 | Initial AI fairness/bias SOP for KFM-MCP v11. |
| v11.0.0 | 2025-12-13 | Updated to KFM-MDP v11.2.6 structure (directory layout profile, tilde fences, governed header/footer, deterministic evaluation artifact set). |

---

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · KFM-OP v11.0 · KFM-PDC v11.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
