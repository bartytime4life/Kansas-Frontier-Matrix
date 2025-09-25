Here’s a tightened, GitHub-safe `ROADMAP.md` you can paste in as a full replacement. I fixed Mermaid fencing (triple backticks), quoted node labels (GitHub parser quirk), normalized headings/anchors, and wired quick “how to edit” + local sync instructions that match your `kfm-roadmap-sync` tool.

````markdown
# Kansas-Frontier-Matrix — Roadmap

This roadmap mirrors **.github/roadmap/roadmap.yaml** and is synced to GitHub
**labels, milestones, and issues** by `.github/workflows/roadmap.yml`.

> 🔁 Pull Requests run the sync in **dry-run** (no writes).  
> ✅ Pushes to `main` (or manual run with `dry_run=false`) **apply** changes.

---

## Milestones (targets)

| Key            | Title                        | Target date |
|----------------|------------------------------|-------------|
| `m1-data`      | Enrich Data Sources          | 2025-10-31  |
| `m2-analytics` | Analytical Enhancements      | 2025-11-30  |
| `m3-story`     | Storytelling & Education     | 2025-12-31  |
| `m4-tech`      | Technical Enhancements       | —           |
| `m5-mcp`       | MCP Integration              | —           |

```mermaid
flowchart TD
  M1["Milestone 1\nEnrich Data Sources (Oct 31, 2025)"] --> M2["Milestone 2\nAnalytical Enhancements (Nov 30, 2025)"]
  M2 --> M3["Milestone 3\nStorytelling & Education (Dec 31, 2025)"]
  M3 --> M4["Milestone 4\nTechnical Enhancements"]
  M4 --> M5["Milestone 5\nMCP Integration"]
````

---

## Milestone 1 — Enrich Data Sources (`m1-data`)

### Issue: Oral Histories & Indigenous Narratives (`oral-histories`)

* [ ] Identify oral-history archives (tribal, local historical societies, KHRI).
* [ ] Digitize + geocode transcripts (use MCP experiment template).
* [ ] Link narratives to features with glossary tooltips/popups.
  **Deliverables**: `data/sources/oral_histories.json` (license, contact, update cadence).

### Issue: Paleoclimate & Fire Regimes (`paleo-fire`)

* [ ] Integrate drought indices, pollen cores, charcoal/fire records.
* [ ] Cross-link to KGS + Neotoma paleo datasets.
  **Deliverables**: `data/sources/paleoclimate.json` + STAC registration.

### Issue: Hydrology & Water Management Expansion (`hydro-expansion`)

* [ ] Add flood-event datasets (NOAA/FEMA), irrigation/management layers (where public).
* [ ] Prototype HEC-RAS historical flood scenarios (MCP modeling SOP).
  **Deliverables**: `data/sources/hydrology.json` + hydrology collections/items in `stac/`.

### Issue: Kansas River (KGS) — Source → STAC → Viewer (`kgs-kansas-river`)

* [ ] Source: `data/sources/ks_kansas_river.json` (ArcGIS REST + metadata).
* [ ] STAC: `stac/collections/ks_kansas_river.json` (+ child links).
* [ ] Items: channels/floodplains/gauges under `stac/items/ks_kansas_river_*.json`.
* [ ] Makefile targets: `hydrology-fetch`, `hydrology-stac`, `hydrology`.
* [ ] Web config: add `ksriv_*` layers to `web/app.config.json` and `web/layers.json`.
  **Acceptance**: layers render in the viewer; provenance cited in STAC.

---

## Milestone 2 — Analytical Enhancements (`m2-analytics`)

### Issue: Predictive Modeling (`predictive-modeling`)

* [ ] Train models on known settlement sites + drivers (DEM, hydrology, soils).
* [ ] Log experiments in `mcp/experiments/EXP-SETTLE-PRED.md`.
* [ ] Explore Bayesian + ABM/GIS hybrids.
  **Acceptance**: reproducible notebook + experiment report with metrics.

### Issue: Uncertainty Quantification (`uncertainty-quant`)

* [ ] Confidence scores for NLP toponyms & georeferencing/rectification output.
* [ ] UI: opacity/error bars/probabilistic shading rules.
  **Acceptance**: uncertainty visible in UI; documented in STAC/README.

### Issue: Symbolic & Knowledge-Based Reasoning (`symbolic-reasoning`)

* [ ] Define ontology schema (CIDOC-CRM + GeoSciML + treaty/legal vocabs).
* [ ] Implement treaty/legal land-transfer inference rules.
  **Acceptance**: example queries + rule snippets; export RDF/OWL snapshot.

### Issue: Fractal & Pattern Analysis (`fractal-patterns`)

* [ ] Meander fractal dimension, sinuosity metrics; clustering/power-law analysis.
  **Acceptance**: metrics JSON + short analysis note; hooks for UI overlays.

---

## Milestone 3 — Storytelling & Education (`m3-story`)

### Issue: Interactive Story Maps — Santa Fe Trail (`sft-storymap`)

* [ ] Assemble route layers + primary sources; timeline step-through views.
  **Acceptance**: hosted story page with linked sources.

### Issue: Dust Bowl Timeline Prototype (`dustbowl-timeline`)

* [ ] Compose time-series overlays (1930s climate + newspapers + soils).
  **Acceptance**: time slider demo; brief uncertainty notes.

### Issue: Glossary & Educational Annotations (`glossary-annotations`)

* [ ] Link MCP glossary terms into map tooltips.
* [ ] Overlays: railroads, treaties, forts, migration routes.
  **Acceptance**: glossary tooltips render; examples documented.

### Issue: Crowdsourcing Submission Portal (`crowdsourcing-portal`)

* [ ] Web form → GitHub PR bot; contributor guide `docs/CONTRIBUTING.md`.
  **Acceptance**: end-to-end submission merged via PR.

---

## Milestone 4 — Technical Enhancements (`m4-tech`)

### Issue: 3D Time Animation (`time-3d`)

* [ ] CesiumJS prototype (1850–present); regionated KML/KMZ exports.
  **Acceptance**: 3D demo + KML sample.

### Issue: Semantic Web Integration (`semantic-web`)

* [ ] Map entities to Wikidata; publish RDF/OWL.
  **Acceptance**: dump + minimal SPARQL/GraphQL access plan.

### Issue: Modularity & Extensibility (`modularity`)

* [ ] Plugin boundaries for ingestion/AI/UI; extension sections in docs.
  **Acceptance**: `docs/architecture.md` sections + example plugin.

### Issue: APIs & External Tools (`apis-downloads`)

* [ ] REST/GraphQL endpoints; GeoJSON/CSV downloads.
  **Acceptance**: minimal API spec + sample responses.

---

## Milestone 5 — MCP Integration (`m5-mcp`)

### Issue: Experiment Reports (First Three) (`experiments-first-3`)

* [ ] Use `mcp/experiments/experiment_template.md`.
* [ ] Georeferencing, NLP placename extraction, predictive settlement modeling.
  **Acceptance**: three completed reports with artifacts.

### Issue: SOP Documentation (`sop-docs`)

* [ ] `mcp/sops/georeference_map.md`, `mcp/sops/add_dataset.md`.
  **Acceptance**: SOPs followed by CI checks.

### Issue: Model Cards (`model-cards`)

* [ ] `mcp/model_cards/nlp_placename.md`, `mcp/model_cards/change_detection.md`.
  **Acceptance**: cards complete; linked in README/docs.

### Issue: CI/CD Reproducibility (`ci-repro`)

* [ ] Add STAC validation job; `make reproducibility` target.
  **Acceptance**: CI green; target documented.

---

## Working Agreements

* **Each Milestone → GitHub Milestone.**
* **Each Issue → GitHub Issue** linked to a milestone (auto-synced).
* **Tasks** are the issue checklist items.
* **Experiments** live in `mcp/experiments/`; **model cards** in `mcp/model_cards/`; **SOPs** in `mcp/sops/`.

### Propose new work

Open an issue using one of the templates in `.github/ISSUE_TEMPLATE/`:

* Bug: `bug_report.md`
* Data: `data_addition.md`
* Experiment: `experiment_report.md`

---

## Edit the source roadmap

All edits should be made in **.github/roadmap/roadmap.yaml**; this file is generated documentation.

**Example snippet**:

```yaml
milestones:
  - key: m1-data
    title: Enrich Data Sources
    due: 2025-10-31

issues:
  - key: oral-histories
    title: Oral Histories & Indigenous Narratives
    milestone: m1-data
    labels: [data, narrative, indigenous]
    tasks:
      - Identify oral-history archives (tribal, KHRI, local societies)
      - Digitize + geocode transcripts (MCP template)
      - Link narratives to features with glossary tooltips
```

---

## Run the sync locally (optional)

```bash
npm ci
npm run validate
# Dry run (prints plan, no writes)
npm run sync:dry
# Apply (writes to GitHub; requires GITHUB_TOKEN with repo scope)
GITHUB_TOKEN=ghp_xxx npm run sync
```

```
```
