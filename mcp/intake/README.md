# 📥 MCP Intake — Data & Evidence Ingestion Runbook

![MCP](https://img.shields.io/badge/MCP-Intake%20SOP-blue)
![Provenance](https://img.shields.io/badge/Provenance-First-success)
![Catalogs](https://img.shields.io/badge/Metadata-STAC%20%7C%20DCAT%20%7C%20PROV-informational)
![Pipelines](https://img.shields.io/badge/ETL-Deterministic%20%26%20Idempotent-orange)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-purple)

> [!IMPORTANT]
> **Nothing enters KFM “as a usable layer/evidence artifact” until it’s** (1) produced by a repeatable pipeline, and (2) published with **STAC + DCAT + PROV** boundary artifacts, and (3) passes governance + CI gates.

---

## 🧭 What this SOP is

This README is the **MCP (Master Coder Protocol)** “intake” runbook for Kansas Frontier Matrix (KFM).

It defines the **canonical** way to bring anything into the platform:
- 🗺️ geospatial datasets (vector/raster/tiles)
- 📄 documents & corpora (OCR, text, reports)
- 🧪 analysis outputs & simulations
- 🤖 AI-generated “evidence artifacts” (summaries, extracted entities, derived layers)

The core promise: **evidence-first publishing** — every user-facing layer, chart, and citation is traceable back to **raw inputs + deterministic transforms + provenance**.

---

## 🧱 Non‑negotiable invariants

> [!TIP]
> Print these. Treat them like build rules. ✅

1) **Pipeline ordering is absolute**  
   `ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode`

2) **Raw is immutable**  
   Raw snapshots are append-only. Never “fix” raw by editing it in-place.

3) **No ad-hoc manual manipulation**  
   If a processed result is wrong: update code/config, re-run, re-publish.

4) **Catalog triplet required**  
   Every dataset/evidence artifact must have:
   - 🛰️ STAC Collection + Items (assets & spatiotemporal metadata)
   - 🗂️ DCAT dataset entry (discovery + distributions)
   - 🧾 PROV bundle (lineage: inputs → work → outputs; agents; parameters)

5) **Graph stores relationships, not bulky payloads**  
   Neo4j nodes should **reference** catalog IDs (e.g., STAC Item IDs / persistent IDs), not embed full data.

6) **Governance & sovereignty propagate forward**  
   Outputs can’t be less restricted than inputs; sensitive classifications carry through derivatives.

---

## 📌 Table of contents

