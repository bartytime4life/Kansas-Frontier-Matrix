<div align="center">

# 📘 **Kansas Frontier Matrix — Glossary**  
`docs/glossary.md`

**Mission:** Provide a **canonical reference** for all technical, geospatial, historical, and procedural terms used across the **Kansas Frontier Matrix (KFM)** — ensuring cross-discipline clarity, transparency, and interoperability in documentation, datasets, pipelines, and AI systems.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue?logo=markdown)](../docs/)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../.github/workflows/docs-validate.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&logo=json)](../.github/workflows/stac-validate.yml)
[![Security](https://img.shields.io/badge/security-CodeQL%20%7C%20Trivy-red?logo=github)](../.github/workflows/)
[![SBOM & SLSA](https://img.shields.io/badge/Supply--Chain-SBOM%20%7C%20SLSA-green)](../.github/workflows/sbom.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Glossary"
version: "v1.4.0"
last_updated: "2025-10-18"
owners: ["@kfm-docs","@kfm-architecture"]
tags: ["glossary","standards","mcp","ontology","stac","graph","etl","security","ai","ethics","ci/cd"]
status: "Active"
license: "CC-BY 4.0"
ci_required_checks:
  - docs-validate
  - markdownlint
  - policy-check
semantic_alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - DCAT 2.0
  - CIDOC CRM
  - OWL-Time
  - GeoSPARQL
  - JSON Schema
  - ISO 8601
  - SLSA 3
  - FAIR Principles
---
```

---

## 📚 Overview

The **KFM Glossary** is a **cross-domain reference** for developers, researchers, historians, and data scientists.  
It aligns terminology across all MCP-compliant documentation and serves as a **knowledge interface** linking the project’s **data architecture**, **pipelines**, **ontologies**, **security posture**, and **CI/CD systems**.

**Organization**
- 🧱 Architecture & Infrastructure  
- 🌎 Geospatial & Environmental Data  
- 🧩 Metadata & Interoperability  
- 🧠 Knowledge Graph & Semantics  
- ⚙️ CI/CD & Governance  
- 🔐 Security & Supply Chain  
- 🧪 AI/ML & NLP  
- 🧭 Ethics & Cultural Safeguards  
- 🔗 Cross-Ontology & Provenance  

> All entries should be concise, source-linked (when relevant), and reflect current implementation.

---

## 🧩 Core Terminology

| Term | Definition | Context |
|:------|:-------------|:----------|
| **MCP / MCP-DL** | Documentation-first methodology & house style ensuring reproducibility, provenance, and transparency. | Required across all modules & READMEs. |
| **RMI / DCI** | Repository Maturity Index / Dynamic Compliance Index — metrics tracking MCP & CI coverage. | `docs/audit/repository_compliance.md`. |
| **STAC (SpatioTemporal Asset Catalog)** | Schema for describing spatiotemporal assets: Collections / Items / Assets. | `data/stac/` · STAC writer in pipelines. |
| **DCAT 2.0** | W3C vocabulary for dataset catalogs and distributions. | Metadata crosswalks in `docs/standards`. |
| **ETL** | Extract → Transform → (Enrich) → Load pipeline stages. | `src/etl/*`. |
| **Checksum (SHA-256)** | Cryptographic hash for integrity verification & provenance. | CI + `checksums.yml`. |
| **CIDOC CRM** | Cultural heritage ontology for people, places, events, documents. | Graph schema (`src/graph/`). |
| **OWL-Time** | Temporal ontology for instants/intervals & ordering. | Timeline normalization. |
| **JSON Schema** | Validation for JSON structures. | STAC & internal configs. |
| **GeoTIFF (COG)** | Cloud-Optimized GeoTIFF for HTTP-range streaming. | `data/processed/rasters/`. |
| **GeoJSON** | Vector data format for geospatial features. | Vector emitters in ETL. |
| **OCR** | Optical Character Recognition (scan → text). | Kansas Memory / newspapers. |
| **Pipeline** | Automated sequence of jobs governed by MCP. | `Makefile` + CI. |
| **Provenance / Lineage** | Source → transforms → outputs trail. | STAC `derived_from`, PROV-O, CI artifacts. |
| **Ontology** | Structured representation of conceptual relationships. | Knowledge Graph modeling. |
| **Knowledge Graph** | Semantic network linking entities (people, places, events, docs). | Neo4j + JSON-LD export. |
| **SPARQL / Cypher** | Query languages for RDF and Neo4j graphs. | API/analysis. |
| **PROV-O** | W3C Provenance Ontology. | Metadata enrichment & audit. |
| **Docs-as-Code** | Treat documentation like code (CI lint, links, policy). | `docs-validate.yml` + policy gates. |

---

## 🌎 Geospatial & Environmental Terms

| Term | Definition | Context |
|:------|:-------------|:----------|
| **DEM** | Digital Elevation Model raster. | USGS 3DEP / Kansas 1m DEM. |
| **LiDAR** | Laser-based elevation capture; point cloud → DEM/DSM. | Elevation derivation. |
| **Raster / Vector** | Pixel grid vs. geometric features. | DEMs vs. NHD flowlines. |
| **COG** | Cloud-Optimized GeoTIFF for tiling/overviews. | Web map performance. |
| **EPSG:4326 (WGS84)** | Latitude/Longitude CRS. | Standard output projection. |
| **CRS** | Coordinate Reference System. | Reprojection step in ETL. |
| **BBox** | Bounding box for spatial extent. | STAC fields. |
| **NHD / WBD** | Hydrography / Watershed boundaries datasets. | Hydrology overlays. |
| **PRISM / Daymet** | Gridded climate normals/daily weather data. | Climate integration. |

---

## 🧠 Knowledge Graph & Semantics

| Term | Definition | Context |
|:------|:-------------|:----------|
| **Entity / Relationship** | Node (Person/Place/Event/Document) & edge (e.g., `OCCURRED_AT`). | Neo4j schema. |
| **Graph Schema** | Labels, properties, relationships, constraints. | `src/graph/graph_schema.py`. |
| **Inference / Rules** | Derive implicit facts from explicit triples. | `src/graph/reasoner.py`. |
| **JSON-LD Export** | Semantic web export format. | `graph_export.py --format jsonld`. |
| **Similarity Edge** | `SIMILAR_TO` based on NLP embeddings. | Entity linking enrichment. |
| **PeriodO** | Gazetteer of historical time periods. | Temporal tagging in docs/UI. |

---

## 🧩 Metadata & Interoperability

| Term | Definition | Context |
|:------|:-------------|:----------|
| **FAIR** | Findable, Accessible, Interoperable, Reusable. | Data policy baseline. |
| **Open Standards** | Non-proprietary formats/schemas. | JSON, CSV, GeoTIFF, STAC, JSON Schema. |
| **STAC Extensions** | Optional fields (`proj:`, `processing:`, `scientific:`). | Catalog enrichment. |
| **DCAT Crosswalk** | Mapping STAC → DCAT terms. | Publishing/portals. |

---

## ⚙️ CI/CD & Governance

| Term | Definition | Context |
|:------|:-------------|:----------|
| **GitHub Actions** | Build/Test/Deploy workflows. | `.github/workflows/`. |
| **Golden Tests** | Expected outputs for regression. | ETL test data. |
| **Artifact** | Build/validation output (logs, docs, SBOM). | CI retention. |
| **OIDC** | OpenID Connect (keyless CI auth). | Deploy & attestation. |
| **Conventional Commits** | Semantic commit format. | Releases/changelogs. |
| **Policy-as-Code** | OPA/Conftest enforcement in CI. | `policy-check.yml`. |

---

## 🔐 Security & Supply Chain

| Term | Definition | Context |
|:------|:-------------|:----------|
| **CodeQL** | Static application security testing. | `codeql.yml`. |
| **Trivy** | Dependency/container CVE scanning; SBOM scan. | `trivy.yml`. |
| **SBOM** | Software Bill of Materials (Syft/Spdx). | `sbom.yml`. |
| **SLSA** | Supply-chain Levels for Software Artifacts. | `slsa.yml` (attestations). |
| **Gitleaks** | Secret scanning with SARIF. | `gitleaks.yml`. |
| **Dependabot/Renovate** | Automated dependency updates. | Release hygiene. |

---

## 🧪 AI/ML & NLP

| Term | Definition | Context |
|:------|:-------------|:----------|
| **NER** | Named Entity Recognition (people/places/events/dates). | `src/ai/ner_model.py`. |
| **Summarization** | Abstractive/extractive text condensation. | `src/ai/summarizer.py`. |
| **Entity Linking** | Map mentions → canonical graph nodes. | `src/ai/entity_linker.py`. |
| **Correlation Matrix** | Multi-source evidence scoring table. | Enrichment pipeline. |
| **Embedding Similarity** | Vector search/semantic ranking. | API `/search`. |
| **Model Card** | Human-readable model metadata (purpose/data/metrics/ethics). | `docs/templates/model_card.md`. |
| **Bias/Quality Gates** | Min metrics & fairness checks required in CI. | `ai-model.yml`. |

---

## 🧭 Ethics & Cultural Safeguards

| Term | Definition | Context |
|:------|:-------------|:----------|
| **Data Ethics Tag** | STAC `properties.data_ethics` flag (e.g., `restricted-derivatives`). | Sensitive/Indigenous datasets. |
| **Public Artifact Scrub** | Exclude restricted layers from public Pages builds. | CI hardening policy. |
| **Co-stewardship** | Collaborative handling of cultural data. | Governance guidance. |

---

## 🔗 Cross-Ontology Mapping

| KFM Concept | CIDOC CRM Entity | DCAT Property | STAC Field | Notes |
|:------------|:------------------|:-------------|:-----------|:------|
| Person      | E21_Person        | dcat:contactPoint | —        | Historical & modern figures. |
| Place       | E53_Place         | dcat:spatial | geometry   | Linked to CRS/EPSG. |
| Event       | E5_Event          | dcat:temporal | datetime  | Bound to OWL-Time intervals. |
| Document    | E31_Document      | dcat:dataset | assets     | OCR + metadata integration. |
| Dataset     | E73_Information_Object | dcat:Dataset | collection | Dataset-level alignment. |

---

## 🤖 Machine-Readable Export

The glossary is automatically exported to **JSON-LD** and **YAML** for integration with:
- KFM Docs Search API (`/api/v1/terms`)
- AI Assistant (MapLibre frontend; Focus Mode)
- STAC Validator semantic enrichment

**Command**
```bash
make export-glossary
```

**Outputs**
- `docs/glossary.jsonld`
- `docs/glossary.yaml`

---

## 🖊 Reviewer Sign-off

| Reviewer | Role | Date | Signature |
|:---------|:-----|:-----|:----------|
| @kfm-docs | Documentation Maintainer | 2025-10-18 | 🔏 SHA256:45e8…12a |
| @kfm-architecture | System Architect | 2025-10-18 | 🔏 SHA256:e4c9…91a |

---

## 🧭 Planned Extensions (v6.4)

| Feature | Description | ETA |
|:--------|:------------|:----|
| **Glossary AI Validation** | Detect inconsistent term usage across READMEs. | Q1 2026 |
| **Ontology Graph Export** | Convert glossary → RDF triples → graph ingestion. | Q2 2026 |
| **Glossary API Endpoint** | REST + GraphQL endpoint for dynamic term access. | Q2 2026 |

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
|:--------------|:----------------|
| **Documentation-first** | Definitions maintained before feature implementation. |
| **Reproducibility** | Terms bound to data paths, workflows, and CI validation. |
| **Open Standards** | STAC, DCAT, CIDOC CRM, OWL-Time, GeoSPARQL, JSON Schema. |
| **Provenance** | Versioned with metadata; linked to audit reports. |
| **Auditability** | Validated via `docs-validate.yml` and Markdownlint. |

---

## 🕰️ Version History

| Version | Date | Summary |
|:--------|:-----|:--------|
| **v1.4.0** | 2025-10-18 | Added ethics section, supply-chain badges, Docs-Validate/Policy gates, FAIR & GeoSPARQL alignment, reviewer sign-off. |
| **v1.3.0** | 2025-10-17 | Semantic tags, ontology mapping, machine-readable export, provenance metadata. |
| **v1.2.0** | 2025-10-17 | Security/supply-chain & AI/ML terms; cross-references. |
| **v1.1.0** | 2025-10-05 | Expanded ontology/geospatial/governance sections; GFM improvements. |
| **v1.0.0** | 2025-10-04 | Initial glossary of architecture, data, pipelines. |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*"Every Definition. Every Domain. Linked and Reproducible."*  
📍 `docs/glossary.md` — Canonical terminology reference for the Kansas Frontier Matrix documentation ecosystem.

</div>