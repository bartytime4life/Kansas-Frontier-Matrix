<!--
🚀 Kansas Frontier Matrix (KFM) / Kansas-Frontier-Matrix — Pull Request Template (v2)

✅ Keep this template intact.
🧹 Delete helper comments (`<!-- ... -->`) as you fill it out.
🧭 Prefer concrete paths, commands, IDs, and sample outputs over vague descriptions.
🧬 KFM is "evidence-first": if it can't be traced (STAC/DCAT/PROV + run manifests), it's not shippable.

PR Title format (pick one)
- [web] Add timeline slider snapping
- [data] Ingest 1870s county boundaries (COG/GeoJSON)
- [ml] Improve NER for 19th-century spelling
- [api] Add /layers/{id} endpoint
- [infra] Harden Docker + CI caching
- [graph] Add spectral metrics endpoint for subgraph summaries
- [sim] Add hydrology scenario runner + V&V gates

🚫 Don’t:
- paste secrets, keys, tokens, or private dataset links
- attach raw sensitive payloads (use pointers + governed catalogs)
- bypass pipeline order (ETL → catalogs → graph → API → UI → Story Nodes → Focus Mode)
-->

<p align="left">
  <img alt="KFM" src="https://img.shields.io/badge/KFM-governed%20pipeline-1f6feb" />
  <img alt="Evidence" src="https://img.shields.io/badge/evidence-STAC%20%7C%20DCAT%20%7C%20PROV-845ef7" />
  <img alt="Policy" src="https://img.shields.io/badge/policy-deny--by--default-critical" />
  <img alt="Repro" src="https://img.shields.io/badge/reproducible-seeds%20%2B%20manifests-22c55e" />
  <img alt="Human-centered" src="https://img.shields.io/badge/human--centered-digital%20humanism-f97316" />
</p>

> [!NOTE]
> **Reviewer-friendly PRs win.** If you can’t explain it in 2–3 sentences + reproducible steps + evidence links, it’s not done yet.

> [!IMPORTANT]
> **KFM boundary rule:** UI/clients must never query internal stores directly. The API (and governed pipelines) enforce auth + policy + redaction + classification propagation.

---

# 🚀 Pull Request

