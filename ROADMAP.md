# Kansas-Frontier-Matrix — Roadmap

## Milestone 1 — Enrich Data Sources

* **\[Issue] Oral Histories & Indigenous Narratives**

  * [ ] Identify oral history archives (tribal, local historical societies).
  * [ ] Digitize + geocode transcripts.
  * [ ] Link narratives to map features (with context popups).

* **\[Issue] Paleoclimate & Fire Regimes**

  * [ ] Integrate NOAA tree-ring drought indices, pollen core datasets.
  * [ ] Add charcoal/fire frequency records.
  * [ ] Document dataset sources in `data/sources/paleoclimate.json`.

* **\[Issue] Hydrology & Water Management Expansion**

  * [ ] Add flood event datasets + irrigation project layers.
  * [ ] Prototype HEC-RAS flood simulation (historical scenario).

---

## Milestone 2 — Analytical Enhancements

* **\[Issue] Predictive Modeling**

  * [ ] Train model on known settlement sites + environmental factors.
  * [ ] Add experiment log in `mcp/experiments/EXP-SETTLE-PRED.md`.

* **\[Issue] Uncertainty Quantification**

  * [ ] Attach confidence scores to georeferencing + NLP.
  * [ ] Display uncertainty in UI (layer opacity / error bars).

* **\[Issue] Symbolic & Knowledge-Based Reasoning**

  * [ ] Define ontology schema (CIDOC-CRM + geoscience vocab).
  * [ ] Implement rules for treaty/legal inferences.

* **\[Issue] Fractal & Pattern Analysis**

  * [ ] Compute fractal dimension of river meanders.
  * [ ] Run scaling-law analysis on settlement clustering.

---

## Milestone 3 — Storytelling & Education

* **\[Issue] Interactive Story Maps**

  * [ ] Build “Santa Fe Trail” narrative module.
  * [ ] Prototype Dust Bowl timeline (1930s climate + newspapers).

* **\[Issue] Educational Annotations & Glossary Integration**

  * [ ] Link MCP glossary terms into map tooltips.
  * [ ] Add explanatory overlays (railroads, treaties).

* **\[Issue] Crowdsourcing Contributions**

  * [ ] Design submission portal (web form → GitHub PR).
  * [ ] Add contributor guide in `docs/CONTRIBUTING.md`.

* **\[Issue] Thematic Story Layers**

  * [ ] Build “Law & Order” layer (crime events, forts).
  * [ ] Build “Migration” layer (settler + tribal movements).

---

## Milestone 4 — Technical Enhancements

* **\[Issue] 3D Time Animation**

  * [ ] CesiumJS prototype for 1850–present terrain evolution.
  * [ ] Export regionated KML sequences for Google Earth.

* **\[Issue] Semantic Web Integration**

  * [ ] Map entities to Wikidata IDs.
  * [ ] Publish internal knowledge graph as RDF.

* **\[Issue] Modularity & Extensibility**

  * [ ] Refactor ingestion, AI, UI into plugin modules.
  * [ ] Document extension points in `docs/architecture.md`.

* **\[Issue] APIs & External Tools**

  * [ ] Provide REST/GraphQL API endpoints.
  * [ ] Enable GeoJSON/CSV download for datasets.

---

## Milestone 5 — MCP Integration

* **\[Issue] Experiment Reports**

  * [ ] Use template from `mcp/experiments/experiment_template.md`.
  * [ ] Populate first 3 experiments (georeferencing, NLP, predictive site modeling).

* **\[Issue] SOP Documentation**

  * [ ] Add `mcp/sops/georeference_map.md`.
  * [ ] Add `mcp/sops/add_dataset.md`.

* **\[Issue] Model Cards**

  * [ ] Create `mcp/model_cards/nlp_placename.md`.
  * [ ] Create `mcp/model_cards/change_detection.md`.

* **\[Issue] CI/CD Reproducibility**

  * [ ] Add GitHub Actions test to validate STAC JSON.
  * [ ] Add `make reproducibility-check` target.

---

📌 **How to Use This Roadmap**

* Each Milestone → GitHub Milestone.
* Each Issue → GitHub Issue, linked to milestone.
* Each Task → GitHub checklist item inside the issue.
* All experiments → documented in `mcp/experiments/`.
* All models → documented with `mcp/model_cards/`.
* All workflows → documented with `mcp/sops/`.

---
