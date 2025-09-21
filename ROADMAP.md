# Kansas-Frontier-Matrix — Roadmap

---

## Milestone 1 — Enrich Data Sources

* **[Issue] Oral Histories & Indigenous Narratives**
  * [ ] Identify oral history archives (tribal, local historical societies, KHRI collections).
  * [ ] Digitize + geocode transcripts (standard MCP `experiment.md` template).
  * [ ] Link narratives to map features with contextual popups & glossary integration:contentReference[oaicite:0]{index=0}.

* **[Issue] Paleoclimate & Fire Regimes**
  * [ ] Integrate NOAA tree-ring drought indices, pollen core datasets, and charcoal/fire frequency records:contentReference[oaicite:1]{index=1}.
  * [ ] Cross-link to KGS + Neotoma paleo datasets:contentReference[oaicite:2]{index=2}.
  * [ ] Document dataset sources in `data/sources/paleoclimate.json`.

* **[Issue] Hydrology & Water Management Expansion**
  * [ ] Add flood event datasets, irrigation projects, aquifer/well registers:contentReference[oaicite:3]{index=3}.
  * [ ] Prototype HEC-RAS flood simulation (historical scenarios, MCP modeling protocol):contentReference[oaicite:4]{index=4}.
  * [ ] Document in `data/sources/hydrology.json`.

---

## Milestone 2 — Analytical Enhancements

* **[Issue] Predictive Modeling**
  * [ ] Train models on known settlement sites + environmental drivers (DEM, hydrology, soils).
  * [ ] Add experiment log in `mcp/experiments/EXP-SETTLE-PRED.md`.
  * [ ] Explore Bayesian + hybrid (ABM + GIS) predictive frameworks:contentReference[oaicite:5]{index=5}.

* **[Issue] Uncertainty Quantification**
  * [ ] Attach confidence scores to georeferencing, NLP place extraction, and historical map rectification:contentReference[oaicite:6]{index=6}.
  * [ ] Display uncertainty in UI (layer opacity, error bars, probabilistic map shading).

* **[Issue] Symbolic & Knowledge-Based Reasoning**
  * [ ] Define ontology schema (CIDOC-CRM + GeoSciML + treaty/legal vocabularies):contentReference[oaicite:7]{index=7}.
  * [ ] Implement inference rules for treaty/legal land transfers.

* **[Issue] Fractal & Pattern Analysis**
  * [ ] Compute fractal dimension of river meanders, fire scars, and settlement clustering:contentReference[oaicite:8]{index=8}.
  * [ ] Run scaling-law / power-law analysis on migration/event data:contentReference[oaicite:9]{index=9}.

---

## Milestone 3 — Storytelling & Education

* **[Issue] Interactive Story Maps**
  * [ ] Build “Santa Fe Trail” narrative module:contentReference[oaicite:10]{index=10}.
  * [ ] Prototype Dust Bowl timeline (1930s climate + newspapers + soil data).

* **[Issue] Educational Annotations & Glossary Integration**
  * [ ] Link MCP glossary terms into map tooltips:contentReference[oaicite:11]{index=11}.
  * [ ] Add explanatory overlays (railroads, treaties, forts, migration routes).

* **[Issue] Crowdsourcing Contributions**
  * [ ] Design submission portal (web form → GitHub PR):contentReference[oaicite:12]{index=12}.
  * [ ] Add contributor guide in `docs/CONTRIBUTING.md`.

* **[Issue] Thematic Story Layers**
  * [ ] Build “Law & Order” layer (crime events, forts, legal boundaries).
  * [ ] Build “Migration” layer (settler + tribal relocations).

---

## Milestone 4 — Technical Enhancements

* **[Issue] 3D Time Animation**
  * [ ] CesiumJS prototype for 1850–present terrain/land use evolution:contentReference[oaicite:13]{index=13}.
  * [ ] Export regionated KML sequences for Google Earth:contentReference[oaicite:14]{index=14}.

* **[Issue] Semantic Web Integration**
  * [ ] Map entities to Wikidata IDs, align with Linked Open Data vocabularies:contentReference[oaicite:15]{index=15}.
  * [ ] Publish internal knowledge graph as RDF/OWL.

* **[Issue] Modularity & Extensibility**
  * [ ] Refactor ingestion, AI, and UI into plugin modules:contentReference[oaicite:16]{index=16}.
  * [ ] Document extension points in `docs/architecture.md`:contentReference[oaicite:17]{index=17}.

* **[Issue] APIs & External Tools**
  * [ ] Provide REST/GraphQL API endpoints for datasets and knowledge graph:contentReference[oaicite:18]{index=18}.
  * [ ] Enable GeoJSON/CSV downloads for reproducibility.

---

## Milestone 5 — MCP Integration

* **[Issue] Experiment Reports**
  * [ ] Use template from `mcp/experiments/experiment_template.md`:contentReference[oaicite:19]{index=19}.
  * [ ] Populate first 3 experiments (georeferencing, NLP placename extraction, predictive settlement modeling).

* **[Issue] SOP Documentation**
  * [ ] Add `mcp/sops/georeference_map.md`.
  * [ ] Add `mcp/sops/add_dataset.md`.

* **[Issue] Model Cards**
  * [ ] Create `mcp/model_cards/nlp_placename.md`.
  * [ ] Create `mcp/model_cards/change_detection.md`.

* **[Issue] CI/CD Reproducibility**
  * [ ] Add GitHub Actions test to validate STAC JSON:contentReference[oaicite:20]{index=20}.
  * [ ] Add `make reproducibility-check` target.

---

📌 **How to Use This Roadmap**
* Each Milestone → GitHub Milestone.
* Each Issue → GitHub Issue linked to milestone.
* Each Task → GitHub checklist item inside the issue.
* All experiments → `mcp/experiments/`.
* All models → `mcp/model_cards/`.
* All workflows → `mcp/sops/`.

---
