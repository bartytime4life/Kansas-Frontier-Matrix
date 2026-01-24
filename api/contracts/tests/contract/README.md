# 🧾 KFM API Contract Tests
![Contract-First](https://img.shields.io/badge/contract--first-%E2%9C%85-informational)
![Provenance-First](https://img.shields.io/badge/provenance--first-%F0%9F%A7%AC-informational)
![OpenAPI](https://img.shields.io/badge/OpenAPI-%F0%9F%93%9C-blue)
![GraphQL](https://img.shields.io/badge/GraphQL-%F0%9F%95%B8%EF%B8%8F-purple)
![OPA+Conftest](https://img.shields.io/badge/OPA%20%2B%20Conftest-%F0%9F%9B%A1%EF%B8%8F-critical)
![Fail-Closed](https://img.shields.io/badge/gates-fail--closed-red)

> [!IMPORTANT]
> **KFM is contract-first & provenance-first**: anything that appears in the UI or Focus Mode must be traceable to cataloged sources and provable processing — **no “mystery layers”**.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

This folder contains the **contract test harness** for KFM’s API boundary. It exists to keep **UI ↔ API ↔ data** aligned as KFM evolves.

---

## 🧠 Why contract tests exist in KFM

KFM’s architecture emphasizes **clean separation of concerns**: front-end, back-end, and pipelines are decoupled and communicate only through **APIs and data contracts**.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

The API layer is described as a **stateless FastAPI backend** with **REST (OpenAPI/Swagger)** and **GraphQL** for core operations, and it enforces validation/business rules before accepting/serving data.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

The UI is designed to be **decoupled** and to communicate with the backend via **API endpoints (REST) and GraphQL queries**, not by directly touching graph/DBs.  [oai_citation:3‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## ✅ What these tests protect

### 🧾 Contract surfaces we lock down
1. **REST contract** (OpenAPI / Swagger)  
2. **GraphQL contract** (schema + query constraints like depth/pagination guards)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
3. **Evidence contracts** (STAC + DCAT + PROV “evidence triplet”)  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
4. **Governance contracts** (Policy-as-Code via OPA/Rego + Conftest gates)  [oai_citation:6‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 🛡️ KFM-specific invariants (non-negotiable)
- **Evidence triplet required**: no dataset/node should appear without STAC + DCAT + PROV evidence attached.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Policy gates are fail-closed**: if a rule can’t be satisfied, CI rejects the change.  [oai_citation:8‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- **API boundary enforced**: policy can deny changes that try to let UI/code directly access databases or the graph.  [oai_citation:9‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Backwards compatibility is expected** unless a version bump is declared; contract changes must be tested against known inputs/outputs.  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📁 Where this fits in the repo

KFM’s canonical ordering (as a governance guardrail) is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**  [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Contract tests help ensure the **API step** remains trustworthy and stable as upstream artifacts evolve.

---

## 🗂️ Expected folder layout

> Adjust filenames to match what’s actually in your repo — the point is the **test categories** 👇

```text
📦 api/
└─ 📦 contracts/
   ├─ 📁 openapi/                # 📜 REST contract artifacts (snapshots / pinned specs)
   ├─ 📁 graphql/                # 🕸️ GraphQL schema artifacts (SDL / introspection snapshot)
   ├─ 📁 data/                   # 🧬 Data contract profiles/schemas (STAC/DCAT/PROV)
   └─ 📦 tests/
      └─ 📦 contract/
         ├─ 📄 README.md         # 👈 you are here
         ├─ 🧪 test_openapi_contract.py
         ├─ 🧪 test_graphql_contract.py
         ├─ 🧪 test_dataset_endpoints_contract.py
         ├─ 🧪 test_evidence_triplet_contract.py
         ├─ 🧪 test_redaction_and_classification_contract.py
         └─ 📁 fixtures/
            └─ 📄 sample_ids.json
```

---

## 🧪 Running the contract tests

### 1) Fast checks (no running API)
Use these when you’ve changed schema files, generated contracts, or updated policy rules.

```bash
# from repo root
pytest -q api/contracts/tests/contract
```

Recommended: run in CI on every PR (fail-closed) alongside policy gates.  [oai_citation:12‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 2) Contract checks against a running API
Bring up your dev stack (often via docker compose in KFM-style environments) and point tests at it.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

```bash
export KFM_API_BASE_URL="http://localhost:8000"
pytest -q api/contracts/tests/contract -k live
```

> [!TIP]
> If you don’t have a live marker yet, add one (e.g., `@pytest.mark.live`) so CI can run fast checks by default and run live checks in scheduled/nightly pipelines.

---

## 🧾 What “API contract” means here (KFM definition)

KFM explicitly treats metadata as a **data contract**: every dataset is expected to have contract fields (source, license, spatial/temporal extent, processing steps, etc.) and validators enforce them before acceptance.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

KFM also uses **open standards** (STAC/DCAT/PROV) and runs schema validation in CI — effectively treating metadata “as code with tests.”  [oai_citation:15‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧪 Test categories & what to assert

### 1) OpenAPI contract tests (REST) 📜
**Goal:** keep the REST API stable and documented.

What to test:
- The OpenAPI document is generated and valid (JSON/YAML parse)
- The schema for critical endpoints hasn’t drifted unexpectedly (snapshot / pinned contract)
- Responses conform to the OpenAPI schema for known fixtures

KFM’s API is described as FastAPI-based and documented via OpenAPI/Swagger.  [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 2) GraphQL contract tests 🕸️
**Goal:** keep the GraphQL schema stable + enforce query safety rules.

What to test:
- Schema SDL (or introspection JSON) matches the pinned baseline
- Guards like depth limits / pagination constraints exist and are enforced (part of the contract surface)  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Example query shape (from KFM docs):
```graphql
{
  dataset(id:"kfm.ks.landcover.2020") {
    title
    description
    stac { assets { href } }
    relations { derivedFrom { id } }
  }
}
``` 
 [oai_citation:18‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 3) Evidence triplet contract tests 🧬
**Goal:** prevent “mystery nodes/layers” from reaching users.

KFM’s intake model centers an evidence triplet:
- **STAC** (spatial assets)
- **DCAT** (dataset discovery metadata)
- **PROV-O** (provenance lineage)  
…and requires them for anything that appears in UI/Focus Mode.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

What to test (suggested):
- Any dataset returned by `/datasets/{id}` includes references/links to its STAC and PROV artifacts (directly or via fields)
- The API never returns a dataset without license/source metadata (contract expectations + policy gates)  [oai_citation:20‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- Breaking the evidence linkage causes a failure (fail-closed posture)  [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 4) Redaction + classification contract tests 🔐
**Goal:** enforce CARE/FAIR and prevent sensitive leakage.

KFM’s policies include sovereignty/classification rules where the most restrictive classification must carry forward to outputs, and UI safeguards (like generalization/blurring) are part of compliance.  [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

What to test (suggested):
- Restricted datasets cannot be fetched without auth (or are omitted/filtered)
- Public responses do not contain restricted geometries/attributes when inputs were sensitive
- Classification tags propagate into API responses so UI can apply safeguards

### 5) Streaming / real-time contract tests ⏱️
**Goal:** real-time doesn’t bypass provenance and governance.

KFM describes “real-time” layers as UI → API → PostGIS queries returning GeoJSON points, with source labeling from DCAT and classification respected.  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

It also states provenance-first publishing rules cover streaming: even real-time data needs at least stub provenance before display.  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

What to test (suggested):
- Real-time endpoints return GeoJSON with required metadata markers
- Source attribution fields exist (or can be resolved via dataset id)
- Provenance linkage exists (or a stub is present) for displayed readings

### 6) Artifact packaging contract tests 📦
**Goal:** packaged outputs ship with catalogs.

KFM proposals include bundling processed outputs into **GeoParquet** and generating **PMTiles** tilesets, and then “registering” them with a STAC/DCAT record.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

What to test (suggested):
- Every packaged artifact has a catalog record
- Catalog record points to artifact distributions
- Versioning fields are present (so UI can cite and provenance can attach)

---

## 🧩 Adding/changing an API endpoint (contract-first workflow)

KFM guidance for new API work: **define the contract first**, then implement, then add contract tests + redaction rules if sensitive.  [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Workflow checklist:**
1. 🧾 Update OpenAPI spec and/or GraphQL schema (contract surface)
2. 🧪 Add/extend tests in this folder to cover:
   - Schema compatibility (snapshot / pinned spec)
   - Example request/response fixtures
   - Evidence + classification invariants
3. ⚖️ Ensure policy gates still pass (OPA/Rego + Conftest in CI)  [oai_citation:27‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
4. 📚 Document the endpoint so UI consumers know how to use it (and what guarantees exist)

> [!NOTE]
> Per v13 guidance, API contract definitions may live under something like `src/server/contracts/` (or the equivalent in your repo).  [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔒 Governance hooks: Policy Pack & CI (how it ties together)

KFM uses an OPA-based policy pack (Rego) run via Conftest in CI; if a rule is broken, CI fails and reports what policy was violated.  [oai_citation:29‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

Examples of policy-enforced boundaries that contract tests should **align with** (even if they’re enforced elsewhere):
- Pipeline Ordering Rule (no bypassing prior stages)
- API Boundary Rule (UI must not directly access DB/graph)  [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Provenance-first publishing (processed data requires matching PROV updates)  [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## ✅ Definition of Done (DoD) for contract changes

- [ ] OpenAPI and/or GraphQL contracts updated (and versioned if breaking)  [oai_citation:32‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Contract tests added/updated with fixtures for known inputs/outputs  [oai_citation:33‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Evidence triplet invariants preserved (STAC/DCAT/PROV linkage intact)  [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Redaction/classification rules are validated (no leakage)  [oai_citation:35‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Policy gates pass in CI (fail-closed)  [oai_citation:36‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧵 Upcoming / planned contract expansions (keep tests ready)

KFM working ideas include additional platform capabilities that will likely need **new endpoint contracts** and **new contract tests**, such as:
- Pulse Threads (for hypothesis iteration and provenance-chained narrative drafts)
- Conceptual Attention Nodes (first-class semantic nodes for “what matters”)
- Graph health checks & integrity gates
- OCI Artifact Distribution & supply-chain attestations (SLSA/Sigstore)  
 [oai_citation:37‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

Related: KFM proposals include supply chain security practices like attestations and signatures/verification concepts.  [oai_citation:38‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:39‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 📚 Design drivers (project files used)

Core KFM system docs:
- **Comprehensive Technical Documentation** (contract-first & provenance-first; OpenAPI/GraphQL)  [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Comprehensive Architecture, Features, and Design** (API-centric modular design; UI via API)  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **AI System Overview** (Policy Pack OPA+Conftest; CI detect→validate→promote)  [oai_citation:42‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **Comprehensive UI System Overview** (UI decoupled; REST + GraphQL)  [oai_citation:43‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Data Intake – Technical & Design Guide** (evidence triplet; policy pack rules; endpoints examples)  [oai_citation:44‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

Governance + repo organization guides:
- **MARKDOWN_GUIDE v13** (contracts by subsystem; backwards compatibility; contract tests)  [oai_citation:46‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **MASTER_GUIDE v13 excerpts** (canonical pipeline ordering; canonical subsystem homes)  [oai_citation:47‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Future-facing design inputs:
- **Latest Ideas & Future Proposals** (GeoParquet + PMTiles packaging + catalogs; supply chain ideas)  [oai_citation:48‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:49‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- **Additional Project Ideas** (Policy Gate / Conftest; OCI artifacts; Cosign)  [oai_citation:50‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

Reference library (PDF portfolios — open locally in Acrobat to view contents):
- **AI Concepts & more** (PDF portfolio container)  [oai_citation:51‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- **Maps / Virtual Worlds / WebGL / Geospatial graphics** (PDF portfolio container)  [oai_citation:52‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- **Various programming languages & resources** (PDF portfolio container)  [oai_citation:53‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- **Data Management / Theories / Bayesian / Programming ideas** (PDF portfolio container)  [oai_citation:54‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

Methodology support docs (quality + reproducibility mindset):
- **Scientific Method / Master Coder Protocol** (testing + CI expectations)  [oai_citation:55‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- **Data Mining Concepts & Applications** (notes on dynamic data & the need for repeatable processes)  [oai_citation:56‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
