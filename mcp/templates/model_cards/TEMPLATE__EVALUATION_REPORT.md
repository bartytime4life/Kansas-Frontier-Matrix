---
id: "{{EVAL_REPORT_ID}}"                  # e.g. eval_2026-01-21_focusmode_gpt-XYZ
title: "Model Evaluation Report — {{MODEL_NAME}} ({{MODEL_VERSION}})"
status: "draft"                           # draft | review | final
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"

# Ownership 👥
model_owner: "{{NAME_OR_TEAM}}"
evaluation_lead: "{{NAME_OR_TEAM}}"
governance_reviewer: "{{NAME_OR_TEAM}}"
security_reviewer: "{{NAME_OR_TEAM}}"

# Traceability ⛓️
repo: "{{GIT_REMOTE_URL}}"
commit_sha: "{{GIT_COMMIT_SHA}}"
run_id: "{{RUN_ID}}"                      # stable ID for this evaluation run
environment: "{{ENVIRONMENT}}"            # dev | staging | prod-like | offline
mcp_server: "{{MCP_SERVER_NAME}}"         # if applicable
mcp_server_version: "{{MCP_SERVER_VERSION}}"

# Classification ⚖️
distribution: "{{PUBLIC|INTERNAL|RESTRICTED}}"
sensitivity_notes: "{{NONE|SUMMARY}}"
---

# 🧪 Model Evaluation Report — {{MODEL_NAME}} ({{MODEL_VERSION}})

