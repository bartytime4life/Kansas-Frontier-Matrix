# 🧾 Contract Tests (KFM) — `tests/contracts/`

![contracts](https://img.shields.io/badge/tests-contracts-blue)
![provenance](https://img.shields.io/badge/provenance-first-success)
![catalog](https://img.shields.io/badge/catalog-STAC%20%2B%20DCAT%20%2B%20PROV-informational)
![policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-orange)
![ai](https://img.shields.io/badge/AI-Focus%20Mode%20%2B%20Citations-purple)
![fail-closed](https://img.shields.io/badge/quality-fail--closed-critical)

> **What this folder is:** merge-blocking “promises” that keep the Kansas Frontier Matrix from ever shipping *mystery data*, *mystery layers*, or *mystery AI answers*.  
> **What contract tests protect:** data → metadata → graph → API → UI → Story Nodes → Focus Mode AI.

---

<details>
<summary>🧭 Table of Contents</summary>

- [📌 What is a contract test?](#-what-is-a-contract-test)
- [🧠 KFM’s contract spine](#-kfms-contract-spine)
- [✅ Non‑negotiable invariants](#-nonnegotiable-invariants)
- [📁 Expected layout](#-expected-layout)
- [▶️ How to run](#️-how-to-run)
- [🧱 Contract suites](#-contract-suites)
  - [1) Data lifecycle + staging](#1-data-lifecycle--staging)
  - [2) Catalog boundary: Evidence Triplet](#2-catalog-boundary-evidence-triplet)
  - [3) Geospatial artifacts: GeoParquet / COG / PMTiles / 3D Tiles](#3-geospatial-artifacts-geoparquet--cog--pmtiles--3d-tiles)
  - [4) Knowledge Graph (Neo4j)](#4-knowledge-graph-neo4j)
  - [5) API (FastAPI REST + GraphQL)](#5-api-fastapi-rest--graphql)
  - [6) UI contracts (MapLibre + Cesium + Timeline)](#6-ui-contracts-maplibre--cesium--timeline)
  - [7) Story Nodes (Markdown + JSON config)](#7-story-nodes-markdown--json-config)
  - [8) Focus Mode AI (citations + refusal)](#8-focus-mode-ai-citations--refusal)
  - [9) Policy Pack (OPA / Conftest)](#9-policy-pack-opa--conftest)
  - [10) Agents (Watcher → Planner → Executor)](#10-agents-watcher--planner--executor)
  - [11) Simulations + scenario outputs](#11-simulations--scenario-outputs)
  - [12) Offline packs + AR readiness](#12-offline-packs--ar-readiness)
- [🧪 Adding/updating a contract](#-addingupdating-a-contract)
- [🔁 Versioning & breaking changes](#-versioning--breaking-changes)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 Reference docs & embedded libraries](#-reference-docs--embedded-libraries)

</details>

---

## 📌 What is a contract test?

A **contract** is a *versioned, testable promise* between a producer and a consumer.

- **Producer** examples: ingest pipeline, ETL packager, graph builder, API server, Story Node author, Focus Mode service.
- **Consumer** examples: UI layer registry, timeline slider, story engine, knowledge graph queries, audit tools, downstream exports.

A **contract test** asserts that promise in a way that:
- ✅ is machine-checkable (schemas, constraints, invariants),
- ✅ runs in CI as a merge gate,
- ✅ fails *loudly* and *early* (fail‑closed).

> [!IMPORTANT]
> Contract tests are *not* unit tests. They protect **boundaries** (data ↔ metadata ↔ API ↔ UI ↔ AI), where breakage causes the highest user‑trust damage.

---

## 🧠 KFM’s contract spine

KFM is designed so that everything is governed through a **data + metadata + provenance** spine (a.k.a. “the map behind the map”).

```mermaid
flowchart LR
  RAW[📥 Raw Sources] --> ETL[🧪 Ingestion / ETL]
  ETL --> EVID[🧾 Evidence Triplet<br/>STAC + DCAT + PROV]
  EVID --> KG[🕸️ Knowledge Graph]
  KG --> API[🔌 APIs (REST + GraphQL)]
  API --> UI[🗺️ UI (MapLibre + Cesium + Timeline)]
  UI --> STORY[📚 Story Nodes]
  STORY --> AI[🧠 Focus Mode AI (Citations)]
```

**Key idea:** if an artifact can’t be traced (source → transformations → published form), it’s not allowed to appear in the UI or in AI answers.

---

## ✅ Non‑negotiable invariants

These are the “merge blockers” that keep KFM trustworthy. If any fail, **CI should block**.

### 📦 Data & provenance invariants
- [ ] **Raw is immutable**: raw inputs are never overwritten; downstream products are derived.
- [ ] **Deterministic packaging**: the same inputs + specs ⇒ the same outputs (hash‑traceable).
- [ ] **No bypassing catalogs**: anything visible/served must be registered via catalogs.
- [ ] **Evidence Triplet is mandatory**: every published dataset has **STAC + DCAT + PROV**.
- [ ] **License is mandatory**: no dataset/layer/story without explicit license + attribution.
- [ ] **CRS is explicit**: original CRS recorded; display standard is consistent (e.g., WGS84).

### 🕸️ Graph invariants
- [ ] **No orphan nodes**: entities/layers/stories always link to provenance & catalog entries.
- [ ] **Stable IDs**: once published, IDs are durable; changes are versioned, not mutated silently.
- [ ] **Constraints exist**: graph schema constraints/indexes are in place (and tested).

### 🔌 API invariants
- [ ] **Schema-valid IO**: request/response bodies conform to published schemas (OpenAPI/GraphQL).
- [ ] **Time is first-class**: time filters are consistent and ISO‑8601 aligned where applicable.
- [ ] **Fail‑closed validation**: invalid payloads don’t partially ingest; they reject with reason.

### 🗺️ UI & storytelling invariants
- [ ] **No mystery layers**: every visible layer has a “Layer Info” provenance trail (source, license, processing summary).
- [ ] **Story Nodes are machine-ingestible**: Story content is Markdown + a JSON map‑state script.
- [ ] **Timeline compatibility**: time-filterable layers declare their temporal dimension clearly.
- [ ] **Accessibility baseline**: keyboard nav + ARIA roles for custom widgets where needed.

### 🧠 AI invariants (Focus Mode)
- [ ] **Citations are required**: every claim is backed by a cited KFM source (or the model refuses).
- [ ] **Refusal over speculation**: if evidence is missing, answer is “I can’t verify” + suggested next step.
- [ ] **Auditability**: AI output is treated as an artifact with provenance + governance logging.

---

## 📁 Expected layout

This folder is the “contract gate.” Keep contracts **small, explicit, and ruthless**.

```text
tests/contracts/ 🧾
├─ README.md 🧭 (you are here)
├─ schemas/ 🧩                 # JSON Schemas / SHACL shapes / contract definitions
│  ├─ catalog/ 📚              # STAC / DCAT / PROV schemas + shapes
│  ├─ api/ 🔌                  # OpenAPI snapshots, GraphQL SDL/introspection, error model
│  ├─ ui/ 🗺️                   # layer registry schema, story node config schema, offline-pack schema
│  ├─ ai/ 🧠                   # Focus Mode response schema, citation model, audit log schema
│  └─ ops/ ⚙️                  # run_manifest schema, idempotency key, artifact manifest schema
├─ fixtures/ 🧪                # positive + negative examples (golden files)
│  ├─ valid/ ✅
│  └─ invalid/ ❌
├─ policies/ 🛡️               # OPA/Conftest policy tests + sample inputs
├─ graph/ 🕸️                  # Cypher/queries + expected invariants
├─ runners/ 🏃                 # thin wrappers to run validators consistently in CI
└─ docs/ 📎                    # contract rationale + migration notes (optional but recommended)
```

> [!NOTE]
> Canonical specs may live elsewhere (e.g., `src/server/contracts/` for API schemas).  
> This folder’s job is to **verify** them (and pin behavior with fixtures).

---

## ▶️ How to run

> These are reference commands. Wire them into your actual toolchain (`make`, `task`, `pnpm`, etc.) so CI runs them automatically.

### 🐍 Python-first (common for data + API validation)
```bash
pytest -q tests/contracts
```

### 🛡️ Policy Pack (OPA / Conftest)
```bash
# Example layout:
# - policies live at tools/validation/policy/
# - tests/contracts/policies contains inputs + expectations
conftest test tests/contracts/policies -p tools/validation/policy
```

### 🧩 Targeted runs
```bash
pytest -q tests/contracts -k stac
pytest -q tests/contracts -k dcat
pytest -q tests/contracts -k prov
pytest -q tests/contracts -k story_node
pytest -q tests/contracts -k focus_mode
```

---

## 🧱 Contract suites

### 1) Data lifecycle + staging

**Why:** KFM assumes a clean lifecycle (raw → work → processed → catalog). Contract tests ensure nobody “cheats” the pipeline.

**Validate**
- Folder/file conventions for the lifecycle stages.
- Raw immutability (no overwrites; new versions = new paths/IDs).
- Deterministic packaging: outputs are reproducible and hashable.
- Run manifests exist (inputs, outputs, versions, hashes).

**Typical tests**
- ✅ `run_manifest.json` exists per run and is schema-valid.
- ✅ hashes match actual artifacts (no “silent changes”).
- ✅ idempotency keys prevent accidental double-publish.

---

### 2) Catalog boundary: Evidence Triplet

**The Evidence Triplet is the boundary contract:**
- **STAC**: spatial/temporal + assets (what exists, where it is)
- **DCAT**: dataset catalog metadata (who/what/why/licensing)
- **PROV**: lineage (how it was produced)

**Validate**
- Every published dataset/layer has all three.
- STAC items/collections validate via schema + pystac validation.
- DCAT records validate (JSON-LD or RDF) and include license/attribution.
- PROV bundle connects: raw sources → transforms → published assets.

**Typical tests**
- ✅ STAC `id`, `bbox`, `datetime`/`start_datetime`/`end_datetime`, assets w/ media types.
- ✅ DCAT has publisher/source/license, keywords, spatial + temporal.
- ✅ PROV includes `wasDerivedFrom` or equivalent derivation edges for outputs.

---

### 3) Geospatial artifacts: GeoParquet / COG / PMTiles / 3D Tiles

KFM supports both **analysis-friendly** and **UI-friendly** packaging.

**Validate**
- **GeoParquet**: readable, geometry column, CRS metadata, schema stable.
- **COG**: cloud-optimized structure for rasters; supports range requests in serving contexts.
- **PMTiles**: contains expected tilejson metadata & layer names; decode sample tile.
- **3D Tiles/CZML**: tileset root exists; bounding volumes defined; minimal metadata present.

**Contract pattern (dual-format packaging)**
- Same source → produces:
  - `*.parquet` (analytics)
  - `*.pmtiles` (map rendering)
  - plus **STAC + DCAT** entries that register these artifacts, traceable by hashes.

**Typical tests**
- ✅ Both artifacts exist and appear in STAC assets with correct roles.
- ✅ PMTiles header present; minzoom/maxzoom and bounds declared.
- ✅ Parquet schema includes required fields (e.g., unit_code, lithology, age… where applicable).
- ✅ No mismatched CRS: original CRS tracked; display CRS consistent.

---

### 4) Knowledge Graph (Neo4j)

The graph is where KFM becomes a “matrix” rather than a pile of files.

**Validate**
- Required node labels + required properties (IDs, names, types).
- Relationships exist for provenance & catalog linking (no orphan metadata nodes).
- Graph constraints/indexes exist and match expected schema.
- “Graph Health Check” queries are clean (no missing provenance edges, no dangling refs).

**Typical tests**
- ✅ constraint existence (`SHOW CONSTRAINTS`) includes required uniqueness keys.
- ✅ orphan scan query returns 0 rows.
- ✅ all Story Nodes link to at least one evidence artifact (catalog or source reference).

---

### 5) API (FastAPI REST + GraphQL)

KFM is API-centric: UI and future clients (AR, offline packs, mobile) rely on **stable contracts**.

**Validate**
- OpenAPI schema generated by server matches pinned snapshot.
- Pydantic models validate request/response payloads.
- Error model is consistent (shape + codes).
- GraphQL schema is stable (types, fields, nullability).
- Time filters use consistent conventions (ISO‑8601 where applicable).
- Tile endpoints behave predictably (e.g., time-param aware where supported).

**Typical tests**
- ✅ `openapi.json` diff is intentional (breaking changes require version bump).
- ✅ sample requests pass; invalid payloads fail with structured errors.
- ✅ endpoints serving tiles return correct content types.

---

### 6) UI contracts (MapLibre + Cesium + Timeline)

The UI is designed to be **decoupled**: it evolves independently as long as API + schemas hold.

**Validate**
- Layer registry entries have:
  - source + license + attribution
  - dataset ID that resolves to catalog entry
  - geometry/time semantics (for timeline playback)
  - optional sensitivity flags (locks/warnings)
- Timeline slider respects time filters and layer refresh patterns.
- 2D/3D toggle only activates for layers that have 3D equivalents.

**Typical tests**
- ✅ every layer shown in UI resolves to a STAC/DCAT record.
- ✅ “Layer Info” can be computed from metadata (no missing fields).
- ✅ accessibility lint baseline (ARIA + keyboard focus) for core widgets.

---

### 7) Story Nodes (Markdown + JSON config)

Story Nodes are a **governed storytelling engine**:
- Markdown = narrative + citations/media
- JSON = map choreography (map state per step)

**Validate**
- Each story is a folder with:
  - `story.md` (or `<slug>.md`)
  - `story.json` (or `<slug>.json`)
- JSON schema: steps, mapState, layers toggles, timeline year/time, camera/viewport rules.
- Markdown rules: citation format + evidence references must resolve.
- Optional: evidence manifest exists and matches citations.

**Typical tests**
- ✅ JSON config schema-valid (no missing `steps`, no unknown layer IDs).
- ✅ all referenced layers exist in registry/cat.
- ✅ citations resolve to catalog/provenance objects (or approved external references).

> [!TIP]
> Treat Story Nodes like code: PR review required, fixtures recommended, and CI must validate schema.

---

### 8) Focus Mode AI (citations + refusal)

Focus Mode is a **trust-preserving AI assistant** that operates inside KFM’s governance rules.

**Validate**
- Response schema includes:
  - `answer` (text)
  - `citations[]` (machine-resolvable references)
  - `confidence/uncertainty` signals (as defined by the project)
  - `limits` / `cannot_verify` when applicable
- Citations must point to KFM evidence artifacts (STAC/DCAT/PROV, graph nodes, story sources).
- If citations cannot be produced, the system must **refuse** rather than speculate.
- Output is logged (governance ledger / audit trail).

**Typical tests**
- ✅ policy check rejects any AI response that contains claims without citations.
- ✅ “refusal shape” is consistent and user-helpful (suggests next step: ingest missing source, run query, etc.).
- ✅ explainability hooks exist (at minimum: why these sources were used).

---

### 9) Policy Pack (OPA / Conftest)

KFM uses policy-as-code to enforce non-negotiables across CI and runtime.

**Validate**
- Policies exist for:
  - provenance-first publication
  - classification/sensitivity requirements
  - license/attribution requirements
  - AI citation requirements
  - “no bypassing catalogs”
- Conftest tests cover allow/deny scenarios with fixtures.

**Typical tests**
- ✅ `allow = false` for missing license / missing provenance.
- ✅ `allow = false` for AI answers without citations.
- ✅ `allow = false` for datasets added directly to UI registry without catalog record.

---

### 10) Agents (Watcher → Planner → Executor)

KFM proposes (or uses) a multi-agent workflow:
- **Watcher** detects issues/anomalies (signals)
- **Planner** produces deterministic plans with evidence
- **Executor** performs actions (PRs, jobs), but stays governed

**Validate**
- Watcher alerts are stored as artifacts (not ephemeral logs).
- Planner output is structured and reproducible.
- Executor actions are idempotent (safe re-runs), and never bypass review.

**Typical tests**
- ✅ executor PR templates include provenance links.
- ✅ idempotency keys prevent duplicate publish events.
- ✅ kill switch / “manual approval required” gates exist for high-risk actions.

---

### 11) Simulations + scenario outputs

Simulations are **first-class artifacts** (not screenshots).

**Validate**
- Each simulation run produces:
  - output bundle (data + visualization assets)
  - PROV lineage: inputs + parameters + code version
  - catalog entry (STAC/DCAT) so UI can browse and replay results
- Simulation result layers declare time semantics if they animate.

**Typical tests**
- ✅ simulation bundle schema-valid (inputs, params, outputs, hashes).
- ✅ outputs are discoverable via catalog + graph.
- ✅ UI can load result layers like any other dataset (no special cases).

---

### 12) Offline packs + AR readiness

KFM is designed to support offline and future AR clients without changing data governance.

**Validate**
- Offline pack manifests list:
  - included layers/stories
  - artifact hashes
  - licenses/attribution bundle
  - tile archives (e.g., PMTiles/MBTiles) + optional terrain packs
- AR clients remain just “another consumer” of the same APIs and catalog.

**Typical tests**
- ✅ offline pack manifest schema-valid; all referenced artifacts exist.
- ✅ attribution bundle is complete.
- ✅ pack uses open formats (no proprietary lock-in).

---

## 🧪 Adding/updating a contract

### ✅ Golden path (do this in PRs)
1. **Write/Update the schema** in `tests/contracts/schemas/...`
2. **Add fixtures**
   - `fixtures/valid/...`
   - `fixtures/invalid/...` (missing license, missing provenance, broken steps, etc.)
3. **Add/Update the test runner**
   - Schema validation (JSONSchema / SHACL / pystac / cypher checks / conftest)
4. **Update policy rules** (if the invariant is policy-enforced)
5. **Document the change**
   - Add a short note in `tests/contracts/docs/` if breaking/behavior-changing.

### 🧠 Rule of thumb
If a change would cause **the UI** to show something untraceable, or **the AI** to answer without evidence, it must be expressed as a contract test.

---

## 🔁 Versioning & breaking changes

- **Contracts are versioned**. Breaking changes require:
  - a schema version bump (and ideally parallel support for old version during migration),
  - updated fixtures,
  - a migration note.
- Prefer **additive** changes (new optional fields) over **breaking** changes.
- If you must break:
  - ship a migration tool or compatibility adapter,
  - pin old behavior until consumers are updated.

---

## 🧯 Troubleshooting

**“CI says missing Evidence Triplet”**
- You probably published an artifact but didn’t create STAC/DCAT/PROV entries.

**“Layer registry points to unknown dataset ID”**
- The UI is trying to reference a dataset that was never cataloged (blocked by design).

**“Story Node JSON invalid”**
- Step scripts drifted from schema; update either the schema (if feature) or the story config (if mistake).

**“Focus Mode response rejected”**
- You likely emitted claims without citations. Either attach evidence artifacts or return a refusal shape.

**“Graph health check found orphans”**
- A graph ingest job created nodes without catalog/provenance edges. Fix pipeline mapping or constraints.

---

## 📚 Reference docs & embedded libraries

### 📄 Normative KFM docs (design intent → enforced here)
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**
- **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf**
- **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf**
- **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf**
- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf**
- **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf**
- **Additional Project Ideas.pdf**

### 📦 Embedded reference libraries (PDF portfolios)
These are “books inside a PDF.” They’re **non‑normative** but useful for implementation and research.

<details>
<summary>🧠 AI / ML library — <code>AI Concepts &amp; more.pdf</code></summary>

**List embedded docs**
```bash
pdfdetach -list "AI Concepts & more.pdf"
```

**Extract all into a local library folder**
```bash
mkdir -p docs/library/ai
cd docs/library/ai
pdfdetach -saveall "../../../AI Concepts & more.pdf"
```

</details>

<details>
<summary>🗃️ Data engineering + architecture library — <code>Data Managment-Theories-...</code></summary>

```bash
pdfdetach -list "Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf"
```

Notable embedded refs include CI/CD guides, data engineering cookbooks, clean architecture, and statistics texts.

</details>

<details>
<summary>🧰 Programming language + platform library — <code>Various programming langurages &amp; resources 1.pdf</code></summary>

```bash
pdfdetach -list "Various programming langurages & resources 1.pdf"
```

Includes Docker, Postgres, React/TypeScript, security handbooks, and more—handy when wiring contract runners and CI.

</details>

<details>
<summary>🗺️ Mapping + WebGL + GIS library — <code>Maps-GoogleMaps-VirtualWorlds-...</code></summary>

```bash
pdfdetach -list "Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf"
```

Includes WebGL programming references, map projections, geoprocessing with Python, map design, and GIS basics—useful for rendering & projection contracts.

</details>

---

## 🧷 Maintainer checklist (PR review)

- [ ] New dataset/layer has **STAC + DCAT + PROV**
- [ ] License + attribution included everywhere (catalog, UI, exports)
- [ ] Story Nodes changed? ✅ schema-valid, citations resolve
- [ ] API changed? ✅ OpenAPI/GraphQL contracts updated intentionally
- [ ] Graph ingest changed? ✅ health check + constraints pass
- [ ] AI changed? ✅ policy gates still enforce citations/refusal
- [ ] Offline pack changed? ✅ manifest schema + hashes pass

---

> [!FINAL THOUGHT 💡]
> Contract tests are the “trust firewall” of KFM.  
> If a feature can’t be governed, traced, and validated… it doesn’t ship.

