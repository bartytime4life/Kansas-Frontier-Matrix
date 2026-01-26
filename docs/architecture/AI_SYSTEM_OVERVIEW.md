# 🧭🤖 AI System Overview
> **Kansas Frontier Matrix (KFM)** — **Focus Mode AI** is a provenance-first, evidence-backed, *advisory-only* assistant that helps users interpret maps, timelines, stories, and datasets without turning KFM into a black box.

---

## 🧷 At a glance

| 🏷️ Area | ✅ What KFM’s AI *does* | 🚫 What it *doesn’t do* |
|---|---|---|
| 🗣️ User experience | Answers natural-language questions *in context* (map viewport, selected layers, timeline) | Doesn’t “drive” the UI or change layers/time for the user |
| 🔎 Knowledge access | Uses hybrid retrieval across **PostGIS + Neo4j + Search Index + Vector Store** | Doesn’t browse the internet or pull from external sources by default |
| 🧾 Trust model | “**No citation, no answer**” + provenance panels + audit trails | Doesn’t present uncited facts as truth |
| 🛡️ Safety | Prompt Gate (input) + OPA (output) + allow/deny tool model | Doesn’t run arbitrary code, call HTTP tools, or access filesystem |
| 🦙 LLM runtime | Local-first LLM runtime via **Ollama** (pluggable) | Doesn’t require cloud AI to function in dev |

---

## 🎯 Purpose

Focus Mode AI exists to make KFM feel like a **knowledgeable research librarian + GIS analyst** living inside the map:

- Explain what a user is seeing (“What does this layer show in 1935 here?”)
- Summarize connected evidence (“What happened here around this time?”)
- Point to next steps (“Open this dataset / story node / provenance record”)
- Maintain accountability with citations, provenance metadata, and auditability

---

## 🧠 Core principles

### 1) 🔗 Provenance-first (chain-of-custody)
Every insight is tethered to:
- a dataset/story/document **ID**
- metadata (STAC/DCAT)
- lineage (PROV)
- governance checks (policy decisions)

### 2) 🧭 Advisory-only (human stays in control)
Focus Mode provides **guidance** and **interpretation**. It does *not* take actions on behalf of users.

### 3) 🧱 Layered architecture (clean boundaries)
The UI never calls an LLM directly. The AI is orchestrated **server-side** behind the governed API.

### 4) 🛡️ “Least privilege” AI
The model is treated like untrusted code:
- sandboxed
- tool access is explicit (allowlist)
- input/output validation enforced

### 5) 🧪 Reproducible + reviewable
AI behavior is versioned and auditable:
- prompts are versioned
- policies are versioned
- model versions are tracked
- responses can be logged with sources and policy results

---

## 🏗️ Where AI fits in the KFM system

KFM’s AI is **not** a separate “smart layer” floating above the platform. It is an **interface** into KFM’s governed data ecosystem.

### 🧩 Primary building blocks

- 🖥️ **UI (React/TypeScript)**  
  Focus Mode panel + chat UX + citation rendering + “audit/explain” UI affordances.
- 🚪 **Governed API (FastAPI + REST + GraphQL)**  
  The only gateway for data access, retrieval orchestration, and AI execution.
- 🗃️ **Datastores**
  - 🌍 **PostGIS** — geospatial + temporal queries, layers, tiles
  - 🕸️ **Neo4j** — entities/relationships, story graph, semantic traversal
  - 🧾 **Search Index** — full-text (docs/story content)
  - 🧠 **Vector Store** — semantic similarity (embeddings)
- 🦙 **LLM Runtime (Ollama)**  
  Local model serving + embeddings API + pluggable models.
- 🛡️ **Policy Layer (OPA + prompt guards)**  
  Enforces input/output rules, redactions, refusals, and governance constraints.
- 🧾 **Provenance + Governance Ledger**  
  Append-only event record of AI interactions and decisions.

---

## 🔄 End-to-end Focus Mode flow

```mermaid
flowchart LR
  U[👤 User] --> UI[🗺️ UI: Focus Mode Panel]
  UI -->|POST /focus-mode/query + map context| API[🚪 Governed API (FastAPI)]

  API --> PG[🧼 Prompt Gate\n(input sanitize + injection defense)]
  PG --> INT[🧭 Intent + Context Parser\n(entities, time, place, layers)]
  INT --> RET[🔎 Retrieval Layer\nNeo4j + PostGIS + Search + Vector]
  RET --> PB[🧩 Prompt Builder\n(prompt template + cited context)]
  PB --> LLM[🦙 Ollama\n(generate)]
  LLM --> OPA[🛡️ OPA Output Policy\n(redact / block / require citations)]
  OPA --> CITE[🔗 Citation + Provenance Enforcer\n(no citation => refuse)]
  CITE --> LED[🧾 Immutable AI Ledger\n(log Q/A, sources, policy hashes)]
  CITE --> UI2[🗺️ UI Render\n(answer + footnotes + audit panel)]
```

---

## 🗺️ Context awareness (the “map state is part of the question”)

