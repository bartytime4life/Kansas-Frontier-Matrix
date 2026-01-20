# 🧾 Contracts (KFM)

![Status](https://img.shields.io/badge/status-draft-blue)
![Principle](https://img.shields.io/badge/principle-contract--first-7b2cbf)
![Principle](https://img.shields.io/badge/principle-provenance--first-2a9d8f)
![Governance](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-0f62fe)
![API](https://img.shields.io/badge/API-OpenAPI%20%7C%20GraphQL-black)

> **KFM rule:** anything that shows up in the **UI** or **Focus Mode** must be traceable to **cataloged sources** and **provable processing**—no “mystery layers”.:contentReference[oaicite:0]{index=0}

This directory is the **contract index** for Kansas Frontier Matrix (KFM): the **schemas, profiles, invariants, and versioning rules** that define how subsystems communicate and what *must always be true*.

---

## 🎯 Purpose

KFM is intentionally **contract-first** and **provenance-first**:

- Every dataset must ship with **metadata JSON (“data contract”)** (source, license, extent, processing steps, etc.) and pass validators **before acceptance**.:contentReference[oaicite:1]{index=1}
- KFM uses open standards for interchange and lineage (**STAC**, **DCAT**, **W3C PROV**) so provenance is machine-checkable and reusable across subsystems.:contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}
- Policy gates run at ingestion, inference, and publication, and KFM is “**fail closed**” (if it doesn’t pass, it doesn’t ship).:contentReference[oaicite:4]{index=4}

---

## 🧠 What counts as a “contract” in KFM?

A KFM contract is any artifact that makes subsystem interactions **predictable, verifiable, and versionable**, including:

- 📦 **Data contracts** (dataset metadata envelopes, schema profiles)
- 🗂️ **Catalog contracts** (STAC/DCAT/PROV profiles, completeness rules)
- 🧱 **Graph contracts** (ontology labels/relationships, constraints, migrations)
- 🔌 **API contracts** (OpenAPI + GraphQL schemas; request/response envelopes)
- 🗺️ **UI contracts** (layer registry formats; Story Node schemas/config)
- 🤖 **AI contracts** (Focus Mode evidence/citations + explainability/XAI expectations)
- 🔐 **Policy contracts** (OPA/Conftest “policy packs”, governance gates, audit trails)
- 👥 **Community contracts** (draft/review workflows + verification rules)

---

## 🧭 Contract stack (from raw → user)

```mermaid
flowchart LR
  A[📥 Raw inputs] --> B[🧪 ETL / Pipelines]
  B --> C[📦 Processed artifacts]
  C --> D[🗂️ Catalogs: STAC/DCAT/PROV]
  D --> E[🕸️ Knowledge Graph (Neo4j)]
  E --> F[🔌 APIs (REST/GraphQL)]
  F --> G[🗺️ UI (2D/3D, timeline)]
  F --> H[🤖 Focus Mode (AI)]
  G --> I[📚 Story Nodes]
  H --> I
```

- APIs are explicitly documented via **OpenAPI/Swagger** (REST) and a **GraphQL schema** for external + internal integration.:contentReference[oaicite:5]{index=5}
- The UI is decoupled from the backend through well-defined **REST + GraphQL** APIs and is designed to *surface provenance and citations everywhere* (“map behind the map”).:contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}

---

## 🧱 Subsystem contracts at a glance

These “must exist” artifacts and “do not break” invariants are the baseline contract set across KFM subsystems.:contentReference[oaicite:8]{index=8}

| Subsystem | Contract artifacts (must exist) | “Do not break” rule (invariants) |
|---|---|---|
| 🧪 ETL / Pipelines | Pipeline configs, run logs, validation reports | Runs are deterministic + replayable; outputs explain diffs:contentReference[oaicite:9]{index=9} |
| 🗂️ Catalogs | JSON Schemas for STAC/DCAT/PROV + validators | No dataset accepted without valid machine-checked metadata:contentReference[oaicite:10]{index=10} |
| 🕸️ Graph | Ontology definitions, migration scripts, integrity constraints | Graph schema stable; changes require migrations; integrity upheld:contentReference[oaicite:11]{index=11} |
| 🔌 APIs | OpenAPI spec / GraphQL schema + contract tests | Backwards compatible unless version bump; contract tests required:contentReference[oaicite:12]{index=12} |
| 🗺️ UI | Layer registry config + accessibility + audit hooks | UI must not leak data; must respect redaction + accessibility:contentReference[oaicite:13]{index=13} |
| 📚 Story / Focus | Story Node templates/schemas + Focus context bundle | Only provenance-linked content; Focus Mode must not add unsourced claims:contentReference[oaicite:14]{index=14} |

---

## ✅ Policy gates that enforce contracts

KFM enforces automated policy gates at key checkpoints. Minimum set includes:

- schema validation
- STAC/DCAT/PROV completeness
- license presence
- sensitivity classification
- provenance completeness
- **Focus Mode output must include citations** (or it must refuse):contentReference[oaicite:15]{index=15}

These gates run both:
- **in code** (validators that raise errors), and  
- **in CI** (e.g., Conftest policy tests per commit).:contentReference[oaicite:16]{index=16}

---

## 📁 Proposed contract layout for this folder

> This README is an **index**. The *actual* canonical schemas and specs may live in their subsystem homes (e.g., `api/`, `docs/standards/`, `schemas/`). The goal is “one canonical directory per subsystem”.:contentReference[oaicite:17]{index=17}

```text
📁 docs/architecture/contracts/
├── 📄 README.md                     # you are here ✨
├── 📁 data/                         # data + metadata contract notes (profiles, invariants)
├── 📁 catalogs/                      # STAC/DCAT/PROV expectations + completeness rules
├── 📁 graph/                         # ontology + constraints + migrations (index)
├── 📁 api/                           # API contract conventions (OpenAPI/GraphQL, envelopes)
├── 📁 ui/                            # layer registry + Story Node config contracts
├── 📁 ai/                            # Focus Mode evidence & XAI contract expectations
├── 📁 policy/                        # policy-as-code contract overview (OPA/Conftest packs)
└── 📁 examples/                      # minimal “golden” contract examples
```

---

## 📦 1) Data & Metadata Contracts

### What’s required (baseline)
Every dataset entering KFM must carry a metadata envelope (“data contract”), including at minimum:

- source + acquisition info
- license
- spatial/temporal extent
- processing steps and reproducibility metadata:contentReference[oaicite:18]{index=18}

**Why?** Because contract-first metadata enables:
- consistent ingestion
- auto-generated attributions/credits
- evidence-backed UI/Focus Mode citations:contentReference[oaicite:19]{index=19}

### Standards (preferred / default)
KFM anchors interchange + lineage to:
- **STAC** (spatial assets)
- **DCAT** (dataset cataloging)
- **W3C PROV** (provenance/lineage):contentReference[oaicite:20]{index=20}

---

## 🧪 2) Pipeline & Simulation Contracts

### Determinism & replayability
ETL jobs must be deterministic and replayable with stable outputs for stable inputs (or diffs are logged and explained).:contentReference[oaicite:21]{index=21}

### AI-assisted transforms (safe pattern)
AI may propose *structured* transform configs, but execution happens in code after validation:

- AI suggests a JSON config (regex mapping, field mapping, etc.)
- pipeline validates JSON (often against schema)
- pipeline executes transform in sandboxed code
- pipeline logs the **AgentAction JSON** into provenance:contentReference[oaicite:22]{index=22}

### “Run manifest” contract (tiny schema, big payoff)
Pulse proposals introduce a small **run manifest** artifact to link:
- inputs (CatalogRef)
- outputs (Artifact URIs)
- env hash + seed
- metrics digests  
…and to support UI evidence drawers + story citations.:contentReference[oaicite:23]{index=23}:contentReference[oaicite:24]{index=24}

Example payload pattern (pipeline → API → graph), including `env_hash`, STAC refs, artifact URIs, and metrics.:contentReference[oaicite:25]{index=25}

---

## 🕸️ 3) Knowledge Graph Contracts

### Ontology alignment
KFM maps data into well-known ontologies (semantic web approach), referencing **CIDOC-CRM** and **GeoSPARQL** concepts even when using a property graph DB (Neo4j).:contentReference[oaicite:26]{index=26}

Pulse adds a more explicit “KFM-OP” style alignment: CIDOC-CRM + GeoSPARQL + OWL-Time, plus version relationships like `:PREDECESSOR` / `:SUCCESSOR`.:contentReference[oaicite:27]{index=27}

### Stability & migrations
Graph schema changes (labels, relationship types) must remain backwards-compatible unless handled through a deliberate migration process.:contentReference[oaicite:28]{index=28}:contentReference[oaicite:29]{index=29}

---

## 🔌 4) API Contracts

### Contract sources of truth
- REST: OpenAPI / Swagger definition is the contract (versioned).:contentReference[oaicite:30]{index=30}
- GraphQL: schema is the contract (versioned).:contentReference[oaicite:31]{index=31}

### Compatibility rules
Breaking changes require either:
- a new versioned endpoint, or
- a negotiation strategy and explicit deprecation plan (don’t silently break clients).:contentReference[oaicite:32]{index=32}

### Tiles and spatial endpoints
The PostGIS adapter supports tile generation (e.g., vector tiles via `ST_AsMVT`) and endpoints like:

- `GET /tiles/<layer>/{z}/{x}/{y}.pbf`:contentReference[oaicite:33]{index=33}

### Evidence envelope (recommended contract extension)
Pulse proposes extending response envelopes to include evidence:

- `{ data, evidence: { run_id, env_hash, seed, metrics[] } }`:contentReference[oaicite:34]{index=34}

---

## 🗺️ 5) UI + Story Contracts

### UI ↔ backend separation
The UI is a modular React web app, decoupled through REST/GraphQL APIs so the interface can evolve independently.:contentReference[oaicite:35]{index=35}:contentReference[oaicite:36]{index=36}

### Evidence-backed UX
The UI is designed for transparency:
- layers surface source attributions
- AI answers include citations
- exports/views carry credits where possible:contentReference[oaicite:37]{index=37}

### Story Node contract direction
Latest proposals emphasize:
- story authoring tools
- a **Markdown/JSON story convention**
- hybrid “2D → 3D” guided stories (MapLibre → Cesium transitions):contentReference[oaicite:38]{index=38}

### Offline packs (future contract surface)
An offline pack may bundle:
- tile archives (PMTiles/MBTiles)
- a mini local web app pointing to local tile sources
- optional offline terrain options (Cesium):contentReference[oaicite:39]{index=39}

---

## 🤖 6) AI Contracts (Focus Mode + Agents)

### Focus Mode: evidence and refusal rules
Focus Mode is advisory-only and must:
- generate answers grounded in KFM data
- **always cite sources** (datasets/documents/graph entities)
- refuse or indicate uncertainty if it can’t source the claim:contentReference[oaicite:40]{index=40}

### Focus Mode: context & explainability (XAI)
Focus Mode can incorporate UI context (location, timeframe, active layers) and may expose an audit panel showing influential factors and governance flags.:contentReference[oaicite:41]{index=41}

### Runtime policy enforcement
Data intake docs propose runtime checks (including OPA rules) ensuring every AI claim is cited, plus logging AI outputs into an immutable governance ledger w/ provenance.:contentReference[oaicite:42]{index=42}

### Watcher–Planner–Executor (W-P-E) agent contract
W-P-E introduces automation with accountability:
- watcher detects issues
- planner proposes plans (within strict rules)
- executor materializes plans via PRs/commits
- actions remain auditable and can be cryptographically signed:contentReference[oaicite:43]{index=43}

**Ethical constraint contract:** planner must not violate FAIR/CARE or data sovereignty; executor refuses execution when approvals/policy checks fail.:contentReference[oaicite:44]{index=44}

**Agent parity contract:** “policy applies equally to human and agent PRs”; agent PRs are not auto-merged and require human review; agents can be globally frozen via a kill-switch (e.g., `.agent-freeze`).:contentReference[oaicite:45]{index=45}

---

## 🔐 7) Governance, Policy-as-Code, and Audit Contracts

### Policy pack
Latest proposals explicitly call for a **Policy Pack** built with **Open Policy Agent (Rego)** and **Conftest** to enforce governance rules.:contentReference[oaicite:46]{index=46}

### Audit trails (sensitive data)
Governance includes audit logging for sensitive access/transforms; example telemetry event: `focus_mode_redaction_notice_shown` to record that data was withheld/generalized.:contentReference[oaicite:47]{index=47}

---

## 👥 8) Community & Verification Contracts

Innovative Concepts recommends an OpenStreetMap-style approach for community contributions:

- robust QA tools + validators
- peer review ethos (monitor changes, rollback where needed)
- contributor items have status (draft / needs-review)
- provenance logs support rollback and transparency:contentReference[oaicite:48]{index=48}

This implies contract expectations for:
- moderation state machine
- review metadata
- version history requirements

---

## 🧬 9) DevOps Provenance Contracts (code → provenance → graph)

Latest proposals describe mapping GitHub PRs into PROV-O:

- PR = PROV Activity
- commits = PROV Entities
- authors/reviewers = PROV Agents
- JSON-LD ingested into Neo4j for queryable dev history provenance:contentReference[oaicite:49]{index=49}

This enables queries like “which code version produced this dataset and who reviewed it” and supports invariants checked by CI.:contentReference[oaicite:50]{index=50}

---

## 🕰️ Versioning & Compatibility Rules

### Graph + ontology
Graph structure should remain backwards-compatible unless migration is performed and recorded.:contentReference[oaicite:51]{index=51}

### API
Breaking changes require new versioned endpoint or explicit deprecation/negotiation; OpenAPI definition is the contract.:contentReference[oaicite:52]{index=52}

### Repo releases
KFM releases follow semantic versioning; major versions represent significant structural change, minors are backwards-compatible additions.:contentReference[oaicite:53]{index=53}

---

## ✅ CI/CD Enforcement Checklist

A “typical” data intake PR pipeline includes steps such as:
1) linting/formatting  
2) schema validation (STAC JSON; DCAT RDF checks; PROV structure; manifests)  
3) link/reference checks  
4) policy-as-code tests (OPA/Conftest):contentReference[oaicite:54]{index=54}

