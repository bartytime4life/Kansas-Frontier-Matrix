# 🧪 GraphQL Contract Tests (KFM)

> 📍 **Path:** `api/contracts/graphql/tests/`  
> 🧭 **Mission:** Protect KFM’s **GraphQL boundary** so the UI + external consumers can evolve safely *without breaking trust, governance, or provenance*.  
> 🧱 **Why GraphQL matters in KFM:** KFM uses GraphQL for relationship-heavy queries (graph traversal) and expects **cost controls** (depth limits, pagination, result sizing). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🎯 What these tests are for

These are **contract tests**, not “unit tests for resolvers.”

They validate the *public promise* of the GraphQL API:
- ✅ The schema stays stable (or changes in controlled, reviewable ways)
- ✅ Example operations keep working with stable response shapes
- ✅ Governance & safety invariants are enforced **at the API boundary**
- ✅ Responses remain **evidence-first** / **provenance-safe**

KFM’s broader architecture is explicitly **contract-first** and **provenance-first**: anything that shows up in the UI (or in Focus Mode) must remain traceable back to cataloged sources, with continuous checks preventing “mystery layers.” [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧬 KFM contract philosophy (applies here)

KFM treats metadata + interfaces as “code with gates”:
- **STAC / DCAT / PROV** are linked and validated in CI; KFM uses profile versioning to keep these consistent over time. [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Governance is enforced via **Policy Packs** (OPA + Conftest), with a **fail-closed** posture. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- Focus Mode outputs must carry citations and are blocked if they cannot cite evidence (policy + runtime checks). [oai_citation:5‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:6‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

**Translation for GraphQL contracts:**  
Schema changes and new fields are not “just code”—they are governance surface area.

---

## 🧱 What we test (contract layers)

### 1) 📜 Schema-level contracts (SDL & introspection)
Typical checks:
- Schema compiles ✅
- No accidental breaking changes ✅  
  (removed fields, changed nullability, changed enum values, etc.)
- Deprecations are used intentionally (instead of silent breaks) ✅
- Required “governance fields” exist where mandated (e.g., provenance hooks, citations metadata) ✅

> 📝 Contributor guidance aligns with this: define the contract first (GraphQL schema), implement resolver/controller, **include contract tests**, and add **redaction rules** if data is sensitive. [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

### 2) 🧾 Operation-level contracts (known queries/mutations)
These tests run a curated set of `.graphql` operations that represent:
- UI critical paths (search, entities, datasets, map layers)
- Graph traversal patterns (people → events → places)
- Dataset discovery paths (Dataset / Collection / Distribution style flows)

KFM’s technical docs describe GraphQL types like **Person**, **Place**, **Event**, **Dataset**, etc., and emphasize graph traversal use-cases. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

### 3) 🛡️ Governance & safety contracts (must never regress)
These are the “trust gates” most likely to be enforced in CI and (optionally) runtime:
- **Provenance-first behavior** (no unsourced “official” outputs) [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Citations required** for AI-mediated outputs and certain narrative responses [oai_citation:10‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **Sensitivity-aware handling** (classification tags, access control, location generalization, restrictions) [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Fail closed** enforcement (if governance signals are missing, the contract test should fail) [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

KFM explicitly plans to encode and enforce ethics-aware access patterns (including cultural protocols / restricted content workflows) and geo-obfuscation patterns for sensitive location data. [oai_citation:13‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) [oai_citation:14‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

### 4) 💸 Query cost & abuse contracts (GraphQL needs guardrails)
The GraphQL endpoint is expected to guard against expensive queries via:
- recursion depth limits
- pagination requirements
- maximum result sizes [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Contract tests here typically prove:
- “too deep” queries are rejected
- unpaginated list queries fail or are capped
- overly expensive queries return a controlled error (not timeouts)

---

## 🗂️ Suggested folder map

> This is a *recommended* layout. Your repo may already have some of these files; if not, this is the target structure that makes contract tests easy to maintain.

```text
📁 api/
  📁 contracts/
    📁 graphql/
      📄 schema.graphql          # or schema.graphqls / generated SDL
      📁 operations/             # contract operations used by UI + integrations
        📄 person_by_name.graphql
        📄 dataset_by_id.graphql
      📁 fixtures/               # stable expected responses (goldens)
        📄 person_by_name.json
        📄 dataset_by_id.json
      📁 tests/
        📄 README.md             # (you are here)
        🧪 test_schema_snapshot.py
        🧪 test_operations_contracts.py
        🧪 test_query_limits.py
        🧪 test_sensitivity_redaction.py
        🧪 test_provenance_invariants.py
```

---

## ⚙️ Running the contract tests locally

Because KFM’s backend is described as a **stateless FastAPI service** with REST + GraphQL endpoints, most contract tests run in one of two modes:
1) **Against a running API** (fast iteration)
2) **Against a test stack** (API + Neo4j/PostGIS seeded fixtures), if/when included [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Environment variables (suggested)
- `KFM_GRAPHQL_URL` (default idea: `http://localhost:8000/graphql`)
- `KFM_TEST_AUTH_MODE` (`public` | `internal` | `admin`)
- `KFM_AUTH_TOKEN` (optional; for restricted contract suites)

> 🧠 Why “auth modes” matter: KFM expects sensitivity classification and role-based filtering (hide or generalize sensitive locations, restrict certain datasets, etc.). [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🧪 Example commands (pick what matches your repo)
> Adjust for your tooling (Poetry / uv / pip / tox). Keep the *intent* consistent.

```bash
# Run only GraphQL contract tests
pytest api/contracts/graphql/tests -q

# Run a single contract module
pytest api/contracts/graphql/tests/test_schema_snapshot.py -q
```

---

## 🧷 How contract fixtures should work (golden testing)

### ✅ Principle
Golden fixtures are for **shape + invariants**, not for brittle “every value must match forever.”

Best practice:
- Assert *structure*, *required fields*, *nullability rules*, *pagination shape*, and *governance metadata presence*.
- Allow values to vary when they are expected to vary (timestamps, IDs, counts), but validate their format.

### 🎯 Why this aligns with KFM
KFM describes “metadata as code with tests” and CI schema validation for core profiles (STAC/DCAT/PROV). Contract fixtures are the GraphQL equivalent: a stable consumer-facing promise backed by automated gates. [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧰 Adding or changing GraphQL contracts

### ✅ When adding a new field/type/query
1. **Update the GraphQL contract first** (schema / SDL).
2. Add/extend **contract tests** for:
   - schema diff / snapshot
   - at least one real operation that exercises it
3. If the field can expose sensitive content:
   - implement redaction rules
   - add sensitivity tests  
   (this is explicitly called out in KFM’s contributor guidance) [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
4. Ensure provenance hooks exist where relevant (datasets, AI outputs, story-linked content).

### 🚨 When making breaking changes
Preferred pattern:
- **Deprecate** → add replacement → migrate consumers → remove later
- Add a contract test that proves:
  - deprecated field still exists (until removal window)
  - replacement field works and is documented

---

## 🔒 Governance invariants (non-negotiables)

### 1) 📎 Provenance-first (no “mystery outputs”)
KFM’s architecture requires traceability for anything presented in the UI or Focus Mode. [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Contract tests should enforce (as applicable):**
- dataset-like objects expose identifiers that can link to STAC/DCAT/PROV
- derived responses include provenance summaries or reference IDs
- “official” endpoints do not return uncataloged entities

### 2) 🧾 Citations required (especially AI outputs)
Focus Mode is designed to always provide citations and refuse if it cannot cite evidence. [oai_citation:22‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

**Contract tests should enforce (if GraphQL exposes AI/Focus Mode features):**
- responses include `citations[]` or a similar evidence payload
- empty citations ⇒ hard fail (or controlled refusal response)

### 3) 🪶 Sensitivity-aware access
KFM applies:
- location generalization (coarsening coordinates)
- access controls (login / restricted)
- sensitivity tagging in metadata [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

The broader roadmap emphasizes cultural protocol thinking and sensitivity filters, including geo-obfuscation patterns for vulnerable locations. [oai_citation:24‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) [oai_citation:25‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

**Contract tests should include:**
- “public” mode returns generalized locations (or hides them)
- “internal/admin” mode can access full precision where allowed
- sensitive datasets are tagged and handled consistently

### 4) 🕵️ Privacy doesn’t stop at raw data
Data mining outputs can leak sensitive information even when raw data isn’t exposed; privacy needs to include downstream/derived outputs too. [oai_citation:26‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

**Contract tests should consider:**
- aggregate endpoints: minimum group size thresholds
- redaction of quasi-identifiers
- stable rules around “what can be inferred” from outputs

---

## 🧯 Policy-as-code alignment

KFM’s governance approach includes:
- structured manifests for runs (auditability)
- policies in Rego (OPA) evaluated in CI (Conftest)
- secret scanning style checks
- **fail closed** defaults [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

**How GraphQL contract tests can support this:**
- produce machine-readable test artifacts (JSON summaries) consumable by policy gates
- ensure schema/contract changes cannot bypass governance checks

---

## 🔁 CI expectations (how this should behave in PRs)

KFM’s CI is described as a Detect → Validate → Promote pipeline, including schema conformance and policy gates. [oai_citation:28‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

**Recommended PR rule:**
- Any GraphQL schema change must include:
  - updated schema snapshot (or equivalent)
  - at least one contract operation test
  - governance/sensitivity tests if relevant

KFM also explores mapping GitHub PR activity into PROV records to make development history queryable and auditable (including invariants for CI completeness). [oai_citation:29‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🧩 How this connects to the UI (why UI folks care)

KFM’s UI is designed as a decoupled React app communicating via REST + GraphQL; trust is preserved by surfacing provenance, citations, and context directly in the UX. [oai_citation:30‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

Focus Mode answers are displayed with citations and click-through evidence, turning AI into a transparent guide—not a black box. [oai_citation:31‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

**So contract tests here protect:**
- UI data-fetch assumptions
- Story Node + Focus Mode integrations
- “map behind the map” trust model

---

## 🧠 Quick checklist for new tests

- [ ] Does the test protect a **consumer promise** (UI/external), not an implementation detail?
- [ ] Does it enforce **provenance/citation** invariants where required?
- [ ] Does it cover **public vs restricted** access differences?
- [ ] Does it prevent **expensive GraphQL abuse** (depth/pagination)?
- [ ] If it adds new capability, did we add/adjust **policy-as-code** gates?

---

## 📚 Project docs used for this README

> These are the primary KFM design references that inform the GraphQL contract testing philosophy.

-  [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  
-  [oai_citation:33‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf  
-  [oai_citation:34‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf  
-  [oai_citation:35‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) Kansas Frontier Matrix – Comprehensive UI System Overview.pdf  
-  [oai_citation:36‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf  
-  [oai_citation:37‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) MARKDOWN_GUIDE_v13.md.gdoc  
-  [oai_citation:38‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf  
-  [oai_citation:39‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) Additional Project Ideas.pdf  
-  [oai_citation:40‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH) Data Mining Concepts & applictions.pdf  
-  [oai_citation:41‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf  
-  [oai_citation:42‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf  
-  [oai_citation:43‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr) AI Concepts & more.pdf  
-  [oai_citation:44‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2) Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf  
-  [oai_citation:45‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6) Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf  
-  [oai_citation:46‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi) Various programming langurages & resources 1.pdf  

---

## 🧵 TODOs (optional but recommended)

- 🧪 Add schema snapshot + diff tooling (SDL + introspection)  
- 🧾 Add curated `.graphql` operations representing UI critical paths  
- 🛡️ Add explicit “public vs internal” redaction fixtures (coordinates + sensitive fields)  
- 💸 Add query depth + pagination enforcement tests (guardrails)  
- 🔐 Wire test output summaries into policy-as-code gates (fail closed)
