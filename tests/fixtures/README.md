<div align="center">

# 🧱 Kansas Frontier Matrix — Test Fixtures (`/tests/fixtures/`)

**Mission:** Provide **deterministic, minimal, and transparent data samples**  
for validating every subsystem in the Kansas Frontier Matrix (KFM) stack —  
from ETL pipelines and STAC validation to AI/NLP and Web UI integration.

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)

</div>

---

## 🧩 Fixture Lifecycle Overview

```mermaid
flowchart TD
    A([Fixture Created<br/>geo · text · stac · config]) --> B([Used in Unit / Integration Tests])
    B --> C([Schema Validation<br/>STAC · JSON Schema])
    C --> D([CI Execution<br/>GitHub Actions])
    D --> E([Coverage Reports<br/>Codecov / Logs])
    E --> F([Validated Build<br/>Deploys Docs & Web UI])

    %% Styles (GitHub-safe)
    classDef src fill:#d7ebff,stroke:#0078d4,color:#111;
    classDef test fill:#eafaf1,stroke:#1a7f37,color:#111;
    classDef ci fill:#fff8e1,stroke:#ffb300,color:#111;
    classDef done fill:#d1ffd7,stroke:#1a7f37,color:#111;

    class A src;
    class B,C test;
    class D ci;
    class E,F done;
````

*Fixtures begin as synthetic data → fuel tests → verified in CI → feed reproducible deployments.*

---

## 📚 Structure

```text
tests/fixtures/
├── geo/                     # GeoJSON / raster samples
│   ├── ks_county_sample.geojson
│   ├── tiny_vector.geojson
│   └── dem_sample.tif
├── text/                    # OCR / diary / treaty snippets
│   ├── sample_diary.txt
│   └── treaty_excerpt.txt
├── stac/                    # STAC + schema examples
│   ├── stac_item_min.json
│   └── stac_collection_min.json
├── sources/                 # data/sources/ manifests for fetch tests
│   └── usgs_topo_sample.json
├── configs/                 # UI config fixtures
│   ├── layers_min.json
│   └── app_config_min.json
└── __init__.py              # allows `import fixtures` in Pytest
```

---

## 🧩 Fixture Categories

| Category    | Used By                                          | Purpose                                         |
| ----------- | ------------------------------------------------ | ----------------------------------------------- |
| **Geo**     | `convert_gis`, `validate_stac`, UI map rendering | Validate GeoJSON & COG conversions, projections |
| **Text**    | NLP pipeline                                     | Test NER extraction of names, places, dates     |
| **STAC**    | `validate_stac.py`, schema tests                 | Confirm STAC JSON compliance                    |
| **Sources** | `fetch_data.py`                                  | Mock remote downloads / manifests               |
| **Configs** | `build_config.py`, Web UI                        | Verify config generation, layer mapping         |

---

## 🧪 Guidelines

* Keep fixtures **small** (≤ 50 KB each).
* Ensure **valid schema** (GeoJSON, STAC 1.0, JSON Schema).
* Prefer **Kansas-specific** examples (“Larned”, “Ellsworth”, “Arkansas River”).
* Encode **UTF-8**, newline =`\n`.
* Include CRS info (`EPSG:4326`) for all spatial data.
* Use **deterministic random seeds** if generated.
* Raster fixtures → ≤ 10 × 10 pixels, single band.
* Document provenance (source/generator) below or inline comments.

---

## ⚙️ Usage

### 🐍 Python

```python
from pathlib import Path
import json
import pytest

@pytest.fixture
def stac_item(fixtures_dir):
    return json.loads((fixtures_dir / "stac/stac_item_min.json").read_text())
```

`conftest.py` typically defines:

```python
import pytest
from pathlib import Path

@pytest.fixture(scope="session")
def fixtures_dir() -> Path:
    return Path(__file__).parent
```

### 💻 JavaScript

```javascript
import fs from "fs";
const geo = JSON.parse(fs.readFileSync("tests/fixtures/geo/ks_county_sample.geojson", "utf8"));
test("GeoJSON loads", () => expect(geo.type).toBe("FeatureCollection"));
```

---

## 🧱 Example Fixture — `stac_item_min.json`

```json
{
  "type": "Feature",
  "id": "usgs_topo_larned_1894",
  "properties": {
    "datetime": "1894-01-01T00:00:00Z",
    "proj:epsg": 4326
  },
  "assets": {
    "cog": {
      "href": "data/cogs/usgs_topo_larned_1894.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  },
  "bbox": [-99.4, 38.1, -99.0, 38.4]
}
```

> Minimal STAC Item: schema-valid and suitable for both STAC and GeoJSON validation tests.

---

## 🔄 Maintenance & Provenance

* Regenerate fixtures **only** through approved scripts or notebooks.
* Keep regeneration notebooks under `tools/notebooks/` and cross-link here.
* Update STAC fixtures when spec versions change.
* No private or large data — use mock or public-domain examples.
* Commit each change with a provenance note in PR description.

---

<div align="center">

🧩 *Small data → big confidence.*
Fixtures are the **lab samples** that keep Kansas Frontier Matrix reproducible and auditable.

</div>