> **Rule:** bots/agents do not bypass CI; parity is required for trust.:contentReference[oaicite:55]{index=55}

---

## 🧰 Templates & Canonical Contract Artifacts

From the v13 guide index (paths are part of the evolving contract ecosystem):
- `docs/templates/TEMPLATE__STORY_NODE_V3.md` (Story Node template)
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (API extension template)
- `docs/standards/KFM_STAC_PROFILE.md`
- `docs/standards/KFM_DCAT_PROFILE.md`
- `docs/standards/KFM_PROV_PROFILE.md`:contentReference[oaicite:56]{index=56}

---

## 🧪 Example contract: Real-time feeds (GTFS-RT watcher)

Latest proposals sketch an idempotent Watcher that:
- polls GTFS-RT feeds efficiently
- emits STAC Items per observation with transit-specific fields
- creates DCAT Dataset entries for catalog exposure
- tags each update with source + retrieval provenance metadata  
…and displays as a live map layer (PostGIS + MapLibre).:contentReference[oaicite:57]{index=57}

---

## 🧊 Example contract: Artifact storage invariants

Large artifacts (rasters, PDFs, images, tile sets) are stored in file/object storage and must be referenced by metadata; checksums can be computed and stored to avoid orphaned/hidden files.:contentReference[oaicite:58]{index=58}:contentReference[oaicite:59]{index=59}