- [🧰 Intake deliverables](#-intake-deliverables)
- [🗂️ Canonical repo layout](#️-canonical-repo-layout)
- [🔁 Intake workflow](#-intake-workflow)
- [✅ Definition of done](#-definition-of-done)
- [🧩 Templates](#-templates)
- [🗺️ Geospatial-specific guidance](#️-geospatial-specific-guidance)
- [📡 Streaming / watcher intake](#-streaming--watcher-intake)
- [🤖 AI & evidence artifacts](#-ai--evidence-artifacts)
- [🧪 Validation & CI gates](#-validation--ci-gates)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 Project file index](#-project-file-index)

---

## 🧰 Intake deliverables

| Deliverable ✅ | What it is | Why it exists |
|---|---|---|
| **Raw snapshot** | Immutable input files | Reproducibility & auditing |
| **Source receipt** | URL/license/citation/checksums/access date | Provenance + legal clarity |
| **Pipeline** | Config-driven deterministic transform | Repeatable builds |
| **Processed assets** | Publishable outputs (COG, GeoParquet, tiles, etc.) | UI/API performance |
| **STAC** | Collection + Item(s) | Spatial/temporal indexing + asset pointers |
| **DCAT** | Dataset record (JSON-LD) | Discovery + external harvesting |
| **PROV** | Activity bundle | Full lineage, agents, parameters |
| **Store ingest** (as needed) | PostGIS + Neo4j + search/vector index | Query speed + relationships |

---

## 🗂️ Canonical repo layout

> [!NOTE]
> Folder names may vary slightly between deployments; **the intent does not**. Keep the “raw/work/processed + catalogs” staging discipline.

```text
📦 repo-root/
├─ 📁 data/
│  ├─ 📁 raw/                  # ✅ immutable snapshots (append-only)
│  ├─ 📁 work/                 # 🧪 intermediate/temporary (rebuildable)
│  ├─ 📁 processed/            # 🚀 publishable outputs (stable paths)
│  ├─ 📁 stac/
│  │  ├─ 📁 collections/       # 🛰️ STAC Collections
│  │  └─ 📁 items/             # 🛰️ STAC Items
│  ├─ 📁 catalog/
│  │  └─ 📁 dcat/              # 🗂️ DCAT datasets (JSON-LD)
│  ├─ 📁 prov/                 # 🧾 PROV bundles (or data/provenance/)
│  └─ 📁 sources/              # 🧾 source receipts (per-source JSON + indexes)
│
├─ 📁 pipelines/               # 🧰 ETL + normalization code/configs
│  └─ 📁 <domain>/
│     └─ 📁 <dataset_slug>/
│
├─ 📁 docs/
│  └─ 📁 data/
│     └─ 📁 <domain>/
│        └─ 📁 <dataset_slug>/
│           └─ 📄 README.md    # domain/dataset runbook
│
└─ 📁 mcp/
   └─ 📁 intake/
      └─ 📄 README.md          # 👈 you are here
```

---

## 🔁 Intake workflow

### 0) Pick a dataset identity 🏷️
- **domain:** e.g. `historical`, `air-quality`, `soils`, `hydrology`
- **dataset_slug:** kebab-case, stable: `kansas-county-boundaries`
- **dataset_version:** `vYYYY-MM-DD` or semantic version (keep it consistent)

> [!CAUTION]
> If you can’t clearly state **license + attribution**, you’re not ready to intake.

---

### 1) Acquire & snapshot raw inputs 📦
1. Create the dataset folder:
   - `data/raw/<domain>/<dataset_slug>/<dataset_version>/`
2. Download/copy raw inputs into that folder **unchanged**
3. Generate checksums (sha256 recommended)
4. Record retrieval context (URL, date, auth method if applicable)

Example (bash):
```bash
# Example only — adapt to your environment
mkdir -p data/raw/<domain>/<dataset_slug>/<dataset_version>
sha256sum data/raw/<domain>/<dataset_slug>/<dataset_version>/* > data/raw/<domain>/<dataset_slug>/<dataset_version>/SHA256SUMS.txt
```

---

### 2) Create a source receipt 🧾
Create one (or both) of:
- `data/sources/<dataset_slug>.source.json`
- `data/sources/sources.json` (index of sources)

Minimal receipt fields (guideline):
- `id`, `title`, `source_url`
- `retrieved_at` (ISO-8601)
- `license`, `attribution`, `citation`
- `checksums` (sha256 per file or per archive)
- `spatial_extent`, `temporal_extent` (if known)
- `sensitivity` / `classification` (governance)

> [!TIP]
> Treat the source receipt like a “data bill of materials”.

---

### 3) Build the pipeline (deterministic + idempotent) 🧰
Create:
- `pipelines/<domain>/<dataset_slug>/` (code + configs)

Rules:
- **Deterministic:** same inputs ⇒ same outputs  
- **Idempotent:** re-run safely without duplicating/dirtying outputs
- **Logged:** capture run IDs, parameters, and input/output hashes
- **Stage-aware:** write intermediates to `data/work/`, finals to `data/processed/`

---

### 4) Produce publishable outputs 🚀
Write final outputs to:
- `data/processed/<domain>/<dataset_slug>/<dataset_version>/`

Guidelines:
- Prefer open + stable formats:
  - vector: GeoParquet / GeoPackage (depending on needs), GeoJSON for small
  - raster: COG (Cloud-Optimized GeoTIFF)
  - tiles: MBTiles / vector tiles (as needed)
- If you reproject, simplify, or normalize attributes: record it in PROV.

---

### 5) Emit boundary artifacts: STAC + DCAT + PROV 🛰️🗂️🧾
Create:
- `data/stac/collections/<domain>__<dataset_slug>.collection.json`
- `data/stac/items/<domain>__<dataset_slug>__<dataset_version>__*.item.json`
- `data/catalog/dcat/<domain>__<dataset_slug>.dataset.jsonld`
- `data/prov/<domain>__<dataset_slug>__<dataset_version>.prov.jsonld` (or `data/provenance/`)

Cross-link expectations:
- STAC Item **must** point to processed assets (`data/processed/**` or stable storage URL)
- DCAT entry links to STAC and/or direct distributions
- PROV links the chain: raw → work → processed, and identifies run/config/commit

> [!IMPORTANT]
> These “boundary artifacts” are the contract to downstream layers (graph → API → UI → story → focus).

---

### 6) Ingest into stores (as needed) 🕸️🗄️
Depending on dataset type:
- 🗄️ **PostGIS**: load geometries/rasters for spatial queries & serving
- 🕸️ **Neo4j**: ingest catalog-derived nodes + relationships (keep it reference-based)
- 🔎 **Search index**: full-text indexing for documents, story nodes, metadata
- 🧠 **Vector index** (optional): embeddings for retrieval (still provenance-linked)

---

### 7) Document the domain module 📚
Create / update:
- `docs/data/<domain>/<dataset_slug>/README.md`

Include:
- purpose & use cases
- exact source URLs + licensing
- pipeline steps (how to rebuild)
- validation steps
- known limitations / uncertainty

---

### 8) PR + CI gates ✅
Open a PR that includes:
- raw snapshot + checksums
- source receipt
- pipeline code/config
- processed outputs
- STAC/DCAT/PROV artifacts
- docs updates

CI should fail if:
- metadata missing
- provenance incomplete
- broken links
- license absent
- governance rules violated
- tests failing

---

## ✅ Definition of done

Use this checklist before requesting review:

- [ ] Dataset slug + version chosen and documented
- [ ] Raw snapshot stored under `data/raw/**` (immutable)
- [ ] Checksums generated and committed
- [ ] Source receipt created (license + attribution + citation included)
- [ ] Pipeline added under `pipelines/**` (deterministic + idempotent)
- [ ] Processed outputs stored under `data/processed/**`
- [ ] STAC Collection + Items created and validated
- [ ] DCAT dataset entry created and validated
- [ ] PROV bundle created (raw → work → processed; agents; params; run/config/commit)
- [ ] Governance tags applied (classification propagates)
- [ ] (If needed) PostGIS/Neo4j/search ingest steps documented
- [ ] Domain dataset README updated under `docs/data/**`
- [ ] CI green ✅

---

## 🧩 Templates

> [!NOTE]
> These are **starter shapes**. Align with your project profiles (e.g., `docs/standards/KFM_*_PROFILE.md`) once present.

<details>
<summary><strong>🧾 Source receipt template (JSON)</strong></summary>

```json
{
  "id": "kansas-county-boundaries",
  "title": "Kansas County Boundaries",
  "source_url": "https://example.org/datasets/kansas_counties.zip",
  "retrieved_at": "2026-01-26T00:00:00Z",
  "license": "CC-BY-4.0",
  "attribution": "Example Agency (2024)",
  "citation": "Example Agency. Kansas County Boundaries (2024).",
  "checksums": {
    "kansas_counties.zip": {
      "sha256": "REPLACE_ME"
    }
  },
  "spatial_extent": {
    "bbox": [-102.05, 36.99, -94.59, 40.00],
    "crs": "EPSG:4326"
  },
  "temporal_extent": {
    "start": "2024-01-01",
    "end": "2024-12-31"
  },
  "governance": {
    "classification": "public",
    "faircare": {
      "collective_benefit": "TBD",
      "authority_to_control": "TBD",
      "responsibility": "TBD",
      "ethics": "TBD"
    }
  }
}
```

</details>

<details>
<summary><strong>🛰️ STAC Item skeleton (JSON)</strong></summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "historical__kansas-county-boundaries__v2026-01-26",
  "collection": "historical__kansas-county-boundaries",
  "geometry": null,
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "properties": {
    "datetime": "2026-01-26T00:00:00Z",
    "license": "CC-BY-4.0"
  },
  "assets": {
    "data": {
      "href": "data/processed/historical/kansas-county-boundaries/v2026-01-26/kansas_counties.parquet",
      "type": "application/x-parquet",
      "roles": ["data"]
    },
    "provenance": {
      "href": "data/prov/historical__kansas-county-boundaries__v2026-01-26.prov.jsonld",
      "type": "application/ld+json",
      "roles": ["metadata"]
    }
  }
}
```

</details>

<details>
<summary><strong>🗂️ DCAT Dataset skeleton (JSON-LD)</strong></summary>

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@type": "dcat:Dataset",
  "dct:identifier": "historical__kansas-county-boundaries",
  "dct:title": "Kansas County Boundaries",
  "dct:description": "County boundary polygons for Kansas.",
  "dct:license": "CC-BY-4.0",
  "dcat:keyword": ["kansas", "boundaries", "counties"],
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dcat:accessURL": "data/stac/items/historical__kansas-county-boundaries__v2026-01-26.item.json",
      "dct:format": "STAC Item JSON"
    }
  ],
  "prov:wasGeneratedBy": "data/prov/historical__kansas-county-boundaries__v2026-01-26.prov.jsonld"
}
```

</details>

<details>
<summary><strong>🧾 PROV bundle skeleton (JSON-LD)</strong></summary>

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "prov:bundle/historical__kansas-county-boundaries__v2026-01-26",
  "@type": "prov:Bundle",
  "prov:entity": [
    {
      "@id": "prov:entity/raw_zip",
      "prov:atLocation": "data/raw/historical/kansas-county-boundaries/v2026-01-26/kansas_counties.zip",
      "prov:label": "Raw source archive"
    },
    {
      "@id": "prov:entity/processed_parquet",
      "prov:atLocation": "data/processed/historical/kansas-county-boundaries/v2026-01-26/kansas_counties.parquet",
      "prov:label": "Processed GeoParquet output"
    }
  ],
  "prov:activity": [
    {
      "@id": "prov:activity/etl_run",
      "@type": "prov:Activity",
      "prov:startedAtTime": {"@value": "2026-01-26T00:00:00Z", "@type": "xsd:dateTime"},
      "prov:used": ["prov:entity/raw_zip"],
      "prov:generated": ["prov:entity/processed_parquet"],
      "prov:label": "ETL + normalization",
      "prov:wasAssociatedWith": "prov:agent/pipeline"
    }
  ],
  "prov:agent": [
    {
      "@id": "prov:agent/pipeline",
      "@type": "prov:SoftwareAgent",
      "prov:label": "pipelines/historical/kansas-county-boundaries (commit: REPLACE_ME)"
    }
  ]
}
```

</details>

---

## 🗺️ Geospatial-specific guidance

### CRS & projection sanity ✅
- Store the original CRS (raw), and clearly document any reprojection.
- Use consistent CRS conventions (many pipelines standardize on EPSG:4326 for metadata and web mapping).
- Validate:
  - geometry validity (self-intersections, nulls)
  - bbox correctness
  - “looks right” quick map preview (spot-check)

### Scanned maps / georeferencing 🧭
If ingesting historical maps:
- Record control points and method in the PROV bundle
- Track georeferencing error metrics (e.g., RMS error) in metadata
- Preserve raw scans untouched; derived georeferenced raster belongs in `data/processed/**`

---

## 📡 Streaming / watcher intake

For data feeds that change over time:
- Prefer conditional HTTP requests (ETag / If-Modified-Since)
- Snapshot new versions as new dataset versions, don’t overwrite
- Emit new STAC Item(s) per release/version and link revisions via DCAT + PROV

> [!TIP]
> Treat each watcher run as a PROV activity; treat each output as a versioned entity.

---

## 🤖 AI & evidence artifacts

KFM treats AI/analysis outputs as **first-class datasets** (not “special cases”):
- stored in `data/processed/**`
- cataloged in STAC/DCAT (with “derived / AI-generated” flags)
- traced in PROV with:
  - inputs (datasets/docs)
  - model/algorithm identity
  - parameters
  - confidence/uncertainty
- integrated with graph **cautiously** (explicit provenance pointers)
- exposed only via governed APIs (redaction/classification enforced)

---

## 🧪 Validation & CI gates

Minimum gates for intake PRs:
- ✅ schema validation for STAC/DCAT/PROV (project profiles)
- ✅ link integrity checks (assets & metadata references)
- ✅ license presence checks
- ✅ provenance completeness checks
- ✅ security scans (secrets, sensitive data leaks)
- ✅ pipeline tests (unit/integration) where applicable

> [!IMPORTANT]
> CI should reject contributions that violate pipeline ordering, provenance requirements, or governance rules.

---

## 🧯 Troubleshooting

**“CI says PROV missing / incomplete”**
- Confirm you generated a PROV bundle for the dataset version
- Ensure the PROV entity chain references raw → processed
- Include pipeline run identifiers (run ID / config / commit hash)

**“STAC asset links are broken”**
- STAC Items must point to stable `data/processed/**` paths (or stable storage URLs)
- Avoid absolute local paths

**“Output is wrong but raw is correct”**
- Fix pipeline/config and re-run
- Publish as a new dataset version; link via `prov:wasRevisionOf` in DCAT/PROV

**“Sensitive data might be exposed”**
- Stop intake, classify inputs, and apply redaction/generalization
- Ensure outputs are not less restricted than inputs

---

## 📚 Project file index

These project files inform this SOP (core design + architecture + AI + UI + tooling + learning library):

### 🧭 Core KFM design & roadmap
- Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf
- Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf

### 🤖 AI & governance
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf
- KFM AI Infrastructure – Ollama Integration Overview.pdf

### 🧰 Expanded guide & research process
- 📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf
- AI Concepts & more.pdf
- Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf
- Data Mining Concepts & applictions.pdf
- Scientific Method _ Research _ Master Coder Protocol Documentation.pdf

### 🗺️ Mapping, GIS, and web stack references
- Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf
- Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf
- Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf
- Various programming langurages & resources 1.pdf

---

## 🧩 Suggested next additions (nice-to-have)

- 📁 `mcp/intake/templates/` (source receipt + STAC/DCAT/PROV templates)
- 📁 `mcp/intake/checklists/` (PR checklist, governance checklist)
- 📁 `mcp/intake/examples/` (one worked example per domain)
- ✅ A CI rule: “no STAC/DCAT/PROV → no merge” (hard gate)
- 🔏 Optional: artifact signing / attestations for releases (cosign)

---