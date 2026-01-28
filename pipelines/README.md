# 🧪 pipelines/ — ETL & Simulation Pipelines

![Provenance First](https://img.shields.io/badge/provenance-first-blue)
![Deterministic](https://img.shields.io/badge/pipelines-deterministic-brightgreen)
![No Manual Steps](https://img.shields.io/badge/automation-no%20manual%20steps-brightgreen)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT-informational)
![Lineage](https://img.shields.io/badge/lineage-W3C%20PROV-informational)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-purple)

> According to a document from *(date not specified in the PDF export)*, KFM’s canonical pipeline order is **Raw → Processed → Catalog/Prov → Database → API → UI** — shortcuts (e.g., injecting directly into UI or bypassing metadata) are considered flawed unless proven otherwise.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

This folder is where KFM’s “data processing magic” lives: **ETL scripts, ingestion notebooks, and simulation/analysis code** that run offline/batch to populate and update KFM datasets.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

KFM treats this directory as an **active data refinery**: raw evidence comes in, code transforms it, and verified knowledge comes out — in a way that supports **reproducibility** (rebuilding datasets from the same inputs).  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 Quick Navigation

- [Canonical Contract](#-canonical-contract-non-negotiable)
- [Repo & Data Layout](#-repo--data-layout)
- [Pipeline Types](#-pipeline-types)
- [Hard Requirements](#-hard-requirements)
- [Plugin-Based Pipelines](#-plugin-based-pipelines)
- [Metadata & Provenance](#-metadata--provenance)
- [Determinism & Reproducibility](#-determinism--reproducibility)
- [Quality Checks](#-quality-checks)
- [Performance & Scaling](#-performance--scaling)
- [Special Patterns: Remote Sensing & Time](#-special-patterns-remote-sensing--time)
- [Governance & Sensitive Data](#-governance--sensitive-data)
- [Contribution Checklist](#-contribution-checklist)
- [References](#-references)

---

## 🔁 Canonical Contract (Non-Negotiable)

### ✅ The pipeline flow

```mermaid
flowchart LR
  A[data/raw/ 🧾] -->|ETL / Sim / Analysis| B[data/processed/ 🧼]
  B --> C[data/catalog/ 🗂️ (STAC/DCAT)]
  B --> D[data/provenance/ 🧬 (PROV)]
  C --> E[(Database 🗄️)]
  D --> E
  E --> F[API 🔌]
  F --> G[UI 🖥️]
```

- Raw inputs are preserved as evidence and **not edited by pipelines**.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Processed outputs are standardized, ready-for-use datasets served by the system.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Metadata + lineage are not optional: each dataset must ship with catalog and provenance artifacts.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> [!WARNING]
> Pipelines that don’t emit **Catalog (STAC/DCAT)** and **Provenance (PROV)** are likely to be rejected by CI, because “no data enters KFM without documentation.”  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🗃️ Repo & Data Layout

KFM stores project data under `data/` as a “single source of truth” (with pragmatic handling for very large assets).  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 📁 Expected directories (mental model)

```text
Kansas-Frontier-Matrix/
├─ 🧪 pipelines/
│  ├─ README.md  👈 you are here
│  ├─ plugins/   🧩 (optional, recommended)
│  ├─ simulations/ 🌪️ (optional)
│  └─ shared/    🧰 (optional)
└─ 🗺️ data/
   ├─ raw/         🧾 immutable evidence
   ├─ processed/   🧼 curated outputs
   ├─ catalog/     🗂️ STAC/DCAT metadata
   └─ provenance/  🧬 PROV lineage logs
```

### 🧾 `data/raw/` is sacred

- It holds **exactly what was downloaded/collected** and is treated as read-only evidence.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🧼 `data/processed/` is what the platform serves

- Outputs are the cleaned/standardized datasets ready for use by the system.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧰 Pipeline Types

| Type | What it does | Typical outputs |
|---|---|---|
| 🧲 Ingestion (ETL) | Pulls/parses a source dataset and standardizes it | Processed dataset + STAC/DCAT + PROV |
| 🧽 Normalization | CRS conversions, unit normalization, schema alignment | Updated processed dataset + updated PROV |
| 🧠 Enrichment | Joins, derived fields, aggregates, computed indices | New derived dataset + metadata updates |
| 🌪️ Simulation | Generates “what-if” layers (climate scenarios, projections) | Sim outputs + provenance of assumptions |
| ♻️ Refresh | Adds new time slices / new releases of the same source | Version bump + lineage updates |

Blueprint examples include scripts/notebooks like:
- `pipelines/import_census.py`
- `pipelines/landsat_imagery.ipynb`
- `pipelines/simulations/climate_scenario.py`  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧱 Hard Requirements

### 1) Deterministic, reproducible execution
Every official pipeline must run start-to-finish automatically (no interactive prompts), producing the same outputs given the same inputs/config.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 2) Idempotent behavior (don’t duplicate outputs)
Re-running a pipeline without changes should not create duplicate copies; checksums/version checks are recommended.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3) Standard ETL shape (Raw → Process → Write → Describe)
A typical pipeline:
1. Reads from `data/raw/`
2. Cleans/transforms (incl. CRS conversion if needed)
3. Writes to `data/processed/`
4. Updates `data/catalog/` (STAC/DCAT) and `data/provenance/` (PROV)  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 4) Metadata + provenance are first-class outputs
A pipeline that produces data must also produce:
- STAC Item/Collection (as appropriate)
- DCAT dataset record
- PROV lineage log (script version, inputs, run timestamp, outputs, etc.)  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧩 Plugin-Based Pipelines

KFM’s blueprint proposes a **plugin-based ETL framework**: each integration becomes a self-contained module discovered by a lightweight orchestrator.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 📦 Recommended plugin layout

```text
pipelines/plugins/
└─ 🧩 usgs_water/
   ├─ pipeline.yml
   ├─ src/
   │  ├─ __init__.py
   │  └─ pipeline.py   # ingest / transform / load
   ├─ tests/
   └─ README.md
```

### 🗒️ `pipeline.yml` (manifest) — suggested schema

```yaml
name: usgs_water
version: 0.1.0
kind: ingestion            # ingestion | enrichment | simulation | refresh
description: "USGS water observations standardized for KFM"

inputs:
  - path: data/raw/usgs_water/
    required: true

outputs:
  processed:
    - path: data/processed/hydrology/usgs_water.parquet
  catalog:
    - path: data/catalog/usgs_water.stac.json
    - path: data/catalog/usgs_water.dcat.json
  provenance:
    - path: data/provenance/usgs_water.prov.json

reproducibility:
  deterministic: true
  seed: 42
  timezone: UTC

governance:
  accessLevel: Public       # Public | Restricted | Withdrawn
  ownerGroup: null          # e.g., "TribeABC" when restricted
  license: "CC-BY-4.0"
```

> [!NOTE]
> Governance fields matter because KFM uses policy enforcement (fail-closed) and CARE-aligned access control patterns (e.g., owner group restrictions).  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🗂️ Metadata & Provenance

### 🗂️ Catalog outputs: STAC + DCAT (minimum viable)

Pipelines should produce catalog metadata:
- **STAC**: Item for single dataset; Collection + Items for multi-date/multi-part datasets
- **DCAT**: dataset record for broader data portals/catalogs  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🧬 Provenance outputs: W3C PROV (or a compatible structured log)

The provenance log should answer: **“How was this data produced?”** and typically records:
- **Entities**: input raw files + output dataset
- **Activity**: the process (pipeline name), timestamps, environment info
- **Agents**: pipeline script/software version + human trigger (if relevant)  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

#### 🔎 Example `*.prov.json` (minimal)

```json
{
  "dataset_id": "usgs_water",
  "prov": {
    "entity": {
      "raw:zip": {"path": "data/raw/usgs_water/source.zip", "sha256": "…"},
      "out:parquet": {"path": "data/processed/hydrology/usgs_water.parquet", "sha256": "…"}
    },
    "activity": {
      "run:2026-01-28T00:00:00Z": {
        "type": "pipelines/plugins/usgs_water",
        "git_commit": "abc123",
        "started_at": "2026-01-28T00:00:00Z",
        "ended_at": "2026-01-28T00:01:12Z",
        "params": {"normalize_units": true}
      }
    },
    "agent": {
      "software:pipeline": {"name": "usgs_water", "version": "0.1.0"},
      "person:trigger": {"name": "CI"}
    }
  }
}
```

---

## 🎯 Determinism & Reproducibility

> [!IMPORTANT]
> Determinism is not a vibe — it’s a contract: reruns on the same inputs/config should yield byte-identical outputs whenever feasible.  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ✅ Best practices (recommended)

- **Pin environments** (lockfiles, containers)  
- **Fix randomness** (explicit seeds; record them in provenance)  
- **Stable ordering** (sort keys before writing output)  
- **Stable timestamps** (avoid embedding “now” in data rows; keep it in PROV)  
- **No manual steps** (no prompts, no clicking, no “open this UI and export…”)  [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧪 Quality Checks

Pipelines may validate:
- required columns / schema expectations
- plausible value ranges
- geometry validity
- CRS correctness (e.g., “standard projection like EPSG:4326 or Kansas-specific”)  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

They can also emit summary stats/logs (record counts, min/max, etc.) to help maintainers verify successful imports.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ⚡ Performance & Scaling

### 🧱 Git-friendly dataset strategy
KFM acknowledges that very large data is challenging to store in Git and may require:
- storing references/hashes for huge assets (e.g., large rasters)
- slicing datasets into diff-friendly chunks (line-delimited GeoJSON/CSV)  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 📈 Plan for growth (pipelines are ingestion engines)
As the system grows, track ingestion rate and burstiness; storage sizing should account for growth variability.  [oai_citation:27‡Database Performance at Scale.pdf](sediment://file_000000002cf871f5905f30dcc65cc90b)

---

## 🌍 Special Patterns: Remote Sensing & Time

### 🛰️ Remote Sensing pipelines (Google Earth Engine)

Earth Engine time-series workflows frequently rely on **filter → map → reduce**:
- filter ImageCollections to criteria
- map a function across images
- reduce/summarize results  [oai_citation:28‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6) [oai_citation:29‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)

Earth Engine also supports moving between raster/vector models using **FeatureCollections** to clip and summarize imagery.  [oai_citation:30‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)

**KFM implication:** remote sensing pipelines should produce:
- derived rasters (e.g., GeoTIFF) and/or extracted tables (Parquet/CSV)
- vector summaries (zonal stats by county/region)
- complete STAC/DCAT + PROV describing filters, reducers, cloud thresholds, and export parameters

### 🕰️ Time-oriented datasets (for UI exploration)

Time-oriented visualization systems often depend on:
- interactive navigation/zoom along time
- selecting/highlighting events
- multiple linked variables/views  [oai_citation:31‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)

Common “timeline” views represent incidents/durations with bars and allow grouping/facets.  [oai_citation:32‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)

**KFM implication:** pipelines that produce time series should also produce:
- clean temporal indexes
- rollups/aggregations that can be fetched quickly by the API/UI
- metadata that clearly encodes temporal extent and resolution

---

## 🛡️ Governance & Sensitive Data

KFM is designed to **fail closed**: if checks/policies fail, the action should be blocked.  [oai_citation:33‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

KFM also embeds **FAIR + CARE** principles as concrete policy-enforced behaviors (not just guidelines).  [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🔒 Restricted data patterns (owner group + access level)

The blueprint describes patterns like:
- `accessLevel: "Restricted"`
- `ownerGroup: "TribeABC"`
…so only authorized users/groups can access, and takedown/withdrawal can be enforced.  [oai_citation:35‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> [!CAUTION]
> Pipelines MUST carry governance metadata forward. If an upstream dataset is Restricted, downstream derived datasets must not “launder” it into Public.

---

## 🧬 Data Spaces & Federation (Future-Facing)

Data Spaces literature emphasizes that “dataspaces” are often a **co-existence** approach (not full integration), enabling incremental refinement with lower up-front costs (“pay-as-you-go”).  [oai_citation:36‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

It also emphasizes pillars like **interoperability, trust, and governance**.  [oai_citation:37‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

**KFM implication:**  
Pipelines should be built so KFM can:
- keep some data *in-place* (federated, via APIs) while still cataloging it
- maintain trustworthy metadata and lineage even when bytes aren’t stored centrally
- adopt “OpenAPI-first” interfaces for data services where appropriate  [oai_citation:38‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

---

## 🧾 Pipeline Documentation Standard (Required for Human Review)

Beyond code, each pipeline should document:
- stages (extract/transform/load), dependencies, constraints
- ETL diagrams / pipeline flow for reviewers
- workflow management assumptions (if any)  [oai_citation:39‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## ✅ Contribution Checklist

Before opening a PR for a new/updated pipeline, verify:

- [ ] **Raw inputs** are added under `data/raw/` and are not modified by the pipeline.  [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Running the pipeline is **non-interactive** and deterministic.  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Outputs are written under `data/processed/` in appropriate formats.  [oai_citation:42‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] `data/catalog/` has **STAC/DCAT** describing the dataset.  [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] `data/provenance/` has **PROV** describing the run, inputs, outputs, and script version.  [oai_citation:44‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Governance metadata (license/access level/owner group) is present and correct.  [oai_citation:45‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Optional but encouraged: schema/range checks + summary stats logged.  [oai_citation:46‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📚 References

Project sources used to shape this README (clickable in this workspace):

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint  [oai_citation:47‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- Scientific Method Master Coder Protocol V12  [oai_citation:48‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals & Applications)  [oai_citation:49‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)  
- Visualization of Time-Oriented Data  [oai_citation:50‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)  
- Database Performance at Scale  [oai_citation:51‡Database Performance at Scale.pdf](sediment://file_000000002cf871f5905f30dcc65cc90b)  
- Data Spaces: Design, Deployment, and Future Directions  [oai_citation:52‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)  
- Scalable Data Management for Future Hardware  [oai_citation:53‡Scalable Data Management for Future Hardware.pdf](sediment://file_000000007d74722fa87beabc663630f7)  