---
# =============================================================================
# 🧩 KFM / MCP Model Card Template
# File: mcp/model_cards/templates/MODEL_CARD.template.md
# Copy to: mcp/model_cards/{{MODEL_ID}}/MODEL_CARD.md
#
# Notes:
# - Keep the YAML front-matter (this is used by tooling + UI model panels).
# - Prefer stable IDs + digests over “latest”.
# - If "citations_required: true", runtime must refuse uncited factual claims.
# =============================================================================

# ✅ KFM-required metadata (machine-readable)
model_name: "{{MODEL_NAME}}"                       # e.g., "NowCast v2 – Air Quality"
model_id: "{{MODEL_ID}}"                           # stable slug, e.g., "nowcast-v2-air"
version: "{{VERSION}}"                             # semver or date tag, e.g., "2.1.0" / "2026-01-23"
status: "{{STATUS}}"                               # experimental | staging | production | deprecated
owner: "{{OWNER_TEAM_OR_PERSON}}"                  # e.g., "KFM Core AI"
maintainers:
  - "{{MAINTAINER_1}}"
created: "{{YYYY-MM-DD}}"
last_updated: "{{YYYY-MM-DD}}"

# ✅ Licensing & usage rights
license: "{{LICENSE}}"                             # e.g., "Apache-2.0", "MIT", "CC-BY-4.0", "Proprietary"
license_notes: "{{LICENSE_NOTES}}"                 # dataset/model-specific constraints

# (Optional) HF-style model card metadata for compatibility
language:
  - en
pipeline_tag: "{{PIPELINE_TAG}}"                   # e.g., text-generation | token-classification | image-to-text | tabular-regression
library_name: "{{LIBRARY_NAME}}"                   # e.g., "transformers", "pytorch", "sklearn", "xgboost"
tags:
  - kansas-frontier-matrix
  - geospatial
  - provenance-first
  - focus-mode
datasets:
  - "{{DATASET_OR_CORPUS_ID}}"                     # internal dataset IDs or public dataset names
metrics:
  - "{{PRIMARY_METRIC}}"                           # e.g., "MAE", "F1", "citation_coverage"

# ✅ KFM runtime + governance extensions
kfm:
  domain: "{{DOMAIN}}"                             # e.g., air-quality | hydrology | historical-narrative | extraction | forecasting
  model_type: "{{MODEL_TYPE}}"                     # LLM | RAG | classifier | simulation | bias-correction | rules | ensemble
  risk_tier: "{{RISK_TIER}}"                       # low | medium | high
  sensitivity_max: "{{SENSITIVITY_MAX}}"           # 0-4 (see “🔐 Sensitivity” section)
  citations_required: true                         # true unless explicitly justified
  tool_access:
    mode: "{{TOOL_MODE}}"                          # none | read-only | gated-write
    tools_allowed:
      - "{{TOOL_NAME_1}}"
      - "{{TOOL_NAME_2}}"
  policy_pack:
    - "{{POLICY_ID_1}}"                            # e.g., "KFM-PROV-001", "KFM-SENS-002"
    - "{{POLICY_ID_2}}"
  offline_pack_supported: "{{true_or_false}}"      # if packaged for field/offline mode
  geospatial:
    default_crs: "EPSG:4326"
    supported_crs:
      - "EPSG:4326"
      - "{{EPSG_CODE_IF_ANY}}"
    max_zoom_if_sensitive: "{{MAX_ZOOM_OR_NA}}"
  provenance:
    prov_activity_id: "{{PROV_ACTIVITY_ID}}"       # W3C PROV-O Activity ID (or JSON-LD @id)
    artifact_digest: "{{OCI_DIGEST_OR_SHA256}}"    # immutable artifact reference
    sbom_ref: "{{SBOM_PATH_OR_DIGEST}}"            # SBOM path or digest
    signature_ref: "{{COSIGN_SIGNATURE_REF}}"      # signature/ref used for verification
  ui:
    show_in_focus_mode: "{{true_or_false}}"
    model_details_panel: "{{true_or_false}}"
    simulated_output_badge: "{{true_or_false}}"    # REQUIRED for simulation/forecast models
---

# {{MODEL_NAME}} 🧭🤖

![KFM Banner](./assets/{{MODEL_ID}}_banner.png)

