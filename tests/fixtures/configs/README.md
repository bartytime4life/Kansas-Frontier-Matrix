<div align="center">

# ⚙️ Kansas Frontier Matrix — **Config Fixtures**  
`tests/fixtures/configs/`

**Web Configuration · Layer Definitions · App Settings**

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../../.github/workflows/tests.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Config Fixtures (tests/fixtures/configs/)"
version: "v1.0.0"
last_updated: "2025-10-14"
owners: ["@kfm-web", "@kfm-engineering"]
tags: ["config","layers","app-settings","fixtures","frontend","mcp"]
license: "MIT"
semantic_alignment:
  - JSON Schema Validation
  - STAC Integration
  - MCP-DL v6.2 (Configuration Provenance)
---
````

---

## 🧭 Overview

The `tests/fixtures/configs/` directory provides **mock configuration files** for validating KFM’s
frontend build system and UI layer mappings.

These fixtures mimic the structure of `web/config/*.json` —
specifically **`layers.json`** and **`app.config.json`** — ensuring
tools like `build_config.py` and the React frontend properly interpret and load configuration data.

> **Purpose:** To test that every KFM deployment can reconstruct its configuration files deterministically from STAC metadata and MCP-aligned manifests.

---

## 🧱 Directory Structure

```text
tests/fixtures/configs/
├── layers_min.json          # Minimal test version of layers.json
├── app_config_min.json      # Minimal test version of app.config.json
└── README.md                # This documentation file
```

---

## 🧩 Fixture Overview

| File                  | Purpose                                               | Consumed By                                           | Schema                   |
| :-------------------- | :---------------------------------------------------- | :---------------------------------------------------- | :----------------------- |
| `layers_min.json`     | Defines test layers used by MapView and LayerControls | `build_config.py`, `web/src/components/LayerControls` | STAC-derived JSON Schema |
| `app_config_min.json` | Global app metadata, API base, flags, map defaults    | `web/config/app.config.json`, `Header`, `AppShell`    | App Configuration Schema |

---

## 🧩 Example Fixture — `layers_min.json`

```json
[
  {
    "id": "historic_topo_1894",
    "title": "USGS Topographic Map (1894)",
    "type": "raster",
    "url": "https://example.org/maps/topo_1894.tif",
    "opacity": 0.8,
    "visible": true,
    "timeRange": { "start": "1894-01-01", "end": "1894-12-31" },
    "legend": "maps/legend_topo_1894.png",
    "license": "Public Domain"
  },
  {
    "id": "kansas_treaties",
    "title": "Kansas Treaty Boundaries",
    "type": "vector",
    "url": "https://example.org/layers/treaties.geojson",
    "opacity": 1,
    "visible": false,
    "legend": "maps/legend_treaty.png",
    "license": "CC-BY 4.0"
  }
]
```

> A schema-valid sample representing two dataset layers linked to STAC metadata.
> Used to validate frontend rendering and backend configuration rebuild workflows.

---

## 🧩 Example Fixture — `app_config_min.json`

```json
{
  "appName": "Kansas Frontier Matrix (Test)",
  "version": "1.0.0-test",
  "apiBaseUrl": "https://api.frontiermatrix.test",
  "defaultMapCenter": [-98.3, 38.5],
  "defaultZoom": 6,
  "enableAI": true,
  "enableAccessibilityFeatures": true,
  "supportedLanguages": ["en"],
  "contactEmail": "test@frontiermatrix.org"
}
```

> A compact mock of the global configuration file, used to test `build_config.py`
> and React Context initialization in `ThemeContext` and `AccessibilityContext`.

---

## 🧪 Usage in Tests

### 🐍 Example — `test_build_config.py`

```python
import json
from tools.build_config import validate_layers

def test_layer_config_schema(fixtures_dir):
    layers = json.loads((fixtures_dir / "configs/layers_min.json").read_text())
    for layer in layers:
        assert "id" in layer and "url" in layer
        assert layer["type"] in ("raster", "vector")
```

### 💻 Example — Frontend Validation (CI)

```bash
npm run validate-config
# Uses app_config_min.json & layers_min.json fixtures
```

---

## 🧮 Schema Validation Workflow

| Step | Tool         | Description                                                     |
| :--- | :----------- | :-------------------------------------------------------------- |
| 1️⃣  | `jsonschema` | Validate keys and field types against schema definitions        |
| 2️⃣  | `pystac`     | Cross-reference STAC metadata for URL and ID alignment          |
| 3️⃣  | `pytest`     | Ensure all config fixtures are loadable and syntactically valid |
| 4️⃣  | `vite`       | Web build simulation using fixtures as injected runtime config  |

---

## ♿ Accessibility & Design Integration

* All fields use human-readable labels for design system traceability.
* `themes.json` tokens used indirectly in tests via simulated color scheme toggles.
* Configs validated against **WCAG 2.1 AA** for theme and accessibility flag consistency.
* `enableAccessibilityFeatures: true` ensures UI respects reduced-motion, high-contrast mode.

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                           |
| :--------------- | :---------------------------------------------------- |
| **Inputs**       | STAC-derived metadata, example endpoints              |
| **Outputs**      | Schema-validated config JSONs                         |
| **Dependencies** | Python (pytest, jsonschema), Node.js (vite)           |
| **Integrity**    | SHA256 checksums recorded per fixture                 |
| **Traceability** | Cross-linked to STAC ID and versioned via Git commits |

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                    |
| :------------------ | :------------------------------------------------ |
| Documentation-first | Each configuration fixture fully documented here  |
| Reproducibility     | Deterministic mock configs with fixed values      |
| Provenance          | Cross-referenced STAC sources and schema hashes   |
| Accessibility       | WCAG 2.1 AA theme + accessibility flag testing    |
| Open Standards      | JSON Schema validated configs                     |
| Auditability        | CI enforces syntax + schema integrity on every PR |

---

<div align="center">

⚙️ **Configuration defines the experience.**
These fixtures ensure that Kansas Frontier Matrix builds remain **stable, reproducible, and standards-aligned** — from STAC metadata to web interface.

</div>
```

