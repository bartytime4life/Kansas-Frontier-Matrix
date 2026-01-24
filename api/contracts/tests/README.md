# 🧪 API Contracts & Contract Tests (KFM)

![Contract-First](https://img.shields.io/badge/contract--first-yes-brightgreen)
![Provenance](https://img.shields.io/badge/provenance-required-blue)
![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-6e40c9)
![API](https://img.shields.io/badge/API-FastAPI%20%7C%20OpenAPI%20%7C%20GraphQL-009688)
![UI](https://img.shields.io/badge/UI-React%20%2B%20MapLibre%20%2B%20Cesium-1f6feb)

> **KFM ships trust.** This folder is where we *prove* our API + data + AI contracts stay stable, governed, and evidence-backed. ✅🔒  
> **Fail closed** philosophy: if a contract can’t be validated, it doesn’t ship.

---

## 🧭 What lives here

📁 **`api/contracts/tests/`** contains **contract tests** (plus fixtures) that validate:

- ✅ **REST contract** (OpenAPI / Swagger)
- ✅ **GraphQL contract** (schema + compatibility)
- ✅ **Data contracts** (metadata JSON “data contract”, plus STAC/DCAT/PROV completeness)
- ✅ **Content contracts** (Story Nodes = Markdown + JSON map state)
- ✅ **AI contracts** (Focus Mode = citations required, refuse if unsourced)
- ✅ **Governance contracts** (OPA/Conftest “Policy Pack” gates + redaction rules)
- ✅ **Deprecation / compatibility** (no surprise breaks; consumers stay safe)

This matches KFM’s architecture: the UI is decoupled from the backend via well-defined REST/GraphQL APIs, data is contract-first, and governance is enforced by automated gates across ingestion → inference → publication. 🧱🛰️🤖

---

## 📌 Quick links

- 🗂️ [Folder layout](#️-folder-layout)
- ✅ [Contracts we enforce](#-contracts-we-enforce)
- 🚀 [Run locally](#-run-locally)
- 🧩 [Add/change an endpoint](#-addchange-an-endpoint-the-kfm-way)
- 🛡️ [Policy Pack + redaction](#️-policy-pack--redaction-tests)
- 🤖 [Focus Mode contracts](#-focus-mode-ai-contracts)
- 🗺️ [Geospatial contracts](#️-geospatial-contracts)
- 🧵 [Graph health checks](#-graph-integrity--health-checks)

---

## 🗂️ Folder layout

> **Goal:** Make it obvious where the *contracts* live and where the *proof* lives.

```text
📦 api/
 └─ 📜 contracts/
    ├─ 🧾 openapi/                 # OpenAPI source-of-truth (YAML/JSON)
    ├─ 🧬 graphql/                 # GraphQL schema / introspection snapshots
    ├─ 🧩 jsonschema/              # JSON Schemas (dataset metadata, Story Node config, etc.)
    ├─ 🛡️ policy/                  # OPA/Rego policies (or references to tools/validation/policy/*.rego)
    └─ 🧪 tests/
       ├─ README.md                # 👈 you are here
       ├─ 🧪 test_openapi_*.py
       ├─ 🧪 test_graphql_*.py
       ├─ 🧪 test_policy_*.py
       ├─ 🧪 test_provenance_*.py
       └─ 🧰 fixtures/
          ├─ 📄 openapi/           # sample requests/responses, example payloads
          ├─ 📄 graphql/
          ├─ 📄 datasets/          # metadata JSON contracts (valid + invalid)
          └─ 📄 story_nodes/       # story node markdown + JSON map-state configs
```

> 🔎 **Tip:** If your repo places contracts elsewhere (e.g., `src/server/contracts/`), keep the **tests here** but link to the canonical contract source so this folder remains the *testing hub*.

---

## ✅ Contracts we enforce

| Contract type 🧩 | Primary consumers 👥 | What we verify 🧪 | “Pass” means ✅ |
|---|---|---|---|
| **OpenAPI (REST)** | UI, scripts, external integrators | Spec is valid + stable; endpoints match request/response schemas; no breaking changes without versioning | API behavior matches OpenAPI |
| **GraphQL schema** | UI, analytics clients | Schema is valid; non-breaking evolution; resolvers satisfy types | No unintended breaking schema drift |
| **Dataset metadata “data contract”** | Pipelines, catalogs, Focus Mode | Required fields present (source/license/spatial+temporal extents/provenance) | No “mystery layers”; everything is attributable |
| **STAC/DCAT/PROV completeness** | Map layers, citations, provenance ledger | Required STAC/DCAT/PROV fields exist and link correctly | Provenance chain is queryable + complete |
| **Story Nodes (Markdown + JSON)** | Story engine, Focus Mode | Story node structure, citations, graph entity references, map config schema | Stories are machine-ingestible + governed |
| **Focus Mode output contract** | UI assistant panel, audit panel | AI outputs include citations; refuse or mark uncertainty if not supported | No hallucinations; evidence-backed answers only |
| **Policy Pack (OPA/Conftest)** | CI gates, automation agents | Rules enforce licensing, sensitivity/CARE, deprecated endpoint bans | Governance rules are non-bypassable |
| **Redaction / sensitivity** | Public UI, exports | Sensitive fields are removed/generalized based on classification | CARE compliance; no accidental leakage |

---

## 🚀 Run locally

### 1) Fast checks (no server needed) ⚡
Use this for **schema validation + policy checks + fixtures validation**:

```bash
pytest -q api/contracts/tests
```

### 2) Provider verification (API running) 🧪🌐
If your contract tests call the live FastAPI app (recommended for OpenAPI provider verification):

```bash
export KFM_API_BASE_URL="http://localhost:8000"
pytest -q api/contracts/tests -m "provider"
```

### 3) Policy Pack gate checks (Conftest/OPA) 🛡️
If your policies are in Rego and enforced by Conftest in CI:

```bash
conftest test api/contracts/policy -p tools/validation/policy
```

> 🧠 **Design intent:** KFM uses policy-as-code (OPA + Conftest) so governance rules become testable gates in CI, not “best effort” guidelines.

---

## 🧩 Add/change an endpoint (the KFM way)

KFM’s master guidance is blunt (in a good way 😄): **define the contract first**, then implement, then prove it with contract tests.

### ✅ Workflow

1) **Update the contract first**
- REST: update the **OpenAPI spec**
- GraphQL: update the **GraphQL schema**
- Add **redaction rules** if the endpoint touches sensitive data

2) **Implement the controller/resolver**
- Keep implementation *behind* the contract (don’t leak internals into your public shape)

3) **Add contract tests**
- ✅ Happy path
- ✅ “Fail closed” path (missing license, missing provenance, unsourced AI answer, etc.)
- ✅ Redaction expectations (sensitive data never leaves)

4) **Document + notify consumers**
- Add to API docs
- Coordinate with UI usage (especially for map layers + Story Nodes)

### 🧾 Definition of Done (endpoint contract)
- [ ] OpenAPI/GraphQL contract updated **first**
- [ ] Contract tests added (positive + negative + redaction)
- [ ] Policy Pack updated (if new governance surface)
- [ ] Deprecation plan included (if breaking)
- [ ] Story/Layer UI impact documented (if it changes map layers, timeline, story playback)

---

## 🧪 Contract test patterns we use

### 1) Contract linting (static) 🔍
Validate specs/schemas compile and are internally consistent:
- OpenAPI validity (schema references resolve)
- GraphQL schema validity
- JSON Schema validity (draft version consistent)

### 2) “Provider verification” for OpenAPI 🧷
Run requests against a real app (or TestClient) and verify responses satisfy OpenAPI:
- ✅ response body schema
- ✅ status codes
- ✅ headers (esp. caching + content type for tiles/data)
- ✅ pagination shapes

### 3) Backward compatibility checks ♻️
For each change:
- block removing response fields without bumping version
- block renaming fields without alias/deprecation
- block silent enum changes

> 💡 KFM is built for federation and reuse; stable contracts are how other “Frontier Matrix” deployments can interoperate.

### 4) “Fail closed” negative tests 🔒
Every major gate must have a “this should be rejected” test:
- Missing **license**
- Missing **provenance**
- Missing **sensitivity classification**
- AI answer without **citations**
- Deprecated endpoints still referenced

### 5) Determinism & reproducibility for modeling endpoints 🎛️
If an endpoint triggers an analysis/simulation:
- fixed seed / deterministic output where applicable
- output includes parameters + provenance
- output is labeled as evidence w/ uncertainty (not “truth”)

---

## 🛡️ Policy Pack + redaction tests

KFM uses OPA + Conftest policy gates to codify governance rules like:
- “Every dataset must have a license”
- “AI outputs must include at least one citation”
- “No use of deprecated API endpoints”
- “Sensitive locations must be generalized/hidden”

### Recommended tests
- ✅ **Policy unit tests**: policy inputs → expected allow/deny
- ✅ **Policy integration tests**: run Conftest against real PR artifacts
- ✅ **Redaction tests**: given a restricted dataset/entity, verify API output is generalized or blocked

---

## 🤖 Focus Mode (AI) contracts

Focus Mode is powerful, but KFM’s rule is non-negotiable:

✅ **Always cites sources**  
✅ **Refuses or signals uncertainty when not supported**  
✅ **Surfaces explainability signals (audit panel / governance flags) when available**

### Contract expectations (recommended response shape)
Even if your exact JSON differs, the *concept* should hold:

```json
{
  "answer": "…",
  "citations": [
    { "kind": "dataset|doc|graph", "id": "…", "uri": "…", "quote": "…" }
  ],
  "uncertainty": { "level": "low|medium|high", "notes": "…" },
  "governance": { "flags": ["sensitive_data", "restricted_layer"], "actions": ["redacted"] }
}
```

### Contract tests to include
- ✅ returns at least one citation for grounded answers  
- ✅ refuses when no source exists (no “creative fill-in”)  
- ✅ respects UI context (time range, active layers) when provided  
- ✅ never leaks restricted data (CARE + classification gates)

---

## 🗺️ Geospatial contracts

KFM’s UI (MapLibre 2D + Cesium 3D) demands predictable geospatial shapes.

### Contract checks we care about
- ✅ CRS/coordinate assumptions (documented; consistent)
- ✅ Bounding boxes, tile metadata, and query parameters
- ✅ GeoJSON validity (if used)
- ✅ STAC assets link to the correct distributions
- ✅ 3D tiles endpoints (if present) return correct content types + metadata

> 🛰️ Remember: layers must always tie back to provenance. If you can’t cite the layer, it can’t go live.

---

## 🧵 Graph integrity & health checks

KFM’s graph is a *governed knowledge substrate* (not an ad-hoc graph dump).  
This directory can also host **contract-style health checks** that run nightly/weekly:

- ✅ schema drift detection (labels/relationships missing)
- ✅ orphan nodes (entities not connected to provenance)
- ✅ missing required relationships (e.g., Dataset → derivedFrom/prov Activity)
- ✅ deprecated node types still in use

> 🕵️ This aligns with the “graph health checks” idea: prevent the knowledge graph from silently degrading over time.

---

## 🧰 Troubleshooting

<details>
  <summary>🧩 “OpenAPI contract test failed”</summary>

- Confirm you updated the OpenAPI spec *and* the implementation.
- If you changed a response field:
  - add a deprecation alias (preferred), or
  - version the endpoint.
- Re-run provider tests with verbose output:
  ```bash
  pytest -q api/contracts/tests -m provider -vv
  ```

</details>

<details>
  <summary>🛡️ “Policy Pack blocked my change”</summary>

- Read the failing rule ID and locate the corresponding `.rego`.
- If your change is valid but new:
  - update the policy with a justified exception, **or**
  - update metadata/classification so it complies.
- Add/adjust tests to lock the behavior in.

</details>

<details>
  <summary>🤖 “Focus Mode has no citations”</summary>

- This should be treated like a **hard failure**.
- Either:
  - add the missing sources to catalogs/graph, or
  - adjust retrieval so the system can find evidence, or
  - ensure the assistant **refuses** when evidence is unavailable.

</details>

---

## 📚 Design drivers & reference pack (read-only)

These docs informed the *contracts + gates* we enforce here (architecture, UI/API boundaries, provenance, policy-as-code, Story Nodes, Focus Mode, federation, CI/CD rigor, reproducibility, and geospatial/WebGL considerations).

> ✅ Keep this README aligned with the docs when updating contracts.  
> 🧠 If the docs change, update the tests (and vice versa).

### 📦 Core KFM docs
- 🧱 Comprehensive Technical Documentation
- 🧭 Comprehensive Architecture, Features, and Design
- 🤖 AI System Overview
- 🗺️ UI System Overview
- 📥 Data Intake Guide
- 🌟 Latest Ideas & Future Proposals
- 💡 Innovative Concepts to Evolve KFM
- 🧠 Additional Project Ideas
- 🧾 Master Markdown / contribution guidance

### 📚 Supporting reference libraries (portfolios)
- 🤖 AI concepts & safety/reliability reading pack
- 🗺️ Maps/WebGL/virtual worlds reading pack
- 🧰 Programming/CI/CD/security reading pack
- 🗃️ Data management/architecture/DS reading pack
- 🧪 Scientific method / master coder protocol
- 🧾 Documentation/Markdown best practices + templates
- 📊 Data mining notes (data quality, classification, governance relevance)

<!--
SOURCE LINKS (ChatGPT workspace file handles) — safe to keep hidden in GitHub:

Required earlier citations:
-  [oai_citation:0‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
-  [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
-  [oai_citation:2‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
-  [oai_citation:3‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

Primary KFM documents:
- Comprehensive Technical Documentation:  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Comprehensive Architecture, Features, and Design:  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- AI System Overview 🧭🤖:  [oai_citation:6‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- UI System Overview:  [oai_citation:7‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- Data Intake – Technical & Design Guide:  [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Latest Ideas & Future Proposals:  [oai_citation:9‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- Innovative Concepts to Evolve KFM:  [oai_citation:10‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- Additional Project Ideas:  [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- MARKDOWN_GUIDE v13:  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Reference portfolios & supporting docs:
- AI Concepts & more (portfolio):  [oai_citation:13‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- Maps / GoogleMaps / VirtualWorlds / WebGL (portfolio):  [oai_citation:14‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- Various programming languages & resources (portfolio):  [oai_citation:15‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- Data Management / Theories / Architecture / Bayesian (portfolio):  [oai_citation:16‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- Scientific Method / Master Coder Protocol:  [oai_citation:17‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Markdown best practices (docx):  [oai_citation:18‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- Data Mining Concepts & applications:  [oai_citation:19‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
-->

---

## ✅ Maintainer note (tone + intent)

This folder is not “tests for tests’ sake.” It’s how KFM keeps its core promises:

- **Contract-first**
- **Provenance-first**
- **Policy-as-code**
- **Fail closed**
- **Evidence-backed AI**
- **Federation-ready interoperability**

If you’re changing anything that affects these promises, add or update a contract test here. 🧪✨
