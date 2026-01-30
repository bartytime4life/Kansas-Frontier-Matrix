# 🧠📇 MCP Model Cards

![MCP](https://img.shields.io/badge/MCP-Documentation--First-2ea44f)
![Provenance](https://img.shields.io/badge/Provenance-First-blue)
![AI](https://img.shields.io/badge/AI-Citations%20Required-orange)
![Runtime](https://img.shields.io/badge/Runtime-Ollama-000000)
![Status](https://img.shields.io/badge/Status-Active-informational)

Welcome to `mcp/model_cards/` — the **single source of truth** for documenting every ML/AI/LLM model used in this repo.  
Model cards keep our AI components **transparent, reproducible, auditable, and governable** ✅

> [!IMPORTANT]
> If a model influences **data ingestion**, **entity extraction**, **ranking**, **retrieval**, **summarization**, **classification**, or **user-facing answers**… it **must** have a model card.

---

## 🧭 Quick Navigation

- [📌 What lives here](#-what-lives-here)
- [🎯 What is a model card](#-what-is-a-model-card)
- [🧱 Folder structure](#-folder-structure)
- [🏁 Quickstart](#-quickstart)
- [🧾 Model card template](#-model-card-template)
- [✅ Definition of Done](#-definition-of-done)
- [🧪 How model cards relate to experiments](#-how-model-cards-relate-to-experiments)
- [🛡️ Governance + safety expectations](#️-governance--safety-expectations)
- [🧰 Ollama-specific guidance](#-ollama-specific-guidance)
- [🧩 FAQ](#-faq)

---

## 📌 What lives here

This folder contains **documentation**, not raw weights.

Typical contents per model:

- 📄 `model_card.md` → the actual model card (required)
- 🧪 `eval/` → metrics, test sets (or pointers), and reproducible evaluation commands
- 🧵 `prompts/` → system prompts / few-shots / tool schemas used in production
- 🧱 `ollama/` → `Modelfile` / runtime config when model is served via Ollama
- 🧾 `datasets/` → links to datasheets for training/eval data (when we curate/compile it)
- 🧩 `integrations/` → notes about how it plugs into the platform (API endpoints, tool allowlists)

---

## 🎯 What is a model card

A model card is a **standardized, human-readable spec** that answers:

- **What is this model?** (origin + purpose)
- **What data shaped it?** (training + finetuning + eval sets)
- **How well does it work?** (metrics + qualitative examples)
- **Where does it fail?** (limitations, biases, known issues)
- **When should / shouldn’t we use it?** (intended vs out-of-scope use)
- **How is it deployed here?** (runtime config, prompts, tools, guardrails)
- **How do we reproduce results?** (versions, hashes, commands, environment)

If we ever have to ask:
> “Why did the AI do that?”  
…the model card is where we start. 🔍

---

## 🧱 Folder structure

Recommended layout (copy/paste-friendly):

```text
mcp/
  model_cards/
    README.md
    _TEMPLATE/
      model_card.md
      eval/
        README.md
      prompts/
        system.md
        few_shots.md
      ollama/
        Modelfile
    focus_mode_llm__qwen3__v1/
      model_card.md
      prompts/
        system.md
        tool_schema.json
      eval/
        metrics.json
        golden_questions.md
      ollama/
        Modelfile
    ner_place_names__spacy__v2/
      model_card.md
      eval/
        metrics.json
        confusion_matrix.csv
```

> [!NOTE]
> If your model is “just” an embeddings model or a reranker model — it still needs a card.  
> Retrieval models directly affect what evidence is surfaced and what answers become possible.

---

## 🏁 Quickstart

### 1) Create a new model folder 📁

Use a name like:

- `task__modelname__v#`
- `task__vendor__model__v#`
- `component__model__variant__v#`

Examples:
- `focus_mode_llm__gpt-oss__v1`
- `embeddings__nomic-embed-text__v1`
- `ocr__tesseract__v3`
- `reranker__bge-reranker__v2`

### 2) Copy the template 🧬

```bash
cp -R mcp/model_cards/_TEMPLATE mcp/model_cards/<your_model_folder>
mv mcp/model_cards/<your_model_folder>/model_card.md mcp/model_cards/<your_model_folder>/model_card.md
```

(Then edit the card.)

### 3) Link your experiments 🧪

Any meaningful change requires:
- a **model card update**
- an **experiment report** (see `mcp/experiments/`)

### 4) Keep runtime + prompts versioned 🔧

If the model is used in production behavior:
- commit the prompt(s)
- commit tool schemas / allowlists
- commit runtime config (Ollama Modelfile, env vars, etc.)

---

## 🧾 Model card template

Below is the **minimum viable** model card.  
Copy this into `model_card.md` inside your model folder.

```markdown
---
name: <human-friendly name>
id: <stable-id-like focus_mode_llm__qwen3__v1>
task: <LLM QA | NER | OCR | embeddings | reranking | classification | etc>
owner: <team/person or "community">
status: <proposed | active | deprecated>
last_updated: YYYY-MM-DD
---

# 🧠 Model Summary
**One-liner:** What it does and where it is used.

## 🎯 Intended Use
- ✅ In-scope:
  - ...
- 🚫 Out-of-scope / not allowed:
  - ...

## 🧬 Model Details
- Architecture / family:
- Version / tag:
- Context window (if LLM):
- Quantization (if applicable):
- License:

## 🧾 Data
### Training / Finetuning Data
- What datasets (or sources) shaped the model?
- If internal/curated: link datasheets in `datasets/`
- Sensitive data notes (if any):

### Evaluation Data
- What test sets were used?
- Are they representative of frontier-era spelling, OCR noise, etc.?

## 📈 Evaluation
- Metrics (with date + commit hash):
- Qualitative examples (good + bad):
- Regression checks:

## ⚠️ Limitations & Failure Modes
- Known blind spots:
- Bias / skew risks:
- Hallucination risks (for LLMs):
- Geography-specific pitfalls:

## 🧰 Runtime & Integration
### How it runs
- Runtime: Ollama | Python | TorchServe | etc.
- Env vars:
- Hardware assumptions:

### Prompts / Policies / Tooling (if LLM)
- System prompt file(s):
- Tool allowlist:
- Citation requirements:
- Any special guardrails:

## 🔁 Reproducibility
- Repo commit:
- Build instructions:
- Exact commands to reproduce eval:

## 🧯 Safety, Ethics, Governance
- Data access tier assumptions:
- CARE / FAIR considerations:
- Refusal / safety behavior expectations:

## 🗂️ Change Log
- v1 (YYYY-MM-DD): ...
- v2 (YYYY-MM-DD): ...
```

---

## ✅ Definition of Done

Before a model is considered **MCP-ready**, confirm:

- [ ] 📄 `model_card.md` exists and is filled out
- [ ] 🧪 Evaluation results are included (or reproducible pointers)
- [ ] 🧵 Prompts / tool schemas are committed (if applicable)
- [ ] 🔧 Runtime config is captured (Ollama Modelfile / env vars / params)
- [ ] 🧾 Data lineage is described (and datasheets linked when we curate data)
- [ ] 🛡️ Limitations and out-of-scope uses are explicit
- [ ] 🔁 Reproduction steps work from a clean machine/container
- [ ] 🧭 “How this plugs into the platform” is documented

> [!TIP]
> If you cannot share an eval dataset publicly, you can still be reproducible:
> - document how it’s generated
> - provide hashes for private artifacts
> - include a public “proxy” test set where possible

---

## 🧪 How model cards relate to experiments

Model cards tell the **what** and the **how**.  
Experiment reports explain the **why**.

📁 Expected partner folders:
- `mcp/experiments/` → hypotheses, methods, results, uncertainty
- `mcp/sops/` → repeatable procedures (ingestion, QC, retraining, deployment)
- `data/provenance/` → provenance logs for datasets and pipeline runs (when applicable)

**Rule of thumb:**  
If you changed anything that could alter outputs (weights, prompts, retrieval logic, tool access, thresholds)…  
👉 write an experiment report and update the card.

---

## 🛡️ Governance + safety expectations

This project treats AI as a **constrained analyst**, not an oracle.

Minimum expectations for any model used in user-facing workflows:

- 🧾 **Citations required** for factual claims (LLM answers must “show their work”)
- 🔐 **Tool-gated access** only (models should not bypass governance layers)
- 🧭 **Provenance-first mindset** (trace inputs → transformations → outputs)
- 🧨 **Sensitive data care**
  - no leaking private or restricted information
  - honor community control and takedown/withdrawal rules
  - document any special handling (redaction, aggregation, refusal behavior)

---

## 🧰 Ollama-specific guidance

Many KMS/KFM components run locally via **Ollama** for privacy and offline capability.

### What to record in a model card (Ollama)

At minimum, include:

- `ollama` model identifier + tag (example: `qwen3:14b`, `llama3.1:8b`)
- quantization level (if known)
- context length assumptions
- runtime parameters (temperature, top_p, mirostat, etc.)
- whether “thinking”/reasoning traces are enabled
- whether tool-calling is enabled (and which tools are allowed)

### Suggested files

- `ollama/Modelfile` ✅ (preferred)
- `prompts/system.md` ✅
- `prompts/tool_schema.json` ✅ (if the model calls tools)
- `eval/metrics.json` ✅

> [!WARNING]
> Ollama may support optional tool execution (e.g., web search, python execution) depending on model + configuration.  
> **Do not enable** any tool capability in production unless it is explicitly permitted by repo policy and documented in the model card.

---

## 🧩 FAQ

### “Do we need model cards for third‑party models we didn’t train?”
✅ Yes. Even if we didn’t train it, we still:
- deploy it
- configure it
- choose how it’s prompted
- decide what it can access
- decide how outputs affect users

That makes it part of the system and it needs documentation.

### “Where do we put big artifacts?”
Not in Git unless they’re small. Prefer:
- external artifact storage (with hashes)
- DVC (if used in this repo)
- reproducible build instructions that pull artifacts on demand

### “What if the model is deprecated?”
Mark it clearly:
- `status: deprecated`
- explain why
- link to the replacement model card
- note any migration steps

---

## 🗺️ Next Step: Add your first card

If no cards exist yet, start with:
1) an **LLM card** for the Focus Mode / assistant model  
2) an **embeddings card** for semantic search / retrieval  
3) an **NER/OCR card** if we extract entities from historical documents

Happy documenting 🚀