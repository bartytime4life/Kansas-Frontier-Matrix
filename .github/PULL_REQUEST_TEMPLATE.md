<!--
🚀 Kansas Frontier Matrix (KFM) — Pull Request Template

✅ Keep this template intact.
🧹 Delete helper comments (`<!-- ... -->`) as you fill it out.
🧭 Prefer concrete paths, commands, IDs, and sample outputs over vague descriptions.

PR title format (pick one):
- [web] Add timeline slider snapping
- [data] Ingest 1870s county boundaries (COG/GeoJSON)
- [ml] Improve NER for 19th-century spelling
- [api] Add /layers/{id} endpoint
- [infra] Harden Docker + CI caching
-->

# 🚀 Pull Request

> [!NOTE]
> **Keep it reviewable:** 2–3 sentences + reproducible steps + evidence links (when claims/data/models are involved).

> [!IMPORTANT]
> ⛓️ **Pipeline order is absolute:** **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**  
> If it isn’t **cataloged + provenance-linked**, it isn’t publishable in KFM.

---

## 📌 Summary (what + why)

<!-- 1–3 sentences. Assume the reviewer is seeing this cold. -->
**Problem / context:**  

**What changed (solution):**  

**Why it matters (impact):**  

**User-visible outcome:**  

**Release note (optional, 1 line):**  

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
- [ ] 🟡 Medium (touches hot paths / contracts / catalogs)
- [ ] 🔴 High (migrations, infra, widespread behavior change)

**Compatibility / migration required?**
- [ ] No migration needed
- [ ] Data migration needed (describe below)
- [ ] API clients may break (describe below)
- [ ] Feature flag / staged rollout recommended

**Feature flag (if any):** `FLAG_NAME_HERE`  
**Rollback lever:** (revert PR / disable flag / rollback migration / redeploy previous image)  

---

## 🧩 Scope / Areas Touched (check all that apply)
- [ ] 📂 `web/` (UI, map viewer, timeline controls, charts)
- [ ] 📂 `api/` (API boundary, workers, contracts, policy)
- [ ] 📂 `api/scripts/` or `scripts/` (ingestion, conversions, batch jobs)
- [ ] 📂 `notebooks/` (EDA, prototypes, demos)
- [ ] 📂 `mcp/` (experiments/, sops/, glossary, research protocols)
- [ ] 📂 `docs/` (guides, datasets, model cards, architecture)
- [ ] 🗄️ PostgreSQL/PostGIS (migrations, indexes, storage)
- [ ] 🕸️ Neo4j / graph ingestion / graph QA
- [ ] 🛰️ Raster/RS pipeline (GEE, COG, tiles, quicklooks)
- [ ] 🧠 NLP/CV/ML models
- [ ] 🐳 Docker/Compose/CI workflows
- [ ] 🧱 Infrastructure (cloud resources, secrets, networking)

---

## 🔗 Related Issues / Context
Closes: <!-- #123 -->  
Related: <!-- #456, discussion link, doc link -->  

**Optional context links:**
- Design doc:  
- SOP / MCP protocol:  
- Dataset card / model card:  

---

## 🧠 Design & Architecture Notes

**What layer(s) changed?**
- [ ] 🧩 Domain entities / core models
- [ ] 🧠 Use cases / application services
- [ ] 🔁 Interfaces (ports)
- [ ] 🔌 Adapters (DB/web/external services)
- [ ] 🏗️ Infrastructure (frameworks, DB, cloud, containers)

**Interfaces/contracts touched (OpenAPI / JSON Schema / GeoJSON props / STAC fields):**
- 

**Notable tradeoffs / decisions (and why):**
- 

**Reviewer focus (where to look):**
- Key files:  
- Non-obvious logic:  
- Known limitations:  

---

## 🧾 Governance & Evidence (required when making claims)

> [!IMPORTANT]
> Fill this section if your PR adds/changes anything that produces **claims** (datasets, analyses, model outputs, published layers, story/focus artifacts).

**Max input classification touched:** `public | internal | restricted | unknown`  
**Output classification (must be ≥ strictest input):** `public | internal | restricted`  
**Redaction mode:** `strict | balanced | off (must justify)`  

**Evidence pointers (IDs/paths preferred over raw blobs):**
| Type | ID / Path | Notes |
|---|---|---|
| 🛰️ STAC (items/collections) |  |  |
| 🧾 DCAT (dataset/distributions) |  |  |
| 🧬 PROV (run/bundle) |  |  |
| 📄 Run manifest |  |  |
| 🔎 Checksums / diffs |  |  |
| ✅ QA / gate report |  |  |

Checklist:
- [ ] Provenance is recorded (inputs → activity → outputs)
- [ ] No privacy downgrade (classification propagated)
- [ ] License/usage constraints preserved
- [ ] Large binaries avoided in git (use pointers/artifacts)

---

## 🧪 How to Test (repro steps)

### ✅ Local (required)
<!-- Provide exact commands + expected outcome. -->
1.  
2.  
3.  

### 🧰 Commands I ran
- [ ] `make test`
- [ ] `make lint` / `make format`
- [ ] `pytest`
- [ ] `npm test` / `npm run lint`
- [ ] `docker compose up --build`
- [ ] DB migration run + rollback verified
- [ ] Smoke test: map loads + timeline filter works + layers render