Focus Mode is designed to interpret user questions relative to the UI state, such as:

- 📍 geographic focus (county/feature/viewport bounds)
- 🕰️ timeline slider (year/range)
- 🧱 active layers
- 📚 open story node / narrative context
- 🎛️ filters (if any)

This allows “here/now/this layer” questions to be resolved correctly (e.g., “What happened here around this time?”).

---

## 🔎 Retrieval & RAG architecture

### 🧬 Hybrid retrieval
Focus Mode uses multiple retrieval channels and merges them into a single “evidence pack”:

1) 🕸️ **Graph retrieval (Neo4j)**  
   Traverses relationships to find connected entities/events/places/sources.

2) 🌍 **Geospatial retrieval (PostGIS)**  
   Spatial + temporal queries: intersections, proximity, bounding boxes, time-filtered aggregates.

3) 🧾 **Text retrieval (Search Index)**  
   Full-text search over documents, narrative content, dataset descriptions.

4) 🧠 **Semantic retrieval (Vector Store)**  
   Embedding similarity search for “meaning-match” and paraphrases.

> ✅ The LLM is a **composer**, not a source of truth. Retrieval provides the facts; the model writes the explanation.

### 🧱 Evidence packaging rules
To keep provenance tight, retrieval results should be normalized into a common schema:

```json
{
  "evidence": [
    {
      "id": "kg:event:1856_black_jack",
      "type": "knowledge_graph",
      "title": "Battle of Black Jack (1856)",
      "snippet": "Event summary…",
      "provenance": {
        "source_ids": ["doc:news:1856_05_31", "dataset:places_kansas_v1"],
        "stac": "catalog/stac/…",
        "prov": "provenance/prov/…"
      }
    }
  ]
}
```

### 🧾 Citation mapping strategy
To prevent “citation theater” (random sources pasted at the end):

- Each retrieved chunk is assigned a stable `evidence_id`
- Prompt template instructs the model to cite with `[evidence_id]` markers
- Post-processing maps markers → structured citations list
- OPA enforces minimum citation rules (and optional stricter policies)

---

## 🦙 Model runtime & infrastructure (Ollama-first)

### ✅ Why Ollama
Ollama provides a **local** LLM runtime compatible with:
- offline development
- containerized deployment
- fast iteration without API keys
- model version switching

### 🧩 Model packaging
KFM can package a custom model with:
- a base model (`FROM llama…`)
- optional LoRA adapter (`ADAPTER …`)
- a template ensuring system instructions + citation behavior

<details>
<summary>🧱 Example Modelfile (illustrative)</summary>

```txt
FROM llama2:latest
ADAPTER ./kansas_finetune_lora.safetensors

TEMPLATE """{{ if .System }}<|system|>{{ .System }}<|end|>{{ end }}
{{ if .Prompt }}<|user|>{{ .Prompt }}<|end|>{{ end }}<|assistant|>"""

SYSTEM """You are KFM's assistant. Use ONLY provided context. Provide answers with sources."""
```
</details>

### 🧠 Embeddings + vector store
For semantic search, KFM generates embeddings using an embedding model (e.g., `all-minilm` / `mxbai-embed-large`) and stores vectors in a vector DB (e.g., **Chroma** or **Qdrant**).

---

## 🧩 Suggested backend module layout

The AI integration is designed to be modular so the LLM runtime can be swapped with minimal impact.

```text
📦 KFM-Backend/
├── 📂 api/
│   └── 📂 routes/
│       └── 🧠 focus_mode.py          # /focus-mode/query
├── 📂 ai/
│   ├── 🧠 focus_pipeline.py          # parse → retrieve → prompt → generate → postprocess
│   ├── 🔎 retrieval.py               # Neo4j + PostGIS + Search + Vector queries
│   ├── 🦙 ollama_client.py           # generate() + embed()
│   ├── 🛡 policy_checks.py           # OPA integration + rule helpers
│   └── 📂 prompt_templates/
│       └── 📝 focus_mode.txt
└── ...
```

---

## 🛡️ Governance & safety model

### 🧼 Prompt Gate (input security)
Incoming questions are sanitized before reaching the model:

- prompt-injection stripping / normalization
- profanity / hate / disallowed-content filtering
- PII/sensitive request detection (deny or safe-rewrite)

### 🧰 Tooling sandbox (deny-by-default)
Focus Mode is intentionally constrained:

- 🚫 no arbitrary code execution  
- 🚫 no direct filesystem or secret access  
- 🚫 no internet calls  
- ✅ only retrieval through governed KFM interfaces  
- ✅ any future tools must be explicitly allowlisted

### 🧾 OPA Output Policy (runtime enforcement)
OPA evaluates outputs **after generation**:

- block disallowed content
- redact sensitive details
- enforce “no citation, no answer”
- require hedging language for uncertainty (optional)
- require entity existence (optional anti-hallucination policy)

> 🧠 Policies are *code*, not “guidelines.” They’re versioned, testable, and auditable.

---

