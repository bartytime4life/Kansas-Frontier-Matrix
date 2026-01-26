# 🧠 tools/ai — Evidence‑Backed AI Toolbelt

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-1f6feb)
![AI](https://img.shields.io/badge/AI-Focus%20Mode%20%7C%20RAG-6f42c1)
![Policy](https://img.shields.io/badge/Policy-OPA%20(Policy%20as%20Code)-0b7285)
![Runtime](https://img.shields.io/badge/Runtime-Ollama%20(Local%20LLM)-f97316)
![Trust](https://img.shields.io/badge/Trust-Provenance%E2%80%91First%20%F0%9F%91%A3-2ea44f)
![Data](https://img.shields.io/badge/Data-STAC%20%2B%20DCAT%20%2B%20PROV-0ea5e9)

> [!IMPORTANT]
> **KFM AI is advisory-only and evidence-first.** Every answer must include citations, and any output is policy-checked before it reaches the UI.

---

## 🎯 What this folder is for

`tools/ai/` is the **developer toolbelt + runbook** for KFM’s AI features (especially **Focus Mode**), including:

- 🧩 **Local model runtime** guidance (Ollama) and deployment patterns  
- 🔎 **Retrieval + indexing** helpers (hybrid: graph + spatial + text/vector)  
- 🛡 **Governance + safety** (Prompt Gate + OPA policy checks + allow/deny tool controls)  
- 🧪 **Evaluation & reproducibility** workflows (golden sets, deterministic scenarios, audits)  
- 🧾 **Provenance enforcement** (“no citation, no answer”) and logging conventions

> [!NOTE]
> This README defines the **contract** for AI tooling in KFM. If your repo structure differs, keep the principles and update paths accordingly.

---

## 🧭 North Star rules (non‑negotiables)

### ✅ Evidence-first (no black boxes)
- All AI answers must cite supporting KFM sources (footnote-style, e.g. `[1]`, `[2]`).
- Datasets are packaged with metadata + lineage via the **catalog triplet**: **STAC + DCAT + PROV**.
- If a claim can’t be supported by retrieved evidence, the assistant must refuse or clearly express uncertainty.

### ✅ Least privilege by default
- Focus Mode’s model runtime is **sandboxed**: no internet, no filesystem, no arbitrary tool execution.
- Any future tool use is gated via explicit **allowlists**.

### ✅ Policy as code (OPA)
- Inputs are filtered through a **Prompt Gate** (prompt injection + disallowed content).
- Outputs are checked by **OPA** rules that can **block, redact, or require safe fallbacks**.

### ✅ Reproducible by design
- Pipelines and modeling runs should be deterministic (seeded, frozen dependencies, controlled external calls).
- Scenario testing stays isolated until humans approve merges.

---

## 🧠 How Focus Mode works

### 🧩 High-level pipeline

```mermaid
flowchart LR
  U[👤 User] --> UI[🖥️ Focus Mode UI Panel]
  UI --> PG[🧼 Prompt Gate\nsanitize + normalize input]
  PG --> RET[🔎 Hybrid Retrieval\nNeo4j + PostGIS + Search/Vector]
  RET --> CTX[📦 Context Bundle\nsnippets + IDs + metadata]
  CTX --> LLM[🤖 LLM Runtime\n(Ollama / local)]
  LLM --> DRAFT[📝 Draft Answer\n+ citations]
  DRAFT --> OPA[🛡 OPA Policy Check\nblock/redact/allow]
  OPA --> LEDGER[🧾 PROV/AI Ledger\nhash + version metadata]
  OPA --> UI
```

### 🔍 Hybrid retrieval (why it matters)
Focus Mode is designed to “ground” answers using:
- 🧠 **Knowledge graph** relationships (Neo4j)  
- 🗺 **Spatial queries** (PostGIS)  
- 🧾 **Full-text + vector similarity** (search index + embeddings)  

Then it packages evidence as a **context bundle** so the LLM answers from *KFM data*, not vibes.

---

## 🗂️ Suggested layout inside `tools/ai/`

> [!TIP]
> If the repo already has a different layout, treat this as a **recommended standard**. The key is: prompts, policies, retrieval, evals are versioned and testable.

```text
tools/ai/
├── 📄 README.md
├── 📁 ollama/                      # local LLM runtime helpers
│   ├── 📄 docker-compose.ollama.yml
│   ├── 📄 Modelfile                # optional: pinned settings / system prompt
│   └── 📄 models.md                # approved models list + pinning notes
├── 📁 prompts/                     # system prompts + templates (versioned)
│   ├── 📄 focus_mode.system.md
│   ├── 📄 focus_mode.user.md
│   └── 📄 citations.contract.md
├── 📁 policies/                    # governance as code
│   ├── 📁 opa/
│   │   ├── 📄 ai_output.rego        # citation + safety rules
│   │   ├── 📄 sensitive_geo.rego    # redaction rules (sacred sites, etc.)
│   │   └── 📄 pii.rego              # PII protections
│   └── 📁 schemas/                 # JSON Schema / SHACL / validators
├── 📁 retrieval/                   # indexing + retrieval glue
│   ├── 📄 build_index.py
│   ├── 📄 embed_corpus.py
│   └── 📄 kg_query_templates.cypher
├── 📁 eval/                        # eval harness + golden sets
│   ├── 📁 golden/
│   ├── 📁 datasets/
│   └── 📄 run_eval.py
└── 📁 runbooks/                    # operational playbooks
    ├── 📄 incident_ai.md
    ├── 📄 model_upgrade.md
    └── 📄 policy_changes.md
```

---

## 🚀 Quickstart (local)

### 1) Start an LLM runtime (Ollama)

You can run Ollama either as:
- 🧑‍💻 **Host service** (`ollama serve`)  
- 🐳 **Docker container** (recommended for consistent dev environments)

#### 🐳 Example `docker-compose` for Ollama

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    environment:
      - OLLAMA_KEEP_ALIVE=24h
    deploy:
      resources:
        limits:
          memory: 16g
volumes:
  ollama_data:
```

> [!IMPORTANT]
> In production, prefer **pinning** images/models by digest + recording versions in provenance logs (model upgrades must be auditable).

---

### 2) Point KFM to the runtime

Typical env vars (names may differ—standardize them in your repo):

```bash
export OLLAMA_API_URL="http://localhost:11434"
export KFM_AI_MODEL="your-chat-model"
export KFM_EMBED_MODEL="your-embedding-model"
```

---

### 3) Smoke test (LLM reachable)

```bash
curl -s "$OLLAMA_API_URL/api/tags" | head
```

If that returns JSON, the runtime is up ✅

---

## 🧾 Provenance & citations

### “No citation, no answer” enforcement

Focus Mode should always produce **footnote-style** citations:

- In text: `… drought conditions peaked in 1936 [1].`
- Then a footer list mapping `[1]` → dataset record / STAC item / document ID.

> [!NOTE]
> This is intentionally strict: it reduces hallucinations and makes answers auditable.

### 🛡 OPA policy example: enforce citation markers

A simple rule pattern is: *if the answer contains factual claims, require at least one `[\d+]` marker.*

```rego
package kfm.ai.output

default allow = false

# naive example: require at least one [number] style citation
allow {
  regex.match("\\[[0-9]+\\]", input.answer)
}
```

> [!WARNING]
> This is only a starter. Real policies should also cover: sensitive locations, PII redaction, dataset permission checks, and “hallucinated entities” constraints.

---

## 🛡️ Security & governance checklist

### 🧼 Prompt Gate (input)
- Detect + neutralize prompt injection attempts
- Block disallowed requests (PII fishing, hate speech, etc.)
- Normalize the prompt before it hits the model

### 🧰 Tool allow/deny lists
- Default: **no tools** (text-only)
- Any future tool must be explicitly approved, reviewed, logged, and monitored

### 🧯 Output checks (OPA)
- Block unsafe content
- Redact sensitive geo coordinates (e.g., protected cultural sites)
- Require hedging for speculative content
- Require that referenced entities exist in the knowledge graph (anti-hallucination guardrail)

### 🔐 Secrets & UI hardening
- Keep credentials inaccessible to the AI process
- Use CSP headers to reduce XSS risk
- Rate-limit AI endpoints

---

## 🧪 Evaluation, reproducibility & “safe experimentation”

### 🧰 Deterministic scenario testing (`kfm-sim-run`)
KFM’s design includes a sandbox runner that:
- creates an isolated copy of the data environment
- freezes timestamps/seeds/external calls for repeatability
- can produce a **draft PR** including updated data + metadata + PROV  
- keeps simulated outputs separate until **human review & merge**

### 🌬 Bias correction models (example: `kfm-air-correct`)
Domain modules can “improve data quality” using transparent, documented methods (e.g., quantile mapping + extreme handling) and publish outputs as new datasets with full provenance.

---

## 🌐 Federation-ready AI (long-term)

KFM’s roadmap anticipates a network of interoperable “Frontier Matrix” instances:
- Standard schemas + APIs so regions can interoperate
- Potential **GraphQL federation** to query across multiple instances
- Shared artifact practices (OCI-style packaging, signed attestations) so datasets/models remain verifiable across deployments

---

## 📚 Project docs & reference library (used to shape this README)

> [!TIP]
> Keep authoritative PDFs under something like `docs/pdfs/` (or `docs/_sources/`) and link them here for discoverability.

### 🧭 Core KFM architecture & AI governance
- **Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap**  
- **Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide)**  
- **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design**  
- **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖**  
- **📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide**  
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**  
- **KFM AI Infrastructure – Ollama Integration Overview**

### 🧪 Engineering rigor & documentation standards
- **Scientific Method / Research / Master Coder Protocol Documentation** (testing, CI, deterministic outputs, experiment tracking)
- **Markdown guide / repo layout guidance** (recommended structure for docs/data/schemas/tools)

### 🧠 AI + data science reading binders (PDF portfolios)
- **AI Concepts & more** (AI/ML concepts + reference materials)
- **Data Management / Theories / Architectures / Data Science / Bayesian Methods** (data architecture + probabilistic modeling references)
- **Various programming languages & resources** (polyglot skill-up binder)
- **Mapping/Modeling/Python/Git/HTTP/CSS/Docker/GraphQL/Data Compression/Linux/Security** (full-stack + infra references)
- **Geographic Information/Security/Git/R/SciPy/MATLAB/ArcGIS/Spark/TypeScript/Web Apps** (geo + compute + app references)
- **Maps/GoogleMaps/VirtualWorlds/Archaeological Computer Graphics/Geospatial/WebGL** (3D/immersive geovis + webgl references)

---

## 🤝 Contributing to AI tooling

### ✅ Pull-request expectations
- 🧪 Tests included (unit + integration where relevant)
- 🧾 Policies updated alongside new behaviors (OPA + prompts)
- 🧠 Prompts treated as versioned artifacts (reviewed like code)
- ♻️ Determinism where possible (seed, pinned deps, controlled externals)
- 📓 Logs + provenance updates included (so outputs remain auditable)

### 🧷 A practical PR checklist
- [ ] Does the change preserve **“no citation, no answer”**?
- [ ] Are any new data sources represented as **STAC/DCAT/PROV**?
- [ ] Did we update **OPA** rules for new edge cases?
- [ ] Are we leaking anything sensitive (PII / protected locations)?
- [ ] Did we pin model/runtime versions and record them?

---

## 🆘 Troubleshooting quick hits

- **Model answers without citations** → treat as failure; block or refuse by policy  
- **OPA blocks too aggressively** → revise policy + add regression tests (don’t bypass)  
- **Slow answers** → check retrieval scope, context size, and caching (don’t remove guardrails)  
- **Weird hallucinated entities** → enforce “entity must exist in KG” policy + tighten retrieval

---

### 🧩 Related areas
- `src/pipelines/` ⚙️ ETL + model runs (deterministic, provenance tracked)  
- `src/graph/` 🧠 ontology + graph build + constraints  
- `src/server/` 🌐 FastAPI/GraphQL boundary  
- `web/` 🗺 React + MapLibre/Cesium UI (Focus Mode panel lives here)  
- `schemas/` 📐 JSON Schema / SHACL contracts (telemetry, story nodes, catalogs)  

---