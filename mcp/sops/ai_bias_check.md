---
title: "🧠 KFM SOP — AI Bias, Fairness & Governance Check (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/ai_bias_check.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · FAIR+CARE Council & AI Governance Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/mcp-sops-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-sops-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active / Enforced"
doc_kind: "SOP"
intent: "ai-bias-check"
semantic_document_id: "kfm-sop-ai-bias-check"
doc_uuid: "urn:kfm:mcp:sop:ai-bias-check:v11.0.0"
machine_extractable: true
classification: "Governed AI Document"
sensitivity: "Mixed"
fair_category: "F1-A1-I3-R3"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧠 **KFM Standard Operating Procedure — AI Bias, Fairness & Governance Check (v11 LTS)**  
`mcp/sops/ai_bias_check.md`

**Purpose:**  
Define the **governed, reproducible, FAIR+CARE–aligned procedure** for evaluating model bias, fairness risk, sovereignty conflicts, and compliance with AI ethics policies for all AI models deployed in KFM pipelines, Focus Mode, and Story Node v3 generation.

</div>

---

## 📘 1. Scope

This SOP applies to:

- All **AI/ML models** used in KFM pipelines (ETL, climate, hydrology, NLP)  
- **Focus Mode v3** narrative engines  
- **Story Node generators**  
- **Geospatial inference models**  
- Any CrewAI or LangGraph-based AI worker  
- Any AI system whose output is visible to users or affects downstream data  

This SOP is mandatory **before model deployment**, **before model update**, and **whenever datasets change**.

---

## 🧩 2. Preconditions

Before running this SOP, ensure:

- You have the **model card** for the model under evaluation (`mcp/model_cards/**`)  
- The related **experiments** are up-to-date (`mcp/experiments/**`)  
- Data Contracts (`docs/contracts/*.json`) are satisfied  
- FAIR+CARE classification is available for all datasets used  
- You have access to:
  - Neo4j graph (read-only)  
  - OpenLineage logs  
  - STAC/DCAT metadata  

Governance documents:

- `FAIRCARE-GUIDE.md`
- `INDIGENOUS-DATA-PROTECTION.md`
- AI safety requirements (Focus Mode v3 / narrative compliance)

---

## 🧪 3. Inputs

| Required Input | Description |
|----------------|-------------|
| **Model artifacts** | Weights, config, tokenizer, seeds |
| **Training dataset STAC/DCAT IDs** | Exact dataset versions used |
| **Eval datasets** | Balanced and imbalanced sets |
| **Model card** | Must exist prior to evaluation |
| **Experiment logs** | Reproducible references for training/evaluation |
| **Governance metadata** | CARE classification, sovereignty tags |
| **Prompt integrity hashes** | For narrative / LLM components |

---

## 📜 4. Procedure (Step-by-Step, Deterministic)

### 4.1 Step 1 — Load Model + Metadata

- Load model weights, configs, seeds  
- Validate all metadata hashes (config, model, dataset lineage)  
- Confirm STAC/DCAT entries match declared model card inputs  

If mismatch → STOP and update lineage or reject model.

---

### 4.2 Step 2 — Bias & Fairness Risk Matrix

Construct a fairness matrix:

| Domain | Risk Type | Required Test |
|--------|-----------|----------------|
| **Environmental** | spatial bias | compare predictions across regions |
| **Cultural** | narrative framing | CARE-compliant narrative evaluation |
| **Historical** | archival misrepresentation | story-node validation |
| **Indigenous data** | sovereignty conflict | H3 masking & policy application |
| **Hydrology/Climate** | data-decadal skew | bias-by-time-period tests |
| **Semantic AI** | demographic bias | SHAP clusters + embedding drift |

Models must declare risk domains in their **model card**.

---

### 4.3 Step 3 — Run Explainability (XAI Layer)

Run:

- **SHAP** values  
- **LIME** explanations  
- Prototype/scatter attribution  
- Embedding drift detection  
- Saliency maps (for neural models)

Save all outputs to:

```
mcp/experiments/YYYY-MM-DD_<DOMAIN>-EXP-###.md
```

Attach plots/tables.

---

