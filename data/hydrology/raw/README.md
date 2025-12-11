---
title: "💧 Kansas Frontier Matrix — Hydrology Raw Data Directory (v11.2.6)"
path: "data/hydrology/raw/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Hydrology & Hazards Council"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-data-hydrology-raw-index"
doc_uuid: "urn:kfm:data:hydrology:raw:index:v11.0.0"
event_source_id: "ledger:data/hydrology/raw/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-hydrology-raw-index-v1.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active · Enforced"
doc_kind: "Dataset Directory Guide"
intent: "hydrology-raw-data-directory"
role: "raw-ingest-registry"
category: "Data · Hydrology · Raw"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity_level: "Mixed"
public_exposure_risk: "Dataset-level"
indigenous_rights_flag: "Dataset-level"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Varies by dataset"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next hydrology-raw-directory update"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology Raw Data Directory (v11.2.6)**  
`data/hydrology/raw/README.md`

**Purpose**  
Define the **authoritative layout, governance, and ETL contracts** for the  
**hydrology raw data layer**, the first step in the pipeline:

Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

</div>

---

## 📘 1. Overview

This document governs **all raw hydrology data** stored under:

- `data/hydrology/raw/**`

Scope:

- **Included**
  - As-received files from agencies, instruments, surveys, models, and archives  
  - Landing copies from APIs (USGS, USACE, KDHE, Mesonet, NOAA, etc.)  
  - Original WID experiment exports (sensors, ADCP, ops logs)  
  - Raw bathymetry, sediment core records, and water-quality lab reports  

- **Excluded**
  - Harmonized / cleaned / gap-filled timeseries → `data/hydrology/processed/**`
  - STAC / DCAT / PROV JSON → `data/hydrology/stac/**` and `data/stac/**`
  - Graph and Story Node content → Neo4j / `src/graph/**` / Focus Mode

**Key principles**

- **Immutability**: once written and verified, files in `raw/` are **append-only** (no in-place edits).  
- **Traceability**: every file is traceable to a **source manifest** and **ETL activity**.  
- **FAIR+CARE**: raw data is governed by FAIR+CARE and Indigenous sovereignty policies;  
  sensitive content may be generalized or access-restricted at higher layers.

---

## 🗂️ 2. Directory Layout (Hydrology Raw · Emoji Style A)

~~~text
📁 data/hydrology/raw/
├── 📄 README.md                      # This file (governance & layout)
│
├── 💧 inflows/                       # As-received inflow / upstream gage data
│   ├── 📂 usgs-nwis/                 # NWIS exports (JSON/CSV/RDB)
│   └── 📂 other-providers/           # KGS, local agencies, project CSVs
│
├── 💧 outflows/                      # As-received dam releases, diversions
│   ├── 📂 usace/                     # USACE reservoir/dam outlets
│   └── 📂 local-ops/                 # Local operations logs & CSVs
│
├── 🗺️ bathymetry/                    # Survey deliveries (raw soundings & grids)
│   ├── 📂 multibeam/                 # Vendor survey drops, unedited
│   ├── 📂 singlebeam/                # Legacy single-beam tracks
│   └── 📂 documentation/             # Field notes, PDFs, CAD/DWG, etc.
│
├── 🧪 sediment-cores/                # Cores, lab sheets, logs, imagery
│   ├── 📂 core-logs/                 # Stratigraphy logs, spreadsheets
│   ├── 📂 lab-results/               # Grain size, density, chemistry exports
│   └── 📂 photos/                    # Core box and section photos
│
├── 🧪 water-quality/                 # Raw water-quality datasets
│   ├── 📂 kdhe/                      # KDHE station downloads
│   ├── 📂 usgs/                      # USGS water-quality exports
│   └── 📂 other-providers/           # Universities, consultants, etc.
│
├── 🚜 wid-2025/                      # Water Injection Dredging raw data
│   ├── 📂 sensors/                   # Turbidity / DO / ADCP raw files
│   ├── 📂 ops-logs/                  # Jet operations logs, notes
│   └── 📂 docs/                      # Protocols, vendor docs, emails
│
├── 🌦️ climate/                       # Climate & hydroclimate drivers (raw)
│   ├── 📂 mesonet/                   # Kansas Mesonet exports
│   ├── 📂 prism/                     # PRISM rasters / tables as delivered
│   └── 📂 noaa/                      # NOAA/NCEI station & grid products
│
└── 🌊 downstream/                    # Downstream sensors & ecological co-data
    ├── 📂 turbidity/                 # Below-dam turbidity sensors (raw)
    ├── 📂 do/                        # Dissolved oxygen raw series
    └── 📂 ecology/                   # Mussels, fish, macroinvertebrate raw files
