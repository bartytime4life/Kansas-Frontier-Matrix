<div align="center">

# 📘 **Kansas Frontier Matrix — Glossary**  
`docs/glossary.md`

**Mission:** Provide a **canonical reference** for all technical, geospatial, historical, and procedural terms used across the **Kansas Frontier Matrix (KFM)** — ensuring cross-discipline clarity, transparency, and interoperability in documentation, datasets, and pipelines.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue?logo=markdown)](../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Glossary"
version: "v1.2.0"
last_updated: "2025-10-17"
owners: ["@kfm-docs","@kfm-architecture"]
tags: ["glossary","standards","mcp","ontology","stac","graph","etl","security"]
status: "Active"
license: "CC-BY 4.0"
ci_required_checks:
  - docs-validate
  - markdownlint
semantic_alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - DCAT 2.0
  - CIDOC CRM
  - OWL-Time
  - JSON Schema
  - ISO 8601
---
```

---

## 📚 Overview

The **KFM Glossary** is a **cross-domain reference** for developers, researchers, historians, and data scientists.  
It aligns language across all MCP-compliant documentation and serves as a **knowledge interface** linking the project’s **data architecture**, **pipelines**, **ontologies**, and **CI/CD systems**.

**Organization**
- 🧱 Architecture & Infrastructure
- 🌎 Geospatial & Environmental Data
- 🧩 Metadata & Interoperability
- 🧠 Knowledge Graph & Semantics
- 📜 Historical & Archival Concepts
- ⚙️ CI/CD & Governance
- 🔐 Security & Supply Chain
- 🧪 AI/ML & NLP

---

## 🧩 Core Terminology

| Term | Definition | Context |
|:------|:-------------|:----------|
| **MCP / MCP-DL** | Documentation-first methodology ensuring reproducibility, provenance, and transparency (Markdown **house style**). | Required across all KFM modules and READMEs. |
| **RMI / DCI** | Repository Maturity Index / Dynamic Compliance Index — metrics tracking MCP-DL & CI coverage. | Reported in `docs/audit/repository_compliance.md`. |
| **STAC (SpatioTemporal Asset Catalog)** | Open schema for describing spatiotemporal assets (Collections/Items/Assets). | `data/stac/` + `src/pipelines/load/stac_writer.py`. |
| **DCAT 2.0** | W3C vocabulary for dataset catalogs. | Metadata crosswalks in docs/standards. |
| **ETL (Extract–Transform–Load)** | Fetch → Transform → Enrich → Load pipelines. | `src/pipelines/*/`. |
| **Checksum (SHA-256)** | Cryptographic hash for integrity verification and provenance. | Created in CI and `checksum_utils.py`. |
| **CIDOC CRM** | Cultural heritage ontology used for people/places/events/documents. | Graph schema in `src/graph/`. |
| **OWL-Time** | Temporal ontology representing instants/intervals and sequencing. | Timeline normalization in `date_normalizer.py`. |
| **JSON Schema** | Validation standard for JSON structures. | STAC and internal metadata validation. |
| **GeoTIFF (COG)** | Cloud-Optimized GeoTIFF for web-ready rasters. | Terrain/imagery in `data/processed/rasters/`. |
| **GeoJSON** | Vector data format for geospatial entities. | Output of `vector_to_geojson.py`. |
| **CSV / Parquet** | Tabular formats for time-series/statistical data. | Census and hydrology datasets. |
| **OCR** | Optical Character Recognition — scans → text. | `kansas_memory_ingest.py`, newspapers. |
| **Pipeline** | Automated sequence of ETL tasks bound by MCP. | `Makefile` + CI workflows. |
| **Provenance** | Dataset lineage from source → transforms → artifacts. | Sidecars `.meta.json`, CI logs, STAC. |
| **Auditability** | Ability to verify each dataset/model result. | Checksums, CI artifacts, golden tests. |
| **Ontology** | Structured representation of concepts/relations. | Knowledge Graph modeling. |
| **Knowledge Graph** | Semantic network linking entities (people, places, events, docs). | Neo4j / RDF exports. |
| **RDF / JSON-LD / TTL** | Linked data formats for graph export. | `graph_export.py`. |
| **SPARQL / Cypher** | Query languages for RDF/Neo4j. | Semantic/graph queries in API. |
| **PROV-O** | W3C Provenance Ontology for lineage modeling. | Enrichment metadata. |
| **STAC Item / Collection** | Item = asset record; Collection = grouped items. | Catalog indexing and timelines. |
| **Temporal Range** | Start/end or interval for datasets/events. | Timeline slider + OWL-Time. |
| **Makefile** | Task automation wrapper for reproducible builds. | `make fetch/transform/enrich/load`. |

---

## 🌎 Geospatial & Environmental Terms

| Term | Definition | Context |
|:------|:-------------|:----------|
| **DEM** | Digital Elevation Model raster. | USGS 3DEP / Kansas 1m DEM. |
| **LiDAR** | Laser-based elevation capture. | Source for DEMs/hillshades. |
| **Raster / Vector** | Pixel/geometry-based geodata. | DEMs vs. roads/hydrology. |
| **COG** | Cloud-Optimized GeoTIFF for HTTP-range streaming. | Web map performance. |
| **EPSG:4326 (WGS84)** | Lat/Lon coordinate system. | Standardized output CRS. |
| **CRS** | Spatial projection reference. | Reprojection step in transform. |
| **BBox** | Bounding box for queries/metadata. | STAC `bbox` fields. |
| **NHD / WBD** | Hydrography / Watershed boundaries. | Hydrologic modeling overlays. |

---

## 🧠 Knowledge Graph & Semantics

| Term | Definition | Context |
|:------|:-------------|:----------|
| **Entity / Relationship** | Node (Person/Place/Event/Document) and edge (e.g., `OCCURRED_AT`). | Neo4j schema. |
| **Graph Schema** | Definition of labels, properties, and relationships. | `src/graph/graph_schema.py`. |
| **Inference** | Rule-based reasoning to derive relations. | `src/graph/reasoner.py`. |
| **JSON-LD Export** | Graph export for semantic web consumption. | `graph_export.py --format jsonld`. |
| **Similarity Edge** | `SIMILAR_TO` relation for AI/NLP similarity. | Enrichment → Graph linking. |

---

## 🧩 Metadata & Interoperability

| Term | Definition | Context |
|:------|:-------------|:----------|
| **FAIR** | Findable, Accessible, Interoperable, Reusable. | Data strategy baseline. |
| **Open Standards** | Non-proprietary formats and schemas. | JSON, CSV, GeoTIFF, STAC, JSON Schema. |
| **STAC Extensions** | Additional fields beyond core spec (e.g., `processing:`, `proj:`). | Catalog enrichment. |
| **DCAT** | W3C dataset catalog vocabulary. | Crosswalking with STAC for portals. |

---

## ⚙️ CI/CD & Governance

| Term | Definition | Context |
|:------|:-------------|:----------|
| **GitHub Actions** | Build/Test/Deploy workflows. | `.github/workflows/`. |
| **Golden Tests** | Expected outputs for regression checks. | ETL pipelines. |
| **Artifact** | Build/validation output (logs, docs, SBOM). | CI retention policy. |
| **OIDC** | OpenID Connect for cloud auth (no PATs). | Pages/deploy security. |
| **Conventional Commits** | Semantic commit message format. | Release notes & changelogs. |

---

## 🔐 Security & Supply Chain

| Term | Definition | Context |
|:------|:-------------|:----------|
| **CodeQL** | Static application security testing. | `codeql.yml` |
| **Trivy** | Dependency & container CVE scanning + SBOM. | `trivy.yml` |
| **SLSA** | Supply-chain Levels for Software Artifacts. | Target L3 with provenance signing. |
| **Sigstore / Cosign** | Artifact signing & verification. | Planned `provenance.yml`. |
| **Dependabot** | Automated dependency PRs. | Security posture. |

---

## 🧪 AI/ML & NLP

| Term | Definition | Context |
|:------|:-------------|:----------|
| **NER** | Named Entity Recognition (people/places/events/dates). | `src/nlp/ner_model.py`. |
| **Summarization** | LLM-based text condensation. | `src/nlp/summarizer.py`. |
| **Entity Linking** | Mapping mentions to canonical nodes (graph-aware). | `src/nlp/entity_linker.py`. |
| **Correlation Matrix** | Multi-source evidence score table. | `src/pipelines/enrich/correlate_sources.py`. |
| **Embedding Similarity** | Vector-based semantic search. | API `/search`, optional module. |

---

## 🧱 Acronyms

| Acronym | Full Form | Description |
|:-----------|:-----------|:-------------|
| **KFM** | Kansas Frontier Matrix | Repository/system. |
| **MCP** | Master Coder Protocol | Documentation/provenance framework. |
| **STAC** | SpatioTemporal Asset Catalog | Geospatial metadata standard. |
| **ETL** | Extract–Transform–Load | Data pipeline. |
| **CI/CD** | Continuous Integration / Deployment | Automation for quality gates. |
| **RDF** | Resource Description Framework | Linked data model. |
| **COG** | Cloud-Optimized GeoTIFF | Raster format for web. |
| **NHD** | National Hydrography Dataset | Stream network dataset. |
| **WBD** | Watershed Boundary Dataset | Hydrologic boundaries. |
| **NOAA** | National Oceanic and Atmospheric Administration | Climate/hazards. |
| **USGS** | U.S. Geological Survey | Elevation/hydro/imagery. |
| **KSHS** | Kansas State Historical Society | Archives & documents. |

---

## 🔗 Cross-References

| Document | Description |
|:-----------|:-------------|
| `docs/architecture/architecture.md` | System architecture overview. |
| `docs/architecture/data-architecture.md` | Data flow & lineage. |
| `docs/architecture/knowledge-graph.md` | Graph schema & ontologies. |
| `docs/architecture/pipelines.md` | ETL & AI/ML pipelines. |
| `docs/standards/metadata-standards.md` | Metadata & schema compliance. |
| `docs/audit/repository_compliance.md` | Repository compliance dashboard. |

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
|:--------------|:----------------|
| **Documentation-first** | Definitions maintained before feature implementation. |
| **Reproducibility** | Terms bound to code, data paths, and CI validation. |
| **Open Standards** | STAC, DCAT, CIDOC CRM, OWL-Time, JSON Schema. |
| **Provenance** | Glossary versioned with metadata; linked to audit report. |
| **Auditability** | Validated via `docs-validate.yml` and Markdownlint. |

---

## 🕰️ Version History

| Version | Date | Summary |
|:---------|:------|:----------|
| **v1.2.0** | 2025-10-17 | Upgraded to MCP-DL v6.3 style; added **RMI/DCI**, security/supply-chain, AI/ML terms, cross-references. |
| **v1.1.0** | 2025-10-05 | Expanded ontology/geospatial/governance sections; GitHub rendering improvements. |
| **v1.0.0** | 2025-10-04 | Initial MCP-aligned glossary covering architecture, data, pipelines. |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*"Every Definition. Every Domain. Linked and Reproducible."*  
📍 `docs/glossary.md` — Canonical terminology reference for the Kansas Frontier Matrix documentation ecosystem.

</div>
```
````
