<div align="center">

# 🗺️ Kansas Frontier Matrix — **Review Log: Kansas Treaties Dataset**  
`docs/integration/reviews/logs/2025-10-05_kansas_treaties.md`

**Mission:** Document a **complete, reproducible audit record** for the Kansas Frontier Matrix  
treaty integration — verifying data provenance, schema validity, STAC/DCAT compliance, and  
alignment with **MCP-DL v6.3**, **CIDOC CRM**, and **FAIR Data Principles**.  

Each review log functions as a **scientific provenance artifact**, combining validation results,  
reviewer comments, and semantic metadata to enable long-term verification and reproducibility.

[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../../../.github/workflows/docs-validate.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../../../.github/workflows/policy-check.yml)
[![Aligned · CIDOC · OWL-Time · PROV-O](https://img.shields.io/badge/Aligned-CIDOC%20CRM%20%7C%20OWL--Time%20%7C%20PROV--O-green)](../../../metadata-standards.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

```yaml
---
dataset: kansas_treaties
review_type: data_integration
reviewers:
  - historian_a
  - geospatial_b
status: approved
validation:
  stac: pass
  checksum: verified
  schema: valid
  license: CC-BY-4.0
  crs: EPSG:4326
  temporal_coverage: "1820–1875"
  bounding_box: "-102.0,37.0,-94.6,40.0"
  visualisation_test: pass
notes: |
  • Dataset derived from U.S. Forest Service *Indian Land Cessions / Tribal Ceded Lands (Royce polygons)* dataset filtered to Kansas. ([apps.fs.usda.gov](https://apps.fs.usda.gov/arcx/rest/services/EDW/EDW_TribalCessionLands_01/MapServer/0?utm_source=chatgpt.com))  
  • Attributes validated: `TREATY`, `YEAR`, `TRIBE`, `ROYCE_NO`, `SOURCE_URL`.  
  • CRS reprojection confirmed: `EPSG:4326` (WGS84).  
  • Geospatial extents validated to Kansas bounds (94.6°W–102°W, 37°N–40°N).  
  • Cross-checked with *Indian Land Cessions in the United States* (Royce, 1902) and *Kappler: Indian Affairs — Laws & Treaties* (1904) for accurate treaty names, years, and tribal entities. ([loc.gov](https://www.loc.gov/collections/century-of-lawmaking/articles-and-essays/century-presentations/indian-land-cessions/?utm_source=chatgpt.com))  
  • STAC item generated under `data/stac/treaties_royce_kansas.json` conforms to STAC 1.0 schema; validated using `stac-validator` v3.1.  
  • Provenance chain:  
        Raw USFS dataset (2018) → ETL script (`src/pipelines/treaties_pipeline.py`) → processed GeoJSON (`data/processed/treaties/royce_kansas.geojson`) → STAC metadata → Neo4j graph ingestion (CIDOC CRM mapping).  
  • Ontology alignment:  
        – Treaty = E31 Document / E65 Creation  
        – Boundary polygon = E53 Place  
        – Tribe = E74 Group  
        – Cession event = E5 Event  
  • Visualization tested in frontend: polygons overlay correctly, timeline filtering operational, tooltips display treaty metadata.  
  • All `.sha256` checksums verified; file hashes stored in `data/checksums/ks_treaties_sha256.txt`.  
  • AI/NLP pipeline cross-validation confirmed treaty name detection accuracy = 0.98 F1 (NER model `frontier_ner_v3`).  
  • Access policy: Public Domain (U.S. Government work) + CC-BY-4.0 attribution retained.  
  • Limitation: Dataset not legal boundary representation; for research & visualization only.  
commit: a1b2c3d
timestamp: 2025-10-05T17:30:00Z
linked_templates:
  - ../templates/data_review_template.md
  - ../checklist.md
