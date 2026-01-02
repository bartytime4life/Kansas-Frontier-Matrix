<!--
🚀 Kansas Frontier Matrix (KFM) / Kansas-Frontier-Matrix — Pull Request Template

Tip: PR Title format (pick one)
- [web] Add timeline slider snapping
- [data] Ingest 1870s county boundaries (COG/GeoJSON)
- [ml] Improve NER for 19th-century spelling
- [api] Add /layers/{id} endpoint
- [infra] Harden Docker + CI caching

(Please keep this template intact—delete helper comments as you fill it out.)
-->

# 🚀 Pull Request

## 📌 Summary (what + why)
<!--
1–3 sentences. Assume a reviewer is seeing this cold.

Example:
Adds a new ingestion step that converts scanned historical map TIFFs to COGs and registers metadata in the spatial catalog, enabling the web viewer to time-filter layers reliably.
-->
**What changed?**  

**Why does it matter?**  

**User impact / outcome:**  

---

## 🎯 Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 🧹 Refactor / cleanup (no behavior change)
- [ ] ⚡ Performance improvement
- [ ] 🔐 Security hardening
- [ ] 🗄️ Data / database change (schemas, migrations, catalog metadata)
- [ ] 🗺️ GIS / remote sensing / mapping change
- [ ] 🤖 AI/ML change (training, inference, prompts, evaluation)
- [ ] 🧪 Scientific modeling / simulation change
- [ ] 📝 Documentation / SOP / research workflow change
- [ ] 🧰 DevOps / CI / Docker / infra change

---

## 🧩 Scope / Areas Touched (check all that apply)
- [ ] 📂 `web/` (UI, map viewer, timeline controls, charts)
- [ ] 📂 `scripts/` (ingestion, georeferencing, conversions, batch jobs)
- [ ] 📂 `notebooks/` (EDA, prototypes, demos)
- [ ] 📂 `mcp/` (experiments/, sops/, glossary, research protocols)
- [ ] 🔌 API / services (REST/RPC, queues, adapters)
- [ ] 🗄️ Database (PostgreSQL/PostGIS / migrations / indexes)
- [ ] 🛰️ Remote sensing / raster pipeline (COG, tiles, QA)
- [ ] 🧠 NLP / CV / ML models
- [ ] 🧭 Visualization / 3D (WebGL / Cesium / terrain tiles)
- [ ] 🐳 Docker / Compose / CI workflows

---

## 🔗 Related Issues / Context
Closes: <!-- #123 -->  
Related: <!-- #456, discussion link, doc link -->  

---

## 🧭 Design & Architecture Notes (keep reviewers oriented)
<!--
KFM is built as a layered system with clean architecture principles:
- keep domain/use-case logic independent of frameworks
- talk inwards with simple structures; talk outwards through interfaces
Add notes here only if it helps reviewers understand boundaries or tradeoffs.
-->
**What layer(s) changed?**
- [ ] 🧩 Domain entities / core models
- [ ] 🧠 Use cases / application services
- [ ] 🔁 Interfaces (ports)
- [ ] 🔌 Adapters (DB/web/external services)
- [ ] 🏗️ Infrastructure (frameworks, DB, cloud, containers)

**New/changed interfaces (ports):**
- 

**Data contracts touched (schemas, GeoJSON properties, STAC-like metadata, API payloads):**
- 

**Notable tradeoffs / decisions:**
- 

---

## 🧪 How to Test (repro steps)
### ✅ Local (required)
<!-- Provide exact commands + expected outcome. -->
1. 
2. 
3. 

### 🧰 Suggested Commands (if applicable)
- [ ] `make test`
- [ ] `make lint` / `make format`
- [ ] `pytest`
- [ ] `npm test` / `npm run lint`
- [ ] `docker compose up --build` (or `docker-compose up --build`)
- [ ] DB migration run + rollback verified

### 🧬 Reproducibility Notes (datasets/experiments)
<!-- If you changed data pipelines, models, or simulation results, explain how a reviewer can reproduce. -->
- Inputs used:
- Seed(s) / config(s):
- Output artifacts:

---

## 🖼️ Evidence (screenshots, maps, before/after)
<!-- If UI/maps changed, include screenshots or short clips. If data changed, include sample output or a small diff snippet. -->
- Before:
- After:

---

## 🧾 Data Provenance & Licensing (required if you added/updated data)
**Source(s) / citation:**  
**License / usage constraints:**  
**Temporal coverage:**  
**Spatial coverage (bbox / region):**  
**Processing steps recorded:**  
- [ ] Updated `sources.json` / catalog metadata
- [ ] Added/updated README/docs for the dataset
- [ ] Included validation notes (QA checks)

---

## 🗄️ Database / Storage Impact (required if DB changes)
- [ ] Migration included (forward + rollback)
- [ ] PostGIS/geometry columns validated (SRID, geometry type)
- [ ] Indexes reviewed (esp. spatial + time filters)
- [ ] Query plan / performance checked for hot paths
- [ ] Backfill strategy documented (if needed)

**Migration notes / commands:**
- 

**Rollback plan:**
- 

---

## 🔐 Security, Privacy, and Human-Centered Impact
<!-- Digital humanism lens: preserve user agency, transparency, privacy, and safety. -->
- [ ] No secrets committed (keys, tokens, credentials)
- [ ] Dependencies reviewed (new packages pinned + vetted)
- [ ] Sensitive data handling considered (PII, location traces, private documents)
- [ ] Outputs are explainable enough for intended users (no “black box surprise”)
- [ ] If AI is involved: limitations + uncertainty are communicated