### 🧬 Repro notes (pipelines/models/simulations)
- Inputs used (paths/IDs):  
- Seed(s) / config(s):  
- Output artifacts (where to find):  
- Expected checks (what “good” looks like):  

---

## 🖼️ Evidence (screenshots, maps, before/after)

**Before:**  
**After:**  

Optional:
- [ ] GIF / short clip (UI interactions)
- [ ] Sample GeoJSON/STAC snippet (sanitized)
- [ ] EXPLAIN / query plan (for hot SQL paths)

---

## 🧾 Data Provenance & Licensing (required if data changed)

**Source(s) / citation:**  
**License / usage constraints:**  
**Temporal coverage:**  
**Spatial coverage:**  
**Processing steps (tools + parameters):**  

Checklist:
- [ ] Dataset docs updated
- [ ] Catalog metadata updated (STAC/DCAT/PROV)
- [ ] CRS/SRID + units recorded
- [ ] QA checks recorded

---

## 🗄️ Database / Storage Impact (required if DB changes)

- [ ] Migration included (forward + rollback)
- [ ] PostGIS geometry validated (SRID, geometry type)
- [ ] Indexes reviewed (spatial + time filters)
- [ ] Hot query plan checked (EXPLAIN)

**Migration commands:**
- 

**Rollback plan:**
- 

**Storage impact (rough):**
- New data size:  
- Index size:  
- Expected growth rate:  

---

## 🔐 Security, Privacy, and Human-Centered Impact

- [ ] No secrets committed
- [ ] Dependencies reviewed (new packages pinned + vetted)
- [ ] Sensitive data handling considered (PII, location traces, private docs)
- [ ] Input validation updated (assume hostile inputs)
- [ ] Outputs are explainable for intended users
- [ ] If AI involved: limitations + uncertainty communicated

**Security notes / threat considerations:**
- 

---

## 📈 Performance & Cost Notes (if relevant)

- [ ] Streaming/paging used (no giant responses)
- [ ] Rasters/tiles optimized (COG/overviews/appropriate zooms)
- [ ] API bounded (limits/timeouts)
- [ ] Batch job runtime/memory noted

**Benchmarks / profiling:**
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

## ✅ Final Review Checklist (required)

- [ ] Scoped change (no drive-by edits)
- [ ] Tests added/updated **or** explained why not
- [ ] Docs/SOPs updated if behavior changed
- [ ] Relevant commands run (see “How to Test”)
- [ ] Clean architecture boundaries preserved
- [ ] Edge cases considered (nulls, missing geometry, CRS, time ranges)
- [ ] Evidence included for UI/map/data/model changes
- [ ] Provenance + license recorded if data changed
- [ ] Quick security sanity check done

---

<details>
<summary><strong>🧭 Clean Architecture Guardrails (fill out if you changed core logic)</strong></summary>

- [ ] Domain remains framework-agnostic (no DB/web/FS imports)
- [ ] Use cases call outward via ports, not concrete adapters
- [ ] Adapters translate external formats ↔ domain structures
- [ ] New dependencies added only in outer layers
- [ ] Unit tests exist at the use-case level with mocked/stubbed ports

Notes:
- 

</details>

<details>
<summary><strong>🗺️ GIS / Remote Sensing Checklist (fill out if you touched geospatial/raster)</strong></summary>

- [ ] CRS/SRID explicit end-to-end
- [ ] Geometry validity checked
- [ ] Time fields validated (timezone assumptions)
- [ ] Raster outputs cloud-optimized when intended (COG + overviews)
- [ ] Tiles/quicklooks verified (bounds/zooms/seams)
- [ ] Catalog metadata updated (bbox, time range, processing, provenance)

Notes:
- 

</details>

<details>
<summary><strong>🤖 AI/ML Checklist (fill out if you changed models, prompts, training, or inference)</strong></summary>

- [ ] Training config captured (hyperparams, seeds, data version)
- [ ] Train/val/test split documented; leakage avoided
- [ ] Metrics reported (uncertainty where sensible)
- [ ] Model card updated (`docs/model_cards/` if applicable)
- [ ] Limitations/failure modes noted

Notes:
- 

</details>

<details>
<summary><strong>🧫 Scientific Modeling / Simulation Checklist (fill out if you changed simulation/modeling)</strong></summary>

- [ ] Verification checks run (units/invariants/convergence)
- [ ] Validation vs baseline/observations (if available)
- [ ] Assumptions documented
- [ ] Sensitivity analysis noted (key parameters)
- [ ] Results reproducible (inputs + configuration captured)

Notes:
- 

</details>

<details>
<summary><strong>🐳 DevOps / Docker / CI Checklist (fill out if you touched infra)</strong></summary>

- [ ] Images pinned where feasible; least-privilege defaults
- [ ] Secrets injected via env/secret manager (not committed)
- [ ] CI updated (tests/lint/caching)
- [ ] Security scanning considered (deps/images)

Notes:
- 

</details>

<!--
🔎 Grounding marker (template intent):
KFM is interdisciplinary: maps + time + provenance + clean architecture + human-centered impact.
-->