## 🔗 Provenance, auditability, and explainability

### 🧾 Citations are mandatory
- Answers are rendered with numbered footnotes and clickable sources
- If sufficient evidence cannot be retrieved, the assistant should refuse or express uncertainty (never fabricate)

### ⛓️ PROV lineage for AI outputs
Each AI response can be recorded as a provenance **Activity** that:
- consumed evidence Entities
- used model version X
- produced an answer Entity
- occurred at time T

### 🧾 Immutable governance ledger
Every Focus Mode interaction can be logged as an append-only record including:
- question (or privacy-preserving summary)
- answer
- source IDs used
- policy checks triggered
- policy version hashes
- model version hashes

### 🔍 “AI Audit Panel”
A user-facing explanation layer can surface:

- which sources were most influential
- which graph paths were traversed (simplified)
- any computations performed (with inputs shown)
- governance flags (e.g., “details omitted due to policy”)

---

## ✅ Quality assurance (QA) & human-in-the-loop

### 🤖 Automated QA gates (“watchers”)
Examples:
- AI output scanned for citations (and format)
- ingestion output checked for required metadata triplet
- sensitive terms flagged for review
- policy violations alerting

### 🧑‍⚖️ Human review & community governance
- PR-based review on data/pipeline/policy/prompt changes
- domain expert review for sensitive datasets
- governance committee/council can update policy packs

### 👍 User feedback loop
- “flag answer” flows into issue tracking
- feedback can improve retrieval, prompts, and policy

---

## 🧰 API contract: recommended shapes

### `POST /focus-mode/query`
**Inputs (recommended)**
- `question`: string
- `map_context`: viewport bounds, selected feature/county ID
- `time_context`: year/range
- `active_layers`: IDs
- `story_context`: open story node ID (optional)
- `user_context`: role/permissions (derived server-side)

**Outputs (recommended)**
- `answer_text`: string (with `[1]` footnotes)
- `citations`: list (IDs + titles + types)
- `audit`: optional (explainability bundle)
- `provenance`: optional (PROV activity ID, model version)

---

## 🧾 Data provenance requirements that support AI

Focus Mode inherits KFM’s “evidence-first” data pipeline:

- Immutable raw inputs
- Repeatable ETL/processing
- Catalog metadata (STAC/DCAT)
- Lineage records (PROV)
- Indexing into PostGIS/Neo4j/Search/Vector

> 🧱 AI reliability rises directly with data provenance quality.

---

## 🧭 Roadmap hooks (AI-related)

These are common extension points that fit the architecture without breaking governance:

- 🧑‍💼 **AI Data Steward**: metadata drafting + suggested entity linking on ingest
- 📓 **Notebook workflows**: reproducible analyses that read from KFM → compute → write back with provenance
- 🧠 **Domain models**: statistical/ML modules (e.g., regression, Bayesian models) publishing outputs as governed datasets
- 🧩 **Federation**: multi-region “Frontier Matrices” with cross-instance search (GraphQL federation)

---

## 📚 Project file library used to inform this overview

### 🏛️ KFM system design docs
- `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`
- `KFM AI Infrastructure – Ollama Integration Overview.pdf`
- `📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf`

### 🧪 R&D + documentation protocol resources
- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`
- `Data Mining Concepts & applictions.pdf`

### 🧰 Curated learning/reference portfolios (open in Adobe Reader)
- `AI Concepts & more.pdf`
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`
- `Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf`
- `Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf`
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`
- `Various programming langurages & resources 1.pdf`

---

## 🧾 Glossary

- **Focus Mode** — KFM’s AI assistant mode (context-aware Q&A with citations)
- **RAG** — Retrieval-Augmented Generation (retrieve evidence → LLM composes answer)
- **OPA** — Open Policy Agent (policy engine for runtime enforcement)
- **PROV** — W3C provenance model (activities/entities/agents + lineage)
- **STAC** — SpatioTemporal Asset Catalog (spatiotemporal dataset catalog metadata)
- **DCAT** — Data Catalog Vocabulary (dataset catalog metadata)
- **Neo4j** — graph DB for semantic relationships
- **PostGIS** — geospatial extension for PostgreSQL
- **Vector store** — embedding similarity DB (semantic retrieval)
- **Prompt Gate** — input sanitization + injection defense layer

---

## ✅ Implementation checklist (starter)

- [ ] Add `POST /focus-mode/query` route
- [ ] Implement `parse_intent(question, ui_context)`  
- [ ] Implement retrieval connectors: `neo4j()`, `postgis()`, `search()`, `vector()`
- [ ] Create `focus_mode.txt` prompt template with strict citation format
- [ ] Add Ollama client wrapper (`generate`, `embed`)
- [ ] Add output post-processor to normalize citations + structure response
- [ ] Integrate OPA policies (deny-by-default + citation enforcement)
- [ ] Add immutable ledger entry creation for each request (hash chaining)
- [ ] Add regression tests: “no citation → refuse” + “policy violation → redact/block”
- [ ] Add UI citation renderer + optional Audit Panel view

---