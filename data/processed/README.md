---
title: "data/processed — Final Data Products"
path: "data/processed/README.md"
version: "v1.0.0"
last_updated: "2026-01-02"
status: "active"
doc_kind: "Data Runbook"
license: "TBD"

# Protocol + contracts (KFM)
markdown_protocol_version: "1.0"
pipeline_contract_version: "v13"

# Governance (folder-level; per-dataset may override)
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "mixed"
classification: "mixed"
jurisdiction: "US"

doc_uuid: "urn:kfm:doc:data:processed:readme:v1.0.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# 📦 `data/processed/` — Final Data Products (KFM)

![stage](https://img.shields.io/badge/data%20stage-processed-success)
![metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-important)
![pipeline](https://img.shields.io/badge/pipeline-deterministic%20%26%20contract--first-informational)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-blueviolet)

> [!IMPORTANT]
> In KFM, “processed” means **final, stable outputs** produced by a **deterministic, idempotent, config-driven** pipeline — not scratch work. “Published” requires the metadata boundary artifacts (STAC/DCAT/PROV). [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧭 Quick navigation

- 📌 [What belongs here](#-what-belongs-here)
- 🔁 [Lifecycle: raw → work → processed](#-lifecycle-raw--work--processed)
- 🛰️ [Metadata boundary artifacts: STAC / DCAT / PROV](#️-metadata-boundary-artifacts-stac--dcat--prov)
- 🧠 [Evidence artifacts: ML + simulation outputs](#-evidence-artifacts-ml--simulation-outputs)
- 🧾 [Versioning & traceability](#-versioning--traceability)
- 🧪 [Validation & CI gates](#-validation--ci-gates)
- 🗺️ [Geospatial specifics (rasters, vectors, tiles)](#️-geospatial-specifics-rasters-vectors-tiles)
- 🔐 [Privacy + sensitive locations](#-privacy--sensitive-locations)
- ➕ [Add a new processed dataset](#-add-a-new-processed-dataset-checklist)
- 📚 [Project reference shelf](#-project-reference-shelf)

---

## 📌 What belongs here

This folder holds **final data products** that are ready to be:

- queried (DB tables / Parquet / CSV),
- mapped (COGs, tiles, GeoJSON/GeoPackage),
- indexed into the KFM catalog/graph,
- served through the API to the UI (with governance + redaction as needed). [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

✅ **Examples of “processed” artifacts**
- Final NDVI rasters, hillshades, classified landcover, drought risk surfaces (often GeoTIFF/tiles). [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L) [oai_citation:5‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- Cleaned & joined tables (e.g., field health index time series, prediction outputs). [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- “Ready-to-serve” GeoJSON exports (e.g., PostGIS → GeoJSON for web). [oai_citation:7‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

🚫 **Not for this folder**
- Raw downloads, unverified source dumps → put in `data/raw/…` [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- One-off scratch outputs, half-finished joins → put in `data/work/…` [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- “Mystery data” with no provenance or schema → won’t pass governance gates [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔁 Lifecycle: raw → work → processed

KFM expects data to move through stages (domain-scoped):

- `data/raw/<domain>/` → ingest as-is  
- `data/work/<domain>/` → intermediate/working products  
- `data/processed/<domain>/` → final outputs (this folder) [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

```mermaid
flowchart LR
  RAW[📥 data/raw/<domain>\n(source as-is)] --> WORK[🧪 data/work/<domain>\n(intermediate, scratch, joins)]
  WORK --> PROC[📦 data/processed/<domain>\n(final products)]
  PROC --> STAC[🛰️ data/stac/\n(Items + Collections)]
  PROC --> DCAT[🗂️ data/catalog/dcat/\n(datasets + distributions)]
  PROC --> PROV[🧬 data/prov/\n(lineage bundles)]
  STAC --> GRAPH[🕸️ Neo4j graph]
  DCAT --> GRAPH
  PROV --> GRAPH
  GRAPH --> API[🔌 API gateway]
  API --> UI[🗺️ Map UI / apps]
  UI --> STORY[📖 Story Nodes / Focus Mode]
```

This mirrors the canonical KFM flow: raw → ETL → STAC → DCAT/PROV → graph → API → UI → story content. [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🛰️ Metadata boundary artifacts: STAC / DCAT / PROV

A processed dataset is only treated as **“published”** once it has the boundary artifacts:

- **STAC**: `data/stac/collections/…` and `data/stac/items/…`  
- **DCAT**: `data/catalog/dcat/…` dataset entry  
- **PROV**: `data/prov/…` lineage bundle (inputs → transforms → outputs) [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> [!NOTE]
> The graph should generally **reference** catalog artifacts (STAC/DCAT/PROV) rather than duplicating bulky data, keeping the graph “light” and navigable. [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧠 Evidence artifacts: ML + simulation outputs

KFM explicitly treats AI/analytics outputs as **first-class evidence**. That means:

- AI/model outputs are **not special-cased** — they must be stored as regular processed artifacts.  
- They must be **cataloged** (STAC/DCAT) and **traced** (PROV).  
- They can enter the graph, but must be **flagged** and remain **explainable + auditable**.  
- The **API is the gatekeeper** for public delivery (redaction, aggregation, and access controls happen there). [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

This matches KFM’s broader orchestration approach where pipelines can include: NDVI processing → DB updates → model inference → completion notifications — typically orchestrated via workflow engines like Airflow (DAGs). [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧾 Versioning & traceability

**Dataset versioning expectations (KFM):**
- STAC Items should have **stable unique IDs** and explicit versions (e.g., `ndvi_2025-03-01_v1`).  
- DCAT entries should include `version`, `modified`, and distribution URIs.  
- PROV should reference the dataset version(s).  
- Reprocessing should preserve previous versions unless policy requires removal. [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Contract-first means** schema/profile changes are versioned and treated as first-class, with compatibility checks and migration plans for breaking changes. [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Helpful profile pointers (expected in repo):
- `docs/standards/KFM_STAC_PROFILE.md`
- `docs/standards/KFM_DCAT_PROFILE.md`
- `docs/standards/KFM_PROV_PROFILE.md` [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Validation & CI gates

KFM CI expects documentation + metadata + governance to be enforceable, including:

- YAML front-matter + required sections checks  
- Link/reference validation  
- JSON Schema validation for STAC/DCAT/PROV (and Story Node schema where applicable)  
- Graph integrity tests (Neo4j constraints, relationships)  
- API contract tests (OpenAPI/GraphQL lint + endpoint behavior)  
- Security & governance scans: secret scanning, PII scans, sensitive location checks, and classification consistency checks (prevent “downgrading” a dataset’s sensitivity through processing). [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗺️ Geospatial specifics (rasters, vectors, tiles)

### 🧱 Raster outputs (NDVI, hillshade, statewide surfaces)
- KFM processing often produces large rasters (e.g., statewide NDVI), stored as GeoTIFF or generated into tile pyramids for efficient front-end delivery. [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- Practical raster workflows commonly compute derived indices (like NDVI) and build overviews for performance (multi-resolution browsing). [oai_citation:24‡geoprocessing-with-python.pdf](file-service://file-NkXrdB4FwTruwhQ9Ggn53T)

Earth Engine workflows reinforce two critical habits:
1) attach **run metadata** (parameters/arguments) to the exported asset, and  
2) set appropriate **pyramiding policy** for multi-resolution behavior. [oai_citation:25‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk)

### 🧩 Vector outputs (boundaries, features, overlays)
Vector exports are often generated from PostGIS via spatial SQL and transformed into web-friendly formats like GeoJSON. Example patterns include exporting geometries as WGS84 (`4326`) GeoJSON and filtering using spatial predicates like `ST_WITHIN`. [oai_citation:26‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) [oai_citation:27‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### 🧠 Raster + vector together
Many built-environment datasets have both raster and vector components; being able to convert and reconcile them is a core skill for KFM-style mapping pipelines. [oai_citation:28‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk)

---

## 🧰 Storage outcomes & orchestration (what “processed” can mean)

After processing, KFM typically stores outputs in two primary ways:

1) **Relational/structured tables** (e.g., a `field_health_index` table with time series values like NDVI/rainfall/predicted yield, with indexes for performance).  
2) **Geospatial stores** for maps/imagery (GeoTIFF files, tile services, tile pyramids). [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

Orchestration and compute patterns commonly used:
- PostGIS spatial SQL for “heavy lifting” close to the data (buffers, intersections, containment).  
- Distributed processing (Spark/Dask) when volumes are huge.  
- Shell + command-line tooling as glue (e.g., `ogr2ogr` conversions).  
- Workflow engines (Airflow DAGs) for dependent pipelines, retries, and logging.  
- Incremental processing (process new increments; backfill only when needed). [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

> [!CAUTION]
> If you’re using shell automation as glue, treat command construction as a security boundary: unsanitized input + shell execution can create injection risk (avoid unsafe patterns like `shell=True` with untrusted input). [oai_citation:31‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

## 🔐 Privacy + sensitive locations

Two non-negotiables for KFM outputs:

1) **Sensitive locations & sovereignty**  
   If something must be protected (sacred sites, community-protected places), redact precise coordinates or aggregate appropriately, and label handling requirements (e.g., `care_label`). [oai_citation:32‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

2) **Processed outputs can still leak**  
   Results from data mining/ML can disclose sensitive information even without access to the original dataset — so privacy protections must apply to outputs too. [oai_citation:33‡Data Mining Concepts & applictions.pdf](file-service://file-CCSRY2RwLx1w6m1RMReuBG)

For sensitive outputs, consider “query auditing / inference control” approaches as part of the access layer (API/warehouse) when appropriate. [oai_citation:34‡Data Mining Concepts & applictions.pdf](file-service://file-CCSRY2RwLx1w6m1RMReuBG)

---

## 📁 Expected layout inside `data/processed/`

> [!TIP]
> Keep the top level tidy: **domain → dataset → version/run**. Prefer stable slugs.

```text
📁 data/
└── 📁 processed/
    ├── 📄 README.md   👈 you are here
    ├── 📁 <domain>/
    │   ├── 📁 <dataset_slug>/
    │   │   ├── 📁 <version_or_run_id>/
    │   │   │   ├── 📄 MANIFEST.json
    │   │   │   ├── 📄 checksums.sha256
    │   │   │   ├── 📄 dataset.schema.json
    │   │   │   ├── 🗺️ layer.geojson
    │   │   │   └── 🛰️ raster.tif
    │   │   └── 📄 README.md   (dataset card)
    │   └── 📁 _tmp/  (ignored / optional)
    └── 📁 _shared/   (only if truly cross-domain)
```

A companion “domain module” runbook is typically maintained under `docs/data/<domain>/README.md` (example domains include air-quality, soils, land-treaties). [oai_citation:35‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ➕ Add a new processed dataset (checklist)

> [!IMPORTANT]
> If you can’t explain the lineage, it’s not processed — it’s just a file.

### ✅ Processing checklist
- [ ] **Ingest** raw inputs into `data/raw/<domain>/…` (preserve original + record source info). [oai_citation:36‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] **Transform** into `data/work/<domain>/…` (joins, cleaning, intermediate artifacts). [oai_citation:37‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] **Finalize** into `data/processed/<domain>/…` (stable outputs + manifests). [oai_citation:38‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] **Generate boundary artifacts**:
  - [ ] STAC Item(s) + Collection in `data/stac/…` [oai_citation:39‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
  - [ ] DCAT dataset entry in `data/catalog/dcat/…` [oai_citation:40‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
  - [ ] PROV lineage bundle in `data/prov/…` [oai_citation:41‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] **Evidence labeling** (if ML/simulation-derived): flag as evidence artifact; ensure explainability hooks + API gating/redaction rules. [oai_citation:42‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] **Validate**: schemas, links, CI checks, and security/governance scans pass (no secret leaks, no PII surprises, no classification downgrade). [oai_citation:43‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] **Version**: stable IDs + explicit dataset versioning in STAC/DCAT/PROV. [oai_citation:44‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧩 Notes on large files & storage

This repository may use strategies like DVC or external storage for large raw/processed assets, keeping pointers/manifests in Git while storing heavy binaries elsewhere. [oai_citation:45‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## 📚 Project reference shelf

These project files collectively inform how we process, validate, govern, and serve data products:

### 🧠 KFM system + governance
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** (pipelines, storage, orchestration, ML integration) [oai_citation:46‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- **MARKDOWN_GUIDE_v13** (contracts, stages, metadata profiles, CI gates) [oai_citation:47‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:48‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Comprehensive Markdown Guide** (front-matter templates, CARE labels, Definition of Done practices) [oai_citation:49‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz) [oai_citation:50‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

### 🛰️ Remote sensing + GIS processing
- **Cloud-Based Remote Sensing with Google Earth Engine** (metadata habits, pyramiding policy, raster/vector interplay) [oai_citation:51‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk) [oai_citation:52‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk)
- **geoprocessing-with-python** (raster derivations like NDVI + overviews) [oai_citation:53‡geoprocessing-with-python.pdf](file-service://file-NkXrdB4FwTruwhQ9Ggn53T)
- **python-geospatial-analysis-cookbook** (PostGIS → GeoJSON patterns; raster tooling + cautions) [oai_citation:54‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) [oai_citation:55‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### 🔐 Privacy + output risk
- **Data Mining Concepts & Applications** (processed outputs can still disclose sensitive info; auditing considerations) [oai_citation:56‡Data Mining Concepts & applictions.pdf](file-service://file-CCSRY2RwLx1w6m1RMReuBG)

### ⚙️ Scale + performance (optional deep dives)
- **Scalable Data Management for Future Hardware** (AQP, bootstrapping/BLB, performance tradeoffs) [oai_citation:57‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)

---

## ✅ Definition of Done (for this README)

- [x] Front-matter present (template-inspired; placeholders allowed) [oai_citation:58‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- [x] Directory layout + lifecycle described (raw → work → processed) [oai_citation:59‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [x] Publication gate stated (STAC/DCAT/PROV) [oai_citation:60‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [x] Governance + sovereignty considerations included (CARE label + sensitive redaction patterns) [oai_citation:61‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz) [oai_citation:62‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Reviewed by a domain steward / data steward (recommended) [oai_citation:63‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)