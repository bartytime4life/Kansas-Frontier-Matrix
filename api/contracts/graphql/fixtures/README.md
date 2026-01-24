# 🧩 GraphQL Fixtures (KFM Contracts)

![GraphQL](https://img.shields.io/badge/GraphQL-contracts-blue?logo=graphql&logoColor=white)
![KFM](https://img.shields.io/badge/KFM-provenance--first-success)
![STAC](https://img.shields.io/badge/STAC-metadata-informational)
![DCAT](https://img.shields.io/badge/DCAT-catalog-informational)
![PROV](https://img.shields.io/badge/W3C%20PROV-lineage-informational)
![Policy](https://img.shields.io/badge/policy-fail--closed-critical)

> **Golden queries + golden responses** for KFM’s GraphQL contract tests.  
> Deterministic ✅ • Evidence-first 🔎 • Provenance-first 🧾 • Redaction-aware 🛡️

---

## 📍 Where you are

📁 `api/contracts/graphql/fixtures/`

This folder documents and stores **GraphQL fixtures** used to:
- 🔒 Lock the **public GraphQL contract** (schema + resolver behavior)
- 🧭 Protect the **UI contract** (React UI, map viewer, story engine, Focus Mode)
- 🧪 Enable **contract tests** (snapshot/golden-file testing) that catch breaking changes early
- 🏛️ Enforce **governance at the API boundary** (provenance, citations, sensitivity rules)

---

## 🧠 What “fixture” means (in KFM terms)

A fixture is a small, self-contained **scenario**:

✅ Includes:
- A **GraphQL operation** (`query`, `mutation`, or `subscription`)
- Optional **variables**
- Expected **response JSON** (`data` and/or `errors`)
- A **meta file** describing intent + coverage + policy expectations
- (Optional) **seed inputs** for the test environment (Neo4j + PostGIS + document index)

🚫 Not a fixture:
- Production data dumps
- UI mocks without provenance links
- Any response that can drift with time/randomness/network calls

---

## 🗂️ Suggested folder layout

> Keep fixtures **discoverable** and **traceable**. Favor small folders over huge monolith files.

```text
📁 api/contracts/graphql/fixtures/
├─ 📄 README.md
├─ 📄 _manifest.yml                 # the “table of contents” for the fixture runner
├─ 📁 core/                         # core graph traversal + domain primitives
│  └─ 📁 person_events_places/
│     ├─ 📄 query.graphql
│     ├─ 📄 variables.json
│     ├─ 📄 expected.json
│     ├─ 📄 meta.yml
│     ├─ 📄 seed.cypher             # optional
│     └─ 📄 seed.sql                # optional
├─ 📁 evidence/                     # DCAT + STAC + PROV contract coverage
├─ 📁 ui/                           # queries used directly by UI widgets / panels
├─ 📁 focus-mode/                   # AI assistant contracts (must cite, must refuse if not grounded)
├─ 📁 realtime/                     # streaming/simulations (time-aware + provenance-first)
└─ 📁 experimental/                 # Pulse Threads, Concept Nodes, federation, etc.
```

---

## ✅ Fixture quality bar

### ✅ MUST (non-negotiable)

- **Deterministic outputs**
  - Stable IDs, stable ordering, stable timestamps
  - No “now()”, no random seeds, no network calls
- **Evidence-first responses**
  - If a response is derived from a dataset, it must include enough metadata to trace back:
    - DCAT dataset/catalog ID
    - STAC item/collection references (if geospatial assets)
    - PROV activity/entity references (lineage)
- **Governance behavior included**
  - Sensitive data must be **redacted/blurred/role-gated** (fixture should assert the behavior)
  - Focus Mode must **include citations** or **refuse/flag uncertainty**
- **UI-ready contract**
  - Responses powering UI panels include the fields the UI needs:
    - attribution/license, time range, bbox/geometry hints, provenance pointers

### ✅ SHOULD (strongly recommended)

- Include `__typename` for union/interface responses
- Include `pageInfo` (or equivalent) and test pagination behaviors
- Include a “negative case” fixture for common policy failures:
  - missing provenance → fail closed
  - missing citations in AI answer → fail/deny

### 🚫 MUST NOT

- Include real private personal data (PII) in fixture payloads
- Include exact coordinates for restricted/sensitive sites (use generalized geometry)
- Depend on dataset size/ordering that changes with ingestion timing

---

## 🧾 Provenance-first fixture rule (the KFM “Evidence Triplet”)

KFM’s contract philosophy expects **every dataset to be verifiable**:

- **DCAT**: dataset-level catalog + licensing + attribution  
- **STAC**: asset-level spatial/temporal metadata (bbox, time range, links)  
- **PROV**: lineage / how it was produced (pipeline run, parameters, inputs, outputs)

📌 Fixture pattern: if you return a `Dataset`, `Layer`, `Observation`, or “derived insight”, the response should expose references like:

- `dcatId` / `catalogId`
- `stacCollectionId`, `stacItemIds`
- `provActivityId` / `provEntityId`
- `license`, `attribution`

---

## 🗺️ Geospatial & temporal fixture rule

Because KFM is a **map + time** platform:
- always include **time range signals** (e.g., `startDate`, `endDate`, `timestamp`, or `timeExtent`)
- include spatial hints (bbox, centroid, geometry type) sufficient for UI prefetch + filtering
- test **bbox/time filtered queries** (critical for map viewer & timeline slider)

---

## 🤖 Focus Mode fixture rule (AI assistant)

Focus Mode contract fixtures must prove:

- 🧾 **Every answer cites sources** (datasets/docs/graph entities)
- 🧪 **Governance check** is applied before returning an answer
- 🛑 If the system can’t derive an answer from available sources, it must:
  - refuse, or
  - return uncertainty + explain why

📌 Fixtures should include:
- A “happy path” with citations
- A “refusal path” (no sources / policy violation)
- A “sensitive” path (answer exists but user lacks permission → redact/deny)

---

## 🧷 Story Nodes & narrative fixtures

Story content is not just text — it’s a **queryable, evidence-linked artifact**.

Your fixtures should validate that:
- Story Nodes can be retrieved with their **narrative content**
- Story Nodes expose or link to **evidence manifests** (sources used)
- Story Nodes link to graph entities (places/events/datasets) for discovery & auditing

---

## 🧠 Experimental fixtures (Pulse Threads + Concept Nodes)

If enabled in the schema, reserve `experimental/` fixtures for:
- 🧵 **Pulse Threads** (continuous, evidence-backed narratives over time)
- 🧠 **Conceptual Attention Nodes** (knowledge graph “topic hubs”)
- 📦 OCI artifact references for dataset distribution (digest/signature refs)
- 🌐 Federation / cross-matrix queries (Kansas ↔ other “Frontier Matrices”)

---

## 🧪 Fixture file templates

### `meta.yml` (recommended)

```yaml
id: core.person_events_places.v1
title: "Graph traversal: Person → Events → Places"
tags: [core, graph, ui-search]
covers:
  - Query.person
  - Person.events
  - Event.location
policy_expectations:
  citations_required: false
  redaction_expected: false
notes:
  - "Ensures stable ordering by event.startDate ASC then id."
```

### `query.graphql`

```graphql
# id: core.person_events_places.v1
# tags: core, graph, ui-search
query PersonEventsPlaces($name: String!) {
  person(name: $name) {
    id
    name
    events {
      id
      name
      startDate
      location {
        id
        name
      }
    }
  }
}
```

### `variables.json`

```json
{ "name": "Example Person" }
```

### `expected.json` (snippet)

```json
{
  "data": {
    "person": {
      "id": "kfm:person:demo:001",
      "name": "Example Person",
      "events": [
        {
          "id": "kfm:event:demo:1856:001",
          "name": "Example Event",
          "startDate": "1856-05-01",
          "location": { "id": "kfm:place:demo:001", "name": "Example Place" }
        }
      ]
    }
  }
}
```

---

## 🧾 Example: Evidence triplet fixture (Dataset → STAC → PROV)

> Use this to prove the API exposes **traceability hooks** needed for auditing and trust.

```graphql
query DatasetEvidenceTriplet($id: ID!) {
  dataset(id: $id) {
    id
    title
    license
    attribution
    dcat {
      id
      landingPage
    }
    stac {
      collectionId
      itemIds
      bbox
      timeRange { start end }
    }
    prov {
      activityId
      generatedEntityIds
      usedEntityIds
    }
  }
}
```

---

## 🛡️ Example: Sensitivity-aware fixture (geo-obfuscation)

> If a record is classified sensitive, fixtures must assert that **public responses** are generalized or masked.

```graphql
query SensitiveSitePublicView($id: ID!) {
  place(id: $id) {
    id
    name
    sensitivity
    # geometry should be null or generalized depending on policy
    geometry { type coordinates }
    geometryGeneralized { type coordinates }
  }
}
```

Expected behaviors (choose per policy):
- `geometry == null` and `geometryGeneralized` present ✅
- or `geometry.coordinates` rounded / snapped ✅
- or request returns an authorization error ✅

---

## 🧠 Example: Focus Mode fixture (answer with citations)

```graphql
query FocusAnswer($question: String!, $context: FocusContextInput) {
  focusAnswer(question: $question, context: $context) {
    answerMarkdown
    citations {
      kind
      id
      label
    }
    governanceFlags {
      code
      message
    }
  }
}
```

Expected rules:
- `citations.length > 0` for factual claims ✅
- if no grounding sources exist → `errors[]` or `governanceFlags[]` indicate refusal/uncertainty ✅

---

## 🧰 Running / updating fixtures (workflow)

1. 🧱 Update schema (contract-first)
   - add/change fields in the GraphQL SDL
2. 🧪 Add/modify fixtures in this folder
3. 🧾 Update `_manifest.yml`
4. ✅ Run the contract test runner locally (repo-specific command)
5. 🚦 Ensure CI passes
6. 🧭 If breaking change: document it + coordinate with UI + version accordingly

> Tip: if a change is intentional, update the fixture with a clear commit message like:
> `contracts(graphql): update dataset.evidenceTriplet response shape`

---

## 🧭 Fixture coverage checklist

Use this checklist when expanding fixture coverage:

- [ ] Core graph traversal (Person/Place/Event)
- [ ] Dataset discovery (search + filters + pagination)
- [ ] Evidence triplet exposure (DCAT + STAC + PROV)
- [ ] Layer catalog query (for map UI)
- [ ] Time filtering (timeline slider scenarios)
- [ ] Focus Mode: cites or refuses (governance enforced)
- [ ] Sensitivity/redaction behavior
- [ ] Streaming/simulation hooks (if present)
- [ ] Experimental: Pulse Threads / Concept Nodes / federation

---

## 📚 Project references (what these fixtures are designed to match)

### 🧱 Primary KFM design docs

- 📄 *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf*
- 📄 *Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf*
- 📄 *Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf*
- 📄 *Kansas Frontier Matrix – Comprehensive UI System Overview.pdf*
- 📄 *📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf*
- 📄 *Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf*
- 📄 *Additional Project Ideas.pdf*
- 📄 *🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf*
- 📄 *Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design.pdf*

### 📦 Reference library bundles (PDF portfolios)

These are large “portfolio” PDFs containing many embedded books/guides used across KFM engineering:

<details>
<summary>🤖 AI Concepts &amp; more (portfolio) — what’s inside</summary>

- AI Foundations of Computational Agents (3rd Ed)  
- Deep Learning for Coders (fastai + PyTorch)  
- Deep Learning with Python  
- Neural Networks and Deep Learning  
- Artificial Neural Networks (models + applications)

</details>

<details>
<summary>🗺️ Maps / Virtual Worlds / WebGL (portfolio) — what’s inside</summary>

- WebGL Programming Guide (interactive 3D graphics)  
- Understanding Map Projections  
- Google Maps JavaScript API Cookbook  
- Geoprocessing with Python  
- Python Geospatial Analysis Cookbook  
- Archaeological 3D GIS

</details>

<details>
<summary>🧰 Programming languages &amp; resources (portfolio) — what’s inside</summary>

- Comprehensive CI/CD Guide for Software and Data Projects  
- Introduction to Docker  
- TypeScript Notes for Professionals  
- Python Notes for Professionals  
- PostgreSQL / SQL Server / MySQL Notes for Professionals

</details>

<details>
<summary>🗄️ Data Management / Bayesian / Architectures (portfolio) — what’s inside</summary>

- Database Performance at Scale  
- Clean Architectures in Python  
- Data Science: Theories, Models, Algorithms, and Analytics  
- Bayesian Methods for Hackers  
- Comprehensive CI/CD Guide (also mirrored here)

</details>

---

## 🆘 Troubleshooting

### “Fixture failed but code seems fine”
- Check ordering (arrays are the #1 source of nondeterminism)
- Check time defaults (anything “latest” must be explicitly pinned)
- Ensure the seed data exactly matches the expected graph relationships

### “GraphQL change broke UI”
- Add/adjust a `ui/` fixture representing the UI’s query
- Ensure the contract test fails before the UI does ✅

### “Focus Mode test is flaky”
- Fix retrieval scope (use pinned context + deterministic sources)
- Ensure the answer is generated from stable inputs (no live data in this fixture)

---

## ✅ Definition of done (DoD)

A fixture is “done” when:
- ✅ It is deterministic
- ✅ It proves provenance expectations (where applicable)
- ✅ It encodes governance outcomes (redaction/citations)
- ✅ It matches real UI/API usage patterns
- ✅ It’s small, readable, and tagged in `_manifest.yml`

—  
🧭 If you’re unsure where a fixture belongs, default to **`core/`** or **`ui/`**, and add tags for policy coverage.
