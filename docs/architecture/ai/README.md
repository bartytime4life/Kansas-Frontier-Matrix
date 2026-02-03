# 🧠🤖 AI Architecture — Kansas Frontier Matrix (KFM)

![Evidence First](https://img.shields.io/badge/evidence--first-no%20source%2C%20no%20answer-brightgreen)
![RAG](https://img.shields.io/badge/architecture-RAG-blue)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)
![Policy](https://img.shields.io/badge/governance-OPA%20policy%20gate-orange)
![Provenance](https://img.shields.io/badge/audit-W3C%20PROV--O%20ready-purple)

> [!NOTE]
> This folder documents **Focus Mode** (KFM’s AI assistant) and the **evidence-first** AI pipeline: retrieval ➜ grounded generation ➜ policy gating ➜ provenance logging.  
> The core requirement: **“No Source, No Answer.”**  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🔭 What lives in `docs/architecture/ai/`

This directory describes **how AI works in KFM**, not just what model is used:

- 🧩 **System contracts** (inputs/outputs, citation mapping, source objects)
- 🧼 **Prompt gate** (sanitize input, reduce prompt injection risk)
- 🔎 **Hybrid retrieval** (graph + spatial + full-text + vector search)
- 🦙 **Ollama LLM runtime** (local/self-hosted generation + embeddings)
- 🛡️ **OPA policy enforcement** (block uncited or unauthorized answers)
- ⛓️ **Provenance/audit** (trace answers to sources + model version)

---

## 🧭 Quick links

- 📄 `../AI_SYSTEM_OVERVIEW.md` (higher-level AI overview)
- 📄 `../system_overview.md` (whole system “truth path” & governance)
- 📄 `./OLLAMA_INTEGRATION.md` (Ollama + RAG specifics)

> [!TIP]
> Keep AI docs **implementation-grounded**: endpoints, contracts, policy rules, and “what must never happen” (hallucinated claims, uncited assertions, unauthorized disclosure).

---

## 🧩 Core principles

### 1) ✅ Evidence-first (Grounded outputs only)
- Every factual claim must be backed by a **retrieved source** and rendered as a **clickable citation marker** in the UI (e.g., `[1] [2]`).  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- If retrieval yields nothing relevant, the assistant must **refuse** (or request more context) rather than guess.  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 2) 🧱 Governed path (UI never talks to the LLM directly)
- The UI calls the **governed backend API**, and only the backend can talk to Ollama.  [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- The backend enforces **retrieval + policy checks + logging** before returning an answer.  [oai_citation:4‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 3) 🛡️ Policy gates are non-negotiable
- Answers without citations are rejected.  [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Role-based and sensitivity-based access controls must be enforced at the API/policy layer (not in the UI).

### 4) ♻️ Reproducible & auditable
- Log: question, sources, model name/tag, prompt version, policy decision, and response.  [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Store provenance in a form that can be inspected later (e.g., PROV-O compatible records).

### 5) 🧪 Trust and adoption mindset
Even outside healthcare, KFM is a **public-facing, high-trust system**. Best-practice framing emphasizes:
- **Safety, transparency, accountability, and ethical use** as prerequisites for acceptance.  [oai_citation:7‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)  
- Avoiding “pitfalls” (bias, bad data, opaque decisions) via deliberate practice and governance.  [oai_citation:8‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)

---

## 🗺️ End-to-end flow (Focus Mode)

```mermaid
flowchart LR
  UI["🗺️ React UI<br/>Focus Mode Panel"] -->|POST /focus-mode/query| API["🌐 FastAPI AI Orchestrator"]

  API --> PG["🧼 Prompt Gate<br/>(sanitize / neutralize attacks)"]
  API --> RET["🔎 Retrieval (Hybrid)<br/>Neo4j + PostGIS + Search + Vector"]
  RET --> SRC["📦 Curated SOURCES<br/>[1..N] short excerpts + IDs"]

  SRC --> LLM["🦙 Ollama<br/>/api/generate"]
  LLM --> DRAFT["📝 Draft answer<br/>with [#] citations"]

  DRAFT --> OPA["🛡️ Policy Gate (OPA)<br/>citations + auth + safety"]
  OPA -->|allow| RESP["📎 Response<br/>Answer + Citation Map"]
  OPA -->|deny| SAFE["🚫 Safe refusal / ask for more info"]

  RESP --> LOG["⛓️ Provenance Ledger<br/>(sources + model tag + prompt ver)"]
  SAFE --> LOG
```

**Pipeline specifics (as designed):**
- Request hits `POST /focus-mode/query` on the FastAPI server.  [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Prompt Gate cleanses malicious input (prompt injection attempts, profanity, etc.).  [oai_citation:10‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Retrieval gathers compact “high-signal” context from **four channels**: Neo4j, PostGIS, full-text search, vector similarity search.  [oai_citation:11‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Prompt includes the numbered SOURCES list `[1]...[N]` and instructs the model to cite every factual claim.  [oai_citation:12‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- OPA/policy logic blocks answers without citations and enforces access rules.  [oai_citation:13‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Provenance is recorded (sources + model tag + prompt version) to support audits.  [oai_citation:14‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧱 Component responsibilities

### 📌 FastAPI AI Orchestrator (server-side)
Owns the whole orchestration:
- Accepts question + map context (bbox, time slider, active layers, selected feature/county)
- Runs Prompt Gate
- Executes retrieval (hybrid)
- Builds prompt with **SOURCES**
- Calls Ollama `/api/generate`
- Validates citations + runs policy checks
- Returns answer + citation metadata mapping

### 🧼 Prompt Gate
Must:
- Strip/neutralize attempts to override system rules (“ignore citations…”, “reveal secrets…”, etc.)
- Remove profanity / disallowed content
- Prevent “prompt-only exfil” by ensuring the LLM sees only what it needs  [oai_citation:15‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🔎 Retrieval (Hybrid: structured + unstructured)
A typical retrieval bundle can include:
- **Neo4j**: entity relationships, events, document nodes
- **PostGIS**: spatial aggregations / filters (e.g., “count in county”)
- **Full-text**: keyword matches (documents, stories, archival text)
- **Vector store**: semantic similarity over chunked text via embeddings  [oai_citation:16‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🦙 Ollama (Local LLM runtime)
- Runs on-prem / private cloud and is container-friendly.  [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Supports:
  - **Generation models** (example: `kfm-llama2:latest`)
  - **Embedding models** (example: `mxbai-embed-large`)  [oai_citation:18‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Model selection is configuration-driven (env vars), enabling swapping without code changes.  [oai_citation:19‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🛡️ OPA Policy Gate
OPA (or equivalent governance layer) should validate:
- ✅ At least one citation marker exists (and ideally: citation coverage threshold)
- ✅ User role can access all cited sources
- ✅ No restricted content leaked
- ✅ Output format is valid for UI rendering

### ⛓️ Provenance Ledger
Records:
- query + map context
- list of sources used (IDs + metadata)
- model tag/version
- prompt template version
- policy decision + any redactions

Designed to align with **W3C PROV-O** style provenance graphs.  [oai_citation:20‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧾 Citation system (how “No Source, No Answer” works)

### Required behavior
- The model’s output **must include** numeric citation markers like `[1]`, `[2]`.  [oai_citation:21‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- The backend rejects answers that contain **no** citation markers.  [oai_citation:22‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Each marker maps to a real record:
  - Neo4j node ID
  - document ID
  - dataset reference  
  …and the UI renders clickable footnotes.  [oai_citation:23‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Suggested response contract (example)
```json
{
  "answer_markdown": "In the mid-1930s, this area experienced severe drought impacts [1].",
  "citations": [
    {
      "index": 1,
      "source_id": "dataset:ks_drought_1935",
      "title": "Kansas Drought Index (1935)",
      "type": "dataset",
      "license": "public-domain-or-open",
      "uri": "/api/v1/datasets/ks_drought_1935"
    }
  ],
  "model": "kfm-llama2:latest",
  "policy": { "decision": "allow" }
}
```

---

## 🦙 Model management (Modelfile, LoRA, version switching)

KFM anticipates **domain specialization** via a Modelfile + optional LoRA adapter. Example structure:  [oai_citation:24‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

```text
FROM llama2:latest
ADAPTER ./kansas_finetune_lora.safetensors

TEMPLATE """{{ if .System }}<|system|>{{ .System }}<|end|>{{ end }}
{{ if .Prompt }}<|user|>{{ .Prompt }}<|end|>{{ end }}<|assistant|>"""

SYSTEM """You are KFM's assistant, with access to Kansas data. Provide answers with sources."""
```

### Version switching & A/B testing
Ollama can host multiple models (small/fast vs large/accurate) and the backend can select a model by name/tag—supporting A/B tests and rollbacks.  [oai_citation:25‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🔍 Embeddings + vector index (semantic retrieval)

- Generate embeddings using Ollama embedding API (e.g., `/api/embed`) with an embedding model such as `mxbai-embed-large` or `all-minilm`.  [oai_citation:26‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Store embeddings in a vector DB (examples mentioned: **Chroma** or **Qdrant**) keyed by document chunk ID.  [oai_citation:27‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- At runtime:
  1. Embed the user query
  2. Fetch top-K similar chunks
  3. Merge with Neo4j/PostGIS retrieval results
  4. Pass a compact sources list to the LLM  [oai_citation:28‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## ⚡ Performance considerations

### 🧠 Context size
- Prefer models with larger context windows when answers require many supporting excerpts.
- Configure `num_ctx` (or equivalent) in the Modelfile when needed.  [oai_citation:29‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🧊 Caching (application layer)
Because Ollama may not cache past queries internally, KFM caches:
- repeated retrieval bundles (common topics like “1930s drought”)
- session context for follow-ups  
to avoid repeating heavy retrieval steps.  [oai_citation:30‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧪 Testing & evaluation checklist

> [!IMPORTANT]
> “Works on my machine” is not acceptable for a high-trust assistant. Measure groundedness.

### Minimum automated checks
- ✅ **Citation presence**: reject uncited answers (hard fail)
- ✅ **Citation validity**: every `[n]` maps to a real source ID
- ✅ **Authorization**: user role can access every cited source
- ✅ **Groundedness smoke tests**: golden Q/A set with expected citations
- ✅ **Prompt injection tests**: “ignore policies”, “reveal hidden info”, etc.

### Trust-oriented best practices (adapted to KFM)
- Bias & representativeness matter when building models on real-world data.  [oai_citation:31‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)  
- Transparency and accountability improve acceptance and long-term adoption.  [oai_citation:32‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)

---

## 🧰 Local development (conceptual)

> [!NOTE]
> Exact commands may differ by environment; keep configs in `.env` and document them in your compose files.

Typical env vars:
```bash
# LLM
OLLAMA_API_URL=http://ollama:11434
FOCUS_MODE_MODEL=kfm-llama2:latest
FOCUS_MODE_EMBED_MODEL=mxbai-embed-large

# Retrieval stores (examples)
NEO4J_URI=bolt://neo4j:7687
POSTGIS_DSN=postgresql://postgres:postgres@postgis:5432/kfm
VECTOR_DB_URL=http://qdrant:6333

# Policy
OPA_URL=http://opa:8181
```

---

## 📚 References (project source material)

- **Kansas Frontier Matrix — Comprehensive System Documentation**  [oai_citation:33‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- **Artificial Intelligence & Machine Learning in Health Care & Medical Sciences** (trust/best-practice framing, pitfalls)  [oai_citation:34‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)  

---

## ✅ Suggested next docs to add (if missing)

<details>
<summary>📁 Proposed files to grow this folder</summary>

- `PROMPT_GATE.md` — sanitization rules, examples, unit tests
- `POLICY_RULES.md` — OPA rules (citation enforcement, access control, redaction)
- `RAG_RETRIEVAL.md` — retrieval ranking, chunking strategy, vector DB schema
- `EVAL.md` — evaluation harness, golden sets, metrics (groundedness/citation precision)
- `RUNBOOK.md` — ops: model upgrades, rollbacks, incident response for hallucinations

</details>