![Status](https://img.shields.io/badge/status-{{STATUS}}-blue)
![Risk](https://img.shields.io/badge/risk-{{RISK_TIER}}-orange)
![Provenance](https://img.shields.io/badge/provenance-required-success)
![Citations](https://img.shields.io/badge/citations-required-success)
![Sensitivity](https://img.shields.io/badge/sensitivity-max%20{{SENSITIVITY_MAX}}-purple)

> 🧠 **Evidence-first rule:** If you can’t cite it, say you can’t.  
> 🧾 **Provenance-first rule:** Every output must be traceable to inputs + code + parameters + run context.  
> 🔐 **Policy-first rule:** If policy can’t be evaluated, **fail closed**.

---

## 📦 Where this card lives (expected layout)

```text
📁 mcp/
  📁 model_cards/
    📁 templates/
      📄 MODEL_CARD.template.md   👈 (this file)
    📁 {{MODEL_ID}}/
      📄 MODEL_CARD.md            👈 (filled-in card)
      ⚙️ config/                  (prompts, params, schemas)
      🧪 eval/                    (benchmarks, reports, red-team notes)
      🧾 provenance/              (PROV JSON-LD, manifests, attestations)
      📦 artifacts/               (optional: local mirrors, weights, exports)
      📊 monitoring/              (dashboards, drift checks, canaries)
```

---

## 🧾 TL;DR Summary

| Field | Value |
|---|---|
| **Primary purpose** | {{PRIMARY_PURPOSE}} |
| **Model type** | {{MODEL_TYPE}} |
| **KFM domain** | {{DOMAIN}} |
| **Who uses it** | {{PRIMARY_USERS}} |
| **Citations required** | ✅ Yes |
| **Sensitivity max** | {{SENSITIVITY_MAX}} (0–4) |
| **Release status** | {{STATUS}} |
| **Last updated** | {{YYYY-MM-DD}} |
| **Artifact digest** | `{{OCI_DIGEST_OR_SHA256}}` |

### ✅ What this model does well
- {{STRENGTH_1}}
- {{STRENGTH_2}}
- {{STRENGTH_3}}

### ⚠️ What this model does *not* do
- {{OUT_OF_SCOPE_1}}
- {{OUT_OF_SCOPE_2}}

---

## 🎯 Intended Use

### ✅ In-scope use cases (KFM)
- 🗺️ **Geospatial Q&A / Focus Mode**: {{IN_SCOPE_USE_CASE_1}}
- 🧠 **Analysis / classification / extraction**: {{IN_SCOPE_USE_CASE_2}}
- ⏱️ **Temporal reasoning / timeline support**: {{IN_SCOPE_USE_CASE_3}}
- 📈 **Forecasting / NowCast / simulation** *(if applicable)*: {{IN_SCOPE_USE_CASE_4}}

### 🚫 Out-of-scope use cases
- {{OUT_OF_SCOPE_USE_CASE_1}}
- {{OUT_OF_SCOPE_USE_CASE_2}}
- {{OUT_OF_SCOPE_USE_CASE_3}}

### 👥 Intended users & environments
- **User types:** {{USER_TYPES}}
- **UI surfaces:** Focus Mode / map overlays / dashboards / offline packs / API
- **Operational context:** {{OPERATIONAL_CONTEXT}}

---

## 🧩 How it fits into KFM (architecture & flow)

### 🧠 Runtime behavior
- **Invocation path:** {{UI_OR_API_ENTRYPOINT}}
- **Retrieval (if RAG):** {{RETRIEVAL_SOURCES}}  
- **Policy enforcement:** {{POLICY_ENGINE}} (e.g., OPA/Rego)  
- **Output types:** {{OUTPUT_TYPES}} (text, GeoJSON, raster, STAC Item, etc.)

<details>
<summary>🗺️ Mermaid: “Evidence-first” flow (optional)</summary>

```mermaid
flowchart LR
  U[User / UI] -->|query| PG[Prompt Gate 🔐]
  PG -->|allowed| R[Retriever 🔎]
  R -->|sources + metadata| PE[Policy Engine (OPA) ✅/❌]
  PE -->|allowed| M[Model / Reasoner 🧠]
  M --> C[Citations + Provenance 🧾]
  C --> O[Response / Layer / Artifact 📦]
  PE -->|deny| D[Refusal / Redaction 🛑]
```

</details>

### 🧰 Tooling & permissions
> 🔒 **Principle:** Tools are *explicitly allowlisted* and *policy-gated*.

| Tool / Capability | Allowed? | Conditions | Notes |
|---|---:|---|---|
| Read from catalog / STAC | {{YES_NO}} | {{CONDITIONS}} | {{NOTES}} |
| Read from knowledge graph | {{YES_NO}} | {{CONDITIONS}} | {{NOTES}} |
| Generate derived artifacts | {{YES_NO}} | {{CONDITIONS}} | {{NOTES}} |
| Create PRs / write outputs | {{YES_NO}} | {{CONDITIONS}} | {{NOTES}} |

---

## 🔐 Sensitivity & Governance

### 🧷 Sensitivity levels (KFM standard)
Fill in which levels this model can **ingest** and **emit**.

| Level | Meaning (example) | Allowed output? |
|---:|---|---|
| 0 | Public / open | ✅ |
| 1 | Limited / community-shareable | {{YES_NO}} |
| 2 | Restricted (controlled access) | {{YES_NO}} |
| 3 | Sensitive (e.g., vulnerable sites, certain personal info) | {{YES_NO}} |
| 4 | Highly sensitive (sacred sites / protected info) | {{YES_NO}} |

> 🧭 **Hard rule:** Output must not be *less restricted* than the most sensitive input.

### 🧿 Sensitive geospatial handling (if applicable)
- **Geo-obfuscation strategy:** {{GEO_OBFUSCATION_STRATEGY}} (e.g., rounding, jitter, hex aggregation, zoom cap)
- **Display restrictions:** {{DISPLAY_RESTRICTIONS}} (e.g., mask attributes, hide geometry, show bounding region only)
- **Cultural protocols / community rules:** {{CULTURAL_PROTOCOLS}} (e.g., TK Labels-inspired restrictions)

### ✅ Governance checklist
- [ ] Licensing confirmed for all training & retrieval sources  
- [ ] Sensitivity labels present on inputs and enforced on outputs  
- [ ] Provenance record created for this release (PROV JSON-LD + artifact digest)  
- [ ] Policy Pack IDs listed and CI policy tests passing  
- [ ] Red-team / abuse testing performed for this risk tier  
- [ ] “Simulated / Modeled Output” badge enabled (if forecasting/simulation)

---

## 🗃️ Data & Provenance

### 📚 Data sources (training, tuning, or retrieval)
> Attach **manifests** and **licenses**. Prefer STAC/DCAT/PROV identifiers.

| Source | Type | License | Sensitivity | Version / Digest | Notes |
|---|---|---|---:|---|---|
| {{SOURCE_1}} | {{TYPE}} | {{LICENSE}} | {{0-4}} | {{ID_OR_DIGEST}} | {{NOTES}} |
| {{SOURCE_2}} | {{TYPE}} | {{LICENSE}} | {{0-4}} | {{ID_OR_DIGEST}} | {{NOTES}} |

### 🧹 Preprocessing & transforms
- **Parsing / extraction:** {{PARSING_STEPS}}
- **Geospatial steps:** {{GEO_STEPS}} (reprojection, georeferencing RMS, topology checks, etc.)
- **Normalization:** {{NORMALIZATION_STEPS}}
- **Dedup / entity resolution:** {{DEDUP_STEPS}}
- **Quality checks:** {{QUALITY_CHECKS}} (schemas, constraints, outliers)

### 🧾 Provenance artifacts (required)
- **PROV Activity:** `{{PROV_ACTIVITY_ID}}`
- **Manifest:** `provenance/{{MODEL_ID}}.manifest.json`
- **Attestation:** `provenance/{{MODEL_ID}}.attestation.jsonl`
- **SBOM:** `provenance/{{MODEL_ID}}.sbom.spdx.json` *(or equivalent)*
- **Signature:** `{{COSIGN_SIGNATURE_REF}}`

---

## 🧠 Model Details

### 🧬 Lineage
- **Base model / algorithm:** {{BASE_MODEL_OR_ALGO}}
- **Fine-tuning (if any):** {{FINETUNE_METHOD}}
- **Embedding model (if RAG):** {{EMBEDDING_MODEL}}
- **Retrieval store:** {{RETRIEVAL_STORE}} (vector DB / graph / hybrid)
- **Model artifact digest:** `{{OCI_DIGEST_OR_SHA256}}`
- **Training run ID:** {{TRAIN_RUN_ID}}
- **Code commit:** {{GIT_COMMIT_SHA}}

### 🧾 Assumptions (be explicit)
- {{ASSUMPTION_1}}
- {{ASSUMPTION_2}}
- {{ASSUMPTION_3}}

### 🧠 Output semantics (“Evidence Ladder”)
Mark what the model emits and how it should be interpreted:

- [ ] **Observation** (direct measurement / primary source)
- [ ] **Derived** (computed from observations)
- [ ] **Modeled / Simulated** (forecast, scenario, nowcast)
- [ ] **Interpretation / Narrative** (synthesis, explanation)

> 🏷️ If *Modeled / Simulated*, **UI must display**: “Simulated / Modeled Output” badge + assumptions + uncertainty.

---

## 🏋️ Training & Configuration (if applicable)

### 🧷 Training configuration
- **Objective:** {{TRAIN_OBJECTIVE}}
- **Loss / optimization:** {{LOSS_OPTIMIZER}}
- **Hyperparameters:** {{HYPERPARAMS}}
- **Random seed(s):** {{SEEDS}}
- **Hardware:** {{HARDWARE}}
- **Framework versions:** {{FRAMEWORK_VERSIONS}}

### ♻️ Reproducibility notes
- **Determinism:** {{DETERMINISM_NOTES}}
- **Container image digest:** {{CONTAINER_DIGEST}}
- **Rebuild steps:** {{REBUILD_STEPS}}

---

## 🧪 Evaluation & Validation

### ✅ Primary evaluation summary
| Metric | Value | Dataset / Split | Target / Threshold | Notes |
|---|---:|---|---:|---|
| {{METRIC_1}} | {{VALUE_1}} | {{DATASET}} | {{TARGET}} | {{NOTES}} |
| {{METRIC_2}} | {{VALUE_2}} | {{DATASET}} | {{TARGET}} | {{NOTES}} |

### 📎 Benchmark sets & ground truth
- **Gold / labeled datasets:** {{GROUND_TRUTH_DATASETS}}
- **Sampling strategy:** {{SAMPLING_STRATEGY}}
- **Geospatial validation:** {{GEO_VALIDATION}} (CRS correctness, spatial joins, topology, positional accuracy)
- **Temporal validation:** {{TIME_VALIDATION}} (time windows, leakage checks)

### 🧾 Citation & provenance quality (KFM-specific)
- **Citation coverage:** {{CITATION_COVERAGE}}%
- **Citation correctness audit:** {{CITATION_AUDIT_METHOD}}
- **Refusal rate when sources missing:** {{REFUSAL_RATE}}%
- **“Show your work” compliance:** {{SHOW_YOUR_WORK_COMPLIANCE}}

### 🧨 Red teaming & abuse testing
- **Prompt injection tests:** {{INJECTION_TESTS}}
- **Sensitive data exfiltration tests:** {{EXFIL_TESTS}}
- **Geo-sensitive disclosure tests:** {{GEO_SENSITIVE_TESTS}}
- **Tool misuse tests (if tools enabled):** {{TOOL_MISUSE_TESTS}}
- **Results & fixes:** {{REDTEAM_RESULTS_LINK}}

---

## ⚠️ Limitations & Known Failure Modes

### Known limitations
- {{LIMITATION_1}}
- {{LIMITATION_2}}
- {{LIMITATION_3}}

### Common failure modes & mitigations
| Failure mode | Example | Mitigation | Residual risk |
|---|---|---|---|
| Hallucinated attribution | {{EXAMPLE}} | Enforce citations + refusal | {{LOW_MED_HIGH}} |
| Overconfident forecast | {{EXAMPLE}} | Uncertainty + scenario labeling | {{LOW_MED_HIGH}} |
| CRS confusion | {{EXAMPLE}} | Require CRS + validation checks | {{LOW_MED_HIGH}} |
| Sensitive location leakage | {{EXAMPLE}} | Geo-obfuscation + zoom caps + policy | {{LOW_MED_HIGH}} |

---

## 🛡️ Safety, Security & Privacy

### 🔐 Prompt & tool security
- **Prompt Gate rules:** {{PROMPT_GATE_RULES}}
- **Allow/block lists:** {{ALLOW_BLOCK_LISTS}}
- **Policy checks (OPA/Rego):** {{OPA_CHECKS}}
- **Secrets handling:** {{SECRETS_HANDLING}}

### 🕵️ Privacy protections (pick what applies)
- [ ] k-anonymity / aggregation thresholds
- [ ] l-diversity / t-closeness (for sensitive attribute release)
- [ ] Differential privacy (ε={{EPSILON_OR_NA}})
- [ ] Query auditing / rate limiting
- [ ] Role-based access control (RBAC)
- [ ] Geo-obfuscation / location generalization

### 🧯 Incident response
- **Escalation path:** {{ESCALATION_PATH}}
- **Kill switch / disable plan:** {{KILL_SWITCH_PLAN}}
- **User reporting:** {{REPORTING_CHANNEL}}
- **Post-incident requirements:** {{POST_INCIDENT_REQUIREMENTS}}

---

## 📊 Monitoring & Maintenance

### 📈 Monitoring signals
| Signal | How measured | Threshold | Action |
|---|---|---:|---|
| Drift (data) | {{METHOD}} | {{THRESH}} | {{ACTION}} |
| Drift (model) | {{METHOD}} | {{THRESH}} | {{ACTION}} |
| Citation failures | {{METHOD}} | {{THRESH}} | {{ACTION}} |
| Policy denials | {{METHOD}} | {{THRESH}} | {{ACTION}} |
| Latency / cost | {{METHOD}} | {{THRESH}} | {{ACTION}} |

### 🧪 Canary tests & health checks
- **Weekly graph/data health check:** {{HEALTH_CHECKS}}
- **Schema invariants:** {{SCHEMA_INVARIANTS}}
- **Provenance invariants:** {{PROV_INVARIANTS}}

---

## 🚀 Deployment

### Serving / packaging
- **Serving mode:** {{SERVING_MODE}} (API / batch / streaming / offline pack)
- **Container image:** `{{CONTAINER_IMAGE_REF}}`
- **Runtime deps:** {{RUNTIME_DEPS}}
- **GPU/CPU requirements:** {{HW_REQUIREMENTS}}

### Offline / field mode (if applicable) 🏕️
- **Offline pack name:** {{OFFLINE_PACK_NAME}}
- **Included artifacts:** {{OFFLINE_PACK_CONTENTS}}
- **On-device model:** {{ON_DEVICE_MODEL_NOTES}}
- **Sync strategy:** {{SYNC_STRATEGY}}

---

## 🌱 Sustainability (optional but encouraged)
- **Training energy estimate:** {{ENERGY_ESTIMATE}}
- **Carbon estimate:** {{CARBON_ESTIMATE}}
- **Efficiency improvements:** {{EFFICIENCY_NOTES}}

---

## 🔗 Related Artifacts & Links

### KFM internal references
- **Config:** `mcp/model_cards/{{MODEL_ID}}/config/{{CONFIG_FILE}}`
- **Evaluation report:** `mcp/model_cards/{{MODEL_ID}}/eval/{{EVAL_REPORT}}`
- **Provenance:** `mcp/model_cards/{{MODEL_ID}}/provenance/`
- **Monitoring:** `mcp/model_cards/{{MODEL_ID}}/monitoring/`

### External references (optional)
- Papers / docs: {{PAPERS}}
- Standards used: {{STANDARDS}} (e.g., STAC, DCAT, PROV-O)

---

## 🗓️ Changelog

| Date | Version | Change | Author | PR / Provenance |
|---|---|---|---|---|
| {{YYYY-MM-DD}} | {{VERSION}} | {{CHANGE_SUMMARY}} | {{AUTHOR}} | {{PR_OR_PROV_LINK}} |

---

## ✅ Release Sign-off

| Role | Name | Date | Approved? |
|---|---|---:|---:|
| Owner | {{OWNER_TEAM_OR_PERSON}} | {{YYYY-MM-DD}} | {{YES_NO}} |
| Reviewer | {{REVIEWER_1}} | {{YYYY-MM-DD}} | {{YES_NO}} |
| Governance / Data Steward | {{STEWARD}} | {{YYYY-MM-DD}} | {{YES_NO}} |

> 🧾 **Reminder:** If this model produces *Modeled/Simulated* outputs, ensure the UI displays assumptions, uncertainty, and the “Simulated / Modeled Output” badge by default.
