# Kansas-Frontier-Matrix — Roadmap

This doc mirrors **`.github/roadmap/roadmap.yaml`** and is synced to GitHub **labels, milestones, and issues** via **`.github/workflows/roadmap.yml`** (drives `scripts/sync-roadmap.js`).

> 🔁 **Pull Requests** run the sync in **dry-run** (no writes).  
> ✅ **Pushes to `main`** (or manual dispatch with `dry_run=false`) **apply** changes.

---

## Contents

- [Milestones (targets)](#milestones-targets)
- [Milestone 1 — Enrich Data Sources (`m1-data`)](#milestone-1--enrich-data-sources-m1-data)
- [Milestone 2 — Analytical Enhancements (`m2-analytics`)](#milestone-2--analytical-enhancements-m2-analytics)
- [Milestone 3 — Storytelling & Education (`m3-story`)](#milestone-3--storytelling--education-m3-story)
- [Milestone 4 — Technical Enhancements (`m4-tech`)](#milestone-4--technical-enhancements-m4-tech)
- [Milestone 5 — MCP Integration (`m5-mcp`)](#milestone-5--mcp-integration-m5-mcp)
- [Label taxonomy (suggested)](#label-taxonomy-suggested)
- [Working agreements](#working-agreements)
- [Edit the source roadmap](#edit-the-source-roadmap)
- [Run the sync locally (optional)](#run-the-sync-locally-optional)

---

## Milestones (targets)

| Key            | Title                     | Target date |
|----------------|---------------------------|-------------|
| `m1-data`      | Enrich Data Sources       | 2025-10-31  |
| `m2-analytics` | Analytical Enhancements   | 2025-11-30  |
| `m3-story`     | Storytelling & Education  | 2025-12-31  |
| `m4-tech`      | Technical Enhancements    | —           |
| `m5-mcp`       | MCP Integration           | —           |

```mermaid
flowchart TD
  M1["Milestone 1\n&quot;Enrich Data Sources&quot;\n(Oct 31, 2025)"] --> M2["Milestone 2\n&quot;Analytical Enhancements&quot;\n(Nov 30, 2025)"]
  M2 --> M3["Milestone 3\n&quot;Storytelling &amp; Education&quot;\n(Dec 31, 2025)"]
  M3 --> M4["Milestone 4\n&quot;Technical Enhancements&quot;"]
  M4 --> M5["Milestone 5\n&quot;MCP Integration&quot;"]
````

---

## Milestone 1 — Enrich Data Sources (`m1-data`)

### Issue: Oral Histories & Indigenous Narratives (`oral-histories`)

**Tasks**

* [ ] Inventory oral-history archives (tribal, KHRI, local historical societies).
* [ ] Digitize & geocode transcripts (use MCP experiment template).
* [ ] Link narratives to features via glossary tooltips/popups.

**Deliverables**

* `data/sources/oral_histories.json` (license, contact, update cadence).
* Story hooks in `web/config/story_layers.json`.

---

### Issue: Paleoclimate & Fire Regimes (`paleo-fire`)

**Tasks**

* [ ] Integrate drought indices, pollen cores, charcoal/fire records.
* [ ] Cross-link with KGS & Neotoma sources; add STAC entries.

**Deliverables**

* `data/sources/paleoclimate.json`
* STAC collections/items under `stac/collections/*`, `stac/items/*`.

---

### Issue: Hydrology & Water Management Expansion (`hydro-expansion`)

**Tasks**

* [ ] Add flood-event datasets (NOAA/FEMA) & irrigation/management (when public).
* [ ] Prototype historical flood scenarios (HEC-RAS; MCP modeling SOP).

**Deliverables**

* `data/sources/hydrology.json`
* Hydrology wired in STAC (`stac/collections/`, `stac/items/`).

---

### Issue: Kansas River (KGS) — Source → STAC → Viewer (`kgs-kansas-river`)

**Tasks**

* [ ] Source: `data/sources/ks_kansas_river.json` (ArcGIS REST + metadata).
* [ ] STAC: `stac/collections/ks_kansas_river.json` (+ children).
* [ ] Items: channels/floodplains/gauges under `stac/items/ks_kansas_river/*.json`.
* [ ] Makefile: `hydrology-fetch`, `hydrology-stac` (plus `site` to mirror vectors to `web/data/**`).
* [ ] Web config: ensure `ksriv_*` layers in generated `web/app.config.json` and fallback `web/layers.json`.

**Acceptance**

* Layers render in the web viewer; provenance in STAC; `make site` mirrors `web/data/processed/hydrology/kansas_river/*.geojson`.

**Directories touched**

* `data/processed/hydrology/kansas_river/`
* `stac/collections/ks_kansas_river.json`
* `stac/items/ks_kansas_river/*.json`
* `web/data/processed/hydrology/kansas_river/*.geojson`
* `web/app.config.json`, `web/layers.json`

---

## Milestone 2 — Analytical Enhancements (`m2-analytics`)

### Issue: Predictive Modeling (`predictive-modeling`)

**Tasks**

* [ ] Train on settlement sites + drivers (DEM, hydrology, soils).
* [ ] Log experiments in `mcp/experiments/EXP-SETTLE-PRED.md`.
* [ ] Explore Bayesian + ABM/GIS hybrids.

**Acceptance**

* Reproducible notebook + experiment report with metrics.

---

### Issue: Uncertainty Quantification (`uncertainty-quant`)

**Tasks**

* [ ] Confidence scores for NLP toponyms & georeferencing/rectification.
* [ ] UI encodings: opacity/error bars/probabilistic shading.

**Acceptance**

* Uncertainty visible in UI; documented in STAC and `docs/`.

---

### Issue: Symbolic & Knowledge-Based Reasoning (`symbolic-reasoning`)

**Tasks**

* [ ] Ontology schema (CIDOC-CRM + GeoSciML + treaty/legal vocabs).
* [ ] Treaty/legal land-transfer inference rules.

**Acceptance**

* Example queries + rule snippets; export RDF/OWL snapshot.

---

### Issue: Fractal & Pattern Analysis (`fractal-patterns`)

**Tasks**

* [ ] Meander fractal dimension, sinuosity metrics; clustering/power-law tests.

**Acceptance**

* Metrics JSON + brief analysis note; optional UI overlay hook.

---

## Milestone 3 — Storytelling & Education (`m3-story`)

### Issue: Interactive Story Maps — Santa Fe Trail (`sft-storymap`)

**Tasks**

* [ ] Assemble routes + primary sources; timeline step-through views.

**Acceptance**

* Hosted story page with linked sources (uses `web/config/story_layers.json`).

---

### Issue: Dust Bowl Timeline Prototype (`dustbowl-timeline`)

**Tasks**

* [ ] Compose 1930s time-series overlays (climate + newspapers + soils).

**Acceptance**

* Time slider demo; uncertainty notes.

---

### Issue: Glossary & Educational Annotations (`glossary-annotations`)

**Tasks**

* [ ] Link MCP glossary terms into map tooltips.
* [ ] Overlays: railroads, treaties, forts, migration routes.

**Acceptance**

* Glossary tooltips render; examples documented.

---

### Issue: Crowdsourcing Submission Portal (`crowdsourcing-portal`)

**Tasks**

* [ ] Web form → GitHub PR bot; contributor guide `docs/CONTRIBUTING.md`.

**Acceptance**

* End-to-end submission merged via PR.

---

## Milestone 4 — Technical Enhancements (`m4-tech`)

### Issue: 3D Time Animation (`time-3d`)

**Tasks**

* [ ] CesiumJS prototype (1850–present); regionated KML/KMZ exports.

**Acceptance**

* 3D demo + KML sample.

---

### Issue: Semantic Web Integration (`semantic-web`)

**Tasks**

* [ ] Map entities to Wikidata; publish RDF/OWL.

**Acceptance**

* RDF dump + minimal SPARQL/GraphQL access plan.

---

### Issue: Modularity & Extensibility (`modularity`)

**Tasks**

* [ ] Define plugin boundaries for ingestion/AI/UI; document extension points.

**Acceptance**

* `docs/architecture.md` sections + example plugin.

---

### Issue: APIs & External Tools (`apis-downloads`)

**Tasks**

* [ ] REST/GraphQL endpoints; GeoJSON/CSV downloads.

**Acceptance**

* Minimal API spec + sample responses.

---

## Milestone 5 — MCP Integration (`m5-mcp`)

### Issue: Experiment Reports (First Three) (`experiments-first-3`)

**Tasks**

* [ ] Use `mcp/experiments/experiment_template.md`.
* [ ] Georeferencing, NLP placename extraction, predictive settlement modeling.

**Acceptance**

* Three completed reports with artifacts.

---

### Issue: SOP Documentation (`sop-docs`)

**Tasks**

* [ ] `mcp/sops/georeference_map.md`, `mcp/sops/add_dataset.md`.

**Acceptance**

* SOPs enforced by CI checks.

---

### Issue: Model Cards (`model-cards`)

**Tasks**

* [ ] `mcp/model_cards/nlp_placename.md`, `mcp/model_cards/change_detection.md`.

**Acceptance**

* Model cards complete; linked in README/docs.

---

### Issue: CI/CD Reproducibility (`ci-repro`)

**Tasks**

* [ ] STAC validation job + CodeQL in CI; `make prebuild` path green.

**Acceptance**

* CI green; targets documented in `README.md` and `docs/`.

---

## Label taxonomy (suggested)

`data`, `hydrology`, `stac`, `web`, `story`, `education`, `analytics`, `uncertainty`, `ontology`, `reasoning`, `fractal`, `3d`, `semantic-web`, `api`, `mcp`, `sop`, `model-card`, `ci`, `docs`, `good-first-issue`.

---

## Working agreements

* **Each Milestone → GitHub Milestone.**
* **Each Issue → GitHub Issue**, linked to a milestone (auto-synced).
* **Tasks** are the issue checklist items.
* **Experiments** in `mcp/experiments/`; **model cards** in `mcp/model_cards/`; **SOPs** in `mcp/sops/`.

**Propose new work:** open an Issue using `.github/ISSUE_TEMPLATE/`
— Bug: `bug_report.md`, Data: `data_addition.md`, Experiment: `experiment_report.md`.

---

## Edit the source roadmap

Make edits in **`.github/roadmap/roadmap.yaml`**; this file is generated documentation.

**Example snippet**

```yaml
milestones:
  - key: m1-data
    title: Enrich Data Sources
    due: 2025-10-31

issues:
  - key: kgs-kansas-river
    title: Kansas River (KGS) — Source → STAC → Viewer
    milestone: m1-data
    labels: [data, hydrology, stac, web]
    tasks:
      - Add sources, collections, items
      - Wire Makefile hydrology targets
      - Mirror vectors to web/data and render layers
```

---

## Run the sync locally (optional)

```bash
npm ci
npm run validate
# Dry run (prints plan, no writes)
npm run sync:dry
# Apply (writes to GitHub; requires a token with repo scope)
GITHUB_TOKEN=ghp_xxx npm run sync
```

```
```
