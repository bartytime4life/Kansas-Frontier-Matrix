---
title: "🧭 KFM Architecture Diagrams"
doc_kind: "Diagram Index"
status: "active"
version: "v2.0.0"
last_updated: "2026-01-26"
owners:
  - "KFM Core Maintainers"
tags:
  - "architecture"
  - "diagrams"
  - "mermaid"
  - "c4"
  - "provenance"
  - "policy-as-code"
  - "FAIR+CARE"
---

# 🧭 KFM Architecture Diagrams

![Docs](https://img.shields.io/badge/docs-diagrams-informational)
![Mermaid](https://img.shields.io/badge/diagrams-Mermaid-ff69b4)
![C4](https://img.shields.io/badge/architecture-C4%20style-1f6feb)
![Provenance](https://img.shields.io/badge/provenance-first-2ea44f)
![Policy Gates](https://img.shields.io/badge/policy-fail--closed-critical)
![FAIR%2BCARE](https://img.shields.io/badge/governance-FAIR%2BCARE-7c3aed)
![SBOM](https://img.shields.io/badge/supply--chain-SBOM%2FSLSA-f59e0b)

> **Why this folder exists:** KFM diagrams are *not decoration* — they’re a shared mental model **and** a contract.  
> If the UI can show it, we should be able to explain: **(1) where it came from**, **(2) what transformations happened**, and **(3) what policy allowed it**.  
> That “evidence-first” contract spans **data pipelines → STAC/DCAT/PROV catalogs → PostGIS/Neo4j → API → UI → Focus Mode** (with governance enforced end-to-end). 🧾🧬🛡️

---

## 🧭 Quick Nav

- [📌 Quick Start](#-quick-start)
- [📁 Folder Layout](#-folder-layout)
- [🗺️ Diagram Index](#️-diagram-index)
- [🧠 Canonical Starter Diagrams](#-canonical-starter-diagrams)
- [✅ Standards & CI](#-standards--ci)
- [🧪 Definition of Done](#-definition-of-done)
- [📎 Sources](#-sources-project-files)
- [🧰 Reference Libraries](#-reference-libraries)

---

## 📌 Quick Start

### ✅ Add a new diagram (the “happy path”)

1. **Pick the next ID** (e.g., `D13`) + a short, sortable name  
   `D13__supply_chain_provenance.mmd`
2. Add **Mermaid source** (`.mmd`) and an **export** (`.svg`)  
3. Update the **Diagram Index** table below  
4. Ensure it answers at least **one concrete question** (and says so)  
5. Open a PR (human-reviewed, policy-gated) 🔀

> Tip: treat diagrams like code — review diffs, require CI checks, keep naming stable. 🧰

---

## 📁 Folder Layout

KFM keeps diagram sources and exports together so changes are reviewable, diffable, and stable in docs.

```text
📁 docs/
  📁 architecture/
    📁 diagrams/
      📄 README.md                  👈 you are here (index + canon)
      📄 diagrams.yml               👈 optional manifest (recommended)
      📄 D01__system_spine.mmd      👈 Mermaid source
      📄 D01__system_spine.svg      👈 Export for stable rendering
      📄 D02__c4_context.mmd
      📄 D02__c4_context.svg
      📁 drawio/                    👈 optional (when Mermaid gets too cramped)
      📁 assets/                    👈 optional (icons, screenshots, etc.)
```

### 🧾 Naming scheme (stable + sortable)

- `D01__system_spine.mmd`
- `D06__focus_mode.mmd`
- `D12__sensitivity_controls.mmd`

Exports mirror source names:

- `D06__focus_mode.svg`

---

## 🧷 Evidence Tags

To keep the index readable, diagrams reference these evidence tags:

- **[ROAD]** Platform overview & roadmap (what we’re building next)
- **[ARCH]** Architecture / features / design (core system layout)
- **[TECH]** Technical documentation (implementation + standards)
- **[UI]** UI architecture guide (Map/Timeline/Story/Focus UX contract)
- **[AI]** AI system overview (Focus Mode, governance, guardrails)
- **[OLL]** LLM runtime integration (Ollama patterns)
- **[MD]** Markdown governance patterns (front-matter, provenance in docs)
- **[SM]** Scientific method / master coder protocol (reproducibility + rigor)
- **[LIB]** Reference libraries (geospatial, AI, data engineering, security)

---

## 🗺️ Diagram Index

> **Rule of thumb:** If we can’t answer **“where did this come from?”** and **“what policy allowed it?”** from the diagrams, we’re missing a diagram.  
> KFM aims for **fail-closed** policy gates across ingestion, AI outputs, and publication — *including how we build & ship artifacts (SBOM/SLSA)*. 🔒🧾

| ID | Diagram | Suggested files | Type | Answers | Status | Evidence |
|---:|---|---|---|---|---|---|
| D01 | **System Spine** (Sources → Raw → ETL → Evidence Catalogs → Stores → API → UI/Story → Focus Mode) | `D01__system_spine.mmd/.svg` | Mermaid | “How does anything become visible?” | ✅ Canon | ARCH • TECH • AI • MD |
| D02 | **C4 Context** | `D02__c4_context.mmd/.svg` | Mermaid | “Who uses KFM & what touches it?” | ✅ Canon | ROAD • ARCH |
| D03 | **C4 Containers** (Web/API/Pipelines/Stores/Policy/Obs/LLM) | `D03__c4_containers.mmd/.svg` | Mermaid | “What are the big moving parts?” | ✅ Canon | TECH • ARCH • OLL |
| D04 | **Intake DAG + Policy Gates** (fetch → parse → normalize → validate → dedupe → publish) | `D04__intake_dag.mmd/.svg` | Mermaid | “How do we ingest safely?” | ✅ Canon | ARCH • TECH |
| D05 | **PostGIS + Neo4j Query Orchestration** | `D05__query_orchestration.mmd/.svg` | Mermaid | “How do geometry + semantics recombine?” | ✅ Canon | TECH |
| D06 | **Focus Mode RAG + Governance** (prompt gate → retrieve → generate → cite/refuse → ledger) | `D06__focus_mode.mmd/.svg` | Mermaid + Seq | “How does AI answer safely?” | ✅ Canon | AI • UI • TECH |
| D07 | **Watcher–Planner–Executor (W‑P‑E)** (bots open PRs; CI gates; humans merge) | `D07__wpe_agents.mmd/.svg` | Mermaid | “How do automations ship safely?” | ✅ Canon | ARCH • TECH • ROAD |
| D08 | **UI Composition** (Map/Timeline/Story/Focus/Provenance/Offline) | `D08__ui_composition.mmd/.svg` | Mermaid | “How does UI stay evidence-first?” | ✅ Canon | UI • MD |
| D09 | **Federation** (multi-region catalogs + endpoint swapping + federated search) | `D09__federation.mmd/.svg` | Mermaid | “How do sister matrices interoperate?” | ✅ Canon | ROAD • ARCH |
| D10 | **Real-Time Feeds** (watchers → events → live layers) | `D10__realtime_feeds.mmd/.svg` | Mermaid | “How do live layers work?” | 🟡 Draft | ROAD • ARCH |
| D11 | **Simulation Promotion Path** (sandbox → verify → catalog → publish) | `D11__simulation_promotion.mmd/.svg` | Mermaid | “How do sims become trustworthy?” | 🟡 Draft | ROAD • SM • TECH |
| D12 | **Sensitivity + Sovereignty Controls** (CARE flags → access control → generalization → UI warnings) | `D12__sensitivity_controls.mmd/.svg` | Mermaid | “How do we handle restricted/cultural data?” | ✅ Canon | UI • TECH • AI |
| D13 | **Supply Chain Provenance** (SBOM/SLSA attestations + signing) | `D13__supply_chain_provenance.mmd/.svg` | Mermaid | “How do we prove builds weren’t tampered?” | 🟡 Recommended | TECH • SM |
| D14 | **LLM Provider Router** (Ollama/local ↔ hosted; policy wrapper) | `D14__llm_provider_router.mmd/.svg` | Mermaid | “How do we swap LLM backends safely?” | 🟡 Recommended | OLL • AI |
| D15 | **AI Security Boundaries** (prompt gate, tool allowlist, secrets isolation, rate limits) | `D15__ai_security_boundaries.mmd/.svg` | Mermaid | “How do we keep Focus Mode contained?” | 🟡 Recommended | AI • TECH |

---

## 🧠 Canonical Starter Diagrams

> These are “starter canonical” diagrams. Keep `Dxx__*.mmd` in sync with the embedded versions below.  
> If the diagram changes, **update both the file and the embedded copy** (or delete embedded copy and link out).

---

<details>
<summary><strong>🧬 D01 — KFM System Spine</strong> (the “single picture”)</summary>

KFM’s dominant path is:

**Deterministic pipelines → Evidence catalogs (STAC/DCAT/PROV) → PostGIS/Neo4j/search → API → UI (Map/Timeline/Story) → Focus Mode**.

Key invariant: user-facing output is always backed by **cataloged evidence** (and policy gates can refuse/redact when evidence isn’t sufficient). 🧾✅

```mermaid
flowchart LR
  %% -------------------------
  %% 🌎 Sources
  %% -------------------------
  subgraph S["🌎 Sources"]
    S1["🔌 APIs / feeds"]
    S2["📄 Files (CSV / GeoJSON / GeoTIFF / PDF)"]
    S3["📡 Sensors / realtime"]
  end

  %% -------------------------
  %% 📥 Raw / Work / Processed
  %% -------------------------
  subgraph R["📥 data/raw"]
    R1["🧱 Raw payloads (immutable)"]
    R2["🧾 source.json (license • sensitivity • provenance hints)"]
  end

  subgraph W["🧪 data/work"]
    W1["🧰 Staging + experiments"]
    W2["🧬 Sims / drafts (not official)"]
  end

  subgraph P["✅ data/processed"]
    P1["📦 Canonical datasets"]
    P2["🧱 Derived assets (tiles • COGs • summaries)"]
  end

  %% -------------------------
  %% 📚 Evidence Catalogs
  %% -------------------------
  subgraph C["📚 Evidence Catalogs"]
    C1["🛰️ STAC (collections/items)"]
    C2["🗂️ DCAT (dataset records)"]
    C3["🧬 PROV (prov.jsonld bundles)"]
  end

  %% -------------------------
  %% 🗄 Runtime stores
  %% -------------------------
  subgraph D["🗄 Runtime Stores"]
    D1["🗃️ PostGIS (geometry/tiles)"]
    D2["🕸️ Neo4j (entities/relations/provenance links)"]
    D3["🔎 Search/Embeddings index"]
    D4["🪣 Object store (artifacts)"]
  end

  %% -------------------------
  %% 🧩 API + 🖥 UI
  %% -------------------------
  subgraph A["🧩 API Layer"]
    A1["🔌 FastAPI (OpenAPI)"]
    A2["🧬 GraphQL (optional)"]
    A3["🛡️ Policy Pack (OPA/Rego + Conftest)"]
  end

  subgraph U["🖥️ UI Layer"]
    U1["🗺️ Map/Timeline/Story (React + TS)"]
    U2["🤖 Focus Mode (answers w/ citations or refuse)"]
    U3["🧾 Provenance drawer (STAC/DCAT/PROV)"]
  end

  subgraph G["🧾 Audit + Governance"]
    G1["📓 AI ledger / audit logs"]
  end

  %% -------------------------
  %% Flows
  %% -------------------------
  S1 --> R1
  S2 --> R1
  S3 --> R1

  R1 --> W1
  W1 --> P1
  W2 --> P1

  P1 --> C1
  P1 --> C2
  P1 --> C3

  C1 --> D1
  C2 --> D3
  C3 --> D2
  C3 --> D4

  D1 --> A1
  D2 --> A1
  D3 --> A1
  D4 --> A1

  A1 --> U1
  A1 --> U3

  %% Focus Mode uses API + stores, but must pass policy & log
  U2 --> A1
  A1 --> U2
  U2 --> G1

  %% Governance hooks (fail-closed)
  A3 -.-> R1
  A3 -.-> P1
  A3 -.-> A1
  A3 -.-> U2
```

</details>

---

<details>
<summary><strong>🧱 D02 — C4 Context</strong> (people & systems)</summary>

KFM is built for public exploration **and** serious research workflows, with federation as a first-class path (sister matrices + catalog aggregation). 🌐

```mermaid
flowchart TB
  %% Actors
  user["👤 Public user<br/>explore maps + stories"]
  researcher["🧑‍🔬 Researcher/analyst<br/>query + export"]
  contributor["🧑‍💻 Contributor<br/>add datasets + stories"]
  maintainer["🛡️ Maintainer/curator<br/>review PRs + policy"]

  %% External systems
  sources["🌎 External providers<br/>agencies • archives • sensors • APIs"]
  sister["🧭 Sister matrices<br/>multi-region federation"]
  tools["🧰 External tools<br/>QGIS • notebooks • downstream apps"]

  %% System
  subgraph kfm["🗺️ Kansas Frontier Matrix (KFM)"]
    ui["🖥️ Web UI<br/>Map • Timeline • Story • Focus Mode"]
    api["🔌 API Layer<br/>OpenAPI • (optional) GraphQL"]
    catalogs["📚 Evidence catalogs<br/>STAC • DCAT • PROV"]
  end

  user --> ui
  researcher --> ui
  contributor --> api
  maintainer --> api

  sources --> api
  api --> catalogs

  tools --> api
  api --> tools

  sister <--> api
```

</details>

---

<details>
<summary><strong>🧰 D03 — C4 Containers</strong> (services & boundaries)</summary>

This diagram keeps the “big boxes” honest: **UI**, **API**, **pipelines**, **policy**, **stores**, **observability**, and **LLM runtime** are decoupled and connected via contracts. 🧩

```mermaid
flowchart LR
  subgraph WEB["🖥️ Web"]
    FE["⚛️ React + TypeScript<br/>MapLibre/Cesium • Timeline • Story Nodes • Focus UI"]
  end

  subgraph APIS["🧩 API"]
    BE["🔌 FastAPI (stateless) • OpenAPI"]
    GQL["🧬 GraphQL (optional)"]
    POL["🛡️ Policy Pack (OPA/Rego + Conftest)"]
  end

  subgraph PIPE["⚙️ Pipelines + Workers"]
    WATCH["👀 Watchers (feeds/schedules/changes)"]
    ETL["🏗️ Deterministic ETL jobs"]
    QA["✅ QA + validations + metrics"]
  end

  subgraph CAT["📚 Evidence Catalogs"]
    STAC["🛰️ STAC"]
    DCAT["🗂️ DCAT"]
    PROV["🧬 PROV (prov.jsonld)"]
  end

  subgraph DATA["🗄️ Stores"]
    PG["🗃️ PostGIS"]
    N4J["🕸️ Neo4j"]
    IDX["🔎 Search/Embeddings"]
    OBJ["🪣 Artifact store"]
  end

  subgraph LLM["🤖 LLM Runtime"]
    ROUTER["🧭 Provider Router"]
    OLLAMA["🦙 Ollama (local)"]
    HOSTED["☁️ Hosted LLM (optional)"]
  end

  subgraph OBS["📈 Observability"]
    LOGS["📜 Logs"]
    METRICS["📊 Metrics"]
    TRACE["🧵 Tracing"]
    LEDGER["📓 Audit ledger"]
  end

  FE --> BE
  FE --> GQL

  WATCH --> ETL
  QA --> ETL
  ETL --> PG
  ETL --> N4J
  ETL --> IDX
  ETL --> OBJ
  ETL --> STAC
  ETL --> DCAT
  ETL --> PROV

  BE --> PG
  BE --> N4J
  BE --> IDX
  BE --> OBJ
  BE --> STAC
  BE --> DCAT
  BE --> PROV

  %% Focus Mode calls LLM through policy wrapper
  BE --> POL
  POL --> ROUTER
  ROUTER --> OLLAMA
  ROUTER --> HOSTED

  %% Telemetry
  BE --> LOGS
  BE --> METRICS
  BE --> TRACE
  BE --> LEDGER

  ETL --> LOGS
  ETL --> METRICS
  ETL --> TRACE
```

</details>

---

<details>
<summary><strong>🚦 D04 — Intake DAG + Policy Gates</strong> (safe ingestion)</summary>

Intake is designed to be **systematic like code**: fetch → parse → normalize → validate → policy gate → publish artifacts → PR promotion.  
If validation fails, data routes to human QA (fail-closed). ✅🔒

```mermaid
flowchart TD
  IN["📥 Incoming payloads<br/>APIs • PDFs • feeds • attachments"] --> FETCH["📡 Fetch<br/>ETag/Last-Modified • retries • checksums"]
  FETCH --> PRE["🔎 Pre-parse<br/>MIME sniff • extract attachments • OCR (when needed)"]
  PRE --> EX["🧠 Extract<br/>fields + confidence (LLM-assisted where appropriate)"]
  EX --> NORM["🧼 Normalize<br/>canonical schema • controlled vocab"]
  NORM --> TYPE["🧾 Validate<br/>strict typing • ranges • required metadata"]
  TYPE --> GATE["🚦 Policy gates (fail-closed)<br/>license • sensitivity • AOI • embargo • required fields"]

  GATE -->|pass| DEDUPE["🧬 Dedupe + stable IDs<br/>hashes • near-duplicate detection"]
  GATE -->|fail| HQ["👀 Human QA queue<br/>diffs • evidence • confidence"]

  DEDUPE --> OUT["📦 Emit artifacts"]
  OUT --> STAC["🛰️ STAC Items/Collections"]
  OUT --> DCAT["🗂️ DCAT dataset records"]
  OUT --> PROV["🧬 PROV bundle (prov.jsonld)"]
  OUT --> GPQ["🧱 GeoParquet (analytics)"]
  OUT --> PMT["🗺️ PMTiles (UI perf)"]
  OUT --> DIFF["🧾 Diffs (auditable deltas)"]

  STAC --> PR["🔀 PR promotion<br/>reviewable + reproducible"]
  DCAT --> PR
  PROV --> PR
  DIFF --> PR
```

</details>

---

<details>
<summary><strong>🧭 D05 — PostGIS + Neo4j Query Orchestration</strong></summary>

KFM intentionally separates:
- **PostGIS** → geometry-heavy work (tiles, bbox filters, distance, aggregation) 🗺️  
- **Neo4j** → semantic/provenance relationships (entities, events, lineage) 🕸️  
- **API** → orchestration layer (combine results without fragile cross-DB joins) 🧩

```mermaid
flowchart LR
  UI["🖥 UI"] --> API["🧩 API Router"]
  API -->|geometry/tiles| PG[(🗃️ PostGIS)]
  API -->|entities/relations/lineage| N4J[(🕸️ Neo4j)]
  API -->|metadata| CAT["📚 STAC/DCAT/PROV"]
  PG --> API
  N4J --> API
  CAT --> API
  API --> UI
```

</details>

---

<details>
<summary><strong>🤖 D06 — Focus Mode Pipeline</strong> (RAG + governance + ledger)</summary>

Focus Mode is policy-wrapped by design:

- **Prompt Gate** (sanitize, detect injection, reject disallowed requests) 🛡️  
- **Retrieval** (catalogs + graph + spatial) 🔎  
- **Generation** (draft + citation map) ✍️  
- **Governance** (citations required; sensitivity/bias checks; redact/refuse) 🚦  
- **Ledger/PROV** (AI answer is a traceable derived product) 🧾🧬

```mermaid
flowchart LR
  Q["❓ User question"] --> PG["🛡️ Prompt Gate<br/>sanitize • injection checks • deny disallowed"]
  PG --> PARSE["🧠 Parser<br/>intent • entities • time • place • UI context"]
  PARSE --> RETR["🔎 Retrieval<br/>STAC/DCAT/PROV • Neo4j • PostGIS • search"]
  RETR --> GEN["🗣 LLM generation<br/>draft answer + citation map"]
  GEN --> GOV["🚦 Governance Gate<br/>citations • sensitivity • FAIR/CARE • bias checks"]
  GOV -->|pass| A["✅ Answer + citations"]
  GOV -->|redact| X["🟨 Redacted answer + citations"]
  GOV -->|fail| R["⛔ Refuse / safe fallback<br/>policy violation or insufficient evidence"]
  A --> LED["📓 Log to AI ledger + PROV activity"]
  X --> LED
  R --> LED
```

### Focus Mode sequence (who talks to whom)

```mermaid
sequenceDiagram
  participant U as User
  participant UI as UI (Focus Mode)
  participant API as API
  participant P as Prompt Gate
  participant C as STAC/DCAT/PROV
  participant G as Neo4j
  participant S as PostGIS
  participant L as LLM
  participant K as Policy Gate
  participant D as Ledger/PROV

  U->>UI: Ask question
  UI->>API: /focus/query (question + map/time context)
  API->>P: sanitize + validate request
  P-->>API: ok / block

  API->>C: fetch evidence metadata
  API->>G: graph query (entities/relations/lineage)
  API->>S: spatial query (bbox/tiles/aggregates)
  API->>L: generate draft + citation map

  L-->>API: draft answer + sources map
  API->>K: enforce policy (citations, sensitivity, bias)
  K-->>API: PASS / REDACT / FAIL
  API->>D: append ledger + provenance record
  API-->>UI: answer (or refusal)
  UI-->>U: render response + citations + provenance
```

</details>

---

<details>
<summary><strong>🛰 D07 — Watcher–Planner–Executor (W‑P‑E)</strong> (safe automation)</summary>

W‑P‑E is “automation that ships PRs, not silent mutations.”  
It integrates with policy-as-code checks and supply-chain artifacts (checksums/SBOM) so every change is auditable. 🔀✅

```mermaid
flowchart LR
  W["👁 Watcher<br/>detect change: feeds • QA • gaps"] --> PL["🧠 Planner<br/>propose patch + evidence<br/>refuse if policy violated"]
  PL --> EX["🛠 Executor<br/>run pipeline in container<br/>emit artifacts + checksums"]
  EX --> PR["🔀 Open PR<br/>diffs • PROV • STAC/DCAT • SBOM"]
  PR --> CI["✅ CI gates<br/>tests • conftest/OPA • schema • security"]
  CI --> HR["👀 Human review"]
  HR -->|merge| PUB["📦 Publish/promote<br/>catalogs + stores + UI"]
  HR -->|reject| FIX["🔁 Iterate"]
  FIX --> PL
```

</details>

---

<details>
<summary><strong>🗺 D08 — UI Composition</strong> (Map + Timeline + Story + Focus + Offline)</summary>

The UI is “trust-first”:
- provenance panels + clickable citations 🧾  
- restriction icons + warnings for governed layers 🔒⚠️  
- offline packs for field use (subset bundles) 🧳📱

```mermaid
flowchart TB
  subgraph UI["🖥️ React UI"]
    MAP["🗺️ Map View (2D/3D)"]
    TIME["⏳ Timeline"]
    STORY["📖 Story Viewer (Story Nodes)"]
    FOCUS["🤖 Focus Mode Panel"]
    META["🧾 Provenance Drawer (STAC/DCAT/PROV)"]
    LAYERS["🧩 Layer Manager (locks/warnings)"]
    SEARCH["🔍 Search/Browse"]
    OFF["📦 Offline Pack Mode (PWA/mobile)"]
  end

  STORY --> MAP
  STORY --> TIME

  LAYERS --> MAP
  SEARCH --> MAP

  MAP --> META
  TIME --> META
  FOCUS --> META
  FOCUS --> MAP

  OFF --> MAP
  OFF --> STORY
```

</details>

---

<details>
<summary><strong>🌐 D09 — Federation</strong> (multi-region interoperability)</summary>

Federation is driven by open catalogs and config:
- harvest/merge catalogs (DCAT/STAC) 🗂️  
- UI swaps endpoints based on region/config 🧭  
- optional GraphQL federation patterns for cross-region querying 🧬

```mermaid
flowchart LR
  subgraph KS["🗺️ Kansas KFM"]
    KS_CAT["📚 Catalogs (DCAT/STAC/PROV)"]
    KS_API["🔌 API"]
  end

  subgraph NE["🧭 Sister Matrix (example)"]
    NE_CAT["📚 Catalogs (DCAT/STAC/PROV)"]
    NE_API["🔌 API"]
  end

  HUB["🧷 Federation Hub<br/>harvest + merge catalogs"] --> SEARCH["🔍 Federated Search"]

  KS_CAT --> HUB
  NE_CAT --> HUB

  UI["🖥️ UI"] --> SEARCH
  UI --> KS_API
  UI --> NE_API
```

</details>

---

<details>
<summary><strong>⚡ D10 — Real‑Time Feeds</strong> (watchers → events → UI layers)</summary>

Real-time layers follow the same governance rules as batch data — policy gates first, then publish. ⚡✅

```mermaid
flowchart TD
  FEED["📡 Realtime feed (GTFS-RT / sensors)"] --> WATCH["👁 Watcher poll/subscribe"]
  WATCH --> PARSE["🧾 Parse + normalize"]
  PARSE --> GATE["🚦 Policy gates<br/>schema • AOI • sensitivity"]
  GATE -->|pass| STAC["📚 STAC event items"]
  GATE -->|pass| PG[(🗃️ PostGIS realtime tables)]
  GATE -->|pass| N4J[(🕸️ Neo4j relations)]
  STAC --> API["🧩 API"]
  PG --> API
  N4J --> API
  API --> UI["🗺 UI realtime layer"]
```

</details>

---

<details>
<summary><strong>🧪 D11 — Simulation Promotion Path</strong> (sandbox → verified → published)</summary>

Sims are powerful — and dangerous — unless promotion is explicit:
- run in **work/sandbox**
- validate + peer review + policy gate
- only then promote to processed/cataloged outputs ✅🧾

```mermaid
flowchart LR
  CFG["🧾 Simulation config"] --> RUN["🏃 Run sim (data/work/sims)"]
  RUN --> OUT["📦 Outputs (draft)"]
  OUT --> QA["✅ Validation + QA<br/>tests • sanity checks • policy gates"]
  QA -->|pass| PROMOTE["📦 Promote to data/processed"]
  QA -->|fail| HOLD["🧯 Hold + investigate"]
  PROMOTE --> CATALOG["📚 STAC/DCAT/PROV"]
  CATALOG --> STORES["🗄 PostGIS/Neo4j/Search"]
  STORES --> API["🧩 API"]
  API --> UI["🗺 UI + Focus Mode"]
```

</details>

---

<details>
<summary><strong>🔒 D12 — Sensitivity + Sovereignty Controls</strong> (CARE-driven UX + policy)</summary>

KFM handles sensitive/sovereign data by:
- propagating governance metadata (FAIR/CARE flags) 🏷️  
- enforcing access control at API/runtime 🔐  
- using generalization (e.g., bins) for public views 🟦  
- showing UI warnings/locks and contextual disclaimers 🔒⚠️

```mermaid
flowchart TD
  IN["📥 Inputs<br/>licensed + classified"] --> GATE["🚦 Policy gates<br/>license • sensitivity • FAIR/CARE"]
  GATE --> PROC["⚙️ Processing"]
  PROC --> OUT["📦 Outputs"]
  OUT --> TAG["🏷 Carry-forward governance tags<br/>restrictions • disclaimers"]
  TAG --> API["🧩 API enforces access control"]
  API --> UI["🖥 UI shows locks/warnings + provenance"]
  API -->|restricted| GEN["🟦 Generalize / redact<br/>e.g., bins instead of points"]
  API -->|deny| DENY["⛔ Deny (fail-closed)"]
```

</details>

---

## ✅ Standards & CI

### 🧼 Mermaid conventions (keep diagrams diffable)

1. ✅ Keep node labels short (put prose outside the diagram).  
2. ✅ Quote labels if punctuation gets weird.  
3. ✅ Prefer `flowchart LR` for pipelines (reads like a “spine”).  
4. ✅ Avoid fancy Markdown inside node labels.  
5. ✅ Treat diagrams as *source code* (review diffs like code). 👀

### 🧾 Governed documentation patterns (recommended)

For “contract docs” (like this README or any diagram notes), use **YAML front-matter** and enforce required fields in CI (title, status, version, last_updated, classification, etc.). 🧷

### 🖼 Exports: why `.svg` is preferred

- Stable, crisp, searchable text 🔍  
- Good PR diffs (size and structure are reviewable)  
- Works across docs systems

### 🧪 Suggested CI checks

- Mermaid parse + render (fail the build if invalid)  
- Ensure `.svg` exports are up to date with `.mmd` sources  
- Policy gates for doc metadata (front-matter fields)  
- Lint: Markdown + Mermaid formatting  
- Security hygiene: secrets scan, dependency audits (where applicable) 🛡️

---

## 🧪 Definition of Done

Use this checklist when adding/updating a diagram:

- [ ] Added/updated **Diagram Index** entry  
- [ ] Diagram answers at least **one clear question**  
- [ ] `.mmd` source committed  
- [ ] `.svg` export committed (or justified why not)  
- [ ] Labels are readable + minimal (prose outside)  
- [ ] Evidence tags included (ARCH/TECH/UI/AI/…)  
- [ ] CI passes (Mermaid validation + doc checks)  
- [ ] If the diagram changes system behavior, open/update an issue or ADR 🧾

---

## 📎 Sources (Project Files)

> These are the project docs used to ground the diagram set and the governance rules described here.

### 🧭 Core KFM documents (primary)

- **📘 KFM — Platform Overview & Roadmap**  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf](file-service://file-J9i6fUc35zPWB2U62zUnEN)  
- **🏗️ KFM — Comprehensive Architecture, Features, and Design**  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-Qj23Z329hf1Q1WD86hXYfL)  
- **🧠 KFM — AI System Overview 🧭🤖**  [oai_citation:2‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-P4zHoJicw1HG6bXmqFygG8)  
- **🖥️ KFM — UI System Overview (Technical Architecture Guide)**  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf](file-service://file-MbEYbsLWBmpXVYXVF79c38)  
- **📚 KFM — Expanded Technical & Design Guide**  [oai_citation:4‡📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf](file-service://file-Tjmzn5F3sT5VNvVFhqj1Vo)  [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf](file-service://file-Tjmzn5F3sT5VNvVFhqj1Vo)  
- **📗 KFM — Comprehensive Technical Documentation**  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-VgLA7nv34M5muqZ5MQxBLG)  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-VgLA7nv34M5muqZ5MQxBLG)  

### 🤖 LLM runtime + infrastructure

- **🦙 KFM AI Infrastructure — Ollama Integration Overview**  [oai_citation:8‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)  [oai_citation:9‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)  

### 🧾 Documentation & rigor (process)

- **🧷 MARKDOWN_GUIDE_v13 (governed docs patterns)**  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **🧪 Scientific Method / Master Coder Protocol (reproducibility & review discipline)**  [oai_citation:11‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- **📝 Comprehensive Markdown Guide (syntax + governance suggestions)**  [oai_citation:12‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  

### 🗺️ Adjacent / legacy concept docs (useful context)

- **🗺 Kansas-Frontier-Matrix — Open-source Geospatial Historical Mapping Hub Design**  [oai_citation:13‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  

---

## 🧰 Reference Libraries

> These are “toolbox” libraries that influence architecture decisions (geospatial, AI, data engineering, security).  
> They are often **portfolios** containing multiple embedded PDFs/books.

- **🧠 AI Concepts & more (portfolio)**  [oai_citation:14‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- **🗺 Maps / Google Maps / Virtual Worlds / Archaeology / WebGL (portfolio)**  [oai_citation:15‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- **🧰 Various programming languages & resources (portfolio)**  [oai_citation:16‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  
- **🗄 Data Management / Architectures / Data Science / Bayesian Methods (portfolio)**  [oai_citation:17‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  
- **🐍 Mapping/Modeling + Python/Git/HTTP/CSS/Docker/GraphQL/Security (portfolio)**  [oai_citation:18‡Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf](file-service://file-2QvRgQbts8ENJQSRC6oGme)  
- **🧭 Geographic Info + Security + R/SciPy/MATLAB/ArcGIS/Spark/TypeScript/Web Apps (portfolio)**  [oai_citation:19‡Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf](file-service://file-TH7HttQXn8Bh1hVhcj858V)  

### 📚 Selected deep dives (pulled from the library)

- **🧬 Python Geospatial Analysis Cookbook (PostGIS recipes, APIs, routing)**  [oai_citation:20‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- **🔐 Data Mining — Concepts & Applications (privacy techniques, auditing, differential privacy)**  [oai_citation:21‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  

---

## 🧯 If something changes…

If code, pipelines, governance, or UI behavior diverge from these diagrams, treat it as a **documentation bug**:

- update the diagram(s), or  
- open a tracking issue, or  
- add a “Known divergence” note in the diagram section.

Because KFM’s promise is **clarity + auditability**, and diagrams are part of how we enforce that promise. ✅🧭🧾