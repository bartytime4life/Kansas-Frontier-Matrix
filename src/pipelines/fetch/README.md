<div align="center">

# 🌐 Kansas Frontier Matrix — Data Fetch Pipelines  
`src/pipelines/fetch/README.md`

**Automated Data Acquisition · Provenance · Reproducibility**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Code](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 🎯 Purpose

This directory contains all **data acquisition and source ingestion scripts** for the **Kansas Frontier Matrix (KFM)** project.  
Fetch pipelines automate retrieval of raw datasets from verified external sources — ensuring transparent provenance,  
repeatability, and traceable links between **data/sources/** manifests and the files produced in **data/raw/**.

Each fetch module is responsible for a specific data provider or domain:
- 🌧 **NOAA** → climate and storm records  
- 🏞 **USGS** → topographic maps, DEM, hydrology, geology  
- 🌀 **FEMA** → disaster declarations and hazard maps  
- 🗺 **Kansas GIS / DASC** → vector and raster state datasets  
- 📰 **Kansas Memory & Newspapers** → archives, OCR, documents  
- ⚙️ **Custom sources** → one-off fetch scripts or experimental APIs  

All fetch scripts follow **MCP (Master Coder Protocol)** standards for:
- provenance logging (`sha256`, timestamps, URLs)  
- open data compliance (license tags)  
- reproducibility (configurable parameters, Makefile integration)  

---

## 🏗 Architecture Overview

```mermaid
flowchart TD
    A["data/sources/*.json<br/>(source manifests)"] --> B["fetch/*.py<br/>fetch scripts (USGS, NOAA, FEMA, etc.)"]
    B --> C["data/raw/<source>/...<br/>downloaded files"]
    B --> D["logs/pipelines/fetch.log<br/>provenance logs + checksums"]
    C --> E["Makefile: make fetch<br/>runs all enabled sources"]
````

<!-- END OF MERMAID -->

---

## 📂 Directory Layout

```
src/pipelines/fetch/
├── __init__.py
├── noaa_ingest.py          # NOAA weather, storm events, climate normals
├── usgs_ingest.py          # USGS DEM, topographic maps, hydrology
├── fema_ingest.py          # FEMA disaster declarations
├── kansas_archive_ingest.py# Kansas GIS archive layers via ArcGIS REST
├── kansas_memory_ingest.py # Kansas Historical Society & Kansas Memory items
├── newspapers_ingest.py    # Chronicling America / local OCR texts
├── blm_ingest.py           # Land patents and deeds (BLM GLO Records)
├── generic_fetch.py        # Common HTTP / API download utilities
└── README.md               # (this file)
```

Each module exports a function like:

```python
def fetch(config: dict) -> None:
    """Fetch data from the target source defined in its JSON manifest."""
```

---

## ⚙️ Configuration and Usage

Each fetch script references a corresponding manifest file under `data/sources/`.
These manifests define where, when, and how to pull the data.

Example: `data/sources/noaa_storms.json`

```json
{
  "id": "noaa_storms",
  "title": "NOAA Storm Events Database (Kansas)",
  "endpoint": "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/",
  "license": "Public Domain (US NOAA)",
  "temporal": {"start": "1950-01-01", "end": "2025-01-01"},
  "destination": "data/raw/noaa/storm_events/",
  "fetch": {
    "type": "http",
    "pattern": "StormEvents_details-*.csv.gz"
  }
}
```

### 🧮 Run Commands

Use the project `Makefile` or Python CLI:

```bash
# Run all fetch tasks
make fetch

# Or call an individual source
python src/pipelines/fetch/noaa_ingest.py --year 2020

# Example: Fetch and log Kansas DEM tiles
python src/pipelines/fetch/usgs_ingest.py --bbox -102,36,-94,40 --resolution 1m
```

Each fetch creates:

* a data file (or directory) under `data/raw/<source>/`
* a `.sha256` checksum file
* a structured log entry in `logs/pipelines/fetch.log`

---

## 🧩 Script Template (for New Sources)

When adding a new source, follow this template:

```python
#!/usr/bin/env python3
"""
@MCP-LOG Kansas Frontier Matrix – Data Fetch Script Template
Purpose: Retrieve and log external datasets for reproducibility.
"""

import os, json, hashlib, requests
from datetime import datetime

def fetch(config_path: str):
    cfg = json.load(open(config_path))
    url = cfg["endpoint"]
    dest = cfg["destination"]
    os.makedirs(dest, exist_ok=True)
    fn = os.path.join(dest, os.path.basename(url))
    
    r = requests.get(url, stream=True)
    with open(fn, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    
    checksum = hashlib.sha256(open(fn, "rb").read()).hexdigest()
    with open(fn + ".sha256", "w") as h:
        h.write(checksum)
    print(f"[{datetime.now()}] ✅ Fetched {fn} ({checksum[:12]}...)")

if __name__ == "__main__":
    fetch("data/sources/new_source.json")
```

---

## 🧠 Data Provenance & Validation

Every fetched dataset must include:

* **Checksum** → `.sha256` file (auto-created by the fetch script)
* **Source manifest** → JSON metadata in `data/sources/`
* **License tag** → clearly specify usage rights in manifest
* **Validation** → run schema check:

```bash
make validate-sources
```

This runs STAC/JSON Schema validation on all source manifests and ensures metadata integrity.

---

## 🔒 Logging & Error Handling

All fetch scripts log to `logs/pipelines/fetch.log` with the following schema:

```
[2025-10-05 13:44:22] NOAA | storm_events_2024.csv | 41.2MB | SHA256=ab19df... | OK
[2025-10-05 13:47:10] USGS | ks_dem_1m_tile.tif     | 850MB  | SHA256=cd892f... | OK
[2025-10-05 13:55:12] KHS  | kansas_memory_001.pdf  | 4.2MB  | SHA256=91efac... | RETRY(1)
```

Errors (network timeouts, 404s, bad checksums) are retried automatically up to 3 times and logged with `FAIL`.

---

## 🧾 Adding a New Fetch Module

1. Create a JSON manifest in `data/sources/` with metadata and URLs.
2. Create a Python fetch script in `src/pipelines/fetch/`.
3. Register it in the Makefile under `FETCH_TARGETS`.
4. Add tests in `tests/pipelines/test_fetch_<source>.py`.
5. Run `make fetch && make validate`.
6. Commit with message:

   ```
   feat(fetch): add <source> ingestion pipeline
   ```

---

## 📚 References

* [Kansas Frontier Matrix – File & Data Architecture Guide](../../../docs/architecture.md)
* [AI/ML Developer Documentation](../../../docs/ai-system.md)
* [Scientific Method & MCP Templates](../../../docs/templates/experiment.md)
* [Integrating Historical, Cartographic, and Geological Research (MCP Reference)](../../../docs/integration/README.md)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Open Source · Open Data · Reproducible Science*

</div>