~~~

> The tree above is **normative** for v11.2.6. New subdirectories MUST follow  
> this emoji + kebab-case style, with a **local README.md** when semantics are non-obvious.

---

## 💾 3. Raw Data Governance & Immutability

Hydrology raw data is the **system of record** for upstream ingest. Rules:

- **Write path**
  - Only **deterministic ETL jobs** and controlled bulk imports may write to `raw/`.
  - Direct manual edits (Excel-in-place, hand renames) are **not allowed**.
- **Immutability**
  - Existing files are never modified or deleted to “fix” values.
  - Corrections are handled by:
    - adding new versions (e.g., `_v02`), and  
    - marking supersession in STAC / PROV / graph metadata.
- **Provenance**
  - Every ingest produces:
    - a **source manifest** under `data/sources/hydrology/`, and  
    - a **PROV activity record** linking source → raw files → processed outputs.
- **Access**
  - Raw hydrology data may contain:
    - dataset-specific licenses and restrictions, and  
    - locations of culturally or ecologically sensitive sites.
  - Downstream views (processed, graph, Story Nodes) may be generalized or redacted  
    even when raw files retain original precision.

---

## 🧾 4. File Naming & Landing Conventions

To keep raw hydrology files **searchable and machine-parseable**, filenames should follow:

### 4.1 Canonical pattern

~~~text
<domain>_<provider>_<site-or-area>_<parameter-or-theme>_<start>-<end>_v<version>.<ext>
~~~

Examples (illustrative):

- `hydro_usgs_06887000_flow_1950-2025_v01.csv`  
- `hydro_kdhe_tuttle-wq_do-turbidity_2010-2019_v01.xlsx`  
- `hydro_usace_tuttle-bathy_multibeam_2025-03_campaignA_v01.zip`

**Rules**

- `domain` → `hydro` for hydrology domain raw data.  
- `provider` → stable slug, e.g. `usgs`, `usace`, `kdhe`, `mesonet`, `noaa`.  
- `site-or-area` → canonicalized site ID, reservoir, reach, or polygon name.  
- `parameter-or-theme` → short slug: `flow`, `stage`, `turbidity`, `do`, `bathy`, `cores`, `climate`.  
- `start` / `end` → `YYYY` or `YYYYMMDD` as appropriate.  
- `v<version>` → integer starting at `v01`, incrementing for each new delivery or correction.  

Within archives (`.zip` / `.tar.gz`), internal paths should be **sensible** and avoid  
collisions across datasets, e.g. include `provider` + `site` in nested directories.

---

## 🔗 5. Source Manifests, STAC/DCAT/PROV Linkage

For each logical raw dataset (not every file), hydrology ingestion MUST create:

1. **Source manifest**  
   - Location: `data/sources/hydrology/<dataset-id>.source.json`  
   - Captures:
     - `dataset-id`, `title`, `description`  
     - `source_uri`, `provider`, `license`, `terms_of_use`  
     - `temporal_coverage`, `spatial_coverage`  
     - `file_list` (or glob) pointing into `data/hydrology/raw/**`  
     - CARE + sovereignty flags and notes

2. **STAC / DCAT metadata**
   - STAC Collections and Items under `data/hydrology/stac/**` and/or `data/stac/**`  
     referencing the raw files (or representing them as input assets).
   - DCAT entries at the catalog layer so hydrology datasets are discoverable  
     alongside other KFM data domains.

3. **PROV-O provenance**
   - Entities: raw files, source manifest, STAC Item(s)  
   - Activities: ETL ingest runs, manual curation steps (if any)  
   - Agents: agencies, vendors, KFM ETL services, hydrology stewards

Downstream processed datasets **must** reference their raw inputs via `prov:wasDerivedFrom`.

---

## 🌊 6. Hydrology Raw Data Classes (Per Subdirectory)