![Template](https://img.shields.io/badge/template-Evaluation%20Report-blue)
![KFM](https://img.shields.io/badge/KFM-provenance--first-2ea44f)
![Governance](https://img.shields.io/badge/OPA%2FConftest-policy%20gates-6f42c1)
![Status](https://img.shields.io/badge/status-{{STATUS_BADGE}}-orange)

> [!IMPORTANT]
> This report is **evidence-first**. If results can’t be traced to datasets, logs, and artifacts, treat the evaluation as **incomplete**.

---

## 🔎 At-a-glance

| Item | Value |
|---|---|
| **Release decision** | ✅ Ship / 🟡 Ship w/ Mitigations / ⛔ Hold |
| **Primary use in KFM** | {{FOCUS_MODE / INGESTION / EXTRACTION / CLASSIFICATION / OTHER}} |
| **Model category** | {{LLM / Vision / Embeddings / Tabular / Time-series / Other}} |
| **Safety risk** | 🟢 Low / 🟡 Medium / 🔴 High |
| **Data sensitivity exposure risk** | 🟢 Low / 🟡 Medium / 🔴 High |
| **Evaluation coverage** | {{%}} ({{NUM_TESTS}} tests; {{NUM_SCENARIOS}} scenarios) |
| **Key metrics** | {{TOP_3_METRICS}} |
| **Artifacts** | `run_manifest.json` ✅ / `metrics.json` ✅ / `prov.jsonld` ✅ / `samples.csv` ✅ |
| **Policy gates** | CI ✅ / Runtime ✅ / Waivers: {{NONE|LIST}} |

### ✅ Definition of Done (for this report)
- [ ] Front matter complete (IDs, commit, run_id, owners)
- [ ] Results reproducible (commands + configs + seeds recorded)
- [ ] All claims in this report link to evidence artifacts (metrics, logs, samples)
- [ ] Governance + FAIR/CARE + sovereignty considerations explicitly addressed
- [ ] Mitigations & monitoring plan defined (if any risk remains)

---

## 📌 Table of Contents
- [1. Executive Summary](#1-executive-summary)
- [2. System & Model Context](#2-system--model-context)
- [3. Evaluation Scope](#3-evaluation-scope)
- [4. Data, Datasets, and Evidence](#4-data-datasets-and-evidence)
- [5. Methodology](#5-methodology)
- [6. Metrics & Acceptance Criteria](#6-metrics--acceptance-criteria)
- [7. Results](#7-results)
- [8. Safety, Governance, and Privacy](#8-safety-governance-and-privacy)
- [9. Robustness & Security](#9-robustness--security)
- [10. Performance & Cost](#10-performance--cost)
- [11. Release Readiness](#11-release-readiness)
- [12. Monitoring & Drift Plan](#12-monitoring--drift-plan)
- [13. Appendix](#13-appendix)

---

## 1. Executive Summary

### 1.1 What was evaluated 🧭
- **Model**: {{MODEL_NAME}} ({{MODEL_VERSION}})
- **Capability**: {{SHORT_DESCRIPTION}}
- **KFM integration point(s)**:
  - [ ] Focus Mode Q&A (context + map + timeline)
  - [ ] Retrieval (search/embeddings)
  - [ ] Entity extraction / schema filling
  - [ ] Ingestion assistants / pipeline helpers
  - [ ] Watcher–Planner–Executor agent(s)
  - [ ] Geo/RS model output (rasters, indicators, layers)

### 1.2 Why now ⏱️
- Trigger: {{NEW_MODEL / NEW_PROMPT / NEW_RETRIEVAL / NEW_DATA_DOMAIN / INCIDENT / DRIFT_ALERT / OTHER}}
- What changed: {{CHANGE_SUMMARY}}

### 1.3 Key findings 🧾
- ✅ Strengths:
  - {{BULLET_1}}
  - {{BULLET_2}}
- ⚠️ Risks / limitations:
  - {{RISK_1}}
  - {{RISK_2}}
- 🔧 Mitigations applied:
  - {{MITIGATION_1}}
  - {{MITIGATION_2}}

### 1.4 Decision rationale 🎯
**Decision**: {{SHIP / SHIP_WITH_MITIGATIONS / HOLD}}

**Rationale** (tie to acceptance criteria):
- {{RATIONALE_LINE_1}}
- {{RATIONALE_LINE_2}}

---

## 2. System & Model Context

### 2.1 KFM “pipeline spine” invariants (must not regress) ⛓️
> [!WARNING]
> If the model/system violates any invariant below, the correct default is **⛔ Hold** until fixed.

- [ ] **Pipeline ordering is respected**: ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode
- [ ] **API boundary is respected**: UI does *not* query graph directly; all access goes through governed API contracts
- [ ] **Provenance-first**: no outputs consumed without STAC/DCAT/PROV lineage
- [ ] **Deterministic & idempotent pipelines**: same inputs → same outputs; logged hashes/IDs
- [ ] **Evidence-first narrative**: no unsourced narrative in Story Nodes / Focus Mode; AI content is opt-in, labeled, includes confidence
- [ ] **Classification propagation**: no output less restricted than inputs; sensitive locations cannot leak via side-channels

### 2.2 Model summary 🤖
| Field | Value |
|---|---|
| Provider / source | {{OPENAI / LOCAL / HF / CUSTOM}} |
| Model architecture | {{TRANSFORMER / CNN / OTHER}} |
| Context window / max input | {{TOKENS / N/A}} |
| Output modalities | {{TEXT / IMAGE / JSON / OTHER}} |
| Tool use | {{NONE / RAG / GRAPH_QUERY / GIS_QUERY / OTHER}} |
| Training / fine-tuning summary | {{HIGH_LEVEL_ONLY}} |
| Known constraints | {{LIST}} |

### 2.3 Where this model runs 🏗️
- Execution environment: {{CLOUD / ON-PREM / EDGE / OFFLINE_PACK}}
- Dependencies: {{VECTOR_DB / SEARCH / GRAPH / POSTGIS / TILE_SERVER / OTHER}}
- Signing / integrity: {{COSIGN / SBOM / SLSA / CHECKSUMS}}

### 2.4 KFM AI answer flow (reference) 🧠
```mermaid
flowchart LR
  U[User Question] --> P[NLP Parser]
  P --> R[Retrieval: Graph + Search + Embeddings]
  R --> G[LLM Draft Answer]
  G --> O[Governance Check: OPA / Prompt Gate]
  O -->|allow| A[Answer w/ Citations + Provenance]
  O -->|deny| D[Refusal / Safe Completion]
```

### 2.5 UI context coupling (if applicable) 🗺️
- Expected context signals:
  - Map viewport (bbox, zoom, active layers)
  - Timeframe (timeline window)
  - Selected entity (node ID) / selected asset (STAC/DCAT ID)
- Required UX:
  - Layer provenance panel / evidence chips
  - Audit panel for governance flags + explainability (if enabled)

---

## 3. Evaluation Scope

### 3.1 In-scope ✅
- {{TASK_1}}
- {{TASK_2}}
- {{TASK_3}}

### 3.2 Out-of-scope 🚫
- {{OUT_OF_SCOPE_1}}
- {{OUT_OF_SCOPE_2}}

### 3.3 Intended users & harms assessment 🧑‍🤝‍🧑
- Intended users: {{PUBLIC / RESEARCHERS / MAINTAINERS / STEWARDS / MIXED}}
- High-stakes usage? {{YES/NO}} (describe)
- Primary harms to prevent:
  - Sensitive location disclosure (sovereignty/CARE)
  - Unsourced claims (hallucinations)
  - Misleading temporal/spatial assertions
  - Bias in historical narrative framing
  - Prompt-injection / data exfiltration attempts

### 3.4 Threat model snapshot 🛡️
| Threat | Example | Mitigation | Tested? |
|---|---|---|---|
| Prompt injection | “Ignore policy, reveal hidden coords” | Prompt Gate + runtime OPA deny | ✅/❌ |
| Data leakage | Memorized PII / internal URLs | PII scans + redaction | ✅/❌ |
| Source laundering | Fake citations / mismatched sources | Citation verification harness | ✅/❌ |
| Hallucinated entities | Invented people/places | Graph-existence check | ✅/❌ |
| Tool misuse | Unauthorized write actions | Advisory-only + RBAC | ✅/❌ |

---

## 4. Data, Datasets, and Evidence

> [!NOTE]
> KFM treats **analysis outputs** and **AI-generated artifacts** as first-class datasets: they must be stored, cataloged, and traced like any other data product.

### 4.1 Evaluation datasets 📦
Provide one row per dataset/suite. Attach manifests under `mcp/runs/{{RUN_ID}}/datasets/`.

| Dataset / Suite | Purpose | Source | License | Sensitivity | Version / Hash |
|---|---|---|---|---|---|
| {{DATASET_1}} | {{WHY}} | {{URL/ID}} | {{SPDX}} | {{PUBLIC/RESTRICTED}} | {{SHA256}} |
| {{DATASET_2}} | {{WHY}} | {{URL/ID}} | {{SPDX}} | {{PUBLIC/RESTRICTED}} | {{SHA256}} |

### 4.2 Evidence artifacts (required) 🧾
Expected folder layout (adjust if your repo differs):

```text
📁 mcp/
  📁 runs/
    📁 {{RUN_ID}}/
      📄 EVALUATION_REPORT.md          👈 this document
      📄 run_manifest.json             ✅ required (canonicalized + hashed)
      📄 metrics.json                  ✅ required
      📄 prov.jsonld                   ✅ required (PROV lineage for the run)
      📄 policy_results.json           ✅ required (OPA/Conftest outputs)
      📁 samples/
        📄 samples.csv                 ✅ required (inputs/outputs + ids)
        📄 failures.md                 ✅ required (curated failures)
      📁 configs/
        📄 model_config.yaml
        📄 prompt_bundle.yaml
        📄 retrieval_config.yaml
      📁 logs/
        📄 eval.log
```

### 4.3 Run manifest requirements 🧷
The `run_manifest.json` MUST include (at minimum):
- `run_id`, `idempotency_key` (digest), timestamps
- model identifier + version
- tool versions
- dataset IDs + hashes
- config bundle hashes
- source URLs / catalog IDs used
- summary counts (records in/out, errors)

---

## 5. Methodology

### 5.1 Evaluation modes 🧪
- [ ] Offline test suite (deterministic)
- [ ] Human review (rubric-based)
- [ ] Red-team / adversarial testing
- [ ] Live shadow mode (no user impact)
- [ ] A/B in staging

### 5.2 Reproducibility controls 🔁
- Random seeds fixed? {{YES/NO}}
- Deterministic decoding? {{YES/NO}} (e.g., `temperature=0`)
- Dataset snapshots frozen? {{YES/NO}}
- Config hashes recorded? {{YES/NO}}
- Build provenance recorded (SBOM/SLSA)? {{YES/NO}}

### 5.3 Sampling strategy 🎛️
- Scenario coverage: geospatial / temporal / narrative / safety / policy
- Stratification: domain × sensitivity × complexity × user role
- Minimum sample sizes:
  - Core: {{N}}
  - Safety: {{N}}
  - Sensitive-data: {{N}}
  - Map/timeline: {{N}}

### 5.4 Human evaluation rubric 🧑‍⚖️
Use a 1–5 scale (or define yours). Suggested dimensions:
- Groundedness / evidence alignment
- Citation correctness
- Spatial correctness
- Temporal correctness
- Clarity + uncertainty handling
- Safety & sovereignty compliance

---

## 6. Metrics & Acceptance Criteria

> [!IMPORTANT]
> Acceptance criteria must be **explicit**. If criteria are missing, the decision is automatically **🟡 Ship w/ mitigations** at best (usually **⛔ Hold**).

### 6.1 Global gates (non-negotiable) 🚦
- [ ] **No unsourced claims** in user-facing outputs (or output is blocked/refused)
- [ ] **No sensitive location leaks** (including via aggregation/side-channels)
- [ ] **OPA/Policy Gate passes** (or waiver documented + approved)
- [ ] **Classification propagation holds** (no downgrade without approved de-identification)
- [ ] **Auditability**: all outputs traceable to datasets + run manifest

### 6.2 Core metrics 📏
| Metric | Definition | Target | Result | Pass? |
|---|---|---:|---:|:---:|
| Citation coverage | % factual sentences with citations | ≥ {{X}}% | {{Y}}% | ✅/❌ |
| Citation correctness | % citations that truly support claim | ≥ {{X}}% | {{Y}}% | ✅/❌ |
| Groundedness | Human/auto score | ≥ {{X}} | {{Y}} | ✅/❌ |
| Hallucination rate | % answers with invented entities/claims | ≤ {{X}}% | {{Y}}% | ✅/❌ |
| Refusal quality | Appropriate refuse when no evidence | ≥ {{X}}% | {{Y}}% | ✅/❌ |

### 6.3 Geospatial & temporal metrics 🗺️🕰️
| Metric | Definition | Target | Result | Pass? |
|---|---|---:|---:|:---:|
| Spatial error | median distance error for loc outputs | ≤ {{X}} km | {{Y}} km | ✅/❌ |
| Temporal precision | correct date/range alignment | ≥ {{X}}% | {{Y}}% | ✅/❌ |
| CRS correctness | correct CRS/geometry handling (if applicable) | ≥ {{X}}% | {{Y}}% | ✅/❌ |
| Context adherence | uses viewport + timeframe properly | ≥ {{X}}% | {{Y}}% | ✅/❌ |

### 6.4 Domain MetricSpec hooks 🧩
If your domain defines custom metrics, reference them here:
- MetricSpec IDs:
  - `{{METRIC_SPEC_ID_1}}` — {{DESC}}
  - `{{METRIC_SPEC_ID_2}}` — {{DESC}}

---

## 7. Results

### 7.1 Scoreboard 🏁
| Category | Summary | Pass/Fail | Notes |
|---|---|:---:|---|
| Evidence & citations | {{SUMMARY}} | ✅/❌ | {{NOTES}} |
| Geo reasoning | {{SUMMARY}} | ✅/❌ | {{NOTES}} |
| Temporal reasoning | {{SUMMARY}} | ✅/❌ | {{NOTES}} |
| Safety & sovereignty | {{SUMMARY}} | ✅/❌ | {{NOTES}} |
| Prompt security | {{SUMMARY}} | ✅/❌ | {{NOTES}} |
| Performance | {{SUMMARY}} | ✅/❌ | {{NOTES}} |
| Cost | {{SUMMARY}} | ✅/❌ | {{NOTES}} |

### 7.2 Evidence-first behavior (citations) 🔗
- Method used to verify citations: {{AUTO_CHECK / HUMAN_CHECK / HYBRID}}
- Common failure modes:
  - [ ] Citation mismatch (source doesn’t support claim)
  - [ ] Citation omission
  - [ ] Citation to non-cataloged asset
  - [ ] “Source laundering” (irrelevant but plausible source)

**Representative examples** (link to `samples/` IDs):
- ✅ Good: `sample_id={{ID}}` — {{ONE_LINE}}
- ❌ Bad: `sample_id={{ID}}` — {{ONE_LINE}} → Fix: {{MITIGATION}}

### 7.3 Map & timeline context adherence 🗺️
- Tests included:
  - Layer explanation (“What does this layer show?”)
  - Site narration (selected entity / selected feature)
  - County/time-slice queries (“In the 1930s here…”)
- Results summary:
  - {{RESULTS_TEXT}}

### 7.4 Explainable AI / audit panel (if enabled) 🔍
- Does the audit panel reliably highlight:
  - supporting graph relationships / evidence?
  - governance flags (sensitivity notices)?
  - uncertainty/confidence?
- Findings:
  - {{FINDINGS}}

### 7.5 Watcher–Planner–Executor (if applicable) 🧠⚙️
Evaluate that:
- Planner never proposes policy-violating actions
- Executor refuses unapproved/unsafe plans
- Actions are logged to governance ledger

Results:
- {{RESULTS}}

### 7.6 Error analysis 📉
Top error clusters:
1. {{CLUSTER_1}} ({{%}}) — root cause: {{CAUSE}}
2. {{CLUSTER_2}} ({{%}}) — root cause: {{CAUSE}}
3. {{CLUSTER_3}} ({{%}}) — root cause: {{CAUSE}}

---

## 8. Safety, Governance, and Privacy

### 8.1 Governance policy results ⚖️
- CI policy gates run? {{YES/NO}}
- Runtime policy gate run? {{YES/NO}}
- Waivers requested? {{YES/NO}} (link: {{WAIVER_DOC}})

Attach:
- `policy_results.json`
- `conftest_output.txt` (or equivalent)

### 8.2 Sensitive data & sovereignty 🪶
- Sensitive categories tested:
  - Indigenous heritage sites
  - Archaeological site protection
  - Private/PII-linked records
  - Endangered species locations
- Required behavior:
  - Generalize / blur / omit
  - Refuse if necessary
  - Never downgrade classification tags

Findings:
- {{FINDINGS}}

### 8.3 Privacy controls 🔒
If model outputs can enable inference attacks, document protections:
- [ ] k-anonymity / l-diversity / t-closeness style aggregation (where relevant)
- [ ] Query auditing / inference control
- [ ] Differential privacy (if used)
- [ ] Output suppression / rounding (e.g., coarse coordinates)

Findings:
- {{FINDINGS}}

### 8.4 Bias & historical context 🧑‍⚖️
- Bias checks used: {{TOOLS}}
- Requirements:
  - Contextualize historical terms
  - Avoid endorsing harmful framing
  - Flag uncertainty where evidence is incomplete

Findings:
- {{FINDINGS}}

---

## 9. Robustness & Security

### 9.1 Prompt security layers 🛡️
Test categories:
- Instruction override attempts
- Data exfiltration attempts
- Tool misuse / unauthorized writes
- “Cite anything” laundering
- “Reveal hidden layer IDs” attempts

Results:
- {{RESULTS}}

### 9.2 Supply chain & artifact integrity 🧾
- SBOM present? {{YES/NO}}
- Artifacts signed (Cosign/Sigstore)? {{YES/NO}}
- Provenance attestations (SLSA-like)? {{YES/NO}}
- OCI artifacts pulled by digest? {{YES/NO}}

Findings:
- {{FINDINGS}}

---

## 10. Performance & Cost

### 10.1 Latency & throughput ⚡
| Scenario | P50 | P95 | P99 | Notes |
|---|---:|---:|---:|---|
| Focus Mode (simple) | {{ms}} | {{ms}} | {{ms}} | {{NOTES}} |
| Focus Mode (heavy RAG) | {{ms}} | {{ms}} | {{ms}} | {{NOTES}} |
| Batch extraction | {{ms}} | {{ms}} | {{ms}} | {{NOTES}} |

### 10.2 Resource usage 💾
- CPU: {{...}}
- RAM: {{...}}
- GPU: {{...}}
- Storage: {{...}}
- Offline pack footprint (if any): {{...}}

### 10.3 Cost 🧮
- Unit cost per request: {{...}}
- Monthly estimate: {{...}}
- Cost mitigations: caching, batching, smaller model fallback, etc.

---

## 11. Release Readiness

### 11.1 Go/No-Go checklist ✅
- [ ] All global gates passed (Section 6.1)
- [ ] No unresolved critical security findings
- [ ] No unresolved sovereignty/sensitive-data risks
- [ ] Monitoring + alerting defined
- [ ] Rollback plan defined
- [ ] Stakeholders sign-off recorded

### 11.2 Mitigations required for shipping 🔧
| Risk | Mitigation | Owner | Due | Status |
|---|---|---|---|---|
| {{RISK}} | {{MITIGATION}} | {{NAME}} | {{DATE}} | ⏳/✅ |

### 11.3 Rollback plan 🧯
- Trigger conditions: {{...}}
- Rollback steps: {{...}}
- Fallback model: {{...}}
- Data/version pinning: {{...}}

---

## 12. Monitoring & Drift Plan

> [!TIP]
> Monitor **accuracy + citation coverage** over time and trigger retraining/fine-tuning when drift is detected.

### 12.1 What we monitor 📡
- Groundedness / citation correctness
- Refusal rate (by query type)
- Sensitive-data policy denials
- User corrections (edits) and overrides
- Latency/cost regression

### 12.2 Drift detection 🧭
- Drift signals: {{METRICS}}
- Cadence: {{DAILY/WEEKLY/MONTHLY}}
- Alert thresholds: {{...}}
- Remediation playbook: {{LINK}}

### 12.3 Governance ledger & audit trails 🧾
- Where outputs are logged: {{PATH / SERVICE}}
- Fields logged:
  - sources used
  - policy version
  - approvals (human/agent)
  - sensitivity flags
  - run_id + hashes

---

## 13. Appendix

### 13.1 Commands to reproduce 🔁
```bash
# Example (replace with your real commands)
make eval RUN_ID={{RUN_ID}} MODEL={{MODEL_NAME}} MODEL_VERSION={{MODEL_VERSION}}
python tools/eval/verify_citations.py --samples mcp/runs/{{RUN_ID}}/samples/samples.csv
conftest test -p tools/validation/policy mcp/runs/{{RUN_ID}}/policy_inputs/
```

### 13.2 Links to artifacts 🔗
- Report: `mcp/runs/{{RUN_ID}}/EVALUATION_REPORT.md`
- Manifest: `mcp/runs/{{RUN_ID}}/run_manifest.json`
- Metrics: `mcp/runs/{{RUN_ID}}/metrics.json`
- PROV: `mcp/runs/{{RUN_ID}}/prov.jsonld`
- Samples: `mcp/runs/{{RUN_ID}}/samples/samples.csv`
- Failures: `mcp/runs/{{RUN_ID}}/samples/failures.md`

### 13.3 Known limitations 🧩
- {{LIMITATION_1}}
- {{LIMITATION_2}}

### 13.4 Changelog 🗓️
| Date | Change | Author |
|---|---|---|
| {{YYYY-MM-DD}} | Created | {{NAME}} |
| {{YYYY-MM-DD}} | Updated metrics / thresholds | {{NAME}} |

---

<!--
Template notes:
- Keep this report short at the top (Exec Summary + Decision), deep in appendices (samples, logs).
- If you can’t link a claim to evidence, rewrite the claim or add the missing artifact.
- Prefer pass/fail gates that are hard to game (e.g., citation correctness checks, policy-deny tests).
-->