## 🧭 Quick Nav
- [📌 Summary](#-summary-what--why)
- [⛓️ Pipeline Stage](#️-pipeline-stage-check-all-that-apply)
- [🎯 Type of Change](#-type-of-change)
- [🧯 Risk & Compatibility](#-risk--compatibility)
- [🧩 Scope](#-scope--areas-touched-check-all-that-apply)
- [🔗 Related Issues](#-related-issues--context)
- [🧠 Architecture](#-design--architecture-notes-keep-reviewers-oriented)
- [🧾 Governance & Evidence Gate](#-governance--evidence-gate-required-for-data-claims)
- [🧪 How to Test](#-how-to-test-repro-steps)
- [🖼️ Evidence](#-evidence-screenshots-maps-beforeafter)
- [🧾 Data Provenance](#-data-provenance--licensing-required-if-you-addedupdated-data)
- [🗄️ DB Impact](#-database--storage-impact-required-if-db-changes)
- [🔐 Security & Human Impact](#-security-privacy-and-human-centered-impact)
- [📈 Performance & Cost](#-performance--cost-notes-if-relevant)
- [🚦 Rollout](#-rollout--backout-plan)
- [✅ Final Review Checklist](#-final-review-checklist-required)

---

## 📌 Summary (what + why)
<!--
1–3 sentences. Assume a reviewer is seeing this cold.

Example:
Adds a deterministic ingestion step that converts scanned historical map TIFFs to COGs, registers STAC/DCAT/PROV metadata,
and exposes a catalog-backed layer endpoint for time-filtered viewing in the web map.
-->
**Problem / context:**  

**What changed (solution):**  

**Why it matters (impact):**  

**User impact / outcome:**  

**Release note (1 line, optional):**  

---

## ⛓️ Pipeline Stage (check all that apply)
<!-- KFM ordering matters: don't skip stages. -->
- [ ] 📥 ETL / ingestion / normalization
- [ ] 🏷️ Catalogs (STAC / DCAT / PROV)
- [ ] 🕸️ Graph (references + context, not raw payloads)
- [ ] 🚪 API boundary (contracts + auth + policy + redaction)
- [ ] 🌐 UI / map / timeline / charts
- [ ] 📚 Story Nodes (governed narrative artifacts)
- [ ] 🎯 Focus Mode (evidence-bundled experience)

**If you changed earlier stages, what downstream stages did you validate?**  
- 

---

## 🎯 Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 🧹 Refactor / cleanup (no behavior change)
- [ ] ⚡ Performance improvement
- [ ] 🔐 Security hardening
- [ ] 🗄️ Data / database change (schemas, migrations, catalog metadata)
- [ ] 🗺️ GIS / remote sensing / mapping change
- [ ] 🕸️ Graph / ontology / knowledge modeling change
- [ ] 🤖 AI/ML change (training, inference, prompts, evaluation)
- [ ] 🧪 Statistics / experimental results / analytics change
- [ ] 🧫 Scientific modeling / simulation / optimization change
- [ ] 📝 Documentation / SOP / research workflow change
- [ ] 🧰 DevOps / CI / Docker / infra change
- [ ] 💥 Breaking change (requires coordination)

---

## 🧯 Risk & Compatibility
**Risk level:**  
- [ ] 🟢 Low (localized, easy rollback)
- [ ] 🟡 Medium (touches hot paths / data contracts)
- [ ] 🔴 High (migrations, infra, widespread behavior change)

**Compatibility / migration required?**
- [ ] No migration needed
- [ ] Data migration needed (describe below)
- [ ] API clients may break (describe below)
- [ ] Feature flag / staged rollout recommended

**Feature flag (if any):** `FLAG_NAME_HERE`  
**Rollback lever:** (e.g., revert migration / disable flag / deploy previous image)  

---

## 🧩 Scope / Areas Touched (check all that apply)
- [ ] 📂 `web/` (UI, map viewer, timeline controls, charts, a11y, perf)
- [ ] 📂 `api/` (API boundary, workers, contracts, policy)
- [ ] 📂 `scripts/` / `api/scripts/` (ingestion, conversions, batch jobs)
- [ ] 📂 `notebooks/` (EDA, prototypes, demos)
- [ ] 📂 `mcp/` (experiments/, sops/, glossary, research protocols)
- [ ] 📂 `docs/` (guides, datasets, model cards, architecture)
- [ ] 🗄️ Database (PostgreSQL/PostGIS / migrations / indexes)
- [ ] 🕸️ Graph (Neo4j / ontology / graph QA)
- [ ] 🛰️ Remote sensing / raster pipeline (GEE, COG, tiles, QA)
- [ ] 🧠 NLP / CV / ML models
- [ ] 🧭 Visualization / 3D (WebGL / Cesium / terrain tiles)
- [ ] 🐳 Docker / Compose / CI workflows
- [ ] 🧱 Infrastructure (cloud resources, secrets, networking)
- [ ] 📦 Catalog artifacts (STAC/DCAT/PROV bundles)
- [ ] 🧾 Provenance / attestations / SBOM

---

## 🔗 Related Issues / Context
Closes: <!-- #123 -->  
Related: <!-- #456, discussion link, doc link -->  

**Context links (optional):**
- Design doc:  
- SOP / MCP protocol:  
- Dataset card / model card:  
- Prior art / references:  

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

**Notable tradeoffs / decisions (and why):**
- 

**Reviewer focus (where to look):**
- Key files:  
- Non-obvious logic:  
- Known limitations:  

---

## 🧾 Governance & Evidence Gate (required for data claims)
> [!IMPORTANT]
> **If your PR makes a claim** (new dataset, new analysis result, new model output, new map layer), you must link to evidence:
> - **What changed** (diffs)
> - **How it was produced** (command + params + versions)
> - **Where it is cataloged** (STAC/DCAT/PROV IDs/paths)
> - **What gates passed** (schema/policy/QA/reproducibility)

### 🔐 Classification & Redaction
**Max input classification touched:** `public | internal | restricted | unknown`  
**Output classification (must be ≥ strictest input):** `public | internal | restricted`  
**Redaction mode:** `strict | balanced | off (must justify)`  

**Redaction / privacy notes (what fields were removed/generalized and why):**
- 

### 📦 Evidence pointers (fill what applies)
<!-- Prefer stable IDs over raw links; use governed catalogs/pointers. -->
| Evidence Type | ID / Path / Link | Notes |
|---|---|---|
| 🛰️ STAC Item(s) / Collection(s) |  |  |
| 📚 DCAT Dataset / Distribution |  |  |
| 🧾 PROV Run / Bundle |  |  |
| 📄 Run manifest (`run.manifest.json`) |  |  |
| 🧱 Diffs (CAS / checksums) |  |  |
| ✅ Gate report (`gates.json`) |  |  |
| 🧬 SBOM (SPDX) |  |  |
| 🔏 Attestation (SLSA/DSSE/Sigstore) |  |  |
| 📈 Telemetry (runtime/mem/energy) |  |  |
| 🖼️ UI preview artifacts (thumbs/golden images) |  |  |

### ✅ Gate Matrix (check what you ran)
- [ ] 🧾 Contract/schema validation (OpenAPI / JSON Schema)
- [ ] 🧩 Policy-as-code (OPA/Conftest) — **default deny**
- [ ] 🧪 Domain QA (CRS/bbox/time/units/invariants)
- [ ] 🔁 Reproducibility check (same seed/time → same hashes)
- [ ] 🔐 Security checks (secrets, dependency audit, SSRF/validation)
- [ ] 🧬 Supply-chain checks (SBOM present; images pinned; signatures verified)
- [ ] 🌿 Energy/carbon telemetry recorded (if applicable / SLOs)

**Artifacts location (repo path):**  
- e.g. `.artifacts/<lane>/<domain>/<YYYY-MM-DD>/...`

**Reproducer (paste exact command):**
```bash
# Example pattern (adapt to your tool/lane):
# kfm-sim-run --domain <x> --change <run.yaml> --seed <0x...> --commit <sha> --time "<ISO>" --fixtures <path> --out <dir>
```

---

## 🧪 How to Test (repro steps)
### ✅ Local (required)
<!-- Provide exact commands + expected outcome. -->
1.  
2.  
3.  

### 🧰 Suggested Commands (check what you ran)
- [ ] `make test`
- [ ] `make lint` / `make format`
- [ ] `pytest`
- [ ] `npm test` / `npm run lint`
- [ ] `docker compose up --build` (or `docker-compose up --build`)
- [ ] DB migration run + rollback verified
- [ ] Smoke test: map loads + timeline filter works + layers render
- [ ] Contract tests: OpenAPI/Schema examples validated
- [ ] Policy gates: OPA/Conftest deny-by-default verified
- [ ] Repro run: hash-equality verified (if artifacts produced)

### 🧬 Reproducibility Notes (datasets/experiments/simulations)
<!-- If you changed pipelines, models, simulations, or analytics, explain how to reproduce exactly. -->
- Inputs used (paths/IDs):  
- Seed(s) / config(s) / frozen time (if any):  
- Toolchain versions (docker digests / lockfiles):  
- Output artifacts (where to find):  
- Expected metrics / checks (what “good” looks like):  

---

## 🖼️ Evidence (screenshots, maps, before/after)
<!-- If UI/maps changed, include screenshots or short clips. If data changed, include sample output or a small diff snippet. -->
**Before:**  
**After:**  

**Helpful extras (optional):**
- [ ] GIF / short clip of interaction (timeline slider, layer toggles)
- [ ] Sample GeoJSON snippet / STAC item snippet (sanitized)
- [ ] Query plan / EXPLAIN output (for hot SQL paths)
- [ ] Golden image diff (UI/tiles/quicklooks)

---

## 🧾 Data Provenance & Licensing (required if you added/updated data)
> [!IMPORTANT]
> If you added/updated data, KFM needs **provenance + licensing** captured as first-class facts.

**Source(s) / citation:**  
**License / usage constraints:**  
**Temporal coverage:**  
**Spatial coverage (bbox / region):**  
**Processing steps recorded (tooling + parameters):**  
**Catalog IDs (STAC/DCAT/PROV):**  

Checklist:
- [ ] Updated dataset docs / catalog metadata
- [ ] Added/updated a dataset README/docs (what it is, how to use, caveats)
- [ ] Included validation notes (QA checks)
- [ ] Captured CRS/SRID + units explicitly
- [ ] Avoided committing giant binaries (use pointers/object store where possible)

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

**Storage impact (rough):**
- New data size:  
- New indexes size:  
- Expected growth rate (if known):  

---

## 🔐 Security, Privacy, and Human-Centered Impact
<!-- Digital humanism lens: preserve user agency, transparency, privacy, and safety. -->
- [ ] No secrets committed (keys, tokens, credentials)
- [ ] Dependencies reviewed (new packages pinned + vetted)
- [ ] Sensitive data handling considered (PII, location traces, private documents)
- [ ] Input validation added/updated for new endpoints / ingestion (assume hostile inputs)
- [ ] Outputs are explainable enough for intended users (no “black box surprise”)
- [ ] If AI is involved: limitations + uncertainty are communicated; **advisory-only** posture maintained
- [ ] If map outputs are involved: cartographic choices aren’t misleading (ramps, legends, aggregation)

**Threat considerations (1–3 bullets):**
- Likely abuse case(s):  
- Worst plausible data exposure if compromised:  
- Mitigations added:  

---

## 📈 Performance & Cost Notes (if relevant)
- [ ] Large rasters/tiles are streamed efficiently (COG/tiling strategy)
- [ ] Frontend remains responsive (layer count, tile sizes, GPU load)
- [ ] API endpoints measured (latency/throughput) and bounded (limits/timeouts)
- [ ] Batch jobs tracked (runtime, memory, cloud cost considerations)
- [ ] Large queries are paged/streamed; no accidental O(N) defaults on huge data

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
- [ ] If artifacts were produced: I linked **run manifest + gates report + checksums** (or equivalent)

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

### 🧭 Coordinate Systems & Geometry
- [ ] CRS/SRID is explicit and consistent end-to-end
- [ ] Geometry validity checked (self-intersections, empties, wrong types)
- [ ] Spatial joins/overlays tested with representative Kansas-area samples
- [ ] Time fields validated (timezone assumptions, missing dates, ranges)
- [ ] GeoJSON/SQL building is safe (no string-format injection; parameters validated)

### 🛰️ Raster / Imagery (GeoTIFF/COG/Tiles)
- [ ] Rasters are cloud-optimized (COG) when intended for web streaming
- [ ] Overviews/pyramids generated as appropriate
- [ ] Nodata handling verified (visual + analytic)
- [ ] Tile generation verified (zoom levels, bounds, seams)
- [ ] Quicklooks/legends generated with documented symbology choices

### ☁️ GEE / Remote Platforms (if applicable)
- [ ] Export params captured (scale, CRS, region, resampling, reducer, bands)
- [ ] Derived products documented (units, QA thresholds, masks)
- [ ] Outputs registered in catalogs (STAC/DCAT) with PROV lineage

### 🧾 Metadata / Catalog
- [ ] STAC/DCAT metadata updated (bbox, time range, source, processing)
- [ ] Provenance recorded (inputs, tooling, parameters, versions)
- [ ] Any OCR/georeferencing steps documented in SOP/notes

</details>

<details>
<summary>🕸️ Graph / Knowledge Model Checklist (fill out if you touched graph/ontology)</summary>

- [ ] Graph stores **references** to cataloged artifacts (no raw sensitive payload duplication)
- [ ] Node/edge IDs are stable + documented (no accidental churn)
- [ ] Cardinality/constraints considered (avoid “explode the graph” patterns)
- [ ] Query complexity bounded (limits, pagination, timeouts)
- [ ] If you added graph metrics (e.g., spectral/centrality): explainability + cost noted
- [ ] Orphan checks / referential integrity checks run

Notes:
- 

</details>

<details>
<summary>🏗️ Optimization / Topology Optimization Checklist (fill out if you changed optimization workflows)</summary>

- [ ] Objective(s) stated clearly (what is minimized/maximized)
- [ ] Constraints stated clearly (bounds, feasibility, safety factors)
- [ ] Solver/config recorded (method, tolerances, stopping criteria)
- [ ] Convergence evidence included (plots/iterations/residuals)
- [ ] Sensitivity to key parameters noted
- [ ] Results are cataloged + provenance-linked (inputs → activity → outputs)

Notes:
- 

</details>

<details>
<summary>🤖 AI/ML Checklist (fill out if you changed models, prompts, training, or inference)</summary>

### ♻️ Reproducibility
- [ ] Training config captured (hyperparams, seeds, data version)
- [ ] Train/val/test separation is clear; leakage avoided
- [ ] Metrics reported with uncertainty where sensible
- [ ] Model artifacts versioned (hashes), not “latest.bin”

### 🧾 Documentation & Governance
- [ ] Model Card updated (`docs/model_cards/` if applicable)
- [ ] Dataset datasheet updated (if you curated/modified a dataset)
- [ ] Limitations & failure modes noted (esp. historical spelling/scan artifacts)
- [ ] AI outputs are labeled where surfaced; advisory-only + evidence-backed in Focus Mode

### 🛡️ Quality & Safety
- [ ] Bias/fairness considerations documented (where applicable)
- [ ] Prompted/LLM outputs include citations/traceability when needed
- [ ] Monitoring plan noted for productionized inference

Notes:
- 

</details>

<details>
<summary>🧪 Statistics / Experimental Design Checklist (fill out if you report results)</summary>

- [ ] Hypothesis/objective stated clearly
- [ ] Assumptions stated (design, sampling, independence, stationarity where relevant)
- [ ] Report effect sizes + uncertainty (not just “significant/not significant”)
- [ ] Multiple comparisons / p-hacking risks considered
- [ ] Validation approach described (holdout, k-fold, time-split, spatial-split)
- [ ] Diagnostics included (residual checks, outliers, leverage/influence, posterior checks)
- [ ] Plots/tables are labeled (units, axes, CRS/time window if geospatial)

Notes:
- 

</details>

<details>
<summary>🧫 Scientific Modeling / Simulation Checklist (fill out if you changed simulation/modeling)</summary>

- [ ] Verification: numerical correctness checks (units, invariants, convergence)
- [ ] Validation: compared against baseline/observations where available
- [ ] Sensitivity analysis noted (key parameters)
- [ ] Assumptions documented (boundary conditions, simplifications)
- [ ] Results are reproducible (inputs + configuration captured; seeds/time frozen if needed)
- [ ] Outputs are treated as governed artifacts (cataloged + provenance-linked)

Notes:
- 

</details>

<details>
<summary>🌐 Web / UI / 3D Checklist (fill out if you touched frontend, tiles, visuals, or WebGL)</summary>

- [ ] Responsive behavior verified (desktop/tablet/mobile)
- [ ] A11y basics checked (labels, contrast, keyboard nav where applicable)
- [ ] Performance budget considered (bundle size, tile sizes, GPU load)
- [ ] Map symbology not misleading (legends, ramps, aggregation choices documented)
- [ ] 3D is optional + degrades gracefully (feature flag or capability detect)
- [ ] Media formats chosen intentionally (PNG/JPEG/GIF) with correct content-types
- [ ] Thumbnails/quicklooks optimized (size/quality tradeoff documented)

Notes:
- 

</details>

<details>
<summary>🐳 DevOps / Docker / CI Checklist (fill out if you touched infra)</summary>

- [ ] Docker images follow best practices (small base, pinned versions)
- [ ] Containers run as non-root where feasible
- [ ] Secrets are injected via env/secret manager (not committed)
- [ ] CI updated (tests, lint, caching)
- [ ] Security scanning considered (deps + images)
- [ ] Supply-chain: SBOM generated where required; attestations attached where applicable
- [ ] OIDC/token scopes are least-privilege (PR open/update ≠ merge)

Notes:
- 

</details>

<details>
<summary>📝 Docs / MCP Workflow Checklist (fill out if you touched docs, experiments, SOPs)</summary>

- [ ] Updated relevant SOPs (`mcp/sops/`) for repeatable processes
- [ ] Added/updated experiment log (`mcp/experiments/`) for new results
- [ ] Updated glossary if new terms/acronyms introduced
- [ ] Docs reviewed like code (clear, accurate, linked to changes)
- [ ] Claims in narrative docs are evidence-linked (catalog IDs, citations)

Notes:
- 

</details>

<details>
<summary>📚 Project Reference Library Alignment (why these sections exist)</summary>

> This section is reference-only: it maps the project’s research/library files to the PR “gates” and checklists above.
> If your change touches a domain, fill out the matching checklist.

| Project file | PR sections it reinforces |
|---|---|
| Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation | Pipeline stages, governance gate, clean architecture, Focus Mode evidence posture |
| MARKDOWN_GUIDE_v13 (Master Guide) | “Evidence-first” + canonical pipeline ordering + Story/Focus constraints |
| Latest Ideas | Deterministic runs (seed/time), hermetic CI, OPA/Conftest gates, SBOM/attestations, artifact tables |
| Data Spaces | Pointer-over-payload, avoid committing huge binaries, stable IDs + references |
| Introduction to Digital Humanism | Security/privacy + human agency + transparency requirements |
| Principles of Biological Autonomy | Explicit state transitions, bounded automation, feedback loops (jobs/simulations) |
| On the path to AI Law’s prophecies… | AI output labeling/auditability, dispute/appeal readiness, provenance expectations |
| Cloud-Based Remote Sensing with Google Earth Engine | GEE export parameters, reproducible remote sensing workflows, catalog emission |
| python-geospatial-analysis-cookbook | CRS/SRID hygiene, PostGIS patterns, safe geometry handling |
| making-maps-a-visual-guide-to-map-design-for-gis | Cartographic ethics, legends/symbology documentation, avoid misleading defaults |
| Mobile Mapping: Space, Cartography and the Digital | Offline/low-bandwidth UX patterns, location sensitivity considerations |
| PostgreSQL Notes for Professionals | Migration discipline, indexes, EXPLAIN plans, safe DB ops |
| Scalable Data Management for Future Hardware | Bounded work, streaming/paging, performance awareness on large datasets |
| Concurrent, Real-Time and Distributed Programming (Java) | Idempotency, backpressure, deadlines/timeouts for queues/jobs |
| Spectral Geometry of Graphs | Explainable graph metrics and bounded graph computations |
| Scientific Modeling and Simulation (NASA-grade) | V&V, assumptions, reproducibility, scenario metadata, sensitivity |
| Generalized Topology Optimization for Structural Design | Objective/constraints metadata, convergence evidence, governed artifacts |
| Understanding Statistics & Experimental Design | Avoid misleading inference; effect sizes + uncertainty; proper validation |
| graphical-data-analysis-with-r | EDA artifacts, diagnostics, outlier reporting, exploration discipline |
| regression-analysis-with-python + regression slides | Regression assumptions + diagnostics; standardized result tables |
| think-bayes-bayesian-statistics-in-python | Priors disclosed, posterior summaries, credible intervals |
| Deep Learning for Coders (fastai/PyTorch) | Artifact/version-driven ML; training outside API runtime; model cards |
| responsive-web-design-with-html5-and-css3 | Responsive delivery + performance budgets for UI assets |
| webgl-programming-guide (WebGL) | 3D safety, coordinate sanity, optional/feature-gated 3D |
| compressed-image-file-formats (JPEG/PNG/GIF/…) | Quicklook/thumbnail format choices; compression tradeoffs |
| A / B–C / D–E / F–H / I–L / M–N / O–R / S–T / U–X programming books | Contributor shelf: cross-language conventions, tooling literacy, future adapters |

</details>

<!--
🔎 Grounding marker (template intent):
KFM is interdisciplinary: maps + time + data provenance + clean architecture + human-centered impact.
-->
