<div align="center">

# ⚙️ Kansas Frontier Matrix — Core Utilities  
`src/utils/README.md`

**Shared Tools · Helpers · Configuration · Reproducibility**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Code](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/utils/`** package contains **shared, project-wide helper functions and system utilities**  
for the **Kansas Frontier Matrix (KFM)** platform.  

These modules support **ETL pipelines**, **AI/ML components**, and **API services**, enabling reproducibility,  
traceability, and maintainability across all stages of the system.

Utilities in this directory are designed to be lightweight, dependency-minimal, and consistent with  
the project’s **Master Coder Protocol (MCP)** principles — documentation-first, auditable, and modular.

---

## 🏗️ Role in the System

```mermaid
flowchart TD
    A["Pipelines<br/>ETL + Enrichment + Load"] --> B["src/utils<br/>helpers, logging, config"]
    B --> C["Graph Layer<br/>Neo4j / RDF"]
    B --> D["API Layer<br/>FastAPI / GraphQL"]
    B --> E["Frontend<br/>MapLibre + Timeline"]
````

<!-- END OF MERMAID -->

Utilities provide **common logic** reused by all components:

* Environment configuration
* File I/O and checksum verification
* Logging and provenance
* Data validation and schema helpers
* Time utilities (ISO, temporal parsing)
* JSON and geospatial helpers

---

## 📂 Directory Layout

```
src/utils/
├── __init__.py
├── config.py         # Global configuration management (YAML, .env)
├── fileio.py         # Safe file read/write utilities
├── checksum.py       # SHA-256 hashing and verification
├── json_tools.py     # JSON read/write, schema validation helpers
├── geo_utils.py      # Simple geospatial math (bbox, distance, reprojection)
├── time_utils.py     # ISO 8601 and temporal parsing helpers
├── logger.py         # Unified logger used across all modules
├── validators.py     # Lightweight schema & data validation tools
└── README.md         # (this file)
```

---

## ⚙️ Configuration (`config.py`)

Centralizes configuration loading and environment management.

```python
# config.py
import os, yaml
from dotenv import load_dotenv

load_dotenv()

def get_config(file="config.yml"):
    """Load configuration YAML file if present, else fallback to environment vars."""
    if os.path.exists(file):
        with open(file) as f:
            return yaml.safe_load(f)
    return {k: v for k, v in os.environ.items() if k.startswith("KFM_")}
```

Example usage:

```python
from src.utils.config import get_config
cfg = get_config()
print(cfg.get("KFM_NEO4J_URI", "bolt://localhost:7687"))
```

---

## 🔒 Checksums (`checksum.py`)

Provides **integrity verification** for reproducibility and provenance tracking.

```python
# checksum.py
import hashlib, json, pathlib

def sha256sum(file_path: str) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def verify(file_path: str) -> bool:
    chk_file = file_path + ".sha256"
    if not pathlib.Path(chk_file).exists():
        return False
    stored = open(chk_file).read().strip()
    return stored == sha256sum(file_path)
```

---

## 🧮 JSON Tools (`json_tools.py`)

Simplifies JSON I/O and schema validation.

```python
import json, jsonschema

def read_json(path):
    with open(path) as f:
        return json.load(f)

def write_json(obj, path, indent=2):
    with open(path, "w") as f:
        json.dump(obj, f, indent=indent)

def validate_json(data, schema_path):
    schema = read_json(schema_path)
    jsonschema.validate(instance=data, schema=schema)
```

---

## 🌍 Geospatial Utilities (`geo_utils.py`)

Provides lightweight spatial operations without requiring heavy GIS dependencies.

```python
import math

def haversine(lat1, lon1, lat2, lon2):
    """Return distance in kilometers between two lat/lon points."""
    R = 6371
    dlat, dlon = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))

def bbox_union(b1, b2):
    """Combine two bounding boxes."""
    return [
        min(b1[0], b2[0]),
        min(b1[1], b2[1]),
        max(b1[2], b2[2]),
        max(b1[3], b2[3]),
    ]
```

---

## ⏱️ Temporal Utilities (`time_utils.py`)

Converts irregular or vague date strings into standard ISO 8601 and temporal intervals.

```python
from datetime import datetime

def parse_date(date_str: str) -> str:
    try:
        return datetime.fromisoformat(date_str).date().isoformat()
    except ValueError:
        return None

def now_iso() -> str:
    return datetime.utcnow().isoformat() + "Z"
```

---

## 🧾 Logger (`logger.py`)

Unified logging system used by pipelines, API, and graph loader.

```python
import logging, sys
from datetime import datetime

logger = logging.getLogger("kfm")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def log(msg, level="info"):
    getattr(logger, level)(msg)
```

Example:

```
[2025-10-05 15:44:02] [INFO] Fetch complete for usgs_ingest (3.2 GB)
```

---

## 🧩 Validators (`validators.py`)

Lightweight schema and type validation helpers.

```python
def ensure_fields(data: dict, required: list):
    missing = [k for k in required if k not in data]
    if missing:
        raise KeyError(f"Missing required fields: {', '.join(missing)}")

def is_valid_coordinate(lat, lon) -> bool:
    return -90 <= lat <= 90 and -180 <= lon <= 180
```

---

## 🧰 Example Usage Across Pipelines

```python
from src.utils import checksum, time_utils, logger

f = "data/processed/ks_1m_dem.tif"
print("Checksum:", checksum.sha256sum(f))
logger.log(f"Validated {f} at {time_utils.now_iso()}")
```

Logs:

```
[2025-10-05 16:05:43] [INFO] Validated data/processed/ks_1m_dem.tif at 2025-10-05T16:05:43Z
```

---

## 🧾 Integration Flow

| Layer             | Utility Usage                                | Example                                      |
| :---------------- | :------------------------------------------- | :------------------------------------------- |
| **ETL Pipelines** | `config`, `checksum`, `logger`, `time_utils` | Validation, timestamps, reproducible builds  |
| **Graph Loader**  | `json_tools`, `validators`, `logger`         | Node/relationship validation                 |
| **API Layer**     | `config`, `geo_utils`, `logger`              | Query parameter validation, response logging |
| **CI/CD**         | `checksum`, `json_tools`                     | Artifact integrity and validation checks     |

---

## 🧪 Testing

Each utility module has dedicated unit tests in `tests/utils/`:

```bash
pytest tests/utils/ --maxfail=1 --disable-warnings -q
```

All changes must pass type-checking (`mypy`) and static linting (`ruff`, `black`).

---

## 📚 References

* [Kansas Frontier Matrix — Architecture Overview](../../docs/architecture.md)
* [Scientific Method & Master Coder Protocol Templates](../../docs/templates/experiment.md)
* [SpatioTemporal Asset Catalog (STAC) Spec 1.0.0](https://stacspec.org/)
* [CIDOC CRM Ontology](https://cidoc-crm.org/)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Efficient Utilities · Transparent Workflows · Provenance by Design*

</div>