| Subdir              | Typical sources                | Typical formats                 | Notes |
|---------------------|--------------------------------|---------------------------------|-------|
| `inflows/`          | USGS NWIS, KGS, local gauges  | CSV, RDB, JSON, XML, TXT       | Streamflow, stage, upstream controls. |
| `outflows/`         | USACE, local ops teams        | CSV, XLSX, PDF logs            | Dam releases, gate logs, diversion records. |
| `bathymetry/`       | Survey vendors, USACE, KGS    | RAW sonar, LAS/LAZ, XYZ, CAD   | Unprocessed soundings, grids, and documentation. |
| `sediment-cores/`   | Labs, universities, agencies  | CSV, XLSX, PDF, JPEG/PNG       | Logs, lab sheets, images; may require careful sensitivity review. |
| `water-quality/`    | KDHE, USGS, others            | CSV, XLSX, RDB, JSON           | Discrete samples (turbidity, nutrients, DO, etc.). |
| `wid-2025/`         | WID project instruments       | CSV, proprietary logger files   | High-frequency sensors, ops notes, experimental configs. |
| `climate/`          | Mesonet, PRISM, NOAA/NCEI     | CSV, NetCDF, GeoTIFF, GRIB     | Raw station and gridded climate/hydroclimate inputs. |
| `downstream/`       | Project sensors, agencies     | CSV, RDB, JSON, photos, shapefiles | Downstream turbidity/DO, ecology surveys, transects. |

Each subdirectory SHOULD have a **local `README.md`** if:

- The schema differs from other datasets in the same class, or  
- Special cleaning, sovereignty constraints, or QA practices apply.

---

## 🛠️ 7. ETL Integration (Deterministic Raw Ingest)

The hydrology raw layer is the output of **deterministic ETL** jobs. At minimum:

1. **Config**
   - ETL configs live under a domain-specific config path (e.g. `configs/hydrology/`),  
     declaring:
     - source endpoints / download URLs  
     - expected schemas  
     - output `raw/` target subdirectories  
     - random seeds (if used) and schedule.

2. **Execution**
   - ETL jobs are implemented under `src/pipelines/hydrology/` (or equivalent), and:
     - fetch source data  
     - validate checksums where available  
     - write files into `data/hydrology/raw/**` using the naming pattern above  
     - emit PROV and log telemetry.

3. **Logging & experiments**
   - ETL runs are logged under `mcp/experiments/hydrology/` with:
     - execution timestamps  
     - git commit SHA, config file version  
     - summary stats (rows, sites, temporal range, failures).

4. **Handoff to processed layer**
   - Separate normalization pipelines read from `raw/` and write to:
     - `data/hydrology/processed/**` (contract-validated outputs), and  
     - `data/hydrology/stac/**` (STAC Items referencing the processed assets and raw lineage).

---

## 🧬 8. FAIR+CARE, Sovereignty, and Sensitivity

Although this directory is tagged as **“Public · Low-Risk”** at the doc level, individual datasets may be:

- **Public, low risk** (e.g., public hydrometric timeseries).  
- **License-restricted** (vendor proprietary bathymetry, lab results).  
- **Sensitive** (ecological locations, culturally significant sites).

Hydrology stewards MUST:

- Respect CARE principles and `INDIGENOUS-DATA-PROTECTION.md`.  
- Avoid placing raw files here that:
  - directly expose restricted sacred sites, or  
  - violate agreements with Tribes, agencies, or data providers.
- Where necessary:
  - store detailed data in a more restricted path, and  
  - surface only generalized / aggregated views to the graph, API, and Focus Mode.

Any dataset requiring special handling SHOULD be flagged in its source manifest  
and, where appropriate, in STAC / DCAT / graph metadata.

---

## 🎯 9. Focus Mode & Story Node Linkages

Hydrology raw data is **not** rendered directly in Focus Mode, but it underpins:

- **Story Nodes** for floods, droughts, WID operations, reservoir transitions.  
- **Focus Mode narratives** that:
  - reference processed datasets and graph nodes, and  
  - expose provenance chips that trace back to raw hydrology sources.

Requirements:

- Raw dataset IDs must be **stable and graph-addressable** so:
  - Story Nodes can reference them as `wasDerivedFrom` sources, and  
  - Focus Mode can show “Data behind this story” panels that ultimately trace back  
    to `data/hydrology/raw/**` via STAC/DCAT/PROV and Neo4j.

---

## 🕰 10. Version History

| Version  | Date       | Author / Steward            | Notes                                                                 |
|---------:|-----------:|-----------------------------|-----------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Hydrology & Hazards Council | Initial hydrology raw directory guide aligned to KFM-MDP v11.2.6 and hydrology domain index. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[⬅️ Back to Hydrology Domain Index](../README.md) ·  
[🗃️ Data Sources Registry](../../../data/sources/) ·  
[🛡️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