**Security notes / threat considerations:**
- 

---

## 📈 Performance & Cost Notes (if relevant)
- [ ] Large rasters/tiles are streamed efficiently (COG/tiling strategy)
- [ ] Frontend remains responsive (map layer count, tile sizes, GPU load)
- [ ] API endpoints measured (latency/throughput)
- [ ] Batch jobs tracked (runtime, memory, cloud cost considerations)

**Benchmarks / profiling results:**
- 

---

## 🚦 Rollout / Backout Plan
- [ ] Safe to merge as-is
- [ ] Needs feature flag
- [ ] Needs staged rollout
- [ ] Needs data migration window

**Rollout steps:**
1.  
2.  

**Backout steps:**
1.  
2.  

---

# ✅ Final Review Checklist (required)
- [ ] My PR is scoped (no unrelated drive-by changes)
- [ ] I wrote/updated tests **or** explained why not
- [ ] I updated docs/SOPs where behavior changed
- [ ] I ran the relevant commands in “How to Test”
- [ ] I didn’t break clean architecture boundaries (domain/use-cases don’t import infrastructure)
- [ ] I considered edge cases (nulls, missing geometry, CRS mismatches, time ranges)
- [ ] I included screenshots/evidence for UI/map changes
- [ ] I recorded data provenance + license (if data changed)
- [ ] I included model card/datasheet updates (if ML changed)
- [ ] I did a quick security sanity check (secrets, deps, input validation)

---

<details>
<summary>🧭 Clean Architecture Guardrails (fill out if you changed core logic)</summary>

- [ ] Domain entities remain framework-agnostic (no DB/web/FS imports)
- [ ] Use cases call outward through interfaces (ports), not concrete adapters
- [ ] Adapters translate external formats ↔ simple domain structures
- [ ] New dependency added only in outer layers (infrastructure), not core
- [ ] Unit tests exist at the use-case level with mocked/stubbed ports

Notes:
- 

</details>

<details>
<summary>🗺️ GIS / Remote Sensing Checklist (fill out if you touched geospatial/raster)</summary>

### Coordinate Systems & Geometry
- [ ] CRS/SRID is explicit and consistent end-to-end
- [ ] Geometry validity checked (self-intersections, empties, wrong types)
- [ ] Spatial joins/overlays tested with representative Kansas-area samples

### Raster / Imagery (GeoTIFF/COG/Tiles)
- [ ] Rasters are cloud-optimized (COG) when intended for web streaming
- [ ] Overviews/pyramids generated as appropriate
- [ ] Nodata handling verified (visual + analytic)
- [ ] Tile generation verified (zoom levels, bounds, seams)

### Metadata / Catalog
- [ ] STAC-like metadata updated (bbox, time range, source, processing)
- [ ] Provenance recorded (inputs, tooling, parameters)
- [ ] Any OCR/georeferencing steps documented in SOP/notes

</details>

<details>
<summary>🤖 AI/ML Checklist (fill out if you changed models, prompts, training, or inference)</summary>

### Reproducibility
- [ ] Training config captured (hyperparams, seeds, data version)
- [ ] Train/val/test separation is clear; leakage avoided
- [ ] Metrics reported with uncertainty where sensible

### Documentation
- [ ] Model Card updated (`docs/model_cards/` if applicable)
- [ ] Dataset datasheet updated (if you curated/modified a dataset)
- [ ] Limitations & failure modes noted (esp. historical spelling/scan artifacts)

### Quality & Safety
- [ ] Bias/fairness considerations documented (where applicable)
- [ ] Prompted/LLM outputs include citations or traceability when needed
- [ ] Monitoring plan noted for productionized inference

</details>

<details>
<summary>🧪 Statistics / Experimental Design Checklist (fill out if you report results)</summary>

- [ ] Hypothesis/objective stated clearly
- [ ] Report effect sizes + uncertainty (not just “significant/not significant”)
- [ ] Multiple comparisons / p-hacking risks considered
- [ ] Validation approach described (holdout, k-fold, time-split, spatial-split)
- [ ] Plots/tables are labeled (units, axes, CRS/time window if geospatial)

</details>

<details>
<summary>🧫 Scientific Modeling / Simulation Checklist (fill out if you changed simulation/modeling)</summary>

- [ ] Verification: numerical correctness checks (units, invariants, convergence)
- [ ] Validation: compared against baseline/observations where available
- [ ] Sensitivity analysis noted (key parameters)
- [ ] Assumptions documented (boundary conditions, simplifications)
- [ ] Results are reproducible (inputs + configuration captured)

</details>

<details>
<summary>🐳 DevOps / Docker / CI Checklist (fill out if you touched infra)</summary>

- [ ] Docker images follow best practices (small base, pinned versions)
- [ ] Containers run as non-root where feasible
- [ ] Secrets are injected via env/secret manager (not committed)
- [ ] CI updated (tests, lint, caching)
- [ ] Security scanning considered (deps + images)

</details>

<details>
<summary>📝 Docs / MCP Workflow Checklist (fill out if you touched docs, experiments, SOPs)</summary>

- [ ] Updated relevant SOPs (`mcp/sops/`) for repeatable processes
- [ ] Added/updated experiment log (`mcp/experiments/`) for new results
- [ ] Updated glossary if new terms/acronyms introduced
- [ ] Docs reviewed like code (clear, accurate, linked to changes)

</details>

<!--
🔎 Project-doc grounding markers (for traceability of this template’s intent):
:contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}
:contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}
-->
