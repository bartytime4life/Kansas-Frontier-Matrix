# 🧠 Model Cards (MCP)

![MCP](https://img.shields.io/badge/MCP-Model%20Cards-blue)
![Reproducible](https://img.shields.io/badge/Reproducibility-First-success)
![Governance](https://img.shields.io/badge/Governance-Required-orange)
![Provenance](https://img.shields.io/badge/Provenance-Never%20Optional-purple)

Welcome to `mcp/model_cards/` 📁 — the **single source of truth** for every AI/ML model used anywhere in this repo (pipelines, experiments, Focus Mode, embeddings, NER, OCR helpers, rerankers, etc.).

A **model card** is a short, standardized, version-controlled document that explains:

- ✅ **What** the model is (family/version/weights/runtime)
- ✅ **How** we run it (Ollama/local runtime, configs, parameters)
- ✅ **Where** it came from (license, provenance, training/fine-tuning notes)
- ✅ **What it’s allowed to do** in KFM/Kansas-Matrix-System (tools, access boundaries)
- ✅ **How well it performs** (evaluation + known failure modes)
- ✅ **How to interpret outputs safely** (limits, risks, redaction expectations)

---

## 🎯 Non‑Negotiables

> [!IMPORTANT]
> If a model is used by **code** or influences **user-facing output**, it **must** have a model card.

**Minimum bar (required):**
- **Intended Use** + **Out-of-Scope Use**
- **Model Details** (identity + runtime + version/variant)
- **Data / Provenance** (what’s known + what’s unknown)
- **Evaluation** (even if “informal baseline” at first)
- **Limitations & Risks** (hallucination modes, bias, edge cases)
- **KFM Integration Contract** (tools/APIs, redaction, citation behavior)

---

## 🗂️ Recommended Folder Layout

You can keep it flat or grouped. Grouped is preferred as the library grows:

```text
📁 mcp/
└─ 📁 model_cards/                           🧾 model documentation (capabilities, evals, safety, provenance)
   ├─ 📄 README.md                            📘 how model cards are organized + required fields
   ├─ 📁 templates/                           🧩 “copy-me” templates for consistency
   │  ├─ 📄 MODEL_CARD_TEMPLATE.md             🪪 standard model card template
   │  └─ 📄 EVAL_REPORT_TEMPLATE.md            📊 evaluation report template
   ├─ 📁 llm/                                 🤖 large language models (chat, agents, Focus Mode)
   │  ├─ 📄 focus_mode__<model_id>.md          🧠 Focus Mode deployment card (policy + citations + tools)
   │  └─ 📄 agents__<model_id>.md              🧩 agent runtime card (roles, permissions, guardrails)
   ├─ 📁 embeddings/                          🧲 embedding models (vectorization + retrieval)
   │  └─ 📄 <model_id>.md                      📘 embedding model card (dims, distance, evals)
   ├─ 📁 nlp/                                 🧠 classic NLP models (task-specific)
   │  ├─ 📄 ner__<model_id>.md                 📍 NER model card (labels, coverage, evals)
   │  └─ 📄 ocr_post__<model_id>.md            🧾 OCR post-processing card (rules, evals, failure modes)
   └─ 📁 vision/                              👁️ vision models (detection, segmentation, VQA)
      └─ 📄 <model_id>.md                      📘 vision model card (inputs, limits, evals, safety)
```

**Naming convention (recommended):**
- `category__purpose__model_id.md` (best for searching)
- Use `__` to keep filenames grep-friendly
- Keep `model_id` stable across upgrades; track upgrades in **Changelog**

Examples:
- `llm/focus_mode__gpt-oss__q4_k_m.md`
- `embeddings/nomic-embed-text-v1.5.md`
- `nlp/ner__spacy_en_core_web_trf.md`

---

## 🧾 Model Card Format

We use **Markdown** with optional **YAML front-matter** (recommended) for machine parsing.

### ✅ YAML Front-Matter (Recommended)

```yaml
---
id: llm.focus_mode.gpt-oss.q4_k_m
display_name: "GPT-OSS (Focus Mode)"
category: llm
purpose: focus_mode
runtime: ollama
source: "ollama://gpt-oss:latest"   # or huggingface/model@sha, local path, etc.
weights_version: "unknown-or-link"
quantization: "Q4_K_M"
context_window: 8192
license: "UNKNOWN (must fill)"
owners:
  - "@maintainer_handle"
last_reviewed: "YYYY-MM-DD"
risk_tier: "LOW | MEDIUM | HIGH"
---
```

> [!TIP]
> If you don’t know something (license details, training data specifics), **say so explicitly** and add a TODO. Unknown is better than guessed.

---

## 🧩 Required Sections

Copy/paste this outline into each model card:

1. **Summary**
2. **Intended Use**
3. **Out-of-Scope / Prohibited Use**
4. **Model Details**
   - family / variant / version
   - runtime (Ollama/local/etc.)
   - parameters (temperature defaults, max tokens, system prompt policy)
5. **Training / Fine-Tuning Data**
   - what’s known (and what isn’t)
   - data licensing notes
6. **Evaluation**
   - datasets/tasks
   - metrics (or qualitative rubric)
   - “known good” and “known bad” examples
7. **Limitations**
   - common error patterns
   - domain weaknesses (dates, OCR noise, historical spelling, etc.)
8. **Risks & Mitigations**
   - hallucination controls
   - privacy/redaction expectations
   - bias / representational harms
9. **KFM / Kansas-Matrix Integration Contract**
   - allowed tools/APIs
   - citation requirements
   - “fail-closed” behavior expectations
   - logging / audit hooks (PROV + experiment logs)
10. **Reproducibility**
   - exact run commands
   - pinned versions / hashes
   - hardware notes (VRAM/RAM, CPU expectations)
11. **Changelog**
12. **References**
   - papers/docs
   - internal experiment reports (link into `mcp/experiments/`)

---

## 🔌 KFM Integration Contract (What Every Card Must Declare)

Every model card must explicitly answer:

### 1) What data can this model see?
- ✅ Only **approved** tool outputs and governed API responses
- ✅ No direct reads of restricted files or raw secrets
- ✅ State whether prompts include **retrieved context** (RAG) and from where

### 2) What tools can it call (if any)?
If the model is used agentically (tool calling), list:
- tool name
- inputs/outputs schema
- rate limits / cost notes
- safety boundaries (redaction, allowlist queries)

### 3) What must the UI/user see?
For user-facing models:
- citation expectations
- how uncertainty is communicated
- what “refusal” looks like

> [!NOTE]
> If the model can’t reliably cite or is prone to confident errors, the card must document the mitigation (stronger retrieval, stricter prompting, output validators, policy checks, etc.).

---

## 🧪 Evaluation: Minimum Viable Standard

At minimum, include:
- A **small benchmark set** (even 20–50 prompts)
- A **scoring rubric** (Correct / Partially Correct / Incorrect / Unsupported)
- A **failure log** (what broke and why)
- A link to the corresponding experiment record:
  - `mcp/experiments/<date>__<experiment_name>/README.md`

**For Focus Mode models**, also test:
- citation fidelity (does it cite the right artifact?)
- tool calling correctness (no invented tool outputs)
- refusal behavior (sensitive data, policy-prohibited asks)
- geospatial reasoning sanity checks (coords, distances, projections)

---

## ✅ Add / Update Workflow

### Adding a new model
1. Create a model card in the right category folder
2. Add or link:
   - eval report (or baseline rubric + examples)
   - experiment log under `mcp/experiments/`
3. Update configuration that selects the model (wherever it lives)
4. If the model is agentic:
   - update tool allowlists / policies
   - ensure logging + provenance hooks exist

### Updating an existing model
Update the card when you change **anything** that affects behavior:
- weights/version/quantization
- prompts/system policies
- tool schema
- retrieval strategy
- redaction rules
- evaluation results

Add a changelog entry with:
- what changed
- why
- expected impact
- links to experiment/eval artifacts

---

## 🧰 Templates

You should maintain these in `mcp/model_cards/templates/`:

- `MODEL_CARD_TEMPLATE.md`
- `EVAL_REPORT_TEMPLATE.md`

Quick starter (drop-in):

<details>
<summary><strong>📄 Minimal Model Card Skeleton</strong> (click to expand)</summary>

```markdown
---
id: <fill>
display_name: "<fill>"
category: <llm|embeddings|nlp|vision|other>
runtime: <ollama|python|other>
license: "<fill>"
owners: ["@<fill>"]
last_reviewed: "YYYY-MM-DD"
risk_tier: "LOW|MEDIUM|HIGH"
---

# Summary
# Intended Use
# Out-of-Scope Use
# Model Details
# Training / Data Notes
# Evaluation
# Limitations
# Risks & Mitigations
# KFM Integration Contract
# Reproducibility
# Changelog
# References
```
</details>

---

## 🔎 Quick Index Tips

- Keep `id:` stable and grep-friendly
- Prefer **one model = one card**
- Link cards from:
  - `mcp/README.md` (high-level)
  - relevant SOPs (e.g., model update process)
  - experiment folders

---

## 📍 Where This Fits in the Bigger System

Model cards connect the dots between:
- 🧪 **experiments** (`mcp/experiments/`)
- 🧭 **SOPs** (`mcp/sops/`)
- 🧾 **governance + policies** (policy-as-code, redaction rules)
- 🧬 **provenance** (PROV logs + dataset lineage)
- 🗺️ **Focus Mode behavior** (tool boundaries + citations)

If it’s not documented here, it’s not “real” yet 🚫✨