---

## 🔭 Future contract surfaces (planned / exploratory)

These aren’t “baseline” contracts yet, but they inform where the contract system is heading:

- 🌍 **4D digital twins** (time as a first-class dimension):contentReference[oaicite:60]{index=60}
- 🕶️ **AR / hybrid 3D storytelling** (guided “storyscapes”):contentReference[oaicite:61]{index=61}
- 📚 **Bulk document ingestion** (OCR + NLP + graph linking with citations):contentReference[oaicite:62]{index=62}

---

## 📚 Reference library (implementation inspiration)

Some project PDFs are **PDF portfolios** and are best opened in Adobe Reader; they are included as concept/reference libraries:

- `AI Concepts & more.pdf`:contentReference[oaicite:63]{index=63}
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`:contentReference[oaicite:64]{index=64}
- `Various programming langurages & resources 1.pdf`:contentReference[oaicite:65]{index=65}
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`:contentReference[oaicite:66]{index=66}

Additional conceptual support:
- Data governance and lineage are repeatedly emphasized as critical for analytics tooling and compliance.:contentReference[oaicite:67]{index=67}

---

## 🧾 Sources used to build this contract index

- KFM contract-first + provenance-first architecture:contentReference[oaicite:68]{index=68}
- Automated policy gates + “fail closed” enforcement model:contentReference[oaicite:69]{index=69}
- UI transparency + API decoupling + provenance surfacing:contentReference[oaicite:70]{index=70}
- Focus Mode evidence rules + XAI expectations:contentReference[oaicite:71]{index=71}
- Data intake CI contract + agent parity + kill-switch patterns:contentReference[oaicite:72]{index=72}
- v13 subsystem contract artifacts + invariants + versioning rules:contentReference[oaicite:73]{index=73}
- Run manifest / evidence envelope contract proposals:contentReference[oaicite:74]{index=74}:contentReference[oaicite:75]{index=75}
- Community verification workflow concepts (OSM-style QA + review):contentReference[oaicite:76]{index=76}
- Latest proposals: real-time feeds + PR→PROV integration + policy pack direction:contentReference[oaicite:77]{index=77}:contentReference[oaicite:78]{index=78}

