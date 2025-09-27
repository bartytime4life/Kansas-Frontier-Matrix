# Experiment Template — Kansas Frontier Matrix (MCP Standard)

This template ensures **scientific rigor, transparency, and reproducibility** across all experiments  
(historical, cartographic, geological, environmental, or computational).

- Use glossary links like `[[Glossary:Hypothesis]]` to keep terminology consistent. See: [Glossary](../glossary.md)  
- Keep **raw data** separate and reference paths/IDs. Capture **provenance** and **checksums**.

---

## Metadata

- **Experiment Title/ID**:
- **Date(s)**:
- **Researcher(s)**:
- **Version / Run ID**:
- **Related Repo Branch/Commit**:
- **Links**: PR/Issue, Notebook(s), Dashboard(s)

---

## Problem Statement

> What question or knowledge gap is this experiment addressing?  
> Clearly state the objective (historical, environmental, geospatial, or computational).

---

## Background / Motivation

> Context or theory behind the problem.  
> Why is this important? Include references to prior research, archival sources, or datasets.

---

## Hypothesis

> A testable prediction [[Glossary:Hypothesis]] framed as:  
> *If X (Independent Variable [[Glossary:Independent Variable]]) is changed, then Y (Dependent Variable [[Glossary:Dependent Variable]]) will result.*

---

## Methodology / Procedure

- **Design & Approach**: Step-by-step description of how the experiment will be conducted.
- **Tools & Equipment**: GIS [[Glossary:Cartography]], Python ETL, R spatial analysis, lab methods, etc.
- **Cross-disciplinary Roles** (if applicable):
  - Historian: archival/document analysis [[Glossary:Primary Source]]
  - Cartographer: georeferencing [[Glossary:Georeferencing]], GIS integration [[Glossary:STAC]], layer styling
  - Geologist: stratigraphy [[Glossary:Stratigraphy]], dating, paleo/environmental context [[Glossary:Paleoclimate Proxy]]

---

## Parameters and Variables

- **Independent Variables (IV)**: [[Glossary:Independent Variable]]
- **Dependent Variables (DV)**: [[Glossary:Dependent Variable]]
- **Control Variables**: [[Glossary:Control Variable]]
- **Configurations**: parameter values, ranges, algorithm/model settings
- **Assumptions / Constraints**: list any domain or data limits

---

## Data Collection & References

- **Sources**: raw datasets (e.g., archival docs [[Glossary:Archival Document]], USGS maps [[Glossary:Raster Data]], NOAA climate, KGS boreholes [[Glossary:Core Sample]])
- **Access Paths / IDs**: (`data/raw/...`, STAC item ID [[Glossary:STAC]], API endpoint, DOI)
- **Processing Scripts / Notebooks**: (`scripts/fetch.py`, `scripts/etl/*.py`, `notebooks/*.ipynb`)
- **Licenses & Terms**: cite usage constraints for each source
- **External References**: literature, archives, or documentation

### Data Lineage (fill this table)

| Artifact | Source/ID | Transform(s) | Output Path | SHA-256 |
|---|---|---|---|---|
| Raw map (GeoTIFF) | STAC: usgs_topo_1894 | — | `data/raw/...tif` |  |
| COG | gdal/rio-cogeo | reproject → tile → overviews | `data/cogs/...tif` |  |
| Vector overlay | ogr2ogr | reproject → simplify | `data/processed/...json` |  |

---

## Results / Observations

> Objective reporting (no interpretation here).
- Tables, charts, maps (attach artifacts or link to images).
- Summaries of logs/outputs.
- Notable intermediate results or anomalies.

---

## Analysis / Discussion

- Interpret results relative to the [[Glossary:Hypothesis]].
- Did outcomes support or contradict expectations?
- Identify trends, correlations, or sources of [[Glossary:Uncertainty]].
- Cross-validate historical, cartographic, and geological perspectives.
- Limitations & potential biases.

---

## Conclusion

- Succinct summary of findings.
- State whether the [[Glossary:Hypothesis]] was supported.
- Connect back to the Problem Statement and research objectives.

---

## Future Work / Next Steps

> Improvements, follow-ups, open questions.  
> Example: integrate new [[Glossary:Paleoclimate Proxy]] cores, extend GIS overlays, test symbolic reasoning, expand temporal coverage.

---

## References

- Cite all external data, software, and literature consistently.
- Include version/DOI/URL and access date where applicable.

---

## Reproducibility Notes

- **Environment Config**: (e.g., `configs/exp_ks_treaty_boundary.yaml`) with package pins & seeds
- **Runtime**: OS, CPU/GPU, memory, container image/tag
- **Checksums**: SHA-256 for raw/processed data (`scripts/gen_sha256.sh`) [[Glossary:Reproducibility]]
- **Logs**: `logs/experiments/<ID>/` (JSONL + Markdown run log)
- **STAC / Metadata**: link to catalog item(s) [[Glossary:STAC]]
- **Randomness**: seeds, # of trials, confidence intervals

---

### Checklists

**Pre-run**
- [ ] Hypothesis and variables defined
- [ ] Inputs located, licensed, checksummed
- [ ] Config committed & tagged
- [ ] Glossary terms referenced where relevant

**Post-run**
- [ ] Results artifacts saved (tables/charts/maps)
- [ ] Data lineage table completed
- [ ] Logs & hashes recorded
- [ ] Conclusions & next steps documented

---

✅ By following this template, each experiment becomes a **self-contained, reproducible research log**, consistent with MCP and Kansas-Frontier-Matrix standards.