### 4.4 Step 4 — Narrative/Factual Safety Checks (For AI text models)

For Focus Mode / Story Node models:

- Check for:
  - Colonial bias  
  - Sensitive heritage exposure  
  - Unverified claims  
  - Speculation about Indigenous genealogy  
  - Use of restricted terms  
  - Exposure of raw coordinates for sensitive heritage sites  
- Validate:
  - CARE alignment  
  - Sovereignty compliance  
  - Fair representation rules  
  - Neutral historical language criteria  

Narrative violations must be escalated to:

### → **FAIR+CARE Council**  
### → **Indigenous Data Steward or delegated reviewer**

---

### 4.5 Step 5 — Statistical Bias Scoring

Compute:

- Mean Absolute Bias  
- Demographic Parity / Equalized Odds (if applicable)  
- Spatial Autocorrelation Bias (Moran’s I)  
- Temporal skew metrics  
- Error-by-region heatmaps  
- Uncertainty bounds  

Store evaluation as structured metadata in:

```
mcp/model_cards/<model>.md
```

---

### 4.6 Step 6 — Policy & Governance Validations

Enforce:

- Sovereignty policies  
- Data masking (H3 generalization)  
- Ethics constraints (narrative & spatial layers)  
- AI output safety policies  
- KFM-PDC v11 data contract rules  
- Prohibited-output patterns

Record:

- Violations  
- Auto-remediation  
- Escalation events (FAIR+CARE Council)  

---

### 4.7 Step 7 — Lineage, Telemetry & Reproducibility

Write:

- **OpenLineage v2.5 event**  
- **PROV-O JSON-LD provenance block**  
- Energy + carbon telemetry  
- Config & seed  
- Experiment ID  

Save to:

```
data/provenance/experiments/<model>/<timestamp>.json
```

---

### 4.8 Step 8 — Final Compliance Decision

The model may:

| State | Meaning |
|-------|---------|
| **Approved** | Safe for deployment |
| **Approved with restrictions** | Must use masking, narrative filters |
| **Rejected** | High bias / sovereignty conflicts / safety failures |
| **Escalated** | Requires FAIR+CARE Council decision |

---

## 🛡️ 5. Verification

A successful SOP completion requires:

- All XAI evaluations present  
- All governance metadata valid  
- No CARE violations  
- Provenance complete  
- Telemetry present (energy, carbon, run time)  
- Model card updated  
- CI/CD passing:

  - `mcp-validate.yml`  
  - `docs_validate.yml`  
  - `schema-lint-v11`  
  - `governance-audit-v11`

---

## 🧯 6. Failure Modes & Recovery

### **Critical Failures**

- Model produces culturally harmful narratives  
- Coordinate leakage of sensitive sites  
- Severe demographic/spatial/temporal bias  
- Missing lineage or untracked datasets  
- Model trained on unapproved data  

**Recovery Actions:**

- Retrain with balanced datasets  
- Apply masking / sovereignty enforcement  
- Adjust prompts / narrative templates  
- Re-run XAI and experiment logs  
- Submit for governance review  

---

## 🧭 7. CARE, Sovereignty & Ethics Notes

All models must:

- Avoid reinforcing historical or cultural bias  
- Prevent exposure of sensitive tribal, archaeological, or sacred information  
- Use **H3 masking** and **Dynamic Generalization Standard** for risk areas  
- Be reviewed by FAIR+CARE Council for Tier A domains  
- Follow ethical narrative style guidelines used in Focus Mode v3  

No exceptions without formal governance approval.

---

## 📊 8. Telemetry & Sustainability Requirements

Record:

- Energy usage (Wh)  
- Carbon emissions (gCO₂e)  
- Compute duration  
- IO & memory patterns  

Telemetry is aggregated into:

```
releases/<version>/mcp-sops-telemetry.json
```

Used for long-term:

- Sustainability scoring  
- Model efficiency analysis  
- Governance and reproducibility audits  

---

## 🕰 9. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial AI fairness/bias SOP for KFM-MCP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MCP-DL v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
FAIR+CARE · Sovereignty-Aware · Reproducible · Governed  

</div>
